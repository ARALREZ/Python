plik_historia = "historia_dzialan.txt"


def potegowanie_rekurencyjne(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return potegowanie_rekurencyjne(a * a, b // 2)
    else:
        return a * potegowanie_rekurencyjne(a, b - 1)

def pierwiastek_kwadratowy(n):
    if n < 0:
        raise ValueError("Pierwiastek z liczby ujemnej")
    x = n
    y = (x + 1) / 2
    while abs(y - x) > 1e-10:
        x = y
        y = (x + n / x) / 2
    return y


def pokaz_menu():
    print("""
***************************************
Witamy w konsolowym kalkulatorze!
Jeżeli jestes nowy zapoznaj sie z podpunktami o numerach 4 i 5
***************************************
Wybierz:
1. Nowe obliczenie
2. Wyświetl historie obliczen
3. Wyczyść Historie obliczeń
4. Dostepne funkcje
5. Odpowiedni zapis działań i przykładowe dziłania
0. Zakoncz dzialanie kalkulatora
***************************************
""")

def zapisz_do_pliku(wyrazenie, wynik):
    with open(plik_historia, "a") as f:
        f.write(f"{wyrazenie} = {wynik}\n")

def wczytaj_historie():
    try:
        with open(plik_historia, "r") as f:
            return f.readlines()
    except:
        return []

def wyczysc_historie():
    open(plik_historia, "w").close()

def priorytet(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/', '%'):
        return 2
    elif op == '^':
        return 3
    return 0


def zmiana(wyrazenie):
    wyrazenie = wyrazenie.replace('[', '(').replace(']', ')')
    wynik = []
    liczba = ''
    i = 0
    while i < len(wyrazenie):
        znak = wyrazenie[i]
        if znak.isdigit() or (znak == '-' and (i == 0 or wyrazenie[i - 1] in '()+-*/%^')):
            liczba += znak
        elif znak in '+-*/%^()':
            if liczba:
                wynik.append(liczba)
                liczba = ''
            wynik.append(znak)
        elif wyrazenie[i:i+4] == 'sqrt':
            wynik.append('sqrt')
            i += 3
        else:
            raise ValueError(f"Błąd: Nieznany znak '{znak}'")
        i += 1
    if liczba:
        wynik.append(liczba)
    return wynik



def szereg(znaki):
    wynik = []
    stos = []
    for slop in znaki:
        if slop.lstrip('-').isdigit():
            wynik.append(slop)
        elif slop == 'sqrt':
            stos.append(slop)
        elif slop == '(':
            stos.append(slop)
        elif slop == ')':
            while stos and stos[-1] != '(':
                wynik.append(stos.pop())
            if stos and stos[-1] == '(':
                stos.pop()
            if stos and stos[-1] == 'sqrt':
                wynik.append(stos.pop())
        elif slop in '+-*/%^':
            while stos and priorytet(stos[-1]) >= priorytet(slop):
                wynik.append(stos.pop())
            stos.append(slop)
    while stos:
        wynik.append(stos.pop())
    return wynik

def oblicz_onp(onp):
    stos = []
    for slop in onp:
        try:
            stos.append(int(slop))
        except ValueError:
            if slop in '+-*/%^':
                if len(stos) < 2:
                    raise ValueError("Błąd: Za mało argumentów do operatora.")
                b = stos.pop()
                a = stos.pop()
                if slop == '+':
                    stos.append(a + b)
                elif slop == '-':
                    stos.append(a - b)
                elif slop == '*':
                    stos.append(a * b)
                elif slop == '/':
                    if b == 0:
                        raise ValueError("Błąd: Dzielenie przez zero.")
                    stos.append(a / b)
                elif slop == '%':
                    if b == 0:
                        raise ValueError("Błąd: Dzielenie modulo przez zero.")
                    stos.append(a % b)
                elif slop == '^':
                    stos.append(potegowanie_rekurencyjne(a, b))
            elif slop == 'sqrt':
                if not stos:
                    raise ValueError("Błąd: Brak argumentu dla funkcji sqrt.")
                liczba = stos.pop()
                stos.append(pierwiastek_kwadratowy(liczba))
            else:
                raise ValueError(f"Błąd: Nieznany symbol '{slop}'.")

    if len(stos) != 1:
        raise ValueError("Błąd: Nieprawidłowe wyrażenie.")

    return stos[0]



kontynuuj = True
while kontynuuj:
    pokaz_menu()
    wybor = input("Twoj wybor: ")
    if wybor == '1':
        wyrazenie = input("Wpisz wyrażenie (np. 7*1+sqrt(49)): ")
        if not wyrazenie.strip():
            continue
        try:
            zmiany = zmiana(wyrazenie)
            onp = szereg(zmiany)
            wynik = oblicz_onp(onp)
            print("Wynik:", wynik)
            zapisz_do_pliku(wyrazenie, wynik)
        except Exception as problem:
            print("Błąd w obliczeniach:", problem)
    elif wybor == '2':
        historia = wczytaj_historie()
        if not historia:
            print("Brak historii.")
        else:
            for i in range(len(historia)):
                print(f"{i + 1}. {historia[i].strip()}")
            wybor_hist = input("Wybierz numer, aby wczytac wyrazenie lub 0, aby wrocic: ")
            if wybor_hist.isdigit():
                numer = int(wybor_hist)
                if numer > 0 and numer <= len(historia):
                    wyrazenie_wybrane = historia[numer-1].split('=')[0].strip()
                    print("Wybrane wyrażenie:", wyrazenie_wybrane)
                    edytowane = input("Edytuj wyrażenie (lub pozostaw bez zmian): [" + wyrazenie_wybrane + "] >> ")
                    if not edytowane.strip():
                        edytowane = wyrazenie_wybrane
                    try:
                        zmiany = zmiana(edytowane)
                        onp = szereg(zmiany)
                        wynik = oblicz_onp(onp)
                        print("Wynik:", wynik)
                        zapisz_do_pliku(edytowane, wynik)
                    except Exception as problem:
                        print("Błąd w obliczeniach:", problem)
    elif wybor == '3':
        wyczysc_historie()
        print("Historia wyczyszczona.")
    elif wybor == '4':
        print("Dostępne operacje: + - * / % ^ sqrt(liczba), nawiasy ( ) i liczby całkowite.\n"
              " +  -->   dodawanie\n"
              " -  -->  odejmowanie\n"
              " *  -->   mnożenie\n"
              " /  -->   dzielenie\n"
              " %  -->   reszta z dzielenia\n"
              " sqrt() --> pierwiastek kwadratowy z liczby umieszczonej w ()\n"
              " PRZYKŁADOWE ZAPISY ZNAJDZIESZ W PODPUNKCIE 5"
              )
    elif wybor == '5':
        print("Przykłady dostępnych funkcji i złożonych działań:")
        print("Dodawanie: 2+3")
        print("Odejmowanie: 5-2")
        print("Mnożenie: 4*3")
        print("Dzielenie: 10/2")
        print("Reszta z dzielenia: 10%3")
        print("Potęgowanie: 2^5")
        print("Pierwiastek kwadratowy: sqrt(49)")
        print("Złożone działanie z nawiasami: 4*(2+3)^2 - sqrt(16)")
        print("Ujemne liczby: -5 + 3 * (-2)")
    elif wybor == '0':
        print("Zakończono działanie kalkulatora. Do zobaczenia!")
        kontynuuj = False
    else:
        print("Nieprawidłowy wybór.")
