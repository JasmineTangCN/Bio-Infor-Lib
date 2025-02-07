# 获取用户输入的文件名
filename = input('读取的文件名字为：')

# 打开原始文件读取内容，并创建一个新的文件用于写入修改后的内容
with open(filename, 'r') as file, open(f"{filename}_modified", 'w') as outfile:
    for line in file:
        # 替换每一行中的 'T' 为 'U'
        modified_line = line.replace('T', 'U')
        # 将修改后的行写入新文件
        outfile.write(modified_line)

print(f"修改完成，结果已保存到文件 {filename}_modified")
