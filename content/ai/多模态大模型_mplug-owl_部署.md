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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGRHUI5I%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCt0CpGUzlEvWm4ZIow%2FTFjW01TcmmvfV2E%2F501P9efEwIhAMtKBHcOkFGv7%2BO6at8qncK7A2wHIguzIevExuRHhIrVKv8DCHwQABoMNjM3NDIzMTgzODA1IgztxTmIyOzUzE8yIQAq3AMOWYJNgHcdvW38nq2u%2FbwQypYCZhJu8jHv7jtS7YDMrZgDfLDOvfp3m9B6Zy2%2BlsCjtU6YwT0mXPMcgWNN7SMc9WSwMt2Sny%2FtBMbg4KhglW9YOhElPlrGYTJplRJWNpCCCymJlBuTiGy0U8Y6KAJ9UIMKv7tN6SAmWaPXFkyj%2FwRPcvgt3kT%2FENPO0%2BedZWMxGlzn7CwIyGM5ih%2Fn8gxI4CVHR%2Bn3MVv9FmV6UeUltUFdmsEdGzagR1lx93OD%2BzuKq9PaEDglmPWhMHZSAxFev9DYFM6l9j47gzR3PRvRCmxkbJtl3XvhpqEBYGxk%2FWgzlMlQkA2aHEfj2nKZnTH0GgPHnboP3x4z79w95VijrbhuHu%2F5Lb3PqZOsBUc%2BMg271Lwsrd43utxfY44aeNO7rtJhGpCzltp7kFjEQDwwuGlFWQrv23bxAxTC8%2BqGnP3%2FLmGx2UKVPppwg1dAqroaduU5yv7Szlna3Muwvy93SykpTXLHBZZALilTlf6199ZbDOFp14jSwjeJ8rVmZ0zKHIdt2z7%2FMoy8YmilZExDytnYwSVSJa0VGVQ3aM%2FaSiQsPX6NvAl5uN7s71%2BbSzKNj6niuU8%2FnGcm8pvWqAjwF4Wq8IG9B4BCcuuacjCH47zOBjqkAcuyiw0ui9%2Fcd3GXbngslPOKS2%2BIObt0JtiW27lviXHYFiHi%2FcMf5G%2F%2FVuWegHZURLsisr%2FFYKeNURiCz3qAknc943o6aR1ltYPPTR5kGdecpBnRDjW6F0dtrA8t1dIpSUAkNU88wA51NdRSOlWkOzr1ggxMBHkhWI%2FJkEGaWCk3ygNRQwO3FX3U5xHbW%2BBQ0lNZzQixKhlJpyukyIprQDnjAB%2Fr&X-Amz-Signature=36ab80fa5255d75811abe9adc4610c01f29221a4499c4ecb6fa3c8f09daddfd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGRHUI5I%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCt0CpGUzlEvWm4ZIow%2FTFjW01TcmmvfV2E%2F501P9efEwIhAMtKBHcOkFGv7%2BO6at8qncK7A2wHIguzIevExuRHhIrVKv8DCHwQABoMNjM3NDIzMTgzODA1IgztxTmIyOzUzE8yIQAq3AMOWYJNgHcdvW38nq2u%2FbwQypYCZhJu8jHv7jtS7YDMrZgDfLDOvfp3m9B6Zy2%2BlsCjtU6YwT0mXPMcgWNN7SMc9WSwMt2Sny%2FtBMbg4KhglW9YOhElPlrGYTJplRJWNpCCCymJlBuTiGy0U8Y6KAJ9UIMKv7tN6SAmWaPXFkyj%2FwRPcvgt3kT%2FENPO0%2BedZWMxGlzn7CwIyGM5ih%2Fn8gxI4CVHR%2Bn3MVv9FmV6UeUltUFdmsEdGzagR1lx93OD%2BzuKq9PaEDglmPWhMHZSAxFev9DYFM6l9j47gzR3PRvRCmxkbJtl3XvhpqEBYGxk%2FWgzlMlQkA2aHEfj2nKZnTH0GgPHnboP3x4z79w95VijrbhuHu%2F5Lb3PqZOsBUc%2BMg271Lwsrd43utxfY44aeNO7rtJhGpCzltp7kFjEQDwwuGlFWQrv23bxAxTC8%2BqGnP3%2FLmGx2UKVPppwg1dAqroaduU5yv7Szlna3Muwvy93SykpTXLHBZZALilTlf6199ZbDOFp14jSwjeJ8rVmZ0zKHIdt2z7%2FMoy8YmilZExDytnYwSVSJa0VGVQ3aM%2FaSiQsPX6NvAl5uN7s71%2BbSzKNj6niuU8%2FnGcm8pvWqAjwF4Wq8IG9B4BCcuuacjCH47zOBjqkAcuyiw0ui9%2Fcd3GXbngslPOKS2%2BIObt0JtiW27lviXHYFiHi%2FcMf5G%2F%2FVuWegHZURLsisr%2FFYKeNURiCz3qAknc943o6aR1ltYPPTR5kGdecpBnRDjW6F0dtrA8t1dIpSUAkNU88wA51NdRSOlWkOzr1ggxMBHkhWI%2FJkEGaWCk3ygNRQwO3FX3U5xHbW%2BBQ0lNZzQixKhlJpyukyIprQDnjAB%2Fr&X-Amz-Signature=0ca62462b61b5093a688bc24c13b5c4704be1eb510bb41bbaef5aed319936b5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

