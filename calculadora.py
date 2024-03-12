def soma(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x / y

def main():
    isEnd = False
    while not isEnd:
        verify = False
        while not verify:
            numero1 = input("\nDigite o primeiro número: ")
            try:
                numero1 = float(numero1)
                verify = True
            except:
                print("Tente novamente, numero invalido.")
        verify = False
        operacoes_possiveis = ["+","-","*","/","."]
        operacao = input("Escolha a operação:\n+ para soma\n- para subtracao\n* para multiplicar\n/ para divisao\n. para finalizar\n")
        while not verify:
            if operacao not in operacoes_possiveis:
                print('Operacao invalida digite novamente.')
                operacao = input("Escolha a operação:\n+ para soma\n- para subtracao\n* para multiplicar\n/ para divisao\n. para finalizar\n")
            else:
                verify = True
        if operacao == ".": 
            break
        verify = False
        while not verify:
            numero2 = input("\nDigite o segundo número: ")
            try:
                numero2 = float(numero2)
                verify = True
            except:
                print("Tente novamente, numero invalido.")

        resultado = None
        if operacao == "+":
            resultado = soma(numero1, numero2)
        elif operacao == "-":
            resultado = subtracao(numero1, numero2)
        elif operacao == "*":
            resultado = multiplicacao(numero1, numero2)
        else:
            resultado = divisao(numero1, numero2)

        print(f"\nO resultado de {numero1} {operacao} {numero2} = {resultado}\n")


main()

        