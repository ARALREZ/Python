with open('cyfry.txt') as plik:
    dane = plik.readlines()
    for a in range(len(dane)):
        dane[a] =dane[a].rstrip()

odp = open('zadanie4.txt','w')
odp.write('a)\n')

def ile_parzystych(zmienna):
    parzyste = 0
    for i in range(len(zmienna)):
        if int(zmienna[i]) % 2 == 0:
            parzyste+=1
    return parzyste

liczba = ile_parzystych(dane)
odp.write(f'{liczba}\n')

odp.write('b)\n')

def najwieksza_najmniejsza(zmienna):
    max = 0
    min = 99999999999999999999
    liczba_max = 0
    liczba_min = 0
    for i in range(len(zmienna)):
        liczba = int(zmienna[i])
        suma = 0
        while liczba > 0:
            cyfra = liczba % 10
            suma +=cyfra
            liczba = liczba //10

        if suma > max:
            max = suma
            liczba_max = zmienna[i]
        if suma < min:
            min = suma
            liczba_min = zmienna[i]

    return liczba_max,liczba_min


maxymalna , minimalna = najwieksza_najmniejsza(dane)

odp.write(f'Liczba z najwieksza suma cyfr: {maxymalna}\n')
odp.write(f'Liczba z najmniejsza suma cyfr: {minimalna}\n')

odp.write('c)\n')

def czy_rosnacy(zmienna):
    for j in range(len(zmienna)-1):
        if int(zmienna[j]) >= int(zmienna[j+1]):
            return False
    return True


for i in range(len(dane)):
    if czy_rosnacy(dane[i]):
        odp.write(f'{dane[i]}\n')

odp.close()







