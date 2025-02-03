# Programación Orientada a Objetos - UNAL
## Sexto Reto 
### Aplicando Excepciones al Reto 1:
1. Creé una función que se llama `operaciones`, que recibe dos números y el operador (+, -, *, /) del usuario, la función aplica condicionales dependiendo del operador, para hacer la operación con los dos números, e imprime el resultado.
```python
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
```

2. Creé una función llamada `palindromo` que toma una palabra como entrada, para evitar problemas de mayúsculas y minúsculas, convertí la palabra a minúsculas usando el método `lower()`. Luego calculé la longitud de la palabra con `len()`, para verificar si es un palíndromo, implementé un bucle `for` que recorre los caracteres desde los extremos hacia el centro de la palabra. En cada iteración, comparé el carácter de la posición inicial con el correspondiente desde el final.
```python
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

```
3. Creé una función que verifica si un número es primo, el número se pide al usuario, utilicé un condional para descartar los numeros menores o iguales a 1. Luego utilizo un bucle `for` que recorre desde 2 hasta la raíz cuadrada del número, redondeada hacia abajo y aumentada en 1, comprobando si el número es divisible por alguno de esos valores; si encuentra un divisor retorna `False`, indicando que no es primo. Si pasa las pruebas retorna `True`, indicando que el número es primo.
```python
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

        for i in range(2, int(numero**0.5) + 1):  # Itera hasta la raíz cuadrada del número.
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

```
4. Creé una función que encuentra la suma más grande entre dos números consecutivos de una lista. Ya teniendo la lista calcula las primeras dos posiciones y las toma como la `mayor_suma`. Luego, revisa todas las parejas de números consecutivos, mediante un ciclo `for`, itera desde el segundo número hasta el penúltimo, calculando la suma de cada pareja . Si encuentra una suma mayor que la que tenía registrada, actualiza el valor de `mayor_suma`. Al finalizar el ciclo, imprime la `mayor_suma`.
```python
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
```
5. Creé una función que utiliza dos bucles `for` para comparar cada palabra de la lista con las que vienen después de ella, para cada par de palabras ordena sus letras y mira si son iguales, lo que indica que tienen las mismas letras. Se añaden a una lista vacía e imprime la lista con las palabras con letras iguales.
```python
class ListaPalabrasInvalidaException(Exception):
    """Excepción para manejar listas de palabras no válidas."""
    def __init__(self, mensaje):
        super().__init__(mensaje)

class VerificadorMismosCaracteres:
    """Clase que verifica qué palabras en una lista tienen las mismas letras."""

    def mismos_caracteres(self, lista):
        """
        Encuentra las palabras que tienen las mismas letras en una lista.

        Args:
            lista (list): Lista de palabras.

        Returns:
            list: Lista con palabras que tienen los mismos caracteres.

        Raises:
            ListaPalabrasInvalidaException: Si la lista es vacía, tiene menos de dos palabras o contiene elementos no válidos.
        """
        if not isinstance(lista, list) or len(lista) < 2:
            raise ListaPalabrasInvalidaException("La lista debe contener al menos dos palabras.")
        if not all(isinstance(palabra, str) and palabra.isalpha() for palabra in lista):
            raise ListaPalabrasInvalidaException("Todos los elementos de la lista deben ser palabras válidas.")

        resultado = []
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                if sorted(lista[i].lower()) == sorted(lista[j].lower()):
                    if lista[i] not in resultado:
                        resultado.append(lista[i])
                    if lista[j] not in resultado:
                        resultado.append(lista[j])
        return resultado

if __name__ == "__main__":
    try:
        entrada = ["amor", "roma", "perro"]
        verificador = VerificadorMismosCaracteres()
        resultado = verificador.mismos_caracteres(entrada)
        print(f"Palabras con los mismos caracteres: {resultado}")
    except ListaPalabrasInvalidaException as e:
        print(f"Error: {e}")
```
