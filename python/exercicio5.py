# Exercício 5 – (1.0 ponto) – Elaborar um algoritmo que leia um nome qualquer e mostre o nome em formato de escada ede escada invertida.

nome = input("Entre com um nome: ")
length = int(len(nome))
for i in range(length):
    print(nome[0 : i + 1])
for i in range(length):
    print(nome[-length : -i -1])