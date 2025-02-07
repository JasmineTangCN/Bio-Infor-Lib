a = int(input('请输入a的值：'))
b = int(input('请输入b的值：'))
n = 0
for i in range(a,b+1):
    if i % 2 == 1:
        n += i
print(n)
