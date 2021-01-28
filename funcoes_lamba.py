soma = lambda a, b: a+b
multiplica = lambda a, b, c: (a + b) * c

r = soma(5, 10)
print(r)
print(multiplica(5, 3, 10))

print((lambda a, b: a + b)(3, 5))

r = lambda x, func: x + func(x)

print(r(2, lambda a: a*a))
