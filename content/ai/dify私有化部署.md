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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK6XZQFE%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCega%2Bv3NskJCpCeVjR2xvKXVAYNy%2BK4p%2BifYCoxCVyAgIhAJ%2FjGp9nvECB8E%2Fe1VjE8wRx83gzGUmHasjsC6kWhjIvKv8DCHsQABoMNjM3NDIzMTgzODA1Igxh1TpKqh2FtRngX6Qq3AMdK9zXOMahhBrAwrm%2FZTCPC3S%2BkB9vdd7M6cmtn%2BWrFgQ1KnIeLK4Wz1UWP1NPZJxAK5GgeiIf6fClhripyY5EqbPDna4yrtbL%2BQPqrZEJtVi9u5TtYvvkwzb3MQbhiCTilFAHbUIgErfvE8dOjVGMcenWuajohmggsl111ktPRBPxpfQ1et3SKLxGLEqU0W6yesY1QISQM%2B%2BjYvDv86kPgYW%2Bq0JgSIgQahul0uWKDxuIV0Uxw41Q1IRkvfgGBIKsJtulKfGJcR3J3L7dWy7pbGolNxhD9vhqkkZQR%2BOGM%2BjvYu7dWfyMGT1TlC%2BZLEmEj01o1uMvgpJZp1qUk7eeUOUJAKz7pFfstfxP1mTfjkSElqyzjZvoNNcezqCcr11jcPtGLj%2FGwXiYIsj2HXw%2FMf3RmvzAC5G4VuTzsqdGlkMvLE0t9bhuk%2F4MTnXpcM8zvNxNrVIiaEpVkst0s%2BeTgWHTLxVC661cMjisMrQ6hAVdkYNjMIcxMpDzLakJAlJcfOXxhjWQzXZ92ItSOx%2FrCZVpO619%2FF013vHurA8kNwdt1%2Fx5wG%2B0cZSc6IIzg9w3rgLTU1t0pmjwT11lm8yd%2BGG2T6jdMLAJMphbqzuZdpC7VqavfBOXcO2HQTCXsJnJBjqkAbiEf9%2B%2BOdZHo43Gb29AdL015yPi%2FUTi24A7f%2Fi9NIBexZjH424mO7H6eFyz4FuLIYMn13wo%2B6fqhOqlGMnsV69FwbEOU%2FA513D6JLkdUa6lIqiyJJ9gTdAvNAAzVVbT7qVx0IVMfmoJIe%2Bn5Lect05m%2FKuqHPqc9ofNSP4qd8aNbqAATk4T4%2BEo%2FkkPSuTlZIDaKjERwlHB%2FZ%2BrXsjqij9eF%2BYl&X-Amz-Signature=a357498e0293a118d1e7c967ac4285684b14adb389793087539494e9c241791e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK6XZQFE%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCega%2Bv3NskJCpCeVjR2xvKXVAYNy%2BK4p%2BifYCoxCVyAgIhAJ%2FjGp9nvECB8E%2Fe1VjE8wRx83gzGUmHasjsC6kWhjIvKv8DCHsQABoMNjM3NDIzMTgzODA1Igxh1TpKqh2FtRngX6Qq3AMdK9zXOMahhBrAwrm%2FZTCPC3S%2BkB9vdd7M6cmtn%2BWrFgQ1KnIeLK4Wz1UWP1NPZJxAK5GgeiIf6fClhripyY5EqbPDna4yrtbL%2BQPqrZEJtVi9u5TtYvvkwzb3MQbhiCTilFAHbUIgErfvE8dOjVGMcenWuajohmggsl111ktPRBPxpfQ1et3SKLxGLEqU0W6yesY1QISQM%2B%2BjYvDv86kPgYW%2Bq0JgSIgQahul0uWKDxuIV0Uxw41Q1IRkvfgGBIKsJtulKfGJcR3J3L7dWy7pbGolNxhD9vhqkkZQR%2BOGM%2BjvYu7dWfyMGT1TlC%2BZLEmEj01o1uMvgpJZp1qUk7eeUOUJAKz7pFfstfxP1mTfjkSElqyzjZvoNNcezqCcr11jcPtGLj%2FGwXiYIsj2HXw%2FMf3RmvzAC5G4VuTzsqdGlkMvLE0t9bhuk%2F4MTnXpcM8zvNxNrVIiaEpVkst0s%2BeTgWHTLxVC661cMjisMrQ6hAVdkYNjMIcxMpDzLakJAlJcfOXxhjWQzXZ92ItSOx%2FrCZVpO619%2FF013vHurA8kNwdt1%2Fx5wG%2B0cZSc6IIzg9w3rgLTU1t0pmjwT11lm8yd%2BGG2T6jdMLAJMphbqzuZdpC7VqavfBOXcO2HQTCXsJnJBjqkAbiEf9%2B%2BOdZHo43Gb29AdL015yPi%2FUTi24A7f%2Fi9NIBexZjH424mO7H6eFyz4FuLIYMn13wo%2B6fqhOqlGMnsV69FwbEOU%2FA513D6JLkdUa6lIqiyJJ9gTdAvNAAzVVbT7qVx0IVMfmoJIe%2Bn5Lect05m%2FKuqHPqc9ofNSP4qd8aNbqAATk4T4%2BEo%2FkkPSuTlZIDaKjERwlHB%2FZ%2BrXsjqij9eF%2BYl&X-Amz-Signature=60394d6500e2ec35e94a567d0d42d173379ebf91c72f9ae0be1ed76235a9d9fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK6XZQFE%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCega%2Bv3NskJCpCeVjR2xvKXVAYNy%2BK4p%2BifYCoxCVyAgIhAJ%2FjGp9nvECB8E%2Fe1VjE8wRx83gzGUmHasjsC6kWhjIvKv8DCHsQABoMNjM3NDIzMTgzODA1Igxh1TpKqh2FtRngX6Qq3AMdK9zXOMahhBrAwrm%2FZTCPC3S%2BkB9vdd7M6cmtn%2BWrFgQ1KnIeLK4Wz1UWP1NPZJxAK5GgeiIf6fClhripyY5EqbPDna4yrtbL%2BQPqrZEJtVi9u5TtYvvkwzb3MQbhiCTilFAHbUIgErfvE8dOjVGMcenWuajohmggsl111ktPRBPxpfQ1et3SKLxGLEqU0W6yesY1QISQM%2B%2BjYvDv86kPgYW%2Bq0JgSIgQahul0uWKDxuIV0Uxw41Q1IRkvfgGBIKsJtulKfGJcR3J3L7dWy7pbGolNxhD9vhqkkZQR%2BOGM%2BjvYu7dWfyMGT1TlC%2BZLEmEj01o1uMvgpJZp1qUk7eeUOUJAKz7pFfstfxP1mTfjkSElqyzjZvoNNcezqCcr11jcPtGLj%2FGwXiYIsj2HXw%2FMf3RmvzAC5G4VuTzsqdGlkMvLE0t9bhuk%2F4MTnXpcM8zvNxNrVIiaEpVkst0s%2BeTgWHTLxVC661cMjisMrQ6hAVdkYNjMIcxMpDzLakJAlJcfOXxhjWQzXZ92ItSOx%2FrCZVpO619%2FF013vHurA8kNwdt1%2Fx5wG%2B0cZSc6IIzg9w3rgLTU1t0pmjwT11lm8yd%2BGG2T6jdMLAJMphbqzuZdpC7VqavfBOXcO2HQTCXsJnJBjqkAbiEf9%2B%2BOdZHo43Gb29AdL015yPi%2FUTi24A7f%2Fi9NIBexZjH424mO7H6eFyz4FuLIYMn13wo%2B6fqhOqlGMnsV69FwbEOU%2FA513D6JLkdUa6lIqiyJJ9gTdAvNAAzVVbT7qVx0IVMfmoJIe%2Bn5Lect05m%2FKuqHPqc9ofNSP4qd8aNbqAATk4T4%2BEo%2FkkPSuTlZIDaKjERwlHB%2FZ%2BrXsjqij9eF%2BYl&X-Amz-Signature=6a64bba7d79653626dddfca2d92701cc3dc66c98d435fdff1bdc47e8740bda40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK6XZQFE%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCega%2Bv3NskJCpCeVjR2xvKXVAYNy%2BK4p%2BifYCoxCVyAgIhAJ%2FjGp9nvECB8E%2Fe1VjE8wRx83gzGUmHasjsC6kWhjIvKv8DCHsQABoMNjM3NDIzMTgzODA1Igxh1TpKqh2FtRngX6Qq3AMdK9zXOMahhBrAwrm%2FZTCPC3S%2BkB9vdd7M6cmtn%2BWrFgQ1KnIeLK4Wz1UWP1NPZJxAK5GgeiIf6fClhripyY5EqbPDna4yrtbL%2BQPqrZEJtVi9u5TtYvvkwzb3MQbhiCTilFAHbUIgErfvE8dOjVGMcenWuajohmggsl111ktPRBPxpfQ1et3SKLxGLEqU0W6yesY1QISQM%2B%2BjYvDv86kPgYW%2Bq0JgSIgQahul0uWKDxuIV0Uxw41Q1IRkvfgGBIKsJtulKfGJcR3J3L7dWy7pbGolNxhD9vhqkkZQR%2BOGM%2BjvYu7dWfyMGT1TlC%2BZLEmEj01o1uMvgpJZp1qUk7eeUOUJAKz7pFfstfxP1mTfjkSElqyzjZvoNNcezqCcr11jcPtGLj%2FGwXiYIsj2HXw%2FMf3RmvzAC5G4VuTzsqdGlkMvLE0t9bhuk%2F4MTnXpcM8zvNxNrVIiaEpVkst0s%2BeTgWHTLxVC661cMjisMrQ6hAVdkYNjMIcxMpDzLakJAlJcfOXxhjWQzXZ92ItSOx%2FrCZVpO619%2FF013vHurA8kNwdt1%2Fx5wG%2B0cZSc6IIzg9w3rgLTU1t0pmjwT11lm8yd%2BGG2T6jdMLAJMphbqzuZdpC7VqavfBOXcO2HQTCXsJnJBjqkAbiEf9%2B%2BOdZHo43Gb29AdL015yPi%2FUTi24A7f%2Fi9NIBexZjH424mO7H6eFyz4FuLIYMn13wo%2B6fqhOqlGMnsV69FwbEOU%2FA513D6JLkdUa6lIqiyJJ9gTdAvNAAzVVbT7qVx0IVMfmoJIe%2Bn5Lect05m%2FKuqHPqc9ofNSP4qd8aNbqAATk4T4%2BEo%2FkkPSuTlZIDaKjERwlHB%2FZ%2BrXsjqij9eF%2BYl&X-Amz-Signature=3744d89074b78f9c2f559f6113d5ecae7013595d810f44eeaff845c29ca40e9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK6XZQFE%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCega%2Bv3NskJCpCeVjR2xvKXVAYNy%2BK4p%2BifYCoxCVyAgIhAJ%2FjGp9nvECB8E%2Fe1VjE8wRx83gzGUmHasjsC6kWhjIvKv8DCHsQABoMNjM3NDIzMTgzODA1Igxh1TpKqh2FtRngX6Qq3AMdK9zXOMahhBrAwrm%2FZTCPC3S%2BkB9vdd7M6cmtn%2BWrFgQ1KnIeLK4Wz1UWP1NPZJxAK5GgeiIf6fClhripyY5EqbPDna4yrtbL%2BQPqrZEJtVi9u5TtYvvkwzb3MQbhiCTilFAHbUIgErfvE8dOjVGMcenWuajohmggsl111ktPRBPxpfQ1et3SKLxGLEqU0W6yesY1QISQM%2B%2BjYvDv86kPgYW%2Bq0JgSIgQahul0uWKDxuIV0Uxw41Q1IRkvfgGBIKsJtulKfGJcR3J3L7dWy7pbGolNxhD9vhqkkZQR%2BOGM%2BjvYu7dWfyMGT1TlC%2BZLEmEj01o1uMvgpJZp1qUk7eeUOUJAKz7pFfstfxP1mTfjkSElqyzjZvoNNcezqCcr11jcPtGLj%2FGwXiYIsj2HXw%2FMf3RmvzAC5G4VuTzsqdGlkMvLE0t9bhuk%2F4MTnXpcM8zvNxNrVIiaEpVkst0s%2BeTgWHTLxVC661cMjisMrQ6hAVdkYNjMIcxMpDzLakJAlJcfOXxhjWQzXZ92ItSOx%2FrCZVpO619%2FF013vHurA8kNwdt1%2Fx5wG%2B0cZSc6IIzg9w3rgLTU1t0pmjwT11lm8yd%2BGG2T6jdMLAJMphbqzuZdpC7VqavfBOXcO2HQTCXsJnJBjqkAbiEf9%2B%2BOdZHo43Gb29AdL015yPi%2FUTi24A7f%2Fi9NIBexZjH424mO7H6eFyz4FuLIYMn13wo%2B6fqhOqlGMnsV69FwbEOU%2FA513D6JLkdUa6lIqiyJJ9gTdAvNAAzVVbT7qVx0IVMfmoJIe%2Bn5Lect05m%2FKuqHPqc9ofNSP4qd8aNbqAATk4T4%2BEo%2FkkPSuTlZIDaKjERwlHB%2FZ%2BrXsjqij9eF%2BYl&X-Amz-Signature=d61dc2d38353f1c30a176023db5ef38fe057d263343d15a1662bec091ec5dec7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK6XZQFE%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCega%2Bv3NskJCpCeVjR2xvKXVAYNy%2BK4p%2BifYCoxCVyAgIhAJ%2FjGp9nvECB8E%2Fe1VjE8wRx83gzGUmHasjsC6kWhjIvKv8DCHsQABoMNjM3NDIzMTgzODA1Igxh1TpKqh2FtRngX6Qq3AMdK9zXOMahhBrAwrm%2FZTCPC3S%2BkB9vdd7M6cmtn%2BWrFgQ1KnIeLK4Wz1UWP1NPZJxAK5GgeiIf6fClhripyY5EqbPDna4yrtbL%2BQPqrZEJtVi9u5TtYvvkwzb3MQbhiCTilFAHbUIgErfvE8dOjVGMcenWuajohmggsl111ktPRBPxpfQ1et3SKLxGLEqU0W6yesY1QISQM%2B%2BjYvDv86kPgYW%2Bq0JgSIgQahul0uWKDxuIV0Uxw41Q1IRkvfgGBIKsJtulKfGJcR3J3L7dWy7pbGolNxhD9vhqkkZQR%2BOGM%2BjvYu7dWfyMGT1TlC%2BZLEmEj01o1uMvgpJZp1qUk7eeUOUJAKz7pFfstfxP1mTfjkSElqyzjZvoNNcezqCcr11jcPtGLj%2FGwXiYIsj2HXw%2FMf3RmvzAC5G4VuTzsqdGlkMvLE0t9bhuk%2F4MTnXpcM8zvNxNrVIiaEpVkst0s%2BeTgWHTLxVC661cMjisMrQ6hAVdkYNjMIcxMpDzLakJAlJcfOXxhjWQzXZ92ItSOx%2FrCZVpO619%2FF013vHurA8kNwdt1%2Fx5wG%2B0cZSc6IIzg9w3rgLTU1t0pmjwT11lm8yd%2BGG2T6jdMLAJMphbqzuZdpC7VqavfBOXcO2HQTCXsJnJBjqkAbiEf9%2B%2BOdZHo43Gb29AdL015yPi%2FUTi24A7f%2Fi9NIBexZjH424mO7H6eFyz4FuLIYMn13wo%2B6fqhOqlGMnsV69FwbEOU%2FA513D6JLkdUa6lIqiyJJ9gTdAvNAAzVVbT7qVx0IVMfmoJIe%2Bn5Lect05m%2FKuqHPqc9ofNSP4qd8aNbqAATk4T4%2BEo%2FkkPSuTlZIDaKjERwlHB%2FZ%2BrXsjqij9eF%2BYl&X-Amz-Signature=39d04e6502a0e663940d1c2e35ff9c3265933aa6e576e2671a561c4e6870c97a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK6XZQFE%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCega%2Bv3NskJCpCeVjR2xvKXVAYNy%2BK4p%2BifYCoxCVyAgIhAJ%2FjGp9nvECB8E%2Fe1VjE8wRx83gzGUmHasjsC6kWhjIvKv8DCHsQABoMNjM3NDIzMTgzODA1Igxh1TpKqh2FtRngX6Qq3AMdK9zXOMahhBrAwrm%2FZTCPC3S%2BkB9vdd7M6cmtn%2BWrFgQ1KnIeLK4Wz1UWP1NPZJxAK5GgeiIf6fClhripyY5EqbPDna4yrtbL%2BQPqrZEJtVi9u5TtYvvkwzb3MQbhiCTilFAHbUIgErfvE8dOjVGMcenWuajohmggsl111ktPRBPxpfQ1et3SKLxGLEqU0W6yesY1QISQM%2B%2BjYvDv86kPgYW%2Bq0JgSIgQahul0uWKDxuIV0Uxw41Q1IRkvfgGBIKsJtulKfGJcR3J3L7dWy7pbGolNxhD9vhqkkZQR%2BOGM%2BjvYu7dWfyMGT1TlC%2BZLEmEj01o1uMvgpJZp1qUk7eeUOUJAKz7pFfstfxP1mTfjkSElqyzjZvoNNcezqCcr11jcPtGLj%2FGwXiYIsj2HXw%2FMf3RmvzAC5G4VuTzsqdGlkMvLE0t9bhuk%2F4MTnXpcM8zvNxNrVIiaEpVkst0s%2BeTgWHTLxVC661cMjisMrQ6hAVdkYNjMIcxMpDzLakJAlJcfOXxhjWQzXZ92ItSOx%2FrCZVpO619%2FF013vHurA8kNwdt1%2Fx5wG%2B0cZSc6IIzg9w3rgLTU1t0pmjwT11lm8yd%2BGG2T6jdMLAJMphbqzuZdpC7VqavfBOXcO2HQTCXsJnJBjqkAbiEf9%2B%2BOdZHo43Gb29AdL015yPi%2FUTi24A7f%2Fi9NIBexZjH424mO7H6eFyz4FuLIYMn13wo%2B6fqhOqlGMnsV69FwbEOU%2FA513D6JLkdUa6lIqiyJJ9gTdAvNAAzVVbT7qVx0IVMfmoJIe%2Bn5Lect05m%2FKuqHPqc9ofNSP4qd8aNbqAATk4T4%2BEo%2FkkPSuTlZIDaKjERwlHB%2FZ%2BrXsjqij9eF%2BYl&X-Amz-Signature=a6e9921533d5d5100a36d71aab117ab0bbcdda65acbdbe3cbf92f6c75076889f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK6XZQFE%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCega%2Bv3NskJCpCeVjR2xvKXVAYNy%2BK4p%2BifYCoxCVyAgIhAJ%2FjGp9nvECB8E%2Fe1VjE8wRx83gzGUmHasjsC6kWhjIvKv8DCHsQABoMNjM3NDIzMTgzODA1Igxh1TpKqh2FtRngX6Qq3AMdK9zXOMahhBrAwrm%2FZTCPC3S%2BkB9vdd7M6cmtn%2BWrFgQ1KnIeLK4Wz1UWP1NPZJxAK5GgeiIf6fClhripyY5EqbPDna4yrtbL%2BQPqrZEJtVi9u5TtYvvkwzb3MQbhiCTilFAHbUIgErfvE8dOjVGMcenWuajohmggsl111ktPRBPxpfQ1et3SKLxGLEqU0W6yesY1QISQM%2B%2BjYvDv86kPgYW%2Bq0JgSIgQahul0uWKDxuIV0Uxw41Q1IRkvfgGBIKsJtulKfGJcR3J3L7dWy7pbGolNxhD9vhqkkZQR%2BOGM%2BjvYu7dWfyMGT1TlC%2BZLEmEj01o1uMvgpJZp1qUk7eeUOUJAKz7pFfstfxP1mTfjkSElqyzjZvoNNcezqCcr11jcPtGLj%2FGwXiYIsj2HXw%2FMf3RmvzAC5G4VuTzsqdGlkMvLE0t9bhuk%2F4MTnXpcM8zvNxNrVIiaEpVkst0s%2BeTgWHTLxVC661cMjisMrQ6hAVdkYNjMIcxMpDzLakJAlJcfOXxhjWQzXZ92ItSOx%2FrCZVpO619%2FF013vHurA8kNwdt1%2Fx5wG%2B0cZSc6IIzg9w3rgLTU1t0pmjwT11lm8yd%2BGG2T6jdMLAJMphbqzuZdpC7VqavfBOXcO2HQTCXsJnJBjqkAbiEf9%2B%2BOdZHo43Gb29AdL015yPi%2FUTi24A7f%2Fi9NIBexZjH424mO7H6eFyz4FuLIYMn13wo%2B6fqhOqlGMnsV69FwbEOU%2FA513D6JLkdUa6lIqiyJJ9gTdAvNAAzVVbT7qVx0IVMfmoJIe%2Bn5Lect05m%2FKuqHPqc9ofNSP4qd8aNbqAATk4T4%2BEo%2FkkPSuTlZIDaKjERwlHB%2FZ%2BrXsjqij9eF%2BYl&X-Amz-Signature=9a56f53f1815584b1019297e20cb8e6aef1f33fad49d211b2b5f019a20a9ad29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK6XZQFE%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCega%2Bv3NskJCpCeVjR2xvKXVAYNy%2BK4p%2BifYCoxCVyAgIhAJ%2FjGp9nvECB8E%2Fe1VjE8wRx83gzGUmHasjsC6kWhjIvKv8DCHsQABoMNjM3NDIzMTgzODA1Igxh1TpKqh2FtRngX6Qq3AMdK9zXOMahhBrAwrm%2FZTCPC3S%2BkB9vdd7M6cmtn%2BWrFgQ1KnIeLK4Wz1UWP1NPZJxAK5GgeiIf6fClhripyY5EqbPDna4yrtbL%2BQPqrZEJtVi9u5TtYvvkwzb3MQbhiCTilFAHbUIgErfvE8dOjVGMcenWuajohmggsl111ktPRBPxpfQ1et3SKLxGLEqU0W6yesY1QISQM%2B%2BjYvDv86kPgYW%2Bq0JgSIgQahul0uWKDxuIV0Uxw41Q1IRkvfgGBIKsJtulKfGJcR3J3L7dWy7pbGolNxhD9vhqkkZQR%2BOGM%2BjvYu7dWfyMGT1TlC%2BZLEmEj01o1uMvgpJZp1qUk7eeUOUJAKz7pFfstfxP1mTfjkSElqyzjZvoNNcezqCcr11jcPtGLj%2FGwXiYIsj2HXw%2FMf3RmvzAC5G4VuTzsqdGlkMvLE0t9bhuk%2F4MTnXpcM8zvNxNrVIiaEpVkst0s%2BeTgWHTLxVC661cMjisMrQ6hAVdkYNjMIcxMpDzLakJAlJcfOXxhjWQzXZ92ItSOx%2FrCZVpO619%2FF013vHurA8kNwdt1%2Fx5wG%2B0cZSc6IIzg9w3rgLTU1t0pmjwT11lm8yd%2BGG2T6jdMLAJMphbqzuZdpC7VqavfBOXcO2HQTCXsJnJBjqkAbiEf9%2B%2BOdZHo43Gb29AdL015yPi%2FUTi24A7f%2Fi9NIBexZjH424mO7H6eFyz4FuLIYMn13wo%2B6fqhOqlGMnsV69FwbEOU%2FA513D6JLkdUa6lIqiyJJ9gTdAvNAAzVVbT7qVx0IVMfmoJIe%2Bn5Lect05m%2FKuqHPqc9ofNSP4qd8aNbqAATk4T4%2BEo%2FkkPSuTlZIDaKjERwlHB%2FZ%2BrXsjqij9eF%2BYl&X-Amz-Signature=09bea8ae4648de2315768deb1fb7dd5c7827a185c20253f1ae2436af646641b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK6XZQFE%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCega%2Bv3NskJCpCeVjR2xvKXVAYNy%2BK4p%2BifYCoxCVyAgIhAJ%2FjGp9nvECB8E%2Fe1VjE8wRx83gzGUmHasjsC6kWhjIvKv8DCHsQABoMNjM3NDIzMTgzODA1Igxh1TpKqh2FtRngX6Qq3AMdK9zXOMahhBrAwrm%2FZTCPC3S%2BkB9vdd7M6cmtn%2BWrFgQ1KnIeLK4Wz1UWP1NPZJxAK5GgeiIf6fClhripyY5EqbPDna4yrtbL%2BQPqrZEJtVi9u5TtYvvkwzb3MQbhiCTilFAHbUIgErfvE8dOjVGMcenWuajohmggsl111ktPRBPxpfQ1et3SKLxGLEqU0W6yesY1QISQM%2B%2BjYvDv86kPgYW%2Bq0JgSIgQahul0uWKDxuIV0Uxw41Q1IRkvfgGBIKsJtulKfGJcR3J3L7dWy7pbGolNxhD9vhqkkZQR%2BOGM%2BjvYu7dWfyMGT1TlC%2BZLEmEj01o1uMvgpJZp1qUk7eeUOUJAKz7pFfstfxP1mTfjkSElqyzjZvoNNcezqCcr11jcPtGLj%2FGwXiYIsj2HXw%2FMf3RmvzAC5G4VuTzsqdGlkMvLE0t9bhuk%2F4MTnXpcM8zvNxNrVIiaEpVkst0s%2BeTgWHTLxVC661cMjisMrQ6hAVdkYNjMIcxMpDzLakJAlJcfOXxhjWQzXZ92ItSOx%2FrCZVpO619%2FF013vHurA8kNwdt1%2Fx5wG%2B0cZSc6IIzg9w3rgLTU1t0pmjwT11lm8yd%2BGG2T6jdMLAJMphbqzuZdpC7VqavfBOXcO2HQTCXsJnJBjqkAbiEf9%2B%2BOdZHo43Gb29AdL015yPi%2FUTi24A7f%2Fi9NIBexZjH424mO7H6eFyz4FuLIYMn13wo%2B6fqhOqlGMnsV69FwbEOU%2FA513D6JLkdUa6lIqiyJJ9gTdAvNAAzVVbT7qVx0IVMfmoJIe%2Bn5Lect05m%2FKuqHPqc9ofNSP4qd8aNbqAATk4T4%2BEo%2FkkPSuTlZIDaKjERwlHB%2FZ%2BrXsjqij9eF%2BYl&X-Amz-Signature=24d76e9e46dc027b8d08e138701bad6b52945090abb64fb8dbdd6300534fb09e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

