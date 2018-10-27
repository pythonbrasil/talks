import os
import sys
from contextlib import redirect_stdout

STDOUT_FD = sys.stdout.fileno()

new_list = ['pybr', 'natal', '2018', 'palestras']

count = 0

with open('python_brasil.txt', 'w') as fhand:
    with redirect_stdout(fhand):
        for item in new_list:
            count = count + 1
            os.write(STDOUT_FD,
                     bytes('Line written: {}'.format(count) + '\n', 'utf8'))
            fhand.write(str(item)+'\n')
