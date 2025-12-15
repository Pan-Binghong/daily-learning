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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YOYBV6E%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCICLBXLaCk%2BVmg%2FX46iZ6Pr%2Bte%2BxzRyuFN0Rpsw3cOFkYAiEA%2FToYpKyq3WYS9SMb01uuiVjBZcDaAddujKb2kaPDOusq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDObOWPS5qS8yYWbmlSrcAwf6a18tG22ADTEhZNhiZDfoUY6W6aBYAS%2FUY2Rb6FPawfR5jhZNCR1xSURGLbbDejQkOLWI7MSFrZ52Lzg3BDLBhvOFEUVvdq2YN05TjLxA7Tl9icdIEgmlHKevN%2BmXRiyCOsKbvLEokxl8XUjRaR1F1ebx%2Bdt1KcAIGmWLvkOLB79lhThJxEkkOE1%2BWMsWG5vmwqfv5aqU8OAhRo05G5gC2TiASFbcZz3VB8K8Q%2BGuRTHKejW%2BgKk8gDJTQ3Fh38uT7%2BefpTeQcE8HhhIIEXoYX7gofxqNfSRRKIr%2BYtUxHJ1R%2BmiLWZyXmeBuP1mhwZr1n3fsJBwRHUUE1j8hJ%2BLCY5Hk4NP4VarbkfzdYKzOsowpfFyQtw40cs4KZyqBzFvvW7uh3ELJFxlonutKTmENKaXWRfV7yuTiSsxCCHqSSKhxXpdr%2BKhi5QYgn2VfHrVUQBUYQOfNrRW6QtKyaFr9ydUU2RIO5oQezML1s%2FRM22yFAxJ%2FALpsyGzrL%2B%2FVnavbZL%2Fx28cK%2B1CB27BjzCXXgVK5iwoWP7n3sobUf7N9%2F5%2BET4WrHVRAblswWMj9RRmXMrL1Y6vhc1YKOzvDWMHbnqKXf7XOLdqVQ%2BPFLK2RlwKvFOXVXVpEpiTEMOva%2FMkGOqUB6PEjoBtdMNk0Q4wgQDGBbr3LkAKlGUdAvuOWCYskcTDjBB9zw%2FjMlDLRB%2B4dRcu7cxZsfx%2FSP8PUYEa3sQfLs57Qyuf6q2k1P%2BY9Sp4rP%2BMZ2yVef3WMd%2BnSI%2FmG3%2FbU192wYuKDp1HxOJtY54r2r4ozhaHz0i0fbmJ4Mpt5bIG%2B9g6JC4GNvkDNd8ZHck1GmXa%2BemmUb%2BlJ%2FXy%2Fr%2Brjg9Gp%2FJ47&X-Amz-Signature=75f958f9690f209e89a9eb7396cab09cc5d860749c8192d9092932d5df388de3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

