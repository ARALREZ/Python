import random
import time

PLIK_DANE = "przyklad.txt"
PLIK_WYNIKI = "wyniki.txt"
PLIK_RANKING = "ranking.txt"


def utworz_puste_pliki():
    for nazwa in ["wyniki.txt", "ranking.txt"]:
        try:
            open(nazwa, "w").close()
        except Exception as e:
            print(f"Błąd przy tworzeniu pliku '{nazwa}': {e}")


def inicjalizuj_przykladowy_plik():
    utworz_puste_pliki()
    istnieje = False
    try:
        with open(PLIK_DANE, "r"):
            istnieje = True
    except:
        pass
    if not istnieje:
        try:
            with open(PLIK_DANE, 'w') as f:
                domyslne_rozmiary = [10, 50, 100]
                i = 1
                for ilosc in domyslne_rozmiary:
                    liczby = [str(random.randint(1, 10000)) for _ in range(ilosc)]
                    f.write(f"{i}|{' '.join(liczby)}\n")
                    i += 1
            print("Utworzono plik 'przyklad.txt' z 3 zestawami testowymi.")
        except Exception as e:
            print(f"Błąd podczas tworzenia pliku 'przyklad.txt': {e}")


inicjalizuj_przykladowy_plik()


def sortowanie_babelkowe_rosnace(tablica):
    iteracje = 0
    n = len(tablica)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            iteracje += 1
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    return iteracje


def sortowanie_babelkowe_malejace(tablica):
    iteracje = 0
    n = len(tablica)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            iteracje += 1
            if tablica[j] < tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    return iteracje


def sortowanie_przez_wstawianie_rosnace(tablica):
    iteracje = 0
    for i in range(1, len(tablica)):
        klucz = tablica[i]
        j = i - 1
        iteracje += 1
        while j >= 0 and tablica[j] > klucz:
            tablica[j + 1] = tablica[j]
            j -= 1
            iteracje += 1
        tablica[j + 1] = klucz
    return iteracje


def sortowanie_przez_wstawianie_malejace(tablica):
    iteracje = 0
    for i in range(1, len(tablica)):
        klucz = tablica[i]
        j = i - 1
        iteracje += 1
        while j >= 0 and tablica[j] < klucz:
            tablica[j + 1] = tablica[j]
            j -= 1
            iteracje += 1
        tablica[j + 1] = klucz
    return iteracje


def sortowanie_scalanie_rosnace(tablica):
    iteracje = [0]

    def scalanie(lewa, prawa):
        wynik = []
        i = j = 0
        while i < len(lewa) and j < len(prawa):
            iteracje[0] += 1
            if lewa[i] <= prawa[j]:
                wynik.append(lewa[i]);
                i += 1
            else:
                wynik.append(prawa[j]);
                j += 1
        return wynik + lewa[i:] + prawa[j:]

    def sortuj(lista):
        if len(lista) <= 1:
            return lista
        s = len(lista) // 2
        return scalanie(sortuj(lista[:s]), sortuj(lista[s:]))

    pos = sortuj(tablica)
    for i in range(len(tablica)):
        tablica[i] = pos[i]
    return iteracje[0]


def sortowanie_scalanie_malejace(tablica):
    iteracje = [0]

    def scalanie(lewa, prawa):
        wynik = []
        i = j = 0
        while i < len(lewa) and j < len(prawa):
            iteracje[0] += 1
            if lewa[i] >= prawa[j]:
                wynik.append(lewa[i]);
                i += 1
            else:
                wynik.append(prawa[j]);
                j += 1
        return wynik + lewa[i:] + prawa[j:]

    def sortuj(lista):
        if len(lista) <= 1:
            return lista
        s = len(lista) // 2
        return scalanie(sortuj(lista[:s]), sortuj(lista[s:]))

    pos = sortuj(tablica)
    for i in range(len(tablica)):
        tablica[i] = pos[i]
    return iteracje[0]


