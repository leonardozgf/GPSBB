# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação matemática desejada
operacao = input("Digite a operação desejada (soma, subtração, multiplicação, divisão): ").lower()

# Realiza a operação correspondente usando if, elif e else
if operacao == "soma":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif operacao == "subtração" or operacao == "subtracao":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "multiplicação" or operacao == "multiplicacao":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "divisão" or operacao == "divisao":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Tente novamente.")
