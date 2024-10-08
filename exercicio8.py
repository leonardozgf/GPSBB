from pymongo import MongoClient

# Conectar ao MongoDB local
client = MongoClient('localhost', 27017)

# Escolher o banco de dados
db = client['fiap']  # Substitua pelo nome do seu banco de dados

# Acessar a coleção "alunos"
colecao = db['alunos']

# Consultar todos os documentos da coleção
documentos = colecao.find()

# Exibir cada documento no console
print("Documentos na coleção 'alunos':")
for documento in documentos:
    print(documento)

# Fechar a conexão
client.close()
