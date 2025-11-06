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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNYVRNQP%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDEUEt9mzCWDke71oLQOdJ5XfTRn5WMmctvICbMoy4SgAiA%2F0yPm77WGj8cY5vad3%2FTrbNEyjUbnX7xaa96oce6iIiqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM8a4bvu0TrMsRCb8KtwDqpEivnWuJi6JBD9Qq6mYtRvHzl5omiRnd044o%2Bym6G0p7m2i%2B%2Fz2lh%2B2iYIsPQLOzVaAnhAwPIPA9JSqSo8CUAFNBlULrzHAXUyLS8jkwBR6%2Bt%2FvHe6dGTaRC%2Fs7Ojv1y0REGjqnDF397bTU1yUr4qzY5KDVhw4PUBxtdt522Le7pB8tW%2BJdodHbNZVG%2FwJ9HsnVrrAnxIjslgA1Uu2Bqs0Eu8AZMHnSUECrMgagYzPveVgeDCRJfZBw6vVjkQcEZ3xrVWxTIBiEj%2BmfJxxzDBQ84hQwvZTlpO%2FJPSGnV2BXBYAv3sW4abDzzcykq37NbRQ1r1QjUDIXkg2b%2Fyd8eRjUC24pUiP34lJ5d3fXikpviF1%2FH9d57cX%2B8Ub4D7KPWDqRStx%2FEgswqimF0sY8AdUtZIgdXuGrVgTuat9m2hkALBr5ryOjLw09vizmQkQB4vzDVcq%2Fu20aPSxrIo%2FBpZnl9s0k9gS8dteyx2K9TfmW7S5Usw0KdcOJRK3PJXMBASJyIgOHFdl4ciManQqRN1Q28SYIw8ethXiKLnEnf7DyXVxbc8pxXpXHkjH6w%2F8Z61jFQsCrjZlCD64VApQul15zIZbNZxBH49ELPF2qOwbdUG81t%2BY7%2BcyNBF4w2vCvyAY6pgHJRNQFhvPBoDa%2BbZmTIjqdbIDYbob73YyQeQiPBMEcVHK%2BoIxb9BV5oRQifApGAkdrr4Vc2kGNack8y%2FVlGxOaVxqLh8fWbKGgwSrF9oDzxzV9lydBpd4Zk8LiVkUkMgreAu%2FDYrx65G3G%2B9279680bJ8Qjvkv3TbthKrBLm7vAcAYs3XVW8aVIjxR2tJop7MJv4DQKy6qvko6OXx4iWqquPJLMRMc&X-Amz-Signature=66c7a056f31f8cc684a23ab7a287cdb23224be2ae3a4dac9fa31e8c26b0d3a83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

