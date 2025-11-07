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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDC7VKKA%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeIQVGNEuQT%2FlTBP%2BZcJsOEdprrtRDip93c7LOGofOnAIgSMSc77OWUdembAQtA7JdVG%2BDpHbuRcbRarlt8ObPtUYqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJmz8UDOEulSC6hZpircA91B7pSNYA2lGonowVad2an6yFgU7Vi9mUrY3GC5KRWRolA9v0FD0aGfVDSnOLxL%2B3tSl1utShX6e651dErTX%2FGIjOPoCK3KzJSAp%2F%2FZfB77yRlmyz74LESEsZHCYpPQVl41SVfS0hiDGODRiJkajdzANdA6H%2FcnQoz9UMVFmWcnsEFRinLR7j%2FmlJLzD4d7JZ8eYVuaRCeEoVY6%2Fyany3ehjtdEQasZ1Er6FOwlAddLvyB3KKyf0n0SBFum144wwsMnPj%2B2SsR8CEi5%2F5LUeBu36TiR0PDs66QbtE3TDclkZwTpH4RcGzw2RTqn3va4vt%2FsCoI1I5w7yCHKykWnXaG%2BZfX4izg%2FfwSy8CMM%2BKMsMXZz6Aw6Ti60Rt6KlXqZoA6PBA9IrZh2p3xpQpE5EOLXTp9sOT3C8N8dk1zOzT0l8a5K3vKAEo%2FS14E274w%2BHo5C2rwlxpkINtcizkxJ8U7lxKn8lsAsTsD9j6jVFAfa0eE2ECqZCRAaPNn%2BCXTWhy9tLM3XLoVTnRnnooGWgazwKfwYQwhjLgrD4dRuyXIx6XWxp6uYmWaC50GOgj26yQgjzmydcPQ4QuJBhVJEZECUAI%2BM%2FsvqJiGSZLRnAO%2B89ZhU2lKlEGFd83XnMLu1tcgGOqUBTrIaNTOLV2%2FaQxcUFvJqohyHhRdMjJdUierN3aYUogipwoC0LcyoSW5QISWa7JGn40iArV6%2F863j5%2FNpd%2BxU8TQpTSMpZfLdHdIkkN9KpJgM8X62sn%2FcYytCYL%2BYKMKZEsO0JJ69n5qc%2BZCwQB4NXK6n%2FsDAFWvNc4W%2FM%2FAMpWWlVIcbUPtoKASaFfxa8ektDQssbz8J6Ztljh7QhZ5tgFf63I5U&X-Amz-Signature=44c232b360d63bb159be1204d14220a3358a3913fd8f97c44a612b549f0f6e1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
