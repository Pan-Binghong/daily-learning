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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664FJSY7L%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5aCHNt1xcEy9%2BtpMVpI6xtGpNkA05GQqP1XpvjSsCaAiAs1td4x3Alz0UG9kjG1vfzv0wIA5fM9ATm5yh9YaN5HSr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMMBNIogSQHR4cLz7WKtwDYxzryj2FzJLXUQ1caYm4njiVHjtvzgMdjBHgRKwL9nDg%2FfptkM9Rfteg%2FoMyuxiTfJ%2F%2FS7%2B9OXUPEr9CCTn5WlZc2kKadd4DRLIBAxNF0rz8KI1UZ%2FxgxDNSZrvCTC5SAsutjJ3Rs4Ej9wNHXXpYLhZftbQ1AVtIgZAOxrllqTPQsP%2BPqzaM%2F0nTSrEThhMNFVRCfw%2B4xJeh47eASi4edKUa5MejLWJ4mnNY8hbJjS7w%2Fn9S3tO3xtmmNOZaDJZ%2BAQJqx1DECKCgsOUAK7XUTeVfKLhjdA7dRHe2vGY67r%2FA%2B5BoKkE0bc86QOCPScXmyecXLBxdbPWSEQAChVHD0D2tq52Za4wrgVioTtkW%2FcSHQh6YUJq9154BK76Uyct1CqpWXxKvFzBQdZZaMguAXaPa0s6HX69Ssf1DXWKgVldsI3FeJJyCjncMIzVTwn%2F42dqOHA5Myv5gjeqpEK0PgeKX9pvS8PgVJbyu64lOD5m75viZLsUaBM0fxdor%2BEbMwxm48LjmSL7NSEg2ko%2FROMdjUWbAtuK%2FdilBsFso6cbzSSEYpYf0zQUZABdvj0lM%2BIoQ%2Bxeno%2FHEzCk1tpC8hs7E%2F1smcaP%2FBSQxESFaRvLaCbeJOmISg8Pw8k0w9ZaJzQY6pgEm%2FIO%2FLjYyF0N5s6xZRJWaH5BZvaXbDfOPksR2TIHqf4d0j2z%2F7mKKBs2ox2kzPRcuUMNEbokYE6qP5dDQjoxlv8UlWcVSErTxKCqfzbg1Xp75RKFq9SRs3egFo9YTAThWjsVVvy%2Bksw%2Bw4LwrBnmxxW0zam74whJLr6tYTmN4e776d9XybYDaYKuzzKyHD54ogw9KJQj04ClIsyg%2FU%2BAPoC8ZgWB5&X-Amz-Signature=f303dc46a52a2b2b94a933d2941eb79e90a6fd8c7e2bf0b411f4dad42dacc40c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
