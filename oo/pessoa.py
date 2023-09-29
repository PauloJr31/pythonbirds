class Pessoa:
    def __init__(self, *filhos, nome=None, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    paulo = Pessoa(nome='Paulo')
    edmar = Pessoa(paulo, nome='Edmar')
    print(Pessoa.cumprimentar(edmar))
    print(id(edmar))
    print(edmar.cumprimentar())
    print(edmar.nome)
    print(edmar.idade)
    for filho in edmar.filhos:
        print(filho.nome)
    edmar.sobrenome = 'Bezerra'
    del edmar.filhos
    print(edmar.__dict__)
    print(paulo.__dict__)

