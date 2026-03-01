---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7GNR3UZ%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHujRTzILAi1mk33hQ4ZqlC1EAdF%2By%2Bf%2B9BvQxNbZtDQAiEAzk9lK4xaIMATErrx623VB5uLGQIPupNtc%2FAo4fAZtKgq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDK7sUyYDGxPfEXvnPyrcA5Dn5BiHcornFVbvAIxwykVEddVYs%2F6PnXwLHaz4JIfn%2BfDbhKolf5zIYqBO5Ofx8oUSEyZtGMDU9ONe%2FQ1grRcOMC%2BKasKsZiprRZOeId6XWz%2BM1Zx61I2Yb6TCF9uGo%2FBo48aEuMp1SyiP8isImNC5Oi47mP3nsd%2FF5tWXqs%2BqT9eYpHuLQjpjRwOqnj%2FJcMbjEPZu2WMEZTLu5W8AxRbUDD5VisNlGX6HESiCN%2FJvAmetP6U8NyBPjNLQYSPDZ%2B5p28vSpShBFVFL%2Fo5nc0A3WZOI3J1V0hJ9%2Fcuz%2BaTOEvV4va1NMTQ7ulOeXfPdydqSOK6%2FIHWL7QHVm1hJ9x1QYLg0A%2BOZWppw7uKRE3I0MQErUKmyb1x8klUanF7aKU0HJu8YwyNKo11jAkz8t9fSbSxWoPX%2FAIv0Ou9vG5ic8gZq%2F36j90aFpPEFJfA%2FAVYdQ5uq0Ta1jryI%2BekDnK%2FEsF1CIQpE%2BeCir9Xd6w0FenuRSdizi4vBHRH8O3ULlqtrGrlu9hQhR3%2Be2CdiVB3%2FdQXysLsGTK3jUHEq3OZXWiUO9jaKO%2FvcKyZOWsOyeJo3k4%2BOw7nymUcAOPlx9Bo5rV2RFFfSYEkTQkD3UbfjZHJk%2FemYvJ27CycTMKjNjs0GOqUBdqy1f61DlgQKGSL2io7tfHbph1AnO2z6fQ3dLo6I%2B6gq4s7m26fwahUhRaNWr%2F2n12JBDlYG4VoV8TBFi1Ln0OaFcE6SXg%2F9g28JDnEr%2Fe8LufHv5VDvzR%2FBbPBKjTq70OpMPWdSJ1xCmVbqF67jgjwgNRXHrJtcNNIpGDdpSDEEAZmGH9MrEg9LkXSBpovc9MY8H3NGsK8W5YVudD5XnKvR0oyv&X-Amz-Signature=245d54e786c8866f042eb213634c2c130d602a46ce3fdf85ff754edc4fae7d54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7GNR3UZ%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHujRTzILAi1mk33hQ4ZqlC1EAdF%2By%2Bf%2B9BvQxNbZtDQAiEAzk9lK4xaIMATErrx623VB5uLGQIPupNtc%2FAo4fAZtKgq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDK7sUyYDGxPfEXvnPyrcA5Dn5BiHcornFVbvAIxwykVEddVYs%2F6PnXwLHaz4JIfn%2BfDbhKolf5zIYqBO5Ofx8oUSEyZtGMDU9ONe%2FQ1grRcOMC%2BKasKsZiprRZOeId6XWz%2BM1Zx61I2Yb6TCF9uGo%2FBo48aEuMp1SyiP8isImNC5Oi47mP3nsd%2FF5tWXqs%2BqT9eYpHuLQjpjRwOqnj%2FJcMbjEPZu2WMEZTLu5W8AxRbUDD5VisNlGX6HESiCN%2FJvAmetP6U8NyBPjNLQYSPDZ%2B5p28vSpShBFVFL%2Fo5nc0A3WZOI3J1V0hJ9%2Fcuz%2BaTOEvV4va1NMTQ7ulOeXfPdydqSOK6%2FIHWL7QHVm1hJ9x1QYLg0A%2BOZWppw7uKRE3I0MQErUKmyb1x8klUanF7aKU0HJu8YwyNKo11jAkz8t9fSbSxWoPX%2FAIv0Ou9vG5ic8gZq%2F36j90aFpPEFJfA%2FAVYdQ5uq0Ta1jryI%2BekDnK%2FEsF1CIQpE%2BeCir9Xd6w0FenuRSdizi4vBHRH8O3ULlqtrGrlu9hQhR3%2Be2CdiVB3%2FdQXysLsGTK3jUHEq3OZXWiUO9jaKO%2FvcKyZOWsOyeJo3k4%2BOw7nymUcAOPlx9Bo5rV2RFFfSYEkTQkD3UbfjZHJk%2FemYvJ27CycTMKjNjs0GOqUBdqy1f61DlgQKGSL2io7tfHbph1AnO2z6fQ3dLo6I%2B6gq4s7m26fwahUhRaNWr%2F2n12JBDlYG4VoV8TBFi1Ln0OaFcE6SXg%2F9g28JDnEr%2Fe8LufHv5VDvzR%2FBbPBKjTq70OpMPWdSJ1xCmVbqF67jgjwgNRXHrJtcNNIpGDdpSDEEAZmGH9MrEg9LkXSBpovc9MY8H3NGsK8W5YVudD5XnKvR0oyv&X-Amz-Signature=37dbea61ece99f9c5e4a9625f9b33b797e678d0fcb16c0781b2a0aa158fed2f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

