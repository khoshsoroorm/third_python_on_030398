# prime num with i**2 < n

num_1 = 13

i = 2
is_prime = True

while i ** 2 < num_1:
    if num_1 % i == 0:
        is_prime = False
        break
    i = i + 1

print(is_prime)
