"""
A list contains a sequence of data surrounded by brackets
A tuple contains a sequence of data surrounded by parenthesis
Other than notation there seems to be little difference between the two
"""

# List example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple example
perfect_squares = (1, 4, 9, 15, 36)

# Display lengths
print(' # Primes = ' + str(len(prime_numbers)))
print(' # Squares = ' + str(len(perfect_squares)))
# Identical behavior when displaying lengths


# Iterate over both sequences
print('\n', )

for x in prime_numbers:
    print('Prime: ', x)

print('\n', )

for x in perfect_squares:
    print('Squares: ', x)
# Identical behavior when iterating


import sys

list_ex = [1, 2, 3, 'a', 'b', 'c', True, 3.14159]
tuple_ex = (1, 2, 3, 'a', 'b', 'c', True, 3.14159)

print('\n', )

print('List size =', sys.getsizeof(list_ex))
print('Tuple size =', sys.getsizeof(tuple_ex))