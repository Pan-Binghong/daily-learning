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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666W2QS3GY%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCICYhmKxZ1Off64wqSuQfcNurP9263UEK4htkDiolramdAiAsAaw5z1sV5K8nE5Fp9GmMcFWRrUUABBMFzSgu6qurxyqIBAjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMB2iwhvfWbRLyixveKtwD9cbLsIooIt0Yoj%2BLyGx3nDI0juv2xPw%2BCpM6xXYP%2FT6MWqO0PZO5bHOtXhisKwUcvyyOV8NPTk0dS%2FHQM2Cs%2Bnt491GbQxQf%2F4Qmay2QDMc1NuRiUN9zaCkkmKW9XIugAYwRg630YA6yu06uPRsFITtIM%2FwiokdecpEmPIXxA0IDG3AOePNW2tfrB%2B8SAL87mGM102pTZBqxmFpWPDsNQZU1xJPA7dJ69No6j%2BlJWn714AS8S%2FMuhDdMwdce%2B8Nv7yiL6QlFDm3mvI4Oc725BNcQ9IKC5gMFEjt3CZ%2F7JL3KsRKfpYPG7YTwQ75KMxNSRUBU19zv2MefYlrl0%2FYZroY72pmC23Q7OMOCTO9t4dTNfsTlIxh72dvdVHgdJrQTB%2FL9HtGn0dmf30Tc%2FnLTMSXa2qHZ6jVqeYAc%2FaZ41RXqLK%2BddpQNRT6C5BnOXkSCXgu2GgJfcHbuEjVLgkV9Yuiy1j5RLptOqIU9yUCclRfEOKD4CHzNvCuLjPRL0mjyn7%2F9kWmLG6l%2B1fBfTsYFm5IVGSb5jVzzg2oFZst4UfVbiI0%2FL6ylC4ejXOhtxH6ed%2BmiYA%2BG5%2FT2Kl%2FBg50%2F7fYsBPaTY0mhzHU5fjoajxSeWYGx4V8qpJ9HvWswi4OzyQY6pgGfK2A0v5vOG98AdxieYEqog9oWTSozzmcJazO7KSVRQ36thxQilNtjBBmUAj9qy5y2ZAy8mIw8aCDJrwVQ1ZX2HHSc20eLSN72PScUjsmGxwjG36i%2B8ZBKYIpfXGMiHvEwGMqmgjDn2PQE5gqcdAbUUHqQyFIc80ViREKrHsFHHZDMDmMQFLRCMfgkOEBs%2BI6W7Ci9PSYpTBB8awiXqGsTA8dhzoeF&X-Amz-Signature=44a3a2524d58c9772b13b11ac09b2a945e471d5c955cd13095080a6b9931eec3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
