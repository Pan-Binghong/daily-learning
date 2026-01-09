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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEJOARF%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE7FFKCMz2OdTBVmL3TqJ8CPARN5U%2FzWR6iZOrefTTrYAiEA4C4Yr9oqvr4gYtgLXHnKdQk%2FiqfbaSLiopTXESwpScEqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPLRDaUtBlj4SiosLSrcA9Eil455mAT3qFRs0MomWFRDvKWrq59TIUnrDOIQHNmaDFQ2sSDmbqGJqhaft6W9uOyOomL8ZDvQsoqMp21rJtynR7s%2Bc6tntKov%2B41CLQqFSSr5GibLafnKEKaaX0Dno70dmKA1QN9mWGhsCQInOqYrkiSL21h%2BFyDwGHpwKXTXmCn7pls%2FMJl8Sy81AbZde%2Bfao4MDJVEE7iO5tCm3yQoaYR7IFvP7qiMWmMDey5KB%2FDnRhTxNWV3x1GHGiPcgNuGJLOpYwIWFjNJ%2BuiG2otHP08hjEQJrD07kZp1QqHSYD6fCDTpOW4DlwKaK0FrLnKGMEuSO3CMXBmxliHCUiL%2Fu86OoNhHCUPE1HZ7ctlpcRoNmuE6xvMkUOgl1ydi3e6aNloJuaV3lIKL0kniIyVenhK66iH2eSphxw6OddPvhoTsy%2BOymjaRdj%2Bhqg%2BEMCMePGQY%2Fmccz0hRXZlKVO0cbZ7l%2B%2BZCgE9NnPbgGiUzzCmtmZpYXrg7gyOcrYfCuL1bJf2Kcb9vPU5oa3zW7q3ifSKAMc6SarAJzHfe3JM2MlRWWn%2BWG1%2BUBBOw1jY0rzgbewkOj0pl6vv0Qh82D5gUC6%2FFC7kVIkgVBdJbnlUMR44oS9F52JGCHBi14MJXFgcsGOqUBwnSY4XcAxjJQoT9eBFlh%2Buq6ABz%2B6gmtkNugYto%2BLPa9q2WhXEuAy8tsVyUBnH7TrL2ZNUoGTJD9fSN%2B5gaiOAL7lO2vnB29rGR5heJda1aMkCaAqjWINuYKtm52SXOruXrtl0PfIvuFZSS3upDl2J0cyEK7lTRxdIWcU4kgXM2JUE%2FYTxWdwvvkwaqPAqUkZU3iKue5W0ZSnqJgMiPAbw1QpYLa&X-Amz-Signature=2a17ac47dea8fca41f46b6c18b0c933fcb87e6cc551d0f4cad83b66ca3a45f4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEEJOARF%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE7FFKCMz2OdTBVmL3TqJ8CPARN5U%2FzWR6iZOrefTTrYAiEA4C4Yr9oqvr4gYtgLXHnKdQk%2FiqfbaSLiopTXESwpScEqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPLRDaUtBlj4SiosLSrcA9Eil455mAT3qFRs0MomWFRDvKWrq59TIUnrDOIQHNmaDFQ2sSDmbqGJqhaft6W9uOyOomL8ZDvQsoqMp21rJtynR7s%2Bc6tntKov%2B41CLQqFSSr5GibLafnKEKaaX0Dno70dmKA1QN9mWGhsCQInOqYrkiSL21h%2BFyDwGHpwKXTXmCn7pls%2FMJl8Sy81AbZde%2Bfao4MDJVEE7iO5tCm3yQoaYR7IFvP7qiMWmMDey5KB%2FDnRhTxNWV3x1GHGiPcgNuGJLOpYwIWFjNJ%2BuiG2otHP08hjEQJrD07kZp1QqHSYD6fCDTpOW4DlwKaK0FrLnKGMEuSO3CMXBmxliHCUiL%2Fu86OoNhHCUPE1HZ7ctlpcRoNmuE6xvMkUOgl1ydi3e6aNloJuaV3lIKL0kniIyVenhK66iH2eSphxw6OddPvhoTsy%2BOymjaRdj%2Bhqg%2BEMCMePGQY%2Fmccz0hRXZlKVO0cbZ7l%2B%2BZCgE9NnPbgGiUzzCmtmZpYXrg7gyOcrYfCuL1bJf2Kcb9vPU5oa3zW7q3ifSKAMc6SarAJzHfe3JM2MlRWWn%2BWG1%2BUBBOw1jY0rzgbewkOj0pl6vv0Qh82D5gUC6%2FFC7kVIkgVBdJbnlUMR44oS9F52JGCHBi14MJXFgcsGOqUBwnSY4XcAxjJQoT9eBFlh%2Buq6ABz%2B6gmtkNugYto%2BLPa9q2WhXEuAy8tsVyUBnH7TrL2ZNUoGTJD9fSN%2B5gaiOAL7lO2vnB29rGR5heJda1aMkCaAqjWINuYKtm52SXOruXrtl0PfIvuFZSS3upDl2J0cyEK7lTRxdIWcU4kgXM2JUE%2FYTxWdwvvkwaqPAqUkZU3iKue5W0ZSnqJgMiPAbw1QpYLa&X-Amz-Signature=dedb44cfa8550a1d1c5f75aea58430ddfc56e6b800d75319687ad70adc0678a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

