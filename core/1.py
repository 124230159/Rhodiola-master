import os
import base64
import re

def recover_gif_from_parts(parts_dir, output_gif_name="final_recovered.gif"):
    # 1. 找出目录下所有符合 part_x.txt 命名的文件
    files = [f for f in os.listdir(parts_dir) if f.startswith("part_") and f.endswith(".txt")]
    
    # 2. 核心：必须按照数字大小自然排序（防止 part_10.txt 排在 part_2.txt 前面）
    files.sort(key=lambda var: [int(x) if x.isdigit() else x for x in re.split(r'(\d+)', var)])
    
    # 3. 依次读取并拼接所有文本内容
    full_base64_str = ""
    for file_name in files:
        file_path = os.path.join(parts_dir, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            # 读取的同时去掉所有换行和回车
            full_base64_str += f.read().replace("\n", "").replace("\r", "")
        print(f"已成功读取并拼接: {file_name}")
            
    # 4. 解码并保存为最终的 GIF 动图
    gif_bytes = base64.b64decode(full_base64_str)
    with open(output_gif_name, "wb") as gif_f:
        gif_f.write(gif_bytes)
        
    print(f"\n🎉 恭喜！所有切片已完美重组，原 GIF 已还原为：{output_gif_name}")

# 执行合并（假设你把外网收到的 part 文件都放在 download_parts 文件夹里）
recover_gif_from_parts("download_parts")
