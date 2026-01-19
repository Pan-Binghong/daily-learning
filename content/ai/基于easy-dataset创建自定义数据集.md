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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY7QLTPM%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDee5FSVtJuCTkEWzo%2Bu4N3c%2B2ROjVGk4%2FTwo%2BWmIP%2F1QIgGVhR00AC2KeQd0T%2F2hf0Yb1f22yLA36FRm3799a3CwYqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7kijC6lEZF%2FbYBHircAwlx8R0m3VBFoJx1t34vwjUBpTw1ckUbFaMnCG0TEO5tHefsWT%2FqHvkHo4f5V%2F9NopI1i5tS9UGoHyG%2Fqnr4%2BswuBfLurE7mJ8cY3hVVzIaEZHd%2F5uVVkx1wYC%2BlCzTIKO80XZ3uqiGEOesHV82zCrkghWiWYlAlTGsIHyOoFHYiM53s8ICw6CYySPbO1cQ4KG4iSZE62mkfUfInh%2FHUPBZ6%2FylbE7F5glwgKFOyKDzvEs8a0W8PF42o%2FBR0HtelhWNErQiR9Tm700Zh%2Bu06pgwAJ%2Fmavv2JoCxE3OWRGSKlvUiYxHSodO3fvWNkZSiGj93VOGFJb3jK8kKBdnuBP2SfNJCProBx8%2F8YYwx63JfHVSuljb%2FyrC%2F06sz6JcP1bsXHtS0K87T7Hj2unWiSQ5yJ0mr544fMmKR4jC3DTBfbQll2mrEvVNDdAZ%2BHQ9htVY9VZbcgGbphtvZ00xYYEdypBsyqBDXbvVu%2B00mIlVFI0UOC8MicZHyHQJOuDZoy%2Byr6wkrnnDVJTVt27pWzYra2ndrJo%2BDzQmgrcyzMnBdSW91aXIg%2BTIDoYVDZ0VNhsrj%2BS%2Bj9uSOODQys9CZbuoa4q3mjxuiBdp2XvR6uOyiItgH69dRmtuLbv1CwMIrdtcsGOqUBIBLo2dTGiaVl1KzuVdfLghqkPztSiLQq%2BkwWcOtCLVN6BXwnIxgm3snONsx0ZAJdy4JxyIlaQnA7FYMSil%2FtGexp5%2BvlkknFkrTp1c1cdF%2FITWddXJOZqYsee3ckb0gjQutlnp5hhiXPE73oNa5uAacpLPA3oal3vLKbNQueWd%2F0p1GDjSudPPOMuXcIk2%2F%2BiA8r6TEnYMhPuvk3IF2QrvfXa7To&X-Amz-Signature=c87c67f846135abcaa44424a1a3dec5da46f86570fc67d2504fb95f49780cd0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

