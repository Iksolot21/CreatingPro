import os
import csv
from datetime import datetime

def get_file_info(path, include_hidden=False, include_dirs=False):
    """
    Возвращает информацию о файлах в указанном каталоге в виде CSV-файла.
    
    Параметры:
    path (str): Путь к анализируемой директории.
    include_hidden (bool): Включать ли скрытые файлы и каталоги.
    include_dirs (bool): Включать ли информацию о каталогах.
    
    Возвращает:
    str: Путь к сгенерированному CSV-файлу.
    """
    file_info = []
    for root, dirs, files in os.walk(path):
        if not include_hidden:
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files[:] = [f for f in files if not f.startswith('.')]
        
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_ext = os.path.splitext(file)
            file_size = os.path.getsize(file_path)
            file_mod_time = os.path.getmtime(file_path)
            file_info.append({
                'full_path': file_path,
                'file_name': file_name,
                'file_ext': file_ext[1:],  # Удаляем начальную точку
                'file_size': file_size,
                'mod_time': datetime.fromtimestamp(file_mod_time).strftime('%Y-%m-%d %H:%M:%S')
            })
        
        if include_dirs:
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                file_info.append({
                    'full_path': dir_path,
                    'file_name': directory,
                    'file_ext': '',
                    'file_size': '',
                    'mod_time': ''
                })
    
    csv_file = f"file_info_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['full_path', 'file_name', 'file_ext', 'file_size', 'mod_time']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(file_info)
    
    return os.path.abspath(csv_file)

