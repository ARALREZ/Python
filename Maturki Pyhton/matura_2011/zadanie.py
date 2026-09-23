with open ('hasla.txt') as plik:
    dane = plik.readlines()
    for i in range(len(dane)):
        dane[i]=dane[i].rstrip()

odp = open('wynik4a.txt','w')
odp.write('a)\n')

def ile_hasel(zmienna):
    parzy = 0
    niepa = 0
    for i in range(len(zmienna)):
        ile = 0
        for znak in zmienna[i]:
            if znak !=' ':
                ile +=1
        if ile % 2 == 0:
            parzy +=1
        else:
           niepa +=1
    return parzy,niepa

parzyste , nieparzyste = ile_hasel(dane)
odp.write(f'Parzyste {parzyste}\n')
odp.write(f'Nieparzyste {nieparzyste}\n')
odp.close()

odp = open('wynik4b.txt', 'w')
odp.write('b)\n')

def czy_palindrom(zmienna):
    if zmienna == zmienna[::-1]:
        return True
    return False

for i in range(len(dane)):
    if czy_palindrom(dane[i]):
        odp.write(f'{dane[i]}\n')

odp.close()

odp = open('wynik4c.txt','w')
odp.write('c)\n')

def czy_kod(zmienna):
    for i in range(len(zmienna)-1):
        if ord(zmienna[i]) + ord(zmienna[i+1]) == 220:
            return True
    return False

for index in range(len(dane)):
    if czy_kod(dane[index]):
        odp.write(f'{dane[index]}\n')

odp.close()
