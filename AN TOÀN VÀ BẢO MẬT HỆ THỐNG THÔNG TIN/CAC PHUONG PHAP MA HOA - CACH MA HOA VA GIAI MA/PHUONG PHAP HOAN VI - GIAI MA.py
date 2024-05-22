cypher_text = input()
k = int(input())
pos = [0] * 1500 
for _ in range(k):
    x, y = map(int, input().split())
    pos[x-1] = y-1
#Ban đầu, chuyển ký tự thứ x ban đầu bị chuyển xuống vị trí thứ y
#Do đó, muốn biết ban đầu ký tự thứ x nằm đâu thì truy qua vị trí
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
UKAGLSCAORPEOSAN
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
SACKGAULSPARENOO
'''