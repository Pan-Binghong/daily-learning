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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625BKHFK6%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkoZQ3Ym7SPntWteYPuNJHsgSgLXG3Yj1lKZyDreldzAIhAIm5ICiwkgcAHvaXDPgfSdzbk%2BkU5ZW1prncbdKtvgmjKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwAOICtb6dx1RZ9xKUq3AOxuwxemz43qsQHgmI1jPbxa%2BJUYh%2BOP4tG4Ms4Ct%2FYAz4hEtfAVkwBwvWy0XtAGrt%2BKL1xtdJLs%2Bl28xhzU2husVvyL2nHXV42Xk3WJfPd8jB4fEYGOQOB5C4%2F2D7rkXEyC1vhG9J9UeCHiism8KcJbklGKaqwsx0YeZRDkCf29n%2BK4VUOUEeUgmqPVhYurJX7Ezu1hXpxv2a%2F4km0TiPL0eTS2dbHnjLpXE0vKQNPAUcHgkJ7KfAXm7S%2Bfcu6r68AkmFuqmME2v8AY80VG2zNAY2k3TDHUoC6HgUJTr7zqtE%2BXmnHdTjBw35wzv8unCm%2B96nARI%2Bq1ywRsgNigtoE7BC4rqIMbCeV0b661onwkr9oErjlSZDrAm30pTS6dleQbXqDvefQyvAu8XCgqiSA8i54HX5RzjmvIeBqJGtxIOqfCc48XPotnfwCpwX%2F0fIsldOpNmawdyzqh7hKgJi1yDbosaM5jQeYtsi%2F8lWLP8GnwaXBFB0Uy0i6V%2Fpr3NOotrUudyKOZOC%2BLBTFWl4VXiT18P9L8OlPottK5ZbVVF56DWDt1LukvCwRbfAUqSpRjrtJIoOWc3fN0Il8YTT9R0Qu4PW3i6XFm0kpFuYL2TH2%2FjZ6mbCWYxTiDDCIhpjKBjqkAaHHinvjp0EiEHMXm1u3nmXqo0q9x8PEvlyto96Whdh%2FSYSkA1keLnbXdW0IQdx1pLbRjqEmJdqOGDhqC5P%2FeBv6QvVtKSMfGC7mEc8TIc0waS7%2BIanBBpoFhyr4VW82IqIwcVkelWh%2BY%2BdACl0eiznmR0eHw1xgtRgsydLyMVPlN%2FJebKsos1NosCiS2f25mQTu6z%2Fn1iXz9JyV%2FM5D480o1VD8&X-Amz-Signature=293bd2d3553280f6ec0a0345815de7032b5132ba5e5b456a9c156283425c4baa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
