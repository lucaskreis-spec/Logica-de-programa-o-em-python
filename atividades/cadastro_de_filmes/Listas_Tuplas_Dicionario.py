# 1. Cadastro de filmes

#Crie um programa para organizar uma lista de filmes. O programa deverá:

#1. Criar uma lista contendo inicialmente 5 filmes.

lista = ["Resident Evil", "Homem-Aranha", "Tusk", "O Carro Assassino", "Os Tomates Assassinos"]
#2. Exibir todos os filmes cadastrados.

print(lista)

#3. Exibir o primeiro filme da lista.

print(lista[0])

#4. Exibir o último filme da lista.

print(lista[-1])

#5. Adicionar um novo filme ao final da lista.

lista.append("O Biscote de Gengibre Assassino")
print(lista)

#6. Inserir um novo filme em uma posição específica.

lista.insert(3, "SCREAMBOAT")
print(lista)
#7. Remover um filme da lista.

lista.remove("Homem-Aranha")
print(lista)
#8. Alterar o nome de um dos filmes.

lista[1] = "Nosferatu"
print(lista)
#9. Exibir a quantidade de filmes cadastrados.

print(len(lista))
#10. Verificar se um determinado filme está presente na lista.
if "Resident Evil" in lista:
    print("O filme Resident Evil está na lista.")
else:
    print("O filme Resident Evil não está na lista.")
