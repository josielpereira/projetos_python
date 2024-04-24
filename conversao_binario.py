def converte(decimal):
    binario = []
    resto = 0

    while(decimal != 0):
        resto = decimal % 2
        decimal = decimal // 2
        binario.append(resto)
    for i in range(len(binario) -1, -1, -1):
        print(binario[i])

    binario.reverse()
    print(binario)
    string_binario = ""
    for i in range(len(binario)):
        string_binario += str(binario[i])
    print(string_binario) # melhor exibição
    

def main():
    numero = int(input("Digite um numero decimal para ser convertido: "))
    converte(numero)
        
main()


