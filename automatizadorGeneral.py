import os
import re
import subprocess

def get_current_branch():
    """Obtiene el nombre de la rama actual de Git"""
    try:
        result = subprocess.run(['git', 'branch', '--show-current'], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("No se pudo obtener la rama actual de Git. Usando 'main' por defecto.")
        return "main"

def create_90dias_script_content():
    """Contenido del script 90DiasDevOps.py"""
    return '''#Recordatorio este escript hace que los archivos .png que se encuentren en la carpeta donde se ejecuta 
#este script sean renombrados con el nombre del script y el nombre del padre de la carpeta donde se ejecuta.  
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
script_name = os.path.splitext(os.path.basename(__file__))[0]

parent_dir = os.path.basename(os.path.dirname(script_dir))

match_parent = re.match(r'(Dia)(\\d+)', parent_dir, re.IGNORECASE)
if match_parent:
    dia_str = f"{match_parent.group(1)}_{match_parent.group(2)}"
else:
    dia_str = parent_dir  

print(f'funcionando en: {script_dir}')
archivos = os.listdir(script_dir)
print('Archivos encontrados:', archivos)

for filename in archivos:
    match = re.fullmatch(r'(\\d+)\\.png', filename, re.IGNORECASE)
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
'''

def create_md_content(dia_number, branch_name):
    """Contenido básico para el archivo markdown"""
    return f'''# Actividad {dia_number} - {branch_name}

## Descripción
Actividad correspondiente al Día {dia_number} del reto 90 Días DevOps.

## Objetivos
- [ ] Objetivo 1
- [ ] Objetivo 2
- [ ] Objetivo 3

## Notas
*Agregar notas y observaciones aquí*

## Recursos
- Enlace 1
- Enlace 2

## Conclusiones
*Agregar conclusiones al finalizar la actividad*
'''

def process_dia_folders():
    """Procesa todas las carpetas que inician con 'Dia' y crea los archivos necesarios"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_branch = get_current_branch()
    
    print(f"Procesando carpetas en: {current_dir}")
    print(f"Rama actual: {current_branch}")
    
    # Buscar todas las carpetas que inician con "Dia"
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        
        # Verificar si es una carpeta que inicia con "Dia"
        if os.path.isdir(item_path) and re.match(r'^Dia\d+$', item, re.IGNORECASE):
            match = re.match(r'^Dia(\d+)$', item, re.IGNORECASE)
            if match:
                dia_number = match.group(1)
                print(f"\n📁 Procesando carpeta: {item}")
                
                # Crear archivo markdown de actividad
                md_filename = f"actividad{dia_number}_{current_branch}.md"
                md_path = os.path.join(item_path, md_filename)
                
                if not os.path.exists(md_path):
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(create_md_content(dia_number, current_branch))
                    print(f"✅ Creado: {md_filename}")
                else:
                    print(f"⚠️  Ya existe: {md_filename}")
                
                # Crear carpeta img si no existe
                img_dir = os.path.join(item_path, "img")
                if not os.path.exists(img_dir):
                    os.makedirs(img_dir)
                    print(f"✅ Creada carpeta: img/")
                else:
                    print(f"⚠️  Ya existe carpeta: img/")
                
                # Crear archivo 90DiasDevOps.py dentro de img
                script_path = os.path.join(img_dir, "90DiasDevOps.py")
                if not os.path.exists(script_path):
                    with open(script_path, 'w', encoding='utf-8') as f:
                        f.write(create_90dias_script_content())
                    print(f"✅ Creado: img/90DiasDevOps.py")
                else:
                    print(f"⚠️  Ya existe: img/90DiasDevOps.py")

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