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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI7JFREO%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTJoBsF%2F7Xg1GYlO7vSJztBlFQpbcoAgepGpB7JIrvwQIhAJ7KRKykjg78nSEHvaN1sHrtUg0vMA7Mkawrv4Z5N3w%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbMUGGhFm5pmHC1NAq3APNuFjHMZTaN2zhuqw0VeK2f6EcXUF69DPiW43XJsd%2FBn8fuV9pQ9trZOonpcCUr6g3FJ4eociYzzsL1F6WhtnkLT0pmgxG9uGtQZSGg0aYPlkrXoW3zEIaIOP770CYk%2FzCrTdXb9KmloMF48DZAFsSZWbl8y1QEDnlHoYVaWnp4z7fsI9bynOcy%2BVbtWoNXLcEEcwy%2BJECnqWB6BSO16WsybMW2MAgO8n5AoutPYo0cMKxdeMIY%2BQTXYDB7KhB%2BM1evGnXgh%2BAFDqrWwN0pozYGOoaV%2FD5TMfbRgPbaXcKM8WmGyA64s1x4lQH%2FIQG7r8SNDmdM2Aj2jqbF%2BczFXcoY3p%2F0K2k%2FR3%2BDVCrFXXcf%2B9iYYhNHyzf6hJMLwIAj9tFTllWA%2Fx6oOsqYZKnbaRbl%2BCfueUU%2FTkz6jhRJfr%2B5iJEw3aj%2F0XwUXvpYTK4qA0jIbNLfdUFPIZsIRn53tySg36El8YYI5fOCrXFtq7wAqDx%2FuH9Y2b0SsXVau5whIYY%2FVe9nULCd6ydO3Mphp%2BM8q9Sr0K6bGqcVuFCp4gDZExlMjyaxFcdVc7PP4XXxpQePWV6y6QC43rX2IgT%2FggbaNqvsW0WAnTQxWA3%2BJj%2FolKC3KqnytpqClFl%2BjCDxIHLBjqkAQVC9wMFYn5m2AXuOMc67RhZFdYmFN6KTrrSR%2FvOqXoqQhQiIxFWW%2BmWcnEiO9Iy2gxwFIX1DmSsfQKfLxJJ%2F%2F9P1dwslYz0xh8F7HIceXGidTnBfrTkC%2BQguqWDiWd6OiIH96Wmf0y5mihpDfTQVhChomzo5S2iOf%2FrR7yuuWUjRUyrVbXtccnTtWekmf4A9uPvr%2F2KbQfBMOLPZxWvmibzGjXx&X-Amz-Signature=1060fd5476be60b5b8137693ce79a0e20eaafb1c376b08ab93f1f9736358b8b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI7JFREO%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTJoBsF%2F7Xg1GYlO7vSJztBlFQpbcoAgepGpB7JIrvwQIhAJ7KRKykjg78nSEHvaN1sHrtUg0vMA7Mkawrv4Z5N3w%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbMUGGhFm5pmHC1NAq3APNuFjHMZTaN2zhuqw0VeK2f6EcXUF69DPiW43XJsd%2FBn8fuV9pQ9trZOonpcCUr6g3FJ4eociYzzsL1F6WhtnkLT0pmgxG9uGtQZSGg0aYPlkrXoW3zEIaIOP770CYk%2FzCrTdXb9KmloMF48DZAFsSZWbl8y1QEDnlHoYVaWnp4z7fsI9bynOcy%2BVbtWoNXLcEEcwy%2BJECnqWB6BSO16WsybMW2MAgO8n5AoutPYo0cMKxdeMIY%2BQTXYDB7KhB%2BM1evGnXgh%2BAFDqrWwN0pozYGOoaV%2FD5TMfbRgPbaXcKM8WmGyA64s1x4lQH%2FIQG7r8SNDmdM2Aj2jqbF%2BczFXcoY3p%2F0K2k%2FR3%2BDVCrFXXcf%2B9iYYhNHyzf6hJMLwIAj9tFTllWA%2Fx6oOsqYZKnbaRbl%2BCfueUU%2FTkz6jhRJfr%2B5iJEw3aj%2F0XwUXvpYTK4qA0jIbNLfdUFPIZsIRn53tySg36El8YYI5fOCrXFtq7wAqDx%2FuH9Y2b0SsXVau5whIYY%2FVe9nULCd6ydO3Mphp%2BM8q9Sr0K6bGqcVuFCp4gDZExlMjyaxFcdVc7PP4XXxpQePWV6y6QC43rX2IgT%2FggbaNqvsW0WAnTQxWA3%2BJj%2FolKC3KqnytpqClFl%2BjCDxIHLBjqkAQVC9wMFYn5m2AXuOMc67RhZFdYmFN6KTrrSR%2FvOqXoqQhQiIxFWW%2BmWcnEiO9Iy2gxwFIX1DmSsfQKfLxJJ%2F%2F9P1dwslYz0xh8F7HIceXGidTnBfrTkC%2BQguqWDiWd6OiIH96Wmf0y5mihpDfTQVhChomzo5S2iOf%2FrR7yuuWUjRUyrVbXtccnTtWekmf4A9uPvr%2F2KbQfBMOLPZxWvmibzGjXx&X-Amz-Signature=a6283e66d2af8574eb3175c9ccc54bbf7667a5c72b91384183b7a5d29a94f4a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI7JFREO%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTJoBsF%2F7Xg1GYlO7vSJztBlFQpbcoAgepGpB7JIrvwQIhAJ7KRKykjg78nSEHvaN1sHrtUg0vMA7Mkawrv4Z5N3w%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbMUGGhFm5pmHC1NAq3APNuFjHMZTaN2zhuqw0VeK2f6EcXUF69DPiW43XJsd%2FBn8fuV9pQ9trZOonpcCUr6g3FJ4eociYzzsL1F6WhtnkLT0pmgxG9uGtQZSGg0aYPlkrXoW3zEIaIOP770CYk%2FzCrTdXb9KmloMF48DZAFsSZWbl8y1QEDnlHoYVaWnp4z7fsI9bynOcy%2BVbtWoNXLcEEcwy%2BJECnqWB6BSO16WsybMW2MAgO8n5AoutPYo0cMKxdeMIY%2BQTXYDB7KhB%2BM1evGnXgh%2BAFDqrWwN0pozYGOoaV%2FD5TMfbRgPbaXcKM8WmGyA64s1x4lQH%2FIQG7r8SNDmdM2Aj2jqbF%2BczFXcoY3p%2F0K2k%2FR3%2BDVCrFXXcf%2B9iYYhNHyzf6hJMLwIAj9tFTllWA%2Fx6oOsqYZKnbaRbl%2BCfueUU%2FTkz6jhRJfr%2B5iJEw3aj%2F0XwUXvpYTK4qA0jIbNLfdUFPIZsIRn53tySg36El8YYI5fOCrXFtq7wAqDx%2FuH9Y2b0SsXVau5whIYY%2FVe9nULCd6ydO3Mphp%2BM8q9Sr0K6bGqcVuFCp4gDZExlMjyaxFcdVc7PP4XXxpQePWV6y6QC43rX2IgT%2FggbaNqvsW0WAnTQxWA3%2BJj%2FolKC3KqnytpqClFl%2BjCDxIHLBjqkAQVC9wMFYn5m2AXuOMc67RhZFdYmFN6KTrrSR%2FvOqXoqQhQiIxFWW%2BmWcnEiO9Iy2gxwFIX1DmSsfQKfLxJJ%2F%2F9P1dwslYz0xh8F7HIceXGidTnBfrTkC%2BQguqWDiWd6OiIH96Wmf0y5mihpDfTQVhChomzo5S2iOf%2FrR7yuuWUjRUyrVbXtccnTtWekmf4A9uPvr%2F2KbQfBMOLPZxWvmibzGjXx&X-Amz-Signature=a42c4921a7ae901ecc601311ffe1d76951fa564c80da7286d1e5582527d683fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI7JFREO%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTJoBsF%2F7Xg1GYlO7vSJztBlFQpbcoAgepGpB7JIrvwQIhAJ7KRKykjg78nSEHvaN1sHrtUg0vMA7Mkawrv4Z5N3w%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbMUGGhFm5pmHC1NAq3APNuFjHMZTaN2zhuqw0VeK2f6EcXUF69DPiW43XJsd%2FBn8fuV9pQ9trZOonpcCUr6g3FJ4eociYzzsL1F6WhtnkLT0pmgxG9uGtQZSGg0aYPlkrXoW3zEIaIOP770CYk%2FzCrTdXb9KmloMF48DZAFsSZWbl8y1QEDnlHoYVaWnp4z7fsI9bynOcy%2BVbtWoNXLcEEcwy%2BJECnqWB6BSO16WsybMW2MAgO8n5AoutPYo0cMKxdeMIY%2BQTXYDB7KhB%2BM1evGnXgh%2BAFDqrWwN0pozYGOoaV%2FD5TMfbRgPbaXcKM8WmGyA64s1x4lQH%2FIQG7r8SNDmdM2Aj2jqbF%2BczFXcoY3p%2F0K2k%2FR3%2BDVCrFXXcf%2B9iYYhNHyzf6hJMLwIAj9tFTllWA%2Fx6oOsqYZKnbaRbl%2BCfueUU%2FTkz6jhRJfr%2B5iJEw3aj%2F0XwUXvpYTK4qA0jIbNLfdUFPIZsIRn53tySg36El8YYI5fOCrXFtq7wAqDx%2FuH9Y2b0SsXVau5whIYY%2FVe9nULCd6ydO3Mphp%2BM8q9Sr0K6bGqcVuFCp4gDZExlMjyaxFcdVc7PP4XXxpQePWV6y6QC43rX2IgT%2FggbaNqvsW0WAnTQxWA3%2BJj%2FolKC3KqnytpqClFl%2BjCDxIHLBjqkAQVC9wMFYn5m2AXuOMc67RhZFdYmFN6KTrrSR%2FvOqXoqQhQiIxFWW%2BmWcnEiO9Iy2gxwFIX1DmSsfQKfLxJJ%2F%2F9P1dwslYz0xh8F7HIceXGidTnBfrTkC%2BQguqWDiWd6OiIH96Wmf0y5mihpDfTQVhChomzo5S2iOf%2FrR7yuuWUjRUyrVbXtccnTtWekmf4A9uPvr%2F2KbQfBMOLPZxWvmibzGjXx&X-Amz-Signature=6bd1abdc00342ed5779dcdead131bcc4b9e26502d94c957d4a43f101adce47b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI7JFREO%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTJoBsF%2F7Xg1GYlO7vSJztBlFQpbcoAgepGpB7JIrvwQIhAJ7KRKykjg78nSEHvaN1sHrtUg0vMA7Mkawrv4Z5N3w%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbMUGGhFm5pmHC1NAq3APNuFjHMZTaN2zhuqw0VeK2f6EcXUF69DPiW43XJsd%2FBn8fuV9pQ9trZOonpcCUr6g3FJ4eociYzzsL1F6WhtnkLT0pmgxG9uGtQZSGg0aYPlkrXoW3zEIaIOP770CYk%2FzCrTdXb9KmloMF48DZAFsSZWbl8y1QEDnlHoYVaWnp4z7fsI9bynOcy%2BVbtWoNXLcEEcwy%2BJECnqWB6BSO16WsybMW2MAgO8n5AoutPYo0cMKxdeMIY%2BQTXYDB7KhB%2BM1evGnXgh%2BAFDqrWwN0pozYGOoaV%2FD5TMfbRgPbaXcKM8WmGyA64s1x4lQH%2FIQG7r8SNDmdM2Aj2jqbF%2BczFXcoY3p%2F0K2k%2FR3%2BDVCrFXXcf%2B9iYYhNHyzf6hJMLwIAj9tFTllWA%2Fx6oOsqYZKnbaRbl%2BCfueUU%2FTkz6jhRJfr%2B5iJEw3aj%2F0XwUXvpYTK4qA0jIbNLfdUFPIZsIRn53tySg36El8YYI5fOCrXFtq7wAqDx%2FuH9Y2b0SsXVau5whIYY%2FVe9nULCd6ydO3Mphp%2BM8q9Sr0K6bGqcVuFCp4gDZExlMjyaxFcdVc7PP4XXxpQePWV6y6QC43rX2IgT%2FggbaNqvsW0WAnTQxWA3%2BJj%2FolKC3KqnytpqClFl%2BjCDxIHLBjqkAQVC9wMFYn5m2AXuOMc67RhZFdYmFN6KTrrSR%2FvOqXoqQhQiIxFWW%2BmWcnEiO9Iy2gxwFIX1DmSsfQKfLxJJ%2F%2F9P1dwslYz0xh8F7HIceXGidTnBfrTkC%2BQguqWDiWd6OiIH96Wmf0y5mihpDfTQVhChomzo5S2iOf%2FrR7yuuWUjRUyrVbXtccnTtWekmf4A9uPvr%2F2KbQfBMOLPZxWvmibzGjXx&X-Amz-Signature=e82e6803abe71c09c56baabcbcf5a683d8b567d4709977c93150f16c3977196d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI7JFREO%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTJoBsF%2F7Xg1GYlO7vSJztBlFQpbcoAgepGpB7JIrvwQIhAJ7KRKykjg78nSEHvaN1sHrtUg0vMA7Mkawrv4Z5N3w%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbMUGGhFm5pmHC1NAq3APNuFjHMZTaN2zhuqw0VeK2f6EcXUF69DPiW43XJsd%2FBn8fuV9pQ9trZOonpcCUr6g3FJ4eociYzzsL1F6WhtnkLT0pmgxG9uGtQZSGg0aYPlkrXoW3zEIaIOP770CYk%2FzCrTdXb9KmloMF48DZAFsSZWbl8y1QEDnlHoYVaWnp4z7fsI9bynOcy%2BVbtWoNXLcEEcwy%2BJECnqWB6BSO16WsybMW2MAgO8n5AoutPYo0cMKxdeMIY%2BQTXYDB7KhB%2BM1evGnXgh%2BAFDqrWwN0pozYGOoaV%2FD5TMfbRgPbaXcKM8WmGyA64s1x4lQH%2FIQG7r8SNDmdM2Aj2jqbF%2BczFXcoY3p%2F0K2k%2FR3%2BDVCrFXXcf%2B9iYYhNHyzf6hJMLwIAj9tFTllWA%2Fx6oOsqYZKnbaRbl%2BCfueUU%2FTkz6jhRJfr%2B5iJEw3aj%2F0XwUXvpYTK4qA0jIbNLfdUFPIZsIRn53tySg36El8YYI5fOCrXFtq7wAqDx%2FuH9Y2b0SsXVau5whIYY%2FVe9nULCd6ydO3Mphp%2BM8q9Sr0K6bGqcVuFCp4gDZExlMjyaxFcdVc7PP4XXxpQePWV6y6QC43rX2IgT%2FggbaNqvsW0WAnTQxWA3%2BJj%2FolKC3KqnytpqClFl%2BjCDxIHLBjqkAQVC9wMFYn5m2AXuOMc67RhZFdYmFN6KTrrSR%2FvOqXoqQhQiIxFWW%2BmWcnEiO9Iy2gxwFIX1DmSsfQKfLxJJ%2F%2F9P1dwslYz0xh8F7HIceXGidTnBfrTkC%2BQguqWDiWd6OiIH96Wmf0y5mihpDfTQVhChomzo5S2iOf%2FrR7yuuWUjRUyrVbXtccnTtWekmf4A9uPvr%2F2KbQfBMOLPZxWvmibzGjXx&X-Amz-Signature=47d82245f5efb461085c2c206368e507a7fef2676cfce9c7f76d3fa408c4d93e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI7JFREO%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTJoBsF%2F7Xg1GYlO7vSJztBlFQpbcoAgepGpB7JIrvwQIhAJ7KRKykjg78nSEHvaN1sHrtUg0vMA7Mkawrv4Z5N3w%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbMUGGhFm5pmHC1NAq3APNuFjHMZTaN2zhuqw0VeK2f6EcXUF69DPiW43XJsd%2FBn8fuV9pQ9trZOonpcCUr6g3FJ4eociYzzsL1F6WhtnkLT0pmgxG9uGtQZSGg0aYPlkrXoW3zEIaIOP770CYk%2FzCrTdXb9KmloMF48DZAFsSZWbl8y1QEDnlHoYVaWnp4z7fsI9bynOcy%2BVbtWoNXLcEEcwy%2BJECnqWB6BSO16WsybMW2MAgO8n5AoutPYo0cMKxdeMIY%2BQTXYDB7KhB%2BM1evGnXgh%2BAFDqrWwN0pozYGOoaV%2FD5TMfbRgPbaXcKM8WmGyA64s1x4lQH%2FIQG7r8SNDmdM2Aj2jqbF%2BczFXcoY3p%2F0K2k%2FR3%2BDVCrFXXcf%2B9iYYhNHyzf6hJMLwIAj9tFTllWA%2Fx6oOsqYZKnbaRbl%2BCfueUU%2FTkz6jhRJfr%2B5iJEw3aj%2F0XwUXvpYTK4qA0jIbNLfdUFPIZsIRn53tySg36El8YYI5fOCrXFtq7wAqDx%2FuH9Y2b0SsXVau5whIYY%2FVe9nULCd6ydO3Mphp%2BM8q9Sr0K6bGqcVuFCp4gDZExlMjyaxFcdVc7PP4XXxpQePWV6y6QC43rX2IgT%2FggbaNqvsW0WAnTQxWA3%2BJj%2FolKC3KqnytpqClFl%2BjCDxIHLBjqkAQVC9wMFYn5m2AXuOMc67RhZFdYmFN6KTrrSR%2FvOqXoqQhQiIxFWW%2BmWcnEiO9Iy2gxwFIX1DmSsfQKfLxJJ%2F%2F9P1dwslYz0xh8F7HIceXGidTnBfrTkC%2BQguqWDiWd6OiIH96Wmf0y5mihpDfTQVhChomzo5S2iOf%2FrR7yuuWUjRUyrVbXtccnTtWekmf4A9uPvr%2F2KbQfBMOLPZxWvmibzGjXx&X-Amz-Signature=0d2c3421ffb2b44c1fa49a9d0450435b5768feb1ac58f46c3345ac7309b84c4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI7JFREO%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTJoBsF%2F7Xg1GYlO7vSJztBlFQpbcoAgepGpB7JIrvwQIhAJ7KRKykjg78nSEHvaN1sHrtUg0vMA7Mkawrv4Z5N3w%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbMUGGhFm5pmHC1NAq3APNuFjHMZTaN2zhuqw0VeK2f6EcXUF69DPiW43XJsd%2FBn8fuV9pQ9trZOonpcCUr6g3FJ4eociYzzsL1F6WhtnkLT0pmgxG9uGtQZSGg0aYPlkrXoW3zEIaIOP770CYk%2FzCrTdXb9KmloMF48DZAFsSZWbl8y1QEDnlHoYVaWnp4z7fsI9bynOcy%2BVbtWoNXLcEEcwy%2BJECnqWB6BSO16WsybMW2MAgO8n5AoutPYo0cMKxdeMIY%2BQTXYDB7KhB%2BM1evGnXgh%2BAFDqrWwN0pozYGOoaV%2FD5TMfbRgPbaXcKM8WmGyA64s1x4lQH%2FIQG7r8SNDmdM2Aj2jqbF%2BczFXcoY3p%2F0K2k%2FR3%2BDVCrFXXcf%2B9iYYhNHyzf6hJMLwIAj9tFTllWA%2Fx6oOsqYZKnbaRbl%2BCfueUU%2FTkz6jhRJfr%2B5iJEw3aj%2F0XwUXvpYTK4qA0jIbNLfdUFPIZsIRn53tySg36El8YYI5fOCrXFtq7wAqDx%2FuH9Y2b0SsXVau5whIYY%2FVe9nULCd6ydO3Mphp%2BM8q9Sr0K6bGqcVuFCp4gDZExlMjyaxFcdVc7PP4XXxpQePWV6y6QC43rX2IgT%2FggbaNqvsW0WAnTQxWA3%2BJj%2FolKC3KqnytpqClFl%2BjCDxIHLBjqkAQVC9wMFYn5m2AXuOMc67RhZFdYmFN6KTrrSR%2FvOqXoqQhQiIxFWW%2BmWcnEiO9Iy2gxwFIX1DmSsfQKfLxJJ%2F%2F9P1dwslYz0xh8F7HIceXGidTnBfrTkC%2BQguqWDiWd6OiIH96Wmf0y5mihpDfTQVhChomzo5S2iOf%2FrR7yuuWUjRUyrVbXtccnTtWekmf4A9uPvr%2F2KbQfBMOLPZxWvmibzGjXx&X-Amz-Signature=d9361b4e6284ac179fb6ad028a05106b6cd12f2ae4a729b05df09e4959864143&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI7JFREO%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTJoBsF%2F7Xg1GYlO7vSJztBlFQpbcoAgepGpB7JIrvwQIhAJ7KRKykjg78nSEHvaN1sHrtUg0vMA7Mkawrv4Z5N3w%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbMUGGhFm5pmHC1NAq3APNuFjHMZTaN2zhuqw0VeK2f6EcXUF69DPiW43XJsd%2FBn8fuV9pQ9trZOonpcCUr6g3FJ4eociYzzsL1F6WhtnkLT0pmgxG9uGtQZSGg0aYPlkrXoW3zEIaIOP770CYk%2FzCrTdXb9KmloMF48DZAFsSZWbl8y1QEDnlHoYVaWnp4z7fsI9bynOcy%2BVbtWoNXLcEEcwy%2BJECnqWB6BSO16WsybMW2MAgO8n5AoutPYo0cMKxdeMIY%2BQTXYDB7KhB%2BM1evGnXgh%2BAFDqrWwN0pozYGOoaV%2FD5TMfbRgPbaXcKM8WmGyA64s1x4lQH%2FIQG7r8SNDmdM2Aj2jqbF%2BczFXcoY3p%2F0K2k%2FR3%2BDVCrFXXcf%2B9iYYhNHyzf6hJMLwIAj9tFTllWA%2Fx6oOsqYZKnbaRbl%2BCfueUU%2FTkz6jhRJfr%2B5iJEw3aj%2F0XwUXvpYTK4qA0jIbNLfdUFPIZsIRn53tySg36El8YYI5fOCrXFtq7wAqDx%2FuH9Y2b0SsXVau5whIYY%2FVe9nULCd6ydO3Mphp%2BM8q9Sr0K6bGqcVuFCp4gDZExlMjyaxFcdVc7PP4XXxpQePWV6y6QC43rX2IgT%2FggbaNqvsW0WAnTQxWA3%2BJj%2FolKC3KqnytpqClFl%2BjCDxIHLBjqkAQVC9wMFYn5m2AXuOMc67RhZFdYmFN6KTrrSR%2FvOqXoqQhQiIxFWW%2BmWcnEiO9Iy2gxwFIX1DmSsfQKfLxJJ%2F%2F9P1dwslYz0xh8F7HIceXGidTnBfrTkC%2BQguqWDiWd6OiIH96Wmf0y5mihpDfTQVhChomzo5S2iOf%2FrR7yuuWUjRUyrVbXtccnTtWekmf4A9uPvr%2F2KbQfBMOLPZxWvmibzGjXx&X-Amz-Signature=9ce12cd9e3bbf6d1b14a30a9377718882ac1f4156933f4af0c19adb090ae3859&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI7JFREO%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTJoBsF%2F7Xg1GYlO7vSJztBlFQpbcoAgepGpB7JIrvwQIhAJ7KRKykjg78nSEHvaN1sHrtUg0vMA7Mkawrv4Z5N3w%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbMUGGhFm5pmHC1NAq3APNuFjHMZTaN2zhuqw0VeK2f6EcXUF69DPiW43XJsd%2FBn8fuV9pQ9trZOonpcCUr6g3FJ4eociYzzsL1F6WhtnkLT0pmgxG9uGtQZSGg0aYPlkrXoW3zEIaIOP770CYk%2FzCrTdXb9KmloMF48DZAFsSZWbl8y1QEDnlHoYVaWnp4z7fsI9bynOcy%2BVbtWoNXLcEEcwy%2BJECnqWB6BSO16WsybMW2MAgO8n5AoutPYo0cMKxdeMIY%2BQTXYDB7KhB%2BM1evGnXgh%2BAFDqrWwN0pozYGOoaV%2FD5TMfbRgPbaXcKM8WmGyA64s1x4lQH%2FIQG7r8SNDmdM2Aj2jqbF%2BczFXcoY3p%2F0K2k%2FR3%2BDVCrFXXcf%2B9iYYhNHyzf6hJMLwIAj9tFTllWA%2Fx6oOsqYZKnbaRbl%2BCfueUU%2FTkz6jhRJfr%2B5iJEw3aj%2F0XwUXvpYTK4qA0jIbNLfdUFPIZsIRn53tySg36El8YYI5fOCrXFtq7wAqDx%2FuH9Y2b0SsXVau5whIYY%2FVe9nULCd6ydO3Mphp%2BM8q9Sr0K6bGqcVuFCp4gDZExlMjyaxFcdVc7PP4XXxpQePWV6y6QC43rX2IgT%2FggbaNqvsW0WAnTQxWA3%2BJj%2FolKC3KqnytpqClFl%2BjCDxIHLBjqkAQVC9wMFYn5m2AXuOMc67RhZFdYmFN6KTrrSR%2FvOqXoqQhQiIxFWW%2BmWcnEiO9Iy2gxwFIX1DmSsfQKfLxJJ%2F%2F9P1dwslYz0xh8F7HIceXGidTnBfrTkC%2BQguqWDiWd6OiIH96Wmf0y5mihpDfTQVhChomzo5S2iOf%2FrR7yuuWUjRUyrVbXtccnTtWekmf4A9uPvr%2F2KbQfBMOLPZxWvmibzGjXx&X-Amz-Signature=8dda4854d3234bb79ac1f192f233fc26081f5eeec2ee71809d8cade37dc7f04f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

