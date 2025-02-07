def calculate(k, m, n, t):
    total = t * (t-1) / 2
    a1 = m * n * 0.5 #杂合X纯隐
    a2 = n * (n-1) / 2 #纯隐X纯隐
    a3 = (m * (m-1) / 2) * 0.25 #杂合X杂合
    p = 1 - (a1 + a2 +a3)/total
    return p

k = int(input('显性纯合体个数为：'))
m = int(input('杂合体个数为：'))
n = int(input('隐性纯合体个数为：'))
t = k + m + n
Pr = calculate(k, m, n, t)
print(Pr)
