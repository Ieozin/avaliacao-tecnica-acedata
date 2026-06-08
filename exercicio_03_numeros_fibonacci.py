# Entradas do usuário 
while True:
    try:
        sequencia_numero = int(input("Olá, quantos números da sequência de Fibonacci você quer?: "))
        if sequencia_numero < 0:
            print("Erro! Você inseriu uma quantidade negativa, tente novamente")
            continue
        break
    except ValueError:
        print("Erro! Entrada inválida, tente novamente!")

# Valores iniciais da sequência
x = 1
y = 1

# Listas para armazenar sequência
fibonnaci = []
fibonnaci_01 = []

# Gera sequência pela entrada
for i in range(sequencia_numero):
    fibonnaci.append(x)
    z = x
    x = y 
    y = z + y

# Exibe resultado 
print(f"Estes são os números: {fibonnaci}")

# Entradas para verificação 
verificar_numero = int(input("Qual número você quer verificar se está na sequência?:"))

# Reinicia valor
x = 1
y = 1

# Gera sequência para verificar
while x <= verificar_numero:
    fibonnaci_01.append(x)
    z = x
    x = y 
    y = z + y

# Exibe resultado 
if verificar_numero in fibonnaci_01:
    print(f"O número {verificar_numero} que você escolheu está na sequência de Fibonacci!")
else:
    print(f"O número {verificar_numero} que você escolheu não está na sequência de Fibonacci!")    