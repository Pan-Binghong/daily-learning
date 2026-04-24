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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K3Y2WVE%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB2J8It%2FUH278KX2KBKxvOSPT1WHYh%2FDEOw7%2F6S%2FPzsMAiEA5PzmSImopL2dEVPdVcr6SybqwXO%2FMlg%2Bqp6osAIhPY0q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDJ%2BrdgUeac6J2ZCT6ircA6PrW93A9a8DPviNaeV1f4wfGeYoBnJejEBGcty%2F2C3k%2F5IHvbXZubAe%2F0lLfbg%2F692vfQdqYGzzlWMqQEb3EPQjoG6o6GC1OIhrTMo4XNSQzO6yl%2BhppcWmI2oE5LFkELO3X1aoXCarFeXB6LV6%2F4MjAzRCxG8JU%2F%2FxIj9ihUg16QQ%2FE8tHWTxx4zxZeTsBJIAS2idgm3oFEciYtzvSU0nLxEIRIhyuHnIuY2vFvGJM8V34znAYEJYJsJn2Q0aHRwnvVMip3RoOsVIys1gRYikrGUJ8oqDZ2Wpk5bT4O57%2BZgA5syGzqPf4C%2BUDTMNLeBejP2pkIG5h0nhSGdxMVXmB2YQ0a%2FfhKCr7Yx4UocdX%2BnKFpX8ipgSCcaY4d4zvaLHTMDp%2FnoANSWuxtreK7LFw%2F%2FTfSjvwHYhc%2B6UzIQLYUALU6d66FSrJjxhoTzUVD%2BZXAqsz7YdR4017FrC%2FLXdG87u6BeU%2B1Nfy8slGN9UzhuWmPU3d6%2FuP5rjf1P4mTafunrxqgMQ3PzVv0phmtecuH8N4%2B%2Bi5N0UT%2BfKFIwt%2BtssZEAglVkFHE00usLjRriUIjNcrY3GrXzrn8mpaR6iHaGVNOlo8r1wvguzFiNHmLhwBSZNzZCAsKWqdMLKtq88GOqUBtb6qdsEuKNksqu7IYc8acvsVZtp3ARpQ7XJA0zRsyNzGttJheLFXz3sPt1fxd0WCW0J2QYn%2FZJw5D%2BsgMaS5%2FiqPOrMp2F6LzZ%2BzA0wsa9S8VYWex%2FFxycGCxzVTcBTqTdZZibGg%2BIvt019uCQTT1RXuWRGBZZ7kpy%2FYx%2FV8PxpOZKQeSvM%2FqbmJJ%2BVoFOZjjg366osXL1tz1a6SAAIvY3%2B4hkTS&X-Amz-Signature=7a2a8972b4aff3b8d87a2deedd4c21e939587aabb9e990e771faaed5827edbbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
