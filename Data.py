import Card


class Data:

    def __init__(self):
        self.list_of_cards = list()

    def add_card(self, card):
        self.list_of_cards.append(card)

    def read_from_file(self, path):
        temp_x = 0
        temp_y = 0

        with open(path, 'r') as file:
            for line in file:
                for word in line.split():
                    temp_x = float(word)
                    temp_y = float(word)
                self.add_card(Card.Card(temp_x, temp_y))
