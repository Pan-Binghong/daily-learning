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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWC2I3V5%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAIwuVahXe5bJuTMMTzBOppnfmMJEJQCR%2B6wmdm22xDQIhAIk%2BFo5Tl%2BCEsDy2PTDwoSaPEHRcNMFLme1Me3AKFgcTKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwtBSRfyfrKaqDrxHwq3AOZCE1Qo%2FXfwBY0kUMJH3m%2BDnranDlwxj5RIH40%2B%2FdVj%2B0prtmPgRdbejcfEbjY79AW4XUAEcxgATd8g4Hf5eQ%2FhU03tJNImNwCHc9m6b6BqiroxUyyENar33xx25yDWZU7P26KUK3lDIDJAHRd%2FSZafXFSIc%2BAcmY9YRCa5yJYO5TyIr3O42LkJZA9Xgo9%2Bg4WOUWLWDHq55RFGfvU35aksEqnt%2FJyorL0R7HjXQZQ5e1b%2Bk1f0QDSLGINdCvRYbiJHhzxCbQOdV4gCerEhc3wTfTKyyORSOqhQLpc0juvlizzYb8oPFYjSkNiaBTGRimvB1FsYUagCWhqwrVgDlL6ZquJkBoCg7jqw6VRqHnhXTjnOpjEbNwFp95u3iUBGCSZ%2B47go1HLXmAumG75L9Tb%2FofC9G50bW1j%2F8MxVxO1PXBUvl3CTgPnaVNKBl1cpI7lqwGz%2BXxyzTbGn9A7GzAPh86Z3WToicJCZRAO8XObTIwhPJVrsAlIH3trfMiXuF6WuctiOurc5teFq2ZgFhkrFfR4Ql1WDPtSGKGIkOPweNV7NQiDAhOLwcbw2Pp5ue8LxlymnD4ASfXfgU0re1Ag%2Bg%2Bm4a5dPRXtgQv18kradmCnzUh5lHR3CIzEVDCz%2B9HKBjqkAS6rpP45eUGT4zoafaA3mVwWbTBnKMJl8CQeJm72NG%2FtTNcryanIIiSsTtPRA14W0sS6H%2Fa8j5%2FOGoizzhbmPghZaQJICh2FQjK%2B%2FNg371WnjktmOsYcrp0VR49y7mcJJVNuhzpgOlGkikXZYgz8TQyDWOXxDj%2BAsrD%2FJiWP%2FR3K6Pi1ZukEPb7LszraASepcfuMut1i6daehfZEpiCvRm3dvXCy&X-Amz-Signature=12aafbf4040bd22d72fc9cba738f6ea06e755321eca8b6a550cef954b7de25e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
