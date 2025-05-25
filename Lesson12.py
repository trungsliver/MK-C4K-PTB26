# Hàm - Chương trình con

# Hàm không có giá trị trả về
def say_hello():
    print("Hello Khiêm")
    print("Hello Bảo Hoàng")

    # gọi hàm khi cần sử dụng
say_hello()

# Hàm có dữ liệu đầu vào (tham số)
def hello2(name):
    print("Hello ", name)

hello2('Minh Trí')
hello2('Mai Hoàng Minh')

# Hàm có giá trị trả về (sử dụng được như 1 biến)
def dtic_HCN(a:float, b:float):
    return a * b
    # Gọi hàm và lưu kết quả vào biến
print('Kết quả:', dtic_HCN(5,10))

# Ví dụ:
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(check_even(20))
print(check_even(21))

# ================== LUYỆN TẬP =======================
# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.