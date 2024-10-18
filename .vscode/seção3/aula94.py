#Listas dentro de listas

salas = [['Ana','Joao','Helena'], ['Pedro','José'], ['Luis','Kaua']]

print(salas[0][2])

for sala in salas:
    for aluno in sala:
        print(aluno)