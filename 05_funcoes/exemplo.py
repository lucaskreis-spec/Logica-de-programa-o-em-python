#Função:
#Uma função é um bloco de código criado para realizar uma determinada tarefa.
#Ela permite organizar e reutilizar código.

#1. Criando uma função
#Utilizar a palavra def para uma função

def saudacao():
    print("Olá, seja bem-vindo!")

saudacao()

#2. Criando uma função com parâmetro

#Parâmetros permitem enviar informações para a função.

def saudacao(nome):
    print(f"Olá {nome}!")

saudacao("Ana")
saudacao("João")

#3. Mais de um parâmetro
def apresentar(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

apresentar("Maria", 17)
apresentar("João", 20)

#4. Função com cálculo

def somar(n1, n2):
    resultado = n1 + n2
    print(f"Resultado: {resultado}")

somar(20,10)
somar(90,70)

#5. Retornando um valor
#return devolve um valor para o local onde a função foi chamada.

def somar(n1, n2):
    return n1 + n2

print(somar(10,5))

#6. Função com condição
def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(verificarIdade(16))
print(verificarIdade(18))

#7. Parâmetro com valor padrão
def saudacao(nome = "Aluno"):
    print(f"Olá {nome}")

saudacao("João")
saudacao()

#8. Função utilizando lista

def calcularMedia():
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)

notas = [8, 7, 9, 10]
media = calcularMedia()

print(f"Média: {media}")