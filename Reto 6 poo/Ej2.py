class PalabraInvalidaException(Exception):
    """Excepción para manejar palabras no válidas."""
    def __init__(self, mensaje):
        super().__init__(mensaje)

class VerificadorPalindromo:
    """Clase que verifica si una palabra es un palíndromo."""
    
    def es_palindromo(self, palabra):
        """
        Verifica si una palabra es un palíndromo.

        Args:
            palabra (str): Palabra a evaluar.

        Returns:
            bool: True si es un palíndromo, False si no lo es.

        Raises:
            PalabraInvalidaException: Si la entrada no es válida (vacía o contiene caracteres no alfabéticos).
        """
        if not palabra.isalpha():
            raise PalabraInvalidaException("La palabra debe contener solo letras y no estar vacía.")

        palabra = palabra.lower()
        return palabra == palabra[::-1]

if __name__ == "__main__":
    try:
        palabra = input("Escribe una palabra: ")
        verificador = VerificadorPalindromo()

        if verificador.es_palindromo(palabra):
            print(f'"{palabra}" es un palíndromo.')
        else:
            print(f'"{palabra}" no es un palíndromo.')

    except PalabraInvalidaException as e:
        print(f"Error: {e}")

