---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQSPQWCB%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIBTjeAruqQ%2FjeXZ7zEzIm1YqlCsBVONDCDgDQq2Pgx1WAiBNvttHmukNXiIJ8DRzJbGjJ4atb4pRbMRIsD7qtP%2B4oiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcJFcALOPVLLpYYWLKtwDGIJY4p9Yk6b%2F1jnwXodsiOc%2BCcQhP59TuJvZq7Ex1zJTj1UkkIxw%2BlEv%2FM94C2HrQhdM3Jt%2BHoV1M6JZsO4zY7dAfI2Bue9RRO2q4Hl0GKDE9EL2AHFD4ZpRrMikXhCW0VyNtIFK%2BS4NIbeXqNd7D6QvywcyMaCnHWymXvZneIH5r%2BIxABVdu%2Fgi350x8wKWE6ooDoAojWJG6UotDuTfKra6prqpUogMlUMQrswy4GxgImYt%2FTK8gfj1jCEbvibsk5MQv7R2F26wVlokZmaRp2OK%2FtxriQX%2B2Ndi5F%2FArOUWWGCqgHniieOEhKJH4%2BnCHbtZ5hWr3FT61vkZZEeeBjQuL8Qn%2Fe%2FmPBdawZxjZNhYsjZQh7OcQC2cAnAVf2maWxy4vDr1jkpKAygxCa0HkBjnGPv1YoE7ukbMjk1oriDhUH1hWw%2Fv%2FUAr8Qtl1VVsWvdnlaPCrlXFgepVnQhUsL4MzyWbAhATOY54V4%2FhYNNR51wKhwPudTlX%2FQmf4y%2FJH%2FBaNA5d4xcltLxJPildxwEyvYzGZK4slB%2BzaKjcf3UW6kYkoSjQ%2F9ZzNDO7HOFRA%2F6GksarFOckschQ%2B5qVR3tTD92iTwGiah4I4kvwv7%2BbjyVW489f7yEK7i8wotC6yAY6pgEO4106ucd9%2BpHavSAz7sY4rr%2BN%2BluOefbuiYADdpzxas9E4s6UBc47jyHEc%2BQpVBg66uyZlsTiTu0NaLRa9z73KByv16aCcHrOYn%2F9dRuOtl13oSEcsjZSA40KmreFhQyJ3G5tAyX7lZt4j4NSnLIsbynHusCEIImxjyo3zqrqzBSPCo%2BOTs9u%2BEdsA77WzDiZrlBEeE4l4Wua%2FZ1NpIoNKY3R0h9d&X-Amz-Signature=bfaa7753e307f91b1b22b7b2f79fb89280e7423087600529d201307644353c3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 环境安装

本人使用Ubuntu系统。首先安装node.js以及npm。

1. 使用nvm，安装nodejs以及npm
1. 安装pnpm
1. 检查安装是否正确
---

# Easy DataSet平台安装

1. 使用github下载源代码
1. 安装代码所需依赖包
> 使用pnpm的特点:

---

# Easy DataSet启动

1. 基于代码构建项目
1. 启动应用程序
---

# 怎么使用Easy DataSet

1. 新建项目
1. 配置大模型
1. 上传数据
1. 基于分割的文本，构建问题
1. 构建数据集
1. 导出数据集
---

> References

