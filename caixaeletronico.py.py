nota = int(input('Digite o valor que deseja sacar?: R$'))

#Verifica se é possível sacar o valor
if nota % 10 != 0:
    print('Desculpe, o caixa só possui as notas [R$ 100, 50, 20,10], escolha outro valor.')
else:
    total = nota
    cedula = 100

while total > 0:
    quantidade_cedula = total // cedula
    total %= cedula

    if quantidade_cedula > 0:
        print(f'{quantidade_cedula} notas de R${cedula}')

    if cedula == 100:
        cedula = 50
    elif cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
