import subprocess
import time

def ejecutar_comando_repetidamente(comando, intervalo):
    while True:
        resultado = subprocess.run(comando, shell=True)
        print(f"Comando ejecutado con código de retorno: {resultado.returncode}")
        time.sleep(intervalo)

if __name__ == "__main__":
    # Cambia el comando y el intervalo aquí
    comando = "echo 'Hola mundo'"  # Comando que deseas ejecutar
    intervalo = 2  # Intervalo en segundos

    ejecutar_comando_repetidamente(comando, intervalo)
