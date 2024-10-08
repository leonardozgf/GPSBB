# Função que encontra o máximo em uma lista
def encontrar_maximo(lista):
    if len(lista) == 0:
        return None
    return max(lista)

# Testa a função com diferentes listas
lista1 = [10, 20, 30, 40, 50]
lista2 = [5, 7, 8, 9, 10]
lista3 = []

# Exibe o maior número de cada lista
print(f"O maior número da lista1 é: {encontrar_maximo(lista1)}")
print(f"O maior número da lista2 é: {encontrar_maximo(lista2)}")
print(f"O maior número da lista3 é: {encontrar_maximo(lista3)}")
