import re
from datetime import datetime

def convert_md_to_txt(md_content):
    """将 Markdown 内容转换为纯文本格式"""
    
    # 提取并优化标题
    title = "C++通用函数库设计与实现 - 字符串/文件/时间/网络工具类完整源码分享"
    
    txt_content = md_content
    
    # 在开头添加优化后的标题
    header = f"""{title}
{'='*70}

"""
    
    # 处理导读部分
    txt_content = re.sub(r'> \*\*导读\*\*: ', '【导读】', txt_content)
    txt_content = re.sub(r'> \*\*GitHub 地址\*\*: ', '\n【GitHub 地址】', txt_content)
    txt_content = re.sub(r'> \*\*技术栈\*\*: ', '\n【技术栈】', txt_content)
    txt_content = re.sub(r'> ', '', txt_content)
    
    # 移除原来的主标题行
    txt_content = re.sub(r'^# \[.*?\].*?\n', '', txt_content, flags=re.MULTILINE)
    
    # 组合新标题和内容
    final_content = header + txt_content
    
    # 移除代码块标记但保留内容
    final_content = re.sub(r'```cpp\n?', '', final_content)
    final_content = re.sub(r'```\n?', '', final_content)
    
    # 转换剩余标题层级
    final_content = re.sub(r'^## (.*$)', r'\n\1\n' + '-'*40, final_content, flags=re.MULTILINE)
    final_content = re.sub(r'^### (.*$)', r'\n\1', final_content, flags=re.MULTILINE)
    final_content = re.sub(r'^#### (.*$)', r'\n  ● \1', final_content, flags=re.MULTILINE)
    
    # 移除粗体和斜体标记
    final_content = re.sub(r'\*\*(.*?)\*\*', r'\1', final_content)
    final_content = re.sub(r'\*(.*?)\*', r'\1', final_content)
    
    # 转换列表
    final_content = re.sub(r'^- (.*$)', r'  • \1', final_content, flags=re.MULTILINE)
    final_content = re.sub(r'^\d+\. (.*$)', r'  \g<0>', final_content, flags=re.MULTILINE)
    
    # 移除表情符号
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\U00002702-\U000027B0"
        "]+", flags=re.UNICODE)
    final_content = emoji_pattern.sub(r'', final_content)
    
    # 移除分隔线
    final_content = re.sub(r'^---+$', '', final_content, flags=re.MULTILINE)
    final_content = re.sub(r'^\*\*\*+$', '', final_content, flags=re.MULTILINE)
    
    # 清理多余空行
    final_content = re.sub(r'\n{3,}', '\n\n', final_content)
    
    return final_content.strip()


def main():
    # 读取 Markdown 文件
    md_file = 'ready_to_publish_20260305_171701.md'
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 转换为 TXT 格式
    txt_content = convert_md_to_txt(md_content)
    
    # 生成文件名
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    txt_file = f'ready_to_publish_{timestamp}.txt'
    
    # 保存 TXT 文件
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(txt_content)
    
    print(f'✅ TXT 格式已生成：{txt_file}')
    print(f'\n📋 主要改进:')
    print(f'  • 移除了所有 Markdown 符号 (# * ` 等)')
    print(f'  • 使用中文标点符号 (● • — 等)')
    print(f'  • 清晰的标题层次 (使用下划线分隔)')
    print(f'  • 优化的段落间距')
    print(f'  • 更适合直接复制到 CSDN 编辑器')
    print(f'\n💡 使用方法:')
    print(f'  1. 打开 {txt_file}')
    print(f'  2. 全选复制 (Ctrl+A → Ctrl+C)')
    print(f'  3. 粘贴到 CSDN 编辑器 (Ctrl+V)')
    print(f'  4. 微调格式后发布')


if __name__ == '__main__':
    main()
