import re

txt = 'Seja bem vindo ao maravilho mundo de Python'

re = re.split(' ', txt)
print(re)
for r in re:
    print(r)
