# Entradas do usuário
while True:
    try:
        numeros_sequencia = int(input("Quantos números você vai digitar?:"))
        if numeros_sequencia < 0:
            print("Erro! A quantidade de números não pode ser negativa, tente novamente.")
            continue
        break
    except ValueError:
        print("Erro! Número inválido, tente novamente")
    
# Cria lista vazia
numeros = []

# Recebe os números e armazena na lista
for i in range(numeros_sequencia):
    n = float(input("Digite um número: "))
    numeros.append(n)

# Exibe resultado
print(f"A sequência de números é {numeros}")
print(f"O maior número da sequência é {max(numeros)}")
print(f"O menor número da sequência é {min(numeros)}")
