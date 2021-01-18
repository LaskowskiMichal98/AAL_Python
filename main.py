import Generator
import Data

if __name__ == '__main__':
    Generator.generate(100, "test.txt")
    data = Data.Data()
    data.read_from_file("test.txt")

    for i in range(len(data.list_of_cards)):
        print(data.list_of_cards[i].__str__())

