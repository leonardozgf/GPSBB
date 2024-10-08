from pymongo import MongoClient

# Conectar ao MongoDB local
client = MongoClient('localhost', 27017)

# Escolher o banco de dados
db = client['fiap']  # Substitua pelo nome do seu banco de dados

# Acessar a coleção "alunos"
colecao = db['alunos']

# Solicitar o nome do aluno a ser removido
nome_aluno = input("Digite o nome do aluno que deseja remover: ")

# Remover o documento com o nome especificado
resultado = colecao.delete_one({"nome": nome_aluno})

# Verificar se algum documento foi removido
if resultado.deleted_count > 0:
    print(f"O aluno '{nome_aluno}' foi removido com sucesso.")
else:
    print(f"Nenhum aluno encontrado com o nome '{nome_aluno}'.")

# Fechar a conexão
client.close()
