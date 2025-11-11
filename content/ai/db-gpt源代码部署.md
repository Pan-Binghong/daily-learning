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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAQEXQBQ%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDZhF6sXjMi6iuk%2BMMMK1C%2BDBTBJ8ag0iLLf5HqUUJLhgIgO2ZgJIjFDTK77q5rj2HuWF9ReemJ9Hk2VOIe6bJlNs0q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDGqkcBJHAbX2FvKPrircA671aNnKRtA5TWvLwReAL9F5nkO%2Fb8iuXQUBhLYmPvJiuOJJxRDQrW3sh%2BvMb1N%2FzcoZCCgM5acRiMRid3tKK3Nsb4D1oX7Nze%2FYPNiTk3DuRUXcPQyyJPlzTXUw1Vv0iCVB8QkCBQSJKCsBg%2B5ftZdGYLZHeGDYY9%2FvskLhfrVP7u5rrAEA8qYXG5FWwAqTxUmQcvEXPRw0uNI6bjvi4Twy9yQq1xMVN1ujJo5cm%2BwWt7m49eAexZJlwNgnHyJrGxJthQKdCeNl5%2BYcR8qAfcsxLtjQNEozgp0hV8STpdxHgOA8pDP87MUU3HEU0%2BtUbNo%2F7AeG50nAtdEZIlC%2B7SOFhnT0BQJTxmYouyxp5Cvuyc7%2BgBu2ckXj0umIUinA%2Fovkcrx5wGea0qqI8RMyJWuQXt0y7A8F5VhLRD7KslJFCbjE3J2s2zHDhWO2aO4f720OkwzkMcHPi%2FNiu1Z4HWo75b4DL8Y7ozc0SQq09DCmIXab5uE5zt2mQjb5CajrcKPRwRbwq3qUrCo2lfUR0kINKmD4E0xdWZ%2B%2Fhz6chUnqwY%2FpDULHDjYaD1%2FD0I0yGle0ylJJgyU5IM4LCBr8YnSRIH7wRuAYr4Hni1EFUknuuh681I4JragX2ntxMMq%2BysgGOqUB8VY%2Bba4hbzBIjtCL3Dvu2%2FNaeF5gN058%2B5fYP6UJpCV1FTDaGMzLTFhmIK8acvZ4m7mdOZXFytvnJLgOoOInTyGttIINWtjrJVzuvsUnj7TzGa9N%2Fqi%2FdLgfAmQG9hiNF0AUbVDimNCakvJBMlPWbFJhYOInDhh5A5aU9dDgUmkIXeXp3X2Eo%2FNesFt5vWOgU7ea5s25QYQYf4jJdD%2Bc69kxn3QB&X-Amz-Signature=6c5c098b170ab7e198c9ffd8bdf87d50292710403b1dfb36fcb0d813f01839d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
