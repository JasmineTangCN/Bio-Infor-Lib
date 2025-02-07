k = int(input('k的值是多少：'))
n = int(input('n的值是多少：'))
a = [1,1]
for i in range(2,n):
    an = a[i-1] + a[i-2] * k
    a.append(an)

print(f"第{n}项结果为：{a[n-1]}")
