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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD4E4LZ6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQCablaio6bGfFeICTh3Eb4Npzas5TABlaW0mVtfL2K3agIgTTbHli90fO%2Fx8WlG6uFLeaLp5McM8jbeg0lRv48O6R4q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDFZUNNv%2FeVCUzcoJtircAyFNoLvT4XOBir%2FddktqaPDYnNLa57OshVgzo72c%2BFXtol%2FZ714ZRStBwfBLsQ0Rf5nsh0roZGwj7rcThyVx6dRpWS0zeLmVgtuD5dON5gp5VgdSbVQmxPle0qLTiQUKW7oEfZ02JD%2Ftq%2Fm8Znyx18Z2FqnIwWz3j%2BWQ9ZWb6sJCStab0Tb%2FOiBI1R%2B7fePTMkJHrw8%2FO9x%2FXcqsxSmAzRX0JvvmtTsczhgEe4vvHvVFQMb8hVdhvI6ZvdvLvIrGc7s3%2BiCEa0LBKKt0J2gFFznTEQf9yrgJldSZpfiMqNdeq8H3c36GDRsXM5Y7cApEc6Ccr1UYOpWobjzNFu%2B99l%2FbbIlVrdXJXrkE2HwTwkJs7RHiRINh7hTB94tKMa8LpBZPNX6Nd3GNI7ma%2FQn9dHJjs9ltF5my7nsO2hk38ICBn8vjZeGOM4i1dJ9d6fEFkgeNkCZTBtx4wCXq4Sz%2FYUE%2BJtxbaCeq4U7M3xSol0yACDboSRmosVE9iFlHslnsW176%2F6C9iKg6nyWBfy0csMstjRygdlpx6SmdAd5uxPebDbQbauoH1RzWKLR4ow0fvoSqYVQ7RcKNm9i7JcS7MN8WWBiIikx59QREAKjdb6ik2NhvbHMtMFBkRmRMMLCM88kGOqUBEGLL1MlDEAVjBeevamSHrhzMcIEo%2BH9Tb0H0M0%2F660zUiHrM7gM3Rr8tPn3p%2BagSzJw%2FFIalYhmDhWdgM3N1NvmY7hot0v4UTohwW9eJkjir%2FsDS7DjM1%2BYle7w0ELyuBwAq3j8cUUKTwPodhmZRjmrsfliy3DQNI%2FYRnvAFt7YoSx9Xq4FvtAU1s5ba7rmnizXo02YwD260Z1RLReWRj5x8i5FB&X-Amz-Signature=123a190b6881c38cc58961af039d089e6534bb34ffe0a7fb0321507d699a0f2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
