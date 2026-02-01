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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJB63BGS%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFbGkY4atdCrboCjsvNRCR9lMV2ZfmdsKavOv8dWs0j4AiBEkO0B%2B1PI8MT9NJpXC%2FyLsbmTozgRkK87hHFfkoHM7CqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoxRHLnf%2B1NM5Oc8QKtwD%2F5DUrH2L%2BPiP3m2ygih1p7uN29XcT4XKc5KKmfVNURwSs1SQYTSu%2BnS8yMAK1GSrzCyXR9%2BNjclZkcV7knJlp9V8U84vOxdevZ0SFg1lJulJquhZRFsntbRZTP8pjjqqzk1dqg029HXohfx05AjIGS%2FQp4MZMdC652%2FXZ5W1Wx1PGXynp7rVIa7%2Fwrqe48zDKNp8TOuUbCuHRI%2Fca%2FEjncUESqyh1LHPOzN%2B%2F%2FRiciGa6TUwYa1%2BLXyr0dMukS3HWfddvYUqc9Y2MFWuk2IS7leNnbLy6ioGksWluklzLP8ludXZH80nWuBAUjPPBGB9BC3mgjCXo25VE93b7U2nOTnqA3nB748cPfCYuAt%2FWSFbCZ184AhBFPn7bZvh98EZ056nrKfdIuFik%2BHVpVToVdPxLF%2FqfuhaIgo9PZe9ehfQdUuvS6Is0Ofof97Iqf8iYn6%2BjfaYir7lrtW8jyGw7NlWd2E9APl7sZwidJ8IcdzIvWuvkfqyIrW9277hXDf%2BbgVgvQTfGnITz0BCAUdhunaLtjI%2B1qzjvea5Qhtn7oz1o8EaXNR2MxVyczF1rg%2B4Cx7BA00KnN%2FtcFuOG5ia%2BN21Ay%2FJJ1sGyBM8tcaP2fxxbyxdpNlFe2D%2FI1Ywx7H6ywY6pgG1ucDxNbWTqLqvAboSG58hQYedAa7nArd9xYRSMUuhT3mg6ogf%2B8T4ZdxyzniXuw6qhHuku7u3nfn46DuSaj4bMKoRaLf%2B%2F8Y4J1%2F%2BLmvVoAuu2Si1THzw1AmC6jm6C16oVKaeRZaPGD1VcNTnY3ZfLFhD0wHDTgpGAncz7QGrAd5vPqXD%2FH9ZoetmgnEEkJB4Mb%2FrdY6cDUW3tM9fLhx7IMk9Pwhh&X-Amz-Signature=25d2a247a14f47df890b976b0785392d65e0d6113d878bf3d23fbc962b1af3ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

