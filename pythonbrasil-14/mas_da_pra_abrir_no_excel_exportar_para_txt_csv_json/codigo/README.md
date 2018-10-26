# "Mas dá pra abrir no Excel?", exportando para TXT, CSV e JSON com Python

Slides e códigos para palestra apresentada na PythonBrasil[14] em Natal, RN, Brasil.

### Descrição

Você conseguiu escrever o programa todo para pegar da web as informações que precisa, mas... o que fazer com elas? E quando clientes não tem conhecimento técnico e só quer saberem de ver o relatório na telinha dos programas que usam (sem interagir com terminal)?

Nessa palestra, mostrarei como utilizar ferramentas da biblioteca padrão do Python para salvar em arquivos texto, csv (separados por vírgulas) e JSON as informações geradas pelo seu programa.

Ao final, você não vai saber entregar um arquivo .xlsx com macros e tabelas dinâmicas. Vai saber como montar um arquivo que, sim, vai dar para abrir no Excel (spoiler: e em outros programas também!).

**get_and_export.py**

Script Python que usa Selenium para buscar cidade e data dos eventos Django Girls no site DjangoGirls.org/events e exporta para arquivo texto (TXT), separado por vírgulas (CSV) ou Notação de Objeto JavaScript (JSON).

Para demonstração, ao criar um arquivo TXT também envia para o terminal o processamento, contando as cidades e mostrando cada uma delas com sua data.


## Instalando e rodando

#### Instale pip

- Debian e derivativos:

```
$ sudo apt install python3-pip
```

#### Instale pipenv com um dos seguintes comandos ([mais informações - em inglês](https://docs.pipenv.org/install/#installing-pipenv))

```
$ pip3 install --user pipenv
$ python3 -m pip install --user pipenv
```

#### Crie um novo ambiente com Python 3

```
$ pipenv --three
```

#### Instale as dependências

```
$ pipenv install
```

#### Você vai precisar ter o Geckodriver instalado e disponível no PATH para utilizar o Selenium:

- Baixe o geckodriver:
[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

- Extraia, mova para o diretório bin e coloque no PATH:
```
$ tar -xvzf geckodriver-v0.21.0-linux64.tar.gz
$ cp geckodriver /usr/local/bin
$ chmod +x /usr/local/bin/geckodriver
$ export PATH=$PATH:/usr/local/bin/geckodriver
```

#### Rode a app (com ou sem os argumentos)
```
$ pipenv run python get_and_export.py
```

Com argumentos:

```
$ pipenv run python get_and_export.py --txt
$ pipenv run python get_and_export.py --csv
$ pipenv run python get_and_export.py --json
```

#### Arquivo de configuração (data_source.py)

Se quiser mudar a URL utilizada para, digamos, acessar um arquivo local, altere esse item no data_source.py. Você também pode mudar o nome do arquivo a ser salvo.
