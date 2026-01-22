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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSNDXB6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAvp6aC8Lo5slL2b4EBZFBmnQmqZRqKQgg89EXiWMABYAiEAzxpyyCq0SD7xKOcjnVoiTmRQj5J1IWyhYSkN9dxrNMwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOwJERGAl9EF21myqCrcAzpfaPVk1%2BSL%2F22zCzqY2udvk%2Bn%2F0e56brv2mLx1a%2Bdoot8jjhjUSxJ7OAFEba1yKpAS5Sg5tj3jP9zD9QBQqKBIyqjhz25FoQxNXzPEEOCmQXbaYse9Yg36lQWefx%2FlZL%2FyGy0XfmbzDvz0BIFQapFxQrX9fEbL1JHd1ur73g5rdxepTqJOGgR38iVIw%2BiCNgRUhGFeUnqniow0kkuLS3AO%2BAbVRrH1TGbwFEFh%2F3qhcLVfbpBuop5Abjr8p4%2BjdHviuf4xksZJqLvQsrM3c%2FJ5sughkCtALL145P7b7t%2F6Eu0f%2B0GtjFofqNkcnpeotspms65912RRFiCjfczCHNVDRa03UVJPxnNwTt0lbCYRLwsoxp5R7uEqQja5OoQyD5ESFaHMhlhmXXpIuuJzRRRlYhAWMXWTpXxh1GdXzsQEbkZPd1HNepych4P0ETJwDOeytSmEi1lR2AQfbKV0zyq96RftnoFOvm3ayfex4DtWdVpeDATauYfAtviyA%2Fh%2FimHqReSb9D6OFGXsEGACd4YWhBrljXmpMhRqKNW9IwfBi6yWfMzfcIJcq8FMUPbeozkWXCSlAwCz6BPIhtz7tH5mzyedhkMuE0Yp9nQnt6XhXtF4B8g4IzFAT0KSMOTXxcsGOqUBKcgOy5JLhc4HP1t5zTX78vQshGyl2lzuGfUN0ZdJS1tPnojewWXIUbbItLmRBsww0aaCOxDBxjN1gMVgGxalI%2BaOpVtS15WCDo0HhAGNiaT6tPGCYZJoVTZ51YquYxTREV0APpxwRhQX69K7gguHkW1BZpYi1muTcUbldKv9j21KtLzMlTN0cOzQ1Sb%2BfaJC1h7LZz70Yk4OS3Irb%2FSZ36%2FUDzFW&X-Amz-Signature=f7c992c0bd1da3bc543c23b32290429e1120e18963ef485b9a45f8baefc10338&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSNDXB6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAvp6aC8Lo5slL2b4EBZFBmnQmqZRqKQgg89EXiWMABYAiEAzxpyyCq0SD7xKOcjnVoiTmRQj5J1IWyhYSkN9dxrNMwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOwJERGAl9EF21myqCrcAzpfaPVk1%2BSL%2F22zCzqY2udvk%2Bn%2F0e56brv2mLx1a%2Bdoot8jjhjUSxJ7OAFEba1yKpAS5Sg5tj3jP9zD9QBQqKBIyqjhz25FoQxNXzPEEOCmQXbaYse9Yg36lQWefx%2FlZL%2FyGy0XfmbzDvz0BIFQapFxQrX9fEbL1JHd1ur73g5rdxepTqJOGgR38iVIw%2BiCNgRUhGFeUnqniow0kkuLS3AO%2BAbVRrH1TGbwFEFh%2F3qhcLVfbpBuop5Abjr8p4%2BjdHviuf4xksZJqLvQsrM3c%2FJ5sughkCtALL145P7b7t%2F6Eu0f%2B0GtjFofqNkcnpeotspms65912RRFiCjfczCHNVDRa03UVJPxnNwTt0lbCYRLwsoxp5R7uEqQja5OoQyD5ESFaHMhlhmXXpIuuJzRRRlYhAWMXWTpXxh1GdXzsQEbkZPd1HNepych4P0ETJwDOeytSmEi1lR2AQfbKV0zyq96RftnoFOvm3ayfex4DtWdVpeDATauYfAtviyA%2Fh%2FimHqReSb9D6OFGXsEGACd4YWhBrljXmpMhRqKNW9IwfBi6yWfMzfcIJcq8FMUPbeozkWXCSlAwCz6BPIhtz7tH5mzyedhkMuE0Yp9nQnt6XhXtF4B8g4IzFAT0KSMOTXxcsGOqUBKcgOy5JLhc4HP1t5zTX78vQshGyl2lzuGfUN0ZdJS1tPnojewWXIUbbItLmRBsww0aaCOxDBxjN1gMVgGxalI%2BaOpVtS15WCDo0HhAGNiaT6tPGCYZJoVTZ51YquYxTREV0APpxwRhQX69K7gguHkW1BZpYi1muTcUbldKv9j21KtLzMlTN0cOzQ1Sb%2BfaJC1h7LZz70Yk4OS3Irb%2FSZ36%2FUDzFW&X-Amz-Signature=f858db4c2df41c1673d0516492a465900b7442964a340fd4bf87cad3a085ed02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSNDXB6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAvp6aC8Lo5slL2b4EBZFBmnQmqZRqKQgg89EXiWMABYAiEAzxpyyCq0SD7xKOcjnVoiTmRQj5J1IWyhYSkN9dxrNMwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOwJERGAl9EF21myqCrcAzpfaPVk1%2BSL%2F22zCzqY2udvk%2Bn%2F0e56brv2mLx1a%2Bdoot8jjhjUSxJ7OAFEba1yKpAS5Sg5tj3jP9zD9QBQqKBIyqjhz25FoQxNXzPEEOCmQXbaYse9Yg36lQWefx%2FlZL%2FyGy0XfmbzDvz0BIFQapFxQrX9fEbL1JHd1ur73g5rdxepTqJOGgR38iVIw%2BiCNgRUhGFeUnqniow0kkuLS3AO%2BAbVRrH1TGbwFEFh%2F3qhcLVfbpBuop5Abjr8p4%2BjdHviuf4xksZJqLvQsrM3c%2FJ5sughkCtALL145P7b7t%2F6Eu0f%2B0GtjFofqNkcnpeotspms65912RRFiCjfczCHNVDRa03UVJPxnNwTt0lbCYRLwsoxp5R7uEqQja5OoQyD5ESFaHMhlhmXXpIuuJzRRRlYhAWMXWTpXxh1GdXzsQEbkZPd1HNepych4P0ETJwDOeytSmEi1lR2AQfbKV0zyq96RftnoFOvm3ayfex4DtWdVpeDATauYfAtviyA%2Fh%2FimHqReSb9D6OFGXsEGACd4YWhBrljXmpMhRqKNW9IwfBi6yWfMzfcIJcq8FMUPbeozkWXCSlAwCz6BPIhtz7tH5mzyedhkMuE0Yp9nQnt6XhXtF4B8g4IzFAT0KSMOTXxcsGOqUBKcgOy5JLhc4HP1t5zTX78vQshGyl2lzuGfUN0ZdJS1tPnojewWXIUbbItLmRBsww0aaCOxDBxjN1gMVgGxalI%2BaOpVtS15WCDo0HhAGNiaT6tPGCYZJoVTZ51YquYxTREV0APpxwRhQX69K7gguHkW1BZpYi1muTcUbldKv9j21KtLzMlTN0cOzQ1Sb%2BfaJC1h7LZz70Yk4OS3Irb%2FSZ36%2FUDzFW&X-Amz-Signature=c6be4cd9b25b8f666199affced9d38cac69b0c9af332da41ce75c5cbcc0f871d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSNDXB6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAvp6aC8Lo5slL2b4EBZFBmnQmqZRqKQgg89EXiWMABYAiEAzxpyyCq0SD7xKOcjnVoiTmRQj5J1IWyhYSkN9dxrNMwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOwJERGAl9EF21myqCrcAzpfaPVk1%2BSL%2F22zCzqY2udvk%2Bn%2F0e56brv2mLx1a%2Bdoot8jjhjUSxJ7OAFEba1yKpAS5Sg5tj3jP9zD9QBQqKBIyqjhz25FoQxNXzPEEOCmQXbaYse9Yg36lQWefx%2FlZL%2FyGy0XfmbzDvz0BIFQapFxQrX9fEbL1JHd1ur73g5rdxepTqJOGgR38iVIw%2BiCNgRUhGFeUnqniow0kkuLS3AO%2BAbVRrH1TGbwFEFh%2F3qhcLVfbpBuop5Abjr8p4%2BjdHviuf4xksZJqLvQsrM3c%2FJ5sughkCtALL145P7b7t%2F6Eu0f%2B0GtjFofqNkcnpeotspms65912RRFiCjfczCHNVDRa03UVJPxnNwTt0lbCYRLwsoxp5R7uEqQja5OoQyD5ESFaHMhlhmXXpIuuJzRRRlYhAWMXWTpXxh1GdXzsQEbkZPd1HNepych4P0ETJwDOeytSmEi1lR2AQfbKV0zyq96RftnoFOvm3ayfex4DtWdVpeDATauYfAtviyA%2Fh%2FimHqReSb9D6OFGXsEGACd4YWhBrljXmpMhRqKNW9IwfBi6yWfMzfcIJcq8FMUPbeozkWXCSlAwCz6BPIhtz7tH5mzyedhkMuE0Yp9nQnt6XhXtF4B8g4IzFAT0KSMOTXxcsGOqUBKcgOy5JLhc4HP1t5zTX78vQshGyl2lzuGfUN0ZdJS1tPnojewWXIUbbItLmRBsww0aaCOxDBxjN1gMVgGxalI%2BaOpVtS15WCDo0HhAGNiaT6tPGCYZJoVTZ51YquYxTREV0APpxwRhQX69K7gguHkW1BZpYi1muTcUbldKv9j21KtLzMlTN0cOzQ1Sb%2BfaJC1h7LZz70Yk4OS3Irb%2FSZ36%2FUDzFW&X-Amz-Signature=97735bc844b70a6ddc4a60db7ca683e8dc43e18383d68c6a8e66bb91bacb9019&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSNDXB6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAvp6aC8Lo5slL2b4EBZFBmnQmqZRqKQgg89EXiWMABYAiEAzxpyyCq0SD7xKOcjnVoiTmRQj5J1IWyhYSkN9dxrNMwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOwJERGAl9EF21myqCrcAzpfaPVk1%2BSL%2F22zCzqY2udvk%2Bn%2F0e56brv2mLx1a%2Bdoot8jjhjUSxJ7OAFEba1yKpAS5Sg5tj3jP9zD9QBQqKBIyqjhz25FoQxNXzPEEOCmQXbaYse9Yg36lQWefx%2FlZL%2FyGy0XfmbzDvz0BIFQapFxQrX9fEbL1JHd1ur73g5rdxepTqJOGgR38iVIw%2BiCNgRUhGFeUnqniow0kkuLS3AO%2BAbVRrH1TGbwFEFh%2F3qhcLVfbpBuop5Abjr8p4%2BjdHviuf4xksZJqLvQsrM3c%2FJ5sughkCtALL145P7b7t%2F6Eu0f%2B0GtjFofqNkcnpeotspms65912RRFiCjfczCHNVDRa03UVJPxnNwTt0lbCYRLwsoxp5R7uEqQja5OoQyD5ESFaHMhlhmXXpIuuJzRRRlYhAWMXWTpXxh1GdXzsQEbkZPd1HNepych4P0ETJwDOeytSmEi1lR2AQfbKV0zyq96RftnoFOvm3ayfex4DtWdVpeDATauYfAtviyA%2Fh%2FimHqReSb9D6OFGXsEGACd4YWhBrljXmpMhRqKNW9IwfBi6yWfMzfcIJcq8FMUPbeozkWXCSlAwCz6BPIhtz7tH5mzyedhkMuE0Yp9nQnt6XhXtF4B8g4IzFAT0KSMOTXxcsGOqUBKcgOy5JLhc4HP1t5zTX78vQshGyl2lzuGfUN0ZdJS1tPnojewWXIUbbItLmRBsww0aaCOxDBxjN1gMVgGxalI%2BaOpVtS15WCDo0HhAGNiaT6tPGCYZJoVTZ51YquYxTREV0APpxwRhQX69K7gguHkW1BZpYi1muTcUbldKv9j21KtLzMlTN0cOzQ1Sb%2BfaJC1h7LZz70Yk4OS3Irb%2FSZ36%2FUDzFW&X-Amz-Signature=f291a6c888385c27af12efc158da91bad22f4117fa538a4c6b3849c2a395ab22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSNDXB6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAvp6aC8Lo5slL2b4EBZFBmnQmqZRqKQgg89EXiWMABYAiEAzxpyyCq0SD7xKOcjnVoiTmRQj5J1IWyhYSkN9dxrNMwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOwJERGAl9EF21myqCrcAzpfaPVk1%2BSL%2F22zCzqY2udvk%2Bn%2F0e56brv2mLx1a%2Bdoot8jjhjUSxJ7OAFEba1yKpAS5Sg5tj3jP9zD9QBQqKBIyqjhz25FoQxNXzPEEOCmQXbaYse9Yg36lQWefx%2FlZL%2FyGy0XfmbzDvz0BIFQapFxQrX9fEbL1JHd1ur73g5rdxepTqJOGgR38iVIw%2BiCNgRUhGFeUnqniow0kkuLS3AO%2BAbVRrH1TGbwFEFh%2F3qhcLVfbpBuop5Abjr8p4%2BjdHviuf4xksZJqLvQsrM3c%2FJ5sughkCtALL145P7b7t%2F6Eu0f%2B0GtjFofqNkcnpeotspms65912RRFiCjfczCHNVDRa03UVJPxnNwTt0lbCYRLwsoxp5R7uEqQja5OoQyD5ESFaHMhlhmXXpIuuJzRRRlYhAWMXWTpXxh1GdXzsQEbkZPd1HNepych4P0ETJwDOeytSmEi1lR2AQfbKV0zyq96RftnoFOvm3ayfex4DtWdVpeDATauYfAtviyA%2Fh%2FimHqReSb9D6OFGXsEGACd4YWhBrljXmpMhRqKNW9IwfBi6yWfMzfcIJcq8FMUPbeozkWXCSlAwCz6BPIhtz7tH5mzyedhkMuE0Yp9nQnt6XhXtF4B8g4IzFAT0KSMOTXxcsGOqUBKcgOy5JLhc4HP1t5zTX78vQshGyl2lzuGfUN0ZdJS1tPnojewWXIUbbItLmRBsww0aaCOxDBxjN1gMVgGxalI%2BaOpVtS15WCDo0HhAGNiaT6tPGCYZJoVTZ51YquYxTREV0APpxwRhQX69K7gguHkW1BZpYi1muTcUbldKv9j21KtLzMlTN0cOzQ1Sb%2BfaJC1h7LZz70Yk4OS3Irb%2FSZ36%2FUDzFW&X-Amz-Signature=c2db1913f7c6ab7878d47b78caad4272a02f2d5eb0b3b943bfec839d33355c16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSNDXB6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAvp6aC8Lo5slL2b4EBZFBmnQmqZRqKQgg89EXiWMABYAiEAzxpyyCq0SD7xKOcjnVoiTmRQj5J1IWyhYSkN9dxrNMwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOwJERGAl9EF21myqCrcAzpfaPVk1%2BSL%2F22zCzqY2udvk%2Bn%2F0e56brv2mLx1a%2Bdoot8jjhjUSxJ7OAFEba1yKpAS5Sg5tj3jP9zD9QBQqKBIyqjhz25FoQxNXzPEEOCmQXbaYse9Yg36lQWefx%2FlZL%2FyGy0XfmbzDvz0BIFQapFxQrX9fEbL1JHd1ur73g5rdxepTqJOGgR38iVIw%2BiCNgRUhGFeUnqniow0kkuLS3AO%2BAbVRrH1TGbwFEFh%2F3qhcLVfbpBuop5Abjr8p4%2BjdHviuf4xksZJqLvQsrM3c%2FJ5sughkCtALL145P7b7t%2F6Eu0f%2B0GtjFofqNkcnpeotspms65912RRFiCjfczCHNVDRa03UVJPxnNwTt0lbCYRLwsoxp5R7uEqQja5OoQyD5ESFaHMhlhmXXpIuuJzRRRlYhAWMXWTpXxh1GdXzsQEbkZPd1HNepych4P0ETJwDOeytSmEi1lR2AQfbKV0zyq96RftnoFOvm3ayfex4DtWdVpeDATauYfAtviyA%2Fh%2FimHqReSb9D6OFGXsEGACd4YWhBrljXmpMhRqKNW9IwfBi6yWfMzfcIJcq8FMUPbeozkWXCSlAwCz6BPIhtz7tH5mzyedhkMuE0Yp9nQnt6XhXtF4B8g4IzFAT0KSMOTXxcsGOqUBKcgOy5JLhc4HP1t5zTX78vQshGyl2lzuGfUN0ZdJS1tPnojewWXIUbbItLmRBsww0aaCOxDBxjN1gMVgGxalI%2BaOpVtS15WCDo0HhAGNiaT6tPGCYZJoVTZ51YquYxTREV0APpxwRhQX69K7gguHkW1BZpYi1muTcUbldKv9j21KtLzMlTN0cOzQ1Sb%2BfaJC1h7LZz70Yk4OS3Irb%2FSZ36%2FUDzFW&X-Amz-Signature=02b1f4261d436c872138e31fd04aca3ae6ce89e656249fa10b3ac876018bcd84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSNDXB6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAvp6aC8Lo5slL2b4EBZFBmnQmqZRqKQgg89EXiWMABYAiEAzxpyyCq0SD7xKOcjnVoiTmRQj5J1IWyhYSkN9dxrNMwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOwJERGAl9EF21myqCrcAzpfaPVk1%2BSL%2F22zCzqY2udvk%2Bn%2F0e56brv2mLx1a%2Bdoot8jjhjUSxJ7OAFEba1yKpAS5Sg5tj3jP9zD9QBQqKBIyqjhz25FoQxNXzPEEOCmQXbaYse9Yg36lQWefx%2FlZL%2FyGy0XfmbzDvz0BIFQapFxQrX9fEbL1JHd1ur73g5rdxepTqJOGgR38iVIw%2BiCNgRUhGFeUnqniow0kkuLS3AO%2BAbVRrH1TGbwFEFh%2F3qhcLVfbpBuop5Abjr8p4%2BjdHviuf4xksZJqLvQsrM3c%2FJ5sughkCtALL145P7b7t%2F6Eu0f%2B0GtjFofqNkcnpeotspms65912RRFiCjfczCHNVDRa03UVJPxnNwTt0lbCYRLwsoxp5R7uEqQja5OoQyD5ESFaHMhlhmXXpIuuJzRRRlYhAWMXWTpXxh1GdXzsQEbkZPd1HNepych4P0ETJwDOeytSmEi1lR2AQfbKV0zyq96RftnoFOvm3ayfex4DtWdVpeDATauYfAtviyA%2Fh%2FimHqReSb9D6OFGXsEGACd4YWhBrljXmpMhRqKNW9IwfBi6yWfMzfcIJcq8FMUPbeozkWXCSlAwCz6BPIhtz7tH5mzyedhkMuE0Yp9nQnt6XhXtF4B8g4IzFAT0KSMOTXxcsGOqUBKcgOy5JLhc4HP1t5zTX78vQshGyl2lzuGfUN0ZdJS1tPnojewWXIUbbItLmRBsww0aaCOxDBxjN1gMVgGxalI%2BaOpVtS15WCDo0HhAGNiaT6tPGCYZJoVTZ51YquYxTREV0APpxwRhQX69K7gguHkW1BZpYi1muTcUbldKv9j21KtLzMlTN0cOzQ1Sb%2BfaJC1h7LZz70Yk4OS3Irb%2FSZ36%2FUDzFW&X-Amz-Signature=214184666fe3c7edc338ffc151ce816e3546eec3c44e2f3c745836ce4f3a8109&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSNDXB6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAvp6aC8Lo5slL2b4EBZFBmnQmqZRqKQgg89EXiWMABYAiEAzxpyyCq0SD7xKOcjnVoiTmRQj5J1IWyhYSkN9dxrNMwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOwJERGAl9EF21myqCrcAzpfaPVk1%2BSL%2F22zCzqY2udvk%2Bn%2F0e56brv2mLx1a%2Bdoot8jjhjUSxJ7OAFEba1yKpAS5Sg5tj3jP9zD9QBQqKBIyqjhz25FoQxNXzPEEOCmQXbaYse9Yg36lQWefx%2FlZL%2FyGy0XfmbzDvz0BIFQapFxQrX9fEbL1JHd1ur73g5rdxepTqJOGgR38iVIw%2BiCNgRUhGFeUnqniow0kkuLS3AO%2BAbVRrH1TGbwFEFh%2F3qhcLVfbpBuop5Abjr8p4%2BjdHviuf4xksZJqLvQsrM3c%2FJ5sughkCtALL145P7b7t%2F6Eu0f%2B0GtjFofqNkcnpeotspms65912RRFiCjfczCHNVDRa03UVJPxnNwTt0lbCYRLwsoxp5R7uEqQja5OoQyD5ESFaHMhlhmXXpIuuJzRRRlYhAWMXWTpXxh1GdXzsQEbkZPd1HNepych4P0ETJwDOeytSmEi1lR2AQfbKV0zyq96RftnoFOvm3ayfex4DtWdVpeDATauYfAtviyA%2Fh%2FimHqReSb9D6OFGXsEGACd4YWhBrljXmpMhRqKNW9IwfBi6yWfMzfcIJcq8FMUPbeozkWXCSlAwCz6BPIhtz7tH5mzyedhkMuE0Yp9nQnt6XhXtF4B8g4IzFAT0KSMOTXxcsGOqUBKcgOy5JLhc4HP1t5zTX78vQshGyl2lzuGfUN0ZdJS1tPnojewWXIUbbItLmRBsww0aaCOxDBxjN1gMVgGxalI%2BaOpVtS15WCDo0HhAGNiaT6tPGCYZJoVTZ51YquYxTREV0APpxwRhQX69K7gguHkW1BZpYi1muTcUbldKv9j21KtLzMlTN0cOzQ1Sb%2BfaJC1h7LZz70Yk4OS3Irb%2FSZ36%2FUDzFW&X-Amz-Signature=b27d13547d7d69ede1df903c438c5256be49667fb67a555e65e83e54ee4d0c51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSNDXB6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAvp6aC8Lo5slL2b4EBZFBmnQmqZRqKQgg89EXiWMABYAiEAzxpyyCq0SD7xKOcjnVoiTmRQj5J1IWyhYSkN9dxrNMwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOwJERGAl9EF21myqCrcAzpfaPVk1%2BSL%2F22zCzqY2udvk%2Bn%2F0e56brv2mLx1a%2Bdoot8jjhjUSxJ7OAFEba1yKpAS5Sg5tj3jP9zD9QBQqKBIyqjhz25FoQxNXzPEEOCmQXbaYse9Yg36lQWefx%2FlZL%2FyGy0XfmbzDvz0BIFQapFxQrX9fEbL1JHd1ur73g5rdxepTqJOGgR38iVIw%2BiCNgRUhGFeUnqniow0kkuLS3AO%2BAbVRrH1TGbwFEFh%2F3qhcLVfbpBuop5Abjr8p4%2BjdHviuf4xksZJqLvQsrM3c%2FJ5sughkCtALL145P7b7t%2F6Eu0f%2B0GtjFofqNkcnpeotspms65912RRFiCjfczCHNVDRa03UVJPxnNwTt0lbCYRLwsoxp5R7uEqQja5OoQyD5ESFaHMhlhmXXpIuuJzRRRlYhAWMXWTpXxh1GdXzsQEbkZPd1HNepych4P0ETJwDOeytSmEi1lR2AQfbKV0zyq96RftnoFOvm3ayfex4DtWdVpeDATauYfAtviyA%2Fh%2FimHqReSb9D6OFGXsEGACd4YWhBrljXmpMhRqKNW9IwfBi6yWfMzfcIJcq8FMUPbeozkWXCSlAwCz6BPIhtz7tH5mzyedhkMuE0Yp9nQnt6XhXtF4B8g4IzFAT0KSMOTXxcsGOqUBKcgOy5JLhc4HP1t5zTX78vQshGyl2lzuGfUN0ZdJS1tPnojewWXIUbbItLmRBsww0aaCOxDBxjN1gMVgGxalI%2BaOpVtS15WCDo0HhAGNiaT6tPGCYZJoVTZ51YquYxTREV0APpxwRhQX69K7gguHkW1BZpYi1muTcUbldKv9j21KtLzMlTN0cOzQ1Sb%2BfaJC1h7LZz70Yk4OS3Irb%2FSZ36%2FUDzFW&X-Amz-Signature=b8a6b9bb5eb11f6480952d5eb1834ef0dfa3dd22b9ae2fadbf29fd18a4f15fa2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

