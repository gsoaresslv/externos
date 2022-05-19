def main():
    init = 's'
    while init == 's':
        f = input("Qual valor da função você quer descobrir? (ab, a, b, x, y, r): ")
        if(f == "ab" or f == "Ab"):
            print(
                '\n\nPara descobrir o valor de A e B, você deve inserir dois intervalos. \n')
            x1 = int(input('Insira o valor de X1: '))
            y1 = int(input('Insira o valor de Y1: '))
            x2 = int(input('Insira o valor de X2: '))
            y2 = int(input('insira o valor de Y2: '))
            a = (y2 - y1)/(x2-x1)
            b = (a * x1 - y1)
            print(
                f'O valor de A é = {a}, e o valor de B é = {b*-1}')
        elif(f == "y" or f == "Y"):
            a = float(input("Insira o valor de A: "))
            b = float(input("Insira o valor de B: "))
            x = float(input("Insira o valor de X: "))
            y = a*x+b
            if a < 0:
                print(f'O valor de Y é = {y*-1}')
            else:
                print(f'O valor de Y é = {y}')
        elif(f == "a" or f == "A"):
            y = float(input("Insira o valor de Y: "))
            b = float(input("Insira o valor de B: "))
            x = float(input("Insira o valor de X: "))
            a=(y-b)/x
            print(f'O valor de A é = {a}')
        elif(f == "b" or f == "B"):
            a = float(input("Insira o valor de A: "))
            x = float(input("Insira o valor de X: "))
            y = float(input("Insira o valor de Y: "))
            b = a*x-y
            print(f'O valor de B é = {b}')
        elif(f == "x" or f == "X"):
            a = float(input("Insira o valor de A: "))
            b = float(input("Insira o valor de B: "))
            y = float(input("Insira o valor de Y: "))
            x = b/a - y
            if x < 0:
                print(f'O valor de X é = {x*-1}')
            else:
                print(f'O valor de X é = {x}')
        elif(f == 'r' or f == 'R'):
            a = float(input("Insira o valor de A: "))
            b = float(input("Insira o valor de B: "))
            r = b/a
            if a < 0:
                print(f'O valor da raiz é = {r*-1}')
            else:
                print(f'O valor da raiz é = {r}')
        else:
            init = input(
                "Resposta invalída, deseja tentar novamente? (s para sim / n para não): ")
        init = input("Deseja tentar novamente? (s para sim / n para não): ")
    if(init == "n"):
        print("Ok, fechando programa.")
main()
