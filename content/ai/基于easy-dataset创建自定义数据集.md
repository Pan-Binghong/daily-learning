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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUSZ6VJ7%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCCfKkgAd5%2BuFD%2FkChUeYymjzUXX62Btf2E1T2SSZzfagIgUoXrk4iA1pKoO8IV4VlJcxesIc%2B99UMxgKUOWr4xeCkq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDGDBviVofs1W0In5kircA%2Bce8Uqr0HaKUE8k8zMtcUKoFRNuzEi%2F7DfNth%2FUjvZSz3eAGiqKMR%2F%2B9cQPSrZzCZMM33oUSUM3EGPIzLmNw4uDFJpPfJMUvRtbv%2BM%2BcXuy3aG3YSkxRgZvYRAoUHNTAa4EahIy5mPYXMdx0SHuxm%2FweDpM47SrbM9zuayz%2FZRN2l9bqV8wJbfDT3x5eR81Dhe1AqyEOq3W4qNdKFmtXFMBepX6i6Y4zSDDinyv9R4q0Qbf5SBC%2BIZwITD19oN5ItF1f8RJbg1T07ujqUTa7I5k0ijExaEw8iMhP7Ofklj%2FelH5B%2FLxH04YypYzxgSgE%2B0chzvBtp2fulGZfTDKYmW0Xc6QxFNf3e78uzw6E575jGORBwxNkucT7oPitr1UTE00lhfVA7WfHOOagz5iy%2FEHh5W4TGrA7eKMnfg4dcocs7QtrXWv8rF6xL9sjWdeiLmOe7a5xInjMhe7D4lkswEyEW6roszvy%2BpL1I6cdXzpxQbPcq1enmYsnUdhVgm7Ryq3WUWrPEL%2FzSePjV9NnwkF9dTlOer2kYfc%2FZH2lMClhAC495Ja%2FMAJo8XaLufgQ5G0koXRTd3nMQrm6XtnuIThTa%2Bg4RIe1cHJyUOj7mGEgkCb29iaBiKQ37KkMKC38s0GOqUBbfrIUcI9vS1i4cFZa5GRjlqluJdwIRo5yxcxaNlt0q4%2BPW4BKQY9YAeqZKgp1egXwD0CsJ3KbR%2FQMuGZQTbqFEs21ypcK7jBmbCREwvKtB1lGXsRlqZuC%2F4lQn0n4hV%2FG0XqlJhenoZ4JTlV0IHOfs6lh%2F25cyU0FTnuOxF66c1r%2BQpbmyZly1CTiMapL9M2EJJmUyON4QMn3sgxI8PiwD7pSIzY&X-Amz-Signature=08c79a6d7138292f57f6d200a45e37820c236861226b0db15656281c3c30354d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

