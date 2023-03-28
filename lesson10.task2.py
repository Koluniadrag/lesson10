#
def digital():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = a ** 2 / b
        return result
    except ValueError:
        print("Ошибка: одно или оба введенных значения не являются числами.")
    except ZeroDivisionError:
        print("Ошибка: второе введенное значение равно нулю (деление на ноль невозможно).")

result = digital()
if result is not None:
    print(f"Результат: {result}")

