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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVZKMUK2%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwPWuIZruskfXwa5cyKaq9GZyaaATd7Iy79wBC67AHmQIgWWufGbfGniG2mZpnE4ouc1FSiafPvEpI2%2BdYAZ4eBXcq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDABuSkjo37ZHNULDQCrcAwLjw0kPGPR1LPovoZ4t%2B3wn99MOAJElp4P9cMkhx27fmbjwc%2BIQUMWL4r0HVrnSzjvmBXrgUilrtQpl72Ao0r404dKlB5FynE%2BMlxDjl3DCYA35JNvh9YRXixBu%2Bi3r8JSDUYfMDpooGdBmL2ZJZGRlDbeQ9Hky%2BGn4ok8Iw1XOS%2BpVWa6g9NgJ%2F%2F%2F%2ByYkr%2Fe72TElkgsK13VRlzps3u0lHiQgf0MbTcBPMLd2MEQx24P5ld7mmofoS1IhQCJB%2BAF8ThyladE%2BxBsUIolyK2ayEb9%2BM7Z6C8Jj120iaOLHd8B5MZu8li4hoReJgEw9Q%2FzGqGtv1zIXMQdeEutdAreTI3L4Vpv7K2TNPiiMX8Al7pXld4GFHCaiQT8wQfH4ZZJlFc%2B4qrDxeba7Sx32jeNfQENwTE8X%2Be0eODWeC3EPT%2BJ0oJq1hfxpyp8waMbh7d8HJ0F78pfe6n8587fNbQ5hJ7kO7FSbSLoGl6An5nhdb0zbaZnc%2F5nZ3eII%2FdiKcR0VBRE2dEmq%2FVbGjjNZBznbHjb4WLKFbV2WaEghSufjvOrw1zk6Tsu%2BVkCrNJp4Y9TRqh8%2B18TtKInPQaHU6Se2rLPLN%2FsABcPTYMfk9SxfFXUl1luw33UTcRH%2FEMJbNjs0GOqUBf1AbQKVKSLy0NQ3hQHlRlteFz3x52xf23SExMgJz%2FBn7ch8Yj5xkK%2B8NsU0iHHZbuNfsZ3XG0kj85vgTRS2IyuHlQg2Mn3k3aGtSYci0YaqJ91tLxlTcknZ2M8O0Wlnsk3%2FKop2erEiYNvjWEc3y8OySOJ%2F%2BMV5MiTuwqL%2BzHbFXuE%2FdyYKeevuCNtppSAROG992Cg4%2Ba2hAc6gXUeHM2705bCXo&X-Amz-Signature=dd4ccace1427199e8407f4c1f4cf72eacbddec7cfd23c05ab1721af02a20227a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

