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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY4OGW3E%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHV0ve6BYhed2f1wEmQD0VegOKqOZ56kqJzj7n%2BuKYfIAiB5Z%2FS1gE48lfQNN7C8CFix8vgtjmE24LsnJ3dUQzLiAiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo78lueSAzNu7YPIvKtwD4BIcOGIKe4FSR%2Bfz%2FwNYTC1%2BjwdW3DUJJuV7o5YzS%2BHNIgG7SbLO7yYZ4pW4n86ZCh1SXYH7RvjIuX2WZGTlL%2Fjbi3HFINTYzUnPaweZUqXbrNkTHb75k7dXUG0BNU6MUwN9jhaAzZsu4lt8eAsOi%2F86%2BBo9B%2BuBh0HsoeyW6rhh7Y0WngF7ybL5zPrjyHffPJ6kJ%2FCz5sIjObspkM3W2AN1opsd7Ov4mR8Tv51OBalrUN0D5XbQZjDxAPitbIMdrhusZv1iHn%2FjdFjb7C%2Fa5HvAJ1bqNqfl%2BGiX9UNc5HVK%2FMG3Cen%2FvcXxQ%2FlAlgQkyFRDC7Z0Z2lpbejITed%2B3IDftts5BWzrHkCp16shLIWmPxZf9p9RM7XMChGmEHQlMIECLVaSvjnXxy9nEea35dY3X7Yg3gRfHiRir2GjnCh7HR5BIrnyXsoBrpF5lpgcHGYGo3ZCV3%2BLMMCB7guBwIbIr8wnsgnsfiRk888NAEXvdFMGTtmAETWei%2FsEAw%2Fi2X7nyVZlDGDwp4vvBR0rJRTQXwXdPj8p%2FvI3t2Q1%2FFuKLsuWSQN2D8whzk0h0KQzEV7ZVxMFFolEyp6IeJFuo00ZZ9tYikHat%2FvACatSZKiz1%2BqBpZa9WOr11P4wrPeQywY6pgHNcv9e3hZYXxn9nyuN90DQT5DH8yIWxMVIHGYBcHZislsBYtnF1GUTU7pVtmI5MEtBDVcUrmmkCPbV142LjXvq967e4E9PKmiYFNzL1Tae%2BXEGCGrjPyMkS6D7GiojYqHbURl%2FTFEMYcIq9u1UA1gzJGP%2F%2Bwd6Ne40dkhpTlwtpXhtF4PmyX1hH6GTV6f8ByshLLo3986kAq3VpTz77NBleklCVoTI&X-Amz-Signature=378beec3906127c36a894fb1f859b7b08dc46eaa1db0af984d8eef8a52cdec39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY4OGW3E%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHV0ve6BYhed2f1wEmQD0VegOKqOZ56kqJzj7n%2BuKYfIAiB5Z%2FS1gE48lfQNN7C8CFix8vgtjmE24LsnJ3dUQzLiAiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo78lueSAzNu7YPIvKtwD4BIcOGIKe4FSR%2Bfz%2FwNYTC1%2BjwdW3DUJJuV7o5YzS%2BHNIgG7SbLO7yYZ4pW4n86ZCh1SXYH7RvjIuX2WZGTlL%2Fjbi3HFINTYzUnPaweZUqXbrNkTHb75k7dXUG0BNU6MUwN9jhaAzZsu4lt8eAsOi%2F86%2BBo9B%2BuBh0HsoeyW6rhh7Y0WngF7ybL5zPrjyHffPJ6kJ%2FCz5sIjObspkM3W2AN1opsd7Ov4mR8Tv51OBalrUN0D5XbQZjDxAPitbIMdrhusZv1iHn%2FjdFjb7C%2Fa5HvAJ1bqNqfl%2BGiX9UNc5HVK%2FMG3Cen%2FvcXxQ%2FlAlgQkyFRDC7Z0Z2lpbejITed%2B3IDftts5BWzrHkCp16shLIWmPxZf9p9RM7XMChGmEHQlMIECLVaSvjnXxy9nEea35dY3X7Yg3gRfHiRir2GjnCh7HR5BIrnyXsoBrpF5lpgcHGYGo3ZCV3%2BLMMCB7guBwIbIr8wnsgnsfiRk888NAEXvdFMGTtmAETWei%2FsEAw%2Fi2X7nyVZlDGDwp4vvBR0rJRTQXwXdPj8p%2FvI3t2Q1%2FFuKLsuWSQN2D8whzk0h0KQzEV7ZVxMFFolEyp6IeJFuo00ZZ9tYikHat%2FvACatSZKiz1%2BqBpZa9WOr11P4wrPeQywY6pgHNcv9e3hZYXxn9nyuN90DQT5DH8yIWxMVIHGYBcHZislsBYtnF1GUTU7pVtmI5MEtBDVcUrmmkCPbV142LjXvq967e4E9PKmiYFNzL1Tae%2BXEGCGrjPyMkS6D7GiojYqHbURl%2FTFEMYcIq9u1UA1gzJGP%2F%2Bwd6Ne40dkhpTlwtpXhtF4PmyX1hH6GTV6f8ByshLLo3986kAq3VpTz77NBleklCVoTI&X-Amz-Signature=7bc42be8abb8085b050d27851085d63c5ee9d13edaa0fb67a17ae4c53da3525c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY4OGW3E%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHV0ve6BYhed2f1wEmQD0VegOKqOZ56kqJzj7n%2BuKYfIAiB5Z%2FS1gE48lfQNN7C8CFix8vgtjmE24LsnJ3dUQzLiAiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo78lueSAzNu7YPIvKtwD4BIcOGIKe4FSR%2Bfz%2FwNYTC1%2BjwdW3DUJJuV7o5YzS%2BHNIgG7SbLO7yYZ4pW4n86ZCh1SXYH7RvjIuX2WZGTlL%2Fjbi3HFINTYzUnPaweZUqXbrNkTHb75k7dXUG0BNU6MUwN9jhaAzZsu4lt8eAsOi%2F86%2BBo9B%2BuBh0HsoeyW6rhh7Y0WngF7ybL5zPrjyHffPJ6kJ%2FCz5sIjObspkM3W2AN1opsd7Ov4mR8Tv51OBalrUN0D5XbQZjDxAPitbIMdrhusZv1iHn%2FjdFjb7C%2Fa5HvAJ1bqNqfl%2BGiX9UNc5HVK%2FMG3Cen%2FvcXxQ%2FlAlgQkyFRDC7Z0Z2lpbejITed%2B3IDftts5BWzrHkCp16shLIWmPxZf9p9RM7XMChGmEHQlMIECLVaSvjnXxy9nEea35dY3X7Yg3gRfHiRir2GjnCh7HR5BIrnyXsoBrpF5lpgcHGYGo3ZCV3%2BLMMCB7guBwIbIr8wnsgnsfiRk888NAEXvdFMGTtmAETWei%2FsEAw%2Fi2X7nyVZlDGDwp4vvBR0rJRTQXwXdPj8p%2FvI3t2Q1%2FFuKLsuWSQN2D8whzk0h0KQzEV7ZVxMFFolEyp6IeJFuo00ZZ9tYikHat%2FvACatSZKiz1%2BqBpZa9WOr11P4wrPeQywY6pgHNcv9e3hZYXxn9nyuN90DQT5DH8yIWxMVIHGYBcHZislsBYtnF1GUTU7pVtmI5MEtBDVcUrmmkCPbV142LjXvq967e4E9PKmiYFNzL1Tae%2BXEGCGrjPyMkS6D7GiojYqHbURl%2FTFEMYcIq9u1UA1gzJGP%2F%2Bwd6Ne40dkhpTlwtpXhtF4PmyX1hH6GTV6f8ByshLLo3986kAq3VpTz77NBleklCVoTI&X-Amz-Signature=7bf75aa21bec677f5619e9fd22bf43d07eb6d3facb4acda032e638cbde636102&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY4OGW3E%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHV0ve6BYhed2f1wEmQD0VegOKqOZ56kqJzj7n%2BuKYfIAiB5Z%2FS1gE48lfQNN7C8CFix8vgtjmE24LsnJ3dUQzLiAiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo78lueSAzNu7YPIvKtwD4BIcOGIKe4FSR%2Bfz%2FwNYTC1%2BjwdW3DUJJuV7o5YzS%2BHNIgG7SbLO7yYZ4pW4n86ZCh1SXYH7RvjIuX2WZGTlL%2Fjbi3HFINTYzUnPaweZUqXbrNkTHb75k7dXUG0BNU6MUwN9jhaAzZsu4lt8eAsOi%2F86%2BBo9B%2BuBh0HsoeyW6rhh7Y0WngF7ybL5zPrjyHffPJ6kJ%2FCz5sIjObspkM3W2AN1opsd7Ov4mR8Tv51OBalrUN0D5XbQZjDxAPitbIMdrhusZv1iHn%2FjdFjb7C%2Fa5HvAJ1bqNqfl%2BGiX9UNc5HVK%2FMG3Cen%2FvcXxQ%2FlAlgQkyFRDC7Z0Z2lpbejITed%2B3IDftts5BWzrHkCp16shLIWmPxZf9p9RM7XMChGmEHQlMIECLVaSvjnXxy9nEea35dY3X7Yg3gRfHiRir2GjnCh7HR5BIrnyXsoBrpF5lpgcHGYGo3ZCV3%2BLMMCB7guBwIbIr8wnsgnsfiRk888NAEXvdFMGTtmAETWei%2FsEAw%2Fi2X7nyVZlDGDwp4vvBR0rJRTQXwXdPj8p%2FvI3t2Q1%2FFuKLsuWSQN2D8whzk0h0KQzEV7ZVxMFFolEyp6IeJFuo00ZZ9tYikHat%2FvACatSZKiz1%2BqBpZa9WOr11P4wrPeQywY6pgHNcv9e3hZYXxn9nyuN90DQT5DH8yIWxMVIHGYBcHZislsBYtnF1GUTU7pVtmI5MEtBDVcUrmmkCPbV142LjXvq967e4E9PKmiYFNzL1Tae%2BXEGCGrjPyMkS6D7GiojYqHbURl%2FTFEMYcIq9u1UA1gzJGP%2F%2Bwd6Ne40dkhpTlwtpXhtF4PmyX1hH6GTV6f8ByshLLo3986kAq3VpTz77NBleklCVoTI&X-Amz-Signature=a29214de0adfaef5f362502431f2fe3378f1012ad38b0b691dec1210e324e560&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY4OGW3E%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHV0ve6BYhed2f1wEmQD0VegOKqOZ56kqJzj7n%2BuKYfIAiB5Z%2FS1gE48lfQNN7C8CFix8vgtjmE24LsnJ3dUQzLiAiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo78lueSAzNu7YPIvKtwD4BIcOGIKe4FSR%2Bfz%2FwNYTC1%2BjwdW3DUJJuV7o5YzS%2BHNIgG7SbLO7yYZ4pW4n86ZCh1SXYH7RvjIuX2WZGTlL%2Fjbi3HFINTYzUnPaweZUqXbrNkTHb75k7dXUG0BNU6MUwN9jhaAzZsu4lt8eAsOi%2F86%2BBo9B%2BuBh0HsoeyW6rhh7Y0WngF7ybL5zPrjyHffPJ6kJ%2FCz5sIjObspkM3W2AN1opsd7Ov4mR8Tv51OBalrUN0D5XbQZjDxAPitbIMdrhusZv1iHn%2FjdFjb7C%2Fa5HvAJ1bqNqfl%2BGiX9UNc5HVK%2FMG3Cen%2FvcXxQ%2FlAlgQkyFRDC7Z0Z2lpbejITed%2B3IDftts5BWzrHkCp16shLIWmPxZf9p9RM7XMChGmEHQlMIECLVaSvjnXxy9nEea35dY3X7Yg3gRfHiRir2GjnCh7HR5BIrnyXsoBrpF5lpgcHGYGo3ZCV3%2BLMMCB7guBwIbIr8wnsgnsfiRk888NAEXvdFMGTtmAETWei%2FsEAw%2Fi2X7nyVZlDGDwp4vvBR0rJRTQXwXdPj8p%2FvI3t2Q1%2FFuKLsuWSQN2D8whzk0h0KQzEV7ZVxMFFolEyp6IeJFuo00ZZ9tYikHat%2FvACatSZKiz1%2BqBpZa9WOr11P4wrPeQywY6pgHNcv9e3hZYXxn9nyuN90DQT5DH8yIWxMVIHGYBcHZislsBYtnF1GUTU7pVtmI5MEtBDVcUrmmkCPbV142LjXvq967e4E9PKmiYFNzL1Tae%2BXEGCGrjPyMkS6D7GiojYqHbURl%2FTFEMYcIq9u1UA1gzJGP%2F%2Bwd6Ne40dkhpTlwtpXhtF4PmyX1hH6GTV6f8ByshLLo3986kAq3VpTz77NBleklCVoTI&X-Amz-Signature=463deaacc1506f322654c7fac88f503c5fd5d035c24f82e7527d3f772a654bba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY4OGW3E%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHV0ve6BYhed2f1wEmQD0VegOKqOZ56kqJzj7n%2BuKYfIAiB5Z%2FS1gE48lfQNN7C8CFix8vgtjmE24LsnJ3dUQzLiAiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo78lueSAzNu7YPIvKtwD4BIcOGIKe4FSR%2Bfz%2FwNYTC1%2BjwdW3DUJJuV7o5YzS%2BHNIgG7SbLO7yYZ4pW4n86ZCh1SXYH7RvjIuX2WZGTlL%2Fjbi3HFINTYzUnPaweZUqXbrNkTHb75k7dXUG0BNU6MUwN9jhaAzZsu4lt8eAsOi%2F86%2BBo9B%2BuBh0HsoeyW6rhh7Y0WngF7ybL5zPrjyHffPJ6kJ%2FCz5sIjObspkM3W2AN1opsd7Ov4mR8Tv51OBalrUN0D5XbQZjDxAPitbIMdrhusZv1iHn%2FjdFjb7C%2Fa5HvAJ1bqNqfl%2BGiX9UNc5HVK%2FMG3Cen%2FvcXxQ%2FlAlgQkyFRDC7Z0Z2lpbejITed%2B3IDftts5BWzrHkCp16shLIWmPxZf9p9RM7XMChGmEHQlMIECLVaSvjnXxy9nEea35dY3X7Yg3gRfHiRir2GjnCh7HR5BIrnyXsoBrpF5lpgcHGYGo3ZCV3%2BLMMCB7guBwIbIr8wnsgnsfiRk888NAEXvdFMGTtmAETWei%2FsEAw%2Fi2X7nyVZlDGDwp4vvBR0rJRTQXwXdPj8p%2FvI3t2Q1%2FFuKLsuWSQN2D8whzk0h0KQzEV7ZVxMFFolEyp6IeJFuo00ZZ9tYikHat%2FvACatSZKiz1%2BqBpZa9WOr11P4wrPeQywY6pgHNcv9e3hZYXxn9nyuN90DQT5DH8yIWxMVIHGYBcHZislsBYtnF1GUTU7pVtmI5MEtBDVcUrmmkCPbV142LjXvq967e4E9PKmiYFNzL1Tae%2BXEGCGrjPyMkS6D7GiojYqHbURl%2FTFEMYcIq9u1UA1gzJGP%2F%2Bwd6Ne40dkhpTlwtpXhtF4PmyX1hH6GTV6f8ByshLLo3986kAq3VpTz77NBleklCVoTI&X-Amz-Signature=d88ab9c36e8704aea1e9fbc5c56b9e3b21831d4a70f300fb08076ca3637ff437&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY4OGW3E%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHV0ve6BYhed2f1wEmQD0VegOKqOZ56kqJzj7n%2BuKYfIAiB5Z%2FS1gE48lfQNN7C8CFix8vgtjmE24LsnJ3dUQzLiAiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo78lueSAzNu7YPIvKtwD4BIcOGIKe4FSR%2Bfz%2FwNYTC1%2BjwdW3DUJJuV7o5YzS%2BHNIgG7SbLO7yYZ4pW4n86ZCh1SXYH7RvjIuX2WZGTlL%2Fjbi3HFINTYzUnPaweZUqXbrNkTHb75k7dXUG0BNU6MUwN9jhaAzZsu4lt8eAsOi%2F86%2BBo9B%2BuBh0HsoeyW6rhh7Y0WngF7ybL5zPrjyHffPJ6kJ%2FCz5sIjObspkM3W2AN1opsd7Ov4mR8Tv51OBalrUN0D5XbQZjDxAPitbIMdrhusZv1iHn%2FjdFjb7C%2Fa5HvAJ1bqNqfl%2BGiX9UNc5HVK%2FMG3Cen%2FvcXxQ%2FlAlgQkyFRDC7Z0Z2lpbejITed%2B3IDftts5BWzrHkCp16shLIWmPxZf9p9RM7XMChGmEHQlMIECLVaSvjnXxy9nEea35dY3X7Yg3gRfHiRir2GjnCh7HR5BIrnyXsoBrpF5lpgcHGYGo3ZCV3%2BLMMCB7guBwIbIr8wnsgnsfiRk888NAEXvdFMGTtmAETWei%2FsEAw%2Fi2X7nyVZlDGDwp4vvBR0rJRTQXwXdPj8p%2FvI3t2Q1%2FFuKLsuWSQN2D8whzk0h0KQzEV7ZVxMFFolEyp6IeJFuo00ZZ9tYikHat%2FvACatSZKiz1%2BqBpZa9WOr11P4wrPeQywY6pgHNcv9e3hZYXxn9nyuN90DQT5DH8yIWxMVIHGYBcHZislsBYtnF1GUTU7pVtmI5MEtBDVcUrmmkCPbV142LjXvq967e4E9PKmiYFNzL1Tae%2BXEGCGrjPyMkS6D7GiojYqHbURl%2FTFEMYcIq9u1UA1gzJGP%2F%2Bwd6Ne40dkhpTlwtpXhtF4PmyX1hH6GTV6f8ByshLLo3986kAq3VpTz77NBleklCVoTI&X-Amz-Signature=8cf2f1d20f753165eae1e5ac14dd0b200fc2070b05ab7127cc11504459b0a80e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY4OGW3E%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHV0ve6BYhed2f1wEmQD0VegOKqOZ56kqJzj7n%2BuKYfIAiB5Z%2FS1gE48lfQNN7C8CFix8vgtjmE24LsnJ3dUQzLiAiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo78lueSAzNu7YPIvKtwD4BIcOGIKe4FSR%2Bfz%2FwNYTC1%2BjwdW3DUJJuV7o5YzS%2BHNIgG7SbLO7yYZ4pW4n86ZCh1SXYH7RvjIuX2WZGTlL%2Fjbi3HFINTYzUnPaweZUqXbrNkTHb75k7dXUG0BNU6MUwN9jhaAzZsu4lt8eAsOi%2F86%2BBo9B%2BuBh0HsoeyW6rhh7Y0WngF7ybL5zPrjyHffPJ6kJ%2FCz5sIjObspkM3W2AN1opsd7Ov4mR8Tv51OBalrUN0D5XbQZjDxAPitbIMdrhusZv1iHn%2FjdFjb7C%2Fa5HvAJ1bqNqfl%2BGiX9UNc5HVK%2FMG3Cen%2FvcXxQ%2FlAlgQkyFRDC7Z0Z2lpbejITed%2B3IDftts5BWzrHkCp16shLIWmPxZf9p9RM7XMChGmEHQlMIECLVaSvjnXxy9nEea35dY3X7Yg3gRfHiRir2GjnCh7HR5BIrnyXsoBrpF5lpgcHGYGo3ZCV3%2BLMMCB7guBwIbIr8wnsgnsfiRk888NAEXvdFMGTtmAETWei%2FsEAw%2Fi2X7nyVZlDGDwp4vvBR0rJRTQXwXdPj8p%2FvI3t2Q1%2FFuKLsuWSQN2D8whzk0h0KQzEV7ZVxMFFolEyp6IeJFuo00ZZ9tYikHat%2FvACatSZKiz1%2BqBpZa9WOr11P4wrPeQywY6pgHNcv9e3hZYXxn9nyuN90DQT5DH8yIWxMVIHGYBcHZislsBYtnF1GUTU7pVtmI5MEtBDVcUrmmkCPbV142LjXvq967e4E9PKmiYFNzL1Tae%2BXEGCGrjPyMkS6D7GiojYqHbURl%2FTFEMYcIq9u1UA1gzJGP%2F%2Bwd6Ne40dkhpTlwtpXhtF4PmyX1hH6GTV6f8ByshLLo3986kAq3VpTz77NBleklCVoTI&X-Amz-Signature=4f50e3333c38048c06b3104c69709657acdd942aab49d2c3a1bbf10fb2906800&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY4OGW3E%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHV0ve6BYhed2f1wEmQD0VegOKqOZ56kqJzj7n%2BuKYfIAiB5Z%2FS1gE48lfQNN7C8CFix8vgtjmE24LsnJ3dUQzLiAiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo78lueSAzNu7YPIvKtwD4BIcOGIKe4FSR%2Bfz%2FwNYTC1%2BjwdW3DUJJuV7o5YzS%2BHNIgG7SbLO7yYZ4pW4n86ZCh1SXYH7RvjIuX2WZGTlL%2Fjbi3HFINTYzUnPaweZUqXbrNkTHb75k7dXUG0BNU6MUwN9jhaAzZsu4lt8eAsOi%2F86%2BBo9B%2BuBh0HsoeyW6rhh7Y0WngF7ybL5zPrjyHffPJ6kJ%2FCz5sIjObspkM3W2AN1opsd7Ov4mR8Tv51OBalrUN0D5XbQZjDxAPitbIMdrhusZv1iHn%2FjdFjb7C%2Fa5HvAJ1bqNqfl%2BGiX9UNc5HVK%2FMG3Cen%2FvcXxQ%2FlAlgQkyFRDC7Z0Z2lpbejITed%2B3IDftts5BWzrHkCp16shLIWmPxZf9p9RM7XMChGmEHQlMIECLVaSvjnXxy9nEea35dY3X7Yg3gRfHiRir2GjnCh7HR5BIrnyXsoBrpF5lpgcHGYGo3ZCV3%2BLMMCB7guBwIbIr8wnsgnsfiRk888NAEXvdFMGTtmAETWei%2FsEAw%2Fi2X7nyVZlDGDwp4vvBR0rJRTQXwXdPj8p%2FvI3t2Q1%2FFuKLsuWSQN2D8whzk0h0KQzEV7ZVxMFFolEyp6IeJFuo00ZZ9tYikHat%2FvACatSZKiz1%2BqBpZa9WOr11P4wrPeQywY6pgHNcv9e3hZYXxn9nyuN90DQT5DH8yIWxMVIHGYBcHZislsBYtnF1GUTU7pVtmI5MEtBDVcUrmmkCPbV142LjXvq967e4E9PKmiYFNzL1Tae%2BXEGCGrjPyMkS6D7GiojYqHbURl%2FTFEMYcIq9u1UA1gzJGP%2F%2Bwd6Ne40dkhpTlwtpXhtF4PmyX1hH6GTV6f8ByshLLo3986kAq3VpTz77NBleklCVoTI&X-Amz-Signature=cbad5143c8c0b4fcbc360de681ccedccbb056930981e5605d33bd5045400ceac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY4OGW3E%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHV0ve6BYhed2f1wEmQD0VegOKqOZ56kqJzj7n%2BuKYfIAiB5Z%2FS1gE48lfQNN7C8CFix8vgtjmE24LsnJ3dUQzLiAiqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMo78lueSAzNu7YPIvKtwD4BIcOGIKe4FSR%2Bfz%2FwNYTC1%2BjwdW3DUJJuV7o5YzS%2BHNIgG7SbLO7yYZ4pW4n86ZCh1SXYH7RvjIuX2WZGTlL%2Fjbi3HFINTYzUnPaweZUqXbrNkTHb75k7dXUG0BNU6MUwN9jhaAzZsu4lt8eAsOi%2F86%2BBo9B%2BuBh0HsoeyW6rhh7Y0WngF7ybL5zPrjyHffPJ6kJ%2FCz5sIjObspkM3W2AN1opsd7Ov4mR8Tv51OBalrUN0D5XbQZjDxAPitbIMdrhusZv1iHn%2FjdFjb7C%2Fa5HvAJ1bqNqfl%2BGiX9UNc5HVK%2FMG3Cen%2FvcXxQ%2FlAlgQkyFRDC7Z0Z2lpbejITed%2B3IDftts5BWzrHkCp16shLIWmPxZf9p9RM7XMChGmEHQlMIECLVaSvjnXxy9nEea35dY3X7Yg3gRfHiRir2GjnCh7HR5BIrnyXsoBrpF5lpgcHGYGo3ZCV3%2BLMMCB7guBwIbIr8wnsgnsfiRk888NAEXvdFMGTtmAETWei%2FsEAw%2Fi2X7nyVZlDGDwp4vvBR0rJRTQXwXdPj8p%2FvI3t2Q1%2FFuKLsuWSQN2D8whzk0h0KQzEV7ZVxMFFolEyp6IeJFuo00ZZ9tYikHat%2FvACatSZKiz1%2BqBpZa9WOr11P4wrPeQywY6pgHNcv9e3hZYXxn9nyuN90DQT5DH8yIWxMVIHGYBcHZislsBYtnF1GUTU7pVtmI5MEtBDVcUrmmkCPbV142LjXvq967e4E9PKmiYFNzL1Tae%2BXEGCGrjPyMkS6D7GiojYqHbURl%2FTFEMYcIq9u1UA1gzJGP%2F%2Bwd6Ne40dkhpTlwtpXhtF4PmyX1hH6GTV6f8ByshLLo3986kAq3VpTz77NBleklCVoTI&X-Amz-Signature=e1561bf87daa1161b7fcb2e4cf7cc1bd7e9b90723679d8f50ea55690ec8bc8af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

