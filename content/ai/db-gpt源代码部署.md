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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NMLCOSZ%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDzH0qJNZdnXxHjmIorCdps1AFr6oj1GT9MjjYLhwE2vQIhALv4HcoYe%2F75WVR3%2Fsu1wn16vAPgg7wm%2Br1xFKTb%2FJh4KogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzISO6gmlHCrToXjRIq3AOMGlAr%2BHW0rqWzBpzA6nEGEkiPu4mMV9yR%2BdZjmLQ9WSDY2IjXrIQMNNR2okMt9JIime72uDt%2FqLNW00Vd6nNCyFvgd5mlGo4lXwWJw4hxdgTuFBHpIOnpO89jfvkI7XU2Lx%2BqTijPi%2F%2FViG%2BcQqamboo4ap9OpXwWd0u%2FP0xJWbg9Zf0pzPKvVxI74OkHcXoxTxRA3kbHB3jEMP9k5FivE4GvIJBfVrEOFFj4f71r7fWKu7K9K3u9yHj3oZibSC2f3pjzoMkXIJ4%2FxjR5SHGRC3va3%2FxZg2DVWH0ZoBhPE1uNlT8OG7WPVyWtP0uCOncQrO4lcag6KLXoETixrjl1kZ0hq66g%2BT1fUckE9NYhnmKCvSbP8kh%2BdBlQE9cOgX3eMIgq3e9XhjxJSLXJCf31N9jO%2BzTDI7XzEhtUZZhFw4MsL3ToI6AaQlCY6yH1EynAvFuVGf%2FTnm2uVt1VPj3weiIZQGb0c5h%2F11uY8dl5PHli1%2BgUjrJTZMsYQ3%2B8zb%2B6vJBmnEld3CHurIi%2BA34nQhmVHsrOe561uAl1QGGK6BhyxxfsAH7BFq%2F3TV9oWTBSexS%2FHnopx2wLleXLeX1Z4Vzbv7CGf04ZCe21DfVHmE9NqEycPZuCtYjc3jDLvt3NBjqkAdQ3JuJ5B5OqiybEORleEb67RiFd8OU2l1z6XQic3rAGe2fSGvS%2FuZsj7VAmCS9FkpJ9sWxt3wkkKjl7fD2DwxSmAREVX3Ti%2Bm%2FT45%2FtUt%2FpdRBvT06K00eddy2AAOodPcU%2B2Eqi1gR9cJihCHs09N1H95IlKcLouqed6Rs7tw%2BPaz0VuM0paRN6WmVzL68YlJvbydVXNL4uiIiL9VxefQbiJBlk&X-Amz-Signature=0a603066fe43cfb0e50a2862bd096c50977cad8c82ba48e411c85a6c5821987b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
