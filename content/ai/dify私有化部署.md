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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642M4WTHD%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGdKvjdxpH1mUdoEbF8julvgY9FShJU6tFYJFKODZgF%2BAiEA6y7SGLB3Yow8xcIhKNQbiRUBj0yazZkMx2HYCCHsFT0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbI0nvLT5XjAHriPCrcA1%2Fw%2BVNE2UYkVMYgmreWgHNdW1kOzgpa3F0bILA%2Bk0tviDL2zbpmdgsGtRFEhYYYO6CME9z33G7vS8u1BVk7cO%2Fl4CoEJpQRQmVcfzrtvOBCivC59T2WuRBLIxE%2FylgJAcahzSQpHhPzzsNtvw1Et6sx8g5NoxOfhkAJ%2F3jowt5d5Nbvt9xokHIgWBpqJ%2Bw1rGcAeLrX8Rct2yC18ecfM06QDIjUFtpW4i9b9d7bfZDJlfsco5VvNlj%2F1iXeJhlSivBNvrCx15NRepe8MDu3oWq1g2713W5FonuZlNcS9QCnak2gPTNFxSUhMdmC0QisotcMWtiNl%2Bt%2B3gYMBs6NropdP2PNorRAH02shHe8NJPzY95Bun744ET9o0z4A%2BRgMo0oei%2FD5wRJYippFJeAEDsx2dYnn7OFcnoQ9e98Jwbiy8gDesF0cHS0zwzv5%2BSOkb9LV6Vn6oz1MjdAJOiEpOGjHlkDhEla95K34XX%2FnZAkIZ%2BE%2BMY6BYuffgZTGorTDlHTlkfJgL2AnPCHM%2BvI2akZV9QaDRwLNV8XLHbkOt2Xz5NutcFPk2QiqN%2BhcFit56fHrCtAXNPzeZLWmuOes%2BdINaTrOgO4QHkXrxgpz76sfzatdKf4gQbQnxQiMOaui88GOqUBjsaBm2OHZP6p%2FIUEPEiuCfgQhQ%2FcQy%2BNhKtLHFzovHBZBU5Xxa%2BT2%2B0AnYSMHoTQhISNY%2FhJPXd1xYMXbvALB2axX2lO%2F4R5OIp%2BxH325WjhsTOF3SFz%2Fz6uJ0NsQzgSCDVEk8xIUFLfVLvQVyGCJwZyhrprDLNyEVIcT3KALwYkRQ23nQ3W5VxenMAHS97KxG3KO5itvNcJNeD1fiYiLkCjBhXZ&X-Amz-Signature=ce285e0f96924c43b3f6acfb5dad0d72af091f3a567a3ee9252d8f23a3b91874&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642M4WTHD%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGdKvjdxpH1mUdoEbF8julvgY9FShJU6tFYJFKODZgF%2BAiEA6y7SGLB3Yow8xcIhKNQbiRUBj0yazZkMx2HYCCHsFT0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbI0nvLT5XjAHriPCrcA1%2Fw%2BVNE2UYkVMYgmreWgHNdW1kOzgpa3F0bILA%2Bk0tviDL2zbpmdgsGtRFEhYYYO6CME9z33G7vS8u1BVk7cO%2Fl4CoEJpQRQmVcfzrtvOBCivC59T2WuRBLIxE%2FylgJAcahzSQpHhPzzsNtvw1Et6sx8g5NoxOfhkAJ%2F3jowt5d5Nbvt9xokHIgWBpqJ%2Bw1rGcAeLrX8Rct2yC18ecfM06QDIjUFtpW4i9b9d7bfZDJlfsco5VvNlj%2F1iXeJhlSivBNvrCx15NRepe8MDu3oWq1g2713W5FonuZlNcS9QCnak2gPTNFxSUhMdmC0QisotcMWtiNl%2Bt%2B3gYMBs6NropdP2PNorRAH02shHe8NJPzY95Bun744ET9o0z4A%2BRgMo0oei%2FD5wRJYippFJeAEDsx2dYnn7OFcnoQ9e98Jwbiy8gDesF0cHS0zwzv5%2BSOkb9LV6Vn6oz1MjdAJOiEpOGjHlkDhEla95K34XX%2FnZAkIZ%2BE%2BMY6BYuffgZTGorTDlHTlkfJgL2AnPCHM%2BvI2akZV9QaDRwLNV8XLHbkOt2Xz5NutcFPk2QiqN%2BhcFit56fHrCtAXNPzeZLWmuOes%2BdINaTrOgO4QHkXrxgpz76sfzatdKf4gQbQnxQiMOaui88GOqUBjsaBm2OHZP6p%2FIUEPEiuCfgQhQ%2FcQy%2BNhKtLHFzovHBZBU5Xxa%2BT2%2B0AnYSMHoTQhISNY%2FhJPXd1xYMXbvALB2axX2lO%2F4R5OIp%2BxH325WjhsTOF3SFz%2Fz6uJ0NsQzgSCDVEk8xIUFLfVLvQVyGCJwZyhrprDLNyEVIcT3KALwYkRQ23nQ3W5VxenMAHS97KxG3KO5itvNcJNeD1fiYiLkCjBhXZ&X-Amz-Signature=49621a3fc4c29954c8419ca98f96bdccfa72554653b40be95a736678aa814418&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642M4WTHD%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGdKvjdxpH1mUdoEbF8julvgY9FShJU6tFYJFKODZgF%2BAiEA6y7SGLB3Yow8xcIhKNQbiRUBj0yazZkMx2HYCCHsFT0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbI0nvLT5XjAHriPCrcA1%2Fw%2BVNE2UYkVMYgmreWgHNdW1kOzgpa3F0bILA%2Bk0tviDL2zbpmdgsGtRFEhYYYO6CME9z33G7vS8u1BVk7cO%2Fl4CoEJpQRQmVcfzrtvOBCivC59T2WuRBLIxE%2FylgJAcahzSQpHhPzzsNtvw1Et6sx8g5NoxOfhkAJ%2F3jowt5d5Nbvt9xokHIgWBpqJ%2Bw1rGcAeLrX8Rct2yC18ecfM06QDIjUFtpW4i9b9d7bfZDJlfsco5VvNlj%2F1iXeJhlSivBNvrCx15NRepe8MDu3oWq1g2713W5FonuZlNcS9QCnak2gPTNFxSUhMdmC0QisotcMWtiNl%2Bt%2B3gYMBs6NropdP2PNorRAH02shHe8NJPzY95Bun744ET9o0z4A%2BRgMo0oei%2FD5wRJYippFJeAEDsx2dYnn7OFcnoQ9e98Jwbiy8gDesF0cHS0zwzv5%2BSOkb9LV6Vn6oz1MjdAJOiEpOGjHlkDhEla95K34XX%2FnZAkIZ%2BE%2BMY6BYuffgZTGorTDlHTlkfJgL2AnPCHM%2BvI2akZV9QaDRwLNV8XLHbkOt2Xz5NutcFPk2QiqN%2BhcFit56fHrCtAXNPzeZLWmuOes%2BdINaTrOgO4QHkXrxgpz76sfzatdKf4gQbQnxQiMOaui88GOqUBjsaBm2OHZP6p%2FIUEPEiuCfgQhQ%2FcQy%2BNhKtLHFzovHBZBU5Xxa%2BT2%2B0AnYSMHoTQhISNY%2FhJPXd1xYMXbvALB2axX2lO%2F4R5OIp%2BxH325WjhsTOF3SFz%2Fz6uJ0NsQzgSCDVEk8xIUFLfVLvQVyGCJwZyhrprDLNyEVIcT3KALwYkRQ23nQ3W5VxenMAHS97KxG3KO5itvNcJNeD1fiYiLkCjBhXZ&X-Amz-Signature=84a121ab69cf9dc2b6d17843e4d515582b659eb381f7db319092e56e27002496&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642M4WTHD%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGdKvjdxpH1mUdoEbF8julvgY9FShJU6tFYJFKODZgF%2BAiEA6y7SGLB3Yow8xcIhKNQbiRUBj0yazZkMx2HYCCHsFT0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbI0nvLT5XjAHriPCrcA1%2Fw%2BVNE2UYkVMYgmreWgHNdW1kOzgpa3F0bILA%2Bk0tviDL2zbpmdgsGtRFEhYYYO6CME9z33G7vS8u1BVk7cO%2Fl4CoEJpQRQmVcfzrtvOBCivC59T2WuRBLIxE%2FylgJAcahzSQpHhPzzsNtvw1Et6sx8g5NoxOfhkAJ%2F3jowt5d5Nbvt9xokHIgWBpqJ%2Bw1rGcAeLrX8Rct2yC18ecfM06QDIjUFtpW4i9b9d7bfZDJlfsco5VvNlj%2F1iXeJhlSivBNvrCx15NRepe8MDu3oWq1g2713W5FonuZlNcS9QCnak2gPTNFxSUhMdmC0QisotcMWtiNl%2Bt%2B3gYMBs6NropdP2PNorRAH02shHe8NJPzY95Bun744ET9o0z4A%2BRgMo0oei%2FD5wRJYippFJeAEDsx2dYnn7OFcnoQ9e98Jwbiy8gDesF0cHS0zwzv5%2BSOkb9LV6Vn6oz1MjdAJOiEpOGjHlkDhEla95K34XX%2FnZAkIZ%2BE%2BMY6BYuffgZTGorTDlHTlkfJgL2AnPCHM%2BvI2akZV9QaDRwLNV8XLHbkOt2Xz5NutcFPk2QiqN%2BhcFit56fHrCtAXNPzeZLWmuOes%2BdINaTrOgO4QHkXrxgpz76sfzatdKf4gQbQnxQiMOaui88GOqUBjsaBm2OHZP6p%2FIUEPEiuCfgQhQ%2FcQy%2BNhKtLHFzovHBZBU5Xxa%2BT2%2B0AnYSMHoTQhISNY%2FhJPXd1xYMXbvALB2axX2lO%2F4R5OIp%2BxH325WjhsTOF3SFz%2Fz6uJ0NsQzgSCDVEk8xIUFLfVLvQVyGCJwZyhrprDLNyEVIcT3KALwYkRQ23nQ3W5VxenMAHS97KxG3KO5itvNcJNeD1fiYiLkCjBhXZ&X-Amz-Signature=51c9c8e7c7d0e002426cf1cb00188ece15ea4cf3930684e5bd5ef790b0dcbb70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642M4WTHD%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGdKvjdxpH1mUdoEbF8julvgY9FShJU6tFYJFKODZgF%2BAiEA6y7SGLB3Yow8xcIhKNQbiRUBj0yazZkMx2HYCCHsFT0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbI0nvLT5XjAHriPCrcA1%2Fw%2BVNE2UYkVMYgmreWgHNdW1kOzgpa3F0bILA%2Bk0tviDL2zbpmdgsGtRFEhYYYO6CME9z33G7vS8u1BVk7cO%2Fl4CoEJpQRQmVcfzrtvOBCivC59T2WuRBLIxE%2FylgJAcahzSQpHhPzzsNtvw1Et6sx8g5NoxOfhkAJ%2F3jowt5d5Nbvt9xokHIgWBpqJ%2Bw1rGcAeLrX8Rct2yC18ecfM06QDIjUFtpW4i9b9d7bfZDJlfsco5VvNlj%2F1iXeJhlSivBNvrCx15NRepe8MDu3oWq1g2713W5FonuZlNcS9QCnak2gPTNFxSUhMdmC0QisotcMWtiNl%2Bt%2B3gYMBs6NropdP2PNorRAH02shHe8NJPzY95Bun744ET9o0z4A%2BRgMo0oei%2FD5wRJYippFJeAEDsx2dYnn7OFcnoQ9e98Jwbiy8gDesF0cHS0zwzv5%2BSOkb9LV6Vn6oz1MjdAJOiEpOGjHlkDhEla95K34XX%2FnZAkIZ%2BE%2BMY6BYuffgZTGorTDlHTlkfJgL2AnPCHM%2BvI2akZV9QaDRwLNV8XLHbkOt2Xz5NutcFPk2QiqN%2BhcFit56fHrCtAXNPzeZLWmuOes%2BdINaTrOgO4QHkXrxgpz76sfzatdKf4gQbQnxQiMOaui88GOqUBjsaBm2OHZP6p%2FIUEPEiuCfgQhQ%2FcQy%2BNhKtLHFzovHBZBU5Xxa%2BT2%2B0AnYSMHoTQhISNY%2FhJPXd1xYMXbvALB2axX2lO%2F4R5OIp%2BxH325WjhsTOF3SFz%2Fz6uJ0NsQzgSCDVEk8xIUFLfVLvQVyGCJwZyhrprDLNyEVIcT3KALwYkRQ23nQ3W5VxenMAHS97KxG3KO5itvNcJNeD1fiYiLkCjBhXZ&X-Amz-Signature=10267b87b6325caeefc86af0b949fc693dbd67e6dc6324d2cdd0e5059533d3de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642M4WTHD%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGdKvjdxpH1mUdoEbF8julvgY9FShJU6tFYJFKODZgF%2BAiEA6y7SGLB3Yow8xcIhKNQbiRUBj0yazZkMx2HYCCHsFT0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbI0nvLT5XjAHriPCrcA1%2Fw%2BVNE2UYkVMYgmreWgHNdW1kOzgpa3F0bILA%2Bk0tviDL2zbpmdgsGtRFEhYYYO6CME9z33G7vS8u1BVk7cO%2Fl4CoEJpQRQmVcfzrtvOBCivC59T2WuRBLIxE%2FylgJAcahzSQpHhPzzsNtvw1Et6sx8g5NoxOfhkAJ%2F3jowt5d5Nbvt9xokHIgWBpqJ%2Bw1rGcAeLrX8Rct2yC18ecfM06QDIjUFtpW4i9b9d7bfZDJlfsco5VvNlj%2F1iXeJhlSivBNvrCx15NRepe8MDu3oWq1g2713W5FonuZlNcS9QCnak2gPTNFxSUhMdmC0QisotcMWtiNl%2Bt%2B3gYMBs6NropdP2PNorRAH02shHe8NJPzY95Bun744ET9o0z4A%2BRgMo0oei%2FD5wRJYippFJeAEDsx2dYnn7OFcnoQ9e98Jwbiy8gDesF0cHS0zwzv5%2BSOkb9LV6Vn6oz1MjdAJOiEpOGjHlkDhEla95K34XX%2FnZAkIZ%2BE%2BMY6BYuffgZTGorTDlHTlkfJgL2AnPCHM%2BvI2akZV9QaDRwLNV8XLHbkOt2Xz5NutcFPk2QiqN%2BhcFit56fHrCtAXNPzeZLWmuOes%2BdINaTrOgO4QHkXrxgpz76sfzatdKf4gQbQnxQiMOaui88GOqUBjsaBm2OHZP6p%2FIUEPEiuCfgQhQ%2FcQy%2BNhKtLHFzovHBZBU5Xxa%2BT2%2B0AnYSMHoTQhISNY%2FhJPXd1xYMXbvALB2axX2lO%2F4R5OIp%2BxH325WjhsTOF3SFz%2Fz6uJ0NsQzgSCDVEk8xIUFLfVLvQVyGCJwZyhrprDLNyEVIcT3KALwYkRQ23nQ3W5VxenMAHS97KxG3KO5itvNcJNeD1fiYiLkCjBhXZ&X-Amz-Signature=c3d5d1dfddd5d189a96c6e59dad3a9549727fbcf047a6a75996dfa8394733210&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642M4WTHD%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGdKvjdxpH1mUdoEbF8julvgY9FShJU6tFYJFKODZgF%2BAiEA6y7SGLB3Yow8xcIhKNQbiRUBj0yazZkMx2HYCCHsFT0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbI0nvLT5XjAHriPCrcA1%2Fw%2BVNE2UYkVMYgmreWgHNdW1kOzgpa3F0bILA%2Bk0tviDL2zbpmdgsGtRFEhYYYO6CME9z33G7vS8u1BVk7cO%2Fl4CoEJpQRQmVcfzrtvOBCivC59T2WuRBLIxE%2FylgJAcahzSQpHhPzzsNtvw1Et6sx8g5NoxOfhkAJ%2F3jowt5d5Nbvt9xokHIgWBpqJ%2Bw1rGcAeLrX8Rct2yC18ecfM06QDIjUFtpW4i9b9d7bfZDJlfsco5VvNlj%2F1iXeJhlSivBNvrCx15NRepe8MDu3oWq1g2713W5FonuZlNcS9QCnak2gPTNFxSUhMdmC0QisotcMWtiNl%2Bt%2B3gYMBs6NropdP2PNorRAH02shHe8NJPzY95Bun744ET9o0z4A%2BRgMo0oei%2FD5wRJYippFJeAEDsx2dYnn7OFcnoQ9e98Jwbiy8gDesF0cHS0zwzv5%2BSOkb9LV6Vn6oz1MjdAJOiEpOGjHlkDhEla95K34XX%2FnZAkIZ%2BE%2BMY6BYuffgZTGorTDlHTlkfJgL2AnPCHM%2BvI2akZV9QaDRwLNV8XLHbkOt2Xz5NutcFPk2QiqN%2BhcFit56fHrCtAXNPzeZLWmuOes%2BdINaTrOgO4QHkXrxgpz76sfzatdKf4gQbQnxQiMOaui88GOqUBjsaBm2OHZP6p%2FIUEPEiuCfgQhQ%2FcQy%2BNhKtLHFzovHBZBU5Xxa%2BT2%2B0AnYSMHoTQhISNY%2FhJPXd1xYMXbvALB2axX2lO%2F4R5OIp%2BxH325WjhsTOF3SFz%2Fz6uJ0NsQzgSCDVEk8xIUFLfVLvQVyGCJwZyhrprDLNyEVIcT3KALwYkRQ23nQ3W5VxenMAHS97KxG3KO5itvNcJNeD1fiYiLkCjBhXZ&X-Amz-Signature=81703ed11be67d690774356567506ff5f0d2e8e5307e4abec930666edd07888c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642M4WTHD%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGdKvjdxpH1mUdoEbF8julvgY9FShJU6tFYJFKODZgF%2BAiEA6y7SGLB3Yow8xcIhKNQbiRUBj0yazZkMx2HYCCHsFT0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbI0nvLT5XjAHriPCrcA1%2Fw%2BVNE2UYkVMYgmreWgHNdW1kOzgpa3F0bILA%2Bk0tviDL2zbpmdgsGtRFEhYYYO6CME9z33G7vS8u1BVk7cO%2Fl4CoEJpQRQmVcfzrtvOBCivC59T2WuRBLIxE%2FylgJAcahzSQpHhPzzsNtvw1Et6sx8g5NoxOfhkAJ%2F3jowt5d5Nbvt9xokHIgWBpqJ%2Bw1rGcAeLrX8Rct2yC18ecfM06QDIjUFtpW4i9b9d7bfZDJlfsco5VvNlj%2F1iXeJhlSivBNvrCx15NRepe8MDu3oWq1g2713W5FonuZlNcS9QCnak2gPTNFxSUhMdmC0QisotcMWtiNl%2Bt%2B3gYMBs6NropdP2PNorRAH02shHe8NJPzY95Bun744ET9o0z4A%2BRgMo0oei%2FD5wRJYippFJeAEDsx2dYnn7OFcnoQ9e98Jwbiy8gDesF0cHS0zwzv5%2BSOkb9LV6Vn6oz1MjdAJOiEpOGjHlkDhEla95K34XX%2FnZAkIZ%2BE%2BMY6BYuffgZTGorTDlHTlkfJgL2AnPCHM%2BvI2akZV9QaDRwLNV8XLHbkOt2Xz5NutcFPk2QiqN%2BhcFit56fHrCtAXNPzeZLWmuOes%2BdINaTrOgO4QHkXrxgpz76sfzatdKf4gQbQnxQiMOaui88GOqUBjsaBm2OHZP6p%2FIUEPEiuCfgQhQ%2FcQy%2BNhKtLHFzovHBZBU5Xxa%2BT2%2B0AnYSMHoTQhISNY%2FhJPXd1xYMXbvALB2axX2lO%2F4R5OIp%2BxH325WjhsTOF3SFz%2Fz6uJ0NsQzgSCDVEk8xIUFLfVLvQVyGCJwZyhrprDLNyEVIcT3KALwYkRQ23nQ3W5VxenMAHS97KxG3KO5itvNcJNeD1fiYiLkCjBhXZ&X-Amz-Signature=767eeaf6412bbb2b685e680500ed7f471bde0e88a3a70b5968adfca267bd3090&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642M4WTHD%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGdKvjdxpH1mUdoEbF8julvgY9FShJU6tFYJFKODZgF%2BAiEA6y7SGLB3Yow8xcIhKNQbiRUBj0yazZkMx2HYCCHsFT0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbI0nvLT5XjAHriPCrcA1%2Fw%2BVNE2UYkVMYgmreWgHNdW1kOzgpa3F0bILA%2Bk0tviDL2zbpmdgsGtRFEhYYYO6CME9z33G7vS8u1BVk7cO%2Fl4CoEJpQRQmVcfzrtvOBCivC59T2WuRBLIxE%2FylgJAcahzSQpHhPzzsNtvw1Et6sx8g5NoxOfhkAJ%2F3jowt5d5Nbvt9xokHIgWBpqJ%2Bw1rGcAeLrX8Rct2yC18ecfM06QDIjUFtpW4i9b9d7bfZDJlfsco5VvNlj%2F1iXeJhlSivBNvrCx15NRepe8MDu3oWq1g2713W5FonuZlNcS9QCnak2gPTNFxSUhMdmC0QisotcMWtiNl%2Bt%2B3gYMBs6NropdP2PNorRAH02shHe8NJPzY95Bun744ET9o0z4A%2BRgMo0oei%2FD5wRJYippFJeAEDsx2dYnn7OFcnoQ9e98Jwbiy8gDesF0cHS0zwzv5%2BSOkb9LV6Vn6oz1MjdAJOiEpOGjHlkDhEla95K34XX%2FnZAkIZ%2BE%2BMY6BYuffgZTGorTDlHTlkfJgL2AnPCHM%2BvI2akZV9QaDRwLNV8XLHbkOt2Xz5NutcFPk2QiqN%2BhcFit56fHrCtAXNPzeZLWmuOes%2BdINaTrOgO4QHkXrxgpz76sfzatdKf4gQbQnxQiMOaui88GOqUBjsaBm2OHZP6p%2FIUEPEiuCfgQhQ%2FcQy%2BNhKtLHFzovHBZBU5Xxa%2BT2%2B0AnYSMHoTQhISNY%2FhJPXd1xYMXbvALB2axX2lO%2F4R5OIp%2BxH325WjhsTOF3SFz%2Fz6uJ0NsQzgSCDVEk8xIUFLfVLvQVyGCJwZyhrprDLNyEVIcT3KALwYkRQ23nQ3W5VxenMAHS97KxG3KO5itvNcJNeD1fiYiLkCjBhXZ&X-Amz-Signature=92a4c8a4342e587e595f0480de0c4c1ce487766c1bf25ebd4c0cf4345e9d2901&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642M4WTHD%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIGdKvjdxpH1mUdoEbF8julvgY9FShJU6tFYJFKODZgF%2BAiEA6y7SGLB3Yow8xcIhKNQbiRUBj0yazZkMx2HYCCHsFT0qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMbI0nvLT5XjAHriPCrcA1%2Fw%2BVNE2UYkVMYgmreWgHNdW1kOzgpa3F0bILA%2Bk0tviDL2zbpmdgsGtRFEhYYYO6CME9z33G7vS8u1BVk7cO%2Fl4CoEJpQRQmVcfzrtvOBCivC59T2WuRBLIxE%2FylgJAcahzSQpHhPzzsNtvw1Et6sx8g5NoxOfhkAJ%2F3jowt5d5Nbvt9xokHIgWBpqJ%2Bw1rGcAeLrX8Rct2yC18ecfM06QDIjUFtpW4i9b9d7bfZDJlfsco5VvNlj%2F1iXeJhlSivBNvrCx15NRepe8MDu3oWq1g2713W5FonuZlNcS9QCnak2gPTNFxSUhMdmC0QisotcMWtiNl%2Bt%2B3gYMBs6NropdP2PNorRAH02shHe8NJPzY95Bun744ET9o0z4A%2BRgMo0oei%2FD5wRJYippFJeAEDsx2dYnn7OFcnoQ9e98Jwbiy8gDesF0cHS0zwzv5%2BSOkb9LV6Vn6oz1MjdAJOiEpOGjHlkDhEla95K34XX%2FnZAkIZ%2BE%2BMY6BYuffgZTGorTDlHTlkfJgL2AnPCHM%2BvI2akZV9QaDRwLNV8XLHbkOt2Xz5NutcFPk2QiqN%2BhcFit56fHrCtAXNPzeZLWmuOes%2BdINaTrOgO4QHkXrxgpz76sfzatdKf4gQbQnxQiMOaui88GOqUBjsaBm2OHZP6p%2FIUEPEiuCfgQhQ%2FcQy%2BNhKtLHFzovHBZBU5Xxa%2BT2%2B0AnYSMHoTQhISNY%2FhJPXd1xYMXbvALB2axX2lO%2F4R5OIp%2BxH325WjhsTOF3SFz%2Fz6uJ0NsQzgSCDVEk8xIUFLfVLvQVyGCJwZyhrprDLNyEVIcT3KALwYkRQ23nQ3W5VxenMAHS97KxG3KO5itvNcJNeD1fiYiLkCjBhXZ&X-Amz-Signature=19889cec377ebed6df13bd3632463be30036b20aa4b2dea1987ac5f76ccb8df8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

