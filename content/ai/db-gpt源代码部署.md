---
title: DB-GPT源代码部署
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- DB-GPT
categories:
- AI
---

源代码部署DB-GPT操作流程, 含测试, 部署, 注意事项等。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663H4QOJPO%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T030941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCyIcWUBOOMBrj7rSc6CDecxKdow5uub2cGua0ZWfF54gIhAOk%2FqnPymY9co9v72K%2B5AGluoz9%2FY3Uq9oUgvrpyze54KogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzXZr6e%2FdDZU69HIzIq3AMycJKQMFzrkYwjLAOA0xyNt9eUxFYr5JoXc9tCUZrtsQlB0jPPe6oxo0enVQiMY%2FidPCNoRPs87EMkB25Wog1hKBCZtrhsfwEno2s8SDAf4YMQzAEk0M6CdAAaIxzqpE3%2BSOUtOfotwa%2FYyk2YHkkya7AITNjZ8Z0TH5nU1HVfiQ4Nr6OJqssdHmK98Rky1z6Fy3YjNqvuFS3Tq4AImT9VdpuUopVPj8JzvIp7MS20jYrBKMxsWApwSLi1UyY9jZ3Ud%2Fl8KvelnlaBW3qwrycsWhCjE45dAOLGRqypPwlftotQDG6%2FQ3dC0IRwHnoMAX8tnUhj9%2BFoUUDkxAAfUpd%2FZq%2BYXAEfZ0z1TG4xDnnRmkBSJHI4TedT0ACPZoCTLxqblUvoK43o7c0dOlMj3Qz8JAuVUSJAQfXHzjuT1nq8lpNpoNt7J8zyTGrnLQ%2BPaDjGoGmwUkDIP0Dp6F6dLwfv6mBrfGydY1WU5eSpUtbePDg%2BcJPCb2LZYElV5q3IomTHBe0vKi0pdlZRrI%2FghCi621LWpjQjCffi2W1jDnZskTOCszydh0bgDSTfHpWoRCbj8CGdtqcf34KwlQacDsSy4K4Jd0OUQU%2BDjMGFlQPMpGu12a1CcWbOfd%2BzazDi94vLBjqkAV11sLrHPLHh0ImGibv2jN3QZDW5CEj5dWP1MKmsyeabRWs%2BnuLpnU5pRLKBy7841Qwt0bH2YjnBTLGLM%2Fl46w3KmcEvq2%2FgCaKANMicwGVSZuGJHm%2FQq8xPGeNDRZ5xodXXHYofMo0M1b6MQuUa7wA8WCZtRSZKNppDT4c7NDZp35u8DCmcPvbJTbal03Xa%2B3kXPaiXEyMVvKAiE48J4%2BRnRf0i&X-Amz-Signature=d262743eff4d0d6d1fa140786915b898082b436106fd1ae5039118c3397a3574&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 1. 下载源码

```dhall
git clone https://github.com/eosphoros-ai/DB-GPT.git
```

### 2. 安装Minconda(运行环境)

```shell
# 新建文件夹mkdir -p ~/miniconda3
# 在线下载minconda安装包wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
# 运行安装程序bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
# 删除安装包rm -rf ~/miniconda3/miniconda.sh
```

> [!NOTE]

```plain text
初始化
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

### 3. 新建代码运行环境

```shell
# 基于minconda新建一个名称为dbgpt_env的基础环境, 且python版本为3.10conda create -n dbgpt_env python=3.10
```

- Conda环境常用命令 :
- 清华源地址
- 修改pip下载源的地址
### 4. 安装项目所需依赖包/库

- DB-GPT下有setup.py, 为作者写的安装依赖脚本
```shell
pip install -e ".[default]"
```

### 5. 安装可以远程访问模型的软件

```plain text
apt-get install git-lfs
```

### 6. 调用在线Qwen接口进行访问

- 安装qwen接口所需依赖
### 7 .下载Embedding模型

- 在DB-GPT项目下, 新建文件夹models| 用于放置Embedding模型
- 在线下载Embedding模型 | 目前好用的有:m3e-large, text2vec-large-chinese等
### 8. 配置模型

- 在DB-GPT根目录处, 复制环境cp .env.template .env
- 编辑VIM .env
- 按照文档进行修改
- 具体的模型名称可查看cat /home/ubuntu/DB-GPT/dbgpt/configs/model_config.py文件
### 9. 安装SQLite

- sudo apt install sqlite
### 10. 运行服务

- # 在DB-GPT根目录运行 python dbgpt/app/dbgpt_server.py
- 在浏览器输入:http://localhost:5670/可查看web网站
