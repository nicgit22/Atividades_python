numero = int(input("Digite o numero desejado para fatorar: "))
fat = 1

if numero < 0:
    print("Não é possivel fatorar esse número")
    numero = int(input("Digite um numero valido: "))

for i in range(1, numero +1):
    fat = fat*i
print(fat)