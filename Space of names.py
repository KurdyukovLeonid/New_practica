calls = 0

def count_calls():
    global calls
    calls += 1




def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(line_, list_):
    count_calls()
    for i in list_:
        if line_.lower() == i.lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