def sortowanie_szybkie_rosnace(tablica):
    iteracje = [0]

    def quicksort(lewy, prawy):
        if lewy < prawy:
            pi = podzial(lewy, prawy)
            quicksort(lewy, pi - 1)
            quicksort(pi + 1, prawy)

    def podzial(lewy, prawy):
        pivot = tablica[prawy]
        i = lewy - 1
        for j in range(lewy, prawy):
            iteracje[0] += 1
            if tablica[j] <= pivot:
                i += 1
                tablica[i], tablica[j] = tablica[j], tablica[i]
        tablica[i + 1], tablica[prawy] = tablica[prawy], tablica[i + 1]
        return i + 1

    quicksort(0, len(tablica) - 1)
    return iteracje[0]


def sortowanie_szybkie_malejace(tablica):
    iteracje = [0]

    def quicksort(lewy, prawy):
        if lewy < prawy:
            pi = podzial(lewy, prawy)
            quicksort(lewy, pi - 1)
            quicksort(pi + 1, prawy)

    def podzial(lewy, prawy):
        pivot = tablica[prawy]
        i = lewy - 1
        for j in range(lewy, prawy):
            iteracje[0] += 1
            if tablica[j] >= pivot:
                i += 1
                tablica[i], tablica[j] = tablica[j], tablica[i]
        tablica[i + 1], tablica[prawy] = tablica[prawy], tablica[i + 1]
        return i + 1

    quicksort(0, len(tablica) - 1)
    return iteracje[0]


