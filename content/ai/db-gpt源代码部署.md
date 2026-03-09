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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKPRMCFX%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIHYvOagc01BI6wQjlhmGC99Obp11XTL3x9%2FBOGuRger1AiBPzvCDy9ojaYYEuBdJBtQBCC9A4xxfnhl7JqPFwAnEqSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMOU8SZKUl7KgPCjj8KtwD%2FKu3Ikdsa0DQvWbXNICm08NtNzQ3Mhb6%2BNGnJVeDF6oZB7tmvGXtkew5sTNL45K%2Fq4PiXd2HQmYeubmCsgsNjkUsp%2Fqq21FGxPn23717YNvKmrARZilnAvS79gBTtfbnGSWiFfhH9jAqo2ec2k%2Bwd0NuyVamG%2F7XY6XKAL7KRM3PpagRTZ5Iw1d%2F1SJd8OEgVBW%2Fuo2oJTh5iJ68MtX5sR%2BCzfu1OyppnfKCwqk101diQe0%2F3W0FIbL2K%2Fn27%2B6KcWVzA%2FOaVJHBJtIDiFhqUP1ivQWHBbpyXwLSHRbjUKvKo%2Be8MjgwCZPwnmgQsbDJxk0ywhXfEJvN2W3YM9aWVy9yR%2FltJSFL5m3id%2F09vCsQnbsB%2F0fYUWRet5QEDC2ckNGw8xGTfJWv7iMsx%2BOU1ltVL9iCpVXhAPeyBXYfE3u8tbGLcx7B%2FvYjiWOhReoukuqDy8FtcAAfvSuyAYM%2BmXaQXdnHbKE7G5iWVhzWT3As2dZ5vAGdUDwkKeJ%2Bx4ngZht5FP4jEyZppB4SdRuUTXOhFKvpd0GIgOMC5VTtCf6coOJARw2LWbvrXnfbR18JmftNEO%2FlH0xHuz4sb0bwDTMzvpZRjQptIHCQ78MB5t8E7EcfQdOo9%2Bkv%2BaEwmv24zQY6pgHY9trMJEQoOrXcFWaUvgbtuRSw%2FYV7%2FgL%2B0Uzov57b4GwpMbM8Tdh3WRYT0rArSNDhCFts4VPfaYICggdKElXrBDj9w1wytV64BK84UKbB%2BXMMqEKskZ7OfBeilF8eSRKAE3W3SGWjSYFSQkxJYRxXrbvv9Z7Trt4iXq7bQFc1JNnuUCNRmfRbUyM2YDMxP%2FKugQxfWMKrVqT44Fbh9O1v9pJpn9Ud&X-Amz-Signature=1d3011fed14f287347c287d8f9f03320e2c4fc06ad7e757966fc8901b4f99ea7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
