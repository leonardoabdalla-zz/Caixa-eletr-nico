print(f'='*50)
print(f'{"CAIXA ELETRÔNICO":^50}')
print(f'='*50)
while True:
    sacar = int(input('Qual valor deseja sacar? '))
    valor = cont50 = cont20 = cont10 = cont1 = cont = 0
    while sacar > 0:
        if sacar >= 50:
            sacar -= 50
            cont50 += 1
            cont += 1
        elif sacar >= 20 and sacar < 50:
            sacar -= 20
            cont20 += 1
            cont += 1
        elif sacar >= 10 and sacar < 20:
            sacar -= 10
            cont10 += 1
            cont += 1
        elif sacar > 0 and sacar < 10:
            sacar -= 1
            cont1 += 1
            cont += 1
    print(f'{"Cédulas de R$ 50,00":.<50}0{cont50}\n{"Cédulas de R$ 20,00":.<50}0{cont20}\n'
          f'{"Cédulas de R$ 10,00":.<50}0{cont10}\n{"Cédulas de R$ 01,00":.<50}0{cont1}\n\n\n'
          f'{"Total de cédulas":.<50}{cont}')
    sacar = input('Deseja realizar novo saque?[S/N] ').strip().upper()
    if sacar == 'N' or sacar == 'NÃO' or sacar == '2':
        break

