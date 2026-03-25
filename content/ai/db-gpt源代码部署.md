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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CUCKGNZ%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFUlLN2CD2knJjU%2FjRIo%2B3%2FRu38GpPR7bD8Q7C4OUWeKAiAaj4wDbPExMKB7BFi%2F32odLCI%2BQJKmjlQfAWwCa6YOvSqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2fCcrE8Fo64%2Boy8OKtwD8QPAPBm5eIcuouY%2BQpQGQ9q0y93pjuceq2m1yQ69iLwHZyr2UC4WW4NwZfTT6X5e%2Fsarz7TSuCEP8mff6G7vD1EPyq8njJnVeaJYQ0drZNswOC92PRU1n9UMHkoLBRmG8NVDG6DK5uuRGhx6g3%2BIY%2FPOrPQ1lYfwJJBZDxZlqu1bGqXKYRshxIdqlNrypkFiXKLYpaqy983uvqiB%2FvV3RLgLYNuB64amG3SZYn3%2BI1NBA6yZW6KrzOoZ%2Fx60ZQQEYHr0kFIaWnw%2FdvTabEoUNilZLbwPmlj%2FQ6yw%2BXZvHiV6TD9Lcb2UzgGX2o4greNR5xlxkshvKnSg%2BY%2BycfvE9hGTW7gk6joF1h0oN2MIEd%2BemImYPZXClKNxhfxfGlMJhEj5qdxQe%2FBSmti0RRmR0fwKjfF1ax8BeQXbsb0EYrAC3Lkda9U7Huk3Y8gjVGXBorjn0HqOO6rIttisc7HxMTGsouakvDdWiZ6ymsEW0TpFfZeOe600%2BoYMPf3wil53wRigcDqUB%2BYLqEvBy2tL0NkI3cwIY7HkX0OwDtqATp2N7LMUZbCxNuIzwgjlhCw5iNrQhiQVLJ3Zy9z7Xvlc%2FRHLAKohJ5jCyyp1W3ZuMAqPNo1b74XUjfTF0qYwsNaOzgY6pgHfctu5LtjRw%2BcAw68m0MCpgmkBMIpmQEXsm4nb6mQp64VpK4V9%2BVxB%2FZaluehLEyU97qkwF%2BxP4U1%2Bn5nk84z%2BBNWwGw7syyfgGXUxtF310ALimSSJdwdkmRXba57TVT%2FOhKNDCeeOpwHXejQgzGqaQGVwAFCbnhCGLmsn8PxTWBlJKUc2tCs6PWOYWjfyA18LcZ9OL7Yr4u1gWW35THmYWRImKAMV&X-Amz-Signature=afdd99405ce14cd7dd2e92d96c34fc0e8fc7765469349b92925a404145f3d8c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
