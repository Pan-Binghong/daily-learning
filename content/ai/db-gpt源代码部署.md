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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664G3OSAGM%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlf3%2BqcylRaZQ1nseMjIq1ao8lEr5Zqf4H9XEj9sUEmAIgUUw2q1LAz7B7jRiHtvshvMLmi%2Ft%2BCAkEP7HcYuaR0jQq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDPKh2PIRgClFdwyglCrcA%2BKRDsaYOF4IdoVWCgwiBUhoXO92U2QR12WoawiZw59xwKkGbIH743x2e7JuhSmap3a5kFgCYa%2B8Ha%2BMZq8aejw7FSfZRFm3E3zupKjKWWILdHBIYGtrr81uUMY2h6bl7EK6F5yI24VwCzbw7p0forTf%2Fa4ckRT5lynLTffHlCZzM25RrGHbszq0llN0ZVUc%2Fk6m%2BDGSvXahJlZK%2BHc8kJW8j2vyhks%2FeGb%2FUPwJRNpeCSb8t7L1iYRASrzCOHmpzKMZe%2BWMaNOTyYiuvId1C2eo7lc8ZRBFlF62hm9BUgG6X0FuxvvYVSNfyBtNUWdDvMQxDuMm%2FNfhgUAq9mfUYFS1EG%2FoE59aeppeUpm1GxXA1MlX%2FWWSEEDn7JFV85CmoPDNi3q6mIWj6mW7AYZg%2BzEUKH%2F2yfRn5e0DN%2Bj9eDRk4x8mNBVuO95IyErQEp5Ukbt7xWqJzPld8DpP4ADkFcmq7Tr5vX%2FDKWQW8B8D9xjjcnjype8%2Bx%2BvkuPMCxzg7ox9YRWPV676FAxEJDi8L06Cfq5Gx81GStZwFOvmr5%2BLwVaWlSzdfAz1UORU7nBgq7Z%2F2t%2B%2Frxe5oMvIhN34NFQk%2BVMggTMYL2Bsbj1KWPMB0RxUlivXq%2BI8IJxaAMPeMg8oGOqUBqjoHK4MqY5A3Twj%2BIZCa4RaoNGLKgxVjk9MKKfZ87SYU05sPr71YlDA3438iUy37jBExXr%2FhiZggqgmavu8zWNoQ8rmKIn9ixypAsylFsZJENdXDgPQ6Q2z195rHc5UoPREhI6yG05zFUsCDKPMUbd7L2WAKM%2FT3iHzPJ%2F1%2FhFBM4NtOET2IE0oyZwolKEJXO0iHd4koObRws74vR9KiyMn8Pkfs&X-Amz-Signature=306fab7c6b745a88d2fe82e83f9ce4322e59dc2b777fcf8fd4dd6b9f23b87482&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
