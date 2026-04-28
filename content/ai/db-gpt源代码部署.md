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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SH6AC25F%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIDluLXo3Ud76zNj1n3FvEshVmlEIpEY4jIXM2fDJM0qMAiEA1VurAvuGqTuahHqQ5AmhOyA0ev%2F3xnlqn1B9a1MMjGUqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPGI%2BIBpyy6%2FRNr2GyrcA3EvNHC5XIgAtjX3p0KehA4So7BW9qwW9hEY6crx%2FcRJbxPvAoS%2FDJqIECcmTituEKPiN3F1W7DgIcJiyejk%2BbCVQH%2FHXg4DR%2FSMdCkQQIsjiWRIZKm60g9pnfuqnqmC6STZQCAyPuGvgm6Rd1kj43Zf7N7uvLyhdzT8GosV8ouStXZk9g4yoqiYLk3sAW403y3tcn86RYxdh5PnbBe2AmzhuzgF44fZNUdxaSwpRT6iTG0FBYjYds7rcvTyoSY9nxVliShyE2IG60jF4RCriIjafOsnwu4yUXue0YxuwJsaTnnbm2MWJRA5sknwdbvyPM5NbDUNWlY0tmRP%2FvxVh6ATLoNNewOWIeBc0lJeU4n62mqebgnijkiMS2sWnrODHUwD4vWOFoC0boleMc9a%2Fn2j9RU0d1Kbxw69jweMHwPEO6gPr5ylK%2FLTs0yzMVhka%2Bg4kFsnrOcZztxR4Uv5ZSEnrlKWkoLIyeAJwVE2v248GZjRNJrKIc3MsHy4kZ6tbTJYUKKD3lHBiFnfh0dV0OLn%2FFmFSKugzkhQyjil37lRgL3dcm9ykF96SxXWsi5%2BBne8GHL3kmqyOuC6%2Fqx32RK37eJjQqFlIIXOHB3NVnoGvdy%2FMoLKvAOMKaO4MK7twM8GOqUB0wUzsT7fjZE5zRTKJmoKNBiREcfXthsNXC67OXpmqh6W01MaYnQyCDSS8O9CiGBAauAU7%2BFeiS7BPqozaJzda5ed4PU7r4xFXasR%2FYs3h%2F2k3ex3lFm66BxNGfvnntQZcuJ%2Fm8t5NKOKlkMK1iael68DZDfOnPXqwDh%2B4ecQKJn8yee%2BxXG0cqpybPTtP7VW%2BaLukvv2bQlG6KrDi6Tz1gKuZ6QP&X-Amz-Signature=15bc34786b68c4a6ec8698627bf1521989747ba5ace548c18661eb3ece44ba03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
