nome = input("Digite seu nome (maior que 3 caracteres): ")
while len(nome) <= 3:
    print("Seu nome deve ter mais que 3 caracteres, insira novamente")
    nome = input("Digite seu nome (maior que 3 caracteres): ")

idade = int(input("Digite sua idade de 0 a 150: "))
if idade < 0 or idade > 150:
    print("Digite um numero valido")
    idade = int(input("Digite sua idade de 0 a 150: "))

salario = int(input("Digite seu salario: "))
if salario < 0:
    print("Seu salario deve ser maior do que zero")
    salario = int(input("Digite seu salario: "))

sexo = input("Insira seu sexo 'f' ou 'm':" )
while sexo != "f" and sexo != "m":
    print("Use apena 'f' ou 'm'")
    sexo = input("Insira seu sexo 'f' ou 'm':" )
estado = input("Digite seu estado civil com 's', 'c', 'v' ou 'd'")
if estado != "s" and estado and "c" and estado and "v" and estado != "d":
    print("Insira valores validos")
    estado = input("Digite seu estado civil com 's', 'c', 'v' ou 'd'")



