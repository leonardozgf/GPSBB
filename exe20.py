# Função que converte temperatura
def converter_temperatura(celsius, tipo="F"):
    if tipo == "F":
        # Converte para Fahrenheit
        return (celsius * 9/5) + 32
    elif tipo == "K":
        # Converte para Kelvin
        return celsius + 273.15
    else:
        # Retorna Fahrenheit por padrão
        return (celsius * 9/5) + 32

# Solicita a temperatura em Celsius ao usuário
celsius = float(input("Digite a temperatura em Celsius: "))

# Solicita o tipo de conversão (opcional)
tipo = input("Digite 'F' para Fahrenheit ou 'K' para Kelvin (opcional): ").upper()

# Chama a função e exibe o resultado
temperatura_convertida = converter_temperatura(celsius, tipo)
print(f"A temperatura convertida é: {temperatura_convertida}")
