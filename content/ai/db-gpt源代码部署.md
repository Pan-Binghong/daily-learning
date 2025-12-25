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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQKFOM73%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQDW95y2I5VjnHdjuI6w0AuCY0YlYjtd%2BszS8%2B93ppXPHwIgHPaN%2FKufhKZhXDSFaKWxVU5%2F%2FAmXLzJlixPmtY7GEdwq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDJEyyF2kycTUR9UuASrcA3FM173QUlTRq571Sku%2FMJOzG%2F5Xo%2B%2Br87HkHU%2BHuKogjkbXCSChXElONqyTWRD2FwaANrCjl7opEVtHOYNemgUmNp2nXaiJzLH%2BivZ4cheUVyW%2FQEbCo0YmdcJJMlrtQjN01FOL9eSli8DVovNYH%2FUpZhvIThGBH8DR83N5u43GC%2BAgaSidNtin%2BSUgKB%2BW0QqfSoKVrsxiWKhb2rUzwXj2BEASjz%2BXkU9IldI5%2BgNMCjqewXV30vPgqrq2TPUzaSYQPQ60c9o1A6ugwSdx9BACAPywqKzQtHmwBmAX6Ml12ODKX6K2pBiwizaA0B0GdY5dvPqI8ngl3enYa9u1UKRbme8rQIKTsr%2FURPkTC4q3JzuAFHLHMydhMcu25HzMVvG1AUAqZweUwnjIWDpJe8LSLgCxABFMnoZV9MNILIMIZBizLNoO7nM99jgaGXlPUpzdeurCmO%2BYsPCX2Cz8wyL%2Be6vCZjLfcAmueKCzyrol1m6ueHvsr%2BycKNSz%2FjrMLtDzbEsop5kr6KwzyM4p45W5sOInmwpN5jzHuZUXXsY%2FpHLLmcxNHWZa%2F2fVomowxZNcOIntzGiC6hnUoyBBKKUjpvkMJrga0HZ%2BP%2BK2VmdvUfm6ntlrt2GgTfz5MPymssoGOqUBY0SKaRG76L29v%2BAsxEDTosLVVLB60lZA3nGauQ9AeogeMMXiy9rfKstCw63pwA3tNuxwqs5xYOPohSzEB%2BAvvUwmDdt9l1wOyIxUgQrXUczp2XuB0Ny3ZtuTbfm4TZ5xQBoIeRksBmpWg0UniNgQR%2FJUJAZc%2FpC%2BzoUtH0Ou72dmJ0FMLCRgZD8sg5JEL5DO4PKd1FWjklRU3jIIsZCkslNBEiLG&X-Amz-Signature=a2b200c7f997c6159d1bb73f983bf552edd9fe4468756a0922def6efe054d2fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
