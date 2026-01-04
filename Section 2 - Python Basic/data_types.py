
# =====================================================
# PYTHON DATA TYPES – COMPLETE GUIDE
# =====================================================


# -----------------------------------------------------
# 1. Numeric Data Types
# -----------------------------------------------------

# int
a = 10
print(a, type(a))

# float
b = 3.14
print(b, type(b))

# complex
c = 2 + 3j
print(c, type(c))


# -----------------------------------------------------
# 2. Boolean Data Type
# -----------------------------------------------------

x = True
y = False
print(x, type(x))
print(y, type(y))


# -----------------------------------------------------
# 3. String Data Type
# -----------------------------------------------------

name = "Shivam"
msg = 'Python Data Types'
multi_line = """This is
a multi-line
string"""

print(name, msg)
print(multi_line)


# -----------------------------------------------------
# 4. Sequence Data Types
# -----------------------------------------------------

# List (Mutable)
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers, type(numbers))

# Tuple (Immutable)
coords = (10, 20)
print(coords, type(coords))

# Range
r = range(1, 6)
print(list(r), type(r))


# -----------------------------------------------------
# 5. Set Data Types
# -----------------------------------------------------

# set (unordered, unique)
s = {1, 2, 3, 3}
print(s, type(s))

# frozenset (immutable set)
fs = frozenset([1, 2, 3])
print(fs, type(fs))


# -----------------------------------------------------
# 6. Mapping Data Type
# -----------------------------------------------------

# Dictionary (key-value)
student = {
    "name": "Shivam",
    "age": 25,
    "course": "Data Science"
}
print(student, type(student))


# -----------------------------------------------------
# 7. None Data Type
# -----------------------------------------------------

x = None
print(x, type(x))


# -----------------------------------------------------
# 8. Type Checking
# -----------------------------------------------------

a = 10
print(isinstance(a, int))
print(type(a))


# -----------------------------------------------------
# 9. Type Conversion (Type Casting)
# -----------------------------------------------------

x = "100"
x = int(x)
print(x, type(x))

y = 5
y = float(y)
print(y, type(y))

z = 3.14
z = str(z)
print(z, type(z))


# -----------------------------------------------------
# 10. Mutable vs Immutable
# -----------------------------------------------------

# Immutable Example
x = 10
y = x
y = 20
print(x, y)

# Mutable Example
a = [1, 2, 3]
b = a
b.append(4)
print(a, b)


# -----------------------------------------------------
# 11. Object Identity (Memory Reference)
# -----------------------------------------------------

x = 10
y = 10
print(id(x), id(y))

a = [1, 2]
b = [1, 2]
print(id(a), id(b))


# -----------------------------------------------------
# 12. Built-in Data Type Summary
# -----------------------------------------------------

data_types = [
    int, float, complex,
    bool,
    str,
    list, tuple, range,
    set, frozenset,
    dict,
    type(None)
]

for dt in data_types:
    print(dt)
