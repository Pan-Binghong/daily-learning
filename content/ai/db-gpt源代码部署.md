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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLCKW5AK%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCjlP4UIl8eiQJg3OLQPTERaDbN%2BVRDiT2CGK%2BOcfplOwIgCQw1dicGgJ1N1YDTvGE1hEUISNumjFCSDKtBLNa2jEgq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDHGf1tpyCH8lMceWCyrcAxFf84kjcxU2oGaVT7VowXi9H8meX65ghKHf%2Fy3M2vEhoSO72%2B3LIzNrBR%2FUX%2BUcyzTeH5mfDj9Wdo%2BtXIXMZYwCxix04ZBuMXFZhHYDB1ARFPOuUEyitCgf2LyHw2rAPq6SeffUnNhMz1M19j%2F%2FIBrdJMs8NJ%2B5bX5Erv39pa%2FN7IwiBF4L%2Fkxee3tkuPOaZkkae8PN7CQyW2B466Uht9a9hFtKE9mjYLHGIoUeog3Qrvv1Rb3UVpaMpFc%2FRywkFQgkOu3H%2B2AeR0tUPuXUT4ZYIkgt5xQ%2BgaaboC9%2FXr4WDHlU6v3nQuYQuQ0OPnadv1KE3gVw6xHTxIahoibocdnI9VoZfFTYurXnLwVmwRw1kEAoiKkgVrFr8KLd8z3tYZAN%2F%2FWO03Q45xsXT35Asr1F1475uuowhbzYN8PvW%2BEhpJHnVeNjK7j4%2FZ1oWiyehjbCTtDoqvkLrs%2BR6uGLbfm6IFVNox74eaUi%2FZt8jwzZMHq30QiFQtezYY2k4bskG0x6rggkPfrt5qS5NtkKbS6EjGhwcbCB70RtgSpuEQNTF0euca06RrhqDeEQR9eQQsFbMgns40HPJTaWHN0AyojfyuVf8YWWoq%2Fg1b5%2Bd2sy8g0pxt8wxUljSFtIMNCczM8GOqUBDMlNUx171ekYx0VxXw5geA5%2Bd1sfGkUjbJhvpvn26gGXVAifElp%2BKk6BXwrkILqDvPA4KTGcS0Z5AWuW4HMPfyPtoblTTQh44x0tsPUkUY4vfujE%2BbdbI8mWJIM92N27PsbAOe7BoGmMbJqJOsC4Dy1no5Fz2iHMyvbIY63kjckckqNwIIcCXHs9nxnBoiFkuodYvWpd3CMrNOLzZOGCHlIBBMSN&X-Amz-Signature=a64c80e79ab4d193ebe3d9f090dc59ed3c6ac6be08a5c71e64cc8bc69c44bfca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
