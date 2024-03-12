salario = float(input("Digite o salario: "))

if salario <= 1903.98:
    print("Isento de imposto de renda")
elif salario >= 1903.99 and salario <= 2826.65:
    result = salario - 142.80
    print(f"R$142.80 deduzido, salario a pagar: R${result}")
elif salario >= 2826.66 and salario <=3751.05:
    result = salario - 354.80
    print(f"R$352.80 deduzido, salario a pagar: R${result}")
elif salario >= 3751.06 and salario <= 4664.68:
    result = salario - 636.13
    print(f"R$636.13 deduzido, salario a pagar: R${result}")
else:
    result = salario - 869.36
    print(f"R$869.36 deduzido, salario a pagar: R${result}")