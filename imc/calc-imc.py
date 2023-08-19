altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em quilogramas: '))
imc = peso / (altura ** 2)
print('Seu Índice de Massa Corporal é:', imc)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está com peso normal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
else:
    print('Você está obeso.')