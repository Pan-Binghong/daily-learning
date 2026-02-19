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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CCALHY2%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDoyAZUXycTg9oWz29e3Ksgb8YvdEpeEUKNkJE7dhbH6AIgANOBc1fX9l5oyK0soRZBnW0h3vg9VWPvp2wa6xrZ8f8q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlvdmf2LLFi%2BmA21yrcAzJCp5iGz%2B%2BgUU9V8lpRclPlEO1uaXNb4fsQ4LiqwkADfve6FWHU0Yh3kd%2Bc%2BwaMgbMLwNUu6Fe9fWiQeKlErR09700nz6DJkiNCc3IQQP3DmBXwZpCmE11jkTkTb5zSqizQ2aEAsIJYebKgvehSy4tP6BCdC4AZv1c3xPCMQSbQCULmmyBxni4MhX3te0KW172dTLcAgAVD1P%2BT1pZBWcb8LVqfR05EXu6ent6vYZcVKfhSSWgRyiItOCaQxusevyU1%2Bk30kjDxSfp7ZSBqYmbha60w8HZkpRwxJoPFZ3TPRH1R%2BkmLR%2BVy6wDOEpX4irmVA97pfUpGdsZqk%2B75RdCK53ZucOXz6Vm9OF1yJta47hpDPlhY7UcScI%2F2KagHnBEhw04h%2FSvxQy1A08fhv3TkTNm%2F5dAoKtOfeROEVJ4MJZSJPlTETeSiLIl%2BVKI6IJ6XvJvRtvXqLjCzo9o%2F7z2YPURNtqIV4iaGXKvmm%2BJdsu%2B6EJsM796T%2FcEHuQfYwD4Chz2u%2FsA7oUEjP6UzWHjaU8q%2BBHr%2F44zF6ZFNjfSZSUGt%2FN1Qz80PHR%2FNr9lLjna2nPwyrun09M9UqRV%2FmQEFa%2B5BZ0ppsdQ6%2B6U6YqY84WDsEqqXgLfgpaFSMLXx2cwGOqUBpTl9QbpayRh2qXF%2FnYILgwULV%2BTruytasN%2FlGytCxkXuQERK0XeEQVIirIfRPt%2Baqi3EZQZZoD45Tz9DvVYVhv1wSZcp76UopmwRaOuaJimQPNue4wQjh814t1XQo5N12orwOTr%2BC7%2FjfirLA%2F9C%2Bu7pOKfhVK85B1aq0mcT2hobtnu16uT6LNfADv%2F1xZMX8A8cT8chhZr7LyGnaiOyd8p4emwU&X-Amz-Signature=9bb7238066d9dd36ae685ed83f511cda241ba51dea3cf48a0a43fb49113f65d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

