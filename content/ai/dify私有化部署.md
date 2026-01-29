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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IETEVMA%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6M4lmsH8z6Z2uxnWs2O%2Fl%2B7V3NHhKPExt3DPk%2BVqDzgIhAK2h2QSJHqA2DXRyUUQTg5xusB5gPPtqTahrLgwb7QoVKv8DCHwQABoMNjM3NDIzMTgzODA1Igx4qoIDKOzuP4rY0QUq3AO3%2Ft9kG5AZ5Ir7zcQs7luk3vhLfs2zVhyphm1lhbvw1BYr6AwtX%2Bauij66SrUTeq4wpLOIO7fZpzmFc3qd%2B5FHSHpu7qjMrwHZTQ%2FGfhSPyFlXwSgLJt%2FNOEIHKDCuRZaV5c9j0q6Vn%2Fd2W4Ii63ax74%2FXiHoVtHFy3KfxWk0nHY13jeWCQ1Xk3syfa69pp%2FuSYGPfjZcswu1JSL9Jx1oh1%2FvJDC5gcVfhkivojL8bFqifrrY%2F2jfo2%2F%2BOl91f%2BV%2BcEQP7Db1xkBPnfz6TErvolE%2BmwMmTnLqMt5LWVzI10LicGYv8%2Fxz1GB1Eeg5vvxLpIyerYvHGq%2FQg2Vvhub7SgFfJ0xMTnJYKTVEs%2FVGBavgafAmuHP2P8tf9XM7q28P3TlCeOFxKjKo%2FmCkGMo9mq77ZA5u1WN6GA3pTpYfoSraIvTZuO5yRUOYeMC%2F5K22TXB5kY%2FGACwvn6Zbpk7yHrz8JutHasRU55180bDPA%2BlUhlm8cmHv9ib%2FxxMSsM4njHRqwLSqSZiJXE4fcd7wolZoMQvC152MHSsLKqhgmeDNhc0lp4BlNVgxHw4okcmYiEkQ194xIkEZB0xb28azBAWsivCzTggR0HXGNVso3oG50BX3kvPC5b7wCtDCoouvLBjqkAYsq8WCI0mTSNx4i93wF5H2amVry%2BlaibvMvYESljGdtY7%2FKJhMFb2i%2BfmCMAL17EnqErF2gT%2FCBlDWopAyPvJMuKOI7T5tejGFKZ7G6MAHVAxVDy8BvcK1D1hcKtUBFmvVteoGjdW%2F%2FUKl26eOgGXuF4yY0NMb%2BzWo1ahubROWlF1mf0ddNEkYAFHI%2B7VhGhKJz8RhsRrEzaD9Zsmcx1i6t3Ltq&X-Amz-Signature=78db93b1482e56b33d211048be9a41e6d92525875fbcfec65cebbdf2c8bd44cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IETEVMA%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6M4lmsH8z6Z2uxnWs2O%2Fl%2B7V3NHhKPExt3DPk%2BVqDzgIhAK2h2QSJHqA2DXRyUUQTg5xusB5gPPtqTahrLgwb7QoVKv8DCHwQABoMNjM3NDIzMTgzODA1Igx4qoIDKOzuP4rY0QUq3AO3%2Ft9kG5AZ5Ir7zcQs7luk3vhLfs2zVhyphm1lhbvw1BYr6AwtX%2Bauij66SrUTeq4wpLOIO7fZpzmFc3qd%2B5FHSHpu7qjMrwHZTQ%2FGfhSPyFlXwSgLJt%2FNOEIHKDCuRZaV5c9j0q6Vn%2Fd2W4Ii63ax74%2FXiHoVtHFy3KfxWk0nHY13jeWCQ1Xk3syfa69pp%2FuSYGPfjZcswu1JSL9Jx1oh1%2FvJDC5gcVfhkivojL8bFqifrrY%2F2jfo2%2F%2BOl91f%2BV%2BcEQP7Db1xkBPnfz6TErvolE%2BmwMmTnLqMt5LWVzI10LicGYv8%2Fxz1GB1Eeg5vvxLpIyerYvHGq%2FQg2Vvhub7SgFfJ0xMTnJYKTVEs%2FVGBavgafAmuHP2P8tf9XM7q28P3TlCeOFxKjKo%2FmCkGMo9mq77ZA5u1WN6GA3pTpYfoSraIvTZuO5yRUOYeMC%2F5K22TXB5kY%2FGACwvn6Zbpk7yHrz8JutHasRU55180bDPA%2BlUhlm8cmHv9ib%2FxxMSsM4njHRqwLSqSZiJXE4fcd7wolZoMQvC152MHSsLKqhgmeDNhc0lp4BlNVgxHw4okcmYiEkQ194xIkEZB0xb28azBAWsivCzTggR0HXGNVso3oG50BX3kvPC5b7wCtDCoouvLBjqkAYsq8WCI0mTSNx4i93wF5H2amVry%2BlaibvMvYESljGdtY7%2FKJhMFb2i%2BfmCMAL17EnqErF2gT%2FCBlDWopAyPvJMuKOI7T5tejGFKZ7G6MAHVAxVDy8BvcK1D1hcKtUBFmvVteoGjdW%2F%2FUKl26eOgGXuF4yY0NMb%2BzWo1ahubROWlF1mf0ddNEkYAFHI%2B7VhGhKJz8RhsRrEzaD9Zsmcx1i6t3Ltq&X-Amz-Signature=76ae11c9bde3797632ce99509497bbc56d427b7e6f583f6da847d1ac94643c0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IETEVMA%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6M4lmsH8z6Z2uxnWs2O%2Fl%2B7V3NHhKPExt3DPk%2BVqDzgIhAK2h2QSJHqA2DXRyUUQTg5xusB5gPPtqTahrLgwb7QoVKv8DCHwQABoMNjM3NDIzMTgzODA1Igx4qoIDKOzuP4rY0QUq3AO3%2Ft9kG5AZ5Ir7zcQs7luk3vhLfs2zVhyphm1lhbvw1BYr6AwtX%2Bauij66SrUTeq4wpLOIO7fZpzmFc3qd%2B5FHSHpu7qjMrwHZTQ%2FGfhSPyFlXwSgLJt%2FNOEIHKDCuRZaV5c9j0q6Vn%2Fd2W4Ii63ax74%2FXiHoVtHFy3KfxWk0nHY13jeWCQ1Xk3syfa69pp%2FuSYGPfjZcswu1JSL9Jx1oh1%2FvJDC5gcVfhkivojL8bFqifrrY%2F2jfo2%2F%2BOl91f%2BV%2BcEQP7Db1xkBPnfz6TErvolE%2BmwMmTnLqMt5LWVzI10LicGYv8%2Fxz1GB1Eeg5vvxLpIyerYvHGq%2FQg2Vvhub7SgFfJ0xMTnJYKTVEs%2FVGBavgafAmuHP2P8tf9XM7q28P3TlCeOFxKjKo%2FmCkGMo9mq77ZA5u1WN6GA3pTpYfoSraIvTZuO5yRUOYeMC%2F5K22TXB5kY%2FGACwvn6Zbpk7yHrz8JutHasRU55180bDPA%2BlUhlm8cmHv9ib%2FxxMSsM4njHRqwLSqSZiJXE4fcd7wolZoMQvC152MHSsLKqhgmeDNhc0lp4BlNVgxHw4okcmYiEkQ194xIkEZB0xb28azBAWsivCzTggR0HXGNVso3oG50BX3kvPC5b7wCtDCoouvLBjqkAYsq8WCI0mTSNx4i93wF5H2amVry%2BlaibvMvYESljGdtY7%2FKJhMFb2i%2BfmCMAL17EnqErF2gT%2FCBlDWopAyPvJMuKOI7T5tejGFKZ7G6MAHVAxVDy8BvcK1D1hcKtUBFmvVteoGjdW%2F%2FUKl26eOgGXuF4yY0NMb%2BzWo1ahubROWlF1mf0ddNEkYAFHI%2B7VhGhKJz8RhsRrEzaD9Zsmcx1i6t3Ltq&X-Amz-Signature=1aede32f445788273408bcb80fe4e34ef44d6ea43bfc71c9d727989798cb1d55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IETEVMA%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6M4lmsH8z6Z2uxnWs2O%2Fl%2B7V3NHhKPExt3DPk%2BVqDzgIhAK2h2QSJHqA2DXRyUUQTg5xusB5gPPtqTahrLgwb7QoVKv8DCHwQABoMNjM3NDIzMTgzODA1Igx4qoIDKOzuP4rY0QUq3AO3%2Ft9kG5AZ5Ir7zcQs7luk3vhLfs2zVhyphm1lhbvw1BYr6AwtX%2Bauij66SrUTeq4wpLOIO7fZpzmFc3qd%2B5FHSHpu7qjMrwHZTQ%2FGfhSPyFlXwSgLJt%2FNOEIHKDCuRZaV5c9j0q6Vn%2Fd2W4Ii63ax74%2FXiHoVtHFy3KfxWk0nHY13jeWCQ1Xk3syfa69pp%2FuSYGPfjZcswu1JSL9Jx1oh1%2FvJDC5gcVfhkivojL8bFqifrrY%2F2jfo2%2F%2BOl91f%2BV%2BcEQP7Db1xkBPnfz6TErvolE%2BmwMmTnLqMt5LWVzI10LicGYv8%2Fxz1GB1Eeg5vvxLpIyerYvHGq%2FQg2Vvhub7SgFfJ0xMTnJYKTVEs%2FVGBavgafAmuHP2P8tf9XM7q28P3TlCeOFxKjKo%2FmCkGMo9mq77ZA5u1WN6GA3pTpYfoSraIvTZuO5yRUOYeMC%2F5K22TXB5kY%2FGACwvn6Zbpk7yHrz8JutHasRU55180bDPA%2BlUhlm8cmHv9ib%2FxxMSsM4njHRqwLSqSZiJXE4fcd7wolZoMQvC152MHSsLKqhgmeDNhc0lp4BlNVgxHw4okcmYiEkQ194xIkEZB0xb28azBAWsivCzTggR0HXGNVso3oG50BX3kvPC5b7wCtDCoouvLBjqkAYsq8WCI0mTSNx4i93wF5H2amVry%2BlaibvMvYESljGdtY7%2FKJhMFb2i%2BfmCMAL17EnqErF2gT%2FCBlDWopAyPvJMuKOI7T5tejGFKZ7G6MAHVAxVDy8BvcK1D1hcKtUBFmvVteoGjdW%2F%2FUKl26eOgGXuF4yY0NMb%2BzWo1ahubROWlF1mf0ddNEkYAFHI%2B7VhGhKJz8RhsRrEzaD9Zsmcx1i6t3Ltq&X-Amz-Signature=32c63f9d2d38f49722cfceaadbc94a633675bb15dddfbdc1a1a30d075e7e897f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IETEVMA%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6M4lmsH8z6Z2uxnWs2O%2Fl%2B7V3NHhKPExt3DPk%2BVqDzgIhAK2h2QSJHqA2DXRyUUQTg5xusB5gPPtqTahrLgwb7QoVKv8DCHwQABoMNjM3NDIzMTgzODA1Igx4qoIDKOzuP4rY0QUq3AO3%2Ft9kG5AZ5Ir7zcQs7luk3vhLfs2zVhyphm1lhbvw1BYr6AwtX%2Bauij66SrUTeq4wpLOIO7fZpzmFc3qd%2B5FHSHpu7qjMrwHZTQ%2FGfhSPyFlXwSgLJt%2FNOEIHKDCuRZaV5c9j0q6Vn%2Fd2W4Ii63ax74%2FXiHoVtHFy3KfxWk0nHY13jeWCQ1Xk3syfa69pp%2FuSYGPfjZcswu1JSL9Jx1oh1%2FvJDC5gcVfhkivojL8bFqifrrY%2F2jfo2%2F%2BOl91f%2BV%2BcEQP7Db1xkBPnfz6TErvolE%2BmwMmTnLqMt5LWVzI10LicGYv8%2Fxz1GB1Eeg5vvxLpIyerYvHGq%2FQg2Vvhub7SgFfJ0xMTnJYKTVEs%2FVGBavgafAmuHP2P8tf9XM7q28P3TlCeOFxKjKo%2FmCkGMo9mq77ZA5u1WN6GA3pTpYfoSraIvTZuO5yRUOYeMC%2F5K22TXB5kY%2FGACwvn6Zbpk7yHrz8JutHasRU55180bDPA%2BlUhlm8cmHv9ib%2FxxMSsM4njHRqwLSqSZiJXE4fcd7wolZoMQvC152MHSsLKqhgmeDNhc0lp4BlNVgxHw4okcmYiEkQ194xIkEZB0xb28azBAWsivCzTggR0HXGNVso3oG50BX3kvPC5b7wCtDCoouvLBjqkAYsq8WCI0mTSNx4i93wF5H2amVry%2BlaibvMvYESljGdtY7%2FKJhMFb2i%2BfmCMAL17EnqErF2gT%2FCBlDWopAyPvJMuKOI7T5tejGFKZ7G6MAHVAxVDy8BvcK1D1hcKtUBFmvVteoGjdW%2F%2FUKl26eOgGXuF4yY0NMb%2BzWo1ahubROWlF1mf0ddNEkYAFHI%2B7VhGhKJz8RhsRrEzaD9Zsmcx1i6t3Ltq&X-Amz-Signature=ca5e7cee75c68b450a5198ed0fc7cf1429ae69ff4516746c9b76d8c9051671eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IETEVMA%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6M4lmsH8z6Z2uxnWs2O%2Fl%2B7V3NHhKPExt3DPk%2BVqDzgIhAK2h2QSJHqA2DXRyUUQTg5xusB5gPPtqTahrLgwb7QoVKv8DCHwQABoMNjM3NDIzMTgzODA1Igx4qoIDKOzuP4rY0QUq3AO3%2Ft9kG5AZ5Ir7zcQs7luk3vhLfs2zVhyphm1lhbvw1BYr6AwtX%2Bauij66SrUTeq4wpLOIO7fZpzmFc3qd%2B5FHSHpu7qjMrwHZTQ%2FGfhSPyFlXwSgLJt%2FNOEIHKDCuRZaV5c9j0q6Vn%2Fd2W4Ii63ax74%2FXiHoVtHFy3KfxWk0nHY13jeWCQ1Xk3syfa69pp%2FuSYGPfjZcswu1JSL9Jx1oh1%2FvJDC5gcVfhkivojL8bFqifrrY%2F2jfo2%2F%2BOl91f%2BV%2BcEQP7Db1xkBPnfz6TErvolE%2BmwMmTnLqMt5LWVzI10LicGYv8%2Fxz1GB1Eeg5vvxLpIyerYvHGq%2FQg2Vvhub7SgFfJ0xMTnJYKTVEs%2FVGBavgafAmuHP2P8tf9XM7q28P3TlCeOFxKjKo%2FmCkGMo9mq77ZA5u1WN6GA3pTpYfoSraIvTZuO5yRUOYeMC%2F5K22TXB5kY%2FGACwvn6Zbpk7yHrz8JutHasRU55180bDPA%2BlUhlm8cmHv9ib%2FxxMSsM4njHRqwLSqSZiJXE4fcd7wolZoMQvC152MHSsLKqhgmeDNhc0lp4BlNVgxHw4okcmYiEkQ194xIkEZB0xb28azBAWsivCzTggR0HXGNVso3oG50BX3kvPC5b7wCtDCoouvLBjqkAYsq8WCI0mTSNx4i93wF5H2amVry%2BlaibvMvYESljGdtY7%2FKJhMFb2i%2BfmCMAL17EnqErF2gT%2FCBlDWopAyPvJMuKOI7T5tejGFKZ7G6MAHVAxVDy8BvcK1D1hcKtUBFmvVteoGjdW%2F%2FUKl26eOgGXuF4yY0NMb%2BzWo1ahubROWlF1mf0ddNEkYAFHI%2B7VhGhKJz8RhsRrEzaD9Zsmcx1i6t3Ltq&X-Amz-Signature=058a718778ef2b2f261b996fbf0cf10e14cb23eef9d8409c741a3764a4fe2fd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IETEVMA%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6M4lmsH8z6Z2uxnWs2O%2Fl%2B7V3NHhKPExt3DPk%2BVqDzgIhAK2h2QSJHqA2DXRyUUQTg5xusB5gPPtqTahrLgwb7QoVKv8DCHwQABoMNjM3NDIzMTgzODA1Igx4qoIDKOzuP4rY0QUq3AO3%2Ft9kG5AZ5Ir7zcQs7luk3vhLfs2zVhyphm1lhbvw1BYr6AwtX%2Bauij66SrUTeq4wpLOIO7fZpzmFc3qd%2B5FHSHpu7qjMrwHZTQ%2FGfhSPyFlXwSgLJt%2FNOEIHKDCuRZaV5c9j0q6Vn%2Fd2W4Ii63ax74%2FXiHoVtHFy3KfxWk0nHY13jeWCQ1Xk3syfa69pp%2FuSYGPfjZcswu1JSL9Jx1oh1%2FvJDC5gcVfhkivojL8bFqifrrY%2F2jfo2%2F%2BOl91f%2BV%2BcEQP7Db1xkBPnfz6TErvolE%2BmwMmTnLqMt5LWVzI10LicGYv8%2Fxz1GB1Eeg5vvxLpIyerYvHGq%2FQg2Vvhub7SgFfJ0xMTnJYKTVEs%2FVGBavgafAmuHP2P8tf9XM7q28P3TlCeOFxKjKo%2FmCkGMo9mq77ZA5u1WN6GA3pTpYfoSraIvTZuO5yRUOYeMC%2F5K22TXB5kY%2FGACwvn6Zbpk7yHrz8JutHasRU55180bDPA%2BlUhlm8cmHv9ib%2FxxMSsM4njHRqwLSqSZiJXE4fcd7wolZoMQvC152MHSsLKqhgmeDNhc0lp4BlNVgxHw4okcmYiEkQ194xIkEZB0xb28azBAWsivCzTggR0HXGNVso3oG50BX3kvPC5b7wCtDCoouvLBjqkAYsq8WCI0mTSNx4i93wF5H2amVry%2BlaibvMvYESljGdtY7%2FKJhMFb2i%2BfmCMAL17EnqErF2gT%2FCBlDWopAyPvJMuKOI7T5tejGFKZ7G6MAHVAxVDy8BvcK1D1hcKtUBFmvVteoGjdW%2F%2FUKl26eOgGXuF4yY0NMb%2BzWo1ahubROWlF1mf0ddNEkYAFHI%2B7VhGhKJz8RhsRrEzaD9Zsmcx1i6t3Ltq&X-Amz-Signature=76aee618a753da7f6ef3ccaf1c198bb8ae3b2e0e9abbbebe1320ba9c30c1d4bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IETEVMA%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6M4lmsH8z6Z2uxnWs2O%2Fl%2B7V3NHhKPExt3DPk%2BVqDzgIhAK2h2QSJHqA2DXRyUUQTg5xusB5gPPtqTahrLgwb7QoVKv8DCHwQABoMNjM3NDIzMTgzODA1Igx4qoIDKOzuP4rY0QUq3AO3%2Ft9kG5AZ5Ir7zcQs7luk3vhLfs2zVhyphm1lhbvw1BYr6AwtX%2Bauij66SrUTeq4wpLOIO7fZpzmFc3qd%2B5FHSHpu7qjMrwHZTQ%2FGfhSPyFlXwSgLJt%2FNOEIHKDCuRZaV5c9j0q6Vn%2Fd2W4Ii63ax74%2FXiHoVtHFy3KfxWk0nHY13jeWCQ1Xk3syfa69pp%2FuSYGPfjZcswu1JSL9Jx1oh1%2FvJDC5gcVfhkivojL8bFqifrrY%2F2jfo2%2F%2BOl91f%2BV%2BcEQP7Db1xkBPnfz6TErvolE%2BmwMmTnLqMt5LWVzI10LicGYv8%2Fxz1GB1Eeg5vvxLpIyerYvHGq%2FQg2Vvhub7SgFfJ0xMTnJYKTVEs%2FVGBavgafAmuHP2P8tf9XM7q28P3TlCeOFxKjKo%2FmCkGMo9mq77ZA5u1WN6GA3pTpYfoSraIvTZuO5yRUOYeMC%2F5K22TXB5kY%2FGACwvn6Zbpk7yHrz8JutHasRU55180bDPA%2BlUhlm8cmHv9ib%2FxxMSsM4njHRqwLSqSZiJXE4fcd7wolZoMQvC152MHSsLKqhgmeDNhc0lp4BlNVgxHw4okcmYiEkQ194xIkEZB0xb28azBAWsivCzTggR0HXGNVso3oG50BX3kvPC5b7wCtDCoouvLBjqkAYsq8WCI0mTSNx4i93wF5H2amVry%2BlaibvMvYESljGdtY7%2FKJhMFb2i%2BfmCMAL17EnqErF2gT%2FCBlDWopAyPvJMuKOI7T5tejGFKZ7G6MAHVAxVDy8BvcK1D1hcKtUBFmvVteoGjdW%2F%2FUKl26eOgGXuF4yY0NMb%2BzWo1ahubROWlF1mf0ddNEkYAFHI%2B7VhGhKJz8RhsRrEzaD9Zsmcx1i6t3Ltq&X-Amz-Signature=ab604901ed0b397e3b8f49b295b13a18762e85027f33584b3fb22815c414669c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IETEVMA%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6M4lmsH8z6Z2uxnWs2O%2Fl%2B7V3NHhKPExt3DPk%2BVqDzgIhAK2h2QSJHqA2DXRyUUQTg5xusB5gPPtqTahrLgwb7QoVKv8DCHwQABoMNjM3NDIzMTgzODA1Igx4qoIDKOzuP4rY0QUq3AO3%2Ft9kG5AZ5Ir7zcQs7luk3vhLfs2zVhyphm1lhbvw1BYr6AwtX%2Bauij66SrUTeq4wpLOIO7fZpzmFc3qd%2B5FHSHpu7qjMrwHZTQ%2FGfhSPyFlXwSgLJt%2FNOEIHKDCuRZaV5c9j0q6Vn%2Fd2W4Ii63ax74%2FXiHoVtHFy3KfxWk0nHY13jeWCQ1Xk3syfa69pp%2FuSYGPfjZcswu1JSL9Jx1oh1%2FvJDC5gcVfhkivojL8bFqifrrY%2F2jfo2%2F%2BOl91f%2BV%2BcEQP7Db1xkBPnfz6TErvolE%2BmwMmTnLqMt5LWVzI10LicGYv8%2Fxz1GB1Eeg5vvxLpIyerYvHGq%2FQg2Vvhub7SgFfJ0xMTnJYKTVEs%2FVGBavgafAmuHP2P8tf9XM7q28P3TlCeOFxKjKo%2FmCkGMo9mq77ZA5u1WN6GA3pTpYfoSraIvTZuO5yRUOYeMC%2F5K22TXB5kY%2FGACwvn6Zbpk7yHrz8JutHasRU55180bDPA%2BlUhlm8cmHv9ib%2FxxMSsM4njHRqwLSqSZiJXE4fcd7wolZoMQvC152MHSsLKqhgmeDNhc0lp4BlNVgxHw4okcmYiEkQ194xIkEZB0xb28azBAWsivCzTggR0HXGNVso3oG50BX3kvPC5b7wCtDCoouvLBjqkAYsq8WCI0mTSNx4i93wF5H2amVry%2BlaibvMvYESljGdtY7%2FKJhMFb2i%2BfmCMAL17EnqErF2gT%2FCBlDWopAyPvJMuKOI7T5tejGFKZ7G6MAHVAxVDy8BvcK1D1hcKtUBFmvVteoGjdW%2F%2FUKl26eOgGXuF4yY0NMb%2BzWo1ahubROWlF1mf0ddNEkYAFHI%2B7VhGhKJz8RhsRrEzaD9Zsmcx1i6t3Ltq&X-Amz-Signature=5c807c196965f37b4daa7c2d19b5320b829033fc3aab4ec598a65984f0d4faef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IETEVMA%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6M4lmsH8z6Z2uxnWs2O%2Fl%2B7V3NHhKPExt3DPk%2BVqDzgIhAK2h2QSJHqA2DXRyUUQTg5xusB5gPPtqTahrLgwb7QoVKv8DCHwQABoMNjM3NDIzMTgzODA1Igx4qoIDKOzuP4rY0QUq3AO3%2Ft9kG5AZ5Ir7zcQs7luk3vhLfs2zVhyphm1lhbvw1BYr6AwtX%2Bauij66SrUTeq4wpLOIO7fZpzmFc3qd%2B5FHSHpu7qjMrwHZTQ%2FGfhSPyFlXwSgLJt%2FNOEIHKDCuRZaV5c9j0q6Vn%2Fd2W4Ii63ax74%2FXiHoVtHFy3KfxWk0nHY13jeWCQ1Xk3syfa69pp%2FuSYGPfjZcswu1JSL9Jx1oh1%2FvJDC5gcVfhkivojL8bFqifrrY%2F2jfo2%2F%2BOl91f%2BV%2BcEQP7Db1xkBPnfz6TErvolE%2BmwMmTnLqMt5LWVzI10LicGYv8%2Fxz1GB1Eeg5vvxLpIyerYvHGq%2FQg2Vvhub7SgFfJ0xMTnJYKTVEs%2FVGBavgafAmuHP2P8tf9XM7q28P3TlCeOFxKjKo%2FmCkGMo9mq77ZA5u1WN6GA3pTpYfoSraIvTZuO5yRUOYeMC%2F5K22TXB5kY%2FGACwvn6Zbpk7yHrz8JutHasRU55180bDPA%2BlUhlm8cmHv9ib%2FxxMSsM4njHRqwLSqSZiJXE4fcd7wolZoMQvC152MHSsLKqhgmeDNhc0lp4BlNVgxHw4okcmYiEkQ194xIkEZB0xb28azBAWsivCzTggR0HXGNVso3oG50BX3kvPC5b7wCtDCoouvLBjqkAYsq8WCI0mTSNx4i93wF5H2amVry%2BlaibvMvYESljGdtY7%2FKJhMFb2i%2BfmCMAL17EnqErF2gT%2FCBlDWopAyPvJMuKOI7T5tejGFKZ7G6MAHVAxVDy8BvcK1D1hcKtUBFmvVteoGjdW%2F%2FUKl26eOgGXuF4yY0NMb%2BzWo1ahubROWlF1mf0ddNEkYAFHI%2B7VhGhKJz8RhsRrEzaD9Zsmcx1i6t3Ltq&X-Amz-Signature=94164a391b099652cf0c00d0ab7cfee0240472f7e6ebb04e7197f376196706e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

