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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2YR5KC%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC6e0NjpXHQugVR5Lovm0gJzfPbMtPFplig7dTfbJqYZwIhAL2JYhqOhEy3kvgzOckUFEQkc2%2FBeDL0KUrTEK7XL5gyKv8DCAUQABoMNjM3NDIzMTgzODA1Igweu0Eky2Oi0RcITGMq3ANZVEporUQh81WBoyidTUkoqVluDgCbuWSmlV9RcEjtz4sTQ9BT41X8ROQ1Nncui%2F%2FtuaSzT2UbJcQToesKPVmsXz6O2qv4CgG%2BOEbCIRVssa8BY1AlM9QvE%2FZP06jgLdcm4TLJzTRV3tD7c9hrK8NnROMsNdO6cTxVx7Y7pjjQEvlXu%2BOLbT1TfKryhEo974TSVI3UKZ4vMH4Hb%2B4LhTnu8WW1fyfQDQeVfLcy5vaZJ4zYBJq1GrVD0BKMK43a5k%2BvoLpoSWIJltEHNji8OT1xCboUi3oLnXMsFhNEB7%2F90902HpRZhbAlKXKjnE6H7j3mJvtgVYW8hMVAuc7%2FCS%2F4eYHC%2BhwSGSigl%2B9cqwwN%2BomygmcHXe6o4zWC7G6aZlb%2Bi0gnBKaCOrk25Om6%2FJo3dWTUgcTf7hNi1BFtZPl0Ep5bntlL3R73yB%2Fg%2BK4KDvi1XLKJp%2Bu5FkaRqOFys%2B3d%2FbjaG6VmSGvfvwvdBbxRj%2FBXVtN%2B8%2FGMF0vfYv%2F%2FBNEAHc4%2Bm43LKtuPny24aCumThyCjvuGSzrdRdWC6XR9%2BxN3WLbUGwBPA271VZ6o%2BELWFHrk4YWXzwQwZsuMUr0AiYDDmVkuJ8%2BUqqAefN9MCk0VDhDOd9bB8bDt%2FzDbvaLOBjqkAalL4Na63MY8UIbVpYx0trbi1aR%2Fa38vIQ9kkeRi3qXXpwPI4BVGBczQt6hkeKGmWicmZjZMAjOTCtI21WVGVEiK4VlF8AV9QBbX2ViD%2F4NPkmU4qpPc7DPZd4Ny%2FFZzNrSCdcw1XDbAuZXZ6btOcadGby2I1VuxfpUqbw6hzSwJYt%2FWigVrEO1JKGJr%2Bwt9wKWE5wKO0go4%2BMTQ8S0ZVPmLyP4q&X-Amz-Signature=59c0f669bc9b8456fcc234ad78c3aedb2267bd6d07f5fe1a0ad7b9f7a8ba3e97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2YR5KC%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC6e0NjpXHQugVR5Lovm0gJzfPbMtPFplig7dTfbJqYZwIhAL2JYhqOhEy3kvgzOckUFEQkc2%2FBeDL0KUrTEK7XL5gyKv8DCAUQABoMNjM3NDIzMTgzODA1Igweu0Eky2Oi0RcITGMq3ANZVEporUQh81WBoyidTUkoqVluDgCbuWSmlV9RcEjtz4sTQ9BT41X8ROQ1Nncui%2F%2FtuaSzT2UbJcQToesKPVmsXz6O2qv4CgG%2BOEbCIRVssa8BY1AlM9QvE%2FZP06jgLdcm4TLJzTRV3tD7c9hrK8NnROMsNdO6cTxVx7Y7pjjQEvlXu%2BOLbT1TfKryhEo974TSVI3UKZ4vMH4Hb%2B4LhTnu8WW1fyfQDQeVfLcy5vaZJ4zYBJq1GrVD0BKMK43a5k%2BvoLpoSWIJltEHNji8OT1xCboUi3oLnXMsFhNEB7%2F90902HpRZhbAlKXKjnE6H7j3mJvtgVYW8hMVAuc7%2FCS%2F4eYHC%2BhwSGSigl%2B9cqwwN%2BomygmcHXe6o4zWC7G6aZlb%2Bi0gnBKaCOrk25Om6%2FJo3dWTUgcTf7hNi1BFtZPl0Ep5bntlL3R73yB%2Fg%2BK4KDvi1XLKJp%2Bu5FkaRqOFys%2B3d%2FbjaG6VmSGvfvwvdBbxRj%2FBXVtN%2B8%2FGMF0vfYv%2F%2FBNEAHc4%2Bm43LKtuPny24aCumThyCjvuGSzrdRdWC6XR9%2BxN3WLbUGwBPA271VZ6o%2BELWFHrk4YWXzwQwZsuMUr0AiYDDmVkuJ8%2BUqqAefN9MCk0VDhDOd9bB8bDt%2FzDbvaLOBjqkAalL4Na63MY8UIbVpYx0trbi1aR%2Fa38vIQ9kkeRi3qXXpwPI4BVGBczQt6hkeKGmWicmZjZMAjOTCtI21WVGVEiK4VlF8AV9QBbX2ViD%2F4NPkmU4qpPc7DPZd4Ny%2FFZzNrSCdcw1XDbAuZXZ6btOcadGby2I1VuxfpUqbw6hzSwJYt%2FWigVrEO1JKGJr%2Bwt9wKWE5wKO0go4%2BMTQ8S0ZVPmLyP4q&X-Amz-Signature=2a343447f83dcdde13e5a8b8a1d59dc0bf2c3492f2cfe878b4cef6eb6506b36c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2YR5KC%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC6e0NjpXHQugVR5Lovm0gJzfPbMtPFplig7dTfbJqYZwIhAL2JYhqOhEy3kvgzOckUFEQkc2%2FBeDL0KUrTEK7XL5gyKv8DCAUQABoMNjM3NDIzMTgzODA1Igweu0Eky2Oi0RcITGMq3ANZVEporUQh81WBoyidTUkoqVluDgCbuWSmlV9RcEjtz4sTQ9BT41X8ROQ1Nncui%2F%2FtuaSzT2UbJcQToesKPVmsXz6O2qv4CgG%2BOEbCIRVssa8BY1AlM9QvE%2FZP06jgLdcm4TLJzTRV3tD7c9hrK8NnROMsNdO6cTxVx7Y7pjjQEvlXu%2BOLbT1TfKryhEo974TSVI3UKZ4vMH4Hb%2B4LhTnu8WW1fyfQDQeVfLcy5vaZJ4zYBJq1GrVD0BKMK43a5k%2BvoLpoSWIJltEHNji8OT1xCboUi3oLnXMsFhNEB7%2F90902HpRZhbAlKXKjnE6H7j3mJvtgVYW8hMVAuc7%2FCS%2F4eYHC%2BhwSGSigl%2B9cqwwN%2BomygmcHXe6o4zWC7G6aZlb%2Bi0gnBKaCOrk25Om6%2FJo3dWTUgcTf7hNi1BFtZPl0Ep5bntlL3R73yB%2Fg%2BK4KDvi1XLKJp%2Bu5FkaRqOFys%2B3d%2FbjaG6VmSGvfvwvdBbxRj%2FBXVtN%2B8%2FGMF0vfYv%2F%2FBNEAHc4%2Bm43LKtuPny24aCumThyCjvuGSzrdRdWC6XR9%2BxN3WLbUGwBPA271VZ6o%2BELWFHrk4YWXzwQwZsuMUr0AiYDDmVkuJ8%2BUqqAefN9MCk0VDhDOd9bB8bDt%2FzDbvaLOBjqkAalL4Na63MY8UIbVpYx0trbi1aR%2Fa38vIQ9kkeRi3qXXpwPI4BVGBczQt6hkeKGmWicmZjZMAjOTCtI21WVGVEiK4VlF8AV9QBbX2ViD%2F4NPkmU4qpPc7DPZd4Ny%2FFZzNrSCdcw1XDbAuZXZ6btOcadGby2I1VuxfpUqbw6hzSwJYt%2FWigVrEO1JKGJr%2Bwt9wKWE5wKO0go4%2BMTQ8S0ZVPmLyP4q&X-Amz-Signature=4a80606961e78094f3b2d3491c88e447bab4d5f2cf365bdf764fbdc61de4f685&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2YR5KC%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC6e0NjpXHQugVR5Lovm0gJzfPbMtPFplig7dTfbJqYZwIhAL2JYhqOhEy3kvgzOckUFEQkc2%2FBeDL0KUrTEK7XL5gyKv8DCAUQABoMNjM3NDIzMTgzODA1Igweu0Eky2Oi0RcITGMq3ANZVEporUQh81WBoyidTUkoqVluDgCbuWSmlV9RcEjtz4sTQ9BT41X8ROQ1Nncui%2F%2FtuaSzT2UbJcQToesKPVmsXz6O2qv4CgG%2BOEbCIRVssa8BY1AlM9QvE%2FZP06jgLdcm4TLJzTRV3tD7c9hrK8NnROMsNdO6cTxVx7Y7pjjQEvlXu%2BOLbT1TfKryhEo974TSVI3UKZ4vMH4Hb%2B4LhTnu8WW1fyfQDQeVfLcy5vaZJ4zYBJq1GrVD0BKMK43a5k%2BvoLpoSWIJltEHNji8OT1xCboUi3oLnXMsFhNEB7%2F90902HpRZhbAlKXKjnE6H7j3mJvtgVYW8hMVAuc7%2FCS%2F4eYHC%2BhwSGSigl%2B9cqwwN%2BomygmcHXe6o4zWC7G6aZlb%2Bi0gnBKaCOrk25Om6%2FJo3dWTUgcTf7hNi1BFtZPl0Ep5bntlL3R73yB%2Fg%2BK4KDvi1XLKJp%2Bu5FkaRqOFys%2B3d%2FbjaG6VmSGvfvwvdBbxRj%2FBXVtN%2B8%2FGMF0vfYv%2F%2FBNEAHc4%2Bm43LKtuPny24aCumThyCjvuGSzrdRdWC6XR9%2BxN3WLbUGwBPA271VZ6o%2BELWFHrk4YWXzwQwZsuMUr0AiYDDmVkuJ8%2BUqqAefN9MCk0VDhDOd9bB8bDt%2FzDbvaLOBjqkAalL4Na63MY8UIbVpYx0trbi1aR%2Fa38vIQ9kkeRi3qXXpwPI4BVGBczQt6hkeKGmWicmZjZMAjOTCtI21WVGVEiK4VlF8AV9QBbX2ViD%2F4NPkmU4qpPc7DPZd4Ny%2FFZzNrSCdcw1XDbAuZXZ6btOcadGby2I1VuxfpUqbw6hzSwJYt%2FWigVrEO1JKGJr%2Bwt9wKWE5wKO0go4%2BMTQ8S0ZVPmLyP4q&X-Amz-Signature=da7fa425a23c8b9b6f2e83cd409103f6c41ca7060e5f73a7b9410813422198ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2YR5KC%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC6e0NjpXHQugVR5Lovm0gJzfPbMtPFplig7dTfbJqYZwIhAL2JYhqOhEy3kvgzOckUFEQkc2%2FBeDL0KUrTEK7XL5gyKv8DCAUQABoMNjM3NDIzMTgzODA1Igweu0Eky2Oi0RcITGMq3ANZVEporUQh81WBoyidTUkoqVluDgCbuWSmlV9RcEjtz4sTQ9BT41X8ROQ1Nncui%2F%2FtuaSzT2UbJcQToesKPVmsXz6O2qv4CgG%2BOEbCIRVssa8BY1AlM9QvE%2FZP06jgLdcm4TLJzTRV3tD7c9hrK8NnROMsNdO6cTxVx7Y7pjjQEvlXu%2BOLbT1TfKryhEo974TSVI3UKZ4vMH4Hb%2B4LhTnu8WW1fyfQDQeVfLcy5vaZJ4zYBJq1GrVD0BKMK43a5k%2BvoLpoSWIJltEHNji8OT1xCboUi3oLnXMsFhNEB7%2F90902HpRZhbAlKXKjnE6H7j3mJvtgVYW8hMVAuc7%2FCS%2F4eYHC%2BhwSGSigl%2B9cqwwN%2BomygmcHXe6o4zWC7G6aZlb%2Bi0gnBKaCOrk25Om6%2FJo3dWTUgcTf7hNi1BFtZPl0Ep5bntlL3R73yB%2Fg%2BK4KDvi1XLKJp%2Bu5FkaRqOFys%2B3d%2FbjaG6VmSGvfvwvdBbxRj%2FBXVtN%2B8%2FGMF0vfYv%2F%2FBNEAHc4%2Bm43LKtuPny24aCumThyCjvuGSzrdRdWC6XR9%2BxN3WLbUGwBPA271VZ6o%2BELWFHrk4YWXzwQwZsuMUr0AiYDDmVkuJ8%2BUqqAefN9MCk0VDhDOd9bB8bDt%2FzDbvaLOBjqkAalL4Na63MY8UIbVpYx0trbi1aR%2Fa38vIQ9kkeRi3qXXpwPI4BVGBczQt6hkeKGmWicmZjZMAjOTCtI21WVGVEiK4VlF8AV9QBbX2ViD%2F4NPkmU4qpPc7DPZd4Ny%2FFZzNrSCdcw1XDbAuZXZ6btOcadGby2I1VuxfpUqbw6hzSwJYt%2FWigVrEO1JKGJr%2Bwt9wKWE5wKO0go4%2BMTQ8S0ZVPmLyP4q&X-Amz-Signature=f65ed4125ea10085f22963341bdf2d5fbad8976c80c2815d57996ddc16c80b2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2YR5KC%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC6e0NjpXHQugVR5Lovm0gJzfPbMtPFplig7dTfbJqYZwIhAL2JYhqOhEy3kvgzOckUFEQkc2%2FBeDL0KUrTEK7XL5gyKv8DCAUQABoMNjM3NDIzMTgzODA1Igweu0Eky2Oi0RcITGMq3ANZVEporUQh81WBoyidTUkoqVluDgCbuWSmlV9RcEjtz4sTQ9BT41X8ROQ1Nncui%2F%2FtuaSzT2UbJcQToesKPVmsXz6O2qv4CgG%2BOEbCIRVssa8BY1AlM9QvE%2FZP06jgLdcm4TLJzTRV3tD7c9hrK8NnROMsNdO6cTxVx7Y7pjjQEvlXu%2BOLbT1TfKryhEo974TSVI3UKZ4vMH4Hb%2B4LhTnu8WW1fyfQDQeVfLcy5vaZJ4zYBJq1GrVD0BKMK43a5k%2BvoLpoSWIJltEHNji8OT1xCboUi3oLnXMsFhNEB7%2F90902HpRZhbAlKXKjnE6H7j3mJvtgVYW8hMVAuc7%2FCS%2F4eYHC%2BhwSGSigl%2B9cqwwN%2BomygmcHXe6o4zWC7G6aZlb%2Bi0gnBKaCOrk25Om6%2FJo3dWTUgcTf7hNi1BFtZPl0Ep5bntlL3R73yB%2Fg%2BK4KDvi1XLKJp%2Bu5FkaRqOFys%2B3d%2FbjaG6VmSGvfvwvdBbxRj%2FBXVtN%2B8%2FGMF0vfYv%2F%2FBNEAHc4%2Bm43LKtuPny24aCumThyCjvuGSzrdRdWC6XR9%2BxN3WLbUGwBPA271VZ6o%2BELWFHrk4YWXzwQwZsuMUr0AiYDDmVkuJ8%2BUqqAefN9MCk0VDhDOd9bB8bDt%2FzDbvaLOBjqkAalL4Na63MY8UIbVpYx0trbi1aR%2Fa38vIQ9kkeRi3qXXpwPI4BVGBczQt6hkeKGmWicmZjZMAjOTCtI21WVGVEiK4VlF8AV9QBbX2ViD%2F4NPkmU4qpPc7DPZd4Ny%2FFZzNrSCdcw1XDbAuZXZ6btOcadGby2I1VuxfpUqbw6hzSwJYt%2FWigVrEO1JKGJr%2Bwt9wKWE5wKO0go4%2BMTQ8S0ZVPmLyP4q&X-Amz-Signature=a0abdc0c8015d2fdd2d7c7a7e105485809b95ab0e8aa99250478da2842ff6420&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2YR5KC%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC6e0NjpXHQugVR5Lovm0gJzfPbMtPFplig7dTfbJqYZwIhAL2JYhqOhEy3kvgzOckUFEQkc2%2FBeDL0KUrTEK7XL5gyKv8DCAUQABoMNjM3NDIzMTgzODA1Igweu0Eky2Oi0RcITGMq3ANZVEporUQh81WBoyidTUkoqVluDgCbuWSmlV9RcEjtz4sTQ9BT41X8ROQ1Nncui%2F%2FtuaSzT2UbJcQToesKPVmsXz6O2qv4CgG%2BOEbCIRVssa8BY1AlM9QvE%2FZP06jgLdcm4TLJzTRV3tD7c9hrK8NnROMsNdO6cTxVx7Y7pjjQEvlXu%2BOLbT1TfKryhEo974TSVI3UKZ4vMH4Hb%2B4LhTnu8WW1fyfQDQeVfLcy5vaZJ4zYBJq1GrVD0BKMK43a5k%2BvoLpoSWIJltEHNji8OT1xCboUi3oLnXMsFhNEB7%2F90902HpRZhbAlKXKjnE6H7j3mJvtgVYW8hMVAuc7%2FCS%2F4eYHC%2BhwSGSigl%2B9cqwwN%2BomygmcHXe6o4zWC7G6aZlb%2Bi0gnBKaCOrk25Om6%2FJo3dWTUgcTf7hNi1BFtZPl0Ep5bntlL3R73yB%2Fg%2BK4KDvi1XLKJp%2Bu5FkaRqOFys%2B3d%2FbjaG6VmSGvfvwvdBbxRj%2FBXVtN%2B8%2FGMF0vfYv%2F%2FBNEAHc4%2Bm43LKtuPny24aCumThyCjvuGSzrdRdWC6XR9%2BxN3WLbUGwBPA271VZ6o%2BELWFHrk4YWXzwQwZsuMUr0AiYDDmVkuJ8%2BUqqAefN9MCk0VDhDOd9bB8bDt%2FzDbvaLOBjqkAalL4Na63MY8UIbVpYx0trbi1aR%2Fa38vIQ9kkeRi3qXXpwPI4BVGBczQt6hkeKGmWicmZjZMAjOTCtI21WVGVEiK4VlF8AV9QBbX2ViD%2F4NPkmU4qpPc7DPZd4Ny%2FFZzNrSCdcw1XDbAuZXZ6btOcadGby2I1VuxfpUqbw6hzSwJYt%2FWigVrEO1JKGJr%2Bwt9wKWE5wKO0go4%2BMTQ8S0ZVPmLyP4q&X-Amz-Signature=bb9ddf14256ccc4122f95bbdeb80efe5ae7db1cbea8fe6f9ecccce8c065504b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2YR5KC%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC6e0NjpXHQugVR5Lovm0gJzfPbMtPFplig7dTfbJqYZwIhAL2JYhqOhEy3kvgzOckUFEQkc2%2FBeDL0KUrTEK7XL5gyKv8DCAUQABoMNjM3NDIzMTgzODA1Igweu0Eky2Oi0RcITGMq3ANZVEporUQh81WBoyidTUkoqVluDgCbuWSmlV9RcEjtz4sTQ9BT41X8ROQ1Nncui%2F%2FtuaSzT2UbJcQToesKPVmsXz6O2qv4CgG%2BOEbCIRVssa8BY1AlM9QvE%2FZP06jgLdcm4TLJzTRV3tD7c9hrK8NnROMsNdO6cTxVx7Y7pjjQEvlXu%2BOLbT1TfKryhEo974TSVI3UKZ4vMH4Hb%2B4LhTnu8WW1fyfQDQeVfLcy5vaZJ4zYBJq1GrVD0BKMK43a5k%2BvoLpoSWIJltEHNji8OT1xCboUi3oLnXMsFhNEB7%2F90902HpRZhbAlKXKjnE6H7j3mJvtgVYW8hMVAuc7%2FCS%2F4eYHC%2BhwSGSigl%2B9cqwwN%2BomygmcHXe6o4zWC7G6aZlb%2Bi0gnBKaCOrk25Om6%2FJo3dWTUgcTf7hNi1BFtZPl0Ep5bntlL3R73yB%2Fg%2BK4KDvi1XLKJp%2Bu5FkaRqOFys%2B3d%2FbjaG6VmSGvfvwvdBbxRj%2FBXVtN%2B8%2FGMF0vfYv%2F%2FBNEAHc4%2Bm43LKtuPny24aCumThyCjvuGSzrdRdWC6XR9%2BxN3WLbUGwBPA271VZ6o%2BELWFHrk4YWXzwQwZsuMUr0AiYDDmVkuJ8%2BUqqAefN9MCk0VDhDOd9bB8bDt%2FzDbvaLOBjqkAalL4Na63MY8UIbVpYx0trbi1aR%2Fa38vIQ9kkeRi3qXXpwPI4BVGBczQt6hkeKGmWicmZjZMAjOTCtI21WVGVEiK4VlF8AV9QBbX2ViD%2F4NPkmU4qpPc7DPZd4Ny%2FFZzNrSCdcw1XDbAuZXZ6btOcadGby2I1VuxfpUqbw6hzSwJYt%2FWigVrEO1JKGJr%2Bwt9wKWE5wKO0go4%2BMTQ8S0ZVPmLyP4q&X-Amz-Signature=83d36ceccdf858922170096e298ff497efaadbeb139f2e299673a94feb27d366&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2YR5KC%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC6e0NjpXHQugVR5Lovm0gJzfPbMtPFplig7dTfbJqYZwIhAL2JYhqOhEy3kvgzOckUFEQkc2%2FBeDL0KUrTEK7XL5gyKv8DCAUQABoMNjM3NDIzMTgzODA1Igweu0Eky2Oi0RcITGMq3ANZVEporUQh81WBoyidTUkoqVluDgCbuWSmlV9RcEjtz4sTQ9BT41X8ROQ1Nncui%2F%2FtuaSzT2UbJcQToesKPVmsXz6O2qv4CgG%2BOEbCIRVssa8BY1AlM9QvE%2FZP06jgLdcm4TLJzTRV3tD7c9hrK8NnROMsNdO6cTxVx7Y7pjjQEvlXu%2BOLbT1TfKryhEo974TSVI3UKZ4vMH4Hb%2B4LhTnu8WW1fyfQDQeVfLcy5vaZJ4zYBJq1GrVD0BKMK43a5k%2BvoLpoSWIJltEHNji8OT1xCboUi3oLnXMsFhNEB7%2F90902HpRZhbAlKXKjnE6H7j3mJvtgVYW8hMVAuc7%2FCS%2F4eYHC%2BhwSGSigl%2B9cqwwN%2BomygmcHXe6o4zWC7G6aZlb%2Bi0gnBKaCOrk25Om6%2FJo3dWTUgcTf7hNi1BFtZPl0Ep5bntlL3R73yB%2Fg%2BK4KDvi1XLKJp%2Bu5FkaRqOFys%2B3d%2FbjaG6VmSGvfvwvdBbxRj%2FBXVtN%2B8%2FGMF0vfYv%2F%2FBNEAHc4%2Bm43LKtuPny24aCumThyCjvuGSzrdRdWC6XR9%2BxN3WLbUGwBPA271VZ6o%2BELWFHrk4YWXzwQwZsuMUr0AiYDDmVkuJ8%2BUqqAefN9MCk0VDhDOd9bB8bDt%2FzDbvaLOBjqkAalL4Na63MY8UIbVpYx0trbi1aR%2Fa38vIQ9kkeRi3qXXpwPI4BVGBczQt6hkeKGmWicmZjZMAjOTCtI21WVGVEiK4VlF8AV9QBbX2ViD%2F4NPkmU4qpPc7DPZd4Ny%2FFZzNrSCdcw1XDbAuZXZ6btOcadGby2I1VuxfpUqbw6hzSwJYt%2FWigVrEO1JKGJr%2Bwt9wKWE5wKO0go4%2BMTQ8S0ZVPmLyP4q&X-Amz-Signature=92af52d3f0df8dcfc047945477a16f3aede7d29dc148af7e2316ea6738263be0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WD2YR5KC%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC6e0NjpXHQugVR5Lovm0gJzfPbMtPFplig7dTfbJqYZwIhAL2JYhqOhEy3kvgzOckUFEQkc2%2FBeDL0KUrTEK7XL5gyKv8DCAUQABoMNjM3NDIzMTgzODA1Igweu0Eky2Oi0RcITGMq3ANZVEporUQh81WBoyidTUkoqVluDgCbuWSmlV9RcEjtz4sTQ9BT41X8ROQ1Nncui%2F%2FtuaSzT2UbJcQToesKPVmsXz6O2qv4CgG%2BOEbCIRVssa8BY1AlM9QvE%2FZP06jgLdcm4TLJzTRV3tD7c9hrK8NnROMsNdO6cTxVx7Y7pjjQEvlXu%2BOLbT1TfKryhEo974TSVI3UKZ4vMH4Hb%2B4LhTnu8WW1fyfQDQeVfLcy5vaZJ4zYBJq1GrVD0BKMK43a5k%2BvoLpoSWIJltEHNji8OT1xCboUi3oLnXMsFhNEB7%2F90902HpRZhbAlKXKjnE6H7j3mJvtgVYW8hMVAuc7%2FCS%2F4eYHC%2BhwSGSigl%2B9cqwwN%2BomygmcHXe6o4zWC7G6aZlb%2Bi0gnBKaCOrk25Om6%2FJo3dWTUgcTf7hNi1BFtZPl0Ep5bntlL3R73yB%2Fg%2BK4KDvi1XLKJp%2Bu5FkaRqOFys%2B3d%2FbjaG6VmSGvfvwvdBbxRj%2FBXVtN%2B8%2FGMF0vfYv%2F%2FBNEAHc4%2Bm43LKtuPny24aCumThyCjvuGSzrdRdWC6XR9%2BxN3WLbUGwBPA271VZ6o%2BELWFHrk4YWXzwQwZsuMUr0AiYDDmVkuJ8%2BUqqAefN9MCk0VDhDOd9bB8bDt%2FzDbvaLOBjqkAalL4Na63MY8UIbVpYx0trbi1aR%2Fa38vIQ9kkeRi3qXXpwPI4BVGBczQt6hkeKGmWicmZjZMAjOTCtI21WVGVEiK4VlF8AV9QBbX2ViD%2F4NPkmU4qpPc7DPZd4Ny%2FFZzNrSCdcw1XDbAuZXZ6btOcadGby2I1VuxfpUqbw6hzSwJYt%2FWigVrEO1JKGJr%2Bwt9wKWE5wKO0go4%2BMTQ8S0ZVPmLyP4q&X-Amz-Signature=ee44c2b2e0c9d931b9e15bdec1547e5eca4b2c0eaf9a498c6aa4d2d9a72e33c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

