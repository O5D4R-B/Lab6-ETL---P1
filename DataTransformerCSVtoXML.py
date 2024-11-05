import pandas as pd
import os
import xml.etree.ElementTree as ET

# Paso 1: Cargar el archivo CSV en memoria
csv_file_path = r'C:\Users\osdar\Documents\Carpeta\5toSemestre\BDA\Ejercicio de Lab 6\sales_data.csv'

# Cambio de codificación 
data = pd.read_csv(csv_file_path, encoding='ISO-8859-1')  # O 'Windows-1252'

# Paso 2: Procesar la información y eliminar filas donde la columna 'STATE' esté vacía
cleaned_data = data.dropna(subset=['STATE'])

# Paso 3: Guardar los datos restantes en un archivo XML
xml_file_path = r'C:\Users\osdar\Documents\Carpeta\5toSemestre\BDA\Ejercicio de Lab 6\output\sales_data_cleaned.xml'

# Crear la carpeta de salida si no existe
os.makedirs(os.path.dirname(xml_file_path), exist_ok=True)

# Crear el árbol XML
root = ET.Element('SalesData')

for _, row in cleaned_data.iterrows():
    entry = ET.SubElement(root, 'Entry')
    for col in cleaned_data.columns:
        child = ET.SubElement(entry, col)
        child.text = str(row[col])

# Guardar el archivo XML
tree = ET.ElementTree(root)
tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

print(f'Datos procesados y guardados en {xml_file_path}')
