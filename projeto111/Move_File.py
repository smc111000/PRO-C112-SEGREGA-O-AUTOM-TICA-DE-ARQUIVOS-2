import os
import shutil

from_dir = "C:/Users/Family/Downloads"
to_dir = "C:/Users/Family/OneDrive/Área de Trabalho/ESTUDOS/BYJUS/vs code"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == "":
        continue

    if extension.endswith(('.txt', '.doc', '.docx', '.pdf')):

        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Arquivos_Documentos")
        path3 = os.path.join(to_dir, "Arquivos_Documentos", file_name)

        if not os.path.isdir(path2):
            os.makedirs(path2)

        print("Movendo", file_name)
        shutil.move(path1, path3)

print("Fim do processo!")


