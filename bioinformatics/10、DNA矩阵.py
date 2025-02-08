def read_and_count(filename):
    result = []
    count_A = []  
    count_T = []  
    count_C = []  
    count_G = []
    
    with open(f"{filename}",'r') as f:
        lines = f.read().strip().split('>')[1:]
        
    for entry in lines:
        lines = entry.split('\n', 1)  # 分割ID和序列
        Matrix_lines = lines[1].replace('\n', '')  # 去掉换行符

        if not count_A:  # 如果是第一次
            count_A = [0] * len(Matrix_lines)
            count_T = [0] * len(Matrix_lines)
            count_C = [0] * len(Matrix_lines)
            count_G = [0] * len(Matrix_lines)

        for i in range(len(Matrix_lines)):
            if Matrix_lines[i] == 'A':
                count_A[i] += 1
            elif Matrix_lines[i] == 'T':
                count_T[i] += 1                
            elif Matrix_lines[i] == 'C':
                count_C[i] += 1
            else:
                count_G[i] += 1
                
    for i in range(len(Matrix_lines)):
        max_count = max(count_A[i],count_T[i],count_C[i],count_G[i])
        if max_count == count_A[i]:
            result.append('A')
        elif max_count == count_T[i]:
            result.append('T')
        elif max_count == count_C[i]:
            result.append('C')
        else:
            result.append('G')
    result = ''.join(result)
    with open(f"output_{filename}",'w') as outfile:
        output_string = (
            result + "\n" +
            "A: " + ' '.join(map(str, count_A)) + "\n" +
            "T: " + ' '.join(map(str, count_T)) + "\n" +
            "C: " + ' '.join(map(str, count_C)) + "\n" +
            "G: " + ' '.join(map(str, count_G))
        )
        outfile.write(output_string)
    print('您的文件已保存于',f"output_{filename}")
            
filename = input('请输入要读取的矩阵文件名称：')
read_and_count(filename)

                
            
    
