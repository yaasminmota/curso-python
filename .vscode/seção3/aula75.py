# O continue,break,else e etc que foi usado no while tbm funciona no for

for i in range(10):

    if i == 2:
        print(f'i é 2, pulando...')
        continue
    
    if i == 8:
        break

    for j in range(1,3):
        print(i, j)

else:
    print('For completo com sucesso')