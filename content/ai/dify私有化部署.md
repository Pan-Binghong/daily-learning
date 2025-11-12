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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2UAVZ7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEFQfD3v1pW3JbhMkK6n%2FQKhMnY%2B9mrMhUNDJ9FptOCLAiBEpW6vUYgpO6Q8Rts0cT%2F8IBrfFe%2FzPesv%2FRae3Amz%2BSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMY1iADUUSDvayRYZ6KtwDLGiGDXpXVID58RZc%2FouLGBbWbMFSUlJfTvWAndr3PZgkfZMU0ccF1fHBzawyaL%2F5BP04j4qat5BjTAUA%2FV6iTk1BRwPOv09t%2FU1UAo%2FTw5IZeW%2BY2mA3LpsBH%2FUaszRw9nvLYP3izN6EJq9HkEsKva0DJSevgFMa57CDywOY%2FXEvO%2Bhdj4IOLNW%2F%2F%2BnjBfjxVZctEeMDWcGM3ZSoNF41PQBbYdO1bzlxGGBqwU%2BMw3759lVf3%2Fm%2Fnx05SIaczKIDBwR9wBHyOO2aDI1C89u5vZlLKiIqtUB8NlS6Iqg3IkvWbW1L1WkQVQR4e8srJ1AXMTm5b8mec0XVrab3rjzSHSPSQUGmoNGhfLoM77nPH7fhJ8B077fDv%2BekZjVWuQ0lpEHp5rPtiL%2FJHjJV1%2FFKTFGAs6KjhNk3taRmbc9NMq5sG6VH%2FX6p3CC0CE3PZxe6q1OZafvughBPM0IZn5sSBKIOCnHx3D2aK%2Bim2obkou39%2BvUAJTLBxKm%2FD2j8UD2TNKen0csLQjgx7dtGDFwjT%2Bik%2BCDxf0HVqspg8YMdrwDGgm8MjMwaR7paqnM9vCLYR4dJCSr1aVuKdXNtyrjP9rUodYKoxwFyBIEOLJBhn3f%2B3vXQ981%2FYKVRKtcwq%2BPPyAY6pgFVvK1ammDLCtzKOaWnsLDX%2BZmQdCXhD2%2B6oazvefibqfh2Gbk9K5FcL%2BXOi5%2BttJS2MWcBsy8aIaZNo5yZdFmKP%2BjZ%2BeGE%2BwRa%2BaBdOjdfSef7C3r7llUzn9GaNLNdUhGDvPNGgZU92PmAmx7t8snbMWFdVMoS1Y%2BWngLsL6QerrknXJzSJwECo4I7SHLX3V8jlvrC9t2eM5RN5a95yJI9hXfb7Ial&X-Amz-Signature=b30bbd139354e76b8c4d65bddb6efcd9ef5c51dfa28e882751752ec6b179fd70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2UAVZ7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEFQfD3v1pW3JbhMkK6n%2FQKhMnY%2B9mrMhUNDJ9FptOCLAiBEpW6vUYgpO6Q8Rts0cT%2F8IBrfFe%2FzPesv%2FRae3Amz%2BSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMY1iADUUSDvayRYZ6KtwDLGiGDXpXVID58RZc%2FouLGBbWbMFSUlJfTvWAndr3PZgkfZMU0ccF1fHBzawyaL%2F5BP04j4qat5BjTAUA%2FV6iTk1BRwPOv09t%2FU1UAo%2FTw5IZeW%2BY2mA3LpsBH%2FUaszRw9nvLYP3izN6EJq9HkEsKva0DJSevgFMa57CDywOY%2FXEvO%2Bhdj4IOLNW%2F%2F%2BnjBfjxVZctEeMDWcGM3ZSoNF41PQBbYdO1bzlxGGBqwU%2BMw3759lVf3%2Fm%2Fnx05SIaczKIDBwR9wBHyOO2aDI1C89u5vZlLKiIqtUB8NlS6Iqg3IkvWbW1L1WkQVQR4e8srJ1AXMTm5b8mec0XVrab3rjzSHSPSQUGmoNGhfLoM77nPH7fhJ8B077fDv%2BekZjVWuQ0lpEHp5rPtiL%2FJHjJV1%2FFKTFGAs6KjhNk3taRmbc9NMq5sG6VH%2FX6p3CC0CE3PZxe6q1OZafvughBPM0IZn5sSBKIOCnHx3D2aK%2Bim2obkou39%2BvUAJTLBxKm%2FD2j8UD2TNKen0csLQjgx7dtGDFwjT%2Bik%2BCDxf0HVqspg8YMdrwDGgm8MjMwaR7paqnM9vCLYR4dJCSr1aVuKdXNtyrjP9rUodYKoxwFyBIEOLJBhn3f%2B3vXQ981%2FYKVRKtcwq%2BPPyAY6pgFVvK1ammDLCtzKOaWnsLDX%2BZmQdCXhD2%2B6oazvefibqfh2Gbk9K5FcL%2BXOi5%2BttJS2MWcBsy8aIaZNo5yZdFmKP%2BjZ%2BeGE%2BwRa%2BaBdOjdfSef7C3r7llUzn9GaNLNdUhGDvPNGgZU92PmAmx7t8snbMWFdVMoS1Y%2BWngLsL6QerrknXJzSJwECo4I7SHLX3V8jlvrC9t2eM5RN5a95yJI9hXfb7Ial&X-Amz-Signature=98e8a6fefd7f317d4eae55222fccfc9a6873971bf77e6e457eb5a43a34c85b7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2UAVZ7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEFQfD3v1pW3JbhMkK6n%2FQKhMnY%2B9mrMhUNDJ9FptOCLAiBEpW6vUYgpO6Q8Rts0cT%2F8IBrfFe%2FzPesv%2FRae3Amz%2BSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMY1iADUUSDvayRYZ6KtwDLGiGDXpXVID58RZc%2FouLGBbWbMFSUlJfTvWAndr3PZgkfZMU0ccF1fHBzawyaL%2F5BP04j4qat5BjTAUA%2FV6iTk1BRwPOv09t%2FU1UAo%2FTw5IZeW%2BY2mA3LpsBH%2FUaszRw9nvLYP3izN6EJq9HkEsKva0DJSevgFMa57CDywOY%2FXEvO%2Bhdj4IOLNW%2F%2F%2BnjBfjxVZctEeMDWcGM3ZSoNF41PQBbYdO1bzlxGGBqwU%2BMw3759lVf3%2Fm%2Fnx05SIaczKIDBwR9wBHyOO2aDI1C89u5vZlLKiIqtUB8NlS6Iqg3IkvWbW1L1WkQVQR4e8srJ1AXMTm5b8mec0XVrab3rjzSHSPSQUGmoNGhfLoM77nPH7fhJ8B077fDv%2BekZjVWuQ0lpEHp5rPtiL%2FJHjJV1%2FFKTFGAs6KjhNk3taRmbc9NMq5sG6VH%2FX6p3CC0CE3PZxe6q1OZafvughBPM0IZn5sSBKIOCnHx3D2aK%2Bim2obkou39%2BvUAJTLBxKm%2FD2j8UD2TNKen0csLQjgx7dtGDFwjT%2Bik%2BCDxf0HVqspg8YMdrwDGgm8MjMwaR7paqnM9vCLYR4dJCSr1aVuKdXNtyrjP9rUodYKoxwFyBIEOLJBhn3f%2B3vXQ981%2FYKVRKtcwq%2BPPyAY6pgFVvK1ammDLCtzKOaWnsLDX%2BZmQdCXhD2%2B6oazvefibqfh2Gbk9K5FcL%2BXOi5%2BttJS2MWcBsy8aIaZNo5yZdFmKP%2BjZ%2BeGE%2BwRa%2BaBdOjdfSef7C3r7llUzn9GaNLNdUhGDvPNGgZU92PmAmx7t8snbMWFdVMoS1Y%2BWngLsL6QerrknXJzSJwECo4I7SHLX3V8jlvrC9t2eM5RN5a95yJI9hXfb7Ial&X-Amz-Signature=9ce67525885c37feed2f9d81e7d4ac20645db111e979b448578363468d032b85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2UAVZ7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEFQfD3v1pW3JbhMkK6n%2FQKhMnY%2B9mrMhUNDJ9FptOCLAiBEpW6vUYgpO6Q8Rts0cT%2F8IBrfFe%2FzPesv%2FRae3Amz%2BSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMY1iADUUSDvayRYZ6KtwDLGiGDXpXVID58RZc%2FouLGBbWbMFSUlJfTvWAndr3PZgkfZMU0ccF1fHBzawyaL%2F5BP04j4qat5BjTAUA%2FV6iTk1BRwPOv09t%2FU1UAo%2FTw5IZeW%2BY2mA3LpsBH%2FUaszRw9nvLYP3izN6EJq9HkEsKva0DJSevgFMa57CDywOY%2FXEvO%2Bhdj4IOLNW%2F%2F%2BnjBfjxVZctEeMDWcGM3ZSoNF41PQBbYdO1bzlxGGBqwU%2BMw3759lVf3%2Fm%2Fnx05SIaczKIDBwR9wBHyOO2aDI1C89u5vZlLKiIqtUB8NlS6Iqg3IkvWbW1L1WkQVQR4e8srJ1AXMTm5b8mec0XVrab3rjzSHSPSQUGmoNGhfLoM77nPH7fhJ8B077fDv%2BekZjVWuQ0lpEHp5rPtiL%2FJHjJV1%2FFKTFGAs6KjhNk3taRmbc9NMq5sG6VH%2FX6p3CC0CE3PZxe6q1OZafvughBPM0IZn5sSBKIOCnHx3D2aK%2Bim2obkou39%2BvUAJTLBxKm%2FD2j8UD2TNKen0csLQjgx7dtGDFwjT%2Bik%2BCDxf0HVqspg8YMdrwDGgm8MjMwaR7paqnM9vCLYR4dJCSr1aVuKdXNtyrjP9rUodYKoxwFyBIEOLJBhn3f%2B3vXQ981%2FYKVRKtcwq%2BPPyAY6pgFVvK1ammDLCtzKOaWnsLDX%2BZmQdCXhD2%2B6oazvefibqfh2Gbk9K5FcL%2BXOi5%2BttJS2MWcBsy8aIaZNo5yZdFmKP%2BjZ%2BeGE%2BwRa%2BaBdOjdfSef7C3r7llUzn9GaNLNdUhGDvPNGgZU92PmAmx7t8snbMWFdVMoS1Y%2BWngLsL6QerrknXJzSJwECo4I7SHLX3V8jlvrC9t2eM5RN5a95yJI9hXfb7Ial&X-Amz-Signature=5472e989eff7b32d05c20413349e4dbed36ebfd1fb5a10cc2a8a967036f3591a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2UAVZ7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEFQfD3v1pW3JbhMkK6n%2FQKhMnY%2B9mrMhUNDJ9FptOCLAiBEpW6vUYgpO6Q8Rts0cT%2F8IBrfFe%2FzPesv%2FRae3Amz%2BSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMY1iADUUSDvayRYZ6KtwDLGiGDXpXVID58RZc%2FouLGBbWbMFSUlJfTvWAndr3PZgkfZMU0ccF1fHBzawyaL%2F5BP04j4qat5BjTAUA%2FV6iTk1BRwPOv09t%2FU1UAo%2FTw5IZeW%2BY2mA3LpsBH%2FUaszRw9nvLYP3izN6EJq9HkEsKva0DJSevgFMa57CDywOY%2FXEvO%2Bhdj4IOLNW%2F%2F%2BnjBfjxVZctEeMDWcGM3ZSoNF41PQBbYdO1bzlxGGBqwU%2BMw3759lVf3%2Fm%2Fnx05SIaczKIDBwR9wBHyOO2aDI1C89u5vZlLKiIqtUB8NlS6Iqg3IkvWbW1L1WkQVQR4e8srJ1AXMTm5b8mec0XVrab3rjzSHSPSQUGmoNGhfLoM77nPH7fhJ8B077fDv%2BekZjVWuQ0lpEHp5rPtiL%2FJHjJV1%2FFKTFGAs6KjhNk3taRmbc9NMq5sG6VH%2FX6p3CC0CE3PZxe6q1OZafvughBPM0IZn5sSBKIOCnHx3D2aK%2Bim2obkou39%2BvUAJTLBxKm%2FD2j8UD2TNKen0csLQjgx7dtGDFwjT%2Bik%2BCDxf0HVqspg8YMdrwDGgm8MjMwaR7paqnM9vCLYR4dJCSr1aVuKdXNtyrjP9rUodYKoxwFyBIEOLJBhn3f%2B3vXQ981%2FYKVRKtcwq%2BPPyAY6pgFVvK1ammDLCtzKOaWnsLDX%2BZmQdCXhD2%2B6oazvefibqfh2Gbk9K5FcL%2BXOi5%2BttJS2MWcBsy8aIaZNo5yZdFmKP%2BjZ%2BeGE%2BwRa%2BaBdOjdfSef7C3r7llUzn9GaNLNdUhGDvPNGgZU92PmAmx7t8snbMWFdVMoS1Y%2BWngLsL6QerrknXJzSJwECo4I7SHLX3V8jlvrC9t2eM5RN5a95yJI9hXfb7Ial&X-Amz-Signature=a70138bd5fe760ed71a58555a1a8c1f3e10b9906f888ffd17cf59d2ac5416a3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2UAVZ7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEFQfD3v1pW3JbhMkK6n%2FQKhMnY%2B9mrMhUNDJ9FptOCLAiBEpW6vUYgpO6Q8Rts0cT%2F8IBrfFe%2FzPesv%2FRae3Amz%2BSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMY1iADUUSDvayRYZ6KtwDLGiGDXpXVID58RZc%2FouLGBbWbMFSUlJfTvWAndr3PZgkfZMU0ccF1fHBzawyaL%2F5BP04j4qat5BjTAUA%2FV6iTk1BRwPOv09t%2FU1UAo%2FTw5IZeW%2BY2mA3LpsBH%2FUaszRw9nvLYP3izN6EJq9HkEsKva0DJSevgFMa57CDywOY%2FXEvO%2Bhdj4IOLNW%2F%2F%2BnjBfjxVZctEeMDWcGM3ZSoNF41PQBbYdO1bzlxGGBqwU%2BMw3759lVf3%2Fm%2Fnx05SIaczKIDBwR9wBHyOO2aDI1C89u5vZlLKiIqtUB8NlS6Iqg3IkvWbW1L1WkQVQR4e8srJ1AXMTm5b8mec0XVrab3rjzSHSPSQUGmoNGhfLoM77nPH7fhJ8B077fDv%2BekZjVWuQ0lpEHp5rPtiL%2FJHjJV1%2FFKTFGAs6KjhNk3taRmbc9NMq5sG6VH%2FX6p3CC0CE3PZxe6q1OZafvughBPM0IZn5sSBKIOCnHx3D2aK%2Bim2obkou39%2BvUAJTLBxKm%2FD2j8UD2TNKen0csLQjgx7dtGDFwjT%2Bik%2BCDxf0HVqspg8YMdrwDGgm8MjMwaR7paqnM9vCLYR4dJCSr1aVuKdXNtyrjP9rUodYKoxwFyBIEOLJBhn3f%2B3vXQ981%2FYKVRKtcwq%2BPPyAY6pgFVvK1ammDLCtzKOaWnsLDX%2BZmQdCXhD2%2B6oazvefibqfh2Gbk9K5FcL%2BXOi5%2BttJS2MWcBsy8aIaZNo5yZdFmKP%2BjZ%2BeGE%2BwRa%2BaBdOjdfSef7C3r7llUzn9GaNLNdUhGDvPNGgZU92PmAmx7t8snbMWFdVMoS1Y%2BWngLsL6QerrknXJzSJwECo4I7SHLX3V8jlvrC9t2eM5RN5a95yJI9hXfb7Ial&X-Amz-Signature=277ce3a7761613767bc6710fb7a2d82feff683af752200f58743812cf9b1e6cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2UAVZ7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEFQfD3v1pW3JbhMkK6n%2FQKhMnY%2B9mrMhUNDJ9FptOCLAiBEpW6vUYgpO6Q8Rts0cT%2F8IBrfFe%2FzPesv%2FRae3Amz%2BSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMY1iADUUSDvayRYZ6KtwDLGiGDXpXVID58RZc%2FouLGBbWbMFSUlJfTvWAndr3PZgkfZMU0ccF1fHBzawyaL%2F5BP04j4qat5BjTAUA%2FV6iTk1BRwPOv09t%2FU1UAo%2FTw5IZeW%2BY2mA3LpsBH%2FUaszRw9nvLYP3izN6EJq9HkEsKva0DJSevgFMa57CDywOY%2FXEvO%2Bhdj4IOLNW%2F%2F%2BnjBfjxVZctEeMDWcGM3ZSoNF41PQBbYdO1bzlxGGBqwU%2BMw3759lVf3%2Fm%2Fnx05SIaczKIDBwR9wBHyOO2aDI1C89u5vZlLKiIqtUB8NlS6Iqg3IkvWbW1L1WkQVQR4e8srJ1AXMTm5b8mec0XVrab3rjzSHSPSQUGmoNGhfLoM77nPH7fhJ8B077fDv%2BekZjVWuQ0lpEHp5rPtiL%2FJHjJV1%2FFKTFGAs6KjhNk3taRmbc9NMq5sG6VH%2FX6p3CC0CE3PZxe6q1OZafvughBPM0IZn5sSBKIOCnHx3D2aK%2Bim2obkou39%2BvUAJTLBxKm%2FD2j8UD2TNKen0csLQjgx7dtGDFwjT%2Bik%2BCDxf0HVqspg8YMdrwDGgm8MjMwaR7paqnM9vCLYR4dJCSr1aVuKdXNtyrjP9rUodYKoxwFyBIEOLJBhn3f%2B3vXQ981%2FYKVRKtcwq%2BPPyAY6pgFVvK1ammDLCtzKOaWnsLDX%2BZmQdCXhD2%2B6oazvefibqfh2Gbk9K5FcL%2BXOi5%2BttJS2MWcBsy8aIaZNo5yZdFmKP%2BjZ%2BeGE%2BwRa%2BaBdOjdfSef7C3r7llUzn9GaNLNdUhGDvPNGgZU92PmAmx7t8snbMWFdVMoS1Y%2BWngLsL6QerrknXJzSJwECo4I7SHLX3V8jlvrC9t2eM5RN5a95yJI9hXfb7Ial&X-Amz-Signature=96774fe10c69cb7aae77138fc684695247d8b816d1fc4b1e8e42049d296e563b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2UAVZ7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEFQfD3v1pW3JbhMkK6n%2FQKhMnY%2B9mrMhUNDJ9FptOCLAiBEpW6vUYgpO6Q8Rts0cT%2F8IBrfFe%2FzPesv%2FRae3Amz%2BSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMY1iADUUSDvayRYZ6KtwDLGiGDXpXVID58RZc%2FouLGBbWbMFSUlJfTvWAndr3PZgkfZMU0ccF1fHBzawyaL%2F5BP04j4qat5BjTAUA%2FV6iTk1BRwPOv09t%2FU1UAo%2FTw5IZeW%2BY2mA3LpsBH%2FUaszRw9nvLYP3izN6EJq9HkEsKva0DJSevgFMa57CDywOY%2FXEvO%2Bhdj4IOLNW%2F%2F%2BnjBfjxVZctEeMDWcGM3ZSoNF41PQBbYdO1bzlxGGBqwU%2BMw3759lVf3%2Fm%2Fnx05SIaczKIDBwR9wBHyOO2aDI1C89u5vZlLKiIqtUB8NlS6Iqg3IkvWbW1L1WkQVQR4e8srJ1AXMTm5b8mec0XVrab3rjzSHSPSQUGmoNGhfLoM77nPH7fhJ8B077fDv%2BekZjVWuQ0lpEHp5rPtiL%2FJHjJV1%2FFKTFGAs6KjhNk3taRmbc9NMq5sG6VH%2FX6p3CC0CE3PZxe6q1OZafvughBPM0IZn5sSBKIOCnHx3D2aK%2Bim2obkou39%2BvUAJTLBxKm%2FD2j8UD2TNKen0csLQjgx7dtGDFwjT%2Bik%2BCDxf0HVqspg8YMdrwDGgm8MjMwaR7paqnM9vCLYR4dJCSr1aVuKdXNtyrjP9rUodYKoxwFyBIEOLJBhn3f%2B3vXQ981%2FYKVRKtcwq%2BPPyAY6pgFVvK1ammDLCtzKOaWnsLDX%2BZmQdCXhD2%2B6oazvefibqfh2Gbk9K5FcL%2BXOi5%2BttJS2MWcBsy8aIaZNo5yZdFmKP%2BjZ%2BeGE%2BwRa%2BaBdOjdfSef7C3r7llUzn9GaNLNdUhGDvPNGgZU92PmAmx7t8snbMWFdVMoS1Y%2BWngLsL6QerrknXJzSJwECo4I7SHLX3V8jlvrC9t2eM5RN5a95yJI9hXfb7Ial&X-Amz-Signature=702dd3a97e782634e22a8e093a41f9517994d8e6fc4a7495b5e7c01c75dd5c5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2UAVZ7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEFQfD3v1pW3JbhMkK6n%2FQKhMnY%2B9mrMhUNDJ9FptOCLAiBEpW6vUYgpO6Q8Rts0cT%2F8IBrfFe%2FzPesv%2FRae3Amz%2BSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMY1iADUUSDvayRYZ6KtwDLGiGDXpXVID58RZc%2FouLGBbWbMFSUlJfTvWAndr3PZgkfZMU0ccF1fHBzawyaL%2F5BP04j4qat5BjTAUA%2FV6iTk1BRwPOv09t%2FU1UAo%2FTw5IZeW%2BY2mA3LpsBH%2FUaszRw9nvLYP3izN6EJq9HkEsKva0DJSevgFMa57CDywOY%2FXEvO%2Bhdj4IOLNW%2F%2F%2BnjBfjxVZctEeMDWcGM3ZSoNF41PQBbYdO1bzlxGGBqwU%2BMw3759lVf3%2Fm%2Fnx05SIaczKIDBwR9wBHyOO2aDI1C89u5vZlLKiIqtUB8NlS6Iqg3IkvWbW1L1WkQVQR4e8srJ1AXMTm5b8mec0XVrab3rjzSHSPSQUGmoNGhfLoM77nPH7fhJ8B077fDv%2BekZjVWuQ0lpEHp5rPtiL%2FJHjJV1%2FFKTFGAs6KjhNk3taRmbc9NMq5sG6VH%2FX6p3CC0CE3PZxe6q1OZafvughBPM0IZn5sSBKIOCnHx3D2aK%2Bim2obkou39%2BvUAJTLBxKm%2FD2j8UD2TNKen0csLQjgx7dtGDFwjT%2Bik%2BCDxf0HVqspg8YMdrwDGgm8MjMwaR7paqnM9vCLYR4dJCSr1aVuKdXNtyrjP9rUodYKoxwFyBIEOLJBhn3f%2B3vXQ981%2FYKVRKtcwq%2BPPyAY6pgFVvK1ammDLCtzKOaWnsLDX%2BZmQdCXhD2%2B6oazvefibqfh2Gbk9K5FcL%2BXOi5%2BttJS2MWcBsy8aIaZNo5yZdFmKP%2BjZ%2BeGE%2BwRa%2BaBdOjdfSef7C3r7llUzn9GaNLNdUhGDvPNGgZU92PmAmx7t8snbMWFdVMoS1Y%2BWngLsL6QerrknXJzSJwECo4I7SHLX3V8jlvrC9t2eM5RN5a95yJI9hXfb7Ial&X-Amz-Signature=1caec60a56f4b101e0497aa7235606ba6da73d05b8569135cc0d2813c9032bfe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2UAVZ7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIEFQfD3v1pW3JbhMkK6n%2FQKhMnY%2B9mrMhUNDJ9FptOCLAiBEpW6vUYgpO6Q8Rts0cT%2F8IBrfFe%2FzPesv%2FRae3Amz%2BSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMY1iADUUSDvayRYZ6KtwDLGiGDXpXVID58RZc%2FouLGBbWbMFSUlJfTvWAndr3PZgkfZMU0ccF1fHBzawyaL%2F5BP04j4qat5BjTAUA%2FV6iTk1BRwPOv09t%2FU1UAo%2FTw5IZeW%2BY2mA3LpsBH%2FUaszRw9nvLYP3izN6EJq9HkEsKva0DJSevgFMa57CDywOY%2FXEvO%2Bhdj4IOLNW%2F%2F%2BnjBfjxVZctEeMDWcGM3ZSoNF41PQBbYdO1bzlxGGBqwU%2BMw3759lVf3%2Fm%2Fnx05SIaczKIDBwR9wBHyOO2aDI1C89u5vZlLKiIqtUB8NlS6Iqg3IkvWbW1L1WkQVQR4e8srJ1AXMTm5b8mec0XVrab3rjzSHSPSQUGmoNGhfLoM77nPH7fhJ8B077fDv%2BekZjVWuQ0lpEHp5rPtiL%2FJHjJV1%2FFKTFGAs6KjhNk3taRmbc9NMq5sG6VH%2FX6p3CC0CE3PZxe6q1OZafvughBPM0IZn5sSBKIOCnHx3D2aK%2Bim2obkou39%2BvUAJTLBxKm%2FD2j8UD2TNKen0csLQjgx7dtGDFwjT%2Bik%2BCDxf0HVqspg8YMdrwDGgm8MjMwaR7paqnM9vCLYR4dJCSr1aVuKdXNtyrjP9rUodYKoxwFyBIEOLJBhn3f%2B3vXQ981%2FYKVRKtcwq%2BPPyAY6pgFVvK1ammDLCtzKOaWnsLDX%2BZmQdCXhD2%2B6oazvefibqfh2Gbk9K5FcL%2BXOi5%2BttJS2MWcBsy8aIaZNo5yZdFmKP%2BjZ%2BeGE%2BwRa%2BaBdOjdfSef7C3r7llUzn9GaNLNdUhGDvPNGgZU92PmAmx7t8snbMWFdVMoS1Y%2BWngLsL6QerrknXJzSJwECo4I7SHLX3V8jlvrC9t2eM5RN5a95yJI9hXfb7Ial&X-Amz-Signature=ad08ae5e043cf49a97f4e6a2309299c83422c41be9aaf399dc2de8013c6cd201&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

