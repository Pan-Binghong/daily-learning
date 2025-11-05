---
title: Dify私有化部署
date: '2024-11-15T09:08:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- Dify
categories:
- AI
---

# 1.创建服务器准备工作

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WQZLEZK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkuXgYgEvcEasOWi43WLeHHw3BGba%2BNqwfGQBTx%2FCPPgIhAOt2b%2Fdqr2XN4B%2F106rKhFMltklqB2vhMKeEAjYem1TwKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp8LOA%2BJuzemk6oQIq3ANLPDe2u2at1LQ4ws%2Fdik2bUkHFerEUNj6Rf0a7WCGit%2FnNexylBjpar4U2YifJgarFzwBs4Jn73TMRmCitZQ7CP4abDvCBj24nVueIVbUC18mjhpEIcIwP0I3sGB3p1kApxOK9OX68rIex0CgBEXWH9Za1w4V4a0%2FmcX%2FwhT8jJ0Xkwg%2FQD6nxrkH4Jzn%2F%2FH8C%2FUwSIKLq%2BBlyxKvGmrjFL%2FTt2X56LTDj4qAJxOzmLkxwtKsNeMbIdd%2BbNiI97EI8RQmgumIgCXEw88BfdzlzLQed7geiZfsxHCeroFOje9JrY2X42reB%2FAfieSKMFJnOqrZ5Kc3VUvi%2FhamtjmGtY18%2BUWV0QDBfAVLwjGXv1247CADxdUjYfWlbPKp8mdn662ao4s2rX82hgRfu8kIF7u%2FEKnWhSbHDudf3FRjKN180HCAGV7Bq3705H2YMc94r8q3QuKv1E82LI8%2B%2BLJ1NXWhguz4Wk7k9yQrf8gWgxJwyopnjKF6BOQkE71yeGZdetS72TFtmR%2FDQZgebPgR%2FwlyogZNclX2fKRkjppTCltAw1%2F6GDQg9vq5z9N0TEBZZC91I06MlH10jud9qXwhjuZbR2N0%2FmjqmZe5mi9aiV6VD%2Fn3tUtpVlwWDNjCwoqzIBjqkAcO5wuVruPzMwb6pxaEsv82EFXEzQ9f%2Bcq2KF3BrIaXAbG1mxwJ70w7zUS%2FErz1Qwz0Ry1obwbAZTTHXgiQUHM4nqzs6Y29nUHTd52grz7z8AxtcHHhE9GWYRxC6V7vCwEbLZvDalAhnKH3nwAegH8NQD4NL0wUqgxpu7N7uQmEzxz2vXhoHWZLo5EKGASiINbV3c2GPY6QCjz%2BdXzcZKk0avjW0&X-Amz-Signature=40dc886c5053457241314ac18e7074e2f84622822ee720d61a0251b98a44da32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WQZLEZK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkuXgYgEvcEasOWi43WLeHHw3BGba%2BNqwfGQBTx%2FCPPgIhAOt2b%2Fdqr2XN4B%2F106rKhFMltklqB2vhMKeEAjYem1TwKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp8LOA%2BJuzemk6oQIq3ANLPDe2u2at1LQ4ws%2Fdik2bUkHFerEUNj6Rf0a7WCGit%2FnNexylBjpar4U2YifJgarFzwBs4Jn73TMRmCitZQ7CP4abDvCBj24nVueIVbUC18mjhpEIcIwP0I3sGB3p1kApxOK9OX68rIex0CgBEXWH9Za1w4V4a0%2FmcX%2FwhT8jJ0Xkwg%2FQD6nxrkH4Jzn%2F%2FH8C%2FUwSIKLq%2BBlyxKvGmrjFL%2FTt2X56LTDj4qAJxOzmLkxwtKsNeMbIdd%2BbNiI97EI8RQmgumIgCXEw88BfdzlzLQed7geiZfsxHCeroFOje9JrY2X42reB%2FAfieSKMFJnOqrZ5Kc3VUvi%2FhamtjmGtY18%2BUWV0QDBfAVLwjGXv1247CADxdUjYfWlbPKp8mdn662ao4s2rX82hgRfu8kIF7u%2FEKnWhSbHDudf3FRjKN180HCAGV7Bq3705H2YMc94r8q3QuKv1E82LI8%2B%2BLJ1NXWhguz4Wk7k9yQrf8gWgxJwyopnjKF6BOQkE71yeGZdetS72TFtmR%2FDQZgebPgR%2FwlyogZNclX2fKRkjppTCltAw1%2F6GDQg9vq5z9N0TEBZZC91I06MlH10jud9qXwhjuZbR2N0%2FmjqmZe5mi9aiV6VD%2Fn3tUtpVlwWDNjCwoqzIBjqkAcO5wuVruPzMwb6pxaEsv82EFXEzQ9f%2Bcq2KF3BrIaXAbG1mxwJ70w7zUS%2FErz1Qwz0Ry1obwbAZTTHXgiQUHM4nqzs6Y29nUHTd52grz7z8AxtcHHhE9GWYRxC6V7vCwEbLZvDalAhnKH3nwAegH8NQD4NL0wUqgxpu7N7uQmEzxz2vXhoHWZLo5EKGASiINbV3c2GPY6QCjz%2BdXzcZKk0avjW0&X-Amz-Signature=de028e52a463d90d30e0af24b10a8682f05f6a03d72b12886a8327eb39d17202&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WQZLEZK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkuXgYgEvcEasOWi43WLeHHw3BGba%2BNqwfGQBTx%2FCPPgIhAOt2b%2Fdqr2XN4B%2F106rKhFMltklqB2vhMKeEAjYem1TwKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp8LOA%2BJuzemk6oQIq3ANLPDe2u2at1LQ4ws%2Fdik2bUkHFerEUNj6Rf0a7WCGit%2FnNexylBjpar4U2YifJgarFzwBs4Jn73TMRmCitZQ7CP4abDvCBj24nVueIVbUC18mjhpEIcIwP0I3sGB3p1kApxOK9OX68rIex0CgBEXWH9Za1w4V4a0%2FmcX%2FwhT8jJ0Xkwg%2FQD6nxrkH4Jzn%2F%2FH8C%2FUwSIKLq%2BBlyxKvGmrjFL%2FTt2X56LTDj4qAJxOzmLkxwtKsNeMbIdd%2BbNiI97EI8RQmgumIgCXEw88BfdzlzLQed7geiZfsxHCeroFOje9JrY2X42reB%2FAfieSKMFJnOqrZ5Kc3VUvi%2FhamtjmGtY18%2BUWV0QDBfAVLwjGXv1247CADxdUjYfWlbPKp8mdn662ao4s2rX82hgRfu8kIF7u%2FEKnWhSbHDudf3FRjKN180HCAGV7Bq3705H2YMc94r8q3QuKv1E82LI8%2B%2BLJ1NXWhguz4Wk7k9yQrf8gWgxJwyopnjKF6BOQkE71yeGZdetS72TFtmR%2FDQZgebPgR%2FwlyogZNclX2fKRkjppTCltAw1%2F6GDQg9vq5z9N0TEBZZC91I06MlH10jud9qXwhjuZbR2N0%2FmjqmZe5mi9aiV6VD%2Fn3tUtpVlwWDNjCwoqzIBjqkAcO5wuVruPzMwb6pxaEsv82EFXEzQ9f%2Bcq2KF3BrIaXAbG1mxwJ70w7zUS%2FErz1Qwz0Ry1obwbAZTTHXgiQUHM4nqzs6Y29nUHTd52grz7z8AxtcHHhE9GWYRxC6V7vCwEbLZvDalAhnKH3nwAegH8NQD4NL0wUqgxpu7N7uQmEzxz2vXhoHWZLo5EKGASiINbV3c2GPY6QCjz%2BdXzcZKk0avjW0&X-Amz-Signature=cb2eba31ef556365bbffa29e4f50b6cf85476620553e00e9fbb711db7aa32a71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WQZLEZK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkuXgYgEvcEasOWi43WLeHHw3BGba%2BNqwfGQBTx%2FCPPgIhAOt2b%2Fdqr2XN4B%2F106rKhFMltklqB2vhMKeEAjYem1TwKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp8LOA%2BJuzemk6oQIq3ANLPDe2u2at1LQ4ws%2Fdik2bUkHFerEUNj6Rf0a7WCGit%2FnNexylBjpar4U2YifJgarFzwBs4Jn73TMRmCitZQ7CP4abDvCBj24nVueIVbUC18mjhpEIcIwP0I3sGB3p1kApxOK9OX68rIex0CgBEXWH9Za1w4V4a0%2FmcX%2FwhT8jJ0Xkwg%2FQD6nxrkH4Jzn%2F%2FH8C%2FUwSIKLq%2BBlyxKvGmrjFL%2FTt2X56LTDj4qAJxOzmLkxwtKsNeMbIdd%2BbNiI97EI8RQmgumIgCXEw88BfdzlzLQed7geiZfsxHCeroFOje9JrY2X42reB%2FAfieSKMFJnOqrZ5Kc3VUvi%2FhamtjmGtY18%2BUWV0QDBfAVLwjGXv1247CADxdUjYfWlbPKp8mdn662ao4s2rX82hgRfu8kIF7u%2FEKnWhSbHDudf3FRjKN180HCAGV7Bq3705H2YMc94r8q3QuKv1E82LI8%2B%2BLJ1NXWhguz4Wk7k9yQrf8gWgxJwyopnjKF6BOQkE71yeGZdetS72TFtmR%2FDQZgebPgR%2FwlyogZNclX2fKRkjppTCltAw1%2F6GDQg9vq5z9N0TEBZZC91I06MlH10jud9qXwhjuZbR2N0%2FmjqmZe5mi9aiV6VD%2Fn3tUtpVlwWDNjCwoqzIBjqkAcO5wuVruPzMwb6pxaEsv82EFXEzQ9f%2Bcq2KF3BrIaXAbG1mxwJ70w7zUS%2FErz1Qwz0Ry1obwbAZTTHXgiQUHM4nqzs6Y29nUHTd52grz7z8AxtcHHhE9GWYRxC6V7vCwEbLZvDalAhnKH3nwAegH8NQD4NL0wUqgxpu7N7uQmEzxz2vXhoHWZLo5EKGASiINbV3c2GPY6QCjz%2BdXzcZKk0avjW0&X-Amz-Signature=9c6ea654499cc69926d0b3c595e63024285282372412b84a46be31cf01a6af92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WQZLEZK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkuXgYgEvcEasOWi43WLeHHw3BGba%2BNqwfGQBTx%2FCPPgIhAOt2b%2Fdqr2XN4B%2F106rKhFMltklqB2vhMKeEAjYem1TwKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp8LOA%2BJuzemk6oQIq3ANLPDe2u2at1LQ4ws%2Fdik2bUkHFerEUNj6Rf0a7WCGit%2FnNexylBjpar4U2YifJgarFzwBs4Jn73TMRmCitZQ7CP4abDvCBj24nVueIVbUC18mjhpEIcIwP0I3sGB3p1kApxOK9OX68rIex0CgBEXWH9Za1w4V4a0%2FmcX%2FwhT8jJ0Xkwg%2FQD6nxrkH4Jzn%2F%2FH8C%2FUwSIKLq%2BBlyxKvGmrjFL%2FTt2X56LTDj4qAJxOzmLkxwtKsNeMbIdd%2BbNiI97EI8RQmgumIgCXEw88BfdzlzLQed7geiZfsxHCeroFOje9JrY2X42reB%2FAfieSKMFJnOqrZ5Kc3VUvi%2FhamtjmGtY18%2BUWV0QDBfAVLwjGXv1247CADxdUjYfWlbPKp8mdn662ao4s2rX82hgRfu8kIF7u%2FEKnWhSbHDudf3FRjKN180HCAGV7Bq3705H2YMc94r8q3QuKv1E82LI8%2B%2BLJ1NXWhguz4Wk7k9yQrf8gWgxJwyopnjKF6BOQkE71yeGZdetS72TFtmR%2FDQZgebPgR%2FwlyogZNclX2fKRkjppTCltAw1%2F6GDQg9vq5z9N0TEBZZC91I06MlH10jud9qXwhjuZbR2N0%2FmjqmZe5mi9aiV6VD%2Fn3tUtpVlwWDNjCwoqzIBjqkAcO5wuVruPzMwb6pxaEsv82EFXEzQ9f%2Bcq2KF3BrIaXAbG1mxwJ70w7zUS%2FErz1Qwz0Ry1obwbAZTTHXgiQUHM4nqzs6Y29nUHTd52grz7z8AxtcHHhE9GWYRxC6V7vCwEbLZvDalAhnKH3nwAegH8NQD4NL0wUqgxpu7N7uQmEzxz2vXhoHWZLo5EKGASiINbV3c2GPY6QCjz%2BdXzcZKk0avjW0&X-Amz-Signature=f0dc8509ab034151880c863c9ed72bf321d75df5a3664c59ef88c15e18fea6ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WQZLEZK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkuXgYgEvcEasOWi43WLeHHw3BGba%2BNqwfGQBTx%2FCPPgIhAOt2b%2Fdqr2XN4B%2F106rKhFMltklqB2vhMKeEAjYem1TwKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp8LOA%2BJuzemk6oQIq3ANLPDe2u2at1LQ4ws%2Fdik2bUkHFerEUNj6Rf0a7WCGit%2FnNexylBjpar4U2YifJgarFzwBs4Jn73TMRmCitZQ7CP4abDvCBj24nVueIVbUC18mjhpEIcIwP0I3sGB3p1kApxOK9OX68rIex0CgBEXWH9Za1w4V4a0%2FmcX%2FwhT8jJ0Xkwg%2FQD6nxrkH4Jzn%2F%2FH8C%2FUwSIKLq%2BBlyxKvGmrjFL%2FTt2X56LTDj4qAJxOzmLkxwtKsNeMbIdd%2BbNiI97EI8RQmgumIgCXEw88BfdzlzLQed7geiZfsxHCeroFOje9JrY2X42reB%2FAfieSKMFJnOqrZ5Kc3VUvi%2FhamtjmGtY18%2BUWV0QDBfAVLwjGXv1247CADxdUjYfWlbPKp8mdn662ao4s2rX82hgRfu8kIF7u%2FEKnWhSbHDudf3FRjKN180HCAGV7Bq3705H2YMc94r8q3QuKv1E82LI8%2B%2BLJ1NXWhguz4Wk7k9yQrf8gWgxJwyopnjKF6BOQkE71yeGZdetS72TFtmR%2FDQZgebPgR%2FwlyogZNclX2fKRkjppTCltAw1%2F6GDQg9vq5z9N0TEBZZC91I06MlH10jud9qXwhjuZbR2N0%2FmjqmZe5mi9aiV6VD%2Fn3tUtpVlwWDNjCwoqzIBjqkAcO5wuVruPzMwb6pxaEsv82EFXEzQ9f%2Bcq2KF3BrIaXAbG1mxwJ70w7zUS%2FErz1Qwz0Ry1obwbAZTTHXgiQUHM4nqzs6Y29nUHTd52grz7z8AxtcHHhE9GWYRxC6V7vCwEbLZvDalAhnKH3nwAegH8NQD4NL0wUqgxpu7N7uQmEzxz2vXhoHWZLo5EKGASiINbV3c2GPY6QCjz%2BdXzcZKk0avjW0&X-Amz-Signature=d2bbdb2a409e352daf40abf722c39bc936a5fa8f58de6a092362e8d27a22a339&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WQZLEZK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkuXgYgEvcEasOWi43WLeHHw3BGba%2BNqwfGQBTx%2FCPPgIhAOt2b%2Fdqr2XN4B%2F106rKhFMltklqB2vhMKeEAjYem1TwKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp8LOA%2BJuzemk6oQIq3ANLPDe2u2at1LQ4ws%2Fdik2bUkHFerEUNj6Rf0a7WCGit%2FnNexylBjpar4U2YifJgarFzwBs4Jn73TMRmCitZQ7CP4abDvCBj24nVueIVbUC18mjhpEIcIwP0I3sGB3p1kApxOK9OX68rIex0CgBEXWH9Za1w4V4a0%2FmcX%2FwhT8jJ0Xkwg%2FQD6nxrkH4Jzn%2F%2FH8C%2FUwSIKLq%2BBlyxKvGmrjFL%2FTt2X56LTDj4qAJxOzmLkxwtKsNeMbIdd%2BbNiI97EI8RQmgumIgCXEw88BfdzlzLQed7geiZfsxHCeroFOje9JrY2X42reB%2FAfieSKMFJnOqrZ5Kc3VUvi%2FhamtjmGtY18%2BUWV0QDBfAVLwjGXv1247CADxdUjYfWlbPKp8mdn662ao4s2rX82hgRfu8kIF7u%2FEKnWhSbHDudf3FRjKN180HCAGV7Bq3705H2YMc94r8q3QuKv1E82LI8%2B%2BLJ1NXWhguz4Wk7k9yQrf8gWgxJwyopnjKF6BOQkE71yeGZdetS72TFtmR%2FDQZgebPgR%2FwlyogZNclX2fKRkjppTCltAw1%2F6GDQg9vq5z9N0TEBZZC91I06MlH10jud9qXwhjuZbR2N0%2FmjqmZe5mi9aiV6VD%2Fn3tUtpVlwWDNjCwoqzIBjqkAcO5wuVruPzMwb6pxaEsv82EFXEzQ9f%2Bcq2KF3BrIaXAbG1mxwJ70w7zUS%2FErz1Qwz0Ry1obwbAZTTHXgiQUHM4nqzs6Y29nUHTd52grz7z8AxtcHHhE9GWYRxC6V7vCwEbLZvDalAhnKH3nwAegH8NQD4NL0wUqgxpu7N7uQmEzxz2vXhoHWZLo5EKGASiINbV3c2GPY6QCjz%2BdXzcZKk0avjW0&X-Amz-Signature=bf3eff242528d28930684839d500cb9e667a1f3486b4626f37f0cb6b8e350b4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WQZLEZK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkuXgYgEvcEasOWi43WLeHHw3BGba%2BNqwfGQBTx%2FCPPgIhAOt2b%2Fdqr2XN4B%2F106rKhFMltklqB2vhMKeEAjYem1TwKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp8LOA%2BJuzemk6oQIq3ANLPDe2u2at1LQ4ws%2Fdik2bUkHFerEUNj6Rf0a7WCGit%2FnNexylBjpar4U2YifJgarFzwBs4Jn73TMRmCitZQ7CP4abDvCBj24nVueIVbUC18mjhpEIcIwP0I3sGB3p1kApxOK9OX68rIex0CgBEXWH9Za1w4V4a0%2FmcX%2FwhT8jJ0Xkwg%2FQD6nxrkH4Jzn%2F%2FH8C%2FUwSIKLq%2BBlyxKvGmrjFL%2FTt2X56LTDj4qAJxOzmLkxwtKsNeMbIdd%2BbNiI97EI8RQmgumIgCXEw88BfdzlzLQed7geiZfsxHCeroFOje9JrY2X42reB%2FAfieSKMFJnOqrZ5Kc3VUvi%2FhamtjmGtY18%2BUWV0QDBfAVLwjGXv1247CADxdUjYfWlbPKp8mdn662ao4s2rX82hgRfu8kIF7u%2FEKnWhSbHDudf3FRjKN180HCAGV7Bq3705H2YMc94r8q3QuKv1E82LI8%2B%2BLJ1NXWhguz4Wk7k9yQrf8gWgxJwyopnjKF6BOQkE71yeGZdetS72TFtmR%2FDQZgebPgR%2FwlyogZNclX2fKRkjppTCltAw1%2F6GDQg9vq5z9N0TEBZZC91I06MlH10jud9qXwhjuZbR2N0%2FmjqmZe5mi9aiV6VD%2Fn3tUtpVlwWDNjCwoqzIBjqkAcO5wuVruPzMwb6pxaEsv82EFXEzQ9f%2Bcq2KF3BrIaXAbG1mxwJ70w7zUS%2FErz1Qwz0Ry1obwbAZTTHXgiQUHM4nqzs6Y29nUHTd52grz7z8AxtcHHhE9GWYRxC6V7vCwEbLZvDalAhnKH3nwAegH8NQD4NL0wUqgxpu7N7uQmEzxz2vXhoHWZLo5EKGASiINbV3c2GPY6QCjz%2BdXzcZKk0avjW0&X-Amz-Signature=072a9bd747c3c8549b3d261e6b1c51de5dd9329dc527e4092045fb319d17f5d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WQZLEZK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkuXgYgEvcEasOWi43WLeHHw3BGba%2BNqwfGQBTx%2FCPPgIhAOt2b%2Fdqr2XN4B%2F106rKhFMltklqB2vhMKeEAjYem1TwKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp8LOA%2BJuzemk6oQIq3ANLPDe2u2at1LQ4ws%2Fdik2bUkHFerEUNj6Rf0a7WCGit%2FnNexylBjpar4U2YifJgarFzwBs4Jn73TMRmCitZQ7CP4abDvCBj24nVueIVbUC18mjhpEIcIwP0I3sGB3p1kApxOK9OX68rIex0CgBEXWH9Za1w4V4a0%2FmcX%2FwhT8jJ0Xkwg%2FQD6nxrkH4Jzn%2F%2FH8C%2FUwSIKLq%2BBlyxKvGmrjFL%2FTt2X56LTDj4qAJxOzmLkxwtKsNeMbIdd%2BbNiI97EI8RQmgumIgCXEw88BfdzlzLQed7geiZfsxHCeroFOje9JrY2X42reB%2FAfieSKMFJnOqrZ5Kc3VUvi%2FhamtjmGtY18%2BUWV0QDBfAVLwjGXv1247CADxdUjYfWlbPKp8mdn662ao4s2rX82hgRfu8kIF7u%2FEKnWhSbHDudf3FRjKN180HCAGV7Bq3705H2YMc94r8q3QuKv1E82LI8%2B%2BLJ1NXWhguz4Wk7k9yQrf8gWgxJwyopnjKF6BOQkE71yeGZdetS72TFtmR%2FDQZgebPgR%2FwlyogZNclX2fKRkjppTCltAw1%2F6GDQg9vq5z9N0TEBZZC91I06MlH10jud9qXwhjuZbR2N0%2FmjqmZe5mi9aiV6VD%2Fn3tUtpVlwWDNjCwoqzIBjqkAcO5wuVruPzMwb6pxaEsv82EFXEzQ9f%2Bcq2KF3BrIaXAbG1mxwJ70w7zUS%2FErz1Qwz0Ry1obwbAZTTHXgiQUHM4nqzs6Y29nUHTd52grz7z8AxtcHHhE9GWYRxC6V7vCwEbLZvDalAhnKH3nwAegH8NQD4NL0wUqgxpu7N7uQmEzxz2vXhoHWZLo5EKGASiINbV3c2GPY6QCjz%2BdXzcZKk0avjW0&X-Amz-Signature=a4b98f1e2952415fe5af785dd7a217f61952b57c5668245b7a972ed072d65481&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WQZLEZK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkuXgYgEvcEasOWi43WLeHHw3BGba%2BNqwfGQBTx%2FCPPgIhAOt2b%2Fdqr2XN4B%2F106rKhFMltklqB2vhMKeEAjYem1TwKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyp8LOA%2BJuzemk6oQIq3ANLPDe2u2at1LQ4ws%2Fdik2bUkHFerEUNj6Rf0a7WCGit%2FnNexylBjpar4U2YifJgarFzwBs4Jn73TMRmCitZQ7CP4abDvCBj24nVueIVbUC18mjhpEIcIwP0I3sGB3p1kApxOK9OX68rIex0CgBEXWH9Za1w4V4a0%2FmcX%2FwhT8jJ0Xkwg%2FQD6nxrkH4Jzn%2F%2FH8C%2FUwSIKLq%2BBlyxKvGmrjFL%2FTt2X56LTDj4qAJxOzmLkxwtKsNeMbIdd%2BbNiI97EI8RQmgumIgCXEw88BfdzlzLQed7geiZfsxHCeroFOje9JrY2X42reB%2FAfieSKMFJnOqrZ5Kc3VUvi%2FhamtjmGtY18%2BUWV0QDBfAVLwjGXv1247CADxdUjYfWlbPKp8mdn662ao4s2rX82hgRfu8kIF7u%2FEKnWhSbHDudf3FRjKN180HCAGV7Bq3705H2YMc94r8q3QuKv1E82LI8%2B%2BLJ1NXWhguz4Wk7k9yQrf8gWgxJwyopnjKF6BOQkE71yeGZdetS72TFtmR%2FDQZgebPgR%2FwlyogZNclX2fKRkjppTCltAw1%2F6GDQg9vq5z9N0TEBZZC91I06MlH10jud9qXwhjuZbR2N0%2FmjqmZe5mi9aiV6VD%2Fn3tUtpVlwWDNjCwoqzIBjqkAcO5wuVruPzMwb6pxaEsv82EFXEzQ9f%2Bcq2KF3BrIaXAbG1mxwJ70w7zUS%2FErz1Qwz0Ry1obwbAZTTHXgiQUHM4nqzs6Y29nUHTd52grz7z8AxtcHHhE9GWYRxC6V7vCwEbLZvDalAhnKH3nwAegH8NQD4NL0wUqgxpu7N7uQmEzxz2vXhoHWZLo5EKGASiINbV3c2GPY6QCjz%2BdXzcZKk0avjW0&X-Amz-Signature=2e335f2aa2be266c87d9f22085acf0426f155fd2434ae02b53eacd519d8e24c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

