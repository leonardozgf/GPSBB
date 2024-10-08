# Função que calcula a média de uma lista de números
def calcular_media(numeros):
    if len(numeros) == 0:
        return 0  # Evita divisão por zero
    return sum(numeros) / len(numeros)

# Testa a função com diferentes listas
lista1 = [10, 20, 30, 40, 50]
lista2 = [5, 7, 8, 9, 10]
lista3 = [100, 200, 300]

# Exibe a média de cada lista
print(f"A média da lista1 é: {calcular_media(lista1)}")
print(f"A média da lista2 é: {calcular_media(lista2)}")
print(f"A média da lista3 é: {calcular_media(lista3)}")
