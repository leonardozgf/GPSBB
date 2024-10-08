# Solicita um número inteiro ao usuário
# A função input() coleta a entrada do usuário como string. 
# A função int() converte essa entrada para um número inteiro.
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar usando if e else
# A condição numero % 2 == 0 verifica se o resto da divisão do número por 2 é igual a 0.
# Se for, o número é par; caso contrário, é ímpar.
if numero % 2 == 0:
    # Se a condição for verdadeira, imprime que o número é par.
    print(f"O número {numero} é par.")
else:
    # Se a condição for falsa, imprime que o número é ímpar.
    print(f"O número {numero} é ímpar.")
