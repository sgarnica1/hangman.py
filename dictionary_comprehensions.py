import math


def run():
    # my_dictionary = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dictionary[i] = i**3

    # my_dictionary = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    # print(my_dictionary)

    my_new_dictionary = {i: math.sqrt(i) for i in range(1, 1001)}
    print(my_new_dictionary)


if __name__ == '__main__':
    run()
