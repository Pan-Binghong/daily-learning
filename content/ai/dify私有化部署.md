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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGETWKZD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8ztR9nm4X%2FjXgQdfLJl9O%2BDtDZw4UOeO7V0ju9OPcAAiEArwm9SyufkhK%2Fg4S6nPGq6cOWv%2BJceuHoHviuYIMq0zcq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDEDaQuGRpOU0TPPfHircA7IYcIkGvbOo%2F1Lof9l2RzKipnHM2AA8i%2F0pruEz9WIrqrlpCUmXYtTF%2FBzzAjkFB%2BEs5KsxYcCj5es7xobXcbFm2XVddjIn5kLA3J8mg31QWbFiMfxLZWMow0LrTupWXGuM2h0w%2BSTZvkKO09n8F1gIG8Lag0DS%2FDlPl27C%2B9Lpwdo4UDTgx3py%2FSIr45TUpx7oGy9KOsHQA53dXZuhv8ZKmT0p3BmZVi7ACYiDxQ1hdbLe344O6ciLpZFpLYPFR16%2FrvpYFuLmxgKi88WvHZTyJ92K6USP9Yhn%2Bx6nkWP80cSy6ZgjepciImQnh%2FVE2sBkMsfpZt7qifs62IGdNcyORNuYlepASmYyclk132FPwfFessn10OnhNTgwZIyyTzrj1TK7BPGemxGwXb9Tc%2F26yhrBUDhkSPdrecrBNoNdLfjiHdLBhlbIx%2FB3e%2F0reIlGP4tLj0v5BPXTB6MvicUc5y6OzjySlh12fARAO0%2FOAfwADdbbaoNnrVHg%2F%2B4lGcj%2F5x%2FKt0c0pChtDikmZjhCTjn5rhJQ6GYGqfBQwTtjocW5edTg0mOOm84xR8nb9qXnWgnlrhABKc%2B3dHJ52b5dxaod32tTgyDcMaS2aAwgizUPi5pp3Uz%2FpKW4MODA38gGOqUBAjkBlHkDSaMy%2BRnbsJbFBdyoJaBkg8jr%2FOQTgWWFv7WSIHsm2tLWpaENaHE0Xe6fuHbehBlVHRutR28f8yniA7n6uyaJEFepiEDGMBJQSC1AjM46jibAwGT0AGuM694c2StKnRaxU1YVLsuXoMi9bPwr%2FECZdX7kQEI3N%2FJYGcdDc3LqPYBp5Kpm2qDomWISj0IKtG%2BiQT0M4dtC8StnhXtzOzhE&X-Amz-Signature=36c6f03853cdb8175fe843f0a15d505cfa249b72cb27587250731d5781b39e95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGETWKZD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8ztR9nm4X%2FjXgQdfLJl9O%2BDtDZw4UOeO7V0ju9OPcAAiEArwm9SyufkhK%2Fg4S6nPGq6cOWv%2BJceuHoHviuYIMq0zcq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDEDaQuGRpOU0TPPfHircA7IYcIkGvbOo%2F1Lof9l2RzKipnHM2AA8i%2F0pruEz9WIrqrlpCUmXYtTF%2FBzzAjkFB%2BEs5KsxYcCj5es7xobXcbFm2XVddjIn5kLA3J8mg31QWbFiMfxLZWMow0LrTupWXGuM2h0w%2BSTZvkKO09n8F1gIG8Lag0DS%2FDlPl27C%2B9Lpwdo4UDTgx3py%2FSIr45TUpx7oGy9KOsHQA53dXZuhv8ZKmT0p3BmZVi7ACYiDxQ1hdbLe344O6ciLpZFpLYPFR16%2FrvpYFuLmxgKi88WvHZTyJ92K6USP9Yhn%2Bx6nkWP80cSy6ZgjepciImQnh%2FVE2sBkMsfpZt7qifs62IGdNcyORNuYlepASmYyclk132FPwfFessn10OnhNTgwZIyyTzrj1TK7BPGemxGwXb9Tc%2F26yhrBUDhkSPdrecrBNoNdLfjiHdLBhlbIx%2FB3e%2F0reIlGP4tLj0v5BPXTB6MvicUc5y6OzjySlh12fARAO0%2FOAfwADdbbaoNnrVHg%2F%2B4lGcj%2F5x%2FKt0c0pChtDikmZjhCTjn5rhJQ6GYGqfBQwTtjocW5edTg0mOOm84xR8nb9qXnWgnlrhABKc%2B3dHJ52b5dxaod32tTgyDcMaS2aAwgizUPi5pp3Uz%2FpKW4MODA38gGOqUBAjkBlHkDSaMy%2BRnbsJbFBdyoJaBkg8jr%2FOQTgWWFv7WSIHsm2tLWpaENaHE0Xe6fuHbehBlVHRutR28f8yniA7n6uyaJEFepiEDGMBJQSC1AjM46jibAwGT0AGuM694c2StKnRaxU1YVLsuXoMi9bPwr%2FECZdX7kQEI3N%2FJYGcdDc3LqPYBp5Kpm2qDomWISj0IKtG%2BiQT0M4dtC8StnhXtzOzhE&X-Amz-Signature=258614cfc38d42d9509f16a0a706debf12df74e1437e005951759db5d8866aba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGETWKZD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8ztR9nm4X%2FjXgQdfLJl9O%2BDtDZw4UOeO7V0ju9OPcAAiEArwm9SyufkhK%2Fg4S6nPGq6cOWv%2BJceuHoHviuYIMq0zcq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDEDaQuGRpOU0TPPfHircA7IYcIkGvbOo%2F1Lof9l2RzKipnHM2AA8i%2F0pruEz9WIrqrlpCUmXYtTF%2FBzzAjkFB%2BEs5KsxYcCj5es7xobXcbFm2XVddjIn5kLA3J8mg31QWbFiMfxLZWMow0LrTupWXGuM2h0w%2BSTZvkKO09n8F1gIG8Lag0DS%2FDlPl27C%2B9Lpwdo4UDTgx3py%2FSIr45TUpx7oGy9KOsHQA53dXZuhv8ZKmT0p3BmZVi7ACYiDxQ1hdbLe344O6ciLpZFpLYPFR16%2FrvpYFuLmxgKi88WvHZTyJ92K6USP9Yhn%2Bx6nkWP80cSy6ZgjepciImQnh%2FVE2sBkMsfpZt7qifs62IGdNcyORNuYlepASmYyclk132FPwfFessn10OnhNTgwZIyyTzrj1TK7BPGemxGwXb9Tc%2F26yhrBUDhkSPdrecrBNoNdLfjiHdLBhlbIx%2FB3e%2F0reIlGP4tLj0v5BPXTB6MvicUc5y6OzjySlh12fARAO0%2FOAfwADdbbaoNnrVHg%2F%2B4lGcj%2F5x%2FKt0c0pChtDikmZjhCTjn5rhJQ6GYGqfBQwTtjocW5edTg0mOOm84xR8nb9qXnWgnlrhABKc%2B3dHJ52b5dxaod32tTgyDcMaS2aAwgizUPi5pp3Uz%2FpKW4MODA38gGOqUBAjkBlHkDSaMy%2BRnbsJbFBdyoJaBkg8jr%2FOQTgWWFv7WSIHsm2tLWpaENaHE0Xe6fuHbehBlVHRutR28f8yniA7n6uyaJEFepiEDGMBJQSC1AjM46jibAwGT0AGuM694c2StKnRaxU1YVLsuXoMi9bPwr%2FECZdX7kQEI3N%2FJYGcdDc3LqPYBp5Kpm2qDomWISj0IKtG%2BiQT0M4dtC8StnhXtzOzhE&X-Amz-Signature=fec01f20c9e110dfc982a70e24fe3b3ecc35922cc668f85cffdf31402b1ea97a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGETWKZD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8ztR9nm4X%2FjXgQdfLJl9O%2BDtDZw4UOeO7V0ju9OPcAAiEArwm9SyufkhK%2Fg4S6nPGq6cOWv%2BJceuHoHviuYIMq0zcq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDEDaQuGRpOU0TPPfHircA7IYcIkGvbOo%2F1Lof9l2RzKipnHM2AA8i%2F0pruEz9WIrqrlpCUmXYtTF%2FBzzAjkFB%2BEs5KsxYcCj5es7xobXcbFm2XVddjIn5kLA3J8mg31QWbFiMfxLZWMow0LrTupWXGuM2h0w%2BSTZvkKO09n8F1gIG8Lag0DS%2FDlPl27C%2B9Lpwdo4UDTgx3py%2FSIr45TUpx7oGy9KOsHQA53dXZuhv8ZKmT0p3BmZVi7ACYiDxQ1hdbLe344O6ciLpZFpLYPFR16%2FrvpYFuLmxgKi88WvHZTyJ92K6USP9Yhn%2Bx6nkWP80cSy6ZgjepciImQnh%2FVE2sBkMsfpZt7qifs62IGdNcyORNuYlepASmYyclk132FPwfFessn10OnhNTgwZIyyTzrj1TK7BPGemxGwXb9Tc%2F26yhrBUDhkSPdrecrBNoNdLfjiHdLBhlbIx%2FB3e%2F0reIlGP4tLj0v5BPXTB6MvicUc5y6OzjySlh12fARAO0%2FOAfwADdbbaoNnrVHg%2F%2B4lGcj%2F5x%2FKt0c0pChtDikmZjhCTjn5rhJQ6GYGqfBQwTtjocW5edTg0mOOm84xR8nb9qXnWgnlrhABKc%2B3dHJ52b5dxaod32tTgyDcMaS2aAwgizUPi5pp3Uz%2FpKW4MODA38gGOqUBAjkBlHkDSaMy%2BRnbsJbFBdyoJaBkg8jr%2FOQTgWWFv7WSIHsm2tLWpaENaHE0Xe6fuHbehBlVHRutR28f8yniA7n6uyaJEFepiEDGMBJQSC1AjM46jibAwGT0AGuM694c2StKnRaxU1YVLsuXoMi9bPwr%2FECZdX7kQEI3N%2FJYGcdDc3LqPYBp5Kpm2qDomWISj0IKtG%2BiQT0M4dtC8StnhXtzOzhE&X-Amz-Signature=4322afda0d641e702942463c270060b69f744ce0f8e08cc807a34918a5b36825&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGETWKZD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8ztR9nm4X%2FjXgQdfLJl9O%2BDtDZw4UOeO7V0ju9OPcAAiEArwm9SyufkhK%2Fg4S6nPGq6cOWv%2BJceuHoHviuYIMq0zcq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDEDaQuGRpOU0TPPfHircA7IYcIkGvbOo%2F1Lof9l2RzKipnHM2AA8i%2F0pruEz9WIrqrlpCUmXYtTF%2FBzzAjkFB%2BEs5KsxYcCj5es7xobXcbFm2XVddjIn5kLA3J8mg31QWbFiMfxLZWMow0LrTupWXGuM2h0w%2BSTZvkKO09n8F1gIG8Lag0DS%2FDlPl27C%2B9Lpwdo4UDTgx3py%2FSIr45TUpx7oGy9KOsHQA53dXZuhv8ZKmT0p3BmZVi7ACYiDxQ1hdbLe344O6ciLpZFpLYPFR16%2FrvpYFuLmxgKi88WvHZTyJ92K6USP9Yhn%2Bx6nkWP80cSy6ZgjepciImQnh%2FVE2sBkMsfpZt7qifs62IGdNcyORNuYlepASmYyclk132FPwfFessn10OnhNTgwZIyyTzrj1TK7BPGemxGwXb9Tc%2F26yhrBUDhkSPdrecrBNoNdLfjiHdLBhlbIx%2FB3e%2F0reIlGP4tLj0v5BPXTB6MvicUc5y6OzjySlh12fARAO0%2FOAfwADdbbaoNnrVHg%2F%2B4lGcj%2F5x%2FKt0c0pChtDikmZjhCTjn5rhJQ6GYGqfBQwTtjocW5edTg0mOOm84xR8nb9qXnWgnlrhABKc%2B3dHJ52b5dxaod32tTgyDcMaS2aAwgizUPi5pp3Uz%2FpKW4MODA38gGOqUBAjkBlHkDSaMy%2BRnbsJbFBdyoJaBkg8jr%2FOQTgWWFv7WSIHsm2tLWpaENaHE0Xe6fuHbehBlVHRutR28f8yniA7n6uyaJEFepiEDGMBJQSC1AjM46jibAwGT0AGuM694c2StKnRaxU1YVLsuXoMi9bPwr%2FECZdX7kQEI3N%2FJYGcdDc3LqPYBp5Kpm2qDomWISj0IKtG%2BiQT0M4dtC8StnhXtzOzhE&X-Amz-Signature=0f8b37f626ee60cc974cbac465225f7dfd5a2b2c398578593ea4d8032c939fc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGETWKZD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8ztR9nm4X%2FjXgQdfLJl9O%2BDtDZw4UOeO7V0ju9OPcAAiEArwm9SyufkhK%2Fg4S6nPGq6cOWv%2BJceuHoHviuYIMq0zcq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDEDaQuGRpOU0TPPfHircA7IYcIkGvbOo%2F1Lof9l2RzKipnHM2AA8i%2F0pruEz9WIrqrlpCUmXYtTF%2FBzzAjkFB%2BEs5KsxYcCj5es7xobXcbFm2XVddjIn5kLA3J8mg31QWbFiMfxLZWMow0LrTupWXGuM2h0w%2BSTZvkKO09n8F1gIG8Lag0DS%2FDlPl27C%2B9Lpwdo4UDTgx3py%2FSIr45TUpx7oGy9KOsHQA53dXZuhv8ZKmT0p3BmZVi7ACYiDxQ1hdbLe344O6ciLpZFpLYPFR16%2FrvpYFuLmxgKi88WvHZTyJ92K6USP9Yhn%2Bx6nkWP80cSy6ZgjepciImQnh%2FVE2sBkMsfpZt7qifs62IGdNcyORNuYlepASmYyclk132FPwfFessn10OnhNTgwZIyyTzrj1TK7BPGemxGwXb9Tc%2F26yhrBUDhkSPdrecrBNoNdLfjiHdLBhlbIx%2FB3e%2F0reIlGP4tLj0v5BPXTB6MvicUc5y6OzjySlh12fARAO0%2FOAfwADdbbaoNnrVHg%2F%2B4lGcj%2F5x%2FKt0c0pChtDikmZjhCTjn5rhJQ6GYGqfBQwTtjocW5edTg0mOOm84xR8nb9qXnWgnlrhABKc%2B3dHJ52b5dxaod32tTgyDcMaS2aAwgizUPi5pp3Uz%2FpKW4MODA38gGOqUBAjkBlHkDSaMy%2BRnbsJbFBdyoJaBkg8jr%2FOQTgWWFv7WSIHsm2tLWpaENaHE0Xe6fuHbehBlVHRutR28f8yniA7n6uyaJEFepiEDGMBJQSC1AjM46jibAwGT0AGuM694c2StKnRaxU1YVLsuXoMi9bPwr%2FECZdX7kQEI3N%2FJYGcdDc3LqPYBp5Kpm2qDomWISj0IKtG%2BiQT0M4dtC8StnhXtzOzhE&X-Amz-Signature=10f1c093258d2e3daa434101c4201387b335a16167e9b565d61118118bbd9099&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGETWKZD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8ztR9nm4X%2FjXgQdfLJl9O%2BDtDZw4UOeO7V0ju9OPcAAiEArwm9SyufkhK%2Fg4S6nPGq6cOWv%2BJceuHoHviuYIMq0zcq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDEDaQuGRpOU0TPPfHircA7IYcIkGvbOo%2F1Lof9l2RzKipnHM2AA8i%2F0pruEz9WIrqrlpCUmXYtTF%2FBzzAjkFB%2BEs5KsxYcCj5es7xobXcbFm2XVddjIn5kLA3J8mg31QWbFiMfxLZWMow0LrTupWXGuM2h0w%2BSTZvkKO09n8F1gIG8Lag0DS%2FDlPl27C%2B9Lpwdo4UDTgx3py%2FSIr45TUpx7oGy9KOsHQA53dXZuhv8ZKmT0p3BmZVi7ACYiDxQ1hdbLe344O6ciLpZFpLYPFR16%2FrvpYFuLmxgKi88WvHZTyJ92K6USP9Yhn%2Bx6nkWP80cSy6ZgjepciImQnh%2FVE2sBkMsfpZt7qifs62IGdNcyORNuYlepASmYyclk132FPwfFessn10OnhNTgwZIyyTzrj1TK7BPGemxGwXb9Tc%2F26yhrBUDhkSPdrecrBNoNdLfjiHdLBhlbIx%2FB3e%2F0reIlGP4tLj0v5BPXTB6MvicUc5y6OzjySlh12fARAO0%2FOAfwADdbbaoNnrVHg%2F%2B4lGcj%2F5x%2FKt0c0pChtDikmZjhCTjn5rhJQ6GYGqfBQwTtjocW5edTg0mOOm84xR8nb9qXnWgnlrhABKc%2B3dHJ52b5dxaod32tTgyDcMaS2aAwgizUPi5pp3Uz%2FpKW4MODA38gGOqUBAjkBlHkDSaMy%2BRnbsJbFBdyoJaBkg8jr%2FOQTgWWFv7WSIHsm2tLWpaENaHE0Xe6fuHbehBlVHRutR28f8yniA7n6uyaJEFepiEDGMBJQSC1AjM46jibAwGT0AGuM694c2StKnRaxU1YVLsuXoMi9bPwr%2FECZdX7kQEI3N%2FJYGcdDc3LqPYBp5Kpm2qDomWISj0IKtG%2BiQT0M4dtC8StnhXtzOzhE&X-Amz-Signature=d2812575010bd4e8ac25d8a660be7510784080aa058b2d192fd55b718ceb2a7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGETWKZD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8ztR9nm4X%2FjXgQdfLJl9O%2BDtDZw4UOeO7V0ju9OPcAAiEArwm9SyufkhK%2Fg4S6nPGq6cOWv%2BJceuHoHviuYIMq0zcq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDEDaQuGRpOU0TPPfHircA7IYcIkGvbOo%2F1Lof9l2RzKipnHM2AA8i%2F0pruEz9WIrqrlpCUmXYtTF%2FBzzAjkFB%2BEs5KsxYcCj5es7xobXcbFm2XVddjIn5kLA3J8mg31QWbFiMfxLZWMow0LrTupWXGuM2h0w%2BSTZvkKO09n8F1gIG8Lag0DS%2FDlPl27C%2B9Lpwdo4UDTgx3py%2FSIr45TUpx7oGy9KOsHQA53dXZuhv8ZKmT0p3BmZVi7ACYiDxQ1hdbLe344O6ciLpZFpLYPFR16%2FrvpYFuLmxgKi88WvHZTyJ92K6USP9Yhn%2Bx6nkWP80cSy6ZgjepciImQnh%2FVE2sBkMsfpZt7qifs62IGdNcyORNuYlepASmYyclk132FPwfFessn10OnhNTgwZIyyTzrj1TK7BPGemxGwXb9Tc%2F26yhrBUDhkSPdrecrBNoNdLfjiHdLBhlbIx%2FB3e%2F0reIlGP4tLj0v5BPXTB6MvicUc5y6OzjySlh12fARAO0%2FOAfwADdbbaoNnrVHg%2F%2B4lGcj%2F5x%2FKt0c0pChtDikmZjhCTjn5rhJQ6GYGqfBQwTtjocW5edTg0mOOm84xR8nb9qXnWgnlrhABKc%2B3dHJ52b5dxaod32tTgyDcMaS2aAwgizUPi5pp3Uz%2FpKW4MODA38gGOqUBAjkBlHkDSaMy%2BRnbsJbFBdyoJaBkg8jr%2FOQTgWWFv7WSIHsm2tLWpaENaHE0Xe6fuHbehBlVHRutR28f8yniA7n6uyaJEFepiEDGMBJQSC1AjM46jibAwGT0AGuM694c2StKnRaxU1YVLsuXoMi9bPwr%2FECZdX7kQEI3N%2FJYGcdDc3LqPYBp5Kpm2qDomWISj0IKtG%2BiQT0M4dtC8StnhXtzOzhE&X-Amz-Signature=37bbf9070acf62c251400fd928e06639ad619c15a5ebec79ee5521b9c425db44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGETWKZD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8ztR9nm4X%2FjXgQdfLJl9O%2BDtDZw4UOeO7V0ju9OPcAAiEArwm9SyufkhK%2Fg4S6nPGq6cOWv%2BJceuHoHviuYIMq0zcq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDEDaQuGRpOU0TPPfHircA7IYcIkGvbOo%2F1Lof9l2RzKipnHM2AA8i%2F0pruEz9WIrqrlpCUmXYtTF%2FBzzAjkFB%2BEs5KsxYcCj5es7xobXcbFm2XVddjIn5kLA3J8mg31QWbFiMfxLZWMow0LrTupWXGuM2h0w%2BSTZvkKO09n8F1gIG8Lag0DS%2FDlPl27C%2B9Lpwdo4UDTgx3py%2FSIr45TUpx7oGy9KOsHQA53dXZuhv8ZKmT0p3BmZVi7ACYiDxQ1hdbLe344O6ciLpZFpLYPFR16%2FrvpYFuLmxgKi88WvHZTyJ92K6USP9Yhn%2Bx6nkWP80cSy6ZgjepciImQnh%2FVE2sBkMsfpZt7qifs62IGdNcyORNuYlepASmYyclk132FPwfFessn10OnhNTgwZIyyTzrj1TK7BPGemxGwXb9Tc%2F26yhrBUDhkSPdrecrBNoNdLfjiHdLBhlbIx%2FB3e%2F0reIlGP4tLj0v5BPXTB6MvicUc5y6OzjySlh12fARAO0%2FOAfwADdbbaoNnrVHg%2F%2B4lGcj%2F5x%2FKt0c0pChtDikmZjhCTjn5rhJQ6GYGqfBQwTtjocW5edTg0mOOm84xR8nb9qXnWgnlrhABKc%2B3dHJ52b5dxaod32tTgyDcMaS2aAwgizUPi5pp3Uz%2FpKW4MODA38gGOqUBAjkBlHkDSaMy%2BRnbsJbFBdyoJaBkg8jr%2FOQTgWWFv7WSIHsm2tLWpaENaHE0Xe6fuHbehBlVHRutR28f8yniA7n6uyaJEFepiEDGMBJQSC1AjM46jibAwGT0AGuM694c2StKnRaxU1YVLsuXoMi9bPwr%2FECZdX7kQEI3N%2FJYGcdDc3LqPYBp5Kpm2qDomWISj0IKtG%2BiQT0M4dtC8StnhXtzOzhE&X-Amz-Signature=d65bc1cf56ed660b6c7b06c8219b45f941675aa411db87f72fc75c4882f27665&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGETWKZD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8ztR9nm4X%2FjXgQdfLJl9O%2BDtDZw4UOeO7V0ju9OPcAAiEArwm9SyufkhK%2Fg4S6nPGq6cOWv%2BJceuHoHviuYIMq0zcq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDEDaQuGRpOU0TPPfHircA7IYcIkGvbOo%2F1Lof9l2RzKipnHM2AA8i%2F0pruEz9WIrqrlpCUmXYtTF%2FBzzAjkFB%2BEs5KsxYcCj5es7xobXcbFm2XVddjIn5kLA3J8mg31QWbFiMfxLZWMow0LrTupWXGuM2h0w%2BSTZvkKO09n8F1gIG8Lag0DS%2FDlPl27C%2B9Lpwdo4UDTgx3py%2FSIr45TUpx7oGy9KOsHQA53dXZuhv8ZKmT0p3BmZVi7ACYiDxQ1hdbLe344O6ciLpZFpLYPFR16%2FrvpYFuLmxgKi88WvHZTyJ92K6USP9Yhn%2Bx6nkWP80cSy6ZgjepciImQnh%2FVE2sBkMsfpZt7qifs62IGdNcyORNuYlepASmYyclk132FPwfFessn10OnhNTgwZIyyTzrj1TK7BPGemxGwXb9Tc%2F26yhrBUDhkSPdrecrBNoNdLfjiHdLBhlbIx%2FB3e%2F0reIlGP4tLj0v5BPXTB6MvicUc5y6OzjySlh12fARAO0%2FOAfwADdbbaoNnrVHg%2F%2B4lGcj%2F5x%2FKt0c0pChtDikmZjhCTjn5rhJQ6GYGqfBQwTtjocW5edTg0mOOm84xR8nb9qXnWgnlrhABKc%2B3dHJ52b5dxaod32tTgyDcMaS2aAwgizUPi5pp3Uz%2FpKW4MODA38gGOqUBAjkBlHkDSaMy%2BRnbsJbFBdyoJaBkg8jr%2FOQTgWWFv7WSIHsm2tLWpaENaHE0Xe6fuHbehBlVHRutR28f8yniA7n6uyaJEFepiEDGMBJQSC1AjM46jibAwGT0AGuM694c2StKnRaxU1YVLsuXoMi9bPwr%2FECZdX7kQEI3N%2FJYGcdDc3LqPYBp5Kpm2qDomWISj0IKtG%2BiQT0M4dtC8StnhXtzOzhE&X-Amz-Signature=4fb0800213ff47fdc04cce88b1f76c9b21b0a801599389289bd072174baf09f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

