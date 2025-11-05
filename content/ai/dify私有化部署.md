---
title: Dify私有化部署
date: '2024-11-15T09:08:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- Dify
categories:
- AI
---

# 1.创建服务器准备工作

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FAR5MXN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxpyljLqXDSxFU1dShY%2B7J31NiZE547mNG1OOPU4GRpAiA4%2FjImqfw%2BuNNl0I3P%2FNzC8kW7GYicDU%2Fldu6s4HlWBCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5TuiEsT5yM8y%2BvZVKtwDtGntONrf5Wiz1m0tpZ8jLB%2FQIOGgggxniS%2Fh9Mw7nodTN5HmcsuxhCKum2S3CwhCy6hQIzISf0svw%2FV4s6x5hYTXZLKjym8T%2BG5X4ebZakFtMMbBxs0qpPfTfRDM8wCpiWEELy9VfU76aMqQlxIMPEEZ%2FyF37KHqYeR8WTrV7QaDK2ptdPVLle5HGGilKk5B6BagiMEfJ0R5LzCYVzlocRNNE2B1aP%2FA8D1SSqwMfF7xBwlyo5aQuNxNLEQZJ%2BKK3B7ttNByopO2zE5HvobXP5z4TA91q2hqMXDmsjcN58akTRoS5hfJdYaGe2K1eB4pjsJH1jdwQwIhUAImUEewICefnoc%2FuG2spc0DvLtzocvr%2FcdgUP617nlYR5%2F7yhwndkaGKJcMH6R6yAbOapV1btvXtqwDeVn7sXavBexQ9zeJcylAWn9mk8oM5UemwuR01HFnxvz2p9L8xB2GzOnDURHRzxe0IB%2FjEXNL9n3pHo5BafIiORlcbyVxbuV38rvyEVQD6JVQScn7x%2BkOD1HHvtsKJSSI7SggMAvIvyuMQ99SGS6TNxH4Uyc4YTQVOrFszl9eB2xEaqp8do7jwNpHkyXiPSAQlwhSl52PgxHDI18tlgBX4Dg6n4lU5Jgwx6KsyAY6pgENsxdmT2aEs3AryOQiHreAdTNVpaoiowRh54LwNfmQUHbGr%2F3AH5Irml2BZ8x6%2FbVbzQ2v%2Bpm%2BPSkx7DTzX637yxdcfKIyGltV4AFum1CdJRA5ectfdVggDflAeUMXXqf1VDB7oxWhWD3MbRlRG7aWuH7PV6Df05%2FU0U%2BPajcuCuEp7AVQ8Nhk1R6GMAJtDg6xhdlQWEt%2FlFofhqb48QhN6H20o0Db&X-Amz-Signature=1accece1f2ba822bcc05c92dfa43703b338c5d9348520763d71a87eb9bad5da7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FAR5MXN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxpyljLqXDSxFU1dShY%2B7J31NiZE547mNG1OOPU4GRpAiA4%2FjImqfw%2BuNNl0I3P%2FNzC8kW7GYicDU%2Fldu6s4HlWBCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5TuiEsT5yM8y%2BvZVKtwDtGntONrf5Wiz1m0tpZ8jLB%2FQIOGgggxniS%2Fh9Mw7nodTN5HmcsuxhCKum2S3CwhCy6hQIzISf0svw%2FV4s6x5hYTXZLKjym8T%2BG5X4ebZakFtMMbBxs0qpPfTfRDM8wCpiWEELy9VfU76aMqQlxIMPEEZ%2FyF37KHqYeR8WTrV7QaDK2ptdPVLle5HGGilKk5B6BagiMEfJ0R5LzCYVzlocRNNE2B1aP%2FA8D1SSqwMfF7xBwlyo5aQuNxNLEQZJ%2BKK3B7ttNByopO2zE5HvobXP5z4TA91q2hqMXDmsjcN58akTRoS5hfJdYaGe2K1eB4pjsJH1jdwQwIhUAImUEewICefnoc%2FuG2spc0DvLtzocvr%2FcdgUP617nlYR5%2F7yhwndkaGKJcMH6R6yAbOapV1btvXtqwDeVn7sXavBexQ9zeJcylAWn9mk8oM5UemwuR01HFnxvz2p9L8xB2GzOnDURHRzxe0IB%2FjEXNL9n3pHo5BafIiORlcbyVxbuV38rvyEVQD6JVQScn7x%2BkOD1HHvtsKJSSI7SggMAvIvyuMQ99SGS6TNxH4Uyc4YTQVOrFszl9eB2xEaqp8do7jwNpHkyXiPSAQlwhSl52PgxHDI18tlgBX4Dg6n4lU5Jgwx6KsyAY6pgENsxdmT2aEs3AryOQiHreAdTNVpaoiowRh54LwNfmQUHbGr%2F3AH5Irml2BZ8x6%2FbVbzQ2v%2Bpm%2BPSkx7DTzX637yxdcfKIyGltV4AFum1CdJRA5ectfdVggDflAeUMXXqf1VDB7oxWhWD3MbRlRG7aWuH7PV6Df05%2FU0U%2BPajcuCuEp7AVQ8Nhk1R6GMAJtDg6xhdlQWEt%2FlFofhqb48QhN6H20o0Db&X-Amz-Signature=14d3e28a3149cb5112d8a25b52fc86e09d9a5921d8775f1d067368f95a55605d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FAR5MXN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxpyljLqXDSxFU1dShY%2B7J31NiZE547mNG1OOPU4GRpAiA4%2FjImqfw%2BuNNl0I3P%2FNzC8kW7GYicDU%2Fldu6s4HlWBCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5TuiEsT5yM8y%2BvZVKtwDtGntONrf5Wiz1m0tpZ8jLB%2FQIOGgggxniS%2Fh9Mw7nodTN5HmcsuxhCKum2S3CwhCy6hQIzISf0svw%2FV4s6x5hYTXZLKjym8T%2BG5X4ebZakFtMMbBxs0qpPfTfRDM8wCpiWEELy9VfU76aMqQlxIMPEEZ%2FyF37KHqYeR8WTrV7QaDK2ptdPVLle5HGGilKk5B6BagiMEfJ0R5LzCYVzlocRNNE2B1aP%2FA8D1SSqwMfF7xBwlyo5aQuNxNLEQZJ%2BKK3B7ttNByopO2zE5HvobXP5z4TA91q2hqMXDmsjcN58akTRoS5hfJdYaGe2K1eB4pjsJH1jdwQwIhUAImUEewICefnoc%2FuG2spc0DvLtzocvr%2FcdgUP617nlYR5%2F7yhwndkaGKJcMH6R6yAbOapV1btvXtqwDeVn7sXavBexQ9zeJcylAWn9mk8oM5UemwuR01HFnxvz2p9L8xB2GzOnDURHRzxe0IB%2FjEXNL9n3pHo5BafIiORlcbyVxbuV38rvyEVQD6JVQScn7x%2BkOD1HHvtsKJSSI7SggMAvIvyuMQ99SGS6TNxH4Uyc4YTQVOrFszl9eB2xEaqp8do7jwNpHkyXiPSAQlwhSl52PgxHDI18tlgBX4Dg6n4lU5Jgwx6KsyAY6pgENsxdmT2aEs3AryOQiHreAdTNVpaoiowRh54LwNfmQUHbGr%2F3AH5Irml2BZ8x6%2FbVbzQ2v%2Bpm%2BPSkx7DTzX637yxdcfKIyGltV4AFum1CdJRA5ectfdVggDflAeUMXXqf1VDB7oxWhWD3MbRlRG7aWuH7PV6Df05%2FU0U%2BPajcuCuEp7AVQ8Nhk1R6GMAJtDg6xhdlQWEt%2FlFofhqb48QhN6H20o0Db&X-Amz-Signature=13f8cce7d2a1ec2d9bcf07f60e8ba20929fee60f376acc6fd9e68b3164709b69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FAR5MXN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxpyljLqXDSxFU1dShY%2B7J31NiZE547mNG1OOPU4GRpAiA4%2FjImqfw%2BuNNl0I3P%2FNzC8kW7GYicDU%2Fldu6s4HlWBCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5TuiEsT5yM8y%2BvZVKtwDtGntONrf5Wiz1m0tpZ8jLB%2FQIOGgggxniS%2Fh9Mw7nodTN5HmcsuxhCKum2S3CwhCy6hQIzISf0svw%2FV4s6x5hYTXZLKjym8T%2BG5X4ebZakFtMMbBxs0qpPfTfRDM8wCpiWEELy9VfU76aMqQlxIMPEEZ%2FyF37KHqYeR8WTrV7QaDK2ptdPVLle5HGGilKk5B6BagiMEfJ0R5LzCYVzlocRNNE2B1aP%2FA8D1SSqwMfF7xBwlyo5aQuNxNLEQZJ%2BKK3B7ttNByopO2zE5HvobXP5z4TA91q2hqMXDmsjcN58akTRoS5hfJdYaGe2K1eB4pjsJH1jdwQwIhUAImUEewICefnoc%2FuG2spc0DvLtzocvr%2FcdgUP617nlYR5%2F7yhwndkaGKJcMH6R6yAbOapV1btvXtqwDeVn7sXavBexQ9zeJcylAWn9mk8oM5UemwuR01HFnxvz2p9L8xB2GzOnDURHRzxe0IB%2FjEXNL9n3pHo5BafIiORlcbyVxbuV38rvyEVQD6JVQScn7x%2BkOD1HHvtsKJSSI7SggMAvIvyuMQ99SGS6TNxH4Uyc4YTQVOrFszl9eB2xEaqp8do7jwNpHkyXiPSAQlwhSl52PgxHDI18tlgBX4Dg6n4lU5Jgwx6KsyAY6pgENsxdmT2aEs3AryOQiHreAdTNVpaoiowRh54LwNfmQUHbGr%2F3AH5Irml2BZ8x6%2FbVbzQ2v%2Bpm%2BPSkx7DTzX637yxdcfKIyGltV4AFum1CdJRA5ectfdVggDflAeUMXXqf1VDB7oxWhWD3MbRlRG7aWuH7PV6Df05%2FU0U%2BPajcuCuEp7AVQ8Nhk1R6GMAJtDg6xhdlQWEt%2FlFofhqb48QhN6H20o0Db&X-Amz-Signature=83a331d9c3dc2464664142ad42316f0a0d6ab82038e78c06d9f74445b1381fcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FAR5MXN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxpyljLqXDSxFU1dShY%2B7J31NiZE547mNG1OOPU4GRpAiA4%2FjImqfw%2BuNNl0I3P%2FNzC8kW7GYicDU%2Fldu6s4HlWBCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5TuiEsT5yM8y%2BvZVKtwDtGntONrf5Wiz1m0tpZ8jLB%2FQIOGgggxniS%2Fh9Mw7nodTN5HmcsuxhCKum2S3CwhCy6hQIzISf0svw%2FV4s6x5hYTXZLKjym8T%2BG5X4ebZakFtMMbBxs0qpPfTfRDM8wCpiWEELy9VfU76aMqQlxIMPEEZ%2FyF37KHqYeR8WTrV7QaDK2ptdPVLle5HGGilKk5B6BagiMEfJ0R5LzCYVzlocRNNE2B1aP%2FA8D1SSqwMfF7xBwlyo5aQuNxNLEQZJ%2BKK3B7ttNByopO2zE5HvobXP5z4TA91q2hqMXDmsjcN58akTRoS5hfJdYaGe2K1eB4pjsJH1jdwQwIhUAImUEewICefnoc%2FuG2spc0DvLtzocvr%2FcdgUP617nlYR5%2F7yhwndkaGKJcMH6R6yAbOapV1btvXtqwDeVn7sXavBexQ9zeJcylAWn9mk8oM5UemwuR01HFnxvz2p9L8xB2GzOnDURHRzxe0IB%2FjEXNL9n3pHo5BafIiORlcbyVxbuV38rvyEVQD6JVQScn7x%2BkOD1HHvtsKJSSI7SggMAvIvyuMQ99SGS6TNxH4Uyc4YTQVOrFszl9eB2xEaqp8do7jwNpHkyXiPSAQlwhSl52PgxHDI18tlgBX4Dg6n4lU5Jgwx6KsyAY6pgENsxdmT2aEs3AryOQiHreAdTNVpaoiowRh54LwNfmQUHbGr%2F3AH5Irml2BZ8x6%2FbVbzQ2v%2Bpm%2BPSkx7DTzX637yxdcfKIyGltV4AFum1CdJRA5ectfdVggDflAeUMXXqf1VDB7oxWhWD3MbRlRG7aWuH7PV6Df05%2FU0U%2BPajcuCuEp7AVQ8Nhk1R6GMAJtDg6xhdlQWEt%2FlFofhqb48QhN6H20o0Db&X-Amz-Signature=9c61307d1d15dd2571e4922ce80110fbeb841d89f566df07332b6f0b4c97538f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FAR5MXN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxpyljLqXDSxFU1dShY%2B7J31NiZE547mNG1OOPU4GRpAiA4%2FjImqfw%2BuNNl0I3P%2FNzC8kW7GYicDU%2Fldu6s4HlWBCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5TuiEsT5yM8y%2BvZVKtwDtGntONrf5Wiz1m0tpZ8jLB%2FQIOGgggxniS%2Fh9Mw7nodTN5HmcsuxhCKum2S3CwhCy6hQIzISf0svw%2FV4s6x5hYTXZLKjym8T%2BG5X4ebZakFtMMbBxs0qpPfTfRDM8wCpiWEELy9VfU76aMqQlxIMPEEZ%2FyF37KHqYeR8WTrV7QaDK2ptdPVLle5HGGilKk5B6BagiMEfJ0R5LzCYVzlocRNNE2B1aP%2FA8D1SSqwMfF7xBwlyo5aQuNxNLEQZJ%2BKK3B7ttNByopO2zE5HvobXP5z4TA91q2hqMXDmsjcN58akTRoS5hfJdYaGe2K1eB4pjsJH1jdwQwIhUAImUEewICefnoc%2FuG2spc0DvLtzocvr%2FcdgUP617nlYR5%2F7yhwndkaGKJcMH6R6yAbOapV1btvXtqwDeVn7sXavBexQ9zeJcylAWn9mk8oM5UemwuR01HFnxvz2p9L8xB2GzOnDURHRzxe0IB%2FjEXNL9n3pHo5BafIiORlcbyVxbuV38rvyEVQD6JVQScn7x%2BkOD1HHvtsKJSSI7SggMAvIvyuMQ99SGS6TNxH4Uyc4YTQVOrFszl9eB2xEaqp8do7jwNpHkyXiPSAQlwhSl52PgxHDI18tlgBX4Dg6n4lU5Jgwx6KsyAY6pgENsxdmT2aEs3AryOQiHreAdTNVpaoiowRh54LwNfmQUHbGr%2F3AH5Irml2BZ8x6%2FbVbzQ2v%2Bpm%2BPSkx7DTzX637yxdcfKIyGltV4AFum1CdJRA5ectfdVggDflAeUMXXqf1VDB7oxWhWD3MbRlRG7aWuH7PV6Df05%2FU0U%2BPajcuCuEp7AVQ8Nhk1R6GMAJtDg6xhdlQWEt%2FlFofhqb48QhN6H20o0Db&X-Amz-Signature=30c4aeb2c759317ca96e4fe8508b80c882ec1aed882d3f88adba9959cbbdd863&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FAR5MXN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxpyljLqXDSxFU1dShY%2B7J31NiZE547mNG1OOPU4GRpAiA4%2FjImqfw%2BuNNl0I3P%2FNzC8kW7GYicDU%2Fldu6s4HlWBCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5TuiEsT5yM8y%2BvZVKtwDtGntONrf5Wiz1m0tpZ8jLB%2FQIOGgggxniS%2Fh9Mw7nodTN5HmcsuxhCKum2S3CwhCy6hQIzISf0svw%2FV4s6x5hYTXZLKjym8T%2BG5X4ebZakFtMMbBxs0qpPfTfRDM8wCpiWEELy9VfU76aMqQlxIMPEEZ%2FyF37KHqYeR8WTrV7QaDK2ptdPVLle5HGGilKk5B6BagiMEfJ0R5LzCYVzlocRNNE2B1aP%2FA8D1SSqwMfF7xBwlyo5aQuNxNLEQZJ%2BKK3B7ttNByopO2zE5HvobXP5z4TA91q2hqMXDmsjcN58akTRoS5hfJdYaGe2K1eB4pjsJH1jdwQwIhUAImUEewICefnoc%2FuG2spc0DvLtzocvr%2FcdgUP617nlYR5%2F7yhwndkaGKJcMH6R6yAbOapV1btvXtqwDeVn7sXavBexQ9zeJcylAWn9mk8oM5UemwuR01HFnxvz2p9L8xB2GzOnDURHRzxe0IB%2FjEXNL9n3pHo5BafIiORlcbyVxbuV38rvyEVQD6JVQScn7x%2BkOD1HHvtsKJSSI7SggMAvIvyuMQ99SGS6TNxH4Uyc4YTQVOrFszl9eB2xEaqp8do7jwNpHkyXiPSAQlwhSl52PgxHDI18tlgBX4Dg6n4lU5Jgwx6KsyAY6pgENsxdmT2aEs3AryOQiHreAdTNVpaoiowRh54LwNfmQUHbGr%2F3AH5Irml2BZ8x6%2FbVbzQ2v%2Bpm%2BPSkx7DTzX637yxdcfKIyGltV4AFum1CdJRA5ectfdVggDflAeUMXXqf1VDB7oxWhWD3MbRlRG7aWuH7PV6Df05%2FU0U%2BPajcuCuEp7AVQ8Nhk1R6GMAJtDg6xhdlQWEt%2FlFofhqb48QhN6H20o0Db&X-Amz-Signature=0988fab0b706d483d07c82f2ebfe5f65003a7054a40783e55536ee9ed1abf247&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FAR5MXN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxpyljLqXDSxFU1dShY%2B7J31NiZE547mNG1OOPU4GRpAiA4%2FjImqfw%2BuNNl0I3P%2FNzC8kW7GYicDU%2Fldu6s4HlWBCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5TuiEsT5yM8y%2BvZVKtwDtGntONrf5Wiz1m0tpZ8jLB%2FQIOGgggxniS%2Fh9Mw7nodTN5HmcsuxhCKum2S3CwhCy6hQIzISf0svw%2FV4s6x5hYTXZLKjym8T%2BG5X4ebZakFtMMbBxs0qpPfTfRDM8wCpiWEELy9VfU76aMqQlxIMPEEZ%2FyF37KHqYeR8WTrV7QaDK2ptdPVLle5HGGilKk5B6BagiMEfJ0R5LzCYVzlocRNNE2B1aP%2FA8D1SSqwMfF7xBwlyo5aQuNxNLEQZJ%2BKK3B7ttNByopO2zE5HvobXP5z4TA91q2hqMXDmsjcN58akTRoS5hfJdYaGe2K1eB4pjsJH1jdwQwIhUAImUEewICefnoc%2FuG2spc0DvLtzocvr%2FcdgUP617nlYR5%2F7yhwndkaGKJcMH6R6yAbOapV1btvXtqwDeVn7sXavBexQ9zeJcylAWn9mk8oM5UemwuR01HFnxvz2p9L8xB2GzOnDURHRzxe0IB%2FjEXNL9n3pHo5BafIiORlcbyVxbuV38rvyEVQD6JVQScn7x%2BkOD1HHvtsKJSSI7SggMAvIvyuMQ99SGS6TNxH4Uyc4YTQVOrFszl9eB2xEaqp8do7jwNpHkyXiPSAQlwhSl52PgxHDI18tlgBX4Dg6n4lU5Jgwx6KsyAY6pgENsxdmT2aEs3AryOQiHreAdTNVpaoiowRh54LwNfmQUHbGr%2F3AH5Irml2BZ8x6%2FbVbzQ2v%2Bpm%2BPSkx7DTzX637yxdcfKIyGltV4AFum1CdJRA5ectfdVggDflAeUMXXqf1VDB7oxWhWD3MbRlRG7aWuH7PV6Df05%2FU0U%2BPajcuCuEp7AVQ8Nhk1R6GMAJtDg6xhdlQWEt%2FlFofhqb48QhN6H20o0Db&X-Amz-Signature=41eb974eccb4a258e18b5c1ffb808d26724400cc8494cc2d5fcdc34c16198be8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FAR5MXN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxpyljLqXDSxFU1dShY%2B7J31NiZE547mNG1OOPU4GRpAiA4%2FjImqfw%2BuNNl0I3P%2FNzC8kW7GYicDU%2Fldu6s4HlWBCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5TuiEsT5yM8y%2BvZVKtwDtGntONrf5Wiz1m0tpZ8jLB%2FQIOGgggxniS%2Fh9Mw7nodTN5HmcsuxhCKum2S3CwhCy6hQIzISf0svw%2FV4s6x5hYTXZLKjym8T%2BG5X4ebZakFtMMbBxs0qpPfTfRDM8wCpiWEELy9VfU76aMqQlxIMPEEZ%2FyF37KHqYeR8WTrV7QaDK2ptdPVLle5HGGilKk5B6BagiMEfJ0R5LzCYVzlocRNNE2B1aP%2FA8D1SSqwMfF7xBwlyo5aQuNxNLEQZJ%2BKK3B7ttNByopO2zE5HvobXP5z4TA91q2hqMXDmsjcN58akTRoS5hfJdYaGe2K1eB4pjsJH1jdwQwIhUAImUEewICefnoc%2FuG2spc0DvLtzocvr%2FcdgUP617nlYR5%2F7yhwndkaGKJcMH6R6yAbOapV1btvXtqwDeVn7sXavBexQ9zeJcylAWn9mk8oM5UemwuR01HFnxvz2p9L8xB2GzOnDURHRzxe0IB%2FjEXNL9n3pHo5BafIiORlcbyVxbuV38rvyEVQD6JVQScn7x%2BkOD1HHvtsKJSSI7SggMAvIvyuMQ99SGS6TNxH4Uyc4YTQVOrFszl9eB2xEaqp8do7jwNpHkyXiPSAQlwhSl52PgxHDI18tlgBX4Dg6n4lU5Jgwx6KsyAY6pgENsxdmT2aEs3AryOQiHreAdTNVpaoiowRh54LwNfmQUHbGr%2F3AH5Irml2BZ8x6%2FbVbzQ2v%2Bpm%2BPSkx7DTzX637yxdcfKIyGltV4AFum1CdJRA5ectfdVggDflAeUMXXqf1VDB7oxWhWD3MbRlRG7aWuH7PV6Df05%2FU0U%2BPajcuCuEp7AVQ8Nhk1R6GMAJtDg6xhdlQWEt%2FlFofhqb48QhN6H20o0Db&X-Amz-Signature=05c9a1eebc5a9aaf743d9dd033c1809fec1ab1ac028671b250faae3465a9450d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FAR5MXN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxpyljLqXDSxFU1dShY%2B7J31NiZE547mNG1OOPU4GRpAiA4%2FjImqfw%2BuNNl0I3P%2FNzC8kW7GYicDU%2Fldu6s4HlWBCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5TuiEsT5yM8y%2BvZVKtwDtGntONrf5Wiz1m0tpZ8jLB%2FQIOGgggxniS%2Fh9Mw7nodTN5HmcsuxhCKum2S3CwhCy6hQIzISf0svw%2FV4s6x5hYTXZLKjym8T%2BG5X4ebZakFtMMbBxs0qpPfTfRDM8wCpiWEELy9VfU76aMqQlxIMPEEZ%2FyF37KHqYeR8WTrV7QaDK2ptdPVLle5HGGilKk5B6BagiMEfJ0R5LzCYVzlocRNNE2B1aP%2FA8D1SSqwMfF7xBwlyo5aQuNxNLEQZJ%2BKK3B7ttNByopO2zE5HvobXP5z4TA91q2hqMXDmsjcN58akTRoS5hfJdYaGe2K1eB4pjsJH1jdwQwIhUAImUEewICefnoc%2FuG2spc0DvLtzocvr%2FcdgUP617nlYR5%2F7yhwndkaGKJcMH6R6yAbOapV1btvXtqwDeVn7sXavBexQ9zeJcylAWn9mk8oM5UemwuR01HFnxvz2p9L8xB2GzOnDURHRzxe0IB%2FjEXNL9n3pHo5BafIiORlcbyVxbuV38rvyEVQD6JVQScn7x%2BkOD1HHvtsKJSSI7SggMAvIvyuMQ99SGS6TNxH4Uyc4YTQVOrFszl9eB2xEaqp8do7jwNpHkyXiPSAQlwhSl52PgxHDI18tlgBX4Dg6n4lU5Jgwx6KsyAY6pgENsxdmT2aEs3AryOQiHreAdTNVpaoiowRh54LwNfmQUHbGr%2F3AH5Irml2BZ8x6%2FbVbzQ2v%2Bpm%2BPSkx7DTzX637yxdcfKIyGltV4AFum1CdJRA5ectfdVggDflAeUMXXqf1VDB7oxWhWD3MbRlRG7aWuH7PV6Df05%2FU0U%2BPajcuCuEp7AVQ8Nhk1R6GMAJtDg6xhdlQWEt%2FlFofhqb48QhN6H20o0Db&X-Amz-Signature=ec348928848f0defc0604914965714e0070f394656357887c50f586a1496d473&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

