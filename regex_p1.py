import re #RegEx

txt = 'Olá Felipe Schmaedecke, seja bem vindo ao curso de RegEx'

p = input('Digite a expressão que deseja pesquisar: ')

res = re.findall(p, txt)

qtd_elems = len(res)
print(res)
print(f'Quantidade encontrada: {qtd_elems}')

for r in res:
    print(r)
