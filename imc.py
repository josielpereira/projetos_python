def calcular_imc(peso, altura):
    # Fórmula do IMC: peso / (altura * altura)
    imc = peso / (altura ** 2)
   
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >18.5 and imc < 25:
        return "Peso normal"
    elif imc > 25 and imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    # Entrada de dados
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))

    # Calculando o IMC
    imc = calcular_imc(peso, altura)

    # Exibindo o resultado
    print("Seu IMC é:", imc)
  

main()
