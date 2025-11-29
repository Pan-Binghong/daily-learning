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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QGHLALH%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCH2mB2ZZ%2F3FOjBt9cD6QPJ5nsj8UDdvW0GqH5e%2BVYhb8CIQC5nIuTxMUsT0R2RCItO5rdqKgHq7QNJeGqgNr5SqrJXSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNsZjsvBaFYszDzmnKtwD6qSzJUBak5SNhr9Bdr65FnvtGkxA4epShaMo8m%2Bt94O6wFIu9y%2FRpjz6HZAryTHr3ibfqYGcmJXHw2hIQJwTak73U45uvatyJ%2FjchMWyizX%2FCW9x1eOd066rpo63iPVHfAjYg0MsmfYNnVR%2F4F%2FCbflH4gmAvb4HGJRfzHeJCAxjhwF0gXTdZQnhsQl7GpsrfZFJSU%2BYWv8%2FqSoqVo4hvDh85LOww79FSO0Z4hluo18q%2BgzC1BqOFqOdEoK%2FMI02Z1iQ48DQN%2FQJYfqdoQlpGxLHh65UH%2BQXmRrTVyyNReaB9VQOktx53Af427%2BTIlZ1%2FACTgrNBxqwxGnrTUm8NTx7p0FS4lwkvzm7L2FSTz%2BbxNIAmXNAmnohtviAv%2BIlK0McS47aQfiGrgbNXpxeEGtAnWx3nNHLRURheopeCRSQl02eB2nWu4Y7p49hSmnq%2BRhTSTzWL%2BzwUYA%2FAv7m6KBEWy%2Bj1ZyJYpmeZ49ir1bUkhyGdjOz3PD6Zz6%2BaZ4f14gGArPO9M7xTJlC%2FYsqQpiHn7cUxbDb79lMCu6OadU0O4TzybCJoMLBO7cO3czcUKLrIX0FNUzNb%2BtT0Zt4X0hvWvRFAWwRoCd17iFZrDHOkodOPwMqSgobEtNgwq56pyQY6pgG0JotXFrU%2BSwSjyhQ1SINvKqyX1mu0yuo01BGMJcjZN7ouInF4NHPHsqMQa30z3f02isErc6tO%2Btsw4JKKz4cZs2F1sRupy7LLsXXrrVvE2iwGnpe0jP8b25a8ffAINBFt4MQTuZxYOlAYTaCnqpLdBgkyIWsHyyr%2BOv2CsO8MhaDZQz1tTHGsTYDjpy7%2Fn%2B%2FrRsXsiNlAqyG9I%2FjgOHA07SBckAbb&X-Amz-Signature=e117c8ae167ec83345ae455f25f2aa6817b969d59b164b2c33365f18f0ab705d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
