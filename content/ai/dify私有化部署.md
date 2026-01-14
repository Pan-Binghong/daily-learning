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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2BVLY6%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBASCop9QgXQfLXB9I1rxbx2w4MmpxoJG2NXO%2FPgW3k6AiB86rRFeOkcKuOaAVikZloUViQUE7GRLQsDbaQ%2F2iTZyir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMdWqyYcFkX5h%2BkP0SKtwDWo49%2Fe3L%2BGveU4GmPhcaerT10%2FOPDRu5qIwknLC9T%2F%2BYKLZtmQTR7buxCgla52HeUM4N3YAA8wLaXYaWsrv86wtn6UgwBRkU1cPhT%2BHjkfCp8PC8ZS4nU7KZGqLW6lwyKgiNR%2FiAb9CJWOziY%2BUQm7uonP%2BK2gnhTyq5WKg1UdioM8yVZ75b1Tgcc7tBtyG80bl6B7KpqZaLyvG221Gxg5QnOO%2Ba8RamnvHZoy3ybIhLonwaOh%2BNB%2F92uUWWlZjlARvhogwkptieNBirUmJtHU%2BV%2BXMntLEQwVHEEjm0k9dNI0y6YUlYqufRI6efqWeKAoFuu%2Fn7QBq4WICnz3OzQDYcqhQ14MNn7rJsqWrTukZFJ6tiRCUZNzLcoqnlZh1nFdYXO9RUaMd1QaWKqiOSHbZrUgSknWdCURhHbHmKHxeuqMiJoHni7w7%2FVYTRLKwsZycenIlOHlegxjt3DIzoPNsi4JJ%2Fumj8qY0TdTSYI09Kt8p%2FdNRyGUVLyNcqjnEtEjdHTb0WXG51sot0rR1Dqi2mTsytP%2FXY%2BHxyQchpv92zL4aBQ7PrWh4yTc%2F0jbGkVKib6y0TC67nkuX6h001xXG5q9RmF0IP1ecdvaXhQtu0udFQHSmCcLgkEqAw0o%2BcywY6pgFgerjqxsDZw74mlCHw8h9O0wiMziLnRP4aDLlWrPuLteKWcoi6tVXmW6W6Bz1XDzlrwCoH7bLOUrtyFnIiXls%2B0Zy01fYR09ntrGMVYHDNBUJT5X0i9Fxv76g%2FfNwEUj%2BeywPIQ9bx24GE4ZhoyCzsQjOY%2B2F1l6FO66KT%2F7ezJGQku1U%2BMT%2BeiIgNP%2FbuXKfErc%2BOHqaXWUzegfgUp%2B4h7hBrVos9&X-Amz-Signature=e7a5f2b3ef181ed16181a5d93bf8b6e97709d1476e2b405e55c3d19d659f5066&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2BVLY6%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBASCop9QgXQfLXB9I1rxbx2w4MmpxoJG2NXO%2FPgW3k6AiB86rRFeOkcKuOaAVikZloUViQUE7GRLQsDbaQ%2F2iTZyir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMdWqyYcFkX5h%2BkP0SKtwDWo49%2Fe3L%2BGveU4GmPhcaerT10%2FOPDRu5qIwknLC9T%2F%2BYKLZtmQTR7buxCgla52HeUM4N3YAA8wLaXYaWsrv86wtn6UgwBRkU1cPhT%2BHjkfCp8PC8ZS4nU7KZGqLW6lwyKgiNR%2FiAb9CJWOziY%2BUQm7uonP%2BK2gnhTyq5WKg1UdioM8yVZ75b1Tgcc7tBtyG80bl6B7KpqZaLyvG221Gxg5QnOO%2Ba8RamnvHZoy3ybIhLonwaOh%2BNB%2F92uUWWlZjlARvhogwkptieNBirUmJtHU%2BV%2BXMntLEQwVHEEjm0k9dNI0y6YUlYqufRI6efqWeKAoFuu%2Fn7QBq4WICnz3OzQDYcqhQ14MNn7rJsqWrTukZFJ6tiRCUZNzLcoqnlZh1nFdYXO9RUaMd1QaWKqiOSHbZrUgSknWdCURhHbHmKHxeuqMiJoHni7w7%2FVYTRLKwsZycenIlOHlegxjt3DIzoPNsi4JJ%2Fumj8qY0TdTSYI09Kt8p%2FdNRyGUVLyNcqjnEtEjdHTb0WXG51sot0rR1Dqi2mTsytP%2FXY%2BHxyQchpv92zL4aBQ7PrWh4yTc%2F0jbGkVKib6y0TC67nkuX6h001xXG5q9RmF0IP1ecdvaXhQtu0udFQHSmCcLgkEqAw0o%2BcywY6pgFgerjqxsDZw74mlCHw8h9O0wiMziLnRP4aDLlWrPuLteKWcoi6tVXmW6W6Bz1XDzlrwCoH7bLOUrtyFnIiXls%2B0Zy01fYR09ntrGMVYHDNBUJT5X0i9Fxv76g%2FfNwEUj%2BeywPIQ9bx24GE4ZhoyCzsQjOY%2B2F1l6FO66KT%2F7ezJGQku1U%2BMT%2BeiIgNP%2FbuXKfErc%2BOHqaXWUzegfgUp%2B4h7hBrVos9&X-Amz-Signature=a1720ee648df2af0b65dbd81e2e9f2a4615a4406e1e0d8ff07c3ae650e70e17f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2BVLY6%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBASCop9QgXQfLXB9I1rxbx2w4MmpxoJG2NXO%2FPgW3k6AiB86rRFeOkcKuOaAVikZloUViQUE7GRLQsDbaQ%2F2iTZyir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMdWqyYcFkX5h%2BkP0SKtwDWo49%2Fe3L%2BGveU4GmPhcaerT10%2FOPDRu5qIwknLC9T%2F%2BYKLZtmQTR7buxCgla52HeUM4N3YAA8wLaXYaWsrv86wtn6UgwBRkU1cPhT%2BHjkfCp8PC8ZS4nU7KZGqLW6lwyKgiNR%2FiAb9CJWOziY%2BUQm7uonP%2BK2gnhTyq5WKg1UdioM8yVZ75b1Tgcc7tBtyG80bl6B7KpqZaLyvG221Gxg5QnOO%2Ba8RamnvHZoy3ybIhLonwaOh%2BNB%2F92uUWWlZjlARvhogwkptieNBirUmJtHU%2BV%2BXMntLEQwVHEEjm0k9dNI0y6YUlYqufRI6efqWeKAoFuu%2Fn7QBq4WICnz3OzQDYcqhQ14MNn7rJsqWrTukZFJ6tiRCUZNzLcoqnlZh1nFdYXO9RUaMd1QaWKqiOSHbZrUgSknWdCURhHbHmKHxeuqMiJoHni7w7%2FVYTRLKwsZycenIlOHlegxjt3DIzoPNsi4JJ%2Fumj8qY0TdTSYI09Kt8p%2FdNRyGUVLyNcqjnEtEjdHTb0WXG51sot0rR1Dqi2mTsytP%2FXY%2BHxyQchpv92zL4aBQ7PrWh4yTc%2F0jbGkVKib6y0TC67nkuX6h001xXG5q9RmF0IP1ecdvaXhQtu0udFQHSmCcLgkEqAw0o%2BcywY6pgFgerjqxsDZw74mlCHw8h9O0wiMziLnRP4aDLlWrPuLteKWcoi6tVXmW6W6Bz1XDzlrwCoH7bLOUrtyFnIiXls%2B0Zy01fYR09ntrGMVYHDNBUJT5X0i9Fxv76g%2FfNwEUj%2BeywPIQ9bx24GE4ZhoyCzsQjOY%2B2F1l6FO66KT%2F7ezJGQku1U%2BMT%2BeiIgNP%2FbuXKfErc%2BOHqaXWUzegfgUp%2B4h7hBrVos9&X-Amz-Signature=afdd9eda4f83d8b1401cd1403cb3790c2b3af2e71c1616cdbf63c23fa9ba7510&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2BVLY6%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBASCop9QgXQfLXB9I1rxbx2w4MmpxoJG2NXO%2FPgW3k6AiB86rRFeOkcKuOaAVikZloUViQUE7GRLQsDbaQ%2F2iTZyir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMdWqyYcFkX5h%2BkP0SKtwDWo49%2Fe3L%2BGveU4GmPhcaerT10%2FOPDRu5qIwknLC9T%2F%2BYKLZtmQTR7buxCgla52HeUM4N3YAA8wLaXYaWsrv86wtn6UgwBRkU1cPhT%2BHjkfCp8PC8ZS4nU7KZGqLW6lwyKgiNR%2FiAb9CJWOziY%2BUQm7uonP%2BK2gnhTyq5WKg1UdioM8yVZ75b1Tgcc7tBtyG80bl6B7KpqZaLyvG221Gxg5QnOO%2Ba8RamnvHZoy3ybIhLonwaOh%2BNB%2F92uUWWlZjlARvhogwkptieNBirUmJtHU%2BV%2BXMntLEQwVHEEjm0k9dNI0y6YUlYqufRI6efqWeKAoFuu%2Fn7QBq4WICnz3OzQDYcqhQ14MNn7rJsqWrTukZFJ6tiRCUZNzLcoqnlZh1nFdYXO9RUaMd1QaWKqiOSHbZrUgSknWdCURhHbHmKHxeuqMiJoHni7w7%2FVYTRLKwsZycenIlOHlegxjt3DIzoPNsi4JJ%2Fumj8qY0TdTSYI09Kt8p%2FdNRyGUVLyNcqjnEtEjdHTb0WXG51sot0rR1Dqi2mTsytP%2FXY%2BHxyQchpv92zL4aBQ7PrWh4yTc%2F0jbGkVKib6y0TC67nkuX6h001xXG5q9RmF0IP1ecdvaXhQtu0udFQHSmCcLgkEqAw0o%2BcywY6pgFgerjqxsDZw74mlCHw8h9O0wiMziLnRP4aDLlWrPuLteKWcoi6tVXmW6W6Bz1XDzlrwCoH7bLOUrtyFnIiXls%2B0Zy01fYR09ntrGMVYHDNBUJT5X0i9Fxv76g%2FfNwEUj%2BeywPIQ9bx24GE4ZhoyCzsQjOY%2B2F1l6FO66KT%2F7ezJGQku1U%2BMT%2BeiIgNP%2FbuXKfErc%2BOHqaXWUzegfgUp%2B4h7hBrVos9&X-Amz-Signature=a70b46000943d5e36065629d57e3b02a92ac1fc03fdeb879f6dcb87ae66ce1b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2BVLY6%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBASCop9QgXQfLXB9I1rxbx2w4MmpxoJG2NXO%2FPgW3k6AiB86rRFeOkcKuOaAVikZloUViQUE7GRLQsDbaQ%2F2iTZyir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMdWqyYcFkX5h%2BkP0SKtwDWo49%2Fe3L%2BGveU4GmPhcaerT10%2FOPDRu5qIwknLC9T%2F%2BYKLZtmQTR7buxCgla52HeUM4N3YAA8wLaXYaWsrv86wtn6UgwBRkU1cPhT%2BHjkfCp8PC8ZS4nU7KZGqLW6lwyKgiNR%2FiAb9CJWOziY%2BUQm7uonP%2BK2gnhTyq5WKg1UdioM8yVZ75b1Tgcc7tBtyG80bl6B7KpqZaLyvG221Gxg5QnOO%2Ba8RamnvHZoy3ybIhLonwaOh%2BNB%2F92uUWWlZjlARvhogwkptieNBirUmJtHU%2BV%2BXMntLEQwVHEEjm0k9dNI0y6YUlYqufRI6efqWeKAoFuu%2Fn7QBq4WICnz3OzQDYcqhQ14MNn7rJsqWrTukZFJ6tiRCUZNzLcoqnlZh1nFdYXO9RUaMd1QaWKqiOSHbZrUgSknWdCURhHbHmKHxeuqMiJoHni7w7%2FVYTRLKwsZycenIlOHlegxjt3DIzoPNsi4JJ%2Fumj8qY0TdTSYI09Kt8p%2FdNRyGUVLyNcqjnEtEjdHTb0WXG51sot0rR1Dqi2mTsytP%2FXY%2BHxyQchpv92zL4aBQ7PrWh4yTc%2F0jbGkVKib6y0TC67nkuX6h001xXG5q9RmF0IP1ecdvaXhQtu0udFQHSmCcLgkEqAw0o%2BcywY6pgFgerjqxsDZw74mlCHw8h9O0wiMziLnRP4aDLlWrPuLteKWcoi6tVXmW6W6Bz1XDzlrwCoH7bLOUrtyFnIiXls%2B0Zy01fYR09ntrGMVYHDNBUJT5X0i9Fxv76g%2FfNwEUj%2BeywPIQ9bx24GE4ZhoyCzsQjOY%2B2F1l6FO66KT%2F7ezJGQku1U%2BMT%2BeiIgNP%2FbuXKfErc%2BOHqaXWUzegfgUp%2B4h7hBrVos9&X-Amz-Signature=d1639f06c657f6bc323e01c1a632cc4283620f6e25e902b2ce42837134c044d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2BVLY6%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBASCop9QgXQfLXB9I1rxbx2w4MmpxoJG2NXO%2FPgW3k6AiB86rRFeOkcKuOaAVikZloUViQUE7GRLQsDbaQ%2F2iTZyir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMdWqyYcFkX5h%2BkP0SKtwDWo49%2Fe3L%2BGveU4GmPhcaerT10%2FOPDRu5qIwknLC9T%2F%2BYKLZtmQTR7buxCgla52HeUM4N3YAA8wLaXYaWsrv86wtn6UgwBRkU1cPhT%2BHjkfCp8PC8ZS4nU7KZGqLW6lwyKgiNR%2FiAb9CJWOziY%2BUQm7uonP%2BK2gnhTyq5WKg1UdioM8yVZ75b1Tgcc7tBtyG80bl6B7KpqZaLyvG221Gxg5QnOO%2Ba8RamnvHZoy3ybIhLonwaOh%2BNB%2F92uUWWlZjlARvhogwkptieNBirUmJtHU%2BV%2BXMntLEQwVHEEjm0k9dNI0y6YUlYqufRI6efqWeKAoFuu%2Fn7QBq4WICnz3OzQDYcqhQ14MNn7rJsqWrTukZFJ6tiRCUZNzLcoqnlZh1nFdYXO9RUaMd1QaWKqiOSHbZrUgSknWdCURhHbHmKHxeuqMiJoHni7w7%2FVYTRLKwsZycenIlOHlegxjt3DIzoPNsi4JJ%2Fumj8qY0TdTSYI09Kt8p%2FdNRyGUVLyNcqjnEtEjdHTb0WXG51sot0rR1Dqi2mTsytP%2FXY%2BHxyQchpv92zL4aBQ7PrWh4yTc%2F0jbGkVKib6y0TC67nkuX6h001xXG5q9RmF0IP1ecdvaXhQtu0udFQHSmCcLgkEqAw0o%2BcywY6pgFgerjqxsDZw74mlCHw8h9O0wiMziLnRP4aDLlWrPuLteKWcoi6tVXmW6W6Bz1XDzlrwCoH7bLOUrtyFnIiXls%2B0Zy01fYR09ntrGMVYHDNBUJT5X0i9Fxv76g%2FfNwEUj%2BeywPIQ9bx24GE4ZhoyCzsQjOY%2B2F1l6FO66KT%2F7ezJGQku1U%2BMT%2BeiIgNP%2FbuXKfErc%2BOHqaXWUzegfgUp%2B4h7hBrVos9&X-Amz-Signature=e083d92bc913304e7b3ebc3c10148b4ff351b74b7c44140b67c77269ac66ca31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2BVLY6%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBASCop9QgXQfLXB9I1rxbx2w4MmpxoJG2NXO%2FPgW3k6AiB86rRFeOkcKuOaAVikZloUViQUE7GRLQsDbaQ%2F2iTZyir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMdWqyYcFkX5h%2BkP0SKtwDWo49%2Fe3L%2BGveU4GmPhcaerT10%2FOPDRu5qIwknLC9T%2F%2BYKLZtmQTR7buxCgla52HeUM4N3YAA8wLaXYaWsrv86wtn6UgwBRkU1cPhT%2BHjkfCp8PC8ZS4nU7KZGqLW6lwyKgiNR%2FiAb9CJWOziY%2BUQm7uonP%2BK2gnhTyq5WKg1UdioM8yVZ75b1Tgcc7tBtyG80bl6B7KpqZaLyvG221Gxg5QnOO%2Ba8RamnvHZoy3ybIhLonwaOh%2BNB%2F92uUWWlZjlARvhogwkptieNBirUmJtHU%2BV%2BXMntLEQwVHEEjm0k9dNI0y6YUlYqufRI6efqWeKAoFuu%2Fn7QBq4WICnz3OzQDYcqhQ14MNn7rJsqWrTukZFJ6tiRCUZNzLcoqnlZh1nFdYXO9RUaMd1QaWKqiOSHbZrUgSknWdCURhHbHmKHxeuqMiJoHni7w7%2FVYTRLKwsZycenIlOHlegxjt3DIzoPNsi4JJ%2Fumj8qY0TdTSYI09Kt8p%2FdNRyGUVLyNcqjnEtEjdHTb0WXG51sot0rR1Dqi2mTsytP%2FXY%2BHxyQchpv92zL4aBQ7PrWh4yTc%2F0jbGkVKib6y0TC67nkuX6h001xXG5q9RmF0IP1ecdvaXhQtu0udFQHSmCcLgkEqAw0o%2BcywY6pgFgerjqxsDZw74mlCHw8h9O0wiMziLnRP4aDLlWrPuLteKWcoi6tVXmW6W6Bz1XDzlrwCoH7bLOUrtyFnIiXls%2B0Zy01fYR09ntrGMVYHDNBUJT5X0i9Fxv76g%2FfNwEUj%2BeywPIQ9bx24GE4ZhoyCzsQjOY%2B2F1l6FO66KT%2F7ezJGQku1U%2BMT%2BeiIgNP%2FbuXKfErc%2BOHqaXWUzegfgUp%2B4h7hBrVos9&X-Amz-Signature=f8b5bfd1920ecec77c475349e8e7e4c6884d7fd2ff80b45c64592642cdc58998&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2BVLY6%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBASCop9QgXQfLXB9I1rxbx2w4MmpxoJG2NXO%2FPgW3k6AiB86rRFeOkcKuOaAVikZloUViQUE7GRLQsDbaQ%2F2iTZyir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMdWqyYcFkX5h%2BkP0SKtwDWo49%2Fe3L%2BGveU4GmPhcaerT10%2FOPDRu5qIwknLC9T%2F%2BYKLZtmQTR7buxCgla52HeUM4N3YAA8wLaXYaWsrv86wtn6UgwBRkU1cPhT%2BHjkfCp8PC8ZS4nU7KZGqLW6lwyKgiNR%2FiAb9CJWOziY%2BUQm7uonP%2BK2gnhTyq5WKg1UdioM8yVZ75b1Tgcc7tBtyG80bl6B7KpqZaLyvG221Gxg5QnOO%2Ba8RamnvHZoy3ybIhLonwaOh%2BNB%2F92uUWWlZjlARvhogwkptieNBirUmJtHU%2BV%2BXMntLEQwVHEEjm0k9dNI0y6YUlYqufRI6efqWeKAoFuu%2Fn7QBq4WICnz3OzQDYcqhQ14MNn7rJsqWrTukZFJ6tiRCUZNzLcoqnlZh1nFdYXO9RUaMd1QaWKqiOSHbZrUgSknWdCURhHbHmKHxeuqMiJoHni7w7%2FVYTRLKwsZycenIlOHlegxjt3DIzoPNsi4JJ%2Fumj8qY0TdTSYI09Kt8p%2FdNRyGUVLyNcqjnEtEjdHTb0WXG51sot0rR1Dqi2mTsytP%2FXY%2BHxyQchpv92zL4aBQ7PrWh4yTc%2F0jbGkVKib6y0TC67nkuX6h001xXG5q9RmF0IP1ecdvaXhQtu0udFQHSmCcLgkEqAw0o%2BcywY6pgFgerjqxsDZw74mlCHw8h9O0wiMziLnRP4aDLlWrPuLteKWcoi6tVXmW6W6Bz1XDzlrwCoH7bLOUrtyFnIiXls%2B0Zy01fYR09ntrGMVYHDNBUJT5X0i9Fxv76g%2FfNwEUj%2BeywPIQ9bx24GE4ZhoyCzsQjOY%2B2F1l6FO66KT%2F7ezJGQku1U%2BMT%2BeiIgNP%2FbuXKfErc%2BOHqaXWUzegfgUp%2B4h7hBrVos9&X-Amz-Signature=82c930e492eaad1521157356d357bc7b0c66efd2c8f81d4d4e23723d3c081ab6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2BVLY6%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBASCop9QgXQfLXB9I1rxbx2w4MmpxoJG2NXO%2FPgW3k6AiB86rRFeOkcKuOaAVikZloUViQUE7GRLQsDbaQ%2F2iTZyir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMdWqyYcFkX5h%2BkP0SKtwDWo49%2Fe3L%2BGveU4GmPhcaerT10%2FOPDRu5qIwknLC9T%2F%2BYKLZtmQTR7buxCgla52HeUM4N3YAA8wLaXYaWsrv86wtn6UgwBRkU1cPhT%2BHjkfCp8PC8ZS4nU7KZGqLW6lwyKgiNR%2FiAb9CJWOziY%2BUQm7uonP%2BK2gnhTyq5WKg1UdioM8yVZ75b1Tgcc7tBtyG80bl6B7KpqZaLyvG221Gxg5QnOO%2Ba8RamnvHZoy3ybIhLonwaOh%2BNB%2F92uUWWlZjlARvhogwkptieNBirUmJtHU%2BV%2BXMntLEQwVHEEjm0k9dNI0y6YUlYqufRI6efqWeKAoFuu%2Fn7QBq4WICnz3OzQDYcqhQ14MNn7rJsqWrTukZFJ6tiRCUZNzLcoqnlZh1nFdYXO9RUaMd1QaWKqiOSHbZrUgSknWdCURhHbHmKHxeuqMiJoHni7w7%2FVYTRLKwsZycenIlOHlegxjt3DIzoPNsi4JJ%2Fumj8qY0TdTSYI09Kt8p%2FdNRyGUVLyNcqjnEtEjdHTb0WXG51sot0rR1Dqi2mTsytP%2FXY%2BHxyQchpv92zL4aBQ7PrWh4yTc%2F0jbGkVKib6y0TC67nkuX6h001xXG5q9RmF0IP1ecdvaXhQtu0udFQHSmCcLgkEqAw0o%2BcywY6pgFgerjqxsDZw74mlCHw8h9O0wiMziLnRP4aDLlWrPuLteKWcoi6tVXmW6W6Bz1XDzlrwCoH7bLOUrtyFnIiXls%2B0Zy01fYR09ntrGMVYHDNBUJT5X0i9Fxv76g%2FfNwEUj%2BeywPIQ9bx24GE4ZhoyCzsQjOY%2B2F1l6FO66KT%2F7ezJGQku1U%2BMT%2BeiIgNP%2FbuXKfErc%2BOHqaXWUzegfgUp%2B4h7hBrVos9&X-Amz-Signature=130438e4b78ad3544b46cbfd7ee27080a99c92010227979c867514370013a24f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR2BVLY6%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBASCop9QgXQfLXB9I1rxbx2w4MmpxoJG2NXO%2FPgW3k6AiB86rRFeOkcKuOaAVikZloUViQUE7GRLQsDbaQ%2F2iTZyir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMdWqyYcFkX5h%2BkP0SKtwDWo49%2Fe3L%2BGveU4GmPhcaerT10%2FOPDRu5qIwknLC9T%2F%2BYKLZtmQTR7buxCgla52HeUM4N3YAA8wLaXYaWsrv86wtn6UgwBRkU1cPhT%2BHjkfCp8PC8ZS4nU7KZGqLW6lwyKgiNR%2FiAb9CJWOziY%2BUQm7uonP%2BK2gnhTyq5WKg1UdioM8yVZ75b1Tgcc7tBtyG80bl6B7KpqZaLyvG221Gxg5QnOO%2Ba8RamnvHZoy3ybIhLonwaOh%2BNB%2F92uUWWlZjlARvhogwkptieNBirUmJtHU%2BV%2BXMntLEQwVHEEjm0k9dNI0y6YUlYqufRI6efqWeKAoFuu%2Fn7QBq4WICnz3OzQDYcqhQ14MNn7rJsqWrTukZFJ6tiRCUZNzLcoqnlZh1nFdYXO9RUaMd1QaWKqiOSHbZrUgSknWdCURhHbHmKHxeuqMiJoHni7w7%2FVYTRLKwsZycenIlOHlegxjt3DIzoPNsi4JJ%2Fumj8qY0TdTSYI09Kt8p%2FdNRyGUVLyNcqjnEtEjdHTb0WXG51sot0rR1Dqi2mTsytP%2FXY%2BHxyQchpv92zL4aBQ7PrWh4yTc%2F0jbGkVKib6y0TC67nkuX6h001xXG5q9RmF0IP1ecdvaXhQtu0udFQHSmCcLgkEqAw0o%2BcywY6pgFgerjqxsDZw74mlCHw8h9O0wiMziLnRP4aDLlWrPuLteKWcoi6tVXmW6W6Bz1XDzlrwCoH7bLOUrtyFnIiXls%2B0Zy01fYR09ntrGMVYHDNBUJT5X0i9Fxv76g%2FfNwEUj%2BeywPIQ9bx24GE4ZhoyCzsQjOY%2B2F1l6FO66KT%2F7ezJGQku1U%2BMT%2BeiIgNP%2FbuXKfErc%2BOHqaXWUzegfgUp%2B4h7hBrVos9&X-Amz-Signature=4f6d665d4eab03d394f7accbe59f0f78738bb42e3c3810113daf9a3f6f54a089&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

