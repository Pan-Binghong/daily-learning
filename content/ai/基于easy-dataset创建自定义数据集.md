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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMLM4NCV%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCICKnCXvo6876wBiL9cDRG%2FZyIqlhQAuPzHJw9WQ8ODFSAiANHVzO%2B37kXNXTJDosRr%2FwwV6CdWjf3wpcPxavxuZVkCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVU34Ie8Veqd4DC0BKtwDL%2FtpIayXbH2x5mtuY0eKaJ5ipmxx1EnxCxRE%2FPwkZKN4tV7eILfK4LQM%2FQABpeMyNmvlE%2FPR%2B71GlrrBVDGBU8iIetNyIorKPIrlJjUHQtTr%2BaBdNz4g4jsr%2BrVX7WBJHlo%2Fkd4WDrEeRCvj3DJRd2EJxW3mwh69FZ8ghG4owD5Ytd7FbhdSl7h4bcmejX26mtN%2BlZHixdQPgCSbIIOQ9Dpxx%2FGNT%2FF%2BXvu7hZzvrI9UUGczX24Zzjvi0HsCBGnAYrklI06w8Go7ydl29xH0ytPGfLuHNFvs9XyG98FEAPRJGt8YpI%2B1qD7zyPFhMzu1Ymuh0dz%2Bz3SCK7bVZ%2F4njQ0oboOUR5ORxaQWBYP05lhIJMsjZct%2BNpcYza89%2BIFu97GF6YWa9Mrs8t6gWOYLN1bUD4jGTHoObC3Oxtm7cLT0Fgy0akwMQWzyGqIgzC4L8RcQXUDvQG0SUqojCy1d9kLtTXrxeVdvTAKg4WWQ%2F3E4gBolVU%2BrA%2BsvwlCZt5s8Yl0O2yVoPj0Q4caiFpH%2BXB%2Ff4k1uzH2JD6Sfuam8mGH%2Bk2JxPzKiy%2FcDVyqF25eNLDk4uQEYK7WdnCxbp0R8aUWUtz5CYd7wWwTXg1AOxqrGQ%2FSy92lSPg2fcb0wrb2GzwY6pgF0SMOj2SfomUbhf2bOQ4p3FH8N4IytC5u%2BqVz1CZIxlIEVOew4Ts%2BNwamFMZcEMEvAwH14rC19wCB1WyELQgmlIdftPUks6wEFcDnRhoubn3P3ZPeEOKgf82hCQOvSsg4l7YNlL6Taz4ZcCkL%2BgMrSAFQOeFB5r6la8LJ4hZ6JBKBZ1zkJuBhTUODTxGDr1xxKezJdZusl0%2BKNzETLRslhzPej4hSs&X-Amz-Signature=bd847e7b47908013fa9ec0c9a2826550398658d1b0f53e46882c7fc52e664f70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

