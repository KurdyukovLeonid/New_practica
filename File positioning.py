def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')
    for index, string in enumerate(strings):
        byte = file.tell()
        file.write(string + '\n')
        strings_positions[(index + 1, byte)] = string
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)