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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LAQVQNW%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJGMEQCID%2FQRBVytF1EWDekXLr6zhD0T5cAKm4UEXbKjEqIYbvCAiBRCxKVyhFbY%2B%2FQcVz%2BIe7XUTwoTiU3LGiPEDtQVeiekCqIBAjs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsNeGKydoWfSBtIQJKtwDMTq1tZleS3TGqgVQsBgtN6s4bbDXgS%2FVZ6ACjfUud5S3hIH9lg4iwlR2P4ifPFveemrjwVuPvhJxKs1YEyXC2k%2BXF18VpdJBgkIStv00bIO5O5sasvEWZvHLVyIfmEHe%2Fff8HJ5cZbkpjVaJDQNoy1xwMipdcgNb1uBTo2Rlm%2FExTTI60%2FUKC95rGkjM%2BJdgSUi%2FosDXTtTDzRQgXBt4Sl6y%2BTELr7XxMTZJmpHhsmOia5yZLj3MdPXZ7a8UpczBnx2q9SphH6NsBjNtybw2%2BgMAw8CBxLURLhCiVTj4J44fiABBeB%2FnDX4OHgFEpTAmsRbFxdqu2hjdyZ5BWvnQgqgCVQVK%2FWUk6Y5FKR7NaoX2dW5j%2BLrUN%2FIdj%2BUfYQg4Yz6rSwNBUtKBS087ac9RO%2FQ%2Bx0a%2FAvSKfgcZ3hS9dI8q5pSLT7qqrSP688NJvrbuZsxLRmUFlWOHOJbxG03pX6zw%2BMCQ%2Bxjxv4zIS9J3kmH2P6ztonNu8j%2F7Xqh8TVjA41H%2BdhTjgtlb2yTZFydTGgnors1BcMkym02IaRluZh6gqlcNh9QN5O4bn%2F3R6Y5pPCmZp%2BFoW2steEOjx5An%2FSBc8rdNu5NIn86nsmUTKz3hBv3oQ1yiqkVXVaIwve7FzwY6pgGLlmPpRylTA9%2FysC1eiZ6UyCPGjIQtMDR5osTxliFxB%2FfdvVKdyIMN1XoJlGYRkLcWvGuHfyowUPAvZlG7uu%2FgwXxTkemDn7MNNieMwkERudo5PNs6mwR1dkc0cazy5d61MKP0Tk2huM8u5mDfpbcvNObN%2Bpgag9F%2FXLgLyQPw5eu1AVTh11r7M%2F5paRhZuxvil7NcQ%2FUjOs1TDaFmeBiwGDsBNd6H&X-Amz-Signature=2ff715fc6205998519e5e09cba1111c805f879f0c863f7ca07fd74d07d0dd844&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LAQVQNW%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJGMEQCID%2FQRBVytF1EWDekXLr6zhD0T5cAKm4UEXbKjEqIYbvCAiBRCxKVyhFbY%2B%2FQcVz%2BIe7XUTwoTiU3LGiPEDtQVeiekCqIBAjs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsNeGKydoWfSBtIQJKtwDMTq1tZleS3TGqgVQsBgtN6s4bbDXgS%2FVZ6ACjfUud5S3hIH9lg4iwlR2P4ifPFveemrjwVuPvhJxKs1YEyXC2k%2BXF18VpdJBgkIStv00bIO5O5sasvEWZvHLVyIfmEHe%2Fff8HJ5cZbkpjVaJDQNoy1xwMipdcgNb1uBTo2Rlm%2FExTTI60%2FUKC95rGkjM%2BJdgSUi%2FosDXTtTDzRQgXBt4Sl6y%2BTELr7XxMTZJmpHhsmOia5yZLj3MdPXZ7a8UpczBnx2q9SphH6NsBjNtybw2%2BgMAw8CBxLURLhCiVTj4J44fiABBeB%2FnDX4OHgFEpTAmsRbFxdqu2hjdyZ5BWvnQgqgCVQVK%2FWUk6Y5FKR7NaoX2dW5j%2BLrUN%2FIdj%2BUfYQg4Yz6rSwNBUtKBS087ac9RO%2FQ%2Bx0a%2FAvSKfgcZ3hS9dI8q5pSLT7qqrSP688NJvrbuZsxLRmUFlWOHOJbxG03pX6zw%2BMCQ%2Bxjxv4zIS9J3kmH2P6ztonNu8j%2F7Xqh8TVjA41H%2BdhTjgtlb2yTZFydTGgnors1BcMkym02IaRluZh6gqlcNh9QN5O4bn%2F3R6Y5pPCmZp%2BFoW2steEOjx5An%2FSBc8rdNu5NIn86nsmUTKz3hBv3oQ1yiqkVXVaIwve7FzwY6pgGLlmPpRylTA9%2FysC1eiZ6UyCPGjIQtMDR5osTxliFxB%2FfdvVKdyIMN1XoJlGYRkLcWvGuHfyowUPAvZlG7uu%2FgwXxTkemDn7MNNieMwkERudo5PNs6mwR1dkc0cazy5d61MKP0Tk2huM8u5mDfpbcvNObN%2Bpgag9F%2FXLgLyQPw5eu1AVTh11r7M%2F5paRhZuxvil7NcQ%2FUjOs1TDaFmeBiwGDsBNd6H&X-Amz-Signature=9d106f8d8c7f6cb5956a21d3ca779454b45c89998ecc4a3036a7b54a082fb629&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

