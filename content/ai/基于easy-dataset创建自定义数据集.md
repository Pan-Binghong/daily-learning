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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL3DTJTO%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGJJjX67U9yB01YiydHFkcmKjZhZsTOFqGB7tRxfZLYtAiEAyx3ab1%2BE7XCyEIoEoTPgptFJ1AMsFerAS07zNiN79Vgq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDHOj%2BvagI%2BssOT%2FgoSrcA8cRyfJOLqpjohkdnlrMCQGAHeH38s6lITTWEAQLPs8qrkMvAcLO8zv%2F9yYyLioQMhTnbVOFUZIBJ4oNtr59k9MAdPsMTNReUpC13aFCXmH9WiLs2XPnH8vT9zVla8kcu5THE5ufFYSV66am0OA7q9940zGie4f1w6F5fzHi7RjJMPpHmW934UXDH0xFtiaSDnhe%2ByVEz%2FHHB0cHdmAvhbYNJvhv8ZCdNZ%2FLoEEMiymUjoOqQiQR1Mf4JDfMmGpMyKAIxaeX05Cy2TZyWW5JfajY7A%2BgObHqAxsXGzdcCmpza4DRBwBsHxgHcRnTsDL49zdRCHlVnUelS0YChAAcnfwjxLxd8mXEY6UNPiCT7svU3ezbajKd4%2BPoRnZ5e1Fo1BbE99CJIIZ5TsLB5dj8bLT9SmIsQBDeqquY4Zbl16Fgfjl0mxGQhjsXBc6BagblzRikuQYbOpkkD%2FOpiUXI7GM3TW1GkCsKRQpPgHG7C60qBDmjzFBQ%2Bbq%2Bn%2BogbwiH3qn4bIbpc5VqdSx1pjghBR512vbg1YQ89U0AOJX6cIEKrGSw4UeQoG9n5qz80XKfK5Zw10Qm0B2IxQJity6IcYT3m7k8s35q1srhR4pEEAgM1A6zK72FUoqbGt0KMKynzskGOqUBl%2FuJ%2BTp5nFL5sadamcLNlSHG8JRMlR8W6zPhzAmUAv8CN5JyqPKJyquk%2BmkLnXplfY7lsqAkPaE%2FUu1URn2FWcS8IGPTcA929XVcyRezCdv3ljUgZrka8%2FmVPCqEBovN9dfeFmO4HqAe49vnoKDGLbyozYQBQkuwkVOP3wVWOVYDWTmkpNOieoS2Hu%2FF9oUYZkhI3kvGOt288YB24biLny%2BRYA7p&X-Amz-Signature=6d81a9521a0428da65f552c278f76232fa9b7a288e67c928eed7ea2bd91969f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

