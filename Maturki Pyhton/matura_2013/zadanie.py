with open('napisy.txt','r') as plik:
    dane = plik.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()


odp = open('zadanie4.txt', 'w')

# a) Podaj, ile jest napisów o parzystej długości
odp.write('a)\n')

def ile_parzystych(zmienna):
    parzyste = 0
    for napis in zmienna:
        if len(napis) % 2 == 0:  # Sprawdzanie długości napisu
            parzyste += 1
    return parzyste

ile = ile_parzystych(dane)
odp.write(f'{ile}\n')

# b) Podaj, ile jest liczb, które mają tyle samo zer i jedynek
odp.write('b)\n')

def zera_jedynki(zmienna):
    ile_liczb = 0
    for liczba in zmienna:
        zera = liczba.count('0')  # Liczenie zer
        jedynki = liczba.count('1')  # Liczenie jedynek
        if zera == jedynki:
            ile_liczb += 1
    return ile_liczb

ile = zera_jedynki(dane)
odp.write(f'{ile}\n')

# c) Podaj, ile jest napisów, które składają się wyłącznie z samych zer lub samych jedynek
odp.write('c)\n')

def czy_same(zmienna):
    zera = 0
    jedynki = 0
    for liczba in zmienna:
        if liczba.count('0') == len(liczba):  # Wszystkie znaki to '0'
            zera += 1
        if liczba.count('1') == len(liczba):  # Wszystkie znaki to '1'
            jedynki += 1
    return jedynki, zera

jeden, zero = czy_same(dane)
odp.write(f'Liczba napisów z samymi 0: {zero}\n')
odp.write(f'Liczba napisów z samymi 1: {jeden}\n')

odp.write('d)\n')

unikalne_k = []
ile = []


for napis in dane:
    k = len(napis)
    if 2 <= k <= 16:
        if k in unikalne_k:
            index = unikalne_k.index(k)
            ile[index] += 1
        else:
            unikalne_k.append(k)
            ile.append(1)

wyniki = sorted(zip(unikalne_k, ile))
print(wyniki)

for k, liczba in wyniki:
    odp.write(f" wyrazy: {k} jest: {liczba}\n")

odp.close()







