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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWIRN4GS%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhk2wYx%2BkpvlBJmkasLM3X1q64xYckABXqFm2TwUkuagIhAMbFAs2bEJNdtOV29ATwmaWWJP7ycQjYzRqJKX2G2arZKv8DCGsQABoMNjM3NDIzMTgzODA1Igyh2SAXiD7Jovw3zFAq3AMMd0358nl4OqivoSRsDe2DXnYX%2B%2FSbrWrmslq7PiJHn1YybmsVomU7Os2w9HGwwxtxzat%2BMvdioZYWFb6L7P73ztpTlXGVpDs3oAxl6pFRi9JzewhqLrPGzMMcORFmwjfIvymPzi9ulhbMSGu9jbbjkNKJpxpPVBBRhk1ifwJt7p4X4q6CVSycYRoQzvdWSGLn3fhOlFd7pgU7wVX8eysFi5S1Cgc8X2PRYKnFa70yfPAwu2p%2FR%2FyydT9%2BEDXn7JHVVLZG7pegmXKQrbW%2B0ieM7EAbQ%2BRTShW7mIdEFIUQ0vOO8V%2BfwQsCQ%2BmEvwSo7itr7GfnCDUgGhT6Qu9ZVEt4%2F0qrKYY252ebo07Uc9PP1PiE04U9vr13yALjJzBXkp7TdmIVINhtXQjFd7bjhMQU8pbPS9GoCMttLZTF8zChyTqd2rHUVxK4fpG5QYTzIC8kwzvHP0RyF0kLvzAADdhx4TfV1y8%2FM%2BPwsXRdNtDn%2Bos6KUgJSilyjnZGSsGbXE9ThaiUNxBuQWeaHVXHNEcMXdLuL7JhxmpvjB7mwxMhi36nO6HQ1zF8GUL4AeD4rSjxF9sJ3bAzK8RoesDI7Rro6aaX17RHPqF%2FR9zBvU3bHh1N6jOdKZ5l8C2sFzDQssjNBjqkAZvbkbfXPpPcInWip2dC8rHJbBjsSjn%2B0z5s1xJYRhi3pjg4rEM61mK5ckMr86h%2Bbk0k%2BDcrrJFa%2F4rDUvD82EHgPMAua2spoG81jw%2BIMNaWW7tZiFJwmVnnU35EZ5JlYWSmMntkGC5nmGJomlHtVW0ggnNScjMclInAK6x6PQ%2Fy2VLdBH3I7lzuN6kzQzc7GOPCbP9oDOYiz%2FZUgdE3SwcLJhHm&X-Amz-Signature=bcebf6ee2f9866536f8a0b5f908b5e6e1c9e8daef5e864fc90f27c12fe9139fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
