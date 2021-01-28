class Carro:
    velMax = 0
    ligado = False
    cor = ''

    def mostrar(self):
        print(f'Velocidade Máxima: {self.velMax}')
        print(f'Cor: {self.cor}')
        print('Carro está', end=' ')
        if self.ligado:
            print('ligado!')
        else:
            print('desligado!')


carro1 = Carro()
carro2 = Carro()
carro3 = Carro()

carro1.velMax = 180
carro1.ligado = True
carro1.cor = 'Vermelho'

carro2.velMax = 200
carro2.cor = 'Prata'

carro3.velMax = 280
carro3.ligado = True
carro3.cor = 'Preto'

carro1.mostrar()
print()
carro2.mostrar()
print()
carro3.mostrar()
