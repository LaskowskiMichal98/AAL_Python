import Data
import Generator
import os
import Algorithm
import xlsxwriter
import random


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    data = Data.Data()
    while True:
        cls()
        print("*********************************")
        print("1. Generuj nowy plik z danymi")
        print("2. Wczytaj dane z pliku")
        print("3. Wyswietl wczytane dane")
        print("4. Uruchom algorytm")
        print("5. Uruchom algorytm i zapisz wyniki do pliku .xlsx")
        print("6. Uruchom algorytm z wielkoscia skoku rozmiaru probleu i zapisz do pliku .xlsx")
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
        elif choice == '5':
            go_go_excel_menu()
        elif choice == '6':
            table_builder_menu()
        elif choice == '0':
            return 0


def generate_new_data():
    cls()
    path = input("Podaj nazwe pliku: ")
    length = int(input("Podaj liczbe kart (max 200k): "))
    Generator.generate(length, path)
    return


def read_data(data):
    cls()
    path = input("Podaj nazwe pliku z danymi: ")
    data.read_from_file(path)
    return


def show_data(data):
    cls()
    for i in range(len(data.list_of_cards)):
        print(data.list_of_cards[i].__str__())
    temp = input("Wcisnij enter, aby wrocic do menu.")
    return


def run_algorithm(data):
    algorithm = Algorithm.Algorithm()
    algorithm.run(data.list_of_cards)
    final_x, final_y, final_trip, time = algorithm.return_results()
    print(f'Punkt, do ktorego udalo sie zajsc: X = {final_x}, Y = {final_y}.')
    print(f'przebyta odleglosc: {final_trip}.')
    print(f'Czas wykonywania algorytmu: {time}.')
    temp = input("Wcisnij enter, aby wrocic/zakonczyc.")
    return


def go_go_excel_menu():
    cls()
    try:
        path = input("Podaj nazwe pliku (.xlsx): ")
        number_of_runs = int(input("Podaj liczbe uruchomien: "))
        go_go_excel(path, number_of_runs)
    except ValueError:
        print("Zla warotsc ilosci uruchomien")
    return


def table_builder_menu():
    cls()
    try:
        path = input("Podaj nazwe pliku (.xlsx): ")
        number_of_runs = int(input("Podaj liczbe uruchomien: "))
        jumps = int(input("Podaj wielkosc skoku: "))
        table_builder(path, number_of_runs, jumps)
    except ValueError:
        print("Zla warotsc ilosci uruchomien lub wielkości skoku")
    return


def go_go_excel(path, number_of_runs):
    if number_of_runs < 1:
        print("Bledna liczba uruchomiec algorytmu")
        return
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'X')
    worksheet.write(0, 1, 'Y')
    worksheet.write(0, 2, 'Odleglosc')
    worksheet.write(0, 3, 'Czas')
    worksheet.write(0, 4, 'N')
    random.seed(None)
    algorithm = Algorithm.Algorithm()
    
    my_data = Data.Data()
    
    for i in range(number_of_runs):
        Generator.generate_for_excel(my_data.list_of_cards, random.randint(1, 200000))
        algorithm.run(my_data.list_of_cards)
        final_x, final_y, final_trip, time = algorithm.return_results()
        worksheet.write(i+1, 0, final_x)
        worksheet.write(i+1, 1, final_y)
        worksheet.write(i+1, 2, final_trip)
        worksheet.write(i+1, 3, time)
        worksheet.write(i+1, 4, len(my_data.list_of_cards))
        
    workbook.close()
    return


def table_builder(path, number_of_runs, jumps):
    if number_of_runs < 1:
        print("Bledna liczba uruchomiec algorytmu")
        return
    if jumps < 1:
        print("Bledna wartosc skoku")
        return

    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'X')
    worksheet.write(0, 1, 'Y')
    worksheet.write(0, 2, 'Odleglosc')
    worksheet.write(0, 3, 'Czas')
    worksheet.write(0, 4, 'N')
    random.seed(None)
    algorithm = Algorithm.Algorithm()

    my_data = Data.Data()
    num = 0
    for i in range(number_of_runs):
        if i == 0:
            Generator.generate_for_excel(my_data.list_of_cards, 1)
        else:
            num += jumps
            Generator.generate_for_excel(my_data.list_of_cards, num)
        algorithm.run(my_data.list_of_cards)
        final_x, final_y, final_trip, time = algorithm.return_results()
        worksheet.write(i + 1, 0, final_x)
        worksheet.write(i + 1, 1, final_y)
        worksheet.write(i + 1, 2, final_trip)
        worksheet.write(i + 1, 3, time)
        worksheet.write(i + 1, 4, len(my_data.list_of_cards))

    workbook.close()
    return
