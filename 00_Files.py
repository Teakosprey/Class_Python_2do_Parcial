import os
print('Holi con os')
print(os.getcwd()) #Devuelve la ruta de trabajo.

from pathlib import Path, PurePath #Lo mismo, pero más barato.
print('Holi desde path')
print(Path.cwd)

#Obtener los archivos en una ruta.

#print(os.listdir()) #Obtenemos una lista con los elementos de nuestra carpeta.
#print(os.listdir('Example4')) #Accedemos a los elementos de la carpeta de example 4.

#Crear carpetas usando Python.

#os.mkdir('Example5') #Creamos una carpeta que se llame Example5
#Path('Example6').mkdir(exist_ok = True)
#os.makedirs(os.path.join('Example7', 'Example8'))

#Renombrar archivos

os.rename('Example7', 'Example10')

for file in os.listdir():
    if file.endswith('.csv'):
        os.rename(file,f'2023_Tarea_{file}')