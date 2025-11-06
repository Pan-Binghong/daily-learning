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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPLKY3X7%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWcQyYzOeRiP8gaLKj0jJXOVR8zmPeoSl0fbfo9bgy7AIhAK4EZkIz4DmF%2FZMtgXghj4fQNRf%2Bqb%2FRWz55c2cde488KogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyteVqCSJ7naa9acSsq3ANILTBR6fljqokU5vJoVxZRhpBeGR0TqARQpol5QBCtWH3bAhUf%2BokHEJ8t9XwPov2yEnFcW%2F8gYdeI63Q7kzUGgtXRM9t2L4LfR0d3N1Dt%2FqelJ61FAAYaOG33a9dZrGmwWX4QJFH2bVww7BcFr1fZoVZ64%2F1w%2BRRH7VRDZ%2B25CI9RH5iWnJYxAAu53%2Flm7Oaxz5nYmbNX3G6y%2FBiBsZXXlYDzP1h7LXipqVbEkr53E2bwmG9JJ8iWPolYDUrZ1ssTRu9ag8d9E8Qx4qh3UmicVbyiduoRN6CJ9Z%2B%2FFQzKhbGSr3%2BicgX35%2BsYrjiO7TMi3b3pPG5LmnxC%2BkpuEhxccW%2F9p6WFKzg1BiXlE63vKPr8yPHZv7r2hfXiA76Ij8y41CnDQkG1s6KFut4I%2BJx%2FY4BRAGvg9xwmxVvooCXRyEHa4azw78uhKLHgNSezTti4Xo31EFHrldZUu9ffzKPPqmMFTXbSiXhfcXRgCnRVnsyL6bsLql5nJU1i8DWYtUAr3PZOP9hiXJUF6CHDKYUmD4fBRNyxEVSsbjrGsuVWG3EpHj73EZQee7DPuhiSQpVcHlUotgjN1c2dJmZHidHjgtvtl04Ktti6maG76gvTVzmom5ckZlmSuBBFfjDG8K%2FIBjqkAROC9U%2FccOjR2qmEBz7JHQ6oH5zBqkYfpWcSvpODBCAwyl51Mc1BYL1%2Fht0fr1i5NCDE20lNX%2B6K5V6PPqAeytsO%2BIPE%2BSn9yS86bhHF7zL2J1P0%2BEQGDD%2BZN6ppv1JpiVZIGWgJbMc8dhdwZvnttCvT8QlesvYWmxeubSDfzqJqM1dEczy2UsqtosWHfKa0GaLvoRllhgfzUawqTcaR3cQtkpqi&X-Amz-Signature=89d5ee4a265a376bed2aa6ed0251dc94aec928509c0da5201128581566e44d09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

