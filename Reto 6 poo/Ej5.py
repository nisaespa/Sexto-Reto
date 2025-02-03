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
