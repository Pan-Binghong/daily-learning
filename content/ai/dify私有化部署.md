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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJZRMMC%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAKEQlsHQoE%2FxAPXOo9TZNaBhTlqyZVFMnPZ2qKBnglmAiEA8XTT2bc2N8wVscncIgJPFhh1U9YM8cYs0RVxjlV7I4oqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX84WtWvkUy0sgcqircA68RJpUUE09F9dIcQyqu42B8W87z8dRSs3cW6Zv1ZMKdCJ4PbltobghD4ZqXPIC2UVbCVONWnOueeDlpiCXgXeQMloCj0FxWc8urJpwfiWPYv0oZ7lzalK9t8OEr3fcwnkvz4K6ij4%2BLw3EGofUp3XSUhkrfksNc2qodgOUss7RCiSccJLJhHemAaMSsnhnNUg3tG4ISEaEE2FjZDVmMsCLhj84Sy52hJeF9xCmoyVqa6QbhdQFHV0rLLEBZ9GwX5X6rT0Q%2BOMp1cuWAs%2FB9WPPoZLcrM83pg6NfA3PQoaJ51MbKbhbGvD0hzRu37h60DNdT9Koa%2F1HGE2HSeHWDSNBBsep3DgQhdY7UL0FV3PgXqGa3BSS3yJGbJYw5QJMjJ0FsPnyvMsPHGY4dZ3ytmYr6go8rx%2BysNuXa4nzCjwQ%2FnztA2nZ2ggEIXgCfEjYUMeWW4YeGEfuk2yMqx0pSAXtEHKtTLzycxV9Bf%2Bxb7%2BswBYIV%2BCtmwiL%2FFztCAG5ffFIYrx3xvEdGHVoPH1rb3G%2FggtrpSVBQckrFq4CnFX1KKKtGGLKetBploasgKkXKoy42PYjlXttAIkTn9DiKvQfMQejNXMF5XJNQwLuaKDDP8gZgIoE3ew1N6eMIMIX5hssGOqUBrA9MRPb%2BPpp0h4VQyEAwGQeQBuVWCD5BD5raNC%2FJ7j2bfKLOTZ%2BjQUEHCYVDKDoyzS2%2Fwm6QSBDJBN9izFm6F2G2a6tzEmJ8zH8VgzQZ1DWOwp8AuoC99S1dtp1yFPoG%2FE9KDtTE3i66R01HXEXijmy%2FEcPw0llbXQdbS5s12iDqy83MVK3oYFH8tLy%2Bbe0DbpArl0kgupeOkfHrUZqI%2BC8DQM2e&X-Amz-Signature=3f9e09207a1cbd6500778c0a0164c49a89eb08c3b67f605c81ca7b68f4f0b829&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJZRMMC%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAKEQlsHQoE%2FxAPXOo9TZNaBhTlqyZVFMnPZ2qKBnglmAiEA8XTT2bc2N8wVscncIgJPFhh1U9YM8cYs0RVxjlV7I4oqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX84WtWvkUy0sgcqircA68RJpUUE09F9dIcQyqu42B8W87z8dRSs3cW6Zv1ZMKdCJ4PbltobghD4ZqXPIC2UVbCVONWnOueeDlpiCXgXeQMloCj0FxWc8urJpwfiWPYv0oZ7lzalK9t8OEr3fcwnkvz4K6ij4%2BLw3EGofUp3XSUhkrfksNc2qodgOUss7RCiSccJLJhHemAaMSsnhnNUg3tG4ISEaEE2FjZDVmMsCLhj84Sy52hJeF9xCmoyVqa6QbhdQFHV0rLLEBZ9GwX5X6rT0Q%2BOMp1cuWAs%2FB9WPPoZLcrM83pg6NfA3PQoaJ51MbKbhbGvD0hzRu37h60DNdT9Koa%2F1HGE2HSeHWDSNBBsep3DgQhdY7UL0FV3PgXqGa3BSS3yJGbJYw5QJMjJ0FsPnyvMsPHGY4dZ3ytmYr6go8rx%2BysNuXa4nzCjwQ%2FnztA2nZ2ggEIXgCfEjYUMeWW4YeGEfuk2yMqx0pSAXtEHKtTLzycxV9Bf%2Bxb7%2BswBYIV%2BCtmwiL%2FFztCAG5ffFIYrx3xvEdGHVoPH1rb3G%2FggtrpSVBQckrFq4CnFX1KKKtGGLKetBploasgKkXKoy42PYjlXttAIkTn9DiKvQfMQejNXMF5XJNQwLuaKDDP8gZgIoE3ew1N6eMIMIX5hssGOqUBrA9MRPb%2BPpp0h4VQyEAwGQeQBuVWCD5BD5raNC%2FJ7j2bfKLOTZ%2BjQUEHCYVDKDoyzS2%2Fwm6QSBDJBN9izFm6F2G2a6tzEmJ8zH8VgzQZ1DWOwp8AuoC99S1dtp1yFPoG%2FE9KDtTE3i66R01HXEXijmy%2FEcPw0llbXQdbS5s12iDqy83MVK3oYFH8tLy%2Bbe0DbpArl0kgupeOkfHrUZqI%2BC8DQM2e&X-Amz-Signature=112b2d13fb11ed7393b6c40771a622ec92f606094a85fdbf49a02377750bde07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJZRMMC%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAKEQlsHQoE%2FxAPXOo9TZNaBhTlqyZVFMnPZ2qKBnglmAiEA8XTT2bc2N8wVscncIgJPFhh1U9YM8cYs0RVxjlV7I4oqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX84WtWvkUy0sgcqircA68RJpUUE09F9dIcQyqu42B8W87z8dRSs3cW6Zv1ZMKdCJ4PbltobghD4ZqXPIC2UVbCVONWnOueeDlpiCXgXeQMloCj0FxWc8urJpwfiWPYv0oZ7lzalK9t8OEr3fcwnkvz4K6ij4%2BLw3EGofUp3XSUhkrfksNc2qodgOUss7RCiSccJLJhHemAaMSsnhnNUg3tG4ISEaEE2FjZDVmMsCLhj84Sy52hJeF9xCmoyVqa6QbhdQFHV0rLLEBZ9GwX5X6rT0Q%2BOMp1cuWAs%2FB9WPPoZLcrM83pg6NfA3PQoaJ51MbKbhbGvD0hzRu37h60DNdT9Koa%2F1HGE2HSeHWDSNBBsep3DgQhdY7UL0FV3PgXqGa3BSS3yJGbJYw5QJMjJ0FsPnyvMsPHGY4dZ3ytmYr6go8rx%2BysNuXa4nzCjwQ%2FnztA2nZ2ggEIXgCfEjYUMeWW4YeGEfuk2yMqx0pSAXtEHKtTLzycxV9Bf%2Bxb7%2BswBYIV%2BCtmwiL%2FFztCAG5ffFIYrx3xvEdGHVoPH1rb3G%2FggtrpSVBQckrFq4CnFX1KKKtGGLKetBploasgKkXKoy42PYjlXttAIkTn9DiKvQfMQejNXMF5XJNQwLuaKDDP8gZgIoE3ew1N6eMIMIX5hssGOqUBrA9MRPb%2BPpp0h4VQyEAwGQeQBuVWCD5BD5raNC%2FJ7j2bfKLOTZ%2BjQUEHCYVDKDoyzS2%2Fwm6QSBDJBN9izFm6F2G2a6tzEmJ8zH8VgzQZ1DWOwp8AuoC99S1dtp1yFPoG%2FE9KDtTE3i66R01HXEXijmy%2FEcPw0llbXQdbS5s12iDqy83MVK3oYFH8tLy%2Bbe0DbpArl0kgupeOkfHrUZqI%2BC8DQM2e&X-Amz-Signature=78e295c36af813c350ace28764a38302f4caf67f64d15d71e9359f902f1901de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJZRMMC%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAKEQlsHQoE%2FxAPXOo9TZNaBhTlqyZVFMnPZ2qKBnglmAiEA8XTT2bc2N8wVscncIgJPFhh1U9YM8cYs0RVxjlV7I4oqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX84WtWvkUy0sgcqircA68RJpUUE09F9dIcQyqu42B8W87z8dRSs3cW6Zv1ZMKdCJ4PbltobghD4ZqXPIC2UVbCVONWnOueeDlpiCXgXeQMloCj0FxWc8urJpwfiWPYv0oZ7lzalK9t8OEr3fcwnkvz4K6ij4%2BLw3EGofUp3XSUhkrfksNc2qodgOUss7RCiSccJLJhHemAaMSsnhnNUg3tG4ISEaEE2FjZDVmMsCLhj84Sy52hJeF9xCmoyVqa6QbhdQFHV0rLLEBZ9GwX5X6rT0Q%2BOMp1cuWAs%2FB9WPPoZLcrM83pg6NfA3PQoaJ51MbKbhbGvD0hzRu37h60DNdT9Koa%2F1HGE2HSeHWDSNBBsep3DgQhdY7UL0FV3PgXqGa3BSS3yJGbJYw5QJMjJ0FsPnyvMsPHGY4dZ3ytmYr6go8rx%2BysNuXa4nzCjwQ%2FnztA2nZ2ggEIXgCfEjYUMeWW4YeGEfuk2yMqx0pSAXtEHKtTLzycxV9Bf%2Bxb7%2BswBYIV%2BCtmwiL%2FFztCAG5ffFIYrx3xvEdGHVoPH1rb3G%2FggtrpSVBQckrFq4CnFX1KKKtGGLKetBploasgKkXKoy42PYjlXttAIkTn9DiKvQfMQejNXMF5XJNQwLuaKDDP8gZgIoE3ew1N6eMIMIX5hssGOqUBrA9MRPb%2BPpp0h4VQyEAwGQeQBuVWCD5BD5raNC%2FJ7j2bfKLOTZ%2BjQUEHCYVDKDoyzS2%2Fwm6QSBDJBN9izFm6F2G2a6tzEmJ8zH8VgzQZ1DWOwp8AuoC99S1dtp1yFPoG%2FE9KDtTE3i66R01HXEXijmy%2FEcPw0llbXQdbS5s12iDqy83MVK3oYFH8tLy%2Bbe0DbpArl0kgupeOkfHrUZqI%2BC8DQM2e&X-Amz-Signature=e7f8a073ade02c50d6c6a38abbb45cf924b7afebee31137011d3152a05a864e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJZRMMC%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAKEQlsHQoE%2FxAPXOo9TZNaBhTlqyZVFMnPZ2qKBnglmAiEA8XTT2bc2N8wVscncIgJPFhh1U9YM8cYs0RVxjlV7I4oqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX84WtWvkUy0sgcqircA68RJpUUE09F9dIcQyqu42B8W87z8dRSs3cW6Zv1ZMKdCJ4PbltobghD4ZqXPIC2UVbCVONWnOueeDlpiCXgXeQMloCj0FxWc8urJpwfiWPYv0oZ7lzalK9t8OEr3fcwnkvz4K6ij4%2BLw3EGofUp3XSUhkrfksNc2qodgOUss7RCiSccJLJhHemAaMSsnhnNUg3tG4ISEaEE2FjZDVmMsCLhj84Sy52hJeF9xCmoyVqa6QbhdQFHV0rLLEBZ9GwX5X6rT0Q%2BOMp1cuWAs%2FB9WPPoZLcrM83pg6NfA3PQoaJ51MbKbhbGvD0hzRu37h60DNdT9Koa%2F1HGE2HSeHWDSNBBsep3DgQhdY7UL0FV3PgXqGa3BSS3yJGbJYw5QJMjJ0FsPnyvMsPHGY4dZ3ytmYr6go8rx%2BysNuXa4nzCjwQ%2FnztA2nZ2ggEIXgCfEjYUMeWW4YeGEfuk2yMqx0pSAXtEHKtTLzycxV9Bf%2Bxb7%2BswBYIV%2BCtmwiL%2FFztCAG5ffFIYrx3xvEdGHVoPH1rb3G%2FggtrpSVBQckrFq4CnFX1KKKtGGLKetBploasgKkXKoy42PYjlXttAIkTn9DiKvQfMQejNXMF5XJNQwLuaKDDP8gZgIoE3ew1N6eMIMIX5hssGOqUBrA9MRPb%2BPpp0h4VQyEAwGQeQBuVWCD5BD5raNC%2FJ7j2bfKLOTZ%2BjQUEHCYVDKDoyzS2%2Fwm6QSBDJBN9izFm6F2G2a6tzEmJ8zH8VgzQZ1DWOwp8AuoC99S1dtp1yFPoG%2FE9KDtTE3i66R01HXEXijmy%2FEcPw0llbXQdbS5s12iDqy83MVK3oYFH8tLy%2Bbe0DbpArl0kgupeOkfHrUZqI%2BC8DQM2e&X-Amz-Signature=c844f5ce6948e575acffcb4a57cad783b441188f65273043d170c18a123ac444&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJZRMMC%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAKEQlsHQoE%2FxAPXOo9TZNaBhTlqyZVFMnPZ2qKBnglmAiEA8XTT2bc2N8wVscncIgJPFhh1U9YM8cYs0RVxjlV7I4oqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX84WtWvkUy0sgcqircA68RJpUUE09F9dIcQyqu42B8W87z8dRSs3cW6Zv1ZMKdCJ4PbltobghD4ZqXPIC2UVbCVONWnOueeDlpiCXgXeQMloCj0FxWc8urJpwfiWPYv0oZ7lzalK9t8OEr3fcwnkvz4K6ij4%2BLw3EGofUp3XSUhkrfksNc2qodgOUss7RCiSccJLJhHemAaMSsnhnNUg3tG4ISEaEE2FjZDVmMsCLhj84Sy52hJeF9xCmoyVqa6QbhdQFHV0rLLEBZ9GwX5X6rT0Q%2BOMp1cuWAs%2FB9WPPoZLcrM83pg6NfA3PQoaJ51MbKbhbGvD0hzRu37h60DNdT9Koa%2F1HGE2HSeHWDSNBBsep3DgQhdY7UL0FV3PgXqGa3BSS3yJGbJYw5QJMjJ0FsPnyvMsPHGY4dZ3ytmYr6go8rx%2BysNuXa4nzCjwQ%2FnztA2nZ2ggEIXgCfEjYUMeWW4YeGEfuk2yMqx0pSAXtEHKtTLzycxV9Bf%2Bxb7%2BswBYIV%2BCtmwiL%2FFztCAG5ffFIYrx3xvEdGHVoPH1rb3G%2FggtrpSVBQckrFq4CnFX1KKKtGGLKetBploasgKkXKoy42PYjlXttAIkTn9DiKvQfMQejNXMF5XJNQwLuaKDDP8gZgIoE3ew1N6eMIMIX5hssGOqUBrA9MRPb%2BPpp0h4VQyEAwGQeQBuVWCD5BD5raNC%2FJ7j2bfKLOTZ%2BjQUEHCYVDKDoyzS2%2Fwm6QSBDJBN9izFm6F2G2a6tzEmJ8zH8VgzQZ1DWOwp8AuoC99S1dtp1yFPoG%2FE9KDtTE3i66R01HXEXijmy%2FEcPw0llbXQdbS5s12iDqy83MVK3oYFH8tLy%2Bbe0DbpArl0kgupeOkfHrUZqI%2BC8DQM2e&X-Amz-Signature=f4dcece791d721645836bca0f447994bfe470f887d7ff4278a4c91ea5224c530&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJZRMMC%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAKEQlsHQoE%2FxAPXOo9TZNaBhTlqyZVFMnPZ2qKBnglmAiEA8XTT2bc2N8wVscncIgJPFhh1U9YM8cYs0RVxjlV7I4oqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX84WtWvkUy0sgcqircA68RJpUUE09F9dIcQyqu42B8W87z8dRSs3cW6Zv1ZMKdCJ4PbltobghD4ZqXPIC2UVbCVONWnOueeDlpiCXgXeQMloCj0FxWc8urJpwfiWPYv0oZ7lzalK9t8OEr3fcwnkvz4K6ij4%2BLw3EGofUp3XSUhkrfksNc2qodgOUss7RCiSccJLJhHemAaMSsnhnNUg3tG4ISEaEE2FjZDVmMsCLhj84Sy52hJeF9xCmoyVqa6QbhdQFHV0rLLEBZ9GwX5X6rT0Q%2BOMp1cuWAs%2FB9WPPoZLcrM83pg6NfA3PQoaJ51MbKbhbGvD0hzRu37h60DNdT9Koa%2F1HGE2HSeHWDSNBBsep3DgQhdY7UL0FV3PgXqGa3BSS3yJGbJYw5QJMjJ0FsPnyvMsPHGY4dZ3ytmYr6go8rx%2BysNuXa4nzCjwQ%2FnztA2nZ2ggEIXgCfEjYUMeWW4YeGEfuk2yMqx0pSAXtEHKtTLzycxV9Bf%2Bxb7%2BswBYIV%2BCtmwiL%2FFztCAG5ffFIYrx3xvEdGHVoPH1rb3G%2FggtrpSVBQckrFq4CnFX1KKKtGGLKetBploasgKkXKoy42PYjlXttAIkTn9DiKvQfMQejNXMF5XJNQwLuaKDDP8gZgIoE3ew1N6eMIMIX5hssGOqUBrA9MRPb%2BPpp0h4VQyEAwGQeQBuVWCD5BD5raNC%2FJ7j2bfKLOTZ%2BjQUEHCYVDKDoyzS2%2Fwm6QSBDJBN9izFm6F2G2a6tzEmJ8zH8VgzQZ1DWOwp8AuoC99S1dtp1yFPoG%2FE9KDtTE3i66R01HXEXijmy%2FEcPw0llbXQdbS5s12iDqy83MVK3oYFH8tLy%2Bbe0DbpArl0kgupeOkfHrUZqI%2BC8DQM2e&X-Amz-Signature=bba2de004e5132e0e29af3e5f5cf94ff74fb4f2aa308d05157373b00c7f5bcc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJZRMMC%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAKEQlsHQoE%2FxAPXOo9TZNaBhTlqyZVFMnPZ2qKBnglmAiEA8XTT2bc2N8wVscncIgJPFhh1U9YM8cYs0RVxjlV7I4oqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX84WtWvkUy0sgcqircA68RJpUUE09F9dIcQyqu42B8W87z8dRSs3cW6Zv1ZMKdCJ4PbltobghD4ZqXPIC2UVbCVONWnOueeDlpiCXgXeQMloCj0FxWc8urJpwfiWPYv0oZ7lzalK9t8OEr3fcwnkvz4K6ij4%2BLw3EGofUp3XSUhkrfksNc2qodgOUss7RCiSccJLJhHemAaMSsnhnNUg3tG4ISEaEE2FjZDVmMsCLhj84Sy52hJeF9xCmoyVqa6QbhdQFHV0rLLEBZ9GwX5X6rT0Q%2BOMp1cuWAs%2FB9WPPoZLcrM83pg6NfA3PQoaJ51MbKbhbGvD0hzRu37h60DNdT9Koa%2F1HGE2HSeHWDSNBBsep3DgQhdY7UL0FV3PgXqGa3BSS3yJGbJYw5QJMjJ0FsPnyvMsPHGY4dZ3ytmYr6go8rx%2BysNuXa4nzCjwQ%2FnztA2nZ2ggEIXgCfEjYUMeWW4YeGEfuk2yMqx0pSAXtEHKtTLzycxV9Bf%2Bxb7%2BswBYIV%2BCtmwiL%2FFztCAG5ffFIYrx3xvEdGHVoPH1rb3G%2FggtrpSVBQckrFq4CnFX1KKKtGGLKetBploasgKkXKoy42PYjlXttAIkTn9DiKvQfMQejNXMF5XJNQwLuaKDDP8gZgIoE3ew1N6eMIMIX5hssGOqUBrA9MRPb%2BPpp0h4VQyEAwGQeQBuVWCD5BD5raNC%2FJ7j2bfKLOTZ%2BjQUEHCYVDKDoyzS2%2Fwm6QSBDJBN9izFm6F2G2a6tzEmJ8zH8VgzQZ1DWOwp8AuoC99S1dtp1yFPoG%2FE9KDtTE3i66R01HXEXijmy%2FEcPw0llbXQdbS5s12iDqy83MVK3oYFH8tLy%2Bbe0DbpArl0kgupeOkfHrUZqI%2BC8DQM2e&X-Amz-Signature=d4e9172ad858f7de6a79a3261373da5a1ba90193ea5e8de3d346ef3f8e440058&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJZRMMC%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAKEQlsHQoE%2FxAPXOo9TZNaBhTlqyZVFMnPZ2qKBnglmAiEA8XTT2bc2N8wVscncIgJPFhh1U9YM8cYs0RVxjlV7I4oqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX84WtWvkUy0sgcqircA68RJpUUE09F9dIcQyqu42B8W87z8dRSs3cW6Zv1ZMKdCJ4PbltobghD4ZqXPIC2UVbCVONWnOueeDlpiCXgXeQMloCj0FxWc8urJpwfiWPYv0oZ7lzalK9t8OEr3fcwnkvz4K6ij4%2BLw3EGofUp3XSUhkrfksNc2qodgOUss7RCiSccJLJhHemAaMSsnhnNUg3tG4ISEaEE2FjZDVmMsCLhj84Sy52hJeF9xCmoyVqa6QbhdQFHV0rLLEBZ9GwX5X6rT0Q%2BOMp1cuWAs%2FB9WPPoZLcrM83pg6NfA3PQoaJ51MbKbhbGvD0hzRu37h60DNdT9Koa%2F1HGE2HSeHWDSNBBsep3DgQhdY7UL0FV3PgXqGa3BSS3yJGbJYw5QJMjJ0FsPnyvMsPHGY4dZ3ytmYr6go8rx%2BysNuXa4nzCjwQ%2FnztA2nZ2ggEIXgCfEjYUMeWW4YeGEfuk2yMqx0pSAXtEHKtTLzycxV9Bf%2Bxb7%2BswBYIV%2BCtmwiL%2FFztCAG5ffFIYrx3xvEdGHVoPH1rb3G%2FggtrpSVBQckrFq4CnFX1KKKtGGLKetBploasgKkXKoy42PYjlXttAIkTn9DiKvQfMQejNXMF5XJNQwLuaKDDP8gZgIoE3ew1N6eMIMIX5hssGOqUBrA9MRPb%2BPpp0h4VQyEAwGQeQBuVWCD5BD5raNC%2FJ7j2bfKLOTZ%2BjQUEHCYVDKDoyzS2%2Fwm6QSBDJBN9izFm6F2G2a6tzEmJ8zH8VgzQZ1DWOwp8AuoC99S1dtp1yFPoG%2FE9KDtTE3i66R01HXEXijmy%2FEcPw0llbXQdbS5s12iDqy83MVK3oYFH8tLy%2Bbe0DbpArl0kgupeOkfHrUZqI%2BC8DQM2e&X-Amz-Signature=550bb102b364b8df7a202545ccf3d9cc5ce159a7db3cc9c6a771a990891ac33e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YJZRMMC%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAKEQlsHQoE%2FxAPXOo9TZNaBhTlqyZVFMnPZ2qKBnglmAiEA8XTT2bc2N8wVscncIgJPFhh1U9YM8cYs0RVxjlV7I4oqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBX84WtWvkUy0sgcqircA68RJpUUE09F9dIcQyqu42B8W87z8dRSs3cW6Zv1ZMKdCJ4PbltobghD4ZqXPIC2UVbCVONWnOueeDlpiCXgXeQMloCj0FxWc8urJpwfiWPYv0oZ7lzalK9t8OEr3fcwnkvz4K6ij4%2BLw3EGofUp3XSUhkrfksNc2qodgOUss7RCiSccJLJhHemAaMSsnhnNUg3tG4ISEaEE2FjZDVmMsCLhj84Sy52hJeF9xCmoyVqa6QbhdQFHV0rLLEBZ9GwX5X6rT0Q%2BOMp1cuWAs%2FB9WPPoZLcrM83pg6NfA3PQoaJ51MbKbhbGvD0hzRu37h60DNdT9Koa%2F1HGE2HSeHWDSNBBsep3DgQhdY7UL0FV3PgXqGa3BSS3yJGbJYw5QJMjJ0FsPnyvMsPHGY4dZ3ytmYr6go8rx%2BysNuXa4nzCjwQ%2FnztA2nZ2ggEIXgCfEjYUMeWW4YeGEfuk2yMqx0pSAXtEHKtTLzycxV9Bf%2Bxb7%2BswBYIV%2BCtmwiL%2FFztCAG5ffFIYrx3xvEdGHVoPH1rb3G%2FggtrpSVBQckrFq4CnFX1KKKtGGLKetBploasgKkXKoy42PYjlXttAIkTn9DiKvQfMQejNXMF5XJNQwLuaKDDP8gZgIoE3ew1N6eMIMIX5hssGOqUBrA9MRPb%2BPpp0h4VQyEAwGQeQBuVWCD5BD5raNC%2FJ7j2bfKLOTZ%2BjQUEHCYVDKDoyzS2%2Fwm6QSBDJBN9izFm6F2G2a6tzEmJ8zH8VgzQZ1DWOwp8AuoC99S1dtp1yFPoG%2FE9KDtTE3i66R01HXEXijmy%2FEcPw0llbXQdbS5s12iDqy83MVK3oYFH8tLy%2Bbe0DbpArl0kgupeOkfHrUZqI%2BC8DQM2e&X-Amz-Signature=a0e463c6f2e39c4434e656b08d9c5f67a30933f9aba1086f6cb599e3cb6cb931&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

