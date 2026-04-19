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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR7RG7NC%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCkx2%2B8KnSWO75zR%2FSkq1onrXKu4dd%2FMzR%2BJFO%2BPVg3EwIhAPz4NE1rPkQnmjXBsRZRCqCN3ktBnTBCgJx70pCpATTUKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwA10JeZqC0BtRpmAIq3AP8vjeX84Xyr8nlHaevgj0P%2FHzYe0FfDPcic2tFVN77Jmeab1K2HEgMm%2BlawSelyP74UDNFsCaroxw3hycCONQuZot2J0jQJ4Tlna%2BVdWqK6lV2yqpJNvbTDu1qe8wIY%2B7NSr%2BPTggKvOcehp92DsqTuC6Piv9b%2BpBKCnBIlhKchdiS0HpTM2uG40t8UW9S6%2Bqs18bbNpry9JyG21hkb4EUCRYFWDvpgtWHqC0ZlTyzF8gzoi93ds6NlQREmNHnYP6OeXwsuiQ9WIW3r3Q9NrKvO7uFlCXeXrk5wTwJXsVkI781wIdNcrdYIlBDwAZSa1JFxWDNGioFgftgDNLMboI57aPZ2OwjxGEddvhUQCMvTMfCztxObMmnoJ8SN7Cpg15woXfzIv8KtO5E5pIoiYI6jShRdpmAnde5esYYP03246FKZmLwI5cyKMCp%2FJS%2FIeXwhOPWmKIibQyloUIKqbK150eaOFhXmTyedUKiUMo%2BEVsZIfpfaHlW1uWy5PJ4vjKfkIWPaPUZJ4YXdTHhCrRFsHCw32J4Jqp2dC3MN%2BHi381vWY6kNfYok7lgStD4DHp8XTEnThAnKMmtHjICVY%2Bit9vHApmKSkfholix%2BKJXxgHNGT%2B5QWdAbznPFzCS3JDPBjqkAf9UDA%2BrVecYkHYzx4zVfwWrEUR7n061MV5aaDrVb8EmbH1Jn45guMxFrlbj6EnSc3kc1zs6jVRqSetvzcOEr8b4%2BcPA9RlUtIL28myXQyhBUvlAlXIO0Yag9Ykq8grKv%2BLWOi%2B9r76iuU1773nQ%2FsPbQfRnTJpFTraofz%2FqacrtQbijMGmU47n9OyZPaCoapyp98JRl3UskjXi8YgrnB9jk6Daw&X-Amz-Signature=52d303ed9f1b6bb76bb66a09d4400a5a2fbe76437444fa320a8e3a9affd9df8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR7RG7NC%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCkx2%2B8KnSWO75zR%2FSkq1onrXKu4dd%2FMzR%2BJFO%2BPVg3EwIhAPz4NE1rPkQnmjXBsRZRCqCN3ktBnTBCgJx70pCpATTUKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwA10JeZqC0BtRpmAIq3AP8vjeX84Xyr8nlHaevgj0P%2FHzYe0FfDPcic2tFVN77Jmeab1K2HEgMm%2BlawSelyP74UDNFsCaroxw3hycCONQuZot2J0jQJ4Tlna%2BVdWqK6lV2yqpJNvbTDu1qe8wIY%2B7NSr%2BPTggKvOcehp92DsqTuC6Piv9b%2BpBKCnBIlhKchdiS0HpTM2uG40t8UW9S6%2Bqs18bbNpry9JyG21hkb4EUCRYFWDvpgtWHqC0ZlTyzF8gzoi93ds6NlQREmNHnYP6OeXwsuiQ9WIW3r3Q9NrKvO7uFlCXeXrk5wTwJXsVkI781wIdNcrdYIlBDwAZSa1JFxWDNGioFgftgDNLMboI57aPZ2OwjxGEddvhUQCMvTMfCztxObMmnoJ8SN7Cpg15woXfzIv8KtO5E5pIoiYI6jShRdpmAnde5esYYP03246FKZmLwI5cyKMCp%2FJS%2FIeXwhOPWmKIibQyloUIKqbK150eaOFhXmTyedUKiUMo%2BEVsZIfpfaHlW1uWy5PJ4vjKfkIWPaPUZJ4YXdTHhCrRFsHCw32J4Jqp2dC3MN%2BHi381vWY6kNfYok7lgStD4DHp8XTEnThAnKMmtHjICVY%2Bit9vHApmKSkfholix%2BKJXxgHNGT%2B5QWdAbznPFzCS3JDPBjqkAf9UDA%2BrVecYkHYzx4zVfwWrEUR7n061MV5aaDrVb8EmbH1Jn45guMxFrlbj6EnSc3kc1zs6jVRqSetvzcOEr8b4%2BcPA9RlUtIL28myXQyhBUvlAlXIO0Yag9Ykq8grKv%2BLWOi%2B9r76iuU1773nQ%2FsPbQfRnTJpFTraofz%2FqacrtQbijMGmU47n9OyZPaCoapyp98JRl3UskjXi8YgrnB9jk6Daw&X-Amz-Signature=ecb226a9446bfacd2bd31eff41107c6cb375e6699c91ddc87fbf55e1163815b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

