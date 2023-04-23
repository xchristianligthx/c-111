import os
import shutil

from_dir = "Descargas/"
to_dir = "Documentos_Archivos/"

list_of_files = os.listdir(from_dir)
print("Archivos en la carpeta de origen: ")
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == ".pdf":
        src_path = from_dir + file_name
        dst_path = to_dir + file_name
        shutil.move(src_path, dst_path)
        print(f"El archivo {file_name} se ha movido correctamente.")
