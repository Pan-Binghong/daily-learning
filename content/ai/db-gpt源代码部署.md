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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QU4NIOGU%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVXZa17nZz3FxwuLmxWFlbmhf0U37EoYVlfOJ2UJhX6QIhAIn8Gc3iT%2BsnhM2Xb%2FuHArQQ%2BsfqsJ9a6AV6baLY6lPzKv8DCFQQABoMNjM3NDIzMTgzODA1Igzra4Fg4Ba7r%2BsBjlwq3APcixN77r5w%2Bq3djTGKOXm84%2BgWL6jt2JVVBjpnDFqwaZ9%2FpYDMgamCfS%2FP4I4ymmAsuMYF66wxU9nDRfgccnPcYWLHCvZF7o31FrAAVDECYbIQbWCLXvWMfXJ6Ws7M7pu5ZrTZLFq7fEiHTL9oT2KI1j71UHqKnfa5DiUUa%2BMj5U%2BMRe7Ci4A%2Fi3TQIwGc%2FhBBa9c1I496n98uKYfW0teLhySuaiShID4YSgVdUHFGVrq43XPtjBYnq6OoYaNQsooIvD3m7ZBFt3dgHME%2BPvKHSE3Xv%2BuU4ue3erYprra5z%2Fj5dltkxy6DCd0uxEG185WuQzOT5uAXj3Na1JBl92L%2FHNr2pBtdBVbDtZ6xv6iI4HZx5adFjNxp83ydWlD56e0%2FNLXZzpGEd%2FWY8SM01YOhDQ%2FzGSzYVvHPkRqkiZ4yH2e3%2F2bQfX%2FQC76PD4E0EKiYPCcdsYU4gbsHxsxgkR8vfzKdXu7Vilel05DjpJDwTYXpE7bbu%2FcX3S0huPATV%2FglCupVgGd%2B8cm6WM2LsDPcdZD%2Fc1mUZwi7WO6gh%2FeAMXejZl4wQQDr72sc8Thn4mXcLO7Tj8ZPud6RLVdcWkeCmIj0sB4jt0ySvCzhH7Bzc8zFl2JWVVbzkYNcvjDLhuzOBjqkAdSowg0PfS7YPZpXN5QvbWD90%2F9nMCKSUT%2BNrnWZoeNW7%2B3i7qmnKbj7Q1K7CwhTYHFICTGJDeyMEIOaZ9DiR7i%2BqD82Sn2kdQHmjyoWD5t6LCVPhK6p5s5rG1Wb9zIHmmstAE030VEQFOchvUljjGVlZ60L0JxoIb262E3bzceTuazdkJ7%2FkiZuOS3dOCuuhVQEeIfNL3xoikO3%2BuqeTzUq98Ka&X-Amz-Signature=7aa4f890022257255c517db8884bde24a22e997826b79df1d0b3c7de13c0b9ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
