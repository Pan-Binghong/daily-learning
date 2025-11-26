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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P6DMR26%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLLY9m%2FKZNoBTMRpfpZ6R2VB38p7himmmX%2F7zsilcI0gIhANFg7JW%2F7D6hCPB3aDW%2FDF65RtXw9SE9m9TbebMJFoFKKv8DCHsQABoMNjM3NDIzMTgzODA1IgxPPodv1c8gpN7cBY4q3APa%2FBHmHXWFbelDWbO0X0wppGqOdc7U2dp2nWcgL3tQXoZB%2FeqCabiwUP1CALbkuVhMZu5uLKAExeKejJLF2%2BhBtFWaNE0OQ9id9uSCSBN8EJQ0A455%2BgFVrnI%2FlIx86gxtEfMNew%2FQ3kmtX8jbjqPRGFIe6rIbHHNM94YrDgxiQyP0uiKcIXhmimmSsz44ASznpwqxdbn31YnfOg77VTYrB0sNQCbpZoMrOfz1wSYR4VZowsxsYMiCFmTFI5y9wBiXBfZQ3hL7wMsnTvJ0BaKM%2BpXTatPGLjsmRPuNIX4BHV8D4UT%2FlRRiionSNcyaMYAIHS8bolqA0ro1brqJ87xLHWirh4U%2FS%2FVHg8CDLxYdjW4PPeatCbyvVBIWbhzwaFJhjPFMqugw5FxSA3vP3SS1V25cvTVX41gFiT8EDJ4V65iY%2Bqkh25gKTPWfKq%2FeK1WbiwlGnMJHMjJxeh6xji0s2Zttn5pOiPG41LjVf%2F0aQ5oPVqIQR%2Fz%2BbmcwQFAnNHFGlnpKni5ippIOqXDXUQ3fPPGjA2d5JS50E8MX7cTDfG%2FLgrBUOFTxytGPdiNsABHnAWN9pT9whNk0BCbHe9ckhbVJoAZC%2FtofZGA%2F8Sgn4HslV9rOrau38SkwPTD8spnJBjqkAa15Zy3T6UiPfqu5H%2BzSSiXGmFCavF%2FdqKCLCuDUvW0l62uvdwJfIhU1dYDxiT1aYtycBPdKUJ9Dq0%2BKU4SXV0FABv11PhdbPKZ%2BSfoIO0yQlgfH51Nt5UCTfpojXvscBCc%2FEtCgrA9pbMr1TZodWZ%2BUU7jb%2F4%2B1qyV0YmveRo0UIDzHrGbl9Xt8mQGR%2BdMIqiZ5A9kGZYp3o8I0tSAyuTRXYVnl&X-Amz-Signature=4a7a25541af14a895206ea9f974bcb55466171b9134fe45b24d99bcac02c96b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
