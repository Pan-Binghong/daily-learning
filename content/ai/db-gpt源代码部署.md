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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673YFYIHC%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQDM6n5VYIZBsDxEkMwjdueIcfvRA%2FgrAqZNH8EA4WGKIwIhAMI0e5jH%2FYzJKeag1I5wZVxtg0kxupdoDTSJOZ5eEgcyKv8DCAMQABoMNjM3NDIzMTgzODA1Igx5wYe5gOKQqP%2F%2B3Nsq3AN3dCEX7jqqQ%2FPnC7d3W%2FFwLOoPkXe20zsNf0NJigCsAn15sCEWzj1qwI6vyR17%2F5gFMCTDeB5HVqMG73I7qMYOhoyLKGMUUKplYgi6w5MIE%2ByNzoVG1j0%2B%2BfS3HBrpb%2FPVWVSM8oYBHdZTsy0OxNYyF7ejbgi9IeObWltsTfiGOXAWCQS1HNCMgCnhUEpiaZvTzUuA2ReKSBrpU%2BGE7i4l%2Fa6qxTnI%2FOH%2B5AwXNwWRPObe6JOYFjBaTjiqVBMvwjxQcLiKW%2BfpdFUzoCg%2F76PAY9XyDic9PPO49zW1Is4YOaj%2FoCMJqoJh3Fomk2W2XV%2BKvdXQQS23Ka8iddAUYpJANTeQewhkAbUTeS7BREfzskVdWCG8r4LBKeLdOn%2Bhq6GlXxonCIRtEBPiqtSTM3EwNgreDeCvG3Ghja0kXt05xhIDEjRAKa1uDl6N7Gp98Rpisk67uFw%2Fod0lOUDR1zRA8d7N%2FpAdWQlRa8cOi08SB9ORRittD%2BD%2FhKDNliBS6%2BMv2e%2BjDEjJOkgo7JI0HS8ILJGbRdZpr72UZzSanFg%2BT0xNoCAACoAZAsNP0sQl7nTwdNNsDzYLvpYd66AoERBBmJ16qcLTUQICbXcOc32oCqi9I8YUHZeB1F8crDCw%2FKfKBjqkAdICWfspVczgZ81%2FMn6Mye2WTfo24Ud1lTbSqp0uszXoAiYDXK2JSZm9lppdXUqzo81PVdLaDBhPjvOKeUiteH7LsT9RpwP5HIg8cdh5rtj5mnANwl%2F82FX434LsONmTkeuDAFGKVdtLWCbz%2FEoljuIqxjGOxKwSgnr%2FEBs%2Fi%2Fj4haT0pXd1x56JIrVOl1%2B21qZF1LxRJ8P%2B9nuuWIpQozRFmB5X&X-Amz-Signature=663d561b755aa02e14605679e115cc6b6d85377b828a822fe356214b18b4b2a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
