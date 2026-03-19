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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4WGZAZO%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBFTZRmOFuZI%2Fs2ACjLcXQ7TWO%2FN5lJfEYN%2FGKndgGWrAiAluolHKTmVGqpeu%2F28%2FZjQ8dQLsXQDCgCdjdzZCjk83ir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMKwF5ur5dZy6%2BmzGNKtwDaxF8natLc9Ns3PjFT%2FrZksUzUTiVnrJfq51cIDtb9%2FpNJv7CT2YEMSDA4ICpKokOEcmW%2BlKtYbd%2F9PRK56EqmcziMi5%2F%2BnzloX%2Bm1wBake8znU8XOKwJjodCcZJsrXl2a5TAyBGCpd8DWNJ7bnTjI4rj2rbBTSmfUPOTZdEF1WAHTdzAEvNtyJI76hfnY%2FSq%2BFaAsDd%2Beow32gdpBddbw%2BbUzbokcao5o2OieIYJkwlUaVEvGO34lXGOouTozg1dpc8jYD%2B4F5uTAtg25fop0Nss19g7Y5VUK2uhPxgcgy5JSxEfnX8coKXF4niZpy2u1zosgS%2F8xjVTByNy4A%2BNLffBN5Bm9a1vgKT6bf%2FJPkxMLSSkFVmGzZwMneu5Lp09Wsac0uIx%2BpkWtd95MzirZFOZnGbtVEw%2BOcXzqM9FllxBagqyXkAPgWGIWBUtdCamf6JOB9VNBPEuOZ1oXb%2BynnthUGlNOIX7Ex%2BjNV35xrugkzOyK3ajlY%2F%2B%2FRa2m8xxoCPvZBXQ9MB3sGjFwdsBnyD5%2FGhuL7wk%2FlDk96r5lCiy1kgJFk6X9DJVFCi42cZWreFJWS8Jj%2BKqgpo%2Bd50WMeoWBAmgbb81x17TBmetHkOZZz2uQaYtY6EZpZMw48btzQY6pgHjCe%2FSTwItRLmF9vi%2Bi9qDi%2B267w4v%2BqMhjWWxI%2Fetl0YmbvlB%2FvR7VNhwAgIint4MPBOLIVkbqP3b%2F6cDdZC%2B2H1I3agSkAoGh17kPf91wYrzhS658dYZO6Q5sRSDt13uI%2FAm5%2FK5o2H6yPQ%2BRwo9J%2BDUfAUs0CBcg5tLF%2F71Z3YGqZn%2B5WpdX1T4DOVfF%2BFGFUG6bOfqhLGT8g9L4ObRk4IU6h9Q&X-Amz-Signature=d77661ecac8f045fd2bd2a58f4cfc1fb97751a9830bf824bf54fc0519af29090&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

