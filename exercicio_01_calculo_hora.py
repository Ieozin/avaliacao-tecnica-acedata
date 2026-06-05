# Constantes do salário bruto
SALARIO_FAIXA_MIN = 788
SALARIO_FAIXA_MAX = 1100

# Constantes do salário família
SALARIO_FAMILIA_MIN = 11.90
SALARIO_FAMILIA_MID = 18.50
SALARIO_FAMILIA_MAX = 30.50

# Entradas do usuário
while True:
    try:
        salario_hora = float(input("Informe o seu salário por hora: "))
        if salario_hora < 0:
            print("Erro! Salário negativo, digite novamente")
            continue
        break
    except ValueError:
        print("Erro! Salário inválido, digite novamente")

while True:
    try:
        horas_mes = float(input("Informe a quantidade de horas que você trabalhou no mês: "))
        if horas_mes < 0:
            print("Erro! Horas negativas, digite novamente")
            continue
        break
    except ValueError:
        print("Erro! Horas inválidas, digite novamente")

while True:
    try:
        filhos_menos_14 = int(input("Informe quantos filhos menores de 14 anos que você tem: "))
        if filhos_menos_14 < 0:
            print("Erro! Quantidade de filhos negativa, digite novamente")
            continue
        break
    except ValueError:
        print("Erro! Quantidade de filhos inválida, digite novamente")

# Calcula salário bruto
salario_bruto = salario_hora * horas_mes

# Define salário família 
if salario_bruto <= SALARIO_FAIXA_MIN:
    salario_familia = SALARIO_FAMILIA_MAX

elif salario_bruto <= SALARIO_FAIXA_MAX:
    salario_familia = SALARIO_FAMILIA_MID

else:   
    salario_familia = SALARIO_FAMILIA_MIN

# Calcula salário final 
salario_familia_final = salario_familia * filhos_menos_14
salario_liquido = salario_bruto + salario_familia_final

# Exibe resultado com condicional para sem filhos
print("--Folha de pagamento--")
print(f"O salário bruto será de: R${salario_bruto:.2f}")

if filhos_menos_14 > 0:
    print(f"O salário família será de R${salario_familia:.2f} por filho") 
    print(f"O salário família final será de R${salario_familia_final:.2f}")
else:
     print("Não há filhos para calcular o benefício")
       
print(f"O salário líquido será de R${salario_liquido:.2f}")