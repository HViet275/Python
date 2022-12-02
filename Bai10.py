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
        for x in range(-1,-len(lst_str) - 1,-1):
            if x == -1:
                if lst_str[x] != "!" or lst_str[x] != "?" or lst_str[x] != ".":
                    lst_str+= "."
                    print(f"{lst_str[i]}")
except:
    print("Nhập không hợp lệ! ")