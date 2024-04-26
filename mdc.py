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
    a = int(input("Digite um número: "))
    b = int(input("Digite o segundo número: "))

    print(maior_divisor(a,b))

main ()

