def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)

    # Se for divisão, mostra com 1 casa decimal
    if funcao == dividir:
        print(f"O resultado da operação é: {resultado:.1f}")
    else:
        print(f"O resultado da operação é: {resultado:.0f}")

# Menu
print("Escolha a operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Digite o número da operação: ")

a = float(input("Digite o primeiro número: "))

# Valida divisão por zero somente se for opção 4
if opcao == "4":
    while True:
        b = float(input("Digite o segundo número (≠ 0): "))
        if b != 0:
            break
        else:
            print("❌ Não é possível dividir por zero. Tente novamente.")
else:
    b = float(input("Digite o segundo número: "))

# Executa a operação escolhida
if opcao == "1":
    exibir_resultado(a, b, somar)
elif opcao == "2":
    exibir_resultado(a, b, subtrair)
elif opcao == "3":
    exibir_resultado(a, b, multiplicar)
elif opcao == "4":
    exibir_resultado(a, b, dividir)
else:
    print("⚠️ Opção inválida.")
