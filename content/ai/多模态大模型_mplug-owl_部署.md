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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IS3QXSN%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID12fsVdJPhQzoJmu7np%2FaxRqBRgyBwtP8NfWwAsidaWAiA3hArAIdztsCGRBOTz2MpORwG3MmP4j4AtDMSzZ5Ec5yr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMZneZHRHUHC7G7whQKtwDwAx410iWLAeqCtojHIAG%2FTrUiwPbYgQWx%2BRux0fOgdA6JaI1ZlUefl2RvSEHrdPzBWcMTV1pwZyZQWefuLgleLcFCyspb2YwpXGd878D4AKLTeazNpZ4pYYSKxLslicj3j%2BKo2YXPR5e1TyibfxFRemfY2i2BhEbh%2BUxrIQUAUd6ti4i5ncqF1IMtDDtv7fN3yuDUxlekvst8epZ2N%2B36SXfaNgdbeP%2B%2BBsXzBjD8fuLpcgwV%2BderuC2vD4tB6SBSCwEY8DIy17AgidvqFDG8LZRl%2FkxjJ1o3BijtIG9k496gmvnF1eT7nVnTFJumj29JaLU6dNxKOVmbbnLiCPozG3IK6uNvi3V0Jx0g0ywpjcJ5SsgMGSsqrUsRljDuEcgVTJqtswZju6KIVnTR48rV2ONH1S%2F3AkKSW0t3bB5D5MasxIPnfZAoJBay1kaWuTAY%2BYlfKLOsaWHxoao8m3ai8g5aAzIv%2FEoahHF7%2FaqcHR17irq5EapaTYKdIeXv2xky%2Fq%2Fw32h%2FQA%2FTiIVUlnntHW3XQRFYS%2BjRauNtkJpObRZyHJGUaiB7%2FFOl6EaM6pYcREtlnvgTfubS1hCxIyvS7hJXSRXPHf%2FSuSqW%2FqRcv%2F79BOV%2Fq7GB7iG6A8worHxzgY6pgGcLI8pNxh%2BsPPzgH3gbFWUeZZ0oVPi4iJKPv9wHEmkTC39dqzupcMw8XE0CcXWDt3wdZRnjhlt8qGZY%2B9NvGvXFX44iU%2FMD%2FT6Wm577vqdCjBoA5ExzjGH08dmASqpPNYFQvWxzslZEd49xPFgazYf56Ly1HuvckNCacBYUZ7wq1jzNg7%2FDNZWWpENWEaRMtQv2dkEJL1DPrlTThGcrm1w2V%2FWVnXy&X-Amz-Signature=6edf3ae9db8f09bbde200d88c55d5131a74987d177eca5bd956ec5c50b2467ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IS3QXSN%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID12fsVdJPhQzoJmu7np%2FaxRqBRgyBwtP8NfWwAsidaWAiA3hArAIdztsCGRBOTz2MpORwG3MmP4j4AtDMSzZ5Ec5yr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMZneZHRHUHC7G7whQKtwDwAx410iWLAeqCtojHIAG%2FTrUiwPbYgQWx%2BRux0fOgdA6JaI1ZlUefl2RvSEHrdPzBWcMTV1pwZyZQWefuLgleLcFCyspb2YwpXGd878D4AKLTeazNpZ4pYYSKxLslicj3j%2BKo2YXPR5e1TyibfxFRemfY2i2BhEbh%2BUxrIQUAUd6ti4i5ncqF1IMtDDtv7fN3yuDUxlekvst8epZ2N%2B36SXfaNgdbeP%2B%2BBsXzBjD8fuLpcgwV%2BderuC2vD4tB6SBSCwEY8DIy17AgidvqFDG8LZRl%2FkxjJ1o3BijtIG9k496gmvnF1eT7nVnTFJumj29JaLU6dNxKOVmbbnLiCPozG3IK6uNvi3V0Jx0g0ywpjcJ5SsgMGSsqrUsRljDuEcgVTJqtswZju6KIVnTR48rV2ONH1S%2F3AkKSW0t3bB5D5MasxIPnfZAoJBay1kaWuTAY%2BYlfKLOsaWHxoao8m3ai8g5aAzIv%2FEoahHF7%2FaqcHR17irq5EapaTYKdIeXv2xky%2Fq%2Fw32h%2FQA%2FTiIVUlnntHW3XQRFYS%2BjRauNtkJpObRZyHJGUaiB7%2FFOl6EaM6pYcREtlnvgTfubS1hCxIyvS7hJXSRXPHf%2FSuSqW%2FqRcv%2F79BOV%2Fq7GB7iG6A8worHxzgY6pgGcLI8pNxh%2BsPPzgH3gbFWUeZZ0oVPi4iJKPv9wHEmkTC39dqzupcMw8XE0CcXWDt3wdZRnjhlt8qGZY%2B9NvGvXFX44iU%2FMD%2FT6Wm577vqdCjBoA5ExzjGH08dmASqpPNYFQvWxzslZEd49xPFgazYf56Ly1HuvckNCacBYUZ7wq1jzNg7%2FDNZWWpENWEaRMtQv2dkEJL1DPrlTThGcrm1w2V%2FWVnXy&X-Amz-Signature=bc45c3b109eb413ba709c58ee3cf401f3e9057d843911fe26cc2ec4327932624&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

