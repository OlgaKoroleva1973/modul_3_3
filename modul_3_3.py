def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [3, 'list', False]
values_dict = {'a': 10, 'b': 25, 'c': 'print'}
values_list_2 = ['list', 5]
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)