
def apply_all_func(int_list, *functions):
    results = {}
    for f in functions:
        results.update({f.__name__: f(int_list)}) #добавляет в качестве ключа имя функции, в значение - список,
    #print(results)
    return results                                           




print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

#functions = [min, max, len, sorted, sum]