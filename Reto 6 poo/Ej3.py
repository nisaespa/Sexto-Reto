class NumeroInvalidoException(Exception):
    """Excepción para manejar números no válidos."""
    def __init__(self, mensaje):
        super().__init__(mensaje)

class VerificadorPrimo:
    """Clase para verificar si un número es primo."""

    def es_primo(self, numero):
        """
        Verifica si un número es primo.

        Args:
            numero (int): Número a evaluar.

        Returns:
            bool: True si es primo, False si no lo es.

        Raises:
            NumeroInvalidoException: Si el número no es un entero positivo.
        """
        if not isinstance(numero, int):
            raise NumeroInvalidoException("El número debe ser un entero.")
        if numero < 2:
            raise NumeroInvalidoException("El número debe ser mayor o igual a 2.")

        for i in range(2, int(numero**0.5) + 1): 
            if numero % i == 0:
                return False
        return True

if __name__ == "__main__":
    try:
        numero = int(input("Ingresa un número entero para verificar si es primo: "))
        verificador = VerificadorPrimo()

        if verificador.es_primo(numero):
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} no es primo.")

    except NumeroInvalidoException as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")
