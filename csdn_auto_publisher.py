#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSDN 博客自动发布工具 - 增强版
用于批量管理和发布技术文章，支持每日自动发布
"""

import os
import json
import time
import requests
from datetime import datetime, timedelta
import schedule
from pathlib import Path
import markdown
import re
import glob

class CSDNAutoPublisher:
    def __init__(self):
        self.config_file = "csdn_config.json"
        self.articles_dir = "CSDN_ARTICLES"
        self.schedule_file = "weekly_publish_schedule.json"
        self.publish_log_file = "publish_log.json"
        self.load_config()
        self.load_publish_log()
        
    def load_config(self):
        """加载配置文件"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = {
                "username": "",
                "password": "",
                "cookie": "",
                "default_category": "C++",
                "tags": ["视频监控", "C++", "系统架构"],
                "publish_time": "09:00",
                "auto_publish_enabled": True,
                "publish_timezone": "Asia/Shanghai"
            }
            self.save_config()
    
    def save_config(self):
        """保存配置文件"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def load_publish_log(self):
        """加载发布日志"""
        if os.path.exists(self.publish_log_file):
            with open(self.publish_log_file, 'r', encoding='utf-8') as f:
                self.publish_log = json.load(f)
        else:
            self.publish_log = {
                "published_articles": [],
                "last_publish_date": None,
                "total_published": 0
            }
            self.save_publish_log()
    
    def save_publish_log(self):
        """保存发布日志"""
        with open(self.publish_log_file, 'w', encoding='utf-8') as f:
            json.dump(self.publish_log, f, indent=2, ensure_ascii=False)
    
    def get_available_articles(self):
        """获取所有可用的文章列表"""
        articles = []
        
        # 扫描 CSDN_ARTICLES 目录下的所有 markdown 文件
        pattern = os.path.join(self.articles_dir, "*.md")
        md_files = glob.glob(pattern)
        
        for file_path in md_files:
            # 跳过 README 文件
            if "README" in os.path.basename(file_path):
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 提取标题
                title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else os.path.basename(file_path).replace('.md', '')
                
                # 提取标签 (如果文章中有定义)
                tags_match = re.search(r'tags:\s*\[(.*?)\]', content, re.IGNORECASE)
                tags = [tag.strip() for tag in tags_match.group(1).split(',')] if tags_match else self.config.get("tags", [])
                
                # 检查是否已发布
                is_published = any(p['file_path'] == file_path for p in self.publish_log['published_articles'])
                
                articles.append({
                    "title": title,
                    "file_path": file_path,
                    "file_name": os.path.basename(file_path),
                    "tags": tags,
                    "is_published": is_published,
                    "create_time": datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S'),
                    "modify_time": datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                })
            except Exception as e:
                print(f"⚠️  读取文件失败 {file_path}: {e}")
        
        return articles
    
    def select_today_article(self):
        """选择今天要发布的文章"""
        articles = self.get_available_articles()
        
        if not articles:
            print("❌ 没有找到可用的文章")
            return None
        
        # 过滤掉已发布的文章
        unpublished = [a for a in articles if not a['is_published']]
        
        if not unpublished:
            print("✅ 所有文章都已发布完毕!")
            # 如果都发布了，可以重新开始循环
            print("🔄 将重新开始发布循环...")
            unpublished = articles
        
        # 按创建时间排序，优先发布最早的文章
        unpublished.sort(key=lambda x: x['create_time'])
        
        # 选择第一篇未发布的文章
        selected = unpublished[0]
        
        print(f"📝 今日选择发布：{selected['title']}")
        return selected
    
    def clean_markdown_for_txt(self, content):
        """清理 Markdown 内容，转换为纯文本格式"""
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
    
    def prepare_article_content(self, article, output_format='txt'):
        """准备文章内容"""
        file_path = article['file_path']
        
        if not os.path.exists(file_path):
            print(f"❌ 文章文件不存在：{file_path}")
            return None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取标题
        title = article['title']
        
        # 添加 CSDN 特定的格式和营销内容
        if output_format == 'txt':
            formatted_content = self.add_marketing_content_txt(content, article)
        else:
            formatted_content = self.add_marketing_content(content, article)
        
        return {
            "title": title,
            "content": formatted_content,
            "tags": article['tags'],
            "category": self.config.get("default_category", "C++"),
            "file_path": file_path,
            "output_format": output_format
        }
    
    def add_marketing_content_txt(self, original_content, article):
        """添加营销内容（TXT 格式）"""
        # 清理 Markdown 格式
        cleaned_content = self.clean_markdown_for_txt(original_content)
        
        # 在文章开头添加引导语（TXT 格式）
        intro = """================================================================
