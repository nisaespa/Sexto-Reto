class OperacionInvalidaException(Exception):
    """Excepción para manejar operadores inválidos."""
    def __init__(self, mensaje):
        super().__init__(mensaje)

class Calculadora:
    """Clase que realiza operaciones matemáticas básicas."""
    def operar(self, operando1, operando2, operador):
        """
        Realiza la operación matemática indicada.

        Args:
            operando1 (float): Primer número.
            operando2 (float): Segundo número.
            operador (str): Operación a realizar (+, -, *, /).

        Returns:
            float: Resultado de la operación.

        Raises:
            OperacionInvalidaException: Si el operador no es válido.
            ZeroDivisionError: Si se intenta dividir por cero.
        """
        if not isinstance(operando1, (int, float)) or not isinstance(operando2, (int, float)):
            raise ValueError("Los operandos deben ser números.")

        if operador == "+":
            return operando1 + operando2
        elif operador == "-":
            return operando1 - operando2
        elif operador == "*":
            return operando1 * operando2
        elif operador == "/":
            if operando2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            return operando1 / operando2
        else:
            raise OperacionInvalidaException("Operación no válida. Usa (+, -, *, /).")

if __name__ == "__main__":
    try:
        numero1 = float(input("Escribe el primer operando: "))
        numero2 = float(input("Escribe el segundo operando: "))
        operador = input("Escribe el símbolo de la operación que quieres hacer (+, -, *, /): ")
        
        calculadora = Calculadora()
        resultado = calculadora.operar(numero1, numero2, operador)

        print("El resultado es:", resultado)

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except OperacionInvalidaException as e:
        print(f"Error: {e}")
