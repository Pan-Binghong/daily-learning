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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZ5GEZU%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIEGVJaEk2wO4Ps%2BwkOaVW%2BiCxkeIwR63fZ4Kbr%2BHX9rfAiAt0WddrUouqEIEHMLzP%2FYUKmsHqUIxjYJg2S0evYQ9Hir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM%2BNdh1cC6N0EbwIIiKtwDozdpfW%2FjYmScSFcgiPhLQOE%2FaqTSOwb2SPLP61ZLzCCh5qVTkXJfLTZZANdu1hpGIu3uCFsF7Cz6VxWpYRyLaiPWi1KwDVSaNpe8d34dCdDGFrEyhAHYxYBEgperkvwPB8ITjfjnVLgrmRERxbt1cSqD5Qq%2FZGlS%2BPuQ40VM6qn5pnp18nX3yRyx175xHEJWEWY1kNiQUbrMMK2tqykh1Rciotq835zXxtt3H%2FbIS6fArmg%2FSYrc1qS1842lC55rtx9klAMqbFF2sGfY4UppEva8Yr85dBOvYkqDHk7KRkBpHSSbiR18h9X9S%2FiyHZdqqLmVU5bXQXT0OqZf4qyLL%2B1MAC5MoC8rY6uNWJOgSRrE89Dp6jb%2FQvex1AEI0ip8%2FHlpRdWEwI8ayDLRBehopX8NGNmHeODrIpAO7JFGIUeNy3oN%2BznEy9Lop%2FtYflefCOZqUziCkuz%2F5GREi8shZLEmtcEwVMJne8VgyUZW40M5yDU9MB7c11gav1d0KRawEDbY2dkCLrp7180MyirowBlC47wUbKdITM4muQ7gHmVTeg9jC3oPOZRsFxHyFLMWEYqs3xA7h0AET1%2BV2y1udbrUSzx9rjRnZo05%2B7lRooIoCXShx3shrs27XqMwt8TmygY6pgEg4O8AHTYb%2FdIh%2F3OyzQn%2FxJ1miwLTaeu4JM4QMbv2gtFV1hmY2osL5TidPj%2FMQ9CnCDkZDDGymxcSVYYwAGHX3Wk0pXx0fCE0UplPTav5APVEFpSu5zKqxM8qoNnSPKSBePkRXsf%2Fd0Ms2Yej6OyKRNW3Ot1HQf2wuLJOiOhkq7xYrDTgyfYqWBoXHrsyejH7au%2FK6rXvObG7qHh9QkPAll0usQrV&X-Amz-Signature=cec3ff5aa0a39fef36a9cb67b467fb15b662319ece703bde8ae5263bdba29070&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZ5GEZU%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIEGVJaEk2wO4Ps%2BwkOaVW%2BiCxkeIwR63fZ4Kbr%2BHX9rfAiAt0WddrUouqEIEHMLzP%2FYUKmsHqUIxjYJg2S0evYQ9Hir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM%2BNdh1cC6N0EbwIIiKtwDozdpfW%2FjYmScSFcgiPhLQOE%2FaqTSOwb2SPLP61ZLzCCh5qVTkXJfLTZZANdu1hpGIu3uCFsF7Cz6VxWpYRyLaiPWi1KwDVSaNpe8d34dCdDGFrEyhAHYxYBEgperkvwPB8ITjfjnVLgrmRERxbt1cSqD5Qq%2FZGlS%2BPuQ40VM6qn5pnp18nX3yRyx175xHEJWEWY1kNiQUbrMMK2tqykh1Rciotq835zXxtt3H%2FbIS6fArmg%2FSYrc1qS1842lC55rtx9klAMqbFF2sGfY4UppEva8Yr85dBOvYkqDHk7KRkBpHSSbiR18h9X9S%2FiyHZdqqLmVU5bXQXT0OqZf4qyLL%2B1MAC5MoC8rY6uNWJOgSRrE89Dp6jb%2FQvex1AEI0ip8%2FHlpRdWEwI8ayDLRBehopX8NGNmHeODrIpAO7JFGIUeNy3oN%2BznEy9Lop%2FtYflefCOZqUziCkuz%2F5GREi8shZLEmtcEwVMJne8VgyUZW40M5yDU9MB7c11gav1d0KRawEDbY2dkCLrp7180MyirowBlC47wUbKdITM4muQ7gHmVTeg9jC3oPOZRsFxHyFLMWEYqs3xA7h0AET1%2BV2y1udbrUSzx9rjRnZo05%2B7lRooIoCXShx3shrs27XqMwt8TmygY6pgEg4O8AHTYb%2FdIh%2F3OyzQn%2FxJ1miwLTaeu4JM4QMbv2gtFV1hmY2osL5TidPj%2FMQ9CnCDkZDDGymxcSVYYwAGHX3Wk0pXx0fCE0UplPTav5APVEFpSu5zKqxM8qoNnSPKSBePkRXsf%2Fd0Ms2Yej6OyKRNW3Ot1HQf2wuLJOiOhkq7xYrDTgyfYqWBoXHrsyejH7au%2FK6rXvObG7qHh9QkPAll0usQrV&X-Amz-Signature=2a5aca8d31c528be774373a82c9d75a2087ec0df1b4ef412f276164180d0aa61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZ5GEZU%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIEGVJaEk2wO4Ps%2BwkOaVW%2BiCxkeIwR63fZ4Kbr%2BHX9rfAiAt0WddrUouqEIEHMLzP%2FYUKmsHqUIxjYJg2S0evYQ9Hir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM%2BNdh1cC6N0EbwIIiKtwDozdpfW%2FjYmScSFcgiPhLQOE%2FaqTSOwb2SPLP61ZLzCCh5qVTkXJfLTZZANdu1hpGIu3uCFsF7Cz6VxWpYRyLaiPWi1KwDVSaNpe8d34dCdDGFrEyhAHYxYBEgperkvwPB8ITjfjnVLgrmRERxbt1cSqD5Qq%2FZGlS%2BPuQ40VM6qn5pnp18nX3yRyx175xHEJWEWY1kNiQUbrMMK2tqykh1Rciotq835zXxtt3H%2FbIS6fArmg%2FSYrc1qS1842lC55rtx9klAMqbFF2sGfY4UppEva8Yr85dBOvYkqDHk7KRkBpHSSbiR18h9X9S%2FiyHZdqqLmVU5bXQXT0OqZf4qyLL%2B1MAC5MoC8rY6uNWJOgSRrE89Dp6jb%2FQvex1AEI0ip8%2FHlpRdWEwI8ayDLRBehopX8NGNmHeODrIpAO7JFGIUeNy3oN%2BznEy9Lop%2FtYflefCOZqUziCkuz%2F5GREi8shZLEmtcEwVMJne8VgyUZW40M5yDU9MB7c11gav1d0KRawEDbY2dkCLrp7180MyirowBlC47wUbKdITM4muQ7gHmVTeg9jC3oPOZRsFxHyFLMWEYqs3xA7h0AET1%2BV2y1udbrUSzx9rjRnZo05%2B7lRooIoCXShx3shrs27XqMwt8TmygY6pgEg4O8AHTYb%2FdIh%2F3OyzQn%2FxJ1miwLTaeu4JM4QMbv2gtFV1hmY2osL5TidPj%2FMQ9CnCDkZDDGymxcSVYYwAGHX3Wk0pXx0fCE0UplPTav5APVEFpSu5zKqxM8qoNnSPKSBePkRXsf%2Fd0Ms2Yej6OyKRNW3Ot1HQf2wuLJOiOhkq7xYrDTgyfYqWBoXHrsyejH7au%2FK6rXvObG7qHh9QkPAll0usQrV&X-Amz-Signature=44ce51912c5a570785acf47473a6b7ccab12fa8a36605f2197f97365d2765655&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZ5GEZU%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIEGVJaEk2wO4Ps%2BwkOaVW%2BiCxkeIwR63fZ4Kbr%2BHX9rfAiAt0WddrUouqEIEHMLzP%2FYUKmsHqUIxjYJg2S0evYQ9Hir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM%2BNdh1cC6N0EbwIIiKtwDozdpfW%2FjYmScSFcgiPhLQOE%2FaqTSOwb2SPLP61ZLzCCh5qVTkXJfLTZZANdu1hpGIu3uCFsF7Cz6VxWpYRyLaiPWi1KwDVSaNpe8d34dCdDGFrEyhAHYxYBEgperkvwPB8ITjfjnVLgrmRERxbt1cSqD5Qq%2FZGlS%2BPuQ40VM6qn5pnp18nX3yRyx175xHEJWEWY1kNiQUbrMMK2tqykh1Rciotq835zXxtt3H%2FbIS6fArmg%2FSYrc1qS1842lC55rtx9klAMqbFF2sGfY4UppEva8Yr85dBOvYkqDHk7KRkBpHSSbiR18h9X9S%2FiyHZdqqLmVU5bXQXT0OqZf4qyLL%2B1MAC5MoC8rY6uNWJOgSRrE89Dp6jb%2FQvex1AEI0ip8%2FHlpRdWEwI8ayDLRBehopX8NGNmHeODrIpAO7JFGIUeNy3oN%2BznEy9Lop%2FtYflefCOZqUziCkuz%2F5GREi8shZLEmtcEwVMJne8VgyUZW40M5yDU9MB7c11gav1d0KRawEDbY2dkCLrp7180MyirowBlC47wUbKdITM4muQ7gHmVTeg9jC3oPOZRsFxHyFLMWEYqs3xA7h0AET1%2BV2y1udbrUSzx9rjRnZo05%2B7lRooIoCXShx3shrs27XqMwt8TmygY6pgEg4O8AHTYb%2FdIh%2F3OyzQn%2FxJ1miwLTaeu4JM4QMbv2gtFV1hmY2osL5TidPj%2FMQ9CnCDkZDDGymxcSVYYwAGHX3Wk0pXx0fCE0UplPTav5APVEFpSu5zKqxM8qoNnSPKSBePkRXsf%2Fd0Ms2Yej6OyKRNW3Ot1HQf2wuLJOiOhkq7xYrDTgyfYqWBoXHrsyejH7au%2FK6rXvObG7qHh9QkPAll0usQrV&X-Amz-Signature=57f25044f005de3ae4edcb7b125d9a45549b4404b5cc62eda8a637bf7e245023&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZ5GEZU%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIEGVJaEk2wO4Ps%2BwkOaVW%2BiCxkeIwR63fZ4Kbr%2BHX9rfAiAt0WddrUouqEIEHMLzP%2FYUKmsHqUIxjYJg2S0evYQ9Hir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM%2BNdh1cC6N0EbwIIiKtwDozdpfW%2FjYmScSFcgiPhLQOE%2FaqTSOwb2SPLP61ZLzCCh5qVTkXJfLTZZANdu1hpGIu3uCFsF7Cz6VxWpYRyLaiPWi1KwDVSaNpe8d34dCdDGFrEyhAHYxYBEgperkvwPB8ITjfjnVLgrmRERxbt1cSqD5Qq%2FZGlS%2BPuQ40VM6qn5pnp18nX3yRyx175xHEJWEWY1kNiQUbrMMK2tqykh1Rciotq835zXxtt3H%2FbIS6fArmg%2FSYrc1qS1842lC55rtx9klAMqbFF2sGfY4UppEva8Yr85dBOvYkqDHk7KRkBpHSSbiR18h9X9S%2FiyHZdqqLmVU5bXQXT0OqZf4qyLL%2B1MAC5MoC8rY6uNWJOgSRrE89Dp6jb%2FQvex1AEI0ip8%2FHlpRdWEwI8ayDLRBehopX8NGNmHeODrIpAO7JFGIUeNy3oN%2BznEy9Lop%2FtYflefCOZqUziCkuz%2F5GREi8shZLEmtcEwVMJne8VgyUZW40M5yDU9MB7c11gav1d0KRawEDbY2dkCLrp7180MyirowBlC47wUbKdITM4muQ7gHmVTeg9jC3oPOZRsFxHyFLMWEYqs3xA7h0AET1%2BV2y1udbrUSzx9rjRnZo05%2B7lRooIoCXShx3shrs27XqMwt8TmygY6pgEg4O8AHTYb%2FdIh%2F3OyzQn%2FxJ1miwLTaeu4JM4QMbv2gtFV1hmY2osL5TidPj%2FMQ9CnCDkZDDGymxcSVYYwAGHX3Wk0pXx0fCE0UplPTav5APVEFpSu5zKqxM8qoNnSPKSBePkRXsf%2Fd0Ms2Yej6OyKRNW3Ot1HQf2wuLJOiOhkq7xYrDTgyfYqWBoXHrsyejH7au%2FK6rXvObG7qHh9QkPAll0usQrV&X-Amz-Signature=287d07e397438041e289ad028a00d81fff7b0871cbb98595efb92dfe0aedd909&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZ5GEZU%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIEGVJaEk2wO4Ps%2BwkOaVW%2BiCxkeIwR63fZ4Kbr%2BHX9rfAiAt0WddrUouqEIEHMLzP%2FYUKmsHqUIxjYJg2S0evYQ9Hir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM%2BNdh1cC6N0EbwIIiKtwDozdpfW%2FjYmScSFcgiPhLQOE%2FaqTSOwb2SPLP61ZLzCCh5qVTkXJfLTZZANdu1hpGIu3uCFsF7Cz6VxWpYRyLaiPWi1KwDVSaNpe8d34dCdDGFrEyhAHYxYBEgperkvwPB8ITjfjnVLgrmRERxbt1cSqD5Qq%2FZGlS%2BPuQ40VM6qn5pnp18nX3yRyx175xHEJWEWY1kNiQUbrMMK2tqykh1Rciotq835zXxtt3H%2FbIS6fArmg%2FSYrc1qS1842lC55rtx9klAMqbFF2sGfY4UppEva8Yr85dBOvYkqDHk7KRkBpHSSbiR18h9X9S%2FiyHZdqqLmVU5bXQXT0OqZf4qyLL%2B1MAC5MoC8rY6uNWJOgSRrE89Dp6jb%2FQvex1AEI0ip8%2FHlpRdWEwI8ayDLRBehopX8NGNmHeODrIpAO7JFGIUeNy3oN%2BznEy9Lop%2FtYflefCOZqUziCkuz%2F5GREi8shZLEmtcEwVMJne8VgyUZW40M5yDU9MB7c11gav1d0KRawEDbY2dkCLrp7180MyirowBlC47wUbKdITM4muQ7gHmVTeg9jC3oPOZRsFxHyFLMWEYqs3xA7h0AET1%2BV2y1udbrUSzx9rjRnZo05%2B7lRooIoCXShx3shrs27XqMwt8TmygY6pgEg4O8AHTYb%2FdIh%2F3OyzQn%2FxJ1miwLTaeu4JM4QMbv2gtFV1hmY2osL5TidPj%2FMQ9CnCDkZDDGymxcSVYYwAGHX3Wk0pXx0fCE0UplPTav5APVEFpSu5zKqxM8qoNnSPKSBePkRXsf%2Fd0Ms2Yej6OyKRNW3Ot1HQf2wuLJOiOhkq7xYrDTgyfYqWBoXHrsyejH7au%2FK6rXvObG7qHh9QkPAll0usQrV&X-Amz-Signature=a06fc921be996441bf3b3c55e74c16a915f38d8d4fefa8a5b38fd6da433d46f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZ5GEZU%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIEGVJaEk2wO4Ps%2BwkOaVW%2BiCxkeIwR63fZ4Kbr%2BHX9rfAiAt0WddrUouqEIEHMLzP%2FYUKmsHqUIxjYJg2S0evYQ9Hir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM%2BNdh1cC6N0EbwIIiKtwDozdpfW%2FjYmScSFcgiPhLQOE%2FaqTSOwb2SPLP61ZLzCCh5qVTkXJfLTZZANdu1hpGIu3uCFsF7Cz6VxWpYRyLaiPWi1KwDVSaNpe8d34dCdDGFrEyhAHYxYBEgperkvwPB8ITjfjnVLgrmRERxbt1cSqD5Qq%2FZGlS%2BPuQ40VM6qn5pnp18nX3yRyx175xHEJWEWY1kNiQUbrMMK2tqykh1Rciotq835zXxtt3H%2FbIS6fArmg%2FSYrc1qS1842lC55rtx9klAMqbFF2sGfY4UppEva8Yr85dBOvYkqDHk7KRkBpHSSbiR18h9X9S%2FiyHZdqqLmVU5bXQXT0OqZf4qyLL%2B1MAC5MoC8rY6uNWJOgSRrE89Dp6jb%2FQvex1AEI0ip8%2FHlpRdWEwI8ayDLRBehopX8NGNmHeODrIpAO7JFGIUeNy3oN%2BznEy9Lop%2FtYflefCOZqUziCkuz%2F5GREi8shZLEmtcEwVMJne8VgyUZW40M5yDU9MB7c11gav1d0KRawEDbY2dkCLrp7180MyirowBlC47wUbKdITM4muQ7gHmVTeg9jC3oPOZRsFxHyFLMWEYqs3xA7h0AET1%2BV2y1udbrUSzx9rjRnZo05%2B7lRooIoCXShx3shrs27XqMwt8TmygY6pgEg4O8AHTYb%2FdIh%2F3OyzQn%2FxJ1miwLTaeu4JM4QMbv2gtFV1hmY2osL5TidPj%2FMQ9CnCDkZDDGymxcSVYYwAGHX3Wk0pXx0fCE0UplPTav5APVEFpSu5zKqxM8qoNnSPKSBePkRXsf%2Fd0Ms2Yej6OyKRNW3Ot1HQf2wuLJOiOhkq7xYrDTgyfYqWBoXHrsyejH7au%2FK6rXvObG7qHh9QkPAll0usQrV&X-Amz-Signature=a9eb4be417be11cac3d8884ba8b4bcb5347ee759d3ca02424d83a81acfc2ec2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZ5GEZU%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIEGVJaEk2wO4Ps%2BwkOaVW%2BiCxkeIwR63fZ4Kbr%2BHX9rfAiAt0WddrUouqEIEHMLzP%2FYUKmsHqUIxjYJg2S0evYQ9Hir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM%2BNdh1cC6N0EbwIIiKtwDozdpfW%2FjYmScSFcgiPhLQOE%2FaqTSOwb2SPLP61ZLzCCh5qVTkXJfLTZZANdu1hpGIu3uCFsF7Cz6VxWpYRyLaiPWi1KwDVSaNpe8d34dCdDGFrEyhAHYxYBEgperkvwPB8ITjfjnVLgrmRERxbt1cSqD5Qq%2FZGlS%2BPuQ40VM6qn5pnp18nX3yRyx175xHEJWEWY1kNiQUbrMMK2tqykh1Rciotq835zXxtt3H%2FbIS6fArmg%2FSYrc1qS1842lC55rtx9klAMqbFF2sGfY4UppEva8Yr85dBOvYkqDHk7KRkBpHSSbiR18h9X9S%2FiyHZdqqLmVU5bXQXT0OqZf4qyLL%2B1MAC5MoC8rY6uNWJOgSRrE89Dp6jb%2FQvex1AEI0ip8%2FHlpRdWEwI8ayDLRBehopX8NGNmHeODrIpAO7JFGIUeNy3oN%2BznEy9Lop%2FtYflefCOZqUziCkuz%2F5GREi8shZLEmtcEwVMJne8VgyUZW40M5yDU9MB7c11gav1d0KRawEDbY2dkCLrp7180MyirowBlC47wUbKdITM4muQ7gHmVTeg9jC3oPOZRsFxHyFLMWEYqs3xA7h0AET1%2BV2y1udbrUSzx9rjRnZo05%2B7lRooIoCXShx3shrs27XqMwt8TmygY6pgEg4O8AHTYb%2FdIh%2F3OyzQn%2FxJ1miwLTaeu4JM4QMbv2gtFV1hmY2osL5TidPj%2FMQ9CnCDkZDDGymxcSVYYwAGHX3Wk0pXx0fCE0UplPTav5APVEFpSu5zKqxM8qoNnSPKSBePkRXsf%2Fd0Ms2Yej6OyKRNW3Ot1HQf2wuLJOiOhkq7xYrDTgyfYqWBoXHrsyejH7au%2FK6rXvObG7qHh9QkPAll0usQrV&X-Amz-Signature=99e2e5c3bed1b99158c1953d3d76d1efe4b157dab431266c931fcc0b2b050f0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZ5GEZU%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIEGVJaEk2wO4Ps%2BwkOaVW%2BiCxkeIwR63fZ4Kbr%2BHX9rfAiAt0WddrUouqEIEHMLzP%2FYUKmsHqUIxjYJg2S0evYQ9Hir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM%2BNdh1cC6N0EbwIIiKtwDozdpfW%2FjYmScSFcgiPhLQOE%2FaqTSOwb2SPLP61ZLzCCh5qVTkXJfLTZZANdu1hpGIu3uCFsF7Cz6VxWpYRyLaiPWi1KwDVSaNpe8d34dCdDGFrEyhAHYxYBEgperkvwPB8ITjfjnVLgrmRERxbt1cSqD5Qq%2FZGlS%2BPuQ40VM6qn5pnp18nX3yRyx175xHEJWEWY1kNiQUbrMMK2tqykh1Rciotq835zXxtt3H%2FbIS6fArmg%2FSYrc1qS1842lC55rtx9klAMqbFF2sGfY4UppEva8Yr85dBOvYkqDHk7KRkBpHSSbiR18h9X9S%2FiyHZdqqLmVU5bXQXT0OqZf4qyLL%2B1MAC5MoC8rY6uNWJOgSRrE89Dp6jb%2FQvex1AEI0ip8%2FHlpRdWEwI8ayDLRBehopX8NGNmHeODrIpAO7JFGIUeNy3oN%2BznEy9Lop%2FtYflefCOZqUziCkuz%2F5GREi8shZLEmtcEwVMJne8VgyUZW40M5yDU9MB7c11gav1d0KRawEDbY2dkCLrp7180MyirowBlC47wUbKdITM4muQ7gHmVTeg9jC3oPOZRsFxHyFLMWEYqs3xA7h0AET1%2BV2y1udbrUSzx9rjRnZo05%2B7lRooIoCXShx3shrs27XqMwt8TmygY6pgEg4O8AHTYb%2FdIh%2F3OyzQn%2FxJ1miwLTaeu4JM4QMbv2gtFV1hmY2osL5TidPj%2FMQ9CnCDkZDDGymxcSVYYwAGHX3Wk0pXx0fCE0UplPTav5APVEFpSu5zKqxM8qoNnSPKSBePkRXsf%2Fd0Ms2Yej6OyKRNW3Ot1HQf2wuLJOiOhkq7xYrDTgyfYqWBoXHrsyejH7au%2FK6rXvObG7qHh9QkPAll0usQrV&X-Amz-Signature=3aea5ef091f786f9dfe52456d2b37ecb509db60c404b2c06c899fe34826bd8fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZ5GEZU%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIEGVJaEk2wO4Ps%2BwkOaVW%2BiCxkeIwR63fZ4Kbr%2BHX9rfAiAt0WddrUouqEIEHMLzP%2FYUKmsHqUIxjYJg2S0evYQ9Hir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM%2BNdh1cC6N0EbwIIiKtwDozdpfW%2FjYmScSFcgiPhLQOE%2FaqTSOwb2SPLP61ZLzCCh5qVTkXJfLTZZANdu1hpGIu3uCFsF7Cz6VxWpYRyLaiPWi1KwDVSaNpe8d34dCdDGFrEyhAHYxYBEgperkvwPB8ITjfjnVLgrmRERxbt1cSqD5Qq%2FZGlS%2BPuQ40VM6qn5pnp18nX3yRyx175xHEJWEWY1kNiQUbrMMK2tqykh1Rciotq835zXxtt3H%2FbIS6fArmg%2FSYrc1qS1842lC55rtx9klAMqbFF2sGfY4UppEva8Yr85dBOvYkqDHk7KRkBpHSSbiR18h9X9S%2FiyHZdqqLmVU5bXQXT0OqZf4qyLL%2B1MAC5MoC8rY6uNWJOgSRrE89Dp6jb%2FQvex1AEI0ip8%2FHlpRdWEwI8ayDLRBehopX8NGNmHeODrIpAO7JFGIUeNy3oN%2BznEy9Lop%2FtYflefCOZqUziCkuz%2F5GREi8shZLEmtcEwVMJne8VgyUZW40M5yDU9MB7c11gav1d0KRawEDbY2dkCLrp7180MyirowBlC47wUbKdITM4muQ7gHmVTeg9jC3oPOZRsFxHyFLMWEYqs3xA7h0AET1%2BV2y1udbrUSzx9rjRnZo05%2B7lRooIoCXShx3shrs27XqMwt8TmygY6pgEg4O8AHTYb%2FdIh%2F3OyzQn%2FxJ1miwLTaeu4JM4QMbv2gtFV1hmY2osL5TidPj%2FMQ9CnCDkZDDGymxcSVYYwAGHX3Wk0pXx0fCE0UplPTav5APVEFpSu5zKqxM8qoNnSPKSBePkRXsf%2Fd0Ms2Yej6OyKRNW3Ot1HQf2wuLJOiOhkq7xYrDTgyfYqWBoXHrsyejH7au%2FK6rXvObG7qHh9QkPAll0usQrV&X-Amz-Signature=2cf55e705c6223f26b42dde7b475345c22430170de8195d2f17c19331f5e7d44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

