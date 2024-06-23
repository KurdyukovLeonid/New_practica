my_dict = {'Leonid': 1998, 'Lydmila': 1992}
print(my_dict)
print(my_dict['Lydmila'])
print(my_dict.get('Valeria', 'Такого ключа нет'))
my_dict.update({'Oleg': 1994,
               'Misha': 1996})
pop_my_dict = my_dict.pop('Leonid')
print(pop_my_dict)
print(my_dict)

my_set = {1, 1, 'hello', 'hello'}
print(my_set)
my_set.add(5)
my_set.add('bye')
my_set.remove(1)
print(my_set)