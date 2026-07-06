# VSPCMService - Device Management Core Service

设备管控核心服务 - 视频监控系统的核心组件

## 📋 项目简介

VSPCMService 是一个成熟的企业级设备管控平台，源自华又科技十年前实际商业项目，经过十年生产环境验证，稳定可靠。

作为 VSPlatform 视频监控系统的核心服务之一，它提供了完整的设备管理、状态监控、配置管理和质量诊断功能。

## 🎯 核心功能

- **设备管理**: 支持多厂商设备接入，统一的设备控制接口
- **状态监控**: 实时设备状态采集与监控
- **配置管理**: 集中化设备配置管理
- **质量诊断**: 视频质量自动诊断与告警
- **服务发现**: 基于 SOAP/WebService 的服务发现机制

## 🏗️ 技术架构

**开发环境:**
- 编程语言：C++17
- 开发工具：Visual Studio 2017
- 操作系统：Windows 7/8/10/11

**核心技术:**
- 高并发网络通信：IOCP 模型
- Web 服务协议：SOAP/WSDL
- 数据库交互：SQL Server/MySQL
- 线程管理：自定义线程池
- 内存管理：内存池优化

**支持的协议:**
- ONVIF - 网络视频设备接口规范
- RTSP - 实时流传输协议
- SIP - 会话初始协议
- GB/T 28181 - 中国安防视频监控联网标准

## 📁 目录结构

```
VSPCMService/
├── MemPool/           # 内存池模块
├── threadpool/        # 线程池模块
├── tools/             # 工具函数库
├── webservice/        # Web 服务接口 (SOAP)
├── DBInteract.cpp     # 数据库交互实现
├── NetProtocol.cpp    # 网络协议处理
├── ServersInfo.cpp    # 服务器信息管理
├── ServiceManager.cpp # 服务管理器
└── VSPCMService.cpp   # 主服务入口
```

## 🚀 快速开始

### 前置条件

- Windows 7/8/10/11
- Visual Studio 2017 (推荐)
- Git

### 编译步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/huayou-tech/videomonitor-platform.git
   cd VSPCMService
   ```

2. **打开解决方案**
   - 使用 Visual Studio 2017 打开 `VSPCMService.sln`

3. **编译项目**
   - 选择 Debug 或 Release 配置
   - 按 F7 或选择 "生成" → "生成解决方案"

4. **运行服务**
   - 编译完成后，可执行文件位于 `bin/` 目录
   - 双击运行或以 Windows 服务方式部署

## 📖 详细文档

完整的技术文档、架构图和使用说明请查看:
- [VSPlatform 项目介绍](https://github.com/huayou-tech/videomonitor-platform/blob/main/README.md)
- [系统架构文档](https://github.com/huayou-tech/videomonitor-platform/blob/main/LEARNING_MATERIALS/ARCHITECTURE/system_architecture_overview.md)

## 💼 应用场景

- **企业园区监控**: 大型园区视频监控设备统一管理
- **智慧城市**: 城市级视频监控网络
- **教育培训**: C++ 大型系统架构学习案例
- **二次开发**: 基于成熟框架快速开发定制化监控系统

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request!

## 📄 许可证

MIT License

## 📧 联系方式

- 邮箱：tech@huayoutech.com
- 技术博客：https://blog.huayoutech.com

---

**华又科技** - 专业视频监控解决方案提供商