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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3RNQIFM%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSlUyOygvEETMhOzKOVo1mxipf0VcSOcA4%2FgZ6H5kHswIgTV%2FHbt3TrHKKI7n9cpefljcE52QM3MfKEWLQNCL5pq0qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHk9ZPzwQz%2FjrqBInyrcA0oYIPJB8s87ei0YwOZSVvLHT5JAf0HEPFlPVTbsLDo%2F2n%2FcT%2BN0xvp%2FQGNRDjfEBJRxNa2J4KMsGAN1QDxHP1qtUbJF0dqSDcMdMTKid6CnrCDVu7f1v3x4ZvkdpG3qLVedyMTczlTQGy4PTWIue1Pb8LKrYKSU%2FBKKHjL0v7gKiLZOkvdxoGWJWsLGOS8UGF%2BPTSloYbW0b5zRxjQ6uUNYAY%2FIbuXykfsm%2F3SAymT%2BZdV8tp8G%2BbS7EgXXS%2BtEZTaJPaF5VkVNbdaXFrX3lVfSJtta6YzCSe3UBN0ZzMuP1ZfqOxIeAry3WcZ0e%2Fj8wiT2jNZwUHwWRhYtHoqUHAC2174j1a7SSR8wlkDjwqfM91r%2B1i%2FfFcquKvFYeuxxzExV35LDOlbGPOhjTlSA9ZNNwa6oPy13b7%2FYB41olZ9DOpzf8%2FdUKUXJ4B7S519uzmgrggm%2BikfMs8Nc1GfbGI92y%2B0THhawaYwYXwaGD0nZw7QZD3IogH0Xi4g%2B4aszE87c9F0h%2FWFr1T6A5TTexoICc2S7l5o47krdwC4jeDiDo7rUkuYjaCLOp6v24WZkISzzaHNTUo8cAICry6YtLkyZHrGJDOObFDk2jfcm56VaEUWUn3sG%2FYNN8id8MIjh5MgGOqUBi6SSzm6Db5gbee0DQbQr7x2z5AwKitsajQ0FaWIB0ebfySJnYQPK8Xz%2F3cHh4KRFiPn5NRXJTIfxq3g3AqrZ9%2Fay1XoCJq3R3ZbHFyePdF7OuoqJCUwKI1NgdSEmISX%2F3d0M3ewODAcyf6XsdCNM%2BfWYmLIMLRSbQYUbatwSmavsdW95d7r54GahnT%2BPUDnGBfe0oN7zYn2NojDEeEbSYkZb2T3P&X-Amz-Signature=8ff4f7b4f3ca5bf44ec0709322b9fbd028d4f6cc2d2fcfc7faa4ad21786a79fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
