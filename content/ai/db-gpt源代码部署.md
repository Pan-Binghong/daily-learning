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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMNFPTTN%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVHuz%2FwacAEC8WTtyf077RvfCTzcxHAxxrbVOisRE6HAIhAKy9EyMmiIBT3KoCWjkx6JINqsBoBSGxKN%2FdRUrXb6ktKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwLswy%2F0TwSAmsnCIUq3ANmUqgoNAX42fVD3D54UMMqIynEbfIXcrB7vFqkX%2FAbf3v%2F7PdfaA9gTdtnYTkb4ElQ%2BgZtzis5Gh81O1DN1fEyouPnEWaHJYdaIjRLJ2yy84jwzQBimT8B0pwkrlwN%2B9dZHh6%2FY3sXzvI8LZpX2ietwsIyznK6jURMbyirCzNSEEqczAJRHF5WuXQxyjuomXl0U4MJqTHu7GtSQCAv11N9PDuRQm1LYzVZ1zW8J86KV821%2FdhTqmpiiNYQM7AmNM4hPsw9K2T5sYIPXqupwKvojbpCC6JhDl%2B%2B5oalwPnH3gdJStdFHYhwOmJC1lNhyor1XUIROPFbBdNGjhI%2FSZwBMK9CETADU9GxH9ZxaacvkGO9T2xuVWcFpdbTk8EwDpFbbMbHFQB%2BqGeVcKGNylFNaOp1dGmISH6FySa9HDp6estPWGXxRtSGgCL6QuytFPXzpnr69faWZviXBniaZMPw8D6WEF5EtdozSpfjfE%2FKglXGZlbQmQMdWG%2BgO9CWv0%2B%2BzNmhnUIyTXniH2P6pOlacO0%2BhQ06fBSN6AYkQ8Mxz%2BKx9f9taqIbsdv6mE9hldTuLSPCIDQQwu2M4iYKAgCdrUEguq6eu30sn9aZGXUa7mvafKPUwnRR%2FXkrMDCBuc3NBjqkAb6rbECLOCuQmCw1osqzqFD3g6o5ze5aGHPIcrxszxb6bJ%2FZWyTTFBADJS%2FglX2iIAsB4TozlNc5LNev3V%2Fa4N27JvZGB%2BmIPgafh01iowDDSoKrHyT7OwyoFklz4%2BDXQX1kFTzWHL7FxdOlmJta63ttp5yILaCo2930I4fSYCgD0VZ5lOdJjyVmu9UVdVSSJxibl1U3e9rPnAKL8oZQWOWv9tyu&X-Amz-Signature=af4b05aef499c8d6798b104b40b67e8f0cb02ddd55ca165271ff17e4838f2417&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
