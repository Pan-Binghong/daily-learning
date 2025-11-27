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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GTAARSJ%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICHAiS5qXv4sXmDgwUC%2BdzigBC0qsCQNYuLjXUMAbNQNAiEA7J%2BEnzip6yrttDM7N7K7VtF8Pcu1to1dPRbDNh7nfJQqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGhpAMPuyHXJkgSdyrcAy2vpXeJALF9RjFjyr38e7EMQ5Rr1A4WztP%2B%2FosOBUEjMEcwzU2SYDPEW4ZsQSnD26tClgQPwCHNfkP82VveT9Pj9DtUKqgN2P1r4bhJB6fZG9ywrThLVrfsbcnYU1qt1tNylLLme7gTcHGwo6jT9E6N%2BPqPs4zitAWaHmChzY3zpyzmQcO3dtFKAD6tJ4YekDM3y%2BTpKTzdKYqJEVa59SHUhivKe6jn7nU6mrTp3WTwglAt5M664Lx3vf9XXAD5OjLBIjdoclC7FuSUK8xy%2BvtUMTw3IdUSi3NT65sCMVkXTQ%2FAbMWJLFbl7kRtGrmE%2BRrTOuyLso0FDMCzYahnB5Hjy8dP3reInAWPAxv4uxln4eiKkBFOQ0Gv54DlPCAOIRdqxSlz6e%2BHvC9y57et3nMPqUTXx13lC8BcM0hyBx2Gh2t01aF8MotSL592CMqCmvViStaXJtEcOiOdQSPratBgdenxHYNvlbjieBVU70J72ZodBs18lulNfTKRcYxM%2Bg8Rbf6xiRZINIahh24yV7apjE9fIPWppupO7iUH2tYSCMlelCF9iDKjAHlPSnvq%2FGVC0CoDRkgM0FbZTTmpAhBnFoplqnrHVN72Lr81oYZE1aA9LR6GHjGw04KlMNXhnskGOqUBGaAfWnUPpFj73%2FX6walz65FLQYRWW5YrKQYWDt1c7YLDfB0npyWfnajSwN5jCSpdcnHhG7308vuUUnmi%2BrIBksFn43LRbR%2BYbYZU9wu%2FuS78oSDJDMTEodT8irwHsNtziPNFopGvsW1gUofcFOUHXXH%2Bo3bD6rLyID4f6LAygFDqXQyzfnUAqFPBZniP8z5nzeFF95zYbIY4Do3TsSyU%2BLp7iieg&X-Amz-Signature=0d6c321e37e539b025bcfc6900d4572efd7e211c80893a3bd9a8c04f1a34af3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
