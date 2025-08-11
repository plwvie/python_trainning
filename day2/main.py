# values
# data types
# input

# numbers: 1, 2, -1, 0 (int); 1,25, 3.14, 0.0 (float)
#string "hello", 'man'
#bolean: True False


print(type(1))
print(type(1.25))
print(type(''))
print(type(True))

# variables

x = 5
print(type(x))

x = 6
print(x) # ctrl + alt + N

_ = 45
print(_)

# input -> str
full_name = input("Nhap vao ten cua ban: ")
print(full_name)
print(type(full_name))

number = input("nhap vao so nguyen: ")
number_as_int = int(number)
print(number_as_int + 3)