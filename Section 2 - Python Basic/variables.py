# %%
# 1. What is a Variable
x = 10
name = "Shivam"
print(x, name)

# %%
# 2. Variable Naming Rules
valid_var = 10
_valid = 20
var_1 = 30
print(valid_var, _valid, var_1)

# %%
# 3. Multiple Assignment
a, b, c = 1, 2, 3
print(a, b, c)

# %%
# 4. Same Value Assignment
x = y = z = 100
print(x, y, z)

# %%
# 5. Dynamic Typing
x = 10
print(type(x))
x = "Data Science"
print(type(x))

# %%
# 6. Common Variable Types
a = 10
b = 3.14
c = "Python"
d = True
e = None
print(type(a), type(b), type(c), type(d), type(e))

# %%
# 7. Type Conversion
x = "100"
x = int(x)
print(x, type(x))

# %%
# 8. Variable Reassignment
x = 10
x = x + 5
print(x)

# %%
# 9. Local Scope
def func():
    x = 10
    print(x)
func()

# %%
# 10. Global Scope
x = 20
def func():
    print(x)
func()

# %%
# 11. global keyword
x = 5
def func():
    global x
    x = 10
func()
print(x)

# %%
# 12. Immutable Example
x = 10
y = x
y = 20
print(x, y)

# %%
# 13. Mutable Example
a = [1, 2, 3]
b = a
b.append(4)
print(a, b)

# %%
# 14. Object Identity
x = 10
y = 10
print(id(x), id(y))

# %%
# 15. Constants (Convention)
PI = 3.14159
GRAVITY = 9.8
print(PI, GRAVITY)

# %%
# 16. Delete Variable
x = 100
del x

# %%
# 17. Python Keywords
import keyword
print(keyword.kwlist)

# %%
# 18. Unpacking
data =
