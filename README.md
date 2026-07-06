# 华又科技 · 企业级视频监控平台（VSPlatform）

> 🏭 一套**经过十年生产环境验证**的安防视频监控平台完整源码
> 覆盖：设备接入 → 流媒体转发 → 质量诊断 → 客户端/电视墙 全链路
> 支持协议：ONVIF / RTSP / SIP / **GB/T 28181 国标**

---

## ⚠️ 重要声明：这不是开源项目

本组织下所有代码**受《源代码授权协议》(LICENSE-SOURCE.txt) 保护**，**不是 MIT / 不是开源**。
- ❌ 禁止公开上传、转售、再分发、打包进其他源码售卖产品
- ✅ 购买后可在**一个**商业项目中使用 / 修改
- 🏢 企业授权（多项目 / 多团队 / 培训）请联系 **tech@huayoutech.com**

---

## 📦 模块清单与价格

### 🆓 免费层（引流 / 学习）
| 仓库 | 内容 |
|------|------|
| [`common-libs`](../../common-libs) | 公共基础库：线程池 / 内存池 / conhash / tinyxml / CxImage / DuiLib / boost / live555 / ffmpeg |
| [`hyclog`](../../hyclog) | 跨平台 C 日志库 |
| [`vsplatform-learning`](../../vsplatform-learning) | 系统架构 / 核心概念 / 实战 / 习题（教程包） |

### 💰 付费层（SDK / 服务）
| 仓库 | 内容 | 参考价 |
|------|------|--------|
| [`vsnetsdk`](../../vsnetsdk) | 设备接入 SDK（登录/预览/云台/回放，含 39 篇接口文档） | ¥XXX |
| [`vsplaysdk`](../../vsplaysdk) | 音视频播放解码 SDK | ¥XXX |
| [`vsmnetsdk`](../../vsmnetsdk) | 媒体资源管理 / 转发 SDK | ¥XXX |
| [`hyvideocapsdk`](../../hyvideocapsdk) | 视频采集 / 编码 SDK（含 IDL，支持 COM） | ¥XXX |
| [`hyrtservice`](../../hyrtservice) | RTSP 实时流转发服务 | ¥XXX |
| [`rtspclientsdk`](../../rtspclientsdk) | RTSP 客户端拉流 SDK | ¥XXX |
| [`hydisplay`](../../hydisplay) | 多媒体客户端 + OCX 网页控件 | ¥XXX |
| [`hycmservice`](../../hycmservice) | 中心管理服务（含 VQD/VSPCM 子模块） | ¥XXX |
| [`hymmservice`](../../hymmservice) | 媒体管理服务 | ¥XXX |
| [`tvwallsystem`](../../tvwallsystem) | 电视墙多屏拼接系统 | ¥XXX |
| [`hyregisterlib`](../../hyregisterlib) | 软件授权注册库（机器码+注册码，可独立用于任何软件） | ¥XXX |

### 💎 高溢价层（核心壁垒）
| 仓库 | 内容 | 参考价 |
|------|------|--------|
| [`hysipserver`](../../hysipserver) | **SIP / GB28181 国标接入**（打通国内安防最大门槛） | ¥XXXX |
| [`vqdservice`](../../vqdservice) | **视频质量诊断**（编码/传输/播放三维，FFmpeg+OpenCV，<100ms/100+路） | ¥XXXX |
| [`vspcmservice`](../../vspcmservice) | **设备管控核心服务**（IOCP 高并发 + 线程池 + SOAP） | ¥XXXX |

> 价格为占位，请按渠道（CSDN / 码市 / 微信）实际定价。打包购买享折扣。

---

## 🚀 典型买家场景
- **集成商**：拿 `vsnetsdk` + `vsplaysdk` 快速对接自家设备
- **创业团队**：用 `vqdservice` 做直播质量监控 SaaS
- **政企项目**：用 `hysipserver` 直接满足 28181 国标接入要求
- **培训机构**：用 `vsplatform-learning` + 全套源码做 C++ 大型系统课程

---

## 📞 购买与支持
- 邮箱：**tech@huayoutech.com**
- 微信公众号：**华又科技**
- 购买后提供：源码私有仓访问 + 编译指导 + 1 个月答疑

---

*© 华又科技 Huayou Technology. All Rights Reserved.*
