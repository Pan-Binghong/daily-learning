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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DKQMYUI%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoXGgOdouE%2F4oWBwUYSsdAI93ueg%2B6u8b%2B51wNw4ZnOQIhAKBvmfdh4%2Fcp3pCYC25Rdj4Bld21u69MpXAnS9GxAhQaKv8DCHQQABoMNjM3NDIzMTgzODA1IgyZ9dJbHXDK8VtmOcQq3AO%2FBA4AZFWvektRXj0U8OMvm4cxuGAwMoF8Ao5es6AwgS2%2FzgH2CEID07G7s3vTTr%2B%2FmZM%2BSZHbG3NaWGi5YrCCx%2BpgeGWqM0YSsdtACpUuEWvlCLwA%2Bdc3t%2BKYRoSDvGEQBNm5Al6%2B4f96izj3rhsk2E%2Bldhpvz6cYYSuwwwN113zpwuzxY32qEN91n6CwHZM7s%2BJt0v5vE%2BBktFRNfBOBANqlHl1uTfW1B45fu5hdkOfYfewNvpmDPk3Rp4jTH9FXwkiKxPlZOMEFhHC6d758FSPkA802XwWUG1g3hwvNqsX%2FF4AI6puHu10A7U2dYN9DJczFlSRaLMUvH7WJgRjJJnCyQlQBzPH3dWbqUPEsEQKMkf%2BujqTuPxjXLP3Gb%2FjRmFI9rGTST%2FY2RPyGyxoU6XP4HUcwh9XtN4vPufDfMqOt%2BJUToouZ6M2XYiUK%2BgJn2ctnBRFDhbCB7PaghDry0uz%2FTQIaUqWaJfgW9ip3pQNZHA5%2FIGaTreEa6bhj6LLeBDqFn%2BuH2%2BJMfref4lxseOVZxijgTdflt2ki5%2FCn%2FNq%2BHN05GtHNrGXwLiNGE1lv7EyG12ub8cGi%2FCr6PCFGD1WiAdH3CgpJmf3k6iasMdPP5aoYPaVD23NIUjCis4jKBjqkAagFiSWhZ1wzsAI4pyx4Gn%2F19hoveM5mrKM%2BJqKfxyV5KVXOArbtXcs4OzpgvdeUnmE88ktAIBM0noGryahGaLDpPvrtgjvvFGHp7q89M%2FkIWZSwhU4686fiRE8FJt2KZqfzwDhyX6PETs0hvbH%2BQ%2BlyZ770UtUZnPdXGPGCDto9%2FpRWVGjba832SOqhLSlJt1xFi82r7%2BSNU6E3wK1RIQcqbNdJ&X-Amz-Signature=b2a6e84a9268756e7d57ecf96ccc4da002377f8cc4cbe2fcd04d6bb86a883f75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

