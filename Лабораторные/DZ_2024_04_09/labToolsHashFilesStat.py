import hashlib
import os
import time
from typing import Dict, List

def format_time(seconds: float) -> str:
    """
    Форматирует время в секундах, используя подходящие приставки (милли-, микро-, нано-).

    Параметры:
    seconds (float): Время в секундах.

    Возвращает:
    str: Отформатированная строка времени с подходящей приставкой.
    """
    if seconds >= 1:
        return f"{seconds:.3f} с"
    elif seconds >= 0.001:
        return f"{seconds * 1000:.3f} мс"
    elif seconds >= 0.000001:
        return f"{seconds * 1_000_000:.3f} мкс"
    else:
        return f"{seconds * 1_000_000_000:.3f} нс"

def HashTimeTable(path: str, hash_names: List[str] = None, recursive: bool = False, exclude_dirs: list = [], exclude_extensions: list = [], repeat: int = 10) -> Dict[str, Dict[str, float]]:
    """
    Создает таблицу с временем выполнения хеширования для файлов в указанной директории.

    Параметры:
    path (str): Путь к директории, которую нужно проанализировать.
    hash_names (List[str]): Список названий алгоритмов хеширования (например, ['sha256', 'md5']). Если None, будут использованы все доступные алгоритмы.
    recursive (bool): Если True, подкаталоги также будут проанализированы.
    exclude_dirs (list): Список директорий, которые нужно исключить из анализа.
    exclude_extensions (list): Список расширений файлов, которые нужно исключить из анализа.
    repeat (int): Количество повторений хеширования для каждого файла для получения более точных результатов.

    Возвращает:
    Dict[str, Dict[str, float]]: Словарь, где ключи - названия алгоритмов хеширования, а значения - словари с временем выполнения.
    """
    if hash_names is None:
        hash_names = hashlib.algorithms_guaranteed

    time_stats = {hash_name: {'total': 0.0, 'count': 0, 'min': float('inf'), 'max': 0.0} for hash_name in hash_names}

    for root, dirs, files in os.walk(path):
        if not recursive:
            dirs[:] = []
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for filename in files:
            if os.path.splitext(filename)[1][1:].lower() in [ext.lower() for ext in exclude_extensions]:
                continue

            file_path = os.path.join(root, filename)

            for hash_name in hash_names:
                hashfunc = getattr(hashlib, hash_name, None)
                if hashfunc is None:
                    print(f"Hash function '{hash_name}' is not available in hashlib.")
                    continue

                try:
                    with open(file_path, 'rb') as file:
                        file_content = file.read()
                    
                    elapsed_times = []
                    for _ in range(repeat):
                        start_time = time.perf_counter()
                        if hash_name.startswith('shake_'):
                            hashfunc(file_content).hexdigest(128)  # Или другая длина по вашему выбору
                        else:
                            hashfunc(file_content).hexdigest()
                        end_time = time.perf_counter()
                        elapsed_times.append(end_time - start_time)
                    
                    elapsed_time = sum(elapsed_times) / repeat

                    time_stats[hash_name]['total'] += elapsed_time
                    time_stats[hash_name]['count'] += 1
                    time_stats[hash_name]['min'] = min(time_stats[hash_name]['min'], elapsed_time)
                    time_stats[hash_name]['max'] = max(time_stats[hash_name]['max'], elapsed_time)
                except Exception as e:
                    print(f"Error processing {file_path} with {hash_name}: {e}")

    for hash_name, stats in time_stats.items():
        if stats['count'] > 0:
            stats['average'] = stats['total'] / stats['count']
        else:
            stats['average'] = 0.0

    return time_stats