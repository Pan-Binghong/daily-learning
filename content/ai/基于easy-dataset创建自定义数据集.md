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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIAJQ4WU%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3rmKdLZaHZflgEe7nB9QcGcn7Sh8FmZfZTZVa80f2WgIgCDAxACytcfn8wDHaX3gFEhNHgnBPuI9b%2BKHTT7jhRN4q%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDID83v9tnBEsZIOHTSrcAzVhQdRbJVUuoa9ZC%2Bla%2B%2Bbsz1yAss3tqgwuPW9SCIcA%2F4Ax5ckVw5Rxkxwk%2FfJbcEd90nTlyrmVa4oCmvVsOXfgG1%2BVjOcRiRTOgHv7xzPIyBTh8ZyC2Si0QCt6fE1DMt7uRkMGX8zosoL1ux7OiUYrKFA5kVnybG5sOxzlel5%2BOZb65TebL5TOXMp4f8Aw9HXyUCXSbWRMRFdm6xkYGxHKLC%2F25QQqUt%2Fm2c%2Fe9ZlAnQtlNd%2FRqkVgJG9g%2FyWHmwI%2B6JwGIpQRbqRpr21sPbFlH%2BbdPuhSZ5rfcSfJwrGBMf%2FBFhh4vvSHyzxmCwSmEtZuKjZUmOu52%2FnbBynFBy%2Fvw5DXDy6JeRIdYIOuhIH%2Fz81lnHtepj9t28oKjStGd2ICNiJhW8gNJfoJ3%2BKJj%2B1jripuHyPqbKk0cK0477vxQlnKBslsNJq5Zfn5NB0ign20JLIQZlxSO8w4jsOXyrUCdwsL1StJi58F1gyboY2ty8YzpRoioqDiqgV8VjNrB8lY3vpAPwNxuqEooKO7EYF%2Btvd6Xro5dfqZCyPsAWS8A04UA2D3temk3gLLxRePZ20AUUMgDGfL0P5WJ%2BWOd1N9nSZzk1L6fE%2F0L4QA9nZKWqiT%2BiyyrrtagdmRMK2X5csGOqUBAJ%2FN7LHvCdAMvOuhcRUrz5tbZrNmZ3qdllWqJsDN34NFUokqeLYwhhgL5XfYxNd6GvI00YGlPpgkrhih0EBYReOma3wth1Gjotv%2FCjdboi8WJoXZp3UrnSnhpyd%2F8mrIHWh9xKdyYnVmzHf7ExAIK5KVWYUGntSFYLjz8R2Ud1H2wsBH96ZU3nKk9998NyTQLJ5hxv3G0tJLVLQoYGiTIl%2Bs%2BzPs&X-Amz-Signature=47ec34fa8b300ef1ccd8cc7c45117745928e0b346e0f5e047250cf014b5f738c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

