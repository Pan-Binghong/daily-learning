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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EYABLNI%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDq7ZK7TzmDzy9Xl9JYuE74992gagGqoQzcRA4wMHE2sAIhAMPVlcku4LmX%2FS561iYz3xEyqYSQ6xz4CP1OujB290ojKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzoBhGdjpcvgvdHS9sq3AOtUkT44PZhkWSeYHFhW6Vexihee7cXAw%2FYm30dvX8WrZvOS%2F45BwLvMjyk4xq09c5lFSC0BzHgLcoHwy8XMhjHQ9WN%2FKKDdmVFqT%2BCxBw6ftF19WN1dYqQH6fguI8F7byWdSHqLPQ5N%2FAWybn7t0THkV%2F9Yp1UpkwqLnP5XpmACIFkf2HeXS%2FbWWe3e2Et3Zlpc5oFQsiubrxiImPnAolbPJh0HxHi1eDZ%2B7s6FrD1rtexEoyHsYqpNVwfsMgPnhqP1YiSeJ03lC%2F6GBJUwMpSIs1hrjKrFSEwo%2BB%2BQ1GJrdx5QlwcgSxNm%2FlhG32IMz5H5AhxnRCyYp7ZQi%2BUw31MwfUsShtwo0As0qbfYpqY7qMaRsxqazyqPqrfLxXvN040sxAZfeYRpZDrqoF1sroypiTeT5J5wxi93ZUqLnsLkSD8lI6cEcHDeKil7QI1lzyVu%2BlfLDHqSOjBV2%2BpDy1Uo0vu1B%2Fox3xcb%2Bn0kffBW4Pr0HWaT0WO%2FTUtMZ26iPlX%2FXcs0Qn3Iqa7bCYMs0FkHhFFfQUAGUQqGfDxsnO0WMuilMZ6QCCUadoAj92pbW06q%2Fb8ML2Ndb5FkYzmZHuN%2BQCF7lmiQnu9xxRdKoVSwHU%2FL586nUE5eJTH8DDGjd7JBjqkAbGh7dW%2FNJv5vj5PRgRX%2FHTSSwK8rLSE1BNO6DID8kptifKvPOENFs9%2FKdfholSnjjRd27Unt1dvtctjffR0LpdFKHLEXBcR6SK20nGg69LhHLfk1MwaFTsympYSEokGOFTQQGs9O6x1aErwi7wrDSY7CVHpB%2BFbhCV0TVZjtxY%2BWGzjOmnKh0BA3TrGZS%2FjfBiKdhQiJFzRVuI6ZMJ4Xjh9vEnp&X-Amz-Signature=00ff24f54552568ff68d14af594c46024864f3226fd6110d2961484bc02fd662&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

