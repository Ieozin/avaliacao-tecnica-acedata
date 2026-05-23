sequencia_numero = int(input("Olá, quantos números da sequência de Fibonacci você quer?:"))
print("Estes são os números:")

x = 1
y = 1

fibonnaci = []
fibonnaci_01 = []

for i in range(sequencia_numero):
    fibonnaci.append(x)
    z = x
    x = y 
    y = z + y

print(fibonnaci)

verificar_numero = int(input("Qual número você quer verificar se está na sequência?:"))

x = 1
y = 1

while x <= verificar_numero:
    fibonnaci_01.append(x)
    z = x
    x = y 
    y = z + y

if verificar_numero in fibonnaci_01:
    print(f"O número {verificar_numero} que você escolheu está na sequência de Fibonacci!")
else:
    print(f"O número {verificar_numero} que você escolheu não está na sequência de Fibonacci!")    