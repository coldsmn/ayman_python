# Введите количество оценок
n = int(input("Введите количество оценок: "))

# Создадим список для хранения оценок
grades = []

# Считаем оценки и добавим их в список
for _ in range(n):
    grade = float(input("Введите оценку: "))
    grades.append(grade)

# Выведем оценки в том же порядке
print("Введенные оценки:", grades)

# Найдем среднюю оценку
average_grade = sum(grades) / n
print("Средняя оценка за урок:", average_grade)
