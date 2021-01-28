import re

txt = 'Bem vindo ao maravilhoso mundo de python'

res = '[' + re.sub(' ', '][', txt) + ']'
print(res)
