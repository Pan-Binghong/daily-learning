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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6NMA3UR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdjpGnj1Q5LhZo8jniP6Oy8rKwAV1WlfdS4X8wLL5C2AiAMyuuRJbnOM9%2BKlL2PtGyOxNts0TnTag35mLv9vpn4VSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMgcHQIge%2B9CNp1AoCKtwDx3H6qC1AEpoMNoFjuTmQsTA9k9zzrejUUpam9a9aE5hrayZThzPxNhltkfBA5Qdb6jr8Aoc%2BoVKo3iNRHBoIC%2FQ2OCHfWApt%2F6xGDNi2JDsIQdA4i2rLXCvYGl7qJJ0B2yiV2kLoZ79lQOZzmzmUulkxuREpLBZzxHWZBfk5QztLCBypRlWsN9Sc9JCpsvYm80c8rkKf%2BYWWKSMF9sECdPzXdk0z%2FqOqyoTAaYakeYNBrT86vtH0O3%2FDAzfWTQEEcArZaeOWwv%2BJX6lZCEY8sSxju80smM9MXOIWYz4dtPvxOBrXJc5bTOfJ9HO5JftIheOHxTv%2Bc8u2cXKEiNRM74cNx3Q3RFLmIVQySxosAd1AlvrAjiQzKKvHP1sFMAWsgURf0mDD7J%2FhNU8rysXF1%2FQ%2F3rQij6ZmPVzj8cqH%2FkQaECjfHR22sbRTd0%2F9txczVjJEP%2BYGFgQOTzqkZz6cE1gKfgd9bH%2BtmgP%2Fp0mt8jL6rhWSq0OKMgO0YBdUKy04PGK60%2FMmc37V9wA3r54R9SY2sedmKUc9tInsXSSaSroMVp89tXJjcpNItVnMNq6MUZFboADuf9YCSf9i%2FtCtC3YNNU55vCYZOX6XGn0tAqPxO7fJHo0EXFCKossw3InayAY6pgGITwfVl7t9P8RRqmQaOZIDXTFpleKn%2FMfrwTfNNp3touH9taHIvtvWNtZdU5o%2FrBdWQ3PZsG%2FVHpcev%2Fuikqz2ULULHIXkrPG65mJ9sPns8jZ5opNCl1WuRidBlQW1OMzqKLmNC6sXqDcZpndk2%2B0xGKKjD8CxR82Lbx269IgDEzN6SAWCGLmm7A5smIMg0Vv6rR32zQFuhnGNO4W0P%2FuE8tADn0e%2F&X-Amz-Signature=141710cc31f04faae039b51989f15f98f2f8a00985829fa751f1d6ce3d7a7b9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6NMA3UR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdjpGnj1Q5LhZo8jniP6Oy8rKwAV1WlfdS4X8wLL5C2AiAMyuuRJbnOM9%2BKlL2PtGyOxNts0TnTag35mLv9vpn4VSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMgcHQIge%2B9CNp1AoCKtwDx3H6qC1AEpoMNoFjuTmQsTA9k9zzrejUUpam9a9aE5hrayZThzPxNhltkfBA5Qdb6jr8Aoc%2BoVKo3iNRHBoIC%2FQ2OCHfWApt%2F6xGDNi2JDsIQdA4i2rLXCvYGl7qJJ0B2yiV2kLoZ79lQOZzmzmUulkxuREpLBZzxHWZBfk5QztLCBypRlWsN9Sc9JCpsvYm80c8rkKf%2BYWWKSMF9sECdPzXdk0z%2FqOqyoTAaYakeYNBrT86vtH0O3%2FDAzfWTQEEcArZaeOWwv%2BJX6lZCEY8sSxju80smM9MXOIWYz4dtPvxOBrXJc5bTOfJ9HO5JftIheOHxTv%2Bc8u2cXKEiNRM74cNx3Q3RFLmIVQySxosAd1AlvrAjiQzKKvHP1sFMAWsgURf0mDD7J%2FhNU8rysXF1%2FQ%2F3rQij6ZmPVzj8cqH%2FkQaECjfHR22sbRTd0%2F9txczVjJEP%2BYGFgQOTzqkZz6cE1gKfgd9bH%2BtmgP%2Fp0mt8jL6rhWSq0OKMgO0YBdUKy04PGK60%2FMmc37V9wA3r54R9SY2sedmKUc9tInsXSSaSroMVp89tXJjcpNItVnMNq6MUZFboADuf9YCSf9i%2FtCtC3YNNU55vCYZOX6XGn0tAqPxO7fJHo0EXFCKossw3InayAY6pgGITwfVl7t9P8RRqmQaOZIDXTFpleKn%2FMfrwTfNNp3touH9taHIvtvWNtZdU5o%2FrBdWQ3PZsG%2FVHpcev%2Fuikqz2ULULHIXkrPG65mJ9sPns8jZ5opNCl1WuRidBlQW1OMzqKLmNC6sXqDcZpndk2%2B0xGKKjD8CxR82Lbx269IgDEzN6SAWCGLmm7A5smIMg0Vv6rR32zQFuhnGNO4W0P%2FuE8tADn0e%2F&X-Amz-Signature=a99ecf1fb69e2763e5e5d05ed94590662f83756a136773f0e339dd8260e3f56d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6NMA3UR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdjpGnj1Q5LhZo8jniP6Oy8rKwAV1WlfdS4X8wLL5C2AiAMyuuRJbnOM9%2BKlL2PtGyOxNts0TnTag35mLv9vpn4VSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMgcHQIge%2B9CNp1AoCKtwDx3H6qC1AEpoMNoFjuTmQsTA9k9zzrejUUpam9a9aE5hrayZThzPxNhltkfBA5Qdb6jr8Aoc%2BoVKo3iNRHBoIC%2FQ2OCHfWApt%2F6xGDNi2JDsIQdA4i2rLXCvYGl7qJJ0B2yiV2kLoZ79lQOZzmzmUulkxuREpLBZzxHWZBfk5QztLCBypRlWsN9Sc9JCpsvYm80c8rkKf%2BYWWKSMF9sECdPzXdk0z%2FqOqyoTAaYakeYNBrT86vtH0O3%2FDAzfWTQEEcArZaeOWwv%2BJX6lZCEY8sSxju80smM9MXOIWYz4dtPvxOBrXJc5bTOfJ9HO5JftIheOHxTv%2Bc8u2cXKEiNRM74cNx3Q3RFLmIVQySxosAd1AlvrAjiQzKKvHP1sFMAWsgURf0mDD7J%2FhNU8rysXF1%2FQ%2F3rQij6ZmPVzj8cqH%2FkQaECjfHR22sbRTd0%2F9txczVjJEP%2BYGFgQOTzqkZz6cE1gKfgd9bH%2BtmgP%2Fp0mt8jL6rhWSq0OKMgO0YBdUKy04PGK60%2FMmc37V9wA3r54R9SY2sedmKUc9tInsXSSaSroMVp89tXJjcpNItVnMNq6MUZFboADuf9YCSf9i%2FtCtC3YNNU55vCYZOX6XGn0tAqPxO7fJHo0EXFCKossw3InayAY6pgGITwfVl7t9P8RRqmQaOZIDXTFpleKn%2FMfrwTfNNp3touH9taHIvtvWNtZdU5o%2FrBdWQ3PZsG%2FVHpcev%2Fuikqz2ULULHIXkrPG65mJ9sPns8jZ5opNCl1WuRidBlQW1OMzqKLmNC6sXqDcZpndk2%2B0xGKKjD8CxR82Lbx269IgDEzN6SAWCGLmm7A5smIMg0Vv6rR32zQFuhnGNO4W0P%2FuE8tADn0e%2F&X-Amz-Signature=fa336a7e116a964369a1a243cc90fe22f0375a954e46156c7f7998a157eb1814&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6NMA3UR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdjpGnj1Q5LhZo8jniP6Oy8rKwAV1WlfdS4X8wLL5C2AiAMyuuRJbnOM9%2BKlL2PtGyOxNts0TnTag35mLv9vpn4VSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMgcHQIge%2B9CNp1AoCKtwDx3H6qC1AEpoMNoFjuTmQsTA9k9zzrejUUpam9a9aE5hrayZThzPxNhltkfBA5Qdb6jr8Aoc%2BoVKo3iNRHBoIC%2FQ2OCHfWApt%2F6xGDNi2JDsIQdA4i2rLXCvYGl7qJJ0B2yiV2kLoZ79lQOZzmzmUulkxuREpLBZzxHWZBfk5QztLCBypRlWsN9Sc9JCpsvYm80c8rkKf%2BYWWKSMF9sECdPzXdk0z%2FqOqyoTAaYakeYNBrT86vtH0O3%2FDAzfWTQEEcArZaeOWwv%2BJX6lZCEY8sSxju80smM9MXOIWYz4dtPvxOBrXJc5bTOfJ9HO5JftIheOHxTv%2Bc8u2cXKEiNRM74cNx3Q3RFLmIVQySxosAd1AlvrAjiQzKKvHP1sFMAWsgURf0mDD7J%2FhNU8rysXF1%2FQ%2F3rQij6ZmPVzj8cqH%2FkQaECjfHR22sbRTd0%2F9txczVjJEP%2BYGFgQOTzqkZz6cE1gKfgd9bH%2BtmgP%2Fp0mt8jL6rhWSq0OKMgO0YBdUKy04PGK60%2FMmc37V9wA3r54R9SY2sedmKUc9tInsXSSaSroMVp89tXJjcpNItVnMNq6MUZFboADuf9YCSf9i%2FtCtC3YNNU55vCYZOX6XGn0tAqPxO7fJHo0EXFCKossw3InayAY6pgGITwfVl7t9P8RRqmQaOZIDXTFpleKn%2FMfrwTfNNp3touH9taHIvtvWNtZdU5o%2FrBdWQ3PZsG%2FVHpcev%2Fuikqz2ULULHIXkrPG65mJ9sPns8jZ5opNCl1WuRidBlQW1OMzqKLmNC6sXqDcZpndk2%2B0xGKKjD8CxR82Lbx269IgDEzN6SAWCGLmm7A5smIMg0Vv6rR32zQFuhnGNO4W0P%2FuE8tADn0e%2F&X-Amz-Signature=b802090b3dee8638fe13338a4ca61fe33f05cbb52efd6924115bfee02ccbb829&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6NMA3UR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdjpGnj1Q5LhZo8jniP6Oy8rKwAV1WlfdS4X8wLL5C2AiAMyuuRJbnOM9%2BKlL2PtGyOxNts0TnTag35mLv9vpn4VSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMgcHQIge%2B9CNp1AoCKtwDx3H6qC1AEpoMNoFjuTmQsTA9k9zzrejUUpam9a9aE5hrayZThzPxNhltkfBA5Qdb6jr8Aoc%2BoVKo3iNRHBoIC%2FQ2OCHfWApt%2F6xGDNi2JDsIQdA4i2rLXCvYGl7qJJ0B2yiV2kLoZ79lQOZzmzmUulkxuREpLBZzxHWZBfk5QztLCBypRlWsN9Sc9JCpsvYm80c8rkKf%2BYWWKSMF9sECdPzXdk0z%2FqOqyoTAaYakeYNBrT86vtH0O3%2FDAzfWTQEEcArZaeOWwv%2BJX6lZCEY8sSxju80smM9MXOIWYz4dtPvxOBrXJc5bTOfJ9HO5JftIheOHxTv%2Bc8u2cXKEiNRM74cNx3Q3RFLmIVQySxosAd1AlvrAjiQzKKvHP1sFMAWsgURf0mDD7J%2FhNU8rysXF1%2FQ%2F3rQij6ZmPVzj8cqH%2FkQaECjfHR22sbRTd0%2F9txczVjJEP%2BYGFgQOTzqkZz6cE1gKfgd9bH%2BtmgP%2Fp0mt8jL6rhWSq0OKMgO0YBdUKy04PGK60%2FMmc37V9wA3r54R9SY2sedmKUc9tInsXSSaSroMVp89tXJjcpNItVnMNq6MUZFboADuf9YCSf9i%2FtCtC3YNNU55vCYZOX6XGn0tAqPxO7fJHo0EXFCKossw3InayAY6pgGITwfVl7t9P8RRqmQaOZIDXTFpleKn%2FMfrwTfNNp3touH9taHIvtvWNtZdU5o%2FrBdWQ3PZsG%2FVHpcev%2Fuikqz2ULULHIXkrPG65mJ9sPns8jZ5opNCl1WuRidBlQW1OMzqKLmNC6sXqDcZpndk2%2B0xGKKjD8CxR82Lbx269IgDEzN6SAWCGLmm7A5smIMg0Vv6rR32zQFuhnGNO4W0P%2FuE8tADn0e%2F&X-Amz-Signature=e5d35fcc887e92950970660e35208d39b16266e74b7d57a635b2fe388015337e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6NMA3UR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdjpGnj1Q5LhZo8jniP6Oy8rKwAV1WlfdS4X8wLL5C2AiAMyuuRJbnOM9%2BKlL2PtGyOxNts0TnTag35mLv9vpn4VSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMgcHQIge%2B9CNp1AoCKtwDx3H6qC1AEpoMNoFjuTmQsTA9k9zzrejUUpam9a9aE5hrayZThzPxNhltkfBA5Qdb6jr8Aoc%2BoVKo3iNRHBoIC%2FQ2OCHfWApt%2F6xGDNi2JDsIQdA4i2rLXCvYGl7qJJ0B2yiV2kLoZ79lQOZzmzmUulkxuREpLBZzxHWZBfk5QztLCBypRlWsN9Sc9JCpsvYm80c8rkKf%2BYWWKSMF9sECdPzXdk0z%2FqOqyoTAaYakeYNBrT86vtH0O3%2FDAzfWTQEEcArZaeOWwv%2BJX6lZCEY8sSxju80smM9MXOIWYz4dtPvxOBrXJc5bTOfJ9HO5JftIheOHxTv%2Bc8u2cXKEiNRM74cNx3Q3RFLmIVQySxosAd1AlvrAjiQzKKvHP1sFMAWsgURf0mDD7J%2FhNU8rysXF1%2FQ%2F3rQij6ZmPVzj8cqH%2FkQaECjfHR22sbRTd0%2F9txczVjJEP%2BYGFgQOTzqkZz6cE1gKfgd9bH%2BtmgP%2Fp0mt8jL6rhWSq0OKMgO0YBdUKy04PGK60%2FMmc37V9wA3r54R9SY2sedmKUc9tInsXSSaSroMVp89tXJjcpNItVnMNq6MUZFboADuf9YCSf9i%2FtCtC3YNNU55vCYZOX6XGn0tAqPxO7fJHo0EXFCKossw3InayAY6pgGITwfVl7t9P8RRqmQaOZIDXTFpleKn%2FMfrwTfNNp3touH9taHIvtvWNtZdU5o%2FrBdWQ3PZsG%2FVHpcev%2Fuikqz2ULULHIXkrPG65mJ9sPns8jZ5opNCl1WuRidBlQW1OMzqKLmNC6sXqDcZpndk2%2B0xGKKjD8CxR82Lbx269IgDEzN6SAWCGLmm7A5smIMg0Vv6rR32zQFuhnGNO4W0P%2FuE8tADn0e%2F&X-Amz-Signature=081d2a51e918c3fb8f24fdb3ae95d29399f7b30c6fe4e76303c2990cad93ee83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6NMA3UR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdjpGnj1Q5LhZo8jniP6Oy8rKwAV1WlfdS4X8wLL5C2AiAMyuuRJbnOM9%2BKlL2PtGyOxNts0TnTag35mLv9vpn4VSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMgcHQIge%2B9CNp1AoCKtwDx3H6qC1AEpoMNoFjuTmQsTA9k9zzrejUUpam9a9aE5hrayZThzPxNhltkfBA5Qdb6jr8Aoc%2BoVKo3iNRHBoIC%2FQ2OCHfWApt%2F6xGDNi2JDsIQdA4i2rLXCvYGl7qJJ0B2yiV2kLoZ79lQOZzmzmUulkxuREpLBZzxHWZBfk5QztLCBypRlWsN9Sc9JCpsvYm80c8rkKf%2BYWWKSMF9sECdPzXdk0z%2FqOqyoTAaYakeYNBrT86vtH0O3%2FDAzfWTQEEcArZaeOWwv%2BJX6lZCEY8sSxju80smM9MXOIWYz4dtPvxOBrXJc5bTOfJ9HO5JftIheOHxTv%2Bc8u2cXKEiNRM74cNx3Q3RFLmIVQySxosAd1AlvrAjiQzKKvHP1sFMAWsgURf0mDD7J%2FhNU8rysXF1%2FQ%2F3rQij6ZmPVzj8cqH%2FkQaECjfHR22sbRTd0%2F9txczVjJEP%2BYGFgQOTzqkZz6cE1gKfgd9bH%2BtmgP%2Fp0mt8jL6rhWSq0OKMgO0YBdUKy04PGK60%2FMmc37V9wA3r54R9SY2sedmKUc9tInsXSSaSroMVp89tXJjcpNItVnMNq6MUZFboADuf9YCSf9i%2FtCtC3YNNU55vCYZOX6XGn0tAqPxO7fJHo0EXFCKossw3InayAY6pgGITwfVl7t9P8RRqmQaOZIDXTFpleKn%2FMfrwTfNNp3touH9taHIvtvWNtZdU5o%2FrBdWQ3PZsG%2FVHpcev%2Fuikqz2ULULHIXkrPG65mJ9sPns8jZ5opNCl1WuRidBlQW1OMzqKLmNC6sXqDcZpndk2%2B0xGKKjD8CxR82Lbx269IgDEzN6SAWCGLmm7A5smIMg0Vv6rR32zQFuhnGNO4W0P%2FuE8tADn0e%2F&X-Amz-Signature=0f6e5068a55a8ce94170c018288979d1d32e7c1abbb57c2db3abedd06e85acaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6NMA3UR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdjpGnj1Q5LhZo8jniP6Oy8rKwAV1WlfdS4X8wLL5C2AiAMyuuRJbnOM9%2BKlL2PtGyOxNts0TnTag35mLv9vpn4VSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMgcHQIge%2B9CNp1AoCKtwDx3H6qC1AEpoMNoFjuTmQsTA9k9zzrejUUpam9a9aE5hrayZThzPxNhltkfBA5Qdb6jr8Aoc%2BoVKo3iNRHBoIC%2FQ2OCHfWApt%2F6xGDNi2JDsIQdA4i2rLXCvYGl7qJJ0B2yiV2kLoZ79lQOZzmzmUulkxuREpLBZzxHWZBfk5QztLCBypRlWsN9Sc9JCpsvYm80c8rkKf%2BYWWKSMF9sECdPzXdk0z%2FqOqyoTAaYakeYNBrT86vtH0O3%2FDAzfWTQEEcArZaeOWwv%2BJX6lZCEY8sSxju80smM9MXOIWYz4dtPvxOBrXJc5bTOfJ9HO5JftIheOHxTv%2Bc8u2cXKEiNRM74cNx3Q3RFLmIVQySxosAd1AlvrAjiQzKKvHP1sFMAWsgURf0mDD7J%2FhNU8rysXF1%2FQ%2F3rQij6ZmPVzj8cqH%2FkQaECjfHR22sbRTd0%2F9txczVjJEP%2BYGFgQOTzqkZz6cE1gKfgd9bH%2BtmgP%2Fp0mt8jL6rhWSq0OKMgO0YBdUKy04PGK60%2FMmc37V9wA3r54R9SY2sedmKUc9tInsXSSaSroMVp89tXJjcpNItVnMNq6MUZFboADuf9YCSf9i%2FtCtC3YNNU55vCYZOX6XGn0tAqPxO7fJHo0EXFCKossw3InayAY6pgGITwfVl7t9P8RRqmQaOZIDXTFpleKn%2FMfrwTfNNp3touH9taHIvtvWNtZdU5o%2FrBdWQ3PZsG%2FVHpcev%2Fuikqz2ULULHIXkrPG65mJ9sPns8jZ5opNCl1WuRidBlQW1OMzqKLmNC6sXqDcZpndk2%2B0xGKKjD8CxR82Lbx269IgDEzN6SAWCGLmm7A5smIMg0Vv6rR32zQFuhnGNO4W0P%2FuE8tADn0e%2F&X-Amz-Signature=e069d0ab986015d5f37a43acb93ac313a204b442988cedce20dbdfc68aa64e3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6NMA3UR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdjpGnj1Q5LhZo8jniP6Oy8rKwAV1WlfdS4X8wLL5C2AiAMyuuRJbnOM9%2BKlL2PtGyOxNts0TnTag35mLv9vpn4VSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMgcHQIge%2B9CNp1AoCKtwDx3H6qC1AEpoMNoFjuTmQsTA9k9zzrejUUpam9a9aE5hrayZThzPxNhltkfBA5Qdb6jr8Aoc%2BoVKo3iNRHBoIC%2FQ2OCHfWApt%2F6xGDNi2JDsIQdA4i2rLXCvYGl7qJJ0B2yiV2kLoZ79lQOZzmzmUulkxuREpLBZzxHWZBfk5QztLCBypRlWsN9Sc9JCpsvYm80c8rkKf%2BYWWKSMF9sECdPzXdk0z%2FqOqyoTAaYakeYNBrT86vtH0O3%2FDAzfWTQEEcArZaeOWwv%2BJX6lZCEY8sSxju80smM9MXOIWYz4dtPvxOBrXJc5bTOfJ9HO5JftIheOHxTv%2Bc8u2cXKEiNRM74cNx3Q3RFLmIVQySxosAd1AlvrAjiQzKKvHP1sFMAWsgURf0mDD7J%2FhNU8rysXF1%2FQ%2F3rQij6ZmPVzj8cqH%2FkQaECjfHR22sbRTd0%2F9txczVjJEP%2BYGFgQOTzqkZz6cE1gKfgd9bH%2BtmgP%2Fp0mt8jL6rhWSq0OKMgO0YBdUKy04PGK60%2FMmc37V9wA3r54R9SY2sedmKUc9tInsXSSaSroMVp89tXJjcpNItVnMNq6MUZFboADuf9YCSf9i%2FtCtC3YNNU55vCYZOX6XGn0tAqPxO7fJHo0EXFCKossw3InayAY6pgGITwfVl7t9P8RRqmQaOZIDXTFpleKn%2FMfrwTfNNp3touH9taHIvtvWNtZdU5o%2FrBdWQ3PZsG%2FVHpcev%2Fuikqz2ULULHIXkrPG65mJ9sPns8jZ5opNCl1WuRidBlQW1OMzqKLmNC6sXqDcZpndk2%2B0xGKKjD8CxR82Lbx269IgDEzN6SAWCGLmm7A5smIMg0Vv6rR32zQFuhnGNO4W0P%2FuE8tADn0e%2F&X-Amz-Signature=a1c4f197bd280de83f419a366f29cada23b56608803b702fd8e333c7c6492422&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6NMA3UR%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdjpGnj1Q5LhZo8jniP6Oy8rKwAV1WlfdS4X8wLL5C2AiAMyuuRJbnOM9%2BKlL2PtGyOxNts0TnTag35mLv9vpn4VSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMgcHQIge%2B9CNp1AoCKtwDx3H6qC1AEpoMNoFjuTmQsTA9k9zzrejUUpam9a9aE5hrayZThzPxNhltkfBA5Qdb6jr8Aoc%2BoVKo3iNRHBoIC%2FQ2OCHfWApt%2F6xGDNi2JDsIQdA4i2rLXCvYGl7qJJ0B2yiV2kLoZ79lQOZzmzmUulkxuREpLBZzxHWZBfk5QztLCBypRlWsN9Sc9JCpsvYm80c8rkKf%2BYWWKSMF9sECdPzXdk0z%2FqOqyoTAaYakeYNBrT86vtH0O3%2FDAzfWTQEEcArZaeOWwv%2BJX6lZCEY8sSxju80smM9MXOIWYz4dtPvxOBrXJc5bTOfJ9HO5JftIheOHxTv%2Bc8u2cXKEiNRM74cNx3Q3RFLmIVQySxosAd1AlvrAjiQzKKvHP1sFMAWsgURf0mDD7J%2FhNU8rysXF1%2FQ%2F3rQij6ZmPVzj8cqH%2FkQaECjfHR22sbRTd0%2F9txczVjJEP%2BYGFgQOTzqkZz6cE1gKfgd9bH%2BtmgP%2Fp0mt8jL6rhWSq0OKMgO0YBdUKy04PGK60%2FMmc37V9wA3r54R9SY2sedmKUc9tInsXSSaSroMVp89tXJjcpNItVnMNq6MUZFboADuf9YCSf9i%2FtCtC3YNNU55vCYZOX6XGn0tAqPxO7fJHo0EXFCKossw3InayAY6pgGITwfVl7t9P8RRqmQaOZIDXTFpleKn%2FMfrwTfNNp3touH9taHIvtvWNtZdU5o%2FrBdWQ3PZsG%2FVHpcev%2Fuikqz2ULULHIXkrPG65mJ9sPns8jZ5opNCl1WuRidBlQW1OMzqKLmNC6sXqDcZpndk2%2B0xGKKjD8CxR82Lbx269IgDEzN6SAWCGLmm7A5smIMg0Vv6rR32zQFuhnGNO4W0P%2FuE8tADn0e%2F&X-Amz-Signature=23af9d0512c83ff315c7b12896d75059d62de8bb233f6dc8c50d5b447f64b031&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

