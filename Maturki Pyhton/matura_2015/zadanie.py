from math import *
with open('dane4.txt','r') as plik:
    dane = plik.readlines()
    for i in range(len(dane)):
        dane[i]= int(dane[i].rstrip())

odp = open('wynik6.txt','w')
odp.write(f'a)\n')

#a)
ile = 0
def czy_pierwsza(zmienna):
    if zmienna <2:
        return False
    for i in range(2,int(zmienna**0.5)+1):
        if zmienna % i == 0:
            return False
    return True

tablica_pierwszych = []
for i in range(len(dane)):
    if czy_pierwsza(dane[i]):
        tablica_pierwszych.append(dane[i])
        ile +=1

odp.write(f'{ile}\n')
odp.write(f'b)\n')

max = 0
min = tablica_pierwszych[0]
for znak in tablica_pierwszych:
    if znak > max:
        max = znak
    if znak < min:
        min = znak

odp.write(f'największa: {max}\n')
odp.write(f'najmniejsza: {min}\n')

odp.write(f'c)\n')

for i in range(len(tablica_pierwszych)-1):
    if fabs(tablica_pierwszych[i] - tablica_pierwszych[i+1]) == 2:
        odp.write(f'{tablica_pierwszych[i]} {tablica_pierwszych[i+1]}\n')
        
odp.close()

