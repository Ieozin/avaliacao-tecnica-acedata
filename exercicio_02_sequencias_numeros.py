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
    while True:
        try:
            n = float(input("Digite um número: "))
            numeros.append(n)
            break
        except ValueError:
            print("Erro! Número inválido, tente novamente!")

# Exibe resultado
if len(numeros) > 0:
    print(f"A sequência de números é {numeros}")
    print(f"O maior número da sequência é {max(numeros)}")
    maior_numero = max(numeros) 
    numeros.remove(maior_numero)
    print(f"O segundo maior número da sequência é {max(numeros)}")
    print(f"O menor número da sequência é {min(numeros)}")
else:
    print("Você não digitou nenhum número.")

