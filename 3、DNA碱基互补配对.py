filename = input('读取的文件名字叫：')
with open(filename, 'r') as file, open(f"complem_{filename}",'w') as outfile:
    # 读取文件的全部内容
    s = file.read()
    # 替换字符
    # 注意：这里需要同时处理所有字符，避免冲突
    s = s.replace('A','X')
    s = s.replace('T','A')
    s = s.replace('X','T')
    s = s.replace('C','Y')
    s = s.replace('G','C')
    s = s.replace('Y','G')
# 反转内容
    s = s[::-1]
# 将处理后的结果写入新文件
    outfile.write(s)
print(f"处理完成，结果已保存到文件 complem_{filename}")
