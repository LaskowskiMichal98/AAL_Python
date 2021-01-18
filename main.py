# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Generator
import Data


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Generator.generate(100, "test.txt")
    data = Data.Data()
    data.read_from_file("test.txt")

    for i in range(len(data.list_of_cards)):
        print(data.list_of_cards[i].__str__())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
