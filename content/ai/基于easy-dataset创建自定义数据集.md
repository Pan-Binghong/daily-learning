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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPZVGGDU%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzvzQJIiPxgObuDrSQ%2FK6jXFbL0EZEXKi14xCbQrm2LQIhAIyFqTItrpX8vxGV1i9%2BURT1usYoxRkLLjBjQPulvlAtKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwf2iPZneWV7gtSKpQq3AOJb4VuE1%2FrVYZQ9poYddsLYO9IlB9q%2Bog3Mnm2QrwdcJHeGN9N8mcWD39SlWfVlmTX953dfxA2TfB1IVZSPANgeodFgAugFdaGI2hwoTINQwWPsJJUiYz1DfHX9WZMxh1BaCYP35Br3muZzbNcXbw8F8UOcMFAfezbgjqHbn78tskJUWFLB%2F8ZcRXwXPLAStXQOE4v%2BZd5BjRmn4j8OFlFTaR6nHbb4TR0WjyyT341H%2F5NG7Ug0VtZF0aWR9YedJ%2BvWURj54t0YNWyz9ufUYV2uv%2Fr77bd5%2Bi3gCGzjR1S91JpaddRdhrzUHX0ecT6b5ZqAFGo1%2FLkjpJgozf2U6vodmerCzQFscNVVlE35uh67G6nl7KDFJ5HP18sy95MXL2wl27OfaiIUWHiIQQ%2FezVLHEj%2BKmq4WyLKGDZgLOYqZgjT%2FlaMIhcKyISDIpHvY5LdsXWibKoEk%2FB2D%2FA80NCT7MRWeW2nN0IwuDCY2zy8tffCnKCkkA5bRxY9E5w2A0H1vHyOvSbrD%2F1kksMi6TIJqjX%2Fip4keQBSXrzlD63ws5tFqWWXABgd8RoBe1znhjIDuim%2BeGeQ5hGgc3cGEBDmoXfxYzHLZbj%2BdoI61%2FZk%2BQNyNn4HXezePToGtTCDqvzKBjqkAX2WTi%2FcIB4fimjkdyWk5v%2B81N7BvSRr%2FUHQOvqp%2FgFeXvlIVZ0D6tD5t6KgQahu%2B3wAjCrn%2Fchlnc7OsXAOMHpGnQvN%2Fx2A8QIEK1H%2FdWx3onQOZsQ4wQOfmYyBbwLsCVRFwMKC6VXxByP1cq1hupiZGEPKe6peAfdVS8e8d8YII%2Bz%2BWcQHSWpgCsM8zcwL0g3ONbSoDe%2BIxeAS4cwD%2BhTfZNVe&X-Amz-Signature=077bdcd99dc0da38b6e619620b2a73a04a4f5f0a01b2f13cceb1a1434f3672bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

