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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFH6KAS5%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWDD8nSMQ6e14NXWFxSFapvZPBxquE87%2BEOopv%2FzY1IgIhAIy5VXBFoiMeB6Ov0qUEZrDrIm9dH6w3fyWvT94zFXv2KogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZ2xB32qD24GsPtxMq3ANKZG5XZ9RLHIFzJEtoaxZXCDAKf2cX3wuQJa93d358Cc3Twd1%2BaEc%2FsF343cvbrNL%2BidZlAkz3m0xqebALn%2BQImGr4IYBsWi9%2F3pxkHceqWzbE9Oo23BLEAriCug8VJ4vwt28jGfykfo1fX37bLoxZ%2FjsQbdJjHEPCpAQGUPCA%2BL4v7dFLu4PBFVGv%2FNwUSCrLM6YFhuGHI8sfYkulKYCswoUIeE6IiXQiuqESBjOkOWAjg9JJA64e7L6WV%2FT%2BeykozmdfFASpoC1vT1rWh5Kk9iNR7T1%2FROtZ0BhXRkzmkI8X2WEfVSxJyY5jMtssEr82aVhQyBLiGA9DhYrVanQkdvUZ1QeFQfuV1y8yRyJxu1hCNciVqT71SJ4mea3gaVMKAdeh0GE4AfCR%2B1Vv5jUwHOWmJ%2FNfLYl%2B53sHakx%2Fqllwqcro1f7%2FFMAWN7%2BSH5aj3mkHjsn2NsC%2BBSRlLYSdtNE%2B54dGRlDyoPugWQQcXBdeZMcWwvYYLssY290XECHxgpfgthc0ycYypKgXTPKkBnWoOhjnlQ0h%2F%2BNPm5tzVgyU17Oby6zbEQYJlqw6qUNrMJbeGXgI6RMyw2PQjYHEbkRSTM7Uhp%2FF1Tv17M%2FY8r7gZFhgXDtUpr5ecTDG8K%2FIBjqkAeVWbwpmiM0aWYumjRHzvqYrPItEhDiD3Dxf5WiRKivicBnGFwH6aiPZOq9FChbihR9YkxZVC%2FOmiUPQ6jfhaWDbtE4CXOzmxWBCfKvsyYE82xt76TF6OnsgEV4MVq%2BANGmTVI8Z%2B2jqb8p0yJrVtICiaQchwPGDy9UOk5U5Oec1CadT0UBAQl2zTQkmJdnnW65PK3aTVxcmV%2BkZTPc0e5mcxvml&X-Amz-Signature=572bc0e926de5cec656c0e3d5f75df78cdf2983bafa3bf6100283157b0f95145&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

