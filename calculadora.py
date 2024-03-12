def soma(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x / y


def main():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    op = int(input("Escolha a operação:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão"))
    aux = 1
    while aux == 1:
        if op == 1:
            res = soma(x,y)
            print("A soma de ",x," e ",y," é: ", res)
            input("")
        elif op == 2:
            res = subtracao(x,y)
            print("A subtração de ",x," e ",y," é: ", res)
        