from Calculator import Calculator

def get_user_input(infix_or_prefix):

    print("****** (Prefix/Infix)*********\n \nType q to exit\n")
    calculator = Calculator()
    while True:
        expression = input(">")
        if infix_or_prefix == 1:
            print(calculator.infix_calculator(expression))
        elif infix_or_prefix ==2:
            print(calculator.prefix_calculator(expression))
        elif expression == 'q':
            exit(0)

if __name__ == '__main__':
    infix_or_prefix = int(input("Do you want to evaluate infix or prefix expression. Enter 1 for infix and 2 for prefix calculator, q for exit"))
    if infix_or_prefix == 1 or infix_or_prefix == 2:
        get_user_input(infix_or_prefix)
    else:
        raise Exception("Invalid expression")
