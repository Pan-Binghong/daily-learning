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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKV4D6HP%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T040924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQDpsdUCrRrwFbycrZkVOWUrHfJQCTvn1XJBZuTOnRb1yAIhAMPyjfEX3QYAhh9kVSTjqPR4CzPzrF5%2F7ZeSYy%2BbHFCMKv8DCBwQABoMNjM3NDIzMTgzODA1IgxZHGBpB%2FK5NjaH0egq3AMJXuHc2If0STKzwDn1Rwz7HI9NBHgBIoR0dRfdscx%2Fip%2FW9CSxJfym2V1t0mUZJjuGBjbTc9DGoFGVIYah65TuhO%2F3YW31UISu9ZGcdnJUIUGeaz4x7O7NGyqMeEZT0XMmc8ygByW1f73mtNRswHce9Dwo6PVYpYOoSk1aSABIFnPsPY2iikG2zFAxl94sRF1%2FiiNLIvq6C86WraXNJv4XqSfAiPyErnav3p2ZXHtWMQbQlafhGKX1uV1KCzoqvLba8YoP17BMyHuXVcY6yFlpqsfmXTyEVrQhqYHa2Aiew9CJ8PSTNb6v95VxeF6A63gwJoXyx7yiEkMjv331QmIGq79IVxIy%2Fp0P%2BLxDkl%2FvYRkzRSyP7MgKNy%2Bq%2FhvW7VRIYtIvOW8INEbjBZqvekK7hzpthe%2FDtc76IqQ2Vv1NiM4lA27%2FMiaxYu2JZBOeZtPkeKxQfcY1WXHPRe5jWTcTzwjKOjBoosRtlw8lmMTak5Pzaacx0X9N1KYj2rMuBm1nW4U1pPnjH2w5aAj3eBqq1uKvDRQqp1gTPZnnUbyGhxfZf5SMYFWwhDI1C%2BTL5rcAGRgcWyiKSC8BiAgMYMnfnhs6ecL6DiiMF7hcBYn%2BCV7m6VUa1eMv6TKTBTDsx6fOBjqkAbgntwXUJLIMsACdPmLEX13TPgk67QyGqu4PI3IkMkYlpCAhr941%2FpT81mB9gcB%2FaHocLEUbpHNLsGPbHX%2BDqRh7vfW5RVjNc0ELU0RBcNf5HEkxSyfgWRUBrklK2kSoYReX%2F52AmGTb%2BR2o1rccE6ZTbzlShZgrVRbO2X9Ew%2FcbKM3%2BNNeqwks9H9v9pBtPpKWsTiQXq%2BpqPSABTFCyoiN5ppw3&X-Amz-Signature=150986ad0e49de9f578f4d5ed3c82a91fd1060933d9048833d1d193939c3042a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
