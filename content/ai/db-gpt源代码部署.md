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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QIN2WHO%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQCuEZh5NYyiDp6RYSvy8AXuc4EpjPfIc7urUyg1ykIVxAIhAOx1R1orytqHd4IdpDaJpwIXsIGvy5QSLYV3ys8ic7MSKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2%2FWX%2FCkGAGL0hPF0q3ANu%2B23eX2Nj%2BuV141cWWMaif1r23pf96eDgWgluAxdn7OHd5qwBNz3Uge7XgVKpMJJArqbt6%2BiwenlO5HjHrWjIqeaqtsnST49xQ0nqliE9dddZrpRfz5r68bHxjoifrU3QhNGW7lTRUhKFmzH%2B%2F6PXRyGy5lz4t3nYz4YqPNF%2BSDa195qHuzqqliFr0Q9ibR530YF9f%2FeX64ch%2F9XhM7EIglUMvUL%2Fr6taCISQmb5c%2F0TmQBitkUQB58ulGPLhx1GbHPF1kgA0bwLikp43I6uuQtTt3TOYkXJIJWp2udGcmH5lFyKH1%2B1l%2FhA8MhKP%2F6tVtU5FnCZkWdaBx78lWKa9aFpOA2gwmr9fpx2cryAXHELYWuwaxveZQwKq0PEUuLcsrl4vFOFp%2FCBznhZttdBC2XTnTP0MoGZomzSOZjS%2FAw4t4OocWcNVakX4vuwP%2F9voUYj2fvrynZ971Ii10yIE46Mf%2F%2F3SjE7raatgYPH%2Fk9PCjdrhHiH1l9Q3JWH9CiNZtPVxLmiMz1LSDdaYeDeu5hbktIuHvIhGwZTWJEjJ%2Bxb8nNvhhhL2jPmSLtaDSJzDnDAjmK494ttmOnRA76qzeSjDrkO8q3IOoh5itT6aLVFLqzP2VV6Bl3aK7TDJucTIBjqkAbG1iBp5Vmo7TLHCTA8Ufu%2BruenyPvq1XpWdIqhtaoanAFE6UVzzaA2kjayrMJ1h2%2FFCzmYTy2%2F59kts8Hm67mylalwqqXxKEdhxFUpEEu594E6EQOYous36I3W7a%2FZX9VwVn2E8i7nYFNV14wRi0lUFt0nQFZbNfUI%2FN%2BTskN4s%2BLt8NJ9wKYl%2BnqHca0oj6ZoW2JGCKqFX8mdtLLTHJnlSpPRD&X-Amz-Signature=fef04f84277e925f671584c4900820cb70da26c33840eb8b9a4cbd29c47e03f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
