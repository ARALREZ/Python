	Instrukcja obsługi programu sortowanie_nowe.py:
1. Polecam program umieścić ze wszystkimi plikami w folderze (aby się nie pogubiły)
2. Konsola działa tylko z plikami .txt także, jeżeli Pan/Pani chciała wypróbować sortowanie musi umieścić to w pliku o takim rozszerzeniu

	Konsola zawiera:
1. Ograniczenia związane z generacją liczb, w obawie o przeciążenie starszych modeli komputerowych
2. Wszystkie dane będą zapisywane w plikach im odpowiadających



3. Konsola zawiera następujące algorytmy sortowania:
a) 	sortowanie_babelkowe_rosnace
   	sortowanie_babelkowe_malejace

b)	sortowanie_przez_wstawianie_rosnace
	sortowanie_przez_wstawianie_malejace

c)	sortowanie_scalanie_rosnace
	sortowanie_scalanie_malejace

d)	sortowanie_szybkie_rosnace
	sortowanie_szybkie_malejace

e)	sortowanie_kubelkowe_rosnace
	sortowanie_kubelkowe_malejace




Pliki co robią, co zawierają: UWAGA: NIE MOGA BYĆ TAKIE SAME PLIKI JAK PODANE - PANI/PANA MUSZA ZAWIERAC INNA NAZWE

przyklad.txt - (jeśli nie istnieje, zostanie utworzony automatycznie z 3 zestawami danych: 10, 50 i 100 losowych liczb z zakresu 1-10000)

wyniki.txt -  (jeśli nie istnieje, zostanie utworzony automatycznie) zawiera wyniki przeprowadzonych sortowań

ranking.txt -  (jeśli nie istnieje, zostanie utworzony automatycznie) zawiera ranking przeprowadzonych sortowań

(nazwa_pliku).txt - W kodzie będzie możliwość stworzenia własnego pliku z losowymi danymi, tylko będzie trzeba podać nazwę zakończoną na .txt




Opis konosoli:

1. WYBÓR PLIKU
- Opcja 1: wybierz plik 'przyklad.txt' (jeśli nie istnieje, zostanie utworzony automatycznie z 3 zestawami danych: 10, 50 i 100 losowych liczb z zakresu 1-10000).
- Opcja 2: podaj własną nazwę pliku kończącą się na .txt — liczby muszą być oddzielone SPACJĄ (inaczej błąd).
- Każdy zestaw poprzedzony indeksem (np. 1| ...). Nowy plik zaczyna od indeksu 1. Kolejne dodania zwiększają indeks.

2. WYŚWIETLANIE DANYCH
- Wyświetl nazwę pliku, liczbę wartości oraz liczby oddzielone TABULATOREM.

3. GENEROWANIE LICZB
- Możesz stworzyć nowy plik z liczbami (unikalna nazwa .txt), użytkownik podaje ile liczb i zakres (np. od 0 do X).
- Możesz też dodać dane do istniejącego pliku — wtedy zostaje dopisany nowy indeks i zestaw.

4. SORTOWANIE
- Uruchamia funkcję `wykonaj_sortowanie(nazwa_pliku)` — zaimplementowane algorytmy: mergeSort, quickSort, bucketSort, bubbleSort, insertSort.

5. DODANIE RĘCZNYCH LICZB
- Użytkownik wpisuje liczby oddzielone SPACJĄ (nie mogą zawierać przecinków, rurek, tabów).
- Dozwolone są tylko cyfry.

6. ZAPISYWANIE WYNIKÓW
- Wyniki zapisywane w pliku `wyniki.txt` w formie tabeli:
  index| iteracje| czas (ms)| algorytm| ilość liczb|

7. RANKING ALGORYTMÓW
- Tworzony na podstawie czasu działania algorytmu dla każdego zestawu danych osobno.

8. USUWANIE ZESTAWU DANYCH
- Wyświetla wszystkie indeksy (z nazwą pliku i ilością liczb), wybierasz, który usunąć.

9. USUWANIE WYNIKÓW I RANKINGÓW
- Czyści pliki `wyniki.txt` oraz `ranking.txt`.

0. ZAKOŃCZENIE PROGRAMU
- Każda opcja zawiera też `0` jako powrót do MENU głównego.


Życzę udanego korzystania z konsoli, mam nadzieję że będzie świetnie działać i spełni oczekiwania <3

