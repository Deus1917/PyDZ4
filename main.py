import math


def poisk_a(b, c):
    a = math.sqrt(c ** 2 - b ** 2)
    print(f"Число а равно {a}, число b равно {b}, число с равно {c}")


def poisk_b(a, c):
    b = math.sqrt(c ** 2 - a ** 2)
    print(f"Число а равно {a}, число b равно {b}, число с равно {c}")


def poisk_c(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    print(f"Число а равно {a}, число b равно {b}, число с равно {c}")


user_solution = (input("Какое число вы хотите найти:a,b или с? "))
if user_solution == "a":
    b = int(input("Введите число b - "))
    c = int(input("Введите число с - "))
    poisk_a(b, c)
elif user_solution == "b":
    a = int(input("Введите число а - "))
    c = int(input("Введите число с - "))
    poisk_b(a, c)
elif user_solution == "c":
    a = int(input("Введите число а - "))
    b = int(input("Введите число b - "))
    poisk_c(a, b)
else:
    print("Error,try again")
