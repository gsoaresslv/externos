def main():
    q1 = "s"
    while(q1 == "s"):
        q = input("Qual valor da função você quer descobrir? (a, b, x ou y): ")
        if(q == "y" or q == "Y"):
            a = float(input("Insira o valor de A: "))
            b = float(input("Insira o valor de B: "))
            x = float(input("Insira o valor de X: "))
            y = a*x+b
            print(f'O valor de Y é igual a {y}')
        elif(q == "a" or q == "A"):
            y = float(input("Insira o valor de Y: "))
            b = float(input("Insira o valor de B: "))
            x = float(input("Insira o valor de X: "))
            y = a*x+b
            print(f'O valor de A é igual a {a}')
        elif(q == "b" or q == "B"):
            a = float(input("Insira o valor de A: "))
            x = float(input("Insira o valor de X: "))
            y = float(input("Insira o valor de Y: "))
            y = a*x+b
            print(f'O valor de B é igual a {b}')
        elif(q == "x" or q == "X"):
            a = float(input("Insira o valor de A: "))
            b = float(input("Insira o valor de B: "))
            y = float(input("Insira o valor de Y: "))
            y = a*x+b
            print(f'O valor de X é igual a {x}')
        else:
            q1 = input(
                "Resposta invalída, deseja tentar novamente? (s para sim / n para não): ")
        q1 = input("Deseja tentar novamente? (s para sim / n para não): ")
    if(q1 == "n"):
        print("Ok, fechando programa.")


if __name__ == "__main__":
    main()
