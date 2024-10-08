# Função que converte Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Solicita a temperatura em graus Celsius ao usuário
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Chama a função e exibe o resultado
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"A temperatura em Fahrenheit é: {fahrenheit}")
