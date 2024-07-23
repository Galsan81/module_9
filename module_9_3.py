first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(l)-len(n) for l, n in zip(first, second) if len(l) != len(n))
print(list(first_result))
second_result = (True if len(first[l])==len(second[l]) else False for l in range (len(first)))
print(list(second_result))
#for elem in first_result:
