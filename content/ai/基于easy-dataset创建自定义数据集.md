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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLQAHYPE%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQCK7xQ%2BhPDlzsc%2FSLezxAsTviGDE6X8oWNDGUyXVK0RCAIgNS7LOiFylYM3c5%2BAt8LR%2FLez3jZGV3B7AduiSUoDgI0q%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDEWG9wt%2Bgc3cJZ3e6yrcAx00Ig%2BPII1Q7gl5dUC4QHbEJHxwydjEtd4FBShmtwLJoVDUqH3E7JOlmmrYPPOb2zdkteQht23bTHPXe63MbdOFf6kSba4htkrvZCCbTCnrxjsnzJg%2BYH8Q2KG1vd%2BdKLVKdnBQbNsWzD6T4p2erwmNXz5w3HNdbAITBWKwMsnclwA3SnPPjYgEuCk313Zp8W8WVyLX6drDDfd8ioZWhucwqb8NPniGxTm2%2FRxz4APZ9q42sKhj%2F21PdAz96TqW9I%2BDBQ%2FlriXs21HQxjtjV1rPeORB%2Bgz8NjBXzl0y%2BsN4Ov0itnLEnN0C5XSNjIEZybNGV2cMREyCvHpGVii%2FnMY3M%2FQd3oGZQHNhBAf3FmSuQ823YTgxtgTzOJVvCSh0G9URzEnS0Ygs4I4ugM2YkG41bnYeEQWTan85r1jMW0ZfNeFZ%2B%2BywnkMwBKIeHB6IiBM5cnt%2Fbm02qUZgpxx7OFvOYgwDf4IwlX0wYNmldEvRqbdZGeLFMNEDH6FtyCfS9f56b%2BklGP6anZCDILrLMRjbu%2BJz%2FwXQiFC4S1sNFxPDNxIQsVQ6yzpWMVzMXLHsDwJXVwJ5jhowTuG5esHSAmUbbj%2BAnQ9YvwTwvxI2ponE6LoSMVDgbvKGg9YEMLa5lcwGOqUBqTRMjDpDXkILsrkrdmH42g1lXfIgi9O247skiTWpPJsYVF4k92fdKE1%2F39K8emwYvHbums3U7tp0tbO6tGxSic3TSA%2FbeBjAV7jiXBVAtYUa1h%2FdwzTcq4KKlYdTRHlr%2BgWacIovzNkYd%2F7YDfJdar7wjzu%2FGDnBalvgBIplouvc2q9k2sI3OHXCsy2gKyMlyzj9tCUIqpgd8IXiAFL%2BgNi%2BqxyL&X-Amz-Signature=97136341524dd88c07428a470e70346320b959bc6089133432ea1957ed8c6fd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

