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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQTE6BCH%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIFoDvKxYzNEj3cNZfeeBeZ2nJYwb8B1JzJaZkIRIIL7nAiBLVcJZ63wnCUpVoKpJqvvfeBqguKUPH08e%2FgoAVkidjCr%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIM6clEBdNHbVSTMnbxKtwDL9TmHYBDetx0UYgS6N86Q%2FncfVa6%2FIKjkrM1q6Uqsrh5TqX%2BBDhisWMv000LpynEHj%2FabBjiGsQO4nYY6%2FMgrddP2OeQvHKpNKj5l%2FX8IcdxIb%2BleDxR%2Bwbp8qfrMBtwM4WM0d0CL3Qqx5s357AVex6zwMQbITy4ZOqdtiGrxvxxAGtNhvyrVlzD6Ee9KmYbneSu6hgKVnTxJZszblNGFqWHPtgsnMjRsr%2BKAD4asWjhto17r1bEkIZ%2FO9YCu%2FCcc9RD6btN%2BD8HfTKdoKMDN5LYvPWfjvMnIl2ouCA0jlOn9z7Uae4ma4EU4KCNGFaATutd%2BIxD%2Bh%2BW%2FTSe7oHYrQP%2Fr1CvB8tQcbpCD7v1t6MeoyM1mLBPEG0pWOJHacQMKRyuCbxPURmFROers1r4IgYR3s%2FZqXvcA0F0EbUcXJO%2BB6DcHUfw9O1Ljd1RU1YDN%2BBfG6OF9IIRg%2BqCyWuwQWtdMXOAxZlI6b51i9dEUbRAWYBvAnaCo90WUpaPfxtHJiLE3PNpr1TT6Kb4KKxy8V8c3fQgK%2FTNt4Lfn6u%2FtIMk7tpBNkLnA9s2fDY8xb5VrCHlSckU7UzMRBebYw5E3t9JW4R%2BIfT%2FGzptTiWaGq0KvV1M%2FIbm8TIdwfMw%2FbDaywY6pgHKXkyx8HAEamD04Zkb3iGMVzYxI3KB%2Bgadx9YjY7BUsecr4qpkLShzk6bJ4LvZSKDDv5uBjFzQVusGSicI9YtJLvuDrRmofdKAO9U5FZOx6cmw%2FKX3pCAD%2B3f1yyI3vpiKHKOrwBSdkJB36n4Etj683SocDS4wJtreGDG%2FpA2VAphlMfl9YIiOFLYmASN0WJ1dvjJrBxSKumBVhoWl61OJBs5lMpXk&X-Amz-Signature=5937a0806d76fe59dad175b8e3610442614dcd9630dc86c75b3bd508c1235132&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
