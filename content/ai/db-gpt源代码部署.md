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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NONURWA%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA0HLuipaK2YfLHhnAzp9n2gU9IYlTML05k%2BfhrdZ9ULAiA8C4KI5DP9w9Jnhyy8fy5yajFZWyOpcqC0NlZYv6BUUSqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGBVqqMqpzNWIWbxnKtwD6qcUT2x3MEfpgiMAjeJ1AnC9Q6S5X0SrziITzNcME%2B%2F2iU2KPVRXOyEua0XPEQwLuXek3jfOCKrKAzVC5KmxUHtJV2WU3l7EtK7YQ7D%2B0rSw4PezDIf9KsIAGn%2BQgweTRuleUvw%2B5sgU%2FZISPxvLa6ECwKE0PQ9uPdbl%2F%2FF63yC%2F0JHx4Vi9VpbLchNJxYMRTQ%2FUn33sP6qnXkbe%2FcKqK0cY0grf%2BXX4UDb8e1AyBt1exdEia0JEKjNWwJV8jotyIHQ5rRJc1iR3anSYDa7etSU9a5vByvVO7R7SNoJEmFtemXlBbaMAGBIgz%2BEC3xdivcZEEvBeyKl2BocX9bcMFR6%2FZaQFzFgtgYyvM9MoG82OnSSSfSsIaflnxDXnY3f%2B5ppYjvIHCuLXbx3keTUOKptAbzE%2BEoP7cN6gBnbqu59jMpod%2FADHo5d3OK8GcnmaMiHWz8RHeBqi9KAtHm5HGxcuLe20PLB1HMqlnWwGLS35A3hqZPkrQaZ1xRGTpiaSR1RZYZdWmKraTZ9jB4iouH3qb9okkLITMTIDYGyyTZdECvdE9GgNLczU%2FQRE7Jz0HEG%2BpdXcW0CWNNPHAOqba2zThEN6OJqDw9l5826f9%2BVPKUK59VXAKtJiHX8wqPKvyAY6pgFDzd%2BRHo6AqPFClb9iMaem%2BzTtWX%2Fd6t%2FVEhQ1kBSvYEdTMwgFYbrDvd36eBg8%2FXKsDaDzgYnCQNO9K9O21e%2F8HNd7e3b%2BjmXNGcb5QNOEyupkn2WmmN7cWHPdu2%2BXIZGaWjjvDv1qEuXUvgd0mIJY5O%2BZFia3pTxU4bgPjLgjPiAk9%2B67ej0ox7krvAoARFptIrmI1dpjKySvQpiVYbqdfmny71jB&X-Amz-Signature=d12c477704f2233d13ba034a2ad887d526dcd7d20e3113402a8b3244a7a5958a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
