from pathlib import Path

if __name__ == "__main__":

    files = [file for file in Path('.').rglob('*.dat') if file.is_file()]
    print(f"Encontre {len(files)} archivos .dat")
 
    """
    Escriba una rutina que itere sobre los
    archivos de la lista files e imprima su
    nombre y contenido (HINT: puede usar el
    método read_text() de Path)
    """

