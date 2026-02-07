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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAM3N7HL%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAk8UILZIDvEiN3bDVct1bbdeg5oaqP0QINE637hhRopAiB3aq1nyevicaUZwiEGslGIne7bc7oY8dJ43d4QpAJluir%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMKwqHtEWZm1uo%2BRlTKtwDEzdXs3NTNCAdz%2F0FMiQJYLBECLlca2kwmC%2Fb7w5og%2Bw3FHTShO2wtRzRoDMq%2BqfmtTPTqz2nxUOa7kiLvSGXPdPO1Kn3hoWJQgDceLgY8isexMMUCBinvYThvzGGjhP8kQTqdf61vxDEY2qKqmq3rcnkgYJscDkE9PPnIiZZs%2F7FcIBVyKaBNiABs03eGsj2ePA1lIUz%2FnAckdDnl9LW6YC5m9BMvA2vqW71eF7fSUBh5wWwnonfxOYEFFkRaWUbTj%2Fbf7RY2PosDOTJ9rAWdYXJNbrx3n4yzxqzm8rN4ZUM5VCySbQm3sZ5VAGd9BhZc50xuMjHvCJ9adS1yoiminb2QjzFz7RjL7C1OcFwIrRYhGiXGyYqhtqTRSAWfwJthE5pglSjT7IOqhjfBhHFxG6nwLWrXO7b6XaeSEfMeM3cd72HjUb6wkt%2FAZK4cRLfg52RHfXYx68%2BZT17v8jwbo4uecrsjL%2Bn4Sz%2BOz%2Bvj4VoMSygAjr8LlqOmuOre5LBps9wVCX58kkENl7YyDLLSfrf3XPLElQP3KEuKZ7keFgjy21Cn3TINtIeVqjmOYxBW9nKMUfQKdvu11VMfT5l7Ljse51mdR4RzOJW%2FOQCbq4X4WG4d2AJTK7XHEMw6sOazAY6pgG5XgHaXbGjugBjpr6SEGvFIvjnaYQpC3cirVyVnjHalCA%2BuV7%2FOqfyQRMbBf6gOzRRtogMoNwQgGTwuJ%2BWIs8m6KPyP2rxMNWqhG0iqNEQA8gQBqSc6pwO1yu5VKRpH5AjuXTTQpTOt6Rtd%2FuwbwaQEZ%2FHQVbzb8LGFHBDqzyk9w0BYThCK6IPhRwMpVKoatDQwaBtzXDzoZuwSY98gm82bh8clatE&X-Amz-Signature=3598b01c3722ed90fd1ead0535027ccf3739c03d00e7439c996330c768511922&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAM3N7HL%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAk8UILZIDvEiN3bDVct1bbdeg5oaqP0QINE637hhRopAiB3aq1nyevicaUZwiEGslGIne7bc7oY8dJ43d4QpAJluir%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMKwqHtEWZm1uo%2BRlTKtwDEzdXs3NTNCAdz%2F0FMiQJYLBECLlca2kwmC%2Fb7w5og%2Bw3FHTShO2wtRzRoDMq%2BqfmtTPTqz2nxUOa7kiLvSGXPdPO1Kn3hoWJQgDceLgY8isexMMUCBinvYThvzGGjhP8kQTqdf61vxDEY2qKqmq3rcnkgYJscDkE9PPnIiZZs%2F7FcIBVyKaBNiABs03eGsj2ePA1lIUz%2FnAckdDnl9LW6YC5m9BMvA2vqW71eF7fSUBh5wWwnonfxOYEFFkRaWUbTj%2Fbf7RY2PosDOTJ9rAWdYXJNbrx3n4yzxqzm8rN4ZUM5VCySbQm3sZ5VAGd9BhZc50xuMjHvCJ9adS1yoiminb2QjzFz7RjL7C1OcFwIrRYhGiXGyYqhtqTRSAWfwJthE5pglSjT7IOqhjfBhHFxG6nwLWrXO7b6XaeSEfMeM3cd72HjUb6wkt%2FAZK4cRLfg52RHfXYx68%2BZT17v8jwbo4uecrsjL%2Bn4Sz%2BOz%2Bvj4VoMSygAjr8LlqOmuOre5LBps9wVCX58kkENl7YyDLLSfrf3XPLElQP3KEuKZ7keFgjy21Cn3TINtIeVqjmOYxBW9nKMUfQKdvu11VMfT5l7Ljse51mdR4RzOJW%2FOQCbq4X4WG4d2AJTK7XHEMw6sOazAY6pgG5XgHaXbGjugBjpr6SEGvFIvjnaYQpC3cirVyVnjHalCA%2BuV7%2FOqfyQRMbBf6gOzRRtogMoNwQgGTwuJ%2BWIs8m6KPyP2rxMNWqhG0iqNEQA8gQBqSc6pwO1yu5VKRpH5AjuXTTQpTOt6Rtd%2FuwbwaQEZ%2FHQVbzb8LGFHBDqzyk9w0BYThCK6IPhRwMpVKoatDQwaBtzXDzoZuwSY98gm82bh8clatE&X-Amz-Signature=c8ab9d333a1b6d0b16ca5026255ae0b4d5df5f5156b6b44abc2abf8d688a6418&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