导读：本文是华又科技视频监控平台系列技术文章之一。我们开源了完整的视频监控系统源码，包含 23 个核心工程项目，全部基于 C++17 和 Visual Studio 2017 开发。
项目地址：https://github.com/huayou-tech/videomonitor-platform
技术栈：C++17 | Windows IOCP | Live555 | SIP/GB28181 | RTSP/ONVIF
================================================================

"""
        
        # 在文章末尾添加推广信息（TXT 格式）
        footer = """

================================================================
关于项目
================================================================
本项目是一个完整的商业级视频监控平台，经过十年验证，稳定可靠。包含以下核心模块：

设备管控：CMService.exe - 设备注册认证、状态监控
流媒体转发：VSPMMService.exe - 基于 Live555 的高性能流媒体服务
SIP 信令：VSPSipService.exe - 支持 GB/T 28181 国标
多媒体客户端：VSPClient.exe - 视频播放、解码控制
视频录制：VRS.exe - 实时录制、存储管理
质量诊断：VQDService.exe - 视频质量分析

学习价值：
通过本项目的学习，你可以掌握：
- 大型 C++ 系统的架构设计能力
- Windows 高性能网络编程 (IOCP)
- 音视频处理核心技术
- 多协议集成 (SIP、RTSP、ONVIF)
- 企业级项目开发经验

资源链接：
- GitHub 源码：https://github.com/huayou-tech/videomonitor-platform
- 完整文档：项目各模块详细说明见 CSDN_ARTICLES 目录
- 技术交流：欢迎在评论区留言讨论

互动支持：
如果你觉得这个项目对你有帮助：
- Star 我们的 GitHub 项目
- 点赞 支持作者
- 评论 留下你的想法
- 分享 给更多需要的人

下期预告：明天我们将继续发布系列文章的下一篇，敬请期待！
"""
        
        return intro + "\n" + cleaned_content + "\n" + footer
    
    def add_marketing_content(self, original_content, article):
        """添加营销内容和推广信息"""
        # 在文章开头添加引导语
        intro = f"""
> **导读**: 本文是华又科技视频监控平台系列技术文章之一。我们开源了完整的视频监控系统源码，包含 23 个核心工程项目，全部基于 C++17 和 Visual Studio 2017 开发。
> 
> **项目地址**: https://github.com/huayou-tech/videomonitor-platform
> 
> **技术栈**: C++17 | Windows IOCP | Live555 | SIP/GB28181 | RTSP/ONVIF
"""
        
        # 在文章末尾添加推广信息
        footer = f"""

---

## 🎯 关于项目

本项目是一个**完整的商业级视频监控平台**,经过十年验证，稳定可靠。包含以下核心模块:

- **设备管控**: CMService.exe - 设备注册认证、状态监控
- **流媒体转发**: VSPMMService.exe - 基于 Live555 的高性能流媒体服务  
- **SIP信令**: VSPSipService.exe - 支持 GB/T 28181 国标
- **多媒体客户端**: VSPClient.exe - 视频播放、解码控制
- **视频录制**: VRS.exe - 实时录制、存储管理
- **质量诊断**: VQDService.exe - 视频质量分析

### 💡 学习价值

通过本项目的学习，你可以掌握:
- ✅ 大型 C++ 系统的架构设计能力
- ✅ Windows 高性能网络编程 (IOCP)
- ✅ 音视频处理核心技术
- ✅ 多协议集成 (SIP、RTSP、ONVIF)
- ✅ 企业级项目开发经验

