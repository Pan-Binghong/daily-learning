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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634BFL4LK%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQos%2Bvr8KgFowtFTb5bDLJC10rtbIwjPVv4Yp35GO3AAiAY2BwfCupthJjmMqIqBDvEgThUXnrsx%2BDe4YCFd4ahiyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2wwyL0Ydxa1H5szaKtwDbk3I%2FUVowVyEYOyabpQ7mPOHFHbRHufEDNP9s36i57f21WzUJIk4Pv2DkZ7MmAPSvGe5mt7UzJrqg47O1%2FOpBEEaxBK8MquTwJBNS5YE6qtweTigDT6%2FaFqEo9MhK2Xc4JbYmAuBF9hw9vjpcLk82xoTe5Peh6YMxbFm4St41tYDlMaQj2I9u0YehTRUL8USiw2QMpUXQXvwU0rkjashgxfHLnkCZuHatnqvAasrcuK82JvnVh3JUTqNKXoXCzJeMJrHRc%2Bv1SlQ6ef4goymBXpS%2B5RPmxg0TivKjrco8Cjt0Snr%2FTiRD0Vkdy82YRNbzYRJCzDETG9TMPYijozhcqnOHH9sreUPMAQu5vD5l31%2B4PX5tZAIsXaxIX6vPNT8bCwHNZN7OsYDg3CQYsyouLfkw%2Fqcb%2B%2FdKENVkOxIkXw%2BhZBn58MNDaQy1zRkWkX%2BjWGdKlyw%2BYbWK3GGez67TczmI%2FIuaE6CE9peGGGnmyD087%2BVwgMd3%2F4PbkpMCavGEcAdS6glj9nFXJx79JKsKTcRRwY99ztzGzZyKSsU5829nS%2BhADsWmpPeca%2FXUNuFswhWDVKFvzXHRBHB1UxK1R%2Fll9%2BkdCkgbLOWcZRqyUov0HYBbVrNk5uGIpsw0suvzAY6pgHBEc6RaVCHdJMfDL6yJhv5IqoQk%2FKhJiYTB0nybuHXMNkfL73u%2Fy7IXZpNwYE6NZsleRwBy1vSOKKs1VZplmDbXiKWLR8s2o1ktkh2CkXqsHCM7vEbbkuQbe0G%2F1FGCyP4QKYER1UWpoLFdalq1ZSmHwBpwbyGuV7EQ9Nf96IQdo%2BiA4lz5QPVMd5r%2FYWRgEFeAHX0dK99hrsjaWjLVcZb52XOcCst&X-Amz-Signature=1ad0f0c1fdf2524b1a70e65d6ae5582eb30bfe023a41911047ce17a36cc83ed9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

