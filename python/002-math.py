addition = 4 + 5
subtraction = 5 - 2
division = 7 / 2
multiplication = 7 * 2


print("addition -> ", addition)

print("subtraction -> ", subtraction)

print("division -> ", division)

print("multiplication -> ", multiplication)

exponentiation = 4 ** 4
floor_division = 16 // 5
modulo = 7 % 3



print("exponentiation -> ", exponentiation)

print("floor_division -> ", floor_division)

print("modulo -> ", modulo)

add_assign = 5
add_assign += 7

print("add_assign -> ", add_assign)

# Order of executions

# Expressions: (9 - 7) * 2 ** 3 + 10 % 6 // -1 * 2 - 1
# Step 1: 2 * 2 ** 3 + 10 % 6 // -1 * 2 - 1
# Step 2: 2 * 8 + 10 % 6 // -1 * 2 - 1
# Step 3: 16 + -8 - 1
# Step 4: 7

# Float Approximation error & How to solve
ex1 = 1.23 + 2.80
print (ex1) # 4.0299999999999

# To Solve - Option 1
ex2 = (123 + 280) / 100
print(f'Dividing by 100 => {ex2}')

print (f'Round => {round(ex1, 2)}')