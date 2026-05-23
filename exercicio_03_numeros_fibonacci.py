sequencia_numero = int(input("Olá, quantos números da sequência de Fibonacci você quer?:"))
print("Estes são os números:")


x = 1
y = 1

fibonnaci = []

for i in range(sequencia_numero):
    fibonnaci.append(x)
    z = x
    x = y 
    y = z + y

print(fibonnaci)

if sequencia_numero in fibonnaci:
    print(f"O número {sequencia_numero} que você escolheu está na sequência de Fibonacci!")
else:
    print(f"O número {sequencia_numero} que você escolheu não está na sequência de Fibonacci!")    