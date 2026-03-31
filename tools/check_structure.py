#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/check_structure.py
Проверка наличия файлов задач в проекте

Использование:
    python tools/check_structure.py

Вывод:
    PASS — если все файлы задач на месте
    FAIL — если каких-то файлов нет
"""

import sys
from pathlib import Path


def main():
    """Проверяет наличие файлов задач"""
    
    # Определяем ожидаемые файлы (подходит для обоих проектов)
    expected_files = [
        "tests/task_01_*.py",
        "tests/task_02_*.py",
        "tests/task_03_*.py",
        "tests/task_04_*.py",
        "tests/task_05_*.py",
        "tests/task_06_*.py",
    ]
    
    # Также проверяем базовые файлы проекта
    required_files = [
        "pytest.ini",
        "requirements.txt",
    ]
    
    all_exist = True
    missing = []
    
    # Проверяем файлы задач
    for pattern in expected_files:
        matches = list(Path(".").glob(pattern))
        if not matches:
            all_exist = False
            missing.append(pattern)
    
    # Проверяем базовые файлы
    for file_path in required_files:
        if not Path(file_path).exists():
            all_exist = False
            missing.append(file_path)
    
    # Вывод результата (для bash grep)
    if all_exist:
        print("PASS")
        sys.exit(0)
    else:
        print(f"FAIL: Missing {', '.join(missing)}")
        sys.exit(1)


if __name__ == "__main__":
    main()