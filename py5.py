filename = input('请输入文件名：')
even_content = ""
with open(f"{filename}",'r') as file, open(f"even_lines_{filename}", 'w') as outfile:
    for i, line in enumerate(file,start = 1):
        if i % 2 == 0:
            outfile.write(line)
print(f"修改完成，结果已保存到文件even_lines_{filename}")



#更简单的方法
#with open('rosalind_ini5.txt', 'r') as f:
#    print(''.join(f.readlines()[1::2]))

#读取偶数行：
#   f.readlines() 会将文件的所有行读取为一个列表，每行是一个字符串。
#   使用切片操作 [1::2] 获取从索引 1 开始的每隔一行的内容（即偶数行）。
#连接并打印：
#   使用 ''.join(...) 将偶数行的内容连接成一个字符串。
#   使用 print() 函数将结果打印出来。
