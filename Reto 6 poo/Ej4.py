class ListaInvalidaException(Exception):
    """Excepción para manejar listas no válidas."""
    def __init__(self, mensaje):
        super().__init__(mensaje)

class CalculadoraSumaConsecutiva:
    """Clase para calcular la mayor suma de dos números consecutivos en una lista."""

    def mayor_suma_consecutivos(self, lista_de_numeros):
        """
        Calcula la mayor suma de dos números consecutivos en una lista.

        Args:
            lista_de_numeros (list): Lista de números.

        Returns:
            int/float: La mayor suma consecutiva.

        Raises:
            ListaInvalidaException: Si la lista tiene menos de dos elementos o contiene valores no numéricos.
        """
        if not isinstance(lista_de_numeros, list) or len(lista_de_numeros) < 2:
            raise ListaInvalidaException("La lista debe contener al menos dos números.")
        if not all(isinstance(n, (int, float)) for n in lista_de_numeros):
            raise ListaInvalidaException("Todos los elementos de la lista deben ser números.")
        mayor_suma = lista_de_numeros[0] + lista_de_numeros[1]
        for i in range(1, len(lista_de_numeros) - 1):
            suma_actual = lista_de_numeros[i] + lista_de_numeros[i + 1]
            if suma_actual > mayor_suma:
                mayor_suma = suma_actual
        return mayor_suma
    
if __name__ == "__main__":
    try:
        numeros = [14, 9, 21, 3, 2, 36]  
        calculadora = CalculadoraSumaConsecutiva()
        
        resultado = calculadora.mayor_suma_consecutivos(numeros)
        print(f"El resultado de la mayor suma consecutiva es: {resultado}")

    except ListaInvalidaException as e:
        print(f"Error: {e}")

