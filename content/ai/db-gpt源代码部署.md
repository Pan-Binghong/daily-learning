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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTAEFNML%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoi1cNdhg7Dcb3CchCgCZKQfuK5ESN1U75R4%2FpE%2F%2BO%2BQIhAIJZ2w3Cr434gAE6sO0ynTEny9rMbbfpV0xWfKS4g7rSKv8DCG0QABoMNjM3NDIzMTgzODA1Igzt%2F28ECy1%2FUuqbwrkq3APJwzDCVOP%2BtcyM9dD7nNyVwyxgsPAmssJ1JoyFwYXPwYOBf1nT5dCHGZj35Rn6h9hOow9O7xTv4ngEbaFMy8bBgTPR6kYyIOtEdv%2BEzf%2FbBU5qxqmcrqhMxpY02O0VDWoavSwbVXqUlurvljkfvpYSPe4SGzwhKTCQePBbCWiOTes9h5ZQX4jJFSX1DXgxwdprl%2Fp4vRrehK4yOG8TrMrTlpw%2BBsWX4lbSP3De5ltoE8L6%2F9yVae7YujfQlNZKI1tNUG5uMebstp3DHtHOymlLstqnbkl1ZQrpM2SGinisakJJWlPvLxKaeA6rxvlytxOwKzHqmRi2R3zJbRPxWENyInTWQHnz7H6DdlNwJTOQ7yzAExYNzEzLyrupoV9g9j5n9GvZoxYkdME2fEJH22hbydDq1yYQPp%2Bs1XUxRSv8IbVcbqvBloTqnT68%2Brmn8ZB4HAPepVpoWr5M8N6laDD9Tf8oJOHaL4IYncyJ%2F7M53VEPNgDVPOHOLLvcZtG5t2g1mUAudcjDNaWdsa4osPLnrt9MeoaIp7YAozlV%2BC7IjElSoGIogd6H39BoWkd9hNwkGd1C6haN9kHJigPNHiKPMMl%2Bu9Ki%2FWxtJWVpnT%2BXSHIhq53VAYhPMTLF0DCrjKDMBjqkAYyFCFCMaNxd9G%2B76r8sNDGk9Acqk0SQN8%2Bfa5wSFW1PiLiPOZV4QHB6BB9Ne4D0BdfhDVXEkYs0vs%2FizIEPCOkc1rBuZKVLrcyBU8VuK0hZt6kXsk%2FUr2SoXiuWnpD3PQ07BozVeonrUcVkNrjk3tKo%2FfxdQlvIaZWbuzE3AwRltQIsqHxZAToVTCb1Q9uDmZ8ftd9Ww0DVLX5jfwfYaxC0esuj&X-Amz-Signature=973185fb0d677be12bfbd61967015322ef2de82a8105d1220996a96a4890701a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
