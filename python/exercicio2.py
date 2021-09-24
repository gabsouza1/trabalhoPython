# Exercício 2 – (1.0 ponto) – Elaborar um algoritmo para ler o nome completo de uma pessoa e, em seguida, mostrar:  
# O nome em letras minúsculas (caixa baixa);  
# O nome de trás para frente utilizando somente letras maiúsculas (caixa alta);  
# A concatenação do primeiro e do último nome; 
#  A quantidade de palavras do nome completo;  
#  A quantidade de letras "a's" do nome.

firstName = str(input('Digite seu nome: '))
lastName = str(input('Digite seu sobrenome: '))
fullName = firstName + ' ' + lastName


print(f'Nome minusculo {firstName.lower()}')
print(f'Nome ao contrário em maiúsculo : {firstName.upper()[::-1]}' )
print(f'Seu nome completo é: {fullName}')
print('Quantidade de palavras do nome completo: {} '.format (len(fullName.split())))
print('Quantidade de letras "a" no nome: {}'.format(fullName.lower().count('a')))
print('Quantidade de letras "s" no nome: {}'.format(fullName.lower().count('s')))



