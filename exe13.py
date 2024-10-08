# Solicita a idade ao usuário
idade = int(input("Digite a sua idade: "))

# Classifica a idade nas faixas etárias utilizando if, elif e else
if idade < 12:
    print("Criança")
elif 12 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 64:
    print("Adulto")
else:
    print("Idoso")
