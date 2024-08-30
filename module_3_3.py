
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(2, 3)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [3, 'Hello', True]
values_dict = {'a': 2.3, 'b': 'How are you?', 'c': 5}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
