def code(x): #Chuyen 1 chu ve dang ma ascii nhi phan
    ascii_val = ord(x)
    binary_str = bin(ascii_val)[2:]
    while len(binary_str) < 8: binary_str = "0" + binary_str
    return binary_str 

def chuyenDoi(x): #Chuyen tung tu trong xau roi ghep lai
    res = ""
    for y in x: res+=code(y)
    return res 

ban_ma = input() #Cho trước ở dạng xâu NP
key = input() #Cho trước dưới dạng chữ

#nếu bản mã là chữ thì ta sẽ chuyển về nhị phân trước
if not ban_ma[0].isdigit(): ban_ma=chuyenDoi(ban_ma)
s = chuyenDoi(key) #Chuyển đổi khóa về dạng xâu NP

res = ""
for i in range(len(s)): res+=str(int(s[i])^int(ban_ma[i]))

final_res = ""
for i in range(0, len(res), 8):
    byte = res[i:i+8]
    # Chuyển đổi chuỗi 8 bit thành số thập phân
    decimal_value = int(byte, 2)
    # Chuyển đổi số thập phân thành ký tự ASCII
    final_res += chr(decimal_value)

print(final_res)