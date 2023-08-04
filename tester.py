import password_generator

"""
Firstly, we need to know how many combination we can possibly have for the
3 conditions that can be true or false, that is, has_upper, has_numbers, has_symbols.

In order to find the total combinations we have to multiply the total outcomes for
each condition. Each condition has 2 outcomes, and there are 3 conditions, so we have
2 * 2 * 2 or 2**3 = 8

There are 8 different combinations.
"""
# test passwords in which only the length changed and all other conditions are false
for i in range(100):
    print(password_generator.password_algorithm(12, False, False, False))
print("test passwords with no options END =================\n")

# test passwords with uppercase option only
for i in range(100):
    print(password_generator.password_algorithm(12, True, False, False))
print("test passwords with uppercase option only END =================\n")

# test passwords with numbers option only
for i in range(100):
    print(password_generator.password_algorithm(12, False, True, False))
print("test passwords with numbers option only END =================\n")

# test passwords with symbols option only
for i in range(100):
    print(password_generator.password_algorithm(12, False, False, True))
print("test passwords with symbols option only END =================\n")

# test passwords with both upper cases and numbers
for i in range(100):
    print(password_generator.password_algorithm(12, True, True, False))
print("test passwords with both upper cases and numbers END =================\n")

# test passwords with both upper cases and symbols
for i in range(100):
    print(password_generator.password_algorithm(12, True, False, True))
print("test passwords with both upper cases and symbols END =================\n")

# test passwords with both numbers and symbols
for i in range(100):
    print(password_generator.password_algorithm(12, False, True, True))
print("test passwords with both numbers and symbols END =================\n")

# test passwords with all upper cases, numbers, and symbols
for i in range(100):
    print(password_generator.password_algorithm(12, True, True, True))
print("test passwords with all upper cases, numbers, and symbols END =================\n")