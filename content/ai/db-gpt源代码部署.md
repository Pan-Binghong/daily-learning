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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMGHAWDH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB4W6Kus5%2BSdAnMJIASUAWU9cSm9UQF6dh4kiTqBiwC5AiA4M9RaEqqw07cvGMw2CSio%2F5qrxVgnzvudoMBJgBkT%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMm3mCh9%2FcMZy7MlfwKtwDo6b1EZX5If5rBDNhcIUQyUUSp324B%2FZEb9L7AHX2hm6mwZuI96P52EXpxCCJADAkswLzAsyaZlQxCyEZuMyLY7KywBjDUQABM7BBVYYNiZoSd2loAope8DZhwjipRh8yqMulMFfX1RzaiRfWEsTWxwMtE9SMFv2y%2Bzh%2FPel8ouWgPaxiq9Qs6n%2BjtcaZNv6LPdpB9yY%2BUYTzK3%2BlLwR2zUEkpIL1sq0eY8aLmrIJKb%2F8awtsu0AqWZxQ5ow0yf6BOWqd8v88NTnkETDrZ82entMFcN3D3pgfmmjIivB3eTTfkf7Yv6aL2CZ1mP%2BuiOLQOyobQrroXORRzccldpkLFkxv3YezG0cevYduTtffz1bkUn3LXnnsKuABgisiRGRfN4oSZGouSzO7F6S3zYLhQ%2FCYn9mv9w9DmrSHfeCEpyrY5Cpmpp3EWjjy34byNdlNb1cHrKQeBw9WaDoafX%2Bd9FhXBJTPPdDzZtIgEc2d1ResBPP8Q4gr36cXaNp844sO1Xx3EIKKLBVTKHazG14PY1rSt1wAIegBi%2BYZmkr3wJeUhwceb43a8fHC3gZ1%2B0vZQ1t4AH0zIEDsOEEYux8ac2lgKhztZw15ETJaLT5R2v%2FU1TA4qUcxPNZztTkwoq29zgY6pgEae9sRp%2B%2BIb5C8kwRiJbod1sUEMHfpn2%2FpgapQ5hc4%2F8wQzv9jx7hz7xArNFa1tmVysRK%2FwiYk2N4%2FOOvYw7xaye7d%2FVITjLVu5h6454TJYEA8C%2BTeNMgHOgEUJzqCpHuezZ4oGdr48wk43Qwu86u8Uaz2h1t9zVUUkLZ9u9FF0bwlJ8EP4VjQefMmOlJFIq%2FHxV21i4T0gj6DRZr4E3Dw27ptH5Tp&X-Amz-Signature=24abf4e437df3026cb5a0570fd69d1a20a62fc6f5a5e432b33e2f751b3bc1ddb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
