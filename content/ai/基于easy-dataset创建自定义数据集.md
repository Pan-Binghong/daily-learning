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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFKVAXXH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGKAnWLBFfBJDDgFLH6IccIoK5Om9kWPv4T7o3ydIMhHAiAN4D3l7Ioar%2FjjJCZlPYyWO1jJ45uMwS5iGWfTOL9%2BRir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMqbPZOdfsH4AalfF4KtwDvrzY6ghL5qblgzbhqZesqFUgGdU1ZDJQltW4FV0cEfbP%2BDr1qczqcY3Id0ycJiIuqpBIf%2FygavXOEP3toBUXtE88efS%2F4zCJKZNoV3yaDSZ49%2FOpaKfCd%2BWW4WSrDVRKVO%2BwZCQyo9clt4mN9vTI2aNGyreIC6e2SLy5CVHwfOq1N4p4XrVwNT5%2B3VOLjP7%2B0iAYxR1ee4QkKfdq6yi6SM5uMiUOvh%2BTSdnWu9nSuIKZRhAcmH1krDK2JFzA%2F%2BppLuLMwVWivMQQG3MbL7SC7cTqxuHbXEWqgJMRAMlQ%2FXS9jINFvsTrEW5YJWK0RS2ZJptQ1NUl9IiHndXf3UCy%2Fj339h2hV%2FJBPHdAB5Kb%2BMwPGgjLCtwx7QMpo21Sx%2BbUdJfTJ7e5w2jloyyaTNi8ngdS858A5LXuxR0%2BIUOIhRVMWeytFL7YC%2F18wlCBrLYP7Hf7L1asI8iuncC2Vo6AyTTH4C4CkLuhd8FphQLYgZq%2BSaiaxYT65JAsjboJ25x6Z0ROMvO9hSpg8KX3hsdXiw649GxLlk06XRGQa%2BzoFvANAgNia3ereOU0XIsW8fzI2%2BDFXprRPKMyaqgYSI715evrFW5sfQzRiV%2F64ilMXKy6ABkCMhJ7MdgWxLUwvq%2B9zgY6pgFuWVshKROYDEu4s1Y%2F0UUnbTbxpkBR5VRBGwmjyBdVAePUL4t2zlAVQpuXaDcYBXl2mViUlSpOI3EOvLzAM6HIKySCmf0Zu8b2SW2ATGWBXt6D%2FqPFwZTUCkL6CGZ2oFqu5CiojkOITovWV0CsgyjKWIP9Sa4a7iEG3IuSxIH1HdORVNDNwhCMn%2BxDIiwIw2dy4rEmbkkvM4Xlo84Ui2o5T98aj83c&X-Amz-Signature=cb77bdd978ef70dd0114dd7abe3eb0b4e822644f6f666b5b01f248f11723a9c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

