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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHZDFGDU%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDeBHDtKKGbBz1qxGwcZU4o2Jdf4%2Fj%2FmAkRFVZ7T7sboAiA64G9oWNh7Cc%2F9lQzhx9JZY2m%2FxoIrVWTt7IzPf6uMfyqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEcCVMTvl7S5MZJ76KtwD82u5wcNdKIv%2BRh%2F6M7mcAu%2B2jHO3yKo%2FFE7enXXwaMW6OT6wIHpY39E9GZbzULLgMlABArSnfcT%2FbkldlJvyhDrfesNSwppa9l9x3t6xdg0iePA%2FQhiyXt1lJFLXNFi9JFS9dmfGmd1gVc0wC%2Bf6Oe1DwnO%2FR9PITyexJ55ivyRBdcDImvLZbf6MScmBLOucOomwfnHSfFIdifY8wKhDdbzOmyjVpc2gTDAxxdQsRfp2MBm2At4BhJRio3qa4yBxWRFx1wpbvKvTlOwfuwgyMK1qtyLIUp1yTjz9xOVWrT034iLUVWXNoRF6zTxkwXQFWKjQagOiZ%2FOmG5nziSUH%2BWo%2FFmil2pkxdxp5j6vN737fv%2BPza9lw%2BGPYyR14VVXpxkSWjk1SYUM1RYtcfmd7esvCAIqImP6j3M3XUNyMmFX6dbPV9E38IG5LvqEgoLqcM2YlHwHUPfGcw%2B86yAbWk9jfS6zw3neietGdLCfS%2BhwUnmfHEj1p3ZRWYV4gdplukMbaUtOui4rA0Wb0o68MmLzPd%2Fa75S2MQAEO7Lbyg%2BXW4zMgj4efuhxwQwJEvfnxdO0EDQgpQBrYKC5lgw%2BjtW0jyg%2B8q3e0CxHfbHsqtSRMh5IbTCk47rl3cE8wxOGSygY6pgFF9G9k2L3VMRUB6EnSSi9EwxqDc9WrpTORf7ti0kb0TdUIh1RZ3wHTtMO%2F%2Fqo0FwSrNPcyoMsM0MyWDteAOl2MVbmp5V5RnUeTNs1BiUqCD2iz4o%2FbK%2FCZSDvIFetbRaR7cDlEpcadYCWr%2B664M5glFIMizchGB09excC394uyVYiuZUPWINtKcFWl3wbRIEkuFKdKMSWyQ%2FCA36IYwiRb%2FPMAnbET&X-Amz-Signature=8aedaa9656bfc23db27224c1ac45fae7dc58000ebc15112f9e7a72a27d748103&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

