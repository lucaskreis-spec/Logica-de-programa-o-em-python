class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

def latir(self):
    print(f"{self.nome} diz: Au Au!")
def mostrar_info(self):
    print(f"=== Informações do cachorro {self.nome} ===")
    print(f"Raça: {self.raca}")
    print(f"Idade: {self.idade}")

cachorro1 = Cachorro("Rex", "Rottweiler", 6)
cachorro2 = Cachorro("Mel", "Shihtzu", 3)

latir(cachorro1)
latir(cachorro2)

mostrar_info(cachorro1)
mostrar_info(cachorro2)

cachorro1.idade = 8
mostrar_info(cachorro1)