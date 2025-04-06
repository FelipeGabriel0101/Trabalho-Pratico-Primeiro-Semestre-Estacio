saida = ''

def adicao(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if a == 0 or b == 0:
        print("Não foi possível realizar a divisão por 0")

    else:
        return a/b
    
def calculadora(a,b,op):
    if op == "adicao" or op == "adição" or op ==  "+":
        resultado = adicao(a,b)
    
    elif op == "subtracao" or op == "subtração" or op == "-":
        resultado = subtracao(a,b)
    
    elif op == "multiplicacao" or op == "multiplicação" or op == "*":
        resultado = multiplicacao(a,b)

    elif op == "divisao" or op == "divisão" or op == "/":
        resultado = divisao(a,b)
    
    return resultado


while saida.lower() != "n":
    a = int(input("Digite o primeiro número "))
    b = int(input("Digite o segundo número "))
    op = input("Qual operação deseja realizar? ")
    resultado = calculadora(a,b,op)
    print(f"Resultado da operação: {resultado}")
    saida = input("Deseja continuar? S/N ")