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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTRCRJGS%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIBK5KsW%2BIgcazNA3VEcgqybYjzqdTO%2FoD9hiIVe2X2RdAiEA9ozDGKAREaEvL4GyAWbRkfy977lcNdnCYUfEa0Eizooq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDCnbnD1hoGInrbL4zyrcA4AOjo%2F4eGlQbnj2DpF54rae2Z2rS6ynskrLGRAjL0aRao%2FybqnL2fnuJ%2BhJeUqCBDhL744J2tOe%2BMvInk6gzuWMHaRaRMGoAj%2Bl%2F%2FUx5QnirYu%2FagxepKbbQaPEcNQxI3dDjnzPDIpXTj2EukEnp56WupZmqIEDuWJubSkwI95YSIH0fvPjf4ATHHQj4hUNWtP9O4lmRiOC9t11eylODQ%2BkmJnY5vvhJLNP1FYO9oC3GT1WFdCzF7yKqhuDm1VFY4w8H9BEl%2FLQGWJmXqRXNuq%2FDDFr5Rfv8vdZq1u0xOEU0raqefm0sACsENBsn5ttY5kEQdKc8nM5uNX0Kp4Y6Y55A0i4YvZI7tXZBnNfefARqR3JpZKBXJqIOhqSr76%2BrZJYeUDj08HuWdFhzRitP209MA8jZUNv2i86vHal6alyRwe5E78B7oFpGy5di4JzSRqS9Ng6IwaQMubLuPWnRVaYWOO%2B2GVOpa7Db0IikRZK8aq31Ziwfn4PeYmI4dnaoLYIH4JfVFhjwZl%2BSQEk0uDNMnfANWojWhrXI88Q5h%2Fmn8TvBeR307cvci4wSwy1%2BWhXFN1IRc1r%2BsKr9jmgj%2BEATRKs3kCN4irvRnCmNYd3ZNToxuxESbe2yf%2BmMO7G4c4GOqUBbjer%2BDqq%2BmiIw8d6vLhnV8%2BHVq4Oaq5Q2rw4d%2FPfLJGOn7t8W%2BvgTAOdUfvdQzmtgONVhnirXn23ArVxtQk15ea0%2F5o%2B7VRMONJ52hMDNoJLd%2Fo%2BI4V1vBM6UKYmO0jeNEw4bEL6SchYPyR2q%2Ba9kzr9BRtPSmRmwEmfY4WMlP1LsL4oF3psi9C3%2FHQIphCDh7e5fg7PTsZLLuCE2QgNnKuasS08&X-Amz-Signature=c718df4403f86743158a868fdeb10b2bc76321783adfcb9843a4a5f85b941619&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
