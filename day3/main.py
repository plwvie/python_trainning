# operator - toán tử
# + - * / // ** %

print(1 + 2) 
print(1 - 2)
print(3 * 2)
print(3 / 2) # float
print(3 // 2) # int
print(5 ** 2) # 25
print(3 % 2) # 3 // 2 = 1


# >, <, >=, <=, ==, !=
# Chia lấy phần nguyên với số dương
# print(10 // 3)    # Kết quả: 3 (thay vì 3.333...)
# print(15 // 4)    # Kết quả: 3 (thay vì 3.75)
# print(20 // 6)    # Kết quả: 3 (thay vì 3.333...)

# Chia lấy phần nguyên với số âm
# print(-10 // 3)   # Kết quả: -4 (làm tròn xuống từ -3.333...)
# print(10 // -3)   # Kết quả: -4
# print(-10 // -3)  # Kết quả: 3

# Với số thực
# print(10.5 // 3)  # Kết quả: 3.0
# print(15.8 // 4)  # Kết quả: 3.0
# bool - True/False

# print(3.0 == 3)

# and or not
# Ctrl + Shift + L
# Ctrl + D

print(False and True)   # False
print(False and False)  # False
print(True and True)    # True
print(True and False)   # False

print(False or True)   # True
print(False or False)  # False
print(True or True)    # True
print(True or False)   # True

print(not True)

print(bool(0)) # False
print(bool(1)) # True
print(1 and 2) # ctrl + /
print(0 or 2) # 2

print(not 1)
print(not 0)

# falsy: 0, 0.0, 0j, None: No value
# list: []
# set: set()
# dict: {}
# tuple: ()
# bool(falsy) = False
print(bool(0j))
print(bool(''))


# +=, -=, /=, //=, %=, **=

x = 5
x = x + 5
x += 5

print("x = ", x)

# // - int vs / - float
print (5 // 3)

# i am 30
age = 30
print("I am", str(age))

# f-strings
print(f"I am {age}")

# ham format
print("I am {}".format(age))

#string

s = "Hello World"
lst = s.split()
print(lst) 