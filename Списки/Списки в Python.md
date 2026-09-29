## Введение — Списки

---
Одна переменная хранит одно значение. Но что если нужно хранить сто имён, тысячу цен, миллион записей? Списки — это первая настоящая структура данных. Они позволяют работать с коллекциями объектов как с единым целым. Корзина в интернет-магазине — список. Лента новостей — список. Результаты поиска — список. Без списков ты не можешь написать ни одно реальное приложение которое работает с больше чем одним объектом.
___


### Что такое список?

Список (`list`) — это упорядоченная коллекция элементов. Элементы могут быть любого типа и могут повторяться.

python

```python
numbers = [1, 2, 3, 4, 5]
names = ["Иван", "Мария", "Алексей"]
mixed = [1, "привет", True, 3.14, None]
empty = []
```

---

### Индексация и срезы

Работает так же как со строками:

python

```python
fruits = ["яблоко", "груша", "банан", "манго"]

print(fruits[0])    # яблоко
print(fruits[-1])   # манго
print(fruits[1:3])  # ["груша", "банан"]
print(fruits[::-1]) # ["манго", "банан", "груша", "яблоко"]
```

---

### Изменение элементов

В отличие от строк списки изменяемы:

python

```python
fruits = ["яблоко", "груша", "банан"]
fruits[1] = "апельсин"
print(fruits)   # ["яблоко", "апельсин", "банан"]
```

---

### Основные методы

#### Добавление элементов

python

```python
fruits = ["яблоко", "груша"]

fruits.append("банан")       # добавляет в конец
print(fruits)                # ["яблоко", "груша", "банан"]

fruits.insert(1, "манго")    # вставляет по индексу
print(fruits)                # ["яблоко", "манго", "груша", "банан"]

fruits.extend(["киви", "лимон"])  # добавляет несколько элементов
print(fruits)                # ["яблоко", "манго", "груша", "банан", "киви", "лимон"]
```

#### Удаление элементов

python

```python
fruits = ["яблоко", "груша", "банан", "груша"]

fruits.remove("груша")   # удаляет первое вхождение
print(fruits)            # ["яблоко", "банан", "груша"]

fruits.pop()             # удаляет последний элемент и возвращает его
fruits.pop(0)            # удаляет элемент по индексу

del fruits[0]            # удаляет по индексу

fruits.clear()           # очищает весь список
```

#### Поиск и сортировка

python

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(numbers.index(5))    # 4 — индекс первого вхождения
print(numbers.count(1))    # 2 — сколько раз встречается
print(len(numbers))        # 8 — длина списка

numbers.sort()             # сортировка по возрастанию
print(numbers)             # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True) # сортировка по убыванию
print(numbers)             # [9, 6, 5, 4, 3, 2, 1, 1]

numbers.reverse()          # разворачивает список
```

#### Копирование

python

```python
a = [1, 2, 3]
b = a           # не копия — обе переменные указывают на один список
b = a.copy()    # настоящая копия
b = a[:]        # тоже копия через срез
```

---

### Перебор списка

python

```python
fruits = ["яблоко", "груша", "банан"]

for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

---

### Проверка вхождения

python

```python
fruits = ["яблоко", "груша", "банан"]

print("груша" in fruits)     # True
print("манго" in fruits)     # False
print("манго" not in fruits) # True
```

---

### 
Списковые включения (list comprehension)

Короткий способ создать список:

python

```python
# обычный способ
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

# list comprehension
squares = [i ** 2 for i in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
```

С условием:

python

```python
# только чётные числа
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)   # [2, 4, 6, 8, 10]
```

---

### Вложенные списки

python

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])   # 6 — вторая строка, третий элемент

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
```

---

### Полезные встроенные функции

python

```python
numbers = [3, 1, 4, 1, 5, 9]

print(sum(numbers))    # 23
print(min(numbers))    # 1
print(max(numbers))    # 9
print(sorted(numbers)) # [1, 1, 3, 4, 5, 9] — не меняет оригинал
```

---

### Задание

1. Дан список чисел:

python

```python
numbers = [5, 3, 8, 1, 9, 2, 7, 4, 6]
```

Напиши код который:

- Выводит максимальный и минимальный элемент без `max()` и `min()`
- Выводит сумму всех элементов без `sum()`
- Выводит список отсортированный по убыванию

2. Напиши функцию `remove_duplicates(lst)` которая принимает список и возвращает новый список без повторяющихся элементов, сохраняя порядок:

python

```python
remove_duplicates([1, 2, 2, 3, 1, 4])   # [1, 2, 3, 4]
```

3. Напиши функцию `flatten(matrix)` которая принимает вложенный список и возвращает одномерный:

python

```python
flatten([[1, 2], [3, 4], [5, 6]])   # [1, 2, 3, 4, 5, 6]
```

4. Используя list comprehension создай:

- Список квадратов чисел от 1 до 10
- Список только тех слов из списка длиннее 4 букв

python

```python
words = ["кот", "питон", "код", "программа", "list"]
```

---

#### Задание 1

python

```python
numbers = [5, 3, 8, 1, 9, 2, 7, 4, 6]

# максимум и минимум
max_num = numbers[0]
min_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n
print(f"Макс: {max_num}, Мин: {min_num}")   # Макс: 9, Мин: 1

# сумма
total = 0
for n in numbers:
    total += n
print(f"Сумма: {total}")   # Сумма: 45

# сортировка по убыванию
print(sorted(numbers, reverse=True))   # [9, 8, 7, 6, 5, 4, 3, 2, 1]
```

---

#### Задание 2

python

```python
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))   # [1, 2, 3, 4]
```

---

#### Задание 3

python

```python
def flatten(matrix):
    return [item for row in matrix for item in row]

print(flatten([[1, 2], [3, 4], [5, 6]]))   # [1, 2, 3, 4, 5, 6]
```

---

#### Задание 4

python

```python
squares = [i ** 2 for i in range(1, 11)]
print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

words = ["кот", "питон", "код", "программа", "list"]
long_words = [w for w in words if len(w) > 4]
print(long_words)   # ["питон", "программа"]
```
