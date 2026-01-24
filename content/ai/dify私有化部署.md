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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65SHDZP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBLwSeHthRnrhyuE%2BxGxhWqaSlqwhTUYRL2XY%2BI4BUyiAiAVolIOKytkYuDlhNI8rTEr031QM3B4K%2BrPuRo%2Fo7QsvSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMvOmAyoLq0EhoAOwYKtwD%2FIAhYNLVkyGy1XKe%2FQGgTyxGwyE1febjoTwPFEg16SxIJ1PjbgwB3f9ImRKtW2VK90%2FlrvF878H6V2Cchp9TvUHBGW2ERyzcEBW%2FNLFHKEjGFveci7pSETotjP5jGWxJDWY%2Fhgw9PHskFQK%2FaDr15spWkn7knYZohQneAOFgTgLjPoYLcs3MQ7cJqxic86G4nsiFbej5goInSXpsqcoRue80Tojq5tszVh0ocvNLfUxVynmLYl0kxa6PCGsxs2qv2q2EUGc6YNW%2FtAQRBGGPM%2Bun1Q9uYOf7Ttt2nFdDAJphQowrQuI8QjPxw7kpwMbJzltpLPt%2F0bWGM5yFYHjHQqwBHjcOE9dZ0cIxms20ssZOldkjWvfNl65YtfyT4R8BSrIeZPV0TS9QzpoLozxjLTXXNJrLtCboaeOtnGd6WtYmlCluwfxJAhKfyAZiZs0LFw2BxHJrmMLnV8hte63JNtgWzl7XW8KNsgxldpguYSuClaPbVNGCcbF3W3ceOFEj9GdmkhxqKZjz5zN6x6LVnoGOwg%2BBWKfTpg%2FmY1qneJlhbYyTFgMakoOBdIzIS%2BbjsoznH8l1ADUYDEFHKxsnL3gH%2FhRMteIKQCAurEw%2B2J9vUJf%2FgpvPrN3MOqYwiM%2FQywY6pgGnSvUYyd%2FuDnySIblBB5PBGsKG2NUIHLMB1paTgxjhZVsdREHYwIgnTUrr9xOwjnKuwrVRj0OBjgC%2Bcd5msYUwTQQ67C2E7lhbhVrkLRLPwe1tm9jbczzFI7ikY2Z5PJ9ocpHWTmba%2FLOx7sY40rOJIjuV1DrTdnovBdJKdKtxC%2FM%2B4y%2Bdv1%2BMat8pgowmnh1sC9WtdGD9krgjc0JxNU4Q7cu3zlYd&X-Amz-Signature=2e17738b95a105015c16ce8dda7a7056319f0ef264103b4a9daeef8711cd3955&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65SHDZP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBLwSeHthRnrhyuE%2BxGxhWqaSlqwhTUYRL2XY%2BI4BUyiAiAVolIOKytkYuDlhNI8rTEr031QM3B4K%2BrPuRo%2Fo7QsvSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMvOmAyoLq0EhoAOwYKtwD%2FIAhYNLVkyGy1XKe%2FQGgTyxGwyE1febjoTwPFEg16SxIJ1PjbgwB3f9ImRKtW2VK90%2FlrvF878H6V2Cchp9TvUHBGW2ERyzcEBW%2FNLFHKEjGFveci7pSETotjP5jGWxJDWY%2Fhgw9PHskFQK%2FaDr15spWkn7knYZohQneAOFgTgLjPoYLcs3MQ7cJqxic86G4nsiFbej5goInSXpsqcoRue80Tojq5tszVh0ocvNLfUxVynmLYl0kxa6PCGsxs2qv2q2EUGc6YNW%2FtAQRBGGPM%2Bun1Q9uYOf7Ttt2nFdDAJphQowrQuI8QjPxw7kpwMbJzltpLPt%2F0bWGM5yFYHjHQqwBHjcOE9dZ0cIxms20ssZOldkjWvfNl65YtfyT4R8BSrIeZPV0TS9QzpoLozxjLTXXNJrLtCboaeOtnGd6WtYmlCluwfxJAhKfyAZiZs0LFw2BxHJrmMLnV8hte63JNtgWzl7XW8KNsgxldpguYSuClaPbVNGCcbF3W3ceOFEj9GdmkhxqKZjz5zN6x6LVnoGOwg%2BBWKfTpg%2FmY1qneJlhbYyTFgMakoOBdIzIS%2BbjsoznH8l1ADUYDEFHKxsnL3gH%2FhRMteIKQCAurEw%2B2J9vUJf%2FgpvPrN3MOqYwiM%2FQywY6pgGnSvUYyd%2FuDnySIblBB5PBGsKG2NUIHLMB1paTgxjhZVsdREHYwIgnTUrr9xOwjnKuwrVRj0OBjgC%2Bcd5msYUwTQQ67C2E7lhbhVrkLRLPwe1tm9jbczzFI7ikY2Z5PJ9ocpHWTmba%2FLOx7sY40rOJIjuV1DrTdnovBdJKdKtxC%2FM%2B4y%2Bdv1%2BMat8pgowmnh1sC9WtdGD9krgjc0JxNU4Q7cu3zlYd&X-Amz-Signature=0a6de9507d1f900822baa5c9d85f1ad0130ba95b62162aea0853b7607bce0e57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65SHDZP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBLwSeHthRnrhyuE%2BxGxhWqaSlqwhTUYRL2XY%2BI4BUyiAiAVolIOKytkYuDlhNI8rTEr031QM3B4K%2BrPuRo%2Fo7QsvSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMvOmAyoLq0EhoAOwYKtwD%2FIAhYNLVkyGy1XKe%2FQGgTyxGwyE1febjoTwPFEg16SxIJ1PjbgwB3f9ImRKtW2VK90%2FlrvF878H6V2Cchp9TvUHBGW2ERyzcEBW%2FNLFHKEjGFveci7pSETotjP5jGWxJDWY%2Fhgw9PHskFQK%2FaDr15spWkn7knYZohQneAOFgTgLjPoYLcs3MQ7cJqxic86G4nsiFbej5goInSXpsqcoRue80Tojq5tszVh0ocvNLfUxVynmLYl0kxa6PCGsxs2qv2q2EUGc6YNW%2FtAQRBGGPM%2Bun1Q9uYOf7Ttt2nFdDAJphQowrQuI8QjPxw7kpwMbJzltpLPt%2F0bWGM5yFYHjHQqwBHjcOE9dZ0cIxms20ssZOldkjWvfNl65YtfyT4R8BSrIeZPV0TS9QzpoLozxjLTXXNJrLtCboaeOtnGd6WtYmlCluwfxJAhKfyAZiZs0LFw2BxHJrmMLnV8hte63JNtgWzl7XW8KNsgxldpguYSuClaPbVNGCcbF3W3ceOFEj9GdmkhxqKZjz5zN6x6LVnoGOwg%2BBWKfTpg%2FmY1qneJlhbYyTFgMakoOBdIzIS%2BbjsoznH8l1ADUYDEFHKxsnL3gH%2FhRMteIKQCAurEw%2B2J9vUJf%2FgpvPrN3MOqYwiM%2FQywY6pgGnSvUYyd%2FuDnySIblBB5PBGsKG2NUIHLMB1paTgxjhZVsdREHYwIgnTUrr9xOwjnKuwrVRj0OBjgC%2Bcd5msYUwTQQ67C2E7lhbhVrkLRLPwe1tm9jbczzFI7ikY2Z5PJ9ocpHWTmba%2FLOx7sY40rOJIjuV1DrTdnovBdJKdKtxC%2FM%2B4y%2Bdv1%2BMat8pgowmnh1sC9WtdGD9krgjc0JxNU4Q7cu3zlYd&X-Amz-Signature=070348eabb61151bf77762f9f121410f11aaa12eeffd8cb867807222fde2f79c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65SHDZP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBLwSeHthRnrhyuE%2BxGxhWqaSlqwhTUYRL2XY%2BI4BUyiAiAVolIOKytkYuDlhNI8rTEr031QM3B4K%2BrPuRo%2Fo7QsvSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMvOmAyoLq0EhoAOwYKtwD%2FIAhYNLVkyGy1XKe%2FQGgTyxGwyE1febjoTwPFEg16SxIJ1PjbgwB3f9ImRKtW2VK90%2FlrvF878H6V2Cchp9TvUHBGW2ERyzcEBW%2FNLFHKEjGFveci7pSETotjP5jGWxJDWY%2Fhgw9PHskFQK%2FaDr15spWkn7knYZohQneAOFgTgLjPoYLcs3MQ7cJqxic86G4nsiFbej5goInSXpsqcoRue80Tojq5tszVh0ocvNLfUxVynmLYl0kxa6PCGsxs2qv2q2EUGc6YNW%2FtAQRBGGPM%2Bun1Q9uYOf7Ttt2nFdDAJphQowrQuI8QjPxw7kpwMbJzltpLPt%2F0bWGM5yFYHjHQqwBHjcOE9dZ0cIxms20ssZOldkjWvfNl65YtfyT4R8BSrIeZPV0TS9QzpoLozxjLTXXNJrLtCboaeOtnGd6WtYmlCluwfxJAhKfyAZiZs0LFw2BxHJrmMLnV8hte63JNtgWzl7XW8KNsgxldpguYSuClaPbVNGCcbF3W3ceOFEj9GdmkhxqKZjz5zN6x6LVnoGOwg%2BBWKfTpg%2FmY1qneJlhbYyTFgMakoOBdIzIS%2BbjsoznH8l1ADUYDEFHKxsnL3gH%2FhRMteIKQCAurEw%2B2J9vUJf%2FgpvPrN3MOqYwiM%2FQywY6pgGnSvUYyd%2FuDnySIblBB5PBGsKG2NUIHLMB1paTgxjhZVsdREHYwIgnTUrr9xOwjnKuwrVRj0OBjgC%2Bcd5msYUwTQQ67C2E7lhbhVrkLRLPwe1tm9jbczzFI7ikY2Z5PJ9ocpHWTmba%2FLOx7sY40rOJIjuV1DrTdnovBdJKdKtxC%2FM%2B4y%2Bdv1%2BMat8pgowmnh1sC9WtdGD9krgjc0JxNU4Q7cu3zlYd&X-Amz-Signature=67002444491266173509c9fc66a20cf7d7edb93a496081c4c22f0f379264a92e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65SHDZP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBLwSeHthRnrhyuE%2BxGxhWqaSlqwhTUYRL2XY%2BI4BUyiAiAVolIOKytkYuDlhNI8rTEr031QM3B4K%2BrPuRo%2Fo7QsvSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMvOmAyoLq0EhoAOwYKtwD%2FIAhYNLVkyGy1XKe%2FQGgTyxGwyE1febjoTwPFEg16SxIJ1PjbgwB3f9ImRKtW2VK90%2FlrvF878H6V2Cchp9TvUHBGW2ERyzcEBW%2FNLFHKEjGFveci7pSETotjP5jGWxJDWY%2Fhgw9PHskFQK%2FaDr15spWkn7knYZohQneAOFgTgLjPoYLcs3MQ7cJqxic86G4nsiFbej5goInSXpsqcoRue80Tojq5tszVh0ocvNLfUxVynmLYl0kxa6PCGsxs2qv2q2EUGc6YNW%2FtAQRBGGPM%2Bun1Q9uYOf7Ttt2nFdDAJphQowrQuI8QjPxw7kpwMbJzltpLPt%2F0bWGM5yFYHjHQqwBHjcOE9dZ0cIxms20ssZOldkjWvfNl65YtfyT4R8BSrIeZPV0TS9QzpoLozxjLTXXNJrLtCboaeOtnGd6WtYmlCluwfxJAhKfyAZiZs0LFw2BxHJrmMLnV8hte63JNtgWzl7XW8KNsgxldpguYSuClaPbVNGCcbF3W3ceOFEj9GdmkhxqKZjz5zN6x6LVnoGOwg%2BBWKfTpg%2FmY1qneJlhbYyTFgMakoOBdIzIS%2BbjsoznH8l1ADUYDEFHKxsnL3gH%2FhRMteIKQCAurEw%2B2J9vUJf%2FgpvPrN3MOqYwiM%2FQywY6pgGnSvUYyd%2FuDnySIblBB5PBGsKG2NUIHLMB1paTgxjhZVsdREHYwIgnTUrr9xOwjnKuwrVRj0OBjgC%2Bcd5msYUwTQQ67C2E7lhbhVrkLRLPwe1tm9jbczzFI7ikY2Z5PJ9ocpHWTmba%2FLOx7sY40rOJIjuV1DrTdnovBdJKdKtxC%2FM%2B4y%2Bdv1%2BMat8pgowmnh1sC9WtdGD9krgjc0JxNU4Q7cu3zlYd&X-Amz-Signature=cd7c02e4ec490c76f4af0701bd08546326a63d40c3b512e77c4297e0e5014de3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65SHDZP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBLwSeHthRnrhyuE%2BxGxhWqaSlqwhTUYRL2XY%2BI4BUyiAiAVolIOKytkYuDlhNI8rTEr031QM3B4K%2BrPuRo%2Fo7QsvSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMvOmAyoLq0EhoAOwYKtwD%2FIAhYNLVkyGy1XKe%2FQGgTyxGwyE1febjoTwPFEg16SxIJ1PjbgwB3f9ImRKtW2VK90%2FlrvF878H6V2Cchp9TvUHBGW2ERyzcEBW%2FNLFHKEjGFveci7pSETotjP5jGWxJDWY%2Fhgw9PHskFQK%2FaDr15spWkn7knYZohQneAOFgTgLjPoYLcs3MQ7cJqxic86G4nsiFbej5goInSXpsqcoRue80Tojq5tszVh0ocvNLfUxVynmLYl0kxa6PCGsxs2qv2q2EUGc6YNW%2FtAQRBGGPM%2Bun1Q9uYOf7Ttt2nFdDAJphQowrQuI8QjPxw7kpwMbJzltpLPt%2F0bWGM5yFYHjHQqwBHjcOE9dZ0cIxms20ssZOldkjWvfNl65YtfyT4R8BSrIeZPV0TS9QzpoLozxjLTXXNJrLtCboaeOtnGd6WtYmlCluwfxJAhKfyAZiZs0LFw2BxHJrmMLnV8hte63JNtgWzl7XW8KNsgxldpguYSuClaPbVNGCcbF3W3ceOFEj9GdmkhxqKZjz5zN6x6LVnoGOwg%2BBWKfTpg%2FmY1qneJlhbYyTFgMakoOBdIzIS%2BbjsoznH8l1ADUYDEFHKxsnL3gH%2FhRMteIKQCAurEw%2B2J9vUJf%2FgpvPrN3MOqYwiM%2FQywY6pgGnSvUYyd%2FuDnySIblBB5PBGsKG2NUIHLMB1paTgxjhZVsdREHYwIgnTUrr9xOwjnKuwrVRj0OBjgC%2Bcd5msYUwTQQ67C2E7lhbhVrkLRLPwe1tm9jbczzFI7ikY2Z5PJ9ocpHWTmba%2FLOx7sY40rOJIjuV1DrTdnovBdJKdKtxC%2FM%2B4y%2Bdv1%2BMat8pgowmnh1sC9WtdGD9krgjc0JxNU4Q7cu3zlYd&X-Amz-Signature=54aa6e58e03af8a95d1f316236f9ab72a8bc92c49876ee7911f38ac828a69ac1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65SHDZP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBLwSeHthRnrhyuE%2BxGxhWqaSlqwhTUYRL2XY%2BI4BUyiAiAVolIOKytkYuDlhNI8rTEr031QM3B4K%2BrPuRo%2Fo7QsvSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMvOmAyoLq0EhoAOwYKtwD%2FIAhYNLVkyGy1XKe%2FQGgTyxGwyE1febjoTwPFEg16SxIJ1PjbgwB3f9ImRKtW2VK90%2FlrvF878H6V2Cchp9TvUHBGW2ERyzcEBW%2FNLFHKEjGFveci7pSETotjP5jGWxJDWY%2Fhgw9PHskFQK%2FaDr15spWkn7knYZohQneAOFgTgLjPoYLcs3MQ7cJqxic86G4nsiFbej5goInSXpsqcoRue80Tojq5tszVh0ocvNLfUxVynmLYl0kxa6PCGsxs2qv2q2EUGc6YNW%2FtAQRBGGPM%2Bun1Q9uYOf7Ttt2nFdDAJphQowrQuI8QjPxw7kpwMbJzltpLPt%2F0bWGM5yFYHjHQqwBHjcOE9dZ0cIxms20ssZOldkjWvfNl65YtfyT4R8BSrIeZPV0TS9QzpoLozxjLTXXNJrLtCboaeOtnGd6WtYmlCluwfxJAhKfyAZiZs0LFw2BxHJrmMLnV8hte63JNtgWzl7XW8KNsgxldpguYSuClaPbVNGCcbF3W3ceOFEj9GdmkhxqKZjz5zN6x6LVnoGOwg%2BBWKfTpg%2FmY1qneJlhbYyTFgMakoOBdIzIS%2BbjsoznH8l1ADUYDEFHKxsnL3gH%2FhRMteIKQCAurEw%2B2J9vUJf%2FgpvPrN3MOqYwiM%2FQywY6pgGnSvUYyd%2FuDnySIblBB5PBGsKG2NUIHLMB1paTgxjhZVsdREHYwIgnTUrr9xOwjnKuwrVRj0OBjgC%2Bcd5msYUwTQQ67C2E7lhbhVrkLRLPwe1tm9jbczzFI7ikY2Z5PJ9ocpHWTmba%2FLOx7sY40rOJIjuV1DrTdnovBdJKdKtxC%2FM%2B4y%2Bdv1%2BMat8pgowmnh1sC9WtdGD9krgjc0JxNU4Q7cu3zlYd&X-Amz-Signature=bf560428d6e25ac22d52c0aaa1a476c5a545cc539eb780ea828256b3ae63f144&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65SHDZP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBLwSeHthRnrhyuE%2BxGxhWqaSlqwhTUYRL2XY%2BI4BUyiAiAVolIOKytkYuDlhNI8rTEr031QM3B4K%2BrPuRo%2Fo7QsvSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMvOmAyoLq0EhoAOwYKtwD%2FIAhYNLVkyGy1XKe%2FQGgTyxGwyE1febjoTwPFEg16SxIJ1PjbgwB3f9ImRKtW2VK90%2FlrvF878H6V2Cchp9TvUHBGW2ERyzcEBW%2FNLFHKEjGFveci7pSETotjP5jGWxJDWY%2Fhgw9PHskFQK%2FaDr15spWkn7knYZohQneAOFgTgLjPoYLcs3MQ7cJqxic86G4nsiFbej5goInSXpsqcoRue80Tojq5tszVh0ocvNLfUxVynmLYl0kxa6PCGsxs2qv2q2EUGc6YNW%2FtAQRBGGPM%2Bun1Q9uYOf7Ttt2nFdDAJphQowrQuI8QjPxw7kpwMbJzltpLPt%2F0bWGM5yFYHjHQqwBHjcOE9dZ0cIxms20ssZOldkjWvfNl65YtfyT4R8BSrIeZPV0TS9QzpoLozxjLTXXNJrLtCboaeOtnGd6WtYmlCluwfxJAhKfyAZiZs0LFw2BxHJrmMLnV8hte63JNtgWzl7XW8KNsgxldpguYSuClaPbVNGCcbF3W3ceOFEj9GdmkhxqKZjz5zN6x6LVnoGOwg%2BBWKfTpg%2FmY1qneJlhbYyTFgMakoOBdIzIS%2BbjsoznH8l1ADUYDEFHKxsnL3gH%2FhRMteIKQCAurEw%2B2J9vUJf%2FgpvPrN3MOqYwiM%2FQywY6pgGnSvUYyd%2FuDnySIblBB5PBGsKG2NUIHLMB1paTgxjhZVsdREHYwIgnTUrr9xOwjnKuwrVRj0OBjgC%2Bcd5msYUwTQQ67C2E7lhbhVrkLRLPwe1tm9jbczzFI7ikY2Z5PJ9ocpHWTmba%2FLOx7sY40rOJIjuV1DrTdnovBdJKdKtxC%2FM%2B4y%2Bdv1%2BMat8pgowmnh1sC9WtdGD9krgjc0JxNU4Q7cu3zlYd&X-Amz-Signature=57ed5499baad10ac4bf937d35fd3d7df74bd8ea800b74f5a29754c29c926f132&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65SHDZP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBLwSeHthRnrhyuE%2BxGxhWqaSlqwhTUYRL2XY%2BI4BUyiAiAVolIOKytkYuDlhNI8rTEr031QM3B4K%2BrPuRo%2Fo7QsvSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMvOmAyoLq0EhoAOwYKtwD%2FIAhYNLVkyGy1XKe%2FQGgTyxGwyE1febjoTwPFEg16SxIJ1PjbgwB3f9ImRKtW2VK90%2FlrvF878H6V2Cchp9TvUHBGW2ERyzcEBW%2FNLFHKEjGFveci7pSETotjP5jGWxJDWY%2Fhgw9PHskFQK%2FaDr15spWkn7knYZohQneAOFgTgLjPoYLcs3MQ7cJqxic86G4nsiFbej5goInSXpsqcoRue80Tojq5tszVh0ocvNLfUxVynmLYl0kxa6PCGsxs2qv2q2EUGc6YNW%2FtAQRBGGPM%2Bun1Q9uYOf7Ttt2nFdDAJphQowrQuI8QjPxw7kpwMbJzltpLPt%2F0bWGM5yFYHjHQqwBHjcOE9dZ0cIxms20ssZOldkjWvfNl65YtfyT4R8BSrIeZPV0TS9QzpoLozxjLTXXNJrLtCboaeOtnGd6WtYmlCluwfxJAhKfyAZiZs0LFw2BxHJrmMLnV8hte63JNtgWzl7XW8KNsgxldpguYSuClaPbVNGCcbF3W3ceOFEj9GdmkhxqKZjz5zN6x6LVnoGOwg%2BBWKfTpg%2FmY1qneJlhbYyTFgMakoOBdIzIS%2BbjsoznH8l1ADUYDEFHKxsnL3gH%2FhRMteIKQCAurEw%2B2J9vUJf%2FgpvPrN3MOqYwiM%2FQywY6pgGnSvUYyd%2FuDnySIblBB5PBGsKG2NUIHLMB1paTgxjhZVsdREHYwIgnTUrr9xOwjnKuwrVRj0OBjgC%2Bcd5msYUwTQQ67C2E7lhbhVrkLRLPwe1tm9jbczzFI7ikY2Z5PJ9ocpHWTmba%2FLOx7sY40rOJIjuV1DrTdnovBdJKdKtxC%2FM%2B4y%2Bdv1%2BMat8pgowmnh1sC9WtdGD9krgjc0JxNU4Q7cu3zlYd&X-Amz-Signature=13b000216a2c0c893aff717daa00c449fb9620f3a01d475f22c7925c99f62a52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V65SHDZP%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIBLwSeHthRnrhyuE%2BxGxhWqaSlqwhTUYRL2XY%2BI4BUyiAiAVolIOKytkYuDlhNI8rTEr031QM3B4K%2BrPuRo%2Fo7QsvSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMvOmAyoLq0EhoAOwYKtwD%2FIAhYNLVkyGy1XKe%2FQGgTyxGwyE1febjoTwPFEg16SxIJ1PjbgwB3f9ImRKtW2VK90%2FlrvF878H6V2Cchp9TvUHBGW2ERyzcEBW%2FNLFHKEjGFveci7pSETotjP5jGWxJDWY%2Fhgw9PHskFQK%2FaDr15spWkn7knYZohQneAOFgTgLjPoYLcs3MQ7cJqxic86G4nsiFbej5goInSXpsqcoRue80Tojq5tszVh0ocvNLfUxVynmLYl0kxa6PCGsxs2qv2q2EUGc6YNW%2FtAQRBGGPM%2Bun1Q9uYOf7Ttt2nFdDAJphQowrQuI8QjPxw7kpwMbJzltpLPt%2F0bWGM5yFYHjHQqwBHjcOE9dZ0cIxms20ssZOldkjWvfNl65YtfyT4R8BSrIeZPV0TS9QzpoLozxjLTXXNJrLtCboaeOtnGd6WtYmlCluwfxJAhKfyAZiZs0LFw2BxHJrmMLnV8hte63JNtgWzl7XW8KNsgxldpguYSuClaPbVNGCcbF3W3ceOFEj9GdmkhxqKZjz5zN6x6LVnoGOwg%2BBWKfTpg%2FmY1qneJlhbYyTFgMakoOBdIzIS%2BbjsoznH8l1ADUYDEFHKxsnL3gH%2FhRMteIKQCAurEw%2B2J9vUJf%2FgpvPrN3MOqYwiM%2FQywY6pgGnSvUYyd%2FuDnySIblBB5PBGsKG2NUIHLMB1paTgxjhZVsdREHYwIgnTUrr9xOwjnKuwrVRj0OBjgC%2Bcd5msYUwTQQ67C2E7lhbhVrkLRLPwe1tm9jbczzFI7ikY2Z5PJ9ocpHWTmba%2FLOx7sY40rOJIjuV1DrTdnovBdJKdKtxC%2FM%2B4y%2Bdv1%2BMat8pgowmnh1sC9WtdGD9krgjc0JxNU4Q7cu3zlYd&X-Amz-Signature=3990a0fbf15351a2d82f4ebda094e6f8c21ce5f7103c834fb34050596c1b88ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

