# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Декораторы
# Задание 1
# Создайте функцию, возвращающую список со всеми
# простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько
# секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.
# Задание 2
# Добавьте к первому заданию возможность передавать
# границы диапазона для поиска всех простых чисел.


import time


def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        allTime = time.time() - start
        print(f'Поиск простых чисел  выполнялся {allTime} с.')
        print(f'Простые числа в диапазоне от {args[0]} до {args[1]}: ')
        print(f'Всего {len(result)} чисел')
        return result
    
    return wrapper


@timer
def prime_numbers(n_start: int, n_stop: int):
    n: int = n_start
    primeList = []
    
    while n <= n_stop:
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            primeList.append(n)
        n += 1
    return primeList


print(prime_numbers(100, 10000))





# Задание 3
# Каждый год ваша компания предоставляет различным
# государственным организациям финансовую отчетность.
# В зависимости от организации форматы отчетности разные. Используя механизм декораторов, решите вопрос
# отчетности для организаций.



class the_plant_of_childrens_pots:
    def __init__(self, metall: int,pays: int):
        self.__metall: int = metall
        self.__pays: int = pays
    
    