import pandas as pd
import os
import re

# 设置源目录和目标目录
source_dir = r'源目录'
target_dir = r'目标目录'

# 确保目标目录存在
os.makedirs(target_dir, exist_ok=True)

# 定义文件名匹配模式
pattern = re.compile(r'7月tap游戏节day(\d+)\.xlsx')

# 遍历源目录中的所有文件
for filename in os.listdir(source_dir):
    # 检查文件名是否匹配模式
    match = pattern.match(filename)
    if match:
        # 提取日期编号
        day_number = match.group(1)
        new_filename = f'd{day_number}.xlsx'
        new_filepath = os.path.join(target_dir, new_filename)
        
        # 读取源Excel文件
        try:
            # 读取C列数据，从第2行开始（C2），需要根据实际情况改变
            df = pd.read_excel(os.path.join(source_dir, filename), usecols='C', skiprows=1, header=None)
            
            # 保存提取的数据到新Excel文件
            df.to_excel(new_filepath, index=False, header=False)
            print(f'成功处理: {filename} -> {new_filename}')
        except Exception as e:
            print(f'处理文件 {filename} 时出错: {str(e)}')

print('所有文件处理完成！')