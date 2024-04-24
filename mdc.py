def maior_divisor (a, b):
    resto = 1
    while (resto != 0):
        resto = a % b
        if (resto == 0):
            mdc = b
        else:
            a = b
            b = resto
    return (mdc)

def main ():
    a = int(input("DIGITE UM NÚMERO: "))
    b = int(input("DIGITE UM NÚMERO: "))

    print(maior_divisor(a,b))

main ()

# autor: Luiz Antonio Scarabelot Fiabani