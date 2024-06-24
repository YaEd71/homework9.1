def is_odd(number):
    return number % 2 != 0

def square(number):
    return number * number
numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10] # Входные данные

odd_numbers = filter(is_odd, numbers) # Применяем фильтр для отбора нечетных чисел

odd_squares = map(square, odd_numbers) # Применяем map для возведения в квадрат отобранных нечетных чисел

result = list(odd_squares) # Конвертируем генератор в список

print(result)