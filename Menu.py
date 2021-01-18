import Data
import Generator


def menu():
    data = Data.Data()
    while (True):
        print("*********************************")
        print("1. Generuj nowy plik z danymi")
        print("2. Wczytaj dane z pliku")
        print("3. Wyswietl wczytane dane")
        print("4. Uruchom algorytm")
        print("0. Wyjscie")
        print("*********************************")
        choice = input("Wybieram opcje: ")

        if choice == '1':
            generate_new_data()
        elif choice == '2':
            read_data(data)
        elif choice == '3':
            show_data(data)
        elif choice == '4':
            run_algorithm(data)
        elif choice == '0':
            return 0


def generate_new_data():
    path = input("Podaj nazwe pliku: ")
    length = int(input("Podaj liczbe kart (max 200k): "))
    Generator.generate(length, path)
    return


def read_data(data):
    path = input("Podaj nazwe pliku z danymi: ")
    data.read_from_file(path)
    return


def show_data(data):
    for i in range(len(data.list_of_cards)):
        print(data.list_of_cards[i].__str__())
    temp = input("Wcisnij enter, aby wrocic do menu.")
    return


def run_algorithm(data):
    #TODO
    return
