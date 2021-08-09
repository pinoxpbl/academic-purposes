def valida_int(pergunta):
    while True:
        try:
            x = int(input(pergunta))
            break
        except ValueError:
            print("O dado digitado não é um número...tente novamente")
            continue
    return x

# Programa principal

print("CALCULADORA")
print("ADIÇÃO [+]")
print("SUBTRAÇÃO [-]")
print("MULTIPLICAÇÃO [*]")
print("DIVISÃO [/]")

while True:
    op = input("Qual operador você deseja utilizar?: ")
    if (op not in "+-*/"):
        print("Operador incorreto! somente \"+,-,*,/\" são aceitos")
    else:
        num1 = valida_int("Digite o primeiro número: ")
        num2 = valida_int("Digite o segundo número: ")

    if(op == "+"):
        print("{} + {} = {}".format(num1,num2,num1 + num2))
    elif(op == "-"):
        print("{} - {} = {}".format(num1,num2,num1 - num2))
    elif (op == "*"):
        print("{} * {} = {}".format(num1, num2, num1 * num2))
    elif(op == "/"):
        try:
            print("{} / {} = {}".format(num1, num2, num1 / num2))
        except ZeroDivisionError:
            print("Não é possível dividir por zero")



