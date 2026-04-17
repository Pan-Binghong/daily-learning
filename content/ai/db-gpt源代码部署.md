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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QY7UYV2E%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIEsVYVjRPX2YVXz9nrRrNDlDc8PnJ3uPOvP8dEsc49vJAiB8rKMKUUVGDcTj0zaRs1sO%2FysIJnoQicAxX2RLx3zliSqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BiLtai56CGoYNjCxKtwDpEm6%2BL94IHnQxFSgJRmexYbK%2FOA6%2B88UqkestIoVkvWOodTM745jYJ%2BHe0iP3U7YwCZqNYSslItiosn5dUWMOvIw089QBwR8UzmvbwsZsUnr78QiI1IpNTxuAelqS9JGQGmKuuWO48PkDKdYtnnwoFFYaXMv0KvOnF7UJ%2BdIuZUMgBqCXkfYxF9G9PUHzuFae%2BR3lIbY96XRyWBEBp6x48GVTf2%2FqracvqrF0fdxEriC7XDIKKMAhWn8pkV%2BL4dZGsLKkX6QZwZ7qnd8HD1AzRKGRgdTdOJBrKddAW2JmCUR2KlfUTvYIbQpzBawcTuJVJQlwTL%2BYiP9veq%2BOPMGzoXf7w6PVhen2Y3Q%2BJpYRP6kscfel8br%2BEAmyujPvWWWAfOmT5MlCVfskx8Ls8F2kWALMkvib8Lq260CgLIxhe9SQEPUQ0iyV1vBJU4dCDBQ5AERTlUWjF4j7Ym%2FpxXzMUX0z%2Bx1rXm4vo%2BVMsG1pKPmImb0ZAOpVXpeEYZLpmrI8adK3mmqZl5zLpxcxQPho6Fpco3BtTvtxXemlYuVo26XELr%2BAyTnZPThAs9SKDEXqzlL3JQPqO1rMUyYCQ7pnTeIX%2FwVc4B54lk0quQ2MaBUKK%2FK9USnY1xnBlUw9bqGzwY6pgHcxMmnPWStbwcSOQx%2BgF17b%2FwtPaGZ21AQHGd4jkj44T6ItNLsUU76X4bOTE0RhJFV6lU3MbqTiv75gCCmkE2quqKaa%2BVRQsYF6JSgccFtpHNLEWp1poL847IxtFPxiFweJ7lCAPPNEPAox4Qruw9l%2FpQbNk2YyjXBs%2F70GHCab7fjyBVwJNdZya2i6aBZmlZN%2B5CXPGj82Lq7xIcY1e5Uzhmjk4VJ&X-Amz-Signature=2f742d36d4c96ae05f4f4211055178d84a2307e4755e8750b27e09f756a0958b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
