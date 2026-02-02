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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6AIIPDZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPz261PwK4sdVWGKU5hQnifBlkbNNPhaWLo20Z4dmV8AiBht9ArqsuQNYlm6CD7qZKCk0tQctra67juc9VMzwDvByqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgyGbm2YJfpdLc40%2FKtwDP05qfImDyJLW4hz2ynbNDZTWqF4AaneJub3IA9%2Fm7i%2FykiHzB2krtffJ4IqokXGo7oiUTu6ZyLAvL9ZFisn3JnWy5dis4cl3jEqq3lVFuaQCANmjuaEJV%2FgzX%2B6Jd9MCCyHbptoa9DsHkdjVQeJ5rWKHLyhz4Kxy2ZC9Dc0n6vL1qR%2BOXBx%2Bmllk3X84f4ziiG6KQ4z%2BH%2BmS12L%2B4PCYUCT878j7asFqxZcpCMO6EGDorMKFQmPPsGGG790UstNS9A7dMNkHNizrygcNHEIt3B2d3xprSXWMrTiDzUlkW0m%2Fkdf1G95jBasxU91c%2Bx9B8Dpo%2Bp%2BMYKG%2Fgfps1C%2FyKo3dV4KFzZWRxMR%2FoTiLIqZvkpZWqFgOEEHgclkv9ZIF1W6KgjHdy6tDvNKiFVr7s1WW7BjBL%2FRqfJ8wsBMFAxJr3PdMuNfkqFnamtviuKh2ctj08hNmArLxBeLXDbu7VmBGWJlFsf5B6g9B%2FXWHFm9H7aZ2F7uIAvSV94hPEPT899Bm40N3SpXwjLRHNOKqcz6RVXvJAinmlBEVyem%2BQdzPLwijQMPipuDiQHJxU9L1Jsgi%2Bzng7%2BLyg9QIoXUggIFlTFoW%2Biv7M3C4YPi6InhmO1a%2Ff6BoaKb8UIUw8YeAzAY6pgHwgbbXYmqMmtqNddcAQsHDPmWSXnOwoeVrZOqOUvTcxWa9pgMast1RL8jnW1ygiWhripDxyUJRxumLu%2F9ItJt6u0z3mIyEqyns5GttsYrYyQUSXKflJrlON4oQm1paHl72ymBxKeM4d5iZvDuOQ6WPItuILbeWoWWuiVTEkwmQABcA3Q%2FQDtHN2ews66%2FWehQNxD1EOhheX3q4Q2678aoD4neBtCyA&X-Amz-Signature=462a139ea06aedcef3a6747c821204c58248b266a5bf7d33eedf699150930100&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6AIIPDZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPz261PwK4sdVWGKU5hQnifBlkbNNPhaWLo20Z4dmV8AiBht9ArqsuQNYlm6CD7qZKCk0tQctra67juc9VMzwDvByqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgyGbm2YJfpdLc40%2FKtwDP05qfImDyJLW4hz2ynbNDZTWqF4AaneJub3IA9%2Fm7i%2FykiHzB2krtffJ4IqokXGo7oiUTu6ZyLAvL9ZFisn3JnWy5dis4cl3jEqq3lVFuaQCANmjuaEJV%2FgzX%2B6Jd9MCCyHbptoa9DsHkdjVQeJ5rWKHLyhz4Kxy2ZC9Dc0n6vL1qR%2BOXBx%2Bmllk3X84f4ziiG6KQ4z%2BH%2BmS12L%2B4PCYUCT878j7asFqxZcpCMO6EGDorMKFQmPPsGGG790UstNS9A7dMNkHNizrygcNHEIt3B2d3xprSXWMrTiDzUlkW0m%2Fkdf1G95jBasxU91c%2Bx9B8Dpo%2Bp%2BMYKG%2Fgfps1C%2FyKo3dV4KFzZWRxMR%2FoTiLIqZvkpZWqFgOEEHgclkv9ZIF1W6KgjHdy6tDvNKiFVr7s1WW7BjBL%2FRqfJ8wsBMFAxJr3PdMuNfkqFnamtviuKh2ctj08hNmArLxBeLXDbu7VmBGWJlFsf5B6g9B%2FXWHFm9H7aZ2F7uIAvSV94hPEPT899Bm40N3SpXwjLRHNOKqcz6RVXvJAinmlBEVyem%2BQdzPLwijQMPipuDiQHJxU9L1Jsgi%2Bzng7%2BLyg9QIoXUggIFlTFoW%2Biv7M3C4YPi6InhmO1a%2Ff6BoaKb8UIUw8YeAzAY6pgHwgbbXYmqMmtqNddcAQsHDPmWSXnOwoeVrZOqOUvTcxWa9pgMast1RL8jnW1ygiWhripDxyUJRxumLu%2F9ItJt6u0z3mIyEqyns5GttsYrYyQUSXKflJrlON4oQm1paHl72ymBxKeM4d5iZvDuOQ6WPItuILbeWoWWuiVTEkwmQABcA3Q%2FQDtHN2ews66%2FWehQNxD1EOhheX3q4Q2678aoD4neBtCyA&X-Amz-Signature=2f518968f66e4e966ac8cccdab9b4e0ed5dd3084a1dff949dde5b5f8af20757e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6AIIPDZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPz261PwK4sdVWGKU5hQnifBlkbNNPhaWLo20Z4dmV8AiBht9ArqsuQNYlm6CD7qZKCk0tQctra67juc9VMzwDvByqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgyGbm2YJfpdLc40%2FKtwDP05qfImDyJLW4hz2ynbNDZTWqF4AaneJub3IA9%2Fm7i%2FykiHzB2krtffJ4IqokXGo7oiUTu6ZyLAvL9ZFisn3JnWy5dis4cl3jEqq3lVFuaQCANmjuaEJV%2FgzX%2B6Jd9MCCyHbptoa9DsHkdjVQeJ5rWKHLyhz4Kxy2ZC9Dc0n6vL1qR%2BOXBx%2Bmllk3X84f4ziiG6KQ4z%2BH%2BmS12L%2B4PCYUCT878j7asFqxZcpCMO6EGDorMKFQmPPsGGG790UstNS9A7dMNkHNizrygcNHEIt3B2d3xprSXWMrTiDzUlkW0m%2Fkdf1G95jBasxU91c%2Bx9B8Dpo%2Bp%2BMYKG%2Fgfps1C%2FyKo3dV4KFzZWRxMR%2FoTiLIqZvkpZWqFgOEEHgclkv9ZIF1W6KgjHdy6tDvNKiFVr7s1WW7BjBL%2FRqfJ8wsBMFAxJr3PdMuNfkqFnamtviuKh2ctj08hNmArLxBeLXDbu7VmBGWJlFsf5B6g9B%2FXWHFm9H7aZ2F7uIAvSV94hPEPT899Bm40N3SpXwjLRHNOKqcz6RVXvJAinmlBEVyem%2BQdzPLwijQMPipuDiQHJxU9L1Jsgi%2Bzng7%2BLyg9QIoXUggIFlTFoW%2Biv7M3C4YPi6InhmO1a%2Ff6BoaKb8UIUw8YeAzAY6pgHwgbbXYmqMmtqNddcAQsHDPmWSXnOwoeVrZOqOUvTcxWa9pgMast1RL8jnW1ygiWhripDxyUJRxumLu%2F9ItJt6u0z3mIyEqyns5GttsYrYyQUSXKflJrlON4oQm1paHl72ymBxKeM4d5iZvDuOQ6WPItuILbeWoWWuiVTEkwmQABcA3Q%2FQDtHN2ews66%2FWehQNxD1EOhheX3q4Q2678aoD4neBtCyA&X-Amz-Signature=c94c8a61020b6da332079d4449224346f0e6c887057401c6862c5cc9459b169b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6AIIPDZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPz261PwK4sdVWGKU5hQnifBlkbNNPhaWLo20Z4dmV8AiBht9ArqsuQNYlm6CD7qZKCk0tQctra67juc9VMzwDvByqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgyGbm2YJfpdLc40%2FKtwDP05qfImDyJLW4hz2ynbNDZTWqF4AaneJub3IA9%2Fm7i%2FykiHzB2krtffJ4IqokXGo7oiUTu6ZyLAvL9ZFisn3JnWy5dis4cl3jEqq3lVFuaQCANmjuaEJV%2FgzX%2B6Jd9MCCyHbptoa9DsHkdjVQeJ5rWKHLyhz4Kxy2ZC9Dc0n6vL1qR%2BOXBx%2Bmllk3X84f4ziiG6KQ4z%2BH%2BmS12L%2B4PCYUCT878j7asFqxZcpCMO6EGDorMKFQmPPsGGG790UstNS9A7dMNkHNizrygcNHEIt3B2d3xprSXWMrTiDzUlkW0m%2Fkdf1G95jBasxU91c%2Bx9B8Dpo%2Bp%2BMYKG%2Fgfps1C%2FyKo3dV4KFzZWRxMR%2FoTiLIqZvkpZWqFgOEEHgclkv9ZIF1W6KgjHdy6tDvNKiFVr7s1WW7BjBL%2FRqfJ8wsBMFAxJr3PdMuNfkqFnamtviuKh2ctj08hNmArLxBeLXDbu7VmBGWJlFsf5B6g9B%2FXWHFm9H7aZ2F7uIAvSV94hPEPT899Bm40N3SpXwjLRHNOKqcz6RVXvJAinmlBEVyem%2BQdzPLwijQMPipuDiQHJxU9L1Jsgi%2Bzng7%2BLyg9QIoXUggIFlTFoW%2Biv7M3C4YPi6InhmO1a%2Ff6BoaKb8UIUw8YeAzAY6pgHwgbbXYmqMmtqNddcAQsHDPmWSXnOwoeVrZOqOUvTcxWa9pgMast1RL8jnW1ygiWhripDxyUJRxumLu%2F9ItJt6u0z3mIyEqyns5GttsYrYyQUSXKflJrlON4oQm1paHl72ymBxKeM4d5iZvDuOQ6WPItuILbeWoWWuiVTEkwmQABcA3Q%2FQDtHN2ews66%2FWehQNxD1EOhheX3q4Q2678aoD4neBtCyA&X-Amz-Signature=ab8d3bd0a9650958a7730a43cf6db4871a40d751c9bc6943e294978b504ddb1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6AIIPDZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPz261PwK4sdVWGKU5hQnifBlkbNNPhaWLo20Z4dmV8AiBht9ArqsuQNYlm6CD7qZKCk0tQctra67juc9VMzwDvByqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgyGbm2YJfpdLc40%2FKtwDP05qfImDyJLW4hz2ynbNDZTWqF4AaneJub3IA9%2Fm7i%2FykiHzB2krtffJ4IqokXGo7oiUTu6ZyLAvL9ZFisn3JnWy5dis4cl3jEqq3lVFuaQCANmjuaEJV%2FgzX%2B6Jd9MCCyHbptoa9DsHkdjVQeJ5rWKHLyhz4Kxy2ZC9Dc0n6vL1qR%2BOXBx%2Bmllk3X84f4ziiG6KQ4z%2BH%2BmS12L%2B4PCYUCT878j7asFqxZcpCMO6EGDorMKFQmPPsGGG790UstNS9A7dMNkHNizrygcNHEIt3B2d3xprSXWMrTiDzUlkW0m%2Fkdf1G95jBasxU91c%2Bx9B8Dpo%2Bp%2BMYKG%2Fgfps1C%2FyKo3dV4KFzZWRxMR%2FoTiLIqZvkpZWqFgOEEHgclkv9ZIF1W6KgjHdy6tDvNKiFVr7s1WW7BjBL%2FRqfJ8wsBMFAxJr3PdMuNfkqFnamtviuKh2ctj08hNmArLxBeLXDbu7VmBGWJlFsf5B6g9B%2FXWHFm9H7aZ2F7uIAvSV94hPEPT899Bm40N3SpXwjLRHNOKqcz6RVXvJAinmlBEVyem%2BQdzPLwijQMPipuDiQHJxU9L1Jsgi%2Bzng7%2BLyg9QIoXUggIFlTFoW%2Biv7M3C4YPi6InhmO1a%2Ff6BoaKb8UIUw8YeAzAY6pgHwgbbXYmqMmtqNddcAQsHDPmWSXnOwoeVrZOqOUvTcxWa9pgMast1RL8jnW1ygiWhripDxyUJRxumLu%2F9ItJt6u0z3mIyEqyns5GttsYrYyQUSXKflJrlON4oQm1paHl72ymBxKeM4d5iZvDuOQ6WPItuILbeWoWWuiVTEkwmQABcA3Q%2FQDtHN2ews66%2FWehQNxD1EOhheX3q4Q2678aoD4neBtCyA&X-Amz-Signature=b4e4d3666ab1d44226aa2cc9d3ac6da59f51ffaf9f332fd20088659ba098bf80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6AIIPDZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPz261PwK4sdVWGKU5hQnifBlkbNNPhaWLo20Z4dmV8AiBht9ArqsuQNYlm6CD7qZKCk0tQctra67juc9VMzwDvByqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgyGbm2YJfpdLc40%2FKtwDP05qfImDyJLW4hz2ynbNDZTWqF4AaneJub3IA9%2Fm7i%2FykiHzB2krtffJ4IqokXGo7oiUTu6ZyLAvL9ZFisn3JnWy5dis4cl3jEqq3lVFuaQCANmjuaEJV%2FgzX%2B6Jd9MCCyHbptoa9DsHkdjVQeJ5rWKHLyhz4Kxy2ZC9Dc0n6vL1qR%2BOXBx%2Bmllk3X84f4ziiG6KQ4z%2BH%2BmS12L%2B4PCYUCT878j7asFqxZcpCMO6EGDorMKFQmPPsGGG790UstNS9A7dMNkHNizrygcNHEIt3B2d3xprSXWMrTiDzUlkW0m%2Fkdf1G95jBasxU91c%2Bx9B8Dpo%2Bp%2BMYKG%2Fgfps1C%2FyKo3dV4KFzZWRxMR%2FoTiLIqZvkpZWqFgOEEHgclkv9ZIF1W6KgjHdy6tDvNKiFVr7s1WW7BjBL%2FRqfJ8wsBMFAxJr3PdMuNfkqFnamtviuKh2ctj08hNmArLxBeLXDbu7VmBGWJlFsf5B6g9B%2FXWHFm9H7aZ2F7uIAvSV94hPEPT899Bm40N3SpXwjLRHNOKqcz6RVXvJAinmlBEVyem%2BQdzPLwijQMPipuDiQHJxU9L1Jsgi%2Bzng7%2BLyg9QIoXUggIFlTFoW%2Biv7M3C4YPi6InhmO1a%2Ff6BoaKb8UIUw8YeAzAY6pgHwgbbXYmqMmtqNddcAQsHDPmWSXnOwoeVrZOqOUvTcxWa9pgMast1RL8jnW1ygiWhripDxyUJRxumLu%2F9ItJt6u0z3mIyEqyns5GttsYrYyQUSXKflJrlON4oQm1paHl72ymBxKeM4d5iZvDuOQ6WPItuILbeWoWWuiVTEkwmQABcA3Q%2FQDtHN2ews66%2FWehQNxD1EOhheX3q4Q2678aoD4neBtCyA&X-Amz-Signature=ad8b7f61c92138c19127879718bb485f289fd3a9a58e260d0cdc2fc353cf0ecd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6AIIPDZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPz261PwK4sdVWGKU5hQnifBlkbNNPhaWLo20Z4dmV8AiBht9ArqsuQNYlm6CD7qZKCk0tQctra67juc9VMzwDvByqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgyGbm2YJfpdLc40%2FKtwDP05qfImDyJLW4hz2ynbNDZTWqF4AaneJub3IA9%2Fm7i%2FykiHzB2krtffJ4IqokXGo7oiUTu6ZyLAvL9ZFisn3JnWy5dis4cl3jEqq3lVFuaQCANmjuaEJV%2FgzX%2B6Jd9MCCyHbptoa9DsHkdjVQeJ5rWKHLyhz4Kxy2ZC9Dc0n6vL1qR%2BOXBx%2Bmllk3X84f4ziiG6KQ4z%2BH%2BmS12L%2B4PCYUCT878j7asFqxZcpCMO6EGDorMKFQmPPsGGG790UstNS9A7dMNkHNizrygcNHEIt3B2d3xprSXWMrTiDzUlkW0m%2Fkdf1G95jBasxU91c%2Bx9B8Dpo%2Bp%2BMYKG%2Fgfps1C%2FyKo3dV4KFzZWRxMR%2FoTiLIqZvkpZWqFgOEEHgclkv9ZIF1W6KgjHdy6tDvNKiFVr7s1WW7BjBL%2FRqfJ8wsBMFAxJr3PdMuNfkqFnamtviuKh2ctj08hNmArLxBeLXDbu7VmBGWJlFsf5B6g9B%2FXWHFm9H7aZ2F7uIAvSV94hPEPT899Bm40N3SpXwjLRHNOKqcz6RVXvJAinmlBEVyem%2BQdzPLwijQMPipuDiQHJxU9L1Jsgi%2Bzng7%2BLyg9QIoXUggIFlTFoW%2Biv7M3C4YPi6InhmO1a%2Ff6BoaKb8UIUw8YeAzAY6pgHwgbbXYmqMmtqNddcAQsHDPmWSXnOwoeVrZOqOUvTcxWa9pgMast1RL8jnW1ygiWhripDxyUJRxumLu%2F9ItJt6u0z3mIyEqyns5GttsYrYyQUSXKflJrlON4oQm1paHl72ymBxKeM4d5iZvDuOQ6WPItuILbeWoWWuiVTEkwmQABcA3Q%2FQDtHN2ews66%2FWehQNxD1EOhheX3q4Q2678aoD4neBtCyA&X-Amz-Signature=6cf2ed3f753f6f3077bdcad374159b487c7a60cbfd4f87b87275038922ae48bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6AIIPDZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPz261PwK4sdVWGKU5hQnifBlkbNNPhaWLo20Z4dmV8AiBht9ArqsuQNYlm6CD7qZKCk0tQctra67juc9VMzwDvByqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgyGbm2YJfpdLc40%2FKtwDP05qfImDyJLW4hz2ynbNDZTWqF4AaneJub3IA9%2Fm7i%2FykiHzB2krtffJ4IqokXGo7oiUTu6ZyLAvL9ZFisn3JnWy5dis4cl3jEqq3lVFuaQCANmjuaEJV%2FgzX%2B6Jd9MCCyHbptoa9DsHkdjVQeJ5rWKHLyhz4Kxy2ZC9Dc0n6vL1qR%2BOXBx%2Bmllk3X84f4ziiG6KQ4z%2BH%2BmS12L%2B4PCYUCT878j7asFqxZcpCMO6EGDorMKFQmPPsGGG790UstNS9A7dMNkHNizrygcNHEIt3B2d3xprSXWMrTiDzUlkW0m%2Fkdf1G95jBasxU91c%2Bx9B8Dpo%2Bp%2BMYKG%2Fgfps1C%2FyKo3dV4KFzZWRxMR%2FoTiLIqZvkpZWqFgOEEHgclkv9ZIF1W6KgjHdy6tDvNKiFVr7s1WW7BjBL%2FRqfJ8wsBMFAxJr3PdMuNfkqFnamtviuKh2ctj08hNmArLxBeLXDbu7VmBGWJlFsf5B6g9B%2FXWHFm9H7aZ2F7uIAvSV94hPEPT899Bm40N3SpXwjLRHNOKqcz6RVXvJAinmlBEVyem%2BQdzPLwijQMPipuDiQHJxU9L1Jsgi%2Bzng7%2BLyg9QIoXUggIFlTFoW%2Biv7M3C4YPi6InhmO1a%2Ff6BoaKb8UIUw8YeAzAY6pgHwgbbXYmqMmtqNddcAQsHDPmWSXnOwoeVrZOqOUvTcxWa9pgMast1RL8jnW1ygiWhripDxyUJRxumLu%2F9ItJt6u0z3mIyEqyns5GttsYrYyQUSXKflJrlON4oQm1paHl72ymBxKeM4d5iZvDuOQ6WPItuILbeWoWWuiVTEkwmQABcA3Q%2FQDtHN2ews66%2FWehQNxD1EOhheX3q4Q2678aoD4neBtCyA&X-Amz-Signature=0e8d1a871e6dd5cba95606d6f65bbe0f931f6a8763ad81690d10d07ca15e8e4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6AIIPDZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPz261PwK4sdVWGKU5hQnifBlkbNNPhaWLo20Z4dmV8AiBht9ArqsuQNYlm6CD7qZKCk0tQctra67juc9VMzwDvByqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgyGbm2YJfpdLc40%2FKtwDP05qfImDyJLW4hz2ynbNDZTWqF4AaneJub3IA9%2Fm7i%2FykiHzB2krtffJ4IqokXGo7oiUTu6ZyLAvL9ZFisn3JnWy5dis4cl3jEqq3lVFuaQCANmjuaEJV%2FgzX%2B6Jd9MCCyHbptoa9DsHkdjVQeJ5rWKHLyhz4Kxy2ZC9Dc0n6vL1qR%2BOXBx%2Bmllk3X84f4ziiG6KQ4z%2BH%2BmS12L%2B4PCYUCT878j7asFqxZcpCMO6EGDorMKFQmPPsGGG790UstNS9A7dMNkHNizrygcNHEIt3B2d3xprSXWMrTiDzUlkW0m%2Fkdf1G95jBasxU91c%2Bx9B8Dpo%2Bp%2BMYKG%2Fgfps1C%2FyKo3dV4KFzZWRxMR%2FoTiLIqZvkpZWqFgOEEHgclkv9ZIF1W6KgjHdy6tDvNKiFVr7s1WW7BjBL%2FRqfJ8wsBMFAxJr3PdMuNfkqFnamtviuKh2ctj08hNmArLxBeLXDbu7VmBGWJlFsf5B6g9B%2FXWHFm9H7aZ2F7uIAvSV94hPEPT899Bm40N3SpXwjLRHNOKqcz6RVXvJAinmlBEVyem%2BQdzPLwijQMPipuDiQHJxU9L1Jsgi%2Bzng7%2BLyg9QIoXUggIFlTFoW%2Biv7M3C4YPi6InhmO1a%2Ff6BoaKb8UIUw8YeAzAY6pgHwgbbXYmqMmtqNddcAQsHDPmWSXnOwoeVrZOqOUvTcxWa9pgMast1RL8jnW1ygiWhripDxyUJRxumLu%2F9ItJt6u0z3mIyEqyns5GttsYrYyQUSXKflJrlON4oQm1paHl72ymBxKeM4d5iZvDuOQ6WPItuILbeWoWWuiVTEkwmQABcA3Q%2FQDtHN2ews66%2FWehQNxD1EOhheX3q4Q2678aoD4neBtCyA&X-Amz-Signature=bd0605d296e3b32a9a1128ba6e904120cbe2b348b68e045e61d0b20481e08d85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6AIIPDZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPz261PwK4sdVWGKU5hQnifBlkbNNPhaWLo20Z4dmV8AiBht9ArqsuQNYlm6CD7qZKCk0tQctra67juc9VMzwDvByqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgyGbm2YJfpdLc40%2FKtwDP05qfImDyJLW4hz2ynbNDZTWqF4AaneJub3IA9%2Fm7i%2FykiHzB2krtffJ4IqokXGo7oiUTu6ZyLAvL9ZFisn3JnWy5dis4cl3jEqq3lVFuaQCANmjuaEJV%2FgzX%2B6Jd9MCCyHbptoa9DsHkdjVQeJ5rWKHLyhz4Kxy2ZC9Dc0n6vL1qR%2BOXBx%2Bmllk3X84f4ziiG6KQ4z%2BH%2BmS12L%2B4PCYUCT878j7asFqxZcpCMO6EGDorMKFQmPPsGGG790UstNS9A7dMNkHNizrygcNHEIt3B2d3xprSXWMrTiDzUlkW0m%2Fkdf1G95jBasxU91c%2Bx9B8Dpo%2Bp%2BMYKG%2Fgfps1C%2FyKo3dV4KFzZWRxMR%2FoTiLIqZvkpZWqFgOEEHgclkv9ZIF1W6KgjHdy6tDvNKiFVr7s1WW7BjBL%2FRqfJ8wsBMFAxJr3PdMuNfkqFnamtviuKh2ctj08hNmArLxBeLXDbu7VmBGWJlFsf5B6g9B%2FXWHFm9H7aZ2F7uIAvSV94hPEPT899Bm40N3SpXwjLRHNOKqcz6RVXvJAinmlBEVyem%2BQdzPLwijQMPipuDiQHJxU9L1Jsgi%2Bzng7%2BLyg9QIoXUggIFlTFoW%2Biv7M3C4YPi6InhmO1a%2Ff6BoaKb8UIUw8YeAzAY6pgHwgbbXYmqMmtqNddcAQsHDPmWSXnOwoeVrZOqOUvTcxWa9pgMast1RL8jnW1ygiWhripDxyUJRxumLu%2F9ItJt6u0z3mIyEqyns5GttsYrYyQUSXKflJrlON4oQm1paHl72ymBxKeM4d5iZvDuOQ6WPItuILbeWoWWuiVTEkwmQABcA3Q%2FQDtHN2ews66%2FWehQNxD1EOhheX3q4Q2678aoD4neBtCyA&X-Amz-Signature=a58b098cb20adeff842217bd696b88d2b1d11c633c1706a0f8b9f1406244ff9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

