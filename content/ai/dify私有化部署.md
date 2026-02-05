---
title: Dify私有化部署
date: '2024-11-15T09:08:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- Dify
categories:
- AI
---

# 1.创建服务器准备工作

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYAMRQT%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIB3RsN4g%2FtitqgKqdBssSj6kkjeX%2BWSdqnIyoBXo%2BHB9AiBIESjFfS%2FoSuVDRQ7m0q8RVsNZ5C8DiOJtTYv90wtGfCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMBSfdW8XfGBCcLeo3KtwDVkVAv%2B2m%2BokTzf1It6%2FZTP87Iwc7byzsjeAVG7oPaXrVAT9RA%2F9NZLBE1EH4%2BtF60Q%2BE2MVRGIAIaUqXgul010dD2sr7zfxYStwFr6p0zaH0Q0x31SDwj%2B1yGUYgaLVgIeoK1ypY7SzypZKuh6ZVYxFqJH%2B7PxBiipOlVSK0UCpVaDgBHdgvDoGFl%2FRzGDXyHjM1uw3AHyAUqRpuTtAu4nmGLaHScMFWF6Hg2svfT5NYKeBzmkNsKETgz1nFah2%2BWo9Rg6h5QqUBqHg9CR8aOGgjITvVaZDpvtXjfmm5kpJj1vU18FX%2BXTn8j5Y4h%2FCIqRFoN0CBgZKk83bUjmOwkke5SqrjA3aj%2FYzpo4EOtzuTSSWo%2FJDlrcGiGYv7e6FXb4HW%2FyxPEIv2NbqHHSUDplPkTONK%2BTHEBB0QQff3Nlz7OUZpJDtxnMpDDn616wYaU1M4zIpTclZIWv7ch8JrT3klzSIW4dlK%2BEucgSats7sfO7XkuDw2wYf6R%2BbhuOdEk4p62YodWtx0L5Af%2FdPl5kuIsDQcw821ug8C4YxUsKtYrFsvy%2BYRh1hhQJvI4ZpplTvp9sCoWH9c%2FEW8i6vPuisqL1jX%2FrQAfhAdfmt94%2FNsZ7taA%2FwyCrFT3bwwnJOQzAY6pgGKlfymSrByvivekeNvCwxGvVD1IOP4OY8iXwINJ23uGrac7aG%2B1cW4iandK7CRz3%2Fy9EyTkyZDzf%2F7UynuLRskwzbmaEWaeKh9Rjes2gnwI%2B9ZMyVZ7Zsq9218L9TnzgU8VDq2D95%2Ba%2Fy1iTzzdJiSN27XWqKPn21YuES0XTVU31iX%2BjdzzyNYY7kI7ndSfbU83XynwVq1hCDjQZPOiFR4l7tTBb2o&X-Amz-Signature=7fea200aa477567dfc59a6017fbb2b8b05b4047afd7a2ec5427bd6e8a7c9e0b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYAMRQT%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033504Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIB3RsN4g%2FtitqgKqdBssSj6kkjeX%2BWSdqnIyoBXo%2BHB9AiBIESjFfS%2FoSuVDRQ7m0q8RVsNZ5C8DiOJtTYv90wtGfCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMBSfdW8XfGBCcLeo3KtwDVkVAv%2B2m%2BokTzf1It6%2FZTP87Iwc7byzsjeAVG7oPaXrVAT9RA%2F9NZLBE1EH4%2BtF60Q%2BE2MVRGIAIaUqXgul010dD2sr7zfxYStwFr6p0zaH0Q0x31SDwj%2B1yGUYgaLVgIeoK1ypY7SzypZKuh6ZVYxFqJH%2B7PxBiipOlVSK0UCpVaDgBHdgvDoGFl%2FRzGDXyHjM1uw3AHyAUqRpuTtAu4nmGLaHScMFWF6Hg2svfT5NYKeBzmkNsKETgz1nFah2%2BWo9Rg6h5QqUBqHg9CR8aOGgjITvVaZDpvtXjfmm5kpJj1vU18FX%2BXTn8j5Y4h%2FCIqRFoN0CBgZKk83bUjmOwkke5SqrjA3aj%2FYzpo4EOtzuTSSWo%2FJDlrcGiGYv7e6FXb4HW%2FyxPEIv2NbqHHSUDplPkTONK%2BTHEBB0QQff3Nlz7OUZpJDtxnMpDDn616wYaU1M4zIpTclZIWv7ch8JrT3klzSIW4dlK%2BEucgSats7sfO7XkuDw2wYf6R%2BbhuOdEk4p62YodWtx0L5Af%2FdPl5kuIsDQcw821ug8C4YxUsKtYrFsvy%2BYRh1hhQJvI4ZpplTvp9sCoWH9c%2FEW8i6vPuisqL1jX%2FrQAfhAdfmt94%2FNsZ7taA%2FwyCrFT3bwwnJOQzAY6pgGKlfymSrByvivekeNvCwxGvVD1IOP4OY8iXwINJ23uGrac7aG%2B1cW4iandK7CRz3%2Fy9EyTkyZDzf%2F7UynuLRskwzbmaEWaeKh9Rjes2gnwI%2B9ZMyVZ7Zsq9218L9TnzgU8VDq2D95%2Ba%2Fy1iTzzdJiSN27XWqKPn21YuES0XTVU31iX%2BjdzzyNYY7kI7ndSfbU83XynwVq1hCDjQZPOiFR4l7tTBb2o&X-Amz-Signature=049962dea2930b10b4dbfa2bc98539aed0b3f0524b7f22cbda41f9b908531479&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

