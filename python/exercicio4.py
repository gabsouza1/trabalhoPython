# Exercício 4 – (1.0 ponto) – Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita paraesquerda ou vice−versa. 
# exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços epontuação são ignorados.
#  A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foramignorados. 
# Elaborar um algoritmo para ler uma seqüência de caracteres (palavra ou frase) e informar se a palavra ou frase é um palíndromo ou não.

phrase = str(input('Digite a frase: ').strip())
words = phrase.split()
join = ''.join(words)
backward = ''
for words in range(len(join) -1, -1, -1):
    backward += join[words]
if backward == join:
    print('A palavra ou frase é uma palindromo')
else:
    print('A palavra ou frase não é um palindromo')
