# While/Else

#01235678912345
#Valor qualquer

string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]
    if letra == ' ':
        break
    print(letra)
    i += 1
else:
    print('Não há espaço na string')
# mesmo se nao houver espaco ele printa essa msg
print('Há espaço na string')