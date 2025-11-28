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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LKOKGIN%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmo%2FFEB%2FLsht%2B7HSo4kTXopHXoUXe6sRebZgs81PBIEAiEA6nXrNg9%2B0gWa6MtJROk89oz6WossKCPxjnJyJG%2F%2B5hUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECkGi09PcuqMBlRNyrcA5w6pdLb5IdrbmKn%2BvqVKRVdbH6CYNMFFNX3NWxAw6cmXwdt5skJLE05bhiBIRctYP05CBiGbdDCf43%2BS2BEb%2BV2iEUSwbwIKxcFrHZwRmcNEiTQvqJDMqE%2F8XsKTds3majDciVhyEererOSIQMVujNqWTwWZ0sLQUEOR3C23aTD3GdZiEKDJqa1PXK5QEBNS5IpJYB7XMXQYRsgjzbI4U2cyX6T5xAXLnYh8Bl3Ymza21v76Vs3Ag0aBEWNf%2FyVlhwljaAq%2BeXL4OAF%2FSDMwknOvQDZOgIN%2Fm8hsZRTix44pH5K3r0F2UXiSRAjrujJL5Ql6vsWknWCwim%2FKoGVof8I1eH4z3c4%2FUKJXhJ%2FolOZCwWDUAE%2Brmkyza9awYW1IoYuNihGFAt3wk1Pci%2FESCtM8gQmwYJTx8VhiePZOkK97YaFXHQ%2BRSTAH1X5Lzyw9LXYzhgwYdOde8JDJr0wby8iH3byF%2B8gLe5VDLzCxfRzDEjxZ2f8SKcsjU1OgYAdPQiyEwbAmh7FKLnDJSnRx3QoUF2Bi8VRIhWM7SL%2F6nbQlWMAefgLeG3DvVKGODMka1UDjzLtwb%2FlbLtbT0KbuBRsiNiAB65CPvzi%2Ba1t6qCYsM648N2Pz9a1gf88MMj4o8kGOqUBUdPNXORydoLyxO0u4R%2Fj0JLKVhA9bh7l8Zcg0ZKJmY3VHo%2FJ2Ev0geYhBeiz98Bsdqd0wVQwLUTiIriZqXQ%2FK8y9KnrjypRoet699YHU4ZS%2FzPIr%2BzqOw8Ktlb3bLL4jmDH%2F76sJ73GMxuFMWiXgeOzHvfGk%2BJOVP%2BLzgG8U2QDH5omCMU8%2BbFIl2eEdll1QCU9Krd%2FTyCC%2BAAgngCiXWkw1Od02&X-Amz-Signature=498d15a7783ce56e32a6236eda6c51e8c9831a53f225a83c334d5a1eb41dc4b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LKOKGIN%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmo%2FFEB%2FLsht%2B7HSo4kTXopHXoUXe6sRebZgs81PBIEAiEA6nXrNg9%2B0gWa6MtJROk89oz6WossKCPxjnJyJG%2F%2B5hUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECkGi09PcuqMBlRNyrcA5w6pdLb5IdrbmKn%2BvqVKRVdbH6CYNMFFNX3NWxAw6cmXwdt5skJLE05bhiBIRctYP05CBiGbdDCf43%2BS2BEb%2BV2iEUSwbwIKxcFrHZwRmcNEiTQvqJDMqE%2F8XsKTds3majDciVhyEererOSIQMVujNqWTwWZ0sLQUEOR3C23aTD3GdZiEKDJqa1PXK5QEBNS5IpJYB7XMXQYRsgjzbI4U2cyX6T5xAXLnYh8Bl3Ymza21v76Vs3Ag0aBEWNf%2FyVlhwljaAq%2BeXL4OAF%2FSDMwknOvQDZOgIN%2Fm8hsZRTix44pH5K3r0F2UXiSRAjrujJL5Ql6vsWknWCwim%2FKoGVof8I1eH4z3c4%2FUKJXhJ%2FolOZCwWDUAE%2Brmkyza9awYW1IoYuNihGFAt3wk1Pci%2FESCtM8gQmwYJTx8VhiePZOkK97YaFXHQ%2BRSTAH1X5Lzyw9LXYzhgwYdOde8JDJr0wby8iH3byF%2B8gLe5VDLzCxfRzDEjxZ2f8SKcsjU1OgYAdPQiyEwbAmh7FKLnDJSnRx3QoUF2Bi8VRIhWM7SL%2F6nbQlWMAefgLeG3DvVKGODMka1UDjzLtwb%2FlbLtbT0KbuBRsiNiAB65CPvzi%2Ba1t6qCYsM648N2Pz9a1gf88MMj4o8kGOqUBUdPNXORydoLyxO0u4R%2Fj0JLKVhA9bh7l8Zcg0ZKJmY3VHo%2FJ2Ev0geYhBeiz98Bsdqd0wVQwLUTiIriZqXQ%2FK8y9KnrjypRoet699YHU4ZS%2FzPIr%2BzqOw8Ktlb3bLL4jmDH%2F76sJ73GMxuFMWiXgeOzHvfGk%2BJOVP%2BLzgG8U2QDH5omCMU8%2BbFIl2eEdll1QCU9Krd%2FTyCC%2BAAgngCiXWkw1Od02&X-Amz-Signature=5deff2013c150c618bd5884c416aef8aa3f21cad374aa5f850cf711a4a6a87ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LKOKGIN%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmo%2FFEB%2FLsht%2B7HSo4kTXopHXoUXe6sRebZgs81PBIEAiEA6nXrNg9%2B0gWa6MtJROk89oz6WossKCPxjnJyJG%2F%2B5hUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECkGi09PcuqMBlRNyrcA5w6pdLb5IdrbmKn%2BvqVKRVdbH6CYNMFFNX3NWxAw6cmXwdt5skJLE05bhiBIRctYP05CBiGbdDCf43%2BS2BEb%2BV2iEUSwbwIKxcFrHZwRmcNEiTQvqJDMqE%2F8XsKTds3majDciVhyEererOSIQMVujNqWTwWZ0sLQUEOR3C23aTD3GdZiEKDJqa1PXK5QEBNS5IpJYB7XMXQYRsgjzbI4U2cyX6T5xAXLnYh8Bl3Ymza21v76Vs3Ag0aBEWNf%2FyVlhwljaAq%2BeXL4OAF%2FSDMwknOvQDZOgIN%2Fm8hsZRTix44pH5K3r0F2UXiSRAjrujJL5Ql6vsWknWCwim%2FKoGVof8I1eH4z3c4%2FUKJXhJ%2FolOZCwWDUAE%2Brmkyza9awYW1IoYuNihGFAt3wk1Pci%2FESCtM8gQmwYJTx8VhiePZOkK97YaFXHQ%2BRSTAH1X5Lzyw9LXYzhgwYdOde8JDJr0wby8iH3byF%2B8gLe5VDLzCxfRzDEjxZ2f8SKcsjU1OgYAdPQiyEwbAmh7FKLnDJSnRx3QoUF2Bi8VRIhWM7SL%2F6nbQlWMAefgLeG3DvVKGODMka1UDjzLtwb%2FlbLtbT0KbuBRsiNiAB65CPvzi%2Ba1t6qCYsM648N2Pz9a1gf88MMj4o8kGOqUBUdPNXORydoLyxO0u4R%2Fj0JLKVhA9bh7l8Zcg0ZKJmY3VHo%2FJ2Ev0geYhBeiz98Bsdqd0wVQwLUTiIriZqXQ%2FK8y9KnrjypRoet699YHU4ZS%2FzPIr%2BzqOw8Ktlb3bLL4jmDH%2F76sJ73GMxuFMWiXgeOzHvfGk%2BJOVP%2BLzgG8U2QDH5omCMU8%2BbFIl2eEdll1QCU9Krd%2FTyCC%2BAAgngCiXWkw1Od02&X-Amz-Signature=5603c651f162777c842943281c68aa2774c97a38be5c9b80ccb6648dfd76a9fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LKOKGIN%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmo%2FFEB%2FLsht%2B7HSo4kTXopHXoUXe6sRebZgs81PBIEAiEA6nXrNg9%2B0gWa6MtJROk89oz6WossKCPxjnJyJG%2F%2B5hUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECkGi09PcuqMBlRNyrcA5w6pdLb5IdrbmKn%2BvqVKRVdbH6CYNMFFNX3NWxAw6cmXwdt5skJLE05bhiBIRctYP05CBiGbdDCf43%2BS2BEb%2BV2iEUSwbwIKxcFrHZwRmcNEiTQvqJDMqE%2F8XsKTds3majDciVhyEererOSIQMVujNqWTwWZ0sLQUEOR3C23aTD3GdZiEKDJqa1PXK5QEBNS5IpJYB7XMXQYRsgjzbI4U2cyX6T5xAXLnYh8Bl3Ymza21v76Vs3Ag0aBEWNf%2FyVlhwljaAq%2BeXL4OAF%2FSDMwknOvQDZOgIN%2Fm8hsZRTix44pH5K3r0F2UXiSRAjrujJL5Ql6vsWknWCwim%2FKoGVof8I1eH4z3c4%2FUKJXhJ%2FolOZCwWDUAE%2Brmkyza9awYW1IoYuNihGFAt3wk1Pci%2FESCtM8gQmwYJTx8VhiePZOkK97YaFXHQ%2BRSTAH1X5Lzyw9LXYzhgwYdOde8JDJr0wby8iH3byF%2B8gLe5VDLzCxfRzDEjxZ2f8SKcsjU1OgYAdPQiyEwbAmh7FKLnDJSnRx3QoUF2Bi8VRIhWM7SL%2F6nbQlWMAefgLeG3DvVKGODMka1UDjzLtwb%2FlbLtbT0KbuBRsiNiAB65CPvzi%2Ba1t6qCYsM648N2Pz9a1gf88MMj4o8kGOqUBUdPNXORydoLyxO0u4R%2Fj0JLKVhA9bh7l8Zcg0ZKJmY3VHo%2FJ2Ev0geYhBeiz98Bsdqd0wVQwLUTiIriZqXQ%2FK8y9KnrjypRoet699YHU4ZS%2FzPIr%2BzqOw8Ktlb3bLL4jmDH%2F76sJ73GMxuFMWiXgeOzHvfGk%2BJOVP%2BLzgG8U2QDH5omCMU8%2BbFIl2eEdll1QCU9Krd%2FTyCC%2BAAgngCiXWkw1Od02&X-Amz-Signature=bd87fd89c09e31f9ad5c7cbda914744b6d5fb5fec4430a5961405e95300b0109&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LKOKGIN%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmo%2FFEB%2FLsht%2B7HSo4kTXopHXoUXe6sRebZgs81PBIEAiEA6nXrNg9%2B0gWa6MtJROk89oz6WossKCPxjnJyJG%2F%2B5hUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECkGi09PcuqMBlRNyrcA5w6pdLb5IdrbmKn%2BvqVKRVdbH6CYNMFFNX3NWxAw6cmXwdt5skJLE05bhiBIRctYP05CBiGbdDCf43%2BS2BEb%2BV2iEUSwbwIKxcFrHZwRmcNEiTQvqJDMqE%2F8XsKTds3majDciVhyEererOSIQMVujNqWTwWZ0sLQUEOR3C23aTD3GdZiEKDJqa1PXK5QEBNS5IpJYB7XMXQYRsgjzbI4U2cyX6T5xAXLnYh8Bl3Ymza21v76Vs3Ag0aBEWNf%2FyVlhwljaAq%2BeXL4OAF%2FSDMwknOvQDZOgIN%2Fm8hsZRTix44pH5K3r0F2UXiSRAjrujJL5Ql6vsWknWCwim%2FKoGVof8I1eH4z3c4%2FUKJXhJ%2FolOZCwWDUAE%2Brmkyza9awYW1IoYuNihGFAt3wk1Pci%2FESCtM8gQmwYJTx8VhiePZOkK97YaFXHQ%2BRSTAH1X5Lzyw9LXYzhgwYdOde8JDJr0wby8iH3byF%2B8gLe5VDLzCxfRzDEjxZ2f8SKcsjU1OgYAdPQiyEwbAmh7FKLnDJSnRx3QoUF2Bi8VRIhWM7SL%2F6nbQlWMAefgLeG3DvVKGODMka1UDjzLtwb%2FlbLtbT0KbuBRsiNiAB65CPvzi%2Ba1t6qCYsM648N2Pz9a1gf88MMj4o8kGOqUBUdPNXORydoLyxO0u4R%2Fj0JLKVhA9bh7l8Zcg0ZKJmY3VHo%2FJ2Ev0geYhBeiz98Bsdqd0wVQwLUTiIriZqXQ%2FK8y9KnrjypRoet699YHU4ZS%2FzPIr%2BzqOw8Ktlb3bLL4jmDH%2F76sJ73GMxuFMWiXgeOzHvfGk%2BJOVP%2BLzgG8U2QDH5omCMU8%2BbFIl2eEdll1QCU9Krd%2FTyCC%2BAAgngCiXWkw1Od02&X-Amz-Signature=0341816e5910a64746f6859c90888ac7ae088d26e0d2b9fa2c8eb858a108c807&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LKOKGIN%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmo%2FFEB%2FLsht%2B7HSo4kTXopHXoUXe6sRebZgs81PBIEAiEA6nXrNg9%2B0gWa6MtJROk89oz6WossKCPxjnJyJG%2F%2B5hUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECkGi09PcuqMBlRNyrcA5w6pdLb5IdrbmKn%2BvqVKRVdbH6CYNMFFNX3NWxAw6cmXwdt5skJLE05bhiBIRctYP05CBiGbdDCf43%2BS2BEb%2BV2iEUSwbwIKxcFrHZwRmcNEiTQvqJDMqE%2F8XsKTds3majDciVhyEererOSIQMVujNqWTwWZ0sLQUEOR3C23aTD3GdZiEKDJqa1PXK5QEBNS5IpJYB7XMXQYRsgjzbI4U2cyX6T5xAXLnYh8Bl3Ymza21v76Vs3Ag0aBEWNf%2FyVlhwljaAq%2BeXL4OAF%2FSDMwknOvQDZOgIN%2Fm8hsZRTix44pH5K3r0F2UXiSRAjrujJL5Ql6vsWknWCwim%2FKoGVof8I1eH4z3c4%2FUKJXhJ%2FolOZCwWDUAE%2Brmkyza9awYW1IoYuNihGFAt3wk1Pci%2FESCtM8gQmwYJTx8VhiePZOkK97YaFXHQ%2BRSTAH1X5Lzyw9LXYzhgwYdOde8JDJr0wby8iH3byF%2B8gLe5VDLzCxfRzDEjxZ2f8SKcsjU1OgYAdPQiyEwbAmh7FKLnDJSnRx3QoUF2Bi8VRIhWM7SL%2F6nbQlWMAefgLeG3DvVKGODMka1UDjzLtwb%2FlbLtbT0KbuBRsiNiAB65CPvzi%2Ba1t6qCYsM648N2Pz9a1gf88MMj4o8kGOqUBUdPNXORydoLyxO0u4R%2Fj0JLKVhA9bh7l8Zcg0ZKJmY3VHo%2FJ2Ev0geYhBeiz98Bsdqd0wVQwLUTiIriZqXQ%2FK8y9KnrjypRoet699YHU4ZS%2FzPIr%2BzqOw8Ktlb3bLL4jmDH%2F76sJ73GMxuFMWiXgeOzHvfGk%2BJOVP%2BLzgG8U2QDH5omCMU8%2BbFIl2eEdll1QCU9Krd%2FTyCC%2BAAgngCiXWkw1Od02&X-Amz-Signature=b67b24d7018b31a06ac7f2533d34e425db521102f702c79b59cc7e49dfd0d792&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LKOKGIN%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmo%2FFEB%2FLsht%2B7HSo4kTXopHXoUXe6sRebZgs81PBIEAiEA6nXrNg9%2B0gWa6MtJROk89oz6WossKCPxjnJyJG%2F%2B5hUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECkGi09PcuqMBlRNyrcA5w6pdLb5IdrbmKn%2BvqVKRVdbH6CYNMFFNX3NWxAw6cmXwdt5skJLE05bhiBIRctYP05CBiGbdDCf43%2BS2BEb%2BV2iEUSwbwIKxcFrHZwRmcNEiTQvqJDMqE%2F8XsKTds3majDciVhyEererOSIQMVujNqWTwWZ0sLQUEOR3C23aTD3GdZiEKDJqa1PXK5QEBNS5IpJYB7XMXQYRsgjzbI4U2cyX6T5xAXLnYh8Bl3Ymza21v76Vs3Ag0aBEWNf%2FyVlhwljaAq%2BeXL4OAF%2FSDMwknOvQDZOgIN%2Fm8hsZRTix44pH5K3r0F2UXiSRAjrujJL5Ql6vsWknWCwim%2FKoGVof8I1eH4z3c4%2FUKJXhJ%2FolOZCwWDUAE%2Brmkyza9awYW1IoYuNihGFAt3wk1Pci%2FESCtM8gQmwYJTx8VhiePZOkK97YaFXHQ%2BRSTAH1X5Lzyw9LXYzhgwYdOde8JDJr0wby8iH3byF%2B8gLe5VDLzCxfRzDEjxZ2f8SKcsjU1OgYAdPQiyEwbAmh7FKLnDJSnRx3QoUF2Bi8VRIhWM7SL%2F6nbQlWMAefgLeG3DvVKGODMka1UDjzLtwb%2FlbLtbT0KbuBRsiNiAB65CPvzi%2Ba1t6qCYsM648N2Pz9a1gf88MMj4o8kGOqUBUdPNXORydoLyxO0u4R%2Fj0JLKVhA9bh7l8Zcg0ZKJmY3VHo%2FJ2Ev0geYhBeiz98Bsdqd0wVQwLUTiIriZqXQ%2FK8y9KnrjypRoet699YHU4ZS%2FzPIr%2BzqOw8Ktlb3bLL4jmDH%2F76sJ73GMxuFMWiXgeOzHvfGk%2BJOVP%2BLzgG8U2QDH5omCMU8%2BbFIl2eEdll1QCU9Krd%2FTyCC%2BAAgngCiXWkw1Od02&X-Amz-Signature=548b7f0f25f30dcdc396dfe4be7f4c554bc5e025d6f91cc2a9fc69eb92eabd8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LKOKGIN%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmo%2FFEB%2FLsht%2B7HSo4kTXopHXoUXe6sRebZgs81PBIEAiEA6nXrNg9%2B0gWa6MtJROk89oz6WossKCPxjnJyJG%2F%2B5hUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECkGi09PcuqMBlRNyrcA5w6pdLb5IdrbmKn%2BvqVKRVdbH6CYNMFFNX3NWxAw6cmXwdt5skJLE05bhiBIRctYP05CBiGbdDCf43%2BS2BEb%2BV2iEUSwbwIKxcFrHZwRmcNEiTQvqJDMqE%2F8XsKTds3majDciVhyEererOSIQMVujNqWTwWZ0sLQUEOR3C23aTD3GdZiEKDJqa1PXK5QEBNS5IpJYB7XMXQYRsgjzbI4U2cyX6T5xAXLnYh8Bl3Ymza21v76Vs3Ag0aBEWNf%2FyVlhwljaAq%2BeXL4OAF%2FSDMwknOvQDZOgIN%2Fm8hsZRTix44pH5K3r0F2UXiSRAjrujJL5Ql6vsWknWCwim%2FKoGVof8I1eH4z3c4%2FUKJXhJ%2FolOZCwWDUAE%2Brmkyza9awYW1IoYuNihGFAt3wk1Pci%2FESCtM8gQmwYJTx8VhiePZOkK97YaFXHQ%2BRSTAH1X5Lzyw9LXYzhgwYdOde8JDJr0wby8iH3byF%2B8gLe5VDLzCxfRzDEjxZ2f8SKcsjU1OgYAdPQiyEwbAmh7FKLnDJSnRx3QoUF2Bi8VRIhWM7SL%2F6nbQlWMAefgLeG3DvVKGODMka1UDjzLtwb%2FlbLtbT0KbuBRsiNiAB65CPvzi%2Ba1t6qCYsM648N2Pz9a1gf88MMj4o8kGOqUBUdPNXORydoLyxO0u4R%2Fj0JLKVhA9bh7l8Zcg0ZKJmY3VHo%2FJ2Ev0geYhBeiz98Bsdqd0wVQwLUTiIriZqXQ%2FK8y9KnrjypRoet699YHU4ZS%2FzPIr%2BzqOw8Ktlb3bLL4jmDH%2F76sJ73GMxuFMWiXgeOzHvfGk%2BJOVP%2BLzgG8U2QDH5omCMU8%2BbFIl2eEdll1QCU9Krd%2FTyCC%2BAAgngCiXWkw1Od02&X-Amz-Signature=9dfc704271f5a48f24b8bf8f34e888ebabcaf60a95b3aa71af64e0278faa06ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LKOKGIN%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmo%2FFEB%2FLsht%2B7HSo4kTXopHXoUXe6sRebZgs81PBIEAiEA6nXrNg9%2B0gWa6MtJROk89oz6WossKCPxjnJyJG%2F%2B5hUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECkGi09PcuqMBlRNyrcA5w6pdLb5IdrbmKn%2BvqVKRVdbH6CYNMFFNX3NWxAw6cmXwdt5skJLE05bhiBIRctYP05CBiGbdDCf43%2BS2BEb%2BV2iEUSwbwIKxcFrHZwRmcNEiTQvqJDMqE%2F8XsKTds3majDciVhyEererOSIQMVujNqWTwWZ0sLQUEOR3C23aTD3GdZiEKDJqa1PXK5QEBNS5IpJYB7XMXQYRsgjzbI4U2cyX6T5xAXLnYh8Bl3Ymza21v76Vs3Ag0aBEWNf%2FyVlhwljaAq%2BeXL4OAF%2FSDMwknOvQDZOgIN%2Fm8hsZRTix44pH5K3r0F2UXiSRAjrujJL5Ql6vsWknWCwim%2FKoGVof8I1eH4z3c4%2FUKJXhJ%2FolOZCwWDUAE%2Brmkyza9awYW1IoYuNihGFAt3wk1Pci%2FESCtM8gQmwYJTx8VhiePZOkK97YaFXHQ%2BRSTAH1X5Lzyw9LXYzhgwYdOde8JDJr0wby8iH3byF%2B8gLe5VDLzCxfRzDEjxZ2f8SKcsjU1OgYAdPQiyEwbAmh7FKLnDJSnRx3QoUF2Bi8VRIhWM7SL%2F6nbQlWMAefgLeG3DvVKGODMka1UDjzLtwb%2FlbLtbT0KbuBRsiNiAB65CPvzi%2Ba1t6qCYsM648N2Pz9a1gf88MMj4o8kGOqUBUdPNXORydoLyxO0u4R%2Fj0JLKVhA9bh7l8Zcg0ZKJmY3VHo%2FJ2Ev0geYhBeiz98Bsdqd0wVQwLUTiIriZqXQ%2FK8y9KnrjypRoet699YHU4ZS%2FzPIr%2BzqOw8Ktlb3bLL4jmDH%2F76sJ73GMxuFMWiXgeOzHvfGk%2BJOVP%2BLzgG8U2QDH5omCMU8%2BbFIl2eEdll1QCU9Krd%2FTyCC%2BAAgngCiXWkw1Od02&X-Amz-Signature=77eda277f60c5b492eefffaf7d89d62f0e672c9b81c91bd5c474d3957a666d7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LKOKGIN%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHmo%2FFEB%2FLsht%2B7HSo4kTXopHXoUXe6sRebZgs81PBIEAiEA6nXrNg9%2B0gWa6MtJROk89oz6WossKCPxjnJyJG%2F%2B5hUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECkGi09PcuqMBlRNyrcA5w6pdLb5IdrbmKn%2BvqVKRVdbH6CYNMFFNX3NWxAw6cmXwdt5skJLE05bhiBIRctYP05CBiGbdDCf43%2BS2BEb%2BV2iEUSwbwIKxcFrHZwRmcNEiTQvqJDMqE%2F8XsKTds3majDciVhyEererOSIQMVujNqWTwWZ0sLQUEOR3C23aTD3GdZiEKDJqa1PXK5QEBNS5IpJYB7XMXQYRsgjzbI4U2cyX6T5xAXLnYh8Bl3Ymza21v76Vs3Ag0aBEWNf%2FyVlhwljaAq%2BeXL4OAF%2FSDMwknOvQDZOgIN%2Fm8hsZRTix44pH5K3r0F2UXiSRAjrujJL5Ql6vsWknWCwim%2FKoGVof8I1eH4z3c4%2FUKJXhJ%2FolOZCwWDUAE%2Brmkyza9awYW1IoYuNihGFAt3wk1Pci%2FESCtM8gQmwYJTx8VhiePZOkK97YaFXHQ%2BRSTAH1X5Lzyw9LXYzhgwYdOde8JDJr0wby8iH3byF%2B8gLe5VDLzCxfRzDEjxZ2f8SKcsjU1OgYAdPQiyEwbAmh7FKLnDJSnRx3QoUF2Bi8VRIhWM7SL%2F6nbQlWMAefgLeG3DvVKGODMka1UDjzLtwb%2FlbLtbT0KbuBRsiNiAB65CPvzi%2Ba1t6qCYsM648N2Pz9a1gf88MMj4o8kGOqUBUdPNXORydoLyxO0u4R%2Fj0JLKVhA9bh7l8Zcg0ZKJmY3VHo%2FJ2Ev0geYhBeiz98Bsdqd0wVQwLUTiIriZqXQ%2FK8y9KnrjypRoet699YHU4ZS%2FzPIr%2BzqOw8Ktlb3bLL4jmDH%2F76sJ73GMxuFMWiXgeOzHvfGk%2BJOVP%2BLzgG8U2QDH5omCMU8%2BbFIl2eEdll1QCU9Krd%2FTyCC%2BAAgngCiXWkw1Od02&X-Amz-Signature=340929bbc72b26f612d18fdf745899d1b94fed98806fb5289dabd225529145bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

