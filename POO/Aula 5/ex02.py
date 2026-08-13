class Gafanhoto:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        resultado = self.idade + 1
        return resultado

    def __getstate__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}."

g1 = Gafanhoto("Fulano", 100)

print(g1.__getstate__())
print(g1.aniversario())