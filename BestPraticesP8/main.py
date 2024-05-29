# Python PEP 8 Best Pratices

variavel = 0
TOTAL = 0

class Persona:
    def __init__(self, message):
        self.inicio = message
        print(self.inicio)
    pass


def print_hi_with_message(name):
    pass


# Bad pratices
def printhiwithname(name):
    pass


def printhiwithname(x, y, z):
    t = (x + y) / z
    pass


def printhiwithname(nota1, nota2, divisor):
    t = (nota1 + nota2) / divisor
    pass


def media_aluno(nota1, nota2, divisor):
    t = (nota1 + nota2) / divisor
    pass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
