def verificar_numeros(num1, num2, num3):
    # Encontrando o maior número
    if num1 >= num2 and num1 >= num3:
        maior = num1
    elif num2 >= num1 and num2 >= num3:
        maior = num2
    else:
        maior = num3
    
    # Encontrando o menor número
    if num1 <= num2 and num1 <= num3:
        menor = num1
    elif num2 <= num1 and num2 <= num3:
        menor = num2
    else:
        menor = num3
    
    # Encontrando o intermediário
    intermediario = num1 + num2 + num3 - maior - menor
    
    # Retornando os números em uma lista
    return [maior, intermediario, menor]


n1 = 10
n2 = 5
n3 = 3
resultado = verificar_numeros(n1,n2,n3)
print("Maior:", resultado[0])
print("Intermediário:", resultado[1])
print("Menor:", resultado[2])
