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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCYUEA3J%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS5oq%2BPUvOSxv5u1RP3tL6tFl2EnCAW%2BN3CHWyaC3obAIhAMZxfavvKx7Hp5s6HZDra3n4tGD7V3XrW%2B9JSiDPhjt4KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxprSbEgksFNqDVM6wq3APriIDo72Au64EhHXeYEselngA0JSHvOFQ0Tc%2B4JPXiXNX5BRuNNhgDNoVOeDy4VOzAzFDBWobt4Wiwnj%2FqNT9lYP%2B9cePRx53FM%2FlLzabsh7fH89QBYqj5CMV9FDLQa4cSVIwmeQOLbvCQ2rv3PLOFRmJP3DZtgzZNbkTsy%2BSntxWJooFdPt%2FKBqaO1x3Q1nmD436CA6de2hv1BJhO5IYQIRtpp%2FrGxvEG%2FTaxGINqM6jLwU%2BsA1WJl2nFqDKcTngrGaMS9yOQA7MXVhbztKXToG1uNoG0cLkdal20onCeK7dBgObZvM7ZrZ4uzGcqu9PV7UbCJngkvByqS6B4RN6ahOPD4a1BkmNXZa2MvhvpUfUo5GpgLkbt6Pv1ewK7RQtOi46KsVDrXAQ2LDHckP1OBww%2BjoDJ99ruOQdavLRI7M7WGlHQGH0g8D7h61VEZsyMJGeSdmFx7MbSFtkwUbq1kkmjSf%2BgHP9k%2FwZ91kgLSPtNvd575udbpkm0fvUxpcLW70U6Vf8E%2FNMvvCe78tpC3%2Bl46Sl4EcME77bPIeUpjgUNDUEY8CZS7ItG8Q6a1DnaiIvIRIVk%2FQ9y5zktHyGI04sq5BOMDbB7dLRXIpC%2BysbDdew4Zom7%2BQR8PjDglfzOBjqkAUmk7M7a2IzcILgcVDCKkaDh%2BRP4rKtUM0gnp%2BSPnTWLSqok4t7%2FBF1kEYNWimWekATJxFQ3%2FH%2Bt4aIdi5bo8HnqXxHQXOxwiX6wM2IBbmWmGjh2uvwtCMn8j7oPHFsP%2F9bfmXNVQipRXmkreABnod%2F3oYBXo%2B2UuoN4lgdy94rWImNuWgxVYNNzuAMtDXMF7jvhXAy%2B7sM0sDkcQhJDX%2Btk08jm&X-Amz-Signature=f6e1c1aa9618f811e56e109c8077347dcc74cbf758a167272d5fb5b90cebb25e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCYUEA3J%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS5oq%2BPUvOSxv5u1RP3tL6tFl2EnCAW%2BN3CHWyaC3obAIhAMZxfavvKx7Hp5s6HZDra3n4tGD7V3XrW%2B9JSiDPhjt4KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxprSbEgksFNqDVM6wq3APriIDo72Au64EhHXeYEselngA0JSHvOFQ0Tc%2B4JPXiXNX5BRuNNhgDNoVOeDy4VOzAzFDBWobt4Wiwnj%2FqNT9lYP%2B9cePRx53FM%2FlLzabsh7fH89QBYqj5CMV9FDLQa4cSVIwmeQOLbvCQ2rv3PLOFRmJP3DZtgzZNbkTsy%2BSntxWJooFdPt%2FKBqaO1x3Q1nmD436CA6de2hv1BJhO5IYQIRtpp%2FrGxvEG%2FTaxGINqM6jLwU%2BsA1WJl2nFqDKcTngrGaMS9yOQA7MXVhbztKXToG1uNoG0cLkdal20onCeK7dBgObZvM7ZrZ4uzGcqu9PV7UbCJngkvByqS6B4RN6ahOPD4a1BkmNXZa2MvhvpUfUo5GpgLkbt6Pv1ewK7RQtOi46KsVDrXAQ2LDHckP1OBww%2BjoDJ99ruOQdavLRI7M7WGlHQGH0g8D7h61VEZsyMJGeSdmFx7MbSFtkwUbq1kkmjSf%2BgHP9k%2FwZ91kgLSPtNvd575udbpkm0fvUxpcLW70U6Vf8E%2FNMvvCe78tpC3%2Bl46Sl4EcME77bPIeUpjgUNDUEY8CZS7ItG8Q6a1DnaiIvIRIVk%2FQ9y5zktHyGI04sq5BOMDbB7dLRXIpC%2BysbDdew4Zom7%2BQR8PjDglfzOBjqkAUmk7M7a2IzcILgcVDCKkaDh%2BRP4rKtUM0gnp%2BSPnTWLSqok4t7%2FBF1kEYNWimWekATJxFQ3%2FH%2Bt4aIdi5bo8HnqXxHQXOxwiX6wM2IBbmWmGjh2uvwtCMn8j7oPHFsP%2F9bfmXNVQipRXmkreABnod%2F3oYBXo%2B2UuoN4lgdy94rWImNuWgxVYNNzuAMtDXMF7jvhXAy%2B7sM0sDkcQhJDX%2Btk08jm&X-Amz-Signature=3791aa9f2a1a00465213b270bf01b0c1099e35257d1f6327a10cf2a18a217273&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCYUEA3J%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS5oq%2BPUvOSxv5u1RP3tL6tFl2EnCAW%2BN3CHWyaC3obAIhAMZxfavvKx7Hp5s6HZDra3n4tGD7V3XrW%2B9JSiDPhjt4KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxprSbEgksFNqDVM6wq3APriIDo72Au64EhHXeYEselngA0JSHvOFQ0Tc%2B4JPXiXNX5BRuNNhgDNoVOeDy4VOzAzFDBWobt4Wiwnj%2FqNT9lYP%2B9cePRx53FM%2FlLzabsh7fH89QBYqj5CMV9FDLQa4cSVIwmeQOLbvCQ2rv3PLOFRmJP3DZtgzZNbkTsy%2BSntxWJooFdPt%2FKBqaO1x3Q1nmD436CA6de2hv1BJhO5IYQIRtpp%2FrGxvEG%2FTaxGINqM6jLwU%2BsA1WJl2nFqDKcTngrGaMS9yOQA7MXVhbztKXToG1uNoG0cLkdal20onCeK7dBgObZvM7ZrZ4uzGcqu9PV7UbCJngkvByqS6B4RN6ahOPD4a1BkmNXZa2MvhvpUfUo5GpgLkbt6Pv1ewK7RQtOi46KsVDrXAQ2LDHckP1OBww%2BjoDJ99ruOQdavLRI7M7WGlHQGH0g8D7h61VEZsyMJGeSdmFx7MbSFtkwUbq1kkmjSf%2BgHP9k%2FwZ91kgLSPtNvd575udbpkm0fvUxpcLW70U6Vf8E%2FNMvvCe78tpC3%2Bl46Sl4EcME77bPIeUpjgUNDUEY8CZS7ItG8Q6a1DnaiIvIRIVk%2FQ9y5zktHyGI04sq5BOMDbB7dLRXIpC%2BysbDdew4Zom7%2BQR8PjDglfzOBjqkAUmk7M7a2IzcILgcVDCKkaDh%2BRP4rKtUM0gnp%2BSPnTWLSqok4t7%2FBF1kEYNWimWekATJxFQ3%2FH%2Bt4aIdi5bo8HnqXxHQXOxwiX6wM2IBbmWmGjh2uvwtCMn8j7oPHFsP%2F9bfmXNVQipRXmkreABnod%2F3oYBXo%2B2UuoN4lgdy94rWImNuWgxVYNNzuAMtDXMF7jvhXAy%2B7sM0sDkcQhJDX%2Btk08jm&X-Amz-Signature=4a070373ad9210ef677a61bc23d8fee2778e30c6d436723b51437316045aa93f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCYUEA3J%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS5oq%2BPUvOSxv5u1RP3tL6tFl2EnCAW%2BN3CHWyaC3obAIhAMZxfavvKx7Hp5s6HZDra3n4tGD7V3XrW%2B9JSiDPhjt4KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxprSbEgksFNqDVM6wq3APriIDo72Au64EhHXeYEselngA0JSHvOFQ0Tc%2B4JPXiXNX5BRuNNhgDNoVOeDy4VOzAzFDBWobt4Wiwnj%2FqNT9lYP%2B9cePRx53FM%2FlLzabsh7fH89QBYqj5CMV9FDLQa4cSVIwmeQOLbvCQ2rv3PLOFRmJP3DZtgzZNbkTsy%2BSntxWJooFdPt%2FKBqaO1x3Q1nmD436CA6de2hv1BJhO5IYQIRtpp%2FrGxvEG%2FTaxGINqM6jLwU%2BsA1WJl2nFqDKcTngrGaMS9yOQA7MXVhbztKXToG1uNoG0cLkdal20onCeK7dBgObZvM7ZrZ4uzGcqu9PV7UbCJngkvByqS6B4RN6ahOPD4a1BkmNXZa2MvhvpUfUo5GpgLkbt6Pv1ewK7RQtOi46KsVDrXAQ2LDHckP1OBww%2BjoDJ99ruOQdavLRI7M7WGlHQGH0g8D7h61VEZsyMJGeSdmFx7MbSFtkwUbq1kkmjSf%2BgHP9k%2FwZ91kgLSPtNvd575udbpkm0fvUxpcLW70U6Vf8E%2FNMvvCe78tpC3%2Bl46Sl4EcME77bPIeUpjgUNDUEY8CZS7ItG8Q6a1DnaiIvIRIVk%2FQ9y5zktHyGI04sq5BOMDbB7dLRXIpC%2BysbDdew4Zom7%2BQR8PjDglfzOBjqkAUmk7M7a2IzcILgcVDCKkaDh%2BRP4rKtUM0gnp%2BSPnTWLSqok4t7%2FBF1kEYNWimWekATJxFQ3%2FH%2Bt4aIdi5bo8HnqXxHQXOxwiX6wM2IBbmWmGjh2uvwtCMn8j7oPHFsP%2F9bfmXNVQipRXmkreABnod%2F3oYBXo%2B2UuoN4lgdy94rWImNuWgxVYNNzuAMtDXMF7jvhXAy%2B7sM0sDkcQhJDX%2Btk08jm&X-Amz-Signature=ce7533f5de90b3549b4c8c9301382fc472989139b0e4b062b8828517e85c4ef9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCYUEA3J%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS5oq%2BPUvOSxv5u1RP3tL6tFl2EnCAW%2BN3CHWyaC3obAIhAMZxfavvKx7Hp5s6HZDra3n4tGD7V3XrW%2B9JSiDPhjt4KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxprSbEgksFNqDVM6wq3APriIDo72Au64EhHXeYEselngA0JSHvOFQ0Tc%2B4JPXiXNX5BRuNNhgDNoVOeDy4VOzAzFDBWobt4Wiwnj%2FqNT9lYP%2B9cePRx53FM%2FlLzabsh7fH89QBYqj5CMV9FDLQa4cSVIwmeQOLbvCQ2rv3PLOFRmJP3DZtgzZNbkTsy%2BSntxWJooFdPt%2FKBqaO1x3Q1nmD436CA6de2hv1BJhO5IYQIRtpp%2FrGxvEG%2FTaxGINqM6jLwU%2BsA1WJl2nFqDKcTngrGaMS9yOQA7MXVhbztKXToG1uNoG0cLkdal20onCeK7dBgObZvM7ZrZ4uzGcqu9PV7UbCJngkvByqS6B4RN6ahOPD4a1BkmNXZa2MvhvpUfUo5GpgLkbt6Pv1ewK7RQtOi46KsVDrXAQ2LDHckP1OBww%2BjoDJ99ruOQdavLRI7M7WGlHQGH0g8D7h61VEZsyMJGeSdmFx7MbSFtkwUbq1kkmjSf%2BgHP9k%2FwZ91kgLSPtNvd575udbpkm0fvUxpcLW70U6Vf8E%2FNMvvCe78tpC3%2Bl46Sl4EcME77bPIeUpjgUNDUEY8CZS7ItG8Q6a1DnaiIvIRIVk%2FQ9y5zktHyGI04sq5BOMDbB7dLRXIpC%2BysbDdew4Zom7%2BQR8PjDglfzOBjqkAUmk7M7a2IzcILgcVDCKkaDh%2BRP4rKtUM0gnp%2BSPnTWLSqok4t7%2FBF1kEYNWimWekATJxFQ3%2FH%2Bt4aIdi5bo8HnqXxHQXOxwiX6wM2IBbmWmGjh2uvwtCMn8j7oPHFsP%2F9bfmXNVQipRXmkreABnod%2F3oYBXo%2B2UuoN4lgdy94rWImNuWgxVYNNzuAMtDXMF7jvhXAy%2B7sM0sDkcQhJDX%2Btk08jm&X-Amz-Signature=0ba3e01ed7cb15ed8b18d4768c8293df192a3d3c2d19e7c9df6f5ed523d704d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCYUEA3J%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS5oq%2BPUvOSxv5u1RP3tL6tFl2EnCAW%2BN3CHWyaC3obAIhAMZxfavvKx7Hp5s6HZDra3n4tGD7V3XrW%2B9JSiDPhjt4KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxprSbEgksFNqDVM6wq3APriIDo72Au64EhHXeYEselngA0JSHvOFQ0Tc%2B4JPXiXNX5BRuNNhgDNoVOeDy4VOzAzFDBWobt4Wiwnj%2FqNT9lYP%2B9cePRx53FM%2FlLzabsh7fH89QBYqj5CMV9FDLQa4cSVIwmeQOLbvCQ2rv3PLOFRmJP3DZtgzZNbkTsy%2BSntxWJooFdPt%2FKBqaO1x3Q1nmD436CA6de2hv1BJhO5IYQIRtpp%2FrGxvEG%2FTaxGINqM6jLwU%2BsA1WJl2nFqDKcTngrGaMS9yOQA7MXVhbztKXToG1uNoG0cLkdal20onCeK7dBgObZvM7ZrZ4uzGcqu9PV7UbCJngkvByqS6B4RN6ahOPD4a1BkmNXZa2MvhvpUfUo5GpgLkbt6Pv1ewK7RQtOi46KsVDrXAQ2LDHckP1OBww%2BjoDJ99ruOQdavLRI7M7WGlHQGH0g8D7h61VEZsyMJGeSdmFx7MbSFtkwUbq1kkmjSf%2BgHP9k%2FwZ91kgLSPtNvd575udbpkm0fvUxpcLW70U6Vf8E%2FNMvvCe78tpC3%2Bl46Sl4EcME77bPIeUpjgUNDUEY8CZS7ItG8Q6a1DnaiIvIRIVk%2FQ9y5zktHyGI04sq5BOMDbB7dLRXIpC%2BysbDdew4Zom7%2BQR8PjDglfzOBjqkAUmk7M7a2IzcILgcVDCKkaDh%2BRP4rKtUM0gnp%2BSPnTWLSqok4t7%2FBF1kEYNWimWekATJxFQ3%2FH%2Bt4aIdi5bo8HnqXxHQXOxwiX6wM2IBbmWmGjh2uvwtCMn8j7oPHFsP%2F9bfmXNVQipRXmkreABnod%2F3oYBXo%2B2UuoN4lgdy94rWImNuWgxVYNNzuAMtDXMF7jvhXAy%2B7sM0sDkcQhJDX%2Btk08jm&X-Amz-Signature=e1cc2f41e853dbeb5b7c43110667d2ecdff2edb99d2aa477e8974d3241e39fd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCYUEA3J%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS5oq%2BPUvOSxv5u1RP3tL6tFl2EnCAW%2BN3CHWyaC3obAIhAMZxfavvKx7Hp5s6HZDra3n4tGD7V3XrW%2B9JSiDPhjt4KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxprSbEgksFNqDVM6wq3APriIDo72Au64EhHXeYEselngA0JSHvOFQ0Tc%2B4JPXiXNX5BRuNNhgDNoVOeDy4VOzAzFDBWobt4Wiwnj%2FqNT9lYP%2B9cePRx53FM%2FlLzabsh7fH89QBYqj5CMV9FDLQa4cSVIwmeQOLbvCQ2rv3PLOFRmJP3DZtgzZNbkTsy%2BSntxWJooFdPt%2FKBqaO1x3Q1nmD436CA6de2hv1BJhO5IYQIRtpp%2FrGxvEG%2FTaxGINqM6jLwU%2BsA1WJl2nFqDKcTngrGaMS9yOQA7MXVhbztKXToG1uNoG0cLkdal20onCeK7dBgObZvM7ZrZ4uzGcqu9PV7UbCJngkvByqS6B4RN6ahOPD4a1BkmNXZa2MvhvpUfUo5GpgLkbt6Pv1ewK7RQtOi46KsVDrXAQ2LDHckP1OBww%2BjoDJ99ruOQdavLRI7M7WGlHQGH0g8D7h61VEZsyMJGeSdmFx7MbSFtkwUbq1kkmjSf%2BgHP9k%2FwZ91kgLSPtNvd575udbpkm0fvUxpcLW70U6Vf8E%2FNMvvCe78tpC3%2Bl46Sl4EcME77bPIeUpjgUNDUEY8CZS7ItG8Q6a1DnaiIvIRIVk%2FQ9y5zktHyGI04sq5BOMDbB7dLRXIpC%2BysbDdew4Zom7%2BQR8PjDglfzOBjqkAUmk7M7a2IzcILgcVDCKkaDh%2BRP4rKtUM0gnp%2BSPnTWLSqok4t7%2FBF1kEYNWimWekATJxFQ3%2FH%2Bt4aIdi5bo8HnqXxHQXOxwiX6wM2IBbmWmGjh2uvwtCMn8j7oPHFsP%2F9bfmXNVQipRXmkreABnod%2F3oYBXo%2B2UuoN4lgdy94rWImNuWgxVYNNzuAMtDXMF7jvhXAy%2B7sM0sDkcQhJDX%2Btk08jm&X-Amz-Signature=314b6694428c716f171d3e8c56614f1abcd5aaf498c76e4d7ab2523d4b2553bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCYUEA3J%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS5oq%2BPUvOSxv5u1RP3tL6tFl2EnCAW%2BN3CHWyaC3obAIhAMZxfavvKx7Hp5s6HZDra3n4tGD7V3XrW%2B9JSiDPhjt4KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxprSbEgksFNqDVM6wq3APriIDo72Au64EhHXeYEselngA0JSHvOFQ0Tc%2B4JPXiXNX5BRuNNhgDNoVOeDy4VOzAzFDBWobt4Wiwnj%2FqNT9lYP%2B9cePRx53FM%2FlLzabsh7fH89QBYqj5CMV9FDLQa4cSVIwmeQOLbvCQ2rv3PLOFRmJP3DZtgzZNbkTsy%2BSntxWJooFdPt%2FKBqaO1x3Q1nmD436CA6de2hv1BJhO5IYQIRtpp%2FrGxvEG%2FTaxGINqM6jLwU%2BsA1WJl2nFqDKcTngrGaMS9yOQA7MXVhbztKXToG1uNoG0cLkdal20onCeK7dBgObZvM7ZrZ4uzGcqu9PV7UbCJngkvByqS6B4RN6ahOPD4a1BkmNXZa2MvhvpUfUo5GpgLkbt6Pv1ewK7RQtOi46KsVDrXAQ2LDHckP1OBww%2BjoDJ99ruOQdavLRI7M7WGlHQGH0g8D7h61VEZsyMJGeSdmFx7MbSFtkwUbq1kkmjSf%2BgHP9k%2FwZ91kgLSPtNvd575udbpkm0fvUxpcLW70U6Vf8E%2FNMvvCe78tpC3%2Bl46Sl4EcME77bPIeUpjgUNDUEY8CZS7ItG8Q6a1DnaiIvIRIVk%2FQ9y5zktHyGI04sq5BOMDbB7dLRXIpC%2BysbDdew4Zom7%2BQR8PjDglfzOBjqkAUmk7M7a2IzcILgcVDCKkaDh%2BRP4rKtUM0gnp%2BSPnTWLSqok4t7%2FBF1kEYNWimWekATJxFQ3%2FH%2Bt4aIdi5bo8HnqXxHQXOxwiX6wM2IBbmWmGjh2uvwtCMn8j7oPHFsP%2F9bfmXNVQipRXmkreABnod%2F3oYBXo%2B2UuoN4lgdy94rWImNuWgxVYNNzuAMtDXMF7jvhXAy%2B7sM0sDkcQhJDX%2Btk08jm&X-Amz-Signature=8622da2c22e308d9366b77b9cd17a85734f99b21162927cf60be321a1182b5c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCYUEA3J%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS5oq%2BPUvOSxv5u1RP3tL6tFl2EnCAW%2BN3CHWyaC3obAIhAMZxfavvKx7Hp5s6HZDra3n4tGD7V3XrW%2B9JSiDPhjt4KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxprSbEgksFNqDVM6wq3APriIDo72Au64EhHXeYEselngA0JSHvOFQ0Tc%2B4JPXiXNX5BRuNNhgDNoVOeDy4VOzAzFDBWobt4Wiwnj%2FqNT9lYP%2B9cePRx53FM%2FlLzabsh7fH89QBYqj5CMV9FDLQa4cSVIwmeQOLbvCQ2rv3PLOFRmJP3DZtgzZNbkTsy%2BSntxWJooFdPt%2FKBqaO1x3Q1nmD436CA6de2hv1BJhO5IYQIRtpp%2FrGxvEG%2FTaxGINqM6jLwU%2BsA1WJl2nFqDKcTngrGaMS9yOQA7MXVhbztKXToG1uNoG0cLkdal20onCeK7dBgObZvM7ZrZ4uzGcqu9PV7UbCJngkvByqS6B4RN6ahOPD4a1BkmNXZa2MvhvpUfUo5GpgLkbt6Pv1ewK7RQtOi46KsVDrXAQ2LDHckP1OBww%2BjoDJ99ruOQdavLRI7M7WGlHQGH0g8D7h61VEZsyMJGeSdmFx7MbSFtkwUbq1kkmjSf%2BgHP9k%2FwZ91kgLSPtNvd575udbpkm0fvUxpcLW70U6Vf8E%2FNMvvCe78tpC3%2Bl46Sl4EcME77bPIeUpjgUNDUEY8CZS7ItG8Q6a1DnaiIvIRIVk%2FQ9y5zktHyGI04sq5BOMDbB7dLRXIpC%2BysbDdew4Zom7%2BQR8PjDglfzOBjqkAUmk7M7a2IzcILgcVDCKkaDh%2BRP4rKtUM0gnp%2BSPnTWLSqok4t7%2FBF1kEYNWimWekATJxFQ3%2FH%2Bt4aIdi5bo8HnqXxHQXOxwiX6wM2IBbmWmGjh2uvwtCMn8j7oPHFsP%2F9bfmXNVQipRXmkreABnod%2F3oYBXo%2B2UuoN4lgdy94rWImNuWgxVYNNzuAMtDXMF7jvhXAy%2B7sM0sDkcQhJDX%2Btk08jm&X-Amz-Signature=da4cdc2b64d5f88e053473c465e02a600a54f26b498331ec5114651b6f23129b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCYUEA3J%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS5oq%2BPUvOSxv5u1RP3tL6tFl2EnCAW%2BN3CHWyaC3obAIhAMZxfavvKx7Hp5s6HZDra3n4tGD7V3XrW%2B9JSiDPhjt4KogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxprSbEgksFNqDVM6wq3APriIDo72Au64EhHXeYEselngA0JSHvOFQ0Tc%2B4JPXiXNX5BRuNNhgDNoVOeDy4VOzAzFDBWobt4Wiwnj%2FqNT9lYP%2B9cePRx53FM%2FlLzabsh7fH89QBYqj5CMV9FDLQa4cSVIwmeQOLbvCQ2rv3PLOFRmJP3DZtgzZNbkTsy%2BSntxWJooFdPt%2FKBqaO1x3Q1nmD436CA6de2hv1BJhO5IYQIRtpp%2FrGxvEG%2FTaxGINqM6jLwU%2BsA1WJl2nFqDKcTngrGaMS9yOQA7MXVhbztKXToG1uNoG0cLkdal20onCeK7dBgObZvM7ZrZ4uzGcqu9PV7UbCJngkvByqS6B4RN6ahOPD4a1BkmNXZa2MvhvpUfUo5GpgLkbt6Pv1ewK7RQtOi46KsVDrXAQ2LDHckP1OBww%2BjoDJ99ruOQdavLRI7M7WGlHQGH0g8D7h61VEZsyMJGeSdmFx7MbSFtkwUbq1kkmjSf%2BgHP9k%2FwZ91kgLSPtNvd575udbpkm0fvUxpcLW70U6Vf8E%2FNMvvCe78tpC3%2Bl46Sl4EcME77bPIeUpjgUNDUEY8CZS7ItG8Q6a1DnaiIvIRIVk%2FQ9y5zktHyGI04sq5BOMDbB7dLRXIpC%2BysbDdew4Zom7%2BQR8PjDglfzOBjqkAUmk7M7a2IzcILgcVDCKkaDh%2BRP4rKtUM0gnp%2BSPnTWLSqok4t7%2FBF1kEYNWimWekATJxFQ3%2FH%2Bt4aIdi5bo8HnqXxHQXOxwiX6wM2IBbmWmGjh2uvwtCMn8j7oPHFsP%2F9bfmXNVQipRXmkreABnod%2F3oYBXo%2B2UuoN4lgdy94rWImNuWgxVYNNzuAMtDXMF7jvhXAy%2B7sM0sDkcQhJDX%2Btk08jm&X-Amz-Signature=e093129ba5ca1bdc59a52477a905faeb82ffb60970b8c984df5621997ce78ab2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

