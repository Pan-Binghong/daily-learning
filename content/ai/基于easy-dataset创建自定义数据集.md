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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6TAKA5F%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BCuxNoFG8y9p%2B4rK3gbTxJLXN2OZimlcYhEzL3JQwKQIgV6WB2mghp6x8F5wrJFaWuqcQZHA3hkfTigbq7suhE2gq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDFS6iFmOkD%2FERnkV0SrcA2jvROzRZn0zSVajV4hmZJTRe%2BH7K5JdiowHWnUWV95E5pvZFsIzhAC1b%2BWI8vL6D8BfovDONQbcdrdDD5pxhYPNduSnMuNDyo8sSHGe3M5N3FzzQWfrCzQZJPNWXFIBzU4KlS5KFchzeHztQLgE%2BMs9cY%2Bpcbu2RSA6MBshveiwmfsBeNhyCXLbpd8f9orLOIznGq8OElHGzLDXb23mm%2FAblxoUMjYyaAeAq1jslvohjDEz67r9CvCrLcNIpB2D4sTT%2FAu9Mno46bgb85XnN21RWiIERPhQFIGbGFNEzSKuCL8arYr%2B9HX3pBXqLe6uWpFAUvsJdJICm6N6FD0QC%2B8ikPoVCcR8K0kX%2BmXp%2BeVdL0D8eNYev7p3swICz%2FkNyKUBj7bO0vIq8l%2BiWBpnwl182k3%2FXB6%2BXDRY32R2NQ7BI51a6SF%2BExhm09%2F%2FcF4U9hCA6BgZL%2BUxX7CeiFFg%2F7HmJ3ltNPz%2FhrmD%2BNyFe1cVKFuUwaVfLAJ9AAkq55jBQhnkLIcN0eXix2AlKXTbhAUw%2FkBnSbXs8gboFyg3rK3vL%2FFDkC0zlX22wn7ZoP2z8U%2FaxgP0q9W%2FSJ%2FT2HR3aJix1m4hyWdnzaPlaeGk5s1cHm3AOWZs4V5vCpB2ML%2Bdps8GOqUBKRZpE9S1CsSauS79IJ%2FRDrgrRhgySuriP8wgJGUbbyFjo4aSCd7c8gLibowD3mIl%2Fl9%2F38RrBdWk7MQFKrAvNGkAIDNHcIqbckjzQdnMKlzVPXswcmiPjnrSep5NqQzSwvGlM7vns1VGUtE0Vmqy9sjb0UGvMqO15gIrMbrOKDFIvuImm9tZi4C0fnbnQgUotrmZgErrPSFLDxjrCBFMl7IiV1nR&X-Amz-Signature=0a6c6ffa1f25b3715da30174220f2ae4bd1796f8c81defe59482087eea7979d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

