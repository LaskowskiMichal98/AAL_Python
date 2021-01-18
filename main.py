import Menu
import Data
import Generator
import sys
# TODO opis struktur i plikkow do readme.txt

if __name__ == '__main__':
    if sys.argv[1] == '-m':
        Menu.menu()
    elif sys.argv[1] == '-c':
        Generaton.generate(argv[3], argv[2])
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
        Menu.go_go_excel(sys.argv[2], sys.argv[3])
    else:
        print("Niepoprawna flaga uruchomienia.")
