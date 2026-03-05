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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZSNUW7D%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEL0c2dtiqfYdrYuKEAuEI7K752OLj6VlK%2BLRHzv1rKRAiEA%2F9lfjDl5psuaPw6J7iPvuZjQhPToR1DghNMYZ%2BbE73UqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBh%2BE5%2Fk2R9l3fXkoSrcAxvHdJsqfJm7el6l6lzYJjadxlmg%2FpcAi53QXsIjJPsszNaZv4B8mDWfjpeOqDql%2BYUTg6hc7rhYsJgwDaLAiom7Dts%2FNoH4E29MZj7SoQ%2FFFXnw1NTgkVLIhauxQD99gH4yWUnCE50lbvqljLbz0QKk6FTKDbjgmWTkVwaoKzUqj48%2BsaPan7ySuYE23VHuvpY3ir2%2F9j%2BV1kGkDiewr2uNA6gvcnoGi913EksD0IAk5n2H8XfQxoygRjP3bZW30%2FMnuhCFQ2dNu4itW5yTlvl8Hmzg1zkrNThPlmaJpKRpo%2BLFsyjwQLI0DVaDrzzTkvsFR9T61MhZXM3jf08tzaCpDdvG3VQ6%2FuBMHIpIPP2DlI1qNoBu74rcLrB2PQzCQ6iPg1FcOZILqv4fR62fZBg700S4JrQ9NFKUD8EWChXxJk021M0%2FOH9o4MQOieysKYZbYhvUG8HzeTKiLpDcCs4GOrUTH9IbHaVdXSZJV6m4csQmiIG6L6W6OUbwRRE1dzvrjrF24NQ2COwqzYGN6%2Fhfjjek%2FiXhUkU54YdT1ZtUH2hsHOWOBCHqAKtv4S8P%2F6NXrdJpV1qriaBAwzFMu2WUU0sW5EdNMuyL851CLGatqbkkbHu6v5XGJS3UMKXfo80GOqUBDS912YcYnCDp4Za0SZGf%2BXFWCAXCy0Oi4sTE3IXusIbR5Kf1WPzzmGH0Xds9R98kwC9QIOrOVe0hp5DaSaVssUwiAQVwetf%2FL%2BPKF25X%2Ffzow69NwaNkVcfrj%2Ft2km7bA2ttU%2FfNW0qYfoAazYGW7TKheNlrZjrQ8puGRii3QESadj2COJn9Du7BuRTT0Lbr5EKsoPKeqz7r7D3gvs8%2F9nKmpYQV&X-Amz-Signature=a4ea5ebeed16db60e4ad0f7e532dbed5273bbefd63da559957e853165844f554&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

