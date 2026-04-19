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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627AXY6RJ%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG1jNctsnHU89EmwKtDAhdAdSTxSl2kpxcI3%2BweIglJMAiAM6fUOCMf%2Fg%2BVZR9yacM7UIEw0hKM3UXE0UDqMva%2BqHSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF1LkZKhGoONzngqKtwDiNNXOk2U3FL2F5ivOeA1B%2FP45NKizXQYCU%2Bs2mbzqFNwZ6%2Fr9Cju88miMzUqV%2FhgrTby7pQIEsYZNuTU23PzSCGV06i08BGHxaGK6OnM8el4k5JYS%2FCbBu1mPLUNOPofO3fDed8UgQHcnH%2BlXVtCoZl3CR1A95j489Ur%2F1KHlvW2uMuD%2FA%2BBb2OY4UJHRaDZGDYIJXwrbg8wd2HM1XDm2SdBO3RgNvnkZ1wKCQ50zOvBF2%2BBnMc3YnEzcWRbTH1O23rt65YS6zkQ0OEO8ShR7rK8iVw4WANAbp4ZmlAW%2Bu3jrqTXvvBljr8ND029XddU3G65U%2FMdbmNMV4SGsAWhYLjM4FHQiAJtCWLMqvYBc1uqSBwGmfjvMNsHQfaaWDtElJA6tRjuhijlycBiI2qBAb0jRFUzDGTPeplYLxbxrG7UghO1FRwOuF5diub4hfBYN3RPQ%2FsRlZhv%2FqnB0PfGo8Em6SXcnmSQqr4SCKdJtsjRD6zNnLR2tAvgJk8Emn1a1loBUA05CAPLPN8A2weUD0sHtcb8IYDkr2MTKPcDrkDxMP1Pjv3%2BGYcZfD7izKD0LRJ1NaB%2F%2BTS2oQxDcjWONiG5Vc%2FJBpmlGV8dz2%2FOjZ6tBvkU4m1oJF2YPcswiN6QzwY6pgEeeNOYla%2BQsTGIdlDu7Bots0bvr12AWEQM8G2Dc6g93n0hmKBx6Rn%2FanFaFsLgelNVTZAfFO4rHUsRUusR%2FrtWIyQuAqe3B0IIXl9Od4MJVRxiEmxLlbG8eTOmeoA%2BFIim04bpzuSoXZRjVYSkwsATuUK2iDh47Y%2FItJTyZAtEMWcbEB2DTYuDKxHvz7nZNc%2BteUKV6oaMbNiY%2BPkBrjG2AHCtOpcs&X-Amz-Signature=d173aa040487bc9d5c29ec66558e5d4983e73e0c1abb8ed783f1efefc73f5770&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627AXY6RJ%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG1jNctsnHU89EmwKtDAhdAdSTxSl2kpxcI3%2BweIglJMAiAM6fUOCMf%2Fg%2BVZR9yacM7UIEw0hKM3UXE0UDqMva%2BqHSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF1LkZKhGoONzngqKtwDiNNXOk2U3FL2F5ivOeA1B%2FP45NKizXQYCU%2Bs2mbzqFNwZ6%2Fr9Cju88miMzUqV%2FhgrTby7pQIEsYZNuTU23PzSCGV06i08BGHxaGK6OnM8el4k5JYS%2FCbBu1mPLUNOPofO3fDed8UgQHcnH%2BlXVtCoZl3CR1A95j489Ur%2F1KHlvW2uMuD%2FA%2BBb2OY4UJHRaDZGDYIJXwrbg8wd2HM1XDm2SdBO3RgNvnkZ1wKCQ50zOvBF2%2BBnMc3YnEzcWRbTH1O23rt65YS6zkQ0OEO8ShR7rK8iVw4WANAbp4ZmlAW%2Bu3jrqTXvvBljr8ND029XddU3G65U%2FMdbmNMV4SGsAWhYLjM4FHQiAJtCWLMqvYBc1uqSBwGmfjvMNsHQfaaWDtElJA6tRjuhijlycBiI2qBAb0jRFUzDGTPeplYLxbxrG7UghO1FRwOuF5diub4hfBYN3RPQ%2FsRlZhv%2FqnB0PfGo8Em6SXcnmSQqr4SCKdJtsjRD6zNnLR2tAvgJk8Emn1a1loBUA05CAPLPN8A2weUD0sHtcb8IYDkr2MTKPcDrkDxMP1Pjv3%2BGYcZfD7izKD0LRJ1NaB%2F%2BTS2oQxDcjWONiG5Vc%2FJBpmlGV8dz2%2FOjZ6tBvkU4m1oJF2YPcswiN6QzwY6pgEeeNOYla%2BQsTGIdlDu7Bots0bvr12AWEQM8G2Dc6g93n0hmKBx6Rn%2FanFaFsLgelNVTZAfFO4rHUsRUusR%2FrtWIyQuAqe3B0IIXl9Od4MJVRxiEmxLlbG8eTOmeoA%2BFIim04bpzuSoXZRjVYSkwsATuUK2iDh47Y%2FItJTyZAtEMWcbEB2DTYuDKxHvz7nZNc%2BteUKV6oaMbNiY%2BPkBrjG2AHCtOpcs&X-Amz-Signature=5154e93144605a1077c3a1ac65ca488f6ce08f83c0d394f70a2ccba9cd798612&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627AXY6RJ%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG1jNctsnHU89EmwKtDAhdAdSTxSl2kpxcI3%2BweIglJMAiAM6fUOCMf%2Fg%2BVZR9yacM7UIEw0hKM3UXE0UDqMva%2BqHSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF1LkZKhGoONzngqKtwDiNNXOk2U3FL2F5ivOeA1B%2FP45NKizXQYCU%2Bs2mbzqFNwZ6%2Fr9Cju88miMzUqV%2FhgrTby7pQIEsYZNuTU23PzSCGV06i08BGHxaGK6OnM8el4k5JYS%2FCbBu1mPLUNOPofO3fDed8UgQHcnH%2BlXVtCoZl3CR1A95j489Ur%2F1KHlvW2uMuD%2FA%2BBb2OY4UJHRaDZGDYIJXwrbg8wd2HM1XDm2SdBO3RgNvnkZ1wKCQ50zOvBF2%2BBnMc3YnEzcWRbTH1O23rt65YS6zkQ0OEO8ShR7rK8iVw4WANAbp4ZmlAW%2Bu3jrqTXvvBljr8ND029XddU3G65U%2FMdbmNMV4SGsAWhYLjM4FHQiAJtCWLMqvYBc1uqSBwGmfjvMNsHQfaaWDtElJA6tRjuhijlycBiI2qBAb0jRFUzDGTPeplYLxbxrG7UghO1FRwOuF5diub4hfBYN3RPQ%2FsRlZhv%2FqnB0PfGo8Em6SXcnmSQqr4SCKdJtsjRD6zNnLR2tAvgJk8Emn1a1loBUA05CAPLPN8A2weUD0sHtcb8IYDkr2MTKPcDrkDxMP1Pjv3%2BGYcZfD7izKD0LRJ1NaB%2F%2BTS2oQxDcjWONiG5Vc%2FJBpmlGV8dz2%2FOjZ6tBvkU4m1oJF2YPcswiN6QzwY6pgEeeNOYla%2BQsTGIdlDu7Bots0bvr12AWEQM8G2Dc6g93n0hmKBx6Rn%2FanFaFsLgelNVTZAfFO4rHUsRUusR%2FrtWIyQuAqe3B0IIXl9Od4MJVRxiEmxLlbG8eTOmeoA%2BFIim04bpzuSoXZRjVYSkwsATuUK2iDh47Y%2FItJTyZAtEMWcbEB2DTYuDKxHvz7nZNc%2BteUKV6oaMbNiY%2BPkBrjG2AHCtOpcs&X-Amz-Signature=948348f32a2960f9f503683e4a5837088eb8ad0705ca027636060af1a01d8427&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627AXY6RJ%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG1jNctsnHU89EmwKtDAhdAdSTxSl2kpxcI3%2BweIglJMAiAM6fUOCMf%2Fg%2BVZR9yacM7UIEw0hKM3UXE0UDqMva%2BqHSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF1LkZKhGoONzngqKtwDiNNXOk2U3FL2F5ivOeA1B%2FP45NKizXQYCU%2Bs2mbzqFNwZ6%2Fr9Cju88miMzUqV%2FhgrTby7pQIEsYZNuTU23PzSCGV06i08BGHxaGK6OnM8el4k5JYS%2FCbBu1mPLUNOPofO3fDed8UgQHcnH%2BlXVtCoZl3CR1A95j489Ur%2F1KHlvW2uMuD%2FA%2BBb2OY4UJHRaDZGDYIJXwrbg8wd2HM1XDm2SdBO3RgNvnkZ1wKCQ50zOvBF2%2BBnMc3YnEzcWRbTH1O23rt65YS6zkQ0OEO8ShR7rK8iVw4WANAbp4ZmlAW%2Bu3jrqTXvvBljr8ND029XddU3G65U%2FMdbmNMV4SGsAWhYLjM4FHQiAJtCWLMqvYBc1uqSBwGmfjvMNsHQfaaWDtElJA6tRjuhijlycBiI2qBAb0jRFUzDGTPeplYLxbxrG7UghO1FRwOuF5diub4hfBYN3RPQ%2FsRlZhv%2FqnB0PfGo8Em6SXcnmSQqr4SCKdJtsjRD6zNnLR2tAvgJk8Emn1a1loBUA05CAPLPN8A2weUD0sHtcb8IYDkr2MTKPcDrkDxMP1Pjv3%2BGYcZfD7izKD0LRJ1NaB%2F%2BTS2oQxDcjWONiG5Vc%2FJBpmlGV8dz2%2FOjZ6tBvkU4m1oJF2YPcswiN6QzwY6pgEeeNOYla%2BQsTGIdlDu7Bots0bvr12AWEQM8G2Dc6g93n0hmKBx6Rn%2FanFaFsLgelNVTZAfFO4rHUsRUusR%2FrtWIyQuAqe3B0IIXl9Od4MJVRxiEmxLlbG8eTOmeoA%2BFIim04bpzuSoXZRjVYSkwsATuUK2iDh47Y%2FItJTyZAtEMWcbEB2DTYuDKxHvz7nZNc%2BteUKV6oaMbNiY%2BPkBrjG2AHCtOpcs&X-Amz-Signature=8336f2ad9f0a6e1efd6210690c933e9928e083fc88984b288cb7938f217b4c32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627AXY6RJ%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG1jNctsnHU89EmwKtDAhdAdSTxSl2kpxcI3%2BweIglJMAiAM6fUOCMf%2Fg%2BVZR9yacM7UIEw0hKM3UXE0UDqMva%2BqHSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF1LkZKhGoONzngqKtwDiNNXOk2U3FL2F5ivOeA1B%2FP45NKizXQYCU%2Bs2mbzqFNwZ6%2Fr9Cju88miMzUqV%2FhgrTby7pQIEsYZNuTU23PzSCGV06i08BGHxaGK6OnM8el4k5JYS%2FCbBu1mPLUNOPofO3fDed8UgQHcnH%2BlXVtCoZl3CR1A95j489Ur%2F1KHlvW2uMuD%2FA%2BBb2OY4UJHRaDZGDYIJXwrbg8wd2HM1XDm2SdBO3RgNvnkZ1wKCQ50zOvBF2%2BBnMc3YnEzcWRbTH1O23rt65YS6zkQ0OEO8ShR7rK8iVw4WANAbp4ZmlAW%2Bu3jrqTXvvBljr8ND029XddU3G65U%2FMdbmNMV4SGsAWhYLjM4FHQiAJtCWLMqvYBc1uqSBwGmfjvMNsHQfaaWDtElJA6tRjuhijlycBiI2qBAb0jRFUzDGTPeplYLxbxrG7UghO1FRwOuF5diub4hfBYN3RPQ%2FsRlZhv%2FqnB0PfGo8Em6SXcnmSQqr4SCKdJtsjRD6zNnLR2tAvgJk8Emn1a1loBUA05CAPLPN8A2weUD0sHtcb8IYDkr2MTKPcDrkDxMP1Pjv3%2BGYcZfD7izKD0LRJ1NaB%2F%2BTS2oQxDcjWONiG5Vc%2FJBpmlGV8dz2%2FOjZ6tBvkU4m1oJF2YPcswiN6QzwY6pgEeeNOYla%2BQsTGIdlDu7Bots0bvr12AWEQM8G2Dc6g93n0hmKBx6Rn%2FanFaFsLgelNVTZAfFO4rHUsRUusR%2FrtWIyQuAqe3B0IIXl9Od4MJVRxiEmxLlbG8eTOmeoA%2BFIim04bpzuSoXZRjVYSkwsATuUK2iDh47Y%2FItJTyZAtEMWcbEB2DTYuDKxHvz7nZNc%2BteUKV6oaMbNiY%2BPkBrjG2AHCtOpcs&X-Amz-Signature=153f5ac67b15b9ba5a24c13b72fd29460edf2919203feae396033063abff4b54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627AXY6RJ%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG1jNctsnHU89EmwKtDAhdAdSTxSl2kpxcI3%2BweIglJMAiAM6fUOCMf%2Fg%2BVZR9yacM7UIEw0hKM3UXE0UDqMva%2BqHSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF1LkZKhGoONzngqKtwDiNNXOk2U3FL2F5ivOeA1B%2FP45NKizXQYCU%2Bs2mbzqFNwZ6%2Fr9Cju88miMzUqV%2FhgrTby7pQIEsYZNuTU23PzSCGV06i08BGHxaGK6OnM8el4k5JYS%2FCbBu1mPLUNOPofO3fDed8UgQHcnH%2BlXVtCoZl3CR1A95j489Ur%2F1KHlvW2uMuD%2FA%2BBb2OY4UJHRaDZGDYIJXwrbg8wd2HM1XDm2SdBO3RgNvnkZ1wKCQ50zOvBF2%2BBnMc3YnEzcWRbTH1O23rt65YS6zkQ0OEO8ShR7rK8iVw4WANAbp4ZmlAW%2Bu3jrqTXvvBljr8ND029XddU3G65U%2FMdbmNMV4SGsAWhYLjM4FHQiAJtCWLMqvYBc1uqSBwGmfjvMNsHQfaaWDtElJA6tRjuhijlycBiI2qBAb0jRFUzDGTPeplYLxbxrG7UghO1FRwOuF5diub4hfBYN3RPQ%2FsRlZhv%2FqnB0PfGo8Em6SXcnmSQqr4SCKdJtsjRD6zNnLR2tAvgJk8Emn1a1loBUA05CAPLPN8A2weUD0sHtcb8IYDkr2MTKPcDrkDxMP1Pjv3%2BGYcZfD7izKD0LRJ1NaB%2F%2BTS2oQxDcjWONiG5Vc%2FJBpmlGV8dz2%2FOjZ6tBvkU4m1oJF2YPcswiN6QzwY6pgEeeNOYla%2BQsTGIdlDu7Bots0bvr12AWEQM8G2Dc6g93n0hmKBx6Rn%2FanFaFsLgelNVTZAfFO4rHUsRUusR%2FrtWIyQuAqe3B0IIXl9Od4MJVRxiEmxLlbG8eTOmeoA%2BFIim04bpzuSoXZRjVYSkwsATuUK2iDh47Y%2FItJTyZAtEMWcbEB2DTYuDKxHvz7nZNc%2BteUKV6oaMbNiY%2BPkBrjG2AHCtOpcs&X-Amz-Signature=44ef5b438133ac9556cd463b8d2a111a362ccdfab765f51a4d8be423c23e08ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627AXY6RJ%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG1jNctsnHU89EmwKtDAhdAdSTxSl2kpxcI3%2BweIglJMAiAM6fUOCMf%2Fg%2BVZR9yacM7UIEw0hKM3UXE0UDqMva%2BqHSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF1LkZKhGoONzngqKtwDiNNXOk2U3FL2F5ivOeA1B%2FP45NKizXQYCU%2Bs2mbzqFNwZ6%2Fr9Cju88miMzUqV%2FhgrTby7pQIEsYZNuTU23PzSCGV06i08BGHxaGK6OnM8el4k5JYS%2FCbBu1mPLUNOPofO3fDed8UgQHcnH%2BlXVtCoZl3CR1A95j489Ur%2F1KHlvW2uMuD%2FA%2BBb2OY4UJHRaDZGDYIJXwrbg8wd2HM1XDm2SdBO3RgNvnkZ1wKCQ50zOvBF2%2BBnMc3YnEzcWRbTH1O23rt65YS6zkQ0OEO8ShR7rK8iVw4WANAbp4ZmlAW%2Bu3jrqTXvvBljr8ND029XddU3G65U%2FMdbmNMV4SGsAWhYLjM4FHQiAJtCWLMqvYBc1uqSBwGmfjvMNsHQfaaWDtElJA6tRjuhijlycBiI2qBAb0jRFUzDGTPeplYLxbxrG7UghO1FRwOuF5diub4hfBYN3RPQ%2FsRlZhv%2FqnB0PfGo8Em6SXcnmSQqr4SCKdJtsjRD6zNnLR2tAvgJk8Emn1a1loBUA05CAPLPN8A2weUD0sHtcb8IYDkr2MTKPcDrkDxMP1Pjv3%2BGYcZfD7izKD0LRJ1NaB%2F%2BTS2oQxDcjWONiG5Vc%2FJBpmlGV8dz2%2FOjZ6tBvkU4m1oJF2YPcswiN6QzwY6pgEeeNOYla%2BQsTGIdlDu7Bots0bvr12AWEQM8G2Dc6g93n0hmKBx6Rn%2FanFaFsLgelNVTZAfFO4rHUsRUusR%2FrtWIyQuAqe3B0IIXl9Od4MJVRxiEmxLlbG8eTOmeoA%2BFIim04bpzuSoXZRjVYSkwsATuUK2iDh47Y%2FItJTyZAtEMWcbEB2DTYuDKxHvz7nZNc%2BteUKV6oaMbNiY%2BPkBrjG2AHCtOpcs&X-Amz-Signature=fbc2e1c4642f4bacd0e47e1b454f2531852ff04584d6b909e39256e78b7f9195&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627AXY6RJ%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG1jNctsnHU89EmwKtDAhdAdSTxSl2kpxcI3%2BweIglJMAiAM6fUOCMf%2Fg%2BVZR9yacM7UIEw0hKM3UXE0UDqMva%2BqHSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF1LkZKhGoONzngqKtwDiNNXOk2U3FL2F5ivOeA1B%2FP45NKizXQYCU%2Bs2mbzqFNwZ6%2Fr9Cju88miMzUqV%2FhgrTby7pQIEsYZNuTU23PzSCGV06i08BGHxaGK6OnM8el4k5JYS%2FCbBu1mPLUNOPofO3fDed8UgQHcnH%2BlXVtCoZl3CR1A95j489Ur%2F1KHlvW2uMuD%2FA%2BBb2OY4UJHRaDZGDYIJXwrbg8wd2HM1XDm2SdBO3RgNvnkZ1wKCQ50zOvBF2%2BBnMc3YnEzcWRbTH1O23rt65YS6zkQ0OEO8ShR7rK8iVw4WANAbp4ZmlAW%2Bu3jrqTXvvBljr8ND029XddU3G65U%2FMdbmNMV4SGsAWhYLjM4FHQiAJtCWLMqvYBc1uqSBwGmfjvMNsHQfaaWDtElJA6tRjuhijlycBiI2qBAb0jRFUzDGTPeplYLxbxrG7UghO1FRwOuF5diub4hfBYN3RPQ%2FsRlZhv%2FqnB0PfGo8Em6SXcnmSQqr4SCKdJtsjRD6zNnLR2tAvgJk8Emn1a1loBUA05CAPLPN8A2weUD0sHtcb8IYDkr2MTKPcDrkDxMP1Pjv3%2BGYcZfD7izKD0LRJ1NaB%2F%2BTS2oQxDcjWONiG5Vc%2FJBpmlGV8dz2%2FOjZ6tBvkU4m1oJF2YPcswiN6QzwY6pgEeeNOYla%2BQsTGIdlDu7Bots0bvr12AWEQM8G2Dc6g93n0hmKBx6Rn%2FanFaFsLgelNVTZAfFO4rHUsRUusR%2FrtWIyQuAqe3B0IIXl9Od4MJVRxiEmxLlbG8eTOmeoA%2BFIim04bpzuSoXZRjVYSkwsATuUK2iDh47Y%2FItJTyZAtEMWcbEB2DTYuDKxHvz7nZNc%2BteUKV6oaMbNiY%2BPkBrjG2AHCtOpcs&X-Amz-Signature=95cca98f8fbda2672409a9e2bec25bb1f4c0ce44a6f6c0873529323144083364&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627AXY6RJ%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG1jNctsnHU89EmwKtDAhdAdSTxSl2kpxcI3%2BweIglJMAiAM6fUOCMf%2Fg%2BVZR9yacM7UIEw0hKM3UXE0UDqMva%2BqHSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF1LkZKhGoONzngqKtwDiNNXOk2U3FL2F5ivOeA1B%2FP45NKizXQYCU%2Bs2mbzqFNwZ6%2Fr9Cju88miMzUqV%2FhgrTby7pQIEsYZNuTU23PzSCGV06i08BGHxaGK6OnM8el4k5JYS%2FCbBu1mPLUNOPofO3fDed8UgQHcnH%2BlXVtCoZl3CR1A95j489Ur%2F1KHlvW2uMuD%2FA%2BBb2OY4UJHRaDZGDYIJXwrbg8wd2HM1XDm2SdBO3RgNvnkZ1wKCQ50zOvBF2%2BBnMc3YnEzcWRbTH1O23rt65YS6zkQ0OEO8ShR7rK8iVw4WANAbp4ZmlAW%2Bu3jrqTXvvBljr8ND029XddU3G65U%2FMdbmNMV4SGsAWhYLjM4FHQiAJtCWLMqvYBc1uqSBwGmfjvMNsHQfaaWDtElJA6tRjuhijlycBiI2qBAb0jRFUzDGTPeplYLxbxrG7UghO1FRwOuF5diub4hfBYN3RPQ%2FsRlZhv%2FqnB0PfGo8Em6SXcnmSQqr4SCKdJtsjRD6zNnLR2tAvgJk8Emn1a1loBUA05CAPLPN8A2weUD0sHtcb8IYDkr2MTKPcDrkDxMP1Pjv3%2BGYcZfD7izKD0LRJ1NaB%2F%2BTS2oQxDcjWONiG5Vc%2FJBpmlGV8dz2%2FOjZ6tBvkU4m1oJF2YPcswiN6QzwY6pgEeeNOYla%2BQsTGIdlDu7Bots0bvr12AWEQM8G2Dc6g93n0hmKBx6Rn%2FanFaFsLgelNVTZAfFO4rHUsRUusR%2FrtWIyQuAqe3B0IIXl9Od4MJVRxiEmxLlbG8eTOmeoA%2BFIim04bpzuSoXZRjVYSkwsATuUK2iDh47Y%2FItJTyZAtEMWcbEB2DTYuDKxHvz7nZNc%2BteUKV6oaMbNiY%2BPkBrjG2AHCtOpcs&X-Amz-Signature=93503e58acce3fbb9cc8fc2588335527febe35e8074db5f202566a6be0c662cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627AXY6RJ%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIG1jNctsnHU89EmwKtDAhdAdSTxSl2kpxcI3%2BweIglJMAiAM6fUOCMf%2Fg%2BVZR9yacM7UIEw0hKM3UXE0UDqMva%2BqHSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTF1LkZKhGoONzngqKtwDiNNXOk2U3FL2F5ivOeA1B%2FP45NKizXQYCU%2Bs2mbzqFNwZ6%2Fr9Cju88miMzUqV%2FhgrTby7pQIEsYZNuTU23PzSCGV06i08BGHxaGK6OnM8el4k5JYS%2FCbBu1mPLUNOPofO3fDed8UgQHcnH%2BlXVtCoZl3CR1A95j489Ur%2F1KHlvW2uMuD%2FA%2BBb2OY4UJHRaDZGDYIJXwrbg8wd2HM1XDm2SdBO3RgNvnkZ1wKCQ50zOvBF2%2BBnMc3YnEzcWRbTH1O23rt65YS6zkQ0OEO8ShR7rK8iVw4WANAbp4ZmlAW%2Bu3jrqTXvvBljr8ND029XddU3G65U%2FMdbmNMV4SGsAWhYLjM4FHQiAJtCWLMqvYBc1uqSBwGmfjvMNsHQfaaWDtElJA6tRjuhijlycBiI2qBAb0jRFUzDGTPeplYLxbxrG7UghO1FRwOuF5diub4hfBYN3RPQ%2FsRlZhv%2FqnB0PfGo8Em6SXcnmSQqr4SCKdJtsjRD6zNnLR2tAvgJk8Emn1a1loBUA05CAPLPN8A2weUD0sHtcb8IYDkr2MTKPcDrkDxMP1Pjv3%2BGYcZfD7izKD0LRJ1NaB%2F%2BTS2oQxDcjWONiG5Vc%2FJBpmlGV8dz2%2FOjZ6tBvkU4m1oJF2YPcswiN6QzwY6pgEeeNOYla%2BQsTGIdlDu7Bots0bvr12AWEQM8G2Dc6g93n0hmKBx6Rn%2FanFaFsLgelNVTZAfFO4rHUsRUusR%2FrtWIyQuAqe3B0IIXl9Od4MJVRxiEmxLlbG8eTOmeoA%2BFIim04bpzuSoXZRjVYSkwsATuUK2iDh47Y%2FItJTyZAtEMWcbEB2DTYuDKxHvz7nZNc%2BteUKV6oaMbNiY%2BPkBrjG2AHCtOpcs&X-Amz-Signature=e94560760adb63d127a66d20b8cbf8165ab5d145bc8406303c9a24919f7d5a54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

