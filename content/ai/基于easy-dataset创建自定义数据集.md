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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URCGD5BI%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQD004VTOyWplZVlA4LtEes9S52o6e9qTQ1mbD87BJepKAIhAOBK51xDt%2FU9HyuTqCvsCDWBiPs1Md6UbNK3wROn9Og1Kv8DCDwQABoMNjM3NDIzMTgzODA1IgzMpUSC9clK0%2Bu2Ctwq3AOrdIwsLqGON8uakR6TdmQ1rAeDesZ4hczeVdrdHtseavm%2B%2BtuwLxrwDPaw%2BqtUlxxuiquCiW0jdiLZpe71XRgIb3c%2BYCjmi2IMGjCw1Om1Uv1gJNRUY81XNNZjswXdRZNqQgejIH9lkta4J7yWayF%2Ba38UsjJzXSSby1isQWLshG%2Bgtthf%2FH9n73kO6Xql8pSV%2BnWSyNu9jxxVBbF8HJ20uhUOdj9vxYslVx5ijiuxi60AtUa8hyJU2MXPN%2BtxiSf%2FPbC40L96VrNO2K88Z2RbsAgj1mbvazx0j39KwVEzS6WxicglRPbxcSRHOaPWOZeHCRuNDJmyeATE7%2F4hEBipme9DAjLwgyHKV3ccuuHDaKvuH9pYpRXS8Ah4CRiBaFf0MxXh056Jyeqka9gYnjmGQ0k%2BZYEgzrh2xtbpUnhvpezMD2xtmpdMJeMVlatMIdgMUOXh3El7YQR5%2Bqa2nOsjEzgXgqox8csCrynP29CtPwoSJQBITde0B8UhzCYIPvgxfHLvE0s4NT9rzjutJqtrOXg4cHT9xff%2FfZAWQJ65tayf3HpBeoA7JAUh4tdMM75hOlbTJBiL2SMStZsGC4QPyvi9H4WimzusSAeQSyWb9EyyIMAB8QprVDPLBTDR6ebOBjqkAaWkvBd70IY2aLHUstzqKXWLiOjun7ePWE8B1N0o0w9BDCecJdqh9UjzhUV3MKhheKaG%2BvKLLgT2m3SylPeqalfWBfHB6mKyC1jeRMnSarQ2W4qkk9cFHJQiwcoe355mnY4WKtCLfkZ6vvrcc8jZGyMIcR7YM65y5LFe1EmeQwoiiRoPHthuDLzoVsdDkvWKcfJ0tQUuyVXy6ZjkRG2fbToQWq1Y&X-Amz-Signature=26590e8858474762794287ebd0aa3c353ee0eb0b95c20d6eb0598ce83665ef03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

