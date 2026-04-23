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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S764CQMC%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4AygqKbyVA9krVulv0UZpgBH6ugSxn3lWmBMYdXjRvwIhAJZrPTVOXYANkXkH1VBQorGsnj%2F%2Bzxc0OJC9jarBhMG%2FKv8DCFwQABoMNjM3NDIzMTgzODA1Igw24QIWx3CywBhqIQQq3AODgpxWS0h8t0Ha9bE%2Fg9HhN2xN6f8BLoK28CrOX4V0eM7TU2imaPspU3UTEj0mEJHL2GVzcp%2B%2FSA6%2FWlnOsc9qhMcmop02Bj3RHwQJYYt8cFft%2BRs%2BRI9dw68YgXaJSgtR2jABlrvKbszcdtIiN%2Fq7XkrrcsudFYTvKdbHFd4yqmDK%2F1MOOZPRWAvWamO0wtg2L7rowh1uabPKFcwu8aHJ1J6md8qGQA2zGqAMXniKhGXER8Fgb3rFla9kjitaQPhrglBRYYOGbbWgk05%2BPNPWQaG1CwnJqZZXduUEa3nEDDoXCuirlamMa%2Fl%2B7G3lCQYrDx63mv7hT9SDyZlfoARyLwER%2FKAdod6OP9ho5z2%2Fqw3r827eHqnpbv7U31c4LCI77SMcjYfIcTjweBBgpMB5ODv9tk0KPhWFrlZgplxperTOYm3NpHNeHHSDNBNITUJIxjLC%2BzjjFxtGqNlvQOZSld9JgneFn%2B3v6RRPBlAF3YKDhv6eRiUWFu2UXFuq0S8gJ49nw2VW1CPJ8lYiRYMo6t6YldKfVwleqeG6Gax8L%2FknbTC%2BHlIh4f6hM2r8w%2FJH%2BojI%2BJtnVrflbpGaEvpyHOVDBUlKts2t%2Bkb7kq0p1aSWDKC7XVFVklF6cjDcmKbPBjqkAUjFi6wPUZBYw4Px4TWSWL%2BlGPRGjTBFvZiZc8SlYaOyPJFD9UxrxLE8uPfDiTsPOaRggTDnnmY5VCGXzDnMz2FxmnNfIyCVVYN13DSCtV58v1LQiRKYjn95kYM3CGkZFBs4AT6t%2BiSKS5dmUGxUawQiKEqWkbV0lYMjYHzUs9pUdz8grXkabDFAgnTH5gvWASwpE135B5nv1%2BH9LRJLp4TxXjWw&X-Amz-Signature=11d36b102982aca1aeefc741abdd80659f67bf5e4a29fe511246e02a7aca3304&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S764CQMC%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4AygqKbyVA9krVulv0UZpgBH6ugSxn3lWmBMYdXjRvwIhAJZrPTVOXYANkXkH1VBQorGsnj%2F%2Bzxc0OJC9jarBhMG%2FKv8DCFwQABoMNjM3NDIzMTgzODA1Igw24QIWx3CywBhqIQQq3AODgpxWS0h8t0Ha9bE%2Fg9HhN2xN6f8BLoK28CrOX4V0eM7TU2imaPspU3UTEj0mEJHL2GVzcp%2B%2FSA6%2FWlnOsc9qhMcmop02Bj3RHwQJYYt8cFft%2BRs%2BRI9dw68YgXaJSgtR2jABlrvKbszcdtIiN%2Fq7XkrrcsudFYTvKdbHFd4yqmDK%2F1MOOZPRWAvWamO0wtg2L7rowh1uabPKFcwu8aHJ1J6md8qGQA2zGqAMXniKhGXER8Fgb3rFla9kjitaQPhrglBRYYOGbbWgk05%2BPNPWQaG1CwnJqZZXduUEa3nEDDoXCuirlamMa%2Fl%2B7G3lCQYrDx63mv7hT9SDyZlfoARyLwER%2FKAdod6OP9ho5z2%2Fqw3r827eHqnpbv7U31c4LCI77SMcjYfIcTjweBBgpMB5ODv9tk0KPhWFrlZgplxperTOYm3NpHNeHHSDNBNITUJIxjLC%2BzjjFxtGqNlvQOZSld9JgneFn%2B3v6RRPBlAF3YKDhv6eRiUWFu2UXFuq0S8gJ49nw2VW1CPJ8lYiRYMo6t6YldKfVwleqeG6Gax8L%2FknbTC%2BHlIh4f6hM2r8w%2FJH%2BojI%2BJtnVrflbpGaEvpyHOVDBUlKts2t%2Bkb7kq0p1aSWDKC7XVFVklF6cjDcmKbPBjqkAUjFi6wPUZBYw4Px4TWSWL%2BlGPRGjTBFvZiZc8SlYaOyPJFD9UxrxLE8uPfDiTsPOaRggTDnnmY5VCGXzDnMz2FxmnNfIyCVVYN13DSCtV58v1LQiRKYjn95kYM3CGkZFBs4AT6t%2BiSKS5dmUGxUawQiKEqWkbV0lYMjYHzUs9pUdz8grXkabDFAgnTH5gvWASwpE135B5nv1%2BH9LRJLp4TxXjWw&X-Amz-Signature=8c532057e4081b95a7f9cdc43142a3da155098f513c739c8fbeefa219bb9ad1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S764CQMC%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4AygqKbyVA9krVulv0UZpgBH6ugSxn3lWmBMYdXjRvwIhAJZrPTVOXYANkXkH1VBQorGsnj%2F%2Bzxc0OJC9jarBhMG%2FKv8DCFwQABoMNjM3NDIzMTgzODA1Igw24QIWx3CywBhqIQQq3AODgpxWS0h8t0Ha9bE%2Fg9HhN2xN6f8BLoK28CrOX4V0eM7TU2imaPspU3UTEj0mEJHL2GVzcp%2B%2FSA6%2FWlnOsc9qhMcmop02Bj3RHwQJYYt8cFft%2BRs%2BRI9dw68YgXaJSgtR2jABlrvKbszcdtIiN%2Fq7XkrrcsudFYTvKdbHFd4yqmDK%2F1MOOZPRWAvWamO0wtg2L7rowh1uabPKFcwu8aHJ1J6md8qGQA2zGqAMXniKhGXER8Fgb3rFla9kjitaQPhrglBRYYOGbbWgk05%2BPNPWQaG1CwnJqZZXduUEa3nEDDoXCuirlamMa%2Fl%2B7G3lCQYrDx63mv7hT9SDyZlfoARyLwER%2FKAdod6OP9ho5z2%2Fqw3r827eHqnpbv7U31c4LCI77SMcjYfIcTjweBBgpMB5ODv9tk0KPhWFrlZgplxperTOYm3NpHNeHHSDNBNITUJIxjLC%2BzjjFxtGqNlvQOZSld9JgneFn%2B3v6RRPBlAF3YKDhv6eRiUWFu2UXFuq0S8gJ49nw2VW1CPJ8lYiRYMo6t6YldKfVwleqeG6Gax8L%2FknbTC%2BHlIh4f6hM2r8w%2FJH%2BojI%2BJtnVrflbpGaEvpyHOVDBUlKts2t%2Bkb7kq0p1aSWDKC7XVFVklF6cjDcmKbPBjqkAUjFi6wPUZBYw4Px4TWSWL%2BlGPRGjTBFvZiZc8SlYaOyPJFD9UxrxLE8uPfDiTsPOaRggTDnnmY5VCGXzDnMz2FxmnNfIyCVVYN13DSCtV58v1LQiRKYjn95kYM3CGkZFBs4AT6t%2BiSKS5dmUGxUawQiKEqWkbV0lYMjYHzUs9pUdz8grXkabDFAgnTH5gvWASwpE135B5nv1%2BH9LRJLp4TxXjWw&X-Amz-Signature=63cc68c9e4d8574a44cf86ec1a8543e63c20e3110fa066131bb23ea485f4ff34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S764CQMC%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4AygqKbyVA9krVulv0UZpgBH6ugSxn3lWmBMYdXjRvwIhAJZrPTVOXYANkXkH1VBQorGsnj%2F%2Bzxc0OJC9jarBhMG%2FKv8DCFwQABoMNjM3NDIzMTgzODA1Igw24QIWx3CywBhqIQQq3AODgpxWS0h8t0Ha9bE%2Fg9HhN2xN6f8BLoK28CrOX4V0eM7TU2imaPspU3UTEj0mEJHL2GVzcp%2B%2FSA6%2FWlnOsc9qhMcmop02Bj3RHwQJYYt8cFft%2BRs%2BRI9dw68YgXaJSgtR2jABlrvKbszcdtIiN%2Fq7XkrrcsudFYTvKdbHFd4yqmDK%2F1MOOZPRWAvWamO0wtg2L7rowh1uabPKFcwu8aHJ1J6md8qGQA2zGqAMXniKhGXER8Fgb3rFla9kjitaQPhrglBRYYOGbbWgk05%2BPNPWQaG1CwnJqZZXduUEa3nEDDoXCuirlamMa%2Fl%2B7G3lCQYrDx63mv7hT9SDyZlfoARyLwER%2FKAdod6OP9ho5z2%2Fqw3r827eHqnpbv7U31c4LCI77SMcjYfIcTjweBBgpMB5ODv9tk0KPhWFrlZgplxperTOYm3NpHNeHHSDNBNITUJIxjLC%2BzjjFxtGqNlvQOZSld9JgneFn%2B3v6RRPBlAF3YKDhv6eRiUWFu2UXFuq0S8gJ49nw2VW1CPJ8lYiRYMo6t6YldKfVwleqeG6Gax8L%2FknbTC%2BHlIh4f6hM2r8w%2FJH%2BojI%2BJtnVrflbpGaEvpyHOVDBUlKts2t%2Bkb7kq0p1aSWDKC7XVFVklF6cjDcmKbPBjqkAUjFi6wPUZBYw4Px4TWSWL%2BlGPRGjTBFvZiZc8SlYaOyPJFD9UxrxLE8uPfDiTsPOaRggTDnnmY5VCGXzDnMz2FxmnNfIyCVVYN13DSCtV58v1LQiRKYjn95kYM3CGkZFBs4AT6t%2BiSKS5dmUGxUawQiKEqWkbV0lYMjYHzUs9pUdz8grXkabDFAgnTH5gvWASwpE135B5nv1%2BH9LRJLp4TxXjWw&X-Amz-Signature=7ec4a3ef99cd0de12d66eb4000e47627aa4634fa4a12eefd83783e323743a513&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S764CQMC%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4AygqKbyVA9krVulv0UZpgBH6ugSxn3lWmBMYdXjRvwIhAJZrPTVOXYANkXkH1VBQorGsnj%2F%2Bzxc0OJC9jarBhMG%2FKv8DCFwQABoMNjM3NDIzMTgzODA1Igw24QIWx3CywBhqIQQq3AODgpxWS0h8t0Ha9bE%2Fg9HhN2xN6f8BLoK28CrOX4V0eM7TU2imaPspU3UTEj0mEJHL2GVzcp%2B%2FSA6%2FWlnOsc9qhMcmop02Bj3RHwQJYYt8cFft%2BRs%2BRI9dw68YgXaJSgtR2jABlrvKbszcdtIiN%2Fq7XkrrcsudFYTvKdbHFd4yqmDK%2F1MOOZPRWAvWamO0wtg2L7rowh1uabPKFcwu8aHJ1J6md8qGQA2zGqAMXniKhGXER8Fgb3rFla9kjitaQPhrglBRYYOGbbWgk05%2BPNPWQaG1CwnJqZZXduUEa3nEDDoXCuirlamMa%2Fl%2B7G3lCQYrDx63mv7hT9SDyZlfoARyLwER%2FKAdod6OP9ho5z2%2Fqw3r827eHqnpbv7U31c4LCI77SMcjYfIcTjweBBgpMB5ODv9tk0KPhWFrlZgplxperTOYm3NpHNeHHSDNBNITUJIxjLC%2BzjjFxtGqNlvQOZSld9JgneFn%2B3v6RRPBlAF3YKDhv6eRiUWFu2UXFuq0S8gJ49nw2VW1CPJ8lYiRYMo6t6YldKfVwleqeG6Gax8L%2FknbTC%2BHlIh4f6hM2r8w%2FJH%2BojI%2BJtnVrflbpGaEvpyHOVDBUlKts2t%2Bkb7kq0p1aSWDKC7XVFVklF6cjDcmKbPBjqkAUjFi6wPUZBYw4Px4TWSWL%2BlGPRGjTBFvZiZc8SlYaOyPJFD9UxrxLE8uPfDiTsPOaRggTDnnmY5VCGXzDnMz2FxmnNfIyCVVYN13DSCtV58v1LQiRKYjn95kYM3CGkZFBs4AT6t%2BiSKS5dmUGxUawQiKEqWkbV0lYMjYHzUs9pUdz8grXkabDFAgnTH5gvWASwpE135B5nv1%2BH9LRJLp4TxXjWw&X-Amz-Signature=5ff079e925350028fd2eb38817f674eb05df44ae5595bf843b7764596903882c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S764CQMC%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4AygqKbyVA9krVulv0UZpgBH6ugSxn3lWmBMYdXjRvwIhAJZrPTVOXYANkXkH1VBQorGsnj%2F%2Bzxc0OJC9jarBhMG%2FKv8DCFwQABoMNjM3NDIzMTgzODA1Igw24QIWx3CywBhqIQQq3AODgpxWS0h8t0Ha9bE%2Fg9HhN2xN6f8BLoK28CrOX4V0eM7TU2imaPspU3UTEj0mEJHL2GVzcp%2B%2FSA6%2FWlnOsc9qhMcmop02Bj3RHwQJYYt8cFft%2BRs%2BRI9dw68YgXaJSgtR2jABlrvKbszcdtIiN%2Fq7XkrrcsudFYTvKdbHFd4yqmDK%2F1MOOZPRWAvWamO0wtg2L7rowh1uabPKFcwu8aHJ1J6md8qGQA2zGqAMXniKhGXER8Fgb3rFla9kjitaQPhrglBRYYOGbbWgk05%2BPNPWQaG1CwnJqZZXduUEa3nEDDoXCuirlamMa%2Fl%2B7G3lCQYrDx63mv7hT9SDyZlfoARyLwER%2FKAdod6OP9ho5z2%2Fqw3r827eHqnpbv7U31c4LCI77SMcjYfIcTjweBBgpMB5ODv9tk0KPhWFrlZgplxperTOYm3NpHNeHHSDNBNITUJIxjLC%2BzjjFxtGqNlvQOZSld9JgneFn%2B3v6RRPBlAF3YKDhv6eRiUWFu2UXFuq0S8gJ49nw2VW1CPJ8lYiRYMo6t6YldKfVwleqeG6Gax8L%2FknbTC%2BHlIh4f6hM2r8w%2FJH%2BojI%2BJtnVrflbpGaEvpyHOVDBUlKts2t%2Bkb7kq0p1aSWDKC7XVFVklF6cjDcmKbPBjqkAUjFi6wPUZBYw4Px4TWSWL%2BlGPRGjTBFvZiZc8SlYaOyPJFD9UxrxLE8uPfDiTsPOaRggTDnnmY5VCGXzDnMz2FxmnNfIyCVVYN13DSCtV58v1LQiRKYjn95kYM3CGkZFBs4AT6t%2BiSKS5dmUGxUawQiKEqWkbV0lYMjYHzUs9pUdz8grXkabDFAgnTH5gvWASwpE135B5nv1%2BH9LRJLp4TxXjWw&X-Amz-Signature=b43a1e741047290e9f27ab7a10ac33d8f639b00d68c91bbada6d532ae49ef57e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S764CQMC%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4AygqKbyVA9krVulv0UZpgBH6ugSxn3lWmBMYdXjRvwIhAJZrPTVOXYANkXkH1VBQorGsnj%2F%2Bzxc0OJC9jarBhMG%2FKv8DCFwQABoMNjM3NDIzMTgzODA1Igw24QIWx3CywBhqIQQq3AODgpxWS0h8t0Ha9bE%2Fg9HhN2xN6f8BLoK28CrOX4V0eM7TU2imaPspU3UTEj0mEJHL2GVzcp%2B%2FSA6%2FWlnOsc9qhMcmop02Bj3RHwQJYYt8cFft%2BRs%2BRI9dw68YgXaJSgtR2jABlrvKbszcdtIiN%2Fq7XkrrcsudFYTvKdbHFd4yqmDK%2F1MOOZPRWAvWamO0wtg2L7rowh1uabPKFcwu8aHJ1J6md8qGQA2zGqAMXniKhGXER8Fgb3rFla9kjitaQPhrglBRYYOGbbWgk05%2BPNPWQaG1CwnJqZZXduUEa3nEDDoXCuirlamMa%2Fl%2B7G3lCQYrDx63mv7hT9SDyZlfoARyLwER%2FKAdod6OP9ho5z2%2Fqw3r827eHqnpbv7U31c4LCI77SMcjYfIcTjweBBgpMB5ODv9tk0KPhWFrlZgplxperTOYm3NpHNeHHSDNBNITUJIxjLC%2BzjjFxtGqNlvQOZSld9JgneFn%2B3v6RRPBlAF3YKDhv6eRiUWFu2UXFuq0S8gJ49nw2VW1CPJ8lYiRYMo6t6YldKfVwleqeG6Gax8L%2FknbTC%2BHlIh4f6hM2r8w%2FJH%2BojI%2BJtnVrflbpGaEvpyHOVDBUlKts2t%2Bkb7kq0p1aSWDKC7XVFVklF6cjDcmKbPBjqkAUjFi6wPUZBYw4Px4TWSWL%2BlGPRGjTBFvZiZc8SlYaOyPJFD9UxrxLE8uPfDiTsPOaRggTDnnmY5VCGXzDnMz2FxmnNfIyCVVYN13DSCtV58v1LQiRKYjn95kYM3CGkZFBs4AT6t%2BiSKS5dmUGxUawQiKEqWkbV0lYMjYHzUs9pUdz8grXkabDFAgnTH5gvWASwpE135B5nv1%2BH9LRJLp4TxXjWw&X-Amz-Signature=1fb05bc0dc7ee2dc7b04452b4b4f6588625a9dbe85281175d1b8677c0c07cecf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S764CQMC%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4AygqKbyVA9krVulv0UZpgBH6ugSxn3lWmBMYdXjRvwIhAJZrPTVOXYANkXkH1VBQorGsnj%2F%2Bzxc0OJC9jarBhMG%2FKv8DCFwQABoMNjM3NDIzMTgzODA1Igw24QIWx3CywBhqIQQq3AODgpxWS0h8t0Ha9bE%2Fg9HhN2xN6f8BLoK28CrOX4V0eM7TU2imaPspU3UTEj0mEJHL2GVzcp%2B%2FSA6%2FWlnOsc9qhMcmop02Bj3RHwQJYYt8cFft%2BRs%2BRI9dw68YgXaJSgtR2jABlrvKbszcdtIiN%2Fq7XkrrcsudFYTvKdbHFd4yqmDK%2F1MOOZPRWAvWamO0wtg2L7rowh1uabPKFcwu8aHJ1J6md8qGQA2zGqAMXniKhGXER8Fgb3rFla9kjitaQPhrglBRYYOGbbWgk05%2BPNPWQaG1CwnJqZZXduUEa3nEDDoXCuirlamMa%2Fl%2B7G3lCQYrDx63mv7hT9SDyZlfoARyLwER%2FKAdod6OP9ho5z2%2Fqw3r827eHqnpbv7U31c4LCI77SMcjYfIcTjweBBgpMB5ODv9tk0KPhWFrlZgplxperTOYm3NpHNeHHSDNBNITUJIxjLC%2BzjjFxtGqNlvQOZSld9JgneFn%2B3v6RRPBlAF3YKDhv6eRiUWFu2UXFuq0S8gJ49nw2VW1CPJ8lYiRYMo6t6YldKfVwleqeG6Gax8L%2FknbTC%2BHlIh4f6hM2r8w%2FJH%2BojI%2BJtnVrflbpGaEvpyHOVDBUlKts2t%2Bkb7kq0p1aSWDKC7XVFVklF6cjDcmKbPBjqkAUjFi6wPUZBYw4Px4TWSWL%2BlGPRGjTBFvZiZc8SlYaOyPJFD9UxrxLE8uPfDiTsPOaRggTDnnmY5VCGXzDnMz2FxmnNfIyCVVYN13DSCtV58v1LQiRKYjn95kYM3CGkZFBs4AT6t%2BiSKS5dmUGxUawQiKEqWkbV0lYMjYHzUs9pUdz8grXkabDFAgnTH5gvWASwpE135B5nv1%2BH9LRJLp4TxXjWw&X-Amz-Signature=2dd34d49421024b0844fa1b090de6c9ed10e642070a11c6807d029a01a4de4e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S764CQMC%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4AygqKbyVA9krVulv0UZpgBH6ugSxn3lWmBMYdXjRvwIhAJZrPTVOXYANkXkH1VBQorGsnj%2F%2Bzxc0OJC9jarBhMG%2FKv8DCFwQABoMNjM3NDIzMTgzODA1Igw24QIWx3CywBhqIQQq3AODgpxWS0h8t0Ha9bE%2Fg9HhN2xN6f8BLoK28CrOX4V0eM7TU2imaPspU3UTEj0mEJHL2GVzcp%2B%2FSA6%2FWlnOsc9qhMcmop02Bj3RHwQJYYt8cFft%2BRs%2BRI9dw68YgXaJSgtR2jABlrvKbszcdtIiN%2Fq7XkrrcsudFYTvKdbHFd4yqmDK%2F1MOOZPRWAvWamO0wtg2L7rowh1uabPKFcwu8aHJ1J6md8qGQA2zGqAMXniKhGXER8Fgb3rFla9kjitaQPhrglBRYYOGbbWgk05%2BPNPWQaG1CwnJqZZXduUEa3nEDDoXCuirlamMa%2Fl%2B7G3lCQYrDx63mv7hT9SDyZlfoARyLwER%2FKAdod6OP9ho5z2%2Fqw3r827eHqnpbv7U31c4LCI77SMcjYfIcTjweBBgpMB5ODv9tk0KPhWFrlZgplxperTOYm3NpHNeHHSDNBNITUJIxjLC%2BzjjFxtGqNlvQOZSld9JgneFn%2B3v6RRPBlAF3YKDhv6eRiUWFu2UXFuq0S8gJ49nw2VW1CPJ8lYiRYMo6t6YldKfVwleqeG6Gax8L%2FknbTC%2BHlIh4f6hM2r8w%2FJH%2BojI%2BJtnVrflbpGaEvpyHOVDBUlKts2t%2Bkb7kq0p1aSWDKC7XVFVklF6cjDcmKbPBjqkAUjFi6wPUZBYw4Px4TWSWL%2BlGPRGjTBFvZiZc8SlYaOyPJFD9UxrxLE8uPfDiTsPOaRggTDnnmY5VCGXzDnMz2FxmnNfIyCVVYN13DSCtV58v1LQiRKYjn95kYM3CGkZFBs4AT6t%2BiSKS5dmUGxUawQiKEqWkbV0lYMjYHzUs9pUdz8grXkabDFAgnTH5gvWASwpE135B5nv1%2BH9LRJLp4TxXjWw&X-Amz-Signature=3828d9b6d7d51fab8857ff89a298d3c4a13352f20b31651c06d2c8160374d4f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S764CQMC%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4AygqKbyVA9krVulv0UZpgBH6ugSxn3lWmBMYdXjRvwIhAJZrPTVOXYANkXkH1VBQorGsnj%2F%2Bzxc0OJC9jarBhMG%2FKv8DCFwQABoMNjM3NDIzMTgzODA1Igw24QIWx3CywBhqIQQq3AODgpxWS0h8t0Ha9bE%2Fg9HhN2xN6f8BLoK28CrOX4V0eM7TU2imaPspU3UTEj0mEJHL2GVzcp%2B%2FSA6%2FWlnOsc9qhMcmop02Bj3RHwQJYYt8cFft%2BRs%2BRI9dw68YgXaJSgtR2jABlrvKbszcdtIiN%2Fq7XkrrcsudFYTvKdbHFd4yqmDK%2F1MOOZPRWAvWamO0wtg2L7rowh1uabPKFcwu8aHJ1J6md8qGQA2zGqAMXniKhGXER8Fgb3rFla9kjitaQPhrglBRYYOGbbWgk05%2BPNPWQaG1CwnJqZZXduUEa3nEDDoXCuirlamMa%2Fl%2B7G3lCQYrDx63mv7hT9SDyZlfoARyLwER%2FKAdod6OP9ho5z2%2Fqw3r827eHqnpbv7U31c4LCI77SMcjYfIcTjweBBgpMB5ODv9tk0KPhWFrlZgplxperTOYm3NpHNeHHSDNBNITUJIxjLC%2BzjjFxtGqNlvQOZSld9JgneFn%2B3v6RRPBlAF3YKDhv6eRiUWFu2UXFuq0S8gJ49nw2VW1CPJ8lYiRYMo6t6YldKfVwleqeG6Gax8L%2FknbTC%2BHlIh4f6hM2r8w%2FJH%2BojI%2BJtnVrflbpGaEvpyHOVDBUlKts2t%2Bkb7kq0p1aSWDKC7XVFVklF6cjDcmKbPBjqkAUjFi6wPUZBYw4Px4TWSWL%2BlGPRGjTBFvZiZc8SlYaOyPJFD9UxrxLE8uPfDiTsPOaRggTDnnmY5VCGXzDnMz2FxmnNfIyCVVYN13DSCtV58v1LQiRKYjn95kYM3CGkZFBs4AT6t%2BiSKS5dmUGxUawQiKEqWkbV0lYMjYHzUs9pUdz8grXkabDFAgnTH5gvWASwpE135B5nv1%2BH9LRJLp4TxXjWw&X-Amz-Signature=ff68da686a9fd920c246b8d40fe384d0dc7dab0d9f3a72fce2035cee5e0de7e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

