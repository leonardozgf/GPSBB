from pymongo import MongoClient

# Conectar ao MongoDB local
client = MongoClient('localhost', 27017)

# Listar os bancos de dados disponíveis
bancos_de_dados = client.list_database_names()

# Exibir a lista de bancos de dados
print("Bancos de dados disponíveis:")
for db in bancos_de_dados:
    print(f"- {db}")

# Fechar a conexão
client.close()
