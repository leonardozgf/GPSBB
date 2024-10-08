import json

# Dados dos produtos
produtos = [
    {
        "nome": "Produto A",
        "preco": 10.50,
        "quantidade": 100
    },
    {
        "nome": "Produto B",
        "preco": 20.00,
        "quantidade": 50
    },
    {
        "nome": "Produto C",
        "preco": 15.75,
        "quantidade": 200
    }
]

# Caminho do arquivo JSON
caminho_arquivo = 'produtos.json'

# Criar o arquivo JSON e escrever os dados
with open(caminho_arquivo, mode='w', encoding='utf-8') as arquivo:
    json.dump(produtos, arquivo, indent=4)

print(f'Arquivo "{caminho_arquivo}" criado com sucesso!')

# Função para ler o arquivo JSON e converter em dicionário
def ler_json(caminho):
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        produtos = json.load(arquivo)
        return produtos

# Chamar a função e imprimir o resultado
produtos = ler_json(caminho_arquivo)
print(produtos)
