def codeThuong(a):
    return ord(a) - 96
def codeHoa(a):
    return ord(a) - 64
#Chữ A có mã ASCII là 65 thì trừ đi 64 để còn là 1, chữ B có mã ASCII là 66 thì trừ đi 64 ra 2 v.v...
#Chữ a có mã ASCII là 97 thì trừ đi 96 để còn là 1, chữ b có mã ASCII là 98 thì trừ đi 96 ra 2 v.v...
plain_text = input()
pad_text = input()
res = ""
for i in range (len(plain_text)):
    if plain_text[i].islower():
        ma = codeThuong(plain_text[i]) + codeThuong(pad_text[i])
        if ma > 0: ma-=26
        res+=chr(ma + 96)
    else:
        ma = codeHoa(plain_text[i]) + codeHoa(pad_text[i])
        if ma > 26: ma-=26
        res+=chr(ma + 64)
        #Ví dụ: lấy plain_text cộng pad_text: K + R = 11 + 18 = 29
        #Lấy 29 - 26 = 3
        #Số 1 là chữ A, muốn nó ra ASCII là 65 thì phải cộng với 64
print(res)
'''
Input:
SACKGAULSPARENOONE
FPQRNSBIEHTZLACDGJ
Output: 
YQTCUTWUXXURQORSUO
'''