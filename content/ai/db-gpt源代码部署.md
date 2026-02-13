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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAYTDYW2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQDDeKMdDgw7WTbFrrNUXmnaJ6k3u7GIWrCaO%2FIkcSbQQAIgHHOb9Fl%2B%2FsPemtQK3ZVnuU8jx0pDcABFB2pIRtoovVUqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNNV%2BZd1NfhmCtLKuSrcAwOcPwuTz4kZIdCQfgCRDQLLp5cO6oftYg%2BOBnfFIX%2Bh0mDntn6pta5liZD%2B9%2B90d7VXKF6JT0Z1wRamAz9eWaJFQ3dDpBOmZqKg%2B87RoqpLTF3h8dGzU4rUG9WsuFgCXzQ7JjBamuN1FLklNudkcvRImwBGHb6oO6NISDvCFasB8QHwt%2FfhBVcwf9MkHP%2FSSMa2jwz%2BAAdnikEcCFFUNHcYIzEgd%2BiwUtPMlxE1VVvc%2BjK8tTdKEeZ2izK7RVS7a0CsFb%2F8YjxcxzAF2ccQyP7gfyuFkXEh88a7iSm8W3TGgn4tJEslitCo0l7pzHLFhTx02y%2BZQFz4VDpn%2FotN1fxPgZPdYPs1HxudCdtbLSzWsRWU%2BXzjRv%2B6ikL3GoA7Xm8VT1hA%2FCm0hFXwzhdOXUiFwqnADlgg9v%2Ft8wXzwH6%2B5%2F5FcpBNXa6MB96Po93pfvITGhEFl%2B9ajwCEQRdUzNJ%2BRVdybEeY%2FiokU64ng58OUrgxzkjxIqTEf9dCX%2FKwqgMGtGA82uW58s%2F5l4iCDuOuQFbo9dmy4CknywJtwUW9HCTv2RifKFffKgfoIpEtcSd%2FIYbIpjqM9Ukj75TC9QozIUddSceLFvsSQj%2FS3t%2FW2fggVDbRG%2BSdyxApMN%2B5uswGOqUBhRYwrM6JW%2BuNhrdn7rJxgNaFFz%2BW9eW6tCLFUUUtyLgdHjVtm3ith9tBdXkpKlyIKPNmsQCw%2FllhQtHjFF947ibfDPpoqkxibFHCnjgMtIYYcmbHpP5uDqPOC04%2FaNQbGb76yxhCBwzT9wnJmnvEawKwGoK5PhmeZ8x9NWZb5euWuaoD7UgkOXnuPXqswvJqPtr4frHXV5zXgx2Wb4dBACJwRZjT&X-Amz-Signature=3a83d1c2d44ebc6e27a5110b7854945b9e52d604bb9de05dfd4e53f72bde927b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
