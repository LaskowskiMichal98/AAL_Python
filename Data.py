"""
Zadanie 10 - czołg steampunkowy
Pawel Lech
Michal Laskowski
"""
import Card


class Data:

    def __init__(self):
        self.list_of_cards = list()

    def add_card(self, card):
        self.list_of_cards.append(card)

    def read_from_file(self, path):
        self.list_of_cards.clear()
        temp_x = 0
        temp_y = 0
        try:
            with open(path, 'r') as file:
                for line in file:
                    for word in line.split():
                        temp_x = float(line.split()[0])
                        temp_y = float(line.split()[1])
                    self.add_card(Card.Card(temp_x, temp_y))
        except FileNotFoundError:
            print("Nie znaleziono pliku")
            return
        except ValueError:
            print("Ktoras z wartosci kart nie jest liczba!")
            return
