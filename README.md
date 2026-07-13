# 华又科技 · 企业级视频监控平台（VSPlatform）

> 🏭 一套**经过十年生产环境验证**的安防视频监控平台完整源码
> 覆盖：设备接入 → 流媒体转发 → 质量诊断 → 客户端 / 电视墙 全链路
> 支持协议：ONVIF / RTSP / SIP / **GB/T 28181 国标**

[![十年生产验证](https://img.shields.io/badge/生产验证-10%2B%20years-success)]()
[![模块数](https://img.shields.io/badge/可售模块-19-blue)]()
[![协议](https://img.shields.io/badge/协议-GB28181%20%7C%20ONVIF%20%7C%20RTSP-orange)]()
[![授权](https://img.shields.io/badge/商业授权-非开源-red)]()

---

## 🔥 为什么是这套，而不是网上那些 demo？

- ✅ **真·生产代码**：十年真实安防项目沉淀，跑过上千路设备并发，不是教学玩具。
- ✅ **全链路闭环**：从设备接入、流媒体转发、质量诊断到客户端 / 电视墙，一条龙源码。
- ✅ **国标即开箱**：SIP / GB/T 28181 国标接入直接打通，国内安防项目最大门槛帮你跨过。
- ✅ **文档齐全**：设备接入 SDK 自带 39 篇 HTML 接口文档，买回去能直接编能用。
- ✅ **可独立编译**：每个仓库 = 一个可独立使用的产品，决策成本低。

---

## 🧱 平台架构（一眼看懂）

```
┌─────────────────────────────────────────────────────────────┐
│                        应用层 / 展示层                         │
│   HYDisplay 客户端 · OCX 网页控件 · TVWallSystem 电视墙        │
├─────────────────────────────────────────────────────────────┤
│                        业务 / 管控层                          │
│   HYCMService 中心管理 · HYMMService 媒体管理 · VSPCMService   │
├─────────────────────────────────────────────────────────────┤
│                        智能 / 诊断层                          │
│   VQDService 视频质量诊断（编码/传输/播放三维）                │
├─────────────────────────────────────────────────────────────┤
│                        流媒体 / 协议层                        │
│   HYRTService · RTSPClientSDK · HYSipServer(GB28181)          │
├─────────────────────────────────────────────────────────────┤
│                        接入 / 采集 / 播放层                   │
│   VSNetSDK · VSPlaySDK · VSMNetSDK · HYVideoCapSDK            │
├─────────────────────────────────────────────────────────────┤
│                        设备层（海康/大华/宇视…）              │
│   标准协议 ONVIF / RTSP / SIP / GB28181                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 模块清单与价格

### 🆓 免费层（引流 / 学习，GitHub 公开）

| 仓库 | 内容 |
|------|------|
| [common-libs](https://github.com/huayou-tech/common-libs) | 公共基础库：线程池 / 内存池 / conhash / tinyxml / CxImage / DuiLib / boost / live555 / ffmpeg |
| [hyclog](https://github.com/huayou-tech/hyclog) | 跨平台 C 日志库 |
| [vsplatform-learning](https://github.com/huayou-tech/vsplatform-learning) | 系统架构 / 核心概念 / 实战 / 习题（教程包） |

### 💰 入门 SDK 层（¥299–599）

| 仓库 | 内容 | 参考价 |
|------|------|--------|
| [vsnetsdk](https://github.com/huayou-tech/vsnetsdk) | 设备接入 SDK（登录/预览/云台/回放，含 39 篇接口文档） | ¥399 |
| [vsplaysdk](https://github.com/huayou-tech/vsplaysdk) | 音视频播放解码 SDK（硬解/软解/多画面） | ¥399 |
| [vsmnetsdk](https://github.com/huayou-tech/vsmnetsdk) | 媒体资源管理 / 转发 SDK | ¥399 |
| [rtspclientsdk](https://github.com/huayou-tech/rtspclientsdk) | RTSP 客户端拉流 SDK | ¥299 |
| [hyregisterlib](https://github.com/huayou-tech/hyregisterlib) | 软件授权注册库（机器码+注册码，可独立用于任何软件） | ¥299 |

### 💎 标准服务层（¥799–999）

| 仓库 | 内容 | 参考价 |
|------|------|--------|
| [hyvideocapsdk](https://github.com/huayou-tech/hyvideocapsdk) | 视频采集 / 编码 SDK（含 IDL，支持 COM） | ¥899 |
| [hyrtservice](https://github.com/huayou-tech/hyrtservice) | RTSP 实时流转发服务 | ¥799 |
| [hydisplay](https://github.com/huayou-tech/hydisplay) | 多媒体客户端 + OCX 网页控件 | ¥999 |
| [hymmservice](https://github.com/huayou-tech/hymmservice) | 媒体管理服务 | ¥899 |
| [tvwallsystem](https://github.com/huayou-tech/tvwallsystem) | 电视墙多屏拼接系统 | ¥999 |
| [hycmservice](https://github.com/huayou-tech/hycmservice) | 中心管理服务 | ¥899 |

### 🏆 高溢价核心层（¥2999，核心壁垒）

| 仓库 | 内容 | 参考价 |
|------|------|--------|
| [hysipserver](https://github.com/huayou-tech/hysipserver) | **SIP / GB28181 国标接入**（打通国内安防最大门槛） | ¥2999 |
| [vqdservice](https://github.com/huayou-tech/vqdservice) | **视频质量诊断**（编码/传输/播放三维，FFmpeg+OpenCV，<100ms/100+路） | ¥2999 |
| [vspcmservice](https://github.com/huayou-tech/vspcmservice) | **设备管控核心服务**（IOCP 高并发 + 线程池 + SOAP） | ¥2999 |

> 💡 **打包更划算**：任 2 个入门 SDK ¥899 ｜ 任 3 个标准服务 ¥2999 ｜ 高溢价三件套 ¥8999 ｜ **全套 19 仓含视频课+答疑仅 ¥19999**

---

## 🚀 典型买家场景

- **集成商**：拿 `vsnetsdk` + `vsplaysdk` 快速对接自家设备，省下几个月自研。
- **创业团队**：用 `vqdservice` 做直播质量监控 SaaS。
- **政企项目**：用 `hysipserver` 直接满足 28181 国标接入硬性要求。
- **培训机构**：用 `vsplatform-learning` + 全套源码做 C++ 大型系统架构课程。

---

## 🛒 如何购买（3 步）

1. **选模块**：上面清单挑你要的仓库，或选打包方案。
2. **联系下单**：发邮件 **183144350@qq.com** 或加微信公众号 **华又科技**，告知模块名。
3. **收货**：付款后开通**私有 Git 仓库访问权限** + 编译指导文档 + **1 个月答疑**。

> 支持对公转账 / 微信 / 支付宝。企业多项目、多团队、培训授权另议。

---

## 📜 授权与售后

- ✅ 购买后可在 **一个**商业项目中使用 / 修改源码。
- ❌ 禁止公开上传、转售、再分发、打包进其他源码售卖产品（受 `LICENSE-SOURCE.txt` 保护）。
- 🛠 交付含：私有仓访问 + 编译文档 + 1 个月技术答疑。
- 🏢 企业授权请联系 183144350@qq.com。

---

## ❓ 常见问题

**Q：能用在商用项目吗？**
A：可以，授权允许在一个商业项目中使用/修改，禁止转售源码本身。

**Q：有编译好的 exe 吗？**
A：提供完整可编译源码 + 编译文档，环境为 VS2017 + Windows。

**Q：支持海康/大华设备吗？**
A：通过 ONVIF / GB28181 标准协议接入，主流厂商均兼容。

**Q：能便宜吗？**
A：多模块打包有折扣，全套含视频教程和答疑仅 ¥19999。

---

## 📞 联系我们

- 邮箱：**183144350@qq.com**
- 微信公众号：**华又科技**
- GitHub Org：[@huayou-tech](https://github.com/huayou-tech)

---

*© 华又科技 Huayou Technology. 源码受《源代码授权协议》保护，非开源项目。All Rights Reserved.*
