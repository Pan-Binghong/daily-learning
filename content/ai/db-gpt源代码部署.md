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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZ4PLOVJ%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE5n%2Bth6mGyqOSh0Co42g7JU0V1Vv%2FSOvv3UhPhYmY1bAiEAh6kvXsIkUcVcX%2F2s307cdRfcBbqLUMKNzXds7LES1i0q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDCF0K91FoNNdzrU6PyrcA%2BjpPvBdpa7x7ftIp%2FC9SRGC38HaxfmiQdU%2B%2FdwUV%2FEXPn%2FJw5zXGwllHewTZfzrxym4Tk9qYlTGO9ki8ZJBzgqenadUjv8fEU8SV59lI8Mr422QBKqPbFL1Cggw9bFjoxlZ0ShA0hMFGzxS0zroTM7rjaLoILsA9gcWfVbuZfJfqLGLBj8Ijj7y6AZTuhUa%2BsqaBfZ5FfClnE%2FGy2wfXj3rb0IZgIDHrhzDMBdVtBrJ3jRSA2eBzvi5eN2w17y8EsOBrWhGJRDsq9pyx1nw%2F%2BzbnRp9hSoeZ%2FGl%2FtFwAZl8G35U%2FDOnNPrlwWn2j%2FgO2wW7F0bPcNL%2Fov9XY28cWxN9i1RLL7A1jiEWJHmqPsJc7yFC%2BZJkCAFxAT0bBMqgg4Y10WTXF6jwTxsIZs3cMYF7S9IgYPS9iNTbMzJjfKAV5ug2CVomQ18gr7ts38J6RdtcdDYzvfFrgyFCJpAURjRx7ze5oGB2ZxsJDhgduQh4QWNWnXCV%2FnXrc0L1u8t57bCd8T70djkZywrpOz3q93aLpGVw6CNBmpWIr7LGsOoQ5kI6jD70SyYT8%2FF%2FnhAIUrJSz4wWBkMYM1Xxf3dcAUlYs0hUS9eICiAiepCI77mVrJjlXADQjh8r%2BZ%2BOMPuut84GOqUBDxu8ghXSyaOiYO1u3iiTAF1B6t04QQqX6pRQAKqRJx31BR0XU%2B49lEvjfkMm7jCNfRE4KxNxOSJzX6eZl1MyAErngfUsdYymFZNbR8B2rtqq2DqARG1hkyWf6qzPwHqIOIa5ey%2FNj9T1a2iYFAMZm2TjLQBd3GPcIfK14nzOArUn0gI6QqqdEuIpBJHgBe8ft0inQknm%2BWSPJziUXTPXYsto5%2BNB&X-Amz-Signature=cc7edc62c1f85170b17bd445cee20e8dc8bc57eaba4017f9acbd98a305029cab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
