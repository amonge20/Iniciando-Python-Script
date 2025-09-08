import os, time, shutil

# Creacion de la carpeta Primero
print('\n')
try:
    os.mkdir(r'.\Primero') # Te crea la carpeta primero en la ruta actual en la que estas
    print("Creando el directorio...")
    time.sleep(2) # Simulacion del tiempo de ejecucion
except FileExistsError:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("El directorio 'Primero' ya existe")
else:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("Directorio 'Primero' ya creado")

# Entramos a la carpeta Primero
print("Entrando al directorio primero...")
time.sleep(2) # Simulacion del tiempo de ejecucion
os.chdir(r'.\Primero')
print("Directorio actual: ", os.getcwd()) # Para que muestre la ruta en la que estamos actualmente

# Crea un archivo llamado archivo1.txt
try:
    print("Creando el fichero 'archivo1.txt'...")
    time.sleep(2) # Simulacion del tiempo de ejecucion
    with open('archivo1.txt','w') as f:
        pass # Solo lo crea
except FileExistsError:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("El fichero 'archivo1.txt' ya existe")
else:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("El fichero 'archivo1.txt' ya creado")

# Cambia el nombre del archivo1.txt a archivoFinal.txt
try:
    print("Cambiando de nombre el fichero de 'archivo1.txt' a 'archivoFinal.txt'...")
    time.sleep(2) # Simulacion del tiempo de ejecucion
    os.rename('archivo1.txt','archivoFinal.txt')
except FileExistsError:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("El fichero ya cambio su nombre")
else:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("El fichero 'archivo1.txt' ya renombrado correctamente a 'archivoFinal.txt'")
    
# Haz una copia del 'archivoFinal.txt' y llamalo 'copia.txt' y Mira en que PATH estas
try:
    print("Copiando el fichero 'archivoFinal.txt' para que se llame 'copia.txt'...")
    time.sleep(2) # Simulacion del tiempo de ejecucion
    shutil.copyfile('archivoFinal.txt','copia.txt')
    print("Directorio actual: ", os.getcwd())
except FileExistsError:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("Fichero ya copiado")
else:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("El fichero 'archivoFinal.txt' ya copiado de 'copia.txt'")
    print("Directorio actual: ", os.getcwd())

# Copia 'copia.txt' en este directorio superior




# Salto de linea
# print("\n")

# Eliminacion de la carpeta Primero
# os.chdir(r'..')
# shutil.rmtree(r'.\\Primero')
# print("Eliminando el directorio...")
# time.sleep(2) # Simulacion del tiempo de ejecucion
# print("El directorio 'Primero', eliminado.")
# print('\n')
# print("FIN DEL SCRIPT. GRACIAS POR TODO")
# print('\n')