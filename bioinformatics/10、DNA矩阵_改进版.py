def process_sequences(input_file, output_file):
    with open(input_file, 'r') as f:
        strands = [x.strip() for x in f.readlines() if x.strip()]
    
    matrix = zip(*strands)
    profile = [dict((base, col.count(base)) for base in "ACGT") for col in matrix]
    
    consensus = []
    for col_dict in profile:
        max_base = max(col_dict, key=col_dict.get)
        consensus.append(max_base)
    
    # 生成结果字符串
    consensus_str = ''.join(consensus)
    counts = [
        f"A: {' '.join(map(str, [d['A'] for d in profile]))}",
        f"T: {' '.join(map(str, [d['T'] for d in profile]))}",
        f"C: {' '.join(map(str, [d['C'] for d in profile]))}",
        f"G: {' '.join(map(str, [d['G'] for d in profile]))}"
    ]
    
    result = f"{consensus_str}\n{'\n'.join(counts)}"
    
    with open(output_file, 'w') as f:
        f.write(result)
    
    print(f"结果已保存到文件：{output_file}")

# 示例调用
input_filename = input("请输入要读取的文件名：")
output_filename = f"output_{input_filename}"
process_sequences(input_filename, output_filename)
