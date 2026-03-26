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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654UYOZRZ%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T034920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXhZMiHht%2F8OUuF%2FIJmIaWuThkuf734ovlR6Dyy7jjpQIhALuvL7vJRBSYVYu78EXW7EkZGZE9w293UvUGg6cqyMz0KogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw3VO%2FH2HBiadBX3jgq3ANEumu7qlxYcXCE%2BK%2BVsoKcMx6pNKPH8PtOrgIQcDc%2BiR6UXuyc%2B8hilcsWi5SjPltIWvscexJ%2Fekvo%2FSBPmru8sjBb3uNgW8BBpPELz7Yvef0TYazX8WwYOo3mk5USHStrCMjTtaPldmY8ngjFvbA4dFjiraDZLEwdMEqZDFSfaBFRgQKqVqwiU1oDGJRgk8rXy70jDh5Dz6Z2anavii9j1xYqK1gGrrc6ToCZq0ZPLe5ph98sh8UknhYTcTJjhFtuBnTJM9xQ78JEJLK%2Bd39I5MZo9wNMACCeofn1j%2FCWRvMhQn1JgPxcLTqE8C%2ByBMCktbIlufBJiLFpPp5Lb5rY3SU6zF2296K6c%2FJxQoXoKI60lD%2FvaKi35K4wGZf4%2BtJ%2FIa0s6bvxJ9tRdwxva3Obu3DqhQSI1GoBFYmwlgX9ShNxeAnCevnEvqU%2BIWbvIWsWOQOzM7tD2%2Fmvs23FPPHBLsLxmB4BisxQ6I%2BTBdwjjzx193XxVVCDlSQmlP3phhLcM6PwwhFdbOa3FFsXvW7EW3AyXOboPz9ukVQ85%2Bd9rjCDyNI4TGGgwz5YteFU9u5nQG2Yp9%2BnV%2FleoGGaIraq4LRjdqa3O3K5kwgjxwjLnqchC4xEZGXXtPJg%2BzDEyZLOBjqkAauZmp%2FDN6UsVO54AF%2BgqUskGdVcaXYff2aLn0zVmWZj%2B2NMYbOHBr0rDB0vfJDLDT94gHtz8clXLn7UwWCUfJ2jjSrtqsYCBrIQPelJ%2FOs6FbIqQygREtB%2BT6gBq4caMDFzajLEv6eGBOKGWv8dEQ6udyeHmDi6zlSo1EwUcnUZf8V5lX%2FeUp%2Fl9KPNveyU%2FKhyzal0SP9wzPY17zOtcIpLXNf5&X-Amz-Signature=db42ab20de1db6613ba90c0d43d76f6d70e381794532659b76e0e2a8f2f7be50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
