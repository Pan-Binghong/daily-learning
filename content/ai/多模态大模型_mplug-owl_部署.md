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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REB2CEUW%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025826Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQCsFA2OFwL44BSox1vIbP3v88OFnnEDvrk0SfBf%2FUuSvgIhALU%2FbMeY4R%2BWU3zvtGy4%2B6GHVA7uMUBIDQShZs7IsKMZKv8DCDIQABoMNjM3NDIzMTgzODA1IgyiQAzajElp3JBik9sq3AOCZO5vrgAqSPpJWwQ%2F6Waa8tVBP54ZuYCjh9CSnJQaCTTq%2Bdozr%2BJv0GOTgvjzaiJUs33e1M0k9WKoaZvJQHxpPBu%2BrnDmRbGai58rDIgSxl46FXm8by5RrL8doLG3Y1s79jguSolPoi5r5hH7545fVX4aut5V27peKuiMlLcS3tA1Wh9zZujpQRlLg8OiIWMyG3frqKYZ6CgsdbPG%2BGndJkoNDXmaSC6rxXQ0mV9YDf9u4whuR45FGm8kgli%2FFr6h2Y5NcF%2FM3frWSdfuaUdeBf%2BfnutLRJNtx1uARMNrNT2xI2P9QbbpoM6fg27DQ2arzO5qBSjtNglX7%2F5Vq%2BNje42F5QGI8oIuV4eZ13W1SWZTQ9LXeeFzH6a%2FZD8OYdkMALR65KkQLsGRg2wnB4k1gcyr3F%2FHmw5j3T%2BZfJIXkgTfmwl45mPjBi4LNO1mMUrMyb6PgtqoRDksH0BUcDiw6pyL%2BkV2IHiw6w%2B6pDcwWdtikMqxWZmZ6S%2FufrgXLxIVN2uij0X2Zn0xJ%2BIBR5Wa5C7sddRCSegLlbW4HUtZKPFBSdPqZCxpriEvWptPuV7GJmztIAccWcUm9DrGQn%2FfnxkDwuIIQR6Nnc4ND5zOdovvIZljQY9zvpuZrjDesInJBjqkATA1Uy0t%2FQuIY0I9CtmS6d%2FntxjRm8tKDHBa8y9FNNZv%2BHkkSpRA4REfnngJyKyFfAUDJLTzXPK9N92qRy7yiJtwbQlFzHri7tY9DaYNwR0cLviOJXVJs1yYmCN4uWAQa8cPrK8IhaZ2MwzsHSv20aJfG1rLYhAI5KQgNhIZ1c33FHWYoingo3aQfGIsackJ0l%2FXqFClct7MG0wqtsBuC0EBf1n3&X-Amz-Signature=55fd8deb3fea32389f1a54bf35069df541e0b674bdc722ae6c6c5797daf04684&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REB2CEUW%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025826Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQCsFA2OFwL44BSox1vIbP3v88OFnnEDvrk0SfBf%2FUuSvgIhALU%2FbMeY4R%2BWU3zvtGy4%2B6GHVA7uMUBIDQShZs7IsKMZKv8DCDIQABoMNjM3NDIzMTgzODA1IgyiQAzajElp3JBik9sq3AOCZO5vrgAqSPpJWwQ%2F6Waa8tVBP54ZuYCjh9CSnJQaCTTq%2Bdozr%2BJv0GOTgvjzaiJUs33e1M0k9WKoaZvJQHxpPBu%2BrnDmRbGai58rDIgSxl46FXm8by5RrL8doLG3Y1s79jguSolPoi5r5hH7545fVX4aut5V27peKuiMlLcS3tA1Wh9zZujpQRlLg8OiIWMyG3frqKYZ6CgsdbPG%2BGndJkoNDXmaSC6rxXQ0mV9YDf9u4whuR45FGm8kgli%2FFr6h2Y5NcF%2FM3frWSdfuaUdeBf%2BfnutLRJNtx1uARMNrNT2xI2P9QbbpoM6fg27DQ2arzO5qBSjtNglX7%2F5Vq%2BNje42F5QGI8oIuV4eZ13W1SWZTQ9LXeeFzH6a%2FZD8OYdkMALR65KkQLsGRg2wnB4k1gcyr3F%2FHmw5j3T%2BZfJIXkgTfmwl45mPjBi4LNO1mMUrMyb6PgtqoRDksH0BUcDiw6pyL%2BkV2IHiw6w%2B6pDcwWdtikMqxWZmZ6S%2FufrgXLxIVN2uij0X2Zn0xJ%2BIBR5Wa5C7sddRCSegLlbW4HUtZKPFBSdPqZCxpriEvWptPuV7GJmztIAccWcUm9DrGQn%2FfnxkDwuIIQR6Nnc4ND5zOdovvIZljQY9zvpuZrjDesInJBjqkATA1Uy0t%2FQuIY0I9CtmS6d%2FntxjRm8tKDHBa8y9FNNZv%2BHkkSpRA4REfnngJyKyFfAUDJLTzXPK9N92qRy7yiJtwbQlFzHri7tY9DaYNwR0cLviOJXVJs1yYmCN4uWAQa8cPrK8IhaZ2MwzsHSv20aJfG1rLYhAI5KQgNhIZ1c33FHWYoingo3aQfGIsackJ0l%2FXqFClct7MG0wqtsBuC0EBf1n3&X-Amz-Signature=8a565d6b54e4b25fa7b85688d2703a4137359ffe3f3dff36d1567e0c6aae2047&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

