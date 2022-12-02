#Kiểm tra 0 < t <= 100
try:
    t = int((input("Nhập số dòng muốn in ra: ")))
    if t < 0 :
        print("Nhập số dòng phải lớn hơn 0 !")
    elif t >=100 :
        print("Không quá 100 dòng.")
    lst_str =[]
    for i in range (t):
        str=input(f"Dòng thứ {i+1}: " )
        lst_str.append(str)
    for i in range(len(lst_str)):
        print(f"\nTest {i+1}:")
        for j in (lst_str[i].split()):
            print(f"{j}",end=" ")
except:
    print("Nhập không hợp lệ! ")
