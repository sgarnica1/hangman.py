def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    try:
        num = int(input('Escribe un número: '))
        if num <= 0:
            raise ValueError()
        print(divisors(num))
    except ValueError as ve:
        print('Debes ingresar un número positivo')


if __name__ == "__main__":
    run()
