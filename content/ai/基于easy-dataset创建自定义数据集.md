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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7Q523D7%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8CTz5IqI17UC8fQxYea8ilsTuXAw0zGUeeQmFSDB3igIgYFY%2F23jZ4YU5zV%2BcyG4xgWTafybZ9VmlCIvM1qY9txcq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDHGHJEroJbY7ScqeQircAzDDKq3Etd7CESwvhXRLFR7DlQVYVTXZgcewC3NPwGWfXycnzzN1GBwrwiHqHvh6XFyfllFkia1gGfbMqsUHTTH%2FKbzzh%2B1Q1nNLgUJlnOmp7gHdzGXtSQcZs8MH1gFspqjfwF4AptwbFVsrpA%2FrJ47UvooNOYG%2Bi8Pcwc1TM8SO%2F9hP%2BtpXzMrAKNWdLtla4mxGbN1Sv9OT6sxYb7eh0DnVZtg5K8%2FPMDmjfQMiUCjPxxfNNffFdjWkyatxW%2FH7tybqz006nFwVVCgKUU7CY7%2F4vKKfxlUTnSvYCwmVG7KsZd119cKN2VkXdeBb%2BeAaYrW7JGnT5pejfaAXrrezIM2MW%2FuWlzJgKApVxVxHlmnoYPXhTONjQS9%2B9vG6B58XClxrfjB1XTVhWFKAtgktWJX0CPR8Uwrgz4wJ01lAQzGTBrQ7IpfaY2Wsz81xBMr5ePRQJgqwj6%2BEG8GdL26ZaGvzC%2FqXF0RJA%2F2chQhURSgJRAw99O9Dwua0ZxiHSbw7r5VsbmMmo18gKcnrt5zgSGkSjtSHpg4EiJgZMfjCsArWGCYlQIQ3yCHN2qmIUPj1OQwh1HYbOdo0fhc%2BCYRxBnS%2FjXS7unn4N%2FQtOwJrq5OQJx3%2F4egiEMjX9te%2FMLfS4MsGOqUBbgbn%2FQUVbLLtJNhWZUB7cEviMkhAyxnRwoWSunuUnwoDKm0qrrpvzMqG0nX86rL2cK%2BLsLEXYHY2QnapcWt2OwJ8MIddjAiFHqiSqhPIZ5hVZ3o7LUu%2BujPjNpASwvbNOIlWpsc3BWq%2BlYGRcCWPDHOnVOueq%2BNtwae1WDo56zftBoGML14u6Uhekz0gOLKbfi3VTPTbEax0YthRwc9d%2BKrrGu%2F4&X-Amz-Signature=51adc3e0f0ea46c704e9ed41a97e1564f9adbcb44bbd0c8c02b9538fe7689c70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

