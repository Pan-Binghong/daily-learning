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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDPTM7DO%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCICMBLw9qSG3%2BLbzLDTNeH%2B1QEO2qcngXV3bl5R1z%2FfoeAiAay90vJbtL%2ByxpEETrISZFx3bKgyu3bFWW4Q43SUnapCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMEzZSOcDq6VUtiee5KtwDWW8fFRxSlTkyPi5GMBUmx85cfEiA2H1bK76k8R%2BTX3GUNbj0n%2FDw9OQpmwP%2FYyatCs3rgNGchqNkO6HqQ%2FaD30M8txpszAzJM9BIxe3J6%2FC1sCRxhTqPbN1Quc73AdqMZf4fNOKHCQgiNL%2Bv995nPvE62EkT1dgZmoy8XJLvis4XHLHsncfQV2PBcmwpMeBb9i3Fo%2FjLx4jFhO%2BkD46BaRaJONTaw9e9lwgujZobNVC2obhPuXftz2YHeiqTarlwzGBWDX7VFt1xO2%2F4LNu4krhJf0zRVI4co8DXW9fC00q2J0EjS6EZyXAc%2FTOVHNs6qDbHUeBAiGyE8G%2F5oG0f5irN%2BEn2pPbZ6%2BmrLa9c3%2FsedYYINnGCN3%2FcPr61Hz7gQNHW1DtWg9AwEsc8%2BekuXcezZedQ%2Bm1tvreJhuDXOrK7GSFs6QBWQ%2FWgRDfxXjA4NDsjIt06AqycxG5rOwFW8vMpLVaYyC%2FZtEcQojXNjKLRHTynBsqsgN5MeyyqhM7Re3rm7282s3FSYt3VSqb4%2B%2Fzz2aSvKheNaFWVasdAmLxYXUx29djxQeZB07s6ePa2Udk%2B1r9ft43J72vB72Kyg7WGTk%2BnI1GuHNXjSvVdAf8uvHgDvn%2ByfkyXe8cwnN64yQY6pgGMjb6odY%2FwTVB0AeFg1thkKtFo0iElQTdXv9MJbmQCU6PwU%2Bz4myc0JOifWtEFj3JjO9DADRL0idft7iWJ3CAD5C%2F5jVmkVlWfVPfswTOapzsmsjDLieatehhhnm%2BXY5kzyk9PWfbNoKNGKB1MArHJtBM3UPeMI1xoa0qjVZ0CmiPmH42PfEcYr3bIb4qa7%2B1p0Fxz%2FYOHjLjHhclv4e3wWajEjNfd&X-Amz-Signature=8366d3f77eb26100c485ebeb3dbb3c1be8f1478f1a838f66dc20092a9ec6d9d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

