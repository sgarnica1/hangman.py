def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    num = input('Escribe un número: ')
    assert num.isnumeric(), "Escribe un número positivo"
    print(divisors(int(num)))


if __name__ == "__main__":
    run()
