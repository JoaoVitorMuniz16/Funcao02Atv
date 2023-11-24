def aumento(x):
    salario = x*0.15
    salario_novo = x + salario
    print(salario_novo)

salario = int(input("dgite seu salario, e saiba qual o seu aumento:"))
aumento(salario)