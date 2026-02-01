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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR3R7IUB%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9ordkaM%2Bm0llDDoWUhOEZHgradWz3tb0KO81A%2BZwfJAiAylQ7vr%2FbJFYUT8evuirhcb4cAIcArKWWZSayhzKm0iiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM242ITlVYONnNF5AfKtwDpvZaPTmNnRIWhhQ6S9myyd%2B%2Fev%2FviQbGfVk1aqTdAKiDOdArqcQxt8p4ZnzqxvoyavV1efWz8ueJzCKNIQ6KbwM6US6ar%2FQu%2B2X4vuvZ0pT6n6OGxFNaX3gKwZ%2FiCfKC%2BeJt%2FN9zKWhr91gS846yypZFMIljQ5MdOQ3S7M2Tfn3kB%2F0piZ07r%2BRElvw0RtCDkfYLzBZx1npSTT0INWXTmGxI9I8zOQFkGo1iXBC%2BPpkAfdVLM1zT4x7YyL2zc%2BKhIXW0sU3ZhbJ4D04dr6ajKKY4B7ABKdIaqU9RDN8sAYPKTeJmCm6E7xyE2G5aYUqpwUzfeSAhYj4c%2BIWdD80grKLXVToHDEXT3TVTsop2BVuBukdlFhzVfsFgAPdWEm%2BWWyUFx7x00fAQChWqcP1pRZcNELdstmWnicrEXUb6oM71YIMSllP4y%2BSSHFlq7VCSottNJG9XbXvaZOG2itYtltIXDdVMLINcDiYjziKW4htolJCk%2BuiGx6SWJbd%2BNr%2F64%2BxB8RGsOFQeTIgfLJ5dqJXLt3ULMx%2BMVIDCt0PV8%2FVXQR8TqJkQUY7KiYKlgBB%2FbE4OUuQEoLt2EoOfmhg6r8nR3%2BrzvnZ3VifEO6GlBPepISnvyGdd%2BZtbAmww6Jf7ywY6pgHH27WQUOLYGm8ifim18UYR7kmuouqAwvu9baJDjsCV4D%2F%2Ft010aHc6a1YOn8zCwuSs0fCuG6p0%2F4CPGz6Nk1EmpfZq2%2BSoWc2USTZ41AmSk%2FihVeaEaUQVdI2G0WGKIKS9Tf1pWgYcXRKJBSuMKu0AT%2B2PgKptLqVCT5HGRi2owYgeW4WziFg66DqH0LkFPow4x7T%2BxzxkBaWMh2nmdqn9Q86H5QV5&X-Amz-Signature=e2fb253675efaf6ea0a788dcc2891302a23a6448b7b783e7050763239e7f4da8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR3R7IUB%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9ordkaM%2Bm0llDDoWUhOEZHgradWz3tb0KO81A%2BZwfJAiAylQ7vr%2FbJFYUT8evuirhcb4cAIcArKWWZSayhzKm0iiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM242ITlVYONnNF5AfKtwDpvZaPTmNnRIWhhQ6S9myyd%2B%2Fev%2FviQbGfVk1aqTdAKiDOdArqcQxt8p4ZnzqxvoyavV1efWz8ueJzCKNIQ6KbwM6US6ar%2FQu%2B2X4vuvZ0pT6n6OGxFNaX3gKwZ%2FiCfKC%2BeJt%2FN9zKWhr91gS846yypZFMIljQ5MdOQ3S7M2Tfn3kB%2F0piZ07r%2BRElvw0RtCDkfYLzBZx1npSTT0INWXTmGxI9I8zOQFkGo1iXBC%2BPpkAfdVLM1zT4x7YyL2zc%2BKhIXW0sU3ZhbJ4D04dr6ajKKY4B7ABKdIaqU9RDN8sAYPKTeJmCm6E7xyE2G5aYUqpwUzfeSAhYj4c%2BIWdD80grKLXVToHDEXT3TVTsop2BVuBukdlFhzVfsFgAPdWEm%2BWWyUFx7x00fAQChWqcP1pRZcNELdstmWnicrEXUb6oM71YIMSllP4y%2BSSHFlq7VCSottNJG9XbXvaZOG2itYtltIXDdVMLINcDiYjziKW4htolJCk%2BuiGx6SWJbd%2BNr%2F64%2BxB8RGsOFQeTIgfLJ5dqJXLt3ULMx%2BMVIDCt0PV8%2FVXQR8TqJkQUY7KiYKlgBB%2FbE4OUuQEoLt2EoOfmhg6r8nR3%2BrzvnZ3VifEO6GlBPepISnvyGdd%2BZtbAmww6Jf7ywY6pgHH27WQUOLYGm8ifim18UYR7kmuouqAwvu9baJDjsCV4D%2F%2Ft010aHc6a1YOn8zCwuSs0fCuG6p0%2F4CPGz6Nk1EmpfZq2%2BSoWc2USTZ41AmSk%2FihVeaEaUQVdI2G0WGKIKS9Tf1pWgYcXRKJBSuMKu0AT%2B2PgKptLqVCT5HGRi2owYgeW4WziFg66DqH0LkFPow4x7T%2BxzxkBaWMh2nmdqn9Q86H5QV5&X-Amz-Signature=e8965b1c51c7a9f6f5870176e40846a944dfa2e88d03ff76f307ce69645fcb65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR3R7IUB%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9ordkaM%2Bm0llDDoWUhOEZHgradWz3tb0KO81A%2BZwfJAiAylQ7vr%2FbJFYUT8evuirhcb4cAIcArKWWZSayhzKm0iiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM242ITlVYONnNF5AfKtwDpvZaPTmNnRIWhhQ6S9myyd%2B%2Fev%2FviQbGfVk1aqTdAKiDOdArqcQxt8p4ZnzqxvoyavV1efWz8ueJzCKNIQ6KbwM6US6ar%2FQu%2B2X4vuvZ0pT6n6OGxFNaX3gKwZ%2FiCfKC%2BeJt%2FN9zKWhr91gS846yypZFMIljQ5MdOQ3S7M2Tfn3kB%2F0piZ07r%2BRElvw0RtCDkfYLzBZx1npSTT0INWXTmGxI9I8zOQFkGo1iXBC%2BPpkAfdVLM1zT4x7YyL2zc%2BKhIXW0sU3ZhbJ4D04dr6ajKKY4B7ABKdIaqU9RDN8sAYPKTeJmCm6E7xyE2G5aYUqpwUzfeSAhYj4c%2BIWdD80grKLXVToHDEXT3TVTsop2BVuBukdlFhzVfsFgAPdWEm%2BWWyUFx7x00fAQChWqcP1pRZcNELdstmWnicrEXUb6oM71YIMSllP4y%2BSSHFlq7VCSottNJG9XbXvaZOG2itYtltIXDdVMLINcDiYjziKW4htolJCk%2BuiGx6SWJbd%2BNr%2F64%2BxB8RGsOFQeTIgfLJ5dqJXLt3ULMx%2BMVIDCt0PV8%2FVXQR8TqJkQUY7KiYKlgBB%2FbE4OUuQEoLt2EoOfmhg6r8nR3%2BrzvnZ3VifEO6GlBPepISnvyGdd%2BZtbAmww6Jf7ywY6pgHH27WQUOLYGm8ifim18UYR7kmuouqAwvu9baJDjsCV4D%2F%2Ft010aHc6a1YOn8zCwuSs0fCuG6p0%2F4CPGz6Nk1EmpfZq2%2BSoWc2USTZ41AmSk%2FihVeaEaUQVdI2G0WGKIKS9Tf1pWgYcXRKJBSuMKu0AT%2B2PgKptLqVCT5HGRi2owYgeW4WziFg66DqH0LkFPow4x7T%2BxzxkBaWMh2nmdqn9Q86H5QV5&X-Amz-Signature=3176ac77544241d59e2369124a6bd757eb7b3aaad4070cbaba36f6e6210a5a99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR3R7IUB%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9ordkaM%2Bm0llDDoWUhOEZHgradWz3tb0KO81A%2BZwfJAiAylQ7vr%2FbJFYUT8evuirhcb4cAIcArKWWZSayhzKm0iiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM242ITlVYONnNF5AfKtwDpvZaPTmNnRIWhhQ6S9myyd%2B%2Fev%2FviQbGfVk1aqTdAKiDOdArqcQxt8p4ZnzqxvoyavV1efWz8ueJzCKNIQ6KbwM6US6ar%2FQu%2B2X4vuvZ0pT6n6OGxFNaX3gKwZ%2FiCfKC%2BeJt%2FN9zKWhr91gS846yypZFMIljQ5MdOQ3S7M2Tfn3kB%2F0piZ07r%2BRElvw0RtCDkfYLzBZx1npSTT0INWXTmGxI9I8zOQFkGo1iXBC%2BPpkAfdVLM1zT4x7YyL2zc%2BKhIXW0sU3ZhbJ4D04dr6ajKKY4B7ABKdIaqU9RDN8sAYPKTeJmCm6E7xyE2G5aYUqpwUzfeSAhYj4c%2BIWdD80grKLXVToHDEXT3TVTsop2BVuBukdlFhzVfsFgAPdWEm%2BWWyUFx7x00fAQChWqcP1pRZcNELdstmWnicrEXUb6oM71YIMSllP4y%2BSSHFlq7VCSottNJG9XbXvaZOG2itYtltIXDdVMLINcDiYjziKW4htolJCk%2BuiGx6SWJbd%2BNr%2F64%2BxB8RGsOFQeTIgfLJ5dqJXLt3ULMx%2BMVIDCt0PV8%2FVXQR8TqJkQUY7KiYKlgBB%2FbE4OUuQEoLt2EoOfmhg6r8nR3%2BrzvnZ3VifEO6GlBPepISnvyGdd%2BZtbAmww6Jf7ywY6pgHH27WQUOLYGm8ifim18UYR7kmuouqAwvu9baJDjsCV4D%2F%2Ft010aHc6a1YOn8zCwuSs0fCuG6p0%2F4CPGz6Nk1EmpfZq2%2BSoWc2USTZ41AmSk%2FihVeaEaUQVdI2G0WGKIKS9Tf1pWgYcXRKJBSuMKu0AT%2B2PgKptLqVCT5HGRi2owYgeW4WziFg66DqH0LkFPow4x7T%2BxzxkBaWMh2nmdqn9Q86H5QV5&X-Amz-Signature=1b3ac984bf05bc6c19a61b075bd81b7c8b58283d9a6ef1d19272e4d939f01236&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR3R7IUB%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9ordkaM%2Bm0llDDoWUhOEZHgradWz3tb0KO81A%2BZwfJAiAylQ7vr%2FbJFYUT8evuirhcb4cAIcArKWWZSayhzKm0iiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM242ITlVYONnNF5AfKtwDpvZaPTmNnRIWhhQ6S9myyd%2B%2Fev%2FviQbGfVk1aqTdAKiDOdArqcQxt8p4ZnzqxvoyavV1efWz8ueJzCKNIQ6KbwM6US6ar%2FQu%2B2X4vuvZ0pT6n6OGxFNaX3gKwZ%2FiCfKC%2BeJt%2FN9zKWhr91gS846yypZFMIljQ5MdOQ3S7M2Tfn3kB%2F0piZ07r%2BRElvw0RtCDkfYLzBZx1npSTT0INWXTmGxI9I8zOQFkGo1iXBC%2BPpkAfdVLM1zT4x7YyL2zc%2BKhIXW0sU3ZhbJ4D04dr6ajKKY4B7ABKdIaqU9RDN8sAYPKTeJmCm6E7xyE2G5aYUqpwUzfeSAhYj4c%2BIWdD80grKLXVToHDEXT3TVTsop2BVuBukdlFhzVfsFgAPdWEm%2BWWyUFx7x00fAQChWqcP1pRZcNELdstmWnicrEXUb6oM71YIMSllP4y%2BSSHFlq7VCSottNJG9XbXvaZOG2itYtltIXDdVMLINcDiYjziKW4htolJCk%2BuiGx6SWJbd%2BNr%2F64%2BxB8RGsOFQeTIgfLJ5dqJXLt3ULMx%2BMVIDCt0PV8%2FVXQR8TqJkQUY7KiYKlgBB%2FbE4OUuQEoLt2EoOfmhg6r8nR3%2BrzvnZ3VifEO6GlBPepISnvyGdd%2BZtbAmww6Jf7ywY6pgHH27WQUOLYGm8ifim18UYR7kmuouqAwvu9baJDjsCV4D%2F%2Ft010aHc6a1YOn8zCwuSs0fCuG6p0%2F4CPGz6Nk1EmpfZq2%2BSoWc2USTZ41AmSk%2FihVeaEaUQVdI2G0WGKIKS9Tf1pWgYcXRKJBSuMKu0AT%2B2PgKptLqVCT5HGRi2owYgeW4WziFg66DqH0LkFPow4x7T%2BxzxkBaWMh2nmdqn9Q86H5QV5&X-Amz-Signature=4ce58fac04af9e87c907fca272ba9981cc9226e0bb59880458ff2f39a1ae68e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR3R7IUB%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9ordkaM%2Bm0llDDoWUhOEZHgradWz3tb0KO81A%2BZwfJAiAylQ7vr%2FbJFYUT8evuirhcb4cAIcArKWWZSayhzKm0iiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM242ITlVYONnNF5AfKtwDpvZaPTmNnRIWhhQ6S9myyd%2B%2Fev%2FviQbGfVk1aqTdAKiDOdArqcQxt8p4ZnzqxvoyavV1efWz8ueJzCKNIQ6KbwM6US6ar%2FQu%2B2X4vuvZ0pT6n6OGxFNaX3gKwZ%2FiCfKC%2BeJt%2FN9zKWhr91gS846yypZFMIljQ5MdOQ3S7M2Tfn3kB%2F0piZ07r%2BRElvw0RtCDkfYLzBZx1npSTT0INWXTmGxI9I8zOQFkGo1iXBC%2BPpkAfdVLM1zT4x7YyL2zc%2BKhIXW0sU3ZhbJ4D04dr6ajKKY4B7ABKdIaqU9RDN8sAYPKTeJmCm6E7xyE2G5aYUqpwUzfeSAhYj4c%2BIWdD80grKLXVToHDEXT3TVTsop2BVuBukdlFhzVfsFgAPdWEm%2BWWyUFx7x00fAQChWqcP1pRZcNELdstmWnicrEXUb6oM71YIMSllP4y%2BSSHFlq7VCSottNJG9XbXvaZOG2itYtltIXDdVMLINcDiYjziKW4htolJCk%2BuiGx6SWJbd%2BNr%2F64%2BxB8RGsOFQeTIgfLJ5dqJXLt3ULMx%2BMVIDCt0PV8%2FVXQR8TqJkQUY7KiYKlgBB%2FbE4OUuQEoLt2EoOfmhg6r8nR3%2BrzvnZ3VifEO6GlBPepISnvyGdd%2BZtbAmww6Jf7ywY6pgHH27WQUOLYGm8ifim18UYR7kmuouqAwvu9baJDjsCV4D%2F%2Ft010aHc6a1YOn8zCwuSs0fCuG6p0%2F4CPGz6Nk1EmpfZq2%2BSoWc2USTZ41AmSk%2FihVeaEaUQVdI2G0WGKIKS9Tf1pWgYcXRKJBSuMKu0AT%2B2PgKptLqVCT5HGRi2owYgeW4WziFg66DqH0LkFPow4x7T%2BxzxkBaWMh2nmdqn9Q86H5QV5&X-Amz-Signature=c2875cc496ba71fc5e75c120bcf1267d3dbafd95069b6d9f2a0b3d7a5fe60f91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR3R7IUB%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9ordkaM%2Bm0llDDoWUhOEZHgradWz3tb0KO81A%2BZwfJAiAylQ7vr%2FbJFYUT8evuirhcb4cAIcArKWWZSayhzKm0iiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM242ITlVYONnNF5AfKtwDpvZaPTmNnRIWhhQ6S9myyd%2B%2Fev%2FviQbGfVk1aqTdAKiDOdArqcQxt8p4ZnzqxvoyavV1efWz8ueJzCKNIQ6KbwM6US6ar%2FQu%2B2X4vuvZ0pT6n6OGxFNaX3gKwZ%2FiCfKC%2BeJt%2FN9zKWhr91gS846yypZFMIljQ5MdOQ3S7M2Tfn3kB%2F0piZ07r%2BRElvw0RtCDkfYLzBZx1npSTT0INWXTmGxI9I8zOQFkGo1iXBC%2BPpkAfdVLM1zT4x7YyL2zc%2BKhIXW0sU3ZhbJ4D04dr6ajKKY4B7ABKdIaqU9RDN8sAYPKTeJmCm6E7xyE2G5aYUqpwUzfeSAhYj4c%2BIWdD80grKLXVToHDEXT3TVTsop2BVuBukdlFhzVfsFgAPdWEm%2BWWyUFx7x00fAQChWqcP1pRZcNELdstmWnicrEXUb6oM71YIMSllP4y%2BSSHFlq7VCSottNJG9XbXvaZOG2itYtltIXDdVMLINcDiYjziKW4htolJCk%2BuiGx6SWJbd%2BNr%2F64%2BxB8RGsOFQeTIgfLJ5dqJXLt3ULMx%2BMVIDCt0PV8%2FVXQR8TqJkQUY7KiYKlgBB%2FbE4OUuQEoLt2EoOfmhg6r8nR3%2BrzvnZ3VifEO6GlBPepISnvyGdd%2BZtbAmww6Jf7ywY6pgHH27WQUOLYGm8ifim18UYR7kmuouqAwvu9baJDjsCV4D%2F%2Ft010aHc6a1YOn8zCwuSs0fCuG6p0%2F4CPGz6Nk1EmpfZq2%2BSoWc2USTZ41AmSk%2FihVeaEaUQVdI2G0WGKIKS9Tf1pWgYcXRKJBSuMKu0AT%2B2PgKptLqVCT5HGRi2owYgeW4WziFg66DqH0LkFPow4x7T%2BxzxkBaWMh2nmdqn9Q86H5QV5&X-Amz-Signature=8c3373caedba958c225b8476de87115c34d57cd502757c2d13c7b17742a750a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR3R7IUB%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9ordkaM%2Bm0llDDoWUhOEZHgradWz3tb0KO81A%2BZwfJAiAylQ7vr%2FbJFYUT8evuirhcb4cAIcArKWWZSayhzKm0iiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM242ITlVYONnNF5AfKtwDpvZaPTmNnRIWhhQ6S9myyd%2B%2Fev%2FviQbGfVk1aqTdAKiDOdArqcQxt8p4ZnzqxvoyavV1efWz8ueJzCKNIQ6KbwM6US6ar%2FQu%2B2X4vuvZ0pT6n6OGxFNaX3gKwZ%2FiCfKC%2BeJt%2FN9zKWhr91gS846yypZFMIljQ5MdOQ3S7M2Tfn3kB%2F0piZ07r%2BRElvw0RtCDkfYLzBZx1npSTT0INWXTmGxI9I8zOQFkGo1iXBC%2BPpkAfdVLM1zT4x7YyL2zc%2BKhIXW0sU3ZhbJ4D04dr6ajKKY4B7ABKdIaqU9RDN8sAYPKTeJmCm6E7xyE2G5aYUqpwUzfeSAhYj4c%2BIWdD80grKLXVToHDEXT3TVTsop2BVuBukdlFhzVfsFgAPdWEm%2BWWyUFx7x00fAQChWqcP1pRZcNELdstmWnicrEXUb6oM71YIMSllP4y%2BSSHFlq7VCSottNJG9XbXvaZOG2itYtltIXDdVMLINcDiYjziKW4htolJCk%2BuiGx6SWJbd%2BNr%2F64%2BxB8RGsOFQeTIgfLJ5dqJXLt3ULMx%2BMVIDCt0PV8%2FVXQR8TqJkQUY7KiYKlgBB%2FbE4OUuQEoLt2EoOfmhg6r8nR3%2BrzvnZ3VifEO6GlBPepISnvyGdd%2BZtbAmww6Jf7ywY6pgHH27WQUOLYGm8ifim18UYR7kmuouqAwvu9baJDjsCV4D%2F%2Ft010aHc6a1YOn8zCwuSs0fCuG6p0%2F4CPGz6Nk1EmpfZq2%2BSoWc2USTZ41AmSk%2FihVeaEaUQVdI2G0WGKIKS9Tf1pWgYcXRKJBSuMKu0AT%2B2PgKptLqVCT5HGRi2owYgeW4WziFg66DqH0LkFPow4x7T%2BxzxkBaWMh2nmdqn9Q86H5QV5&X-Amz-Signature=a20f6173e4fc12b5563d114341f78f2303bde8eb43bc775d66325494307d0573&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR3R7IUB%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9ordkaM%2Bm0llDDoWUhOEZHgradWz3tb0KO81A%2BZwfJAiAylQ7vr%2FbJFYUT8evuirhcb4cAIcArKWWZSayhzKm0iiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM242ITlVYONnNF5AfKtwDpvZaPTmNnRIWhhQ6S9myyd%2B%2Fev%2FviQbGfVk1aqTdAKiDOdArqcQxt8p4ZnzqxvoyavV1efWz8ueJzCKNIQ6KbwM6US6ar%2FQu%2B2X4vuvZ0pT6n6OGxFNaX3gKwZ%2FiCfKC%2BeJt%2FN9zKWhr91gS846yypZFMIljQ5MdOQ3S7M2Tfn3kB%2F0piZ07r%2BRElvw0RtCDkfYLzBZx1npSTT0INWXTmGxI9I8zOQFkGo1iXBC%2BPpkAfdVLM1zT4x7YyL2zc%2BKhIXW0sU3ZhbJ4D04dr6ajKKY4B7ABKdIaqU9RDN8sAYPKTeJmCm6E7xyE2G5aYUqpwUzfeSAhYj4c%2BIWdD80grKLXVToHDEXT3TVTsop2BVuBukdlFhzVfsFgAPdWEm%2BWWyUFx7x00fAQChWqcP1pRZcNELdstmWnicrEXUb6oM71YIMSllP4y%2BSSHFlq7VCSottNJG9XbXvaZOG2itYtltIXDdVMLINcDiYjziKW4htolJCk%2BuiGx6SWJbd%2BNr%2F64%2BxB8RGsOFQeTIgfLJ5dqJXLt3ULMx%2BMVIDCt0PV8%2FVXQR8TqJkQUY7KiYKlgBB%2FbE4OUuQEoLt2EoOfmhg6r8nR3%2BrzvnZ3VifEO6GlBPepISnvyGdd%2BZtbAmww6Jf7ywY6pgHH27WQUOLYGm8ifim18UYR7kmuouqAwvu9baJDjsCV4D%2F%2Ft010aHc6a1YOn8zCwuSs0fCuG6p0%2F4CPGz6Nk1EmpfZq2%2BSoWc2USTZ41AmSk%2FihVeaEaUQVdI2G0WGKIKS9Tf1pWgYcXRKJBSuMKu0AT%2B2PgKptLqVCT5HGRi2owYgeW4WziFg66DqH0LkFPow4x7T%2BxzxkBaWMh2nmdqn9Q86H5QV5&X-Amz-Signature=e52af4d48649c00387d1ebe809e6f4ed51649d0784201cca0577b84839355c6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR3R7IUB%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9ordkaM%2Bm0llDDoWUhOEZHgradWz3tb0KO81A%2BZwfJAiAylQ7vr%2FbJFYUT8evuirhcb4cAIcArKWWZSayhzKm0iiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM242ITlVYONnNF5AfKtwDpvZaPTmNnRIWhhQ6S9myyd%2B%2Fev%2FviQbGfVk1aqTdAKiDOdArqcQxt8p4ZnzqxvoyavV1efWz8ueJzCKNIQ6KbwM6US6ar%2FQu%2B2X4vuvZ0pT6n6OGxFNaX3gKwZ%2FiCfKC%2BeJt%2FN9zKWhr91gS846yypZFMIljQ5MdOQ3S7M2Tfn3kB%2F0piZ07r%2BRElvw0RtCDkfYLzBZx1npSTT0INWXTmGxI9I8zOQFkGo1iXBC%2BPpkAfdVLM1zT4x7YyL2zc%2BKhIXW0sU3ZhbJ4D04dr6ajKKY4B7ABKdIaqU9RDN8sAYPKTeJmCm6E7xyE2G5aYUqpwUzfeSAhYj4c%2BIWdD80grKLXVToHDEXT3TVTsop2BVuBukdlFhzVfsFgAPdWEm%2BWWyUFx7x00fAQChWqcP1pRZcNELdstmWnicrEXUb6oM71YIMSllP4y%2BSSHFlq7VCSottNJG9XbXvaZOG2itYtltIXDdVMLINcDiYjziKW4htolJCk%2BuiGx6SWJbd%2BNr%2F64%2BxB8RGsOFQeTIgfLJ5dqJXLt3ULMx%2BMVIDCt0PV8%2FVXQR8TqJkQUY7KiYKlgBB%2FbE4OUuQEoLt2EoOfmhg6r8nR3%2BrzvnZ3VifEO6GlBPepISnvyGdd%2BZtbAmww6Jf7ywY6pgHH27WQUOLYGm8ifim18UYR7kmuouqAwvu9baJDjsCV4D%2F%2Ft010aHc6a1YOn8zCwuSs0fCuG6p0%2F4CPGz6Nk1EmpfZq2%2BSoWc2USTZ41AmSk%2FihVeaEaUQVdI2G0WGKIKS9Tf1pWgYcXRKJBSuMKu0AT%2B2PgKptLqVCT5HGRi2owYgeW4WziFg66DqH0LkFPow4x7T%2BxzxkBaWMh2nmdqn9Q86H5QV5&X-Amz-Signature=bb781f76221baa0151d0e8df888ff36f51b22aaedf9b4fb0f0f2d8f4103e0f68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

