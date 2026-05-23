# Entradas do usuário
salario_hora = float(input("Informe o seu salário por hora: "))
horas_mes = float(input("Informe a quantidade de horas que você trabalhou no mês: "))
filhos_menos_14 = int(input("Informe quantos filhos menores de 14 anos que você tem: "))

# Calcula salário bruto
salario_bruto = salario_hora * horas_mes

# Define salário família 
if salario_bruto <= 788:
    salario_familia = 30.50

elif salario_bruto <= 1100:
    salario_familia = 18.50

else:   
    salario_familia = 11.90

# Calcula salário final 
salario_familia_final = salario_familia * filhos_menos_14
salario_liquido = salario_bruto + salario_familia_final

# Exibe resultado com condicional para sem filhos
print("--Folha de pagamento--")
print(f"O salário bruto será de:R${salario_bruto:.2f}")

if filhos_menos_14 > 0:
    print(f"O salário família será de R${salario_familia:.2f} por cada filho") 
    print(f"O salario família final será de R${salario_familia_final:.2f}")
else:
     print("Você não tem direito á salário família")
       
print(f"O salário líquido será de R${salario_liquido:.2f}")