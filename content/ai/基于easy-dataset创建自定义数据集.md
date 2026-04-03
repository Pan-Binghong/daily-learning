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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7S3VYGS%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8IZgpeRRJob5f7y2kWydX6hRf0WlK%2BkKx9yiQgTJzrgIgR1VwVg%2FVKLjeWTkSsx0wTPPI9XMKjBs0Z%2B%2Foo05boKMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDJoXtSOhqDjg5q%2FhaSrcA%2FTh0k%2BKMIrltZL%2F27EyrWVkuV8wAID5V3%2FOnzJrm2ND9In%2Br8lL0IF9M%2FdRj7Nxffjp1Jh%2FHrWpi44GLxv1mh5R9PK9ayTz3CNdrsTE%2FCwL1FWNmh4Kn%2Fre7l8bl8S0YUU0%2FLpZXP3Wp6EV2fhKU7HLbEdZvYegcdFggO31%2Buw5ORoUzoOq3BqYxIKieBJ%2FHvNQkpNBdMLunD7tvL76lauHlbm9%2BEiD2ZNkQ36KnchLHrYDfxWp5HMrXezUWzHPC29a9sb3jAAcsdtPHqsV0mstTOia5BzsChSkJE24FNGx%2FeOziAJmJSlxe6IHOlvoTAnjQv9FZf%2BzWlRYx%2BW5nVTPlJNkRrthdX7j2To%2BNmdoaK5BwXhr1DAj%2FaJnRL7mfCjNvf%2F4EB0WoQbycf0erDKQsUOeGaJcu5drI%2FKZXuNkponrcB9wdu7CFP6YqqYOw41HsgjK0oFZmVyXmebyS%2BGkWJXNMnULj8RK%2BJec64ADKnBZkdNkZgV7AB1cfXekJDfPGXwvgFvZU3gbstZzPloGfIxPy4GHouq9GflKgTf6d5RK4%2FepXd1EB0ck%2FmAGdwfR0UUKBaCSLLQirL%2FWNuF70tph70lS2Tz%2B5nn0Bh2RMedLAhgZsYjHu3DfMPauvc4GOqUBTwhgC0mou7vBk0oKnhuWm870VvbnfHHlRZzb4p38m%2Bja1zBuSKqZ3UmaW5txIt5CQ1IrA8MnZ95tznT%2Bh1BiGnIrEZeEut1vcV3oS8pEYsnwke3Gm0mrDABeeKfffMIT1gNCJq7hz2TnVY0fFcSlUhoxIuYfqJhZbV%2FCpl24QfgQYwcHPS%2BLsahTaiFVu%2Foe4s9UsIKo3lbe01AqOKv5oF6fMzBH&X-Amz-Signature=a3195f5d7cacd23386a2733c985c1de4c420af176500beb3654e24ff2f82c7e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

