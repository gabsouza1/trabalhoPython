# Exercício 5 – (1.0 ponto) – Elaborar um algoritmo que leia um nome qualquer e mostre o nome em formato de escada ede escada invertida.

nome = str(input('Digite o seu nome: '))
for i in range(0, len(nome)+1):
    print(nome[:i])