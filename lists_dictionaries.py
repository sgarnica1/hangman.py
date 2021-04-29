def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dictionary = {'firstname': 'Sergio', 'lastname': 'Garnica'}

    super_list = [
        {'firstname': 'Sergio', 'lastname': 'Garnica'},
        {'firstname': 'Emilio', 'lastname': 'Garnica'},
        {'firstname': 'Diego', 'lastname': 'Garnica'},
        {'firstname': 'Tere', 'lastname': 'Garnica'},
        {'firstname': 'Sergio', 'lastname': 'Garnica'}
    ]

    super_dictionary = {
        'natural_nums': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'integer_nums': [-2, -1, 1, 2],
        'floating_nums': [0.2, 5.6, 8.4]
    }

    for key, value in super_dictionary.items():
        print(key, '-', value)


if __name__ == '__main__':
    run()
