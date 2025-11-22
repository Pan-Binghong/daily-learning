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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UOXX3TO%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQDuM9M8rnpsFBOOS5VyqvUmlDPaWAL6S0KCtn1hsvJ5OwIgTsWy3rlB83hyYU8lfamPoVpOGqyqTTw6XglmqUTd25gq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDLGQnQrhqUBX1yIJ3CrcA7VUqy7QdcpYFTOuOuCBeTeE2cW0nPwLm5uG%2FbTnLdpE8Y5EjOkqNviU0nY1WYWO%2B717sg6BghvdC3Rssv%2BBgShR4pvSD2F6caGCH9%2Bd%2Fmle%2B%2FssNnue%2Bb2DAfPLlPoOOAiEBxYNlMCcoOTMT%2BcOUiEJKETb8pFKZo1XWwDtm4JKE1c1%2FNnhRgRCg%2FSPPyMfKdT%2FWdKm%2Fh3w3Z22sPCD4NH%2FzQr72qvGUmnvqvHUJ6Mfl5aSDkVtodcvz%2BFvEJ9enDnlu5NUZKPKLuEO1QnPtMnkHQ6vZAF0EzgxiotYYCHuqSF3ji9xBYNb5ycuQTz57U%2BzNYGxx0C%2BX9OzgPiwQ%2BeOJX0cQKrpoRVGsq%2BSwmczoRacVIqwr78eqodlY%2BZrktyJq8Oi5lRN8BtjMx2ajcu5RkPeXi4Co00XOQhmVK6hCQhOZuU%2FbhTHBh2fXY8BLbKmM2JjnGCeZZlbgUK8IW%2B4mYSLNAFMEnGU%2Fqpix%2FJew8On2y4557y5Ahlmn8GEslIsquOPRMAN8kjEh0IuXCcZpSyC5OabLRbiFYq9khx1vFyUdX%2FeQECtTF5uEYSwFami7NZmKjsBIfJVzOG70joWilR1Yq%2BWtNJ9q92BRvIxDjxEVvCFJYa9JVnlMNKghMkGOqUBeUwkkiD87pIGzkyDSSxYt5aIksXEd7GyURwv%2B%2BoldynkwceGPGYH2DUxmok%2Fgl2%2FARBOgXXa2UUxS3JKvzZW24Y5SFuMis0W67VBv0dkdE5aWHXXv0qWIGhjKq0TW3MGjr50FJcL3TgoGdLhP0yzRHuTkrlAIDFedER2WW1dbLe2AVx8VwP3HLs1HV%2BT9bJnsusEw0Y2VCic23D%2B3wzjwha1%2BfYe&X-Amz-Signature=9656601ee5b03b54c1bbe3fac5b6b938e29a6540e6759e5adc2a8c449c8e2fab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
