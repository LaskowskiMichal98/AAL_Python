Autorzy:
Paweł Lech, 276445
Michał Laskowski, 295804


Specyfikacja problemu:
Zadanie 10 - czołg steampunkowy
Jesteś żołnierzem na polu bitwy. To zapewne przykra wiadomość, ale to dopiero początek. Otóż bitwa dzieje się w rzeczywistości alternatywnej, w świecie steampunk, a wokół ciebie walczą olbrzymie machiny wojenne, napędzane parą i kierowane nie przez ludzi a przez maszyny różnicowe :-). Ty masz już dość i chcesz uciec jak najdalej. Na szczęście udało Ci się dostać do środka jednej z machin wojennych - na razie jesteś bezpieczny, ale trzeba uciekać!


Informacje o programie:
Program uruchamiany jest bez żadnych opcji i parametrów wejściowych. Użytkownik ma do dyspozycji proste menu tekstowe, z którego wybierane są poszczególne opcje.
Dane wejściowe programu znajdują się w folderze 'Data_files' - są to proste pliki tekstowe z danymi w formacie:
X1 Y2
X2 Y2
...
Xn Yn
Po zakończeniu obliczeń na standardowe wyjście zostaną wypisane:
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
5. Dla i = 2,...,t wyznaczamy vi = vi-1 + sum(xL(yi) ) - sum(xR(yi) )
6. Koniec wektora Vk{V1,...,Vt} o największej długości znajduje się w najdalej oddalonym od początku układu punkcie, do którego można dotrzeć sumując wektory ze zbioru początkowego.
7. Przechodząc przez początkowy zbiór wektorów i wybierając z niego wektory, których iloczyn skalarny z Vk jest dodatni, znajdujemy wektory, które sumują się do Vk.