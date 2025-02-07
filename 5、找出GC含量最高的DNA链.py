def calculate_gc_content(dna_sequence):
    """计算DNA序列的GC含量"""
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_length = len(dna_sequence)
    return (gc_count / total_length) * 100

def find_highest_gc_content(file_path):
    """读取文件并找出GC含量最高的DNA链"""
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('>')[1:]  # 分割并去掉空行

    max_gc_id = None
    max_gc_content = 0

    for entry in lines:
        lines = entry.split('\n', 1)  # 分割ID和序列
        dna_id = lines[0].strip()
        dna_sequence = lines[1].replace('\n', '')  # 去掉换行符
        gc_content = calculate_gc_content(dna_sequence)

        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_id = dna_id

    return max_gc_id, max_gc_content

# 示例用法
file_path = input("文件名称为：")  # 替换为你的文件路径
highest_gc_id, highest_gc_content = find_highest_gc_content(file_path)
print(f"GC含量最高的链是：{highest_gc_id}")
print(f"GC含量为：{highest_gc_content:.6f}%")
