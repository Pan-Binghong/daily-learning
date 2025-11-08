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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666DDQJZJ%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDUpCiA2vcvYgj%2F0xtUDCDp4CmJRw9DB4kdm5kUwOrEPwIhAKsrTdcdqOEJsWfvEpitmW%2B3YP%2B0HgKStJ7wQ7KJOOudKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwhjaNwh1e9hulYKSsq3APiAs2N%2BLalR31DoAV0OzPApTG%2BfMc6Wd4B%2FdexAd3Fg0fzWGPJ28TnyhUGtqVmu977x73eA4je7EKVMPiSxw5riDkyhECsDZFo2X579rXhASRXr3VpmGUfIYYGbJGYe2EWmG%2BLEfjGG5OYCukKD3PNQSv5R2FxwclqbBBdcreo1k2vVgFK2qoTOEtXM0yZ%2FQYYhO9KOuC3TVHq5xiw6ggsJthqhEwy7BfQwzCoorVRh%2F4WcruUW92KLnswAVoys3gTNM6ONAyIl8w4R8C7jng%2FpDlanO4r1fX1Aj3C53B41zbspzueJP7dCCmlIYKi7R2LWsVtNxIr40ERZtUFGtMh19q7W5Za%2FCmH62baFEJII0hydGMZNsiDx0wc8t4wY8%2BRyxdKVubajXTi9VFKHx4QIUQYRu241FyjpIKpx5b93chJougqNswTiHC8pA1Z0zQF5tZW5m8uhXzcoHlG1b4VY6yyezLhiF%2BHffIi3Cma9VMxUyQhjjcinU8e2KyIKsq77OBahHiwFUHUPlnWsjvylOVGJJn9Wi0j6jEgy29oyUXAuPnoVztjF1iS8iDohoZef%2FA3mCWM8kOe6FmNDm6iCoT8Swwb14%2Fi1zLcV9PJqXtTdVqDuBjjPjuI7jDL0LrIBjqkAazqolYmr7vWYo7lo2jODIvICKi6K9%2FVxD0yY%2FlXhNgT2AbREHJb%2FI1Yr3SDh0TKmPdeTBV2n1I8ocAnSr7Nkbr8Ab5vKvG%2BpRcro%2FM0ABF84dUwMKFjvdzYpnN4Vhuc%2Ff1XFMixd%2BuzkqxgiNuO0Fa2QrxC3SXnJL5rN6CSfKHkLFwgfz1sLYl%2FVFlJf2Gtlf5NAHssXS0faWOJZX2rur54GmA6&X-Amz-Signature=f09d85ab5b4605a29c3c5e2ba563698d7cbb1d3194b3eecc36e6eb21c547ff9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
