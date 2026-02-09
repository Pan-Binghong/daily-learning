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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7H6P35T%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCm2pEZofL%2BsVhWirmT0rBH3aO08DsylN3fNBGM%2B5BI1wIhANkHkPEhBBw4JbDfcKH%2FcK1GToSe23QcRfFFu5oBKvdGKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwbVn9HJWl2Z%2Fp1yUAq3APl1sRACyKw5x1Kcq5v7iJdDQhgqvNiy%2B9um%2FiFeZ7THoj5vzeWKSdaRYX7AWAzjYqO41FGxKI0HhC4peKRJWvCgHdYgAfIgYlJLzxNkFZDFhPnz4JZASftVoQpwoGyFLbABjn9jmZ5bD8Y0coDMkQSyS6ZNkbLlbeNHefwdQA0pVKS7412l8hyOGeP2%2Fa6Pke3a3M5djvJSeWECS6%2BbHKaxyfgqKn2x6aAdVhOV8Md4dQOi8JV%2FobyRlFWrjoUfW14lX%2BqoLskjGjHa9shU6I9eDbHo%2B27jPYv%2BxtOqdYZCInZdYqtrUHGLecugBEZCBrCSHvFUTprJt8GIsPq49PlvpcgQHJ6oZQOL4CieX8r1gHEPN%2B23aBKxCYpJv69FTDnfnfBp0Gr2mszr4koWBDTHSDW9T0yADTNqoxlLCJMfZ0aBqKL%2BLteN2uT%2Bcu4pVkIW%2BcxFARdA6IoCw%2FjwTE1fwW1SCkvehV1bCLlj7IkTXW7kgFJjJITBmXXvq1jq4Y2zQ94Z6uK3ODviorHE%2BUXyvnowrpBqL42ZhMHEYpWt%2BhO9K87bH47%2F8mW6L5t0gQEQNpVgsIgCLcGQviqCbCa8D7NR9HANGwGLn73eA9TXpU70PbSAvqQND%2BaCzCZlqXMBjqkAUS%2B%2FskAHCEBbWDFtogP6tyyxX0NY%2Bc1060x0Z7r%2FuUwloSFYbfM8EXcIYr%2BxllfcNTDc2ABjfoxCHlRrJz16TgOrgOk5rDB0QjQcNIum5YCqf9zjuQtQi3yJj7yaRYmkdFDlnZZ%2BZuvqWWHv32z8luVNe5rdi%2BGArbFF%2FTlK5lVfVNhlqEpjfmZoJhWukxsTW0dL95D1pV5R%2BAtLDr137rYjYqV&X-Amz-Signature=3520f53d4f1e8d3d80811e9c15e3796410970a9c3ea2fce33186520d01d984b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

