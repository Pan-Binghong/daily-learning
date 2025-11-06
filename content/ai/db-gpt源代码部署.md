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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKD3F4TY%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDx2ioorDq8LfuSHOl9%2BOYbMfxU4mPjkrW0mGSZY5vE2QIgD453ce7DzmVoVqIgmfNvxyuRion3wJmBRhXoS20IN7kqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNNlC2P1Le2kv1ZsUCrcA%2BMt2TMvCtWHI2M7Zl1IkxyjBHJXWAj2znmAg5hQ6%2FsWajNby1Do0CmpGAPJLQjz1%2FTAZsjOOv%2BrtB%2FEqaWG4CXHuTy75Ns6kBi%2Bt2EwBxDTKqBPJWGx%2BQ2K5tX0LOsaCSJXpoQjqn3AYi1E9g5jnzIraKJNCglHY0x6bSMvt2JZWAHrBpRpIZ4hZroEOFVo2WqjWGB8hhZHQO8EXSOMHhofqXTZ34nD1nN7Rc%2F0p1vMpEUpjNbIh4HGX9%2Fus1Ffyzr%2FL7Wxt3LUJr7pMgfSjIPIEiK9dJF2hzC8qv0Mo7EoC%2BPnHJARDiXMp3kUI2coalpDC0D9jjMKKLskM65JmLr10vbtebMu3HmaR9gwhuC5aRFQHAC%2BvXYP4qIP1VAyhBilI5PTP%2B1dbENRzcoEPu9TWNpunk8XXKi5HB5KF6iKqg4VC%2BGu%2FGvMQx9YFePbidDIy7LkqR8qhquDb%2BEMtIGL2J5yNHYSrHZuWAahtpzilcphtuLJqdGwvdaqOwR9nsx6jZn%2FlE%2FZ810F2yN7nAuPWs%2BLi2mdIa%2B7Zr4sutqr24TT2nErLCJdzqynVFOIW6YJ0q4LZnHnZmlR2tBgD7Y7q39DINKydp%2FJJ9WTdxMktZ4uAqiIyDnki0OSMNTvr8gGOqUBY3RlQg7a7o1x9WPGCavhdqF2vqL6%2Fk7u5TC4yqv2Qhh%2Bv8ZRk65DEmVxgfvXdDob7w4O8RkPs3lmzk4jIBDlMueuqI7GRmKnvvGUDMi1J9dZjS8xNEH%2BW%2FakFuJL3db4bbyI0yr0bo8mtDPUhZwKm7nh79t8Avh%2FOxp%2FR5A43hPkpbBbEvNzbFxJv6iEr2HcpMZfgnQhGraYPSgy3AYISYYjrnFO&X-Amz-Signature=d442642c510df27afd8ea679ab720f84d48c4e6ad499dc76c7cef338b6083d87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
