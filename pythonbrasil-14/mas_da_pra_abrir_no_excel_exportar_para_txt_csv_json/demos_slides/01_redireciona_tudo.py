new_list = ['pybr', 'natal', '2018', 'palestras']

with open('all_output.txt', 'w') as fhand:
    fhand.write('\n'.join(str(x) for x in new_list))
