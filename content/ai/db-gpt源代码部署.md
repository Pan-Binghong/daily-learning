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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q26ATDJV%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCiBTz5xLPsooGro3SncXne6tE12YC2ok3FDzrHHRqdZQIhAKwSzGGZ2MEnAY6%2F3c7SMEmbb3qyhjOTrN2%2B3to%2BUhF1Kv8DCBQQABoMNjM3NDIzMTgzODA1IgypyIe%2FzkwXKHF34gEq3AP6JxJJao%2FSS4Cq%2FoANAqQrlrwhdWVFfyK74XGBUgO59DURd8KbPjswMbO6IxXYkh%2Bawtw767PNxZqyAUmJ0tfbJKNIv5dewGw7iG%2FACuJ11GK4eCfOWDAiK4psJaNcrIoO4lR4y1Ht5Ehpz4GCyrHjh1LqcwnpEqi2RmsjuKHHzNA%2BAFdKokQ7xkKdY1o9fs7CXwspUwG%2F%2BWzI9GZ807UmUxT7VSPSZ6s%2Fu5vTl%2FjKm5j0qNlOzXym4Yppib%2BOqoHwj48YRe6C29Vr3z%2BfGT2BOegg3YCxfZBYwUvin%2FHxZqf8I%2Bc9bN6j5CtUyGGlHtiCZ%2Fz3GSOdUIMGwDlhFdt2ZtHTdKWwoAZbVU4O%2BJzYJvQdX1HZHks7ZYRxThJxR9r9BzhY%2FBlN8b4hoojgNbMWjmO%2BErqEBAUlzianwDrQoaY2VXe2WxqQeyxFvCqy9zOwXP8iKremQ0UjbBxZbq4NuEI9xyQB1xlepxtiv5%2FYTwhYeSceqkhQyn62%2Bx4fOiOOHgeJCGLpIHqzwZWMiDE8Szm3p%2B80%2BO6XKDqyVm5k8HfCODEGUL9AfeLTLGVDSEaKdr4kTzW9WXWkvG%2BAhI8GjusvwkSv0eGIxGGJQeusAOCYFwZWsmEQQn4r2zCcx%2B3NBjqkAQtNhvcpqO8nzT5I45w%2BmDDxuEu5jaERJcWcSA8tn0EFXbgxlc7gFDA0IFVxWGhyK60IM8e80hIQcdFnV8mLsLfVlPXBeveTOqS22P7gzYjAvLL%2BdftKG%2FU%2FIx6dmBqm5NFTmnOOOpFQtA2VHO4BcxJXy7AHng8h9vM5UgmU20pbXc70EUoh3UMhv76QA3dFalOnMw3WfO81Yvvl6LR0HPcPaERc&X-Amz-Signature=9f5ab83787fff719fadcf1fc36d04780c1b8b36d4ce20cdadea9c6b95cea868b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
