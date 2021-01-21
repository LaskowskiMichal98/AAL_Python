"""
Zadanie 10 - czołg steampunkowy
Pawel Lech
Michal Laskowski
"""
import Menu
import Data
import Generator
import sys


def usage():
    print("""
    Poprawne uruchomienia:
    Menu:                                 > python main.py -m
    Generacja do pliku:                   > python main.py -c [nazwa_pliku.txt] [liczba_kart] 
    Wyświetlenie zawartości pliku:        > python main.py -s [nazwa_pliku.txt]
    Algorytm dla danych z pliku:          > python main.py -r [nazwa_pliku.txt]
    Algorytm dla losowego zestawu danych: > python main.py -e [nazwa_pliku_wynikowego.xlsx] [liczba_uruchomień]
    Algorytm dla losowego zestawu danych: > python main.py -t [nazwa_pliku.xlsx] [liczba_uruchomień] [wielkość_skoku]
    
    Dokładniejszy opis poszczególnych opcji w pliku readme.txt lub dokumentacji projektu.
    """)


if __name__ == '__main__':
    try:
        if sys.argv[1] == '-h':
            usage()
        elif sys.argv[1] == '-m':
            Menu.menu()
        elif sys.argv[1] == '-c':
            Generator.generate(int(sys.argv[3]), sys.argv[2])
            print(f'Wygenerowano {sys.argv[3]} kart do pliku {sys.argv[2]}.')
        elif sys.argv[1] == '-s':
            my_data = Data.Data()
            my_data.read_from_file(sys.argv[2])
            Menu.show_data(my_data)
        elif sys.argv[1] == '-r':
            my_data = Data.Data()
            my_data.read_from_file(sys.argv[2])
            Menu.run_algorithm(my_data)
        elif sys.argv[1] == '-e':
            Menu.go_go_excel(sys.argv[2], int(sys.argv[3]))
        elif sys.argv[1] == '-t':
            Menu.table_builder(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
        else:
            print("Niepoprawna flaga uruchomienia.")
    except ValueError:
        print("Podano wartosc inna niz 'int' jako parametr wejsciowy.")
    except IndexError:
        usage()

