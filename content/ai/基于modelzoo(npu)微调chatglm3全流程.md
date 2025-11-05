---
title: 基于ModelZOO(NPU)微调ChatGLM3全流程
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- NPU
- LLMs
- Fine Tuning
categories:
- AI
---

## 环境准备

1. 新建Conda虚拟环境 
1. 下载ChatGLM3源代码
1. 下载模型权重
1. 安装基础环境
1. 安装npu基础环境
1. 运行以下代码, 验证环境是否安装成功
---

## 推理

1. 修改代码ChatGLM3-main/basic_demo/cli_demo.py
1. 运行代码
---

## 训练

### 安装依赖deepspeed

1. 下载DeepSpeed
1. 本地安装
---

1. 注释微调依赖文件vim requirements.txt , 安装微调相关依赖pip install -r requirements.txt
1. 运行微调脚本, 按需修改路径
---

> References



