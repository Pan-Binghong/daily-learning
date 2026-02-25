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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP35CGLP%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQDXvqxndm9Mf9XQXcJDD96Q4N5aMOgh4cJ34QqNGoXfIQIhAO%2BY81I6%2B8PMPsxaF2oxd47P9vRJh624GN7dclDyl%2B6JKv8DCAIQABoMNjM3NDIzMTgzODA1IgwaqdoXcvY5ykrXuLMq3ANZk2WCgkQHa%2FII4ZcEDDDJCN5xKObQWD1%2FRUfqx012kIm8ATv8kAyOXEGuV5Gz0OG1rUWo5y61okvtmcT%2Fi6K36FI5WoJtdr6%2FbSi0ksjYnicMPu4wtlsBRJg9uQ%2BUZIoErxgYdXjEqJZyj5JzFgg1zI98DwPQAnmzu%2BrsGFjYMH1wyrLSrSBPJpAMgX6YanwIS2kjbxzEQzlo8cU%2B6J%2BVVlVcVCGQzTxkKR1eC3L7A6CcB7V4l3vTbWAIiU%2B%2FZ4Dqopm86tHtv4Y7eM6kd5Gan835nCAzoDbpaEB9MIJFAEqc6eYHC0Y70Z480ZziGpnMcoMdBOW1LYBZZtfBD2iAwAsUAmS0z7vp5yzJNwlgVsVYNfzCd%2BcYnGoaYU6MLl5K8dxn78Ai3tOotQk3ywH07sICXai8KuF5JEjnnLelKWG09%2BxUAzuWfTVeTV1oIYCVpTysQpejEzc0sTFVtta3lXhzv64QxPyDrO%2BN2LuBbVdWqYXF3Ucm3HPQcIuRDZEP68cxH7AsGzI5THJCVXQCgoy7FCdz%2Br1VWGGRbUmrzFznCjGbq%2B1zejE5%2BItLw1FdBctNwUBSrjNdfVWcMBPNzFFNeDAoUrJmxGtltK2f5vqoaBXvr5oFHBiQjDDRg%2FnMBjqkAUCIRxkyr%2FylV6s%2FQiLXAXelcBxo2jx1ra7rWGLyCUrKAaKF8Qhe2gJKP7ohAB82op345eQHHVWc1SoSfmsJsSXbKDLm%2FXoHE0jlhweB%2FOGjvpIQjfOfXqn%2FsN26Kxdq22qunyYe%2FMta2acT8eGfMdoigtnB2D29LyjBR2NFPzLxNWzZDODLOsEBDM8iHQFbh%2FSVRZakpvFM3K6vdMVNrYBCxV8K&X-Amz-Signature=748ada926d581e7ba494488d3aa3d14a9adb9dea4d50dec5fd8d1603a8b2143f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
