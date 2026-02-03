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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VINJFRE%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQDJe8tqMVP0S8NaMg%2F7I4X41ASF6xVK5Tx33OayfLTQdgIgNcEeQQH40V7IHV7ZF178QrQ88BAA3WMXADTXvsOhM4gqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG8PEyb3%2FokUpq9q1ircAzElPxF26WK6TZociKvgLrcQ2KFEqr%2F9qKamsRkRURdBnSX46CNv63TBcGZ3wrSViw1eX4AFFa5X0ptbrO%2BflhUkLTsIgFZBkEai2hhNUSwRAHm1GmlhPlY%2FJpiDNcj8tRLElo5kwg546PlROrgkj6tFUAdV%2Biua5%2FLRNlVDWxN12l5jpuR7rG6TEQUYK6ueInzjlPaYiG1onho3mjgnWcGOn%2BRxSqzjyoQnPxxLokyZdPHbxoLLbHfLkE1uMuyMEWmIovGNf61uOJdGJD%2BFWsyfiJgsKikQkQqX0aX9oDCE02fohFn9DvrjscvTk%2F2vYdAjANQMmemC%2FiUepCxKJfIQaQf3uCh8yemMUkT7rwx1r8ZniQg1S%2BPmrP671zsCkyMk3bRa%2Fr8KEZEbumalmbaBznRo3KoVOrSA3knRrZ45LDjVnoJe5cJ%2BqLnKPvPB%2BKFTP5Z1uEqloBEL8Dz5k7lqtoFpQQelM5Q3jQmzFQkbesAekk%2BwxYTUMf2y3RUgbrusb6z%2FfDdUSjeAL5xNKR5pdXc05ivoufjzhqPeHs40vazXNGcQgcOuh6PKq%2FxDHXl%2FsmDlrH9P2iZkKmaLuONMXh9WgU6pxSpOikRFijwrZbVoZz8yZmmDFiQTMLvYhcwGOqUBJtlBIzRWRlmP0NvoxD6rZ6TfKO2bhPk2oCR5VCgwDBXfhpOcjfzWi7EB1CrYU1a%2BayQz17jrCTFGoD9yM686hvzlbKMNR9BYSfWZ6Jnp8mKHxgxfnRwY1pi5yfjU%2BpT%2FxvNnx08FM%2BgO9FCsXKDnQTlegIqkcP1nzpf9rROrC%2BhVDcq%2FWrvdXFwbfbKeDDqEC%2F%2BjhoCt1CQOq%2BZjoJZNE6utw1YJ&X-Amz-Signature=8aa594e5465bb957e74fbcda6ec047da92c1fc86ebb0a11253da2396d9f0eae0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

