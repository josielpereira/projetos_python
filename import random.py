"""unidade_origem = int(input("Qual a unidade de origem (1. segundos, 2. milisegundos e 3. nanosegundos)"))
unidade_desejada = int(input("Qual a unidade  final (1. segundos, 2. milisegundos e 3. nanosegundos)"))
valor = int(input("Valor a ser convertido"))
resultado = 0 

if(unidade_origem != unidade_desejada):
    if unidade_origem == 1 and unidade_desejada == 2:
        resultado = valor * (10**3)
    elif(unidade_origem == 2 and unidade_desejada ==1):
        resultado = valor * (10**-3)
    elif unidade_origem == 1 and unidade_desejada == 3:
       resultado = valor  * (10**9)
    elif unidade_origem == 3 and unidade_desejada == 1:
       resultado = valor  * (10**-9)

print(resultado)"""


def printa(n):
    if n > 10:
        return 0
    print(printa(n + 1)) 

printa(0)