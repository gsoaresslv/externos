def f_verify(ans: str) -> bool:
    return True if ans.upper() == 'Y' else False if ans.upper() == 'N' else f_verify(input('Invalid value. Please enter a valid value: '))

def f_calculate(value: str) -> None:
    match value.upper():

        case "AB":
            print('To calculate the value of A and B, you must enter two ranges.')
            x1 = float(input('Insert X1 value: '))
            y1 = float(input('Insert Y1 value: '))
            x2 = float(input('Insert X2 value: '))
            y2 = float(input('Insert Y2 value: '))
            print(f'The A value is = {abs((y2 - y1)/(x2-x1))}, and the B value is = {abs((y2 - y1)/(x2-x1) * x1 - y1)}')

        case "A":
            y = float(input("Insert Y value: "))
            b = float(input("Insert B value: "))
            x = float(input("Insert X value: "))
            print(f'The A value is = {abs((y-b)/x)}')

        case "B":
            a = float(input("Insira o valor de A: "))
            x = float(input("Insira o valor de X: "))
            y = float(input("Insira o valor de Y: "))
            print(f'O valor de B é = {abs(a*x-y)}')

        case "X":
            a = float(input("Insira o valor de A: "))
            b = float(input("Insira o valor de B: "))
            y = float(input("Insira o valor de Y: "))
            print(f'O valor de X é = {abs(b/a - y)}')

        case "Y":
            a = float(input("Insira o valor de A: "))
            b = float(input("Insira o valor de B: "))
            x = float(input("Insira o valor de X: "))
            print(f'O valor de Y é = {abs(a*x+b)}')

        case "R":
            a = float(input("Insira o valor de A: "))
            b = float(input("Insira o valor de B: "))
            print(f'O valor da raiz é = {b/a}')

        case _:
            print('Invalid value')
    return None

def main():
    init = True
    while init:
        f_calculate(input("Select the function value you want to calculate (ab, a, b, x, y, r): "))
        init = f_verify(input('Do you want to continue? (Y/N): '))
    return 0
main()
