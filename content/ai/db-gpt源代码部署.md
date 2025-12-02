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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUPLLTTF%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCcXT0o4ZLcEnyTu76Q99ZAMR6B%2FCJSvyx%2BCmLpnGJ6%2FAIgNX1%2Fysp5whAoKNRjzXX1XvAtMFMGJneu39d5fxitj5Yq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDBN53RnMGLu6ockkoCrcA482C%2BXyZ%2BQA8lryXQvltO2TaZBSFVl%2BP73f%2FqcxoY7%2FgyB1igYyrFX46%2BR3zsvgOBMbHCRX8MyP%2FsTO0hdye1N%2FaKoSujnTeEOMupriaLl2qDpdxB6VbkkaRnIIZ0PA2n%2BZg0ADDwlzjKt%2BHyoyZtgOmdztOr1fdF8v8C%2Fazn2YKelCMIw3XzGRP7ZgwXU0e%2FKo9KtPknFok8wLxJPon8IH9mbp3AbG2Mn%2FsstCcgxF%2FdQHQJINgxB2OMCAHgsluhPfP0skMhEXVQh2rDpmYwIs03BApgJrsKqquoYmV77ROV3JXhO2IhvR95yFjcR42GIM0k9BntprJlStnxDSxyFhx%2BIiwCRFGgnLfirD0ttbfPtIdkJYqUq7xiR%2B1EfnPQT%2BOrr%2BTfcRR2YyRpHEtZ0oOduVlMXpYfkeX2BDVOnWOB2ZFELMGsU9LTfDZtRtipDSomM7cSLAV196Xt6vPE%2FeCPyYym0T9dhGqdlRS9iIIFFKHXiZPUjdolkCkmj6leufGh80IH2oXcMBx2g8M%2BNVJ1VpXhl%2FvkFbwx9bejWC6m1rvbsGemv%2BfIjzIQ%2F3gj0Yl9r4KhsWAFmVVD6PqM3i62S4PKgZl%2B8bEQQseeUUYlNf0FYh9LyWFZaVMPTduMkGOqUBjKmqcpUKGPhS7J7v6xl9YRqwZdxpClB6MIp2xO6mPg1PTAtUJeWdY8PDFGpey%2BfhkIXFGVwjlRXNW1fnCkZ%2BHbpoNgUk7UUHuYvmRX01zIYyEjBPuiz2duNykYZ0yZ3PUTkRWHHmblQA4VZRs7OetFqDhWKk5Po0hdgpr9eAfmZ8gtODiUoYVWgtFQDbTagnsHyT%2FSnoFEckAm0Pe0HhUyfpbi9t&X-Amz-Signature=fc7027c5b57dcfdc118c622eb10a729be17cc7d71147e24918ee9a55eb47b224&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
