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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIOO5SRJ%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAynjGCiGX6AO3RQrRvJknBYVas1GsZlHq4waaJi1tRLAiAgzDCQzEGavbJi5D8rqRm7uouD79R%2BtzrkZVxTR3i1Nyr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMSbR%2BZ6bHBqnabBaeKtwDViq7hxTHnt0ICX4r8ept8u1%2FjLslUteEaRQ%2BNpzurh1cDvwR3d6sma1CNYxJ3xEB2RP0%2FxETjSNsstGTcpv%2Bpcfas8oa07DpSvENMy3DhFmcxA03S1fRc8bJbFvRpnTyXsBS6Y9h9fT%2BETJ6JvKAL%2BnjivoaYD2WWbFSSE%2F7sq5qN%2BZOXyvR8fFJrTrY2%2BN7wHw1HlFN%2B1xek3rOF4mwWDd7877s46ISYPGkfruCU06xke2F9rQpaXfBnnzpJOzIs4y26P%2Fmzc%2BtjvcZYqvNU1HDoDgd2aE4rp%2B9IZbcU7ORWY6FbCyXDvhvoo3aPhSydJBsZQVF5l3vcAJEPAOWgGcyKlDi%2FX1AXlBqo1kfMX%2FwHZUeFEF%2BVH3d1ZPPWoyY%2Ff70z58cJ1YvErIIYZMHd%2FXbnMSLjkLRR95sUkMfZb2Mf76%2BsHx3AAB%2Fr1eac1e4ahRNWdH3rDdBwEVJbAdNUL%2BnUWRe61doyknRz5kATy2a5nTusX%2FKvfuy9byLExKRZrMv2Y7E3NRZox0aWnMxhLJFZo%2BYL%2Begwe49sTWR9Z2%2FiucbnDu72%2Bukj8kLSnVGwpvEland8ZcARYoOqRnrciaEKdIMVxlrsF5hd32MYQ39bFHjPaoBw8WiSYswqcDDzQY6pgGnSU6iA%2BAsps9rixFMUk8X4OaZxIOMZ1d817wmM6NtWZYYmi9Te1C0XA3I%2F%2FU%2FDHc9yMsdO0PfqG6Lb1plE%2FLsrp052U%2FDVV8vul5TdQb2EoCWynDInLYD6tW5PLuHolIq793yEDBcd0qXIXCimZYSPG9S5o9xjoTgye33LA9zAbOOF2BX61j8uxxwTnshtqrbUxuEqzy8QxF2Z2xPBFc8gQnqC3sp&X-Amz-Signature=fc34914899017a26dd64025f5fe1d2dad5001a951d8a48cf75ae1fdc3710824f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIOO5SRJ%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAynjGCiGX6AO3RQrRvJknBYVas1GsZlHq4waaJi1tRLAiAgzDCQzEGavbJi5D8rqRm7uouD79R%2BtzrkZVxTR3i1Nyr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMSbR%2BZ6bHBqnabBaeKtwDViq7hxTHnt0ICX4r8ept8u1%2FjLslUteEaRQ%2BNpzurh1cDvwR3d6sma1CNYxJ3xEB2RP0%2FxETjSNsstGTcpv%2Bpcfas8oa07DpSvENMy3DhFmcxA03S1fRc8bJbFvRpnTyXsBS6Y9h9fT%2BETJ6JvKAL%2BnjivoaYD2WWbFSSE%2F7sq5qN%2BZOXyvR8fFJrTrY2%2BN7wHw1HlFN%2B1xek3rOF4mwWDd7877s46ISYPGkfruCU06xke2F9rQpaXfBnnzpJOzIs4y26P%2Fmzc%2BtjvcZYqvNU1HDoDgd2aE4rp%2B9IZbcU7ORWY6FbCyXDvhvoo3aPhSydJBsZQVF5l3vcAJEPAOWgGcyKlDi%2FX1AXlBqo1kfMX%2FwHZUeFEF%2BVH3d1ZPPWoyY%2Ff70z58cJ1YvErIIYZMHd%2FXbnMSLjkLRR95sUkMfZb2Mf76%2BsHx3AAB%2Fr1eac1e4ahRNWdH3rDdBwEVJbAdNUL%2BnUWRe61doyknRz5kATy2a5nTusX%2FKvfuy9byLExKRZrMv2Y7E3NRZox0aWnMxhLJFZo%2BYL%2Begwe49sTWR9Z2%2FiucbnDu72%2Bukj8kLSnVGwpvEland8ZcARYoOqRnrciaEKdIMVxlrsF5hd32MYQ39bFHjPaoBw8WiSYswqcDDzQY6pgGnSU6iA%2BAsps9rixFMUk8X4OaZxIOMZ1d817wmM6NtWZYYmi9Te1C0XA3I%2F%2FU%2FDHc9yMsdO0PfqG6Lb1plE%2FLsrp052U%2FDVV8vul5TdQb2EoCWynDInLYD6tW5PLuHolIq793yEDBcd0qXIXCimZYSPG9S5o9xjoTgye33LA9zAbOOF2BX61j8uxxwTnshtqrbUxuEqzy8QxF2Z2xPBFc8gQnqC3sp&X-Amz-Signature=4c51a4d7248a4074418d67199638ed2e363f03bc27e374982260af204c1f01e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

