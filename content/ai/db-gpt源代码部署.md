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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM66OIDJ%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCICp%2BkXJ3%2BjdlmQZRYBpIHLFkyq3OGM5y7CsZXDoattcSAiA66KuLc7ZdsdehtfILe2BeiOAJw0DR0vilQeOrmJ7RQiqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8DbF8RkaPgBBBEJ%2BKtwD1EEqZiVtkXIhiMusgVarrbdVT%2F%2FGCYs%2FQ0hs4bOjxXfD2UviKH%2FDPRbqTdPs4%2BVlIasoEWDMuEeUsRCuG1e6vDDrBoZPfSsvCv%2BJjFEDHXETaG7KdOq2Lnqz%2FCMD%2FM7eRxeM6AYRY0iKRwkM6vEgM6zMRwZcQSbr2GzrjNdIGhwFyqV0ojHuCEVpI5r0BBAoXpyvnX1fyiK21JGr8osNjmEw5vHBWaqFK6awH%2FLljRMl9ZQHpyVEvT9cjjT17Uy440vkG3aEITQKecGZvgjVl2PHe7J%2Fg309eLYtjTjYcTJqJaIy4m8ftD5%2FxzF7uQFh4bzWzF7OBhQ%2Fo0NfwUni%2FalZv%2FbW5zw960Kadbs0Yw7bLYgtDdo%2FvshHWvcJfTNH%2BtoAsQJbRkVH%2FH22RrHPKU8zLSglWK7l2Bp8YHUdH%2BV7cW76N9jIKIKNBcx1wDiPM9J6VUZBlN91stSPJarOoUZuloGYfi%2BOsVgW01s85Ymg3Chx7RTFmbM81nNRtBOhjJGwfPiC26e5cxi8zFWJMC29NGDGSX0aEydPPK2Vlmgr%2FPUi1VmZv1p6i2XuWgStRLYl1hQmda3VSLq0Cceer74B%2BvjxalHWJ%2FGW812KBLUDWYTMh%2BZOU2C8D9wwz5K1zAY6pgFC7mc5azLDGEQLYVfXkPa6hGbVYzpf9Y40D67hip4K3yFVp5x9TTGAp3LTei%2F8xsZVrnei2pOciE9dwe5TDuKp6sisDD5JaZ4wBBeNPOV2Rkd8s%2FfZKu2vrb9VfN875cTiHbPGeidVQAY2wlznV7rcJ6AycWSyjlMzoAKv2atUIgX%2FZAlVCkG53WHN01AXzwbGUaFyJ4yTaqSwU62Upu%2F65y8rcL3K&X-Amz-Signature=1823977888a0f09c404717d868572e862f64636f3cdfe9d7f36562211ad41f6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
