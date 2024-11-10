def main():
    prob = input("Enter the problem with spaces: ")
    result = calculate(prob)
    print(result)


def calculate(x):
    operations = ['+', '-', '/', '*']
    num1, op, num2 = x.split(" ")
    num1 = int(num1)
    num2 = int(num2)
    if op in operations:
        if op == '+':
            return add(num1, num2)
        elif op == '-':
            return sub(num1, num2)
        elif op == '/':
            return div(num1, num2)
        elif op == '*':
            return mul(num1, num2)
        else:
            raise ValueError("Enter the valid expressions.")
    

def add(n1, n2):
    return n1 + n2 


def sub(n1, n2):
    return n1 - n2


def div(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('Second number is zero.')
    else:
        return n1 / n2
    

def mul(n1, n2):
    return n1 * n2


if __name__ == "__main__":
    main()