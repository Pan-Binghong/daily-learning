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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RJXVORB%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA7Kx0hEPDgcoy9Zc67WRKo8EaZ06Bondk0Ns24KtXO2AiEAkUSmxewtblNTsNFHYU5YtWnBvM2XoUNdLH8IHdqm35gqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJxdHqqKR%2FczDr5xDyrcA9taZ7DTpDEzyIWKSMSq24ZFMz%2FznldfY%2BZnjC66v1ddhuivKDa46uSSL4uRAuXOfyx4X7eFu5YaCLGkeXJdhg4PeOsJpbkuTtMxgbJJKX8TWi6KXQb7%2FG0XVEG7pyAX0Zrnz2TUQUQBdyRxB1fC%2FpnAiIJDCdCuxjO%2Fo9ew4rANRZJGq57LLVneTktZLjJlhPCE4j3Gq7Iqi1%2FMJZPGh0HFkx6ZuhKmJlOHYBEdHyDyLn0dLklVtS85cfyjB6tF3laYia4GksVYseKJ2p8ihDVKbMCcCPS8BcmQIqqhk0FT2xFvpsqEtkHn0g9TKl89Y39cXuJeXr75R4hrahHIxi7TG4LyKykJPwmTW8eoI7FxbaVViA%2BQyJGCgixoAaaR7DWU3t%2Bciwx5cfIyqK%2BDXzJPhKiDaGijIsRT8F5rX0xhK8kAXWXSGNs%2Bt0wsm1n%2ByTWQZhfT3IzqQ74H0ckgFYIyVy8POK2IKo6YduL6XFD%2BJBwL1MgCDNlrztZpKueb%2ByADy4nXAidEbDA7zfRjlUk6Hz9JBKnVRlQeDZcYh04gFb0%2B4PdBfNbC0GfBO4IvaHq%2FYpjNMAcIFVz8s6BrNFW%2BIHyI63CT2kj5cFfLsKL1hbRm8BtbLJGRP%2FpCMK3JjcoGOqUBHuekNJ%2FvTTiLd2aHpTBEHdGcgvLuYtpo5z7kuXbPCZMVU1Y7q%2FXOXNW0cLfZXi7D1GcPHgpKFZfLFXtIOuJFMLwBZjQf7xBVa02ULr4mg%2B749%2BfnNoCdXcWb1wcB%2BEKAaTUUzZGDY6B6r7C7GZkvC8WCynUg%2BsqjLuBeQmbP4RnQUH9T%2FbB3w3V0pbOzk%2FTe5H9p81U8cX0dupvWE0t2xh6XiCKE&X-Amz-Signature=a09560d457530e95a84072e5f9ebf5a30a5b0a6e0104f5e9623f6dd74d205f3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RJXVORB%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA7Kx0hEPDgcoy9Zc67WRKo8EaZ06Bondk0Ns24KtXO2AiEAkUSmxewtblNTsNFHYU5YtWnBvM2XoUNdLH8IHdqm35gqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJxdHqqKR%2FczDr5xDyrcA9taZ7DTpDEzyIWKSMSq24ZFMz%2FznldfY%2BZnjC66v1ddhuivKDa46uSSL4uRAuXOfyx4X7eFu5YaCLGkeXJdhg4PeOsJpbkuTtMxgbJJKX8TWi6KXQb7%2FG0XVEG7pyAX0Zrnz2TUQUQBdyRxB1fC%2FpnAiIJDCdCuxjO%2Fo9ew4rANRZJGq57LLVneTktZLjJlhPCE4j3Gq7Iqi1%2FMJZPGh0HFkx6ZuhKmJlOHYBEdHyDyLn0dLklVtS85cfyjB6tF3laYia4GksVYseKJ2p8ihDVKbMCcCPS8BcmQIqqhk0FT2xFvpsqEtkHn0g9TKl89Y39cXuJeXr75R4hrahHIxi7TG4LyKykJPwmTW8eoI7FxbaVViA%2BQyJGCgixoAaaR7DWU3t%2Bciwx5cfIyqK%2BDXzJPhKiDaGijIsRT8F5rX0xhK8kAXWXSGNs%2Bt0wsm1n%2ByTWQZhfT3IzqQ74H0ckgFYIyVy8POK2IKo6YduL6XFD%2BJBwL1MgCDNlrztZpKueb%2ByADy4nXAidEbDA7zfRjlUk6Hz9JBKnVRlQeDZcYh04gFb0%2B4PdBfNbC0GfBO4IvaHq%2FYpjNMAcIFVz8s6BrNFW%2BIHyI63CT2kj5cFfLsKL1hbRm8BtbLJGRP%2FpCMK3JjcoGOqUBHuekNJ%2FvTTiLd2aHpTBEHdGcgvLuYtpo5z7kuXbPCZMVU1Y7q%2FXOXNW0cLfZXi7D1GcPHgpKFZfLFXtIOuJFMLwBZjQf7xBVa02ULr4mg%2B749%2BfnNoCdXcWb1wcB%2BEKAaTUUzZGDY6B6r7C7GZkvC8WCynUg%2BsqjLuBeQmbP4RnQUH9T%2FbB3w3V0pbOzk%2FTe5H9p81U8cX0dupvWE0t2xh6XiCKE&X-Amz-Signature=a2af139b8cefbc9037ca2c8182dee964285f4d2d3a917b12ae8fe50270d14bdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

