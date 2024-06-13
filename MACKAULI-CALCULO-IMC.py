# Função que calcula o IMC
# Tem como parametro peso e altura.
def imc (peso, altura):
    calculo = peso / (altura*altura)
    return calculo

# Função que retorna a categoria.
# Tem como parametro o imc.
def categoria_imc (imc):

    if imc <= 18.5:
        print("Voce está abaixo do peso")

    elif (imc >= 18.5) and (imc <= 24.9):
        print("Voce está no peso normal")

    elif (imc >= 25) and (imc <= 29.9):
        print("Voce está acima do peso")

    elif (imc >= 30) and (imc <= 39.0):
        print("Voce está com obesidade grau I")

    elif (imc >= 40):
        print("Voce está com obesidade grau II")

# Função principal
if __name__ == '__main__':
    continuar = "s"

    while (continuar == "s"):
        p = float(input("Diga seu peso: "))
        a = float(input("Diga sua altura: "))
        imc_calculo = imc(p, a)
        # Imprimir a categoria do imc


        print(f"O IMC é {imc_calculo}")

        continuar = input("Deseja continuar? (s/n): ")

        categoria_imc(imc_calculo)
