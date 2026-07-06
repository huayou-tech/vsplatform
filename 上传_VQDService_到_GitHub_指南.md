# VQDService 源码上传到 GitHub 指南

本文档详细说明如何将 VQDService（视频质量诊断服务）源码上传到 GitHub。

---

## 📋 准备工作

### 1. 安装 Git

如果尚未安装 Git，请前往 [https://git-scm.com/](https://git-scm.com/) 下载并安装。

安装后验证：
```bash
git --version
```

### 2. 创建 GitHub 账号

如果没有 GitHub 账号，请前往 [https://github.com/](https://github.com/) 注册。

### 3. 创建空仓库

在 GitHub 上创建一个新的空仓库（不要初始化 README、.gitignore 或 license）：
- 访问：[https://github.com/new](https://github.com/new)
- 仓库名称建议：`vsp-vqd-service` 或 `video-quality-diagnostic`
- 设为公开（Public）或私有（Private）
- **不要勾选** "Initialize this repository with a README"

---

## 🚀 快速上传（推荐方式）

### 方法一：使用批处理文件（最简单）

双击运行：
```
上传_vqdservice.bat
```

按照提示操作即可。

### 方法二：使用 PowerShell 脚本

打开 PowerShell，执行：
```powershell
Set-Location "e:\华又科技\VSS\VSPlatform"
.\upload_vqdservice_to_github.ps1
```

或者带参数执行：
```powershell
.\upload_vqdservice_to_github.ps1 -GitHubRepoUrl "https://github.com/yourusername/vsp-vqd-service.git" -CommitMessage "Initial commit: VQDService video quality diagnostic service"
```

---

## 📝 手动上传步骤

如果想手动控制每个步骤：

### 步骤 1：准备项目文件

```powershell
# 进入项目目录
cd "HYCMService\VQDService"

# 复制所有源码到新目录
mkdir temp_upload
Copy-Item *.cpp,*.h,*.rc,*.aps,*.vcxproj,*.vcxproj.filters,*.txt,.ico temp_upload/
Copy-Item Debug/*.dll,temp_upload/Debug/ (如果需要)
```

### 步骤 2：初始化 Git 仓库

```powershell
cd temp_upload
git init
```

### 步骤 3：添加文件

```powershell
# 创建 .gitignore
notepad .gitignore
# 添加以下内容：
Debug/
Release/
*.aps
*.user
.vs/
Thumbs.db

# 添加所有文件到 Git
git add .
```

### 步骤 4：提交更改

```powershell
git commit -m "Initial commit: VQDService video quality diagnostic service"
```

### 步骤 5：连接远程仓库

```powershell
# 替换为你的仓库地址
git remote add origin https://github.com/yourusername/vsp-vqd-service.git
```

### 步骤 6：推送到 GitHub

```powershell
# 首次推送
git push -u origin master

# 或使用新分支
git push -u origin main
```

---

## 🔐 身份验证方式

### 方式一：Personal Access Token（推荐）

1. 访问：[https://github.com/settings/tokens](https://github.com/settings/tokens)
2. 点击 "Generate new token"
3. 选择权限：`repo` (Full control of private repositories)
4. 生成 Token 并复制
5. Push 时输入 Token 而不是密码

### 方式二：SSH Key

```bash
# 生成 SSH Key
ssh-keygen -t ed25519 -C "your_email@example.com"

# 添加到 GitHub
# 访问：https://github.com/settings/keys
# 复制 ~/.ssh/id_ed25519.pub 内容添加到 GitHub

# 使用 SSH URL
git remote add origin git@github.com:yourusername/vsp-vqd-service.git
```

---

## 📊 上传内容清单

上传到 GitHub 的文件包括：

✅ **源代码文件**
- `DiagnoseInstance.cpp/h` - 诊断实例实现
- `SysInit.cpp/h` - 系统初始化
- `VQDService.cpp/h` - 主服务入口
- `DataDef.h` - 数据结构定义
- `md.cpp/h` - 质量诊断核心算法
- `WinCriticalSection.cpp/h` - 临界区封装
- `singleton.h` - 单例模式

✅ **项目配置文件**
- `VQDService.vcxproj` - VS 项目配置
- `VQDService.vcxproj.filters` - 过滤器配置
- `VQDService.rc` - 资源文件
- `resource.h` - 资源头文件

✅ **文档**
- `README.md` - 项目说明文档
- `ReadMe.txt` - 原始说明文件

❌ **不上传的内容**（已在 .gitignore 中排除）
- `Debug/` `Release/` - 编译输出目录
- `*.aps` - 二进制资源文件
- `*.user` - 用户配置文件
- `*.pdb` `*.ilk` `*.obj` - 中间文件
- `.vs/` - VS 缓存

---

## ✅ 验证上传成功

1. 访问你的 GitHub 仓库页面
2. 检查文件是否完整
3. 查看 README.md 是否正确显示
4. 尝试在本地克隆仓库：
   ```bash
   git clone https://github.com/yourusername/vsp-vqd-service.git
   ```

---

## 🔧 常见问题

### Q1: Push 时提示认证失败？

**解决方案**：使用 Personal Access Token 替代密码
```bash
# 设置凭证管理器
git config --global credential.helper wincred

# 重新推送
git push -u origin master
```

### Q2: 仓库已存在内容怎么办？

如果 GitHub 仓库已经有 README 或其他文件：
```bash
# 拉取远程内容
git pull origin master --allow-unrelated-histories

# 解决冲突（如果有）

# 再次推送
git push -u origin master
```

### Q3: 如何更新已上传的代码？

```bash
# 修改代码后
git add .
git commit -m "Fix: 修复 XXX 问题"
git push origin master
```

### Q4: 中文路径乱码？

```bash
# 设置 Git 正确处理 UTF-8
git config --global core.quotepath false
git config --global gui.encoding utf-8
git config --global i18n.commitencoding utf-8
```

---

## 📞 获取帮助

- **GitHub 文档**: [https://docs.github.com/](https://docs.github.com/)
- **Git 教程**: [https://git-scm.com/book/zh/v2](https://git-scm.com/book/zh/v2)
- **技术支持**: 关注微信公众号【华又科技】留言

---

## 🎯 后续步骤

上传成功后：

1. ✅ 在 GitHub 上完善项目描述和标签
2. ✅ 添加 Topics: `video-quality`, `diagnostic`, `cpp`, `surveillance`
3. ✅ 设置 GitHub Pages（可选）
4. ✅ 启用 GitHub Issues（用于问题追踪）
5. ✅ 添加 CI/CD 工作流（可选）
6. ✅ 分享项目到技术社区和社交媒体

---

**🎉 恭喜！您已成功将 VQDService 上传到 GitHub！**

接下来可以开始推广您的开源项目了！