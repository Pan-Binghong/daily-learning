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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVJAAD6M%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIFO75Y1K8zoAcE2XzEDesG0omKBXxdZWag1obYeN5qOtAiEAlwz0m0RnpWrRWIfyWOe1ce5slV61eLMSNdtvblgqAV8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJoIhlO9IQixQsC2XyrcAxsIGDVTnj9NF1h%2F5OWmYHMl4Yw50jR72vy2GyA477T%2B0BKcKEmbJBY8pYjbwPXv0oXaS6VTNNcHMiEhIMqT9I8iLO%2BDX%2FtWJNEzLMY%2BgSQznGsN7mIEowX7VTQ5cjkyqJtp9XdDHLE4osjEzqDRavFueSFrDb%2By6JwpeeZF85kNkCyV2oPWNWxB4k5JeM%2BA2htzYEU8qN6keszgwT0gHkrxiGbS8ygKjUty7bxhTCNc1XDmL0n%2F5G7CdYhSPsiB00KiKOJ0992w5TVx7OmKtYgjDtOsCH3Ada6ugFhZ29OVHFbYUaaPqOX4F6GRAFxMQJBAZswLhsTs9yq35jIRl6%2BI1wEX6dv0yt1V4VyqvfG7BSjjQoLkvVY6fQUM4aclhV%2B%2BXkD2Go7uOrAJs3yf%2BZpWMnIE4EgeRpfmfZp3Bwri7357g3lNYT5I7ssCRK90DMVnNKCMCA%2BYZsJ1bwUodnC%2FcoEmJJowyPC%2FLIr4lNx%2Few03mbCiFHgMtOvyTDytF29ubJK3Uqdmyn8TbYQ07N61P0WCT%2FTz1qMmCJe9iRvhgNnN8nBE%2BTLYSevusSK52IWfNn%2Fmoo2ffyw1uNQnYdgZQRpQz5H%2Byim71Nw%2FsWYVeza7Q7hRbF9Z7sWUMMLn4s0GOqUBN4FZjy6Xvgvs7vsddLCAkE%2FwrgrG0f5tB5tIx7bn%2FXorHkeRoybKq4hb7SRnlLz3nvjwvNRkhmW%2BBwm1S0ErxVugjOBSCbkB0kLBjrDIcVAbpgHvELzLtqu%2FxzqEgyjOlO84Q%2FV24nDgad62KtyYPcsK%2FCIrjnoLtGkqGguXxeQreJFro6hl%2BMMm%2BIWbHE4CqOXSI9LI9Nn0yicBcGQ86XUZV1Iu&X-Amz-Signature=244e6715e35a54f803eed61fb82b5574141e4c6ae6bde406742b534b1b8aa7ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
