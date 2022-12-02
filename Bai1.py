# Kiểm tra 0 < t <= 100
try:
    t = int((input("Nhập số dòng muốn in ra: ")))
    if t < 0:
        print("Nhập số dòng phải lớn hơn 0 !")
    elif t >= 100:
        print("Không quá 100 dòng.")
    # Tạo list rỗng để truyền t vào
    lst_str = []
    # Chạy i để truyền t vào lst_str
    for i in range(t):
        str = input(f"Dòng thứ {i+1}: ")
        lst_str.append(str)
    # Xuất ra lần lượt theo độ dài lst
    for i in range(len(lst_str)):
        print(f"Test {i+1}: \n {lst_str[i].title()}")
except:
    print("Nhập không hợp lệ! ")
