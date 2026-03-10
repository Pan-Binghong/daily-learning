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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAKFL6IM%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIDBqiK8yvmlhl2LPfQMpYQix45s%2FvIpgZSDx7FPnzYWvAiEA%2Bsg8eNDXDU3dH0v4iDrk0TOAF6LqCtEY8QIIymFsPPEq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDPJYEwQk5N2yV6ji%2ByrcA5niP095eRz55bykWFiakKnbhkm2pdr5XIDnOMJOmicWk52YDjUwn60kGEdDye5YVl%2FT1GbknrShRXQk%2BywDhHDvvhoDGxNbx2pYCrS4dKJPe%2FKLWfQeezccr59ySh6z471a%2BdPldTI5%2BohWrhnYpR4oroY9BxZVUDj%2BoKl%2FaZCxHCS2kRsLTVfhpBIl8s8BPreLquUvYQgeNKNatBNO%2B8kPRzdMsi%2FSyFR6sanlAB9JqNV%2BbSEH0Vccyo7zqjvotlfGE8gVEs%2FN7Cog19cLdeSLda%2B1AprOMVY5YvcM%2Bv4r0aR6TarA550Xm1gNKkDzte0egdKph%2BXVm1BHRE8%2Bqhl8iF2VswULonXNxOQG3w7M0fdby6IT3QHJqb5r2AxsnP3s7YSi0co7MvCAGnNTfxs7w2PbYGCFExJOhnn98BY4jJXhcUzG%2Bf1ge730V4DC%2BMovjFUS6FpQJkuhQMLAxVfU7wP0uknv1MsoNUOI6iBqhB349fbUAFm1cFYnHWiI%2BPnnnuKjbb5xujMX%2FPhpSKMCx5Xu66SVgfEAXmVZjNlWCTu%2F5HmbMVr8wepxQm%2FwwOqxTUSsC7SYYivzCO%2FeMuw4bnRx%2B58YgcnRjV63a7DB0TlCeQjlOVSg%2FaDdMMmPvs0GOqUBgRgfsOUYOrTrnfqoyfp9ylH1%2BjNse0NsFbZz%2BIQs9tE5qlfTpRVvXmGuiscKC5is%2FjmKi3XKw4QQJt8Y5wi7hvPqV1l9Iesz9zFIYghGZvGDRJjQeiszOdkNOOOnmCBdN%2Fh8%2FOGRZkvYwjlAAGAUxpEdE%2F%2B4aYFBM6S%2FnY4pOBgX4fQXUEGI0uMPh8JzBHbyA8xq%2FN3hErpN6mzjqJg4kXEcABrH&X-Amz-Signature=d81d9c3cada62a13afd44b5d880055757e59eb240368bdaf5109709a42a2aeed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
