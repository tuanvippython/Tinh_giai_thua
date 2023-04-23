def tinh_giai_thua(n):
    #Kiểm tra nếu giá trị n bằng 1 hoặc 0 thì trả về giá trị 1 vì trong toán học 0! và 1! đều bằng 1
    if n <= 1:
        return 1
    else:
        giai_thua = 1
        #Sử dụng vòng lặp for để lặp qua hết các giá trị từ 2 đến n sau đó trả về kết quả cuối cùng được gán vào biến giai_thua
        for i in range(2,n+1):
            giai_thua = giai_thua*i
        return giai_thua
        
n = int(input("Nhập giá trị cần tính giai thừa: "))
print(f"giai thừa của số {n} là : ",tinh_giai_thua(n))