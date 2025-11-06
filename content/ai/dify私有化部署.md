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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJXSE6ZB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrjAynKu1l8bhxo1OmPdemTs5m80UC9ESXY44Cpzm9ngIhAP299XXWvi9NinTKAFvvtRdbb6TYP6BusN%2FmM0laZYmSKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBJ8blFVzId6lSPeYq3AOgydEj%2F0fw5ISgEtqEeTO2tHCszWRKqq%2F4xP7xDB3QbksNwm1q4yA0My6tSLl5vRA7cRiAkGrxdHteRYEWxKbYsYHtFSMnC6Ro3OS3xZrJOADkzX0I9RZnp5VKX0PunPEKMWw99e1uwsbGGoAddmTydTlGYU2O%2FnxiyqQU6ieQ4lcAg0bLZQ49rjHXODBKqbrGNRkev9XosZZ1dP2Kdw2gPzkwSDOKmv69uEKWCStxsQlkDx%2Fu8LnT7PmkcArXJzQ1qNAkr4Insjph1%2FEQkqim4m5Pz5Lp2wRO2WKjSu4Fs%2BJNSy99YrCn4WW5KSiKogU9nVuyRxLgJaaHIZHhINkweTeTqSYnrdeYL71eK4zsnVp3DnT6d0K3YFzYkpiZEgTiJzS81%2Bngy2E%2BYsk%2B%2FVLvXISzLr2VponkQiBkiwPezG1vg9nmOz%2Bk6bSC2H%2BYbiVUULM1IBHP%2FJolSzRV8HDKds1loSNDBN8a4%2FFrfzrjwOL4x9zdWnO2cbRQp4DJ6vgIC%2B6mqFykV686nxL0TX0LYkXCG%2FiwZnYQu3NY1magFex0wlZwOhUsiuTli79Ngtrus17IepgVl%2FWtKSWAJ8%2B8xYAa%2BkowfFrp%2BScV0%2Fk%2Bz%2B61pzOIIdWkpnpJCjD%2FlLDIBjqkAc5VyqNZX3lWmqmg66g3bnOdQ2yspEgil%2B209S6IWfaLnsCV5G0qMCY8RJ9yEdYX6szI0SLPx5QTIYa4dSwq4fHdMXfjkxGH6GcIpWz3s2NxR9hjUCQq30QVWX%2FC89YFnW%2Bg0NXiB3Uc9p9cqX%2BBR%2Ba8vRQgognqI4bt9QsWDZ3cM15sRmCIO7pSVZOafyuz3rtD%2BxLn9SGBxO0cDjSmnE94Cgno&X-Amz-Signature=c4cc6401a86c3657858b5fa2fc57eafa2435c5b63a131bf7517b7df915b13bad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJXSE6ZB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrjAynKu1l8bhxo1OmPdemTs5m80UC9ESXY44Cpzm9ngIhAP299XXWvi9NinTKAFvvtRdbb6TYP6BusN%2FmM0laZYmSKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBJ8blFVzId6lSPeYq3AOgydEj%2F0fw5ISgEtqEeTO2tHCszWRKqq%2F4xP7xDB3QbksNwm1q4yA0My6tSLl5vRA7cRiAkGrxdHteRYEWxKbYsYHtFSMnC6Ro3OS3xZrJOADkzX0I9RZnp5VKX0PunPEKMWw99e1uwsbGGoAddmTydTlGYU2O%2FnxiyqQU6ieQ4lcAg0bLZQ49rjHXODBKqbrGNRkev9XosZZ1dP2Kdw2gPzkwSDOKmv69uEKWCStxsQlkDx%2Fu8LnT7PmkcArXJzQ1qNAkr4Insjph1%2FEQkqim4m5Pz5Lp2wRO2WKjSu4Fs%2BJNSy99YrCn4WW5KSiKogU9nVuyRxLgJaaHIZHhINkweTeTqSYnrdeYL71eK4zsnVp3DnT6d0K3YFzYkpiZEgTiJzS81%2Bngy2E%2BYsk%2B%2FVLvXISzLr2VponkQiBkiwPezG1vg9nmOz%2Bk6bSC2H%2BYbiVUULM1IBHP%2FJolSzRV8HDKds1loSNDBN8a4%2FFrfzrjwOL4x9zdWnO2cbRQp4DJ6vgIC%2B6mqFykV686nxL0TX0LYkXCG%2FiwZnYQu3NY1magFex0wlZwOhUsiuTli79Ngtrus17IepgVl%2FWtKSWAJ8%2B8xYAa%2BkowfFrp%2BScV0%2Fk%2Bz%2B61pzOIIdWkpnpJCjD%2FlLDIBjqkAc5VyqNZX3lWmqmg66g3bnOdQ2yspEgil%2B209S6IWfaLnsCV5G0qMCY8RJ9yEdYX6szI0SLPx5QTIYa4dSwq4fHdMXfjkxGH6GcIpWz3s2NxR9hjUCQq30QVWX%2FC89YFnW%2Bg0NXiB3Uc9p9cqX%2BBR%2Ba8vRQgognqI4bt9QsWDZ3cM15sRmCIO7pSVZOafyuz3rtD%2BxLn9SGBxO0cDjSmnE94Cgno&X-Amz-Signature=ad9dc708fbd1d40be205c68a99e73c11d0f42734bf1f448e4af1806266c97116&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJXSE6ZB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrjAynKu1l8bhxo1OmPdemTs5m80UC9ESXY44Cpzm9ngIhAP299XXWvi9NinTKAFvvtRdbb6TYP6BusN%2FmM0laZYmSKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBJ8blFVzId6lSPeYq3AOgydEj%2F0fw5ISgEtqEeTO2tHCszWRKqq%2F4xP7xDB3QbksNwm1q4yA0My6tSLl5vRA7cRiAkGrxdHteRYEWxKbYsYHtFSMnC6Ro3OS3xZrJOADkzX0I9RZnp5VKX0PunPEKMWw99e1uwsbGGoAddmTydTlGYU2O%2FnxiyqQU6ieQ4lcAg0bLZQ49rjHXODBKqbrGNRkev9XosZZ1dP2Kdw2gPzkwSDOKmv69uEKWCStxsQlkDx%2Fu8LnT7PmkcArXJzQ1qNAkr4Insjph1%2FEQkqim4m5Pz5Lp2wRO2WKjSu4Fs%2BJNSy99YrCn4WW5KSiKogU9nVuyRxLgJaaHIZHhINkweTeTqSYnrdeYL71eK4zsnVp3DnT6d0K3YFzYkpiZEgTiJzS81%2Bngy2E%2BYsk%2B%2FVLvXISzLr2VponkQiBkiwPezG1vg9nmOz%2Bk6bSC2H%2BYbiVUULM1IBHP%2FJolSzRV8HDKds1loSNDBN8a4%2FFrfzrjwOL4x9zdWnO2cbRQp4DJ6vgIC%2B6mqFykV686nxL0TX0LYkXCG%2FiwZnYQu3NY1magFex0wlZwOhUsiuTli79Ngtrus17IepgVl%2FWtKSWAJ8%2B8xYAa%2BkowfFrp%2BScV0%2Fk%2Bz%2B61pzOIIdWkpnpJCjD%2FlLDIBjqkAc5VyqNZX3lWmqmg66g3bnOdQ2yspEgil%2B209S6IWfaLnsCV5G0qMCY8RJ9yEdYX6szI0SLPx5QTIYa4dSwq4fHdMXfjkxGH6GcIpWz3s2NxR9hjUCQq30QVWX%2FC89YFnW%2Bg0NXiB3Uc9p9cqX%2BBR%2Ba8vRQgognqI4bt9QsWDZ3cM15sRmCIO7pSVZOafyuz3rtD%2BxLn9SGBxO0cDjSmnE94Cgno&X-Amz-Signature=429c368e629a9f429eddfaf3512e40ee068f1b921469ab59350a3aef3e030143&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJXSE6ZB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrjAynKu1l8bhxo1OmPdemTs5m80UC9ESXY44Cpzm9ngIhAP299XXWvi9NinTKAFvvtRdbb6TYP6BusN%2FmM0laZYmSKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBJ8blFVzId6lSPeYq3AOgydEj%2F0fw5ISgEtqEeTO2tHCszWRKqq%2F4xP7xDB3QbksNwm1q4yA0My6tSLl5vRA7cRiAkGrxdHteRYEWxKbYsYHtFSMnC6Ro3OS3xZrJOADkzX0I9RZnp5VKX0PunPEKMWw99e1uwsbGGoAddmTydTlGYU2O%2FnxiyqQU6ieQ4lcAg0bLZQ49rjHXODBKqbrGNRkev9XosZZ1dP2Kdw2gPzkwSDOKmv69uEKWCStxsQlkDx%2Fu8LnT7PmkcArXJzQ1qNAkr4Insjph1%2FEQkqim4m5Pz5Lp2wRO2WKjSu4Fs%2BJNSy99YrCn4WW5KSiKogU9nVuyRxLgJaaHIZHhINkweTeTqSYnrdeYL71eK4zsnVp3DnT6d0K3YFzYkpiZEgTiJzS81%2Bngy2E%2BYsk%2B%2FVLvXISzLr2VponkQiBkiwPezG1vg9nmOz%2Bk6bSC2H%2BYbiVUULM1IBHP%2FJolSzRV8HDKds1loSNDBN8a4%2FFrfzrjwOL4x9zdWnO2cbRQp4DJ6vgIC%2B6mqFykV686nxL0TX0LYkXCG%2FiwZnYQu3NY1magFex0wlZwOhUsiuTli79Ngtrus17IepgVl%2FWtKSWAJ8%2B8xYAa%2BkowfFrp%2BScV0%2Fk%2Bz%2B61pzOIIdWkpnpJCjD%2FlLDIBjqkAc5VyqNZX3lWmqmg66g3bnOdQ2yspEgil%2B209S6IWfaLnsCV5G0qMCY8RJ9yEdYX6szI0SLPx5QTIYa4dSwq4fHdMXfjkxGH6GcIpWz3s2NxR9hjUCQq30QVWX%2FC89YFnW%2Bg0NXiB3Uc9p9cqX%2BBR%2Ba8vRQgognqI4bt9QsWDZ3cM15sRmCIO7pSVZOafyuz3rtD%2BxLn9SGBxO0cDjSmnE94Cgno&X-Amz-Signature=1ff534fd2cb203f0134f5595c55b5cf18ce716b6d25501bba95a3d2167a429ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJXSE6ZB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrjAynKu1l8bhxo1OmPdemTs5m80UC9ESXY44Cpzm9ngIhAP299XXWvi9NinTKAFvvtRdbb6TYP6BusN%2FmM0laZYmSKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBJ8blFVzId6lSPeYq3AOgydEj%2F0fw5ISgEtqEeTO2tHCszWRKqq%2F4xP7xDB3QbksNwm1q4yA0My6tSLl5vRA7cRiAkGrxdHteRYEWxKbYsYHtFSMnC6Ro3OS3xZrJOADkzX0I9RZnp5VKX0PunPEKMWw99e1uwsbGGoAddmTydTlGYU2O%2FnxiyqQU6ieQ4lcAg0bLZQ49rjHXODBKqbrGNRkev9XosZZ1dP2Kdw2gPzkwSDOKmv69uEKWCStxsQlkDx%2Fu8LnT7PmkcArXJzQ1qNAkr4Insjph1%2FEQkqim4m5Pz5Lp2wRO2WKjSu4Fs%2BJNSy99YrCn4WW5KSiKogU9nVuyRxLgJaaHIZHhINkweTeTqSYnrdeYL71eK4zsnVp3DnT6d0K3YFzYkpiZEgTiJzS81%2Bngy2E%2BYsk%2B%2FVLvXISzLr2VponkQiBkiwPezG1vg9nmOz%2Bk6bSC2H%2BYbiVUULM1IBHP%2FJolSzRV8HDKds1loSNDBN8a4%2FFrfzrjwOL4x9zdWnO2cbRQp4DJ6vgIC%2B6mqFykV686nxL0TX0LYkXCG%2FiwZnYQu3NY1magFex0wlZwOhUsiuTli79Ngtrus17IepgVl%2FWtKSWAJ8%2B8xYAa%2BkowfFrp%2BScV0%2Fk%2Bz%2B61pzOIIdWkpnpJCjD%2FlLDIBjqkAc5VyqNZX3lWmqmg66g3bnOdQ2yspEgil%2B209S6IWfaLnsCV5G0qMCY8RJ9yEdYX6szI0SLPx5QTIYa4dSwq4fHdMXfjkxGH6GcIpWz3s2NxR9hjUCQq30QVWX%2FC89YFnW%2Bg0NXiB3Uc9p9cqX%2BBR%2Ba8vRQgognqI4bt9QsWDZ3cM15sRmCIO7pSVZOafyuz3rtD%2BxLn9SGBxO0cDjSmnE94Cgno&X-Amz-Signature=879c8caba18863a70d2d0e72204e54c9f6c75d1c70b009e1c0847754055ff4a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJXSE6ZB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrjAynKu1l8bhxo1OmPdemTs5m80UC9ESXY44Cpzm9ngIhAP299XXWvi9NinTKAFvvtRdbb6TYP6BusN%2FmM0laZYmSKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBJ8blFVzId6lSPeYq3AOgydEj%2F0fw5ISgEtqEeTO2tHCszWRKqq%2F4xP7xDB3QbksNwm1q4yA0My6tSLl5vRA7cRiAkGrxdHteRYEWxKbYsYHtFSMnC6Ro3OS3xZrJOADkzX0I9RZnp5VKX0PunPEKMWw99e1uwsbGGoAddmTydTlGYU2O%2FnxiyqQU6ieQ4lcAg0bLZQ49rjHXODBKqbrGNRkev9XosZZ1dP2Kdw2gPzkwSDOKmv69uEKWCStxsQlkDx%2Fu8LnT7PmkcArXJzQ1qNAkr4Insjph1%2FEQkqim4m5Pz5Lp2wRO2WKjSu4Fs%2BJNSy99YrCn4WW5KSiKogU9nVuyRxLgJaaHIZHhINkweTeTqSYnrdeYL71eK4zsnVp3DnT6d0K3YFzYkpiZEgTiJzS81%2Bngy2E%2BYsk%2B%2FVLvXISzLr2VponkQiBkiwPezG1vg9nmOz%2Bk6bSC2H%2BYbiVUULM1IBHP%2FJolSzRV8HDKds1loSNDBN8a4%2FFrfzrjwOL4x9zdWnO2cbRQp4DJ6vgIC%2B6mqFykV686nxL0TX0LYkXCG%2FiwZnYQu3NY1magFex0wlZwOhUsiuTli79Ngtrus17IepgVl%2FWtKSWAJ8%2B8xYAa%2BkowfFrp%2BScV0%2Fk%2Bz%2B61pzOIIdWkpnpJCjD%2FlLDIBjqkAc5VyqNZX3lWmqmg66g3bnOdQ2yspEgil%2B209S6IWfaLnsCV5G0qMCY8RJ9yEdYX6szI0SLPx5QTIYa4dSwq4fHdMXfjkxGH6GcIpWz3s2NxR9hjUCQq30QVWX%2FC89YFnW%2Bg0NXiB3Uc9p9cqX%2BBR%2Ba8vRQgognqI4bt9QsWDZ3cM15sRmCIO7pSVZOafyuz3rtD%2BxLn9SGBxO0cDjSmnE94Cgno&X-Amz-Signature=0af207bd33de9d3d66baaaadd6c43ab5ac074caff5761cd634a4ed360a31e67e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJXSE6ZB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrjAynKu1l8bhxo1OmPdemTs5m80UC9ESXY44Cpzm9ngIhAP299XXWvi9NinTKAFvvtRdbb6TYP6BusN%2FmM0laZYmSKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBJ8blFVzId6lSPeYq3AOgydEj%2F0fw5ISgEtqEeTO2tHCszWRKqq%2F4xP7xDB3QbksNwm1q4yA0My6tSLl5vRA7cRiAkGrxdHteRYEWxKbYsYHtFSMnC6Ro3OS3xZrJOADkzX0I9RZnp5VKX0PunPEKMWw99e1uwsbGGoAddmTydTlGYU2O%2FnxiyqQU6ieQ4lcAg0bLZQ49rjHXODBKqbrGNRkev9XosZZ1dP2Kdw2gPzkwSDOKmv69uEKWCStxsQlkDx%2Fu8LnT7PmkcArXJzQ1qNAkr4Insjph1%2FEQkqim4m5Pz5Lp2wRO2WKjSu4Fs%2BJNSy99YrCn4WW5KSiKogU9nVuyRxLgJaaHIZHhINkweTeTqSYnrdeYL71eK4zsnVp3DnT6d0K3YFzYkpiZEgTiJzS81%2Bngy2E%2BYsk%2B%2FVLvXISzLr2VponkQiBkiwPezG1vg9nmOz%2Bk6bSC2H%2BYbiVUULM1IBHP%2FJolSzRV8HDKds1loSNDBN8a4%2FFrfzrjwOL4x9zdWnO2cbRQp4DJ6vgIC%2B6mqFykV686nxL0TX0LYkXCG%2FiwZnYQu3NY1magFex0wlZwOhUsiuTli79Ngtrus17IepgVl%2FWtKSWAJ8%2B8xYAa%2BkowfFrp%2BScV0%2Fk%2Bz%2B61pzOIIdWkpnpJCjD%2FlLDIBjqkAc5VyqNZX3lWmqmg66g3bnOdQ2yspEgil%2B209S6IWfaLnsCV5G0qMCY8RJ9yEdYX6szI0SLPx5QTIYa4dSwq4fHdMXfjkxGH6GcIpWz3s2NxR9hjUCQq30QVWX%2FC89YFnW%2Bg0NXiB3Uc9p9cqX%2BBR%2Ba8vRQgognqI4bt9QsWDZ3cM15sRmCIO7pSVZOafyuz3rtD%2BxLn9SGBxO0cDjSmnE94Cgno&X-Amz-Signature=7b1bab719b3ba8bee1058f2a56f44f383c7bca1dd989bef9fc506dc6d97c3129&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJXSE6ZB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrjAynKu1l8bhxo1OmPdemTs5m80UC9ESXY44Cpzm9ngIhAP299XXWvi9NinTKAFvvtRdbb6TYP6BusN%2FmM0laZYmSKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBJ8blFVzId6lSPeYq3AOgydEj%2F0fw5ISgEtqEeTO2tHCszWRKqq%2F4xP7xDB3QbksNwm1q4yA0My6tSLl5vRA7cRiAkGrxdHteRYEWxKbYsYHtFSMnC6Ro3OS3xZrJOADkzX0I9RZnp5VKX0PunPEKMWw99e1uwsbGGoAddmTydTlGYU2O%2FnxiyqQU6ieQ4lcAg0bLZQ49rjHXODBKqbrGNRkev9XosZZ1dP2Kdw2gPzkwSDOKmv69uEKWCStxsQlkDx%2Fu8LnT7PmkcArXJzQ1qNAkr4Insjph1%2FEQkqim4m5Pz5Lp2wRO2WKjSu4Fs%2BJNSy99YrCn4WW5KSiKogU9nVuyRxLgJaaHIZHhINkweTeTqSYnrdeYL71eK4zsnVp3DnT6d0K3YFzYkpiZEgTiJzS81%2Bngy2E%2BYsk%2B%2FVLvXISzLr2VponkQiBkiwPezG1vg9nmOz%2Bk6bSC2H%2BYbiVUULM1IBHP%2FJolSzRV8HDKds1loSNDBN8a4%2FFrfzrjwOL4x9zdWnO2cbRQp4DJ6vgIC%2B6mqFykV686nxL0TX0LYkXCG%2FiwZnYQu3NY1magFex0wlZwOhUsiuTli79Ngtrus17IepgVl%2FWtKSWAJ8%2B8xYAa%2BkowfFrp%2BScV0%2Fk%2Bz%2B61pzOIIdWkpnpJCjD%2FlLDIBjqkAc5VyqNZX3lWmqmg66g3bnOdQ2yspEgil%2B209S6IWfaLnsCV5G0qMCY8RJ9yEdYX6szI0SLPx5QTIYa4dSwq4fHdMXfjkxGH6GcIpWz3s2NxR9hjUCQq30QVWX%2FC89YFnW%2Bg0NXiB3Uc9p9cqX%2BBR%2Ba8vRQgognqI4bt9QsWDZ3cM15sRmCIO7pSVZOafyuz3rtD%2BxLn9SGBxO0cDjSmnE94Cgno&X-Amz-Signature=d18527f71e7a101eeebc75c23d3ada8429b87dee83cb4c347f38b6ae7e577171&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJXSE6ZB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrjAynKu1l8bhxo1OmPdemTs5m80UC9ESXY44Cpzm9ngIhAP299XXWvi9NinTKAFvvtRdbb6TYP6BusN%2FmM0laZYmSKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBJ8blFVzId6lSPeYq3AOgydEj%2F0fw5ISgEtqEeTO2tHCszWRKqq%2F4xP7xDB3QbksNwm1q4yA0My6tSLl5vRA7cRiAkGrxdHteRYEWxKbYsYHtFSMnC6Ro3OS3xZrJOADkzX0I9RZnp5VKX0PunPEKMWw99e1uwsbGGoAddmTydTlGYU2O%2FnxiyqQU6ieQ4lcAg0bLZQ49rjHXODBKqbrGNRkev9XosZZ1dP2Kdw2gPzkwSDOKmv69uEKWCStxsQlkDx%2Fu8LnT7PmkcArXJzQ1qNAkr4Insjph1%2FEQkqim4m5Pz5Lp2wRO2WKjSu4Fs%2BJNSy99YrCn4WW5KSiKogU9nVuyRxLgJaaHIZHhINkweTeTqSYnrdeYL71eK4zsnVp3DnT6d0K3YFzYkpiZEgTiJzS81%2Bngy2E%2BYsk%2B%2FVLvXISzLr2VponkQiBkiwPezG1vg9nmOz%2Bk6bSC2H%2BYbiVUULM1IBHP%2FJolSzRV8HDKds1loSNDBN8a4%2FFrfzrjwOL4x9zdWnO2cbRQp4DJ6vgIC%2B6mqFykV686nxL0TX0LYkXCG%2FiwZnYQu3NY1magFex0wlZwOhUsiuTli79Ngtrus17IepgVl%2FWtKSWAJ8%2B8xYAa%2BkowfFrp%2BScV0%2Fk%2Bz%2B61pzOIIdWkpnpJCjD%2FlLDIBjqkAc5VyqNZX3lWmqmg66g3bnOdQ2yspEgil%2B209S6IWfaLnsCV5G0qMCY8RJ9yEdYX6szI0SLPx5QTIYa4dSwq4fHdMXfjkxGH6GcIpWz3s2NxR9hjUCQq30QVWX%2FC89YFnW%2Bg0NXiB3Uc9p9cqX%2BBR%2Ba8vRQgognqI4bt9QsWDZ3cM15sRmCIO7pSVZOafyuz3rtD%2BxLn9SGBxO0cDjSmnE94Cgno&X-Amz-Signature=0b2fee8a2302880d691090c99c667b2b09b576ba1b98e3740f5368b620928ae1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJXSE6ZB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrjAynKu1l8bhxo1OmPdemTs5m80UC9ESXY44Cpzm9ngIhAP299XXWvi9NinTKAFvvtRdbb6TYP6BusN%2FmM0laZYmSKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBJ8blFVzId6lSPeYq3AOgydEj%2F0fw5ISgEtqEeTO2tHCszWRKqq%2F4xP7xDB3QbksNwm1q4yA0My6tSLl5vRA7cRiAkGrxdHteRYEWxKbYsYHtFSMnC6Ro3OS3xZrJOADkzX0I9RZnp5VKX0PunPEKMWw99e1uwsbGGoAddmTydTlGYU2O%2FnxiyqQU6ieQ4lcAg0bLZQ49rjHXODBKqbrGNRkev9XosZZ1dP2Kdw2gPzkwSDOKmv69uEKWCStxsQlkDx%2Fu8LnT7PmkcArXJzQ1qNAkr4Insjph1%2FEQkqim4m5Pz5Lp2wRO2WKjSu4Fs%2BJNSy99YrCn4WW5KSiKogU9nVuyRxLgJaaHIZHhINkweTeTqSYnrdeYL71eK4zsnVp3DnT6d0K3YFzYkpiZEgTiJzS81%2Bngy2E%2BYsk%2B%2FVLvXISzLr2VponkQiBkiwPezG1vg9nmOz%2Bk6bSC2H%2BYbiVUULM1IBHP%2FJolSzRV8HDKds1loSNDBN8a4%2FFrfzrjwOL4x9zdWnO2cbRQp4DJ6vgIC%2B6mqFykV686nxL0TX0LYkXCG%2FiwZnYQu3NY1magFex0wlZwOhUsiuTli79Ngtrus17IepgVl%2FWtKSWAJ8%2B8xYAa%2BkowfFrp%2BScV0%2Fk%2Bz%2B61pzOIIdWkpnpJCjD%2FlLDIBjqkAc5VyqNZX3lWmqmg66g3bnOdQ2yspEgil%2B209S6IWfaLnsCV5G0qMCY8RJ9yEdYX6szI0SLPx5QTIYa4dSwq4fHdMXfjkxGH6GcIpWz3s2NxR9hjUCQq30QVWX%2FC89YFnW%2Bg0NXiB3Uc9p9cqX%2BBR%2Ba8vRQgognqI4bt9QsWDZ3cM15sRmCIO7pSVZOafyuz3rtD%2BxLn9SGBxO0cDjSmnE94Cgno&X-Amz-Signature=949762f8445838a689af07bd811310a725480cc9260fb4f04fc0e469bee10b44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

