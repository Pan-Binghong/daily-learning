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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQJHAIX%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGmeRKUu4jdmcCDG7UtIgKChcyokwwBXsSSwgaDlSEOoAiEAgbni1IofAB075chE9bz8JilNglEQvgxT7AtF%2BCbm79MqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDTuluYo%2Fa1yUl%2B0cCrcAxsyjQ8rB1iI7q0zSpxd%2BhtMvhVXECHLTRrcKlV8SzXKK7bUFZQgdJ3QNZR03pPu8agIslK0Cnvbc3acE4iCPqpvp4hshsDqGTynACRt6EG3ijBSurY9Vo6Kjsw0ox6h4yYEJbGCS0RHChzQOOAK7%2BWe8OBGVLR1lvPySfZbfjc65SZVnvV%2FjguNzUQcda0ir%2BRcarcA04eduIusckbLPV928V%2B4H5pG%2F9%2BFEgrY0G3zj98H9tew2mw2DMBa0nd8MUDbmAUOU7559%2BEq62rh3iOASJrafYJWcjZmvnqyRy5uoB2L%2ByZIgDz%2F1aRH7VZIXHEed54pHEMjwstHP5%2BA16L4n1NEqdtvaU5%2FeMMr8EA6b5ZTYcbTwqquhWXIELZyErxYk0HvuPvjmQnzn7fLTlM4GgSMxzUCVUo6rHh99qYNZ4JQsnuj%2By7VxdMaAwL7jvtK9i8tnoSfdfc3aRHq1PYqrZdaAPh2kHxlW%2Fq7Q%2FWF02wuvhdtpbI8SK45lXY5HVWeb8xH%2FwoPR7dC%2BcnXreEbCDCh6EgeKVTiv5F53yGSWQVARt%2FtGWn8PT%2F5jZSqGirEHOPG0%2FYfeJYqDlranO%2FsMA04QFzRoPjNqBa9VX%2Fpx6nZw1l4hSRngQyYMNHyh84GOqUBLsbRtpcQ4NM2r4liAm1cZWgc%2FI85rutvnY%2BuZJeBa6sropPamYkFmhRhMZz2APzL3KDny6E%2FJiQ5VhnZvFn0dBfBEmx1HfJ9y5iScvqlypsZGkxTycF1Ru6ZVrqRO54hlqS0UeOP9O25wD%2B4an2yjvwVPV0XYw18BVSDK0%2Bc0iBwE9Ls6UV8emYLghOhflMilyQM7UaBu%2B%2BAlG0RB8uPMkJ%2Fhb6S&X-Amz-Signature=8b3230baf47f8dd9a958032aeeaf62fb93f061220b8e625613c6b34645b7b602&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

