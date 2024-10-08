import csv

# Dados a serem escritos no arquivo
pessoas = [
    ["Nome", "Idade"],
    ["Alice", 30],
    ["Junior", 25],
    ["Macos", 32],
    ["João", 22]
]

# Criar o arquivo CSV
caminho_arquivo = 'pessoas.csv'
with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(pessoas)

print(f'Arquivo "{caminho_arquivo}" criado com sucesso!')

import csv

# Função para ler o arquivo CSV e retornar os dados como uma lista
def ler_csv(caminho):
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)  # Ignora o cabeçalho
        return [linha for linha in leitor]

# Função para escrever os dados de volta no arquivo CSV
def escrever_csv(caminho, dados):
    with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Nome", "Idade"])  # Escreve o cabeçalho
        escritor.writerows(dados)

# Caminho do arquivo CSV
caminho_arquivo = 'pessoas.csv'

# Ler os dados do arquivo
pessoas = ler_csv(caminho_arquivo)

# Mostrar as pessoas disponíveis
print("Pessoas disponíveis:")
for pessoa in pessoas:
    print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}")

# Solicitar ao usuário que escolha uma pessoa pelo nome
nome_escolhido = input("Digite o nome da pessoa para alterar a idade: ")

# Procurar a pessoa na lista
pessoa_encontrada = None
for pessoa in pessoas:
    if pessoa[0].lower() == nome_escolhido.lower():  # Comparação sem considerar maiúsculas/minúsculas
        pessoa_encontrada = pessoa
        break

# Se a pessoa foi encontrada, solicitar nova idade
if pessoa_encontrada:
    nova_idade = input(f"Digite a nova idade para {pessoa_encontrada[0]}: ")
    pessoa_encontrada[1] = nova_idade  # Altera a idade

    # Escrever os dados atualizados de volta no arquivo
    escrever_csv(caminho_arquivo, pessoas)
    print(f"A idade de {pessoa_encontrada[0]} foi alterada com sucesso!")
else:
    print("Pessoa não encontrada.")
