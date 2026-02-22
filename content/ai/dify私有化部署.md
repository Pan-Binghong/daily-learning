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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34I37DH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9hJeg632lhaoSApcuIssXFeFGKtr39Al77CwsZp1JFAiEA9Clb8elj%2BFqcTPOtDBKOPsFgEXTZSnjjx379vlj1X1UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9fbRUKdBJPW9%2FTKSrcAw4VHd4nrABgli63zdqSQkr6uE3Nr9drGOegXfkGwsqJccxKbH6TQvcCsgsQfkxgSv9w%2FlJh3XHwyFoIdlZoAUeWnADzmxfWcz2NgIZmUWYCF2Mf7KsrbBixBan1qYPwU6VjtLYY%2FIwd3UL2c1BzHX7p%2FdzGeuLoQeUe8O2p6fQHhEUJF95G%2BuW61NpR4t%2FH71YLK%2B6Nvi%2BURJ32sKn8wI0zElG3wGQvgk0%2FlHc4Xz%2F1cp6lwgPbFGB8WgJ4qHQPQ4r198fX7Alc7QugMt5iXI%2F7Y6GBiWB6yQBIh6QbRQBUyErqA4VRD3SUAnsidRaA%2BU0YnK1v3IqTl5bE52bHzZ0EPQbK4nd6nsk7eh4kQ3oCtRJu9TvsTSJNMXukjAsg2JTyt4CB%2FASMTEIUElizHBmdU8nmgtpTYIeO%2FXcQtt0GQzvXGujDEFUXGmgWXbFTAKZD2SZcuF%2FUfuXTxVBHSE%2BBx625DGgCaQMHcw2CbAYBxF6B6wR4F7iJsbOdrxWj54F%2Fumb%2BZDbkiiaKaMD0KP6INqIJlTiE2%2F5kbFmXIiks9tvPWf64B0sOLA%2FdmDUPu2nfAgQEtBc9uaE39dahp9tHVpUdgiH7P8VhPVqJ2Sd0%2BasNVDs1KwGSWfUDMPXz6cwGOqUBbYvjrw0U3sbzbDHK5PjPcf4STqH%2BuClkX944yhKH%2Bp82ynZ5LPxcQtqwAlu5C0Vm6dNNzf8jgbh3RLZysZtQ1yitj0FfUJ15eZKn9n%2BqHBuXge77GJwABNXLo8dLs6NI%2B7UpNzbEFEVOYl2HFaiSPf6%2FTAvQXD%2FOmjiokL77wXcQwx0s2hEySfJdY4kVWJDxO8twoVSKr%2BmE9bOEOFBheU9iMQ1B&X-Amz-Signature=23d5cc813175fa017d92f5563410c242cbf69eef03ff14a456220c3a5c710916&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34I37DH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9hJeg632lhaoSApcuIssXFeFGKtr39Al77CwsZp1JFAiEA9Clb8elj%2BFqcTPOtDBKOPsFgEXTZSnjjx379vlj1X1UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9fbRUKdBJPW9%2FTKSrcAw4VHd4nrABgli63zdqSQkr6uE3Nr9drGOegXfkGwsqJccxKbH6TQvcCsgsQfkxgSv9w%2FlJh3XHwyFoIdlZoAUeWnADzmxfWcz2NgIZmUWYCF2Mf7KsrbBixBan1qYPwU6VjtLYY%2FIwd3UL2c1BzHX7p%2FdzGeuLoQeUe8O2p6fQHhEUJF95G%2BuW61NpR4t%2FH71YLK%2B6Nvi%2BURJ32sKn8wI0zElG3wGQvgk0%2FlHc4Xz%2F1cp6lwgPbFGB8WgJ4qHQPQ4r198fX7Alc7QugMt5iXI%2F7Y6GBiWB6yQBIh6QbRQBUyErqA4VRD3SUAnsidRaA%2BU0YnK1v3IqTl5bE52bHzZ0EPQbK4nd6nsk7eh4kQ3oCtRJu9TvsTSJNMXukjAsg2JTyt4CB%2FASMTEIUElizHBmdU8nmgtpTYIeO%2FXcQtt0GQzvXGujDEFUXGmgWXbFTAKZD2SZcuF%2FUfuXTxVBHSE%2BBx625DGgCaQMHcw2CbAYBxF6B6wR4F7iJsbOdrxWj54F%2Fumb%2BZDbkiiaKaMD0KP6INqIJlTiE2%2F5kbFmXIiks9tvPWf64B0sOLA%2FdmDUPu2nfAgQEtBc9uaE39dahp9tHVpUdgiH7P8VhPVqJ2Sd0%2BasNVDs1KwGSWfUDMPXz6cwGOqUBbYvjrw0U3sbzbDHK5PjPcf4STqH%2BuClkX944yhKH%2Bp82ynZ5LPxcQtqwAlu5C0Vm6dNNzf8jgbh3RLZysZtQ1yitj0FfUJ15eZKn9n%2BqHBuXge77GJwABNXLo8dLs6NI%2B7UpNzbEFEVOYl2HFaiSPf6%2FTAvQXD%2FOmjiokL77wXcQwx0s2hEySfJdY4kVWJDxO8twoVSKr%2BmE9bOEOFBheU9iMQ1B&X-Amz-Signature=d9c621d0d5565da53adfb530627b58d9820a928775b480a4d4373e5990069fd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34I37DH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9hJeg632lhaoSApcuIssXFeFGKtr39Al77CwsZp1JFAiEA9Clb8elj%2BFqcTPOtDBKOPsFgEXTZSnjjx379vlj1X1UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9fbRUKdBJPW9%2FTKSrcAw4VHd4nrABgli63zdqSQkr6uE3Nr9drGOegXfkGwsqJccxKbH6TQvcCsgsQfkxgSv9w%2FlJh3XHwyFoIdlZoAUeWnADzmxfWcz2NgIZmUWYCF2Mf7KsrbBixBan1qYPwU6VjtLYY%2FIwd3UL2c1BzHX7p%2FdzGeuLoQeUe8O2p6fQHhEUJF95G%2BuW61NpR4t%2FH71YLK%2B6Nvi%2BURJ32sKn8wI0zElG3wGQvgk0%2FlHc4Xz%2F1cp6lwgPbFGB8WgJ4qHQPQ4r198fX7Alc7QugMt5iXI%2F7Y6GBiWB6yQBIh6QbRQBUyErqA4VRD3SUAnsidRaA%2BU0YnK1v3IqTl5bE52bHzZ0EPQbK4nd6nsk7eh4kQ3oCtRJu9TvsTSJNMXukjAsg2JTyt4CB%2FASMTEIUElizHBmdU8nmgtpTYIeO%2FXcQtt0GQzvXGujDEFUXGmgWXbFTAKZD2SZcuF%2FUfuXTxVBHSE%2BBx625DGgCaQMHcw2CbAYBxF6B6wR4F7iJsbOdrxWj54F%2Fumb%2BZDbkiiaKaMD0KP6INqIJlTiE2%2F5kbFmXIiks9tvPWf64B0sOLA%2FdmDUPu2nfAgQEtBc9uaE39dahp9tHVpUdgiH7P8VhPVqJ2Sd0%2BasNVDs1KwGSWfUDMPXz6cwGOqUBbYvjrw0U3sbzbDHK5PjPcf4STqH%2BuClkX944yhKH%2Bp82ynZ5LPxcQtqwAlu5C0Vm6dNNzf8jgbh3RLZysZtQ1yitj0FfUJ15eZKn9n%2BqHBuXge77GJwABNXLo8dLs6NI%2B7UpNzbEFEVOYl2HFaiSPf6%2FTAvQXD%2FOmjiokL77wXcQwx0s2hEySfJdY4kVWJDxO8twoVSKr%2BmE9bOEOFBheU9iMQ1B&X-Amz-Signature=7103ff6e72fe874b1803c0faf89ded715d66720ca15f0a8d2cbbf2b8e5424d92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34I37DH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9hJeg632lhaoSApcuIssXFeFGKtr39Al77CwsZp1JFAiEA9Clb8elj%2BFqcTPOtDBKOPsFgEXTZSnjjx379vlj1X1UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9fbRUKdBJPW9%2FTKSrcAw4VHd4nrABgli63zdqSQkr6uE3Nr9drGOegXfkGwsqJccxKbH6TQvcCsgsQfkxgSv9w%2FlJh3XHwyFoIdlZoAUeWnADzmxfWcz2NgIZmUWYCF2Mf7KsrbBixBan1qYPwU6VjtLYY%2FIwd3UL2c1BzHX7p%2FdzGeuLoQeUe8O2p6fQHhEUJF95G%2BuW61NpR4t%2FH71YLK%2B6Nvi%2BURJ32sKn8wI0zElG3wGQvgk0%2FlHc4Xz%2F1cp6lwgPbFGB8WgJ4qHQPQ4r198fX7Alc7QugMt5iXI%2F7Y6GBiWB6yQBIh6QbRQBUyErqA4VRD3SUAnsidRaA%2BU0YnK1v3IqTl5bE52bHzZ0EPQbK4nd6nsk7eh4kQ3oCtRJu9TvsTSJNMXukjAsg2JTyt4CB%2FASMTEIUElizHBmdU8nmgtpTYIeO%2FXcQtt0GQzvXGujDEFUXGmgWXbFTAKZD2SZcuF%2FUfuXTxVBHSE%2BBx625DGgCaQMHcw2CbAYBxF6B6wR4F7iJsbOdrxWj54F%2Fumb%2BZDbkiiaKaMD0KP6INqIJlTiE2%2F5kbFmXIiks9tvPWf64B0sOLA%2FdmDUPu2nfAgQEtBc9uaE39dahp9tHVpUdgiH7P8VhPVqJ2Sd0%2BasNVDs1KwGSWfUDMPXz6cwGOqUBbYvjrw0U3sbzbDHK5PjPcf4STqH%2BuClkX944yhKH%2Bp82ynZ5LPxcQtqwAlu5C0Vm6dNNzf8jgbh3RLZysZtQ1yitj0FfUJ15eZKn9n%2BqHBuXge77GJwABNXLo8dLs6NI%2B7UpNzbEFEVOYl2HFaiSPf6%2FTAvQXD%2FOmjiokL77wXcQwx0s2hEySfJdY4kVWJDxO8twoVSKr%2BmE9bOEOFBheU9iMQ1B&X-Amz-Signature=8278f89043950326227743b642cee56e64d85b589ef0f712974eecf4000a1754&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34I37DH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9hJeg632lhaoSApcuIssXFeFGKtr39Al77CwsZp1JFAiEA9Clb8elj%2BFqcTPOtDBKOPsFgEXTZSnjjx379vlj1X1UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9fbRUKdBJPW9%2FTKSrcAw4VHd4nrABgli63zdqSQkr6uE3Nr9drGOegXfkGwsqJccxKbH6TQvcCsgsQfkxgSv9w%2FlJh3XHwyFoIdlZoAUeWnADzmxfWcz2NgIZmUWYCF2Mf7KsrbBixBan1qYPwU6VjtLYY%2FIwd3UL2c1BzHX7p%2FdzGeuLoQeUe8O2p6fQHhEUJF95G%2BuW61NpR4t%2FH71YLK%2B6Nvi%2BURJ32sKn8wI0zElG3wGQvgk0%2FlHc4Xz%2F1cp6lwgPbFGB8WgJ4qHQPQ4r198fX7Alc7QugMt5iXI%2F7Y6GBiWB6yQBIh6QbRQBUyErqA4VRD3SUAnsidRaA%2BU0YnK1v3IqTl5bE52bHzZ0EPQbK4nd6nsk7eh4kQ3oCtRJu9TvsTSJNMXukjAsg2JTyt4CB%2FASMTEIUElizHBmdU8nmgtpTYIeO%2FXcQtt0GQzvXGujDEFUXGmgWXbFTAKZD2SZcuF%2FUfuXTxVBHSE%2BBx625DGgCaQMHcw2CbAYBxF6B6wR4F7iJsbOdrxWj54F%2Fumb%2BZDbkiiaKaMD0KP6INqIJlTiE2%2F5kbFmXIiks9tvPWf64B0sOLA%2FdmDUPu2nfAgQEtBc9uaE39dahp9tHVpUdgiH7P8VhPVqJ2Sd0%2BasNVDs1KwGSWfUDMPXz6cwGOqUBbYvjrw0U3sbzbDHK5PjPcf4STqH%2BuClkX944yhKH%2Bp82ynZ5LPxcQtqwAlu5C0Vm6dNNzf8jgbh3RLZysZtQ1yitj0FfUJ15eZKn9n%2BqHBuXge77GJwABNXLo8dLs6NI%2B7UpNzbEFEVOYl2HFaiSPf6%2FTAvQXD%2FOmjiokL77wXcQwx0s2hEySfJdY4kVWJDxO8twoVSKr%2BmE9bOEOFBheU9iMQ1B&X-Amz-Signature=5beafcd320195f787daf287a57aac35559f665d1e14c1f7910082fe3732ee914&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34I37DH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9hJeg632lhaoSApcuIssXFeFGKtr39Al77CwsZp1JFAiEA9Clb8elj%2BFqcTPOtDBKOPsFgEXTZSnjjx379vlj1X1UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9fbRUKdBJPW9%2FTKSrcAw4VHd4nrABgli63zdqSQkr6uE3Nr9drGOegXfkGwsqJccxKbH6TQvcCsgsQfkxgSv9w%2FlJh3XHwyFoIdlZoAUeWnADzmxfWcz2NgIZmUWYCF2Mf7KsrbBixBan1qYPwU6VjtLYY%2FIwd3UL2c1BzHX7p%2FdzGeuLoQeUe8O2p6fQHhEUJF95G%2BuW61NpR4t%2FH71YLK%2B6Nvi%2BURJ32sKn8wI0zElG3wGQvgk0%2FlHc4Xz%2F1cp6lwgPbFGB8WgJ4qHQPQ4r198fX7Alc7QugMt5iXI%2F7Y6GBiWB6yQBIh6QbRQBUyErqA4VRD3SUAnsidRaA%2BU0YnK1v3IqTl5bE52bHzZ0EPQbK4nd6nsk7eh4kQ3oCtRJu9TvsTSJNMXukjAsg2JTyt4CB%2FASMTEIUElizHBmdU8nmgtpTYIeO%2FXcQtt0GQzvXGujDEFUXGmgWXbFTAKZD2SZcuF%2FUfuXTxVBHSE%2BBx625DGgCaQMHcw2CbAYBxF6B6wR4F7iJsbOdrxWj54F%2Fumb%2BZDbkiiaKaMD0KP6INqIJlTiE2%2F5kbFmXIiks9tvPWf64B0sOLA%2FdmDUPu2nfAgQEtBc9uaE39dahp9tHVpUdgiH7P8VhPVqJ2Sd0%2BasNVDs1KwGSWfUDMPXz6cwGOqUBbYvjrw0U3sbzbDHK5PjPcf4STqH%2BuClkX944yhKH%2Bp82ynZ5LPxcQtqwAlu5C0Vm6dNNzf8jgbh3RLZysZtQ1yitj0FfUJ15eZKn9n%2BqHBuXge77GJwABNXLo8dLs6NI%2B7UpNzbEFEVOYl2HFaiSPf6%2FTAvQXD%2FOmjiokL77wXcQwx0s2hEySfJdY4kVWJDxO8twoVSKr%2BmE9bOEOFBheU9iMQ1B&X-Amz-Signature=d6bffd14d5e8401177f2c0be9b71c8e450b122d0a034cc26c2c5d02c89dfde19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34I37DH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9hJeg632lhaoSApcuIssXFeFGKtr39Al77CwsZp1JFAiEA9Clb8elj%2BFqcTPOtDBKOPsFgEXTZSnjjx379vlj1X1UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9fbRUKdBJPW9%2FTKSrcAw4VHd4nrABgli63zdqSQkr6uE3Nr9drGOegXfkGwsqJccxKbH6TQvcCsgsQfkxgSv9w%2FlJh3XHwyFoIdlZoAUeWnADzmxfWcz2NgIZmUWYCF2Mf7KsrbBixBan1qYPwU6VjtLYY%2FIwd3UL2c1BzHX7p%2FdzGeuLoQeUe8O2p6fQHhEUJF95G%2BuW61NpR4t%2FH71YLK%2B6Nvi%2BURJ32sKn8wI0zElG3wGQvgk0%2FlHc4Xz%2F1cp6lwgPbFGB8WgJ4qHQPQ4r198fX7Alc7QugMt5iXI%2F7Y6GBiWB6yQBIh6QbRQBUyErqA4VRD3SUAnsidRaA%2BU0YnK1v3IqTl5bE52bHzZ0EPQbK4nd6nsk7eh4kQ3oCtRJu9TvsTSJNMXukjAsg2JTyt4CB%2FASMTEIUElizHBmdU8nmgtpTYIeO%2FXcQtt0GQzvXGujDEFUXGmgWXbFTAKZD2SZcuF%2FUfuXTxVBHSE%2BBx625DGgCaQMHcw2CbAYBxF6B6wR4F7iJsbOdrxWj54F%2Fumb%2BZDbkiiaKaMD0KP6INqIJlTiE2%2F5kbFmXIiks9tvPWf64B0sOLA%2FdmDUPu2nfAgQEtBc9uaE39dahp9tHVpUdgiH7P8VhPVqJ2Sd0%2BasNVDs1KwGSWfUDMPXz6cwGOqUBbYvjrw0U3sbzbDHK5PjPcf4STqH%2BuClkX944yhKH%2Bp82ynZ5LPxcQtqwAlu5C0Vm6dNNzf8jgbh3RLZysZtQ1yitj0FfUJ15eZKn9n%2BqHBuXge77GJwABNXLo8dLs6NI%2B7UpNzbEFEVOYl2HFaiSPf6%2FTAvQXD%2FOmjiokL77wXcQwx0s2hEySfJdY4kVWJDxO8twoVSKr%2BmE9bOEOFBheU9iMQ1B&X-Amz-Signature=d1958f0190789dec19a3cb5a72664d12ef201c1cae019168321f23766095d83c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34I37DH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9hJeg632lhaoSApcuIssXFeFGKtr39Al77CwsZp1JFAiEA9Clb8elj%2BFqcTPOtDBKOPsFgEXTZSnjjx379vlj1X1UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9fbRUKdBJPW9%2FTKSrcAw4VHd4nrABgli63zdqSQkr6uE3Nr9drGOegXfkGwsqJccxKbH6TQvcCsgsQfkxgSv9w%2FlJh3XHwyFoIdlZoAUeWnADzmxfWcz2NgIZmUWYCF2Mf7KsrbBixBan1qYPwU6VjtLYY%2FIwd3UL2c1BzHX7p%2FdzGeuLoQeUe8O2p6fQHhEUJF95G%2BuW61NpR4t%2FH71YLK%2B6Nvi%2BURJ32sKn8wI0zElG3wGQvgk0%2FlHc4Xz%2F1cp6lwgPbFGB8WgJ4qHQPQ4r198fX7Alc7QugMt5iXI%2F7Y6GBiWB6yQBIh6QbRQBUyErqA4VRD3SUAnsidRaA%2BU0YnK1v3IqTl5bE52bHzZ0EPQbK4nd6nsk7eh4kQ3oCtRJu9TvsTSJNMXukjAsg2JTyt4CB%2FASMTEIUElizHBmdU8nmgtpTYIeO%2FXcQtt0GQzvXGujDEFUXGmgWXbFTAKZD2SZcuF%2FUfuXTxVBHSE%2BBx625DGgCaQMHcw2CbAYBxF6B6wR4F7iJsbOdrxWj54F%2Fumb%2BZDbkiiaKaMD0KP6INqIJlTiE2%2F5kbFmXIiks9tvPWf64B0sOLA%2FdmDUPu2nfAgQEtBc9uaE39dahp9tHVpUdgiH7P8VhPVqJ2Sd0%2BasNVDs1KwGSWfUDMPXz6cwGOqUBbYvjrw0U3sbzbDHK5PjPcf4STqH%2BuClkX944yhKH%2Bp82ynZ5LPxcQtqwAlu5C0Vm6dNNzf8jgbh3RLZysZtQ1yitj0FfUJ15eZKn9n%2BqHBuXge77GJwABNXLo8dLs6NI%2B7UpNzbEFEVOYl2HFaiSPf6%2FTAvQXD%2FOmjiokL77wXcQwx0s2hEySfJdY4kVWJDxO8twoVSKr%2BmE9bOEOFBheU9iMQ1B&X-Amz-Signature=3ab84aadfa1bc14e4600914f8b3f26a5a93d05a4950d0175b75d0f01dfa84821&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34I37DH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9hJeg632lhaoSApcuIssXFeFGKtr39Al77CwsZp1JFAiEA9Clb8elj%2BFqcTPOtDBKOPsFgEXTZSnjjx379vlj1X1UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9fbRUKdBJPW9%2FTKSrcAw4VHd4nrABgli63zdqSQkr6uE3Nr9drGOegXfkGwsqJccxKbH6TQvcCsgsQfkxgSv9w%2FlJh3XHwyFoIdlZoAUeWnADzmxfWcz2NgIZmUWYCF2Mf7KsrbBixBan1qYPwU6VjtLYY%2FIwd3UL2c1BzHX7p%2FdzGeuLoQeUe8O2p6fQHhEUJF95G%2BuW61NpR4t%2FH71YLK%2B6Nvi%2BURJ32sKn8wI0zElG3wGQvgk0%2FlHc4Xz%2F1cp6lwgPbFGB8WgJ4qHQPQ4r198fX7Alc7QugMt5iXI%2F7Y6GBiWB6yQBIh6QbRQBUyErqA4VRD3SUAnsidRaA%2BU0YnK1v3IqTl5bE52bHzZ0EPQbK4nd6nsk7eh4kQ3oCtRJu9TvsTSJNMXukjAsg2JTyt4CB%2FASMTEIUElizHBmdU8nmgtpTYIeO%2FXcQtt0GQzvXGujDEFUXGmgWXbFTAKZD2SZcuF%2FUfuXTxVBHSE%2BBx625DGgCaQMHcw2CbAYBxF6B6wR4F7iJsbOdrxWj54F%2Fumb%2BZDbkiiaKaMD0KP6INqIJlTiE2%2F5kbFmXIiks9tvPWf64B0sOLA%2FdmDUPu2nfAgQEtBc9uaE39dahp9tHVpUdgiH7P8VhPVqJ2Sd0%2BasNVDs1KwGSWfUDMPXz6cwGOqUBbYvjrw0U3sbzbDHK5PjPcf4STqH%2BuClkX944yhKH%2Bp82ynZ5LPxcQtqwAlu5C0Vm6dNNzf8jgbh3RLZysZtQ1yitj0FfUJ15eZKn9n%2BqHBuXge77GJwABNXLo8dLs6NI%2B7UpNzbEFEVOYl2HFaiSPf6%2FTAvQXD%2FOmjiokL77wXcQwx0s2hEySfJdY4kVWJDxO8twoVSKr%2BmE9bOEOFBheU9iMQ1B&X-Amz-Signature=9bd6034c09275a83bdbd4f3d5dd11c6b461b5e6de739a3780e54b7f798fe3c89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S34I37DH%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9hJeg632lhaoSApcuIssXFeFGKtr39Al77CwsZp1JFAiEA9Clb8elj%2BFqcTPOtDBKOPsFgEXTZSnjjx379vlj1X1UqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI9fbRUKdBJPW9%2FTKSrcAw4VHd4nrABgli63zdqSQkr6uE3Nr9drGOegXfkGwsqJccxKbH6TQvcCsgsQfkxgSv9w%2FlJh3XHwyFoIdlZoAUeWnADzmxfWcz2NgIZmUWYCF2Mf7KsrbBixBan1qYPwU6VjtLYY%2FIwd3UL2c1BzHX7p%2FdzGeuLoQeUe8O2p6fQHhEUJF95G%2BuW61NpR4t%2FH71YLK%2B6Nvi%2BURJ32sKn8wI0zElG3wGQvgk0%2FlHc4Xz%2F1cp6lwgPbFGB8WgJ4qHQPQ4r198fX7Alc7QugMt5iXI%2F7Y6GBiWB6yQBIh6QbRQBUyErqA4VRD3SUAnsidRaA%2BU0YnK1v3IqTl5bE52bHzZ0EPQbK4nd6nsk7eh4kQ3oCtRJu9TvsTSJNMXukjAsg2JTyt4CB%2FASMTEIUElizHBmdU8nmgtpTYIeO%2FXcQtt0GQzvXGujDEFUXGmgWXbFTAKZD2SZcuF%2FUfuXTxVBHSE%2BBx625DGgCaQMHcw2CbAYBxF6B6wR4F7iJsbOdrxWj54F%2Fumb%2BZDbkiiaKaMD0KP6INqIJlTiE2%2F5kbFmXIiks9tvPWf64B0sOLA%2FdmDUPu2nfAgQEtBc9uaE39dahp9tHVpUdgiH7P8VhPVqJ2Sd0%2BasNVDs1KwGSWfUDMPXz6cwGOqUBbYvjrw0U3sbzbDHK5PjPcf4STqH%2BuClkX944yhKH%2Bp82ynZ5LPxcQtqwAlu5C0Vm6dNNzf8jgbh3RLZysZtQ1yitj0FfUJ15eZKn9n%2BqHBuXge77GJwABNXLo8dLs6NI%2B7UpNzbEFEVOYl2HFaiSPf6%2FTAvQXD%2FOmjiokL77wXcQwx0s2hEySfJdY4kVWJDxO8twoVSKr%2BmE9bOEOFBheU9iMQ1B&X-Amz-Signature=d1d8514a75333c076d1125438fc2b720a3fb8220b21ed66d1a6df949524c70d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

