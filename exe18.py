# Função que conta o número de vogais em uma string
def contar_vogais(string):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in string:
        if char in vogais:
            contador += 1
    return contador

# Solicita uma string ao usuário
texto = input("Digite uma string: ")

# Chama a função e exibe o resultado
total_vogais = contar_vogais(texto)
print(f"O total de vogais na string é: {total_vogais}")
