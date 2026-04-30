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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DHS5SEX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIEpAPkfI0gU5Fo3y%2BtIBdeJtY5X3adQkVVEPBu51SJ86AiEA4av1%2BmzlEZUuHRIl9LlOSGhPlisSnFLHbdprkB4VvYIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDCSP6Js%2FyjtyPIrRPCrcA%2BXb6g35IPJrwdY%2FlbvHMO%2Bt0GAktniNoaU9HVu6VuIr0lBDCNN7KUPnG4pzVCdnkhdnXjrM%2B4GmlcoSLh3w3oe2DE0Jzj2NzJRjABJnI%2FxiMUEVbvzNC2aGwWXJLf2zRASPhAGtHzGveMIdWed%2Fzq9zhwruO%2FN45TlFslzK3pp4iL1o7X7YIi5TJdZRkyvHpfxP%2FcHeZdMhFlK%2Fy0uN6FT5b5KiQ%2FFTQ83k%2BbeTZR%2BwGshE9zbGLh9diQlDMwlBeosPdBZdkUys7Zm8TlLdlgeFC5gtC4lrUh0ha%2Fivrvl95VP8vfCX%2FWJUC%2BV4r9KSBvDhO9VVJyeADbilcyTiVE4nYDY5sp%2Bqe1Vbja3E6fwgKNvmhvgK62XCWSsMFx5JiFjdUDmhxKU8aUPLIBpI83u%2BHeQZO1pGv6Y%2B%2BihUh3xfBt%2FBJ7jUEmpPpO%2F6CP%2BSULYwsc7A1dgdssQYqZRLfqi0z6yqshBskJDhfl5hvO6XvGnTJhZrG7hl4Qp5Gl9%2FIRv%2FnJYQxQor9EeqGQE%2FhHM1shJl3HYNQ8Nb65%2FLggUUqybr7uT9lGm1Bjf8qMCNcgrNeYVQb2KCKVrn2fZWEMTYgYlw%2BL7zUTFzkaavgaLK8JpgIyJovDOZagNdMNexy88GOqUBDkGcUAGLcTbs2nEmXMZBpYKsnZ5J0sVjv%2Fruzei8h%2Bk9RJqF3%2B8vQiEjiRvUFsC6aX4qsDESlPhqy1S5ZtigN4RW2CvEuaFZ%2Fiqv4L4rAOHqFeKIfoqMxDS9rT6Kkdezs9qkLeECAfDWcZzlwFnq7YisyOGMe3fn5sCdUO%2Bbh45DNWbtWHAIrj9SH64Nzq8alBihA9KxtPYac2ObKjGkeF1n%2BrxA&X-Amz-Signature=b2636259e8d995781bc94a058cbf61de43eab9946e4cffac02d0dc276f05d93a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DHS5SEX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIEpAPkfI0gU5Fo3y%2BtIBdeJtY5X3adQkVVEPBu51SJ86AiEA4av1%2BmzlEZUuHRIl9LlOSGhPlisSnFLHbdprkB4VvYIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDCSP6Js%2FyjtyPIrRPCrcA%2BXb6g35IPJrwdY%2FlbvHMO%2Bt0GAktniNoaU9HVu6VuIr0lBDCNN7KUPnG4pzVCdnkhdnXjrM%2B4GmlcoSLh3w3oe2DE0Jzj2NzJRjABJnI%2FxiMUEVbvzNC2aGwWXJLf2zRASPhAGtHzGveMIdWed%2Fzq9zhwruO%2FN45TlFslzK3pp4iL1o7X7YIi5TJdZRkyvHpfxP%2FcHeZdMhFlK%2Fy0uN6FT5b5KiQ%2FFTQ83k%2BbeTZR%2BwGshE9zbGLh9diQlDMwlBeosPdBZdkUys7Zm8TlLdlgeFC5gtC4lrUh0ha%2Fivrvl95VP8vfCX%2FWJUC%2BV4r9KSBvDhO9VVJyeADbilcyTiVE4nYDY5sp%2Bqe1Vbja3E6fwgKNvmhvgK62XCWSsMFx5JiFjdUDmhxKU8aUPLIBpI83u%2BHeQZO1pGv6Y%2B%2BihUh3xfBt%2FBJ7jUEmpPpO%2F6CP%2BSULYwsc7A1dgdssQYqZRLfqi0z6yqshBskJDhfl5hvO6XvGnTJhZrG7hl4Qp5Gl9%2FIRv%2FnJYQxQor9EeqGQE%2FhHM1shJl3HYNQ8Nb65%2FLggUUqybr7uT9lGm1Bjf8qMCNcgrNeYVQb2KCKVrn2fZWEMTYgYlw%2BL7zUTFzkaavgaLK8JpgIyJovDOZagNdMNexy88GOqUBDkGcUAGLcTbs2nEmXMZBpYKsnZ5J0sVjv%2Fruzei8h%2Bk9RJqF3%2B8vQiEjiRvUFsC6aX4qsDESlPhqy1S5ZtigN4RW2CvEuaFZ%2Fiqv4L4rAOHqFeKIfoqMxDS9rT6Kkdezs9qkLeECAfDWcZzlwFnq7YisyOGMe3fn5sCdUO%2Bbh45DNWbtWHAIrj9SH64Nzq8alBihA9KxtPYac2ObKjGkeF1n%2BrxA&X-Amz-Signature=77200720f9ff6da19a82d11977ba76fd24be19ee96115110dbd6c49070212cf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DHS5SEX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIEpAPkfI0gU5Fo3y%2BtIBdeJtY5X3adQkVVEPBu51SJ86AiEA4av1%2BmzlEZUuHRIl9LlOSGhPlisSnFLHbdprkB4VvYIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDCSP6Js%2FyjtyPIrRPCrcA%2BXb6g35IPJrwdY%2FlbvHMO%2Bt0GAktniNoaU9HVu6VuIr0lBDCNN7KUPnG4pzVCdnkhdnXjrM%2B4GmlcoSLh3w3oe2DE0Jzj2NzJRjABJnI%2FxiMUEVbvzNC2aGwWXJLf2zRASPhAGtHzGveMIdWed%2Fzq9zhwruO%2FN45TlFslzK3pp4iL1o7X7YIi5TJdZRkyvHpfxP%2FcHeZdMhFlK%2Fy0uN6FT5b5KiQ%2FFTQ83k%2BbeTZR%2BwGshE9zbGLh9diQlDMwlBeosPdBZdkUys7Zm8TlLdlgeFC5gtC4lrUh0ha%2Fivrvl95VP8vfCX%2FWJUC%2BV4r9KSBvDhO9VVJyeADbilcyTiVE4nYDY5sp%2Bqe1Vbja3E6fwgKNvmhvgK62XCWSsMFx5JiFjdUDmhxKU8aUPLIBpI83u%2BHeQZO1pGv6Y%2B%2BihUh3xfBt%2FBJ7jUEmpPpO%2F6CP%2BSULYwsc7A1dgdssQYqZRLfqi0z6yqshBskJDhfl5hvO6XvGnTJhZrG7hl4Qp5Gl9%2FIRv%2FnJYQxQor9EeqGQE%2FhHM1shJl3HYNQ8Nb65%2FLggUUqybr7uT9lGm1Bjf8qMCNcgrNeYVQb2KCKVrn2fZWEMTYgYlw%2BL7zUTFzkaavgaLK8JpgIyJovDOZagNdMNexy88GOqUBDkGcUAGLcTbs2nEmXMZBpYKsnZ5J0sVjv%2Fruzei8h%2Bk9RJqF3%2B8vQiEjiRvUFsC6aX4qsDESlPhqy1S5ZtigN4RW2CvEuaFZ%2Fiqv4L4rAOHqFeKIfoqMxDS9rT6Kkdezs9qkLeECAfDWcZzlwFnq7YisyOGMe3fn5sCdUO%2Bbh45DNWbtWHAIrj9SH64Nzq8alBihA9KxtPYac2ObKjGkeF1n%2BrxA&X-Amz-Signature=6458db45787aaa8cad97fa8de36b80ac321e544104c12df368dc5a6b4fba48bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DHS5SEX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIEpAPkfI0gU5Fo3y%2BtIBdeJtY5X3adQkVVEPBu51SJ86AiEA4av1%2BmzlEZUuHRIl9LlOSGhPlisSnFLHbdprkB4VvYIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDCSP6Js%2FyjtyPIrRPCrcA%2BXb6g35IPJrwdY%2FlbvHMO%2Bt0GAktniNoaU9HVu6VuIr0lBDCNN7KUPnG4pzVCdnkhdnXjrM%2B4GmlcoSLh3w3oe2DE0Jzj2NzJRjABJnI%2FxiMUEVbvzNC2aGwWXJLf2zRASPhAGtHzGveMIdWed%2Fzq9zhwruO%2FN45TlFslzK3pp4iL1o7X7YIi5TJdZRkyvHpfxP%2FcHeZdMhFlK%2Fy0uN6FT5b5KiQ%2FFTQ83k%2BbeTZR%2BwGshE9zbGLh9diQlDMwlBeosPdBZdkUys7Zm8TlLdlgeFC5gtC4lrUh0ha%2Fivrvl95VP8vfCX%2FWJUC%2BV4r9KSBvDhO9VVJyeADbilcyTiVE4nYDY5sp%2Bqe1Vbja3E6fwgKNvmhvgK62XCWSsMFx5JiFjdUDmhxKU8aUPLIBpI83u%2BHeQZO1pGv6Y%2B%2BihUh3xfBt%2FBJ7jUEmpPpO%2F6CP%2BSULYwsc7A1dgdssQYqZRLfqi0z6yqshBskJDhfl5hvO6XvGnTJhZrG7hl4Qp5Gl9%2FIRv%2FnJYQxQor9EeqGQE%2FhHM1shJl3HYNQ8Nb65%2FLggUUqybr7uT9lGm1Bjf8qMCNcgrNeYVQb2KCKVrn2fZWEMTYgYlw%2BL7zUTFzkaavgaLK8JpgIyJovDOZagNdMNexy88GOqUBDkGcUAGLcTbs2nEmXMZBpYKsnZ5J0sVjv%2Fruzei8h%2Bk9RJqF3%2B8vQiEjiRvUFsC6aX4qsDESlPhqy1S5ZtigN4RW2CvEuaFZ%2Fiqv4L4rAOHqFeKIfoqMxDS9rT6Kkdezs9qkLeECAfDWcZzlwFnq7YisyOGMe3fn5sCdUO%2Bbh45DNWbtWHAIrj9SH64Nzq8alBihA9KxtPYac2ObKjGkeF1n%2BrxA&X-Amz-Signature=b2b23cdd00a5bcd50aa6d627497f7f05f0d20fc3407d5be1464666b7a83842a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DHS5SEX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIEpAPkfI0gU5Fo3y%2BtIBdeJtY5X3adQkVVEPBu51SJ86AiEA4av1%2BmzlEZUuHRIl9LlOSGhPlisSnFLHbdprkB4VvYIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDCSP6Js%2FyjtyPIrRPCrcA%2BXb6g35IPJrwdY%2FlbvHMO%2Bt0GAktniNoaU9HVu6VuIr0lBDCNN7KUPnG4pzVCdnkhdnXjrM%2B4GmlcoSLh3w3oe2DE0Jzj2NzJRjABJnI%2FxiMUEVbvzNC2aGwWXJLf2zRASPhAGtHzGveMIdWed%2Fzq9zhwruO%2FN45TlFslzK3pp4iL1o7X7YIi5TJdZRkyvHpfxP%2FcHeZdMhFlK%2Fy0uN6FT5b5KiQ%2FFTQ83k%2BbeTZR%2BwGshE9zbGLh9diQlDMwlBeosPdBZdkUys7Zm8TlLdlgeFC5gtC4lrUh0ha%2Fivrvl95VP8vfCX%2FWJUC%2BV4r9KSBvDhO9VVJyeADbilcyTiVE4nYDY5sp%2Bqe1Vbja3E6fwgKNvmhvgK62XCWSsMFx5JiFjdUDmhxKU8aUPLIBpI83u%2BHeQZO1pGv6Y%2B%2BihUh3xfBt%2FBJ7jUEmpPpO%2F6CP%2BSULYwsc7A1dgdssQYqZRLfqi0z6yqshBskJDhfl5hvO6XvGnTJhZrG7hl4Qp5Gl9%2FIRv%2FnJYQxQor9EeqGQE%2FhHM1shJl3HYNQ8Nb65%2FLggUUqybr7uT9lGm1Bjf8qMCNcgrNeYVQb2KCKVrn2fZWEMTYgYlw%2BL7zUTFzkaavgaLK8JpgIyJovDOZagNdMNexy88GOqUBDkGcUAGLcTbs2nEmXMZBpYKsnZ5J0sVjv%2Fruzei8h%2Bk9RJqF3%2B8vQiEjiRvUFsC6aX4qsDESlPhqy1S5ZtigN4RW2CvEuaFZ%2Fiqv4L4rAOHqFeKIfoqMxDS9rT6Kkdezs9qkLeECAfDWcZzlwFnq7YisyOGMe3fn5sCdUO%2Bbh45DNWbtWHAIrj9SH64Nzq8alBihA9KxtPYac2ObKjGkeF1n%2BrxA&X-Amz-Signature=a66665e64af1cd494c290f376ca236594a0a0079390163fc794ee5a3050eabd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DHS5SEX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIEpAPkfI0gU5Fo3y%2BtIBdeJtY5X3adQkVVEPBu51SJ86AiEA4av1%2BmzlEZUuHRIl9LlOSGhPlisSnFLHbdprkB4VvYIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDCSP6Js%2FyjtyPIrRPCrcA%2BXb6g35IPJrwdY%2FlbvHMO%2Bt0GAktniNoaU9HVu6VuIr0lBDCNN7KUPnG4pzVCdnkhdnXjrM%2B4GmlcoSLh3w3oe2DE0Jzj2NzJRjABJnI%2FxiMUEVbvzNC2aGwWXJLf2zRASPhAGtHzGveMIdWed%2Fzq9zhwruO%2FN45TlFslzK3pp4iL1o7X7YIi5TJdZRkyvHpfxP%2FcHeZdMhFlK%2Fy0uN6FT5b5KiQ%2FFTQ83k%2BbeTZR%2BwGshE9zbGLh9diQlDMwlBeosPdBZdkUys7Zm8TlLdlgeFC5gtC4lrUh0ha%2Fivrvl95VP8vfCX%2FWJUC%2BV4r9KSBvDhO9VVJyeADbilcyTiVE4nYDY5sp%2Bqe1Vbja3E6fwgKNvmhvgK62XCWSsMFx5JiFjdUDmhxKU8aUPLIBpI83u%2BHeQZO1pGv6Y%2B%2BihUh3xfBt%2FBJ7jUEmpPpO%2F6CP%2BSULYwsc7A1dgdssQYqZRLfqi0z6yqshBskJDhfl5hvO6XvGnTJhZrG7hl4Qp5Gl9%2FIRv%2FnJYQxQor9EeqGQE%2FhHM1shJl3HYNQ8Nb65%2FLggUUqybr7uT9lGm1Bjf8qMCNcgrNeYVQb2KCKVrn2fZWEMTYgYlw%2BL7zUTFzkaavgaLK8JpgIyJovDOZagNdMNexy88GOqUBDkGcUAGLcTbs2nEmXMZBpYKsnZ5J0sVjv%2Fruzei8h%2Bk9RJqF3%2B8vQiEjiRvUFsC6aX4qsDESlPhqy1S5ZtigN4RW2CvEuaFZ%2Fiqv4L4rAOHqFeKIfoqMxDS9rT6Kkdezs9qkLeECAfDWcZzlwFnq7YisyOGMe3fn5sCdUO%2Bbh45DNWbtWHAIrj9SH64Nzq8alBihA9KxtPYac2ObKjGkeF1n%2BrxA&X-Amz-Signature=8ebaec753904a2a4ecfe0324035702e3568ad70e79d7b5879a69bbb0b27c9598&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DHS5SEX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIEpAPkfI0gU5Fo3y%2BtIBdeJtY5X3adQkVVEPBu51SJ86AiEA4av1%2BmzlEZUuHRIl9LlOSGhPlisSnFLHbdprkB4VvYIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDCSP6Js%2FyjtyPIrRPCrcA%2BXb6g35IPJrwdY%2FlbvHMO%2Bt0GAktniNoaU9HVu6VuIr0lBDCNN7KUPnG4pzVCdnkhdnXjrM%2B4GmlcoSLh3w3oe2DE0Jzj2NzJRjABJnI%2FxiMUEVbvzNC2aGwWXJLf2zRASPhAGtHzGveMIdWed%2Fzq9zhwruO%2FN45TlFslzK3pp4iL1o7X7YIi5TJdZRkyvHpfxP%2FcHeZdMhFlK%2Fy0uN6FT5b5KiQ%2FFTQ83k%2BbeTZR%2BwGshE9zbGLh9diQlDMwlBeosPdBZdkUys7Zm8TlLdlgeFC5gtC4lrUh0ha%2Fivrvl95VP8vfCX%2FWJUC%2BV4r9KSBvDhO9VVJyeADbilcyTiVE4nYDY5sp%2Bqe1Vbja3E6fwgKNvmhvgK62XCWSsMFx5JiFjdUDmhxKU8aUPLIBpI83u%2BHeQZO1pGv6Y%2B%2BihUh3xfBt%2FBJ7jUEmpPpO%2F6CP%2BSULYwsc7A1dgdssQYqZRLfqi0z6yqshBskJDhfl5hvO6XvGnTJhZrG7hl4Qp5Gl9%2FIRv%2FnJYQxQor9EeqGQE%2FhHM1shJl3HYNQ8Nb65%2FLggUUqybr7uT9lGm1Bjf8qMCNcgrNeYVQb2KCKVrn2fZWEMTYgYlw%2BL7zUTFzkaavgaLK8JpgIyJovDOZagNdMNexy88GOqUBDkGcUAGLcTbs2nEmXMZBpYKsnZ5J0sVjv%2Fruzei8h%2Bk9RJqF3%2B8vQiEjiRvUFsC6aX4qsDESlPhqy1S5ZtigN4RW2CvEuaFZ%2Fiqv4L4rAOHqFeKIfoqMxDS9rT6Kkdezs9qkLeECAfDWcZzlwFnq7YisyOGMe3fn5sCdUO%2Bbh45DNWbtWHAIrj9SH64Nzq8alBihA9KxtPYac2ObKjGkeF1n%2BrxA&X-Amz-Signature=9768a47fddcaa5f61f6cbaab35a2be5d3e4a62547781fd19a9489b40276c0519&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DHS5SEX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIEpAPkfI0gU5Fo3y%2BtIBdeJtY5X3adQkVVEPBu51SJ86AiEA4av1%2BmzlEZUuHRIl9LlOSGhPlisSnFLHbdprkB4VvYIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDCSP6Js%2FyjtyPIrRPCrcA%2BXb6g35IPJrwdY%2FlbvHMO%2Bt0GAktniNoaU9HVu6VuIr0lBDCNN7KUPnG4pzVCdnkhdnXjrM%2B4GmlcoSLh3w3oe2DE0Jzj2NzJRjABJnI%2FxiMUEVbvzNC2aGwWXJLf2zRASPhAGtHzGveMIdWed%2Fzq9zhwruO%2FN45TlFslzK3pp4iL1o7X7YIi5TJdZRkyvHpfxP%2FcHeZdMhFlK%2Fy0uN6FT5b5KiQ%2FFTQ83k%2BbeTZR%2BwGshE9zbGLh9diQlDMwlBeosPdBZdkUys7Zm8TlLdlgeFC5gtC4lrUh0ha%2Fivrvl95VP8vfCX%2FWJUC%2BV4r9KSBvDhO9VVJyeADbilcyTiVE4nYDY5sp%2Bqe1Vbja3E6fwgKNvmhvgK62XCWSsMFx5JiFjdUDmhxKU8aUPLIBpI83u%2BHeQZO1pGv6Y%2B%2BihUh3xfBt%2FBJ7jUEmpPpO%2F6CP%2BSULYwsc7A1dgdssQYqZRLfqi0z6yqshBskJDhfl5hvO6XvGnTJhZrG7hl4Qp5Gl9%2FIRv%2FnJYQxQor9EeqGQE%2FhHM1shJl3HYNQ8Nb65%2FLggUUqybr7uT9lGm1Bjf8qMCNcgrNeYVQb2KCKVrn2fZWEMTYgYlw%2BL7zUTFzkaavgaLK8JpgIyJovDOZagNdMNexy88GOqUBDkGcUAGLcTbs2nEmXMZBpYKsnZ5J0sVjv%2Fruzei8h%2Bk9RJqF3%2B8vQiEjiRvUFsC6aX4qsDESlPhqy1S5ZtigN4RW2CvEuaFZ%2Fiqv4L4rAOHqFeKIfoqMxDS9rT6Kkdezs9qkLeECAfDWcZzlwFnq7YisyOGMe3fn5sCdUO%2Bbh45DNWbtWHAIrj9SH64Nzq8alBihA9KxtPYac2ObKjGkeF1n%2BrxA&X-Amz-Signature=0979a8fb3ef5e8e8a7e04b0cb82610b7235fd599e3be38b9cf0f46ea01ec58be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DHS5SEX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIEpAPkfI0gU5Fo3y%2BtIBdeJtY5X3adQkVVEPBu51SJ86AiEA4av1%2BmzlEZUuHRIl9LlOSGhPlisSnFLHbdprkB4VvYIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDCSP6Js%2FyjtyPIrRPCrcA%2BXb6g35IPJrwdY%2FlbvHMO%2Bt0GAktniNoaU9HVu6VuIr0lBDCNN7KUPnG4pzVCdnkhdnXjrM%2B4GmlcoSLh3w3oe2DE0Jzj2NzJRjABJnI%2FxiMUEVbvzNC2aGwWXJLf2zRASPhAGtHzGveMIdWed%2Fzq9zhwruO%2FN45TlFslzK3pp4iL1o7X7YIi5TJdZRkyvHpfxP%2FcHeZdMhFlK%2Fy0uN6FT5b5KiQ%2FFTQ83k%2BbeTZR%2BwGshE9zbGLh9diQlDMwlBeosPdBZdkUys7Zm8TlLdlgeFC5gtC4lrUh0ha%2Fivrvl95VP8vfCX%2FWJUC%2BV4r9KSBvDhO9VVJyeADbilcyTiVE4nYDY5sp%2Bqe1Vbja3E6fwgKNvmhvgK62XCWSsMFx5JiFjdUDmhxKU8aUPLIBpI83u%2BHeQZO1pGv6Y%2B%2BihUh3xfBt%2FBJ7jUEmpPpO%2F6CP%2BSULYwsc7A1dgdssQYqZRLfqi0z6yqshBskJDhfl5hvO6XvGnTJhZrG7hl4Qp5Gl9%2FIRv%2FnJYQxQor9EeqGQE%2FhHM1shJl3HYNQ8Nb65%2FLggUUqybr7uT9lGm1Bjf8qMCNcgrNeYVQb2KCKVrn2fZWEMTYgYlw%2BL7zUTFzkaavgaLK8JpgIyJovDOZagNdMNexy88GOqUBDkGcUAGLcTbs2nEmXMZBpYKsnZ5J0sVjv%2Fruzei8h%2Bk9RJqF3%2B8vQiEjiRvUFsC6aX4qsDESlPhqy1S5ZtigN4RW2CvEuaFZ%2Fiqv4L4rAOHqFeKIfoqMxDS9rT6Kkdezs9qkLeECAfDWcZzlwFnq7YisyOGMe3fn5sCdUO%2Bbh45DNWbtWHAIrj9SH64Nzq8alBihA9KxtPYac2ObKjGkeF1n%2BrxA&X-Amz-Signature=8ad3f34a447d7ad812930b78c8d61d52adf7f97cdf62e9c908c7eb4ae9672e85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DHS5SEX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIEpAPkfI0gU5Fo3y%2BtIBdeJtY5X3adQkVVEPBu51SJ86AiEA4av1%2BmzlEZUuHRIl9LlOSGhPlisSnFLHbdprkB4VvYIq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDCSP6Js%2FyjtyPIrRPCrcA%2BXb6g35IPJrwdY%2FlbvHMO%2Bt0GAktniNoaU9HVu6VuIr0lBDCNN7KUPnG4pzVCdnkhdnXjrM%2B4GmlcoSLh3w3oe2DE0Jzj2NzJRjABJnI%2FxiMUEVbvzNC2aGwWXJLf2zRASPhAGtHzGveMIdWed%2Fzq9zhwruO%2FN45TlFslzK3pp4iL1o7X7YIi5TJdZRkyvHpfxP%2FcHeZdMhFlK%2Fy0uN6FT5b5KiQ%2FFTQ83k%2BbeTZR%2BwGshE9zbGLh9diQlDMwlBeosPdBZdkUys7Zm8TlLdlgeFC5gtC4lrUh0ha%2Fivrvl95VP8vfCX%2FWJUC%2BV4r9KSBvDhO9VVJyeADbilcyTiVE4nYDY5sp%2Bqe1Vbja3E6fwgKNvmhvgK62XCWSsMFx5JiFjdUDmhxKU8aUPLIBpI83u%2BHeQZO1pGv6Y%2B%2BihUh3xfBt%2FBJ7jUEmpPpO%2F6CP%2BSULYwsc7A1dgdssQYqZRLfqi0z6yqshBskJDhfl5hvO6XvGnTJhZrG7hl4Qp5Gl9%2FIRv%2FnJYQxQor9EeqGQE%2FhHM1shJl3HYNQ8Nb65%2FLggUUqybr7uT9lGm1Bjf8qMCNcgrNeYVQb2KCKVrn2fZWEMTYgYlw%2BL7zUTFzkaavgaLK8JpgIyJovDOZagNdMNexy88GOqUBDkGcUAGLcTbs2nEmXMZBpYKsnZ5J0sVjv%2Fruzei8h%2Bk9RJqF3%2B8vQiEjiRvUFsC6aX4qsDESlPhqy1S5ZtigN4RW2CvEuaFZ%2Fiqv4L4rAOHqFeKIfoqMxDS9rT6Kkdezs9qkLeECAfDWcZzlwFnq7YisyOGMe3fn5sCdUO%2Bbh45DNWbtWHAIrj9SH64Nzq8alBihA9KxtPYac2ObKjGkeF1n%2BrxA&X-Amz-Signature=8080a66b9086317ee1932966b8b57e680d326fc6d3907147292604f6a735f936&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

