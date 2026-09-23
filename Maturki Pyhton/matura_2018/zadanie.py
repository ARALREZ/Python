with open('liczby.txt','r')as plik:
    dane = plik.readlines()

    for i in range(len(dane)):
        dane[i] = int(dane[i].rstrip())

odp = open('wyniki5.txt','w')
odp.write(f'a)\n')

max = 0
for i in range(len(dane)):
    if dane[i] % 2 == 0 and dane[i] > max:
        max = dane[i]

odp.write(f'{max}\n')


odp.close()