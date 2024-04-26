binario = input("Digite o número (binário) para ser convertido para a base decimal: ")
n = len(binario)
decimal = 0
i = 0

for i in range(n):
 decimal += int(binario[n-1]) * 2**i
 n -= 1
 
print("O número (binario) digitado", binario, ", na base decimal, vale:",decimal)
