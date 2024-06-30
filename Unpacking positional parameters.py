def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [5.25, False, 'замена']
values_dict = {'a': 10, 'b': 15, 'c': 20}
values_list_2 = ['проверка', 123456]

print_params()
print_params(b=25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(** values_dict)
print_params(*values_list_2, 42)