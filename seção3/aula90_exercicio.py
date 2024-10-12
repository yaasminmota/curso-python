'''
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar,
 e listar valores da sua lista. 
 Não permita que o programa quebre com erros de índices
 inexistentes na lista.
'''
lista = []
inserir = None
apagar = None
while True:
    entrada = input('Selecione uma opção: \n [I]nserir \n [A]pagar \n [L]istar \n').lower()
    valores = 'ial'

    if entrada not in valores:
        print('Opção inválida')
        continue

    if entrada == 'i':
        while True:
            inserir = input('Digite o item que deseja inserir: ')
            if not inserir:
                print('Inválido')
                continue
            lista.append(inserir)
        
            opcao1 = input('Deseja inserir mais algum item? [S]im ou [N]ão?').lower()

            if opcao1 == 's':
                continue
            else:
                break

    if entrada == 'a':
        for indice,item in enumerate(lista):
                print(indice,item)
        while True:
            try:
                apagar = int(input('Digite o indice que queira apagar: '))
                del lista[apagar]
            
                opcao2 = input('Deseja apagar mais algum item? [S]im ou [N]ão?').lower()

                if opcao2 == 's':
                    continue
                else:
                    break
            except:
                print('Inválido')
                continue
    
    if entrada == 'l':    
        for indice,item in enumerate(lista):
            print(indice,item)
 