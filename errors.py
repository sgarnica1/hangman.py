# try, except
def palindrome(string):
    return string == string[::-1]


try:
    print(palindrome(1))
except TypeError:
    print('Solo se pueden ingresar strings')


# raise
def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError('No se pueden ingresar strings vacíos')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


# finally
try:
    f = open('archivo.txt')
    pass

finally:
    f.close()
