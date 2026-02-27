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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGU6U377%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQDYnACp7C%2BNBBBGeAWvcXlwkWMbGw0zePL7Dm8nhFIxOQIgK%2BrtJFHxbcIFFt9jOERQqtA2yNSa4bLMA5bMV8QCSioq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBu4qUvr6LLWv1osLircA7kpurYcaJQf5ynRlhLJqTnacpRAzF2Ex3cxuS0p2eYST9bHYWvTMT3u23AZyvSVFy70f2q66Rx2RTJH0PnZX5acay7ahTgEHHAyErobtXawECuKo68h%2FjsgZRimhPkQJ1BDfbzDKwX2zm3kP1NuyHtM1Kn4Rac4EJFPXALOQCD0SA9zziArn1T6OCiWcUl985SW0j1vWa7rWduSaf1c9W5Q73hVelCDAFuRh9fT3HZLv%2F8vM9hcF9GX0Ka%2FUx7AcSH5ImHLZtsR2UYlTebbtdGDXzAXZQz%2F4DWy2VB5gts749%2B0bgCNamuj1iLqr2SkLYMPRoiITD39ZrPSDi4%2FAj1XDvSAt0BXA9OjmX3HLIN9izewyNeweTS6LBqI7XDevwkH%2BzClHRFDDjEL9PXlsJEKmZh%2FVUzjFQJHFbynhdZqk6FX%2BO%2BegYO1Jf%2FIWahAuYsYC%2BAcZ%2FdiWNUErG1ce2j5qPOyrm8b%2FKGn9%2Btx%2BX0866aa1ePq45eVUAPHoZrdT0LCVki52%2FLfkoXIgcfkFwNho966PxOVxT3bOLmxdKxojAqRoAa6LqmCl4zAqtaidToYFdC7w3IWDrvvWdrX4JIhjkYpPUc8esM5CBHAeIWWi97ZK4bImXW%2F4zSHMIOGhM0GOqUB5gpyjs8S%2FFl5hMG0yUh7C1dcIBGeOPWIL%2BRybm8jFAzgF6jEPjFIL69mLLVPH%2FMls8FEPefsnjrj%2BBc%2FB%2Bhjo2vZtDAJW%2FImWIZ2epcPY10ziLCRZ7bD28sZFgQ3%2FZ4o78ZNwpvsLtGBz2eJtFGDA95LP4QiNk0%2FBL4CIDxD7Pprzok0t0DVQcHuOh9gZHeqPH6rloppPQbBZYJhK0%2FNSBY%2B7e52&X-Amz-Signature=7c9a3e7f9854c7c87de9172a1a64865543949cd8a69e5217345db324502eba53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