### 🔗 资源链接

- **GitHub 源码**: https://github.com/huayou-tech/videomonitor-platform
- **完整文档**: 项目各模块详细说明见 CSDN_ARTICLES 目录
- **技术交流**: 欢迎在评论区留言讨论

### 👍 互动支持

如果你觉得这个项目对你有帮助:
- ⭐ **Star** 我们的 GitHub 项目
- 👍 **点赞** 支持作者
- 💬 **评论** 留下你的想法
- 📢 **分享** 给更多需要的人

**下期预告**: 明天我们将继续发布系列文章的下一篇，敬请期待!
"""
        
        return intro + "\n" + original_content + "\n" + footer
    
    def simulate_publish(self, article_data):
        """模拟发布过程 (实际发布需要集成 CSDN API 或 Selenium)"""
        print("\n" + "="*60)
        print(f"准备发布文章")
        print("="*60)
        print(f"标题：{article_data['title']}")
        print(f"标签：{', '.join(article_data['tags'])}")
        print(f"分类：{article_data['category']}")
        print(f"计划发布时间：{self.config.get('publish_time', '09:00')}")
        print(f"源文件：{article_data['file_path']}")
        print("="*60)
        
        # 这里可以集成实际的发布逻辑
        # 目前由于 CSDN 没有官方 API，使用 Selenium 自动化
        # 出于安全考虑，这里只做模拟
        
        print("文章内容已准备就绪")
        print("提示：可以使用以下方式完成发布:")
        print("   1. 手动复制内容到 CSDN 编辑器")
        print("   2. 使用 Selenium 自动化发布 (需配置账号)")
        print("   3. 使用 CSDN 客户端工具")
        
        # 保存到文件（根据输出格式决定扩展名）
        output_format = article_data.get('output_format', 'txt')
        extension = 'txt' if output_format == 'txt' else 'md'
        output_file = f"ready_to_publish_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{extension}"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(article_data['content'])
        
        print(f"\n文件已保存至：{output_file}")
        
        # 更新发布日志
        publish_record = {
            "title": article_data['title'],
            "file_path": article_data['file_path'],
            "publish_date": datetime.now().strftime('%Y-%m-%d'),
            "publish_time": datetime.now().strftime('%H:%M:%S'),
            "output_file": output_file,
            "output_format": output_format,
            "status": "ready_to_publish"
        }
        
        self.publish_log['published_articles'].append(publish_record)
        self.publish_log['last_publish_date'] = datetime.now().strftime('%Y-%m-%d')
        self.publish_log['total_published'] += 1
        self.save_publish_log()
        
        print(f"\n✅ 发布日志已更新 (总计：{self.publish_log['total_published']} 篇)")
        return True
    
    def auto_publish_daily(self):
        """每日自动发布任务"""
        print(f"\n📅 执行日期：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)
        
        # 检查今天是否已经发布过
        today = datetime.now().strftime('%Y-%m-%d')
        if self.publish_log['last_publish_date'] == today:
            print(f"✅ 今日 ({today}) 已发布过文章")
            last_article = self.publish_log['published_articles'][-1]['title'] if self.publish_log['published_articles'] else "无"
            print(f"📝 已发布：{last_article}")
            return
        
        # 选择今天的文章
        article = self.select_today_article()
        if not article:
            return
        
        # 准备文章内容
        article_data = self.prepare_article_content(article)
        if not article_data:
            return
        
        # 执行发布
        self.simulate_publish(article_data)
        
        print("\n" + "="*60)
        print("🎉 今日发布任务完成!")
        print("="*60)
    
    def show_publish_status(self):
        """显示发布状态"""
        print("\n" + "="*60)
        print("📊 发布状态统计")
        print("="*60)
        
        articles = self.get_available_articles()
        total = len(articles)
        published = sum(1 for a in articles if a['is_published'])
        unpublished = total - published
        
        print(f"📁 总文章数：{total}")
        print(f"✅ 已发布：{published}")
        print(f"⏳ 待发布：{unpublished}")
        print(f"📈 完成率：{published/total*100:.1f}%" if total > 0 else "📈 完成率：0%")
        
        if published > 0:
            print(f"\n📝 最近发布:")
            recent = self.publish_log['published_articles'][-5:]  # 最近 5 篇
            for i, record in enumerate(recent, 1):
                print(f"  {i}. {record['title']} ({record['publish_date']})")
        
        if unpublished > 0:
            print(f"\n⏳ 待发布文章:")
            unpublished_list = [a for a in articles if not a['is_published']][:5]  # 显示 5 篇
            for i, article in enumerate(unpublished_list, 1):
                print(f"  {i}. {article['title']}")
        
        print("="*60)
    
    def setup_scheduler(self):
        """设置定时任务"""
        publish_time = self.config.get('publish_time', '09:00')
        
        print(f"⏰ 已设置每日自动发布任务：{publish_time}")
        print("💡 提示：请保持程序运行，或使用系统任务计划程序")
        
        # 注册定时任务
        schedule.every().day.at(publish_time).do(self.auto_publish_daily)
        
        # 立即执行一次检查
        print("\n🔍 执行首次检查...")
        self.auto_publish_daily()
        
        # 运行调度器
        while True:
            try:
                schedule.run_pending()
                time.sleep(60)  # 每分钟检查一次
            except KeyboardInterrupt:
                print("\n👋 自动发布已停止")
                break
            except Exception as e:
                print(f"❌ 错误：{e}")
                time.sleep(60)

def main():
    publisher = CSDNAutoPublisher()
    
    print("="*60)
    print("🎯 CSDN 博客自动发布工具 - 华又科技")
    print("="*60)
    print(f"📁 文章目录：{os.path.abspath(publisher.articles_dir)}")
    print(f"⏰ 发布时间：{publisher.config.get('publish_time', '09:00')}")
    print(f"📊 已发布：{publisher.publish_log['total_published']} 篇")
    print("="*60)
    
    while True:
        print("\n请选择操作:")
        print("1. 📅 立即执行今日发布任务")
        print("2. 📊 查看发布状态")
        print("3. ⏰ 启动每日自动发布")
        print("4. 📝 查看所有可用文章")
        print("5. ⚙️  修改配置")
        print("6. 📈 重置发布日志")
        print("7. 👋 退出")
        
        choice = input("\n请输入选项 (1-7): ").strip()
        
        if choice == '1':
            publisher.auto_publish_daily()
            
        elif choice == '2':
            publisher.show_publish_status()
            
        elif choice == '3':
            print("\n⏰ 正在启动每日自动发布...")
            print("💡 提示：按 Ctrl+C 停止自动发布")
            publisher.setup_scheduler()
            
        elif choice == '4':
            articles = publisher.get_available_articles()
            print(f"\n📝 共有 {len(articles)} 篇文章:")
            for i, article in enumerate(articles, 1):
                status = "✅" if article['is_published'] else "⏳"
                print(f"  {i}. {status} {article['title']}")
            
        elif choice == '5':
            print("\n当前配置:")
            for key, value in publisher.config.items():
                if key not in ['password', 'cookie']:  # 不显示敏感信息
                    print(f"  {key}: {value}")
            
            new_time = input("\n输入新的发布时间 (HH:MM, 直接回车保持不变): ").strip()
            if new_time:
                publisher.config['publish_time'] = new_time
                publisher.save_config()
                print("✅ 配置已更新")
            
        elif choice == '6':
            confirm = input("⚠️  确定要重置发布日志吗？(y/n): ").strip().lower()
            if confirm == 'y':
                publisher.publish_log = {
                    "published_articles": [],
                    "last_publish_date": None,
                    "total_published": 0
                }
                publisher.save_publish_log()
                print("✅ 发布日志已重置")
            else:
                print("❌ 已取消操作")
            
        elif choice == '7':
            print("\n👋 感谢使用，再见!")
            break
            
        else:
            print("❌ 无效选项，请重新选择")

if __name__ == "__main__":
    main()