filename = input('请输入DNA长链及片段文件名：')
s, t = open(f"{filename}").read().split('\r\n')
r = ''
for i in range(len(s) - len(t) + 1):
    if s[i:i+len(t)] == t:
        r += str(i+1)
        r += ' '
print(r)
