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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NZJU4IA%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE8vqRaOgzQ99t8dSf2OxNaKH8AnDvCaJxSEpEmYNRr6AiEAlaupUMLihaonkACHVs26SE5rWwLsauNCMWqQ%2FRFgBVIq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDHO2N0rDQczd7YFWsSrcA6vY8IuzZXU5nAJmnqk%2BqJU4qo0xPYugIC7XniEtHH4%2FXfh2NWOkh11ERmFZp4w67Eqv7TbYJ51OWommKoNGnlehEI0ut1XpqnzolzLnwg%2Bq608auqk%2FqtcKCykLvgpZXCOZ%2BjnD1yLJg4bfr%2BvtkfV6Zn8Q1w9ri9AtzZBzZtPtDeFfED4GVDeIUaiW9P2wfxuHmAtb4fpLdyo0%2FilVZW3RGVc0ToI8ceAoMWVg6nFShflVDpcUuzAD23UO26A1uEHsxN3gQgMTjWrbbyf6Q7vb%2FVSCaUS%2Bvrw2nM2gLtMiHxu%2Fl6%2F2nLbHl%2FnSgv50YiaLg0NMtEJSNHGVLoKxshdj55h6wsoXtutI2daUqXsrYrWRAyACjWqivloMCa1Tq2iXqCAi2VDPRF1TGpKltK5bdaC5Z4DmnBelBn2Il4bZkIEfK4xzsD4EQ6Ojkn%2BjLZAwEWEWP3fIldvt2oWPScvf%2FTSoWE9pLGQbjBNMYAnkedqEIfhabJxA1zevP1vlLuWhJBwgGCgY2e6xs3%2FeDufUicCm%2F3kpeQHtDoX33dK7wHL40wWuSGssgCEDIiG9PvkwQKox4q3qKPOu0JJS%2BkqrG%2F5A%2BJJkfowlMAVzS6B64bNd%2FV8IFnlsnol%2BMJ2vt84GOqUB8FR4ymGcmZRHfXGhQk4oRpxIYkLIwrIIEW0QiMukulc1eIdeKBxYQuA070z8ljrvGn3ibpYqzDSsImAj%2B0BuOvfC%2BRRr7CL6%2FaOitGpk0uakITWtoC%2Fer5%2BMYwkKFrAeZtlMDRhpW%2FlP%2BELXpe20l9spkDbBkwUx1TJ2sFxVHLAjxarmLRjZh00IHsKImhimR0BDAUZgKP%2F4o%2BvugWw5rgYnVlUP&X-Amz-Signature=a725deba0fc8660393cf8af40a99457c9c83b798ac167c1ea3a71c2995648d44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

