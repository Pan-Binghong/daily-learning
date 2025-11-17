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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3TEREXG%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBqw7HnA7z3kHhQtW179SBxW%2BKqVgEUlGlgwhFUH0Q7IAiBZMS7KRFjOxcFKUZ9QhY3oQYJko3KjbI%2Bz7Bat04bewCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FLbv0oLs1AAVZc1nKtwDp%2Bq4afMtyQY8iOavD0sUxcehdxnKvzpf4grQ%2FAAFFmIMNTm0bW85s3Bh%2Btaqr5T5N%2FNKDcscGIXJ5VSPCFSos55gIVmucDjv%2BrNv4K8RTKE%2BAUaz3ydsb%2BYtKUiEgdkFx8JPFMfRk75A0QymcBlNlQQogGXqrKjMS%2Bfxg2qNKyNMQ4xzaoGS0mk2j8elMgUdSFRt%2F4XnA%2FCAw%2BUMNQucP%2FZAD7PEVsyomXRV8BJsI%2FfXm8%2BTn02ZOMCvMrK95aygkDnCUnoD2JXUXay3CHnNl%2FMz%2Flh1vwKmRgEJoPjeEjiqtrdgGn1MkV8dmpxfFQBFuGgS0dMD3WfZH714ECczwoHlPn6STalxK0sopVykwFT%2BIm9p6%2FUn4yJReFNtpkQi5YEKt7FdDWFoHAWRQckiXpHhrXPdiBIfpAcI0ZI0voSAybtBYkY%2FNz1tvkOiiUEypD%2B4hViIqF9GuMonF%2Fe9S3YkrrpB%2B1Y6AHUc045nVEnuXJD2KR8ACkzIgShQEg7YvlunDIvncJOQqgiNFY6zaTD6e%2BwvZEZ6zifrczs%2B5tYFWP2XFezqeO%2BM7eehkX6PZhQie3a4Y0vq3aCKDl7KafiNHdNxpQRAN3uYef7A0RecqOm6dC6ZDtr3EeEwlYfqyAY6pgGFN9arnBXr8yhbZi17IkjxBoL7EyWajVIi3V273Z2Gmr%2FKqgITFRcpD4tlq3qQIVT8IptZQca5je9JyO8Zxmxd80MZYuWlLQDB5Oyc5WCef7WHV8GppL4NFFeQLI0GNYDUr0A1IVelPCuyg2SQLcqAuNrpJCMUwafqehu8y81HKe0iF44tGSVOgXUqGN%2BM2e1zMLDibGW6Uj443eMKLuaW7IN3QkZd&X-Amz-Signature=d49553b6dec462f90498c7df3b231f94f7022338e5b3cb7556617ebed78dfcab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
