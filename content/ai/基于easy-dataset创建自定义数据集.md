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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LVZLWHR%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCH48u0l5M55qoX9tHfncwhJRKKrzEuDMyEPx%2FJfH8sxgIgNGzr1s%2BGq4LxGOz9QivpE6kfBramw%2B%2Bdx7rfScwXKvkq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDOfFtQ1oUJDBPM2D9ircA3VgvEg3qzQtddFGfhE11kmmdUru8WXqh2MiwlsFtPiaOHUDquD%2FnR7bUQJS0NL6l34DlR2hP333sx74nW2oA2WlF8gQeRZfBuLOXtXLXw1qejMX0Ovy7%2FA%2Fqz3eIpxER4FqxtHW9K9AQQfub%2Bipr4xWxlJhASEbvD4kSUqKC2zPGlzrQaNxWx%2B%2F8x%2FuB4wKQV6fwK%2BsXqg8ZilhwO%2FokjLzlJOFI22nwrw5eD5rjIDUeRxEDeBMW7iIZC81DkiqZCDoLo34DJBqr%2BFPyWR2L3dUx3TTvy2s6zFDGLeiCTjP3O6tDvAMV9%2BTYqlvQZR1slZrdKtW8sTkQIBlb0FkwF9BSY3YMEI4kph%2BZ7fSIOyVPzrj18%2FIaegHtt2wh%2FI%2FuKyHmq4w0Vs52kPxIAGNr7CWYaF%2FKlLfre%2F2knr%2FYHkro3hrbgzGwqdku06YAirrTW%2BaGBeQ2OTER8IgLdlPXvG5faWKLkApBq7bNsUkck9Pll81sTbzmbZ7mSDoeO25RKp2O120ABA6OqVLxlcoD0WVNqbc6KCT8tmmbilTQk6cBVCDGRE27xZfDMQgw%2FSGli3d9qk4OWgInlVnct65LopyhTNWkoG4XN%2F23LdqvrbhkLOPzI41jzcJ3%2FQWMNSu8c4GOqUBooC%2FQ3eeEhITJQDuO43I1T%2BACYukKa6rfBsgLqZ7Sru89pvPTUURyT2OKZrmWp3a5OU0C79x1oUHv9E%2FWQhD4fL%2BfXhPE%2FD8EbwEyRvuNh0q8ysvdEQQqsM%2B6Bt%2FDjB4JFVpsjTz0%2FAUv%2FzPjnVZPmmwyhkzcZ1hSKf70BW8etFPgxr4h9VPp7i3jjbqkQPVqnhlicjlWgEEb5hWfIY6eqdu4%2B1y&X-Amz-Signature=c6ef559745b015dc0eaf8d416978f6e585705a3bace2228c63c284b889ab674f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

