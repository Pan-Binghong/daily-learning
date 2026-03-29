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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI44GH5E%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIEbjBFgC2hG9pVwH7tqSPQAxUXW2BOqiAnue2ZlGJaf9AiEAh0poy%2BYuiKHGKY%2Bf2lGAUoodsN38aaECOmDuLaQFdmUq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDGAgSREvOzMNfp5geSrcA0itLn%2ByfDjW1QxpQFIyTq4HmB%2BOvh8rNikZflb8JQR%2FeuP6qI7rNFHqAsrenHG4tIBFUAhEWaH5%2BC0P4GB6m9C4zvSV3t7QTs0Pu7qBJMi6u6vhChlHKR9Sc91m19ExSkqEQ5pdF9cIMm4wqyKpzdC2lXo5qNJFQiKxDfPg5jJnXGoqMId6f3gG0hiOPVjSG7j%2FKYsCd9sTddxpvHfcOPMl%2BsGmQ05n58886gRS6gyDqsNmV2xtPkSPuD5t1lhfgHYVutsOA2TaQb1yf%2Fkq%2FNd%2FH0sXEWSjZ0jKvTWlvftJ01iMmaqFaJggDx1McTTRAtBR6Lq8JhfBetnB%2FLSXHj2Cn4TB2n6vI8yYq%2BYcgDo93JTgiHI5YGSSkxTMCjyAfFHoZtfS%2Bf1SoDLiGZyOFPaWK5NupygoJcEpVeh3OTkro8aWOJQ1V75s7qcT%2FFKE41Yg%2BG%2FpztjwqXA2Sud27d2qnXbLAPrYt2HNHpy4sxiur8F9ihZ0ZAP5cYeYhkrN8FqrBmpUxt6kyjlaiPldRsPaMPF6J%2FJ8FREsE8UmtKQV%2BtLnMygINf3VeVcgdWxVZCka2hIes8RnamJWUeS7tY41g8jDZJEjWIEkuDI8E1eQhXKDGVmwdC9IQ9cYMLW%2Bos4GOqUBs6T1CXw9M7GIQnroQS4cTVCeNIJqVwWWl5XJBfDUfAnM1gc5Kf8lurD4tO8kw1cibUZdOpM2%2BL5A9uxNQrzokhEwwbkKnua2Yc8TRjF7MlFihaSgHSvoWHEXGvBHrcghVKpZVVZHeY2J%2Bfspsa7sWSnwkCBwE3Tk90nS7UItRKoYXESmkvgvCz70rLt7enxHeMmV9%2BQhgqzU%2BipTZ7XxxRxzf1Ng&X-Amz-Signature=e2a52fa89756767d634be9ad3190c7aff946297ea5c6525b9dddf2a493e897cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
