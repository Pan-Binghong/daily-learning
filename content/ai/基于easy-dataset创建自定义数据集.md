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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ6KO7IX%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIHPtOkrK5%2BdbBmKkNKOiJ58DC%2BpCCIId9cYtnHv2xpMmAiB4ZSfBtE%2Fp%2FtfX3IKwod%2BeazL0%2BK1w6LrZROOO7CvOdiqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZ2Tb6PZeGxcG9COZKtwDR2ogzU1GFguzU1CRuvPp5yWZifrhlQCjs%2Fu3h80InFJIgY%2FHtW8d2f9rWHtPcI8Syoh3Yu3j5bZFAQDry%2FH2E6bI1oOC0dP76Sw0BCY%2FVgrCtD7iutbS8LlHwrieXyULDcC7bGAB5jet4dNu1zQLEv7gBbrVCrfSHp12qWAxtAb%2BSOrGlXNTC4H9UerOcL%2BcBmLd%2F%2FvpS3VXYO64L9nNyzPX2tBOC1XjolsKbFmnHDTzBDfz8eZZBCXO3yh%2FxFO1cArLWpAokYd8%2FdzDPU2xRlM5U6V5F54ajRu4By7DfsWpr%2FELi6DgN9rSftSqfc8PQXDGjriImq2l%2FNFipI%2Bdw8S5gANtyz2vxZg1cJgKy02H3WiKxVbN7Jc%2FcjwNZ32weTIfhVXP%2B0emaYlMb3GO4Kxo%2BqHxbVATcTfMXAY9wy0msNG5uYGPdoRMV1O0UPnkb83OZu3cbAM44e4hbzjo4Jlwdd79CHOe6Yn48jYisFrYwS8aW99wORvPlYLFF8fd7KplfUQw7PzQM4cs0UvYd%2FxbS3DL1or9uNB0cCvFhLdd%2FY%2FxoujjYpaKiXl5IAIATos%2FJ2ZOehlMzxmqFjOB7QyvCkwT4EaCixglYhM%2F%2BfoM%2BlMIc5KmReao5zowuMHcygY6pgFmexKRkxj1dgQkiIiu4ewSkRlvoKPUi%2Bek9VS3ryB3nrpQmwQMgdrRbvYp45%2FxFP%2Fgp1fXaP%2BRLYxNyNibgjuldQ3lgth%2FdygwAEd7ZwaEJlUbUjVeONQHkGNqVhr0t3Tn6%2FnFGRrNgu72BqfU%2BdTA%2Bew2hYAZsaK3F2xJZXKHJccwCa4z0c6avsUUvfCGxha0GOHXpN2R2hPxweoPv0leVBE0IlJj&X-Amz-Signature=f90432eb36239c18a12978e9ec52b3b36831ce1289a2c5f415badce55ec5dbc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

