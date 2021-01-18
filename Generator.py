import random


def generate(number_of_cards, path):
    if number_of_cards < 1 or number_of_cards > 200000:
        print("Bledna liczba kart")
        return -1

    random.seed(None)
    path = 'Data_files\\' + path
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
