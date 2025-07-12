import os
import re

# Directorio donde está el script
script_dir = os.path.dirname(os.path.abspath(__file__))
script_name = os.path.splitext(os.path.basename(__file__))[0]
print(f'funcionando en: {script_dir}')

archivos = os.listdir(script_dir)
print('Archivos encontrados:', archivos)

for filename in archivos:
    match = re.fullmatch(r'(\d+)\.png', filename, re.IGNORECASE)
    if match:
        number = match.group(1)
        new_name = f"{script_name}{number}.png"
        old_path = os.path.join(script_dir, filename)
        new_path = os.path.join(script_dir, new_name)
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f'Renombrado: {filename} -> {new_name}')
        else:
            print(f'No se renombra {filename}: {new_name} ya existe')
    else:
        print(f'Ignorado: {filename}')