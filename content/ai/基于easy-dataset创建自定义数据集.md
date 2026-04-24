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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OWMPP7L%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgfDzg7nIORxr9AWwcVU0eCjVjBZrQyRwR6CNepRYHQAiAMx73cE00QjzAA64dMlMUAtzQZ8rROjTp%2BN2jmbC1lLSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMAeGXSzmAjD3XXndsKtwDvfmKztMDGwjZSnxPLppWx2L3SzABCHATrNmQ6sovgzSN1n%2FPVQkS5k0KiSb2AEKipDJRBYi0M%2B3CPgIn2PhjTV%2FWN6BqxIUEpUJ3nMKATe36Z9eBJvxfyH2kn%2BCJeFHKdb%2Fgl9z%2BUjYBuxpqaqw3hpJLM2%2FFYGw8Jxijyr8QHFeK1hSzE0fp3XIdb%2BXNzd%2FSV2k2d1hj1lSawVkzt%2F0pBNXpZiTZF4cMeAFjF%2BkRBN3G%2FXGln6zW1z%2BkXV%2Fqcgd0Ya5y5BxuwgqPtEe%2B3Ec56tfh%2BgO2H44jbog%2FG%2FH%2FPrK1ttSvXyk3j%2FL2%2BotMbdbCAAnGBlOrR5e7QyG%2BWVkUJBF5d8lEosmelOOLme8Ztk0%2FGfKr5tHyR5M0x3IDo7UL538RDdARn8Riw9QYeG4ZrVksbqZ32pUjARwWzXesqfIFLGZlBnNx3ZvwUQdNPjQ0Xw0bAJg4vlHjDbPbQSbb1GzudHxYsMUmnQ%2FrPeUeqm8p9dy7sPx9dEM27aKceMjNTyDvWtuuVHJFknvM9AD192%2FT7GRW4qBKyhf%2Bo5Ek9azkosmOXTOI1DHSnHlhzZ%2BUyPAFkIK%2FY6Igfi9G6gR7O8AUEkA64yZod77Fr2%2BbHWj%2BLKUj489%2FrlymjqkwpKurzwY6pgF5EOYRTaYyCMUs6APAkaaX5GOE%2BRiaGy%2FG%2FkmtJsfBybRmeHIKM5NGHHuJEiclQ%2BDV%2Frslz%2BYv1pHKTtYIEO%2Bn2qxVNsKMgMV0VnYRnSni5KvVDL9JDaOKVHPSkeh8jmXgHTP144SNsYn9WKXDLi0t9BooS6Z%2FUacjjG9qysb8LxxzGIxsUcEGG6VmjTIzEbar0PSCa28LSGP2GUq%2B1LGW2x1nUVQ4&X-Amz-Signature=590c462059126944f16ed90e3da5882875e05ff975299e57f8b9d54c36042acf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

