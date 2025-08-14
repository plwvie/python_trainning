# List trong Python là một kiểu dữ liệu tập hợp có thể lưu trữ nhiều giá trị trong một biến. List có thể thay đổi (mutable) và cho phép các phần tử trùng lặp.
# 1. Tạo List
# # List rỗng
# empty_list = []
# empty_list2 = list()

# # List với các phần tử
# numbers = [1, 2, 3, 4, 5]
# fruits = ["táo", "cam", "chuối", "xoài"]
# mixed = [1, "hello", 3.14, True]

# # List từ range
# numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]

#          0  1  2    3 
numbers = [1, 2, 3.5, 4, 1]
print(type(numbers))
print(numbers)


# 2. Truy cập phần tử
# fruits = ["táo", "cam", "chuối", "xoài"]
# # Truy cập bằng chỉ số (index)
# print(fruits[0])    # "táo" (phần tử đầu tiên)
# print(fruits[-1])   # "xoài" (phần tử cuối cùng)
# print(fruits[-2])   # "chuối" (phần tử áp cuối)

# # Slicing (cắt lát)
# print(fruits[1:3])   # ["cam", "chuối"]
# print(fruits[:2])    # ["táo", "cam"]
# print(fruits[2:])    # ["chuối", "xoài"]
# print(fruits[::-1])  # Đảo ngược list

print(numbers[0])
print(numbers[-3])


# 3. Thêm, xoá phần tử
# fruits = ["táo", "cam"]

# # Thêm phần tử
# fruits.append("chuối")           # Thêm vào cuối
# fruits.insert(1, "dưa hấu")      # Thêm vào vị trí chỉ định
# fruits.extend(["xoài", "nho"])   # Thêm nhiều phần tử

# print(fruits)  # ["táo", "dưa hấu", "cam", "chuối", "xoài", "nho"]

# # Xóa phần tử
# fruits.remove("cam")        # Xóa phần tử đầu tiên có giá trị "cam"
# last_fruit = fruits.pop()   # Xóa và trả về phần tử cuối
# fruits.pop(0)              # Xóa phần tử tại vị trí 0
# del fruits[1]              # Xóa phần tử tại vị trí 1
# fruits.clear()             # Xóa tất cả phần tử

numbers.append("Chuoi")
print(numbers)

numbers.insert(0, 1000)
print(numbers)
numbers.insert(1000, 1000)
numbers.insert(-1000, 99)


numbers.remove(1)
print(numbers)

last_value = numbers.pop()
print(numbers)

numbers.extend([1, "haha"])
print(numbers)

numbers[1] = 75
print(numbers)


# 4. Các phương thức hữu ích
# numbers = [3, 1, 4, 1, 5, 9, 2]

# # Tìm kiếm và đếm
# print(numbers.count(1))     # Đếm số lần xuất hiện: 2
# print(numbers.index(4))     # Vị trí đầu tiên của 4: 2

# # Sắp xếp
# numbers.sort()              # Sắp xếp tăng dần (thay đổi list gốc)
# numbers.sort(reverse=True)  # Sắp xếp giảm dần
# sorted_nums = sorted(numbers)  # Tạo list mới đã sắp xếp

# # Đảo ngược
# numbers.reverse()           # Đảo ngược list (thay đổi list gốc)
# reversed_nums = numbers[::-1]  # Tạo list mới đã đảo ngược

# # Sao chép
# copy_list = numbers.copy()   # Sao chép nông
# copy_list2 = numbers[:]      # Cách khác để sao chép

amount = numbers.count(1)
print(amount)

amount = len(numbers)
print(amount)

index_of_3p5 = numbers.index(3.5)
print(index_of_3p5)

numbers.reverse()
print(numbers)

numbers = [1, 4, 5, 3.5]
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)
# 5. Duyệt qua List
# fruits = ["táo", "cam", "chuối"]

# # Duyệt qua giá trị
# for fruit in fruits:
#     print(fruit)

# # Duyệt qua chỉ số và giá trị
# for i, fruit in enumerate(fruits):
#     print(f"{i}: {fruit}")

# # Sử dụng while
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# 6. List Comprehension
# # Tạo list với điều kiện
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Lấy số chẵn
# evens = [x for x in numbers if x % 2 == 0]

# # Bình phương các số
# squares = [x**2 for x in numbers]

# # Kết hợp điều kiện
# even_squares = [x**2 for x in numbers if x % 2 == 0]

# print(evens)         # [2, 4, 6, 8, 10]
# print(squares)       # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(even_squares)  # [4, 16, 36, 64, 100]

# 7. Một số thao tác khác
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# # Nối list
# combined = list1 + list2        # [1, 2, 3, 4, 5, 6]
# list1.extend(list2)             # Thêm list2 vào list1

# # Nhân list
# repeated = [0] * 5              # [0, 0, 0, 0, 0]
# pattern = [1, 2] * 3            # [1, 2, 1, 2, 1, 2]

# # Kiểm tra phần tử
# print(2 in list1)               # True
# print(10 not in list1)          # True

# # Tìm min, max, sum
# numbers = [3, 1, 4, 1, 5, 9]
# print(min(numbers))             # 1
# print(max(numbers))             # 9
# print(sum(numbers))             # 23
# print(len(numbers))             # 6

numbers = [3, 1, 4, 1, 5, 9]
print(min(numbers))             # 1
print(max(numbers))             # 9
#mardy bum