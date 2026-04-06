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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644LASEA7%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICPcQsgsVVSOMHRSLH93y%2B8CJ3Z9PS6jzLWyWixv8rgHAiEA83w0ExMG6dewx703ktigaS2UnttMUqSVcFfv1yZ6OfoqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZuhmTh%2BMBBuhASjCrcA4%2FUxBclx7DJv6Q%2Ff8PL5Z8ARSIV5OAr7DXkdsnT8S0XGtQfgCQIZsiFMRAzMILdcOoddvE3as%2BSeAj%2B7zh7mEQs%2FKUM0XCNDXdvfvQebCifxvdpbDOdsEf%2Fd8%2FGQsok9s1dquoyEcuBJWsWmg49kJ0NXIvUity6I7UQz%2FEQb%2B7WkYoIwmmW%2BjliW7vTARjq9gnGyJSgroExRmEXZernLCnbc%2FxGdXJb25v6o9NsqgjprhzHgKGtC%2FbSU9tjw84kP4BQpzKpvabs1rxm1wLwbzUmltg3Qs%2FVi8qWHOb12XCsHBxVpchjHYWObFUL6KaVdG15hahu7o0ab2l%2F%2BYQUKGrS79md0O64y47VMsMuQ9mdiV2WH1t5OKIadOwEJhxyUpKkCs%2BMZutbTElin5WXWP5po%2FzWK4f%2F%2F1lCSlb9ejy5sY05IodfGI4xPTj%2FUQj9hVUhO15tUd%2FPomWRawHXcGHr63uuxeZW%2B24xU8OGnLFQnAZON8BVWESZSOZjHCs43Z60Lvei1o3XvUdWaHloxRHzfjU1XU%2BJaBnrhDys2Y9tYkd9EE%2BE1FywmnNbqm5EQkj9kaP%2BgQtdkmLI1Kmh8sY9Ys1Sk8D%2F%2B071kBKTHXI6rq%2BuH%2F7to1LTpLZcML2xzM4GOqUBludzlgRfbwpoJeg7aZfpM2wjasiDUS%2B7LFwcUqbL5P%2BR%2BT0ZxWLQxOAYHmFc5tO33XCJqWJ3vG%2FRlACNGNEaUI0nQ1eT1TB0W%2FCSrj3b32MI78%2B5oKA2rfOMrQcEbBdk6YqGP7x2aT5oVNDDrbNZSh3UjkPAb%2BN%2BWJdb29StOFdqHVCk1Z9WmNuajUFxXZsRCmcUPCyLvYlRbWr7d2nK8psQhrvl&X-Amz-Signature=8d3e8653492fe7fffae9c58202bd3dd186bf89d2c7492c1c24e40a7813cc27bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

