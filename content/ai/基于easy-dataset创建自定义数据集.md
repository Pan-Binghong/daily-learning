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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTTGFAXE%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQDKAYEyhZqKC7lEgS6tmOiaiU1aGN2bnyRqRusUkCRakQIhAMIj5Uy2dZ88oSY4vK3egce5VvDqBVxm64pJQT%2FJAfddKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwbegj%2FfIIsOafLE%2B4q3AO9D6d4zlx33U3ostkeCsUf5TAEpzQ21yZqmwzIPDo3E6aK%2BEj66E4mMgFlSRvF8Yo6ppg3prk87SGNtw0agsBBV43vk%2BRU5MzRGL%2FyNoIN1hZSPdZkw3l7Wd0tlPspbEFY473EbYFjKMAcnVmMdkCTXr%2BRIv6YmYggSYJiBMcBkFvhVEDy2TS%2BsGRc7qcce3mxHuprOzxzVHOLuCXJD23xaB0xxWnrtQzyMigC8YPO4qvGR5DGqCsCk5EgtkpUhASCvVPUCu6Xd28VWby2eK5qpbqaMaMP2cSu9v4whhP5%2BAwghWOch2VpOt7Ccl3%2FC1%2Fad5EQbfHMx78w%2BEm2Eibp0cvZORJKuXvECAutWtrhmBPcW6liAnpmIsvVUSPM5D%2F20SCM45n%2FeaeQCsqHFQDDTHaQU2pyeLcUvFcmmkth2gkrXGRPZz8XdptY%2Ftg8TMhQ49b%2BGbA3o44U2GANoADOOSp96kNTXajcNbbZFeHxFYrenBlFvLlxe%2Bqc8CTUPeiPREA7tEdFmU5bPcFKvmRSYhPm%2FRZF38IhsKlRn1oVR4nXIU5BgcNEOn5lbFqvPNeZzgOyKXV1GZvLUXztWhyJL%2Fcll6sBW129Uf%2BbL4vjFlBv8JhGIiwd9sShUzDdyvTIBjqkAZTt%2Fj%2Frfs7xVHyIgWQldf%2BEHJf2TcVV54gQVUWW9RzJWjVxsbUnmzAiPEFM%2BeRG%2BZfeI5GVKKjP69eaNUhlO45Ser0s%2FmfW53O6JId6CwwwTG3IA39EuO%2BkZLtLuxS5L4w6ovXz67v1Q%2Fzq9GrZDtpPJ3597%2Fx8nCp8g2swc0uhQo00sa%2FS%2BDz643csxMQBRmTPSZcj4I7NlmcbH9p3aXDVx6wD&X-Amz-Signature=c50f359e1e721b155f8ee7250ee267e001a5f23a5d02567667872d0fbf8ed322&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

