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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HVPLHF3%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwqRhSNvbjcnR%2B7eI20a4N8xhvv4Tja4c4r46aF6RtpwIgSvD%2BFRfAQBorsvHxI%2Bri%2F20LPe%2BcL4cJWSAeidU%2FXFwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDPFjdhhoMS045B3%2B9SrcA91uBTtBV%2BdJjgRQcVn19zijb%2BAykb8JoEx4T786XhxqYE1%2F1w7794LxLHQGcvKIAuz9F1A0Ihxu5zhaLdMaDwxqGSrYEy%2Bktif0o%2BvGGM6EJlDc9hWWxI9FMxRCipgbxbfnh6lOyMVSqfliHM5RsDC4NZlI6H5AyiNCIS%2BbnUX4OBRVhtWT%2BLl2ZgdmK4RiFNeq78P%2BoDluLOXb7PrVVuaDxpzhBDm6XS6QHA4yz7QMJjqvbEwc7k%2FAJb4DLP%2FmthyYtYVwi5M8QjJ1V0vRboUPgnd9pw3ag43Bn5KQfn7bKuBDOtLDc7fipKoWaP1IHPVBsinJrqyOD26cubowDwf3M3UHlr2PxyQc2UyuCQk6%2F30WKLTnY%2F0Vplav2QFfrzaxmX52ZWkw%2FBvtdAJkQsrToOB1w4JUEDA8w7%2FFzGu8vwOcUeMDsf%2FvFNinDVu623AwCP5vjHk2OEeECCpKSjQVBvaD0YNMNNyKXCALe3weDaEVEZp2t%2FceSqA7nus%2BC9nlD%2Fz6WI0nV4Mcx1EJfBVS%2Bt2R2Bm817JONHc%2FxipZOZgqXDRAYA0W3EJioTfzj3Ih74O37jzPckI7EhB5fnTc06mu5DHDv9qJ4j8IXmL%2BjQnHYNv1B54BwzzaMKG7mckGOqUB4JoVLtoFpw%2FBiYnGwcq%2BmpRxupu1uHED1j5wKt9YxD2YtCktfBzmwHgUKv484KMLEkGIfFGgl0r4BE2B1sLfM%2BeYMDg5vOx7%2Bty0%2FTSJkoHnyjgeQps7v4wrOEeClgvbiQ%2BKSq%2B%2FmjJ%2BCR%2BBVRzdfHhnSNM6HHGxcQvT3disnHi%2BFlTWOVWtjE7S4CD6fZeNQ0d%2BGyivqgfHOlcXW9khFjsSp1pM&X-Amz-Signature=4642b5a876dadf88b51659a66b1ce290661ce0edf5dcdd84a024ec87644bf231&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

