import Menu
import Data
import Generator
import sys


if __name__ == '__main__':
    try:
        if sys.argv[1] == '-m':
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
        else:
            print("Niepoprawna flaga uruchomienia.")
    except ValueError:
        print("Podano wartosc inna niz 'int' jako parametr wejsciowy.")
