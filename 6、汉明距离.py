def Hamming_distance(s1,s2):
    t = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            t += 1
    return t
def read():
    filename = input('请输入要读取的文件名称：')
    with open(f"{filename}",'r') as f:
        lines = f.read().strip().split('\n')
        s1 = lines[0]
        s2 = lines[1]
        return s1,s2

s1, s2 = read()
Hd = Hamming_distance(s1,s2)
print(Hd)
