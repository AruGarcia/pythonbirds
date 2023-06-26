class Pessoa:
    def __init__(self, *filhos, nome=None, idade=43):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Aruana = Pessoa(nome='Aruanã')
    eleonora = Pessoa(Aruana, nome='Eleonora')
    print(Pessoa.cumprimentar(eleonora))
    print(id(eleonora))
    print(eleonora.cumprimentar())
    print(eleonora.nome)
    print(eleonora.idade)
    for filho in eleonora.filhos:
        print(filho.nome)

