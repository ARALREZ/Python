PLIK = "baza_filmow.txt"

def wczytaj_dane():
    dane = []
    try:
        with open(PLIK, "r") as f:
            for linia in f:
                if linia.strip():
                    czesci = linia.strip().split("|")
                    dane.append({
                        "id": czesci[0],
                        "imie": czesci[1],
                        "nazwisko": czesci[2],
                        "wiek": czesci[3],
                        "filmy": czesci[4].split(",") if czesci[4] else []
                    })
    except FileNotFoundError:
        pass
    return dane

def zapisz_dane(dane):
    with open(PLIK, "w") as f:
        for osoba in dane:
            f.write(f"{osoba['id']}|{osoba['imie']}|{osoba['nazwisko']}|{osoba['wiek']}|{','.join(osoba['filmy'])}\n")

def pokaz_menu():
    print("""
***************************************
Witamy w systemie FilmoManiak!
***************************************
1. Pokaż listę osób
2. Dodaj osobę
3. Edytuj osobę
4. Usuń osobę
5. Pokaż liczbę osób
6. Pokaż najpopularniejszy film
0. Zakończ
""")

def pokaz_osoby(dane):
    if not dane:
        print("Brak osób w bazie.")
    for osoba in dane:
        print(f"{osoba['id']}. {osoba['imie']} {osoba['nazwisko']}, wiek: {osoba['wiek']}, filmy: {', '.join(osoba['filmy'])}")

def dodaj_osobe(dane):
    if dane:
        nowe_id = str(max([int(o["id"]) for o in dane]) + 1)
    else:
        nowe_id = "1"
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    wiek = input("Wiek: ")
    filmy = input("Ulubione filmy (oddzielone przecinkami): ").split(",")
    dane.append({
        "id": nowe_id,
        "imie": imie,
        "nazwisko": nazwisko,
        "wiek": wiek,
        "filmy": [f.strip() for f in filmy]
    })
    zapisz_dane(dane)
    print("Osoba dodana.")


def edytuj_osobe(dane):
    id_edytuj = input("Podaj ID osoby do edycji: ")
    for osoba in dane:
        if osoba["id"] == id_edytuj:
            print(f"Edytujesz {osoba['imie']} {osoba['nazwisko']}")
            imie = input(f"Nowe imię ({osoba['imie']}): ")
            nazwisko = input(f"Nowe nazwisko ({osoba['nazwisko']}): ")
            wiek = input(f"Nowy wiek ({osoba['wiek']}): ")
            filmy = input(f"Nowe filmy (oddzielone przecinkami) ({', '.join(osoba['filmy'])}): ")
            if imie: osoba["imie"] = imie
            if nazwisko: osoba["nazwisko"] = nazwisko
            if wiek: osoba["wiek"] = wiek
            if filmy.strip(): osoba["filmy"] = [f.strip() for f in filmy.split(",")]
            zapisz_dane(dane)
            print("Zaktualizowano dane.")
            return
    print("Nie znaleziono osoby!!!")

def usun_osobe(dane):
    id_usun = input("Podaj ID osoby do usunięcia: ")
    nowa_lista = []
    znaleziono = False
    for osoba in dane:
        if osoba["id"] != id_usun:
            nowa_lista.append(osoba)
        else:
            znaleziono = True
    if znaleziono:
        zapisz_dane(nowa_lista)
        print("Osoba usunięta.")
        return nowa_lista
    else:
        print("Nie znaleziono osoby!!!")
        return dane

def liczba_osob(dane):
    print(f"Liczba osób: {len(dane)}")

def najpopularniejszy_film(dane):
    licznik = {}
    for osoba in dane:
        for film in osoba["filmy"]:
            film = film.strip()
            if film:
                if film not in licznik:
                    licznik[film] = 1
                else:
                    licznik[film] += 1
    if not licznik:
        print("Brak filmów w bazie.")
        return
    najfilm = ""
    najliczba = 0
    for film in licznik:
        if licznik[film] > najliczba:
            najliczba = licznik[film]
            najfilm = film
    print(f"Najpopularniejszy film: {najfilm} ({najliczba}x)")

dane = wczytaj_dane()
while True:
    pokaz_menu()
    wybor = input("Twój wybór: ")
    if wybor == "1":
        pokaz_osoby(dane)
    elif wybor == "2":
        dodaj_osobe(dane)
    elif wybor == "3":
        edytuj_osobe(dane)
    elif wybor == "4":
        dane = usun_osobe(dane)
    elif wybor == "5":
        liczba_osob(dane)
    elif wybor == "6":
        najpopularniejszy_film(dane)
    elif wybor == "0":
        print("Do zobaczenia!<3")
        break
    else:
        print("!!!Nieprawidłowy wybór!!!")
