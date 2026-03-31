#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/generate_summary.py
Генерация итогового Summary для GitHub Actions

Использование:
    python tools/generate_summary.py >> $GITHUB_STEP_SUMMARY

Настройка max_score:
    - Через env: MAX_SCORE=110 python tools/generate_summary.py
    - Через файл: создать tools/max_score.txt с числом
    - По умолчанию: 110
"""

import os
import sys
from pathlib import Path


def read_score(file_path, default=0):
    """Читает балл из файла, возвращает default если ошибка"""
    try:
        content = Path(file_path).read_text().strip()
        return int(content) if content else default
    except:
        return default


def get_max_score():
    """Получает максимальный балл из env, файла или default"""
    # 1. Проверяем переменную окружения
    env_score = os.environ.get("MAX_SCORE")
    if env_score:
        return int(env_score)
    
    # 2. Проверяем файл конфигурации
    config_file = Path("tools/max_score.txt")
    if config_file.exists():
        return read_score(config_file, 110)
    
    # 3. По умолчанию
    return 110


def get_grade(total_score, max_score):
    """Определяет оценку по проценту"""
    percentage = (total_score * 100) // max_score if max_score > 0 else 0
    
    if percentage >= 90:
        return "🟢 Отлично", "Зачтено", percentage
    elif percentage >= 70:
        return "🟡 Хорошо", "Зачтено", percentage
    elif percentage >= 50:
        return "🟠 Удовлетворительно", "Зачтено", percentage
    else:
        return "🔴 Требуется доработка", "Не зачтено", percentage


def main():
    """Генерирует итоговый отчёт"""
    
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    
    # Считываем баллы
    structure_score = read_score("tools/output/structure_score.txt", 0)
    
    # Считываем баллы за задачи
    task_scores = []
    task_files = sorted(Path("tools/output").glob("task_*_score.txt"))
    
    for task_file in task_files:
        score = read_score(task_file, 0)
        task_scores.append(score)
    
    total_task_score = sum(task_scores)
    grand_total = structure_score + total_task_score
    
    # Получаем max_score (явно!)
    max_score = get_max_score()
    
    grade, status, percentage = get_grade(grand_total, max_score)
    
    # Формируем отчёт
    lines = []
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# 🏆 ИТОГОВАЯ ОЦЕНКА")
    lines.append("")
    lines.append("| Параметр | Значение |")
    lines.append("|----------|----------|")
    lines.append(f"| 💯 Баллы | **{grand_total} / {max_score}** |")
    lines.append(f"| 📈 Процент | **{percentage}%** |")
    lines.append(f"| 🎓 Оценка | **{grade}** |")
    lines.append(f"| ✅ Статус | **{status}** |")
    lines.append("")
    
    lines.append("## 📋 Детализация по задачам")
    lines.append("")
    lines.append("| Задача | Баллы | Статус |")
    lines.append("|--------|-------|--------|")
    
    # Баллы за каждую задачу (из workflow matrix)
    task_points = [10, 10, 15, 20, 15, 30]  # Для Проекта 1
    # task_points = [15, 20, 15, 20, 15, 35]  # Для Проекта 2 (раскомментируй)
    
    for i, score in enumerate(task_scores, 1):
        task_max = task_points[i-1] if i <= len(task_points) else 20
        status_icon = "✅" if score > 0 else "❌"
        lines.append(f"| Задача {i} | {score} / {task_max} | {status_icon} |")
    
    lines.append(f"| **ИТОГО** | **{grand_total} / {max_score}** | |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*GitHub Classroom Autograder • 2026.03*")
    lines.append("")
    
    # Вывод
    output = "\n".join(lines)
    
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(output)
    else:
        print(output)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())