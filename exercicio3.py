import csv

# Dados a serem escritos no arquivo
dados = [
    ["Nome", "Idade", "Cidade"],
    ["Alice", 30, "São Paulo"],
    ["Bruno", 25, "Rio de Janeiro"],
    ["Carlos", 28, "Belo Horizonte"],
    ["Diana", 22, "Curitiba"]
]

# Criar o arquivo CSV
caminho_arquivo = 'dados.csv'
with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

print(f'Arquivo "{caminho_arquivo}" criado com sucesso!')

# Caminho do arquivo CSV
caminho_arquivo = 'dados.csv'

# Função para ler e imprimir o conteúdo do arquivo CSV
def ler_csv(caminho):
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        # Ignorar o cabeçalho
        next(leitor)
        
        # Ler e imprimir cada linha do arquivo
        for linha in leitor:
            nome, idade, cidade = linha
            print(f'Nome: {nome}, Idade: {idade}, Cidade: {cidade}')

# Chamar as funções
ler_csv(caminho_arquivo)
