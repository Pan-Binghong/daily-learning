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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS3KZGDD%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxmfB4gpDcMXztwFCz8yFiZeCnnbEGf9%2BKEMkJGFGzbwIgO3WKrBaXCyfkufYlqQNlJnUKWxVqE3x9LqYfNQA%2BbjsqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFWp45tUijofEhD7DircA5qFWZVaQiEMPesLLWL6LDGDwERsDOyqxUe9bI6WXM099LqqdAl9WOyR1IQEYF288mqCaC7b3Qu5BjFaFXlRIle8Q1PjqZEoLveMuM3IBM4am2GC9Co9dzuyHT4T8bVQskkYTkj0svQVK77VrQaKsMqnDpgPgVJdhms%2FZ5TQ9YPg09u1CVO851RFtOf%2BvyaSIuk3vxooZwba4DYgDrVWeOzEw39mv1QBrEH7tTmqY3vIF%2Fnzr2%2FDzRzYAq4rxGJiSu2m4l2bHQVM%2FJR0Oz5vcxjJujAQdcaXFhGkE5jjWmvMTaRa5h97FpXiDX%2FCqUWTdgQ9GlabsdwRqbdMAOzVLiN%2BoilWZ74LKZB2yDiAFhZVRcP8VsgGpOTvKsIhrWXib3zvSgbPG9JJFJmJNAD4EHppyjFCv%2B9l%2FptOxUVyjls5DY%2BysZGS5EVRqh4ABmOmD0Kdxb5YtfZVvr8ZFZmZKlaf7BwLsGQBQnUXAyk7OiZk2chI%2FKCdyuP3Ta6pSF5VjT5fGImeNE42CJZ%2FbC6pUJYAxESZgUpkZtno%2B0VJstObMFF0oU8L2u7d5Sb7bGhD%2BFOuzzDvm5XSgKm%2F791osUCEJLAnG88wdUmRGrzctm3GfQa760ci63Chzj4xMKCTqckGOqUBeyFRPYl%2Fe%2FrVjNh41%2BtpxFsQnkHQobOf22WX4h6RwAIPpG%2Fo9zneHGYL%2BgemQ8XAfIQUaQuhztpu6RB56%2FOheqM4Hbg8N0vptBf%2FCR1MZgT76Gv1%2B76CZcEW45S53DenAYGtJJ0QBTDUEAZgo3jFDW5653ySuPk4ouOO%2FY6E3vkDDNuGifY7wjMJufJbnJXBavyUHXc8KzoKDrlSlrvZL2JEzsiy&X-Amz-Signature=26919023f53c08830cafd590a7e81e3e9ca23a27d5c2ed6a3292ea4b327073bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

