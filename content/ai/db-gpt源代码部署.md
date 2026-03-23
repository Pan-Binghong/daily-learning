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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV7ZORJ6%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCo18oEeSclLRmTgrzs0I5ZFP4rzg%2BDAVgxugeSHjkmhAIhAJs1W3xd%2BJ1ZtOcbZ7crwheY3R4gbpOHqUe2JHQ0L0vZKv8DCHQQABoMNjM3NDIzMTgzODA1Igyjd2ZZ99q2yCaL9Osq3AMMLz2ke0soRNzpDA%2F53ALl68CmtBY0R%2Fd4DZaJ5ykk%2FzTTTnOh%2FRrtdvJrA8VM87aRBM23ym0Eoh1VDKEErJqaRNzNuLVleXqbEFC8yZRsaPsHBqVRJj4t2Db30oyXHtAVu2aj0%2FKN%2BixIgM8N0H47qN9KAu7GFkAYGTh2PVUxTd%2F%2FwMCDIi2EyV3OXjl2hVqAohQdXeyN61%2F6ITKjfiLmhaabK4nCs5csl1m9N4z278VglXfjljHOt7dxhSWmviLbPdjZR8IG4tcJf7zvqPDdyhWOqcIrt3KdFGStrJorRHwzWDWxKZPkL%2FCf5WUIyfTpp4RIgkMoZ89%2FUEQL1Fagj93VDnUCRzeyItRvFBommBfuvWPVPS1%2BKKr2F5fYlveDIhV9MJv8DLHZEvY88QO1bai%2F4f5lP5bmODhK5h2KBfc0HL7%2BkQFOp9Nh4thTNNzkcwMLgPUm3PjGMElDYzt3Xlpo4ch1iBOVJU4v5nv5yurfFM5dkuEsmHX4ynpMBfGMVhIZgXFQR0CcRg5RKlSFBPlJi0XQaTTGXSTtAshY0e5E9xPUrOsXBrWxeuhyMobkoB0FIk%2FQu36jQGsTxJjRSmFCgRdNHB5L%2BvrrBK%2FhHOaymOQG%2Bmah%2FAyx6jDn44LOBjqkAXevaSuEYqm%2F2nGWSYA%2FxNP8msTYUFrAHI61mIhbkQTvOdokj52OGHS4YTBfUSRDeG9WDCTw%2Fe9jOgxcQi2KPaOZCPmOKwgAnXxVQ0fdzGWnTsp3IVyCpaen4TVvmSg4oiSVg0Sz9ess6ZEWyt12dY%2BrI59HL4eMP1pRKDrL9cnivBRbUc87pCA2Sv4tOewuJ5ag787rMG0rVvvtdWK%2BKH%2BlsnDo&X-Amz-Signature=3c37003a50d50107e9d9a4a47d7b96ad6e56947bdb7ee85204d13b58c536141b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
