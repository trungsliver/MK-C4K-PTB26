# Strings - Chuỗi / Xâu ký tự
name = 'Duc Khiem'

# Độ dài string
print('Độ dài string:', len(name))

# Ký tự thứ n trong string: string[n]
print('Ký tự đầu tiên:', name[0])
print('Ký tự có index = 4:', name[4])

# Duyệt string
    # Cách 1: Dùng cả index và value
for i in range(len(name)):
    print(name[i], end = ' ')

    # Cách 2: Chỉ dùng value
for item in name:
    print(item, end = ' ')

# Xâu con
str1 = 'KhoiNguyenVipPro'
str2 = 'VipPro'
str3 = 'DepTrai'

    # Kiểm tra xâu con: hàm in => True/False
print(str2 in str1)     # True
print(str3 in str1)     # False

    # Tìm vị trí xâu con: hàm find() => index
print(str1.find('KhoiNguyen'))      # 0
print(str1.find('Nguyen'))          # 4
print(str1.find('Bach'))            # -1

# Slicing - cắt chuỗi
name = 'BaoHoangAoXanh'
    # Cắt từ đầu string
print(name[:3])         # Bao
    # Cắt đến cuối string
print(name[8:])         # AoXanh
    # Cắt vị trí bất kì
print(name[3:8])        # Hoang

# Xóa khoảng trắng ở đầu và cuối - strip()
name = '          Minh Mai Mai      '
print(name)
print(name.strip())

# Thay thế strings - replace()
song = 'baby shark doo doo doo doo doo doo'
    # Thay thế toàn bộ
song2 = song.replace('doo', 'minh')
print(song2)
    # Thay thế với số lượng chỉ định
song3 = song.replace('doo', 'minh', 3)
print(song3)

# Kết hợp chuỗi - join()
arr = ['r','o','n','a','l','d','o']
str1 = ' '.join(arr)
str2 = ''.join(arr)
str3 = '-'.join(arr)
print(str1)         # Output: r o n a l d o
print(str2)         # Output: ronaldo
print(str3)         # Output: r-o-n-a-l-d-o

# Tách chuỗi - split()
a = '1 2 3 4 5 6 7 8 9'
    # Tách theo khoảng trắng
arr1 = a.split()
print(arr1)     

b = 'a,s,d,f,g,h,j,k,l'
    # Tách theo dấu phẩy
arr2 = b.split(',')    
print(arr2)    

# Chuyển đổi kiểu dữ liệu trong danh sách
    # Các phần tử đầu có dataType là strings
arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # cách 1:
arr1 = []
for item in arr:
    arr1.append(int(item))
print(arr1)

    # cách 2:
arr2 = [int(item) for item in arr]
print(arr2)

# -------------------------Luyện tập-----------------------
# Bài 1: Nhập 2 thông tin: họ, tên. In ra màn hình tên đầy đủ
# Bài 2: Nhập vào 1 xâu ký tự định dạng dd/mm/yyyy (01/08/2024)
    # Tách ngày, tháng, năm và hiển thị ra màn hình
# Bài 3: Nhập vào thông tin dạng username:password
    # kiểm tra xem thông tin vừa nhập có trùng với thông tin có sẵn
    # YC2: bắt người dùng nhập đến khi nào trùng username và password thì kết thúc