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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEMSSDMC%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQDs%2BK9yUr0PEQvF%2BZJehW53dHpY9teH40wGtsSs1xWIowIgPdZSXiQd58qd7xiEoXY0ZqnRCtH4FgLHDt6yEFNzzQUqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB9ITxRDkIqkQnxD5SrcA%2B1aOOGLUYN%2BIWyQoRXTMDyY7ngL3F1CIyKCKw5L3tM69QjN6XjtmCxA32N7hBeevI5%2FXkTS9c4sH3ERK8yH3vQrkkU%2F%2FuP4ANk6ZGeasIQNMxhVmucSbDwzmP1ugjoGy9y8uPumQtDDdV9d%2FeYHcQbEsO7JGvryg87MYZma7oZt6UNkxstzZ4a%2B1C7rOQ3WXXl27n4Y%2B4AT0m9YnuGNIKC2E38vPY0DnDfTMCMN2JXQ2mcOSVAqwPQiN476QlEhKsdoMXF19FWA9FZxFYZxpWExUXslTnni7x3dwOpC8CQjk3zfB1yDq41jVjhJCggBrrfr8iLuvd2p4AIiCxEYJULOy3szzi%2B28MiqbiZZP9TIVCFXb4d%2FHhxuym3fmXMTM86uOOHLR3eoSUzyaiSZBkl7N6cB%2B9Fnbyink5%2FJdH7wo97hwCaMCSxNaR1cSxFs%2BMxqbJuut9rQRz0Z2KT9xaML%2BQUDBUcWriPqvtIuRTYDAgO%2FdYbG38PkDlpbUlISvrKCfKSKis5qaJuMtKEiAlphsaE52n%2BoDDGlegS%2FpNiSdja5rJDnB7k7qsRdtbGFlENnqIUO%2FLkaFeOK2kSo0JJNFCX2DiNSccqxypZlT11wSmEnWc1qfl7KgO2hMN3kosoGOqUBrhKGPf6bvcblVhRBGqyIQh00oxKhVJocLYFCeWk%2FM2qKzawNAD%2BxERIfK8TOgxHNB7mOO0PYHicRvfDRqij0uOvDw%2BDzPs8Mx9u6IV%2BCwBZgTmW8USEzi9zQaIkt6hv0%2F88AMAYYPydQSbib9Fysma1lxEEy%2BctFDir%2BphXCp3QTz7baj0srhzOZBxYOmojAix%2Bd0T05N%2BSHLRJ%2FG3gXERHmXixO&X-Amz-Signature=a8c5d7f7667d58f5095dfd0268c1cc8df0dc235044c0534d2ea414832358c1bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
