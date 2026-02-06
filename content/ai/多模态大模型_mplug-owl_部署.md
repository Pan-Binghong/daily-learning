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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WYL4OBS%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDZbUQpKBxKFD0b3C4hbpAcpYNMrRB9rqyzNHLUHRRI%2BwIhAKxgz8%2BsMEMBkOzOWy%2BH6Zj5HOZNkMR47dUC9ILgl44FKv8DCDwQABoMNjM3NDIzMTgzODA1IgwZboWpNI9fmJNE7F8q3ANTnLVVLGj7SgRbdHGRT%2BQs02%2BOcxC2690VTXOyXSiv8Qe5YF7eksZ%2B23Q3B61WVG8IMG3PYBh1ybgpYV9wrT1mcNgtw0QGZYKPSAeM6DQGbqVGjl%2BlQ6nbFyW%2Bk9p2mQNEGEKmapZnyaBkEqGOKvt8zwqe0aHsoOMD718%2FVunZPLUnZSS14wvs8rtNbZQ8uzbWvd4bdT%2BqGgSNJtaKDzoxyXjOCWTcMXpJA1ixlqybA8jCH2d%2FRoJwDWOt0BSAbNbDSMAK4%2Fywf6Dm6tMi83Req859ESkHE7qJba3bh5TGmnxTbMkYYQfHtQgrd5oTwOVAvHMgY4Vw8G%2BN1M0JoTcrmbK%2Bqsqsyf4rjORtnLullsfHJqt%2Fbw%2Fy4srYHxP%2B%2FITDhx3aNxXvhMEIdwNWTl1R%2F8fX%2BM9cXLcShhhBKtSdANlaBy22rVCgAyY0L2iJLHsQ8B7lUIJwdOINTGmgrUgvgPvJme1qgmy6wZiJ4eyh5YLxlJhzMNWDSZmf6R9bavjlq52kn%2Fp412Vqh371UrkoH4yuz6CeNxKLO2S7b%2FiadmfBE9bhGrntKXfH3DJHe8jkBhRybo8mR3f8kwr5szIh7ewpUAgazMYZWP3Qqx%2FMK7nrw%2BMb7W3S7DKMkDCnu5XMBjqkAQVC384ugVXvNF0dkrl0nUnhXWTO17fm9h39hwUCazmKoFEkyCh%2B%2FKM4o82NHPOnsyeIsF%2Bupd15M3g%2BUDllaQS1p%2B%2FgRvwacar6eDiShguss5PQQhymtwwPM9F%2FpYL8QGWJb8sW%2FrAsw1OKBDeDr9Y52ytNaJO4dlDLMivRStxzRxR4cY4HmYgA1VoAfLx1RRZ09Q9cIR%2F08JMSs8oB3MP4zTTS&X-Amz-Signature=d83462844eaf662a1a1fe791134e7d091970032e956f005c83bca7f96f539a6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WYL4OBS%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDZbUQpKBxKFD0b3C4hbpAcpYNMrRB9rqyzNHLUHRRI%2BwIhAKxgz8%2BsMEMBkOzOWy%2BH6Zj5HOZNkMR47dUC9ILgl44FKv8DCDwQABoMNjM3NDIzMTgzODA1IgwZboWpNI9fmJNE7F8q3ANTnLVVLGj7SgRbdHGRT%2BQs02%2BOcxC2690VTXOyXSiv8Qe5YF7eksZ%2B23Q3B61WVG8IMG3PYBh1ybgpYV9wrT1mcNgtw0QGZYKPSAeM6DQGbqVGjl%2BlQ6nbFyW%2Bk9p2mQNEGEKmapZnyaBkEqGOKvt8zwqe0aHsoOMD718%2FVunZPLUnZSS14wvs8rtNbZQ8uzbWvd4bdT%2BqGgSNJtaKDzoxyXjOCWTcMXpJA1ixlqybA8jCH2d%2FRoJwDWOt0BSAbNbDSMAK4%2Fywf6Dm6tMi83Req859ESkHE7qJba3bh5TGmnxTbMkYYQfHtQgrd5oTwOVAvHMgY4Vw8G%2BN1M0JoTcrmbK%2Bqsqsyf4rjORtnLullsfHJqt%2Fbw%2Fy4srYHxP%2B%2FITDhx3aNxXvhMEIdwNWTl1R%2F8fX%2BM9cXLcShhhBKtSdANlaBy22rVCgAyY0L2iJLHsQ8B7lUIJwdOINTGmgrUgvgPvJme1qgmy6wZiJ4eyh5YLxlJhzMNWDSZmf6R9bavjlq52kn%2Fp412Vqh371UrkoH4yuz6CeNxKLO2S7b%2FiadmfBE9bhGrntKXfH3DJHe8jkBhRybo8mR3f8kwr5szIh7ewpUAgazMYZWP3Qqx%2FMK7nrw%2BMb7W3S7DKMkDCnu5XMBjqkAQVC384ugVXvNF0dkrl0nUnhXWTO17fm9h39hwUCazmKoFEkyCh%2B%2FKM4o82NHPOnsyeIsF%2Bupd15M3g%2BUDllaQS1p%2B%2FgRvwacar6eDiShguss5PQQhymtwwPM9F%2FpYL8QGWJb8sW%2FrAsw1OKBDeDr9Y52ytNaJO4dlDLMivRStxzRxR4cY4HmYgA1VoAfLx1RRZ09Q9cIR%2F08JMSs8oB3MP4zTTS&X-Amz-Signature=3de2743e69cbdc6594f74a19924b7eba64e85bb652b7cf94bbbc0f1cff67725c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

