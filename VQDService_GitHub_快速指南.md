# VQDService GitHub 上传快速指南

## 🚀 三种上传方式（任选其一）

### 方式一：双击批处理文件（最简单 ⭐⭐⭐⭐⭐）

```
直接双击运行：上传_vqdservice.bat
```

**优点**：一键操作，自动完成所有步骤  
**适合人群**：Git 初学者

---

### 方式二：PowerShell 命令行（推荐 ⭐⭐⭐⭐）

打开 PowerShell，执行：

```powershell
Set-Location "e:\华又科技\VSS\VSPlatform"
.\upload_vqdservice_to_github.ps1
```

**优点**：可以看到详细输出，支持自定义参数  
**适合人群**：有一定技术基础的用户

**带参数执行示例**：

```powershell
.\upload_vqdservice_to_github.ps1 -GitHubRepoUrl "https://github.com/huayoutech/vsp-vqd-service.git" -CommitMessage "Initial commit: VQDService"
```

---

### 方式三：手动 Git 命令（灵活控制 ⭐⭐⭐）

详见文档：`上传_VQDService_到_GitHub_指南.md`

**优点**：完全控制每个步骤  
**适合人群**：Git 高级用户

---

## 📋 上传前准备清单

✅ **必须完成**：
- [ ] 已安装 Git（验证：`git --version`）
- [ ] 已注册 GitHub 账号
- [ ] 已在 GitHub 创建空仓库（如：`vsp-vqd-service`）
- [ ] 已获取仓库 URL（如：`https://github.com/huayoutech/vsp-vqd-service.git`）

✅ **建议准备**：
- [ ] 配置 Git 用户名和邮箱
- [ ] 生成 Personal Access Token（用于身份验证）
- [ ] 准备好项目描述和标签

---

## 🎯 标准操作流程

### 第 1 步：创建 GitHub 仓库

