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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHKHZ6E6%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAsHlnjtGwgkldEKoCsnCweXagYP98jXE9uECT7ualgiAiARIiklB9oUWrnajOThpD8CrqFwFH3V%2B%2BmMCMN5L7ui%2FCqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpNwiBMUd4vOH9bvBKtwDeASgLDhY8kXOGH%2FRre3DVLdzBg4ZzTo3BJC1HRf5jjjky%2FFJuQkusWqCusANR4SU%2F2PAPlfHqx0zTktrtCt2HZ6Tvy2X1mnlcj683qlbBX0DQ%2BTTpoUr24eOOKOxGvFX7kVBaEzZ%2BQms6ZLRvNW32vQ6rm7Hoqx6t%2F0EEtamIPa0kNA%2BtSn6W6q8q20RhvAAYlNcyV3yRoS0JWeQGyH1VIOYwFB391lYr76P%2BQSuM%2BtxPhzfUKWo12Lsxbw0MKrIAkIbRFjptg8GWV7hdIxaU3RLT35N44drmd4rEw08jaizUKk24Wq7C%2BHXWgokQSQPxfEuJQqhcVCdk1MYdWpKWj4ZWqoKExdqf0u%2FHpjG%2FNXQl6FC%2FdTX0fBvAd2M4h9Y4s17JXeTo6ulYj%2FegG%2FmM7gZxtEdps5LUBc5XOlZnTdAQWRBA4IuI2Bf7v7zSlMHAzY6Ez%2F0aHhw%2BzeRb0ytiRvnx1FGJQ0pSUzwfKjc0jby7GBZYfF1pJRf%2BW8ZxjHU2G5Y1rykFCt8VCCUtZfJ4CLzByuuiq2KuRXxH7ZAE%2FneqYD6Z8PevfsyCyWD4x8kjnFAcBS1mEHHShCLH%2Fmh116N8rr%2BNEY%2FNY0MPB4LBB1QcO%2F4Py2y8T1TtMkwlNnAywY6pgEWZZtG61YvjAM9%2FnzF%2Fd9ZEaUUVkAWUoF39WPYqnROVwYAiBXu9SvwWyNE2z0y3tcomUftRPcDWyZuqeaUxNmdOo2BDIeVAiXuuHJT%2FzU%2BREDWXmVKNgfI2%2FquFhRNRWcZiM7AQ6RNaC49nO3oGQPCcZAqBfWIg03cl6%2FSPPoEFh5i3cIhKXvXbh1bIzFVuNi9bfVMj7yGdrB%2FwzMnoAN2Io4i56jJ&X-Amz-Signature=42b3864a7ac8123a89f31e18b8f311f25d70dfdc4a26cb1baa84d1578ad613be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

