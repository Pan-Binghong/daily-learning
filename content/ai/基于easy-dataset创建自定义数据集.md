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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TXQ5TCS%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF1ZR33bzhOhLshS2dgmdKOLlIOZ15IddLF%2BFBoT7he8AiAmr%2FngU7kIdnIWnGGEk1WwQwCdy3oOws2aLxjKsxzsrCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMxJJZTVAOegnUf3xTKtwD1CLJUItyBsagcE%2FlVE4eoVTOO6tQPiKN4dLWFQIixi8QhOkxvJg2ZdWOPABqaE%2FBOgBeVwy8cxFpkW%2BRzbt%2B%2FwW7S%2Favw3utuy0g4p3EcOdtNgGYO5GspLmVGZXPCzXzRCwFFY6FIWllI0bMvmN5A8dR7zTG%2BFVjn%2BZYCRnKN%2FW1nzvKKX2%2FaEl%2BxVJzv9xqVhD%2BOdpV21D%2FQ3r0YCqf0k83%2B7RETqszStkX972BOqoTpwkghsSAalETDIC4FqIYMRXbJgvh2AAYBevjXibST2Q0avapzryhomO4pdoWihu%2FsRCoxdrawBnTWpgZPEKqMe4fks8%2B5NFrC6wyeWLbczN6jtJLQ9RN0y7xkuz2iUUxfsQk0UUb9sW6nnzbEdwdZnPKakqqsGHyKCVu0RlSWwC7X3xUX%2Fsy44J0n6jizqgGYpwyAtKEQe8%2FOa%2FghlpFtvtUynw67u2vJjTHeImSmt4zmvyYmeky3itelyO6LZWJee9Gk1NUU9i2cYbkniiM42FGUmdI1xRpmKe0iY%2FJg%2BsLpSc3bTY3q09oijH0Odz6wJQbURUI3uWYb6hJvQeGoxIYdSKVHoCXliyFIvjx1TSIe5mQyA07LxEAYL1xonzua3yTWzHaUMX87r4wotC3ygY6pgEMQibYUNBW3EVN%2F7sXUkxwsDRjzrqzB1PYn5b7%2B9kHYqisBWEpqQPYjziNIMcmbjljpSy3bhk8CYy3GS43ay2%2BMi1mVkNowepbP%2FE1EsQIRotKwjbk3B53H7DG2LsbSX0wrDKmq2Z19GxyI1pbQir6GWc%2BJGWCYfp0fXWu8GxW5qmHCOLw%2B3zyVE0EBIxN%2F8wKKRwPfO9bDbEMVUtE70CwaN4jB6Su&X-Amz-Signature=88104a3b1fa4978ee4bed79d1abf503c84f4f7aef8a13cd73f20e5a544df94cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

