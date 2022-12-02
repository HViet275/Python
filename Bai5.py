# Kiểm tra 0 < t <= 100
try:
    t = int((input("Nhập số dòng muốn in ra: ")))
    if t < 0:
        print("Nhập số dòng phải lớn hơn 0 !")
    elif t >= 100:
        print("Không quá 100 dòng.")
    for i in range(t):
        Str1 = input(f"Nhập dòng thứ {i+1}: ")
        Str1_1 = input(f"Nhập chuỗi con thứ {i+1}: ")
        # count() số lần xuất hiện chuỗi con 
        print(f"Test {i+1}: \n {Str1.count(Str1_1, 0, len(Str1))}")
except:
    print("Nhập không hợp lệ! ")