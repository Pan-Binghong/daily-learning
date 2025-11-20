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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWP556R%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDl5WmINoDWQUw2JMCRVyGDbTDj9zUfH5cnHrap%2BwfcEgIhANErLBV8i%2FuUqp0rrDZXYUTG%2B2VJMBw7HkU1OmRcfdqiKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj8Rj15u9er9wpokUq3APeMLEGH1YgXyzA6F0kMSGgQDArKzU77s4RrOQi4lnJVMMl%2FJqVrWv9rdCDRtK9QK3HE%2Frq7fV%2F7E3VircdFAqtZdAuGP65IoafBE5sr3rf3j7Hour9ydf3Tb%2FFVgPytNCv57vv449dMCAQ39PgnfGHmliaP2JbUEw5uaJ52FkhOUwePqz9l1Ag2YyidT48mYS3mwkOFWIuJ4blHBKqarEBkO0cBXJSR7327QoUY5MT4wp6oRSpkaTg6R692j51M93FTWLFi7R0Rq8WnoiZmgma9bu%2F%2FomBDXi5mN9N%2FZmm%2FvbsZc5re52g8ScyLquh6aC%2FW1heA5jAW8VqWKQ4oJ9CNE8dWpeQXbkcHe4Jl42sDXY%2BPSBiVqjOYuqmmQk1cxtrxOxNhlm13gd3JOBPiW1SyeAygGT5xLS7TlOO92S0gTQf18B9V7qav7xOr7G9l%2FQqkOctQOQyhC5yL55unDycqYzyKt5LML4j7TI5qnOBAjCy8U18QjT52xUb3BjKNs4oiuBWzAgUPW9zhOnCPKs2Jmgeh9rM6xmzmIGFn0WglEf55js9X3W%2BD%2FrDm79o7osVvqoWBkBT2joFTGfUQaHbjVcQs%2FU8EtlBp%2BSbgbn2%2B%2FILQI4LK4KnRaeCJzC06vnIBjqkAS2r%2FtRp0lxHthEd82UU9gS1kZWOyHJcGt4Lrnjc8v4gsNcsiif7ia4TM4H95RzaRyb1SgbhtArV%2BhxT1SSLJeaYnxj2n7A0jGFfvEdJwrPb7Dv0pqo56K%2BHzPgbic7VrQYXB130Orn%2FNizoOwHjVDjFjjR7qZeN28cHxneTmUlX7ytYKoYdJ0CoAh9kqH6FPbBtHmNPabPLqIwpVBRaooiRUUr%2F&X-Amz-Signature=b7a9704699e1a8a5d855f9fbe62f1e6bd821f1a96777b44b5f02262aa86a746d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWP556R%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDl5WmINoDWQUw2JMCRVyGDbTDj9zUfH5cnHrap%2BwfcEgIhANErLBV8i%2FuUqp0rrDZXYUTG%2B2VJMBw7HkU1OmRcfdqiKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj8Rj15u9er9wpokUq3APeMLEGH1YgXyzA6F0kMSGgQDArKzU77s4RrOQi4lnJVMMl%2FJqVrWv9rdCDRtK9QK3HE%2Frq7fV%2F7E3VircdFAqtZdAuGP65IoafBE5sr3rf3j7Hour9ydf3Tb%2FFVgPytNCv57vv449dMCAQ39PgnfGHmliaP2JbUEw5uaJ52FkhOUwePqz9l1Ag2YyidT48mYS3mwkOFWIuJ4blHBKqarEBkO0cBXJSR7327QoUY5MT4wp6oRSpkaTg6R692j51M93FTWLFi7R0Rq8WnoiZmgma9bu%2F%2FomBDXi5mN9N%2FZmm%2FvbsZc5re52g8ScyLquh6aC%2FW1heA5jAW8VqWKQ4oJ9CNE8dWpeQXbkcHe4Jl42sDXY%2BPSBiVqjOYuqmmQk1cxtrxOxNhlm13gd3JOBPiW1SyeAygGT5xLS7TlOO92S0gTQf18B9V7qav7xOr7G9l%2FQqkOctQOQyhC5yL55unDycqYzyKt5LML4j7TI5qnOBAjCy8U18QjT52xUb3BjKNs4oiuBWzAgUPW9zhOnCPKs2Jmgeh9rM6xmzmIGFn0WglEf55js9X3W%2BD%2FrDm79o7osVvqoWBkBT2joFTGfUQaHbjVcQs%2FU8EtlBp%2BSbgbn2%2B%2FILQI4LK4KnRaeCJzC06vnIBjqkAS2r%2FtRp0lxHthEd82UU9gS1kZWOyHJcGt4Lrnjc8v4gsNcsiif7ia4TM4H95RzaRyb1SgbhtArV%2BhxT1SSLJeaYnxj2n7A0jGFfvEdJwrPb7Dv0pqo56K%2BHzPgbic7VrQYXB130Orn%2FNizoOwHjVDjFjjR7qZeN28cHxneTmUlX7ytYKoYdJ0CoAh9kqH6FPbBtHmNPabPLqIwpVBRaooiRUUr%2F&X-Amz-Signature=a7e803a91cda41267a9db50f040aba97dc6bac8d2e4e544414050628083a4bf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWP556R%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDl5WmINoDWQUw2JMCRVyGDbTDj9zUfH5cnHrap%2BwfcEgIhANErLBV8i%2FuUqp0rrDZXYUTG%2B2VJMBw7HkU1OmRcfdqiKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj8Rj15u9er9wpokUq3APeMLEGH1YgXyzA6F0kMSGgQDArKzU77s4RrOQi4lnJVMMl%2FJqVrWv9rdCDRtK9QK3HE%2Frq7fV%2F7E3VircdFAqtZdAuGP65IoafBE5sr3rf3j7Hour9ydf3Tb%2FFVgPytNCv57vv449dMCAQ39PgnfGHmliaP2JbUEw5uaJ52FkhOUwePqz9l1Ag2YyidT48mYS3mwkOFWIuJ4blHBKqarEBkO0cBXJSR7327QoUY5MT4wp6oRSpkaTg6R692j51M93FTWLFi7R0Rq8WnoiZmgma9bu%2F%2FomBDXi5mN9N%2FZmm%2FvbsZc5re52g8ScyLquh6aC%2FW1heA5jAW8VqWKQ4oJ9CNE8dWpeQXbkcHe4Jl42sDXY%2BPSBiVqjOYuqmmQk1cxtrxOxNhlm13gd3JOBPiW1SyeAygGT5xLS7TlOO92S0gTQf18B9V7qav7xOr7G9l%2FQqkOctQOQyhC5yL55unDycqYzyKt5LML4j7TI5qnOBAjCy8U18QjT52xUb3BjKNs4oiuBWzAgUPW9zhOnCPKs2Jmgeh9rM6xmzmIGFn0WglEf55js9X3W%2BD%2FrDm79o7osVvqoWBkBT2joFTGfUQaHbjVcQs%2FU8EtlBp%2BSbgbn2%2B%2FILQI4LK4KnRaeCJzC06vnIBjqkAS2r%2FtRp0lxHthEd82UU9gS1kZWOyHJcGt4Lrnjc8v4gsNcsiif7ia4TM4H95RzaRyb1SgbhtArV%2BhxT1SSLJeaYnxj2n7A0jGFfvEdJwrPb7Dv0pqo56K%2BHzPgbic7VrQYXB130Orn%2FNizoOwHjVDjFjjR7qZeN28cHxneTmUlX7ytYKoYdJ0CoAh9kqH6FPbBtHmNPabPLqIwpVBRaooiRUUr%2F&X-Amz-Signature=bc1490bd801755d26fbf2f91120c3e833d128be3541bee798d476553a320d250&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWP556R%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDl5WmINoDWQUw2JMCRVyGDbTDj9zUfH5cnHrap%2BwfcEgIhANErLBV8i%2FuUqp0rrDZXYUTG%2B2VJMBw7HkU1OmRcfdqiKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj8Rj15u9er9wpokUq3APeMLEGH1YgXyzA6F0kMSGgQDArKzU77s4RrOQi4lnJVMMl%2FJqVrWv9rdCDRtK9QK3HE%2Frq7fV%2F7E3VircdFAqtZdAuGP65IoafBE5sr3rf3j7Hour9ydf3Tb%2FFVgPytNCv57vv449dMCAQ39PgnfGHmliaP2JbUEw5uaJ52FkhOUwePqz9l1Ag2YyidT48mYS3mwkOFWIuJ4blHBKqarEBkO0cBXJSR7327QoUY5MT4wp6oRSpkaTg6R692j51M93FTWLFi7R0Rq8WnoiZmgma9bu%2F%2FomBDXi5mN9N%2FZmm%2FvbsZc5re52g8ScyLquh6aC%2FW1heA5jAW8VqWKQ4oJ9CNE8dWpeQXbkcHe4Jl42sDXY%2BPSBiVqjOYuqmmQk1cxtrxOxNhlm13gd3JOBPiW1SyeAygGT5xLS7TlOO92S0gTQf18B9V7qav7xOr7G9l%2FQqkOctQOQyhC5yL55unDycqYzyKt5LML4j7TI5qnOBAjCy8U18QjT52xUb3BjKNs4oiuBWzAgUPW9zhOnCPKs2Jmgeh9rM6xmzmIGFn0WglEf55js9X3W%2BD%2FrDm79o7osVvqoWBkBT2joFTGfUQaHbjVcQs%2FU8EtlBp%2BSbgbn2%2B%2FILQI4LK4KnRaeCJzC06vnIBjqkAS2r%2FtRp0lxHthEd82UU9gS1kZWOyHJcGt4Lrnjc8v4gsNcsiif7ia4TM4H95RzaRyb1SgbhtArV%2BhxT1SSLJeaYnxj2n7A0jGFfvEdJwrPb7Dv0pqo56K%2BHzPgbic7VrQYXB130Orn%2FNizoOwHjVDjFjjR7qZeN28cHxneTmUlX7ytYKoYdJ0CoAh9kqH6FPbBtHmNPabPLqIwpVBRaooiRUUr%2F&X-Amz-Signature=0d6fb1310ffb04e2f4f9cc980d3f93e76e4f808b4e509ec008b7d4eaf7e39c86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWP556R%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDl5WmINoDWQUw2JMCRVyGDbTDj9zUfH5cnHrap%2BwfcEgIhANErLBV8i%2FuUqp0rrDZXYUTG%2B2VJMBw7HkU1OmRcfdqiKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj8Rj15u9er9wpokUq3APeMLEGH1YgXyzA6F0kMSGgQDArKzU77s4RrOQi4lnJVMMl%2FJqVrWv9rdCDRtK9QK3HE%2Frq7fV%2F7E3VircdFAqtZdAuGP65IoafBE5sr3rf3j7Hour9ydf3Tb%2FFVgPytNCv57vv449dMCAQ39PgnfGHmliaP2JbUEw5uaJ52FkhOUwePqz9l1Ag2YyidT48mYS3mwkOFWIuJ4blHBKqarEBkO0cBXJSR7327QoUY5MT4wp6oRSpkaTg6R692j51M93FTWLFi7R0Rq8WnoiZmgma9bu%2F%2FomBDXi5mN9N%2FZmm%2FvbsZc5re52g8ScyLquh6aC%2FW1heA5jAW8VqWKQ4oJ9CNE8dWpeQXbkcHe4Jl42sDXY%2BPSBiVqjOYuqmmQk1cxtrxOxNhlm13gd3JOBPiW1SyeAygGT5xLS7TlOO92S0gTQf18B9V7qav7xOr7G9l%2FQqkOctQOQyhC5yL55unDycqYzyKt5LML4j7TI5qnOBAjCy8U18QjT52xUb3BjKNs4oiuBWzAgUPW9zhOnCPKs2Jmgeh9rM6xmzmIGFn0WglEf55js9X3W%2BD%2FrDm79o7osVvqoWBkBT2joFTGfUQaHbjVcQs%2FU8EtlBp%2BSbgbn2%2B%2FILQI4LK4KnRaeCJzC06vnIBjqkAS2r%2FtRp0lxHthEd82UU9gS1kZWOyHJcGt4Lrnjc8v4gsNcsiif7ia4TM4H95RzaRyb1SgbhtArV%2BhxT1SSLJeaYnxj2n7A0jGFfvEdJwrPb7Dv0pqo56K%2BHzPgbic7VrQYXB130Orn%2FNizoOwHjVDjFjjR7qZeN28cHxneTmUlX7ytYKoYdJ0CoAh9kqH6FPbBtHmNPabPLqIwpVBRaooiRUUr%2F&X-Amz-Signature=5252927ccf3790a1f77bac0bd96a097c87035b54ceff8279c04589b1256e04a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWP556R%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDl5WmINoDWQUw2JMCRVyGDbTDj9zUfH5cnHrap%2BwfcEgIhANErLBV8i%2FuUqp0rrDZXYUTG%2B2VJMBw7HkU1OmRcfdqiKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj8Rj15u9er9wpokUq3APeMLEGH1YgXyzA6F0kMSGgQDArKzU77s4RrOQi4lnJVMMl%2FJqVrWv9rdCDRtK9QK3HE%2Frq7fV%2F7E3VircdFAqtZdAuGP65IoafBE5sr3rf3j7Hour9ydf3Tb%2FFVgPytNCv57vv449dMCAQ39PgnfGHmliaP2JbUEw5uaJ52FkhOUwePqz9l1Ag2YyidT48mYS3mwkOFWIuJ4blHBKqarEBkO0cBXJSR7327QoUY5MT4wp6oRSpkaTg6R692j51M93FTWLFi7R0Rq8WnoiZmgma9bu%2F%2FomBDXi5mN9N%2FZmm%2FvbsZc5re52g8ScyLquh6aC%2FW1heA5jAW8VqWKQ4oJ9CNE8dWpeQXbkcHe4Jl42sDXY%2BPSBiVqjOYuqmmQk1cxtrxOxNhlm13gd3JOBPiW1SyeAygGT5xLS7TlOO92S0gTQf18B9V7qav7xOr7G9l%2FQqkOctQOQyhC5yL55unDycqYzyKt5LML4j7TI5qnOBAjCy8U18QjT52xUb3BjKNs4oiuBWzAgUPW9zhOnCPKs2Jmgeh9rM6xmzmIGFn0WglEf55js9X3W%2BD%2FrDm79o7osVvqoWBkBT2joFTGfUQaHbjVcQs%2FU8EtlBp%2BSbgbn2%2B%2FILQI4LK4KnRaeCJzC06vnIBjqkAS2r%2FtRp0lxHthEd82UU9gS1kZWOyHJcGt4Lrnjc8v4gsNcsiif7ia4TM4H95RzaRyb1SgbhtArV%2BhxT1SSLJeaYnxj2n7A0jGFfvEdJwrPb7Dv0pqo56K%2BHzPgbic7VrQYXB130Orn%2FNizoOwHjVDjFjjR7qZeN28cHxneTmUlX7ytYKoYdJ0CoAh9kqH6FPbBtHmNPabPLqIwpVBRaooiRUUr%2F&X-Amz-Signature=1dc969d094f7ac5604d258fb1672147f12a0c4ff5c33c5a4914b7c8135edcf3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWP556R%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDl5WmINoDWQUw2JMCRVyGDbTDj9zUfH5cnHrap%2BwfcEgIhANErLBV8i%2FuUqp0rrDZXYUTG%2B2VJMBw7HkU1OmRcfdqiKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj8Rj15u9er9wpokUq3APeMLEGH1YgXyzA6F0kMSGgQDArKzU77s4RrOQi4lnJVMMl%2FJqVrWv9rdCDRtK9QK3HE%2Frq7fV%2F7E3VircdFAqtZdAuGP65IoafBE5sr3rf3j7Hour9ydf3Tb%2FFVgPytNCv57vv449dMCAQ39PgnfGHmliaP2JbUEw5uaJ52FkhOUwePqz9l1Ag2YyidT48mYS3mwkOFWIuJ4blHBKqarEBkO0cBXJSR7327QoUY5MT4wp6oRSpkaTg6R692j51M93FTWLFi7R0Rq8WnoiZmgma9bu%2F%2FomBDXi5mN9N%2FZmm%2FvbsZc5re52g8ScyLquh6aC%2FW1heA5jAW8VqWKQ4oJ9CNE8dWpeQXbkcHe4Jl42sDXY%2BPSBiVqjOYuqmmQk1cxtrxOxNhlm13gd3JOBPiW1SyeAygGT5xLS7TlOO92S0gTQf18B9V7qav7xOr7G9l%2FQqkOctQOQyhC5yL55unDycqYzyKt5LML4j7TI5qnOBAjCy8U18QjT52xUb3BjKNs4oiuBWzAgUPW9zhOnCPKs2Jmgeh9rM6xmzmIGFn0WglEf55js9X3W%2BD%2FrDm79o7osVvqoWBkBT2joFTGfUQaHbjVcQs%2FU8EtlBp%2BSbgbn2%2B%2FILQI4LK4KnRaeCJzC06vnIBjqkAS2r%2FtRp0lxHthEd82UU9gS1kZWOyHJcGt4Lrnjc8v4gsNcsiif7ia4TM4H95RzaRyb1SgbhtArV%2BhxT1SSLJeaYnxj2n7A0jGFfvEdJwrPb7Dv0pqo56K%2BHzPgbic7VrQYXB130Orn%2FNizoOwHjVDjFjjR7qZeN28cHxneTmUlX7ytYKoYdJ0CoAh9kqH6FPbBtHmNPabPLqIwpVBRaooiRUUr%2F&X-Amz-Signature=862bb9bd9cdd02ca7188bb1bc2eee22bc8c63d3bd2f10a332f067c4feeddf493&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWP556R%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDl5WmINoDWQUw2JMCRVyGDbTDj9zUfH5cnHrap%2BwfcEgIhANErLBV8i%2FuUqp0rrDZXYUTG%2B2VJMBw7HkU1OmRcfdqiKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj8Rj15u9er9wpokUq3APeMLEGH1YgXyzA6F0kMSGgQDArKzU77s4RrOQi4lnJVMMl%2FJqVrWv9rdCDRtK9QK3HE%2Frq7fV%2F7E3VircdFAqtZdAuGP65IoafBE5sr3rf3j7Hour9ydf3Tb%2FFVgPytNCv57vv449dMCAQ39PgnfGHmliaP2JbUEw5uaJ52FkhOUwePqz9l1Ag2YyidT48mYS3mwkOFWIuJ4blHBKqarEBkO0cBXJSR7327QoUY5MT4wp6oRSpkaTg6R692j51M93FTWLFi7R0Rq8WnoiZmgma9bu%2F%2FomBDXi5mN9N%2FZmm%2FvbsZc5re52g8ScyLquh6aC%2FW1heA5jAW8VqWKQ4oJ9CNE8dWpeQXbkcHe4Jl42sDXY%2BPSBiVqjOYuqmmQk1cxtrxOxNhlm13gd3JOBPiW1SyeAygGT5xLS7TlOO92S0gTQf18B9V7qav7xOr7G9l%2FQqkOctQOQyhC5yL55unDycqYzyKt5LML4j7TI5qnOBAjCy8U18QjT52xUb3BjKNs4oiuBWzAgUPW9zhOnCPKs2Jmgeh9rM6xmzmIGFn0WglEf55js9X3W%2BD%2FrDm79o7osVvqoWBkBT2joFTGfUQaHbjVcQs%2FU8EtlBp%2BSbgbn2%2B%2FILQI4LK4KnRaeCJzC06vnIBjqkAS2r%2FtRp0lxHthEd82UU9gS1kZWOyHJcGt4Lrnjc8v4gsNcsiif7ia4TM4H95RzaRyb1SgbhtArV%2BhxT1SSLJeaYnxj2n7A0jGFfvEdJwrPb7Dv0pqo56K%2BHzPgbic7VrQYXB130Orn%2FNizoOwHjVDjFjjR7qZeN28cHxneTmUlX7ytYKoYdJ0CoAh9kqH6FPbBtHmNPabPLqIwpVBRaooiRUUr%2F&X-Amz-Signature=e65a1cc5cfc77ca988b21c34d3624f8eea8377c78749344720b84f156f9d60ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWP556R%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDl5WmINoDWQUw2JMCRVyGDbTDj9zUfH5cnHrap%2BwfcEgIhANErLBV8i%2FuUqp0rrDZXYUTG%2B2VJMBw7HkU1OmRcfdqiKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj8Rj15u9er9wpokUq3APeMLEGH1YgXyzA6F0kMSGgQDArKzU77s4RrOQi4lnJVMMl%2FJqVrWv9rdCDRtK9QK3HE%2Frq7fV%2F7E3VircdFAqtZdAuGP65IoafBE5sr3rf3j7Hour9ydf3Tb%2FFVgPytNCv57vv449dMCAQ39PgnfGHmliaP2JbUEw5uaJ52FkhOUwePqz9l1Ag2YyidT48mYS3mwkOFWIuJ4blHBKqarEBkO0cBXJSR7327QoUY5MT4wp6oRSpkaTg6R692j51M93FTWLFi7R0Rq8WnoiZmgma9bu%2F%2FomBDXi5mN9N%2FZmm%2FvbsZc5re52g8ScyLquh6aC%2FW1heA5jAW8VqWKQ4oJ9CNE8dWpeQXbkcHe4Jl42sDXY%2BPSBiVqjOYuqmmQk1cxtrxOxNhlm13gd3JOBPiW1SyeAygGT5xLS7TlOO92S0gTQf18B9V7qav7xOr7G9l%2FQqkOctQOQyhC5yL55unDycqYzyKt5LML4j7TI5qnOBAjCy8U18QjT52xUb3BjKNs4oiuBWzAgUPW9zhOnCPKs2Jmgeh9rM6xmzmIGFn0WglEf55js9X3W%2BD%2FrDm79o7osVvqoWBkBT2joFTGfUQaHbjVcQs%2FU8EtlBp%2BSbgbn2%2B%2FILQI4LK4KnRaeCJzC06vnIBjqkAS2r%2FtRp0lxHthEd82UU9gS1kZWOyHJcGt4Lrnjc8v4gsNcsiif7ia4TM4H95RzaRyb1SgbhtArV%2BhxT1SSLJeaYnxj2n7A0jGFfvEdJwrPb7Dv0pqo56K%2BHzPgbic7VrQYXB130Orn%2FNizoOwHjVDjFjjR7qZeN28cHxneTmUlX7ytYKoYdJ0CoAh9kqH6FPbBtHmNPabPLqIwpVBRaooiRUUr%2F&X-Amz-Signature=ffe17ea2e3f149678677607fb2cd1062ac0b607020a44d82ebd47530bc07272d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCWP556R%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDl5WmINoDWQUw2JMCRVyGDbTDj9zUfH5cnHrap%2BwfcEgIhANErLBV8i%2FuUqp0rrDZXYUTG%2B2VJMBw7HkU1OmRcfdqiKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyj8Rj15u9er9wpokUq3APeMLEGH1YgXyzA6F0kMSGgQDArKzU77s4RrOQi4lnJVMMl%2FJqVrWv9rdCDRtK9QK3HE%2Frq7fV%2F7E3VircdFAqtZdAuGP65IoafBE5sr3rf3j7Hour9ydf3Tb%2FFVgPytNCv57vv449dMCAQ39PgnfGHmliaP2JbUEw5uaJ52FkhOUwePqz9l1Ag2YyidT48mYS3mwkOFWIuJ4blHBKqarEBkO0cBXJSR7327QoUY5MT4wp6oRSpkaTg6R692j51M93FTWLFi7R0Rq8WnoiZmgma9bu%2F%2FomBDXi5mN9N%2FZmm%2FvbsZc5re52g8ScyLquh6aC%2FW1heA5jAW8VqWKQ4oJ9CNE8dWpeQXbkcHe4Jl42sDXY%2BPSBiVqjOYuqmmQk1cxtrxOxNhlm13gd3JOBPiW1SyeAygGT5xLS7TlOO92S0gTQf18B9V7qav7xOr7G9l%2FQqkOctQOQyhC5yL55unDycqYzyKt5LML4j7TI5qnOBAjCy8U18QjT52xUb3BjKNs4oiuBWzAgUPW9zhOnCPKs2Jmgeh9rM6xmzmIGFn0WglEf55js9X3W%2BD%2FrDm79o7osVvqoWBkBT2joFTGfUQaHbjVcQs%2FU8EtlBp%2BSbgbn2%2B%2FILQI4LK4KnRaeCJzC06vnIBjqkAS2r%2FtRp0lxHthEd82UU9gS1kZWOyHJcGt4Lrnjc8v4gsNcsiif7ia4TM4H95RzaRyb1SgbhtArV%2BhxT1SSLJeaYnxj2n7A0jGFfvEdJwrPb7Dv0pqo56K%2BHzPgbic7VrQYXB130Orn%2FNizoOwHjVDjFjjR7qZeN28cHxneTmUlX7ytYKoYdJ0CoAh9kqH6FPbBtHmNPabPLqIwpVBRaooiRUUr%2F&X-Amz-Signature=bcf8c4fdc92aa4d300109fd9a46297bfd2c9036b6a9d87c8779f6286c9d58dc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

