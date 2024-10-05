# create a module for writing a file with the string passed

# file_writer.py

def write_to_file(filename, content):
    """
    Escribe el contenido en un archivo especificado por filename.
    
    :param filename: Nombre del archivo donde se escribirá el contenido.
    :param content: Contenido a escribir en el archivo.
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Contenido escrito exitosamente en {filename}")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

def array_to_string(array, joinchar=""):
    """
    Convierte un array en una cadena de texto.
    
    :param array: Array a convertir en cadena de texto.
    :param joinchar: Caracter de unión entre los elementos del array.
    :return: Cadena de texto con los elementos del array.
    """
    return joinchar.join([str(item) for item in array])

