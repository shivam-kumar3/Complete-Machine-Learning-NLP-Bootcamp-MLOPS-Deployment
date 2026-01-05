# =====================================================
# PYTHON OPERATORS 
# =====================================================


# -----------------------------------------------------
# 1. Arithmetic Operators
# -----------------------------------------------------

a = 10
b = 3

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division (float)
print(a // b)   # Floor Division
print(a % b)    # Modulus
print(a ** b)   # Exponentiation


# -----------------------------------------------------
# 2. Comparison (Relational) Operators
# -----------------------------------------------------

x = 10
y = 20

print(x == y)   # Equal to
print(x != y)   # Not equal to
print(x > y)    # Greater than
print(x < y)    # Less than
print(x >= y)   # Greater than or equal to
print(x <= y)   # Less than or equal to


# -----------------------------------------------------
# 3. Assignment Operators
# -----------------------------------------------------

a = 10
a += 5
print(a)

a -= 3
print(a)

a *= 2
print(a)

a /= 4
print(a)

a //= 2
print(a)

a %= 3
print(a)

a **= 2
print(a)


# -----------------------------------------------------
# 4. Logical Operators
# -----------------------------------------------------

x = True
y = False

print(x and y)
print(x or y)
print(not x)


# -----------------------------------------------------
# 5. Bitwise Operators
# -----------------------------------------------------

a = 5      # 101
b = 3      # 011

print(a & b)   # AND
print(a | b)   # OR
print(a ^ b)   # XOR
print(~a)      # NOT
print(a << 1)  # Left shift
print(a >> 1)  # Right shift


# -----------------------------------------------------
# 6. Membership Operators
# -----------------------------------------------------

nums = [1, 2, 3, 4]

print(2 in nums)
print(5 not in nums)


# -----------------------------------------------------
# 7. Identity Operators
# -----------------------------------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)


# -----------------------------------------------------
# 8. Operator Precedence
# -----------------------------------------------------

result = 10 + 3 * 2 ** 2
print(result)

# Precedence order:
# ** → * / // % → + -


# -----------------------------------------------------
# 9. Short-Circuit Evaluation
# -----------------------------------------------------

x = 0
y = 10

print(x != 0 and y / x > 1)   # Safe due to short-circuit
print(x == 0 or y / x > 1)    # Safe due to short-circuit


# -----------------------------------------------------
# 10. Ternary (Conditional) Operator
# -----------------------------------------------------

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)


# -----------------------------------------------------
# 11. Operator Overloading (Intro Example)
# -----------------------------------------------------

print(10 + 20)
print("Data" + "Science")
print([1, 2] + [3, 4])


# -----------------------------------------------------
# 12. Common Operator Pitfalls (Interview)
# -----------------------------------------------------

print(0 == False)    # True
print(0 is False)    # False

print([] == False)  # False
print([] is False)  # False
