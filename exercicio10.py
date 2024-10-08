from pymongo import MongoClient

# Conectar ao MongoDB local
client = MongoClient('localhost', 27017)

# Escolher o banco de dados
db = client['fiap']  # Substitua pelo nome do seu banco de dados

# Acessar a coleção "clientes"
colecao = db['pessoas']  # Substitua pelo nome da sua coleção

# Consultar todos os clientes com idade superior a 30 anos
clientes_maiores_30 = colecao.find({"Idade": {"$gt": 30}})

# Exibir os clientes encontrados
print("Clientes com idade superior a 30 anos:")
for cliente in clientes_maiores_30:
    print(cliente)

# Fechar a conexão
client.close()
