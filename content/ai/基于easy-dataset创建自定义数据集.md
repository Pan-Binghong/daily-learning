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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSI3BU4Q%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE21R13gdOCCfNe7yB5NGg9l8A5hUpkMbg42ery%2FiN8gIhALFl9YgZy5p4JDyOf33sHA2JmcaTxC50HBrzgRhOunHOKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmgAmmMoI3DJ1YDEkq3AOCAuHUGIDlgy5UAnHESXeyWHTUpbVtE99Y3FHFqsVjXXRyYC8rR1apMLe8TWr2fJuYW7iOiPfDaOqt%2Bc5%2BxpUA6zrUBJ5djvH6CgT2BgeRjp1MWH3%2FAa9Hxi43DNksN0TT25VVtxleRG8tnq%2BI9cSk6dPp9GTjlI3ew5u7Wdz%2B4SKupRhjRg0Ejev996JvUO%2BK37B7UZSm%2FsMWC0v%2FPUWCUJ4C%2FVIhDub%2FIzGMgXUfds1s0hlv4s57ETk7kS1Uaa4E9zh8FUUBdYk%2B1RLbqtZqFoLlK5SN9w8LUJWt1qOAEleseAeF37rXKhl%2B5xRZNdy7F0oZxvD2LC0x4cdsi5BiZPAu%2FCR%2F9pBlbC9EfO70OnNLl631AHoSPE6dWos4peh6E11njKqj90z%2BpgYK0LIjWmStOvZj86IGKE0uz6FcM52Gq%2F1HlTFIYGO9x%2Buy62U%2B1VfwyOcdNv8MdkGC%2Br8JeSGe6VVfvuLrD3AHvfSvQ65cxFuo3Uh6JyipYrY5e4G1R%2BPbA6pbGAzWToBMO2EGncTrGDHNYiMGxvCWAr46ia1wMfOhuqi%2BW%2F7p0onnfmfQqKSlYe7gVflfJDnpaXYBXmev4iWc7kKz0cngY9iFzmOoi72Huc7HfCOdGDDky%2FXLBjqkAe50z45ovo2ZqLQjir95rQe%2FaiFhj3klGhTAswvDkXFlM8hK%2FTxkzs2xd%2Bk5mDbMv%2BG5GHlRTwnpqiNM9APeUgSyDjn8XgS1saeQMj5Cy40VWVAZN8dIBJdUEe88c26MRnTUrFPHed1h3AXP%2FEPnnZvqyWtsS9YZXFTE0NMPAjLn9j8MW25Nezf5cmTd4Dsl1RdeDnEH%2FUpqZWX6Qtpx5NSxnCVu&X-Amz-Signature=64f67c7240b794ee9559fbfb42c76938cb3f443c86bdcb546c664fac7af369c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

