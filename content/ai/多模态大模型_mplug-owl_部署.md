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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3CAZJZR%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAy4ySIenxHui8lA4NbqLTVG7%2Bij6lqLvMfX79bveml%2BAiAw6PfUdtubhkYj7ePBiHs3%2BiWuYFAcBBrPz3c31fYLLSqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvt9klMFBSGTvY7wUKtwDWjMijRYf83VtnPSsx6aAiIqUyvFXewiLZlsyk8AybLzatK%2Fq402UL3e60cCOWrvbk2pcGGrtmPUNP7eRsDc3NV4qH8%2BOlNmMnM%2FTS21qr5QCef%2Fa3EZqqPS3B6i2GWGP8m3WPDzN13k3HXGuhF2Wga1L52Txv05wcWPSJQi4FgxR2Sg7hWYECs%2BEh5ecp84wxxP%2Bc4nH99IbuaaWhaiG7rMr1CW5suLxELMaOeXvrUQUmubzpZmEXtvp3hDW3Mtu1JdDiWVUmP%2F8juvZidDNal1U%2FhFV3tK8CgE200DsJzt5EIoWINCEVDhf8ruo1KWwbWc%2FTYzD1qBwbQzegoxQ3wSZFoWK3eAl07%2FercpY2d5wWkMj06WOsw47fqVlIFhWQxzIw%2Fwh7tgpIzT%2FNWvwkLenYk1%2FmGDwhupF9QSPP0ouFxxIdSpmWsrwHBTr4xJtuJ3CeTWIGmEwC%2BYliU1R338oWiQfTrSllXeEkyvA%2FPhWtashzYGnkAGOXXX0%2FcTdKqPd%2BJ74tixkg%2FcqbZ4jVsDzzoUkzCJh52y2Gb%2FAdlF9TQOBEceTGsPbBXa1Faru%2FZoUi8vKl%2FqGbNdJrDSVAf7sgwHGW5mJwKBinJZFDIxNnZCNPvCgj6mYn9AwvJP8zgY6pgFUQp0BAAE%2FwWOC7iQ0GLZ3UISZ5piGB5eWylO6auxe9TdsV%2BYoF3wmidXqioNcoNG1%2Fm%2BdF2kyY9LOUqSU8%2BnBPRf9EtK4qLr%2FXB2iAXPVRMnhOR769obqivaR6Nu4pJxy15Zv%2Bexj6cfS18DQzYhZr0u9Wj491NepeRwIlhIgNZKa6fQCPxrP2UBMK8pbkRrJhOFm%2FDpw5bVPHGX4h6aDwR1n%2B0Cy&X-Amz-Signature=99c3a789357daa8bef3d3f66e0a4dfdd77e2f4f973e3b89809bfc52c00b4d21b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3CAZJZR%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAy4ySIenxHui8lA4NbqLTVG7%2Bij6lqLvMfX79bveml%2BAiAw6PfUdtubhkYj7ePBiHs3%2BiWuYFAcBBrPz3c31fYLLSqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvt9klMFBSGTvY7wUKtwDWjMijRYf83VtnPSsx6aAiIqUyvFXewiLZlsyk8AybLzatK%2Fq402UL3e60cCOWrvbk2pcGGrtmPUNP7eRsDc3NV4qH8%2BOlNmMnM%2FTS21qr5QCef%2Fa3EZqqPS3B6i2GWGP8m3WPDzN13k3HXGuhF2Wga1L52Txv05wcWPSJQi4FgxR2Sg7hWYECs%2BEh5ecp84wxxP%2Bc4nH99IbuaaWhaiG7rMr1CW5suLxELMaOeXvrUQUmubzpZmEXtvp3hDW3Mtu1JdDiWVUmP%2F8juvZidDNal1U%2FhFV3tK8CgE200DsJzt5EIoWINCEVDhf8ruo1KWwbWc%2FTYzD1qBwbQzegoxQ3wSZFoWK3eAl07%2FercpY2d5wWkMj06WOsw47fqVlIFhWQxzIw%2Fwh7tgpIzT%2FNWvwkLenYk1%2FmGDwhupF9QSPP0ouFxxIdSpmWsrwHBTr4xJtuJ3CeTWIGmEwC%2BYliU1R338oWiQfTrSllXeEkyvA%2FPhWtashzYGnkAGOXXX0%2FcTdKqPd%2BJ74tixkg%2FcqbZ4jVsDzzoUkzCJh52y2Gb%2FAdlF9TQOBEceTGsPbBXa1Faru%2FZoUi8vKl%2FqGbNdJrDSVAf7sgwHGW5mJwKBinJZFDIxNnZCNPvCgj6mYn9AwvJP8zgY6pgFUQp0BAAE%2FwWOC7iQ0GLZ3UISZ5piGB5eWylO6auxe9TdsV%2BYoF3wmidXqioNcoNG1%2Fm%2BdF2kyY9LOUqSU8%2BnBPRf9EtK4qLr%2FXB2iAXPVRMnhOR769obqivaR6Nu4pJxy15Zv%2Bexj6cfS18DQzYhZr0u9Wj491NepeRwIlhIgNZKa6fQCPxrP2UBMK8pbkRrJhOFm%2FDpw5bVPHGX4h6aDwR1n%2B0Cy&X-Amz-Signature=630eca4cccf441c3df41591bce8ff12e8f2455d70061e18774f528453939326a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

