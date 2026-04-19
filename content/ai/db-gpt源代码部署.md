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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEJTNWCT%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCFLSBP6eBCrx295VQNH0CvYQ%2FF6aAvMdewP1d9cy7xAAIgR7IfIatSBvmUJAPbSUJYK2lFK2Z8N4ahRmamFw8MVDoqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKcJ6um%2FkZKR1GECfircAw9%2BX4mGpY6PavzvfFMxJIw3hjrP0cZQmGQkFZpDnNxGZjHKmgvuvYlHZauli%2Bfrp0AT9XMWrDoyw6LEKhcsrSZeOY6a02aWZqLLiv2N0dqhnEwcDLX5N9Xhb8oaeG6uMyNDkWW6VMKF8Ql%2F4jIWwg9y6y9%2FEdaEbYCGptyCvNwsVAduA%2Fqz2QtPw2xDb%2FVNPDdCGp%2BNwanPq9uF%2BtVVA8553KrGXWQbs9CNeNvEDXUWky4fA%2BYuf%2F%2FUEbyuFGysU0pfJNPxco3NYpQuG1qv0s8j8tYAwzzC7Rl1iAC3KlKZy0R5Ice1QuNxUtmKQKR6gHmFz6FpBApQrBs6Teh2DG8gcb44GCVlri3ZLI2cX4lyptgzm69DWQFYRpB1w5QvbMULgoUkBarqpsh3HwJ25uT8truDuezviYkMQ5XrOVQr2bJPv%2BCGKbjqo8gfG04%2F5cP%2Bj65WBNdd9JeKHIkrTKwYS%2Fy6YH7rYw18P11r%2FqqS%2FZnwIN8mGpMUPoQVxppXtFYvJpicsog%2Fn6AjUfSGAE8biF0Avf7yUgpYCjLOjFsU%2F1vN0XWEgr7Bzmj3fR5M5cBKGSJwrnJ7JdVTdK%2BbHNquIrRjgnw6UJudDjKSwTrQH7SZXVpTvHWYZsKcMJLdkM8GOqUBD%2F6bm1SKxu3X6CpSu9vHqAlHYJwaP%2FTlZ0bZDfTidFRFAp7pcFVCse8T1auEPuyivpX5USZRW%2BwHxRwDT0iV7VFXZDav%2Bqz71QzXeIawy6hPdhyYtau8SuRx0A5yPnqWzeuxoGvwmGXY4UmWIgbjBNFc%2FxzfjvP99IbSrfDFWvtIUlm8Zgh1Dm32v0n6lF3QsWfhACpV5OhllXK%2Bo7zYcKpUgYuX&X-Amz-Signature=f26a8395f95ddecf92ea0f82d06e56f740e53823d4f904bd3e88d607aeb81b53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
