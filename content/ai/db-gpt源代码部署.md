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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TL2DDN7G%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FcmFRTZPFUjzIhbHwj%2FyXN0MejYcqZ0zM75h7fyFeigIgSynpRVsSQcZbRjzgBZqoKRJbzXf63iE6HJUxylf3PzMq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDHI16dm8Aod%2BEzE5WyrcA%2F%2BxSgvqWXq2yXnqmS9yvWUk2DQtNMDLoirMwdho7krwbf83xYNsM1bKk2J3xdKWKGAKl90pWI2%2FB%2F2wSl4ZWbJj%2FldSH9vWdDjAcEf8lkF5hPPo5qkcO3nyWGMukMgmMuJ0QXi1PYeLSCZCEJj0h%2B6nbTWBz8jgCsC61Lz6OFqf2ui1P%2BWPAah5yACInk6Y878LTCESw11CUbYr8yUZW62XbGAFVQXFxmbW8YnBem1pIAofmL7h99M%2Bkp2oZX4vAic6EN5MdWj%2BK1TMBWN00201F1kBz%2BsIIxVLSCLAUXKAbHNBukECvXT%2BoV6p0i1vvS8ku3%2FsPaqTHtDgFXq5ltFfTcxuj1ANknAUtL4Pisq%2BCkDidmu2uoU9pq8%2FJbw27mok1mCSas398VNfckTPKPJQxsskH04FM3cU8lIQM7aNswzFuhA3Qrj7Z6qlGLgPC9FJd2UHblcnHomRu1YoFYtEBtU9wrVpbzVYKpZkWZa8eaSXA4WaYEnqsHOLpppzi4AErJf9NPCl3lJaPum74z3P4NK11oAK4%2FXzR4BpGehXw9wxpt17WvQ4dFBE2eUInX7exaXOiU1bfB1knYJZb4YNOQWyFMt6K6%2BEPQVS40u91ijBHkqFlJ2fS9yeMLbAw80GOqUBFPrV5yKbMS78UL59NEkGutgSd34tQAKHe3HbTxC%2Brg39If8ta26RiwYISl7%2BdvscDP5BzHHW8lROY9%2F0ZEoIANGW05B%2FxBliNNdw4q0VqlA6beB%2BYk%2FtMqjqj7tPMQLXlryY%2FI55KAKELBcvtWgHMJVx0icvC6HrRtKz%2FlAj%2FLNeQHSzq2EIvPWUQI2ZrUTaTPN7O9%2F7dMqxG%2FVVpCoEjYOIQZqd&X-Amz-Signature=9af147b6199c04c0e14dfa0ef74d27c9b475ce4ed70936f19436cbb13690c0c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
