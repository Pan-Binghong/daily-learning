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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2OJP2VY%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBhfoQ7BTGtWRigGWUuEoHp25TzVPnCo3DpUCyV3EKXWAiBRuranPo6x82Owipw5%2Fu%2FSKO4oEbzB%2FJpskiUmNCvnQCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNsGi4uCj1kNc2nPXKtwDC7HuZaW%2FZR%2F5fdP3J%2B%2BuuIZWdh%2BL8qyE5YqGcb25engfE4U%2FTaDNqWHCryk%2FxHMpNa9FYRcJdnM8a5Np9RjVecP45FXLxpjYym0NL%2FmIQX8tAPbQ125uwy2zEDmACjPLI1ElRGbg5y5wHjJhcRhGt2%2BZ6UJK1RetMn%2BQgVtqnoZIHNGEJ1OGLmfAcB111GwNkS42K%2Beti6qRoFgwIUioFCYzDkF55InWMhI0j4DBMAwN5kFampclaJMP2JdbL9bT%2B3RPgo2zE21r6EwNSgoyQohvxaHF6lC7fXABZpA%2FXlE1bm%2Fxmz2U6XFwgx59%2FwlwI3kNhDB313lIPiEfP4huJSKCsjVfXzG30ovWSQiY78TssUfBrok%2Bm1EWK8Jy7JNaw0exEjk%2FQRxP34ew3b3GsDWdWg2nxT2NGW2tmQdR8xaJt1orN93Zt5OoJRgAJvuO53YrKnimN28qXFIR8IfZx83lSRoX%2BqbEd2hB2E4zQYtLtHrmp7XuJpgFFCeH2UDre2J33tQLrWhWczeZNW9KufqlpouaBPbSeZbrS4GTSLnuqQ8JR0jbSEBbuUA6fSXf7Fzc0C4NaPq6fkubeSaoijLzEhq3A%2BxW9v1Ghs%2FPCy4kphVFBnnWfpjGSdUw9MuvzAY6pgHISQhPsih5qC5S5c2DbkVvEARxphfWq9cn45SIbeFf2PjDuNj2MxqS57aotaAFDxmt40AXzs%2B%2FP7AJsmGhTYghMxobFitdFfxbZfqohgKJCwFAI%2BxeU3pmSzprJURutRScsfN2MT3xDkjQviY%2FrcLqVpe3lOrhZirQTBrFNq5xIVrzv2PuW9fjpkNPRcgfJhCLXaT8jtowi29FyFNm%2BIhsens8ko62&X-Amz-Signature=7ba5d2b1970fe2666e9564aa8123ed83e70c09c45d27406f5d58e157494ba65e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
