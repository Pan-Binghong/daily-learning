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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635S7WC56%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIB9PlOjtYxtxI7XLsKggP2B5TTi89Io%2FIabRckF9Dp%2BYAiEAp85ScL%2F1xfpaEW7dH6wKYQmHJGicmj02QHdVnYY1Mj8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIv3UDdSf9nNTu3IVircA1zkJH6yP7ptfGzShCY6MQInTAbCE6kknlLPRkeZBrTHgVI3AQdLoakJ%2Bq%2FVs5yRelJhRjWMmFkheG6n78rf16uXkZpHdRxA8uj0pxSMcaTwW5a%2F9qYD6mQxTs%2FXps7vGAo6RzhX%2BH2r7MjFoOeEq%2FaxVGNZWDOrJwoZhjwhgPDajLc37P5dzNu5RLT%2BrQ7C76OBfzfbF088uj3thBtvF2xCkfXOMfDGg8fNPZRDxSBfJRlzLjk6wN3sOiQmFXxOjw8AXeuA6LsqnU4ZwpQ3jP00UmjID2CDp%2BtfDkZ1%2FQb26B%2BXDqH%2FRZ2B9xY1UO0JKZ1zRbjUfMghdqzMyUPIsMOADkozT6Yh6AwFa6JAWuiIHlgIqh2dP6NOQ7ZYb2V2Rnucep9elLH%2FUX20l3uNP3ZjrzNblmOglaB51vYwAfiqsNftxMYRyuqLWSZhF%2FKngmg1aKGu6jiX1EWL9onCLRmi1lTD3BkBQCMv7tOsWxoN6GvGz83QX%2BmQeuA1t0UMpg2Wt%2FWS3kRXbqcmrmtNNt8fefF9TN%2FOwOQgp4MfnSSYP6wtWMxib5JTAH6WFL%2BOSV2EbryRf1Dj5t3coTChcgoj9NAqFAkrDhq6p865KjlAgIiWpsvwybbOi%2BP2MMKXls8GOqUBwiEi3LbBw8CSZYAJUNNNcSnvcAK%2FNqWM9LeVigMx1%2FyoTM0MVLnZ3mhJvsmq0iG9uhqdvCfKj5%2FxiUP8NBL8Vhf3KwDjN38vmlp%2BtwcOgKOQ3bsreGLYxp6dW7aTkL5cnyesyipcXnRcP3%2BMBqD%2Bc1Dd0Yf0yQxiCiKrl9XPVnEy53B1cvXCNyCILjHvV12iOM9lJnP0embgxv7K7zCt7mFZGOWc&X-Amz-Signature=83889af856ad16afee12d332645f14b88902367fdbd7d27977d1c8a5458e40df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635S7WC56%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIB9PlOjtYxtxI7XLsKggP2B5TTi89Io%2FIabRckF9Dp%2BYAiEAp85ScL%2F1xfpaEW7dH6wKYQmHJGicmj02QHdVnYY1Mj8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIv3UDdSf9nNTu3IVircA1zkJH6yP7ptfGzShCY6MQInTAbCE6kknlLPRkeZBrTHgVI3AQdLoakJ%2Bq%2FVs5yRelJhRjWMmFkheG6n78rf16uXkZpHdRxA8uj0pxSMcaTwW5a%2F9qYD6mQxTs%2FXps7vGAo6RzhX%2BH2r7MjFoOeEq%2FaxVGNZWDOrJwoZhjwhgPDajLc37P5dzNu5RLT%2BrQ7C76OBfzfbF088uj3thBtvF2xCkfXOMfDGg8fNPZRDxSBfJRlzLjk6wN3sOiQmFXxOjw8AXeuA6LsqnU4ZwpQ3jP00UmjID2CDp%2BtfDkZ1%2FQb26B%2BXDqH%2FRZ2B9xY1UO0JKZ1zRbjUfMghdqzMyUPIsMOADkozT6Yh6AwFa6JAWuiIHlgIqh2dP6NOQ7ZYb2V2Rnucep9elLH%2FUX20l3uNP3ZjrzNblmOglaB51vYwAfiqsNftxMYRyuqLWSZhF%2FKngmg1aKGu6jiX1EWL9onCLRmi1lTD3BkBQCMv7tOsWxoN6GvGz83QX%2BmQeuA1t0UMpg2Wt%2FWS3kRXbqcmrmtNNt8fefF9TN%2FOwOQgp4MfnSSYP6wtWMxib5JTAH6WFL%2BOSV2EbryRf1Dj5t3coTChcgoj9NAqFAkrDhq6p865KjlAgIiWpsvwybbOi%2BP2MMKXls8GOqUBwiEi3LbBw8CSZYAJUNNNcSnvcAK%2FNqWM9LeVigMx1%2FyoTM0MVLnZ3mhJvsmq0iG9uhqdvCfKj5%2FxiUP8NBL8Vhf3KwDjN38vmlp%2BtwcOgKOQ3bsreGLYxp6dW7aTkL5cnyesyipcXnRcP3%2BMBqD%2Bc1Dd0Yf0yQxiCiKrl9XPVnEy53B1cvXCNyCILjHvV12iOM9lJnP0embgxv7K7zCt7mFZGOWc&X-Amz-Signature=31b96258b7b0ddb796e491326631e65e2cc023f8c76dfe641070f37e0e9b73d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635S7WC56%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIB9PlOjtYxtxI7XLsKggP2B5TTi89Io%2FIabRckF9Dp%2BYAiEAp85ScL%2F1xfpaEW7dH6wKYQmHJGicmj02QHdVnYY1Mj8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIv3UDdSf9nNTu3IVircA1zkJH6yP7ptfGzShCY6MQInTAbCE6kknlLPRkeZBrTHgVI3AQdLoakJ%2Bq%2FVs5yRelJhRjWMmFkheG6n78rf16uXkZpHdRxA8uj0pxSMcaTwW5a%2F9qYD6mQxTs%2FXps7vGAo6RzhX%2BH2r7MjFoOeEq%2FaxVGNZWDOrJwoZhjwhgPDajLc37P5dzNu5RLT%2BrQ7C76OBfzfbF088uj3thBtvF2xCkfXOMfDGg8fNPZRDxSBfJRlzLjk6wN3sOiQmFXxOjw8AXeuA6LsqnU4ZwpQ3jP00UmjID2CDp%2BtfDkZ1%2FQb26B%2BXDqH%2FRZ2B9xY1UO0JKZ1zRbjUfMghdqzMyUPIsMOADkozT6Yh6AwFa6JAWuiIHlgIqh2dP6NOQ7ZYb2V2Rnucep9elLH%2FUX20l3uNP3ZjrzNblmOglaB51vYwAfiqsNftxMYRyuqLWSZhF%2FKngmg1aKGu6jiX1EWL9onCLRmi1lTD3BkBQCMv7tOsWxoN6GvGz83QX%2BmQeuA1t0UMpg2Wt%2FWS3kRXbqcmrmtNNt8fefF9TN%2FOwOQgp4MfnSSYP6wtWMxib5JTAH6WFL%2BOSV2EbryRf1Dj5t3coTChcgoj9NAqFAkrDhq6p865KjlAgIiWpsvwybbOi%2BP2MMKXls8GOqUBwiEi3LbBw8CSZYAJUNNNcSnvcAK%2FNqWM9LeVigMx1%2FyoTM0MVLnZ3mhJvsmq0iG9uhqdvCfKj5%2FxiUP8NBL8Vhf3KwDjN38vmlp%2BtwcOgKOQ3bsreGLYxp6dW7aTkL5cnyesyipcXnRcP3%2BMBqD%2Bc1Dd0Yf0yQxiCiKrl9XPVnEy53B1cvXCNyCILjHvV12iOM9lJnP0embgxv7K7zCt7mFZGOWc&X-Amz-Signature=dc1aba8d30beb68e5789262a5413de2e527b295b9be52ccc8f417344e7ae218d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635S7WC56%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIB9PlOjtYxtxI7XLsKggP2B5TTi89Io%2FIabRckF9Dp%2BYAiEAp85ScL%2F1xfpaEW7dH6wKYQmHJGicmj02QHdVnYY1Mj8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIv3UDdSf9nNTu3IVircA1zkJH6yP7ptfGzShCY6MQInTAbCE6kknlLPRkeZBrTHgVI3AQdLoakJ%2Bq%2FVs5yRelJhRjWMmFkheG6n78rf16uXkZpHdRxA8uj0pxSMcaTwW5a%2F9qYD6mQxTs%2FXps7vGAo6RzhX%2BH2r7MjFoOeEq%2FaxVGNZWDOrJwoZhjwhgPDajLc37P5dzNu5RLT%2BrQ7C76OBfzfbF088uj3thBtvF2xCkfXOMfDGg8fNPZRDxSBfJRlzLjk6wN3sOiQmFXxOjw8AXeuA6LsqnU4ZwpQ3jP00UmjID2CDp%2BtfDkZ1%2FQb26B%2BXDqH%2FRZ2B9xY1UO0JKZ1zRbjUfMghdqzMyUPIsMOADkozT6Yh6AwFa6JAWuiIHlgIqh2dP6NOQ7ZYb2V2Rnucep9elLH%2FUX20l3uNP3ZjrzNblmOglaB51vYwAfiqsNftxMYRyuqLWSZhF%2FKngmg1aKGu6jiX1EWL9onCLRmi1lTD3BkBQCMv7tOsWxoN6GvGz83QX%2BmQeuA1t0UMpg2Wt%2FWS3kRXbqcmrmtNNt8fefF9TN%2FOwOQgp4MfnSSYP6wtWMxib5JTAH6WFL%2BOSV2EbryRf1Dj5t3coTChcgoj9NAqFAkrDhq6p865KjlAgIiWpsvwybbOi%2BP2MMKXls8GOqUBwiEi3LbBw8CSZYAJUNNNcSnvcAK%2FNqWM9LeVigMx1%2FyoTM0MVLnZ3mhJvsmq0iG9uhqdvCfKj5%2FxiUP8NBL8Vhf3KwDjN38vmlp%2BtwcOgKOQ3bsreGLYxp6dW7aTkL5cnyesyipcXnRcP3%2BMBqD%2Bc1Dd0Yf0yQxiCiKrl9XPVnEy53B1cvXCNyCILjHvV12iOM9lJnP0embgxv7K7zCt7mFZGOWc&X-Amz-Signature=d49737a06ac99a7b0271cd022490e1ed193dccc9f4c67bee8980666a1a4fc98e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635S7WC56%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIB9PlOjtYxtxI7XLsKggP2B5TTi89Io%2FIabRckF9Dp%2BYAiEAp85ScL%2F1xfpaEW7dH6wKYQmHJGicmj02QHdVnYY1Mj8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIv3UDdSf9nNTu3IVircA1zkJH6yP7ptfGzShCY6MQInTAbCE6kknlLPRkeZBrTHgVI3AQdLoakJ%2Bq%2FVs5yRelJhRjWMmFkheG6n78rf16uXkZpHdRxA8uj0pxSMcaTwW5a%2F9qYD6mQxTs%2FXps7vGAo6RzhX%2BH2r7MjFoOeEq%2FaxVGNZWDOrJwoZhjwhgPDajLc37P5dzNu5RLT%2BrQ7C76OBfzfbF088uj3thBtvF2xCkfXOMfDGg8fNPZRDxSBfJRlzLjk6wN3sOiQmFXxOjw8AXeuA6LsqnU4ZwpQ3jP00UmjID2CDp%2BtfDkZ1%2FQb26B%2BXDqH%2FRZ2B9xY1UO0JKZ1zRbjUfMghdqzMyUPIsMOADkozT6Yh6AwFa6JAWuiIHlgIqh2dP6NOQ7ZYb2V2Rnucep9elLH%2FUX20l3uNP3ZjrzNblmOglaB51vYwAfiqsNftxMYRyuqLWSZhF%2FKngmg1aKGu6jiX1EWL9onCLRmi1lTD3BkBQCMv7tOsWxoN6GvGz83QX%2BmQeuA1t0UMpg2Wt%2FWS3kRXbqcmrmtNNt8fefF9TN%2FOwOQgp4MfnSSYP6wtWMxib5JTAH6WFL%2BOSV2EbryRf1Dj5t3coTChcgoj9NAqFAkrDhq6p865KjlAgIiWpsvwybbOi%2BP2MMKXls8GOqUBwiEi3LbBw8CSZYAJUNNNcSnvcAK%2FNqWM9LeVigMx1%2FyoTM0MVLnZ3mhJvsmq0iG9uhqdvCfKj5%2FxiUP8NBL8Vhf3KwDjN38vmlp%2BtwcOgKOQ3bsreGLYxp6dW7aTkL5cnyesyipcXnRcP3%2BMBqD%2Bc1Dd0Yf0yQxiCiKrl9XPVnEy53B1cvXCNyCILjHvV12iOM9lJnP0embgxv7K7zCt7mFZGOWc&X-Amz-Signature=84f1c5adb77695cda4040cf339140de4fb7d3680ace6b0d6db13a17fc5afaf00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635S7WC56%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIB9PlOjtYxtxI7XLsKggP2B5TTi89Io%2FIabRckF9Dp%2BYAiEAp85ScL%2F1xfpaEW7dH6wKYQmHJGicmj02QHdVnYY1Mj8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIv3UDdSf9nNTu3IVircA1zkJH6yP7ptfGzShCY6MQInTAbCE6kknlLPRkeZBrTHgVI3AQdLoakJ%2Bq%2FVs5yRelJhRjWMmFkheG6n78rf16uXkZpHdRxA8uj0pxSMcaTwW5a%2F9qYD6mQxTs%2FXps7vGAo6RzhX%2BH2r7MjFoOeEq%2FaxVGNZWDOrJwoZhjwhgPDajLc37P5dzNu5RLT%2BrQ7C76OBfzfbF088uj3thBtvF2xCkfXOMfDGg8fNPZRDxSBfJRlzLjk6wN3sOiQmFXxOjw8AXeuA6LsqnU4ZwpQ3jP00UmjID2CDp%2BtfDkZ1%2FQb26B%2BXDqH%2FRZ2B9xY1UO0JKZ1zRbjUfMghdqzMyUPIsMOADkozT6Yh6AwFa6JAWuiIHlgIqh2dP6NOQ7ZYb2V2Rnucep9elLH%2FUX20l3uNP3ZjrzNblmOglaB51vYwAfiqsNftxMYRyuqLWSZhF%2FKngmg1aKGu6jiX1EWL9onCLRmi1lTD3BkBQCMv7tOsWxoN6GvGz83QX%2BmQeuA1t0UMpg2Wt%2FWS3kRXbqcmrmtNNt8fefF9TN%2FOwOQgp4MfnSSYP6wtWMxib5JTAH6WFL%2BOSV2EbryRf1Dj5t3coTChcgoj9NAqFAkrDhq6p865KjlAgIiWpsvwybbOi%2BP2MMKXls8GOqUBwiEi3LbBw8CSZYAJUNNNcSnvcAK%2FNqWM9LeVigMx1%2FyoTM0MVLnZ3mhJvsmq0iG9uhqdvCfKj5%2FxiUP8NBL8Vhf3KwDjN38vmlp%2BtwcOgKOQ3bsreGLYxp6dW7aTkL5cnyesyipcXnRcP3%2BMBqD%2Bc1Dd0Yf0yQxiCiKrl9XPVnEy53B1cvXCNyCILjHvV12iOM9lJnP0embgxv7K7zCt7mFZGOWc&X-Amz-Signature=5d3e3b75e4ebd85c1000be15ed16655215025dfafd1c576200a3c7c006148e34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635S7WC56%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIB9PlOjtYxtxI7XLsKggP2B5TTi89Io%2FIabRckF9Dp%2BYAiEAp85ScL%2F1xfpaEW7dH6wKYQmHJGicmj02QHdVnYY1Mj8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIv3UDdSf9nNTu3IVircA1zkJH6yP7ptfGzShCY6MQInTAbCE6kknlLPRkeZBrTHgVI3AQdLoakJ%2Bq%2FVs5yRelJhRjWMmFkheG6n78rf16uXkZpHdRxA8uj0pxSMcaTwW5a%2F9qYD6mQxTs%2FXps7vGAo6RzhX%2BH2r7MjFoOeEq%2FaxVGNZWDOrJwoZhjwhgPDajLc37P5dzNu5RLT%2BrQ7C76OBfzfbF088uj3thBtvF2xCkfXOMfDGg8fNPZRDxSBfJRlzLjk6wN3sOiQmFXxOjw8AXeuA6LsqnU4ZwpQ3jP00UmjID2CDp%2BtfDkZ1%2FQb26B%2BXDqH%2FRZ2B9xY1UO0JKZ1zRbjUfMghdqzMyUPIsMOADkozT6Yh6AwFa6JAWuiIHlgIqh2dP6NOQ7ZYb2V2Rnucep9elLH%2FUX20l3uNP3ZjrzNblmOglaB51vYwAfiqsNftxMYRyuqLWSZhF%2FKngmg1aKGu6jiX1EWL9onCLRmi1lTD3BkBQCMv7tOsWxoN6GvGz83QX%2BmQeuA1t0UMpg2Wt%2FWS3kRXbqcmrmtNNt8fefF9TN%2FOwOQgp4MfnSSYP6wtWMxib5JTAH6WFL%2BOSV2EbryRf1Dj5t3coTChcgoj9NAqFAkrDhq6p865KjlAgIiWpsvwybbOi%2BP2MMKXls8GOqUBwiEi3LbBw8CSZYAJUNNNcSnvcAK%2FNqWM9LeVigMx1%2FyoTM0MVLnZ3mhJvsmq0iG9uhqdvCfKj5%2FxiUP8NBL8Vhf3KwDjN38vmlp%2BtwcOgKOQ3bsreGLYxp6dW7aTkL5cnyesyipcXnRcP3%2BMBqD%2Bc1Dd0Yf0yQxiCiKrl9XPVnEy53B1cvXCNyCILjHvV12iOM9lJnP0embgxv7K7zCt7mFZGOWc&X-Amz-Signature=ec257e064f236973679c35e32e31b423fbdf7ea1a71d910ec8ab8f14cf77df3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635S7WC56%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIB9PlOjtYxtxI7XLsKggP2B5TTi89Io%2FIabRckF9Dp%2BYAiEAp85ScL%2F1xfpaEW7dH6wKYQmHJGicmj02QHdVnYY1Mj8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIv3UDdSf9nNTu3IVircA1zkJH6yP7ptfGzShCY6MQInTAbCE6kknlLPRkeZBrTHgVI3AQdLoakJ%2Bq%2FVs5yRelJhRjWMmFkheG6n78rf16uXkZpHdRxA8uj0pxSMcaTwW5a%2F9qYD6mQxTs%2FXps7vGAo6RzhX%2BH2r7MjFoOeEq%2FaxVGNZWDOrJwoZhjwhgPDajLc37P5dzNu5RLT%2BrQ7C76OBfzfbF088uj3thBtvF2xCkfXOMfDGg8fNPZRDxSBfJRlzLjk6wN3sOiQmFXxOjw8AXeuA6LsqnU4ZwpQ3jP00UmjID2CDp%2BtfDkZ1%2FQb26B%2BXDqH%2FRZ2B9xY1UO0JKZ1zRbjUfMghdqzMyUPIsMOADkozT6Yh6AwFa6JAWuiIHlgIqh2dP6NOQ7ZYb2V2Rnucep9elLH%2FUX20l3uNP3ZjrzNblmOglaB51vYwAfiqsNftxMYRyuqLWSZhF%2FKngmg1aKGu6jiX1EWL9onCLRmi1lTD3BkBQCMv7tOsWxoN6GvGz83QX%2BmQeuA1t0UMpg2Wt%2FWS3kRXbqcmrmtNNt8fefF9TN%2FOwOQgp4MfnSSYP6wtWMxib5JTAH6WFL%2BOSV2EbryRf1Dj5t3coTChcgoj9NAqFAkrDhq6p865KjlAgIiWpsvwybbOi%2BP2MMKXls8GOqUBwiEi3LbBw8CSZYAJUNNNcSnvcAK%2FNqWM9LeVigMx1%2FyoTM0MVLnZ3mhJvsmq0iG9uhqdvCfKj5%2FxiUP8NBL8Vhf3KwDjN38vmlp%2BtwcOgKOQ3bsreGLYxp6dW7aTkL5cnyesyipcXnRcP3%2BMBqD%2Bc1Dd0Yf0yQxiCiKrl9XPVnEy53B1cvXCNyCILjHvV12iOM9lJnP0embgxv7K7zCt7mFZGOWc&X-Amz-Signature=177311b617ea724a6c780f72a014aa6cf4a639c05349000741e76ab60b9578c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635S7WC56%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIB9PlOjtYxtxI7XLsKggP2B5TTi89Io%2FIabRckF9Dp%2BYAiEAp85ScL%2F1xfpaEW7dH6wKYQmHJGicmj02QHdVnYY1Mj8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIv3UDdSf9nNTu3IVircA1zkJH6yP7ptfGzShCY6MQInTAbCE6kknlLPRkeZBrTHgVI3AQdLoakJ%2Bq%2FVs5yRelJhRjWMmFkheG6n78rf16uXkZpHdRxA8uj0pxSMcaTwW5a%2F9qYD6mQxTs%2FXps7vGAo6RzhX%2BH2r7MjFoOeEq%2FaxVGNZWDOrJwoZhjwhgPDajLc37P5dzNu5RLT%2BrQ7C76OBfzfbF088uj3thBtvF2xCkfXOMfDGg8fNPZRDxSBfJRlzLjk6wN3sOiQmFXxOjw8AXeuA6LsqnU4ZwpQ3jP00UmjID2CDp%2BtfDkZ1%2FQb26B%2BXDqH%2FRZ2B9xY1UO0JKZ1zRbjUfMghdqzMyUPIsMOADkozT6Yh6AwFa6JAWuiIHlgIqh2dP6NOQ7ZYb2V2Rnucep9elLH%2FUX20l3uNP3ZjrzNblmOglaB51vYwAfiqsNftxMYRyuqLWSZhF%2FKngmg1aKGu6jiX1EWL9onCLRmi1lTD3BkBQCMv7tOsWxoN6GvGz83QX%2BmQeuA1t0UMpg2Wt%2FWS3kRXbqcmrmtNNt8fefF9TN%2FOwOQgp4MfnSSYP6wtWMxib5JTAH6WFL%2BOSV2EbryRf1Dj5t3coTChcgoj9NAqFAkrDhq6p865KjlAgIiWpsvwybbOi%2BP2MMKXls8GOqUBwiEi3LbBw8CSZYAJUNNNcSnvcAK%2FNqWM9LeVigMx1%2FyoTM0MVLnZ3mhJvsmq0iG9uhqdvCfKj5%2FxiUP8NBL8Vhf3KwDjN38vmlp%2BtwcOgKOQ3bsreGLYxp6dW7aTkL5cnyesyipcXnRcP3%2BMBqD%2Bc1Dd0Yf0yQxiCiKrl9XPVnEy53B1cvXCNyCILjHvV12iOM9lJnP0embgxv7K7zCt7mFZGOWc&X-Amz-Signature=1c58e21f3589915d9e2102339eb75f0dc19348d9811f322950a1b63ce8029454&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635S7WC56%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIB9PlOjtYxtxI7XLsKggP2B5TTi89Io%2FIabRckF9Dp%2BYAiEAp85ScL%2F1xfpaEW7dH6wKYQmHJGicmj02QHdVnYY1Mj8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIv3UDdSf9nNTu3IVircA1zkJH6yP7ptfGzShCY6MQInTAbCE6kknlLPRkeZBrTHgVI3AQdLoakJ%2Bq%2FVs5yRelJhRjWMmFkheG6n78rf16uXkZpHdRxA8uj0pxSMcaTwW5a%2F9qYD6mQxTs%2FXps7vGAo6RzhX%2BH2r7MjFoOeEq%2FaxVGNZWDOrJwoZhjwhgPDajLc37P5dzNu5RLT%2BrQ7C76OBfzfbF088uj3thBtvF2xCkfXOMfDGg8fNPZRDxSBfJRlzLjk6wN3sOiQmFXxOjw8AXeuA6LsqnU4ZwpQ3jP00UmjID2CDp%2BtfDkZ1%2FQb26B%2BXDqH%2FRZ2B9xY1UO0JKZ1zRbjUfMghdqzMyUPIsMOADkozT6Yh6AwFa6JAWuiIHlgIqh2dP6NOQ7ZYb2V2Rnucep9elLH%2FUX20l3uNP3ZjrzNblmOglaB51vYwAfiqsNftxMYRyuqLWSZhF%2FKngmg1aKGu6jiX1EWL9onCLRmi1lTD3BkBQCMv7tOsWxoN6GvGz83QX%2BmQeuA1t0UMpg2Wt%2FWS3kRXbqcmrmtNNt8fefF9TN%2FOwOQgp4MfnSSYP6wtWMxib5JTAH6WFL%2BOSV2EbryRf1Dj5t3coTChcgoj9NAqFAkrDhq6p865KjlAgIiWpsvwybbOi%2BP2MMKXls8GOqUBwiEi3LbBw8CSZYAJUNNNcSnvcAK%2FNqWM9LeVigMx1%2FyoTM0MVLnZ3mhJvsmq0iG9uhqdvCfKj5%2FxiUP8NBL8Vhf3KwDjN38vmlp%2BtwcOgKOQ3bsreGLYxp6dW7aTkL5cnyesyipcXnRcP3%2BMBqD%2Bc1Dd0Yf0yQxiCiKrl9XPVnEy53B1cvXCNyCILjHvV12iOM9lJnP0embgxv7K7zCt7mFZGOWc&X-Amz-Signature=68d82a80ec29572fd53339b6e4cd8afb500ccb864a64a8fab75faa1a28f927db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

