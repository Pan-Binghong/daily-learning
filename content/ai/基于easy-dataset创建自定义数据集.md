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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRC4I2S5%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIQDB4l3r9qNnO1Aa67C7uT0P7SeIHOyJ3lQgf3QWtw95hAIgSSaWGjTR6ts7j%2Fu9Sb4ZPo4%2BBd%2BTE2Nvl9DUVO1JudYq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDD6QmhZTk6eXTr1PwSrcA6uAP4D78%2FNogQs0hKJYsYprGWTaDvSTtBi8mJSZvdZ89nsBOS8sYdikCNnbO56AHgquoRkJ3l92ioBZgPfJvzayUQmZN79KAuOSo8upfS4lJOfnnVutRvpga1%2FwjWPqcivLlh93V4PHC1sKQDhRK87imxVcFGE6lInWuu%2Fzg3H%2BN%2Fz1o4wIfijhpCEu68zkwWvr0vhokOs4K5cQaB22khvHY%2BpmeGaAMzO%2F7i6MzXC4ecBxwj%2BbCr0AQiTA9LJ03e4DyzpYdYzISmgP%2BM2uUbO0W2OIES88KauKI%2Bgd4ncLChqsq37UjmAT5gU5VygHS%2FDadfzPGJuBRRn1rHK3NaXEV%2BsZbL387t2XlZ2tIN82pQ9%2BpLdQLNcfEKhI9f6Td1SBdhkhNMapw6dk0mJ6SnhYOANFbkZ7GV4B52N%2Fnfo5NWDTOym4hlox%2BGXVARPDaKB%2BecRAgqWiiR%2BFPJG%2BdikREuTjt1e5cOu7reDkZvoA7hl7ogEeKWJE089%2FjAIcjRpMABx3%2Bc2EllchpJKmahk86ACbbAjvQfsXZGXoERJsCAMoS0cri7LlRxUOLEAIK%2BbdykbM3YxkUrz8rOs39ahgz6xMQxVAhxLSUDobRICZBs56ojvoKlfCQjFwMNO%2Fz8wGOqUBSvkAosviz6E3SpOTuaSxzaR%2FrPIVcl3IeWcqhZVzCzrPCms8OfpftiVAhjOKP%2FSktbCfMY49mB2RYY0qwFyewlcvMeSoAm2r83qoBAykNwRzVbPHJfy9OUpFyhkGD4B2Ck1orgJiRl1%2BQ66gcClcaIiUIMsl%2BXWOOG6yfmrtEyw49st%2BEB%2BNptHiBuZnxyPhK1n%2FpMvyb4p1cos5hUjfx%2Bv4VksQ&X-Amz-Signature=a55221b5f8530c6daaa43656658ce5e2bb45da2b9b2bdc731cb36a3bd85a0982&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

