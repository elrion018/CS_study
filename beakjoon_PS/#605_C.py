import sys

table = [0]*26

n, k = map(int, sys.stdin.readline().split())

string = list(sys.stdin.readline().strip())

k_list = sys.stdin.readline().split()
result = 0
for i in k_list:
    table[ord(i)-97] = 1

for j in range(n):
    if table[ord(string[j])-97] == 1:
        string[j] = 'a'
    else:
        string[j] = 'b'
string = "".join(string)
string = string.split('b')
for k in string:
    result += (len(k)*(len(k)+1))//2
print(result)
