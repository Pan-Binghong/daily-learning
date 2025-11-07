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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLCQYVCS%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCoIw%2Fd9UvDx3Ir%2BFiZ6WhWtdXITZhrkLd9HkrAHgMhuAIgLW6Qej2YTvPQQsLfRkHp0aiiyvDKz%2Fj%2B5CHGVhSt6WwqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBp7SvdMk27nXHCRqircA9CVnh2IQFY%2BrVz09ru1yEq33%2B0MSiJNwHy6%2B7cBa8%2FrbYp2cSa6P7aN6fZ2d9VtqlPfmel6J%2B0oKYwM8Et2YbVOi5gBpuzCcSFYDIeD72x0Bxe0GSPNR3xFN0LtFp6TkgoEdRT4e0Zn%2FH6%2FIgCDEj800NDrlC%2BbkOqXzwJ8k0RWxXvQiC%2BZ2jZ5c9NXxGb8hVcS6dJlcnAN5jUqR%2Bqx4ndztZWuMzL2d5fo7MS8IrWdTiyHlXEsXoWBMqLz4LcHcfZUMDMNJrK%2BUUNOpmkR54sJBRaqSW91nzd1wPMZodgDLFFUs6CLFKtJdK6NPX4C9vSNySPFsKHBc3FPiQHdz84SbQ2G0XOerCrNSoZNu3PUZRmGMqDdjHHEQXGIe1WqDgxEnCm89svDqINcAD5SaN5Gw%2FRAD4baEwDp%2FwoQe6ZthgHBd1cddQTxNRLjNSGcNxPfmxIUlQDvH61d2UCivlYsjETVmRNSQCdR9Y6rDmAUsmUmBiOKFTULQNSCUA6t7mUJWqNV0lOL%2BjtHyAR39BGehvS035GVEq8S5Iq41p0XQLgW82BezTSeigc2vc5psWIx2vgqKukdEaZ73lpdQ6AbAkubCi57b6Ya9Xp7KDIYHD9TI3r7g4YrqXznMJ62tcgGOqUBJoVpexJ9R%2FnmMN64UwT68mUoHBk3MV2QY6Tzyk0sTVq6p2rqRgZ%2FolXzO0y%2Fkrm7pNKYln32ztowr5HzUQzR60pTZ6CJ%2BQdfvHYqRG7W2I8X6EJAMSQyuqMFItwigzMSgswlR4AlqGINOpJ6ko%2BDiXsWWkj2xyPnJ1JuXdEHBsArTrNN3ZCPRiYYPi%2BWwB7W8UmDhbJrtRfbHCs9bYcR5nQt4kmy&X-Amz-Signature=4bf7b186d2c4a515eb54916ca9c1183ba06fe2c0dd5a9eac8c738258e72f0da6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLCQYVCS%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCoIw%2Fd9UvDx3Ir%2BFiZ6WhWtdXITZhrkLd9HkrAHgMhuAIgLW6Qej2YTvPQQsLfRkHp0aiiyvDKz%2Fj%2B5CHGVhSt6WwqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBp7SvdMk27nXHCRqircA9CVnh2IQFY%2BrVz09ru1yEq33%2B0MSiJNwHy6%2B7cBa8%2FrbYp2cSa6P7aN6fZ2d9VtqlPfmel6J%2B0oKYwM8Et2YbVOi5gBpuzCcSFYDIeD72x0Bxe0GSPNR3xFN0LtFp6TkgoEdRT4e0Zn%2FH6%2FIgCDEj800NDrlC%2BbkOqXzwJ8k0RWxXvQiC%2BZ2jZ5c9NXxGb8hVcS6dJlcnAN5jUqR%2Bqx4ndztZWuMzL2d5fo7MS8IrWdTiyHlXEsXoWBMqLz4LcHcfZUMDMNJrK%2BUUNOpmkR54sJBRaqSW91nzd1wPMZodgDLFFUs6CLFKtJdK6NPX4C9vSNySPFsKHBc3FPiQHdz84SbQ2G0XOerCrNSoZNu3PUZRmGMqDdjHHEQXGIe1WqDgxEnCm89svDqINcAD5SaN5Gw%2FRAD4baEwDp%2FwoQe6ZthgHBd1cddQTxNRLjNSGcNxPfmxIUlQDvH61d2UCivlYsjETVmRNSQCdR9Y6rDmAUsmUmBiOKFTULQNSCUA6t7mUJWqNV0lOL%2BjtHyAR39BGehvS035GVEq8S5Iq41p0XQLgW82BezTSeigc2vc5psWIx2vgqKukdEaZ73lpdQ6AbAkubCi57b6Ya9Xp7KDIYHD9TI3r7g4YrqXznMJ62tcgGOqUBJoVpexJ9R%2FnmMN64UwT68mUoHBk3MV2QY6Tzyk0sTVq6p2rqRgZ%2FolXzO0y%2Fkrm7pNKYln32ztowr5HzUQzR60pTZ6CJ%2BQdfvHYqRG7W2I8X6EJAMSQyuqMFItwigzMSgswlR4AlqGINOpJ6ko%2BDiXsWWkj2xyPnJ1JuXdEHBsArTrNN3ZCPRiYYPi%2BWwB7W8UmDhbJrtRfbHCs9bYcR5nQt4kmy&X-Amz-Signature=b21b5964883a79e6066ffceb717a32a9391cbed9859aa0a00092ec8668e92845&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

