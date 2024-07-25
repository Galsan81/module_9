'''Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое",
если результат 1ой функции будет простым числом и "Составное" в противном случае.
Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11'''

def is_prime(func):
    def wrapper(a,b,c):
        k = func(a, b, c)
        is_prime = True
        if k > 1:
            for i in range(2, k):
                if k%i == 0 and k!=2:
                    is_prime = False
            if is_prime==True :
                return f"Простое \n{k}"
            else:
                return f'Составное \n{k}'
        else:
            return f'Ни то ни сё \n{k}'
    return wrapper




@is_prime
def sum_three(a, b,c):

    return a + b + c

result = sum_three(3, 2, 7)
print(result)