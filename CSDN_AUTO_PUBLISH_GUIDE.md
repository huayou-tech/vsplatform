# CSDN 每日自动发布工具使用说明

## 📋 工具说明

本工具用于自动管理 CSDN 技术文章的发布流程，每天自动生成一篇待发布的文章。

**重要更新**：现已支持生成 TXT 格式，自动去除 Markdown 符号和多余空行，内容更简洁清晰！

## 🚀 快速开始

### 方法一：使用批处理文件（推荐）

直接双击运行：
```
每日发布.bat
```

### 方法二：使用 PowerShell 脚本

在 PowerShell 中执行：
```powershell
Set-Location "e:\华又科技\VSS\VSPlatform"
python auto_publish_daily.py
```

### 方法三：使用 Python 脚本直接运行

```bash
cd e:\华又科技\VSS\VSPlatform
python auto_publish_daily.py
```

## 📝 发布流程

### 1. 运行自动发布脚本
- 脚本会自动扫描 `CSDN_ARTICLES` 目录
- 选择一篇未发布的文章
- **自动清理 Markdown 格式**（移除 #、*、> 等符号）
- **自动删除多余空行和空白字符**
- 添加营销内容和推广信息
- 生成带时间戳的 `ready_to_publish_*.txt` 文件

### 2. 查看生成的文件
脚本运行后会生成类似这样的文件：
```
ready_to_publish_20260306_170408.txt
```

### 3. 手动发布到 CSDN
1. 打开生成的 txt 文件
2. 复制全部内容
3. 登录 CSDN，进入写作页面
4. 粘贴内容（推荐使用富文本模式）
5. 设置分类和标签
6. 点击发布

## 📊 发布状态管理

### 查看已发布文章
发布日志保存在 `publish_log.json`，包含：
- 已发布的文章列表
- 最后发布日期
- 总计发布数量

### 重置发布日志（如果需要重新开始）
编辑 `publish_log.json`，修改为：
```json
{
  "published_articles": [],
  "last_publish_date": null,
  "total_published": 0
}
```

## 🎯 文章发布顺序

当前预设的发布顺序（按创建时间）：
1. ✅ Windows IOCP 异步模型深度解析（已发布 - 2026-03-03）
2. ✅ CommonFunc 通用函数库（已发布 - 2026-03-05）
3. ✅ DeviceStatuService 设备状态服务（已发布 - 2026-03-06）
4. ⏳ VSPCMService 设备管控核心服务
5. ⏳ HYCMService 设备管控服务详解
6. ⏳ VSPMMService 流媒体转发服务
7. ⏳ ... 更多文章

## 🎯 TXT 格式优势

相比 Markdown 格式，TXT 格式有以下优势：

✅ **无多余符号**：自动移除所有 Markdown 标记（#、*、>、- 等）  
✅ **精简空行**：删除连续多余的空行，只保留必要分段  
✅ **格式清晰**：使用等号线 (====) 分隔不同章节  
✅ **便于复制**：直接粘贴到 CSDN 编辑器即可使用  
✅ **兼容性好**：适用于任何文本编辑器和发布平台  

## ⚙️ 配置选项

配置文件 `csdn_config.json`（可选）：
```json
{
  "username": "your_username",
  "password": "your_password",
  "cookie": "your_cookie",
  "default_category": "C++",
  "tags": ["视频监控", "C++", "系统架构"],
  "publish_time": "09:00",
  "auto_publish_enabled": true,
  "publish_timezone": "Asia/Shanghai",
  "output_format": "txt"
}
```

**配置说明**：
- `output_format`: 设置为 "txt" 生成纯文本格式，设置为 "md" 生成 Markdown 格式

## 🔧 故障排查

### 问题 1：脚本报错"找不到 Python"
**解决方案**：
- 确认已安装 Python 3.x
- 将 Python 添加到系统 PATH 环境变量

### 问题 2：提示文章都已发布
**解决方案**：
- 这是正常提示，表示所有文章都发布过一遍了
- 如需重新发布，重置发布日志即可

### 问题 3：生成的文件格式不对
**解决方案**：
- 检查 csdn_config.json 中的 output_format 配置
- txt 格式会生成 .txt 文件，md 格式会生成 .md 文件

## 💡 最佳实践

1. **固定时间发布**：建议每天早上 9:00 运行一次
2. **内容审核**：发布前检查生成的内容，确保格式正确
3. **标签优化**：根据文章内容调整标签，增加曝光度
4. **互动维护**：及时回复评论，增加文章热度
5. **格式选择**：推荐使用 TXT 格式，更适合 CSDN 发布

## 📈 发布统计

截至今天已发布：**3 篇**文章
- 2026-03-03: Windows IOCP 异步模型深度解析
- 2026-03-05: CommonFunc 通用函数库  
- 2026-03-06: DeviceStatuService 设备状态服务

## 🎁 附加功能

### 自动生成推广内容
每篇文章都会自动添加：
- 项目简介和技术栈说明
- GitHub 仓库链接
- 学习价值和资源链接
- 互动引导语

### 系列文章关联
自动在文章中提及其他系列文章，形成知识体系

### 智能格式清理
- 自动移除 Markdown 符号
- 自动删除多余空行
- 自动清理行首尾空白
- 保留合理的段落结构

---

**技术支持**: 如有问题，请查看 `csdn_auto_publisher.py` 源码或联系开发团队
