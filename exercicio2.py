# Exercicio 2
matriz = [[1,2],[3,4]]
matriz_multiplicada = [[0,0], [0,0]]
escalar = 2
# Percorrendo as linhas
for index_linha, linha in enumerate(matriz):
    # Percorrendo as colunas
    for index_coluna, coluna in enumerate(linha):
        # Multiplicando a coluna pelos escalares
        matriz_multiplicada[index_linha][index_coluna] = matriz[index_linha][index_coluna] * escalar
print(matriz_multiplicada)