def codeThuong(a):
    return ord(a) - 96
def codeHoa(a):
    return ord(a) - 64
#Chữ A có mã ASCII là 65 thì trừ đi 64 để còn là 1, chữ B có mã ASCII là 66 thì trừ đi 64 ra 2 v.v...
#Chữ a có mã ASCII là 97 thì trừ đi 96 để còn là 1, chữ b có mã ASCII là 98 thì trừ đi 96 ra 2 v.v...
cypher_text = input()
pad_text = input()
res = ""
for i in range (len(cypher_text)):
    if cypher_text[i].islower():
        ma = codeThuong(cypher_text[i]) - codeThuong(pad_text[i])
        if ma < 0: ma+=26
        res+=chr(ma + 96)
    else:
        ma = codeHoa(cypher_text[i]) - codeHoa(pad_text[i])
        if ma < 0: ma+=26
        res+=chr(ma + 64)
        #Ví dụ: lấy cypher_text trừ đi pad_text: C - R = 3 - 18 = -15
        #Lấy -15 + 26 = 11
        #Số 1 là chữ A, muốn nó ra ASCII là 65 thì phải cộng với 64
print(res)
# Input:
# YQTCUTWUXXURQORSUO
# FPQRNSBIEHTZLACDGJ
# Output: 
# SACKGAULSPARENOONE