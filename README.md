# 🎯 Playwright Basics — 6 задач

**Темы:** Локаторы, действия, простые проверки

> **Срок:** 12.04.2026  
> **Формат:** Пуш в репозиторий → автопроверка в GitHub Classroom

---

### 📁 Структура проекта

```
playwright-basics-6tasks/
├── .github/
│   └── workflows/
│       └── classroom.yml          # Автопроверка
├── tests/
│   ├── task_01_navigate.py        # Задача 1
│   ├── task_02_click_text.py      # Задача 2
│   ├── task_03_click_role.py      # Задача 3
│   ├── task_04_fill_input.py      # Задача 4
│   ├── task_05_visibility.py      # Задача 5
│   └── task_06_get_text.py        # Задача 6
├── tools/
│   ├── check_structure.py
│   └── generate_summary.py
├── pytest.ini
├── requirements.txt
└── README.md                      # Задание для студентов
```

---

## 📋 Задания (6 задач)

### ✅ Задача 1: Навигация и проверка URL
**Файл:** `tests/task_01_navigate.py`

```python
# Задание:
# 1. Открой страницу https://www.saucedemo.com/
# 2. Проверь, что URL содержит "saucedemo"

from playwright.sync_api import Page, expect

def test_navigate_and_check_url(page: Page):
    pass
```

**Баллы:** 10

---

### ✅ Задача 2: Клик по тексту (get_by_text)
**Файл:** `tests/task_02_click_text.py`

```python
# Задание:
# 1. Открой https://www.saucedemo.com/
# 2. Найди кнопку "Login" по тексту
# 3. Кликни по ней

from playwright.sync_api import Page

def test_click_by_text(page: Page):
    pass
```

**Баллы:** 10

---

### ✅ Задача 3: Клик по роли (get_by_role)
**Файл:** `tests/task_03_click_role.py`

```python
# Задание:
# 1. Открой https://www.saucedemo.com/
# 2. Найди кнопку по роли "button" и имени "Login"
# 3. Кликни по ней

from playwright.sync_api import Page

def test_click_by_role(page: Page):
    pass
```

**Баллы:** 15

---

### ✅ Задача 4: Заполнение поля (fill)
**Файл:** `tests/task_04_fill_input.py`

```python
# Задание:
# 1. Открой https://www.saucedemo.com/
# 2. Заполни поле username: "standard_user"
# 3. Заполни поле password: "secret_sauce"
# 4. Кликни Login
# 5. Проверь, что попал на /inventory.html

from playwright.sync_api import Page, expect

def test_fill_and_login(page: Page):
    pass
```

**Баллы:** 20

---

### ✅ Задача 5: Проверка видимости (is_visible)
**Файл:** `tests/task_05_visibility.py`

```python
# Задание:
# 1. Открой https://www.saucedemo.com/
# 2. Проверь, что поле username видимо
# 3. Проверь, что кнопка Login видима

from playwright.sync_api import Page, expect

def test_element_visibility(page: Page):
    pass
```

**Баллы:** 15

---

### ✅ Задача 6: Получение текста (text_content)
**Файл:** `tests/task_06_get_text.py`

```python
# Задание:
# 1. Авторизуйся (standard_user / secret_sauce)
# 2. Получи текст заголовка страницы
# 3. Проверь, что он содержит "Products"

from playwright.sync_api import Page, expect

def test_get_text(page: Page):
    pass
```

**Баллы:** 30

---

## 📊 Критерии оценки

| Задача | Баллы |
|--------|-------|
| 1. Навигация | 10 |
| 2. Клик по тексту | 10 |
| 3. Клик по роли | 15 |
| 4. Заполнение поля | 20 |
| 5. Проверка видимости | 15 |
| 6. Получение текста | 30 |
| **ИТОГО** | **100** |

### Шкала оценок
| Баллы | Оценка |
|-------|--------|
| 90–100 | 🟢 Отлично |
| 70–89 | 🟡 Хорошо |
| 50–69 | 🟠 Удовлетворительно |
| <50 | 🔴 Требуется доработка |





## 📋 Задания (6 задач)

| № | Тема | Файл | Баллы |
|---|------|------|-------|
| 1 | expect() ожидания | `task_01_expect_wait.py` | 15 |
| 2 | Выпадающий список | `task_02_dropdown.py` | 20 |
| 3 | Чекбоксы | `task_03_checkbox.py` | 15 |
| 4 | Hover + tooltip | `task_04_hover.py` | 20 |
| 5 | Подсчёт элементов | `task_05_count.py` | 15 |
| 6 | Мини-сценарий | `task_06_scenario.py` | 35 |
| **ИТОГО** | | | **120** |

---

## 📊 Критерии оценки

| Компонент | Баллы |
|-----------|-------|
| 📁 Структура проекта | 10 |
| 🧹 Линтинг (flake8) | 15 |
| ✅ Задача 1: expect() | 15 |
| ✅ Задача 2: Dropdown | 20 |
| ✅ Задача 3: Checkbox | 15 |
| ✅ Задача 4: Hover | 20 |
| ✅ Задача 5: Count | 15 |
| ✅ Задача 6: Scenario | 35 |
| **ИТОГО** | **145** |

### Шкала оценок
| Баллы | Оценка | Статус |
|-------|--------|--------|
| 130–145 | 🟢 Отлично | Зачтено |
| 100–129 | 🟡 Хорошо | Зачтено |
| 70–99 | 🟠 Удовлетворительно | Зачтено |
| <70 | 🔴 Требуется доработка | Не зачтено |

---
---

## 🚀 Быстрый старт

```bash
# 1. Установи зависимости
pip install -r requirements.txt
playwright install chromium

# 2. Запусти все тесты
pytest tests/ -v

# 3. Запусти одну задачу
pytest tests/task_01_navigate.py -v

# 4. Отправь на проверку
git add .
git commit -m "feat: completed task 1"
git push
```

---

*GitHub Classroom Autograder • 2026.03*
