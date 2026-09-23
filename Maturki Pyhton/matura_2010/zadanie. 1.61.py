with open ('dane.txt') as plik:
    dane = plik.readlines()
    for i in range(len(dane)):
        dane[i]= dane[i].rstrip()

odp = open('zadanie4.txt','w')
odp.write('Palindromy:\n\n')

#palindromy
def czy_palindrom(zmienna):
    if zmienna == zmienna[::-1]:
        return True
    return False

for i in range(len(dane)):
    if czy_palindrom(dane[i]):
        znak = dane[i]
        odp.write(f'{znak}\n')

odp.close()