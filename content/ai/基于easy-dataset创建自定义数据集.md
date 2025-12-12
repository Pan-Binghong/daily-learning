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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSCUOWHD%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIGA1GUIqI3Vk7Xw80NhzX563ryQb2K5P5nt2GVCrA2pyAiEAkanlYKjlCzWawF5azFDPKZV51cpoteAWeeEkqAQF5fQqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO7JWXC%2B3WOQnr8%2F3yrcA1HEGx0wIMUtUes3bOKmWTTEEXJYsZY5jpF4v0raFXjaOeguSmDv0Zpr1z5N%2BQwLTcyeKdX8nQDqdDAw7SNizTturLcV%2B3GYZZyVncyL2%2B4%2FNozqntOsheFaQLhj%2F4GDSFAtvvllcXBHBQpjup2Ryc6he5WzqxCY2WOrQ0qwpzvH2suV4YcD3g3MsO%2FEMgJHDYGqejF7yRWa7grQrE5%2BuM%2FKXDcW2PhqT26cw4mi4f8ulfRHYn8ih3Q2SljzA3rwYd%2Fa4tfvM9eF8JX%2FGQxfUSsgVznCdXhns0YbNTLpNpTzZRpcUB3h9D3JDuYzDziWOQUfNA5RItUJ6A%2FZBMG%2BXaSDhfjik%2FSv44DfLVEfmQlt2fuRNPM053P0OuD5wDGS3J3dwV3BD%2Fy3waPXgCy9wQYFnYGgupHMvICCT1ICNO%2BW%2BfBTjAute74iwLAVu5DU0v9K1QByBILVaOO4%2BCk6noST0pg7AuwDwHlEzlxVXqbijlA9wDuDCwEKXqV6Nplp2vJ6fYyHKyi5havZ4ct5NDKeHSAkfq%2Bkzc6z2DILKkJJoyH2arclK6gMs80%2BHfDMf3PQU73tWZ%2FHxQfVksspBf8Q1NASTmEOPegnnM3c%2FZZ%2B9Qkrqyb4nZbeT%2BmVMOnU7ckGOqUBfBvsHqB4SZC%2BtgvrBj7gAGqCHd9rxNMDpvt0wmj1Ygi2BW01TZiKlSCJQnKonjGGiHhAMfr4VTkL6q2h0UVawDDqlYMJQDyKMyiOVrLd43ZfC6nss%2FhRuxhxCHZP9lu3Gnn16JZb83YjRYRSijXmUx3guuky7NXyr07Dmfu7IgXJZPgMzdbX6O4EkPqE2lL9D1tdCWUfodwknHpxOsT9JzKYPKJ3&X-Amz-Signature=77e87e01ecd94a3adc96fde69f0721f43ccf0ba188f7f6b704d800b2b3a78d2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

