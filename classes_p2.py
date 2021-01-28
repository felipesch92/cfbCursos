class Carro:
    def __init__(self, v, l, c):
        self.velMax = v
        self.ligado = l
        self.cor = c

    def mostrar(self):
        print(f'Velocidade Máxima: {self.velMax}')
        print(f'Cor: {self.cor}')
        print('Carro está', end=' ')
        if self.ligado:
            print('ligado!')
        else:
            print('desligado!')
        print('-' * 40)

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def andar(self):
        if self.ligado:
            print('Andando')
        else:
            print('Carro está desligado, deseja ligar?')
            r = input().upper()[0]
            if r == 'S':
                self.ligar()
                self.andar()


carro1 = Carro(180, True, 'Vermelho')
carro2 = Carro(240, False, 'Prata')
carro3 = Carro(280, True, 'Preto')

carro1.mostrar()
carro1.desligar()
carro1.andar()
carro1.mostrar()

carro3.andar()
