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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Q3GJW5U%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQChE6zDZQ%2F1%2B4OzjRDOv3UrIDOQDPw2cdy8KFo5U6yIywIhAI9frlHUhyy2HB%2F4ULG%2Bm%2BH%2F2Tga4%2BNd3NSNHYNtw%2FhyKv8DCCwQABoMNjM3NDIzMTgzODA1IgxYiPFCJ9QESk6yecwq3AOzivP9Xs%2FV2HcGSNh4p0IU6SBz%2FuGfbUCsF6%2BXp8lUHNGDSTPNxnW%2FIwWSsiaUnNs47Npm5T0DpIAF6Lpw%2BVhtkOd9iMOUdnKSFrG2rfvsVksqknG%2BSGvl1Ch%2FYZM1lHjAbHpVZwxN4wfPVIkLt0nYFakj%2BVsu%2BRQlgkjRqCpNvQQDX%2FUeKHEmX668aELe3W%2FpfUUbiBSlfSoD1VAmQNXIvT5Qde%2FZvgSGGlcDO94xXrHxdhGlwH32gNktSOil9pV3QSztT0YRpuIc1sVC0rk9t1h9VxTyh12MwvIpvc%2FZEOMsg4wcTTmtmCenSpj899kgpaF63W6cjI%2FZyrdBSMepsUSlociZ%2BXCqM9DlQu%2FHfwsYtjO2KAFaexEDIczYhGhzheD%2Fd%2BX8tVMWnZSqskKXDoSWw6KrYnVC%2F26X6b7nHJHlMdJVOJXxRLweR3wm2b4exlnUM5VpveXkpjTpiRu6sMlocCZ%2FEwsGGLehwhj5BsR%2FmwTPdfUIX9hMdtYa1SU2RUXm5Cs7ZTUSkGYq3q%2BuzoMyEy0kU2S0NGLfYWM%2BFImPqjdWdob0EtdKkm4ilQ3XCgo9LF%2BLy9xshPxgU7GG2JTDp5ez4m5W%2BbhJoklXotALSAxZ1A%2F1wW%2BzYDDH1JvPBjqkAYKGgUeIh6yaS5BEjpj8lY4HOqL%2Bz2KlfxdFp8CJKNnFpk4qtaVfRUkNFT9CtD71SkeUjRN5YXh7A1MIrxMiBgV2t1W%2FZVyi%2BznzYhTG1IOhEwPkBp0BRjs%2B7mE6vv1zgUpDeMoikC3Uxgsuhuam4hbWWCQ%2FyXfVWspO59mdLowP0aNS%2BkrgYgrh7vFGm82uArmsbsJ2Svu4qYij806HjECqbpfe&X-Amz-Signature=94b295a8822cd1e051c3f8a5b73b2f6a4621c5d3d2e6ac26db37d1ae3f23eb17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