1. 访问 [https://github.com/new](https://github.com/new)
2. 填写信息：
   - **Repository name**: `vsp-vqd-service`
   - **Description**: "Video Quality Diagnostic Service - 视频质量诊断服务"
   - **Public**: 公开（开源项目）
   - **Private**: 私有（可选）
3. **不要勾选** "Initialize this repository with a README"
4. 点击 "Create repository"

### 第 2 步：运行上传脚本

```powershell
# 复制仓库 URL
$repoUrl = "https://github.com/huayoutech/vsp-vqd-service.git"

# 执行上传脚本
Set-Location "e:\华又科技\VSS\VSPlatform"
.\upload_vqdservice_to_github.ps1 -GitHubRepoUrl $repoUrl
```

### 第 3 步：按提示操作

脚本会引导您完成以下步骤：
1. ✅ 创建临时上传目录
2. ✅ 复制所有源码文件
3. ✅ 生成 README.md 文档
4. ✅ 初始化 Git 仓库
5. ✅ 配置 Git 用户信息
6. ✅ 创建 .gitignore 文件
7. ✅ 添加文件到暂存区
8. ✅ 提交更改
9. ✅ 连接远程仓库
10. ✅ 推送到 GitHub

### 第 4 步：验证上传成功

1. 访问你的 GitHub 仓库页面
2. 检查文件列表是否完整
3. 查看 README 是否正确显示
4. Star 支持一下自己的项目 ✨

---

## 🔐 身份验证解决方案

### 问题：Push 时要求输入密码？

**原因**：GitHub 从 2021 年 8 月起不再支持账户密码进行 Git 操作

**解决方案**：使用 Personal Access Token

#### 步骤 1：生成 Token

1. 访问：[https://github.com/settings/tokens](https://github.com/settings/tokens)
2. 点击 "Generate new token (classic)"
3. 填写说明（Note）：`VQDService Upload`
4. 选择过期时间：建议 90 天
5. 勾选权限：
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
6. 点击 "Generate token"
7. **立即复制 Token**（只显示一次！）

#### 步骤 2：使用 Token

当 Git 要求输入密码时：
- **Username**: 你的 GitHub 用户名
- **Password**: 粘贴刚才复制的 Token（不是账户密码！）

或者设置凭证管理器避免重复输入：
```bash
git config --global credential.helper wincred
```

---

## 📊 上传内容说明

### ✅ 会被上传的文件

| 类型 | 文件 | 说明 |
|------|------|------|
| **源代码** | *.cpp, *.h | 所有 C++ 源文件和头文件 |
| **项目配置** | *.vcxproj, *.rc | VS 项目文件和资源文件 |
| **文档** | README.md, ReadMe.txt | 项目说明文档 |
| **图标** | *.ico | 应用程序图标 |

### ❌ 不会被上传的文件（已在 .gitignore 中排除）

| 类型 | 文件/目录 | 原因 |
|------|-----------|------|
| **编译输出** | Debug/, Release/ | 体积大，可重新编译 |
| **中间文件** | *.obj, *.pdb, *.ilk | 构建过程文件 |
| **用户配置** | *.user, .vs/ | 个人化设置 |
| **二进制资源** | *.aps | 自动生成 |

---

## 🎉 上传成功后的操作

### 1. 完善 GitHub 仓库信息

- 添加 Topics 标签：
  ```
  video-quality, diagnostic, cpp, surveillance, ffmpeg, opencv, windows
  ```
- 编辑 About 描述：
  ```
  Professional video quality diagnostic service for surveillance platforms
  ```
- 添加网站链接（如果有）

### 2. 推广你的项目

- 📝 发布 CSDN 技术博客（文章已生成：`ready_to_publish_20260318_111410.txt`）
- 💬 分享到技术社区（知乎、掘金、V2EX）
- 🐦 在社交媒体宣传（微博、Twitter）
- 📧 发送给潜在客户和合作伙伴

### 3. 持续维护

- 及时回复 Issues
- 接受 Pull Requests
- 定期更新代码
- 添加新功能和技术文档

---

## 🆘 常见问题快速解决

### ❌ 错误：Git not found

**解决**：安装 Git 并添加到 PATH
```bash
# 下载地址
https://git-scm.com/download/win
```

### ❌ 错误：Remote origin already exists

**解决**：
```bash
git remote remove origin
git remote add origin <your-repo-url>
```

### ❌ 错误：Updates were rejected because the remote contains work that you do not have

**解决**：
```bash
# 强制推送（慎用，会覆盖远程内容）
git push -f origin master

# 或者先拉取再合并
git pull origin master --allow-unrelated-histories
git push -u origin master
```

### ❌ 错误：中文文件名乱码

**解决**：
```bash
git config --global core.quotepath false
git config --global gui.encoding utf-8
```

---

## 📞 获取更多帮助

### 官方文档
- [Git 官方文档](https://git-scm.com/book/zh/v2)
- [GitHub 帮助中心](https://docs.github.com/)

### 视频教程
- Bilibili: "Git 入门教程"
- YouTube: "GitHub Tutorial for Beginners"

### 技术支持
- **微信公众号**: 华又科技
- **GitHub Issues**: 在项目页提问
- **CSDN 博客**: 查看系列技术文章

---

## 🎁 附加工具和模板

### Git 配置优化（推荐）

```bash
# 全局 UTF-8 支持
git config --global core.quotepath false
git config --global gui.encoding utf-8
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding utf-8

# 默认编辑器设置为 VS Code
git config --global core.editor "code --wait"

# 凭证管理（避免重复输入密码）
git config --global credential.helper wincred
```

### 常用 Git 命令速查

```bash
# 查看状态
git status

# 查看提交历史
git log --oneline

# 撤销上次提交
git reset --soft HEAD~1

# 查看远程仓库
git remote -v

# 切换分支
git checkout -b feature/new-feature

# 合并分支
git merge feature/new-feature
```

---

## ✨ 总结

通过本指南，您可以：

✅ **3 分钟内**完成 VQDService 源码上传  
✅ **零门槛**使用自动化脚本工具  
✅ **专业级**GitHub 项目文档和结构  
✅ **一站式**解决所有常见问题  

**立即开始您的开源之旅吧！** 🚀

---

*Last Updated: 2026-03-18*  
*Author: 华又科技技术团队*