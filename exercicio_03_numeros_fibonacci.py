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
anterior = 1
atual = 1

# Listas para armazenar sequência
fibonacci = []
fibonacci_verificacao = []

# Gera sequência pela entrada
for i in range(sequencia_numero):
    fibonacci.append(anterior)
    if atual == eval:
        proximo = anterior + atual + anterior
        anterior = atual
        atual = proximo
    
   
# Exibe resultado 
print(f"Estes são os números: {fibonacci}")

# Entradas para verificação 
while True:
    try:
        verificar_numero = int(input("Qual número você quer verificar se está na sequência?:"))
        if verificar_numero < 0:
            print("Erro! O número não pode ser negativo, tente novamente")
            continue
        break
    except ValueError:
        print("Erro! Entrada inválida, tente novamente!")

# Reinicia valor
anterior = 1
atual = 1

# Gera sequência para verificar
while anterior <= verificar_numero:
    fibonacci_verificacao.append(anterior)
    proximo = anterior + atual
    anterior = atual 
    atual = proximo

# Exibe resultado 
if verificar_numero in fibonacci_verificacao:
    print(f"O número {verificar_numero} que você escolheu está na sequência de Fibonacci!")
else:
    print(f"O número {verificar_numero} que você escolheu não está na sequência de Fibonacci!")    