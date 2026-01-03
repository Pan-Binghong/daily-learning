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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPH3GYB3%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQClp8ysChoXT0ROfo2dZSx5gho0blCrGpVkfAEjaBrHdQIgZcXBgRsDmkWcjh%2Flw2eaG3CbFReyC2UfjdNPZLbK74kq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDK1pf1OoSEPgT%2FnhsCrcA3QS431TV%2F2zx1KWcorZ7wpA6B%2Bs44Viw00q3vJZWebPtxDvi3gNzw%2FUW1OLHaBbZ2t9pDkQ9iGvv%2F3ugpezFJ%2FUf4NKvEZGK5s4%2FqlA6RhdJ9CgkHdMeiQ%2F9YEVCH2QGHP6UN7kgEcQXysOGd7vN1mmKPks6Gk83Cbpf7sWRH81E4UFJ5FDQk%2F2lV%2BP43uevCeh0rylWA2FgA%2BF3H%2Fe3ujA3owhCrWZsTrvB9CmVPFAXh0fnXDwO56no15lB7yZmaGKM3x7emHo%2FLVCX5XS4OLd1AJwpE19wR90NtacezGvST%2FEztoXUKIXrtINS24QiJdXsmw%2BeWOyI8dAac5UHLzf8yR%2BEL5V3vpEcr%2Bk7bqvROcijQzEpqpqJQv%2FnTAQdaQ3WulAX9XasX%2FgIaXPG%2B29AtJfqKPpPc0eaZtbPTDFIaoUXyBQjn9YYUw2vkyUBrEycvIzLmpE0tvWfYilJBbg%2BM6r6atKToyuBhpf3dI4VPY4Rk6hcYKuKbaBKP0Rkfe%2FxITB1D7L47Q2De2a4VzN5xfuwncsPeAa31GmpTnFhPqZN1pJy7AioKFDOUFcAFvdPKvuOQFSBe2SCOHa56YetCoZgQqtntwE9V5ksuIRrRj%2BfTT%2Ff8TzrtFbMJX34coGOqUBHWumfO1px5UnoK8NQ29ttxFAgbbMjXxSgfwdiLSnt%2Ba%2FyxSVXx%2BPGuY8qPQ2zZpkQaLTgsHwfNCJOoeY9Xufp9SV%2BE%2BLfM%2ByXWGyIxzCTbQjZb1gDZiW%2BeCfrmS8ME95W4IYQ44Bpzop2E5w5L2HSCDMzFrIPVINqlFY4aDkTWzCigWmXG568Kee9KpoRGi6BRp938Lzbx3QoUcboX1e3WhYgr8C&X-Amz-Signature=279cf5988d03a9bf351c5d16aa53e144f54498be5bde1267210aa33b1fd44276&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
