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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYQHPV3E%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDKyDRsaVQZB7g4sWpXAxkj0J2cScSdQWzqKjMRLenXqgIhAPqI1bwdu1dt43vazZixlDdekDN4FmeMIcTySvNbSa3HKv8DCBMQABoMNjM3NDIzMTgzODA1IgxwyNbluQIv4dDWYG4q3AOOO7IaZ7LeFj3fz6oRkaxyzLh1Y124EkVXqWLuqrPKEns5GOlAf8lY73rIwl3xcJz25wSjVdEj5HFVRS9cskoBWet9CtMcXWTcnze4JCypNsR4F7HmjV%2FhreZVZPzl2LjALUN4%2FrnyHuyf7IhzhNOQIn%2BtnnL8IV0y2qQxlJoWxBliOPetfJzQvrBM0OhNFguuWoiKAJVIzKKdS%2F9bnRLSWZ%2F%2FCSVXWEyk0pY4NSsGkPH5MuNJ5%2FNfs6rabe5Eb%2F6keIOwZpfjxho4UmYScIHUPXlaUKjrOHI3jGA2v4H7PCIZHUs5LcbAoZs49%2FocV2WnayfYxSshTAuysR0XeJQlKz2fF0cA67fpzrN16USEZBR%2FG0CsoXRkjAtlvVxYAvz1%2FQOHgeKJ%2FTAuSK%2FB2JOeQNJpWvOpUAfeBDnpfTPX8R%2F7a%2BWVaY%2F7wrcin%2B8W9OorQBUWQr2Qg2jfDz2PljBcLy2owSc3Vcw3DWYMNsAqqqur0MAAczJN%2B6XCOixGxrLeZqZzBa4X7Zcv5oLo9zYS5FR%2FEz6mwvt8oeaagd4h0P%2FU1Wowi4tJ%2Bzq15sS%2FJb1k4PiAxxy8d1MHagkN4Ino%2FJ72hAujaUXPnTuGhfQu6rR8z6BdjNClCWclcTCKmJbPBjqkAcH3SdDRPWPmXZAIf0FMfeVHPgHE8daKwrPzGkhuK8wmqGqTbjJi%2FH5yX4bffgXLnrmOVhzmVGTAQ5srnIts6KG9z1by0KYGLI5P6I2Uz%2BEQXrXsq5HMvR5%2Ff93xC7xJ8rfLbgmamLgyed3DLgMN4Jae9%2FFmxjT0o2%2BjNFPeEkxCVPDaJZnoL6lDHI02ojEx19AAVefCeTaDdRd%2BC3O3NSHwUA5n&X-Amz-Signature=0f9f44ae841c9491c1243debeac0d9e1c69ed3af12b7e64644ee038a31f34892&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
