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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6XDUPIB%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHb9KEcFFgOvwMx1C7v%2F1Io9nUKLr3NIBtr3XygAwWUgIhANk9EnmJ5eC%2Fr%2FyBZ6Rogxor6871W0MWvsdMEKi3TA4YKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDQbe0txWtHJOdpsQq3AM5OVbv0iCkuwNg3Y4Vee1%2Fpo8w90TYYwW1aarugOnGXTHCjEgZbRnZCxsIDDgzgRsYl%2FZExTVxh%2Fmv3SNZl1hU6kCwlL0gGE33aOiPHNZAxuy%2BfesSD1N%2F9pbnVw3vWFWfvyQDqhlsfHwGqO7wABW%2BRmV%2FqddiROoL9lJTFLW69hH8H5VprNa6z%2BV1YgxZXbxUCDHbq9LycY1JhQ9K9t7AWzCWR7d%2FEJOAtVj3YnSNPLRWmqgI70CeXuJdieG2T1Pc59tD9YVJxzcGd9jN%2FJpvwvDbCw4mQsA6uzAO7KuwZ247om6AARRi9%2FgLZKkMEN%2FjqMNjS3CYJlJa8ZP7yhRuwBeX4AvqoR2ZprJwuYidTVCw4zv8RzW78fnQzU3hKf0GwA1YNWLMEMBExzOwRuQnQCbqMrHsFy2XudnlsrwrLqm43YvNheMHLdvL7ra7kTkWlcdkyplLXXe2BAF5Wcy5db5TZXUwqEDI7%2FEXBKjZlQ07i0A1IJM8TcNSFfhF0Jgi4VFnLm%2F5P4Q9YVF5d6FcQRV%2BLiOe2MI%2BmwcPVDk4eapSXViV2o9R3ADAtN4xbaE4aUUkkFDPZj%2BCHYb9GhvAnsYOAC9cg1N8kKtLfckaM%2BL8IMcDQcJK6xEwbjCU79jJBjqkAYZuW81RtfPwNxP%2Fcuy0JT%2FWo7uQ36fqUxTJaJ4tXKGy%2BZe2RtM4Vu5cEqtae82tyH7F%2FghAGHNeA715f4S4wXcm2GeH3F71Ll5ysgeISQrhalhX1BlraI6IwtFoirA5W0VFq7KPHvLwxOsS3vwkruaoFGoiF8PFs%2FGPgLcAw99ddabf5yIaSpG741u6Q8OnzD%2F9%2BQhVxQpJvjmsHP79Nj31osbf&X-Amz-Signature=45c7865e83a6edf79d28474ae2bc83330be7b30b9a0b2562348396de1b8b7035&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

