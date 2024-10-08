# Solicita três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica qual é o maior número usando if, elif e else
if num1 > num2 and num1 > num3:
    print(f"O maior número é: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é: {num2}")
else:
    print(f"O maior número é: {num3}")
