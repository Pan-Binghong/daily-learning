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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSRLVWF3%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCD17MO9T%2FMr1WYknYOZQAA6amP5e%2F5X0ieebeXELGgAiB7BRvGcumHYagYE8z3jCXSLzbnSQffVgXcwvbkLxeL6yqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSe8Sjahspy9uSV7kKtwDHWXlVa4jvlNCsl7bp3J11ABM9M8TAHdF2Vfrmu8oUQBBbo0gY7x280LL8Mw5D4%2FezcV7Jkx%2BFqVfS6uBjaKpBRC74%2BUj1RZbsZ6FwEsbPz7zQk9DaS4U0r%2FGU6zuYJSpmyQfF4aPRdDC5i1Am8%2Fkawzo0G4cTMSRNIgPlNbEQjSAzUVhRsek%2B0faaP7OnL0Ekg29Efk0lx2477%2ByZSe2c1%2FafZeU%2Bd8s8XhXdpti1%2Bx3CnzbG%2FjT3aAYvXhGeAqkFBff8UTg%2FaX3F9vIEMDmGvf%2BMtWVrHVIAvuW0Huiw94TqoCzJwmlBn8IcKbDG7G5cFf9L7zUm0ZTzI%2Bf9WUeVT%2B%2FEvhwmPc3dT3DdFowfesYWJLJRpRWIoCDLfol%2Bqnl2uUoekbncHkBKD2OM7LIaGitcZ0WY83bVGNq2UwjoUo3%2BIQFXSOpyZTMSLl7XJAZKrgvrVQ65T6rcYwpziFJPRrySQJFCJsCePgJ6n6n%2B%2B4lkRh%2FwH0tdlEqfpBHiIne3scJGX9zA20IuknTF4L0t6xQXUCLJ5Av8qrR5PAiZZFj3QQIcIO5BAhFaAB%2FwX0CW%2FcuchQ0O1eRcfd3u9k3br1wNjCvzZHALMPCTuxSa%2F8B%2B5hH1KWao5P33RAw09%2F2zgY6pgF3Kq44T8GU928CsOpJEb28UioHu8bX%2FEm%2BnYSNGc%2BhYBJYNYlEdUQR7CMM2Ws%2BkivIfjZVIN5X6ZZgfdwj2OeGXM2%2FsqUjJnl4vI83ydTj8nzj294IWCq2ynRYd%2BzMpnmXotpWWNyjp2h1sDEqNFdCOjHzoyMLNKWijdkLasRBRUgn8iQu%2B92bMt31SOwTv5azITMLZOEkxiD4NaEqvl34EcOb9EAN&X-Amz-Signature=07c056737a424bae2bd0fb42f27ed35c54f1a0319f04e0ff8483a321fbfe82fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSRLVWF3%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCD17MO9T%2FMr1WYknYOZQAA6amP5e%2F5X0ieebeXELGgAiB7BRvGcumHYagYE8z3jCXSLzbnSQffVgXcwvbkLxeL6yqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSe8Sjahspy9uSV7kKtwDHWXlVa4jvlNCsl7bp3J11ABM9M8TAHdF2Vfrmu8oUQBBbo0gY7x280LL8Mw5D4%2FezcV7Jkx%2BFqVfS6uBjaKpBRC74%2BUj1RZbsZ6FwEsbPz7zQk9DaS4U0r%2FGU6zuYJSpmyQfF4aPRdDC5i1Am8%2Fkawzo0G4cTMSRNIgPlNbEQjSAzUVhRsek%2B0faaP7OnL0Ekg29Efk0lx2477%2ByZSe2c1%2FafZeU%2Bd8s8XhXdpti1%2Bx3CnzbG%2FjT3aAYvXhGeAqkFBff8UTg%2FaX3F9vIEMDmGvf%2BMtWVrHVIAvuW0Huiw94TqoCzJwmlBn8IcKbDG7G5cFf9L7zUm0ZTzI%2Bf9WUeVT%2B%2FEvhwmPc3dT3DdFowfesYWJLJRpRWIoCDLfol%2Bqnl2uUoekbncHkBKD2OM7LIaGitcZ0WY83bVGNq2UwjoUo3%2BIQFXSOpyZTMSLl7XJAZKrgvrVQ65T6rcYwpziFJPRrySQJFCJsCePgJ6n6n%2B%2B4lkRh%2FwH0tdlEqfpBHiIne3scJGX9zA20IuknTF4L0t6xQXUCLJ5Av8qrR5PAiZZFj3QQIcIO5BAhFaAB%2FwX0CW%2FcuchQ0O1eRcfd3u9k3br1wNjCvzZHALMPCTuxSa%2F8B%2B5hH1KWao5P33RAw09%2F2zgY6pgF3Kq44T8GU928CsOpJEb28UioHu8bX%2FEm%2BnYSNGc%2BhYBJYNYlEdUQR7CMM2Ws%2BkivIfjZVIN5X6ZZgfdwj2OeGXM2%2FsqUjJnl4vI83ydTj8nzj294IWCq2ynRYd%2BzMpnmXotpWWNyjp2h1sDEqNFdCOjHzoyMLNKWijdkLasRBRUgn8iQu%2B92bMt31SOwTv5azITMLZOEkxiD4NaEqvl34EcOb9EAN&X-Amz-Signature=8f624c31b5d6459f81bc193dbb419a75f0f4ebe16702c769f97c1a21f0fdeb70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSRLVWF3%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCD17MO9T%2FMr1WYknYOZQAA6amP5e%2F5X0ieebeXELGgAiB7BRvGcumHYagYE8z3jCXSLzbnSQffVgXcwvbkLxeL6yqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSe8Sjahspy9uSV7kKtwDHWXlVa4jvlNCsl7bp3J11ABM9M8TAHdF2Vfrmu8oUQBBbo0gY7x280LL8Mw5D4%2FezcV7Jkx%2BFqVfS6uBjaKpBRC74%2BUj1RZbsZ6FwEsbPz7zQk9DaS4U0r%2FGU6zuYJSpmyQfF4aPRdDC5i1Am8%2Fkawzo0G4cTMSRNIgPlNbEQjSAzUVhRsek%2B0faaP7OnL0Ekg29Efk0lx2477%2ByZSe2c1%2FafZeU%2Bd8s8XhXdpti1%2Bx3CnzbG%2FjT3aAYvXhGeAqkFBff8UTg%2FaX3F9vIEMDmGvf%2BMtWVrHVIAvuW0Huiw94TqoCzJwmlBn8IcKbDG7G5cFf9L7zUm0ZTzI%2Bf9WUeVT%2B%2FEvhwmPc3dT3DdFowfesYWJLJRpRWIoCDLfol%2Bqnl2uUoekbncHkBKD2OM7LIaGitcZ0WY83bVGNq2UwjoUo3%2BIQFXSOpyZTMSLl7XJAZKrgvrVQ65T6rcYwpziFJPRrySQJFCJsCePgJ6n6n%2B%2B4lkRh%2FwH0tdlEqfpBHiIne3scJGX9zA20IuknTF4L0t6xQXUCLJ5Av8qrR5PAiZZFj3QQIcIO5BAhFaAB%2FwX0CW%2FcuchQ0O1eRcfd3u9k3br1wNjCvzZHALMPCTuxSa%2F8B%2B5hH1KWao5P33RAw09%2F2zgY6pgF3Kq44T8GU928CsOpJEb28UioHu8bX%2FEm%2BnYSNGc%2BhYBJYNYlEdUQR7CMM2Ws%2BkivIfjZVIN5X6ZZgfdwj2OeGXM2%2FsqUjJnl4vI83ydTj8nzj294IWCq2ynRYd%2BzMpnmXotpWWNyjp2h1sDEqNFdCOjHzoyMLNKWijdkLasRBRUgn8iQu%2B92bMt31SOwTv5azITMLZOEkxiD4NaEqvl34EcOb9EAN&X-Amz-Signature=3f789fc99edd5cf280b6ca9623ef38abba44251d84678386bf8cad64dcbeceb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSRLVWF3%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCD17MO9T%2FMr1WYknYOZQAA6amP5e%2F5X0ieebeXELGgAiB7BRvGcumHYagYE8z3jCXSLzbnSQffVgXcwvbkLxeL6yqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSe8Sjahspy9uSV7kKtwDHWXlVa4jvlNCsl7bp3J11ABM9M8TAHdF2Vfrmu8oUQBBbo0gY7x280LL8Mw5D4%2FezcV7Jkx%2BFqVfS6uBjaKpBRC74%2BUj1RZbsZ6FwEsbPz7zQk9DaS4U0r%2FGU6zuYJSpmyQfF4aPRdDC5i1Am8%2Fkawzo0G4cTMSRNIgPlNbEQjSAzUVhRsek%2B0faaP7OnL0Ekg29Efk0lx2477%2ByZSe2c1%2FafZeU%2Bd8s8XhXdpti1%2Bx3CnzbG%2FjT3aAYvXhGeAqkFBff8UTg%2FaX3F9vIEMDmGvf%2BMtWVrHVIAvuW0Huiw94TqoCzJwmlBn8IcKbDG7G5cFf9L7zUm0ZTzI%2Bf9WUeVT%2B%2FEvhwmPc3dT3DdFowfesYWJLJRpRWIoCDLfol%2Bqnl2uUoekbncHkBKD2OM7LIaGitcZ0WY83bVGNq2UwjoUo3%2BIQFXSOpyZTMSLl7XJAZKrgvrVQ65T6rcYwpziFJPRrySQJFCJsCePgJ6n6n%2B%2B4lkRh%2FwH0tdlEqfpBHiIne3scJGX9zA20IuknTF4L0t6xQXUCLJ5Av8qrR5PAiZZFj3QQIcIO5BAhFaAB%2FwX0CW%2FcuchQ0O1eRcfd3u9k3br1wNjCvzZHALMPCTuxSa%2F8B%2B5hH1KWao5P33RAw09%2F2zgY6pgF3Kq44T8GU928CsOpJEb28UioHu8bX%2FEm%2BnYSNGc%2BhYBJYNYlEdUQR7CMM2Ws%2BkivIfjZVIN5X6ZZgfdwj2OeGXM2%2FsqUjJnl4vI83ydTj8nzj294IWCq2ynRYd%2BzMpnmXotpWWNyjp2h1sDEqNFdCOjHzoyMLNKWijdkLasRBRUgn8iQu%2B92bMt31SOwTv5azITMLZOEkxiD4NaEqvl34EcOb9EAN&X-Amz-Signature=56ed6c328390fba1d28bf81b842b07ba3f87c2e3c741841762c4c1dabd1201b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSRLVWF3%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCD17MO9T%2FMr1WYknYOZQAA6amP5e%2F5X0ieebeXELGgAiB7BRvGcumHYagYE8z3jCXSLzbnSQffVgXcwvbkLxeL6yqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSe8Sjahspy9uSV7kKtwDHWXlVa4jvlNCsl7bp3J11ABM9M8TAHdF2Vfrmu8oUQBBbo0gY7x280LL8Mw5D4%2FezcV7Jkx%2BFqVfS6uBjaKpBRC74%2BUj1RZbsZ6FwEsbPz7zQk9DaS4U0r%2FGU6zuYJSpmyQfF4aPRdDC5i1Am8%2Fkawzo0G4cTMSRNIgPlNbEQjSAzUVhRsek%2B0faaP7OnL0Ekg29Efk0lx2477%2ByZSe2c1%2FafZeU%2Bd8s8XhXdpti1%2Bx3CnzbG%2FjT3aAYvXhGeAqkFBff8UTg%2FaX3F9vIEMDmGvf%2BMtWVrHVIAvuW0Huiw94TqoCzJwmlBn8IcKbDG7G5cFf9L7zUm0ZTzI%2Bf9WUeVT%2B%2FEvhwmPc3dT3DdFowfesYWJLJRpRWIoCDLfol%2Bqnl2uUoekbncHkBKD2OM7LIaGitcZ0WY83bVGNq2UwjoUo3%2BIQFXSOpyZTMSLl7XJAZKrgvrVQ65T6rcYwpziFJPRrySQJFCJsCePgJ6n6n%2B%2B4lkRh%2FwH0tdlEqfpBHiIne3scJGX9zA20IuknTF4L0t6xQXUCLJ5Av8qrR5PAiZZFj3QQIcIO5BAhFaAB%2FwX0CW%2FcuchQ0O1eRcfd3u9k3br1wNjCvzZHALMPCTuxSa%2F8B%2B5hH1KWao5P33RAw09%2F2zgY6pgF3Kq44T8GU928CsOpJEb28UioHu8bX%2FEm%2BnYSNGc%2BhYBJYNYlEdUQR7CMM2Ws%2BkivIfjZVIN5X6ZZgfdwj2OeGXM2%2FsqUjJnl4vI83ydTj8nzj294IWCq2ynRYd%2BzMpnmXotpWWNyjp2h1sDEqNFdCOjHzoyMLNKWijdkLasRBRUgn8iQu%2B92bMt31SOwTv5azITMLZOEkxiD4NaEqvl34EcOb9EAN&X-Amz-Signature=e18ea1657e91de8c0a3d12d2ea0671c82917c78141be8b5e9c3ecb1e1d8498c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSRLVWF3%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCD17MO9T%2FMr1WYknYOZQAA6amP5e%2F5X0ieebeXELGgAiB7BRvGcumHYagYE8z3jCXSLzbnSQffVgXcwvbkLxeL6yqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSe8Sjahspy9uSV7kKtwDHWXlVa4jvlNCsl7bp3J11ABM9M8TAHdF2Vfrmu8oUQBBbo0gY7x280LL8Mw5D4%2FezcV7Jkx%2BFqVfS6uBjaKpBRC74%2BUj1RZbsZ6FwEsbPz7zQk9DaS4U0r%2FGU6zuYJSpmyQfF4aPRdDC5i1Am8%2Fkawzo0G4cTMSRNIgPlNbEQjSAzUVhRsek%2B0faaP7OnL0Ekg29Efk0lx2477%2ByZSe2c1%2FafZeU%2Bd8s8XhXdpti1%2Bx3CnzbG%2FjT3aAYvXhGeAqkFBff8UTg%2FaX3F9vIEMDmGvf%2BMtWVrHVIAvuW0Huiw94TqoCzJwmlBn8IcKbDG7G5cFf9L7zUm0ZTzI%2Bf9WUeVT%2B%2FEvhwmPc3dT3DdFowfesYWJLJRpRWIoCDLfol%2Bqnl2uUoekbncHkBKD2OM7LIaGitcZ0WY83bVGNq2UwjoUo3%2BIQFXSOpyZTMSLl7XJAZKrgvrVQ65T6rcYwpziFJPRrySQJFCJsCePgJ6n6n%2B%2B4lkRh%2FwH0tdlEqfpBHiIne3scJGX9zA20IuknTF4L0t6xQXUCLJ5Av8qrR5PAiZZFj3QQIcIO5BAhFaAB%2FwX0CW%2FcuchQ0O1eRcfd3u9k3br1wNjCvzZHALMPCTuxSa%2F8B%2B5hH1KWao5P33RAw09%2F2zgY6pgF3Kq44T8GU928CsOpJEb28UioHu8bX%2FEm%2BnYSNGc%2BhYBJYNYlEdUQR7CMM2Ws%2BkivIfjZVIN5X6ZZgfdwj2OeGXM2%2FsqUjJnl4vI83ydTj8nzj294IWCq2ynRYd%2BzMpnmXotpWWNyjp2h1sDEqNFdCOjHzoyMLNKWijdkLasRBRUgn8iQu%2B92bMt31SOwTv5azITMLZOEkxiD4NaEqvl34EcOb9EAN&X-Amz-Signature=dbac9f9d1696e8444dab6c84cf995cf8a9d62a0955e22bfe77ca2890f39d4b34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSRLVWF3%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCD17MO9T%2FMr1WYknYOZQAA6amP5e%2F5X0ieebeXELGgAiB7BRvGcumHYagYE8z3jCXSLzbnSQffVgXcwvbkLxeL6yqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSe8Sjahspy9uSV7kKtwDHWXlVa4jvlNCsl7bp3J11ABM9M8TAHdF2Vfrmu8oUQBBbo0gY7x280LL8Mw5D4%2FezcV7Jkx%2BFqVfS6uBjaKpBRC74%2BUj1RZbsZ6FwEsbPz7zQk9DaS4U0r%2FGU6zuYJSpmyQfF4aPRdDC5i1Am8%2Fkawzo0G4cTMSRNIgPlNbEQjSAzUVhRsek%2B0faaP7OnL0Ekg29Efk0lx2477%2ByZSe2c1%2FafZeU%2Bd8s8XhXdpti1%2Bx3CnzbG%2FjT3aAYvXhGeAqkFBff8UTg%2FaX3F9vIEMDmGvf%2BMtWVrHVIAvuW0Huiw94TqoCzJwmlBn8IcKbDG7G5cFf9L7zUm0ZTzI%2Bf9WUeVT%2B%2FEvhwmPc3dT3DdFowfesYWJLJRpRWIoCDLfol%2Bqnl2uUoekbncHkBKD2OM7LIaGitcZ0WY83bVGNq2UwjoUo3%2BIQFXSOpyZTMSLl7XJAZKrgvrVQ65T6rcYwpziFJPRrySQJFCJsCePgJ6n6n%2B%2B4lkRh%2FwH0tdlEqfpBHiIne3scJGX9zA20IuknTF4L0t6xQXUCLJ5Av8qrR5PAiZZFj3QQIcIO5BAhFaAB%2FwX0CW%2FcuchQ0O1eRcfd3u9k3br1wNjCvzZHALMPCTuxSa%2F8B%2B5hH1KWao5P33RAw09%2F2zgY6pgF3Kq44T8GU928CsOpJEb28UioHu8bX%2FEm%2BnYSNGc%2BhYBJYNYlEdUQR7CMM2Ws%2BkivIfjZVIN5X6ZZgfdwj2OeGXM2%2FsqUjJnl4vI83ydTj8nzj294IWCq2ynRYd%2BzMpnmXotpWWNyjp2h1sDEqNFdCOjHzoyMLNKWijdkLasRBRUgn8iQu%2B92bMt31SOwTv5azITMLZOEkxiD4NaEqvl34EcOb9EAN&X-Amz-Signature=6b5e7aa850a6d94558d65f892b1e21329b953f5c6dd963c2700f7a6baf4030f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSRLVWF3%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCD17MO9T%2FMr1WYknYOZQAA6amP5e%2F5X0ieebeXELGgAiB7BRvGcumHYagYE8z3jCXSLzbnSQffVgXcwvbkLxeL6yqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSe8Sjahspy9uSV7kKtwDHWXlVa4jvlNCsl7bp3J11ABM9M8TAHdF2Vfrmu8oUQBBbo0gY7x280LL8Mw5D4%2FezcV7Jkx%2BFqVfS6uBjaKpBRC74%2BUj1RZbsZ6FwEsbPz7zQk9DaS4U0r%2FGU6zuYJSpmyQfF4aPRdDC5i1Am8%2Fkawzo0G4cTMSRNIgPlNbEQjSAzUVhRsek%2B0faaP7OnL0Ekg29Efk0lx2477%2ByZSe2c1%2FafZeU%2Bd8s8XhXdpti1%2Bx3CnzbG%2FjT3aAYvXhGeAqkFBff8UTg%2FaX3F9vIEMDmGvf%2BMtWVrHVIAvuW0Huiw94TqoCzJwmlBn8IcKbDG7G5cFf9L7zUm0ZTzI%2Bf9WUeVT%2B%2FEvhwmPc3dT3DdFowfesYWJLJRpRWIoCDLfol%2Bqnl2uUoekbncHkBKD2OM7LIaGitcZ0WY83bVGNq2UwjoUo3%2BIQFXSOpyZTMSLl7XJAZKrgvrVQ65T6rcYwpziFJPRrySQJFCJsCePgJ6n6n%2B%2B4lkRh%2FwH0tdlEqfpBHiIne3scJGX9zA20IuknTF4L0t6xQXUCLJ5Av8qrR5PAiZZFj3QQIcIO5BAhFaAB%2FwX0CW%2FcuchQ0O1eRcfd3u9k3br1wNjCvzZHALMPCTuxSa%2F8B%2B5hH1KWao5P33RAw09%2F2zgY6pgF3Kq44T8GU928CsOpJEb28UioHu8bX%2FEm%2BnYSNGc%2BhYBJYNYlEdUQR7CMM2Ws%2BkivIfjZVIN5X6ZZgfdwj2OeGXM2%2FsqUjJnl4vI83ydTj8nzj294IWCq2ynRYd%2BzMpnmXotpWWNyjp2h1sDEqNFdCOjHzoyMLNKWijdkLasRBRUgn8iQu%2B92bMt31SOwTv5azITMLZOEkxiD4NaEqvl34EcOb9EAN&X-Amz-Signature=d0ed787ce6731737378b1d1b17d60694f34fbfab9d1585844c3b146260f4dc73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSRLVWF3%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCD17MO9T%2FMr1WYknYOZQAA6amP5e%2F5X0ieebeXELGgAiB7BRvGcumHYagYE8z3jCXSLzbnSQffVgXcwvbkLxeL6yqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSe8Sjahspy9uSV7kKtwDHWXlVa4jvlNCsl7bp3J11ABM9M8TAHdF2Vfrmu8oUQBBbo0gY7x280LL8Mw5D4%2FezcV7Jkx%2BFqVfS6uBjaKpBRC74%2BUj1RZbsZ6FwEsbPz7zQk9DaS4U0r%2FGU6zuYJSpmyQfF4aPRdDC5i1Am8%2Fkawzo0G4cTMSRNIgPlNbEQjSAzUVhRsek%2B0faaP7OnL0Ekg29Efk0lx2477%2ByZSe2c1%2FafZeU%2Bd8s8XhXdpti1%2Bx3CnzbG%2FjT3aAYvXhGeAqkFBff8UTg%2FaX3F9vIEMDmGvf%2BMtWVrHVIAvuW0Huiw94TqoCzJwmlBn8IcKbDG7G5cFf9L7zUm0ZTzI%2Bf9WUeVT%2B%2FEvhwmPc3dT3DdFowfesYWJLJRpRWIoCDLfol%2Bqnl2uUoekbncHkBKD2OM7LIaGitcZ0WY83bVGNq2UwjoUo3%2BIQFXSOpyZTMSLl7XJAZKrgvrVQ65T6rcYwpziFJPRrySQJFCJsCePgJ6n6n%2B%2B4lkRh%2FwH0tdlEqfpBHiIne3scJGX9zA20IuknTF4L0t6xQXUCLJ5Av8qrR5PAiZZFj3QQIcIO5BAhFaAB%2FwX0CW%2FcuchQ0O1eRcfd3u9k3br1wNjCvzZHALMPCTuxSa%2F8B%2B5hH1KWao5P33RAw09%2F2zgY6pgF3Kq44T8GU928CsOpJEb28UioHu8bX%2FEm%2BnYSNGc%2BhYBJYNYlEdUQR7CMM2Ws%2BkivIfjZVIN5X6ZZgfdwj2OeGXM2%2FsqUjJnl4vI83ydTj8nzj294IWCq2ynRYd%2BzMpnmXotpWWNyjp2h1sDEqNFdCOjHzoyMLNKWijdkLasRBRUgn8iQu%2B92bMt31SOwTv5azITMLZOEkxiD4NaEqvl34EcOb9EAN&X-Amz-Signature=c42b7019034f751aad4f3db1127cee6ec2fbe61edae30458fffe919c4922a292&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSRLVWF3%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCD17MO9T%2FMr1WYknYOZQAA6amP5e%2F5X0ieebeXELGgAiB7BRvGcumHYagYE8z3jCXSLzbnSQffVgXcwvbkLxeL6yqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSe8Sjahspy9uSV7kKtwDHWXlVa4jvlNCsl7bp3J11ABM9M8TAHdF2Vfrmu8oUQBBbo0gY7x280LL8Mw5D4%2FezcV7Jkx%2BFqVfS6uBjaKpBRC74%2BUj1RZbsZ6FwEsbPz7zQk9DaS4U0r%2FGU6zuYJSpmyQfF4aPRdDC5i1Am8%2Fkawzo0G4cTMSRNIgPlNbEQjSAzUVhRsek%2B0faaP7OnL0Ekg29Efk0lx2477%2ByZSe2c1%2FafZeU%2Bd8s8XhXdpti1%2Bx3CnzbG%2FjT3aAYvXhGeAqkFBff8UTg%2FaX3F9vIEMDmGvf%2BMtWVrHVIAvuW0Huiw94TqoCzJwmlBn8IcKbDG7G5cFf9L7zUm0ZTzI%2Bf9WUeVT%2B%2FEvhwmPc3dT3DdFowfesYWJLJRpRWIoCDLfol%2Bqnl2uUoekbncHkBKD2OM7LIaGitcZ0WY83bVGNq2UwjoUo3%2BIQFXSOpyZTMSLl7XJAZKrgvrVQ65T6rcYwpziFJPRrySQJFCJsCePgJ6n6n%2B%2B4lkRh%2FwH0tdlEqfpBHiIne3scJGX9zA20IuknTF4L0t6xQXUCLJ5Av8qrR5PAiZZFj3QQIcIO5BAhFaAB%2FwX0CW%2FcuchQ0O1eRcfd3u9k3br1wNjCvzZHALMPCTuxSa%2F8B%2B5hH1KWao5P33RAw09%2F2zgY6pgF3Kq44T8GU928CsOpJEb28UioHu8bX%2FEm%2BnYSNGc%2BhYBJYNYlEdUQR7CMM2Ws%2BkivIfjZVIN5X6ZZgfdwj2OeGXM2%2FsqUjJnl4vI83ydTj8nzj294IWCq2ynRYd%2BzMpnmXotpWWNyjp2h1sDEqNFdCOjHzoyMLNKWijdkLasRBRUgn8iQu%2B92bMt31SOwTv5azITMLZOEkxiD4NaEqvl34EcOb9EAN&X-Amz-Signature=fe5674d84bc9359b5124893b486f814ec3ebf55d3678f554908c4ee1ca762d2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

