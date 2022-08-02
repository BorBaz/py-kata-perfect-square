import math

# Mine
def find_next_square(sq):
    number = math.sqrt(sq)

    if number % 1 != 0.0:
        return -1

    return (int(number) + 1) ** 2


# Best
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1


print(find_next_square(20))
print(find_next_square(25))
print(find_next_square(23))
print(find_next_square(3))
print(find_next_square(4))
