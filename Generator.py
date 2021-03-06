"""
Zadanie 10 - czołg steampunkowy
Pawel Lech
Michal Laskowski
"""
import random
import Card


def generate(number_of_cards, path):
    if number_of_cards < 1 or number_of_cards > 200000:
        print("Bledna liczba kart")
        return

    random.seed(None)

    file = open(path, 'w')
    for i in range(number_of_cards - 1):
        str1 = str(random.randint(-10000, 10000))
        str2 = str(random.randint(-10000, 10000))
        write_string = str1 + " " + str2 + "\n"
        file.writelines(write_string)
    str1 = str(random.randint(-10000, 10000))
    str2 = str(random.randint(-10000, 10000))
    write_string = str1 + " " + str2
    file.writelines(write_string)
    file.close()


def generate_for_excel(list_of_cards, number):
    list_of_cards.clear()
    random.seed(None)
    for i in range(number):
        list_of_cards.append(Card.Card(float(random.randint(-10000, 10000)), float(random.randint(-10000, 10000))))
