import os, time, shutil


# Creacion de la carpeta Primero
print('\n')
try:
    print("Creando el directorio 'Primero'...")
    time.sleep(2) # Simulacion del tiempo de ejecucion
    os.mkdir(r'.\Primero') # Te crea la carpeta primero en la ruta actual en la que estas
except FileExistsError:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("El directorio 'Primero' ya existe")
else:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("Directorio 'Primero' ya creado")


# Entramos a la carpeta Primero
print('\n')
print("Entrando al directorio primero...")
time.sleep(2) # Simulacion del tiempo de ejecucion
os.chdir(r'.\Primero')
print("Directorio actual: ", os.getcwd()) # Para que muestre la ruta en la que estamos actualmente


# Crea un archivo llamado archivo1.txt
print('\n')
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
print('\n')
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
print('\n')
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


# Retrocede directorio, averigua la ruta actual y copia 'copia.txt' en este directorio superior
print('\n')
os.chdir(r'..')
print("Ahora retrocedemos al directorio actual: ", os.getcwd())
print("Copiando el fichero 'copia.txt' al directorio actual...")
shutil.copyfile(r'.\Primero\copia.txt', r'.\copia.txt')
time.sleep(2)
print("El fichero 'copia.txt' ya copiado en el directorio actual: ", os.getcwd())

# Entramos en el directorio 'Primero' y borra 'copia.txt' 
print('\n')
os.chdir('.\Primero')
print("Eliminando el fichero 'copia.txt'...")
time.sleep(2)
os.remove('copia.txt')
print("Eliminacion de 'copia.txt' realizada con exito")


# Copia del directorio Primero y llamalo Segundo
print('\n')
os.chdir(r'..')
try: 
    print("Copiando el directorio 'Primero' y que ahora se llamara 'Segundo'...")
    shutil.copytree(r'.\Primero', r'.\Segundo')
    time.sleep(2)
except FileExistsError:
    time.sleep(2)
    print("Directorio ya copiado")
else:
    time.sleep(2)
    print("El directorio 'Segundo' ya se ha creado con la copia del directorio 'Primero'")


# Comprobacion el contenido de las 2 carpetas
print('\n')
print("Mostrando el contenido de los directorios de 'Primero' y de 'Segundo'...")
time.sleep(2)
print(os.listdir('.\Primero'))
print(os.listdir('.\Segundo'))


# Eliminacion de la carpeta 'Primero' 
print('\n')
print("Eliminando el directorio 'Primero'...")
shutil.rmtree(r'.\Primero')
time.sleep(2) # Simulacion del tiempo de ejecucion
print("El directorio 'Primero', eliminado.")


# Entramos al directorio 'Segundo' y crea un fichero llamado 'archivo2.txt'
print('\n')
print("Entramos al directorio 'Segundo'...")
os.chdir('.\Segundo')

try:
    print("Creando el fichero 'archivo2.txt'...")
    time.sleep(2) # Simulacion del tiempo de ejecucion
    with open('archivo2.txt','w') as f:
        pass # Solo lo crea
except FileExistsError:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("El fichero 'archivo2.txt' ya existe")
else:
    time.sleep(2) # Simulacion del tiempo de ejecucion
    print("El fichero 'archivo2.txt' ya creado")


# "Abrimos" 'archivoFinal.txt' y escribira lo siguiente
with open('archivoFinal.txt','w', encoding="utf-8") as f:
    f.write("esto es una prueba 1\n")
    f.write("esto es una prueba 2\n")
    f.write("esto es una prueba 3\n")
    f.write("esto es una prueba 4\n")
    f.write("esto es una prueba 5\n")
    f.write("esto es una prueba 6\n")
    f.write("esto es una prueba 7\n")
    
with open('archivoFinal.txt','r') as r:
    contenido_archivoFinal = r.read() # Mostrar el contenido escrito
    print("Mostrando el contenido del fichero 'archivoFinal.txt'")
    print(contenido_archivoFinal)
    
# "Abrimos" 'archivo2.txt' y escribira lo siguiente 
with open('archivo2.txt','w', encoding="utf-8") as f:
    f.write("esto es una prueba 8\n")
    f.write("esto es una prueba 9\n")
    f.write("esto es una prueba 10\n")
    f.write("esto es una prueba 11\n")
    f.write("esto es una prueba 12\n")
    f.write("esto es una prueba 13\n")
    f.write("esto es una prueba 14\n")
    
with open('archivo2.txt','r') as r:
    contenido_archivo2 = r.read() # Mostrar el contenido escrito
    print("Mostrando el contenido del fichero 'archivo2.txt'")
    print(contenido_archivo2)

print('\n')
print("Concatenación de archivos con 'archivoFinal.txt' y 'archivo2.txt'")
# Concatena ambos archivos ('archivoFinal.txt', 'archivo2.txt') y crea como resultado un nuevo archivo llamado Resultado.txt 
archivos = ['archivoFinal.txt','archivo2.txt']

archivo_salida = 'Resultado.txt'

with open(archivo_salida,'w', encoding="utf-8") as salida:
    for nombre in archivos:
        try:
            with open(nombre, 'r', encoding='utf-8') as entrada:
              contenido = entrada.read()
              salida.write(contenido)
              salida.write('\n')  
        except FileNotFoundError:
            print("Archivo no encontrado: {nombre}")
        except Exception as e:
            print("Error al leer {nombre}: {e}")
        
# Si todo sale bien
print("Archivos concatenados correctamente en ",archivo_salida)

with open('Resultado.txt','r') as r:
    contenido_archivoResultado = r.read() # Mostrar el contenido escrito
    print(contenido_archivoResultado)

    
# Mostramos las primeras 10 lineas del archivo
print('\n')


# Mostramos las primeras y ultimas 10 lineas del 'Resultado.txt'


# Comprobamos la fecho de creación de los archivos


# Haz un update del fichero 'archivoFinal.txt'


print("FIN DEL SCRIPT. GRACIAS POR TODO")
print('\n')