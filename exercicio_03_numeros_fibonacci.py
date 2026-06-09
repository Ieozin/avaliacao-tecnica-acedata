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
antepenultimo = 1

# Listas para armazenar sequência
fibonacci = []
fibonacci_verificacao = []

# Começo da sequência
if sequencia_numero >= 1:
    fibonacci.append(1)

if sequencia_numero >= 2:
    fibonacci.append(1)

if sequencia_numero >= 3:
    fibonacci.append(2)

# Valores iniciais da sequência
antepenultimo = 1
anterior = 1
atual = 2

# Gera sequência pela entrada
while len(fibonacci) < sequencia_numero:
    if atual % 2 == 0:
        proximo = antepenultimo + anterior + atual
    else:
        proximo = anterior + atual

    fibonacci.append(proximo)

    antepenultimo = anterior
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

# Começo da sequência de verificação
if verificar_numero >= 1:
    fibonacci_verificacao.append(1)
    fibonacci_verificacao.append(1)

# Reinicia valores
antepenultimo = 1
anterior = 1
atual = 2

# Gera sequência para verificar
while atual <= verificar_numero:
    fibonacci_verificacao.append(atual)

    if atual % 2 == 0:
        proximo = antepenultimo + anterior + atual
    else:
        proximo = anterior + atual

    antepenultimo = anterior
    anterior = atual
    atual = proximo
    
# Exibe resultado 
if verificar_numero in fibonacci_verificacao:
    print(f"O número {verificar_numero} que você escolheu está na sequência de Fibonacci!")
else:
    print(f"O número {verificar_numero} que você escolheu não está na sequência de Fibonacci!")    