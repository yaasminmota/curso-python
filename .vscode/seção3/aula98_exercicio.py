# Cálculo primeiro e segundo dígito de um CPF

while True:
    try: 
        cpf = input('Digite seu cpf:')
       
        digitos1 = cpf[:9]

        if len(cpf) < 11:
            print('Inválido')
            continue

        mult1 = 10
        resultado1 = 0

        for digito1 in digitos1:

            resultado1 += int(digito1) * mult1
            mult1 -= 1

        digito1 = (resultado1 * 10) % 11
        digito1 if digito1 <= 9 else 0
        print(f'O primeiro digito é {digito1}')

        digitos2 = digitos1 + str(digito1)
    
        mult2 = 11
        resultado2 = 0

        for digito2 in digitos2:
            resultado2 += int(digito2)*mult2
            mult2 -= 1
        
        digito2 = (resultado2*10)%11
        
        digito2 if digito2 <= 9 else 0
        print(f'O segundo dígito é {digito2}')

    

    except:
        print('Inválido. Digite apenas números.')
