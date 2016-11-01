from docplex.mp.context import DOcloudContext
from docplex.mp.model import Model


docloud_context = DOcloudContext()
model           = Model('Final33', docloud_context=docloud_context)



from datetime import datetime
import itertools


start = datetime.now()


#MATRIZ DE DISTANCIA
d_ij = [[1000000000, 625,           1734,        2791,       2040,       2702,       2121,      2510,        3382       ],
        [625,        1000000000,    1273,        2330,       1580,       2242,       1659,      1952,        2922       ],
        [1734,       1273,          1000000000,  1060,       308,        1030,       654,       1422,        1637       ],
        [2791,       2330,          1060,        1000000000, 775,        346,        854,       1512,        566        ],
        [2040,       1580,          308,         775,        1000000000, 898,        656,       1484,        1300       ],
        [2702,       2242,          1030,        346,        898,        1000000000, 699,       1303,        677        ],
        [2121,       1659,          654,         854,        656,        699,        1000000000,853,         1330       ], 
        [2510,       1952,          1422,        1512,       1484,       1303,       853,       1000000000,  1792       ],
        [3382,       2922,          1637,        566,        1300,       677,        1330,      1792,        1000000000 ]]
     

#QUANTIDADE DE CIDADES
num_cidades = len(d_ij)



#VARIAVEL DE DECISAO
x_ij = [[model.binary_var(name='x_ij_%d_%d' %(I,J))
                        for J in range(0, num_cidades)]
                        for I in range(0, num_cidades)]



#OBJETIVO
model.minimize(model.sum([x_ij[I][J] * d_ij[I][J] for I in range(0, num_cidades) 
                                                  for J in range(0, num_cidades)]))    



#A primeira restricao se refere a que cada cidade so pode ter uma aresta SAINDO. 
for I in range(0, num_cidades):
    model.add_constraint(model.sum([x_ij[I][J] for J in range(0,num_cidades)]) == 1)  


#A segunda restricao se refere a que cada cidade soh pode ter uma aresta CHEGANDO.    
for J in range(0, num_cidades):
    model.add_constraint(model.sum([x_ij[I][J] for I in range(0, num_cidades)]) == 1)



#RESTRICAO DE SUBROTA
for subrota in range(3, num_cidades / 2 + 1):
    combinacao =  list(itertools.permutations(range(num_cidades), subrota - 1))
    for item in combinacao: 
        arestas = list(itertools.permutations(item, 2))
        model.add_constraint(model.sum([x_ij[c[0]][c[1]]for c in arestas]) <= (subrota - 2))
    

#RESOLVENDO O MODELO
status = model.solve()
if not status:
    print "O problema nao encontrou solucao viavel"
    

#OBTENDO A SOLUCAO
solucao = [[x_ij[I][J].solution_value 
                    for J in range(0, num_cidades)]
                    for I in range(0, num_cidades)]


#OBTENDO A FUNCAO OBJETIVO
model.print_solution() 

print "\n"
print "Solucao Matriz de caminhos"
print solucao


#IMPRIMINDO A SOLUCAO 
percurso_desorganizado = [[0,0]]*len(solucao)
for contador, saida in enumerate(solucao):
    for c, entrada in enumerate(saida):
        if entrada != 0:
            percurso_desorganizado[contador] = [contador, c]

percurso_final = []
percurso_final.append(percurso_desorganizado[0][0])
percurso_final.append(percurso_desorganizado[0][1])
while len(percurso_final) < len(solucao)+1:
    prox_cidade = percurso_final[-1]
    for trajeto in percurso_desorganizado:
        if trajeto[0] == prox_cidade:
            percurso_final.append(trajeto[1])
print "\n"
print "Trajeto: ", percurso_final
                

tempo = datetime.now() - start
print "Tempo de execucao: %s" %tempo






