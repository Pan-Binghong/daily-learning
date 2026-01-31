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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6HFSDUA%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDj0U%2F7YqHvvJxxdOSX3MXeU1%2FRwZfHy5Ya5RAzkqp8dAIhAL8iQdXUouM23SxJA%2BPBTFnB0qN3dNmL4eAqHlrEIX%2BuKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPWnP%2FzHhZZb1g3FIq3AOJGqgjvcbZUnypeMhIodLKpUkSVsLKuViah%2F%2Ft4nK3MY%2BgGFZvjzKKlwkqJ%2F5L0Ay8RDQqyvi%2FXwRpPOQHruNh1dgwFoYluSnjHT5bGELRIJSJsFRk4PDxxZD%2FrMjhsn8qZew5mlHC9jcvlPs5tVkU%2FBeGsZW0jQPAWJ%2Bh%2BtThR0xGoqcJ%2BFm1z5JH00An4HPWi%2B3JipmRHRkbXXyrmtGeR8jiDjxWkuNbZSz6fZnFVZExqUtLyC4P9nwjZL%2BRGE2np61nV%2Bbj1U5e51GXZdGc3bKO3szajL9lvc1UeUG4cKmq6T4ViQpnGY4QryKyvml2c3BRrz9yE3DrmEB35qrxaczOJ8%2BN8c2IWTzlUqfNepZm05HyCmLImhyvpunHtWBdPcYM5UQ009DYxwLxRDYvLJjs%2Bki163rdO4Fd1ia3iU4mn5JjJAZ3eMwGMT%2FYzTjOsmwJBhIoti2vopOnuV8aY3zkcG9aNd2sWhMud%2FPC9eSxweDvw%2B%2B0CtLPAZyzlU7PZn8uZqSm9CaFn821RqhLu32Ny19TCZM8jSUCp9XEvFhwoitvBESK6%2Btj76yMexO%2BiVxDTuRWu6qwp620Yw89Fl6zCc3npPaklNeJeUqoUkrXgrq%2F2NQKOBZqsTDszPXLBjqkAfTmB2ZtfFnnMqryagHox3c5gd1QbN1Q1SQYhK79R3ZmuBEfEWuGC9oDrVz0RhSL%2FmGC%2BBDfjDTpcKsrnCUYzNeEolMjr4OAmG0pEtzYLn1Nfp6ge2fjDFHLYw%2Fgqs2X%2F%2FnSUSQI1T4uSanJPvT7nwcRWEoLnna3jHF26KLbZUKF%2BrsHSUJkyfITsGWwou5XWRiAT%2BfYFMyT%2F7UNlr%2FH5fvCpw5s&X-Amz-Signature=10b4390a664fdad85c86fc45b4d9e821f408bd6d636e7790564282c2d5e92644&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6HFSDUA%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDj0U%2F7YqHvvJxxdOSX3MXeU1%2FRwZfHy5Ya5RAzkqp8dAIhAL8iQdXUouM23SxJA%2BPBTFnB0qN3dNmL4eAqHlrEIX%2BuKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPWnP%2FzHhZZb1g3FIq3AOJGqgjvcbZUnypeMhIodLKpUkSVsLKuViah%2F%2Ft4nK3MY%2BgGFZvjzKKlwkqJ%2F5L0Ay8RDQqyvi%2FXwRpPOQHruNh1dgwFoYluSnjHT5bGELRIJSJsFRk4PDxxZD%2FrMjhsn8qZew5mlHC9jcvlPs5tVkU%2FBeGsZW0jQPAWJ%2Bh%2BtThR0xGoqcJ%2BFm1z5JH00An4HPWi%2B3JipmRHRkbXXyrmtGeR8jiDjxWkuNbZSz6fZnFVZExqUtLyC4P9nwjZL%2BRGE2np61nV%2Bbj1U5e51GXZdGc3bKO3szajL9lvc1UeUG4cKmq6T4ViQpnGY4QryKyvml2c3BRrz9yE3DrmEB35qrxaczOJ8%2BN8c2IWTzlUqfNepZm05HyCmLImhyvpunHtWBdPcYM5UQ009DYxwLxRDYvLJjs%2Bki163rdO4Fd1ia3iU4mn5JjJAZ3eMwGMT%2FYzTjOsmwJBhIoti2vopOnuV8aY3zkcG9aNd2sWhMud%2FPC9eSxweDvw%2B%2B0CtLPAZyzlU7PZn8uZqSm9CaFn821RqhLu32Ny19TCZM8jSUCp9XEvFhwoitvBESK6%2Btj76yMexO%2BiVxDTuRWu6qwp620Yw89Fl6zCc3npPaklNeJeUqoUkrXgrq%2F2NQKOBZqsTDszPXLBjqkAfTmB2ZtfFnnMqryagHox3c5gd1QbN1Q1SQYhK79R3ZmuBEfEWuGC9oDrVz0RhSL%2FmGC%2BBDfjDTpcKsrnCUYzNeEolMjr4OAmG0pEtzYLn1Nfp6ge2fjDFHLYw%2Fgqs2X%2F%2FnSUSQI1T4uSanJPvT7nwcRWEoLnna3jHF26KLbZUKF%2BrsHSUJkyfITsGWwou5XWRiAT%2BfYFMyT%2F7UNlr%2FH5fvCpw5s&X-Amz-Signature=8a36e14d4562f2aaf695491a4145ff472d89af22495c6a5e11a279fb6d485f3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

