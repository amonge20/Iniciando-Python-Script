import os, time, shutil

# Borramos los directorios y ficheros que se crearon con el script de 'Inicio.py'
print("Eliminando el fichero 'copia.txt'...")
time.sleep(2)
os.remove(".\copia.txt")
print("Eliminando el directorio 'Segundo'...")
time.sleep(2)
shutil.rmtree(".\Segundo")

print('\n')
print("Todos los directorios y ficheros eliminados correctamente")