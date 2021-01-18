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
        print("**")
        print(path)
        print("**")
        path = 'Data_files\\' + path
        print("**")
        print(path)
        print("**")
        with open(path, 'r') as file:
            for line in file:
                for word in line.split():
                    temp_x = float(line.split()[0])
                    temp_y = float(line.split()[1])
                self.add_card(Card.Card(temp_x, temp_y))
