with open('slowa.txt','r') as plik:
    dane = plik.readlines()

    for i in range(len(dane)):
        dane[i] = dane[i].rstrip()

odp = open('wynik5.txt','w')
odp.write(f'a)\n')

unikalne = []
ilosc = []

for napis in dane:
    n = len(napis)
    if 1<= n <=12:
        if n in unikalne:
            index = unikalne.index(n)
            ilosc[index] +=1
        else:
            unikalne.append(n)
            ilosc.append(1)

wynik = sorted(zip(unikalne,ilosc))
for jeden, dwa in wynik:
    odp.write(f'liczba: {jeden} ilosc {dwa}\n')

odp.write(f'b)\n')