def sortowanie_kubelkowe_rosnace(tablica):
    iteracje = 0
    n = len(tablica)
    if n == 0:
        return iteracje
    maks = max(tablica)
    liczba_kubelkow = 10
    rozmiar = (maks + 1) // liczba_kubelkow + 1
    kubelki = [[] for _ in range(liczba_kubelkow)]
    for liczba in tablica:
        iteracje += 1
        idx = min(liczba // rozmiar, liczba_kubelkow - 1)
        kubelki[idx].append(liczba)
    i = 0
    for kubel in kubelki:
        for j in range(1, len(kubel)):
            klucz = kubel[j]
            k = j - 1
            iteracje += 1
            while k >= 0 and kubel[k] > klucz:
                kubel[k + 1] = kubel[k]
                k -= 1
                iteracje += 1
            kubel[k + 1] = klucz
        for liczba in kubel:
            iteracje += 1
            tablica[i] = liczba
            i += 1
    return iteracje


def sortowanie_kubelkowe_malejace(tablica):
    iteracje = 0
    n = len(tablica)
    if n == 0:
        return iteracje
    maks = max(tablica)
    liczba_kubelkow = 10
    rozmiar = (maks + 1) // liczba_kubelkow + 1
    kubelki = [[] for _ in range(liczba_kubelkow)]
    for liczba in tablica:
        iteracje += 1
        idx = min(liczba // rozmiar, liczba_kubelkow - 1)
        kubelki[idx].append(liczba)
    i = 0
    for kubel in kubelki:
        for j in range(1, len(kubel)):
            klucz = kubel[j]
            k = j - 1
            iteracje += 1
            while k >= 0 and kubel[k] < klucz:
                kubel[k + 1] = kubel[k]
                k -= 1
                iteracje += 1
            kubel[k + 1] = klucz
        for liczba in reversed(kubel):
            iteracje += 1
            tablica[i] = liczba
            i += 1
    return iteracje


def plik_istnieje(nazwa):
    try:
        with open(nazwa, 'r'):
            return True
    except:
        return False


def dodaj_liczby(nazwa_pliku):
    try:
        wejscie = input("Podaj liczby oddzielone spacją: ").strip()

        if not wejscie:
            print("Nie podano danych.")
            return

        for c in wejscie:
            if not (c.isdigit() or c == ' '):
                print("Błąd: liczby muszą być całkowite i oddzielone wyłącznie spacją.")
                return

        liczby = wejscie.split()
        for l in liczby:
            if not l.isdigit():
                print("Błąd: Dozwolone są tylko liczby całkowite oddzielone spacją.")
                return

        with open(nazwa_pliku, 'r') as f:
            indeks = 0
            for _ in f:
                indeks += 1
            indeks += 1

        with open(nazwa_pliku, 'a') as f:
            f.write(f"{indeks}|{' '.join(liczby)}\n")
        print(f"Dodano dane jako zestaw {indeks}.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")


def wykonaj_sortowanie(nazwa_pliku):
    algorytmy = {
        '1': ("Bąbelkowe rosnąco", sortowanie_babelkowe_rosnace),
        '2': ("Bąbelkowe malejąco", sortowanie_babelkowe_malejace),
        '3': ("Wstawianie rosnąco", sortowanie_przez_wstawianie_rosnace),
        '4': ("Wstawianie malejąco", sortowanie_przez_wstawianie_malejace),
        '5': ("Scalanie rosnąco", sortowanie_scalanie_rosnace),
        '6': ("Scalanie malejąco", sortowanie_scalanie_malejace),
        '7': ("Szybkie rosnąco", sortowanie_szybkie_rosnace),
        '8': ("Szybkie malejąco", sortowanie_szybkie_malejace),
        '9': ("Kubełkowe rosnąco", sortowanie_kubelkowe_rosnace),
        '10': ("Kubełkowe malejąco", sortowanie_kubelkowe_malejace),
    }

    print("\nDostępne algorytmy:")
    for klucz in algorytmy:
        nazwa = algorytmy[klucz][0]
        print(f"{klucz}. {nazwa}")

    wybor = input("Wybierz algorytm: ")
    if wybor not in algorytmy:
        print("Błędny wybór.")
        return

    nazwa_algorytmu, funkcja_sortowania = algorytmy[wybor]
    dane = []

    try:
        with open(nazwa_pliku, 'r') as f:
            linie = []
            for l in f:
                linia = l.strip()
                if linia:
                    linie.append(linia)

        poprawione_linie = []
        for i in range(len(linie)):
            if '|' not in linie[i]:
                poprawione_linie.append(f"{i + 1}|{linie[i]}")
            else:
                poprawione_linie.append(linie[i])

        if len(poprawione_linie) != len(linie):
            with open(nazwa_pliku, 'w') as f:
                for linia in poprawione_linie:
                    f.write(linia + '\n')
            print("Poprawiono format pliku - dodano brakujące indeksy i separatory.")

        for linia in poprawione_linie:
            czesci = linia.split('|')
            if len(czesci) >= 2:
                indeks, liczby_str = czesci[0], '|'.join(czesci[1:])
                try:
                    liczby = []
                    for num in liczby_str.strip().split():
                        liczby.append(int(num))
                    dane.append((indeks, liczby))
                except ValueError:
                    print(f"Błąd konwersji liczb w linii: {linia}")
    except Exception as e:
        print(f"Błąd odczytu danych: {e}")
        return

    if not dane:
        print("Brak danych do sortowania.")
        return

    dodaj_naglowek_wyniki = True
    try:
        with open(PLIK_WYNIKI, 'r') as f:
            if f.read(1):
                dodaj_naglowek_wyniki = False
    except:
        pass

    dodaj_naglowek_ranking = True
    try:
        with open(PLIK_RANKING, 'r') as f:
            if f.read(1):
                dodaj_naglowek_ranking = False
    except:
        pass

    with open(PLIK_WYNIKI, 'a') as wyniki:
        if dodaj_naglowek_wyniki:
            wyniki.write("Indeks|Iteracje|Czas (ms)|Algorytm|Ilość liczb\n")

        for indeks, liczby in dane:
            kopia = liczby[:]
            start = time.time()
            iteracje = funkcja_sortowania(kopia)
            czas_ms = (time.time() - start) * 1000

            wynik = f"{indeks}|{iteracje}|{czas_ms:.3f}|{nazwa_algorytmu}|{len(liczby)}\n"
            wyniki.write(wynik)
            print(
                f"Zestaw {indeks} - {nazwa_algorytmu}: {iteracje} iteracji, {czas_ms:.3f} ms (ilość liczb: {len(liczby)})")


def ranking_sortowan():
    try:
        if not plik_istnieje(PLIK_WYNIKI):
            print("Brak pliku wyników.")
            return

        with open(PLIK_WYNIKI, 'r') as f:
            linie = []
            for l in f:
                linia = l.strip()
                if linia:
                    linie.append(linia)

        if not linie or linie[0].startswith("Indeks"):
            linie = linie[1:]

        ranking = {}

        for linia in linie:
            try:
                czesci = linia.split('|')
                if len(czesci) == 5:
                    indeks, iteracje, czas, algorytm, ilosc = czesci
                    czas = float(czas)
                    iteracje = int(iteracje)
                    ilosc = int(ilosc)
                    if indeks not in ranking:
                        ranking[indeks] = []
                    ranking[indeks].append((algorytm, czas, iteracje, ilosc))
            except:
                continue

        if not ranking:
            print("Brak danych do utworzenia rankingu.")
            return

        for indeks in sorted(ranking, key=lambda x: int(x)):
            print(f"\n=== RANKING ZESTAWU {indeks} ===")
            print(f"{'Lp.':<4}{'Algorytm':<25}{'Czas (ms)':<12}{'Iteracje':<10}{'Ilość liczb'}")
            nr = 1
            for alg, czas, it, ilosc in sorted(ranking[indeks], key=lambda x: x[1]):
                print(f"{nr:<4}{alg:<25}{czas:<12.3f}{it:<10}{ilosc}")
                nr += 1

        print(f"\nRanking został wygenerowany na podstawie pliku: {PLIK_WYNIKI}")
    except Exception as e:
        print(f"Błąd przy generowaniu rankingu: {e}")


def wyswietl_zawartosc(nazwa_pliku):
    if not plik_istnieje(nazwa_pliku):
        print("Plik nie istnieje.")
        return
    try:
        with open(nazwa_pliku, 'r') as f:
            zawartosc = f.read().strip()

        if not zawartosc:
            print("Plik jest pusty.")
            return

        print(f"\nZawartość pliku: {nazwa_pliku}")
        print("Indeks\tIlość liczb\tLiczby")
        print("=" * 50)

        linie = zawartosc.split('\n')
        for linia in linie:
            if '|' in linia:
                indeks, liczby = linia.split('|', 1)
                liczby_lista = liczby.strip().split()
                print(f"{indeks}\t{len(liczby_lista)}\t\t{liczby}")
            else:
                print(f"Błędny format linii: {linia}")

    except Exception as e:
        print(f"Błąd odczytu pliku: {e}")


def wybierz_plik():
    print("\nDostępne opcje:")
    print(f"1. {PLIK_DANE}")
    print("2. Własny plik")
    wybor = input("Wybierz opcję (1, 2 lub 0 aby wrócić): ").strip()
    if wybor == '0':
        return None
    if wybor == '1':
        return PLIK_DANE
    elif wybor == '2':
        nazwa = input("Podaj nazwę pliku .txt: ").strip()
        if not nazwa.endswith(".txt"):
            print("Plik musi kończyć się na .txt")
            return None
        if not plik_istnieje(nazwa):
            print("Plik nie istnieje!")
            return None

        try:
            with open(nazwa, 'r') as f:
                linie = []
                for l in f:
                    linia = l.strip()
                    if linia:
                        linie.append(linia)

            poprawione_linie = []
            zmieniono = False
            for i in range(len(linie)):
                if '|' not in linie[i]:
                    poprawione_linie.append(f"{i + 1}|{linie[i]}")
                    zmieniono = True
                else:
                    poprawione_linie.append(linie[i])

            if zmieniono:
                with open(nazwa, 'w') as f:
                    for linia in poprawione_linie:
                        f.write(linia + '\n')
                print("Poprawiono format pliku - dodano brakujące indeksy i separatory.")
        except Exception as e:
            print(f"Błąd podczas sprawdzania pliku: {e}")
            return None

        return nazwa
    else:
        print("Nieprawidłowy wybór.")
        return None


def generuj_nowe_dane():
    print("\n1. Stwórz nowy plik")
    print("2. Dodaj do istniejącego pliku")
    wybor = input("Wybierz opcję (1, 2 lub 0 aby wrócić): ").strip()

    if wybor == '0':
        return None

    try:
        if wybor == '1':
            nazwa = input("Podaj nową nazwę pliku .txt: ").strip()
            if not nazwa.endswith(".txt"):
                print("Plik musi mieć rozszerzenie .txt!")
                return None

            if nazwa in [PLIK_DANE, PLIK_WYNIKI, PLIK_RANKING] or plik_istnieje(nazwa):
                print("Taka nazwa pliku już istnieje lub jest zarezerwowana!")
                return None

            ile = int(input("Ile liczb wygenerować? min. 2 max. 10000: "))
            maks = int(input("Podaj maksymalny zakres min. 10 max. 1000000 "))
            if (ile < 2 or ile > 10000) or (maks < 10 or maks > 1000000):
                print("Podano niedozwolone liczby!")
                return None

            liczby = [str(random.randint(1, maks)) for _ in range(ile)]
            with open(nazwa, 'w') as f:
                f.write(f"1|{' '.join(liczby)}\n")
            print(f"Utworzono plik {nazwa} z zestawem 1.")
            return nazwa

        elif wybor == '2':
            nazwa = input("Podaj nazwę istniejącego pliku .txt: ").strip()
            if not nazwa.endswith(".txt") or not plik_istnieje(nazwa):
                print("Plik nie istnieje lub ma nieprawidłowe rozszerzenie!")
                return None

            ile = int(input("Ile liczb wygenerować? min. 2 max. 10000: "))
            maks = int(input("Podaj maksymalny zakres min. 10 max. 1000000 "))
            if (ile < 2 or ile > 10000) or (maks < 10 or maks > 1000000):
                print("Podano niedozwolone liczby!")
                return None

            liczby = [str(random.randint(1, maks)) for _ in range(ile)]
            with open(nazwa, 'r') as f:
                linie = []
                for l in f:
                    linie.append(l)
                nowy_index = len(linie) + 1
            with open(nazwa, 'a') as f:
                f.write(f"{nowy_index}|{' '.join(liczby)}\n")
            print(f"Dodano zestaw {nowy_index} do pliku {nazwa}.")
            return nazwa

        else:
            print("Nieprawidłowy wybór.")
            return None

    except ValueError:
        print("Podano nieprawidłową wartość!")
    except Exception as e:
        print(f"Błąd: {e}")
    return None


def usun_zestaw():
    print("\nWybierz plik z którego usunąć zestaw:")
    print(f"1. {PLIK_DANE}")
    print("2. Własny plik")
    print("0. Powrót")
    wybor = input("Wybierz plik (1, 2 lub 0): ").strip()

    if wybor == '0':
        return

    if wybor == '1':
        nazwa = PLIK_DANE
    elif wybor == '2':
        nazwa = input("Podaj nazwę istniejącego pliku .txt (lub 0 aby wrócić): ").strip()
        if nazwa == '0':
            return
        if not plik_istnieje(nazwa):
            print("Plik nie istnieje.")
            return
    else:
        print("Nieprawidłowy wybór.")
        return

    try:
        with open(nazwa, 'r') as f:
            linie = []
            for l in f:
                linia = l.strip()
                if linia:
                    linie.append(linia)

        if not linie:
            print("Plik jest pusty.")
            return

        print(f"\nZawartość pliku: {nazwa}")
        for l in linie:
            if '|' in l:
                indeks, liczby = l.split('|', 1)
                ilosc = len(liczby.strip().split())
                print(f"Indeks: {indeks}\tIlość liczb: {ilosc}")
            else:
                print(f"Błędny format linii: {l}")

        indeks_do_usuniecia = input("Podaj indeks do usunięcia (lub 0 aby wrócić): ").strip()
        if indeks_do_usuniecia == '0':
            return

        nowe = []
        for l in linie:
            if not l.startswith(f"{indeks_do_usuniecia}|"):
                nowe.append(l)
        if len(nowe) == len(linie):
            print("Nie znaleziono takiego indeksu.")
            return

        with open(nazwa, 'w') as f:
            for l in nowe:
                f.write(l + '\n')
        print(f"Zestaw {indeks_do_usuniecia} został usunięty z pliku {nazwa}.")
    except Exception as e:
        print(f"Błąd podczas usuwania: {e}")


def usun_wyniki():
    print("\n=== USUWANIE ===")
    print("1. Usuń wyniki")
    print("2. Usuń ranking")
    print("0. Powrót")
    wybor = input("Wybierz opcję: ").strip()
    if wybor == '0':
        return
    elif wybor == '1':
        open(PLIK_WYNIKI, 'w').close()
        print("Wyniki zostały wyczyszczone.")
    elif wybor == '2':
        open(PLIK_RANKING, 'w').close()
        print("Ranking został wyczyszczony.")
    else:
        print("Nieprawidłowy wybór.")


def wyswietl_menu_glowne():
    print("\n=== MENU GŁÓWNE ===")
    print("1. Wybór pliku danych")
    print("2. Wyświetl wybrany plik")
    print("3. Generuj nowe dane")
    print("4. Sortowanie")
    print("5. Dodaj liczby do zestawu")
    print("6. Wyświetl wyniki")
    print("7. Ranking sortowań")
    print("8. Usuń zestaw danych")
    print("9. Usuń ranking/wyniki")
    print("0. Zakończ program")
    return input("Wybierz opcję: ").strip()


wybrany_plik = None

try:
    while True:
        opcja = wyswietl_menu_glowne()
        if opcja == '1':
            wybrany_plik = wybierz_plik()
        elif opcja == '2':
            if wybrany_plik:
                wyswietl_zawartosc(wybrany_plik)
            else:
                print("Najpierw wybierz plik!")
        elif opcja == '3':
            nowy = generuj_nowe_dane()
            if nowy:
                wybrany_plik = nowy
        elif opcja == '4':
            if wybrany_plik:
                wykonaj_sortowanie(wybrany_plik)
            else:
                print("Najpierw wybierz plik!")
        elif opcja == '5':
            if wybrany_plik:
                dodaj_liczby(wybrany_plik)
            else:
                print("Najpierw wybierz plik!")
        elif opcja == '6':
            if not plik_istnieje(PLIK_WYNIKI):
                print("Brak pliku wyników.")
            else:
                with open(PLIK_WYNIKI, "r") as f:
                    linie = []
                    for l in f:
                        linia = l.strip()
                        if linia:
                            linie.append(linia)
                if not linie:
                    print("Plik wyników jest pusty.")
                else:
                    ostatni_algorytm = ""
                    for linia in linie:
                        dane = linia.split("|")
                        if len(dane) == 5:
                            indeks, iteracje, czas, algorytm, ilosc = dane
                            if algorytm != ostatni_algorytm:
                                if ostatni_algorytm != "":
                                    print()
                                ostatni_algorytm = algorytm
                            print(f"{indeks}\t{iteracje}\t\t{czas} ms\t{algorytm:<20}\t{ilosc}")
                        else:
                            print("Błędna linia:", linia)
        elif opcja == '7':
            ranking_sortowan()
        elif opcja == '8':
            usun_zestaw()
        elif opcja == '9':
            usun_wyniki()
        elif opcja == '0':
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór.")
except KeyboardInterrupt:
    print("\nPrzerwano działanie programu.")
except Exception as e:
    print(f"Wystąpił błąd: {e}")