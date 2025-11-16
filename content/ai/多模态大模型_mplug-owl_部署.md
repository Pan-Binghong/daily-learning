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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z22IQRSL%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHb3EQTyHVc7eIB8vsJih7kLop3F653MODw9AkYqRsVAAiB7fIyk%2FtmsSA%2BH6uIFs4AWjrq6QJ2Bjlq5rcAE6xX8VyqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI5XW1sfogA%2BjIxTmKtwD0EVQCi8K93GMKLLoQhHVIoGGz2aY3eNfq0KEgrDms6mV%2FUUav%2FQHwo6d6Sguuu2TagnFFkI9nwbZf2AmyqS3tY4w3bUjRlRM8NwD7mswQQn7H1UMWrsowrHoYeCU2gYUuBI1cGkeLpNi2HVR8TXN0BetrhjvTo%2FYqtgEfZpURHz1gJzAqUbe47dOhSUA1p0geOrI2RFNPfxwV4bbxB5bCpwosiUh4RU9SW529RTy6dmiqULmPXgkmiaAN6jluunBAr2hM0QkfUmHHtP%2FlW3D9zdUy5LiAncuP%2Bab9YNoivbgK0PgoNvpn5fjfrj%2BFpgQaUbgfxU%2BdC38ewfxLHaIiMhqj79LzQd2yncJ2pXf335hGMYBWk3ClwW5BRb92w68GOGH2DenZ3WLL5mjNckUuK5yqegO%2FQnHZFTn2U6M4PtcWSBSrFD8cMi%2BdCnWG%2Fn5BdtpIHGSHFWi%2FnZ%2Bv%2FQhKubdJ%2Bi%2B%2FT%2B1UVsYSXtuQPgAAenUAoAmdgl%2Ft1yV4p12M9wne6Z7XLAtHRLTLDC%2FaAyVJ5qyjN2S3JB5WtbbNvizRsrmRq8JXYO6EiQTZ%2FzSwCBzhm2OwiKdu%2BtTQ14dDKOIbahDrIHFh1CQU1HC%2BwttQW4Yvg3iQgYF5jUwnuHkyAY6pgFPuv1YRoad2vL2m%2F9wiasSIrFhpP3bxJVcL1On%2FU6zMrfWoC5wf%2Ff8Wcs6XZHIIPbD5AxWjzMi0Qzl4Fd9GLMjX7VZbLaEByRrqK4fIe6xOY2I%2F7lMSjgHUUXI92RhiWaJTQt1edq0CBf1%2FtFjQQU446H7zyUSWZkWtcB%2B%2BWseLd6o0VTvfMiPECGe27Eo7eOA%2FqxMTlYGzAXMEYCG1rQpFF5G3HhZ&X-Amz-Signature=da0920d126059de91427e41eebe85c419e96e738b4e94f9d3d9400be61bf9e89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z22IQRSL%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHb3EQTyHVc7eIB8vsJih7kLop3F653MODw9AkYqRsVAAiB7fIyk%2FtmsSA%2BH6uIFs4AWjrq6QJ2Bjlq5rcAE6xX8VyqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI5XW1sfogA%2BjIxTmKtwD0EVQCi8K93GMKLLoQhHVIoGGz2aY3eNfq0KEgrDms6mV%2FUUav%2FQHwo6d6Sguuu2TagnFFkI9nwbZf2AmyqS3tY4w3bUjRlRM8NwD7mswQQn7H1UMWrsowrHoYeCU2gYUuBI1cGkeLpNi2HVR8TXN0BetrhjvTo%2FYqtgEfZpURHz1gJzAqUbe47dOhSUA1p0geOrI2RFNPfxwV4bbxB5bCpwosiUh4RU9SW529RTy6dmiqULmPXgkmiaAN6jluunBAr2hM0QkfUmHHtP%2FlW3D9zdUy5LiAncuP%2Bab9YNoivbgK0PgoNvpn5fjfrj%2BFpgQaUbgfxU%2BdC38ewfxLHaIiMhqj79LzQd2yncJ2pXf335hGMYBWk3ClwW5BRb92w68GOGH2DenZ3WLL5mjNckUuK5yqegO%2FQnHZFTn2U6M4PtcWSBSrFD8cMi%2BdCnWG%2Fn5BdtpIHGSHFWi%2FnZ%2Bv%2FQhKubdJ%2Bi%2B%2FT%2B1UVsYSXtuQPgAAenUAoAmdgl%2Ft1yV4p12M9wne6Z7XLAtHRLTLDC%2FaAyVJ5qyjN2S3JB5WtbbNvizRsrmRq8JXYO6EiQTZ%2FzSwCBzhm2OwiKdu%2BtTQ14dDKOIbahDrIHFh1CQU1HC%2BwttQW4Yvg3iQgYF5jUwnuHkyAY6pgFPuv1YRoad2vL2m%2F9wiasSIrFhpP3bxJVcL1On%2FU6zMrfWoC5wf%2Ff8Wcs6XZHIIPbD5AxWjzMi0Qzl4Fd9GLMjX7VZbLaEByRrqK4fIe6xOY2I%2F7lMSjgHUUXI92RhiWaJTQt1edq0CBf1%2FtFjQQU446H7zyUSWZkWtcB%2B%2BWseLd6o0VTvfMiPECGe27Eo7eOA%2FqxMTlYGzAXMEYCG1rQpFF5G3HhZ&X-Amz-Signature=0f91a163a0e1e178dfb0955c2dcff157025b62c160c95378dc01f6e2ecc1f799&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

