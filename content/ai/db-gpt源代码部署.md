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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644MTLUKQ%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIFqaS1%2FsrCTFfN%2FEpj%2F0ujhM7W0xVvdgovfYvXR8%2FCkCAiBjGOm7a8KtQr8IEBH0QI2HdVP6PYpA0%2FqgghV2nhqQPiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcfgb1tR2NQPhGZTbKtwDWHmrLBJOkyWujsh%2FMNNUFmOs8%2B0j%2F5YQEq6zxgGDwmCv97zYW5pp4nDAne%2BgSIQM9qXvHxHuBH3DpKF2xF7vx%2BqNdjoR60BKQZJfmbHUFI1A0LkLD5A0gM7%2Ft74KHPCQC1gDeALUF359Ba2mi%2FbKJNDCS0CB1pjvz9zTuk7P%2FbSHKTxhL4ufDd47OogKUXSLHwR4xc%2BvPLrv7YkUJRczhonQKfOqanRwPvsuqJorb49XuJ5uyhFQYztZzFpzi0jaNETd6yTPkOQJcWa8mwfp4pQzmvoH1bFXIQ%2Fkc3mAY0MuEM%2FZ5JiVZbt1My2HDysw4274niYlJmx4%2FWkyCFNaAGqH38giY0VT%2Fya7FJ2zGTGOp5Q5eefXkGyXIRWp1FAe6Siq3tdS9vR1J4yfuO%2FBnKSuM5Ot8UfZ6CibL1IkNcXGVEf7mFGMO8K7IO%2FBeOTDSSgWKRRUyIteAnvKxSo2mtdKLZT2vqik5nh8%2F4sJT4zZsX4tl5q2amkr9HZMGiDh%2Beih5mYnRG%2Bfar9wNIQzcZKCR%2FwURfG9bqtjiIguexBAJORs6W1SBp%2FT1hw4e94YsFn5Cco1MnQpqz3iYVVr375%2BPdFGdmPhlcwqEIdex2%2Bvxtx98wtUCvtB%2Fhswhri%2FyAY6pgHrsis%2BneLlwAyYV2YMAyfd%2BLNLl5OTjtX341QFjTgvrIqa%2BfwvRtBKCgiBCmltOV6AHviVJLz7XOZ26%2Bt1Lo5cpg0YJTWuaLV%2F0Jcf8IYMIAVmr1y5Omtz%2Bs8kYSBB6PzWiNOQrm%2FJ6bkeByfvnWSYjfyRKGTOkrzfK8w1ZxRC%2B1qkfxTyC4zkEyEth%2FfhQ6E0SiXqTRkwRlmfjSqvDXvZOXlkHt8l&X-Amz-Signature=e91967ee9b093b439e7389ae00393ba020fa0c9352bc742d1171c879423a1f6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
