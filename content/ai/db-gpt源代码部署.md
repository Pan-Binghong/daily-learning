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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YS3BBAFZ%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQCXuYjRnIU5r56Bo2ydtyO0nwFwazPE1goLME6oQFX25AIhAPYy3prJJb9xJRoGK6JHdShBQaYzttWENAfzaPha6mGPKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxlb%2Fic7%2FisiQNCM0cq3ANUAKEqS6Qj8jVMZK9tXCKs4rZugDySb%2Fgp9OgTX6jX6y4ToSwV5kyy72Y0aRUzT2tOrLK6SoEzvlSX5PTOiniud17ULXWFvNvc5%2FT23plHjm4TDQIyBzBUC0O3wtpoaO7iVim2CBSXY9dRA5Wvyz77QCW8aVu%2ByeOMtfRu2A%2B%2Be1%2FHKSh36%2Fx6HnOashh7pkfNZVh0hVvTjow1gkj86sbm0uPSNmZge6doSyfdLoOxm4atZxkzDtvJn%2BvMkYqGRyHpQEHf6SJKbx3eDCBQN5LuEXW9AUT3jlEgetA9Flj%2FI7lO4h6oyZXzffonYddLJA2lBclw%2BJDe3F6LP%2BXDzNQf3qbdO11qQzcoob6mc5OWQI%2FnzVMpOBDNl%2FednskV%2BHXH8B5IH0XBVT1%2BHFsBPBiRHvemiOQ7Yj3MWh5W8YVe29K9MBvApW%2Flldn2NI9Byp69zKM8MzUUfGxiYym21yGOi2SfM0a4RIBg1mDm2%2BeaP8U98uOL7p9vXJZfmMMjPsfxO8%2FmAINqO8orlfmmB%2B%2FqkkelKkk2KwfUpXS7MfZTW04NHLZ2NG4Z5oA8ELZgcfmswBvTcbfzdMeVU2aRhRutoKAQGoyW2AtUaUb06eC32hphAZYALvvFYn6GsjDr7cXPBjqkAfK2%2BR3miCOIlKUm8IRd5uT4ydP901jMqp7%2FFn80ZemK%2FTsdS0Y%2Fo94hDMuMUjHJY2q9zZ9Uns3zBpUEkfwwdsZtXmz4%2BlMnOXh5CFh6hUmrF1DVP3TUPrvza54jMcO%2FVsBo1Qk%2BlhCwdU2qm8ZYaNo95%2FYgF2GhyvDH2tv3mdpONK6hnY5PHdxZlnSN6pTU66h805STRV2GeCClyddH1BuMILK5&X-Amz-Signature=e92d3e9bd62b06ceec97fc3d940a1f24d0ee261e69552eb0e99e1108637f829d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
