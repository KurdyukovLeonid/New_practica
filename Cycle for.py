numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 0

for i in numbers:
    for j in numbers:
        if i % j == 0:
            is_prime += 1
    if is_prime == 2:
        primes.append(i)
    else:
        not_primes.append(i)
        if 1 in not_primes:
            not_primes.remove(1)
    is_prime = 0

print('Primes:', primes)
print('Not primes:', not_primes)
