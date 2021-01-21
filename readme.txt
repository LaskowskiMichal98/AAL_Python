Autorzy:
Paweł Lech, 276445
Michał Laskowski, 295804


Specyfikacja problemu:
Zadanie 10 - czołg steampunkowy
Jesteś żołnierzem na polu bitwy. To zapewne przykra wiadomość, ale to dopiero początek. Otóż bitwa dzieje się w rzeczywistości alternatywnej, w świecie steampunk, a wokół ciebie walczą olbrzymie machiny wojenne, napędzane parą i kierowane nie przez ludzi a przez maszyny różnicowe :-). Ty masz już dość i chcesz uciec jak najdalej. Na szczęście udało Ci się dostać do środka jednej z machin wojennych - na razie jesteś bezpieczny, ale trzeba uciekać!


Informacje o programie:
main.py - główny plik uruchomieniowy programu
Card.py - klasa Card odpowiada jednemu wektorowi z pliku wejściowego
Data.py - klasa Data stanowi kontener przechowujący karty
Menu.py - klasa Menu pozwala na wyświetlanie użytkownikowi tekstowego interfejsu
Generator.py - dwie funkcje zawarte w pliku umożliwiają generowanie wybranej liczby kart do pliku lub do listy
Algorithm.py - klasa Algorithm odpowiada za wykorzystanie opisanego przez nas algorytmu do znalezienie poszukiwanego rozwiązania

Możliwe tryby uruchomienia programu:
1. python main.py -m : uruchomienie programu z prostym menu tekstowym.
2. python main.py -c [nazwa_pliku.txt] [liczba_kart] : wygenerowanie [liczba_kart] kart z danymi do pliku [nazwa_pliku].
3. python main.py -s [nazwa_pliku.txt] : wyświetlenie zawartości pliku [nazwa_pliku].
4. python main.py -r [nazwa_pliku.txt] : uruchomienie algorytmu dla danych z pliku [nazwa_pliku] oraz wyświetlenie wyniku.
5. python main.py -e [nazwa_pliku.xlsx] [liczba_uruchomien] : uruchomienie algorytmu [liczba_uruchomien] razy dla losowych zestawów danych i zapisanie wyników do pliku .xlsx.
6. python main.py -t [nazwa_pliku.xlsx] [liczba_uruchomien] [wielkosc_skoku] : uruchomienie algorytmu [liczba_uruchomien] razy dla rozmiarów zaczynających się od 1 i rosnących o [wielkosc_skoku] (liczony od wartości 0) i zapisanie wyników do pliku .xlsx.

Dane wejściowe programu znajdują się w folderze 'Data_files' - są to proste pliki tekstowe z danymi w formacie:
X1 Y2
X2 Y2
...
Xn Yn

Po zakończeniu obliczeń (uruchomienie z flagą -r) na standardowe wyjście zostaną wypisane:
1. Współrzędne najdalszego punktu, do jakiego można dotrzeć wykorzystując dane wektory
2. Odległość w jakiej ten punkt się znajduje od punktu wyjścia
3. Czas działania obliczeń


Opis metody rozwiązania problemu:
1. Dla każdego z wektorów należących do badanego zbioru wyznaczenie 2 wektorów powstałych przez normalizację oraz obrócenie analizowanego wektora o 90° oraz -90°. Zbiór nowo powstałych wektorów nazwijmy zbiorem Y.
2. Sortowanie wektorów ze zbioru Y w porządku malejącym od y1 do yt, gdzie t jest mocą zbioru Y, względem kąta między wektorem a osią OX. Usunięcie z tego zbioru wektorów powtarzających się.
3. Dla każdego wektora y ze zbioru Y utworzenie zbiorów L(y) i R(y) gdzie:
    - L(y) - zbiór wektorów należących do zbioru początkowego, które po znormalizowaniu i obróceniu o 90° dadzą wektor y
    - R(y) - zbiór wektorów należących do zbioru początkowego, które po znormalizowaniu i obróceniu o -90° dadzą wektor y
4. Niech v1 będzie sumą wektorów należących do zbioru początkowego, których iloczyn skalarny z wektorem generującym półprostą, będącą dwusieczną kąta między wektorami y1 i y2, jest dodatni.
5. Dla i = 2,...,t wyznaczamy vi = vi-1 + sum(x in L(yi) ) - sum(x in R(yi) )
6. Koniec wektora Vk{V1,...,Vt} o największej długości znajduje się w najdalej oddalonym od początku układu punkcie, do którego można dotrzeć sumując wektory ze zbioru początkowego.
7. Przechodząc przez początkowy zbiór wektorów i wybierając z niego wektory, których iloczyn skalarny z Vk jest dodatni, znajdujemy wektory, które sumują się do Vk.