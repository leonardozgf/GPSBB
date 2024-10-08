import json

# Dados dos produtos
alunos = [
    {
        "nome": "Israel",
        "nota": 8
    },
    {
        "nome": "Larissa",
        "nota": 5
    },
    {
        "nome": "Maria",
        "nota":10
    }
]

# Caminho do arquivo JSON
caminho_arquivo = 'alunos.json'

# Criar o arquivo JSON e escrever os dados
with open(caminho_arquivo, mode='w', encoding='utf-8') as arquivo:
    json.dump(alunos, arquivo, indent=4)

print(f'Arquivo "{caminho_arquivo}" criado com sucesso!')