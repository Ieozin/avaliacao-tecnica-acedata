numeros = []

numeros_sequencia = int(input("Quantos números você vai digitar?:"))

for i in range(numeros_sequencia):
    n = float(input("Digite um número: "))
    numeros.append(n)

print(f"A sequência de números é {numeros}")
print(f"O maior número da sequência é {max(numeros)}")
print(f"O menor número da sequência é {min(numeros)}")
