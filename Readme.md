# 📚 Консольное приложение для управления библиотекой

## Описание проекта
Это консольное приложение для управления библиотекой книг. С помощью него можно добавлять книги, удалять, 
редактировать их статус, искать книги по различным параметрам, а также выводить список всех книг в удобном формате таблицы. 

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
   ```
## Доступные команды   

1. Введите команду: add
    ```bash
    Введите название книги: Гарри Поттер
    Введите автора книги: Джоан Роулинг
    Введите год издания: 1997
    Книга "Гарри Поттер" добавлена.
    ```
2. Введите команду: list
    ```bash
    ===============================================================
    ID  | Название        | Автор         | Год  | Статус   
    ===============================================================
    1   | Гарри Поттер    | Джоан Роулинг | 1997 | в наличии
    2   | Война и мир     | Лев Толстой   | 1869 | выдана   
    ===============================================================
   ```

3. Введите команду: list
    ```bash
    Введите название книги: Война и мир
    ===============================================================
    ID  | Название     | Автор         | Год  | Статус   
    ===============================================================
    2   | Война и мир  | Лев Толстой   | 1869 | выдана   
    ===============================================================
    ```

4. Редактирование статуса
    ```bash
    Введите команду: edit
    Введите ID книги для изменения: 1
    Введите новый статус книги: выдана
    Статус книги с ID 1 изменен.
   ```

5. Удаление книги
    ```bash
    Введите команду: remove
    Введите ID книги для удаления: 2
    Книга с ID 2 удалена.
   ```


## Технологии
**Язык: Python 3.9+**
**База данных: SQLite**


