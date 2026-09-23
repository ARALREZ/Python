with open('slowa.txt','r') as plik:
    dane = plik.readlines()

    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()

odp = open('wynik5.txt','w')
odp.write(f'a)\n')