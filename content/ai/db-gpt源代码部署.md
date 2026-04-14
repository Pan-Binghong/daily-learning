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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REDQST55%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDwytHayhFc%2BcavpIaRT6RwHv6OY6fm7ZBiE43UrVPtDAiEAwe8iS%2Fl5IBD%2BedIk2r%2BUWjdutsvzimGTj7CsmgU7tecqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEoKAnSv7Ks6J4XCMircA9CvGOyuOJ1va6%2FEBmNU8XCxJ0W9yRi8kGmdB4f4eoAyA0Klbz0dZdwOF6%2FcXDdgMOnMQJijw%2F8sKOlbuFVxfeGLzVQhtehkdvzN99vm6xFjaFXh2t2eo7oT3oreJ1d68RJt50Qs8Y9y%2BQRcuLOzfqMceOBQz1gthAJk4uu5hRRK1bM7gX1mH6vrCW%2F6LJ3fz3CVSpWfwjpxbdJZYO2vRXlQsi555SxDHB5uWsJoQryDHa8lrcRacfkD6DNA5Eih9TBiCHhv2sTEw2G7w0zCFJvArnj%2BY52vlzkJ0uPL2M4D22XllvUJabxz84Xdqap81IKbV8%2BBng%2FviQ%2BEpd5Kwqx3YZYyn%2F9Cd%2BJ8LFnXeiv3l1JmalKfydxPUw6vsAWJ2H12ZfDUPcxYqisZ%2B2ZnjiHcOn9cHDKQ5TfwbWj9pSnOtHKtHbAi1TCWwdY0WMG5JgqsRnAexqJ7UTxkt3FYomEc9wZ9pGqpMiqqJjKYV7QBHRn9%2FhdESXd%2Fgl4SE7o%2FXRTr5b773u8ysnIrGAkgAXdI62eOFuGfYyd%2FA1OH62Xfzzc2e7AGM8kHTZSEEXO3ZKYv3%2Fe0drDB79slFJJVO%2BAXmPrn%2BcdpeWzodjDBAwny0vqH4biBhFMPN2OhMIXg9s4GOqUB%2FJrqOhVal0eLWjSuWA8zJKmk2A7TVHZj5UpTKww6zW%2B%2BgPx207pzdiqGQrh6qpThNStZdruxV%2Fol%2Fk4%2Fj0onteDCX8go1C44HqC6zrQsTZpG2C2EhaSXOjccS6z6wWZqoEv%2BcJLT7d7uSSGf2%2B6KDNV2eRWrkmt20w%2FwhKicG1UtvKmJd3Xhi7LU1pPMrDHY21F3HxgGbwez%2BVvmh0RHx%2BnNBeHi&X-Amz-Signature=43ff5a7872eed53230b0a88304801281a69134d8de94439cd88e0d16d1c0115c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
