import random

list = []
for i in range(30):
    while True:
        num = random.randint(0,1)
        if (num >= 0) and (num <= 1):
            break
    list.append(num)

print(list)

countzero, countone = 0,0
for num in list:
    if(num == 0):
        countzero += 1
    else:
        countone += 1
print(f"Numeros de zeros: {countzero}")
print(f"Numeros de um: {countone}")

percent = countone/30 * 100
print(f"Porcentagem de um: {percent}")
percentzero = countone/30 * 100
print(f"Porcentagem de zero: {percentzero}")