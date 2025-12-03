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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKFSFBUP%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIDW9we3kt8mbvfPCrWHY7xHyizx8ndab8ULsILgrLvrlAiEAvZk9SefV%2FUuH7iGgd3xgs67lokKPZHzwhocPKZH08eAq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDDbEyyEgw2SQae7TkyrcA%2BLKY6bUWrdIIhsmWQKkda6HL9B2PHBu5xCxjsiyBR7E3efv2JjP8e1Ssz3iPTeHdXH00yjOogvytCzJNe6PcIHcO9WT%2B%2FVasau94dbeuOI5ET%2FWJZqG6YCWgflY4G5gM1voWdS0%2Fx3Bqdr9c6V0XEx%2Byv4h%2Fq9LFhHxlWxhuki%2Bg8WPbWlXRVm36S3dnXNZjgHRz4tCpF5hKADLBdu4FQJxvek%2B1SSST69yYIWrcKvomnjbuXdBtubA%2FTXIj1TtEFIdkrjpHy3R1cfGIKwwp4lQNtDBV0lRrVbFrnd6CnEfsh5x83nNwR1pP0f6t8MbwnoAdp423dXQ6Pqaago79slT0ZN3fHyr6%2B0NWCNIKKtf0LEeNY8fLqdfUtwg%2FhuaCCpygoliO9jLDnPwrpIqPt1nHVY358sT64S%2FMm0pQLKI22dJNHIJit5ui1dQnPQ606Izfo79YzXjiD%2B7OyXRZhuk3aUaDDH%2FCAM12EV6ROgqETa2PNTmVCO5eI4xmcE4ie3QoCnPQboiFFh%2FAw0r9pgH4Z8BGytlDOGgNHGErNUldKN3YvI2C9czsB9SOW10JDRcfB%2FZh7JKVtrA84NQxmi1IDYpTLZVwORYGWwS5HeJPtrSU%2FfzUxYsFWcuMMaUvskGOqUBg%2FaHPvCqYdwjCUKIc7UOp4iBYBWetkSxpB4jPAlWZIBKiOh72GPEUGyjFmwy4wVkdCbXO7F8oB%2BMkk%2BJtsEXJ9HHufrvJQc%2BUh6gcAsiU4m4qGhyrRkSBmTRA%2BYvob9VUfjImJjM5U4sYtOLOlPACdhl%2Fu41srAe7y2V%2F%2Bj5mDrtBJU6Z97Occh0PEZXv3GdtXhoviJ350%2BIpQJCuJV%2Fg1HwAvXP&X-Amz-Signature=4578d7139798a286efd4fe37efe272806a11affbf0395836c34e3780458dc4a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

