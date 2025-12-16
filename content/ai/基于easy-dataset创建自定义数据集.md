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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBVUPPOK%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGbM5gcbH50Y0bMi2NVkBHTPDPovbkNnB05C2EaVVxTeAiBJUThnCLi6WNYKFVHa9pcXDx33DRifQfwH0Gcj%2F4XE5Cr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIML9N%2BC7DPWpiWyRLCKtwDbQ06oSPHyccbRa4M4GmIM5gbsPcWsIhYnrMGKW3JbKeaLT28mst24icME2cIxSJKxyiLC7%2ButB3TbpOPOZdaTRHU8tvcTQ%2BouF409LCerFazI8rRdQ0xre0DmxL2NOdI661kvfHb85TOSBL0JIz6mYxDLkvDQDFWZ7B%2FsgHpldf0YnRAR7McIviUrvj2Fh4UlgAzAwoLjlGCxgysUwdOA718bqtfnpvcflHQlGyuiy4Ki6m1Y4x%2B7n6%2BiNUI1udqLPP4sXbz%2BE5uZTa57p1iLdflYv9dZzkf4COgczR%2Fr2%2B1FSwblLrKNwH53hcNHoClPyFf0D%2BNTzxDrdFLszzmAoUrvxghaS31GTIGJqE3vmQsZJ1%2B%2BxlvIerJQ5L8dglJRjV4eGj9zhqiIR8l1CRXEBcfJoguJPtLzLQNMcDgGjayUt8UEziEcrhoth2nXCguEJer8v2UHwGthTGxUSj4FPdmWPcrPr2UqnVr5hMgOSE6jSYEAGFuQRZYMdI5RSRcHjjSSbt0uKEcEmkpsFS9ENCLK5pqMfxb%2FtnDHIqhlIGCP6L%2FRSOwe1WGp4wBd6X220Mj%2FTZFtjUX7%2BvBDEO5ZMDGLS9tyBQlKvnDyC4aJUBJTkzJKeifetfKUJMw54yDygY6pgGOasnH%2BrlIsGpuAGT6%2FE%2FYXd0Afoc47Ny9zmhuU9CHNmlhUxOtrtemq0%2FoPy8xcl4WewKXyW%2F9p9cRvJdoV0xkiYyH76OUAW6GeNZCNNIziHohePpODPdTCzfbOGi%2F2srGaBH6cbimhA%2Bhb6cMBN8wCqgrrV0BHX08%2FOze40GEDFXGWqzBel9JL3H6tHyWGSLFd60KSZKzlneu%2FFpKkRySJKhRY4wU&X-Amz-Signature=d8388cddae6bbb01f2bcfc25c9a72af4cf350736bfa6217109233d6d675453b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

