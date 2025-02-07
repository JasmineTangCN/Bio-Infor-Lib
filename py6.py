filename = input('请输入文件名称：')
with open(f"{filename}",'r') as f, open(f"words_times_{filename}",'w') as outfile:
    words = {}
    for line in f:
        for word in line.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    for key, value in words.items():
        outfile.write(f"{key}  {value}\n")
print(f"统计完成，结果已保存到文件 words_times_{filename}")


#
#from collections import Counter
#import string

# 获取用户输入
#user_input = input("请输入要统计的文本：\n")

# 去掉换行符后分割单词
#words = user_input.strip().split()

# 去掉标点符号
#words = [word.strip(string.punctuation) for word in words]

# 统计单词出现次数
#word_counts = Counter(words)

# 打印统计结果
#for word, count in word_counts.items():
#    print(f"{word}: {count}")
