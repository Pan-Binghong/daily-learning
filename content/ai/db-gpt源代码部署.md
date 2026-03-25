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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPOVAOBU%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdi98pyj7liZMgr0VFuTT3hISgMahCz34wfXu2cQKIzAiBHNFO2Gf4rGsjX8z5wr15H4dBIfHBg7pcFfOvGMc7DliqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQdxZWTVyY21vdYotKtwDZ6uqc8cOgq8a7f2rFN9t5wFM1yHz5IhcxGZSBMyh8UuTT%2BB66sWBdtjAbX4x%2Bl8S%2BmsCtHXa9NtW96Kxfr0to37IRUsWCs0VPmAsV69rIS8Mq3jhjsKZ3ioJYkn394bVuks74ElxDTavTngnIykJckCLBfcj1oqaKIFW2LJUBh3IxiiF37yX0RILifMUkWh%2FpayXE%2Frg8ELz4dgaGkwiWC9HsD1T5fU7MFEugWiZMjGPSzasckXonj64eeaK%2FAGu%2BSZAvq%2FikpeIPqtlAu0sP9MtK5DSeIsxVJFiw5ZH7xCz4iuSHRLl5oSKHJq1kflpErC9vg1WsIEv7nJ7IN6cdngj17%2BnMVcfnowW%2FzpMYKuaToj%2Fisw0d6tnhnNN9ES3yFWavzkOCqDo6LiXBfT0khQ53cVniHdAC8PX%2FYLbqkhIhEEUqs8sp47zdXF61yxgHqdQ2EYsnM2wGOgHtmXFyydLbNU8PH%2B24nlozOaDm6J7lc97v6f%2BvAmznVpmFWX%2BFPmesPSAHTRrcrbANMm6H%2FfPIb8FxtUULgGxT3wvvUoYrxjt%2FVDegCcCSS2i8E%2F%2F7rkEQt5ruWbhTqzutHIuEYjrM9WCFoe3Nytub984%2Fp5%2Bl7jaLkBgyIgNW3ww1KSNzgY6pgG%2FBY8Qw7VPu%2FISxbOJDPOwqdwCglZg0bOzb60rk%2BkTGf7L3NDf2s8S8p7q%2F3WpSsPIQE7LmW2UKJY2Qmnb79faSgrLHSRrUh5TYUvuwqnqt%2Bg9J5ftMMXG2mTyZPHrg9ZW%2BRgm%2B109OBUDNAl7MvSbGYxMcvOW2Mlx45bkrANpnDI8FOmUVuQd1keG7KfQmxzseE463pULnHxxJFLVfssFThb3KcyK&X-Amz-Signature=aeaff0b5c054b5ffb8bb7af0f09a18bb8e62a7e8321f6a7d21e711ce8ef5a6a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
