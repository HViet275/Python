# Kiểm tra 0 < t <= 100
try:
    t = int((input("Nhập số dòng muốn in ra: ")))
    if t < 0:
        print("Nhập số dòng phải lớn hơn 0 !")
    elif t >= 100:
        print("Không quá 100 dòng.")
    lst_str = []
    lst_old = []
    lst_new = []
    for i in range(t):
        lst_str.append(input(f"Nhập dòng thứ {i+1}: "))
        lst_old.append(input(f"Nhập chuỗi con thứ {i+1}: "))
        lst_new.append(input(f"Nhập chuỗi con thứ {i+1}: "))
        # Dùng replace() thay thế lst_old thành lst_new
        print(f"Test {i+1}: \n {lst_str[i].replace(lst_old[i], lst_new[i])}")
except:
    print("Nhập không hợp lệ! ")