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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PITJ6Y4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs2jeQK3IkyvHCCETXJpVsfHgZ9hpvnNP0RwmpqP3WJAiEAgP8OaVU282Md%2BAc0uHtwHIf8hDczG6x%2FTDrqJwgxVWwqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqHoClfi5Xb3IMiKCrcAyolHcQXgXn8Gdl21VMt1Q49Wc1XKYBciQqNihJlR0fXxPt9K9vBphHyxt4RluA9Z0TzlO8NT0fqbJgSKt39RBe1nuqLgtELfbdngY1gxD7XTsZOyQ2P8ku8AEm3l6dtBL3CitGGD7p7J7f%2BEcIxFbHolrEmYZTNzLY3H8n%2BaP8RQifnI4ohFdGyqo9vTxHkDtjwjtrBL0Ng%2BMdkkOiPn6TqpEgIx%2BnZjxcfhZJxuvKMa2vaOlh%2FAAHE43cT3D5bSlfEP%2B1qHU7hdd%2FILq6IqUGAH6cqzdfHjqQY7%2F8b%2F%2BkaQhP1DdF81Vxw7pNhF%2BL9UG7n%2B0MZsKe2Geh5g30titRP3edXDulAvapIgnHvjqhYDZVcjpC7xmw%2BJbCMwyCBGBsq7Qq6itElErfJHYkyzgvZCL%2B50SXeRD9Wx8%2BCXQTKD0cRE8YY2kI%2BRxXRtmPDfS1RCB%2BUU2OrjiBInQ4zybso7XUFkE2KEwWQnNC49cOlnbXbuIrSKuU%2BjFPWlJ06mg3wzZn9%2Fb3tYYcBtoAor%2BeRtmlc1fPZGMO2xI6mo6O9z8%2FTwJtOpDkX%2FmHj4DWYFQbGwqK8mzRICIOc4nVkWu%2F9HlpOUbLpI2q1uZfwq1glHVQIsImyDfIJvDshMJDjksoGOqUBrTWsqlMkLxvYkmcnQ51WRoa%2B%2FkGm4O6z9juqxBSThV0pD6A0YMpvtnA6kAyyF13i3aGSHra8Ar69BgOQtfFAZme%2FH4gYMACQBDrpshjMjftrTNIDIP%2FXEhbXJ7GJJ3c0CQnLAXlXOXdJBae%2FGjztjt5SQe0WBBB535NgJfgnFD0xMJiPat%2FVXG7Hs%2B4Xzmg5y4%2B28UUVgZsck94d88O2XZMGWj%2BQ&X-Amz-Signature=3c658fee98d679649946142dbe807842b16f5fe2afa9fe92d187d8252c3d48c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PITJ6Y4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs2jeQK3IkyvHCCETXJpVsfHgZ9hpvnNP0RwmpqP3WJAiEAgP8OaVU282Md%2BAc0uHtwHIf8hDczG6x%2FTDrqJwgxVWwqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqHoClfi5Xb3IMiKCrcAyolHcQXgXn8Gdl21VMt1Q49Wc1XKYBciQqNihJlR0fXxPt9K9vBphHyxt4RluA9Z0TzlO8NT0fqbJgSKt39RBe1nuqLgtELfbdngY1gxD7XTsZOyQ2P8ku8AEm3l6dtBL3CitGGD7p7J7f%2BEcIxFbHolrEmYZTNzLY3H8n%2BaP8RQifnI4ohFdGyqo9vTxHkDtjwjtrBL0Ng%2BMdkkOiPn6TqpEgIx%2BnZjxcfhZJxuvKMa2vaOlh%2FAAHE43cT3D5bSlfEP%2B1qHU7hdd%2FILq6IqUGAH6cqzdfHjqQY7%2F8b%2F%2BkaQhP1DdF81Vxw7pNhF%2BL9UG7n%2B0MZsKe2Geh5g30titRP3edXDulAvapIgnHvjqhYDZVcjpC7xmw%2BJbCMwyCBGBsq7Qq6itElErfJHYkyzgvZCL%2B50SXeRD9Wx8%2BCXQTKD0cRE8YY2kI%2BRxXRtmPDfS1RCB%2BUU2OrjiBInQ4zybso7XUFkE2KEwWQnNC49cOlnbXbuIrSKuU%2BjFPWlJ06mg3wzZn9%2Fb3tYYcBtoAor%2BeRtmlc1fPZGMO2xI6mo6O9z8%2FTwJtOpDkX%2FmHj4DWYFQbGwqK8mzRICIOc4nVkWu%2F9HlpOUbLpI2q1uZfwq1glHVQIsImyDfIJvDshMJDjksoGOqUBrTWsqlMkLxvYkmcnQ51WRoa%2B%2FkGm4O6z9juqxBSThV0pD6A0YMpvtnA6kAyyF13i3aGSHra8Ar69BgOQtfFAZme%2FH4gYMACQBDrpshjMjftrTNIDIP%2FXEhbXJ7GJJ3c0CQnLAXlXOXdJBae%2FGjztjt5SQe0WBBB535NgJfgnFD0xMJiPat%2FVXG7Hs%2B4Xzmg5y4%2B28UUVgZsck94d88O2XZMGWj%2BQ&X-Amz-Signature=52cc5f015ef24f39cf9f0346e65e4844d5f7b654352ce39d9f828b2e7c7177bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PITJ6Y4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs2jeQK3IkyvHCCETXJpVsfHgZ9hpvnNP0RwmpqP3WJAiEAgP8OaVU282Md%2BAc0uHtwHIf8hDczG6x%2FTDrqJwgxVWwqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqHoClfi5Xb3IMiKCrcAyolHcQXgXn8Gdl21VMt1Q49Wc1XKYBciQqNihJlR0fXxPt9K9vBphHyxt4RluA9Z0TzlO8NT0fqbJgSKt39RBe1nuqLgtELfbdngY1gxD7XTsZOyQ2P8ku8AEm3l6dtBL3CitGGD7p7J7f%2BEcIxFbHolrEmYZTNzLY3H8n%2BaP8RQifnI4ohFdGyqo9vTxHkDtjwjtrBL0Ng%2BMdkkOiPn6TqpEgIx%2BnZjxcfhZJxuvKMa2vaOlh%2FAAHE43cT3D5bSlfEP%2B1qHU7hdd%2FILq6IqUGAH6cqzdfHjqQY7%2F8b%2F%2BkaQhP1DdF81Vxw7pNhF%2BL9UG7n%2B0MZsKe2Geh5g30titRP3edXDulAvapIgnHvjqhYDZVcjpC7xmw%2BJbCMwyCBGBsq7Qq6itElErfJHYkyzgvZCL%2B50SXeRD9Wx8%2BCXQTKD0cRE8YY2kI%2BRxXRtmPDfS1RCB%2BUU2OrjiBInQ4zybso7XUFkE2KEwWQnNC49cOlnbXbuIrSKuU%2BjFPWlJ06mg3wzZn9%2Fb3tYYcBtoAor%2BeRtmlc1fPZGMO2xI6mo6O9z8%2FTwJtOpDkX%2FmHj4DWYFQbGwqK8mzRICIOc4nVkWu%2F9HlpOUbLpI2q1uZfwq1glHVQIsImyDfIJvDshMJDjksoGOqUBrTWsqlMkLxvYkmcnQ51WRoa%2B%2FkGm4O6z9juqxBSThV0pD6A0YMpvtnA6kAyyF13i3aGSHra8Ar69BgOQtfFAZme%2FH4gYMACQBDrpshjMjftrTNIDIP%2FXEhbXJ7GJJ3c0CQnLAXlXOXdJBae%2FGjztjt5SQe0WBBB535NgJfgnFD0xMJiPat%2FVXG7Hs%2B4Xzmg5y4%2B28UUVgZsck94d88O2XZMGWj%2BQ&X-Amz-Signature=4337e27425a99c2007c229fe7eabab032ab10c279beb0b883a608417e65d918f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PITJ6Y4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs2jeQK3IkyvHCCETXJpVsfHgZ9hpvnNP0RwmpqP3WJAiEAgP8OaVU282Md%2BAc0uHtwHIf8hDczG6x%2FTDrqJwgxVWwqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqHoClfi5Xb3IMiKCrcAyolHcQXgXn8Gdl21VMt1Q49Wc1XKYBciQqNihJlR0fXxPt9K9vBphHyxt4RluA9Z0TzlO8NT0fqbJgSKt39RBe1nuqLgtELfbdngY1gxD7XTsZOyQ2P8ku8AEm3l6dtBL3CitGGD7p7J7f%2BEcIxFbHolrEmYZTNzLY3H8n%2BaP8RQifnI4ohFdGyqo9vTxHkDtjwjtrBL0Ng%2BMdkkOiPn6TqpEgIx%2BnZjxcfhZJxuvKMa2vaOlh%2FAAHE43cT3D5bSlfEP%2B1qHU7hdd%2FILq6IqUGAH6cqzdfHjqQY7%2F8b%2F%2BkaQhP1DdF81Vxw7pNhF%2BL9UG7n%2B0MZsKe2Geh5g30titRP3edXDulAvapIgnHvjqhYDZVcjpC7xmw%2BJbCMwyCBGBsq7Qq6itElErfJHYkyzgvZCL%2B50SXeRD9Wx8%2BCXQTKD0cRE8YY2kI%2BRxXRtmPDfS1RCB%2BUU2OrjiBInQ4zybso7XUFkE2KEwWQnNC49cOlnbXbuIrSKuU%2BjFPWlJ06mg3wzZn9%2Fb3tYYcBtoAor%2BeRtmlc1fPZGMO2xI6mo6O9z8%2FTwJtOpDkX%2FmHj4DWYFQbGwqK8mzRICIOc4nVkWu%2F9HlpOUbLpI2q1uZfwq1glHVQIsImyDfIJvDshMJDjksoGOqUBrTWsqlMkLxvYkmcnQ51WRoa%2B%2FkGm4O6z9juqxBSThV0pD6A0YMpvtnA6kAyyF13i3aGSHra8Ar69BgOQtfFAZme%2FH4gYMACQBDrpshjMjftrTNIDIP%2FXEhbXJ7GJJ3c0CQnLAXlXOXdJBae%2FGjztjt5SQe0WBBB535NgJfgnFD0xMJiPat%2FVXG7Hs%2B4Xzmg5y4%2B28UUVgZsck94d88O2XZMGWj%2BQ&X-Amz-Signature=9b65b642f7b411b2c57a87dd4b2b027514d154a9471a08dd32304d3cb4bf4fa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PITJ6Y4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs2jeQK3IkyvHCCETXJpVsfHgZ9hpvnNP0RwmpqP3WJAiEAgP8OaVU282Md%2BAc0uHtwHIf8hDczG6x%2FTDrqJwgxVWwqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqHoClfi5Xb3IMiKCrcAyolHcQXgXn8Gdl21VMt1Q49Wc1XKYBciQqNihJlR0fXxPt9K9vBphHyxt4RluA9Z0TzlO8NT0fqbJgSKt39RBe1nuqLgtELfbdngY1gxD7XTsZOyQ2P8ku8AEm3l6dtBL3CitGGD7p7J7f%2BEcIxFbHolrEmYZTNzLY3H8n%2BaP8RQifnI4ohFdGyqo9vTxHkDtjwjtrBL0Ng%2BMdkkOiPn6TqpEgIx%2BnZjxcfhZJxuvKMa2vaOlh%2FAAHE43cT3D5bSlfEP%2B1qHU7hdd%2FILq6IqUGAH6cqzdfHjqQY7%2F8b%2F%2BkaQhP1DdF81Vxw7pNhF%2BL9UG7n%2B0MZsKe2Geh5g30titRP3edXDulAvapIgnHvjqhYDZVcjpC7xmw%2BJbCMwyCBGBsq7Qq6itElErfJHYkyzgvZCL%2B50SXeRD9Wx8%2BCXQTKD0cRE8YY2kI%2BRxXRtmPDfS1RCB%2BUU2OrjiBInQ4zybso7XUFkE2KEwWQnNC49cOlnbXbuIrSKuU%2BjFPWlJ06mg3wzZn9%2Fb3tYYcBtoAor%2BeRtmlc1fPZGMO2xI6mo6O9z8%2FTwJtOpDkX%2FmHj4DWYFQbGwqK8mzRICIOc4nVkWu%2F9HlpOUbLpI2q1uZfwq1glHVQIsImyDfIJvDshMJDjksoGOqUBrTWsqlMkLxvYkmcnQ51WRoa%2B%2FkGm4O6z9juqxBSThV0pD6A0YMpvtnA6kAyyF13i3aGSHra8Ar69BgOQtfFAZme%2FH4gYMACQBDrpshjMjftrTNIDIP%2FXEhbXJ7GJJ3c0CQnLAXlXOXdJBae%2FGjztjt5SQe0WBBB535NgJfgnFD0xMJiPat%2FVXG7Hs%2B4Xzmg5y4%2B28UUVgZsck94d88O2XZMGWj%2BQ&X-Amz-Signature=519b92c151cadfbdbefa79a6f03799db7ce3879e4efd9a4315fe7260837c96ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PITJ6Y4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs2jeQK3IkyvHCCETXJpVsfHgZ9hpvnNP0RwmpqP3WJAiEAgP8OaVU282Md%2BAc0uHtwHIf8hDczG6x%2FTDrqJwgxVWwqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqHoClfi5Xb3IMiKCrcAyolHcQXgXn8Gdl21VMt1Q49Wc1XKYBciQqNihJlR0fXxPt9K9vBphHyxt4RluA9Z0TzlO8NT0fqbJgSKt39RBe1nuqLgtELfbdngY1gxD7XTsZOyQ2P8ku8AEm3l6dtBL3CitGGD7p7J7f%2BEcIxFbHolrEmYZTNzLY3H8n%2BaP8RQifnI4ohFdGyqo9vTxHkDtjwjtrBL0Ng%2BMdkkOiPn6TqpEgIx%2BnZjxcfhZJxuvKMa2vaOlh%2FAAHE43cT3D5bSlfEP%2B1qHU7hdd%2FILq6IqUGAH6cqzdfHjqQY7%2F8b%2F%2BkaQhP1DdF81Vxw7pNhF%2BL9UG7n%2B0MZsKe2Geh5g30titRP3edXDulAvapIgnHvjqhYDZVcjpC7xmw%2BJbCMwyCBGBsq7Qq6itElErfJHYkyzgvZCL%2B50SXeRD9Wx8%2BCXQTKD0cRE8YY2kI%2BRxXRtmPDfS1RCB%2BUU2OrjiBInQ4zybso7XUFkE2KEwWQnNC49cOlnbXbuIrSKuU%2BjFPWlJ06mg3wzZn9%2Fb3tYYcBtoAor%2BeRtmlc1fPZGMO2xI6mo6O9z8%2FTwJtOpDkX%2FmHj4DWYFQbGwqK8mzRICIOc4nVkWu%2F9HlpOUbLpI2q1uZfwq1glHVQIsImyDfIJvDshMJDjksoGOqUBrTWsqlMkLxvYkmcnQ51WRoa%2B%2FkGm4O6z9juqxBSThV0pD6A0YMpvtnA6kAyyF13i3aGSHra8Ar69BgOQtfFAZme%2FH4gYMACQBDrpshjMjftrTNIDIP%2FXEhbXJ7GJJ3c0CQnLAXlXOXdJBae%2FGjztjt5SQe0WBBB535NgJfgnFD0xMJiPat%2FVXG7Hs%2B4Xzmg5y4%2B28UUVgZsck94d88O2XZMGWj%2BQ&X-Amz-Signature=5d5085a730018cdfbd5d44b070abf700a72b829fd7e51f7f385426eff50e409f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PITJ6Y4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs2jeQK3IkyvHCCETXJpVsfHgZ9hpvnNP0RwmpqP3WJAiEAgP8OaVU282Md%2BAc0uHtwHIf8hDczG6x%2FTDrqJwgxVWwqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqHoClfi5Xb3IMiKCrcAyolHcQXgXn8Gdl21VMt1Q49Wc1XKYBciQqNihJlR0fXxPt9K9vBphHyxt4RluA9Z0TzlO8NT0fqbJgSKt39RBe1nuqLgtELfbdngY1gxD7XTsZOyQ2P8ku8AEm3l6dtBL3CitGGD7p7J7f%2BEcIxFbHolrEmYZTNzLY3H8n%2BaP8RQifnI4ohFdGyqo9vTxHkDtjwjtrBL0Ng%2BMdkkOiPn6TqpEgIx%2BnZjxcfhZJxuvKMa2vaOlh%2FAAHE43cT3D5bSlfEP%2B1qHU7hdd%2FILq6IqUGAH6cqzdfHjqQY7%2F8b%2F%2BkaQhP1DdF81Vxw7pNhF%2BL9UG7n%2B0MZsKe2Geh5g30titRP3edXDulAvapIgnHvjqhYDZVcjpC7xmw%2BJbCMwyCBGBsq7Qq6itElErfJHYkyzgvZCL%2B50SXeRD9Wx8%2BCXQTKD0cRE8YY2kI%2BRxXRtmPDfS1RCB%2BUU2OrjiBInQ4zybso7XUFkE2KEwWQnNC49cOlnbXbuIrSKuU%2BjFPWlJ06mg3wzZn9%2Fb3tYYcBtoAor%2BeRtmlc1fPZGMO2xI6mo6O9z8%2FTwJtOpDkX%2FmHj4DWYFQbGwqK8mzRICIOc4nVkWu%2F9HlpOUbLpI2q1uZfwq1glHVQIsImyDfIJvDshMJDjksoGOqUBrTWsqlMkLxvYkmcnQ51WRoa%2B%2FkGm4O6z9juqxBSThV0pD6A0YMpvtnA6kAyyF13i3aGSHra8Ar69BgOQtfFAZme%2FH4gYMACQBDrpshjMjftrTNIDIP%2FXEhbXJ7GJJ3c0CQnLAXlXOXdJBae%2FGjztjt5SQe0WBBB535NgJfgnFD0xMJiPat%2FVXG7Hs%2B4Xzmg5y4%2B28UUVgZsck94d88O2XZMGWj%2BQ&X-Amz-Signature=52b0ba4045d1bdcb51f2c1e53622b97eab01fac9c234a350e5f0afeb693430f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PITJ6Y4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs2jeQK3IkyvHCCETXJpVsfHgZ9hpvnNP0RwmpqP3WJAiEAgP8OaVU282Md%2BAc0uHtwHIf8hDczG6x%2FTDrqJwgxVWwqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqHoClfi5Xb3IMiKCrcAyolHcQXgXn8Gdl21VMt1Q49Wc1XKYBciQqNihJlR0fXxPt9K9vBphHyxt4RluA9Z0TzlO8NT0fqbJgSKt39RBe1nuqLgtELfbdngY1gxD7XTsZOyQ2P8ku8AEm3l6dtBL3CitGGD7p7J7f%2BEcIxFbHolrEmYZTNzLY3H8n%2BaP8RQifnI4ohFdGyqo9vTxHkDtjwjtrBL0Ng%2BMdkkOiPn6TqpEgIx%2BnZjxcfhZJxuvKMa2vaOlh%2FAAHE43cT3D5bSlfEP%2B1qHU7hdd%2FILq6IqUGAH6cqzdfHjqQY7%2F8b%2F%2BkaQhP1DdF81Vxw7pNhF%2BL9UG7n%2B0MZsKe2Geh5g30titRP3edXDulAvapIgnHvjqhYDZVcjpC7xmw%2BJbCMwyCBGBsq7Qq6itElErfJHYkyzgvZCL%2B50SXeRD9Wx8%2BCXQTKD0cRE8YY2kI%2BRxXRtmPDfS1RCB%2BUU2OrjiBInQ4zybso7XUFkE2KEwWQnNC49cOlnbXbuIrSKuU%2BjFPWlJ06mg3wzZn9%2Fb3tYYcBtoAor%2BeRtmlc1fPZGMO2xI6mo6O9z8%2FTwJtOpDkX%2FmHj4DWYFQbGwqK8mzRICIOc4nVkWu%2F9HlpOUbLpI2q1uZfwq1glHVQIsImyDfIJvDshMJDjksoGOqUBrTWsqlMkLxvYkmcnQ51WRoa%2B%2FkGm4O6z9juqxBSThV0pD6A0YMpvtnA6kAyyF13i3aGSHra8Ar69BgOQtfFAZme%2FH4gYMACQBDrpshjMjftrTNIDIP%2FXEhbXJ7GJJ3c0CQnLAXlXOXdJBae%2FGjztjt5SQe0WBBB535NgJfgnFD0xMJiPat%2FVXG7Hs%2B4Xzmg5y4%2B28UUVgZsck94d88O2XZMGWj%2BQ&X-Amz-Signature=f0ef93781ee556019c836ccd668463ced4ef2954c2ffa02f5102bd331391fb55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PITJ6Y4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs2jeQK3IkyvHCCETXJpVsfHgZ9hpvnNP0RwmpqP3WJAiEAgP8OaVU282Md%2BAc0uHtwHIf8hDczG6x%2FTDrqJwgxVWwqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqHoClfi5Xb3IMiKCrcAyolHcQXgXn8Gdl21VMt1Q49Wc1XKYBciQqNihJlR0fXxPt9K9vBphHyxt4RluA9Z0TzlO8NT0fqbJgSKt39RBe1nuqLgtELfbdngY1gxD7XTsZOyQ2P8ku8AEm3l6dtBL3CitGGD7p7J7f%2BEcIxFbHolrEmYZTNzLY3H8n%2BaP8RQifnI4ohFdGyqo9vTxHkDtjwjtrBL0Ng%2BMdkkOiPn6TqpEgIx%2BnZjxcfhZJxuvKMa2vaOlh%2FAAHE43cT3D5bSlfEP%2B1qHU7hdd%2FILq6IqUGAH6cqzdfHjqQY7%2F8b%2F%2BkaQhP1DdF81Vxw7pNhF%2BL9UG7n%2B0MZsKe2Geh5g30titRP3edXDulAvapIgnHvjqhYDZVcjpC7xmw%2BJbCMwyCBGBsq7Qq6itElErfJHYkyzgvZCL%2B50SXeRD9Wx8%2BCXQTKD0cRE8YY2kI%2BRxXRtmPDfS1RCB%2BUU2OrjiBInQ4zybso7XUFkE2KEwWQnNC49cOlnbXbuIrSKuU%2BjFPWlJ06mg3wzZn9%2Fb3tYYcBtoAor%2BeRtmlc1fPZGMO2xI6mo6O9z8%2FTwJtOpDkX%2FmHj4DWYFQbGwqK8mzRICIOc4nVkWu%2F9HlpOUbLpI2q1uZfwq1glHVQIsImyDfIJvDshMJDjksoGOqUBrTWsqlMkLxvYkmcnQ51WRoa%2B%2FkGm4O6z9juqxBSThV0pD6A0YMpvtnA6kAyyF13i3aGSHra8Ar69BgOQtfFAZme%2FH4gYMACQBDrpshjMjftrTNIDIP%2FXEhbXJ7GJJ3c0CQnLAXlXOXdJBae%2FGjztjt5SQe0WBBB535NgJfgnFD0xMJiPat%2FVXG7Hs%2B4Xzmg5y4%2B28UUVgZsck94d88O2XZMGWj%2BQ&X-Amz-Signature=359418633bc0280f6a921f3246bebbffb31ea0347e3918e7d3fa45f055243fd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PITJ6Y4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs2jeQK3IkyvHCCETXJpVsfHgZ9hpvnNP0RwmpqP3WJAiEAgP8OaVU282Md%2BAc0uHtwHIf8hDczG6x%2FTDrqJwgxVWwqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqHoClfi5Xb3IMiKCrcAyolHcQXgXn8Gdl21VMt1Q49Wc1XKYBciQqNihJlR0fXxPt9K9vBphHyxt4RluA9Z0TzlO8NT0fqbJgSKt39RBe1nuqLgtELfbdngY1gxD7XTsZOyQ2P8ku8AEm3l6dtBL3CitGGD7p7J7f%2BEcIxFbHolrEmYZTNzLY3H8n%2BaP8RQifnI4ohFdGyqo9vTxHkDtjwjtrBL0Ng%2BMdkkOiPn6TqpEgIx%2BnZjxcfhZJxuvKMa2vaOlh%2FAAHE43cT3D5bSlfEP%2B1qHU7hdd%2FILq6IqUGAH6cqzdfHjqQY7%2F8b%2F%2BkaQhP1DdF81Vxw7pNhF%2BL9UG7n%2B0MZsKe2Geh5g30titRP3edXDulAvapIgnHvjqhYDZVcjpC7xmw%2BJbCMwyCBGBsq7Qq6itElErfJHYkyzgvZCL%2B50SXeRD9Wx8%2BCXQTKD0cRE8YY2kI%2BRxXRtmPDfS1RCB%2BUU2OrjiBInQ4zybso7XUFkE2KEwWQnNC49cOlnbXbuIrSKuU%2BjFPWlJ06mg3wzZn9%2Fb3tYYcBtoAor%2BeRtmlc1fPZGMO2xI6mo6O9z8%2FTwJtOpDkX%2FmHj4DWYFQbGwqK8mzRICIOc4nVkWu%2F9HlpOUbLpI2q1uZfwq1glHVQIsImyDfIJvDshMJDjksoGOqUBrTWsqlMkLxvYkmcnQ51WRoa%2B%2FkGm4O6z9juqxBSThV0pD6A0YMpvtnA6kAyyF13i3aGSHra8Ar69BgOQtfFAZme%2FH4gYMACQBDrpshjMjftrTNIDIP%2FXEhbXJ7GJJ3c0CQnLAXlXOXdJBae%2FGjztjt5SQe0WBBB535NgJfgnFD0xMJiPat%2FVXG7Hs%2B4Xzmg5y4%2B28UUVgZsck94d88O2XZMGWj%2BQ&X-Amz-Signature=d708cb2ab6407ae5a56429d53c27e8e83ca9ab79f3df25181d175bdbd96b8195&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

