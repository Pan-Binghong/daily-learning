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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T5EB4E%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqXiQYnJTnw7zXyBIHHWAZD3SMlimiOVJIWxu43WLY4AiASJW2RM4AwUOtqHxXLg6orOBP2J4jkJ8KlQBZsQ5VtCSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpQRFgt4xxl5iOXSXKtwDYgx3s69eRS01vsEyqR95f0hljc%2BeOYxFxSYLupUengZin2Lwvz8V4fK8SSbRs5GmLyarFQOAwmbeEF%2BwbIheoC%2B2N2pSSDlj03QoS%2B9V%2FXMHony1Gl3W0PIYR0V01DS0KQ2K6Il2HsE3%2Fx0xisYsaEku0ZWFSGXDbW9uNoOOy1oZUb6isAfJX3LsA4vJutHJLu71XmYYz%2FoapWscXijOGBkNpvyws7SnKEG%2FaRugvNm%2FDbodK14niivTRbunxE1b4mY%2BUuW%2BtojtDguErdCQqCfN5XzpPt7gSji8JkNdk7No2DqEJBmta%2BcdDU0I4%2F96CatG%2BLOx6opu7Q47cFp36Wdp8pjKT7jgHclMNwiTcL1dQ668S84aSd1GVaapR2OQ3yYpHn4Tq3mGMLvil79RDtXnoZuyuo%2BdtHhBjQtgWkGNDU9SyT5rZaAW3S1e58usDStpFjR2k0z86CJvYYM3qJWqpQAZv%2BIkgXLlE%2FCsQNPH6RceK7D28ECrwpcMmGw5OvZAUC9FN4CyMEo5vfE6OsviH6xx7WwBR2yhRjOKD2tDsmBOCmaRXlvHK5rgRYbTzOZJ0LYU53kzky%2BSIvYhmBcmWaxQJM6fHYN%2BZusu1ZBeCmErYuycZ8N01EwwpfKvyAY6pgEZdK%2B0DaWq2iwuQFvXeib6tfS%2FECowAckS77UdLbmTg1Nb1xcm9Btg9pIkP8oYtrHELF4dj4cNBq0KKsI4AdJeXqgLOhbccrreLrCbRmzRWYVwcEpefmuZoRxhxx5F1M9hvNfU0hEZA27nrTs4YjSmD7YtRXRItsbzxwdzATlJpev4yPt0QPLJcv9bHGWvwLiclABTrAJVct1Q2K1zOZRmSX7vWw1z&X-Amz-Signature=88cf0c9a7cea4574e90582f0205b010ab8cebd6f89e53ed77cbd29e806a79867&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T5EB4E%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqXiQYnJTnw7zXyBIHHWAZD3SMlimiOVJIWxu43WLY4AiASJW2RM4AwUOtqHxXLg6orOBP2J4jkJ8KlQBZsQ5VtCSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpQRFgt4xxl5iOXSXKtwDYgx3s69eRS01vsEyqR95f0hljc%2BeOYxFxSYLupUengZin2Lwvz8V4fK8SSbRs5GmLyarFQOAwmbeEF%2BwbIheoC%2B2N2pSSDlj03QoS%2B9V%2FXMHony1Gl3W0PIYR0V01DS0KQ2K6Il2HsE3%2Fx0xisYsaEku0ZWFSGXDbW9uNoOOy1oZUb6isAfJX3LsA4vJutHJLu71XmYYz%2FoapWscXijOGBkNpvyws7SnKEG%2FaRugvNm%2FDbodK14niivTRbunxE1b4mY%2BUuW%2BtojtDguErdCQqCfN5XzpPt7gSji8JkNdk7No2DqEJBmta%2BcdDU0I4%2F96CatG%2BLOx6opu7Q47cFp36Wdp8pjKT7jgHclMNwiTcL1dQ668S84aSd1GVaapR2OQ3yYpHn4Tq3mGMLvil79RDtXnoZuyuo%2BdtHhBjQtgWkGNDU9SyT5rZaAW3S1e58usDStpFjR2k0z86CJvYYM3qJWqpQAZv%2BIkgXLlE%2FCsQNPH6RceK7D28ECrwpcMmGw5OvZAUC9FN4CyMEo5vfE6OsviH6xx7WwBR2yhRjOKD2tDsmBOCmaRXlvHK5rgRYbTzOZJ0LYU53kzky%2BSIvYhmBcmWaxQJM6fHYN%2BZusu1ZBeCmErYuycZ8N01EwwpfKvyAY6pgEZdK%2B0DaWq2iwuQFvXeib6tfS%2FECowAckS77UdLbmTg1Nb1xcm9Btg9pIkP8oYtrHELF4dj4cNBq0KKsI4AdJeXqgLOhbccrreLrCbRmzRWYVwcEpefmuZoRxhxx5F1M9hvNfU0hEZA27nrTs4YjSmD7YtRXRItsbzxwdzATlJpev4yPt0QPLJcv9bHGWvwLiclABTrAJVct1Q2K1zOZRmSX7vWw1z&X-Amz-Signature=a6285c82db31c3d3d735769fe4df64c6feb9d1c102e3a4e972dbe85d43490bdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T5EB4E%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqXiQYnJTnw7zXyBIHHWAZD3SMlimiOVJIWxu43WLY4AiASJW2RM4AwUOtqHxXLg6orOBP2J4jkJ8KlQBZsQ5VtCSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpQRFgt4xxl5iOXSXKtwDYgx3s69eRS01vsEyqR95f0hljc%2BeOYxFxSYLupUengZin2Lwvz8V4fK8SSbRs5GmLyarFQOAwmbeEF%2BwbIheoC%2B2N2pSSDlj03QoS%2B9V%2FXMHony1Gl3W0PIYR0V01DS0KQ2K6Il2HsE3%2Fx0xisYsaEku0ZWFSGXDbW9uNoOOy1oZUb6isAfJX3LsA4vJutHJLu71XmYYz%2FoapWscXijOGBkNpvyws7SnKEG%2FaRugvNm%2FDbodK14niivTRbunxE1b4mY%2BUuW%2BtojtDguErdCQqCfN5XzpPt7gSji8JkNdk7No2DqEJBmta%2BcdDU0I4%2F96CatG%2BLOx6opu7Q47cFp36Wdp8pjKT7jgHclMNwiTcL1dQ668S84aSd1GVaapR2OQ3yYpHn4Tq3mGMLvil79RDtXnoZuyuo%2BdtHhBjQtgWkGNDU9SyT5rZaAW3S1e58usDStpFjR2k0z86CJvYYM3qJWqpQAZv%2BIkgXLlE%2FCsQNPH6RceK7D28ECrwpcMmGw5OvZAUC9FN4CyMEo5vfE6OsviH6xx7WwBR2yhRjOKD2tDsmBOCmaRXlvHK5rgRYbTzOZJ0LYU53kzky%2BSIvYhmBcmWaxQJM6fHYN%2BZusu1ZBeCmErYuycZ8N01EwwpfKvyAY6pgEZdK%2B0DaWq2iwuQFvXeib6tfS%2FECowAckS77UdLbmTg1Nb1xcm9Btg9pIkP8oYtrHELF4dj4cNBq0KKsI4AdJeXqgLOhbccrreLrCbRmzRWYVwcEpefmuZoRxhxx5F1M9hvNfU0hEZA27nrTs4YjSmD7YtRXRItsbzxwdzATlJpev4yPt0QPLJcv9bHGWvwLiclABTrAJVct1Q2K1zOZRmSX7vWw1z&X-Amz-Signature=d7b35178d0375a86e90a52ac1eeb82b897435ed0db4ea132cb9b087405bcd5b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T5EB4E%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqXiQYnJTnw7zXyBIHHWAZD3SMlimiOVJIWxu43WLY4AiASJW2RM4AwUOtqHxXLg6orOBP2J4jkJ8KlQBZsQ5VtCSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpQRFgt4xxl5iOXSXKtwDYgx3s69eRS01vsEyqR95f0hljc%2BeOYxFxSYLupUengZin2Lwvz8V4fK8SSbRs5GmLyarFQOAwmbeEF%2BwbIheoC%2B2N2pSSDlj03QoS%2B9V%2FXMHony1Gl3W0PIYR0V01DS0KQ2K6Il2HsE3%2Fx0xisYsaEku0ZWFSGXDbW9uNoOOy1oZUb6isAfJX3LsA4vJutHJLu71XmYYz%2FoapWscXijOGBkNpvyws7SnKEG%2FaRugvNm%2FDbodK14niivTRbunxE1b4mY%2BUuW%2BtojtDguErdCQqCfN5XzpPt7gSji8JkNdk7No2DqEJBmta%2BcdDU0I4%2F96CatG%2BLOx6opu7Q47cFp36Wdp8pjKT7jgHclMNwiTcL1dQ668S84aSd1GVaapR2OQ3yYpHn4Tq3mGMLvil79RDtXnoZuyuo%2BdtHhBjQtgWkGNDU9SyT5rZaAW3S1e58usDStpFjR2k0z86CJvYYM3qJWqpQAZv%2BIkgXLlE%2FCsQNPH6RceK7D28ECrwpcMmGw5OvZAUC9FN4CyMEo5vfE6OsviH6xx7WwBR2yhRjOKD2tDsmBOCmaRXlvHK5rgRYbTzOZJ0LYU53kzky%2BSIvYhmBcmWaxQJM6fHYN%2BZusu1ZBeCmErYuycZ8N01EwwpfKvyAY6pgEZdK%2B0DaWq2iwuQFvXeib6tfS%2FECowAckS77UdLbmTg1Nb1xcm9Btg9pIkP8oYtrHELF4dj4cNBq0KKsI4AdJeXqgLOhbccrreLrCbRmzRWYVwcEpefmuZoRxhxx5F1M9hvNfU0hEZA27nrTs4YjSmD7YtRXRItsbzxwdzATlJpev4yPt0QPLJcv9bHGWvwLiclABTrAJVct1Q2K1zOZRmSX7vWw1z&X-Amz-Signature=5b02557196165de1528f28f8e82c7b608052a56f581ab62af75cf4c2afdf62c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T5EB4E%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqXiQYnJTnw7zXyBIHHWAZD3SMlimiOVJIWxu43WLY4AiASJW2RM4AwUOtqHxXLg6orOBP2J4jkJ8KlQBZsQ5VtCSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpQRFgt4xxl5iOXSXKtwDYgx3s69eRS01vsEyqR95f0hljc%2BeOYxFxSYLupUengZin2Lwvz8V4fK8SSbRs5GmLyarFQOAwmbeEF%2BwbIheoC%2B2N2pSSDlj03QoS%2B9V%2FXMHony1Gl3W0PIYR0V01DS0KQ2K6Il2HsE3%2Fx0xisYsaEku0ZWFSGXDbW9uNoOOy1oZUb6isAfJX3LsA4vJutHJLu71XmYYz%2FoapWscXijOGBkNpvyws7SnKEG%2FaRugvNm%2FDbodK14niivTRbunxE1b4mY%2BUuW%2BtojtDguErdCQqCfN5XzpPt7gSji8JkNdk7No2DqEJBmta%2BcdDU0I4%2F96CatG%2BLOx6opu7Q47cFp36Wdp8pjKT7jgHclMNwiTcL1dQ668S84aSd1GVaapR2OQ3yYpHn4Tq3mGMLvil79RDtXnoZuyuo%2BdtHhBjQtgWkGNDU9SyT5rZaAW3S1e58usDStpFjR2k0z86CJvYYM3qJWqpQAZv%2BIkgXLlE%2FCsQNPH6RceK7D28ECrwpcMmGw5OvZAUC9FN4CyMEo5vfE6OsviH6xx7WwBR2yhRjOKD2tDsmBOCmaRXlvHK5rgRYbTzOZJ0LYU53kzky%2BSIvYhmBcmWaxQJM6fHYN%2BZusu1ZBeCmErYuycZ8N01EwwpfKvyAY6pgEZdK%2B0DaWq2iwuQFvXeib6tfS%2FECowAckS77UdLbmTg1Nb1xcm9Btg9pIkP8oYtrHELF4dj4cNBq0KKsI4AdJeXqgLOhbccrreLrCbRmzRWYVwcEpefmuZoRxhxx5F1M9hvNfU0hEZA27nrTs4YjSmD7YtRXRItsbzxwdzATlJpev4yPt0QPLJcv9bHGWvwLiclABTrAJVct1Q2K1zOZRmSX7vWw1z&X-Amz-Signature=98a92ff008c6bd30fed1a94a66ecacafd0e8e5ae47ac31f22c2a074e842575e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T5EB4E%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqXiQYnJTnw7zXyBIHHWAZD3SMlimiOVJIWxu43WLY4AiASJW2RM4AwUOtqHxXLg6orOBP2J4jkJ8KlQBZsQ5VtCSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpQRFgt4xxl5iOXSXKtwDYgx3s69eRS01vsEyqR95f0hljc%2BeOYxFxSYLupUengZin2Lwvz8V4fK8SSbRs5GmLyarFQOAwmbeEF%2BwbIheoC%2B2N2pSSDlj03QoS%2B9V%2FXMHony1Gl3W0PIYR0V01DS0KQ2K6Il2HsE3%2Fx0xisYsaEku0ZWFSGXDbW9uNoOOy1oZUb6isAfJX3LsA4vJutHJLu71XmYYz%2FoapWscXijOGBkNpvyws7SnKEG%2FaRugvNm%2FDbodK14niivTRbunxE1b4mY%2BUuW%2BtojtDguErdCQqCfN5XzpPt7gSji8JkNdk7No2DqEJBmta%2BcdDU0I4%2F96CatG%2BLOx6opu7Q47cFp36Wdp8pjKT7jgHclMNwiTcL1dQ668S84aSd1GVaapR2OQ3yYpHn4Tq3mGMLvil79RDtXnoZuyuo%2BdtHhBjQtgWkGNDU9SyT5rZaAW3S1e58usDStpFjR2k0z86CJvYYM3qJWqpQAZv%2BIkgXLlE%2FCsQNPH6RceK7D28ECrwpcMmGw5OvZAUC9FN4CyMEo5vfE6OsviH6xx7WwBR2yhRjOKD2tDsmBOCmaRXlvHK5rgRYbTzOZJ0LYU53kzky%2BSIvYhmBcmWaxQJM6fHYN%2BZusu1ZBeCmErYuycZ8N01EwwpfKvyAY6pgEZdK%2B0DaWq2iwuQFvXeib6tfS%2FECowAckS77UdLbmTg1Nb1xcm9Btg9pIkP8oYtrHELF4dj4cNBq0KKsI4AdJeXqgLOhbccrreLrCbRmzRWYVwcEpefmuZoRxhxx5F1M9hvNfU0hEZA27nrTs4YjSmD7YtRXRItsbzxwdzATlJpev4yPt0QPLJcv9bHGWvwLiclABTrAJVct1Q2K1zOZRmSX7vWw1z&X-Amz-Signature=7f6de7ae5dc062ab965742dab5981cc98c6bdf13aacee647c52d69f8a597a395&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T5EB4E%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqXiQYnJTnw7zXyBIHHWAZD3SMlimiOVJIWxu43WLY4AiASJW2RM4AwUOtqHxXLg6orOBP2J4jkJ8KlQBZsQ5VtCSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpQRFgt4xxl5iOXSXKtwDYgx3s69eRS01vsEyqR95f0hljc%2BeOYxFxSYLupUengZin2Lwvz8V4fK8SSbRs5GmLyarFQOAwmbeEF%2BwbIheoC%2B2N2pSSDlj03QoS%2B9V%2FXMHony1Gl3W0PIYR0V01DS0KQ2K6Il2HsE3%2Fx0xisYsaEku0ZWFSGXDbW9uNoOOy1oZUb6isAfJX3LsA4vJutHJLu71XmYYz%2FoapWscXijOGBkNpvyws7SnKEG%2FaRugvNm%2FDbodK14niivTRbunxE1b4mY%2BUuW%2BtojtDguErdCQqCfN5XzpPt7gSji8JkNdk7No2DqEJBmta%2BcdDU0I4%2F96CatG%2BLOx6opu7Q47cFp36Wdp8pjKT7jgHclMNwiTcL1dQ668S84aSd1GVaapR2OQ3yYpHn4Tq3mGMLvil79RDtXnoZuyuo%2BdtHhBjQtgWkGNDU9SyT5rZaAW3S1e58usDStpFjR2k0z86CJvYYM3qJWqpQAZv%2BIkgXLlE%2FCsQNPH6RceK7D28ECrwpcMmGw5OvZAUC9FN4CyMEo5vfE6OsviH6xx7WwBR2yhRjOKD2tDsmBOCmaRXlvHK5rgRYbTzOZJ0LYU53kzky%2BSIvYhmBcmWaxQJM6fHYN%2BZusu1ZBeCmErYuycZ8N01EwwpfKvyAY6pgEZdK%2B0DaWq2iwuQFvXeib6tfS%2FECowAckS77UdLbmTg1Nb1xcm9Btg9pIkP8oYtrHELF4dj4cNBq0KKsI4AdJeXqgLOhbccrreLrCbRmzRWYVwcEpefmuZoRxhxx5F1M9hvNfU0hEZA27nrTs4YjSmD7YtRXRItsbzxwdzATlJpev4yPt0QPLJcv9bHGWvwLiclABTrAJVct1Q2K1zOZRmSX7vWw1z&X-Amz-Signature=15c41af3c475c1a0ef4e650d06d8db74efa05bc08a26e72b024f3444cf3319d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T5EB4E%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqXiQYnJTnw7zXyBIHHWAZD3SMlimiOVJIWxu43WLY4AiASJW2RM4AwUOtqHxXLg6orOBP2J4jkJ8KlQBZsQ5VtCSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpQRFgt4xxl5iOXSXKtwDYgx3s69eRS01vsEyqR95f0hljc%2BeOYxFxSYLupUengZin2Lwvz8V4fK8SSbRs5GmLyarFQOAwmbeEF%2BwbIheoC%2B2N2pSSDlj03QoS%2B9V%2FXMHony1Gl3W0PIYR0V01DS0KQ2K6Il2HsE3%2Fx0xisYsaEku0ZWFSGXDbW9uNoOOy1oZUb6isAfJX3LsA4vJutHJLu71XmYYz%2FoapWscXijOGBkNpvyws7SnKEG%2FaRugvNm%2FDbodK14niivTRbunxE1b4mY%2BUuW%2BtojtDguErdCQqCfN5XzpPt7gSji8JkNdk7No2DqEJBmta%2BcdDU0I4%2F96CatG%2BLOx6opu7Q47cFp36Wdp8pjKT7jgHclMNwiTcL1dQ668S84aSd1GVaapR2OQ3yYpHn4Tq3mGMLvil79RDtXnoZuyuo%2BdtHhBjQtgWkGNDU9SyT5rZaAW3S1e58usDStpFjR2k0z86CJvYYM3qJWqpQAZv%2BIkgXLlE%2FCsQNPH6RceK7D28ECrwpcMmGw5OvZAUC9FN4CyMEo5vfE6OsviH6xx7WwBR2yhRjOKD2tDsmBOCmaRXlvHK5rgRYbTzOZJ0LYU53kzky%2BSIvYhmBcmWaxQJM6fHYN%2BZusu1ZBeCmErYuycZ8N01EwwpfKvyAY6pgEZdK%2B0DaWq2iwuQFvXeib6tfS%2FECowAckS77UdLbmTg1Nb1xcm9Btg9pIkP8oYtrHELF4dj4cNBq0KKsI4AdJeXqgLOhbccrreLrCbRmzRWYVwcEpefmuZoRxhxx5F1M9hvNfU0hEZA27nrTs4YjSmD7YtRXRItsbzxwdzATlJpev4yPt0QPLJcv9bHGWvwLiclABTrAJVct1Q2K1zOZRmSX7vWw1z&X-Amz-Signature=57ed30532b2d0733ef132ad071e150c58a1c050fe04db3691fc326873c9e39f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T5EB4E%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqXiQYnJTnw7zXyBIHHWAZD3SMlimiOVJIWxu43WLY4AiASJW2RM4AwUOtqHxXLg6orOBP2J4jkJ8KlQBZsQ5VtCSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpQRFgt4xxl5iOXSXKtwDYgx3s69eRS01vsEyqR95f0hljc%2BeOYxFxSYLupUengZin2Lwvz8V4fK8SSbRs5GmLyarFQOAwmbeEF%2BwbIheoC%2B2N2pSSDlj03QoS%2B9V%2FXMHony1Gl3W0PIYR0V01DS0KQ2K6Il2HsE3%2Fx0xisYsaEku0ZWFSGXDbW9uNoOOy1oZUb6isAfJX3LsA4vJutHJLu71XmYYz%2FoapWscXijOGBkNpvyws7SnKEG%2FaRugvNm%2FDbodK14niivTRbunxE1b4mY%2BUuW%2BtojtDguErdCQqCfN5XzpPt7gSji8JkNdk7No2DqEJBmta%2BcdDU0I4%2F96CatG%2BLOx6opu7Q47cFp36Wdp8pjKT7jgHclMNwiTcL1dQ668S84aSd1GVaapR2OQ3yYpHn4Tq3mGMLvil79RDtXnoZuyuo%2BdtHhBjQtgWkGNDU9SyT5rZaAW3S1e58usDStpFjR2k0z86CJvYYM3qJWqpQAZv%2BIkgXLlE%2FCsQNPH6RceK7D28ECrwpcMmGw5OvZAUC9FN4CyMEo5vfE6OsviH6xx7WwBR2yhRjOKD2tDsmBOCmaRXlvHK5rgRYbTzOZJ0LYU53kzky%2BSIvYhmBcmWaxQJM6fHYN%2BZusu1ZBeCmErYuycZ8N01EwwpfKvyAY6pgEZdK%2B0DaWq2iwuQFvXeib6tfS%2FECowAckS77UdLbmTg1Nb1xcm9Btg9pIkP8oYtrHELF4dj4cNBq0KKsI4AdJeXqgLOhbccrreLrCbRmzRWYVwcEpefmuZoRxhxx5F1M9hvNfU0hEZA27nrTs4YjSmD7YtRXRItsbzxwdzATlJpev4yPt0QPLJcv9bHGWvwLiclABTrAJVct1Q2K1zOZRmSX7vWw1z&X-Amz-Signature=1da8bb460d440dcba2d22651d5bdb6861904a5df9231b92fa7167a5efc727dec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T5EB4E%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqXiQYnJTnw7zXyBIHHWAZD3SMlimiOVJIWxu43WLY4AiASJW2RM4AwUOtqHxXLg6orOBP2J4jkJ8KlQBZsQ5VtCSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpQRFgt4xxl5iOXSXKtwDYgx3s69eRS01vsEyqR95f0hljc%2BeOYxFxSYLupUengZin2Lwvz8V4fK8SSbRs5GmLyarFQOAwmbeEF%2BwbIheoC%2B2N2pSSDlj03QoS%2B9V%2FXMHony1Gl3W0PIYR0V01DS0KQ2K6Il2HsE3%2Fx0xisYsaEku0ZWFSGXDbW9uNoOOy1oZUb6isAfJX3LsA4vJutHJLu71XmYYz%2FoapWscXijOGBkNpvyws7SnKEG%2FaRugvNm%2FDbodK14niivTRbunxE1b4mY%2BUuW%2BtojtDguErdCQqCfN5XzpPt7gSji8JkNdk7No2DqEJBmta%2BcdDU0I4%2F96CatG%2BLOx6opu7Q47cFp36Wdp8pjKT7jgHclMNwiTcL1dQ668S84aSd1GVaapR2OQ3yYpHn4Tq3mGMLvil79RDtXnoZuyuo%2BdtHhBjQtgWkGNDU9SyT5rZaAW3S1e58usDStpFjR2k0z86CJvYYM3qJWqpQAZv%2BIkgXLlE%2FCsQNPH6RceK7D28ECrwpcMmGw5OvZAUC9FN4CyMEo5vfE6OsviH6xx7WwBR2yhRjOKD2tDsmBOCmaRXlvHK5rgRYbTzOZJ0LYU53kzky%2BSIvYhmBcmWaxQJM6fHYN%2BZusu1ZBeCmErYuycZ8N01EwwpfKvyAY6pgEZdK%2B0DaWq2iwuQFvXeib6tfS%2FECowAckS77UdLbmTg1Nb1xcm9Btg9pIkP8oYtrHELF4dj4cNBq0KKsI4AdJeXqgLOhbccrreLrCbRmzRWYVwcEpefmuZoRxhxx5F1M9hvNfU0hEZA27nrTs4YjSmD7YtRXRItsbzxwdzATlJpev4yPt0QPLJcv9bHGWvwLiclABTrAJVct1Q2K1zOZRmSX7vWw1z&X-Amz-Signature=39f6a9a4f8fe6a83346090f3890d58fab7dde15c84cdf6ba14cc3586490e00ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

