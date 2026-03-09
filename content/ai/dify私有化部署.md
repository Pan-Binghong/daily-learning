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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CMOB5WU%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDIGy%2FHxB4wFx3WAyiIIjdz5QIefDgSiMjtjAfwDGhe%2BAIgSWtcma9iu2Q8gD6TP%2FYOc4pnL3xpRwieDC4b%2B7MX18Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJy9XvBk1lIy8kxHQCrcA6iK8oAhNszngo0er9ENu%2BoiTb87vhHbHkLIRo5gRWQLkm1GwWQd%2F3Z8U7mMmKu%2BKtby2iTYeZmeRNoNgxYgtNAJh2llWOxVG2z5VRpU9ldTySgFf%2BjWSyzT50pYyLUc7LqjMQ97B0tcPMXMLuvw0ilCrqEuDovITZoTL%2F08NyWKu8caT%2F405SbNreopAQ%2FOAjHXNwy27L1QZrc%2BcnNdYUTfO1XykXmdPqfeDcR7srIjJOZfGqZTxHgyVs%2BybAg70njs6b4MXDDYt%2FU86h%2BJRs9ZlK2SfM7LhvPSnLrHwrwTlopHRV01DFgHZhkFOveV7g2e55Fc3LlyM2wMXTMjVWJKLS6qlW6RnVp0OKbMSYqfr6oVJy5lLw1rKcS1wdsFYwc9vpxyJhNt7%2FuUD%2BdPuN%2FSun9FKCydTXi9HNTpBguQ%2B%2BOcTKfClS0ML1pOjo%2FTe9EqUo%2FKDVmXhBBiy82P%2Fmt5dReBQEDdu4IlzArpszUiHq2Bjg3NwfvavGnhROMHdCvnuzCzAJU3VyH0CYpaYMlczeSDz9WpQRQual1mi2PbgyZAwDym53i55jDAg%2B6yoJxf5JUo2qqiTccpT8OTsh%2BgpcJeCZX%2FbUna7kiu3CV7ud%2FI7C%2BBtGLTklMvMOL9uM0GOqUBxyQFh1wMWnvxQxtnk%2FdzmjJD9KBRY9IlG4Yjq6P%2BRFaYfrK53yKIYSljpTCnx143fQabvjK2seS5whoV0wel8gkS%2FVSuZwMuzAb9KzZRT4B87T9hZb%2B9ULtiNR6Gve4w8jc3s9uFaivYravHAHzmhkZoBXoeH3X8xpuDbguERDhEkuV98eagq%2F%2FPtb4fEW86YtInf7G6P%2BQsuab8ujnjYaYkMwJU&X-Amz-Signature=dc86a5b21e6fd5398ad5206a4b6202941c2f301738a6399ef59cf06f18fac0ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CMOB5WU%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDIGy%2FHxB4wFx3WAyiIIjdz5QIefDgSiMjtjAfwDGhe%2BAIgSWtcma9iu2Q8gD6TP%2FYOc4pnL3xpRwieDC4b%2B7MX18Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJy9XvBk1lIy8kxHQCrcA6iK8oAhNszngo0er9ENu%2BoiTb87vhHbHkLIRo5gRWQLkm1GwWQd%2F3Z8U7mMmKu%2BKtby2iTYeZmeRNoNgxYgtNAJh2llWOxVG2z5VRpU9ldTySgFf%2BjWSyzT50pYyLUc7LqjMQ97B0tcPMXMLuvw0ilCrqEuDovITZoTL%2F08NyWKu8caT%2F405SbNreopAQ%2FOAjHXNwy27L1QZrc%2BcnNdYUTfO1XykXmdPqfeDcR7srIjJOZfGqZTxHgyVs%2BybAg70njs6b4MXDDYt%2FU86h%2BJRs9ZlK2SfM7LhvPSnLrHwrwTlopHRV01DFgHZhkFOveV7g2e55Fc3LlyM2wMXTMjVWJKLS6qlW6RnVp0OKbMSYqfr6oVJy5lLw1rKcS1wdsFYwc9vpxyJhNt7%2FuUD%2BdPuN%2FSun9FKCydTXi9HNTpBguQ%2B%2BOcTKfClS0ML1pOjo%2FTe9EqUo%2FKDVmXhBBiy82P%2Fmt5dReBQEDdu4IlzArpszUiHq2Bjg3NwfvavGnhROMHdCvnuzCzAJU3VyH0CYpaYMlczeSDz9WpQRQual1mi2PbgyZAwDym53i55jDAg%2B6yoJxf5JUo2qqiTccpT8OTsh%2BgpcJeCZX%2FbUna7kiu3CV7ud%2FI7C%2BBtGLTklMvMOL9uM0GOqUBxyQFh1wMWnvxQxtnk%2FdzmjJD9KBRY9IlG4Yjq6P%2BRFaYfrK53yKIYSljpTCnx143fQabvjK2seS5whoV0wel8gkS%2FVSuZwMuzAb9KzZRT4B87T9hZb%2B9ULtiNR6Gve4w8jc3s9uFaivYravHAHzmhkZoBXoeH3X8xpuDbguERDhEkuV98eagq%2F%2FPtb4fEW86YtInf7G6P%2BQsuab8ujnjYaYkMwJU&X-Amz-Signature=1db55e88ceb488f73e1b54c552d202003beee667ca03b44410744c4247c1caf8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CMOB5WU%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDIGy%2FHxB4wFx3WAyiIIjdz5QIefDgSiMjtjAfwDGhe%2BAIgSWtcma9iu2Q8gD6TP%2FYOc4pnL3xpRwieDC4b%2B7MX18Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJy9XvBk1lIy8kxHQCrcA6iK8oAhNszngo0er9ENu%2BoiTb87vhHbHkLIRo5gRWQLkm1GwWQd%2F3Z8U7mMmKu%2BKtby2iTYeZmeRNoNgxYgtNAJh2llWOxVG2z5VRpU9ldTySgFf%2BjWSyzT50pYyLUc7LqjMQ97B0tcPMXMLuvw0ilCrqEuDovITZoTL%2F08NyWKu8caT%2F405SbNreopAQ%2FOAjHXNwy27L1QZrc%2BcnNdYUTfO1XykXmdPqfeDcR7srIjJOZfGqZTxHgyVs%2BybAg70njs6b4MXDDYt%2FU86h%2BJRs9ZlK2SfM7LhvPSnLrHwrwTlopHRV01DFgHZhkFOveV7g2e55Fc3LlyM2wMXTMjVWJKLS6qlW6RnVp0OKbMSYqfr6oVJy5lLw1rKcS1wdsFYwc9vpxyJhNt7%2FuUD%2BdPuN%2FSun9FKCydTXi9HNTpBguQ%2B%2BOcTKfClS0ML1pOjo%2FTe9EqUo%2FKDVmXhBBiy82P%2Fmt5dReBQEDdu4IlzArpszUiHq2Bjg3NwfvavGnhROMHdCvnuzCzAJU3VyH0CYpaYMlczeSDz9WpQRQual1mi2PbgyZAwDym53i55jDAg%2B6yoJxf5JUo2qqiTccpT8OTsh%2BgpcJeCZX%2FbUna7kiu3CV7ud%2FI7C%2BBtGLTklMvMOL9uM0GOqUBxyQFh1wMWnvxQxtnk%2FdzmjJD9KBRY9IlG4Yjq6P%2BRFaYfrK53yKIYSljpTCnx143fQabvjK2seS5whoV0wel8gkS%2FVSuZwMuzAb9KzZRT4B87T9hZb%2B9ULtiNR6Gve4w8jc3s9uFaivYravHAHzmhkZoBXoeH3X8xpuDbguERDhEkuV98eagq%2F%2FPtb4fEW86YtInf7G6P%2BQsuab8ujnjYaYkMwJU&X-Amz-Signature=0e16428df7c673e6d58a91c918ae7a3bcee3f2ee4e0fa755fc218fae0894175a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CMOB5WU%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDIGy%2FHxB4wFx3WAyiIIjdz5QIefDgSiMjtjAfwDGhe%2BAIgSWtcma9iu2Q8gD6TP%2FYOc4pnL3xpRwieDC4b%2B7MX18Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJy9XvBk1lIy8kxHQCrcA6iK8oAhNszngo0er9ENu%2BoiTb87vhHbHkLIRo5gRWQLkm1GwWQd%2F3Z8U7mMmKu%2BKtby2iTYeZmeRNoNgxYgtNAJh2llWOxVG2z5VRpU9ldTySgFf%2BjWSyzT50pYyLUc7LqjMQ97B0tcPMXMLuvw0ilCrqEuDovITZoTL%2F08NyWKu8caT%2F405SbNreopAQ%2FOAjHXNwy27L1QZrc%2BcnNdYUTfO1XykXmdPqfeDcR7srIjJOZfGqZTxHgyVs%2BybAg70njs6b4MXDDYt%2FU86h%2BJRs9ZlK2SfM7LhvPSnLrHwrwTlopHRV01DFgHZhkFOveV7g2e55Fc3LlyM2wMXTMjVWJKLS6qlW6RnVp0OKbMSYqfr6oVJy5lLw1rKcS1wdsFYwc9vpxyJhNt7%2FuUD%2BdPuN%2FSun9FKCydTXi9HNTpBguQ%2B%2BOcTKfClS0ML1pOjo%2FTe9EqUo%2FKDVmXhBBiy82P%2Fmt5dReBQEDdu4IlzArpszUiHq2Bjg3NwfvavGnhROMHdCvnuzCzAJU3VyH0CYpaYMlczeSDz9WpQRQual1mi2PbgyZAwDym53i55jDAg%2B6yoJxf5JUo2qqiTccpT8OTsh%2BgpcJeCZX%2FbUna7kiu3CV7ud%2FI7C%2BBtGLTklMvMOL9uM0GOqUBxyQFh1wMWnvxQxtnk%2FdzmjJD9KBRY9IlG4Yjq6P%2BRFaYfrK53yKIYSljpTCnx143fQabvjK2seS5whoV0wel8gkS%2FVSuZwMuzAb9KzZRT4B87T9hZb%2B9ULtiNR6Gve4w8jc3s9uFaivYravHAHzmhkZoBXoeH3X8xpuDbguERDhEkuV98eagq%2F%2FPtb4fEW86YtInf7G6P%2BQsuab8ujnjYaYkMwJU&X-Amz-Signature=ff96daaac68a6a720f34810ba4a2e2f24d8e63940f1165ba000c09e32799d446&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CMOB5WU%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDIGy%2FHxB4wFx3WAyiIIjdz5QIefDgSiMjtjAfwDGhe%2BAIgSWtcma9iu2Q8gD6TP%2FYOc4pnL3xpRwieDC4b%2B7MX18Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJy9XvBk1lIy8kxHQCrcA6iK8oAhNszngo0er9ENu%2BoiTb87vhHbHkLIRo5gRWQLkm1GwWQd%2F3Z8U7mMmKu%2BKtby2iTYeZmeRNoNgxYgtNAJh2llWOxVG2z5VRpU9ldTySgFf%2BjWSyzT50pYyLUc7LqjMQ97B0tcPMXMLuvw0ilCrqEuDovITZoTL%2F08NyWKu8caT%2F405SbNreopAQ%2FOAjHXNwy27L1QZrc%2BcnNdYUTfO1XykXmdPqfeDcR7srIjJOZfGqZTxHgyVs%2BybAg70njs6b4MXDDYt%2FU86h%2BJRs9ZlK2SfM7LhvPSnLrHwrwTlopHRV01DFgHZhkFOveV7g2e55Fc3LlyM2wMXTMjVWJKLS6qlW6RnVp0OKbMSYqfr6oVJy5lLw1rKcS1wdsFYwc9vpxyJhNt7%2FuUD%2BdPuN%2FSun9FKCydTXi9HNTpBguQ%2B%2BOcTKfClS0ML1pOjo%2FTe9EqUo%2FKDVmXhBBiy82P%2Fmt5dReBQEDdu4IlzArpszUiHq2Bjg3NwfvavGnhROMHdCvnuzCzAJU3VyH0CYpaYMlczeSDz9WpQRQual1mi2PbgyZAwDym53i55jDAg%2B6yoJxf5JUo2qqiTccpT8OTsh%2BgpcJeCZX%2FbUna7kiu3CV7ud%2FI7C%2BBtGLTklMvMOL9uM0GOqUBxyQFh1wMWnvxQxtnk%2FdzmjJD9KBRY9IlG4Yjq6P%2BRFaYfrK53yKIYSljpTCnx143fQabvjK2seS5whoV0wel8gkS%2FVSuZwMuzAb9KzZRT4B87T9hZb%2B9ULtiNR6Gve4w8jc3s9uFaivYravHAHzmhkZoBXoeH3X8xpuDbguERDhEkuV98eagq%2F%2FPtb4fEW86YtInf7G6P%2BQsuab8ujnjYaYkMwJU&X-Amz-Signature=76925a19669b1d89d3401f8383f401abe9a2d9ea374d2d745cf467e031088929&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CMOB5WU%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDIGy%2FHxB4wFx3WAyiIIjdz5QIefDgSiMjtjAfwDGhe%2BAIgSWtcma9iu2Q8gD6TP%2FYOc4pnL3xpRwieDC4b%2B7MX18Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJy9XvBk1lIy8kxHQCrcA6iK8oAhNszngo0er9ENu%2BoiTb87vhHbHkLIRo5gRWQLkm1GwWQd%2F3Z8U7mMmKu%2BKtby2iTYeZmeRNoNgxYgtNAJh2llWOxVG2z5VRpU9ldTySgFf%2BjWSyzT50pYyLUc7LqjMQ97B0tcPMXMLuvw0ilCrqEuDovITZoTL%2F08NyWKu8caT%2F405SbNreopAQ%2FOAjHXNwy27L1QZrc%2BcnNdYUTfO1XykXmdPqfeDcR7srIjJOZfGqZTxHgyVs%2BybAg70njs6b4MXDDYt%2FU86h%2BJRs9ZlK2SfM7LhvPSnLrHwrwTlopHRV01DFgHZhkFOveV7g2e55Fc3LlyM2wMXTMjVWJKLS6qlW6RnVp0OKbMSYqfr6oVJy5lLw1rKcS1wdsFYwc9vpxyJhNt7%2FuUD%2BdPuN%2FSun9FKCydTXi9HNTpBguQ%2B%2BOcTKfClS0ML1pOjo%2FTe9EqUo%2FKDVmXhBBiy82P%2Fmt5dReBQEDdu4IlzArpszUiHq2Bjg3NwfvavGnhROMHdCvnuzCzAJU3VyH0CYpaYMlczeSDz9WpQRQual1mi2PbgyZAwDym53i55jDAg%2B6yoJxf5JUo2qqiTccpT8OTsh%2BgpcJeCZX%2FbUna7kiu3CV7ud%2FI7C%2BBtGLTklMvMOL9uM0GOqUBxyQFh1wMWnvxQxtnk%2FdzmjJD9KBRY9IlG4Yjq6P%2BRFaYfrK53yKIYSljpTCnx143fQabvjK2seS5whoV0wel8gkS%2FVSuZwMuzAb9KzZRT4B87T9hZb%2B9ULtiNR6Gve4w8jc3s9uFaivYravHAHzmhkZoBXoeH3X8xpuDbguERDhEkuV98eagq%2F%2FPtb4fEW86YtInf7G6P%2BQsuab8ujnjYaYkMwJU&X-Amz-Signature=785e7c493dd27c26a90a641dcdf38e2bb634f25632901ba143cbbfef8551c777&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CMOB5WU%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDIGy%2FHxB4wFx3WAyiIIjdz5QIefDgSiMjtjAfwDGhe%2BAIgSWtcma9iu2Q8gD6TP%2FYOc4pnL3xpRwieDC4b%2B7MX18Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJy9XvBk1lIy8kxHQCrcA6iK8oAhNszngo0er9ENu%2BoiTb87vhHbHkLIRo5gRWQLkm1GwWQd%2F3Z8U7mMmKu%2BKtby2iTYeZmeRNoNgxYgtNAJh2llWOxVG2z5VRpU9ldTySgFf%2BjWSyzT50pYyLUc7LqjMQ97B0tcPMXMLuvw0ilCrqEuDovITZoTL%2F08NyWKu8caT%2F405SbNreopAQ%2FOAjHXNwy27L1QZrc%2BcnNdYUTfO1XykXmdPqfeDcR7srIjJOZfGqZTxHgyVs%2BybAg70njs6b4MXDDYt%2FU86h%2BJRs9ZlK2SfM7LhvPSnLrHwrwTlopHRV01DFgHZhkFOveV7g2e55Fc3LlyM2wMXTMjVWJKLS6qlW6RnVp0OKbMSYqfr6oVJy5lLw1rKcS1wdsFYwc9vpxyJhNt7%2FuUD%2BdPuN%2FSun9FKCydTXi9HNTpBguQ%2B%2BOcTKfClS0ML1pOjo%2FTe9EqUo%2FKDVmXhBBiy82P%2Fmt5dReBQEDdu4IlzArpszUiHq2Bjg3NwfvavGnhROMHdCvnuzCzAJU3VyH0CYpaYMlczeSDz9WpQRQual1mi2PbgyZAwDym53i55jDAg%2B6yoJxf5JUo2qqiTccpT8OTsh%2BgpcJeCZX%2FbUna7kiu3CV7ud%2FI7C%2BBtGLTklMvMOL9uM0GOqUBxyQFh1wMWnvxQxtnk%2FdzmjJD9KBRY9IlG4Yjq6P%2BRFaYfrK53yKIYSljpTCnx143fQabvjK2seS5whoV0wel8gkS%2FVSuZwMuzAb9KzZRT4B87T9hZb%2B9ULtiNR6Gve4w8jc3s9uFaivYravHAHzmhkZoBXoeH3X8xpuDbguERDhEkuV98eagq%2F%2FPtb4fEW86YtInf7G6P%2BQsuab8ujnjYaYkMwJU&X-Amz-Signature=9d85e61431300e4c36758a4f36fb6f5ddd6dcab13d483b53494ab32bc51cab9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CMOB5WU%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDIGy%2FHxB4wFx3WAyiIIjdz5QIefDgSiMjtjAfwDGhe%2BAIgSWtcma9iu2Q8gD6TP%2FYOc4pnL3xpRwieDC4b%2B7MX18Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJy9XvBk1lIy8kxHQCrcA6iK8oAhNszngo0er9ENu%2BoiTb87vhHbHkLIRo5gRWQLkm1GwWQd%2F3Z8U7mMmKu%2BKtby2iTYeZmeRNoNgxYgtNAJh2llWOxVG2z5VRpU9ldTySgFf%2BjWSyzT50pYyLUc7LqjMQ97B0tcPMXMLuvw0ilCrqEuDovITZoTL%2F08NyWKu8caT%2F405SbNreopAQ%2FOAjHXNwy27L1QZrc%2BcnNdYUTfO1XykXmdPqfeDcR7srIjJOZfGqZTxHgyVs%2BybAg70njs6b4MXDDYt%2FU86h%2BJRs9ZlK2SfM7LhvPSnLrHwrwTlopHRV01DFgHZhkFOveV7g2e55Fc3LlyM2wMXTMjVWJKLS6qlW6RnVp0OKbMSYqfr6oVJy5lLw1rKcS1wdsFYwc9vpxyJhNt7%2FuUD%2BdPuN%2FSun9FKCydTXi9HNTpBguQ%2B%2BOcTKfClS0ML1pOjo%2FTe9EqUo%2FKDVmXhBBiy82P%2Fmt5dReBQEDdu4IlzArpszUiHq2Bjg3NwfvavGnhROMHdCvnuzCzAJU3VyH0CYpaYMlczeSDz9WpQRQual1mi2PbgyZAwDym53i55jDAg%2B6yoJxf5JUo2qqiTccpT8OTsh%2BgpcJeCZX%2FbUna7kiu3CV7ud%2FI7C%2BBtGLTklMvMOL9uM0GOqUBxyQFh1wMWnvxQxtnk%2FdzmjJD9KBRY9IlG4Yjq6P%2BRFaYfrK53yKIYSljpTCnx143fQabvjK2seS5whoV0wel8gkS%2FVSuZwMuzAb9KzZRT4B87T9hZb%2B9ULtiNR6Gve4w8jc3s9uFaivYravHAHzmhkZoBXoeH3X8xpuDbguERDhEkuV98eagq%2F%2FPtb4fEW86YtInf7G6P%2BQsuab8ujnjYaYkMwJU&X-Amz-Signature=e3453f06ab849a51bf291c11b7b0f3096a3188d67c60fbbfacadc979e49ab1e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CMOB5WU%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDIGy%2FHxB4wFx3WAyiIIjdz5QIefDgSiMjtjAfwDGhe%2BAIgSWtcma9iu2Q8gD6TP%2FYOc4pnL3xpRwieDC4b%2B7MX18Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJy9XvBk1lIy8kxHQCrcA6iK8oAhNszngo0er9ENu%2BoiTb87vhHbHkLIRo5gRWQLkm1GwWQd%2F3Z8U7mMmKu%2BKtby2iTYeZmeRNoNgxYgtNAJh2llWOxVG2z5VRpU9ldTySgFf%2BjWSyzT50pYyLUc7LqjMQ97B0tcPMXMLuvw0ilCrqEuDovITZoTL%2F08NyWKu8caT%2F405SbNreopAQ%2FOAjHXNwy27L1QZrc%2BcnNdYUTfO1XykXmdPqfeDcR7srIjJOZfGqZTxHgyVs%2BybAg70njs6b4MXDDYt%2FU86h%2BJRs9ZlK2SfM7LhvPSnLrHwrwTlopHRV01DFgHZhkFOveV7g2e55Fc3LlyM2wMXTMjVWJKLS6qlW6RnVp0OKbMSYqfr6oVJy5lLw1rKcS1wdsFYwc9vpxyJhNt7%2FuUD%2BdPuN%2FSun9FKCydTXi9HNTpBguQ%2B%2BOcTKfClS0ML1pOjo%2FTe9EqUo%2FKDVmXhBBiy82P%2Fmt5dReBQEDdu4IlzArpszUiHq2Bjg3NwfvavGnhROMHdCvnuzCzAJU3VyH0CYpaYMlczeSDz9WpQRQual1mi2PbgyZAwDym53i55jDAg%2B6yoJxf5JUo2qqiTccpT8OTsh%2BgpcJeCZX%2FbUna7kiu3CV7ud%2FI7C%2BBtGLTklMvMOL9uM0GOqUBxyQFh1wMWnvxQxtnk%2FdzmjJD9KBRY9IlG4Yjq6P%2BRFaYfrK53yKIYSljpTCnx143fQabvjK2seS5whoV0wel8gkS%2FVSuZwMuzAb9KzZRT4B87T9hZb%2B9ULtiNR6Gve4w8jc3s9uFaivYravHAHzmhkZoBXoeH3X8xpuDbguERDhEkuV98eagq%2F%2FPtb4fEW86YtInf7G6P%2BQsuab8ujnjYaYkMwJU&X-Amz-Signature=025ecdd916869a67f2b2fb8114f5bc302cf196f5672e03527a4d28fb29b5f454&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CMOB5WU%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDIGy%2FHxB4wFx3WAyiIIjdz5QIefDgSiMjtjAfwDGhe%2BAIgSWtcma9iu2Q8gD6TP%2FYOc4pnL3xpRwieDC4b%2B7MX18Aq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJy9XvBk1lIy8kxHQCrcA6iK8oAhNszngo0er9ENu%2BoiTb87vhHbHkLIRo5gRWQLkm1GwWQd%2F3Z8U7mMmKu%2BKtby2iTYeZmeRNoNgxYgtNAJh2llWOxVG2z5VRpU9ldTySgFf%2BjWSyzT50pYyLUc7LqjMQ97B0tcPMXMLuvw0ilCrqEuDovITZoTL%2F08NyWKu8caT%2F405SbNreopAQ%2FOAjHXNwy27L1QZrc%2BcnNdYUTfO1XykXmdPqfeDcR7srIjJOZfGqZTxHgyVs%2BybAg70njs6b4MXDDYt%2FU86h%2BJRs9ZlK2SfM7LhvPSnLrHwrwTlopHRV01DFgHZhkFOveV7g2e55Fc3LlyM2wMXTMjVWJKLS6qlW6RnVp0OKbMSYqfr6oVJy5lLw1rKcS1wdsFYwc9vpxyJhNt7%2FuUD%2BdPuN%2FSun9FKCydTXi9HNTpBguQ%2B%2BOcTKfClS0ML1pOjo%2FTe9EqUo%2FKDVmXhBBiy82P%2Fmt5dReBQEDdu4IlzArpszUiHq2Bjg3NwfvavGnhROMHdCvnuzCzAJU3VyH0CYpaYMlczeSDz9WpQRQual1mi2PbgyZAwDym53i55jDAg%2B6yoJxf5JUo2qqiTccpT8OTsh%2BgpcJeCZX%2FbUna7kiu3CV7ud%2FI7C%2BBtGLTklMvMOL9uM0GOqUBxyQFh1wMWnvxQxtnk%2FdzmjJD9KBRY9IlG4Yjq6P%2BRFaYfrK53yKIYSljpTCnx143fQabvjK2seS5whoV0wel8gkS%2FVSuZwMuzAb9KzZRT4B87T9hZb%2B9ULtiNR6Gve4w8jc3s9uFaivYravHAHzmhkZoBXoeH3X8xpuDbguERDhEkuV98eagq%2F%2FPtb4fEW86YtInf7G6P%2BQsuab8ujnjYaYkMwJU&X-Amz-Signature=b6ccb8d405b72a494e57a0e4c0921d4538ac47605eeb6aa93941def5e97702df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

