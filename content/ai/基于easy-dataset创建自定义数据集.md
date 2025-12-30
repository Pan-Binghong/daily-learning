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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNBWIF4B%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9%2BKHH0PcK5Q2qy55vyJ2vLObFQEH3A%2FSLy2nhPLH%2FggIgCTKuJzdwgLoLsuayW4daBBm25wg5qe%2B6B94HPClLJ2wqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPNThHnM0Zzmyf6dsSrcA%2FcXNrVYWy6S0XXcqWFav8lXhQGcxZsOkYsOZqQfa%2FF%2F47l28%2FjPqeAfp2MWzPzzP4ZPEvL7PofAmcqC3Zg3foEXRkLicCftRmXvfH3p9%2Bch%2B6wXIdsOZZys7lIlh6BxW73dJZ5n9nNce%2Fl4AzbGPHDrXHne7%2FDKB60NEfVg5oOJc4QBIjXt2EFrKxApO9ygoxPObOeqWdD8GUjKIfojWG%2FHuHIYHdvN2TPujyLe6tYrkmFDmIuNTPcalKVHnSC5JcVB4WUhFw3LAGSyflAc25NdmSEomBOSpM79QSGk6QYyeKFhLu5MonUMqVbolIlsqZMxi8AwEQ%2BV4TF0AJj0ni3SifLQnxRAfvzD5G%2FIPAmAclqQ16GrcFkV0WzvUGzPO0PupeSzbmtOHlU4h%2BgO%2FW1SKC1%2F9DJoHoOnYk2vIt1wElHWLVjKH0PJH0kBAqKuVrNVwE8vx%2FfyOVOW0%2F4Lz2sRZ6CCAzlHPuV3If5B2tAN6Ow92yBYM5N0zAQLCfm1U1SAGsWUy8g42czEBEZJ4cLkX8KYVgMhRPnToNi6GWV%2FpRRcIl4oD5lCxkP15xKlzFVNa40D7SaIng8lpAZ94CR68zC0i6o4XT8DdTmFxAope2Cs8S6XyU3BjWVyMOfYzMoGOqUBdIj%2BA5ZLEaZe06KO9C%2FuxyKfiVbfDmv82rgNIO%2BeYo6k7enLpJwyCAEeVo0I1jjLLfrBM2G2h1hw3wZOWBapjsWHJ%2F3WImzDAhRu9UrxvQqcBaMkgqmYSBbwd4RLP1cxrxlA0FDJPkAA1Rl6KsqdKyk82brIyork66HMYaEVP8oanCxX3QfD003dK34U%2BcK26A0Gg5cN739NV5I0NuCPfIvocZbG&X-Amz-Signature=e71ace7c7693148dca51323c31022502fbf0d033cd791cad72ab69cb416fed7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

