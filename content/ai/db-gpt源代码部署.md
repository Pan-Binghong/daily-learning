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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSAB2VGF%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWG7nLM7fV0PI%2BQo9g7R8m3ZV1x%2FUJ11irh9XvTvabxAiEAm%2BN%2BrsVqMmppiBQuV6oqdj9VUocyzWxUuLcLFwDbqh0q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDFEBQhwoZAG3cJMMGSrcA6o5pDeXjIH5WyaWimsTVHwmC36MM6al41BCKqxeXZHy7zoGzVXu5yLcEkvPWkglhif2EU4vkYCJT4bjHuZTSv2KjT1Dif0th6l4kxFl5Z6yMWS9H%2BTaKeCJvMJhs%2FR607bmbz9xOiuT%2BMEbHL7MZmefPP7FwBOiKs1MdxgS5lUcJdIsTl5N7DlmwXZIU0mza0Pt6SZGS%2BDyXvbgf1CYtfI6hDHfYom04GAAcdmSdS3YsKTBTRmbvzWKO%2B1LXD%2B6y6CEl4wv6i%2BWVmGgUdZMLlOc1h4JbCciLYpIq50FdFBWfpfKDety8MTguszkPTdRKNWrNFCpexmsXFxIQIshY7Wb6hf71NopscUatPN72IRj3GqnzTpXUL756Gvvqt2vPNQ6JofVjzGu2EgWG9A3ANW8%2FFHTooL95fopt%2Fm2JpzocpQWxNK2yd%2FrmZ7VjAUXRRwPpl%2BfhgKELf1S8u2SRStUmtLx0%2FcVBCfcfJlrb8iP9BxL3KD8ysGlpkybhqX9WgKKIbKW%2Bkqz7Ru%2FhiLD9IG9goG%2B8adBAePOgqnvTqIcttbyP8WAd%2Bp%2FE9pg9zoWHE44dndZkDtzEbm3UwhOIg3ZOzo6vFmzUHnvDpizvi8Z3XTD%2BuRIaVdXN%2FPbMKGw8c4GOqUBDkRIhmSD5KCVVHWdbXG0ra1OQcvVX%2FJT14WHe5Ct4Y4DvN6pyKOZ3hLNuDJ2aB4tlW2NLTrN8%2Bz9%2BhSY4ltqqh3FD7gP0jvyj5piokRNG4B%2BayfFcpPWgDAmfFJMqfphYuavR2NABlXOPvBpJAPk3mSP%2BR9QerEWheIEoPT6Roj4VSQ45u2CjWN9ZrDqDRShvoK102g9olvc8167w2t%2BUW%2FzBAXf&X-Amz-Signature=531759644deb2b21b4f6dedc70091f65901eeb197a7db43d78b44de80f6a7668&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
