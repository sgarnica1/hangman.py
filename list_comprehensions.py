def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    # print(squares)

    squares = [num**2 for num in range(1, 101) if num % 3 != 0]
    print('Not divisible by 3')
    print(squares)

    multiples = [num for num in range(
        1, 10000) if num % 4 == 0 and num % 6 == 0 and num % 9 == 0]
    print('Only divisble by 4,6 and 9')
    print(multiples)


if __name__ == '__main__':
    run()
