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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4BXUQH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDM5QuQ%2F8sUpo29J9LNXfkjlGKTROrFQr%2FVrOBAOief5QIgKnMJPMvZPDSUuGeG3N1g48VuVsd2Kt4vxLNrXKG40mkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7QQupSPihmBFSc0CrcA5ABhDCCb6ZbgZ6qT%2FDd%2F8EkNay6trwTyEfXfH6DGUT1xnDjeb0aE18Qhs8hQLZi0IQwtHUHxtlkxL%2FKOU7ASxy%2BuBfhsWlEOMQwU6nxwitJ8OvcKR3jdB%2BgHBQP22Erc%2F4xFSdatRIOAgZprz7rHQCbScvixyYkUwOMH1hkxO3v4PmTUpi%2BMvBfCG9ln%2FsuLS9fgMYTdBpNfYbJ7X26034aEevJ27NcEWNYSZhvf%2FNrRetiU1XgiBrhMQvPOxm%2BPIk7DQ0WzxE8BCHe3ecv3Jlgvp47OOONfANerpujpphWqMVbpSUYVhRxMy05p3cG5Rjc2uTXZGGo%2Bz2fHlGlbw1FpMul9ZftO3o1nyEr%2F2zwCscCfoYBjEhtddLut7Jm9PWe6KG3sh%2BRuT6iAJ79CvoD%2FVpSttwJXoz6TMoKAM6fyx8xeajok2s4xEw5M0PJnsHX0W8nn72VnaAU3cR6iP8ki68Hhnc%2BOweMnmfgbTNNs2xaENdngO%2BMJipFzfIXX5CM5E%2FBBDa0ONEZR%2B5FwJO%2BRU0hqZ4wGzfSbrFYTPqVTLUYJ42hFrqM6k%2B6h2b806K9Bt%2BLXYwpXXG2ASH%2BdQRjev4FdOwdQnQ1jFT0j4dgTw7v9GrZHBL5nvw0MP%2B%2B3c0GOqUBE7WWjMzBWp7fTaFcSbbg%2BeRgUTyCM22L8QQ2xu3H8cXC78UUfyDFGn%2BLt%2FE16lM5Zsp9P0XZJ7EDFTw5wPo1KybZVWBTupHEdF7ZEHxa98vGtlCTHRZARozjrGOEHKYz9zmRxGyj6ZmZbRk%2BS0gy%2F%2FzIjdQapR3H%2BfxZ7d1Js5Ru6SWX977zt4tsEijyyrrMNy6veJ05f5IOTVkx3KyFGuNz2ExK&X-Amz-Signature=d334ca3659b175a1748490e8d30bfceac7fe083c39b362a2fd4d97da5cb4ebaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4BXUQH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDM5QuQ%2F8sUpo29J9LNXfkjlGKTROrFQr%2FVrOBAOief5QIgKnMJPMvZPDSUuGeG3N1g48VuVsd2Kt4vxLNrXKG40mkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7QQupSPihmBFSc0CrcA5ABhDCCb6ZbgZ6qT%2FDd%2F8EkNay6trwTyEfXfH6DGUT1xnDjeb0aE18Qhs8hQLZi0IQwtHUHxtlkxL%2FKOU7ASxy%2BuBfhsWlEOMQwU6nxwitJ8OvcKR3jdB%2BgHBQP22Erc%2F4xFSdatRIOAgZprz7rHQCbScvixyYkUwOMH1hkxO3v4PmTUpi%2BMvBfCG9ln%2FsuLS9fgMYTdBpNfYbJ7X26034aEevJ27NcEWNYSZhvf%2FNrRetiU1XgiBrhMQvPOxm%2BPIk7DQ0WzxE8BCHe3ecv3Jlgvp47OOONfANerpujpphWqMVbpSUYVhRxMy05p3cG5Rjc2uTXZGGo%2Bz2fHlGlbw1FpMul9ZftO3o1nyEr%2F2zwCscCfoYBjEhtddLut7Jm9PWe6KG3sh%2BRuT6iAJ79CvoD%2FVpSttwJXoz6TMoKAM6fyx8xeajok2s4xEw5M0PJnsHX0W8nn72VnaAU3cR6iP8ki68Hhnc%2BOweMnmfgbTNNs2xaENdngO%2BMJipFzfIXX5CM5E%2FBBDa0ONEZR%2B5FwJO%2BRU0hqZ4wGzfSbrFYTPqVTLUYJ42hFrqM6k%2B6h2b806K9Bt%2BLXYwpXXG2ASH%2BdQRjev4FdOwdQnQ1jFT0j4dgTw7v9GrZHBL5nvw0MP%2B%2B3c0GOqUBE7WWjMzBWp7fTaFcSbbg%2BeRgUTyCM22L8QQ2xu3H8cXC78UUfyDFGn%2BLt%2FE16lM5Zsp9P0XZJ7EDFTw5wPo1KybZVWBTupHEdF7ZEHxa98vGtlCTHRZARozjrGOEHKYz9zmRxGyj6ZmZbRk%2BS0gy%2F%2FzIjdQapR3H%2BfxZ7d1Js5Ru6SWX977zt4tsEijyyrrMNy6veJ05f5IOTVkx3KyFGuNz2ExK&X-Amz-Signature=1dafe59758ef7e3616df886f9b142b81276d272466c28a0a06e3bb2e815ebbce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4BXUQH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDM5QuQ%2F8sUpo29J9LNXfkjlGKTROrFQr%2FVrOBAOief5QIgKnMJPMvZPDSUuGeG3N1g48VuVsd2Kt4vxLNrXKG40mkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7QQupSPihmBFSc0CrcA5ABhDCCb6ZbgZ6qT%2FDd%2F8EkNay6trwTyEfXfH6DGUT1xnDjeb0aE18Qhs8hQLZi0IQwtHUHxtlkxL%2FKOU7ASxy%2BuBfhsWlEOMQwU6nxwitJ8OvcKR3jdB%2BgHBQP22Erc%2F4xFSdatRIOAgZprz7rHQCbScvixyYkUwOMH1hkxO3v4PmTUpi%2BMvBfCG9ln%2FsuLS9fgMYTdBpNfYbJ7X26034aEevJ27NcEWNYSZhvf%2FNrRetiU1XgiBrhMQvPOxm%2BPIk7DQ0WzxE8BCHe3ecv3Jlgvp47OOONfANerpujpphWqMVbpSUYVhRxMy05p3cG5Rjc2uTXZGGo%2Bz2fHlGlbw1FpMul9ZftO3o1nyEr%2F2zwCscCfoYBjEhtddLut7Jm9PWe6KG3sh%2BRuT6iAJ79CvoD%2FVpSttwJXoz6TMoKAM6fyx8xeajok2s4xEw5M0PJnsHX0W8nn72VnaAU3cR6iP8ki68Hhnc%2BOweMnmfgbTNNs2xaENdngO%2BMJipFzfIXX5CM5E%2FBBDa0ONEZR%2B5FwJO%2BRU0hqZ4wGzfSbrFYTPqVTLUYJ42hFrqM6k%2B6h2b806K9Bt%2BLXYwpXXG2ASH%2BdQRjev4FdOwdQnQ1jFT0j4dgTw7v9GrZHBL5nvw0MP%2B%2B3c0GOqUBE7WWjMzBWp7fTaFcSbbg%2BeRgUTyCM22L8QQ2xu3H8cXC78UUfyDFGn%2BLt%2FE16lM5Zsp9P0XZJ7EDFTw5wPo1KybZVWBTupHEdF7ZEHxa98vGtlCTHRZARozjrGOEHKYz9zmRxGyj6ZmZbRk%2BS0gy%2F%2FzIjdQapR3H%2BfxZ7d1Js5Ru6SWX977zt4tsEijyyrrMNy6veJ05f5IOTVkx3KyFGuNz2ExK&X-Amz-Signature=224e5801527f686b8562d8049251f972b2863b642fe28b1120e377049052e95e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4BXUQH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDM5QuQ%2F8sUpo29J9LNXfkjlGKTROrFQr%2FVrOBAOief5QIgKnMJPMvZPDSUuGeG3N1g48VuVsd2Kt4vxLNrXKG40mkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7QQupSPihmBFSc0CrcA5ABhDCCb6ZbgZ6qT%2FDd%2F8EkNay6trwTyEfXfH6DGUT1xnDjeb0aE18Qhs8hQLZi0IQwtHUHxtlkxL%2FKOU7ASxy%2BuBfhsWlEOMQwU6nxwitJ8OvcKR3jdB%2BgHBQP22Erc%2F4xFSdatRIOAgZprz7rHQCbScvixyYkUwOMH1hkxO3v4PmTUpi%2BMvBfCG9ln%2FsuLS9fgMYTdBpNfYbJ7X26034aEevJ27NcEWNYSZhvf%2FNrRetiU1XgiBrhMQvPOxm%2BPIk7DQ0WzxE8BCHe3ecv3Jlgvp47OOONfANerpujpphWqMVbpSUYVhRxMy05p3cG5Rjc2uTXZGGo%2Bz2fHlGlbw1FpMul9ZftO3o1nyEr%2F2zwCscCfoYBjEhtddLut7Jm9PWe6KG3sh%2BRuT6iAJ79CvoD%2FVpSttwJXoz6TMoKAM6fyx8xeajok2s4xEw5M0PJnsHX0W8nn72VnaAU3cR6iP8ki68Hhnc%2BOweMnmfgbTNNs2xaENdngO%2BMJipFzfIXX5CM5E%2FBBDa0ONEZR%2B5FwJO%2BRU0hqZ4wGzfSbrFYTPqVTLUYJ42hFrqM6k%2B6h2b806K9Bt%2BLXYwpXXG2ASH%2BdQRjev4FdOwdQnQ1jFT0j4dgTw7v9GrZHBL5nvw0MP%2B%2B3c0GOqUBE7WWjMzBWp7fTaFcSbbg%2BeRgUTyCM22L8QQ2xu3H8cXC78UUfyDFGn%2BLt%2FE16lM5Zsp9P0XZJ7EDFTw5wPo1KybZVWBTupHEdF7ZEHxa98vGtlCTHRZARozjrGOEHKYz9zmRxGyj6ZmZbRk%2BS0gy%2F%2FzIjdQapR3H%2BfxZ7d1Js5Ru6SWX977zt4tsEijyyrrMNy6veJ05f5IOTVkx3KyFGuNz2ExK&X-Amz-Signature=ab46fd35be61c1111c37fcc3d1ba65c4369d8ee97f3281638cf72175e1a192cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4BXUQH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDM5QuQ%2F8sUpo29J9LNXfkjlGKTROrFQr%2FVrOBAOief5QIgKnMJPMvZPDSUuGeG3N1g48VuVsd2Kt4vxLNrXKG40mkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7QQupSPihmBFSc0CrcA5ABhDCCb6ZbgZ6qT%2FDd%2F8EkNay6trwTyEfXfH6DGUT1xnDjeb0aE18Qhs8hQLZi0IQwtHUHxtlkxL%2FKOU7ASxy%2BuBfhsWlEOMQwU6nxwitJ8OvcKR3jdB%2BgHBQP22Erc%2F4xFSdatRIOAgZprz7rHQCbScvixyYkUwOMH1hkxO3v4PmTUpi%2BMvBfCG9ln%2FsuLS9fgMYTdBpNfYbJ7X26034aEevJ27NcEWNYSZhvf%2FNrRetiU1XgiBrhMQvPOxm%2BPIk7DQ0WzxE8BCHe3ecv3Jlgvp47OOONfANerpujpphWqMVbpSUYVhRxMy05p3cG5Rjc2uTXZGGo%2Bz2fHlGlbw1FpMul9ZftO3o1nyEr%2F2zwCscCfoYBjEhtddLut7Jm9PWe6KG3sh%2BRuT6iAJ79CvoD%2FVpSttwJXoz6TMoKAM6fyx8xeajok2s4xEw5M0PJnsHX0W8nn72VnaAU3cR6iP8ki68Hhnc%2BOweMnmfgbTNNs2xaENdngO%2BMJipFzfIXX5CM5E%2FBBDa0ONEZR%2B5FwJO%2BRU0hqZ4wGzfSbrFYTPqVTLUYJ42hFrqM6k%2B6h2b806K9Bt%2BLXYwpXXG2ASH%2BdQRjev4FdOwdQnQ1jFT0j4dgTw7v9GrZHBL5nvw0MP%2B%2B3c0GOqUBE7WWjMzBWp7fTaFcSbbg%2BeRgUTyCM22L8QQ2xu3H8cXC78UUfyDFGn%2BLt%2FE16lM5Zsp9P0XZJ7EDFTw5wPo1KybZVWBTupHEdF7ZEHxa98vGtlCTHRZARozjrGOEHKYz9zmRxGyj6ZmZbRk%2BS0gy%2F%2FzIjdQapR3H%2BfxZ7d1Js5Ru6SWX977zt4tsEijyyrrMNy6veJ05f5IOTVkx3KyFGuNz2ExK&X-Amz-Signature=34fe032db710393f2cc4bafdc0945be52ae2bb2c68dcc836865b4528c6630636&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4BXUQH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDM5QuQ%2F8sUpo29J9LNXfkjlGKTROrFQr%2FVrOBAOief5QIgKnMJPMvZPDSUuGeG3N1g48VuVsd2Kt4vxLNrXKG40mkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7QQupSPihmBFSc0CrcA5ABhDCCb6ZbgZ6qT%2FDd%2F8EkNay6trwTyEfXfH6DGUT1xnDjeb0aE18Qhs8hQLZi0IQwtHUHxtlkxL%2FKOU7ASxy%2BuBfhsWlEOMQwU6nxwitJ8OvcKR3jdB%2BgHBQP22Erc%2F4xFSdatRIOAgZprz7rHQCbScvixyYkUwOMH1hkxO3v4PmTUpi%2BMvBfCG9ln%2FsuLS9fgMYTdBpNfYbJ7X26034aEevJ27NcEWNYSZhvf%2FNrRetiU1XgiBrhMQvPOxm%2BPIk7DQ0WzxE8BCHe3ecv3Jlgvp47OOONfANerpujpphWqMVbpSUYVhRxMy05p3cG5Rjc2uTXZGGo%2Bz2fHlGlbw1FpMul9ZftO3o1nyEr%2F2zwCscCfoYBjEhtddLut7Jm9PWe6KG3sh%2BRuT6iAJ79CvoD%2FVpSttwJXoz6TMoKAM6fyx8xeajok2s4xEw5M0PJnsHX0W8nn72VnaAU3cR6iP8ki68Hhnc%2BOweMnmfgbTNNs2xaENdngO%2BMJipFzfIXX5CM5E%2FBBDa0ONEZR%2B5FwJO%2BRU0hqZ4wGzfSbrFYTPqVTLUYJ42hFrqM6k%2B6h2b806K9Bt%2BLXYwpXXG2ASH%2BdQRjev4FdOwdQnQ1jFT0j4dgTw7v9GrZHBL5nvw0MP%2B%2B3c0GOqUBE7WWjMzBWp7fTaFcSbbg%2BeRgUTyCM22L8QQ2xu3H8cXC78UUfyDFGn%2BLt%2FE16lM5Zsp9P0XZJ7EDFTw5wPo1KybZVWBTupHEdF7ZEHxa98vGtlCTHRZARozjrGOEHKYz9zmRxGyj6ZmZbRk%2BS0gy%2F%2FzIjdQapR3H%2BfxZ7d1Js5Ru6SWX977zt4tsEijyyrrMNy6veJ05f5IOTVkx3KyFGuNz2ExK&X-Amz-Signature=e4a26a5fa3d895e24b7c2f78d88e756b100b9fe1ea7edd494d00bc3a5facfb76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4BXUQH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDM5QuQ%2F8sUpo29J9LNXfkjlGKTROrFQr%2FVrOBAOief5QIgKnMJPMvZPDSUuGeG3N1g48VuVsd2Kt4vxLNrXKG40mkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7QQupSPihmBFSc0CrcA5ABhDCCb6ZbgZ6qT%2FDd%2F8EkNay6trwTyEfXfH6DGUT1xnDjeb0aE18Qhs8hQLZi0IQwtHUHxtlkxL%2FKOU7ASxy%2BuBfhsWlEOMQwU6nxwitJ8OvcKR3jdB%2BgHBQP22Erc%2F4xFSdatRIOAgZprz7rHQCbScvixyYkUwOMH1hkxO3v4PmTUpi%2BMvBfCG9ln%2FsuLS9fgMYTdBpNfYbJ7X26034aEevJ27NcEWNYSZhvf%2FNrRetiU1XgiBrhMQvPOxm%2BPIk7DQ0WzxE8BCHe3ecv3Jlgvp47OOONfANerpujpphWqMVbpSUYVhRxMy05p3cG5Rjc2uTXZGGo%2Bz2fHlGlbw1FpMul9ZftO3o1nyEr%2F2zwCscCfoYBjEhtddLut7Jm9PWe6KG3sh%2BRuT6iAJ79CvoD%2FVpSttwJXoz6TMoKAM6fyx8xeajok2s4xEw5M0PJnsHX0W8nn72VnaAU3cR6iP8ki68Hhnc%2BOweMnmfgbTNNs2xaENdngO%2BMJipFzfIXX5CM5E%2FBBDa0ONEZR%2B5FwJO%2BRU0hqZ4wGzfSbrFYTPqVTLUYJ42hFrqM6k%2B6h2b806K9Bt%2BLXYwpXXG2ASH%2BdQRjev4FdOwdQnQ1jFT0j4dgTw7v9GrZHBL5nvw0MP%2B%2B3c0GOqUBE7WWjMzBWp7fTaFcSbbg%2BeRgUTyCM22L8QQ2xu3H8cXC78UUfyDFGn%2BLt%2FE16lM5Zsp9P0XZJ7EDFTw5wPo1KybZVWBTupHEdF7ZEHxa98vGtlCTHRZARozjrGOEHKYz9zmRxGyj6ZmZbRk%2BS0gy%2F%2FzIjdQapR3H%2BfxZ7d1Js5Ru6SWX977zt4tsEijyyrrMNy6veJ05f5IOTVkx3KyFGuNz2ExK&X-Amz-Signature=287103c5bf5bf9fa13d283dca4bc9b596b5f720515b1ddbb97666dc347854fc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4BXUQH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDM5QuQ%2F8sUpo29J9LNXfkjlGKTROrFQr%2FVrOBAOief5QIgKnMJPMvZPDSUuGeG3N1g48VuVsd2Kt4vxLNrXKG40mkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7QQupSPihmBFSc0CrcA5ABhDCCb6ZbgZ6qT%2FDd%2F8EkNay6trwTyEfXfH6DGUT1xnDjeb0aE18Qhs8hQLZi0IQwtHUHxtlkxL%2FKOU7ASxy%2BuBfhsWlEOMQwU6nxwitJ8OvcKR3jdB%2BgHBQP22Erc%2F4xFSdatRIOAgZprz7rHQCbScvixyYkUwOMH1hkxO3v4PmTUpi%2BMvBfCG9ln%2FsuLS9fgMYTdBpNfYbJ7X26034aEevJ27NcEWNYSZhvf%2FNrRetiU1XgiBrhMQvPOxm%2BPIk7DQ0WzxE8BCHe3ecv3Jlgvp47OOONfANerpujpphWqMVbpSUYVhRxMy05p3cG5Rjc2uTXZGGo%2Bz2fHlGlbw1FpMul9ZftO3o1nyEr%2F2zwCscCfoYBjEhtddLut7Jm9PWe6KG3sh%2BRuT6iAJ79CvoD%2FVpSttwJXoz6TMoKAM6fyx8xeajok2s4xEw5M0PJnsHX0W8nn72VnaAU3cR6iP8ki68Hhnc%2BOweMnmfgbTNNs2xaENdngO%2BMJipFzfIXX5CM5E%2FBBDa0ONEZR%2B5FwJO%2BRU0hqZ4wGzfSbrFYTPqVTLUYJ42hFrqM6k%2B6h2b806K9Bt%2BLXYwpXXG2ASH%2BdQRjev4FdOwdQnQ1jFT0j4dgTw7v9GrZHBL5nvw0MP%2B%2B3c0GOqUBE7WWjMzBWp7fTaFcSbbg%2BeRgUTyCM22L8QQ2xu3H8cXC78UUfyDFGn%2BLt%2FE16lM5Zsp9P0XZJ7EDFTw5wPo1KybZVWBTupHEdF7ZEHxa98vGtlCTHRZARozjrGOEHKYz9zmRxGyj6ZmZbRk%2BS0gy%2F%2FzIjdQapR3H%2BfxZ7d1Js5Ru6SWX977zt4tsEijyyrrMNy6veJ05f5IOTVkx3KyFGuNz2ExK&X-Amz-Signature=d95396aed5a077ed8fb7173025c05aa1cd67be24436112b922b3045c7d751b4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4BXUQH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDM5QuQ%2F8sUpo29J9LNXfkjlGKTROrFQr%2FVrOBAOief5QIgKnMJPMvZPDSUuGeG3N1g48VuVsd2Kt4vxLNrXKG40mkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7QQupSPihmBFSc0CrcA5ABhDCCb6ZbgZ6qT%2FDd%2F8EkNay6trwTyEfXfH6DGUT1xnDjeb0aE18Qhs8hQLZi0IQwtHUHxtlkxL%2FKOU7ASxy%2BuBfhsWlEOMQwU6nxwitJ8OvcKR3jdB%2BgHBQP22Erc%2F4xFSdatRIOAgZprz7rHQCbScvixyYkUwOMH1hkxO3v4PmTUpi%2BMvBfCG9ln%2FsuLS9fgMYTdBpNfYbJ7X26034aEevJ27NcEWNYSZhvf%2FNrRetiU1XgiBrhMQvPOxm%2BPIk7DQ0WzxE8BCHe3ecv3Jlgvp47OOONfANerpujpphWqMVbpSUYVhRxMy05p3cG5Rjc2uTXZGGo%2Bz2fHlGlbw1FpMul9ZftO3o1nyEr%2F2zwCscCfoYBjEhtddLut7Jm9PWe6KG3sh%2BRuT6iAJ79CvoD%2FVpSttwJXoz6TMoKAM6fyx8xeajok2s4xEw5M0PJnsHX0W8nn72VnaAU3cR6iP8ki68Hhnc%2BOweMnmfgbTNNs2xaENdngO%2BMJipFzfIXX5CM5E%2FBBDa0ONEZR%2B5FwJO%2BRU0hqZ4wGzfSbrFYTPqVTLUYJ42hFrqM6k%2B6h2b806K9Bt%2BLXYwpXXG2ASH%2BdQRjev4FdOwdQnQ1jFT0j4dgTw7v9GrZHBL5nvw0MP%2B%2B3c0GOqUBE7WWjMzBWp7fTaFcSbbg%2BeRgUTyCM22L8QQ2xu3H8cXC78UUfyDFGn%2BLt%2FE16lM5Zsp9P0XZJ7EDFTw5wPo1KybZVWBTupHEdF7ZEHxa98vGtlCTHRZARozjrGOEHKYz9zmRxGyj6ZmZbRk%2BS0gy%2F%2FzIjdQapR3H%2BfxZ7d1Js5Ru6SWX977zt4tsEijyyrrMNy6veJ05f5IOTVkx3KyFGuNz2ExK&X-Amz-Signature=d7b8dcbb7dbf6e01e6a34b0882d0f81b7f7ad53d0a644a7f25f0cf4db6f50c3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK4BXUQH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDM5QuQ%2F8sUpo29J9LNXfkjlGKTROrFQr%2FVrOBAOief5QIgKnMJPMvZPDSUuGeG3N1g48VuVsd2Kt4vxLNrXKG40mkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7QQupSPihmBFSc0CrcA5ABhDCCb6ZbgZ6qT%2FDd%2F8EkNay6trwTyEfXfH6DGUT1xnDjeb0aE18Qhs8hQLZi0IQwtHUHxtlkxL%2FKOU7ASxy%2BuBfhsWlEOMQwU6nxwitJ8OvcKR3jdB%2BgHBQP22Erc%2F4xFSdatRIOAgZprz7rHQCbScvixyYkUwOMH1hkxO3v4PmTUpi%2BMvBfCG9ln%2FsuLS9fgMYTdBpNfYbJ7X26034aEevJ27NcEWNYSZhvf%2FNrRetiU1XgiBrhMQvPOxm%2BPIk7DQ0WzxE8BCHe3ecv3Jlgvp47OOONfANerpujpphWqMVbpSUYVhRxMy05p3cG5Rjc2uTXZGGo%2Bz2fHlGlbw1FpMul9ZftO3o1nyEr%2F2zwCscCfoYBjEhtddLut7Jm9PWe6KG3sh%2BRuT6iAJ79CvoD%2FVpSttwJXoz6TMoKAM6fyx8xeajok2s4xEw5M0PJnsHX0W8nn72VnaAU3cR6iP8ki68Hhnc%2BOweMnmfgbTNNs2xaENdngO%2BMJipFzfIXX5CM5E%2FBBDa0ONEZR%2B5FwJO%2BRU0hqZ4wGzfSbrFYTPqVTLUYJ42hFrqM6k%2B6h2b806K9Bt%2BLXYwpXXG2ASH%2BdQRjev4FdOwdQnQ1jFT0j4dgTw7v9GrZHBL5nvw0MP%2B%2B3c0GOqUBE7WWjMzBWp7fTaFcSbbg%2BeRgUTyCM22L8QQ2xu3H8cXC78UUfyDFGn%2BLt%2FE16lM5Zsp9P0XZJ7EDFTw5wPo1KybZVWBTupHEdF7ZEHxa98vGtlCTHRZARozjrGOEHKYz9zmRxGyj6ZmZbRk%2BS0gy%2F%2FzIjdQapR3H%2BfxZ7d1Js5Ru6SWX977zt4tsEijyyrrMNy6veJ05f5IOTVkx3KyFGuNz2ExK&X-Amz-Signature=69715af6d42bfb1b963d76b0ee055d1cc68453b531f0e302665e7a84909d2004&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

