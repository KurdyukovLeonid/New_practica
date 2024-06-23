immutable_var = (1, 'hello', True, [5, 10])
print(immutable_var)

# immutable_var[0] = 2
# print(immutable_var)
# Нельзя изменить значение элементов кортежа,
# потому что кортеж является неизменяемым типом данных.

mutable_list = [2, 'bye', False]
mutable_list[0] = 5
print(mutable_list)