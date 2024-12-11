# 📚 Консольное приложение для управления библиотекой

## Описание проекта
Это консольное приложение для управления библиотекой книг. С помощью него можно:
- Добавлять книги.
- Удалять книги.
- Редактировать статус книги.
- Искать книги по различным параметрам.
- Выводить список всех книг.

Каждая книга содержит следующие данные:
- **ID**: уникальный идентификатор (генерируется автоматически).
- **Название**: название книги.
- **Автор**: автор книги.
- **Год**: год издания книги.
- **Статус**: текущее состояние книги (например, "в наличии", "выдана").

---

## Функционал
### Основные возможности:
1. **Добавление книги**  
   Пользователь вводит данные о книге: название, автор, год издания. Книга добавляется с уникальным ID и статусом "в наличии".

2. **Удаление книги**  
   Пользователь вводит ID книги для удаления, и запись удаляется из базы данных.

3. **Редактирование статуса книги**  
   Пользователь может изменить статус книги (например, "выдана" или "в наличии") по её ID.

4. **Поиск книг**  
   Возможность поиска книг по названию, автору или году издания. Если передано несколько параметров, то осуществляется фильтрация по всем из них.

5. **Вывод списка всех книг**  
   Отображение всех книг в библиотеке в виде таблицы с заголовками.

---

## Установка и запуск

1. Убедитесь, что на вашем компьютере установлен **Python 3.9+**.
2. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/username/library-management.git
3. Перейдите в папку проекта:
   ```bash
   cd library-management
4. Запустите программу:
   ```bash
   python main.py

### Доступные команды
1. Добавить книгу: Введите команду 1:
   ```bash
   Введите название книги: Гарри Поттер
   Введите автора книги: Джоан Роулинг
   Введите год издания книги: 1997

2. Показать все книги: Введите команду 4:

   ```bash
   ID: 1, Title: Python, Author: Mark Lutc, Year: 1999, Status: выдана

3. Найти книгу: Введите команду 3:

   ```bash
   Введите поисковый запрос (название, автор или год): Python
   ID: 1, Title: Python, Author: Mark Lutc, Year: 1999, Status: выдана

4. Редактировать статус: Введите команду 5:

   ```bash
   Введите команду: edit
   Введите ID книги для изменения: 1
   Введите новый статус книги: выдана

5. Удалить книгу: Введите команду 2:

   ```bash
   Введите ID книги для удаления: 2
   Книга с ID 2 удалена.

6. Выход из программы: Введите команду 6

## Тесты
 Введите команду:
   ```bash
   pytest test.py
   ```

### Технологии:
   Язык: Python 3.9+
   Хранилище данных: JSON
   Тесты: Pytest








