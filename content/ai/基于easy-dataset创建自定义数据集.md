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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKYV3KZE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQChV2QUt6W%2B62wZGxKwP8yfSxkkHUhvHNSkA41bTA2wuAIgOHyk1NH3THfJr3AuBiOUme8KAj38szBvqdXm3GMw1WoqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZ9HrYtEcYzBigltCrcA%2FMj25%2FdiHBgw3m8ruP%2F3AX1JPDaelP48d%2BdOEyjvyQ6j5BQkuDC4gTaWlq8HSbrKe9s8okueJumLsbarUuQ4IU5ka4JDfCranIMTv8RplQAUGzdxVflejC6wOvXB5R9j3DinA%2BM3pFza9vmd3tZkILaU3r%2BgKBDQkK8qx1tjgY4u0zWg5DaL6%2BTS406Ni4jrafugDB%2FpT6BJN%2B5nmiv9Ijv6fVYzLlEowUbHY0MR8sHyz3Tld%2BfRiSRFEYgoFlGtxvTqH6xE4%2B6%2BUIJztAS1F58XcfyCdeVr%2BCDhZxq715%2BSgxWitLHvQI8Z%2FODY7tOvJUV%2B8mwxcnS%2B8cBfuW70APv8sTSXofKn73PvC0w2v9T54RReh%2B7EWHu5eN%2FemEFIOi4o5fRARst51WnyX%2FbYJo6c4WsvqQiI2G4PPCOJgP51dydlcc6N3lrIvJibCyszZwkVd1Ow1oTOcyjYo7e2Ij02ttl9TgU6s4MCHxLk7mKmhUbV2vS6%2BGVcjmCLPB1iTvSi6yvyGHdV0MXqxZULaozW4mSY9%2BiIW%2BPhF1HQC7ra22KDBDkqfKA8qY9vPXTcVsOViefkjKf%2FBm6TfgoaSBG84jOesUfz%2B5GSrKNQntJTLHRaWV5CMmQLhiYMLPyr8gGOqUBEehcevlvObkJhBcPb2ZOBU9PndnhhBaINrGM4Wlaj%2FiFhZ6GyyPZ6LOC6pvJQYkq2CoDKTWuKfw1kXzVyIC8MBxdgRSuGrrMDd%2BwKUH%2FmD5jYeN8emGkGld9YXU97Iaue%2BaaDr98wutSyDEp4J9mmteJOjmWkCZ1tI%2F0inPfRJK5IsB9zVnZdl6ao%2BclgzPO9OJbWm463J76PgjE4YMZIT92Rzb6&X-Amz-Signature=fd2112dcb2607046ccf61c9b20b42ffb07b296670154570802c2b9033f0258a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

