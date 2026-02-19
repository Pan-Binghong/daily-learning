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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667URJYVXN%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLxuj73DzGjn5BUuj%2FCudoZjCzGgSCY8DnThePza3miQIhANwf%2BZfgJt6qXWLDzF%2BHCF9PYaQmiR480l1ueHaUuv%2F%2BKv8DCHQQABoMNjM3NDIzMTgzODA1IgxOEYzUAMVeSdJ3tmcq3ANLB%2B%2FgFzCzd7tfuPipzGMyndCzsEaPhyz23Sfc0WIf2GcvS%2ByJOz2KlIivUdBJbCXe3Xyd0tB0HxoPtREL4hgLQ8a0s4UwGMtWW%2BbkkFrzHpnbGHHpOd1Oue4uio5S7%2F3WPV929q8YmU2ZQTX5A3DZ%2B2opsNXNXs4IRHup8AXiw6drpkIZJNvCZ7GjBPWuiKtGVSJkobKkqZKmN85Sr7N5z%2FXc5S8JYOuoQl8u6cOZb1IdeAkw54W%2Bm%2F8KLHQwIP%2B95on4WUsszHh4lxz6j2dj3x064oKSYDq12CpuKAjtpyOB0%2FhAhdBr%2FBWKnkezpJxVz1kLDk4lzES%2BAflVeFmllwP1Q4opalgYUSBIabMR39YKIz%2FfWEuOEIh4bixm0MyTLat%2FKwadomIPdJX7l3k6SDKHh01db7dud%2BJ%2B1s%2F%2FcGtW8zVrLmzHs%2BTN5oQc9IaCfJ7WMw1EJ2t8VqHUB0%2FpksLJoZEe9aNmfA%2F7DqbWFuDwseO%2FSjqvRA9m%2FcMK7SmOAjvs8ROuUGsVUGuxqNvGr3oP1BK1jZ8BDdOQX9Db0rMtjou1JKxnl%2FFWhMGs%2Fb%2B7NnSRSIiqRSqyIM%2BeG%2BWGQik%2B620yv7VZ2fPJ0VYspzkdqPmoEAnfnsPrkDCf8tnMBjqkAVCuv1KXJxlSvY36XcHeZLe%2Fs%2BMTzzBnM69th446ldFAFF%2Ba4%2FxFoisLPXEHfH8G%2FIeaQnTE8NnIuhnACahqeZkUsc3z1EotOpq9D56wT9c0VEy9C%2BdRqC%2FvAJ6LVdVLT9oqCa8pSAGHg5WemzgCVTGuGQ89mShjn2e4c0Wu6DdeOrcrItqVQmwjnkkl7%2BGXGo6regsqkkCbAUrtDCrkUlpURoSh&X-Amz-Signature=2b99d213f3f3e75e3603283b68bf470ff7da35a143118e209ffa187928263cfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
