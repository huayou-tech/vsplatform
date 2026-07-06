# VSPCMService GitHub 推送操作指南

## 📋 当前状态

✅ **已完成准备工作:**
- 93 个源文件已复制到 `temp_github_upload/` 目录
- Git 仓库已初始化并完成提交 (Commit ID: 5fa76f9)
- Git 用户信息已配置 (huayou-tech / 3153290868@qq.com)
- 远程仓库 URL: https://github.com/huayou-tech/videomonitor-platform.git

⚠️ **遇到的问题:**
- HTTPS 推送：网络连接被重置 (Connection was reset)
- SSH 推送：缺少 SSH key，认证失败

## 🔧 解决方案 (请选择其中一种)

### 方案一：使用 Personal Access Token (推荐)

GitHub 从 2021 年起不再支持密码推送，需要使用 Personal Access Token。

**步骤:**

1. **生成 Personal Access Token:**
   - 访问 GitHub: https://github.com/settings/tokens
   - 点击 "Generate new token" → "Generate new token (classic)"
   - 填写备注 (如: "VSPCMService Upload")
   - 勾选权限：✅ repo (全部)、✅ workflow、✅ write:packages
   - 点击 "Generate token"
   - **重要**: 复制生成的 token (只显示一次!)

2. **使用 Token 进行推送:**

   打开命令行，进入临时目录并执行:
   ```bash
   cd e:\华又科技\VSS\VSPlatform\temp_github_upload
   git push -u origin master
   ```
   
   当提示输入密码时:
   - Username: `huayou-tech`
   - Password: **粘贴刚才生成的 Personal Access Token** (不是 GitHub 密码!)

3. **推送成功后验证:**
   - 访问 https://github.com/huayou-tech/videomonitor-platform
   - 确认代码已成功上传

### 方案二：配置 SSH Key (长期方案)

如果您计划长期使用 GitHub，建议配置 SSH key。

**步骤:**

1. **生成 SSH Key:**
   ```bash
   ssh-keygen -t ed25519 -C "3153290868@qq.com"
   ```
   - 按回车接受默认路径
   - 可选择设置 passphrase 或直接回车跳过

2. **添加 SSH Key 到 GitHub:**
   - 复制公钥内容:
     ```bash
     cat ~/.ssh/id_ed25519.pub
     ```
   - 访问：https://github.com/settings/keys
   - 点击 "New SSH key"
   - 粘贴公钥内容，保存

3. **切换为 SSH 协议并推送:**
   ```bash
   cd e:\华又科技\VSS\VSPlatform\temp_github_upload
   git remote set-url origin git@github.com:huayou-tech/videomonitor-platform.git
   git push -u origin master
   ```

### 方案三：使用 Git Credential Manager (最简单)

Git for Windows 自带凭证管理器，可以自动处理认证。

**步骤:**

1. **清除可能存在的旧凭证:**
   ```bash
   git credential-manager erase
   protocol: https
   host: github.com
   ^D
   ```

2. **重新推送:**
   ```bash
   cd e:\华又科技\VSS\VSPlatform\temp_github_upload
   git push -u origin master
   ```
   
   系统会自动弹出浏览器窗口进行认证，按照提示登录 GitHub 即可。

## 🎯 快速执行命令

在 PowerShell 中直接执行以下命令:

```powershell
cd e:\华又科技\VSS\VSPlatform\temp_github_upload
git remote -v  # 确认远程仓库地址
git push -u origin master  # 执行推送
```

## ✅ 验证推送成功

推送成功后，您应该看到类似输出:
```
Enumerating objects: 93, done.
Counting objects: 100% (93/93), done.
Delta compression using up to 8 threads
Compressing objects: 100% (XX/XX), done.
Writing objects: 100% (93/93), XX.XX KiB | XX.XX MiB/s, done.
Total 93 (delta XX), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (XX/XX), done.
To https://github.com/huayou-tech/videomonitor-platform.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

然后访问 GitHub 仓库页面确认文件已上传。

## 📞 需要帮助?

如果仍然遇到问题，请提供:
1. 完整的错误信息
2. 网络环境 (是否需要代理)
3. GitHub 账号是否有该仓库的写入权限

---
**生成时间**: 2026-03-03
**项目**: VSPCMService Device Management Core Service