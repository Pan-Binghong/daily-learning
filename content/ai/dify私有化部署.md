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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655G37HAT%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkW8SkEBudtfsLieroQrb8aeVcyoISiBRwvtyjJjDJkQIhANNMPEJMyEp095RNb%2F3esYjENdVPn87ATcAOwlUGcGu2Kv8DCEoQABoMNjM3NDIzMTgzODA1Igw9Wn4PZUXvfXmeDXsq3AOnetBF1Aj%2BcTgvZumDLpOgUeGK2mp3BoJxX%2BGwWxm2G6P1esAQW%2FF8j5xH7gnEnDrTWZsmf%2BrRjcSgpZxwSve7DGYvguStESFiDuwW6EjE%2FH3ZxhtPdOkgH5xYsjLsAmZZ05IVNKBXZzrTZo6heM2cOc%2FENT52tgsY07%2FKQ7w%2F%2BrirgY65s3qypA2LLEfr9Psf9SFzDJwYeTH2ltVGm8P%2F%2B7LPuWQDmQRJbp1FRbpayFegGK3wCKkRLL1pNOACm9VsQjPhnTHsC5QXCvO7Xcn5Pq1ITuNo0EK3XTGboM8zDL3hZlxp7rjvELnRJK56lxz3HGKfSdJnaxRJy78cBq%2BAli7wK1Z1FgUFlcD4nRjUZ3hDVOnH%2BfvhNeAqZjJ%2BjFeIsQC2%2FJ5vl44lJkPmGklmQsN9vWcXha0ZR05AZ6TETvV8UExXAz0m33hhZgVlFw3HaZD%2BdKmp4248FJbfvdXdRXbg1EdpchEdhvGJHw6TPTq77iuZ7AdKPU8hDgYDvhhrKSL3ZxMy86x7SPCO9LeyNK3f9Vs3WZmbWgJPqe5mZZpethng2NoZ%2F37dvqYfXftB5QVljtJSoZrKG7VVaF0oFLAeSSRhfT2Co%2FXmvemyhXd9LG5ZxhxoCMjIMzD%2F247JBjqkAX21g3G0wrPVm7Ce0lnf%2BfLVRiQa%2FjeWywJ1Xku8nZWNFFq5lB0MZr%2FeWM5Qc8JI%2BWw45nqvhUpRaKC5QHMY2wnRtE2DI2GvEYLR4KtQgrGJSKTTdWAQ4xjOdJo3bZVWVjfnjVXkcUOxkq2QytfRLMe%2BV1xEzfiL21zQRFlEy0FCS8voyNj4hEDOpVORKW7vubCGAEqX5xSNNGDnhPKAVM9y5egE&X-Amz-Signature=800a7bd9350e7abe664bb534c8bf32f1bcc7d11762cdfd840d50f65100931b3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655G37HAT%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkW8SkEBudtfsLieroQrb8aeVcyoISiBRwvtyjJjDJkQIhANNMPEJMyEp095RNb%2F3esYjENdVPn87ATcAOwlUGcGu2Kv8DCEoQABoMNjM3NDIzMTgzODA1Igw9Wn4PZUXvfXmeDXsq3AOnetBF1Aj%2BcTgvZumDLpOgUeGK2mp3BoJxX%2BGwWxm2G6P1esAQW%2FF8j5xH7gnEnDrTWZsmf%2BrRjcSgpZxwSve7DGYvguStESFiDuwW6EjE%2FH3ZxhtPdOkgH5xYsjLsAmZZ05IVNKBXZzrTZo6heM2cOc%2FENT52tgsY07%2FKQ7w%2F%2BrirgY65s3qypA2LLEfr9Psf9SFzDJwYeTH2ltVGm8P%2F%2B7LPuWQDmQRJbp1FRbpayFegGK3wCKkRLL1pNOACm9VsQjPhnTHsC5QXCvO7Xcn5Pq1ITuNo0EK3XTGboM8zDL3hZlxp7rjvELnRJK56lxz3HGKfSdJnaxRJy78cBq%2BAli7wK1Z1FgUFlcD4nRjUZ3hDVOnH%2BfvhNeAqZjJ%2BjFeIsQC2%2FJ5vl44lJkPmGklmQsN9vWcXha0ZR05AZ6TETvV8UExXAz0m33hhZgVlFw3HaZD%2BdKmp4248FJbfvdXdRXbg1EdpchEdhvGJHw6TPTq77iuZ7AdKPU8hDgYDvhhrKSL3ZxMy86x7SPCO9LeyNK3f9Vs3WZmbWgJPqe5mZZpethng2NoZ%2F37dvqYfXftB5QVljtJSoZrKG7VVaF0oFLAeSSRhfT2Co%2FXmvemyhXd9LG5ZxhxoCMjIMzD%2F247JBjqkAX21g3G0wrPVm7Ce0lnf%2BfLVRiQa%2FjeWywJ1Xku8nZWNFFq5lB0MZr%2FeWM5Qc8JI%2BWw45nqvhUpRaKC5QHMY2wnRtE2DI2GvEYLR4KtQgrGJSKTTdWAQ4xjOdJo3bZVWVjfnjVXkcUOxkq2QytfRLMe%2BV1xEzfiL21zQRFlEy0FCS8voyNj4hEDOpVORKW7vubCGAEqX5xSNNGDnhPKAVM9y5egE&X-Amz-Signature=9349749a70bb18ddcdd9fbad5dc08d0c4d33611f7ac07050934c9bbeb308a9ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655G37HAT%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkW8SkEBudtfsLieroQrb8aeVcyoISiBRwvtyjJjDJkQIhANNMPEJMyEp095RNb%2F3esYjENdVPn87ATcAOwlUGcGu2Kv8DCEoQABoMNjM3NDIzMTgzODA1Igw9Wn4PZUXvfXmeDXsq3AOnetBF1Aj%2BcTgvZumDLpOgUeGK2mp3BoJxX%2BGwWxm2G6P1esAQW%2FF8j5xH7gnEnDrTWZsmf%2BrRjcSgpZxwSve7DGYvguStESFiDuwW6EjE%2FH3ZxhtPdOkgH5xYsjLsAmZZ05IVNKBXZzrTZo6heM2cOc%2FENT52tgsY07%2FKQ7w%2F%2BrirgY65s3qypA2LLEfr9Psf9SFzDJwYeTH2ltVGm8P%2F%2B7LPuWQDmQRJbp1FRbpayFegGK3wCKkRLL1pNOACm9VsQjPhnTHsC5QXCvO7Xcn5Pq1ITuNo0EK3XTGboM8zDL3hZlxp7rjvELnRJK56lxz3HGKfSdJnaxRJy78cBq%2BAli7wK1Z1FgUFlcD4nRjUZ3hDVOnH%2BfvhNeAqZjJ%2BjFeIsQC2%2FJ5vl44lJkPmGklmQsN9vWcXha0ZR05AZ6TETvV8UExXAz0m33hhZgVlFw3HaZD%2BdKmp4248FJbfvdXdRXbg1EdpchEdhvGJHw6TPTq77iuZ7AdKPU8hDgYDvhhrKSL3ZxMy86x7SPCO9LeyNK3f9Vs3WZmbWgJPqe5mZZpethng2NoZ%2F37dvqYfXftB5QVljtJSoZrKG7VVaF0oFLAeSSRhfT2Co%2FXmvemyhXd9LG5ZxhxoCMjIMzD%2F247JBjqkAX21g3G0wrPVm7Ce0lnf%2BfLVRiQa%2FjeWywJ1Xku8nZWNFFq5lB0MZr%2FeWM5Qc8JI%2BWw45nqvhUpRaKC5QHMY2wnRtE2DI2GvEYLR4KtQgrGJSKTTdWAQ4xjOdJo3bZVWVjfnjVXkcUOxkq2QytfRLMe%2BV1xEzfiL21zQRFlEy0FCS8voyNj4hEDOpVORKW7vubCGAEqX5xSNNGDnhPKAVM9y5egE&X-Amz-Signature=8bd9970e159bd2865fe7811f9a4c18be2074d07be3f1e75e14611deeb22a651a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655G37HAT%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkW8SkEBudtfsLieroQrb8aeVcyoISiBRwvtyjJjDJkQIhANNMPEJMyEp095RNb%2F3esYjENdVPn87ATcAOwlUGcGu2Kv8DCEoQABoMNjM3NDIzMTgzODA1Igw9Wn4PZUXvfXmeDXsq3AOnetBF1Aj%2BcTgvZumDLpOgUeGK2mp3BoJxX%2BGwWxm2G6P1esAQW%2FF8j5xH7gnEnDrTWZsmf%2BrRjcSgpZxwSve7DGYvguStESFiDuwW6EjE%2FH3ZxhtPdOkgH5xYsjLsAmZZ05IVNKBXZzrTZo6heM2cOc%2FENT52tgsY07%2FKQ7w%2F%2BrirgY65s3qypA2LLEfr9Psf9SFzDJwYeTH2ltVGm8P%2F%2B7LPuWQDmQRJbp1FRbpayFegGK3wCKkRLL1pNOACm9VsQjPhnTHsC5QXCvO7Xcn5Pq1ITuNo0EK3XTGboM8zDL3hZlxp7rjvELnRJK56lxz3HGKfSdJnaxRJy78cBq%2BAli7wK1Z1FgUFlcD4nRjUZ3hDVOnH%2BfvhNeAqZjJ%2BjFeIsQC2%2FJ5vl44lJkPmGklmQsN9vWcXha0ZR05AZ6TETvV8UExXAz0m33hhZgVlFw3HaZD%2BdKmp4248FJbfvdXdRXbg1EdpchEdhvGJHw6TPTq77iuZ7AdKPU8hDgYDvhhrKSL3ZxMy86x7SPCO9LeyNK3f9Vs3WZmbWgJPqe5mZZpethng2NoZ%2F37dvqYfXftB5QVljtJSoZrKG7VVaF0oFLAeSSRhfT2Co%2FXmvemyhXd9LG5ZxhxoCMjIMzD%2F247JBjqkAX21g3G0wrPVm7Ce0lnf%2BfLVRiQa%2FjeWywJ1Xku8nZWNFFq5lB0MZr%2FeWM5Qc8JI%2BWw45nqvhUpRaKC5QHMY2wnRtE2DI2GvEYLR4KtQgrGJSKTTdWAQ4xjOdJo3bZVWVjfnjVXkcUOxkq2QytfRLMe%2BV1xEzfiL21zQRFlEy0FCS8voyNj4hEDOpVORKW7vubCGAEqX5xSNNGDnhPKAVM9y5egE&X-Amz-Signature=6bb6d113a18ea6e74d6ec27711b7d5c42d7c8e30bbef6b25ace6decb3f618335&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655G37HAT%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkW8SkEBudtfsLieroQrb8aeVcyoISiBRwvtyjJjDJkQIhANNMPEJMyEp095RNb%2F3esYjENdVPn87ATcAOwlUGcGu2Kv8DCEoQABoMNjM3NDIzMTgzODA1Igw9Wn4PZUXvfXmeDXsq3AOnetBF1Aj%2BcTgvZumDLpOgUeGK2mp3BoJxX%2BGwWxm2G6P1esAQW%2FF8j5xH7gnEnDrTWZsmf%2BrRjcSgpZxwSve7DGYvguStESFiDuwW6EjE%2FH3ZxhtPdOkgH5xYsjLsAmZZ05IVNKBXZzrTZo6heM2cOc%2FENT52tgsY07%2FKQ7w%2F%2BrirgY65s3qypA2LLEfr9Psf9SFzDJwYeTH2ltVGm8P%2F%2B7LPuWQDmQRJbp1FRbpayFegGK3wCKkRLL1pNOACm9VsQjPhnTHsC5QXCvO7Xcn5Pq1ITuNo0EK3XTGboM8zDL3hZlxp7rjvELnRJK56lxz3HGKfSdJnaxRJy78cBq%2BAli7wK1Z1FgUFlcD4nRjUZ3hDVOnH%2BfvhNeAqZjJ%2BjFeIsQC2%2FJ5vl44lJkPmGklmQsN9vWcXha0ZR05AZ6TETvV8UExXAz0m33hhZgVlFw3HaZD%2BdKmp4248FJbfvdXdRXbg1EdpchEdhvGJHw6TPTq77iuZ7AdKPU8hDgYDvhhrKSL3ZxMy86x7SPCO9LeyNK3f9Vs3WZmbWgJPqe5mZZpethng2NoZ%2F37dvqYfXftB5QVljtJSoZrKG7VVaF0oFLAeSSRhfT2Co%2FXmvemyhXd9LG5ZxhxoCMjIMzD%2F247JBjqkAX21g3G0wrPVm7Ce0lnf%2BfLVRiQa%2FjeWywJ1Xku8nZWNFFq5lB0MZr%2FeWM5Qc8JI%2BWw45nqvhUpRaKC5QHMY2wnRtE2DI2GvEYLR4KtQgrGJSKTTdWAQ4xjOdJo3bZVWVjfnjVXkcUOxkq2QytfRLMe%2BV1xEzfiL21zQRFlEy0FCS8voyNj4hEDOpVORKW7vubCGAEqX5xSNNGDnhPKAVM9y5egE&X-Amz-Signature=b71883b83594a2892f2f28cb8c080d1166850248ed765dd9237076a6ffb34c4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655G37HAT%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkW8SkEBudtfsLieroQrb8aeVcyoISiBRwvtyjJjDJkQIhANNMPEJMyEp095RNb%2F3esYjENdVPn87ATcAOwlUGcGu2Kv8DCEoQABoMNjM3NDIzMTgzODA1Igw9Wn4PZUXvfXmeDXsq3AOnetBF1Aj%2BcTgvZumDLpOgUeGK2mp3BoJxX%2BGwWxm2G6P1esAQW%2FF8j5xH7gnEnDrTWZsmf%2BrRjcSgpZxwSve7DGYvguStESFiDuwW6EjE%2FH3ZxhtPdOkgH5xYsjLsAmZZ05IVNKBXZzrTZo6heM2cOc%2FENT52tgsY07%2FKQ7w%2F%2BrirgY65s3qypA2LLEfr9Psf9SFzDJwYeTH2ltVGm8P%2F%2B7LPuWQDmQRJbp1FRbpayFegGK3wCKkRLL1pNOACm9VsQjPhnTHsC5QXCvO7Xcn5Pq1ITuNo0EK3XTGboM8zDL3hZlxp7rjvELnRJK56lxz3HGKfSdJnaxRJy78cBq%2BAli7wK1Z1FgUFlcD4nRjUZ3hDVOnH%2BfvhNeAqZjJ%2BjFeIsQC2%2FJ5vl44lJkPmGklmQsN9vWcXha0ZR05AZ6TETvV8UExXAz0m33hhZgVlFw3HaZD%2BdKmp4248FJbfvdXdRXbg1EdpchEdhvGJHw6TPTq77iuZ7AdKPU8hDgYDvhhrKSL3ZxMy86x7SPCO9LeyNK3f9Vs3WZmbWgJPqe5mZZpethng2NoZ%2F37dvqYfXftB5QVljtJSoZrKG7VVaF0oFLAeSSRhfT2Co%2FXmvemyhXd9LG5ZxhxoCMjIMzD%2F247JBjqkAX21g3G0wrPVm7Ce0lnf%2BfLVRiQa%2FjeWywJ1Xku8nZWNFFq5lB0MZr%2FeWM5Qc8JI%2BWw45nqvhUpRaKC5QHMY2wnRtE2DI2GvEYLR4KtQgrGJSKTTdWAQ4xjOdJo3bZVWVjfnjVXkcUOxkq2QytfRLMe%2BV1xEzfiL21zQRFlEy0FCS8voyNj4hEDOpVORKW7vubCGAEqX5xSNNGDnhPKAVM9y5egE&X-Amz-Signature=916b7ba5f709aa7b6286f86afe6f1461cc4b3024ab067bcd141a1dc4565167c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655G37HAT%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkW8SkEBudtfsLieroQrb8aeVcyoISiBRwvtyjJjDJkQIhANNMPEJMyEp095RNb%2F3esYjENdVPn87ATcAOwlUGcGu2Kv8DCEoQABoMNjM3NDIzMTgzODA1Igw9Wn4PZUXvfXmeDXsq3AOnetBF1Aj%2BcTgvZumDLpOgUeGK2mp3BoJxX%2BGwWxm2G6P1esAQW%2FF8j5xH7gnEnDrTWZsmf%2BrRjcSgpZxwSve7DGYvguStESFiDuwW6EjE%2FH3ZxhtPdOkgH5xYsjLsAmZZ05IVNKBXZzrTZo6heM2cOc%2FENT52tgsY07%2FKQ7w%2F%2BrirgY65s3qypA2LLEfr9Psf9SFzDJwYeTH2ltVGm8P%2F%2B7LPuWQDmQRJbp1FRbpayFegGK3wCKkRLL1pNOACm9VsQjPhnTHsC5QXCvO7Xcn5Pq1ITuNo0EK3XTGboM8zDL3hZlxp7rjvELnRJK56lxz3HGKfSdJnaxRJy78cBq%2BAli7wK1Z1FgUFlcD4nRjUZ3hDVOnH%2BfvhNeAqZjJ%2BjFeIsQC2%2FJ5vl44lJkPmGklmQsN9vWcXha0ZR05AZ6TETvV8UExXAz0m33hhZgVlFw3HaZD%2BdKmp4248FJbfvdXdRXbg1EdpchEdhvGJHw6TPTq77iuZ7AdKPU8hDgYDvhhrKSL3ZxMy86x7SPCO9LeyNK3f9Vs3WZmbWgJPqe5mZZpethng2NoZ%2F37dvqYfXftB5QVljtJSoZrKG7VVaF0oFLAeSSRhfT2Co%2FXmvemyhXd9LG5ZxhxoCMjIMzD%2F247JBjqkAX21g3G0wrPVm7Ce0lnf%2BfLVRiQa%2FjeWywJ1Xku8nZWNFFq5lB0MZr%2FeWM5Qc8JI%2BWw45nqvhUpRaKC5QHMY2wnRtE2DI2GvEYLR4KtQgrGJSKTTdWAQ4xjOdJo3bZVWVjfnjVXkcUOxkq2QytfRLMe%2BV1xEzfiL21zQRFlEy0FCS8voyNj4hEDOpVORKW7vubCGAEqX5xSNNGDnhPKAVM9y5egE&X-Amz-Signature=30d4b281ef11aedc024b3c6574221133489270bfbf6cda65175c3479c5332800&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655G37HAT%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkW8SkEBudtfsLieroQrb8aeVcyoISiBRwvtyjJjDJkQIhANNMPEJMyEp095RNb%2F3esYjENdVPn87ATcAOwlUGcGu2Kv8DCEoQABoMNjM3NDIzMTgzODA1Igw9Wn4PZUXvfXmeDXsq3AOnetBF1Aj%2BcTgvZumDLpOgUeGK2mp3BoJxX%2BGwWxm2G6P1esAQW%2FF8j5xH7gnEnDrTWZsmf%2BrRjcSgpZxwSve7DGYvguStESFiDuwW6EjE%2FH3ZxhtPdOkgH5xYsjLsAmZZ05IVNKBXZzrTZo6heM2cOc%2FENT52tgsY07%2FKQ7w%2F%2BrirgY65s3qypA2LLEfr9Psf9SFzDJwYeTH2ltVGm8P%2F%2B7LPuWQDmQRJbp1FRbpayFegGK3wCKkRLL1pNOACm9VsQjPhnTHsC5QXCvO7Xcn5Pq1ITuNo0EK3XTGboM8zDL3hZlxp7rjvELnRJK56lxz3HGKfSdJnaxRJy78cBq%2BAli7wK1Z1FgUFlcD4nRjUZ3hDVOnH%2BfvhNeAqZjJ%2BjFeIsQC2%2FJ5vl44lJkPmGklmQsN9vWcXha0ZR05AZ6TETvV8UExXAz0m33hhZgVlFw3HaZD%2BdKmp4248FJbfvdXdRXbg1EdpchEdhvGJHw6TPTq77iuZ7AdKPU8hDgYDvhhrKSL3ZxMy86x7SPCO9LeyNK3f9Vs3WZmbWgJPqe5mZZpethng2NoZ%2F37dvqYfXftB5QVljtJSoZrKG7VVaF0oFLAeSSRhfT2Co%2FXmvemyhXd9LG5ZxhxoCMjIMzD%2F247JBjqkAX21g3G0wrPVm7Ce0lnf%2BfLVRiQa%2FjeWywJ1Xku8nZWNFFq5lB0MZr%2FeWM5Qc8JI%2BWw45nqvhUpRaKC5QHMY2wnRtE2DI2GvEYLR4KtQgrGJSKTTdWAQ4xjOdJo3bZVWVjfnjVXkcUOxkq2QytfRLMe%2BV1xEzfiL21zQRFlEy0FCS8voyNj4hEDOpVORKW7vubCGAEqX5xSNNGDnhPKAVM9y5egE&X-Amz-Signature=a29baffd4a7dc10c6136ff46a940d74233a332e5fc272703a1d22fbe870117bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655G37HAT%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkW8SkEBudtfsLieroQrb8aeVcyoISiBRwvtyjJjDJkQIhANNMPEJMyEp095RNb%2F3esYjENdVPn87ATcAOwlUGcGu2Kv8DCEoQABoMNjM3NDIzMTgzODA1Igw9Wn4PZUXvfXmeDXsq3AOnetBF1Aj%2BcTgvZumDLpOgUeGK2mp3BoJxX%2BGwWxm2G6P1esAQW%2FF8j5xH7gnEnDrTWZsmf%2BrRjcSgpZxwSve7DGYvguStESFiDuwW6EjE%2FH3ZxhtPdOkgH5xYsjLsAmZZ05IVNKBXZzrTZo6heM2cOc%2FENT52tgsY07%2FKQ7w%2F%2BrirgY65s3qypA2LLEfr9Psf9SFzDJwYeTH2ltVGm8P%2F%2B7LPuWQDmQRJbp1FRbpayFegGK3wCKkRLL1pNOACm9VsQjPhnTHsC5QXCvO7Xcn5Pq1ITuNo0EK3XTGboM8zDL3hZlxp7rjvELnRJK56lxz3HGKfSdJnaxRJy78cBq%2BAli7wK1Z1FgUFlcD4nRjUZ3hDVOnH%2BfvhNeAqZjJ%2BjFeIsQC2%2FJ5vl44lJkPmGklmQsN9vWcXha0ZR05AZ6TETvV8UExXAz0m33hhZgVlFw3HaZD%2BdKmp4248FJbfvdXdRXbg1EdpchEdhvGJHw6TPTq77iuZ7AdKPU8hDgYDvhhrKSL3ZxMy86x7SPCO9LeyNK3f9Vs3WZmbWgJPqe5mZZpethng2NoZ%2F37dvqYfXftB5QVljtJSoZrKG7VVaF0oFLAeSSRhfT2Co%2FXmvemyhXd9LG5ZxhxoCMjIMzD%2F247JBjqkAX21g3G0wrPVm7Ce0lnf%2BfLVRiQa%2FjeWywJ1Xku8nZWNFFq5lB0MZr%2FeWM5Qc8JI%2BWw45nqvhUpRaKC5QHMY2wnRtE2DI2GvEYLR4KtQgrGJSKTTdWAQ4xjOdJo3bZVWVjfnjVXkcUOxkq2QytfRLMe%2BV1xEzfiL21zQRFlEy0FCS8voyNj4hEDOpVORKW7vubCGAEqX5xSNNGDnhPKAVM9y5egE&X-Amz-Signature=59a798badb7869b137500b0673af7bee72540883f66549d4b51fba7bb9029c7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655G37HAT%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkW8SkEBudtfsLieroQrb8aeVcyoISiBRwvtyjJjDJkQIhANNMPEJMyEp095RNb%2F3esYjENdVPn87ATcAOwlUGcGu2Kv8DCEoQABoMNjM3NDIzMTgzODA1Igw9Wn4PZUXvfXmeDXsq3AOnetBF1Aj%2BcTgvZumDLpOgUeGK2mp3BoJxX%2BGwWxm2G6P1esAQW%2FF8j5xH7gnEnDrTWZsmf%2BrRjcSgpZxwSve7DGYvguStESFiDuwW6EjE%2FH3ZxhtPdOkgH5xYsjLsAmZZ05IVNKBXZzrTZo6heM2cOc%2FENT52tgsY07%2FKQ7w%2F%2BrirgY65s3qypA2LLEfr9Psf9SFzDJwYeTH2ltVGm8P%2F%2B7LPuWQDmQRJbp1FRbpayFegGK3wCKkRLL1pNOACm9VsQjPhnTHsC5QXCvO7Xcn5Pq1ITuNo0EK3XTGboM8zDL3hZlxp7rjvELnRJK56lxz3HGKfSdJnaxRJy78cBq%2BAli7wK1Z1FgUFlcD4nRjUZ3hDVOnH%2BfvhNeAqZjJ%2BjFeIsQC2%2FJ5vl44lJkPmGklmQsN9vWcXha0ZR05AZ6TETvV8UExXAz0m33hhZgVlFw3HaZD%2BdKmp4248FJbfvdXdRXbg1EdpchEdhvGJHw6TPTq77iuZ7AdKPU8hDgYDvhhrKSL3ZxMy86x7SPCO9LeyNK3f9Vs3WZmbWgJPqe5mZZpethng2NoZ%2F37dvqYfXftB5QVljtJSoZrKG7VVaF0oFLAeSSRhfT2Co%2FXmvemyhXd9LG5ZxhxoCMjIMzD%2F247JBjqkAX21g3G0wrPVm7Ce0lnf%2BfLVRiQa%2FjeWywJ1Xku8nZWNFFq5lB0MZr%2FeWM5Qc8JI%2BWw45nqvhUpRaKC5QHMY2wnRtE2DI2GvEYLR4KtQgrGJSKTTdWAQ4xjOdJo3bZVWVjfnjVXkcUOxkq2QytfRLMe%2BV1xEzfiL21zQRFlEy0FCS8voyNj4hEDOpVORKW7vubCGAEqX5xSNNGDnhPKAVM9y5egE&X-Amz-Signature=b031f439aa18d85a7bc088fc0fc0960efc388997a769a9c233e86a6b4a45d670&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

