def qt(s):
    return s.count('A'), s.count('C'), s.count('G'), s.count('T')

# 获取用户输入的文件名
filename = input('读取的文件名字为：')

# 初始化计数器
count_A = 0
count_C = 0
count_G = 0
count_T = 0

# 打开文件并逐行读取内容
with open(filename, 'r') as file:
    for line in file:
        line_counts = qt(line)  # 统计当前行中各字符的出现次数
        count_A += line_counts[0]
        count_C += line_counts[1]
        count_G += line_counts[2]
        count_T += line_counts[3]

# 打印结果
print(f"字符 'A' 的出现次数：{count_A}")
print(f"字符 'C' 的出现次数：{count_C}")
print(f"字符 'G' 的出现次数：{count_G}")
print(f"字符 'T' 的出现次数：{count_T}")
