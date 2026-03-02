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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VHLOJLI%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG3%2FBHEdOJ8HWDT%2FcTAPYYxwCj2lmajXF6NhREqIzM4xAiEAwTIIecB%2FCwA4W%2F44ykrRbY%2BVDI4sjvyLQpvcM6G7zF8q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDI6C97kWzmz3vvsQuSrcAxepA1eALwCf5NvtBF0kFWIyPQGMnaiAJMiibJuCs24c42a%2BB%2FKvIpG529pCnU0r18vzVoi8qzrt8sNm%2BgFDToAAS%2FZV5mCiRFG27lmiCJP8eD%2FgzcKxWqR3XKzcYBXZYfePhQanOjjChqX%2FHZ784otDL8RPDG%2FOheS7WDrzlDiAluG3kKcaAv7voBAXdfvpIVDtj3rAuEccoG%2BKMsa6NldcqjdAV8xyx5TgNuwEOH8N4XHyOxUwMwgXVtRqH3Fve3%2F7DdbcTUlTE8%2FjGNAoyDx%2BjNzhQyyRhksazAjPRu%2FYptVkffYxrP1MnE71Hd3gWj3mtq8aJQ9idFIA2XKxGBcpqRGsb77w2FPbhIeoODFDApUgq1Z2FKP5gnnV%2Bd6wVDOLe2WvvVN%2BH%2FJgHRzwA%2BE9sZINACc%2BSAKjAyYlCSOWfCQlqsHZgu8XBaVitiSQb99K%2BkWfKHjumZsc%2Bmhf0Miz2cAx7jFCKRdZ0WeTufswape396bv%2FG9xd5Z5rdyyitP43fVyM08s4ml4VcLhDBYGekKqFtV8Z6Ifdtio7i2rO%2BmnP3aUXWz0TD441Z51XnHBRRfvrFYlo%2Bi%2Bm%2BW%2BOScQ1WIl9hA%2Ft%2FGb5KWK6QyoLq45v5kGLt4DgVmuMMr9k80GOqUBA%2BIjdj0fctFEoPygKNJ6yk8yZj0uZHrtao6WWj%2FTfn7f06kAdqeyJ5M%2Bh5YOgg5kAfoqHnB2yuC1RHUz%2BG7R7c72qjhJW86sMG7DGoq7woBoD7oqpg9b6NQHgcsWidi3LEeLDqiMckj6DeDYHXIK6FEPE9eIx2FymLPTndbha4vNyvYHwFv%2FEeM03ib4mf5JsP3DDdVyFriRNmSGdnjxX0w4K6n1&X-Amz-Signature=2de76d7a87c63881c0157c844387570e3826f59fd06365fc88d2bb465a80c3ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

