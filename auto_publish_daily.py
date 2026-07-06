#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSDN 博客自动发布工具 - 快速启动脚本
直接执行今日发布任务，无需交互
生成 TXT 格式，去除多余字符和空行
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
import glob
import re

def load_articles():
    """加载所有可用文章"""
    articles_dir = "CSDN_ARTICLES"
    articles = []
    
    if not os.path.exists(articles_dir):
        print(f"❌ 文章目录不存在：{articles_dir}")
        return articles
    
    # 扫描所有 markdown 文件
    pattern = os.path.join(articles_dir, "*.md")
    md_files = glob.glob(pattern)
    
    for file_path in md_files:
        file_name = os.path.basename(file_path)
        
        # 跳过 README 和特殊文件
        if "README" in file_name or "指南" in file_name:
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取标题
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else file_name.replace('.md', '')
            
            articles.append({
                "title": title,
                "file_path": file_path,
                "file_name": file_name
            })
        except Exception as e:
            print(f"⚠️  读取失败 {file_name}: {e}")
    
    return articles

def load_publish_log():
    """加载发布日志"""
    log_file = "publish_log.json"
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"published_articles": [], "last_publish_date": None, "total_published": 0}

def save_publish_log(log):
    """保存发布日志"""
    log_file = "publish_log.json"
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(log, f, indent=2, ensure_ascii=False)

def select_today_article(articles, publish_log):
    """选择今天要发布的文章"""
    # 获取已发布的文章路径
    published_paths = [p['file_path'] for p in publish_log['published_articles']]
    
    # 过滤未发布的文章
    unpublished = [a for a in articles if a['file_path'] not in published_paths]
    
    if not unpublished:
        print("✅ 所有文章都已发布完毕!")
        print("🔄 将重新开始发布循环...")
        unpublished = articles
    
    # 简单轮询：选择第一篇未发布的
    return unpublished[0] if unpublished else None

def clean_markdown_content(content):
    """清理 Markdown 内容，转换为适合 CSDN 的纯文本格式"""
    # 1. 移除连续的多个空行（保留单个空行）
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # 2. 移除行首尾的空白字符
    lines = content.split('\n')
    cleaned_lines = [line.rstrip() for line in lines]
    content = '\n'.join(cleaned_lines)
    
    # 3. 移除代码块标记但保留内容
    content = re.sub(r'^```(\w*)\s*$', '', content, flags=re.MULTILINE)
    
    # 4. 将 Markdown 标题转换为普通文本（移除 # 符号）
    content = re.sub(r'^#+\s+(.+)$', r'\1', content, flags=re.MULTILINE)
    
    # 5. 移除引用标记 >
    content = re.sub(r'^>\s*', '', content, flags=re.MULTILINE)
    
    # 6. 移除粗体/斜体标记 ** 和 *
    content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)
    content = re.sub(r'\*(.+?)\*', r'\1', content)
    
    # 7. 移除列表标记 - 和数字列表
    content = re.sub(r'^[\-\*]\s+', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\d+\.\s+', '', content, flags=re.MULTILINE)
    
    # 8. 再次清理多余空行
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # 9. 移除开头和结尾的空白行
    content = content.strip()
    
    return content

def prepare_content_txt(article):
    """准备文章内容（TXT 格式）"""
    with open(article['file_path'], 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 清理 Markdown 格式
    cleaned_content = clean_markdown_content(content)
    
    # 添加简化的导读信息（不使用 Markdown 格式）
    intro = """================================================================
导读：本文是华又科技视频监控平台系列技术文章之一。我们开源了完整的视频监控系统源码，包含 23 个核心工程项目。
GitHub 地址：https://github.com/huayou-tech/videomonitor-platform
技术栈：C++17 | Windows IOCP | Live555 | SIP/GB28181 | RTSP/ONVIF
================================================================

"""
    
    # 添加简化的页脚信息
    footer = """

================================================================
关于项目
================================================================
本项目是一个完整的商业级视频监控平台，经过十年验证，稳定可靠。

资源链接：
- GitHub 源码：https://github.com/huayou-tech/videomonitor-platform
- 技术博客：关注作者获取更多系列文章

支持作者：
- Star 我们的 GitHub 项目
- 点赞 + 收藏 + 评论
- 分享给更多需要的人

下期预告：明天继续发布下一篇技术文章！
"""
    
    return intro + cleaned_content + footer

def main():
    print("="*60)
    print("CSDN 博客自动发布工具 (TXT 格式)")
    print("="*60)
    print(f"日期：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    # 加载文章
    print("\n正在扫描文章目录...")
    articles = load_articles()
    print(f"找到 {len(articles)} 篇文章")
    
    if not articles:
        print("没有找到可用的文章")
        return
    
    # 加载发布日志
    publish_log = load_publish_log()
    print(f"已发布：{publish_log['total_published']} 篇")
    
    # 检查今天是否已发布
    today = datetime.now().strftime('%Y-%m-%d')
    if publish_log['last_publish_date'] == today:
        print(f"\n今日 ({today}) 已发布过文章")
        last_title = publish_log['published_articles'][-1]['title'] if publish_log['published_articles'] else "无"
        print(f"已发布：{last_title}")
        return
    
    # 选择文章
    print("\n正在选择今日文章...")
    article = select_today_article(articles, publish_log)
    
    if not article:
        print("无法选择文章")
        return
    
    print(f"选中：{article['title']}")
    
    # 准备内容
    print("\n正在准备文章内容...")
    final_content = prepare_content_txt(article)
    
    # 保存到临时文件（使用 .txt 扩展名）
    output_file = f"ready_to_publish_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"文章内容已保存到：{output_file}")
    
    # 更新发布日志
    publish_log['published_articles'].append({
        "title": article['title'],
        "file_path": article['file_path'],
        "publish_date": today,
        "publish_time": datetime.now().strftime('%H:%M:%S'),
        "output_file": output_file,
        "status": "ready_to_publish"
    })
    publish_log['last_publish_date'] = today
    publish_log['total_published'] += 1
    save_publish_log(publish_log)
    
    print(f"发布日志已更新 (总计：{publish_log['total_published']} 篇)")
    
    # 显示下一步操作
    print("\n" + "="*60)
    print("下一步操作:")
    print("="*60)
    print(f"1. 打开文件：{output_file}")
    print("2. 复制内容到 CSDN 编辑器")
    print("3. 设置分类、标签后发布")
    print("="*60)
    
    print("\n今日发布任务完成!")
    print("提示：每天运行一次此脚本即可自动发布")

if __name__ == "__main__":
    main()