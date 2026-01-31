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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBH46563%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqLyqu19svp6SiJpw0cdDEyMwDAcc1imp%2BrYODGsM4wAIhANDBpTHIKKwLtleDqt80e1MU4ftp6hel6yTvTzHy1n8AKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuGC49jkxKdgW3iwMq3ANdL9vR15MlTay24D%2FoWUOukZFQKI%2BJy%2BtEXcN%2FR5q8%2FAaj8aaUVGATMaQAWGamvefoK8NLpPISW0nFaP3%2F1Epm2Sry84uFWVD2pUHxojdeE%2BvMX7U0yS%2BVS4n3od8QeSHtCOX%2BqV%2BT46996s0CyHxbGd%2BesGoUKtw9PNeGuz24r0EluKzGnLKEVeuP4%2Fz9OM5eaaU1L1DFSH1ya62v8oUuzWDojCiXmNNx2pqguSYiMK36f5wnrcM%2F%2F%2F9hZZ9BTlEIY776N9AMr8pKSbFHioIiODtCtnh6ZqepWvsitRTZrm3YSXSaXdL4mHOKuIKiEoqWrNsM8AcqamCO9yoNAW6%2FWp7GQ9B48GhpNXY2rDbePhRMyaGhW19bcvxN2NdVnmwNq%2FrILo7THzKVEsIZPuwrwl%2Bs%2B8MApx0zdcgkjc4LNm6pXqRLLW1rdGZMgWjOurnqeogAQjqlk1WxOcn8kUz1I9r6E8gGg5BDUMJmBYR4ACwMQ%2BcLJvtDqK2R8%2B1jh8ewko8RZZd6G7lCpeHa6KzId5YcpwZC%2FtNlzetpdPgDmpjEyFdcF1OSuubIY9dd%2BFdrtYpORFYZCA4E9DzCO%2BRAgfMKUObuRSP7BpOigH%2BVA1a7jMvANHINh6RVtjDZzPXLBjqkATyufZYMu7ESypUBi%2FF%2BIXYYtVUXPcPaxR4pCAojIliiR7LAyIJjmLJ4patTHVDaTt5IdefA0RCKoga6dU4mx2jUX6O2gIyjCmcRErEvaOHJYWvjpPIxh9bPIfQRcCNejgIBWKN%2BSuIaLz48aito32%2Fx1QKNJZEUPCm13zwH3I1e7amhhkKiu7flFgYTK%2FHcOjBc6XmrL2ohbinu4tRtcX6ELAzw&X-Amz-Signature=147c4007a019cf1c5b86a7492224464cae97731e875414b6cb9edea6bc37cd73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBH46563%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqLyqu19svp6SiJpw0cdDEyMwDAcc1imp%2BrYODGsM4wAIhANDBpTHIKKwLtleDqt80e1MU4ftp6hel6yTvTzHy1n8AKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuGC49jkxKdgW3iwMq3ANdL9vR15MlTay24D%2FoWUOukZFQKI%2BJy%2BtEXcN%2FR5q8%2FAaj8aaUVGATMaQAWGamvefoK8NLpPISW0nFaP3%2F1Epm2Sry84uFWVD2pUHxojdeE%2BvMX7U0yS%2BVS4n3od8QeSHtCOX%2BqV%2BT46996s0CyHxbGd%2BesGoUKtw9PNeGuz24r0EluKzGnLKEVeuP4%2Fz9OM5eaaU1L1DFSH1ya62v8oUuzWDojCiXmNNx2pqguSYiMK36f5wnrcM%2F%2F%2F9hZZ9BTlEIY776N9AMr8pKSbFHioIiODtCtnh6ZqepWvsitRTZrm3YSXSaXdL4mHOKuIKiEoqWrNsM8AcqamCO9yoNAW6%2FWp7GQ9B48GhpNXY2rDbePhRMyaGhW19bcvxN2NdVnmwNq%2FrILo7THzKVEsIZPuwrwl%2Bs%2B8MApx0zdcgkjc4LNm6pXqRLLW1rdGZMgWjOurnqeogAQjqlk1WxOcn8kUz1I9r6E8gGg5BDUMJmBYR4ACwMQ%2BcLJvtDqK2R8%2B1jh8ewko8RZZd6G7lCpeHa6KzId5YcpwZC%2FtNlzetpdPgDmpjEyFdcF1OSuubIY9dd%2BFdrtYpORFYZCA4E9DzCO%2BRAgfMKUObuRSP7BpOigH%2BVA1a7jMvANHINh6RVtjDZzPXLBjqkATyufZYMu7ESypUBi%2FF%2BIXYYtVUXPcPaxR4pCAojIliiR7LAyIJjmLJ4patTHVDaTt5IdefA0RCKoga6dU4mx2jUX6O2gIyjCmcRErEvaOHJYWvjpPIxh9bPIfQRcCNejgIBWKN%2BSuIaLz48aito32%2Fx1QKNJZEUPCm13zwH3I1e7amhhkKiu7flFgYTK%2FHcOjBc6XmrL2ohbinu4tRtcX6ELAzw&X-Amz-Signature=aa43a19b786a905911c25ad6abdb354d690945e4b8de1552263273f927bc7d45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBH46563%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqLyqu19svp6SiJpw0cdDEyMwDAcc1imp%2BrYODGsM4wAIhANDBpTHIKKwLtleDqt80e1MU4ftp6hel6yTvTzHy1n8AKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuGC49jkxKdgW3iwMq3ANdL9vR15MlTay24D%2FoWUOukZFQKI%2BJy%2BtEXcN%2FR5q8%2FAaj8aaUVGATMaQAWGamvefoK8NLpPISW0nFaP3%2F1Epm2Sry84uFWVD2pUHxojdeE%2BvMX7U0yS%2BVS4n3od8QeSHtCOX%2BqV%2BT46996s0CyHxbGd%2BesGoUKtw9PNeGuz24r0EluKzGnLKEVeuP4%2Fz9OM5eaaU1L1DFSH1ya62v8oUuzWDojCiXmNNx2pqguSYiMK36f5wnrcM%2F%2F%2F9hZZ9BTlEIY776N9AMr8pKSbFHioIiODtCtnh6ZqepWvsitRTZrm3YSXSaXdL4mHOKuIKiEoqWrNsM8AcqamCO9yoNAW6%2FWp7GQ9B48GhpNXY2rDbePhRMyaGhW19bcvxN2NdVnmwNq%2FrILo7THzKVEsIZPuwrwl%2Bs%2B8MApx0zdcgkjc4LNm6pXqRLLW1rdGZMgWjOurnqeogAQjqlk1WxOcn8kUz1I9r6E8gGg5BDUMJmBYR4ACwMQ%2BcLJvtDqK2R8%2B1jh8ewko8RZZd6G7lCpeHa6KzId5YcpwZC%2FtNlzetpdPgDmpjEyFdcF1OSuubIY9dd%2BFdrtYpORFYZCA4E9DzCO%2BRAgfMKUObuRSP7BpOigH%2BVA1a7jMvANHINh6RVtjDZzPXLBjqkATyufZYMu7ESypUBi%2FF%2BIXYYtVUXPcPaxR4pCAojIliiR7LAyIJjmLJ4patTHVDaTt5IdefA0RCKoga6dU4mx2jUX6O2gIyjCmcRErEvaOHJYWvjpPIxh9bPIfQRcCNejgIBWKN%2BSuIaLz48aito32%2Fx1QKNJZEUPCm13zwH3I1e7amhhkKiu7flFgYTK%2FHcOjBc6XmrL2ohbinu4tRtcX6ELAzw&X-Amz-Signature=ddf5f0487a9980f26d59e9e48e328410a965299dfbdc3cb812f7c595084b6901&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBH46563%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqLyqu19svp6SiJpw0cdDEyMwDAcc1imp%2BrYODGsM4wAIhANDBpTHIKKwLtleDqt80e1MU4ftp6hel6yTvTzHy1n8AKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuGC49jkxKdgW3iwMq3ANdL9vR15MlTay24D%2FoWUOukZFQKI%2BJy%2BtEXcN%2FR5q8%2FAaj8aaUVGATMaQAWGamvefoK8NLpPISW0nFaP3%2F1Epm2Sry84uFWVD2pUHxojdeE%2BvMX7U0yS%2BVS4n3od8QeSHtCOX%2BqV%2BT46996s0CyHxbGd%2BesGoUKtw9PNeGuz24r0EluKzGnLKEVeuP4%2Fz9OM5eaaU1L1DFSH1ya62v8oUuzWDojCiXmNNx2pqguSYiMK36f5wnrcM%2F%2F%2F9hZZ9BTlEIY776N9AMr8pKSbFHioIiODtCtnh6ZqepWvsitRTZrm3YSXSaXdL4mHOKuIKiEoqWrNsM8AcqamCO9yoNAW6%2FWp7GQ9B48GhpNXY2rDbePhRMyaGhW19bcvxN2NdVnmwNq%2FrILo7THzKVEsIZPuwrwl%2Bs%2B8MApx0zdcgkjc4LNm6pXqRLLW1rdGZMgWjOurnqeogAQjqlk1WxOcn8kUz1I9r6E8gGg5BDUMJmBYR4ACwMQ%2BcLJvtDqK2R8%2B1jh8ewko8RZZd6G7lCpeHa6KzId5YcpwZC%2FtNlzetpdPgDmpjEyFdcF1OSuubIY9dd%2BFdrtYpORFYZCA4E9DzCO%2BRAgfMKUObuRSP7BpOigH%2BVA1a7jMvANHINh6RVtjDZzPXLBjqkATyufZYMu7ESypUBi%2FF%2BIXYYtVUXPcPaxR4pCAojIliiR7LAyIJjmLJ4patTHVDaTt5IdefA0RCKoga6dU4mx2jUX6O2gIyjCmcRErEvaOHJYWvjpPIxh9bPIfQRcCNejgIBWKN%2BSuIaLz48aito32%2Fx1QKNJZEUPCm13zwH3I1e7amhhkKiu7flFgYTK%2FHcOjBc6XmrL2ohbinu4tRtcX6ELAzw&X-Amz-Signature=82684b06dcc9c6a47cf22a1be71424d0fe8c0163bc1361ab83fa31f5c87ee859&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBH46563%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqLyqu19svp6SiJpw0cdDEyMwDAcc1imp%2BrYODGsM4wAIhANDBpTHIKKwLtleDqt80e1MU4ftp6hel6yTvTzHy1n8AKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuGC49jkxKdgW3iwMq3ANdL9vR15MlTay24D%2FoWUOukZFQKI%2BJy%2BtEXcN%2FR5q8%2FAaj8aaUVGATMaQAWGamvefoK8NLpPISW0nFaP3%2F1Epm2Sry84uFWVD2pUHxojdeE%2BvMX7U0yS%2BVS4n3od8QeSHtCOX%2BqV%2BT46996s0CyHxbGd%2BesGoUKtw9PNeGuz24r0EluKzGnLKEVeuP4%2Fz9OM5eaaU1L1DFSH1ya62v8oUuzWDojCiXmNNx2pqguSYiMK36f5wnrcM%2F%2F%2F9hZZ9BTlEIY776N9AMr8pKSbFHioIiODtCtnh6ZqepWvsitRTZrm3YSXSaXdL4mHOKuIKiEoqWrNsM8AcqamCO9yoNAW6%2FWp7GQ9B48GhpNXY2rDbePhRMyaGhW19bcvxN2NdVnmwNq%2FrILo7THzKVEsIZPuwrwl%2Bs%2B8MApx0zdcgkjc4LNm6pXqRLLW1rdGZMgWjOurnqeogAQjqlk1WxOcn8kUz1I9r6E8gGg5BDUMJmBYR4ACwMQ%2BcLJvtDqK2R8%2B1jh8ewko8RZZd6G7lCpeHa6KzId5YcpwZC%2FtNlzetpdPgDmpjEyFdcF1OSuubIY9dd%2BFdrtYpORFYZCA4E9DzCO%2BRAgfMKUObuRSP7BpOigH%2BVA1a7jMvANHINh6RVtjDZzPXLBjqkATyufZYMu7ESypUBi%2FF%2BIXYYtVUXPcPaxR4pCAojIliiR7LAyIJjmLJ4patTHVDaTt5IdefA0RCKoga6dU4mx2jUX6O2gIyjCmcRErEvaOHJYWvjpPIxh9bPIfQRcCNejgIBWKN%2BSuIaLz48aito32%2Fx1QKNJZEUPCm13zwH3I1e7amhhkKiu7flFgYTK%2FHcOjBc6XmrL2ohbinu4tRtcX6ELAzw&X-Amz-Signature=30d493142f9e581fea9a0448b80da7cfe86c9fad1fb7e5df127c3a08252bcdf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBH46563%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqLyqu19svp6SiJpw0cdDEyMwDAcc1imp%2BrYODGsM4wAIhANDBpTHIKKwLtleDqt80e1MU4ftp6hel6yTvTzHy1n8AKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuGC49jkxKdgW3iwMq3ANdL9vR15MlTay24D%2FoWUOukZFQKI%2BJy%2BtEXcN%2FR5q8%2FAaj8aaUVGATMaQAWGamvefoK8NLpPISW0nFaP3%2F1Epm2Sry84uFWVD2pUHxojdeE%2BvMX7U0yS%2BVS4n3od8QeSHtCOX%2BqV%2BT46996s0CyHxbGd%2BesGoUKtw9PNeGuz24r0EluKzGnLKEVeuP4%2Fz9OM5eaaU1L1DFSH1ya62v8oUuzWDojCiXmNNx2pqguSYiMK36f5wnrcM%2F%2F%2F9hZZ9BTlEIY776N9AMr8pKSbFHioIiODtCtnh6ZqepWvsitRTZrm3YSXSaXdL4mHOKuIKiEoqWrNsM8AcqamCO9yoNAW6%2FWp7GQ9B48GhpNXY2rDbePhRMyaGhW19bcvxN2NdVnmwNq%2FrILo7THzKVEsIZPuwrwl%2Bs%2B8MApx0zdcgkjc4LNm6pXqRLLW1rdGZMgWjOurnqeogAQjqlk1WxOcn8kUz1I9r6E8gGg5BDUMJmBYR4ACwMQ%2BcLJvtDqK2R8%2B1jh8ewko8RZZd6G7lCpeHa6KzId5YcpwZC%2FtNlzetpdPgDmpjEyFdcF1OSuubIY9dd%2BFdrtYpORFYZCA4E9DzCO%2BRAgfMKUObuRSP7BpOigH%2BVA1a7jMvANHINh6RVtjDZzPXLBjqkATyufZYMu7ESypUBi%2FF%2BIXYYtVUXPcPaxR4pCAojIliiR7LAyIJjmLJ4patTHVDaTt5IdefA0RCKoga6dU4mx2jUX6O2gIyjCmcRErEvaOHJYWvjpPIxh9bPIfQRcCNejgIBWKN%2BSuIaLz48aito32%2Fx1QKNJZEUPCm13zwH3I1e7amhhkKiu7flFgYTK%2FHcOjBc6XmrL2ohbinu4tRtcX6ELAzw&X-Amz-Signature=6ca1fe46a06ab2f34950d5a4418e776b324ab456708bd298dcfcabb7a5efc64d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBH46563%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqLyqu19svp6SiJpw0cdDEyMwDAcc1imp%2BrYODGsM4wAIhANDBpTHIKKwLtleDqt80e1MU4ftp6hel6yTvTzHy1n8AKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuGC49jkxKdgW3iwMq3ANdL9vR15MlTay24D%2FoWUOukZFQKI%2BJy%2BtEXcN%2FR5q8%2FAaj8aaUVGATMaQAWGamvefoK8NLpPISW0nFaP3%2F1Epm2Sry84uFWVD2pUHxojdeE%2BvMX7U0yS%2BVS4n3od8QeSHtCOX%2BqV%2BT46996s0CyHxbGd%2BesGoUKtw9PNeGuz24r0EluKzGnLKEVeuP4%2Fz9OM5eaaU1L1DFSH1ya62v8oUuzWDojCiXmNNx2pqguSYiMK36f5wnrcM%2F%2F%2F9hZZ9BTlEIY776N9AMr8pKSbFHioIiODtCtnh6ZqepWvsitRTZrm3YSXSaXdL4mHOKuIKiEoqWrNsM8AcqamCO9yoNAW6%2FWp7GQ9B48GhpNXY2rDbePhRMyaGhW19bcvxN2NdVnmwNq%2FrILo7THzKVEsIZPuwrwl%2Bs%2B8MApx0zdcgkjc4LNm6pXqRLLW1rdGZMgWjOurnqeogAQjqlk1WxOcn8kUz1I9r6E8gGg5BDUMJmBYR4ACwMQ%2BcLJvtDqK2R8%2B1jh8ewko8RZZd6G7lCpeHa6KzId5YcpwZC%2FtNlzetpdPgDmpjEyFdcF1OSuubIY9dd%2BFdrtYpORFYZCA4E9DzCO%2BRAgfMKUObuRSP7BpOigH%2BVA1a7jMvANHINh6RVtjDZzPXLBjqkATyufZYMu7ESypUBi%2FF%2BIXYYtVUXPcPaxR4pCAojIliiR7LAyIJjmLJ4patTHVDaTt5IdefA0RCKoga6dU4mx2jUX6O2gIyjCmcRErEvaOHJYWvjpPIxh9bPIfQRcCNejgIBWKN%2BSuIaLz48aito32%2Fx1QKNJZEUPCm13zwH3I1e7amhhkKiu7flFgYTK%2FHcOjBc6XmrL2ohbinu4tRtcX6ELAzw&X-Amz-Signature=d177210c8b6770629f8342077e278c9008dd784ef6b960cd7269d861d46a034e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBH46563%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqLyqu19svp6SiJpw0cdDEyMwDAcc1imp%2BrYODGsM4wAIhANDBpTHIKKwLtleDqt80e1MU4ftp6hel6yTvTzHy1n8AKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuGC49jkxKdgW3iwMq3ANdL9vR15MlTay24D%2FoWUOukZFQKI%2BJy%2BtEXcN%2FR5q8%2FAaj8aaUVGATMaQAWGamvefoK8NLpPISW0nFaP3%2F1Epm2Sry84uFWVD2pUHxojdeE%2BvMX7U0yS%2BVS4n3od8QeSHtCOX%2BqV%2BT46996s0CyHxbGd%2BesGoUKtw9PNeGuz24r0EluKzGnLKEVeuP4%2Fz9OM5eaaU1L1DFSH1ya62v8oUuzWDojCiXmNNx2pqguSYiMK36f5wnrcM%2F%2F%2F9hZZ9BTlEIY776N9AMr8pKSbFHioIiODtCtnh6ZqepWvsitRTZrm3YSXSaXdL4mHOKuIKiEoqWrNsM8AcqamCO9yoNAW6%2FWp7GQ9B48GhpNXY2rDbePhRMyaGhW19bcvxN2NdVnmwNq%2FrILo7THzKVEsIZPuwrwl%2Bs%2B8MApx0zdcgkjc4LNm6pXqRLLW1rdGZMgWjOurnqeogAQjqlk1WxOcn8kUz1I9r6E8gGg5BDUMJmBYR4ACwMQ%2BcLJvtDqK2R8%2B1jh8ewko8RZZd6G7lCpeHa6KzId5YcpwZC%2FtNlzetpdPgDmpjEyFdcF1OSuubIY9dd%2BFdrtYpORFYZCA4E9DzCO%2BRAgfMKUObuRSP7BpOigH%2BVA1a7jMvANHINh6RVtjDZzPXLBjqkATyufZYMu7ESypUBi%2FF%2BIXYYtVUXPcPaxR4pCAojIliiR7LAyIJjmLJ4patTHVDaTt5IdefA0RCKoga6dU4mx2jUX6O2gIyjCmcRErEvaOHJYWvjpPIxh9bPIfQRcCNejgIBWKN%2BSuIaLz48aito32%2Fx1QKNJZEUPCm13zwH3I1e7amhhkKiu7flFgYTK%2FHcOjBc6XmrL2ohbinu4tRtcX6ELAzw&X-Amz-Signature=ebf967f9b5fe26a4e79f5b4e1a1b38c99f7d03768496c76edd488a8a64d842b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBH46563%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqLyqu19svp6SiJpw0cdDEyMwDAcc1imp%2BrYODGsM4wAIhANDBpTHIKKwLtleDqt80e1MU4ftp6hel6yTvTzHy1n8AKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuGC49jkxKdgW3iwMq3ANdL9vR15MlTay24D%2FoWUOukZFQKI%2BJy%2BtEXcN%2FR5q8%2FAaj8aaUVGATMaQAWGamvefoK8NLpPISW0nFaP3%2F1Epm2Sry84uFWVD2pUHxojdeE%2BvMX7U0yS%2BVS4n3od8QeSHtCOX%2BqV%2BT46996s0CyHxbGd%2BesGoUKtw9PNeGuz24r0EluKzGnLKEVeuP4%2Fz9OM5eaaU1L1DFSH1ya62v8oUuzWDojCiXmNNx2pqguSYiMK36f5wnrcM%2F%2F%2F9hZZ9BTlEIY776N9AMr8pKSbFHioIiODtCtnh6ZqepWvsitRTZrm3YSXSaXdL4mHOKuIKiEoqWrNsM8AcqamCO9yoNAW6%2FWp7GQ9B48GhpNXY2rDbePhRMyaGhW19bcvxN2NdVnmwNq%2FrILo7THzKVEsIZPuwrwl%2Bs%2B8MApx0zdcgkjc4LNm6pXqRLLW1rdGZMgWjOurnqeogAQjqlk1WxOcn8kUz1I9r6E8gGg5BDUMJmBYR4ACwMQ%2BcLJvtDqK2R8%2B1jh8ewko8RZZd6G7lCpeHa6KzId5YcpwZC%2FtNlzetpdPgDmpjEyFdcF1OSuubIY9dd%2BFdrtYpORFYZCA4E9DzCO%2BRAgfMKUObuRSP7BpOigH%2BVA1a7jMvANHINh6RVtjDZzPXLBjqkATyufZYMu7ESypUBi%2FF%2BIXYYtVUXPcPaxR4pCAojIliiR7LAyIJjmLJ4patTHVDaTt5IdefA0RCKoga6dU4mx2jUX6O2gIyjCmcRErEvaOHJYWvjpPIxh9bPIfQRcCNejgIBWKN%2BSuIaLz48aito32%2Fx1QKNJZEUPCm13zwH3I1e7amhhkKiu7flFgYTK%2FHcOjBc6XmrL2ohbinu4tRtcX6ELAzw&X-Amz-Signature=c572d548794fd5deac9eed538bc083d9cefc3d0f9d409b5ba00d92985bf85476&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBH46563%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqLyqu19svp6SiJpw0cdDEyMwDAcc1imp%2BrYODGsM4wAIhANDBpTHIKKwLtleDqt80e1MU4ftp6hel6yTvTzHy1n8AKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuGC49jkxKdgW3iwMq3ANdL9vR15MlTay24D%2FoWUOukZFQKI%2BJy%2BtEXcN%2FR5q8%2FAaj8aaUVGATMaQAWGamvefoK8NLpPISW0nFaP3%2F1Epm2Sry84uFWVD2pUHxojdeE%2BvMX7U0yS%2BVS4n3od8QeSHtCOX%2BqV%2BT46996s0CyHxbGd%2BesGoUKtw9PNeGuz24r0EluKzGnLKEVeuP4%2Fz9OM5eaaU1L1DFSH1ya62v8oUuzWDojCiXmNNx2pqguSYiMK36f5wnrcM%2F%2F%2F9hZZ9BTlEIY776N9AMr8pKSbFHioIiODtCtnh6ZqepWvsitRTZrm3YSXSaXdL4mHOKuIKiEoqWrNsM8AcqamCO9yoNAW6%2FWp7GQ9B48GhpNXY2rDbePhRMyaGhW19bcvxN2NdVnmwNq%2FrILo7THzKVEsIZPuwrwl%2Bs%2B8MApx0zdcgkjc4LNm6pXqRLLW1rdGZMgWjOurnqeogAQjqlk1WxOcn8kUz1I9r6E8gGg5BDUMJmBYR4ACwMQ%2BcLJvtDqK2R8%2B1jh8ewko8RZZd6G7lCpeHa6KzId5YcpwZC%2FtNlzetpdPgDmpjEyFdcF1OSuubIY9dd%2BFdrtYpORFYZCA4E9DzCO%2BRAgfMKUObuRSP7BpOigH%2BVA1a7jMvANHINh6RVtjDZzPXLBjqkATyufZYMu7ESypUBi%2FF%2BIXYYtVUXPcPaxR4pCAojIliiR7LAyIJjmLJ4patTHVDaTt5IdefA0RCKoga6dU4mx2jUX6O2gIyjCmcRErEvaOHJYWvjpPIxh9bPIfQRcCNejgIBWKN%2BSuIaLz48aito32%2Fx1QKNJZEUPCm13zwH3I1e7amhhkKiu7flFgYTK%2FHcOjBc6XmrL2ohbinu4tRtcX6ELAzw&X-Amz-Signature=4e6ac060ef4b730239d3bfc3c69db577f5660e1b49cac5e1edcb2bdf88e25847&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

