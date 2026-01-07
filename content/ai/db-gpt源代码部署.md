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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642A22ASY%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwNA4vF%2FM8XhrsYNN8NOxUktBae%2BGeusdcIVDTf8ZF%2FQIhAOiNj0XQ0NN57yYPXJGsoQO5nKRW5aOBAuUzbN9L0imZKv8DCGwQABoMNjM3NDIzMTgzODA1Igx2WLDDcjGQf9DeKGEq3AO7fvKqUD2UjUBJs5yl%2FUBwH1L9SPwhnf%2B%2FV4i%2B6aPmxSV5d8JgfAP2O%2BLG488%2FPbgxQxq%2Ftluw5QZFJfuD%2F0FE7POK2mcMM3zqqWHcK2BB9ur0bRYgkvWAh5NrevDPvwHMZIJPjWxGvDmF232TdWHxLg4HynHkPCj23P3hBzEfeXzWgBN90xRoRFIuVGehndoEJuqbTBoVwCc%2Fu8K4GnfQ6OnC2FOU6DJqbZgH%2BOEEX7bLG%2BxMxbBnzZP%2BeqHn6XOzh%2BAhDXKso7RM0p5EDffLABTCMsz7PgCHOfhaOi%2FcgPdPBZZ8Z2lxpkbiLuQ0PJ04Kfrz3vFlAWm9GHvkzQsBSsWZwKyuKrxymEnpzKp%2F0bqpFaAtDbKK%2B%2B89r69Tr4NZ1loqL4qHMpxb6%2BGY6%2BCcWDjZtxbxRhVsJf9KomwejL3w%2FofwA5DdFxGcOb2vEs%2FlHnI1ZgWT2mnfEAaCbhKwx67Ym8jiJqlO9vyQ5PzzVcgVpOdTUiepzyVK%2BPQ8U%2Fayo%2FGY2c6lbanc3BTn75d4F0hvDwjBlZLYOs8joheRZuYp%2FlPWRoEQZdy5cvxaJyLHMwlLpO7dlOEJ9xLxccbG3k8mEkj7Eu0GgPBpxehjorJ%2FQIjd04TkEFMCfTDzjffKBjqkASW7Uz4Dvg816ghfItDe6XkE1VM4LLYah9koQdQO4ndyoPZ%2BgGQWQYYrBM08Ch98jrwa30W7r7kmv8xbIaP3s1rTqablAGuRjrvxzR5TMzsZbm23GFoOwaPzWayxm1wm%2FwqETdj9%2BVvXFCzhbGnKSRrglq5J0rdP%2FDb1yVkl1RLZK8jdngl2BAqqdXxH3bQ4bJAiFM%2FY1Rrjbp0HXMWWE0qr6pwf&X-Amz-Signature=c5aad2a6589a5b76a4eba1dbb9869a083d4c1fdf5fe5bc9f820f64ec0c0cf652&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
