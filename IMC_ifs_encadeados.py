# IMC = Peso ÷ (Altura × Altura)#
print('+------------------------------+------------------------------+')
print('+                      PROGRAMA CÁLCULO IMC                   +')
print('+------------------------------+------------------------------+')
altura = float(input('+ Digite sua altura: '))
peso = float(input('+ Digite seu peso: '))

imc = peso / altura ** 2

print(f'+ IMC = {peso} ÷ {altura}²')
print(f'+ IMC é {imc:.2f}.')

if imc <= 16.9:
    msg = '+ Você está muito abaixo do peso.'
elif imc >= 17:
    if imc <= 18.4:
        msg = '+ Você está abaixo do peso.'
    elif imc >= 18.5:
        if imc <= 24.9:
            msg = '+ Você está com o peso normal. Muito bem!'
        elif imc >= 25:
            if imc <= 29.9:
                msg = '+ Você está acima do peso. Atenção!'
            elif imc >= 30:
                if imc <= 34.9:
                    msg = '+ Você está com obesidade grau I. Cuide-se!'
                elif imc >= 35:
                    if imc <= 40:
                        msg = '+ Você está com obesidade grau II. Cuide-se!! Revise seu hábitos alimentares'
                    elif imc > 40:
                        msg = '+ Você está com obesidade grau III. Vá ao nutricionista!'
print(msg)
