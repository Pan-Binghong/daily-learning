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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675NVEORN%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQC4NZECVHwsQChDo53xDr14Js%2BcgyAdaYlz73ssg0HMuwIgUbOOBF9E6SNRa1UhgzUBzxsozFe5ahFS%2BTmUORCXtZAqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIjJy1yAABNE0bfSISrcA%2B8e19Fwi2dQO6QglDstrMwwCURDB%2BZ7tssTbSO3snk%2BC8TtfW%2BefT4OyzlIrcp0X5kFkcK2A7n93HZ3nipKfvxpKPcZLNoJ1yzDiaOwlFBqtgHRsV8f9wEc6dUTsoR6OGANKPeE9xIgXOwqk%2Fbh%2Bn0rO0uvqc29cB22l%2FtaZw6IzS55Y%2FPMXkOo4n4aCr8xxgNMi6WB1b%2BHf8UqXYN7hQlKH58N1IDyDl2FI79zTp14nK%2FlUT4RGtPle4zM601g4EBiT66%2B0bAFFZ2xi%2BNweMA0Ia8LRvchHqaXf%2BIQR6WWyEjns6qON9QQ1G%2FyyF63BAMPIzh0zrAqJhbGH4Vxd2O%2FEughOjWn%2B15dH0vGv2%2FRxy8NkHCMPVSzIrNt%2FGB%2F5cC3IL4vJxCM96QXbrZZsl9Tdz1vyWZN109f5Bnj0gqTKAmfttbE5pBHMcuf2%2B%2B0POB2A65GSj7i312h%2FHYtZeQETBiAatl2CJ26WZmLViI%2FMk4BX4k%2FRf0IoaavkeRHYM6A3dB5htJu4RnH1WKkBZVilm%2F4lBRtKTUn5EcYjcTe%2FcCyoGz0ROTkQEhQ%2FRAt1TbNHhhIWFtbTiKZRCh43i8VPAJMOhxEJ3DOxyvwcmRD1740JxA6LRjZePF8MMz3kMsGOqUB1Lv%2FRaocJc05kuGpfhwwVOEjw%2BBFjSVMxL8W3SBQmoBsectyTroK%2F2jcQTUPOJPL57HUryIfBeDgWQsde0I9zMgK3iSKSZzbJyr74bVNc%2B1iQdi8TUDAOvVsG4grfnzlEL8SYkhmBcDXbHcYSOmJSTAcHFZXR%2FDyeh3HV3fZyCblgQrN3GRQbAmHrn5Xo%2B%2FeunWC1xwYdV7yoEskOW5VG99TUuQV&X-Amz-Signature=0970944f33d615b557be477daee0114a6ef5b1cd05edcbfc7a8f41d9c3b17cd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

