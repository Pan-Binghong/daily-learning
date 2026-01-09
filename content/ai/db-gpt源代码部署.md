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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6LDUNUY%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T025953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzMupncZ189uocc7KYKu4kG8KSJ0OzKQuqeNpb9L8KzwIhAOs1a8bXarSWaIQ%2FZBUI9WFBbT1uAA1%2B5tF%2F36RAlwFhKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFU%2FweYtY%2F7UqlCgcq3AMXzD2slzPJ4liDIHz86wxEfsLe%2F4bbNgKvtR1YfuUFqDlox7CIolQA8lVGUrIv5Do2tBz778WlJOpFk8JTCrBcJ5w8IIoMMwDyGKN1WsHWldZCjFiaLq%2FBplYOnLjJ18RUDtCA8MPWdpfwaWJmFBN2F13vHMXRP3YUKPYta09UXMbH%2BqWOfKl4eOOd63Si4aNKJZ3SjF9sbI0RohYKZ2NfCK6UlUXy%2F8Bm0fwjevFry%2FikbfnjQvbkYMF8GXfkvuqByW5UWJq7BPSfvqY2QAIAssq5%2FyLtNDHqPiLdIXEYKT8MLzUOTG4DeH2AAzySa3H84Q17ng2y78ol2qgD%2FWvSl4wF0Y%2FZKwccLZkYt3w%2FraiwuZ%2BGPWtYMmie1jP1Xi7JxFrDesB9flCpmJjvrMLlY%2FH6%2F1eSbVqpPYp2JNJf9Y0DtEr1dYRr6xSoaHJSO1XzM8yVupzzaDjgrO3s0dYO8dcnWZqVXc%2FqDuqAqLVdZiBsIPhcekm8Ige82D02zfQ0oYFBfvfOOJ3ybu3m%2BrIq0DItwCdybMBQDqlaujcxWN4VtPmGSQvAKn61jQG1eEvXja9ceAgYhUxorsdP5%2BFN9mnNjLi6f88aliQzmgDJCUKWQwN4v0pZS9WzQTD5xIHLBjqkAQZPrTa4mU2VE9x0MQPoHdDe7fgN9bjZo7ydAVITIHC15BLeO512Gc9QFd%2BU1UU2uMngjqeVnhjg%2F6dzSDeZ8L4a4g5ZYJmmWLdV8PreYEHtQgsrcCOI5lSVrFdckCDPO81LoJjcl8yIAgBcQf%2FDaE91LhOiAGtz1dXRM8kKYZ9JVlVIUn7lOxUP2R3TYb9KXeRxpedEdXliDksYRonps7XK08qz&X-Amz-Signature=45d68618679391099d8de2d111d7159c9b544f172049d1c675be945a77d4370f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
