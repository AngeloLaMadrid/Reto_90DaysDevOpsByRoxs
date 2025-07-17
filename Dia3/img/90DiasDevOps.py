#Recordatorio este escript hace que los archivos .png que se encuentren en la carpeta donde se ejecuta 
#este script sean renombrados con el nombre del script y el nombre del padre de la carpeta donde se ejecuta.  
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
script_name = os.path.splitext(os.path.basename(__file__))[0]

parent_dir = os.path.basename(os.path.dirname(script_dir))

match_parent = re.match(r'(Dia)(\d+)', parent_dir, re.IGNORECASE)
if match_parent:
    dia_str = f"{match_parent.group(1)}_{match_parent.group(2)}"
else:
    dia_str = parent_dir  

print(f'funcionando en: {script_dir}')
archivos = os.listdir(script_dir)
print('Archivos encontrados:', archivos)

for filename in archivos:
    match = re.fullmatch(r'(\d+)\.png', filename, re.IGNORECASE)
    if match:
        number = match.group(1)
        new_name = f"{script_name}_{dia_str}_{number}.png"
        old_path = os.path.join(script_dir, filename)
        new_path = os.path.join(script_dir, new_name)
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f'Renombrado: {filename} -> {new_name}')
        else:
            print(f'No se renombra {filename}: {new_name} ya existe')
    else:
        print(f'Ignorado: {filename}')