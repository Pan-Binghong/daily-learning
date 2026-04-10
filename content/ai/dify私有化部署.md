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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFBKV5ES%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICHQXv75YVcS3OAw5rdKpUmQ9I3qyBGPk2qXwnswMQQsAiEAwspvVNgaHH8DP8F0BsQP8sqUHCo2l8hwq0s1NGdm4LUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNsWdf1D%2B9MaExsYxSrcA0Cct5jo%2BYr1MZw95fouPSD%2B23JzhUFqNvgI4mu0RKZ0e%2FoF%2BNAmeKHVR6fu0VrOdQEqlmb%2FPiP%2BNXEjBPqR7CSp8uZcuXGjVS%2BhFwzItbWr15XKlDNSKzMlnKvsHgf%2Bl%2Bh7BLxnqloNzBm9fid0nZgJhn6WYQsoW4IWyEn%2FZL0X6eK8TKJ9xWrLzLWuj%2BNccm26bJ1r%2FxWosqHnb4iTd2xcFnublYmO%2BtSFeX75r8ZH7vMeaqWV3IGoV8%2Bj1lSwE9FC%2FVnQJjqRoTwqIymtZGbCW1CFYiTOrT8jV9Mbyi6rBk6Wx9miy9E2qkqnnMfvbWDPCXtDiXXaWLv%2FCpy2tq56LvUYCofxOnBLSOSiGqX1jYNE2J%2F6Kc%2FG5pDiUnHui99HqLT3NtOuOOuvXRiz4Xu13u6j%2FEfB2h08BkAl5IyD0DvXoAWnImAfLbZR0%2FxhKWmvCFAUV21xnQaWEgRlG8EPmv6pThAIyFfwT57l2kr5%2FUD5Rlc5NUBUBspsAzerG4oZC575Z1hK2f5cKmdSBkrmCTeQw1Gslwhv7ZZK6l%2Bt8ebYTEr641DcJ75x1IRSZSLHntLjy%2Fawg86%2Bw8y6qlx8TXzgyLqCNfpjQUYIpc4gnHTIvYLDVHs3VHoqMKLH4c4GOqUBU3eer4hkeRdjUyi%2FhGkAh8N%2Fxio41BlwIlC%2FSvnYoMzAUgXJ2Q7aWuZOIc5gtbVmACZdRj%2BEkC3URmNxowqw0oEM9jht%2FGio9ZKMf321jSHBoeVS95wkqn7So%2BmPNGsD%2F1PjafUS0czgYdz1bvjOH2DnoY1d6ZY2mmHhKIsps7xCqNpKs0V0S2aXHBNkinCCP2ACpxFpQ945YveCQ9CrRKCQUbpz&X-Amz-Signature=a159e1cd867c39aa41931b79db203d055c395a2b001ce63b0180cda2d4839983&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFBKV5ES%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICHQXv75YVcS3OAw5rdKpUmQ9I3qyBGPk2qXwnswMQQsAiEAwspvVNgaHH8DP8F0BsQP8sqUHCo2l8hwq0s1NGdm4LUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNsWdf1D%2B9MaExsYxSrcA0Cct5jo%2BYr1MZw95fouPSD%2B23JzhUFqNvgI4mu0RKZ0e%2FoF%2BNAmeKHVR6fu0VrOdQEqlmb%2FPiP%2BNXEjBPqR7CSp8uZcuXGjVS%2BhFwzItbWr15XKlDNSKzMlnKvsHgf%2Bl%2Bh7BLxnqloNzBm9fid0nZgJhn6WYQsoW4IWyEn%2FZL0X6eK8TKJ9xWrLzLWuj%2BNccm26bJ1r%2FxWosqHnb4iTd2xcFnublYmO%2BtSFeX75r8ZH7vMeaqWV3IGoV8%2Bj1lSwE9FC%2FVnQJjqRoTwqIymtZGbCW1CFYiTOrT8jV9Mbyi6rBk6Wx9miy9E2qkqnnMfvbWDPCXtDiXXaWLv%2FCpy2tq56LvUYCofxOnBLSOSiGqX1jYNE2J%2F6Kc%2FG5pDiUnHui99HqLT3NtOuOOuvXRiz4Xu13u6j%2FEfB2h08BkAl5IyD0DvXoAWnImAfLbZR0%2FxhKWmvCFAUV21xnQaWEgRlG8EPmv6pThAIyFfwT57l2kr5%2FUD5Rlc5NUBUBspsAzerG4oZC575Z1hK2f5cKmdSBkrmCTeQw1Gslwhv7ZZK6l%2Bt8ebYTEr641DcJ75x1IRSZSLHntLjy%2Fawg86%2Bw8y6qlx8TXzgyLqCNfpjQUYIpc4gnHTIvYLDVHs3VHoqMKLH4c4GOqUBU3eer4hkeRdjUyi%2FhGkAh8N%2Fxio41BlwIlC%2FSvnYoMzAUgXJ2Q7aWuZOIc5gtbVmACZdRj%2BEkC3URmNxowqw0oEM9jht%2FGio9ZKMf321jSHBoeVS95wkqn7So%2BmPNGsD%2F1PjafUS0czgYdz1bvjOH2DnoY1d6ZY2mmHhKIsps7xCqNpKs0V0S2aXHBNkinCCP2ACpxFpQ945YveCQ9CrRKCQUbpz&X-Amz-Signature=d192e5bec1b3a650da376afcfcac734ffb0cc464a5143074a8176df8a81f1559&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFBKV5ES%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICHQXv75YVcS3OAw5rdKpUmQ9I3qyBGPk2qXwnswMQQsAiEAwspvVNgaHH8DP8F0BsQP8sqUHCo2l8hwq0s1NGdm4LUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNsWdf1D%2B9MaExsYxSrcA0Cct5jo%2BYr1MZw95fouPSD%2B23JzhUFqNvgI4mu0RKZ0e%2FoF%2BNAmeKHVR6fu0VrOdQEqlmb%2FPiP%2BNXEjBPqR7CSp8uZcuXGjVS%2BhFwzItbWr15XKlDNSKzMlnKvsHgf%2Bl%2Bh7BLxnqloNzBm9fid0nZgJhn6WYQsoW4IWyEn%2FZL0X6eK8TKJ9xWrLzLWuj%2BNccm26bJ1r%2FxWosqHnb4iTd2xcFnublYmO%2BtSFeX75r8ZH7vMeaqWV3IGoV8%2Bj1lSwE9FC%2FVnQJjqRoTwqIymtZGbCW1CFYiTOrT8jV9Mbyi6rBk6Wx9miy9E2qkqnnMfvbWDPCXtDiXXaWLv%2FCpy2tq56LvUYCofxOnBLSOSiGqX1jYNE2J%2F6Kc%2FG5pDiUnHui99HqLT3NtOuOOuvXRiz4Xu13u6j%2FEfB2h08BkAl5IyD0DvXoAWnImAfLbZR0%2FxhKWmvCFAUV21xnQaWEgRlG8EPmv6pThAIyFfwT57l2kr5%2FUD5Rlc5NUBUBspsAzerG4oZC575Z1hK2f5cKmdSBkrmCTeQw1Gslwhv7ZZK6l%2Bt8ebYTEr641DcJ75x1IRSZSLHntLjy%2Fawg86%2Bw8y6qlx8TXzgyLqCNfpjQUYIpc4gnHTIvYLDVHs3VHoqMKLH4c4GOqUBU3eer4hkeRdjUyi%2FhGkAh8N%2Fxio41BlwIlC%2FSvnYoMzAUgXJ2Q7aWuZOIc5gtbVmACZdRj%2BEkC3URmNxowqw0oEM9jht%2FGio9ZKMf321jSHBoeVS95wkqn7So%2BmPNGsD%2F1PjafUS0czgYdz1bvjOH2DnoY1d6ZY2mmHhKIsps7xCqNpKs0V0S2aXHBNkinCCP2ACpxFpQ945YveCQ9CrRKCQUbpz&X-Amz-Signature=f2a3947fff0072d1dc15b46efdef2b1cb13df58568a2ba1a38750a77b46830d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFBKV5ES%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICHQXv75YVcS3OAw5rdKpUmQ9I3qyBGPk2qXwnswMQQsAiEAwspvVNgaHH8DP8F0BsQP8sqUHCo2l8hwq0s1NGdm4LUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNsWdf1D%2B9MaExsYxSrcA0Cct5jo%2BYr1MZw95fouPSD%2B23JzhUFqNvgI4mu0RKZ0e%2FoF%2BNAmeKHVR6fu0VrOdQEqlmb%2FPiP%2BNXEjBPqR7CSp8uZcuXGjVS%2BhFwzItbWr15XKlDNSKzMlnKvsHgf%2Bl%2Bh7BLxnqloNzBm9fid0nZgJhn6WYQsoW4IWyEn%2FZL0X6eK8TKJ9xWrLzLWuj%2BNccm26bJ1r%2FxWosqHnb4iTd2xcFnublYmO%2BtSFeX75r8ZH7vMeaqWV3IGoV8%2Bj1lSwE9FC%2FVnQJjqRoTwqIymtZGbCW1CFYiTOrT8jV9Mbyi6rBk6Wx9miy9E2qkqnnMfvbWDPCXtDiXXaWLv%2FCpy2tq56LvUYCofxOnBLSOSiGqX1jYNE2J%2F6Kc%2FG5pDiUnHui99HqLT3NtOuOOuvXRiz4Xu13u6j%2FEfB2h08BkAl5IyD0DvXoAWnImAfLbZR0%2FxhKWmvCFAUV21xnQaWEgRlG8EPmv6pThAIyFfwT57l2kr5%2FUD5Rlc5NUBUBspsAzerG4oZC575Z1hK2f5cKmdSBkrmCTeQw1Gslwhv7ZZK6l%2Bt8ebYTEr641DcJ75x1IRSZSLHntLjy%2Fawg86%2Bw8y6qlx8TXzgyLqCNfpjQUYIpc4gnHTIvYLDVHs3VHoqMKLH4c4GOqUBU3eer4hkeRdjUyi%2FhGkAh8N%2Fxio41BlwIlC%2FSvnYoMzAUgXJ2Q7aWuZOIc5gtbVmACZdRj%2BEkC3URmNxowqw0oEM9jht%2FGio9ZKMf321jSHBoeVS95wkqn7So%2BmPNGsD%2F1PjafUS0czgYdz1bvjOH2DnoY1d6ZY2mmHhKIsps7xCqNpKs0V0S2aXHBNkinCCP2ACpxFpQ945YveCQ9CrRKCQUbpz&X-Amz-Signature=ffa68c7910cd0947c3dfb45cd98b330d3e43dac838af7f611af473b686c194a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFBKV5ES%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICHQXv75YVcS3OAw5rdKpUmQ9I3qyBGPk2qXwnswMQQsAiEAwspvVNgaHH8DP8F0BsQP8sqUHCo2l8hwq0s1NGdm4LUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNsWdf1D%2B9MaExsYxSrcA0Cct5jo%2BYr1MZw95fouPSD%2B23JzhUFqNvgI4mu0RKZ0e%2FoF%2BNAmeKHVR6fu0VrOdQEqlmb%2FPiP%2BNXEjBPqR7CSp8uZcuXGjVS%2BhFwzItbWr15XKlDNSKzMlnKvsHgf%2Bl%2Bh7BLxnqloNzBm9fid0nZgJhn6WYQsoW4IWyEn%2FZL0X6eK8TKJ9xWrLzLWuj%2BNccm26bJ1r%2FxWosqHnb4iTd2xcFnublYmO%2BtSFeX75r8ZH7vMeaqWV3IGoV8%2Bj1lSwE9FC%2FVnQJjqRoTwqIymtZGbCW1CFYiTOrT8jV9Mbyi6rBk6Wx9miy9E2qkqnnMfvbWDPCXtDiXXaWLv%2FCpy2tq56LvUYCofxOnBLSOSiGqX1jYNE2J%2F6Kc%2FG5pDiUnHui99HqLT3NtOuOOuvXRiz4Xu13u6j%2FEfB2h08BkAl5IyD0DvXoAWnImAfLbZR0%2FxhKWmvCFAUV21xnQaWEgRlG8EPmv6pThAIyFfwT57l2kr5%2FUD5Rlc5NUBUBspsAzerG4oZC575Z1hK2f5cKmdSBkrmCTeQw1Gslwhv7ZZK6l%2Bt8ebYTEr641DcJ75x1IRSZSLHntLjy%2Fawg86%2Bw8y6qlx8TXzgyLqCNfpjQUYIpc4gnHTIvYLDVHs3VHoqMKLH4c4GOqUBU3eer4hkeRdjUyi%2FhGkAh8N%2Fxio41BlwIlC%2FSvnYoMzAUgXJ2Q7aWuZOIc5gtbVmACZdRj%2BEkC3URmNxowqw0oEM9jht%2FGio9ZKMf321jSHBoeVS95wkqn7So%2BmPNGsD%2F1PjafUS0czgYdz1bvjOH2DnoY1d6ZY2mmHhKIsps7xCqNpKs0V0S2aXHBNkinCCP2ACpxFpQ945YveCQ9CrRKCQUbpz&X-Amz-Signature=a4921b9ac8dfcc6ca1691bfba83d3bbe0d7b6100a740b7c180cbbb958a6830b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFBKV5ES%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICHQXv75YVcS3OAw5rdKpUmQ9I3qyBGPk2qXwnswMQQsAiEAwspvVNgaHH8DP8F0BsQP8sqUHCo2l8hwq0s1NGdm4LUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNsWdf1D%2B9MaExsYxSrcA0Cct5jo%2BYr1MZw95fouPSD%2B23JzhUFqNvgI4mu0RKZ0e%2FoF%2BNAmeKHVR6fu0VrOdQEqlmb%2FPiP%2BNXEjBPqR7CSp8uZcuXGjVS%2BhFwzItbWr15XKlDNSKzMlnKvsHgf%2Bl%2Bh7BLxnqloNzBm9fid0nZgJhn6WYQsoW4IWyEn%2FZL0X6eK8TKJ9xWrLzLWuj%2BNccm26bJ1r%2FxWosqHnb4iTd2xcFnublYmO%2BtSFeX75r8ZH7vMeaqWV3IGoV8%2Bj1lSwE9FC%2FVnQJjqRoTwqIymtZGbCW1CFYiTOrT8jV9Mbyi6rBk6Wx9miy9E2qkqnnMfvbWDPCXtDiXXaWLv%2FCpy2tq56LvUYCofxOnBLSOSiGqX1jYNE2J%2F6Kc%2FG5pDiUnHui99HqLT3NtOuOOuvXRiz4Xu13u6j%2FEfB2h08BkAl5IyD0DvXoAWnImAfLbZR0%2FxhKWmvCFAUV21xnQaWEgRlG8EPmv6pThAIyFfwT57l2kr5%2FUD5Rlc5NUBUBspsAzerG4oZC575Z1hK2f5cKmdSBkrmCTeQw1Gslwhv7ZZK6l%2Bt8ebYTEr641DcJ75x1IRSZSLHntLjy%2Fawg86%2Bw8y6qlx8TXzgyLqCNfpjQUYIpc4gnHTIvYLDVHs3VHoqMKLH4c4GOqUBU3eer4hkeRdjUyi%2FhGkAh8N%2Fxio41BlwIlC%2FSvnYoMzAUgXJ2Q7aWuZOIc5gtbVmACZdRj%2BEkC3URmNxowqw0oEM9jht%2FGio9ZKMf321jSHBoeVS95wkqn7So%2BmPNGsD%2F1PjafUS0czgYdz1bvjOH2DnoY1d6ZY2mmHhKIsps7xCqNpKs0V0S2aXHBNkinCCP2ACpxFpQ945YveCQ9CrRKCQUbpz&X-Amz-Signature=611e2840b932991402a79ef15edce184748f9f25041fe07050eb3c115b7725ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFBKV5ES%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICHQXv75YVcS3OAw5rdKpUmQ9I3qyBGPk2qXwnswMQQsAiEAwspvVNgaHH8DP8F0BsQP8sqUHCo2l8hwq0s1NGdm4LUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNsWdf1D%2B9MaExsYxSrcA0Cct5jo%2BYr1MZw95fouPSD%2B23JzhUFqNvgI4mu0RKZ0e%2FoF%2BNAmeKHVR6fu0VrOdQEqlmb%2FPiP%2BNXEjBPqR7CSp8uZcuXGjVS%2BhFwzItbWr15XKlDNSKzMlnKvsHgf%2Bl%2Bh7BLxnqloNzBm9fid0nZgJhn6WYQsoW4IWyEn%2FZL0X6eK8TKJ9xWrLzLWuj%2BNccm26bJ1r%2FxWosqHnb4iTd2xcFnublYmO%2BtSFeX75r8ZH7vMeaqWV3IGoV8%2Bj1lSwE9FC%2FVnQJjqRoTwqIymtZGbCW1CFYiTOrT8jV9Mbyi6rBk6Wx9miy9E2qkqnnMfvbWDPCXtDiXXaWLv%2FCpy2tq56LvUYCofxOnBLSOSiGqX1jYNE2J%2F6Kc%2FG5pDiUnHui99HqLT3NtOuOOuvXRiz4Xu13u6j%2FEfB2h08BkAl5IyD0DvXoAWnImAfLbZR0%2FxhKWmvCFAUV21xnQaWEgRlG8EPmv6pThAIyFfwT57l2kr5%2FUD5Rlc5NUBUBspsAzerG4oZC575Z1hK2f5cKmdSBkrmCTeQw1Gslwhv7ZZK6l%2Bt8ebYTEr641DcJ75x1IRSZSLHntLjy%2Fawg86%2Bw8y6qlx8TXzgyLqCNfpjQUYIpc4gnHTIvYLDVHs3VHoqMKLH4c4GOqUBU3eer4hkeRdjUyi%2FhGkAh8N%2Fxio41BlwIlC%2FSvnYoMzAUgXJ2Q7aWuZOIc5gtbVmACZdRj%2BEkC3URmNxowqw0oEM9jht%2FGio9ZKMf321jSHBoeVS95wkqn7So%2BmPNGsD%2F1PjafUS0czgYdz1bvjOH2DnoY1d6ZY2mmHhKIsps7xCqNpKs0V0S2aXHBNkinCCP2ACpxFpQ945YveCQ9CrRKCQUbpz&X-Amz-Signature=4fb82ff5af695382fdc91887daf94c4129cd6e147138723ebdcb2f86a3179260&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFBKV5ES%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICHQXv75YVcS3OAw5rdKpUmQ9I3qyBGPk2qXwnswMQQsAiEAwspvVNgaHH8DP8F0BsQP8sqUHCo2l8hwq0s1NGdm4LUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNsWdf1D%2B9MaExsYxSrcA0Cct5jo%2BYr1MZw95fouPSD%2B23JzhUFqNvgI4mu0RKZ0e%2FoF%2BNAmeKHVR6fu0VrOdQEqlmb%2FPiP%2BNXEjBPqR7CSp8uZcuXGjVS%2BhFwzItbWr15XKlDNSKzMlnKvsHgf%2Bl%2Bh7BLxnqloNzBm9fid0nZgJhn6WYQsoW4IWyEn%2FZL0X6eK8TKJ9xWrLzLWuj%2BNccm26bJ1r%2FxWosqHnb4iTd2xcFnublYmO%2BtSFeX75r8ZH7vMeaqWV3IGoV8%2Bj1lSwE9FC%2FVnQJjqRoTwqIymtZGbCW1CFYiTOrT8jV9Mbyi6rBk6Wx9miy9E2qkqnnMfvbWDPCXtDiXXaWLv%2FCpy2tq56LvUYCofxOnBLSOSiGqX1jYNE2J%2F6Kc%2FG5pDiUnHui99HqLT3NtOuOOuvXRiz4Xu13u6j%2FEfB2h08BkAl5IyD0DvXoAWnImAfLbZR0%2FxhKWmvCFAUV21xnQaWEgRlG8EPmv6pThAIyFfwT57l2kr5%2FUD5Rlc5NUBUBspsAzerG4oZC575Z1hK2f5cKmdSBkrmCTeQw1Gslwhv7ZZK6l%2Bt8ebYTEr641DcJ75x1IRSZSLHntLjy%2Fawg86%2Bw8y6qlx8TXzgyLqCNfpjQUYIpc4gnHTIvYLDVHs3VHoqMKLH4c4GOqUBU3eer4hkeRdjUyi%2FhGkAh8N%2Fxio41BlwIlC%2FSvnYoMzAUgXJ2Q7aWuZOIc5gtbVmACZdRj%2BEkC3URmNxowqw0oEM9jht%2FGio9ZKMf321jSHBoeVS95wkqn7So%2BmPNGsD%2F1PjafUS0czgYdz1bvjOH2DnoY1d6ZY2mmHhKIsps7xCqNpKs0V0S2aXHBNkinCCP2ACpxFpQ945YveCQ9CrRKCQUbpz&X-Amz-Signature=c6b911a9888659d99da885cca8280a7ff3691859bf5543ef45aeed7d1284a2b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFBKV5ES%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICHQXv75YVcS3OAw5rdKpUmQ9I3qyBGPk2qXwnswMQQsAiEAwspvVNgaHH8DP8F0BsQP8sqUHCo2l8hwq0s1NGdm4LUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNsWdf1D%2B9MaExsYxSrcA0Cct5jo%2BYr1MZw95fouPSD%2B23JzhUFqNvgI4mu0RKZ0e%2FoF%2BNAmeKHVR6fu0VrOdQEqlmb%2FPiP%2BNXEjBPqR7CSp8uZcuXGjVS%2BhFwzItbWr15XKlDNSKzMlnKvsHgf%2Bl%2Bh7BLxnqloNzBm9fid0nZgJhn6WYQsoW4IWyEn%2FZL0X6eK8TKJ9xWrLzLWuj%2BNccm26bJ1r%2FxWosqHnb4iTd2xcFnublYmO%2BtSFeX75r8ZH7vMeaqWV3IGoV8%2Bj1lSwE9FC%2FVnQJjqRoTwqIymtZGbCW1CFYiTOrT8jV9Mbyi6rBk6Wx9miy9E2qkqnnMfvbWDPCXtDiXXaWLv%2FCpy2tq56LvUYCofxOnBLSOSiGqX1jYNE2J%2F6Kc%2FG5pDiUnHui99HqLT3NtOuOOuvXRiz4Xu13u6j%2FEfB2h08BkAl5IyD0DvXoAWnImAfLbZR0%2FxhKWmvCFAUV21xnQaWEgRlG8EPmv6pThAIyFfwT57l2kr5%2FUD5Rlc5NUBUBspsAzerG4oZC575Z1hK2f5cKmdSBkrmCTeQw1Gslwhv7ZZK6l%2Bt8ebYTEr641DcJ75x1IRSZSLHntLjy%2Fawg86%2Bw8y6qlx8TXzgyLqCNfpjQUYIpc4gnHTIvYLDVHs3VHoqMKLH4c4GOqUBU3eer4hkeRdjUyi%2FhGkAh8N%2Fxio41BlwIlC%2FSvnYoMzAUgXJ2Q7aWuZOIc5gtbVmACZdRj%2BEkC3URmNxowqw0oEM9jht%2FGio9ZKMf321jSHBoeVS95wkqn7So%2BmPNGsD%2F1PjafUS0czgYdz1bvjOH2DnoY1d6ZY2mmHhKIsps7xCqNpKs0V0S2aXHBNkinCCP2ACpxFpQ945YveCQ9CrRKCQUbpz&X-Amz-Signature=e5f06160f0eb1128cdfa195c10952b84e89b89c3b1ce5d9979301350ce766c92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFBKV5ES%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICHQXv75YVcS3OAw5rdKpUmQ9I3qyBGPk2qXwnswMQQsAiEAwspvVNgaHH8DP8F0BsQP8sqUHCo2l8hwq0s1NGdm4LUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNsWdf1D%2B9MaExsYxSrcA0Cct5jo%2BYr1MZw95fouPSD%2B23JzhUFqNvgI4mu0RKZ0e%2FoF%2BNAmeKHVR6fu0VrOdQEqlmb%2FPiP%2BNXEjBPqR7CSp8uZcuXGjVS%2BhFwzItbWr15XKlDNSKzMlnKvsHgf%2Bl%2Bh7BLxnqloNzBm9fid0nZgJhn6WYQsoW4IWyEn%2FZL0X6eK8TKJ9xWrLzLWuj%2BNccm26bJ1r%2FxWosqHnb4iTd2xcFnublYmO%2BtSFeX75r8ZH7vMeaqWV3IGoV8%2Bj1lSwE9FC%2FVnQJjqRoTwqIymtZGbCW1CFYiTOrT8jV9Mbyi6rBk6Wx9miy9E2qkqnnMfvbWDPCXtDiXXaWLv%2FCpy2tq56LvUYCofxOnBLSOSiGqX1jYNE2J%2F6Kc%2FG5pDiUnHui99HqLT3NtOuOOuvXRiz4Xu13u6j%2FEfB2h08BkAl5IyD0DvXoAWnImAfLbZR0%2FxhKWmvCFAUV21xnQaWEgRlG8EPmv6pThAIyFfwT57l2kr5%2FUD5Rlc5NUBUBspsAzerG4oZC575Z1hK2f5cKmdSBkrmCTeQw1Gslwhv7ZZK6l%2Bt8ebYTEr641DcJ75x1IRSZSLHntLjy%2Fawg86%2Bw8y6qlx8TXzgyLqCNfpjQUYIpc4gnHTIvYLDVHs3VHoqMKLH4c4GOqUBU3eer4hkeRdjUyi%2FhGkAh8N%2Fxio41BlwIlC%2FSvnYoMzAUgXJ2Q7aWuZOIc5gtbVmACZdRj%2BEkC3URmNxowqw0oEM9jht%2FGio9ZKMf321jSHBoeVS95wkqn7So%2BmPNGsD%2F1PjafUS0czgYdz1bvjOH2DnoY1d6ZY2mmHhKIsps7xCqNpKs0V0S2aXHBNkinCCP2ACpxFpQ945YveCQ9CrRKCQUbpz&X-Amz-Signature=8b8daffbb87bd69ff52edce1db70ffe09ebd87f9ba86e0bcbf6f4a908b0464d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

