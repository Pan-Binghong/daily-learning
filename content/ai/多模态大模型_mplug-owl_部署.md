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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNSHABLU%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIACqt%2BVGJlNay%2FbfIj6UgvilhZ5WwuAfhokXpI21mISAAiBsYy1yUX1ecq7%2BZTmEB8MoSIBmtiGrtjepMNkBqQFEjCqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpH4S2zXflzSXBWRTKtwDhfcixWLOcqd8YqHSpZkAVGwrTTvKo2dmfp4oKraEFh8LfW71P7kk%2FI2FImSa0ipUDVk6sOdOJtCNP9UtnHX4fP0S0MuGsu7gjfXkK53U64iyVj4KsbTtfmyokqKuaiZSt1ptEZg6pRo45IK8G6qdH5h0aLAfjEUIv1szZqzcYoAqZ5ae%2Bg%2BQ1ijhpwa5vwWH4Qm6FlZrUVTjPIvdYxZKhEAG88gTJDY0dKHgqanZjE810%2BZWsi98RDzNu7Chpb2f004nH4rwZx65KJYATwiVEjtS%2B8IbW5ISswSnK0sRs19ugggKhPKmls7IhNl5olPd63BYicPkdXyUj9Z8%2FtykkVB5FIJ7DWCISBuySM%2FfU%2Bn7NR2EwmzLAHrJVYikAFmXxbe9hgilnOVpJQynRHqPY9Hjl6cnAp5kkWXWOUnWYLV5FZY4%2BZ7GFcn9YFevsv8kd5bvVGfCH%2FtsOep83FMfS2xmQJRq2Qw%2BIrm%2BTeR6eOXKd14MJ3cav4CO416uPim4X7RTfGN4FEjijkihuH%2BbE7WTFJLRqcR%2FS3MKiI24SyVxlxsjwSHyHxzXZp5jm%2FCY4dHk1APEOSmsWjSzckYUt%2FfQElzjfhfYthQ1sgFyEzpYTU%2Br1ZJFv67cR20w9LXoyQY6pgFJOdXk3tOZxnBCxGVWoeJPJEQ1RzEixEZdRTERMupI7CwPCi7D6xK6de16NgSXiAhqnv4Dh%2BaJJ6nfUT%2FLp2BY%2BgFc03bFIs2Rz6XPXxpunEVtsDUj6yCi%2FETBDcdZsd%2FmzI4wYrKfcLNztK%2BVq57AYnlGxkplIUBSUaRj9QOL95veUvt0dJ0EjnidXobaMKJLDVLB7UnY2Rtn6ndTN6UBP1NdMQrw&X-Amz-Signature=d760522f68596034814f50cea248ed633a07041ea34c4c22399980013a902d4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNSHABLU%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIACqt%2BVGJlNay%2FbfIj6UgvilhZ5WwuAfhokXpI21mISAAiBsYy1yUX1ecq7%2BZTmEB8MoSIBmtiGrtjepMNkBqQFEjCqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpH4S2zXflzSXBWRTKtwDhfcixWLOcqd8YqHSpZkAVGwrTTvKo2dmfp4oKraEFh8LfW71P7kk%2FI2FImSa0ipUDVk6sOdOJtCNP9UtnHX4fP0S0MuGsu7gjfXkK53U64iyVj4KsbTtfmyokqKuaiZSt1ptEZg6pRo45IK8G6qdH5h0aLAfjEUIv1szZqzcYoAqZ5ae%2Bg%2BQ1ijhpwa5vwWH4Qm6FlZrUVTjPIvdYxZKhEAG88gTJDY0dKHgqanZjE810%2BZWsi98RDzNu7Chpb2f004nH4rwZx65KJYATwiVEjtS%2B8IbW5ISswSnK0sRs19ugggKhPKmls7IhNl5olPd63BYicPkdXyUj9Z8%2FtykkVB5FIJ7DWCISBuySM%2FfU%2Bn7NR2EwmzLAHrJVYikAFmXxbe9hgilnOVpJQynRHqPY9Hjl6cnAp5kkWXWOUnWYLV5FZY4%2BZ7GFcn9YFevsv8kd5bvVGfCH%2FtsOep83FMfS2xmQJRq2Qw%2BIrm%2BTeR6eOXKd14MJ3cav4CO416uPim4X7RTfGN4FEjijkihuH%2BbE7WTFJLRqcR%2FS3MKiI24SyVxlxsjwSHyHxzXZp5jm%2FCY4dHk1APEOSmsWjSzckYUt%2FfQElzjfhfYthQ1sgFyEzpYTU%2Br1ZJFv67cR20w9LXoyQY6pgFJOdXk3tOZxnBCxGVWoeJPJEQ1RzEixEZdRTERMupI7CwPCi7D6xK6de16NgSXiAhqnv4Dh%2BaJJ6nfUT%2FLp2BY%2BgFc03bFIs2Rz6XPXxpunEVtsDUj6yCi%2FETBDcdZsd%2FmzI4wYrKfcLNztK%2BVq57AYnlGxkplIUBSUaRj9QOL95veUvt0dJ0EjnidXobaMKJLDVLB7UnY2Rtn6ndTN6UBP1NdMQrw&X-Amz-Signature=e67eb99fe5e398a896af902248ff0e0b1cf53364d3089bce084dd63337e9fd28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

