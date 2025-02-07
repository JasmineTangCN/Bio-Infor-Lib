def dictlib():
    codon_dict = {}
    filename = input('请输入密码子对应的字典名称：')
    with open(f"{filename}",'r') as f:
        for line in f:
            # 去掉每行的首尾空白字符（包括换行符）
            line = line.strip()
            # 按空格分割每行，得到密码子和对应的氨基酸
            if line:  # 确保不处理空行
                codon, amino_acid = line.split()
                codon_dict[codon] = amino_acid
    return codon_dict


def read_and_translate():
    mRNA = []
    prot = ''
    RNAname = input('RNA链文件名称为：')
    with open(f"{RNAname}", 'r') as RNAf:
        for line in RNAf:
            line = line.strip()
            if line:
                mRNA += [line[i:i+3] for i in range(0, len(line), 3)]
    for codon in mRNA:
        if codon in dic:
            amino_acid = dic[codon]
            if amino_acid != 'Stop':
                prot += amino_acid
    return prot

def write(amino_chain,filename):
    with open(filename,'w') as outfile:
        outfile.write(amino_chain)
    print(f'处理完成，结果已保存到文件{filename}')
    
dic = dictlib()
amino_chain = read_and_translate()
output_filename = input('请输入输出文件名：')
write(amino_chain,output_filename)

