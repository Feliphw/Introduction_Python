valor = float(input('Digite o valor: '))
escolha = int(input("Digite 1.Para valor esta em Real\n" "2.Para valor está em dolar\n" "3.Para valor está em Euro"))
d = input('Digite o dia de cotação da moeda. ')

if d == 'd1': 
    dolar, euro = 5,5.70
elif d == 'd2':
    dolar, euro = 6,6.70
elif d == 'd3':
    dolar, euro = 7,7.70
else: 
    print('Não existe cotação para data informada')

if escolha == 1 :
    print(f'O valor final em real é de: R$ {valor}')
elif escolha == 2: 
    result = valor * dolar
    print(f'O valor em real é de: R${result}')
elif escolha == 3:
    result = valor * euro
    print(f'O valor em real é de: R${result}')
else:
    print('Opção digitada invalida')