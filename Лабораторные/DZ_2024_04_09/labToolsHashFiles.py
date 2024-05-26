import hashlib
import os
from typing import Callable, Dict

def HashTable(path: str, hashname: str, recursive: bool = False, exclude_dirs: list = [], exclude_extensions: list = []) -> Dict[str, str]:
   """
   Создает таблицу с хешами файлов в указанной директории.
   
   Параметры:
   path (str): Путь к директории, которую нужно проанализировать.
   hashname (str): Название алгоритма хеширования (например, 'sha256', 'md5').
   recursive (bool): Если True, подкаталоги также будут проанализированы.
   exclude_dirs (list): Список директорий, которые нужно исключить из анализа.
   exclude_extensions (list): Список расширений файлов, которые нужно исключить из анализа.
   
   Возвращает:
   Dict[str, str]: Словарь, где ключи - относительные пути к файлам, а значения - соответствующие хеши.
   """
   hash_table = {}
   hashfunc = getattr(hashlib, hashname)
   
   for root, dirs, files in os.walk(path):
       if not recursive:
           dirs[:] = []
       dirs[:] = [d for d in dirs if d not in exclude_dirs]
       
       for filename in files:
           if os.path.splitext(filename)[1][1:].lower() in [ext.lower() for ext in exclude_extensions]:
               continue
           
           file_path = os.path.join(root, filename)
           relative_path = os.path.relpath(file_path, path)
           
           with open(file_path, 'rb') as file:
               file_hash = hashfunc(file.read()).hexdigest()
               hash_table[relative_path] = file_hash
   
   return hash_table