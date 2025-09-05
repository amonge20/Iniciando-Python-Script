import os
import time

# Creacion de la carpeta Primero
try:
    os.mkdir('.\Primero') # Te crea la carpeta primero en la ruta actual en la que estas
    print("Creando el directorio...")
    time.sleep(2) # Simulacion del tiempo de ejecucion
except FileExistsError:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("El directorio 'Primero' ya existe")
else:
    print("Directorio 'Primero' ya creado")

# Entramos a la carpeta Primero




# Eliminacion de la carpeta Primero
os.rmdir('.\Primero')
print("Eliminando el directorio...")
time.sleep(2) # Simulacion del tiempo de ejecucion
print("El directorio 'Primero', eliminado.")
print('\n')
print("FIN DEL SCRIPT. GRACIAS POR TODO")
print('\n')