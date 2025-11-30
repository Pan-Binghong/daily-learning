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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OUNPMID%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDFfLU26Z262WW3ozENYWgO0MGpfF%2B9PIOc4Jer%2F6tL1wIhAIpYQtT1Nh2Npa8RffJC6GVuyS6c6O4TMjaS0yI2FB1tKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAUaXV%2BROcQ6FGWooq3APNdlJ%2FEpuU0%2Fs7fR%2FpChmbrG0F6GPcbZdV0NPM01WvgxWW%2B7Ea%2BTAkq9Iv4mK9VKGCwDSOQLHQ4HLhxgY4YhMG2MdGXwaxyPkOGekFw1rlwgHc23GPWR%2BrTMgnlcVF0K4v7heNWh%2BsN9IMbPxJLDhsfrzDoB24VGm4Zp%2BbaNWJnHHU3LjLGocxEeQz5UupRiVn9SdohyLliYWbABZ3zNnZGhhEnxxqo59IvVJUCRXaZU7aRSrqKSsVOt0Js46pnwc5QJcRIAGEM4WCHM7NPLQUhSZ0sh5%2FOSmrQzbjblblXYmGBokQWOVoPHeMmCHET4fyP8zniBxn9a%2B9XWA%2BSUsdx8FNnbT4HmPyJgMzIDcoV%2F6hyEMcI2RLqZEuXHRmxHDFuWokixGRMyaYBQ0k2rMyx9K6StDOfCitq%2FSo6JF4KPKJNp7XFoFybK6gqbBVE8PBCdQ18Lud3SxdmBi7Wn1t0zPfewPflfza3e2uA67a8j5qkN23CguYZfDLZIytJhJGcAvl5DHL6YDMnzzY88EjDxg7i5INfdFu%2BAeF68%2BYIRQLOpzvqst4yJXBmlPCt%2BWmK2lBZGorI1yh5Z%2Bxp3zYdY0YPRCK09OM8TSuU5%2BvtNCXrD2n18z7wSXx2zC9z63JBjqkAZPwME3BbM3bH4M2bftn%2BukRhhKdlYFBKNqXz4Gd%2Fru8oP8Kua672F%2FNT8N9nS2DssGf%2FABj6WizeSnTG%2BrfeS2SKJmVjHt8K7MxifqHxPj3eF6gxisKEkA%2BApxhBp%2FgxaxtMt%2BpjpNNpTJu9y4c%2FsKa5bknN1Xi31a%2BDuQr1izAJefAP%2BW4JLRKTcb0r31LkOg%2Bi8Xn0PWt%2F9bj9hAJqehhbABv&X-Amz-Signature=48c693aeac2a4d4fc3b3c95d8c9dae4f9b2b0a7d6c3f6948f97fd89dc9d9de20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OUNPMID%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDFfLU26Z262WW3ozENYWgO0MGpfF%2B9PIOc4Jer%2F6tL1wIhAIpYQtT1Nh2Npa8RffJC6GVuyS6c6O4TMjaS0yI2FB1tKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAUaXV%2BROcQ6FGWooq3APNdlJ%2FEpuU0%2Fs7fR%2FpChmbrG0F6GPcbZdV0NPM01WvgxWW%2B7Ea%2BTAkq9Iv4mK9VKGCwDSOQLHQ4HLhxgY4YhMG2MdGXwaxyPkOGekFw1rlwgHc23GPWR%2BrTMgnlcVF0K4v7heNWh%2BsN9IMbPxJLDhsfrzDoB24VGm4Zp%2BbaNWJnHHU3LjLGocxEeQz5UupRiVn9SdohyLliYWbABZ3zNnZGhhEnxxqo59IvVJUCRXaZU7aRSrqKSsVOt0Js46pnwc5QJcRIAGEM4WCHM7NPLQUhSZ0sh5%2FOSmrQzbjblblXYmGBokQWOVoPHeMmCHET4fyP8zniBxn9a%2B9XWA%2BSUsdx8FNnbT4HmPyJgMzIDcoV%2F6hyEMcI2RLqZEuXHRmxHDFuWokixGRMyaYBQ0k2rMyx9K6StDOfCitq%2FSo6JF4KPKJNp7XFoFybK6gqbBVE8PBCdQ18Lud3SxdmBi7Wn1t0zPfewPflfza3e2uA67a8j5qkN23CguYZfDLZIytJhJGcAvl5DHL6YDMnzzY88EjDxg7i5INfdFu%2BAeF68%2BYIRQLOpzvqst4yJXBmlPCt%2BWmK2lBZGorI1yh5Z%2Bxp3zYdY0YPRCK09OM8TSuU5%2BvtNCXrD2n18z7wSXx2zC9z63JBjqkAZPwME3BbM3bH4M2bftn%2BukRhhKdlYFBKNqXz4Gd%2Fru8oP8Kua672F%2FNT8N9nS2DssGf%2FABj6WizeSnTG%2BrfeS2SKJmVjHt8K7MxifqHxPj3eF6gxisKEkA%2BApxhBp%2FgxaxtMt%2BpjpNNpTJu9y4c%2FsKa5bknN1Xi31a%2BDuQr1izAJefAP%2BW4JLRKTcb0r31LkOg%2Bi8Xn0PWt%2F9bj9hAJqehhbABv&X-Amz-Signature=02d9c2de9c8e5946e902421d76ea3d28211d1c97ac02e7321ccbb73f544091c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OUNPMID%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDFfLU26Z262WW3ozENYWgO0MGpfF%2B9PIOc4Jer%2F6tL1wIhAIpYQtT1Nh2Npa8RffJC6GVuyS6c6O4TMjaS0yI2FB1tKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAUaXV%2BROcQ6FGWooq3APNdlJ%2FEpuU0%2Fs7fR%2FpChmbrG0F6GPcbZdV0NPM01WvgxWW%2B7Ea%2BTAkq9Iv4mK9VKGCwDSOQLHQ4HLhxgY4YhMG2MdGXwaxyPkOGekFw1rlwgHc23GPWR%2BrTMgnlcVF0K4v7heNWh%2BsN9IMbPxJLDhsfrzDoB24VGm4Zp%2BbaNWJnHHU3LjLGocxEeQz5UupRiVn9SdohyLliYWbABZ3zNnZGhhEnxxqo59IvVJUCRXaZU7aRSrqKSsVOt0Js46pnwc5QJcRIAGEM4WCHM7NPLQUhSZ0sh5%2FOSmrQzbjblblXYmGBokQWOVoPHeMmCHET4fyP8zniBxn9a%2B9XWA%2BSUsdx8FNnbT4HmPyJgMzIDcoV%2F6hyEMcI2RLqZEuXHRmxHDFuWokixGRMyaYBQ0k2rMyx9K6StDOfCitq%2FSo6JF4KPKJNp7XFoFybK6gqbBVE8PBCdQ18Lud3SxdmBi7Wn1t0zPfewPflfza3e2uA67a8j5qkN23CguYZfDLZIytJhJGcAvl5DHL6YDMnzzY88EjDxg7i5INfdFu%2BAeF68%2BYIRQLOpzvqst4yJXBmlPCt%2BWmK2lBZGorI1yh5Z%2Bxp3zYdY0YPRCK09OM8TSuU5%2BvtNCXrD2n18z7wSXx2zC9z63JBjqkAZPwME3BbM3bH4M2bftn%2BukRhhKdlYFBKNqXz4Gd%2Fru8oP8Kua672F%2FNT8N9nS2DssGf%2FABj6WizeSnTG%2BrfeS2SKJmVjHt8K7MxifqHxPj3eF6gxisKEkA%2BApxhBp%2FgxaxtMt%2BpjpNNpTJu9y4c%2FsKa5bknN1Xi31a%2BDuQr1izAJefAP%2BW4JLRKTcb0r31LkOg%2Bi8Xn0PWt%2F9bj9hAJqehhbABv&X-Amz-Signature=b8f0f14fbca34bbe0c2ca37380ac1d4911441eaefb5e091e233030621a4d5ebb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OUNPMID%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDFfLU26Z262WW3ozENYWgO0MGpfF%2B9PIOc4Jer%2F6tL1wIhAIpYQtT1Nh2Npa8RffJC6GVuyS6c6O4TMjaS0yI2FB1tKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAUaXV%2BROcQ6FGWooq3APNdlJ%2FEpuU0%2Fs7fR%2FpChmbrG0F6GPcbZdV0NPM01WvgxWW%2B7Ea%2BTAkq9Iv4mK9VKGCwDSOQLHQ4HLhxgY4YhMG2MdGXwaxyPkOGekFw1rlwgHc23GPWR%2BrTMgnlcVF0K4v7heNWh%2BsN9IMbPxJLDhsfrzDoB24VGm4Zp%2BbaNWJnHHU3LjLGocxEeQz5UupRiVn9SdohyLliYWbABZ3zNnZGhhEnxxqo59IvVJUCRXaZU7aRSrqKSsVOt0Js46pnwc5QJcRIAGEM4WCHM7NPLQUhSZ0sh5%2FOSmrQzbjblblXYmGBokQWOVoPHeMmCHET4fyP8zniBxn9a%2B9XWA%2BSUsdx8FNnbT4HmPyJgMzIDcoV%2F6hyEMcI2RLqZEuXHRmxHDFuWokixGRMyaYBQ0k2rMyx9K6StDOfCitq%2FSo6JF4KPKJNp7XFoFybK6gqbBVE8PBCdQ18Lud3SxdmBi7Wn1t0zPfewPflfza3e2uA67a8j5qkN23CguYZfDLZIytJhJGcAvl5DHL6YDMnzzY88EjDxg7i5INfdFu%2BAeF68%2BYIRQLOpzvqst4yJXBmlPCt%2BWmK2lBZGorI1yh5Z%2Bxp3zYdY0YPRCK09OM8TSuU5%2BvtNCXrD2n18z7wSXx2zC9z63JBjqkAZPwME3BbM3bH4M2bftn%2BukRhhKdlYFBKNqXz4Gd%2Fru8oP8Kua672F%2FNT8N9nS2DssGf%2FABj6WizeSnTG%2BrfeS2SKJmVjHt8K7MxifqHxPj3eF6gxisKEkA%2BApxhBp%2FgxaxtMt%2BpjpNNpTJu9y4c%2FsKa5bknN1Xi31a%2BDuQr1izAJefAP%2BW4JLRKTcb0r31LkOg%2Bi8Xn0PWt%2F9bj9hAJqehhbABv&X-Amz-Signature=9ef43ff922a0bf6fc42b48d407c8c6fcb1dfa106a72ca8ac336ed0b9f463424a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OUNPMID%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDFfLU26Z262WW3ozENYWgO0MGpfF%2B9PIOc4Jer%2F6tL1wIhAIpYQtT1Nh2Npa8RffJC6GVuyS6c6O4TMjaS0yI2FB1tKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAUaXV%2BROcQ6FGWooq3APNdlJ%2FEpuU0%2Fs7fR%2FpChmbrG0F6GPcbZdV0NPM01WvgxWW%2B7Ea%2BTAkq9Iv4mK9VKGCwDSOQLHQ4HLhxgY4YhMG2MdGXwaxyPkOGekFw1rlwgHc23GPWR%2BrTMgnlcVF0K4v7heNWh%2BsN9IMbPxJLDhsfrzDoB24VGm4Zp%2BbaNWJnHHU3LjLGocxEeQz5UupRiVn9SdohyLliYWbABZ3zNnZGhhEnxxqo59IvVJUCRXaZU7aRSrqKSsVOt0Js46pnwc5QJcRIAGEM4WCHM7NPLQUhSZ0sh5%2FOSmrQzbjblblXYmGBokQWOVoPHeMmCHET4fyP8zniBxn9a%2B9XWA%2BSUsdx8FNnbT4HmPyJgMzIDcoV%2F6hyEMcI2RLqZEuXHRmxHDFuWokixGRMyaYBQ0k2rMyx9K6StDOfCitq%2FSo6JF4KPKJNp7XFoFybK6gqbBVE8PBCdQ18Lud3SxdmBi7Wn1t0zPfewPflfza3e2uA67a8j5qkN23CguYZfDLZIytJhJGcAvl5DHL6YDMnzzY88EjDxg7i5INfdFu%2BAeF68%2BYIRQLOpzvqst4yJXBmlPCt%2BWmK2lBZGorI1yh5Z%2Bxp3zYdY0YPRCK09OM8TSuU5%2BvtNCXrD2n18z7wSXx2zC9z63JBjqkAZPwME3BbM3bH4M2bftn%2BukRhhKdlYFBKNqXz4Gd%2Fru8oP8Kua672F%2FNT8N9nS2DssGf%2FABj6WizeSnTG%2BrfeS2SKJmVjHt8K7MxifqHxPj3eF6gxisKEkA%2BApxhBp%2FgxaxtMt%2BpjpNNpTJu9y4c%2FsKa5bknN1Xi31a%2BDuQr1izAJefAP%2BW4JLRKTcb0r31LkOg%2Bi8Xn0PWt%2F9bj9hAJqehhbABv&X-Amz-Signature=5188c98862ee4332a9a813a29b74a01a2f68c4e9da8f1c6954e8ac6cb5d9727c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OUNPMID%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDFfLU26Z262WW3ozENYWgO0MGpfF%2B9PIOc4Jer%2F6tL1wIhAIpYQtT1Nh2Npa8RffJC6GVuyS6c6O4TMjaS0yI2FB1tKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAUaXV%2BROcQ6FGWooq3APNdlJ%2FEpuU0%2Fs7fR%2FpChmbrG0F6GPcbZdV0NPM01WvgxWW%2B7Ea%2BTAkq9Iv4mK9VKGCwDSOQLHQ4HLhxgY4YhMG2MdGXwaxyPkOGekFw1rlwgHc23GPWR%2BrTMgnlcVF0K4v7heNWh%2BsN9IMbPxJLDhsfrzDoB24VGm4Zp%2BbaNWJnHHU3LjLGocxEeQz5UupRiVn9SdohyLliYWbABZ3zNnZGhhEnxxqo59IvVJUCRXaZU7aRSrqKSsVOt0Js46pnwc5QJcRIAGEM4WCHM7NPLQUhSZ0sh5%2FOSmrQzbjblblXYmGBokQWOVoPHeMmCHET4fyP8zniBxn9a%2B9XWA%2BSUsdx8FNnbT4HmPyJgMzIDcoV%2F6hyEMcI2RLqZEuXHRmxHDFuWokixGRMyaYBQ0k2rMyx9K6StDOfCitq%2FSo6JF4KPKJNp7XFoFybK6gqbBVE8PBCdQ18Lud3SxdmBi7Wn1t0zPfewPflfza3e2uA67a8j5qkN23CguYZfDLZIytJhJGcAvl5DHL6YDMnzzY88EjDxg7i5INfdFu%2BAeF68%2BYIRQLOpzvqst4yJXBmlPCt%2BWmK2lBZGorI1yh5Z%2Bxp3zYdY0YPRCK09OM8TSuU5%2BvtNCXrD2n18z7wSXx2zC9z63JBjqkAZPwME3BbM3bH4M2bftn%2BukRhhKdlYFBKNqXz4Gd%2Fru8oP8Kua672F%2FNT8N9nS2DssGf%2FABj6WizeSnTG%2BrfeS2SKJmVjHt8K7MxifqHxPj3eF6gxisKEkA%2BApxhBp%2FgxaxtMt%2BpjpNNpTJu9y4c%2FsKa5bknN1Xi31a%2BDuQr1izAJefAP%2BW4JLRKTcb0r31LkOg%2Bi8Xn0PWt%2F9bj9hAJqehhbABv&X-Amz-Signature=78191bffa9f57e9decdf304daebeb3f1bde68217586da3f00dcad926fff7a8e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OUNPMID%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDFfLU26Z262WW3ozENYWgO0MGpfF%2B9PIOc4Jer%2F6tL1wIhAIpYQtT1Nh2Npa8RffJC6GVuyS6c6O4TMjaS0yI2FB1tKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAUaXV%2BROcQ6FGWooq3APNdlJ%2FEpuU0%2Fs7fR%2FpChmbrG0F6GPcbZdV0NPM01WvgxWW%2B7Ea%2BTAkq9Iv4mK9VKGCwDSOQLHQ4HLhxgY4YhMG2MdGXwaxyPkOGekFw1rlwgHc23GPWR%2BrTMgnlcVF0K4v7heNWh%2BsN9IMbPxJLDhsfrzDoB24VGm4Zp%2BbaNWJnHHU3LjLGocxEeQz5UupRiVn9SdohyLliYWbABZ3zNnZGhhEnxxqo59IvVJUCRXaZU7aRSrqKSsVOt0Js46pnwc5QJcRIAGEM4WCHM7NPLQUhSZ0sh5%2FOSmrQzbjblblXYmGBokQWOVoPHeMmCHET4fyP8zniBxn9a%2B9XWA%2BSUsdx8FNnbT4HmPyJgMzIDcoV%2F6hyEMcI2RLqZEuXHRmxHDFuWokixGRMyaYBQ0k2rMyx9K6StDOfCitq%2FSo6JF4KPKJNp7XFoFybK6gqbBVE8PBCdQ18Lud3SxdmBi7Wn1t0zPfewPflfza3e2uA67a8j5qkN23CguYZfDLZIytJhJGcAvl5DHL6YDMnzzY88EjDxg7i5INfdFu%2BAeF68%2BYIRQLOpzvqst4yJXBmlPCt%2BWmK2lBZGorI1yh5Z%2Bxp3zYdY0YPRCK09OM8TSuU5%2BvtNCXrD2n18z7wSXx2zC9z63JBjqkAZPwME3BbM3bH4M2bftn%2BukRhhKdlYFBKNqXz4Gd%2Fru8oP8Kua672F%2FNT8N9nS2DssGf%2FABj6WizeSnTG%2BrfeS2SKJmVjHt8K7MxifqHxPj3eF6gxisKEkA%2BApxhBp%2FgxaxtMt%2BpjpNNpTJu9y4c%2FsKa5bknN1Xi31a%2BDuQr1izAJefAP%2BW4JLRKTcb0r31LkOg%2Bi8Xn0PWt%2F9bj9hAJqehhbABv&X-Amz-Signature=8df133a08d3b9ff1479fe278c6da7378c1439c436218046385d881ed3d5a22d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OUNPMID%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDFfLU26Z262WW3ozENYWgO0MGpfF%2B9PIOc4Jer%2F6tL1wIhAIpYQtT1Nh2Npa8RffJC6GVuyS6c6O4TMjaS0yI2FB1tKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAUaXV%2BROcQ6FGWooq3APNdlJ%2FEpuU0%2Fs7fR%2FpChmbrG0F6GPcbZdV0NPM01WvgxWW%2B7Ea%2BTAkq9Iv4mK9VKGCwDSOQLHQ4HLhxgY4YhMG2MdGXwaxyPkOGekFw1rlwgHc23GPWR%2BrTMgnlcVF0K4v7heNWh%2BsN9IMbPxJLDhsfrzDoB24VGm4Zp%2BbaNWJnHHU3LjLGocxEeQz5UupRiVn9SdohyLliYWbABZ3zNnZGhhEnxxqo59IvVJUCRXaZU7aRSrqKSsVOt0Js46pnwc5QJcRIAGEM4WCHM7NPLQUhSZ0sh5%2FOSmrQzbjblblXYmGBokQWOVoPHeMmCHET4fyP8zniBxn9a%2B9XWA%2BSUsdx8FNnbT4HmPyJgMzIDcoV%2F6hyEMcI2RLqZEuXHRmxHDFuWokixGRMyaYBQ0k2rMyx9K6StDOfCitq%2FSo6JF4KPKJNp7XFoFybK6gqbBVE8PBCdQ18Lud3SxdmBi7Wn1t0zPfewPflfza3e2uA67a8j5qkN23CguYZfDLZIytJhJGcAvl5DHL6YDMnzzY88EjDxg7i5INfdFu%2BAeF68%2BYIRQLOpzvqst4yJXBmlPCt%2BWmK2lBZGorI1yh5Z%2Bxp3zYdY0YPRCK09OM8TSuU5%2BvtNCXrD2n18z7wSXx2zC9z63JBjqkAZPwME3BbM3bH4M2bftn%2BukRhhKdlYFBKNqXz4Gd%2Fru8oP8Kua672F%2FNT8N9nS2DssGf%2FABj6WizeSnTG%2BrfeS2SKJmVjHt8K7MxifqHxPj3eF6gxisKEkA%2BApxhBp%2FgxaxtMt%2BpjpNNpTJu9y4c%2FsKa5bknN1Xi31a%2BDuQr1izAJefAP%2BW4JLRKTcb0r31LkOg%2Bi8Xn0PWt%2F9bj9hAJqehhbABv&X-Amz-Signature=1c137748ee352c0cd80192125e250e7bd3d321ec0e25b96dcf5f97e80dff06aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OUNPMID%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDFfLU26Z262WW3ozENYWgO0MGpfF%2B9PIOc4Jer%2F6tL1wIhAIpYQtT1Nh2Npa8RffJC6GVuyS6c6O4TMjaS0yI2FB1tKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAUaXV%2BROcQ6FGWooq3APNdlJ%2FEpuU0%2Fs7fR%2FpChmbrG0F6GPcbZdV0NPM01WvgxWW%2B7Ea%2BTAkq9Iv4mK9VKGCwDSOQLHQ4HLhxgY4YhMG2MdGXwaxyPkOGekFw1rlwgHc23GPWR%2BrTMgnlcVF0K4v7heNWh%2BsN9IMbPxJLDhsfrzDoB24VGm4Zp%2BbaNWJnHHU3LjLGocxEeQz5UupRiVn9SdohyLliYWbABZ3zNnZGhhEnxxqo59IvVJUCRXaZU7aRSrqKSsVOt0Js46pnwc5QJcRIAGEM4WCHM7NPLQUhSZ0sh5%2FOSmrQzbjblblXYmGBokQWOVoPHeMmCHET4fyP8zniBxn9a%2B9XWA%2BSUsdx8FNnbT4HmPyJgMzIDcoV%2F6hyEMcI2RLqZEuXHRmxHDFuWokixGRMyaYBQ0k2rMyx9K6StDOfCitq%2FSo6JF4KPKJNp7XFoFybK6gqbBVE8PBCdQ18Lud3SxdmBi7Wn1t0zPfewPflfza3e2uA67a8j5qkN23CguYZfDLZIytJhJGcAvl5DHL6YDMnzzY88EjDxg7i5INfdFu%2BAeF68%2BYIRQLOpzvqst4yJXBmlPCt%2BWmK2lBZGorI1yh5Z%2Bxp3zYdY0YPRCK09OM8TSuU5%2BvtNCXrD2n18z7wSXx2zC9z63JBjqkAZPwME3BbM3bH4M2bftn%2BukRhhKdlYFBKNqXz4Gd%2Fru8oP8Kua672F%2FNT8N9nS2DssGf%2FABj6WizeSnTG%2BrfeS2SKJmVjHt8K7MxifqHxPj3eF6gxisKEkA%2BApxhBp%2FgxaxtMt%2BpjpNNpTJu9y4c%2FsKa5bknN1Xi31a%2BDuQr1izAJefAP%2BW4JLRKTcb0r31LkOg%2Bi8Xn0PWt%2F9bj9hAJqehhbABv&X-Amz-Signature=6f0c168c670eda60a130f19cf47a500777a1c566457d98dce4d5a5912ec00993&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OUNPMID%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDFfLU26Z262WW3ozENYWgO0MGpfF%2B9PIOc4Jer%2F6tL1wIhAIpYQtT1Nh2Npa8RffJC6GVuyS6c6O4TMjaS0yI2FB1tKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAUaXV%2BROcQ6FGWooq3APNdlJ%2FEpuU0%2Fs7fR%2FpChmbrG0F6GPcbZdV0NPM01WvgxWW%2B7Ea%2BTAkq9Iv4mK9VKGCwDSOQLHQ4HLhxgY4YhMG2MdGXwaxyPkOGekFw1rlwgHc23GPWR%2BrTMgnlcVF0K4v7heNWh%2BsN9IMbPxJLDhsfrzDoB24VGm4Zp%2BbaNWJnHHU3LjLGocxEeQz5UupRiVn9SdohyLliYWbABZ3zNnZGhhEnxxqo59IvVJUCRXaZU7aRSrqKSsVOt0Js46pnwc5QJcRIAGEM4WCHM7NPLQUhSZ0sh5%2FOSmrQzbjblblXYmGBokQWOVoPHeMmCHET4fyP8zniBxn9a%2B9XWA%2BSUsdx8FNnbT4HmPyJgMzIDcoV%2F6hyEMcI2RLqZEuXHRmxHDFuWokixGRMyaYBQ0k2rMyx9K6StDOfCitq%2FSo6JF4KPKJNp7XFoFybK6gqbBVE8PBCdQ18Lud3SxdmBi7Wn1t0zPfewPflfza3e2uA67a8j5qkN23CguYZfDLZIytJhJGcAvl5DHL6YDMnzzY88EjDxg7i5INfdFu%2BAeF68%2BYIRQLOpzvqst4yJXBmlPCt%2BWmK2lBZGorI1yh5Z%2Bxp3zYdY0YPRCK09OM8TSuU5%2BvtNCXrD2n18z7wSXx2zC9z63JBjqkAZPwME3BbM3bH4M2bftn%2BukRhhKdlYFBKNqXz4Gd%2Fru8oP8Kua672F%2FNT8N9nS2DssGf%2FABj6WizeSnTG%2BrfeS2SKJmVjHt8K7MxifqHxPj3eF6gxisKEkA%2BApxhBp%2FgxaxtMt%2BpjpNNpTJu9y4c%2FsKa5bknN1Xi31a%2BDuQr1izAJefAP%2BW4JLRKTcb0r31LkOg%2Bi8Xn0PWt%2F9bj9hAJqehhbABv&X-Amz-Signature=283f90b547321ab03343bc67e88bf33e592958b41ed20728009fcb40375f311c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