服务器的系统选择Ubuntu 22.04版本并且克隆 Dify 源代码至本地环境

```javascript
git clone https://github.com/langgenius/dify.git
```

# 2.安装docker和docker compose



## 首先，确保你的软件包是最新的：

```javascript
sudo apt-get update
sudo apt-get upgrade -y
```

## 安装docker

### 第一种方法(一键安装)

```javascript
curl -sSL get-docker.geekery.cn | bash
```

### 第二种方法

```javascript
# 安装必要的依赖，让apt支持https
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# 添加 Docker 的官方 GPG 密钥
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 添加 Docker APT 仓库
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 更新 APT 包索引
sudo apt-get update

# 安装 Docker CE
sudo apt-get install -y docker-ce
#验证安装
docker version
```



## 安装docker compose

### 下载最新的 Docker Compose 二进制文件

```javascript
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

```

### 为 Docker Compose 二进制文件添加执行权限

```javascript
sudo chmod +x /usr/local/bin/docker-compose
```

### 验证安装

```javascript
docker-compose --version
```



# 3.docker换源和配置DNS

## docker换源

首先输入

```javascript
vim /etc/docker/daemon.json 
```

按“I”进入编辑者模式之后把一下代码粘贴进去



```javascript
{
    "registry-mirrors": [
        "https://dockerproxy.cn",
        "https://docker.rainbond.cc",
        "https://docker.udayun.com",
        "https://docker.211678.top"
    ]
}
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYAMRQT%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIB3RsN4g%2FtitqgKqdBssSj6kkjeX%2BWSdqnIyoBXo%2BHB9AiBIESjFfS%2FoSuVDRQ7m0q8RVsNZ5C8DiOJtTYv90wtGfCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMBSfdW8XfGBCcLeo3KtwDVkVAv%2B2m%2BokTzf1It6%2FZTP87Iwc7byzsjeAVG7oPaXrVAT9RA%2F9NZLBE1EH4%2BtF60Q%2BE2MVRGIAIaUqXgul010dD2sr7zfxYStwFr6p0zaH0Q0x31SDwj%2B1yGUYgaLVgIeoK1ypY7SzypZKuh6ZVYxFqJH%2B7PxBiipOlVSK0UCpVaDgBHdgvDoGFl%2FRzGDXyHjM1uw3AHyAUqRpuTtAu4nmGLaHScMFWF6Hg2svfT5NYKeBzmkNsKETgz1nFah2%2BWo9Rg6h5QqUBqHg9CR8aOGgjITvVaZDpvtXjfmm5kpJj1vU18FX%2BXTn8j5Y4h%2FCIqRFoN0CBgZKk83bUjmOwkke5SqrjA3aj%2FYzpo4EOtzuTSSWo%2FJDlrcGiGYv7e6FXb4HW%2FyxPEIv2NbqHHSUDplPkTONK%2BTHEBB0QQff3Nlz7OUZpJDtxnMpDDn616wYaU1M4zIpTclZIWv7ch8JrT3klzSIW4dlK%2BEucgSats7sfO7XkuDw2wYf6R%2BbhuOdEk4p62YodWtx0L5Af%2FdPl5kuIsDQcw821ug8C4YxUsKtYrFsvy%2BYRh1hhQJvI4ZpplTvp9sCoWH9c%2FEW8i6vPuisqL1jX%2FrQAfhAdfmt94%2FNsZ7taA%2FwyCrFT3bwwnJOQzAY6pgGKlfymSrByvivekeNvCwxGvVD1IOP4OY8iXwINJ23uGrac7aG%2B1cW4iandK7CRz3%2Fy9EyTkyZDzf%2F7UynuLRskwzbmaEWaeKh9Rjes2gnwI%2B9ZMyVZ7Zsq9218L9TnzgU8VDq2D95%2Ba%2Fy1iTzzdJiSN27XWqKPn21YuES0XTVU31iX%2BjdzzyNYY7kI7ndSfbU83XynwVq1hCDjQZPOiFR4l7tTBb2o&X-Amz-Signature=30946a0311a3eddeed74b2d199d1961064cc49974b9295f98709d2035c6a7d9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

粘贴完成之后按“esc”键，在同时按“shift”和“;”进入上帝模式输入wq保存退出

最后重新启动docker

```javascript
systemctl restart docker
```



## 配置DNS



- 备份文件：
- 修改文件内容：
最后重新启动相关网络服务

```javascript
systemctl restart systemd-resolved
```

# 4.启动dify

### 进入 Dify 源代码的 Docker 目录

```plain text
cd dify/docker
```



### 启动 Docker 容器

根据你系统上的 Docker Compose 版本，选择合适的命令来启动容器。你可以通过 $ docker compose version 命令检查版本，详细说明请参考 Docker 官方文档：

- 如果版本是 Docker Compose V2，使用以下命令：
```plain text
docker compose up -d
```

- 如果版本是 Docker Compose V1，使用以下命令：
```plain text
docker-compose up -d
```



输入docker ps和docker compose ps看看是否启动

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYAMRQT%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIB3RsN4g%2FtitqgKqdBssSj6kkjeX%2BWSdqnIyoBXo%2BHB9AiBIESjFfS%2FoSuVDRQ7m0q8RVsNZ5C8DiOJtTYv90wtGfCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMBSfdW8XfGBCcLeo3KtwDVkVAv%2B2m%2BokTzf1It6%2FZTP87Iwc7byzsjeAVG7oPaXrVAT9RA%2F9NZLBE1EH4%2BtF60Q%2BE2MVRGIAIaUqXgul010dD2sr7zfxYStwFr6p0zaH0Q0x31SDwj%2B1yGUYgaLVgIeoK1ypY7SzypZKuh6ZVYxFqJH%2B7PxBiipOlVSK0UCpVaDgBHdgvDoGFl%2FRzGDXyHjM1uw3AHyAUqRpuTtAu4nmGLaHScMFWF6Hg2svfT5NYKeBzmkNsKETgz1nFah2%2BWo9Rg6h5QqUBqHg9CR8aOGgjITvVaZDpvtXjfmm5kpJj1vU18FX%2BXTn8j5Y4h%2FCIqRFoN0CBgZKk83bUjmOwkke5SqrjA3aj%2FYzpo4EOtzuTSSWo%2FJDlrcGiGYv7e6FXb4HW%2FyxPEIv2NbqHHSUDplPkTONK%2BTHEBB0QQff3Nlz7OUZpJDtxnMpDDn616wYaU1M4zIpTclZIWv7ch8JrT3klzSIW4dlK%2BEucgSats7sfO7XkuDw2wYf6R%2BbhuOdEk4p62YodWtx0L5Af%2FdPl5kuIsDQcw821ug8C4YxUsKtYrFsvy%2BYRh1hhQJvI4ZpplTvp9sCoWH9c%2FEW8i6vPuisqL1jX%2FrQAfhAdfmt94%2FNsZ7taA%2FwyCrFT3bwwnJOQzAY6pgGKlfymSrByvivekeNvCwxGvVD1IOP4OY8iXwINJ23uGrac7aG%2B1cW4iandK7CRz3%2Fy9EyTkyZDzf%2F7UynuLRskwzbmaEWaeKh9Rjes2gnwI%2B9ZMyVZ7Zsq9218L9TnzgU8VDq2D95%2Ba%2Fy1iTzzdJiSN27XWqKPn21YuES0XTVU31iX%2BjdzzyNYY7kI7ndSfbU83XynwVq1hCDjQZPOiFR4l7tTBb2o&X-Amz-Signature=10a2ae5c688820482adabd5e23444c15c655b11c2a03b65dcf2766007e57b51c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYAMRQT%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIB3RsN4g%2FtitqgKqdBssSj6kkjeX%2BWSdqnIyoBXo%2BHB9AiBIESjFfS%2FoSuVDRQ7m0q8RVsNZ5C8DiOJtTYv90wtGfCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMBSfdW8XfGBCcLeo3KtwDVkVAv%2B2m%2BokTzf1It6%2FZTP87Iwc7byzsjeAVG7oPaXrVAT9RA%2F9NZLBE1EH4%2BtF60Q%2BE2MVRGIAIaUqXgul010dD2sr7zfxYStwFr6p0zaH0Q0x31SDwj%2B1yGUYgaLVgIeoK1ypY7SzypZKuh6ZVYxFqJH%2B7PxBiipOlVSK0UCpVaDgBHdgvDoGFl%2FRzGDXyHjM1uw3AHyAUqRpuTtAu4nmGLaHScMFWF6Hg2svfT5NYKeBzmkNsKETgz1nFah2%2BWo9Rg6h5QqUBqHg9CR8aOGgjITvVaZDpvtXjfmm5kpJj1vU18FX%2BXTn8j5Y4h%2FCIqRFoN0CBgZKk83bUjmOwkke5SqrjA3aj%2FYzpo4EOtzuTSSWo%2FJDlrcGiGYv7e6FXb4HW%2FyxPEIv2NbqHHSUDplPkTONK%2BTHEBB0QQff3Nlz7OUZpJDtxnMpDDn616wYaU1M4zIpTclZIWv7ch8JrT3klzSIW4dlK%2BEucgSats7sfO7XkuDw2wYf6R%2BbhuOdEk4p62YodWtx0L5Af%2FdPl5kuIsDQcw821ug8C4YxUsKtYrFsvy%2BYRh1hhQJvI4ZpplTvp9sCoWH9c%2FEW8i6vPuisqL1jX%2FrQAfhAdfmt94%2FNsZ7taA%2FwyCrFT3bwwnJOQzAY6pgGKlfymSrByvivekeNvCwxGvVD1IOP4OY8iXwINJ23uGrac7aG%2B1cW4iandK7CRz3%2Fy9EyTkyZDzf%2F7UynuLRskwzbmaEWaeKh9Rjes2gnwI%2B9ZMyVZ7Zsq9218L9TnzgU8VDq2D95%2Ba%2Fy1iTzzdJiSN27XWqKPn21YuES0XTVU31iX%2BjdzzyNYY7kI7ndSfbU83XynwVq1hCDjQZPOiFR4l7tTBb2o&X-Amz-Signature=c0a8a28c9d0506f1bb8f407385f704e34597e10d31520a8bdde9973374cf7ec6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYAMRQT%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIB3RsN4g%2FtitqgKqdBssSj6kkjeX%2BWSdqnIyoBXo%2BHB9AiBIESjFfS%2FoSuVDRQ7m0q8RVsNZ5C8DiOJtTYv90wtGfCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMBSfdW8XfGBCcLeo3KtwDVkVAv%2B2m%2BokTzf1It6%2FZTP87Iwc7byzsjeAVG7oPaXrVAT9RA%2F9NZLBE1EH4%2BtF60Q%2BE2MVRGIAIaUqXgul010dD2sr7zfxYStwFr6p0zaH0Q0x31SDwj%2B1yGUYgaLVgIeoK1ypY7SzypZKuh6ZVYxFqJH%2B7PxBiipOlVSK0UCpVaDgBHdgvDoGFl%2FRzGDXyHjM1uw3AHyAUqRpuTtAu4nmGLaHScMFWF6Hg2svfT5NYKeBzmkNsKETgz1nFah2%2BWo9Rg6h5QqUBqHg9CR8aOGgjITvVaZDpvtXjfmm5kpJj1vU18FX%2BXTn8j5Y4h%2FCIqRFoN0CBgZKk83bUjmOwkke5SqrjA3aj%2FYzpo4EOtzuTSSWo%2FJDlrcGiGYv7e6FXb4HW%2FyxPEIv2NbqHHSUDplPkTONK%2BTHEBB0QQff3Nlz7OUZpJDtxnMpDDn616wYaU1M4zIpTclZIWv7ch8JrT3klzSIW4dlK%2BEucgSats7sfO7XkuDw2wYf6R%2BbhuOdEk4p62YodWtx0L5Af%2FdPl5kuIsDQcw821ug8C4YxUsKtYrFsvy%2BYRh1hhQJvI4ZpplTvp9sCoWH9c%2FEW8i6vPuisqL1jX%2FrQAfhAdfmt94%2FNsZ7taA%2FwyCrFT3bwwnJOQzAY6pgGKlfymSrByvivekeNvCwxGvVD1IOP4OY8iXwINJ23uGrac7aG%2B1cW4iandK7CRz3%2Fy9EyTkyZDzf%2F7UynuLRskwzbmaEWaeKh9Rjes2gnwI%2B9ZMyVZ7Zsq9218L9TnzgU8VDq2D95%2Ba%2Fy1iTzzdJiSN27XWqKPn21YuES0XTVU31iX%2BjdzzyNYY7kI7ndSfbU83XynwVq1hCDjQZPOiFR4l7tTBb2o&X-Amz-Signature=87beee8c2b860782bee10804f45946877fe49e5cc6a669650267ec383614e4c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYAMRQT%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIB3RsN4g%2FtitqgKqdBssSj6kkjeX%2BWSdqnIyoBXo%2BHB9AiBIESjFfS%2FoSuVDRQ7m0q8RVsNZ5C8DiOJtTYv90wtGfCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMBSfdW8XfGBCcLeo3KtwDVkVAv%2B2m%2BokTzf1It6%2FZTP87Iwc7byzsjeAVG7oPaXrVAT9RA%2F9NZLBE1EH4%2BtF60Q%2BE2MVRGIAIaUqXgul010dD2sr7zfxYStwFr6p0zaH0Q0x31SDwj%2B1yGUYgaLVgIeoK1ypY7SzypZKuh6ZVYxFqJH%2B7PxBiipOlVSK0UCpVaDgBHdgvDoGFl%2FRzGDXyHjM1uw3AHyAUqRpuTtAu4nmGLaHScMFWF6Hg2svfT5NYKeBzmkNsKETgz1nFah2%2BWo9Rg6h5QqUBqHg9CR8aOGgjITvVaZDpvtXjfmm5kpJj1vU18FX%2BXTn8j5Y4h%2FCIqRFoN0CBgZKk83bUjmOwkke5SqrjA3aj%2FYzpo4EOtzuTSSWo%2FJDlrcGiGYv7e6FXb4HW%2FyxPEIv2NbqHHSUDplPkTONK%2BTHEBB0QQff3Nlz7OUZpJDtxnMpDDn616wYaU1M4zIpTclZIWv7ch8JrT3klzSIW4dlK%2BEucgSats7sfO7XkuDw2wYf6R%2BbhuOdEk4p62YodWtx0L5Af%2FdPl5kuIsDQcw821ug8C4YxUsKtYrFsvy%2BYRh1hhQJvI4ZpplTvp9sCoWH9c%2FEW8i6vPuisqL1jX%2FrQAfhAdfmt94%2FNsZ7taA%2FwyCrFT3bwwnJOQzAY6pgGKlfymSrByvivekeNvCwxGvVD1IOP4OY8iXwINJ23uGrac7aG%2B1cW4iandK7CRz3%2Fy9EyTkyZDzf%2F7UynuLRskwzbmaEWaeKh9Rjes2gnwI%2B9ZMyVZ7Zsq9218L9TnzgU8VDq2D95%2Ba%2Fy1iTzzdJiSN27XWqKPn21YuES0XTVU31iX%2BjdzzyNYY7kI7ndSfbU83XynwVq1hCDjQZPOiFR4l7tTBb2o&X-Amz-Signature=7074d469d331454159b40e8fb81cf0ec754ce9ef9e05e9fecdf5f66b7566e200&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYAMRQT%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIB3RsN4g%2FtitqgKqdBssSj6kkjeX%2BWSdqnIyoBXo%2BHB9AiBIESjFfS%2FoSuVDRQ7m0q8RVsNZ5C8DiOJtTYv90wtGfCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMBSfdW8XfGBCcLeo3KtwDVkVAv%2B2m%2BokTzf1It6%2FZTP87Iwc7byzsjeAVG7oPaXrVAT9RA%2F9NZLBE1EH4%2BtF60Q%2BE2MVRGIAIaUqXgul010dD2sr7zfxYStwFr6p0zaH0Q0x31SDwj%2B1yGUYgaLVgIeoK1ypY7SzypZKuh6ZVYxFqJH%2B7PxBiipOlVSK0UCpVaDgBHdgvDoGFl%2FRzGDXyHjM1uw3AHyAUqRpuTtAu4nmGLaHScMFWF6Hg2svfT5NYKeBzmkNsKETgz1nFah2%2BWo9Rg6h5QqUBqHg9CR8aOGgjITvVaZDpvtXjfmm5kpJj1vU18FX%2BXTn8j5Y4h%2FCIqRFoN0CBgZKk83bUjmOwkke5SqrjA3aj%2FYzpo4EOtzuTSSWo%2FJDlrcGiGYv7e6FXb4HW%2FyxPEIv2NbqHHSUDplPkTONK%2BTHEBB0QQff3Nlz7OUZpJDtxnMpDDn616wYaU1M4zIpTclZIWv7ch8JrT3klzSIW4dlK%2BEucgSats7sfO7XkuDw2wYf6R%2BbhuOdEk4p62YodWtx0L5Af%2FdPl5kuIsDQcw821ug8C4YxUsKtYrFsvy%2BYRh1hhQJvI4ZpplTvp9sCoWH9c%2FEW8i6vPuisqL1jX%2FrQAfhAdfmt94%2FNsZ7taA%2FwyCrFT3bwwnJOQzAY6pgGKlfymSrByvivekeNvCwxGvVD1IOP4OY8iXwINJ23uGrac7aG%2B1cW4iandK7CRz3%2Fy9EyTkyZDzf%2F7UynuLRskwzbmaEWaeKh9Rjes2gnwI%2B9ZMyVZ7Zsq9218L9TnzgU8VDq2D95%2Ba%2Fy1iTzzdJiSN27XWqKPn21YuES0XTVU31iX%2BjdzzyNYY7kI7ndSfbU83XynwVq1hCDjQZPOiFR4l7tTBb2o&X-Amz-Signature=899f1daf37c531ab8d446592460af71486e2a4d0307a56ca074825635b423bae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYAMRQT%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIB3RsN4g%2FtitqgKqdBssSj6kkjeX%2BWSdqnIyoBXo%2BHB9AiBIESjFfS%2FoSuVDRQ7m0q8RVsNZ5C8DiOJtTYv90wtGfCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMBSfdW8XfGBCcLeo3KtwDVkVAv%2B2m%2BokTzf1It6%2FZTP87Iwc7byzsjeAVG7oPaXrVAT9RA%2F9NZLBE1EH4%2BtF60Q%2BE2MVRGIAIaUqXgul010dD2sr7zfxYStwFr6p0zaH0Q0x31SDwj%2B1yGUYgaLVgIeoK1ypY7SzypZKuh6ZVYxFqJH%2B7PxBiipOlVSK0UCpVaDgBHdgvDoGFl%2FRzGDXyHjM1uw3AHyAUqRpuTtAu4nmGLaHScMFWF6Hg2svfT5NYKeBzmkNsKETgz1nFah2%2BWo9Rg6h5QqUBqHg9CR8aOGgjITvVaZDpvtXjfmm5kpJj1vU18FX%2BXTn8j5Y4h%2FCIqRFoN0CBgZKk83bUjmOwkke5SqrjA3aj%2FYzpo4EOtzuTSSWo%2FJDlrcGiGYv7e6FXb4HW%2FyxPEIv2NbqHHSUDplPkTONK%2BTHEBB0QQff3Nlz7OUZpJDtxnMpDDn616wYaU1M4zIpTclZIWv7ch8JrT3klzSIW4dlK%2BEucgSats7sfO7XkuDw2wYf6R%2BbhuOdEk4p62YodWtx0L5Af%2FdPl5kuIsDQcw821ug8C4YxUsKtYrFsvy%2BYRh1hhQJvI4ZpplTvp9sCoWH9c%2FEW8i6vPuisqL1jX%2FrQAfhAdfmt94%2FNsZ7taA%2FwyCrFT3bwwnJOQzAY6pgGKlfymSrByvivekeNvCwxGvVD1IOP4OY8iXwINJ23uGrac7aG%2B1cW4iandK7CRz3%2Fy9EyTkyZDzf%2F7UynuLRskwzbmaEWaeKh9Rjes2gnwI%2B9ZMyVZ7Zsq9218L9TnzgU8VDq2D95%2Ba%2Fy1iTzzdJiSN27XWqKPn21YuES0XTVU31iX%2BjdzzyNYY7kI7ndSfbU83XynwVq1hCDjQZPOiFR4l7tTBb2o&X-Amz-Signature=55f6d2af8e699e26251d1914c0746f0af654e991963664eb803a0083a116e0fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXYAMRQT%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIB3RsN4g%2FtitqgKqdBssSj6kkjeX%2BWSdqnIyoBXo%2BHB9AiBIESjFfS%2FoSuVDRQ7m0q8RVsNZ5C8DiOJtTYv90wtGfCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMBSfdW8XfGBCcLeo3KtwDVkVAv%2B2m%2BokTzf1It6%2FZTP87Iwc7byzsjeAVG7oPaXrVAT9RA%2F9NZLBE1EH4%2BtF60Q%2BE2MVRGIAIaUqXgul010dD2sr7zfxYStwFr6p0zaH0Q0x31SDwj%2B1yGUYgaLVgIeoK1ypY7SzypZKuh6ZVYxFqJH%2B7PxBiipOlVSK0UCpVaDgBHdgvDoGFl%2FRzGDXyHjM1uw3AHyAUqRpuTtAu4nmGLaHScMFWF6Hg2svfT5NYKeBzmkNsKETgz1nFah2%2BWo9Rg6h5QqUBqHg9CR8aOGgjITvVaZDpvtXjfmm5kpJj1vU18FX%2BXTn8j5Y4h%2FCIqRFoN0CBgZKk83bUjmOwkke5SqrjA3aj%2FYzpo4EOtzuTSSWo%2FJDlrcGiGYv7e6FXb4HW%2FyxPEIv2NbqHHSUDplPkTONK%2BTHEBB0QQff3Nlz7OUZpJDtxnMpDDn616wYaU1M4zIpTclZIWv7ch8JrT3klzSIW4dlK%2BEucgSats7sfO7XkuDw2wYf6R%2BbhuOdEk4p62YodWtx0L5Af%2FdPl5kuIsDQcw821ug8C4YxUsKtYrFsvy%2BYRh1hhQJvI4ZpplTvp9sCoWH9c%2FEW8i6vPuisqL1jX%2FrQAfhAdfmt94%2FNsZ7taA%2FwyCrFT3bwwnJOQzAY6pgGKlfymSrByvivekeNvCwxGvVD1IOP4OY8iXwINJ23uGrac7aG%2B1cW4iandK7CRz3%2Fy9EyTkyZDzf%2F7UynuLRskwzbmaEWaeKh9Rjes2gnwI%2B9ZMyVZ7Zsq9218L9TnzgU8VDq2D95%2Ba%2Fy1iTzzdJiSN27XWqKPn21YuES0XTVU31iX%2BjdzzyNYY7kI7ndSfbU83XynwVq1hCDjQZPOiFR4l7tTBb2o&X-Amz-Signature=229b82b0e9e1e27d105f202f04d36b734bb750fdabe77fed0f3ec7d11ead11ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

