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
    a = int(input("Digite um número "))
    b = int(input("Digite um segundo número: "))
    c = int(input("Digite um terceiro número: "))

    mmc_a_b = a * b // maior_divisor(a,b)
    mdc_c = maior_divisor(mmc_a_b, c)
    mmc_a_b_c = c * mmc_a_b // mdc_c
    print(mmc_a_b_c)

main()
