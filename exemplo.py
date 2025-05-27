class Calculadora:
    def somar(num1: float, num2: float) -> float:
        return num1 + num2
    
    def subtrair(num1: float, num2: float) -> float:
        return num1 - num2

    def multiplicar(num1: float, num2: float) -> float:
        return num1 * num2

    def dividir(num1: float, num2: float) -> float:
        return num1 / num2

    def potencia(num1: float, num2: float) -> float:
        return num1 ** num2

    def raiz(num1: float, num2: float) -> float:
        return num1 ** (1/num2)

    def fatorial(num1: float) -> float:
        if num1 == 0:
            return 1
        else:
            return num1 * fatorial(num1 - 1)

