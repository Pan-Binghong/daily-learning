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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCI7O5EL%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFG88PotzAvFRVNOzlFfJ7xtFVZCx6vGvUR8%2F7%2B%2FxmD8AiAOtygAROZudQRBOGOKICeKEPKNnl7n9YQlZjdCbzOLryqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNVlhOo7AI4GD%2BqDKtwDxSBSJFhtLAlgpG648Wv62%2FmIC0s5tLiKLTz4qhPWYJLP4NjJOywQ6h4Yc3XIYbsIgiS1cNxRERce82qc2MwVJgmAZZXEM0ZZ2RitrJEeF5RoWrFEgjrIqzVjfIOQdvtaeBIFGMG0DlfK0tSnuNmLYNJRmuPhGys8TMt6b7tl5M3nho8LJBo9U9KMRlo4YXNY0%2FpfOv4gCvpc1Hp5sUTHalTQRJ5tzRdwUV5C9dZbDD2964QEbmOv59niXvtTELLS5CxrfykwcOkYz2mkpuq3erVYcCKaMc8UfI6Cuk4gPoZJcmsCXlLbeKd6YvqyqNmnCfkmq8P4S0lLSs2yFSg03dAUbJ%2F6YuxK7jNy1JoMu91B%2BvupS%2F70J59BAN80xMNtkmsmpl%2Bt59qQhNYyjTuYfp%2Bj2FGvMWx2LjjvM9jwd6M5w7lUiS8ztLuOvwUQsr67%2B0MUO6DLs60Q5WHgnywAWj9TwiVE%2FTUL9q7FPKr48xa06KUdTp%2B4g0Tpu9LUAxbJczjG8r4iRaZFDBUJ7t8xX3NxvbJVNHSjZUyqRQsX0eXnFRHicrpJuVGD8vBAOAeGQEm1XbdlopFF8sYAACcjxhjs9MXBrpmvzzRps9rumg5zZtFu9EcqjS781DkwtbuGzwY6pgGkKbdWVlZIdkMGG%2F9%2Be09j%2B%2BunWnOy%2BldvcAk4Cmw1F%2BQAjrd%2B1XxvXoDMq6kjnfPES4mYJOKx0DMxw5DwYR01tNnOV3rGTXq9i1x07JRcsN4WnZoq%2FuoCNGpHHZlx%2FG58gRP4M65stMWXhdvLQqP1Kr1TpwtVwAidCdDqiwSu3yPgd4PQq8okxwj6GwvDciZRIWQWcx0guwGFjTCt5ZgQ2Ydenl91&X-Amz-Signature=ba3c4015f0eeb90dc3172da66f71ab06babc41cfe8de5c7f7bd66fbe49b3a35f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCI7O5EL%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFG88PotzAvFRVNOzlFfJ7xtFVZCx6vGvUR8%2F7%2B%2FxmD8AiAOtygAROZudQRBOGOKICeKEPKNnl7n9YQlZjdCbzOLryqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNVlhOo7AI4GD%2BqDKtwDxSBSJFhtLAlgpG648Wv62%2FmIC0s5tLiKLTz4qhPWYJLP4NjJOywQ6h4Yc3XIYbsIgiS1cNxRERce82qc2MwVJgmAZZXEM0ZZ2RitrJEeF5RoWrFEgjrIqzVjfIOQdvtaeBIFGMG0DlfK0tSnuNmLYNJRmuPhGys8TMt6b7tl5M3nho8LJBo9U9KMRlo4YXNY0%2FpfOv4gCvpc1Hp5sUTHalTQRJ5tzRdwUV5C9dZbDD2964QEbmOv59niXvtTELLS5CxrfykwcOkYz2mkpuq3erVYcCKaMc8UfI6Cuk4gPoZJcmsCXlLbeKd6YvqyqNmnCfkmq8P4S0lLSs2yFSg03dAUbJ%2F6YuxK7jNy1JoMu91B%2BvupS%2F70J59BAN80xMNtkmsmpl%2Bt59qQhNYyjTuYfp%2Bj2FGvMWx2LjjvM9jwd6M5w7lUiS8ztLuOvwUQsr67%2B0MUO6DLs60Q5WHgnywAWj9TwiVE%2FTUL9q7FPKr48xa06KUdTp%2B4g0Tpu9LUAxbJczjG8r4iRaZFDBUJ7t8xX3NxvbJVNHSjZUyqRQsX0eXnFRHicrpJuVGD8vBAOAeGQEm1XbdlopFF8sYAACcjxhjs9MXBrpmvzzRps9rumg5zZtFu9EcqjS781DkwtbuGzwY6pgGkKbdWVlZIdkMGG%2F9%2Be09j%2B%2BunWnOy%2BldvcAk4Cmw1F%2BQAjrd%2B1XxvXoDMq6kjnfPES4mYJOKx0DMxw5DwYR01tNnOV3rGTXq9i1x07JRcsN4WnZoq%2FuoCNGpHHZlx%2FG58gRP4M65stMWXhdvLQqP1Kr1TpwtVwAidCdDqiwSu3yPgd4PQq8okxwj6GwvDciZRIWQWcx0guwGFjTCt5ZgQ2Ydenl91&X-Amz-Signature=90cc74ba1d42374e3042d4abfb38863ff44a688f2b73096762bb3a67daa757c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCI7O5EL%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFG88PotzAvFRVNOzlFfJ7xtFVZCx6vGvUR8%2F7%2B%2FxmD8AiAOtygAROZudQRBOGOKICeKEPKNnl7n9YQlZjdCbzOLryqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNVlhOo7AI4GD%2BqDKtwDxSBSJFhtLAlgpG648Wv62%2FmIC0s5tLiKLTz4qhPWYJLP4NjJOywQ6h4Yc3XIYbsIgiS1cNxRERce82qc2MwVJgmAZZXEM0ZZ2RitrJEeF5RoWrFEgjrIqzVjfIOQdvtaeBIFGMG0DlfK0tSnuNmLYNJRmuPhGys8TMt6b7tl5M3nho8LJBo9U9KMRlo4YXNY0%2FpfOv4gCvpc1Hp5sUTHalTQRJ5tzRdwUV5C9dZbDD2964QEbmOv59niXvtTELLS5CxrfykwcOkYz2mkpuq3erVYcCKaMc8UfI6Cuk4gPoZJcmsCXlLbeKd6YvqyqNmnCfkmq8P4S0lLSs2yFSg03dAUbJ%2F6YuxK7jNy1JoMu91B%2BvupS%2F70J59BAN80xMNtkmsmpl%2Bt59qQhNYyjTuYfp%2Bj2FGvMWx2LjjvM9jwd6M5w7lUiS8ztLuOvwUQsr67%2B0MUO6DLs60Q5WHgnywAWj9TwiVE%2FTUL9q7FPKr48xa06KUdTp%2B4g0Tpu9LUAxbJczjG8r4iRaZFDBUJ7t8xX3NxvbJVNHSjZUyqRQsX0eXnFRHicrpJuVGD8vBAOAeGQEm1XbdlopFF8sYAACcjxhjs9MXBrpmvzzRps9rumg5zZtFu9EcqjS781DkwtbuGzwY6pgGkKbdWVlZIdkMGG%2F9%2Be09j%2B%2BunWnOy%2BldvcAk4Cmw1F%2BQAjrd%2B1XxvXoDMq6kjnfPES4mYJOKx0DMxw5DwYR01tNnOV3rGTXq9i1x07JRcsN4WnZoq%2FuoCNGpHHZlx%2FG58gRP4M65stMWXhdvLQqP1Kr1TpwtVwAidCdDqiwSu3yPgd4PQq8okxwj6GwvDciZRIWQWcx0guwGFjTCt5ZgQ2Ydenl91&X-Amz-Signature=2673ec9211c32c428f79dd45f19dc05a85a0aee8758dc27530181798cfab4685&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCI7O5EL%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFG88PotzAvFRVNOzlFfJ7xtFVZCx6vGvUR8%2F7%2B%2FxmD8AiAOtygAROZudQRBOGOKICeKEPKNnl7n9YQlZjdCbzOLryqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNVlhOo7AI4GD%2BqDKtwDxSBSJFhtLAlgpG648Wv62%2FmIC0s5tLiKLTz4qhPWYJLP4NjJOywQ6h4Yc3XIYbsIgiS1cNxRERce82qc2MwVJgmAZZXEM0ZZ2RitrJEeF5RoWrFEgjrIqzVjfIOQdvtaeBIFGMG0DlfK0tSnuNmLYNJRmuPhGys8TMt6b7tl5M3nho8LJBo9U9KMRlo4YXNY0%2FpfOv4gCvpc1Hp5sUTHalTQRJ5tzRdwUV5C9dZbDD2964QEbmOv59niXvtTELLS5CxrfykwcOkYz2mkpuq3erVYcCKaMc8UfI6Cuk4gPoZJcmsCXlLbeKd6YvqyqNmnCfkmq8P4S0lLSs2yFSg03dAUbJ%2F6YuxK7jNy1JoMu91B%2BvupS%2F70J59BAN80xMNtkmsmpl%2Bt59qQhNYyjTuYfp%2Bj2FGvMWx2LjjvM9jwd6M5w7lUiS8ztLuOvwUQsr67%2B0MUO6DLs60Q5WHgnywAWj9TwiVE%2FTUL9q7FPKr48xa06KUdTp%2B4g0Tpu9LUAxbJczjG8r4iRaZFDBUJ7t8xX3NxvbJVNHSjZUyqRQsX0eXnFRHicrpJuVGD8vBAOAeGQEm1XbdlopFF8sYAACcjxhjs9MXBrpmvzzRps9rumg5zZtFu9EcqjS781DkwtbuGzwY6pgGkKbdWVlZIdkMGG%2F9%2Be09j%2B%2BunWnOy%2BldvcAk4Cmw1F%2BQAjrd%2B1XxvXoDMq6kjnfPES4mYJOKx0DMxw5DwYR01tNnOV3rGTXq9i1x07JRcsN4WnZoq%2FuoCNGpHHZlx%2FG58gRP4M65stMWXhdvLQqP1Kr1TpwtVwAidCdDqiwSu3yPgd4PQq8okxwj6GwvDciZRIWQWcx0guwGFjTCt5ZgQ2Ydenl91&X-Amz-Signature=87db0c463bc0c6a80ed98a2ace0abff54d73d38d92d7d19846bb2a9cdc80d13d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCI7O5EL%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFG88PotzAvFRVNOzlFfJ7xtFVZCx6vGvUR8%2F7%2B%2FxmD8AiAOtygAROZudQRBOGOKICeKEPKNnl7n9YQlZjdCbzOLryqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNVlhOo7AI4GD%2BqDKtwDxSBSJFhtLAlgpG648Wv62%2FmIC0s5tLiKLTz4qhPWYJLP4NjJOywQ6h4Yc3XIYbsIgiS1cNxRERce82qc2MwVJgmAZZXEM0ZZ2RitrJEeF5RoWrFEgjrIqzVjfIOQdvtaeBIFGMG0DlfK0tSnuNmLYNJRmuPhGys8TMt6b7tl5M3nho8LJBo9U9KMRlo4YXNY0%2FpfOv4gCvpc1Hp5sUTHalTQRJ5tzRdwUV5C9dZbDD2964QEbmOv59niXvtTELLS5CxrfykwcOkYz2mkpuq3erVYcCKaMc8UfI6Cuk4gPoZJcmsCXlLbeKd6YvqyqNmnCfkmq8P4S0lLSs2yFSg03dAUbJ%2F6YuxK7jNy1JoMu91B%2BvupS%2F70J59BAN80xMNtkmsmpl%2Bt59qQhNYyjTuYfp%2Bj2FGvMWx2LjjvM9jwd6M5w7lUiS8ztLuOvwUQsr67%2B0MUO6DLs60Q5WHgnywAWj9TwiVE%2FTUL9q7FPKr48xa06KUdTp%2B4g0Tpu9LUAxbJczjG8r4iRaZFDBUJ7t8xX3NxvbJVNHSjZUyqRQsX0eXnFRHicrpJuVGD8vBAOAeGQEm1XbdlopFF8sYAACcjxhjs9MXBrpmvzzRps9rumg5zZtFu9EcqjS781DkwtbuGzwY6pgGkKbdWVlZIdkMGG%2F9%2Be09j%2B%2BunWnOy%2BldvcAk4Cmw1F%2BQAjrd%2B1XxvXoDMq6kjnfPES4mYJOKx0DMxw5DwYR01tNnOV3rGTXq9i1x07JRcsN4WnZoq%2FuoCNGpHHZlx%2FG58gRP4M65stMWXhdvLQqP1Kr1TpwtVwAidCdDqiwSu3yPgd4PQq8okxwj6GwvDciZRIWQWcx0guwGFjTCt5ZgQ2Ydenl91&X-Amz-Signature=311836bab5d0eca26011c7615e6f69d6eec755bb25a7df3755e603f1d463db49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCI7O5EL%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFG88PotzAvFRVNOzlFfJ7xtFVZCx6vGvUR8%2F7%2B%2FxmD8AiAOtygAROZudQRBOGOKICeKEPKNnl7n9YQlZjdCbzOLryqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNVlhOo7AI4GD%2BqDKtwDxSBSJFhtLAlgpG648Wv62%2FmIC0s5tLiKLTz4qhPWYJLP4NjJOywQ6h4Yc3XIYbsIgiS1cNxRERce82qc2MwVJgmAZZXEM0ZZ2RitrJEeF5RoWrFEgjrIqzVjfIOQdvtaeBIFGMG0DlfK0tSnuNmLYNJRmuPhGys8TMt6b7tl5M3nho8LJBo9U9KMRlo4YXNY0%2FpfOv4gCvpc1Hp5sUTHalTQRJ5tzRdwUV5C9dZbDD2964QEbmOv59niXvtTELLS5CxrfykwcOkYz2mkpuq3erVYcCKaMc8UfI6Cuk4gPoZJcmsCXlLbeKd6YvqyqNmnCfkmq8P4S0lLSs2yFSg03dAUbJ%2F6YuxK7jNy1JoMu91B%2BvupS%2F70J59BAN80xMNtkmsmpl%2Bt59qQhNYyjTuYfp%2Bj2FGvMWx2LjjvM9jwd6M5w7lUiS8ztLuOvwUQsr67%2B0MUO6DLs60Q5WHgnywAWj9TwiVE%2FTUL9q7FPKr48xa06KUdTp%2B4g0Tpu9LUAxbJczjG8r4iRaZFDBUJ7t8xX3NxvbJVNHSjZUyqRQsX0eXnFRHicrpJuVGD8vBAOAeGQEm1XbdlopFF8sYAACcjxhjs9MXBrpmvzzRps9rumg5zZtFu9EcqjS781DkwtbuGzwY6pgGkKbdWVlZIdkMGG%2F9%2Be09j%2B%2BunWnOy%2BldvcAk4Cmw1F%2BQAjrd%2B1XxvXoDMq6kjnfPES4mYJOKx0DMxw5DwYR01tNnOV3rGTXq9i1x07JRcsN4WnZoq%2FuoCNGpHHZlx%2FG58gRP4M65stMWXhdvLQqP1Kr1TpwtVwAidCdDqiwSu3yPgd4PQq8okxwj6GwvDciZRIWQWcx0guwGFjTCt5ZgQ2Ydenl91&X-Amz-Signature=167ad93f26b38be25f50987f80c1866d2da21f1dca7621e3ec98c9aa75f79b4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCI7O5EL%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFG88PotzAvFRVNOzlFfJ7xtFVZCx6vGvUR8%2F7%2B%2FxmD8AiAOtygAROZudQRBOGOKICeKEPKNnl7n9YQlZjdCbzOLryqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNVlhOo7AI4GD%2BqDKtwDxSBSJFhtLAlgpG648Wv62%2FmIC0s5tLiKLTz4qhPWYJLP4NjJOywQ6h4Yc3XIYbsIgiS1cNxRERce82qc2MwVJgmAZZXEM0ZZ2RitrJEeF5RoWrFEgjrIqzVjfIOQdvtaeBIFGMG0DlfK0tSnuNmLYNJRmuPhGys8TMt6b7tl5M3nho8LJBo9U9KMRlo4YXNY0%2FpfOv4gCvpc1Hp5sUTHalTQRJ5tzRdwUV5C9dZbDD2964QEbmOv59niXvtTELLS5CxrfykwcOkYz2mkpuq3erVYcCKaMc8UfI6Cuk4gPoZJcmsCXlLbeKd6YvqyqNmnCfkmq8P4S0lLSs2yFSg03dAUbJ%2F6YuxK7jNy1JoMu91B%2BvupS%2F70J59BAN80xMNtkmsmpl%2Bt59qQhNYyjTuYfp%2Bj2FGvMWx2LjjvM9jwd6M5w7lUiS8ztLuOvwUQsr67%2B0MUO6DLs60Q5WHgnywAWj9TwiVE%2FTUL9q7FPKr48xa06KUdTp%2B4g0Tpu9LUAxbJczjG8r4iRaZFDBUJ7t8xX3NxvbJVNHSjZUyqRQsX0eXnFRHicrpJuVGD8vBAOAeGQEm1XbdlopFF8sYAACcjxhjs9MXBrpmvzzRps9rumg5zZtFu9EcqjS781DkwtbuGzwY6pgGkKbdWVlZIdkMGG%2F9%2Be09j%2B%2BunWnOy%2BldvcAk4Cmw1F%2BQAjrd%2B1XxvXoDMq6kjnfPES4mYJOKx0DMxw5DwYR01tNnOV3rGTXq9i1x07JRcsN4WnZoq%2FuoCNGpHHZlx%2FG58gRP4M65stMWXhdvLQqP1Kr1TpwtVwAidCdDqiwSu3yPgd4PQq8okxwj6GwvDciZRIWQWcx0guwGFjTCt5ZgQ2Ydenl91&X-Amz-Signature=aa0b871a5df9638d267aace7b148136f2c2d1a74a9cdbeb0d67419ad4c434c81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCI7O5EL%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFG88PotzAvFRVNOzlFfJ7xtFVZCx6vGvUR8%2F7%2B%2FxmD8AiAOtygAROZudQRBOGOKICeKEPKNnl7n9YQlZjdCbzOLryqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNVlhOo7AI4GD%2BqDKtwDxSBSJFhtLAlgpG648Wv62%2FmIC0s5tLiKLTz4qhPWYJLP4NjJOywQ6h4Yc3XIYbsIgiS1cNxRERce82qc2MwVJgmAZZXEM0ZZ2RitrJEeF5RoWrFEgjrIqzVjfIOQdvtaeBIFGMG0DlfK0tSnuNmLYNJRmuPhGys8TMt6b7tl5M3nho8LJBo9U9KMRlo4YXNY0%2FpfOv4gCvpc1Hp5sUTHalTQRJ5tzRdwUV5C9dZbDD2964QEbmOv59niXvtTELLS5CxrfykwcOkYz2mkpuq3erVYcCKaMc8UfI6Cuk4gPoZJcmsCXlLbeKd6YvqyqNmnCfkmq8P4S0lLSs2yFSg03dAUbJ%2F6YuxK7jNy1JoMu91B%2BvupS%2F70J59BAN80xMNtkmsmpl%2Bt59qQhNYyjTuYfp%2Bj2FGvMWx2LjjvM9jwd6M5w7lUiS8ztLuOvwUQsr67%2B0MUO6DLs60Q5WHgnywAWj9TwiVE%2FTUL9q7FPKr48xa06KUdTp%2B4g0Tpu9LUAxbJczjG8r4iRaZFDBUJ7t8xX3NxvbJVNHSjZUyqRQsX0eXnFRHicrpJuVGD8vBAOAeGQEm1XbdlopFF8sYAACcjxhjs9MXBrpmvzzRps9rumg5zZtFu9EcqjS781DkwtbuGzwY6pgGkKbdWVlZIdkMGG%2F9%2Be09j%2B%2BunWnOy%2BldvcAk4Cmw1F%2BQAjrd%2B1XxvXoDMq6kjnfPES4mYJOKx0DMxw5DwYR01tNnOV3rGTXq9i1x07JRcsN4WnZoq%2FuoCNGpHHZlx%2FG58gRP4M65stMWXhdvLQqP1Kr1TpwtVwAidCdDqiwSu3yPgd4PQq8okxwj6GwvDciZRIWQWcx0guwGFjTCt5ZgQ2Ydenl91&X-Amz-Signature=f38734ceddf0f63a407377a199dbbb524e74d93f74cc3718df6c9176c5b1b612&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCI7O5EL%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFG88PotzAvFRVNOzlFfJ7xtFVZCx6vGvUR8%2F7%2B%2FxmD8AiAOtygAROZudQRBOGOKICeKEPKNnl7n9YQlZjdCbzOLryqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNVlhOo7AI4GD%2BqDKtwDxSBSJFhtLAlgpG648Wv62%2FmIC0s5tLiKLTz4qhPWYJLP4NjJOywQ6h4Yc3XIYbsIgiS1cNxRERce82qc2MwVJgmAZZXEM0ZZ2RitrJEeF5RoWrFEgjrIqzVjfIOQdvtaeBIFGMG0DlfK0tSnuNmLYNJRmuPhGys8TMt6b7tl5M3nho8LJBo9U9KMRlo4YXNY0%2FpfOv4gCvpc1Hp5sUTHalTQRJ5tzRdwUV5C9dZbDD2964QEbmOv59niXvtTELLS5CxrfykwcOkYz2mkpuq3erVYcCKaMc8UfI6Cuk4gPoZJcmsCXlLbeKd6YvqyqNmnCfkmq8P4S0lLSs2yFSg03dAUbJ%2F6YuxK7jNy1JoMu91B%2BvupS%2F70J59BAN80xMNtkmsmpl%2Bt59qQhNYyjTuYfp%2Bj2FGvMWx2LjjvM9jwd6M5w7lUiS8ztLuOvwUQsr67%2B0MUO6DLs60Q5WHgnywAWj9TwiVE%2FTUL9q7FPKr48xa06KUdTp%2B4g0Tpu9LUAxbJczjG8r4iRaZFDBUJ7t8xX3NxvbJVNHSjZUyqRQsX0eXnFRHicrpJuVGD8vBAOAeGQEm1XbdlopFF8sYAACcjxhjs9MXBrpmvzzRps9rumg5zZtFu9EcqjS781DkwtbuGzwY6pgGkKbdWVlZIdkMGG%2F9%2Be09j%2B%2BunWnOy%2BldvcAk4Cmw1F%2BQAjrd%2B1XxvXoDMq6kjnfPES4mYJOKx0DMxw5DwYR01tNnOV3rGTXq9i1x07JRcsN4WnZoq%2FuoCNGpHHZlx%2FG58gRP4M65stMWXhdvLQqP1Kr1TpwtVwAidCdDqiwSu3yPgd4PQq8okxwj6GwvDciZRIWQWcx0guwGFjTCt5ZgQ2Ydenl91&X-Amz-Signature=7aee0bab7b6a6155ef185bcfcfc325d5fc33df6da9b8919a4669e4ffb1428284&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCI7O5EL%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFG88PotzAvFRVNOzlFfJ7xtFVZCx6vGvUR8%2F7%2B%2FxmD8AiAOtygAROZudQRBOGOKICeKEPKNnl7n9YQlZjdCbzOLryqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNNVlhOo7AI4GD%2BqDKtwDxSBSJFhtLAlgpG648Wv62%2FmIC0s5tLiKLTz4qhPWYJLP4NjJOywQ6h4Yc3XIYbsIgiS1cNxRERce82qc2MwVJgmAZZXEM0ZZ2RitrJEeF5RoWrFEgjrIqzVjfIOQdvtaeBIFGMG0DlfK0tSnuNmLYNJRmuPhGys8TMt6b7tl5M3nho8LJBo9U9KMRlo4YXNY0%2FpfOv4gCvpc1Hp5sUTHalTQRJ5tzRdwUV5C9dZbDD2964QEbmOv59niXvtTELLS5CxrfykwcOkYz2mkpuq3erVYcCKaMc8UfI6Cuk4gPoZJcmsCXlLbeKd6YvqyqNmnCfkmq8P4S0lLSs2yFSg03dAUbJ%2F6YuxK7jNy1JoMu91B%2BvupS%2F70J59BAN80xMNtkmsmpl%2Bt59qQhNYyjTuYfp%2Bj2FGvMWx2LjjvM9jwd6M5w7lUiS8ztLuOvwUQsr67%2B0MUO6DLs60Q5WHgnywAWj9TwiVE%2FTUL9q7FPKr48xa06KUdTp%2B4g0Tpu9LUAxbJczjG8r4iRaZFDBUJ7t8xX3NxvbJVNHSjZUyqRQsX0eXnFRHicrpJuVGD8vBAOAeGQEm1XbdlopFF8sYAACcjxhjs9MXBrpmvzzRps9rumg5zZtFu9EcqjS781DkwtbuGzwY6pgGkKbdWVlZIdkMGG%2F9%2Be09j%2B%2BunWnOy%2BldvcAk4Cmw1F%2BQAjrd%2B1XxvXoDMq6kjnfPES4mYJOKx0DMxw5DwYR01tNnOV3rGTXq9i1x07JRcsN4WnZoq%2FuoCNGpHHZlx%2FG58gRP4M65stMWXhdvLQqP1Kr1TpwtVwAidCdDqiwSu3yPgd4PQq8okxwj6GwvDciZRIWQWcx0guwGFjTCt5ZgQ2Ydenl91&X-Amz-Signature=279b05d8172502082e647298ec5e89f7e7dd320d58f83fce9e0775da62a7e262&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

