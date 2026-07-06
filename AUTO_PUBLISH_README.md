# CSDN 博客自动发布工具使用说明

## 📋 功能概述

本工具可以自动从您的技术文章库中选择文章，每天定时发布到 CSDN 博客。

### 核心功能

✅ **自动选择文章**: 智能扫描 CSDN_ARTICLES 目录下的所有 markdown 文件  
✅ **每日发布**: 每天自动选择一篇未发布的文章进行发布  
✅ **状态跟踪**: 记录已发布文章，避免重复发布  
✅ **内容优化**: 自动添加营销内容和推广信息  
✅ **定时任务**: 支持设置每日固定时间自动发布  

## 🚀 快速开始

### 方法一：使用批处理文件 (推荐)

双击运行:
```
start_auto_publish.bat
```

### 方法二：直接运行 Python 脚本

```bash
python csdn_auto_publisher.py
```

## ⚙️ 配置说明

### 配置文件：csdn_config.json

首次运行时会自动创建配置文件，主要配置项:

```json
{
  "username": "your_username",        // CSDN 用户名 (可选)
  "password": "your_password",        // CSDN 密码 (可选)
  "cookie": "your_cookie",            // CSDN Cookie (可选)
  "default_category": "C++",          // 默认文章分类
  "tags": ["视频监控", "C++", "系统架构"],  // 默认标签
  "publish_time": "09:00",            // 每日发布时间 (24 小时制)
  "auto_publish_enabled": true,       // 是否启用自动发布
  "publish_timezone": "Asia/Shanghai" // 时区设置
}
```

### 修改配置

在交互式界面中选择选项 `5. ⚙️ 修改配置` 即可修改。

## 📊 使用模式

### 模式 1: 立即发布

适合手动控制发布节奏。

**操作步骤:**
1. 运行 `start_auto_publish.bat`
2. 选择 `1. 立即执行今日发布任务`
3. 工具会自动选择今天的文章并准备发布

### 模式 2: 自动发布 (推荐)

适合长期自动化运营。

**操作步骤:**
1. 运行 `start_auto_publish.bat`
2. 选择 `2. 启动每日自动发布`
3. 程序会在后台持续运行，每天定时发布

**注意**: 
- 需要保持程序运行 (可以使用 Windows 任务计划程序)
- 按 Ctrl+C 可停止自动发布

### 模式 3: 查看状态

随时查看发布进度。

**操作步骤:**
1. 运行 `start_auto_publish.bat`
2. 选择 `3. 查看发布状态`

## 📝 发布流程

### 1. 文章选择逻辑

工具会按照以下规则选择文章:

- ✅ 优先选择未发布的文章
- ✅ 按创建时间排序，优先发布最早的文章
- ✅ 如果所有文章都已发布，重新开始循环
- ✅ 跳过 README 等非文章文件

### 2. 内容处理

每篇文章会自动添加:

- 📢 **导读**: 项目介绍和技术栈说明
- 🔗 **资源链接**: GitHub 地址、文档链接
- 💡 **学习价值**: 技术亮点总结
- 👍 **互动引导**: 点赞、评论、分享提示

### 3. 发布日志

发布记录保存在 `publish_log.json`:

```json
{
  "published_articles": [
    {
      "title": "文章标题",
      "file_path": "CSDN_ARTICLES/xxx.md",
      "publish_date": "2026-03-03",
      "publish_time": "09:00:00",
      "status": "ready_to_publish"
    }
  ],
  "last_publish_date": "2026-03-03",
  "total_published": 1
}
```

## 🎯 实际发布到 CSDN

### 当前版本：模拟发布 + 内容准备

由于 CSDN 没有官方 API，工具会:

1. ✅ 准备好完整的文章内容 (包含营销内容)
2. ✅ 显示发布预览
3. ✅ 更新发布日志
4. 💡 提供三种发布方式:
   - **手动复制**: 复制内容到 CSDN 编辑器
   - **Selenium 自动化**: 需自行配置账号和浏览器驱动
   - **CSDN 客户端**: 使用第三方发布工具

### 集成 Selenium (高级用法)

如果您想完全自动化发布，可以参考以下步骤:

1. 安装依赖:
   ```bash
   pip install selenium
   ```

2. 下载 ChromeDriver: https://chromedriver.chromium.org/

3. 在代码中实现发布逻辑 (需要自行编写)

⚠️ **注意**: 自动化发布可能违反 CSDN 使用条款，请谨慎使用。

## 📈 统计与报告

### 查看发布统计

在交互界面选择 `2. 📊 查看发布状态` 可以看到:

- 总文章数
- 已发布数量
- 待发布数量
- 完成率
- 最近发布列表

### 重置发布日志

如果想重新发布所有文章:

1. 运行工具
2. 选择 `6. 📈 重置发布日志`
3. 确认操作

## ⏰ 设置 Windows 任务计划

要让程序每天自动运行，可以设置 Windows 任务计划:

### 步骤:

1. 打开 **任务计划程序**
2. 点击 **创建基本任务**
3. 名称：`CSDN 博客自动发布`
4. 触发器：每天
5. 时间：`09:00` (或您设定的时间)
6. 操作：启动程序
7. 程序/脚本：`wscript.exe`
8. 参数：`//B "E:\华又科技\VSS\VSPlatform\start_auto_publish.vbs"`
9. 完成

或者直接使用批处理文件:
- 程序：`cmd.exe`
- 参数：`/c "cd /d E:\华又科技\VSS\VSPlatform && python csdn_auto_publisher.py"`

## 🔧 故障排除

### 问题 1: Python 未安装

**错误**: `[错误] 未检测到 Python`

**解决**: 
1. 下载安装 Python: https://www.python.org/
2. 安装时勾选 "Add Python to PATH"

### 问题 2: 找不到文章文件

**错误**: `❌ 文章文件不存在`

**解决**:
1. 检查 `CSDN_ARTICLES` 目录是否存在
2. 确认文章是 markdown 格式 (.md 文件)

### 问题 3: 中文乱码

**解决**:
1. 确保文件编码为 UTF-8
2. Windows 系统建议使用 UTF-8 with BOM

## 📝 最佳实践

### 1. 发布时间选择

根据目标受众选择合适时间:
- ☀️ **早上 9:00**: 上班通勤时间
- 🍽️ **中午 12:00**: 午休时间
- 🌙 **晚上 20:00**: 下班学习时间

### 2. 文章顺序规划

建议按以下顺序发布:

1. **入门级**: 系统架构、项目介绍
2. **进阶级**: 核心技术模块
3. **高级**: 性能优化、实战经验

### 3. 互动维护

- 每天检查评论并回复
- 定期更新文章内容
- 根据反馈调整发布策略

## 💡 扩展功能

### 添加新的文章

只需将新的 markdown 文件放入 `CSDN_ARTICLES` 目录，工具会自动识别。

### 自定义营销内容

修改 `add_marketing_content()` 函数来自定义推广文案。

### 多平台发布

可以扩展代码支持:
- 知乎专栏
- 掘金
- 简书
- 微信公众号

## 📞 技术支持

如有问题，请联系:
- 📧 Email: tech@huayoutech.com
- 🌐 Blog: https://blog.csdn.net/your_username
- 💻 GitHub: https://github.com/huayou-tech/videomonitor-platform

---

**华又科技技术团队** - 专注视频监控系统研发十余年