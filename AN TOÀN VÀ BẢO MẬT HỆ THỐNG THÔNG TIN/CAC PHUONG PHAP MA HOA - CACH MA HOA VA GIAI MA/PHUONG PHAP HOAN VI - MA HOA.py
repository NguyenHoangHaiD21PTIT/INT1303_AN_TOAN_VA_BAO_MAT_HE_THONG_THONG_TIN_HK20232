cypher_text = input()
k = int(input())
pos = [0] * 1500 
for _ in range(k):
    x, y = map(int, input().split())
    pos[y-1] = x-1
#Ký tự thứ x bị chuyển xuống vị trí y
#Mỗi vị trí, ta cần biết thằng nào chuyển đến
xau = []
for i in range(0, len(cypher_text), k): xau.append(cypher_text[i: i+k])

res = ""
for x in xau: 
    s = ""
    tmp = x[::-1]
    for i in range(0, k):#Mỗi xâu dài k
        s+=tmp[pos[i]]
    print(s[::-1], end = "")
'''
Input
SACKGAULSPARENOO
8
1 4
2 8
3 1
4 5
5 7
6 2
7 6
8 3
Output:
UKAGLSCAORPEOSAN
'''