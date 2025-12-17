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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NN3SEMX%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1eSmmP8UdkbSrEoCwuJPL132jboy1h6vpLhc4B7PbXAiBnMo5FmqdyZgpTtOhAFB8tPFSXpifbcz3qHuPML8TJDSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMYwVxBPK9mU755vQwKtwD%2B4eY5dtdZNrZuElsEikf30depsZahMhc8G5GF1pVCg3LIr1LRwJpjXmTO6ZRNrIu7HxoXkSvG6LfaTRWYec9jie4IMQR02jJYq02%2FBSNQBTfcV8oAlH3XGMdHRKQfUP6X6OTjy4w%2Bzk3gpqtt5tKEARX%2BPuovjfqkNLs7NGCzE8bZB9KkzrP5leSMv2ZA7r0K8CA9pD9a3amj5bX1VfPpDz%2FnBuBedNeO8hT8UGUc6vNCplI%2Bveyc0i5EEeXRqe%2Fu2sl%2BuDH%2FXZdNXdROWWmGdoUA9QKvaOTdPrNOJszGflRiYkX%2FBuXgqRYvYedSOs5RcD9WMhqUwxH6QCYnZDY4hJZLQsokHWBwi87rW8BFpNZ6Kpm7nSVPwG%2BvCqgikaVhQAyAM%2F47gk%2BNQ%2FXYxzv76b%2FlEKJldiVjogPVTsfsnkXhQcJa9RBOtW0ErID1Gsf0vC3T%2B4tqSi8Ik6nrOXlI5rN%2B3sA1dKsStfUM2s86G7lr4asCYREI%2BaMxgu0VkpCXncckJIvQ3z3KWB%2FW2JbPmfuraGKtgQwl2NjOnUioq5cNEMc3nOHnrf75varVUuJwU9SA3SnhyCuP9%2Fb3mqPOwqYl%2Fz5nnEdEV20PGSsdXIjF9qnqhgHPBsr3y4wyLGIygY6pgG38Se22yK6ezMFU30EUDUkq4iaZspmSjoLVNAO7vcQxT6Gl9weZ9q55MZf64DDXHovl7KavzfA6nDZIGL6DzzkFjPWLkzkFD%2FG5Ec6hT7M7w%2Fl19BCLjl4epYv7gRiop5sqwRMwW6mpXMARyVwcZawGXUAcUn3s4S0yxlUG5AnMghWtHmGyyBzWSpizSkAXejtE2pd34vb3vls01OnKPbsMtsvEQSD&X-Amz-Signature=156c351330eeb131cbd61f8559924d53e468670288594aed7e29b8b2338233ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NN3SEMX%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1eSmmP8UdkbSrEoCwuJPL132jboy1h6vpLhc4B7PbXAiBnMo5FmqdyZgpTtOhAFB8tPFSXpifbcz3qHuPML8TJDSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMYwVxBPK9mU755vQwKtwD%2B4eY5dtdZNrZuElsEikf30depsZahMhc8G5GF1pVCg3LIr1LRwJpjXmTO6ZRNrIu7HxoXkSvG6LfaTRWYec9jie4IMQR02jJYq02%2FBSNQBTfcV8oAlH3XGMdHRKQfUP6X6OTjy4w%2Bzk3gpqtt5tKEARX%2BPuovjfqkNLs7NGCzE8bZB9KkzrP5leSMv2ZA7r0K8CA9pD9a3amj5bX1VfPpDz%2FnBuBedNeO8hT8UGUc6vNCplI%2Bveyc0i5EEeXRqe%2Fu2sl%2BuDH%2FXZdNXdROWWmGdoUA9QKvaOTdPrNOJszGflRiYkX%2FBuXgqRYvYedSOs5RcD9WMhqUwxH6QCYnZDY4hJZLQsokHWBwi87rW8BFpNZ6Kpm7nSVPwG%2BvCqgikaVhQAyAM%2F47gk%2BNQ%2FXYxzv76b%2FlEKJldiVjogPVTsfsnkXhQcJa9RBOtW0ErID1Gsf0vC3T%2B4tqSi8Ik6nrOXlI5rN%2B3sA1dKsStfUM2s86G7lr4asCYREI%2BaMxgu0VkpCXncckJIvQ3z3KWB%2FW2JbPmfuraGKtgQwl2NjOnUioq5cNEMc3nOHnrf75varVUuJwU9SA3SnhyCuP9%2Fb3mqPOwqYl%2Fz5nnEdEV20PGSsdXIjF9qnqhgHPBsr3y4wyLGIygY6pgG38Se22yK6ezMFU30EUDUkq4iaZspmSjoLVNAO7vcQxT6Gl9weZ9q55MZf64DDXHovl7KavzfA6nDZIGL6DzzkFjPWLkzkFD%2FG5Ec6hT7M7w%2Fl19BCLjl4epYv7gRiop5sqwRMwW6mpXMARyVwcZawGXUAcUn3s4S0yxlUG5AnMghWtHmGyyBzWSpizSkAXejtE2pd34vb3vls01OnKPbsMtsvEQSD&X-Amz-Signature=0afd53eb829e0a9ddbfa55c5a77e4081e42f3393d32e4aade0277c8f0e8d9b84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NN3SEMX%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1eSmmP8UdkbSrEoCwuJPL132jboy1h6vpLhc4B7PbXAiBnMo5FmqdyZgpTtOhAFB8tPFSXpifbcz3qHuPML8TJDSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMYwVxBPK9mU755vQwKtwD%2B4eY5dtdZNrZuElsEikf30depsZahMhc8G5GF1pVCg3LIr1LRwJpjXmTO6ZRNrIu7HxoXkSvG6LfaTRWYec9jie4IMQR02jJYq02%2FBSNQBTfcV8oAlH3XGMdHRKQfUP6X6OTjy4w%2Bzk3gpqtt5tKEARX%2BPuovjfqkNLs7NGCzE8bZB9KkzrP5leSMv2ZA7r0K8CA9pD9a3amj5bX1VfPpDz%2FnBuBedNeO8hT8UGUc6vNCplI%2Bveyc0i5EEeXRqe%2Fu2sl%2BuDH%2FXZdNXdROWWmGdoUA9QKvaOTdPrNOJszGflRiYkX%2FBuXgqRYvYedSOs5RcD9WMhqUwxH6QCYnZDY4hJZLQsokHWBwi87rW8BFpNZ6Kpm7nSVPwG%2BvCqgikaVhQAyAM%2F47gk%2BNQ%2FXYxzv76b%2FlEKJldiVjogPVTsfsnkXhQcJa9RBOtW0ErID1Gsf0vC3T%2B4tqSi8Ik6nrOXlI5rN%2B3sA1dKsStfUM2s86G7lr4asCYREI%2BaMxgu0VkpCXncckJIvQ3z3KWB%2FW2JbPmfuraGKtgQwl2NjOnUioq5cNEMc3nOHnrf75varVUuJwU9SA3SnhyCuP9%2Fb3mqPOwqYl%2Fz5nnEdEV20PGSsdXIjF9qnqhgHPBsr3y4wyLGIygY6pgG38Se22yK6ezMFU30EUDUkq4iaZspmSjoLVNAO7vcQxT6Gl9weZ9q55MZf64DDXHovl7KavzfA6nDZIGL6DzzkFjPWLkzkFD%2FG5Ec6hT7M7w%2Fl19BCLjl4epYv7gRiop5sqwRMwW6mpXMARyVwcZawGXUAcUn3s4S0yxlUG5AnMghWtHmGyyBzWSpizSkAXejtE2pd34vb3vls01OnKPbsMtsvEQSD&X-Amz-Signature=a43acdf68a97bcbdd873ef3d91a51e4b2f32744fd566c2100f2039f308a5ec8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NN3SEMX%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1eSmmP8UdkbSrEoCwuJPL132jboy1h6vpLhc4B7PbXAiBnMo5FmqdyZgpTtOhAFB8tPFSXpifbcz3qHuPML8TJDSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMYwVxBPK9mU755vQwKtwD%2B4eY5dtdZNrZuElsEikf30depsZahMhc8G5GF1pVCg3LIr1LRwJpjXmTO6ZRNrIu7HxoXkSvG6LfaTRWYec9jie4IMQR02jJYq02%2FBSNQBTfcV8oAlH3XGMdHRKQfUP6X6OTjy4w%2Bzk3gpqtt5tKEARX%2BPuovjfqkNLs7NGCzE8bZB9KkzrP5leSMv2ZA7r0K8CA9pD9a3amj5bX1VfPpDz%2FnBuBedNeO8hT8UGUc6vNCplI%2Bveyc0i5EEeXRqe%2Fu2sl%2BuDH%2FXZdNXdROWWmGdoUA9QKvaOTdPrNOJszGflRiYkX%2FBuXgqRYvYedSOs5RcD9WMhqUwxH6QCYnZDY4hJZLQsokHWBwi87rW8BFpNZ6Kpm7nSVPwG%2BvCqgikaVhQAyAM%2F47gk%2BNQ%2FXYxzv76b%2FlEKJldiVjogPVTsfsnkXhQcJa9RBOtW0ErID1Gsf0vC3T%2B4tqSi8Ik6nrOXlI5rN%2B3sA1dKsStfUM2s86G7lr4asCYREI%2BaMxgu0VkpCXncckJIvQ3z3KWB%2FW2JbPmfuraGKtgQwl2NjOnUioq5cNEMc3nOHnrf75varVUuJwU9SA3SnhyCuP9%2Fb3mqPOwqYl%2Fz5nnEdEV20PGSsdXIjF9qnqhgHPBsr3y4wyLGIygY6pgG38Se22yK6ezMFU30EUDUkq4iaZspmSjoLVNAO7vcQxT6Gl9weZ9q55MZf64DDXHovl7KavzfA6nDZIGL6DzzkFjPWLkzkFD%2FG5Ec6hT7M7w%2Fl19BCLjl4epYv7gRiop5sqwRMwW6mpXMARyVwcZawGXUAcUn3s4S0yxlUG5AnMghWtHmGyyBzWSpizSkAXejtE2pd34vb3vls01OnKPbsMtsvEQSD&X-Amz-Signature=2ab307d94bbf52a081b167896256cc74dc93758355e9a1c487e805de546c7a64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NN3SEMX%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1eSmmP8UdkbSrEoCwuJPL132jboy1h6vpLhc4B7PbXAiBnMo5FmqdyZgpTtOhAFB8tPFSXpifbcz3qHuPML8TJDSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMYwVxBPK9mU755vQwKtwD%2B4eY5dtdZNrZuElsEikf30depsZahMhc8G5GF1pVCg3LIr1LRwJpjXmTO6ZRNrIu7HxoXkSvG6LfaTRWYec9jie4IMQR02jJYq02%2FBSNQBTfcV8oAlH3XGMdHRKQfUP6X6OTjy4w%2Bzk3gpqtt5tKEARX%2BPuovjfqkNLs7NGCzE8bZB9KkzrP5leSMv2ZA7r0K8CA9pD9a3amj5bX1VfPpDz%2FnBuBedNeO8hT8UGUc6vNCplI%2Bveyc0i5EEeXRqe%2Fu2sl%2BuDH%2FXZdNXdROWWmGdoUA9QKvaOTdPrNOJszGflRiYkX%2FBuXgqRYvYedSOs5RcD9WMhqUwxH6QCYnZDY4hJZLQsokHWBwi87rW8BFpNZ6Kpm7nSVPwG%2BvCqgikaVhQAyAM%2F47gk%2BNQ%2FXYxzv76b%2FlEKJldiVjogPVTsfsnkXhQcJa9RBOtW0ErID1Gsf0vC3T%2B4tqSi8Ik6nrOXlI5rN%2B3sA1dKsStfUM2s86G7lr4asCYREI%2BaMxgu0VkpCXncckJIvQ3z3KWB%2FW2JbPmfuraGKtgQwl2NjOnUioq5cNEMc3nOHnrf75varVUuJwU9SA3SnhyCuP9%2Fb3mqPOwqYl%2Fz5nnEdEV20PGSsdXIjF9qnqhgHPBsr3y4wyLGIygY6pgG38Se22yK6ezMFU30EUDUkq4iaZspmSjoLVNAO7vcQxT6Gl9weZ9q55MZf64DDXHovl7KavzfA6nDZIGL6DzzkFjPWLkzkFD%2FG5Ec6hT7M7w%2Fl19BCLjl4epYv7gRiop5sqwRMwW6mpXMARyVwcZawGXUAcUn3s4S0yxlUG5AnMghWtHmGyyBzWSpizSkAXejtE2pd34vb3vls01OnKPbsMtsvEQSD&X-Amz-Signature=f5f52133762d4488211fa58f0e01fbdca704556700b01aeb0717e435ca6f873d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NN3SEMX%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1eSmmP8UdkbSrEoCwuJPL132jboy1h6vpLhc4B7PbXAiBnMo5FmqdyZgpTtOhAFB8tPFSXpifbcz3qHuPML8TJDSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMYwVxBPK9mU755vQwKtwD%2B4eY5dtdZNrZuElsEikf30depsZahMhc8G5GF1pVCg3LIr1LRwJpjXmTO6ZRNrIu7HxoXkSvG6LfaTRWYec9jie4IMQR02jJYq02%2FBSNQBTfcV8oAlH3XGMdHRKQfUP6X6OTjy4w%2Bzk3gpqtt5tKEARX%2BPuovjfqkNLs7NGCzE8bZB9KkzrP5leSMv2ZA7r0K8CA9pD9a3amj5bX1VfPpDz%2FnBuBedNeO8hT8UGUc6vNCplI%2Bveyc0i5EEeXRqe%2Fu2sl%2BuDH%2FXZdNXdROWWmGdoUA9QKvaOTdPrNOJszGflRiYkX%2FBuXgqRYvYedSOs5RcD9WMhqUwxH6QCYnZDY4hJZLQsokHWBwi87rW8BFpNZ6Kpm7nSVPwG%2BvCqgikaVhQAyAM%2F47gk%2BNQ%2FXYxzv76b%2FlEKJldiVjogPVTsfsnkXhQcJa9RBOtW0ErID1Gsf0vC3T%2B4tqSi8Ik6nrOXlI5rN%2B3sA1dKsStfUM2s86G7lr4asCYREI%2BaMxgu0VkpCXncckJIvQ3z3KWB%2FW2JbPmfuraGKtgQwl2NjOnUioq5cNEMc3nOHnrf75varVUuJwU9SA3SnhyCuP9%2Fb3mqPOwqYl%2Fz5nnEdEV20PGSsdXIjF9qnqhgHPBsr3y4wyLGIygY6pgG38Se22yK6ezMFU30EUDUkq4iaZspmSjoLVNAO7vcQxT6Gl9weZ9q55MZf64DDXHovl7KavzfA6nDZIGL6DzzkFjPWLkzkFD%2FG5Ec6hT7M7w%2Fl19BCLjl4epYv7gRiop5sqwRMwW6mpXMARyVwcZawGXUAcUn3s4S0yxlUG5AnMghWtHmGyyBzWSpizSkAXejtE2pd34vb3vls01OnKPbsMtsvEQSD&X-Amz-Signature=c32c55825cfdba5efd842df02e9e64bd74f3c3a58d86c0769be817c847616fcb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NN3SEMX%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1eSmmP8UdkbSrEoCwuJPL132jboy1h6vpLhc4B7PbXAiBnMo5FmqdyZgpTtOhAFB8tPFSXpifbcz3qHuPML8TJDSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMYwVxBPK9mU755vQwKtwD%2B4eY5dtdZNrZuElsEikf30depsZahMhc8G5GF1pVCg3LIr1LRwJpjXmTO6ZRNrIu7HxoXkSvG6LfaTRWYec9jie4IMQR02jJYq02%2FBSNQBTfcV8oAlH3XGMdHRKQfUP6X6OTjy4w%2Bzk3gpqtt5tKEARX%2BPuovjfqkNLs7NGCzE8bZB9KkzrP5leSMv2ZA7r0K8CA9pD9a3amj5bX1VfPpDz%2FnBuBedNeO8hT8UGUc6vNCplI%2Bveyc0i5EEeXRqe%2Fu2sl%2BuDH%2FXZdNXdROWWmGdoUA9QKvaOTdPrNOJszGflRiYkX%2FBuXgqRYvYedSOs5RcD9WMhqUwxH6QCYnZDY4hJZLQsokHWBwi87rW8BFpNZ6Kpm7nSVPwG%2BvCqgikaVhQAyAM%2F47gk%2BNQ%2FXYxzv76b%2FlEKJldiVjogPVTsfsnkXhQcJa9RBOtW0ErID1Gsf0vC3T%2B4tqSi8Ik6nrOXlI5rN%2B3sA1dKsStfUM2s86G7lr4asCYREI%2BaMxgu0VkpCXncckJIvQ3z3KWB%2FW2JbPmfuraGKtgQwl2NjOnUioq5cNEMc3nOHnrf75varVUuJwU9SA3SnhyCuP9%2Fb3mqPOwqYl%2Fz5nnEdEV20PGSsdXIjF9qnqhgHPBsr3y4wyLGIygY6pgG38Se22yK6ezMFU30EUDUkq4iaZspmSjoLVNAO7vcQxT6Gl9weZ9q55MZf64DDXHovl7KavzfA6nDZIGL6DzzkFjPWLkzkFD%2FG5Ec6hT7M7w%2Fl19BCLjl4epYv7gRiop5sqwRMwW6mpXMARyVwcZawGXUAcUn3s4S0yxlUG5AnMghWtHmGyyBzWSpizSkAXejtE2pd34vb3vls01OnKPbsMtsvEQSD&X-Amz-Signature=2a14c313a366a19e67e385c97c626fd7e39001dc8add20742404a3a11c870408&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NN3SEMX%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1eSmmP8UdkbSrEoCwuJPL132jboy1h6vpLhc4B7PbXAiBnMo5FmqdyZgpTtOhAFB8tPFSXpifbcz3qHuPML8TJDSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMYwVxBPK9mU755vQwKtwD%2B4eY5dtdZNrZuElsEikf30depsZahMhc8G5GF1pVCg3LIr1LRwJpjXmTO6ZRNrIu7HxoXkSvG6LfaTRWYec9jie4IMQR02jJYq02%2FBSNQBTfcV8oAlH3XGMdHRKQfUP6X6OTjy4w%2Bzk3gpqtt5tKEARX%2BPuovjfqkNLs7NGCzE8bZB9KkzrP5leSMv2ZA7r0K8CA9pD9a3amj5bX1VfPpDz%2FnBuBedNeO8hT8UGUc6vNCplI%2Bveyc0i5EEeXRqe%2Fu2sl%2BuDH%2FXZdNXdROWWmGdoUA9QKvaOTdPrNOJszGflRiYkX%2FBuXgqRYvYedSOs5RcD9WMhqUwxH6QCYnZDY4hJZLQsokHWBwi87rW8BFpNZ6Kpm7nSVPwG%2BvCqgikaVhQAyAM%2F47gk%2BNQ%2FXYxzv76b%2FlEKJldiVjogPVTsfsnkXhQcJa9RBOtW0ErID1Gsf0vC3T%2B4tqSi8Ik6nrOXlI5rN%2B3sA1dKsStfUM2s86G7lr4asCYREI%2BaMxgu0VkpCXncckJIvQ3z3KWB%2FW2JbPmfuraGKtgQwl2NjOnUioq5cNEMc3nOHnrf75varVUuJwU9SA3SnhyCuP9%2Fb3mqPOwqYl%2Fz5nnEdEV20PGSsdXIjF9qnqhgHPBsr3y4wyLGIygY6pgG38Se22yK6ezMFU30EUDUkq4iaZspmSjoLVNAO7vcQxT6Gl9weZ9q55MZf64DDXHovl7KavzfA6nDZIGL6DzzkFjPWLkzkFD%2FG5Ec6hT7M7w%2Fl19BCLjl4epYv7gRiop5sqwRMwW6mpXMARyVwcZawGXUAcUn3s4S0yxlUG5AnMghWtHmGyyBzWSpizSkAXejtE2pd34vb3vls01OnKPbsMtsvEQSD&X-Amz-Signature=efcf2e91e83207b77441aea62e61188aa9fbd3f6faa93b8ae269e41b2bbf0258&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NN3SEMX%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1eSmmP8UdkbSrEoCwuJPL132jboy1h6vpLhc4B7PbXAiBnMo5FmqdyZgpTtOhAFB8tPFSXpifbcz3qHuPML8TJDSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMYwVxBPK9mU755vQwKtwD%2B4eY5dtdZNrZuElsEikf30depsZahMhc8G5GF1pVCg3LIr1LRwJpjXmTO6ZRNrIu7HxoXkSvG6LfaTRWYec9jie4IMQR02jJYq02%2FBSNQBTfcV8oAlH3XGMdHRKQfUP6X6OTjy4w%2Bzk3gpqtt5tKEARX%2BPuovjfqkNLs7NGCzE8bZB9KkzrP5leSMv2ZA7r0K8CA9pD9a3amj5bX1VfPpDz%2FnBuBedNeO8hT8UGUc6vNCplI%2Bveyc0i5EEeXRqe%2Fu2sl%2BuDH%2FXZdNXdROWWmGdoUA9QKvaOTdPrNOJszGflRiYkX%2FBuXgqRYvYedSOs5RcD9WMhqUwxH6QCYnZDY4hJZLQsokHWBwi87rW8BFpNZ6Kpm7nSVPwG%2BvCqgikaVhQAyAM%2F47gk%2BNQ%2FXYxzv76b%2FlEKJldiVjogPVTsfsnkXhQcJa9RBOtW0ErID1Gsf0vC3T%2B4tqSi8Ik6nrOXlI5rN%2B3sA1dKsStfUM2s86G7lr4asCYREI%2BaMxgu0VkpCXncckJIvQ3z3KWB%2FW2JbPmfuraGKtgQwl2NjOnUioq5cNEMc3nOHnrf75varVUuJwU9SA3SnhyCuP9%2Fb3mqPOwqYl%2Fz5nnEdEV20PGSsdXIjF9qnqhgHPBsr3y4wyLGIygY6pgG38Se22yK6ezMFU30EUDUkq4iaZspmSjoLVNAO7vcQxT6Gl9weZ9q55MZf64DDXHovl7KavzfA6nDZIGL6DzzkFjPWLkzkFD%2FG5Ec6hT7M7w%2Fl19BCLjl4epYv7gRiop5sqwRMwW6mpXMARyVwcZawGXUAcUn3s4S0yxlUG5AnMghWtHmGyyBzWSpizSkAXejtE2pd34vb3vls01OnKPbsMtsvEQSD&X-Amz-Signature=026e496755be85db932746f0ea6d4490f579eac0169f4f6eac4201eae7394a36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NN3SEMX%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1eSmmP8UdkbSrEoCwuJPL132jboy1h6vpLhc4B7PbXAiBnMo5FmqdyZgpTtOhAFB8tPFSXpifbcz3qHuPML8TJDSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMYwVxBPK9mU755vQwKtwD%2B4eY5dtdZNrZuElsEikf30depsZahMhc8G5GF1pVCg3LIr1LRwJpjXmTO6ZRNrIu7HxoXkSvG6LfaTRWYec9jie4IMQR02jJYq02%2FBSNQBTfcV8oAlH3XGMdHRKQfUP6X6OTjy4w%2Bzk3gpqtt5tKEARX%2BPuovjfqkNLs7NGCzE8bZB9KkzrP5leSMv2ZA7r0K8CA9pD9a3amj5bX1VfPpDz%2FnBuBedNeO8hT8UGUc6vNCplI%2Bveyc0i5EEeXRqe%2Fu2sl%2BuDH%2FXZdNXdROWWmGdoUA9QKvaOTdPrNOJszGflRiYkX%2FBuXgqRYvYedSOs5RcD9WMhqUwxH6QCYnZDY4hJZLQsokHWBwi87rW8BFpNZ6Kpm7nSVPwG%2BvCqgikaVhQAyAM%2F47gk%2BNQ%2FXYxzv76b%2FlEKJldiVjogPVTsfsnkXhQcJa9RBOtW0ErID1Gsf0vC3T%2B4tqSi8Ik6nrOXlI5rN%2B3sA1dKsStfUM2s86G7lr4asCYREI%2BaMxgu0VkpCXncckJIvQ3z3KWB%2FW2JbPmfuraGKtgQwl2NjOnUioq5cNEMc3nOHnrf75varVUuJwU9SA3SnhyCuP9%2Fb3mqPOwqYl%2Fz5nnEdEV20PGSsdXIjF9qnqhgHPBsr3y4wyLGIygY6pgG38Se22yK6ezMFU30EUDUkq4iaZspmSjoLVNAO7vcQxT6Gl9weZ9q55MZf64DDXHovl7KavzfA6nDZIGL6DzzkFjPWLkzkFD%2FG5Ec6hT7M7w%2Fl19BCLjl4epYv7gRiop5sqwRMwW6mpXMARyVwcZawGXUAcUn3s4S0yxlUG5AnMghWtHmGyyBzWSpizSkAXejtE2pd34vb3vls01OnKPbsMtsvEQSD&X-Amz-Signature=ce10c56fff6e7d0e695d204cabecae6bf2a1ef0b6eaf77d7c1c5556aa53ec672&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

