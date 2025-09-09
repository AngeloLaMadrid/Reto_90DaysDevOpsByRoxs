import os
import re
import subprocess

def get_current_branch():
    """Obtiene el nombre de la rama actual de Git"""
    try:
        result = subprocess.run(
            ['git', 'branch', '--show-current'],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("No se pudo obtener la rama actual de Git. Usando 'main' por defecto.")
        return "main"

def create_90dias_script_content():
    """Contenido del script 90DiasDevOps.py actualizado con la detección de rama Git"""
    return '''#Recordatorio este script hace que los archivos .png que se encuentren en la carpeta donde se ejecuta 
#este script sean renombrados con el formato "90DiasDevOps_SemanaX_DiaY_IMGZ.png"
import os
import re
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))

# Obtener el nombre de la rama actual de git
def get_branch_name():
    try:
        branch = subprocess.check_output(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            cwd=script_dir
        ).decode().strip()
        return branch
    except Exception as e:
        print(f'Error obteniendo la rama: {e}')
        return None

branch_name = get_branch_name()
match_semana = re.match(r'Semana(\\d+)', branch_name or '', re.IGNORECASE)
if match_semana:
    semana_str = f"Semana{match_semana.group(1)}"
else:
    print('No se pudo obtener el número de semana de la rama actual.')
    semana_str = "SemanaX"

parent_dir = os.path.basename(os.path.dirname(script_dir))
match_dia = re.match(r'Dia(\\d+)', parent_dir, re.IGNORECASE)
if match_dia:
    dia_str = f"Dia{match_dia.group(1)}"
else:
    dia_str = "DiaX"

print(f'Funcionando en: {script_dir}')
archivos = os.listdir(script_dir)
print('Archivos encontrados:', archivos)

for filename in archivos:
    match = re.fullmatch(r'(\\d+)\\.png', filename, re.IGNORECASE)
    if match:
        img_num = match.group(1)
        new_name = f"90DiasDevOps_{semana_str}_{dia_str}_IMG{img_num}.png"
        old_path = os.path.join(script_dir, filename)
        new_path = os.path.join(script_dir, new_name)
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f'Renombrado: {filename} -> {new_name}')
        else:
            print(f'No se renombra {filename}: {new_name} ya existe')
    else:
        print(f'Ignorado: {filename}')
'''

def create_md_content(dia_number, branch_name):
    """Contenido básico para el archivo markdown"""
    return f'''# Actividad {dia_number} - {branch_name}

## Descripción
Actividad correspondiente al Día {dia_number} del reto 90 Días DevOps.


'''

def sanitize_filename(name: str) -> str:
    """Sanitiza el nombre para usarlo como archivo (solo letras, números, guiones y guiones bajos)."""
    # Reemplaza espacios por guiones bajos y elimina caracteres problemáticos
    name = name.replace(' ', '_')
    return re.sub(r'[^A-Za-z0-9._-]', '', name)

def rename_images_in_folder(img_dir, semana_str, dia_str):
    """Renombra las imágenes en la carpeta especificada con el formato adecuado"""
    if not os.path.exists(img_dir):
        return

    print(f"Procesando imágenes en: {img_dir}")
    archivos = os.listdir(img_dir)
    for filename in archivos:
        match = re.fullmatch(r'(\d+)\.png', filename, re.IGNORECASE)
        if match:
            img_num = match.group(1)
            new_name = f"90DiasDevOps_{semana_str}_{dia_str}_IMG{img_num}.png"
            old_path = os.path.join(img_dir, filename)
            new_path = os.path.join(img_dir, new_name)
            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                print(f'Renombrado: {filename} -> {new_name}')
            else:
                print(f'No se renombra {filename}: {new_name} ya existe')

def process_dia_folders():
    """Procesa y crea carpetas Dia1 a Dia7 y sus archivos internos si no existen"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_branch = get_current_branch()

    print(f"Procesando carpetas en: {current_dir}")
    print(f"Rama actual: {current_branch}")
    
    # Obtener el número de semana de la rama
    match_semana = re.match(r'Semana(\d+)', current_branch or '', re.IGNORECASE)
    if match_semana:
        semana_str = f"Semana{match_semana.group(1)}"
    else:
        print('No se pudo obtener el número de semana de la rama actual.')
        semana_str = "SemanaX"

    # Crear carpetas Dia1 a Dia7 si no existen
    for dia_number in range(1, 8):
        dia_folder = f"Dia{dia_number}"
        dia_str = f"Dia{dia_number}"
        item_path = os.path.join(current_dir, dia_folder)

        if not os.path.exists(item_path):
            os.makedirs(item_path)
            print(f"✅ Creada carpeta: {dia_folder}/")
        else:
            print(f"⚠️  Ya existe carpeta: {dia_folder}/")

        # Crear archivo markdown
        md_filename = sanitize_filename(f"{current_branch}_Actividad{dia_number}.md")
        md_path = os.path.join(item_path, md_filename)
        if not os.path.exists(md_path):
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(create_md_content(dia_number, current_branch))
            print(f"✅ Creado: {dia_folder}/{md_filename}")
        else:
            print(f"⚠️  Ya existe: {dia_folder}/{md_filename}")

        # Crear carpeta img si no existe
        img_dir = os.path.join(item_path, "img")
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
            print(f"✅ Creada carpeta: {dia_folder}/img/")
        else:
            print(f"⚠️  Ya existe carpeta: {dia_folder}/img/")
        
        # Renombrar las imágenes en la carpeta img
        rename_images_in_folder(img_dir, semana_str, dia_str)

def main():
    """Función principal"""
    print("🚀 Automatizador General - Reto 90 Días DevOps")
    print("=" * 50)

    try:
        process_dia_folders()
        print("\n✅ Proceso completado exitosamente!")
    except Exception as e:
        print(f"\n❌ Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()