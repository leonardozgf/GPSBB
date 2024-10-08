# Solicita uma nota ao usuário
nota = float(input("Digite uma nota de 0 a 100: "))

# Verifica a classificação da nota utilizando if, elif e else
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")
