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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WSGCCD%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQC7Z1ISEs75dQxy%2FWQ2o4wh%2FQwo2Nnhbu0j1K1ZYj078QIhAJw40z95e9FDsz3Ycs%2FHezjbHtNCQ%2BN0FEpjtg3wsbTWKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4iVLxnWNWqm8b2IMq3APiie0sQ9Lls3Rsv4iA%2FpUxpJOF0tRsiziqZGqBygFSoZyLamt3Pv1lWERwjg0l5RN5DTcwGwVbWJC%2BA6fAjTRK%2By8AqUEqlt8XZFBGHCMulOWJVQZDD01YdhfHUbzWS3deV6SAwJ4soUZSioEzpDHS6LgiNPQD8aE7lzf%2FE3xfEaH6l5vSWsJgOIs%2BDC9VrgRkuKrOcsES%2BwmJeQ0SdOL0PjKUB3nm60VOikblKxKEYdDIdWG9%2BzKiTHgzaOVivwXysQOUFtFYNtViB0%2BWuCEoJ7hJyDyy4MaIHEjz7NyFtpE%2Be6oS92uSR%2B9BWoYKC5N1bJpsW7ujcd7t%2FSQXGd%2B1gWqKZRs4zPLizzfpb4gylB5rSSHmQYSzupQ2w0ehxEYBwaXjY7I%2FdmX1lOQMrcc5uWF5UFU8hQiXlo7PLu5PZlSsrugWlaUjyrVUxs21sL40nI74fsMfzZqiZm%2FOBVnGwUKimnbBtTkCttLlLLcUnmpD5P8CfyEQrnWA%2Bg8IOa%2B8YeUvUGxG8t7xXvO%2Bhf8sgjj4vG%2BwdMynZjUHd7LZawG8rgaUFrWjSPgBNvS4ktD6a01WfZOI62wzZrWjC4U04ZX5%2BSaGLyZ1ZTYY1FWKE4q%2FPwzS0D32hs7WHDDr7MXPBjqkAfiBVA%2B3RTm2mNtCGkSmzbFPSNHqN5PQaYV2oY6p%2FBW%2B5owUSKUtL6r%2BIq8bFl0r%2FZUEYI4HMSnmu8a0pWpZ9b4e7TXfaGtPLJnGNjyLS4T70O8rCNwfjzzkWX%2FFFxBUVB4USntTZc94jq8%2FECHtghX3vnNGxpuz6Le9FlehfrFk6e8sGRbNcvJzLBqjx4RyPixcfTj1vK7RxJX%2FK7tZbM1lECZZ&X-Amz-Signature=8a255607ed6de19ba0fa751ef71609ba2846596a9eb8589ac3b8c3df0ac37009&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WSGCCD%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQC7Z1ISEs75dQxy%2FWQ2o4wh%2FQwo2Nnhbu0j1K1ZYj078QIhAJw40z95e9FDsz3Ycs%2FHezjbHtNCQ%2BN0FEpjtg3wsbTWKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4iVLxnWNWqm8b2IMq3APiie0sQ9Lls3Rsv4iA%2FpUxpJOF0tRsiziqZGqBygFSoZyLamt3Pv1lWERwjg0l5RN5DTcwGwVbWJC%2BA6fAjTRK%2By8AqUEqlt8XZFBGHCMulOWJVQZDD01YdhfHUbzWS3deV6SAwJ4soUZSioEzpDHS6LgiNPQD8aE7lzf%2FE3xfEaH6l5vSWsJgOIs%2BDC9VrgRkuKrOcsES%2BwmJeQ0SdOL0PjKUB3nm60VOikblKxKEYdDIdWG9%2BzKiTHgzaOVivwXysQOUFtFYNtViB0%2BWuCEoJ7hJyDyy4MaIHEjz7NyFtpE%2Be6oS92uSR%2B9BWoYKC5N1bJpsW7ujcd7t%2FSQXGd%2B1gWqKZRs4zPLizzfpb4gylB5rSSHmQYSzupQ2w0ehxEYBwaXjY7I%2FdmX1lOQMrcc5uWF5UFU8hQiXlo7PLu5PZlSsrugWlaUjyrVUxs21sL40nI74fsMfzZqiZm%2FOBVnGwUKimnbBtTkCttLlLLcUnmpD5P8CfyEQrnWA%2Bg8IOa%2B8YeUvUGxG8t7xXvO%2Bhf8sgjj4vG%2BwdMynZjUHd7LZawG8rgaUFrWjSPgBNvS4ktD6a01WfZOI62wzZrWjC4U04ZX5%2BSaGLyZ1ZTYY1FWKE4q%2FPwzS0D32hs7WHDDr7MXPBjqkAfiBVA%2B3RTm2mNtCGkSmzbFPSNHqN5PQaYV2oY6p%2FBW%2B5owUSKUtL6r%2BIq8bFl0r%2FZUEYI4HMSnmu8a0pWpZ9b4e7TXfaGtPLJnGNjyLS4T70O8rCNwfjzzkWX%2FFFxBUVB4USntTZc94jq8%2FECHtghX3vnNGxpuz6Le9FlehfrFk6e8sGRbNcvJzLBqjx4RyPixcfTj1vK7RxJX%2FK7tZbM1lECZZ&X-Amz-Signature=efdcaad8c49bbc4b8c86eb32a84af07c154b54c4a386a7232721cdc5d31a2887&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WSGCCD%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQC7Z1ISEs75dQxy%2FWQ2o4wh%2FQwo2Nnhbu0j1K1ZYj078QIhAJw40z95e9FDsz3Ycs%2FHezjbHtNCQ%2BN0FEpjtg3wsbTWKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4iVLxnWNWqm8b2IMq3APiie0sQ9Lls3Rsv4iA%2FpUxpJOF0tRsiziqZGqBygFSoZyLamt3Pv1lWERwjg0l5RN5DTcwGwVbWJC%2BA6fAjTRK%2By8AqUEqlt8XZFBGHCMulOWJVQZDD01YdhfHUbzWS3deV6SAwJ4soUZSioEzpDHS6LgiNPQD8aE7lzf%2FE3xfEaH6l5vSWsJgOIs%2BDC9VrgRkuKrOcsES%2BwmJeQ0SdOL0PjKUB3nm60VOikblKxKEYdDIdWG9%2BzKiTHgzaOVivwXysQOUFtFYNtViB0%2BWuCEoJ7hJyDyy4MaIHEjz7NyFtpE%2Be6oS92uSR%2B9BWoYKC5N1bJpsW7ujcd7t%2FSQXGd%2B1gWqKZRs4zPLizzfpb4gylB5rSSHmQYSzupQ2w0ehxEYBwaXjY7I%2FdmX1lOQMrcc5uWF5UFU8hQiXlo7PLu5PZlSsrugWlaUjyrVUxs21sL40nI74fsMfzZqiZm%2FOBVnGwUKimnbBtTkCttLlLLcUnmpD5P8CfyEQrnWA%2Bg8IOa%2B8YeUvUGxG8t7xXvO%2Bhf8sgjj4vG%2BwdMynZjUHd7LZawG8rgaUFrWjSPgBNvS4ktD6a01WfZOI62wzZrWjC4U04ZX5%2BSaGLyZ1ZTYY1FWKE4q%2FPwzS0D32hs7WHDDr7MXPBjqkAfiBVA%2B3RTm2mNtCGkSmzbFPSNHqN5PQaYV2oY6p%2FBW%2B5owUSKUtL6r%2BIq8bFl0r%2FZUEYI4HMSnmu8a0pWpZ9b4e7TXfaGtPLJnGNjyLS4T70O8rCNwfjzzkWX%2FFFxBUVB4USntTZc94jq8%2FECHtghX3vnNGxpuz6Le9FlehfrFk6e8sGRbNcvJzLBqjx4RyPixcfTj1vK7RxJX%2FK7tZbM1lECZZ&X-Amz-Signature=90b6097ebc62188a597b73920d4d885c1c1dd685462b2a0dde6cde9186293c2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WSGCCD%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQC7Z1ISEs75dQxy%2FWQ2o4wh%2FQwo2Nnhbu0j1K1ZYj078QIhAJw40z95e9FDsz3Ycs%2FHezjbHtNCQ%2BN0FEpjtg3wsbTWKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4iVLxnWNWqm8b2IMq3APiie0sQ9Lls3Rsv4iA%2FpUxpJOF0tRsiziqZGqBygFSoZyLamt3Pv1lWERwjg0l5RN5DTcwGwVbWJC%2BA6fAjTRK%2By8AqUEqlt8XZFBGHCMulOWJVQZDD01YdhfHUbzWS3deV6SAwJ4soUZSioEzpDHS6LgiNPQD8aE7lzf%2FE3xfEaH6l5vSWsJgOIs%2BDC9VrgRkuKrOcsES%2BwmJeQ0SdOL0PjKUB3nm60VOikblKxKEYdDIdWG9%2BzKiTHgzaOVivwXysQOUFtFYNtViB0%2BWuCEoJ7hJyDyy4MaIHEjz7NyFtpE%2Be6oS92uSR%2B9BWoYKC5N1bJpsW7ujcd7t%2FSQXGd%2B1gWqKZRs4zPLizzfpb4gylB5rSSHmQYSzupQ2w0ehxEYBwaXjY7I%2FdmX1lOQMrcc5uWF5UFU8hQiXlo7PLu5PZlSsrugWlaUjyrVUxs21sL40nI74fsMfzZqiZm%2FOBVnGwUKimnbBtTkCttLlLLcUnmpD5P8CfyEQrnWA%2Bg8IOa%2B8YeUvUGxG8t7xXvO%2Bhf8sgjj4vG%2BwdMynZjUHd7LZawG8rgaUFrWjSPgBNvS4ktD6a01WfZOI62wzZrWjC4U04ZX5%2BSaGLyZ1ZTYY1FWKE4q%2FPwzS0D32hs7WHDDr7MXPBjqkAfiBVA%2B3RTm2mNtCGkSmzbFPSNHqN5PQaYV2oY6p%2FBW%2B5owUSKUtL6r%2BIq8bFl0r%2FZUEYI4HMSnmu8a0pWpZ9b4e7TXfaGtPLJnGNjyLS4T70O8rCNwfjzzkWX%2FFFxBUVB4USntTZc94jq8%2FECHtghX3vnNGxpuz6Le9FlehfrFk6e8sGRbNcvJzLBqjx4RyPixcfTj1vK7RxJX%2FK7tZbM1lECZZ&X-Amz-Signature=079f062314561224bf475eaa53881d26a83d4c6d1db94c42a2ea7d8925fa68b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WSGCCD%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQC7Z1ISEs75dQxy%2FWQ2o4wh%2FQwo2Nnhbu0j1K1ZYj078QIhAJw40z95e9FDsz3Ycs%2FHezjbHtNCQ%2BN0FEpjtg3wsbTWKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4iVLxnWNWqm8b2IMq3APiie0sQ9Lls3Rsv4iA%2FpUxpJOF0tRsiziqZGqBygFSoZyLamt3Pv1lWERwjg0l5RN5DTcwGwVbWJC%2BA6fAjTRK%2By8AqUEqlt8XZFBGHCMulOWJVQZDD01YdhfHUbzWS3deV6SAwJ4soUZSioEzpDHS6LgiNPQD8aE7lzf%2FE3xfEaH6l5vSWsJgOIs%2BDC9VrgRkuKrOcsES%2BwmJeQ0SdOL0PjKUB3nm60VOikblKxKEYdDIdWG9%2BzKiTHgzaOVivwXysQOUFtFYNtViB0%2BWuCEoJ7hJyDyy4MaIHEjz7NyFtpE%2Be6oS92uSR%2B9BWoYKC5N1bJpsW7ujcd7t%2FSQXGd%2B1gWqKZRs4zPLizzfpb4gylB5rSSHmQYSzupQ2w0ehxEYBwaXjY7I%2FdmX1lOQMrcc5uWF5UFU8hQiXlo7PLu5PZlSsrugWlaUjyrVUxs21sL40nI74fsMfzZqiZm%2FOBVnGwUKimnbBtTkCttLlLLcUnmpD5P8CfyEQrnWA%2Bg8IOa%2B8YeUvUGxG8t7xXvO%2Bhf8sgjj4vG%2BwdMynZjUHd7LZawG8rgaUFrWjSPgBNvS4ktD6a01WfZOI62wzZrWjC4U04ZX5%2BSaGLyZ1ZTYY1FWKE4q%2FPwzS0D32hs7WHDDr7MXPBjqkAfiBVA%2B3RTm2mNtCGkSmzbFPSNHqN5PQaYV2oY6p%2FBW%2B5owUSKUtL6r%2BIq8bFl0r%2FZUEYI4HMSnmu8a0pWpZ9b4e7TXfaGtPLJnGNjyLS4T70O8rCNwfjzzkWX%2FFFxBUVB4USntTZc94jq8%2FECHtghX3vnNGxpuz6Le9FlehfrFk6e8sGRbNcvJzLBqjx4RyPixcfTj1vK7RxJX%2FK7tZbM1lECZZ&X-Amz-Signature=9d2f333a9e50dfe3e25e8b0ccc420b7eb08191618d17afa129e231efc145f2d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WSGCCD%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQC7Z1ISEs75dQxy%2FWQ2o4wh%2FQwo2Nnhbu0j1K1ZYj078QIhAJw40z95e9FDsz3Ycs%2FHezjbHtNCQ%2BN0FEpjtg3wsbTWKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4iVLxnWNWqm8b2IMq3APiie0sQ9Lls3Rsv4iA%2FpUxpJOF0tRsiziqZGqBygFSoZyLamt3Pv1lWERwjg0l5RN5DTcwGwVbWJC%2BA6fAjTRK%2By8AqUEqlt8XZFBGHCMulOWJVQZDD01YdhfHUbzWS3deV6SAwJ4soUZSioEzpDHS6LgiNPQD8aE7lzf%2FE3xfEaH6l5vSWsJgOIs%2BDC9VrgRkuKrOcsES%2BwmJeQ0SdOL0PjKUB3nm60VOikblKxKEYdDIdWG9%2BzKiTHgzaOVivwXysQOUFtFYNtViB0%2BWuCEoJ7hJyDyy4MaIHEjz7NyFtpE%2Be6oS92uSR%2B9BWoYKC5N1bJpsW7ujcd7t%2FSQXGd%2B1gWqKZRs4zPLizzfpb4gylB5rSSHmQYSzupQ2w0ehxEYBwaXjY7I%2FdmX1lOQMrcc5uWF5UFU8hQiXlo7PLu5PZlSsrugWlaUjyrVUxs21sL40nI74fsMfzZqiZm%2FOBVnGwUKimnbBtTkCttLlLLcUnmpD5P8CfyEQrnWA%2Bg8IOa%2B8YeUvUGxG8t7xXvO%2Bhf8sgjj4vG%2BwdMynZjUHd7LZawG8rgaUFrWjSPgBNvS4ktD6a01WfZOI62wzZrWjC4U04ZX5%2BSaGLyZ1ZTYY1FWKE4q%2FPwzS0D32hs7WHDDr7MXPBjqkAfiBVA%2B3RTm2mNtCGkSmzbFPSNHqN5PQaYV2oY6p%2FBW%2B5owUSKUtL6r%2BIq8bFl0r%2FZUEYI4HMSnmu8a0pWpZ9b4e7TXfaGtPLJnGNjyLS4T70O8rCNwfjzzkWX%2FFFxBUVB4USntTZc94jq8%2FECHtghX3vnNGxpuz6Le9FlehfrFk6e8sGRbNcvJzLBqjx4RyPixcfTj1vK7RxJX%2FK7tZbM1lECZZ&X-Amz-Signature=77bc8595c5740552ed3f1187b95c3bc9e79fd684bf4c9016780082bf1c86a2f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WSGCCD%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQC7Z1ISEs75dQxy%2FWQ2o4wh%2FQwo2Nnhbu0j1K1ZYj078QIhAJw40z95e9FDsz3Ycs%2FHezjbHtNCQ%2BN0FEpjtg3wsbTWKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4iVLxnWNWqm8b2IMq3APiie0sQ9Lls3Rsv4iA%2FpUxpJOF0tRsiziqZGqBygFSoZyLamt3Pv1lWERwjg0l5RN5DTcwGwVbWJC%2BA6fAjTRK%2By8AqUEqlt8XZFBGHCMulOWJVQZDD01YdhfHUbzWS3deV6SAwJ4soUZSioEzpDHS6LgiNPQD8aE7lzf%2FE3xfEaH6l5vSWsJgOIs%2BDC9VrgRkuKrOcsES%2BwmJeQ0SdOL0PjKUB3nm60VOikblKxKEYdDIdWG9%2BzKiTHgzaOVivwXysQOUFtFYNtViB0%2BWuCEoJ7hJyDyy4MaIHEjz7NyFtpE%2Be6oS92uSR%2B9BWoYKC5N1bJpsW7ujcd7t%2FSQXGd%2B1gWqKZRs4zPLizzfpb4gylB5rSSHmQYSzupQ2w0ehxEYBwaXjY7I%2FdmX1lOQMrcc5uWF5UFU8hQiXlo7PLu5PZlSsrugWlaUjyrVUxs21sL40nI74fsMfzZqiZm%2FOBVnGwUKimnbBtTkCttLlLLcUnmpD5P8CfyEQrnWA%2Bg8IOa%2B8YeUvUGxG8t7xXvO%2Bhf8sgjj4vG%2BwdMynZjUHd7LZawG8rgaUFrWjSPgBNvS4ktD6a01WfZOI62wzZrWjC4U04ZX5%2BSaGLyZ1ZTYY1FWKE4q%2FPwzS0D32hs7WHDDr7MXPBjqkAfiBVA%2B3RTm2mNtCGkSmzbFPSNHqN5PQaYV2oY6p%2FBW%2B5owUSKUtL6r%2BIq8bFl0r%2FZUEYI4HMSnmu8a0pWpZ9b4e7TXfaGtPLJnGNjyLS4T70O8rCNwfjzzkWX%2FFFxBUVB4USntTZc94jq8%2FECHtghX3vnNGxpuz6Le9FlehfrFk6e8sGRbNcvJzLBqjx4RyPixcfTj1vK7RxJX%2FK7tZbM1lECZZ&X-Amz-Signature=f5534bff33465ef228682dbe6085559d5723e18b5df4cebac648387ab5f927bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WSGCCD%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQC7Z1ISEs75dQxy%2FWQ2o4wh%2FQwo2Nnhbu0j1K1ZYj078QIhAJw40z95e9FDsz3Ycs%2FHezjbHtNCQ%2BN0FEpjtg3wsbTWKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4iVLxnWNWqm8b2IMq3APiie0sQ9Lls3Rsv4iA%2FpUxpJOF0tRsiziqZGqBygFSoZyLamt3Pv1lWERwjg0l5RN5DTcwGwVbWJC%2BA6fAjTRK%2By8AqUEqlt8XZFBGHCMulOWJVQZDD01YdhfHUbzWS3deV6SAwJ4soUZSioEzpDHS6LgiNPQD8aE7lzf%2FE3xfEaH6l5vSWsJgOIs%2BDC9VrgRkuKrOcsES%2BwmJeQ0SdOL0PjKUB3nm60VOikblKxKEYdDIdWG9%2BzKiTHgzaOVivwXysQOUFtFYNtViB0%2BWuCEoJ7hJyDyy4MaIHEjz7NyFtpE%2Be6oS92uSR%2B9BWoYKC5N1bJpsW7ujcd7t%2FSQXGd%2B1gWqKZRs4zPLizzfpb4gylB5rSSHmQYSzupQ2w0ehxEYBwaXjY7I%2FdmX1lOQMrcc5uWF5UFU8hQiXlo7PLu5PZlSsrugWlaUjyrVUxs21sL40nI74fsMfzZqiZm%2FOBVnGwUKimnbBtTkCttLlLLcUnmpD5P8CfyEQrnWA%2Bg8IOa%2B8YeUvUGxG8t7xXvO%2Bhf8sgjj4vG%2BwdMynZjUHd7LZawG8rgaUFrWjSPgBNvS4ktD6a01WfZOI62wzZrWjC4U04ZX5%2BSaGLyZ1ZTYY1FWKE4q%2FPwzS0D32hs7WHDDr7MXPBjqkAfiBVA%2B3RTm2mNtCGkSmzbFPSNHqN5PQaYV2oY6p%2FBW%2B5owUSKUtL6r%2BIq8bFl0r%2FZUEYI4HMSnmu8a0pWpZ9b4e7TXfaGtPLJnGNjyLS4T70O8rCNwfjzzkWX%2FFFxBUVB4USntTZc94jq8%2FECHtghX3vnNGxpuz6Le9FlehfrFk6e8sGRbNcvJzLBqjx4RyPixcfTj1vK7RxJX%2FK7tZbM1lECZZ&X-Amz-Signature=e3efd5626bca238bd7948b7cc67ba628a0c58731019fa8a7a63370717c0a26c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WSGCCD%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQC7Z1ISEs75dQxy%2FWQ2o4wh%2FQwo2Nnhbu0j1K1ZYj078QIhAJw40z95e9FDsz3Ycs%2FHezjbHtNCQ%2BN0FEpjtg3wsbTWKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4iVLxnWNWqm8b2IMq3APiie0sQ9Lls3Rsv4iA%2FpUxpJOF0tRsiziqZGqBygFSoZyLamt3Pv1lWERwjg0l5RN5DTcwGwVbWJC%2BA6fAjTRK%2By8AqUEqlt8XZFBGHCMulOWJVQZDD01YdhfHUbzWS3deV6SAwJ4soUZSioEzpDHS6LgiNPQD8aE7lzf%2FE3xfEaH6l5vSWsJgOIs%2BDC9VrgRkuKrOcsES%2BwmJeQ0SdOL0PjKUB3nm60VOikblKxKEYdDIdWG9%2BzKiTHgzaOVivwXysQOUFtFYNtViB0%2BWuCEoJ7hJyDyy4MaIHEjz7NyFtpE%2Be6oS92uSR%2B9BWoYKC5N1bJpsW7ujcd7t%2FSQXGd%2B1gWqKZRs4zPLizzfpb4gylB5rSSHmQYSzupQ2w0ehxEYBwaXjY7I%2FdmX1lOQMrcc5uWF5UFU8hQiXlo7PLu5PZlSsrugWlaUjyrVUxs21sL40nI74fsMfzZqiZm%2FOBVnGwUKimnbBtTkCttLlLLcUnmpD5P8CfyEQrnWA%2Bg8IOa%2B8YeUvUGxG8t7xXvO%2Bhf8sgjj4vG%2BwdMynZjUHd7LZawG8rgaUFrWjSPgBNvS4ktD6a01WfZOI62wzZrWjC4U04ZX5%2BSaGLyZ1ZTYY1FWKE4q%2FPwzS0D32hs7WHDDr7MXPBjqkAfiBVA%2B3RTm2mNtCGkSmzbFPSNHqN5PQaYV2oY6p%2FBW%2B5owUSKUtL6r%2BIq8bFl0r%2FZUEYI4HMSnmu8a0pWpZ9b4e7TXfaGtPLJnGNjyLS4T70O8rCNwfjzzkWX%2FFFxBUVB4USntTZc94jq8%2FECHtghX3vnNGxpuz6Le9FlehfrFk6e8sGRbNcvJzLBqjx4RyPixcfTj1vK7RxJX%2FK7tZbM1lECZZ&X-Amz-Signature=ed0f2cce0107554410da1036e4c7b9fce1ee65f658d6302221a456d474ec3e2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WSGCCD%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQC7Z1ISEs75dQxy%2FWQ2o4wh%2FQwo2Nnhbu0j1K1ZYj078QIhAJw40z95e9FDsz3Ycs%2FHezjbHtNCQ%2BN0FEpjtg3wsbTWKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4iVLxnWNWqm8b2IMq3APiie0sQ9Lls3Rsv4iA%2FpUxpJOF0tRsiziqZGqBygFSoZyLamt3Pv1lWERwjg0l5RN5DTcwGwVbWJC%2BA6fAjTRK%2By8AqUEqlt8XZFBGHCMulOWJVQZDD01YdhfHUbzWS3deV6SAwJ4soUZSioEzpDHS6LgiNPQD8aE7lzf%2FE3xfEaH6l5vSWsJgOIs%2BDC9VrgRkuKrOcsES%2BwmJeQ0SdOL0PjKUB3nm60VOikblKxKEYdDIdWG9%2BzKiTHgzaOVivwXysQOUFtFYNtViB0%2BWuCEoJ7hJyDyy4MaIHEjz7NyFtpE%2Be6oS92uSR%2B9BWoYKC5N1bJpsW7ujcd7t%2FSQXGd%2B1gWqKZRs4zPLizzfpb4gylB5rSSHmQYSzupQ2w0ehxEYBwaXjY7I%2FdmX1lOQMrcc5uWF5UFU8hQiXlo7PLu5PZlSsrugWlaUjyrVUxs21sL40nI74fsMfzZqiZm%2FOBVnGwUKimnbBtTkCttLlLLcUnmpD5P8CfyEQrnWA%2Bg8IOa%2B8YeUvUGxG8t7xXvO%2Bhf8sgjj4vG%2BwdMynZjUHd7LZawG8rgaUFrWjSPgBNvS4ktD6a01WfZOI62wzZrWjC4U04ZX5%2BSaGLyZ1ZTYY1FWKE4q%2FPwzS0D32hs7WHDDr7MXPBjqkAfiBVA%2B3RTm2mNtCGkSmzbFPSNHqN5PQaYV2oY6p%2FBW%2B5owUSKUtL6r%2BIq8bFl0r%2FZUEYI4HMSnmu8a0pWpZ9b4e7TXfaGtPLJnGNjyLS4T70O8rCNwfjzzkWX%2FFFxBUVB4USntTZc94jq8%2FECHtghX3vnNGxpuz6Le9FlehfrFk6e8sGRbNcvJzLBqjx4RyPixcfTj1vK7RxJX%2FK7tZbM1lECZZ&X-Amz-Signature=5a44161ab717c3ccbb02cf8578b4b55ad7fd4e4086d73aec3cb63c3a290f7e52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

