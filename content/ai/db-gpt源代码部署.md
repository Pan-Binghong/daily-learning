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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U77KOOM%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNQfPEojAOpojMTtyHG91RWYIvEFyx30Byl8m%2BNWyGfAiEAzifUJ2O6c74BBjIcaJFS3WmP%2B8NJ6LWMBmQNPUbV4nIqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGX6soPsh1aPX6phQircAwopNzwv3zahI3gfiSiQo01rliK%2FxUu%2F5GEihBXGofX%2Fmg5yG8plH95ZQv2HO1u8nUn8uqrVXKxsb05pgmVHtsyS63OoxIVBdOKqZQlp1mBiNDg0Bm8z4sLQE3BwdgNeKRrchMGac3zaV96MeFJE%2BW%2FS%2BlYSMWqimayApVoKqNv09NNxKC%2BiLhMwahCosucHEYkDqgxOTIQoE0dQ3eL9WeHTlRYdIqb%2FwGgOZ662BG5aK3pFVgQ5qaNaUFbgmrusa%2Bm88b6BwsJlAraogyapdvluA3Ql1R3A1zST1lyL1MxoonVLyJ4LVSGU9dF6a1u8%2FAMi7T%2FMYGnYG%2FRDBF41t8F67YUI6OCS88AfDMSXzUq8pBRDR%2FpJyUdUEG6N1XmgDrKUrV6X%2BH9KpB7L4K3zHek4c3IzBxgtczL9iO7pF9eIzlbrw9VgNxznDHxk9nG82D9fiEcdG4pB9DeY%2BX9gjcRB85hXQ7H7wMctnVPsihDd77%2BRooffs9AFaqPDEsrGrk%2F1ZhAlWb0NEPQajSCwb%2Fq0fLJjCL33JR5bC9eFKKh1GDHqEj1yKYqd88oIYovDUXa%2FXTYV7VJuC7J9luTijFpZs4I%2Bkl2yGNOHA3R16b%2F%2FHKy3HlUBCrOdXU%2F5MPL90skGOqUBvcaTHu4w7eNQh0M47O7flmCdX4daM94cFL3qEQFnr2TOaf5VavI5%2F9oKlidmjYTqtjq4WOikw25nuarSzT3b2nPHYQKiOB7UD57jyjF5xKO1MJU4EDnNeylteC6zZjR2YqgpWrg7cxWuWrzdadsyxQPvpohvUOI1X1wXpyTQ2xBFUphYaKTFLEHf725%2FvyRWG%2Bugj67HlXnAFkUeCaXoEwH2eniR&X-Amz-Signature=b845b332d2c25cfcae7b6ca5cfd5036eba1f3d7952f694bc402df944e753eb85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
