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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATRPLS2%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeUMTodOJNZdCFmU7OWK3qKBGIh%2FJsKHNEpp%2FQAV6hAAiA9Nhc1Pj559inDBAZfV8%2BjP9tsyUlLANaCFAzLvnRFvir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM2ZsSKz4AYHjX%2BvFoKtwDCPQ5fF0GN1ZH%2Fd0Tv61aWnmVXdxf2I7ku2hrwNHNvx1qEgHkWqxAJyORKnjJHeGQ5%2BXu%2FZYzbxKLCoJS7lXpfk%2BP67G657H5J8aWj0Q3oWc9Gs1MZXY%2F8th9KXiRD0umzOsEPa%2FbmPgi%2BMwF0qwGmR%2BMKrU4ko5bcKkmRzt4cJZaNb6Tu5hrT1oxr%2B32n7%2F9xtoa9%2BVfUh2gizpNQB9Xqoh7erJd3sCws7Rz1afWzmNnOd4Ni6OpY5zY44HQWdJfy5o6XjrPne8nnCIZW2dtSLM8RGQsBrKvXYmiS0ezw%2FLAu7JYjWj7e5MB2nmTdCoNRybmYyC%2B7mRYHR4vFRjlLRQd%2BLzUV7zISDuTNiiuath2d5uUsCkjra2H601LBD2UY0yEzLqLa8hkPZm55ok0efNHlseZA1scE1rvFnWLUloNWBO%2Fy7Jp5m27UIIM0bS7C2UPHPusXWqh8mZcFLdPvrwv5B1XsmpiRSyyQnqMrYfHJyF56bAKrGp8xlOUzaa1kYEQxNUV9N2VvxT23Fc4mcgD5r92zYOthIvLgWND0j0HLZcC86mRSDhw364hPU8oRA3hABQKIKpenPtcmSNX57jToKzn7W2FVaJT8JOkihOoSmueyHJslifYMOwwlqfOyQY6pgHqg2KG7TIawIb5xU0WEuBTRkMVBcFomdoXlDdzGv1JYyaF%2BcWAjeNUDdiKUOsONKhLfubs%2F18%2BFKIAObjK9ELf9SNS7iO5tYzVnoSklp7Gtgvt7yeROU8kfarYGGWbKGLZxIAqs6B0kNLknmtKmupDXSb2ufBq0vMuq2Uwv8DKpARPJpYGgeMxPcTpfVN5KlmnOOHNDku0ziHNA5KU5rXqMvgvy8Jn&X-Amz-Signature=958520159866653b2d13f613ffad3304f0263fea6c0591ad97ad4b4ce77b41d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATRPLS2%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeUMTodOJNZdCFmU7OWK3qKBGIh%2FJsKHNEpp%2FQAV6hAAiA9Nhc1Pj559inDBAZfV8%2BjP9tsyUlLANaCFAzLvnRFvir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM2ZsSKz4AYHjX%2BvFoKtwDCPQ5fF0GN1ZH%2Fd0Tv61aWnmVXdxf2I7ku2hrwNHNvx1qEgHkWqxAJyORKnjJHeGQ5%2BXu%2FZYzbxKLCoJS7lXpfk%2BP67G657H5J8aWj0Q3oWc9Gs1MZXY%2F8th9KXiRD0umzOsEPa%2FbmPgi%2BMwF0qwGmR%2BMKrU4ko5bcKkmRzt4cJZaNb6Tu5hrT1oxr%2B32n7%2F9xtoa9%2BVfUh2gizpNQB9Xqoh7erJd3sCws7Rz1afWzmNnOd4Ni6OpY5zY44HQWdJfy5o6XjrPne8nnCIZW2dtSLM8RGQsBrKvXYmiS0ezw%2FLAu7JYjWj7e5MB2nmTdCoNRybmYyC%2B7mRYHR4vFRjlLRQd%2BLzUV7zISDuTNiiuath2d5uUsCkjra2H601LBD2UY0yEzLqLa8hkPZm55ok0efNHlseZA1scE1rvFnWLUloNWBO%2Fy7Jp5m27UIIM0bS7C2UPHPusXWqh8mZcFLdPvrwv5B1XsmpiRSyyQnqMrYfHJyF56bAKrGp8xlOUzaa1kYEQxNUV9N2VvxT23Fc4mcgD5r92zYOthIvLgWND0j0HLZcC86mRSDhw364hPU8oRA3hABQKIKpenPtcmSNX57jToKzn7W2FVaJT8JOkihOoSmueyHJslifYMOwwlqfOyQY6pgHqg2KG7TIawIb5xU0WEuBTRkMVBcFomdoXlDdzGv1JYyaF%2BcWAjeNUDdiKUOsONKhLfubs%2F18%2BFKIAObjK9ELf9SNS7iO5tYzVnoSklp7Gtgvt7yeROU8kfarYGGWbKGLZxIAqs6B0kNLknmtKmupDXSb2ufBq0vMuq2Uwv8DKpARPJpYGgeMxPcTpfVN5KlmnOOHNDku0ziHNA5KU5rXqMvgvy8Jn&X-Amz-Signature=4e96189ecf9fd7971c4edd071ac9f9a6b4494a7cd1615180926aad9cef2661ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATRPLS2%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeUMTodOJNZdCFmU7OWK3qKBGIh%2FJsKHNEpp%2FQAV6hAAiA9Nhc1Pj559inDBAZfV8%2BjP9tsyUlLANaCFAzLvnRFvir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM2ZsSKz4AYHjX%2BvFoKtwDCPQ5fF0GN1ZH%2Fd0Tv61aWnmVXdxf2I7ku2hrwNHNvx1qEgHkWqxAJyORKnjJHeGQ5%2BXu%2FZYzbxKLCoJS7lXpfk%2BP67G657H5J8aWj0Q3oWc9Gs1MZXY%2F8th9KXiRD0umzOsEPa%2FbmPgi%2BMwF0qwGmR%2BMKrU4ko5bcKkmRzt4cJZaNb6Tu5hrT1oxr%2B32n7%2F9xtoa9%2BVfUh2gizpNQB9Xqoh7erJd3sCws7Rz1afWzmNnOd4Ni6OpY5zY44HQWdJfy5o6XjrPne8nnCIZW2dtSLM8RGQsBrKvXYmiS0ezw%2FLAu7JYjWj7e5MB2nmTdCoNRybmYyC%2B7mRYHR4vFRjlLRQd%2BLzUV7zISDuTNiiuath2d5uUsCkjra2H601LBD2UY0yEzLqLa8hkPZm55ok0efNHlseZA1scE1rvFnWLUloNWBO%2Fy7Jp5m27UIIM0bS7C2UPHPusXWqh8mZcFLdPvrwv5B1XsmpiRSyyQnqMrYfHJyF56bAKrGp8xlOUzaa1kYEQxNUV9N2VvxT23Fc4mcgD5r92zYOthIvLgWND0j0HLZcC86mRSDhw364hPU8oRA3hABQKIKpenPtcmSNX57jToKzn7W2FVaJT8JOkihOoSmueyHJslifYMOwwlqfOyQY6pgHqg2KG7TIawIb5xU0WEuBTRkMVBcFomdoXlDdzGv1JYyaF%2BcWAjeNUDdiKUOsONKhLfubs%2F18%2BFKIAObjK9ELf9SNS7iO5tYzVnoSklp7Gtgvt7yeROU8kfarYGGWbKGLZxIAqs6B0kNLknmtKmupDXSb2ufBq0vMuq2Uwv8DKpARPJpYGgeMxPcTpfVN5KlmnOOHNDku0ziHNA5KU5rXqMvgvy8Jn&X-Amz-Signature=b8ba5bf11d95476a96f12c5714b3c5d4940d156a17a92102922d9048459aca12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATRPLS2%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeUMTodOJNZdCFmU7OWK3qKBGIh%2FJsKHNEpp%2FQAV6hAAiA9Nhc1Pj559inDBAZfV8%2BjP9tsyUlLANaCFAzLvnRFvir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM2ZsSKz4AYHjX%2BvFoKtwDCPQ5fF0GN1ZH%2Fd0Tv61aWnmVXdxf2I7ku2hrwNHNvx1qEgHkWqxAJyORKnjJHeGQ5%2BXu%2FZYzbxKLCoJS7lXpfk%2BP67G657H5J8aWj0Q3oWc9Gs1MZXY%2F8th9KXiRD0umzOsEPa%2FbmPgi%2BMwF0qwGmR%2BMKrU4ko5bcKkmRzt4cJZaNb6Tu5hrT1oxr%2B32n7%2F9xtoa9%2BVfUh2gizpNQB9Xqoh7erJd3sCws7Rz1afWzmNnOd4Ni6OpY5zY44HQWdJfy5o6XjrPne8nnCIZW2dtSLM8RGQsBrKvXYmiS0ezw%2FLAu7JYjWj7e5MB2nmTdCoNRybmYyC%2B7mRYHR4vFRjlLRQd%2BLzUV7zISDuTNiiuath2d5uUsCkjra2H601LBD2UY0yEzLqLa8hkPZm55ok0efNHlseZA1scE1rvFnWLUloNWBO%2Fy7Jp5m27UIIM0bS7C2UPHPusXWqh8mZcFLdPvrwv5B1XsmpiRSyyQnqMrYfHJyF56bAKrGp8xlOUzaa1kYEQxNUV9N2VvxT23Fc4mcgD5r92zYOthIvLgWND0j0HLZcC86mRSDhw364hPU8oRA3hABQKIKpenPtcmSNX57jToKzn7W2FVaJT8JOkihOoSmueyHJslifYMOwwlqfOyQY6pgHqg2KG7TIawIb5xU0WEuBTRkMVBcFomdoXlDdzGv1JYyaF%2BcWAjeNUDdiKUOsONKhLfubs%2F18%2BFKIAObjK9ELf9SNS7iO5tYzVnoSklp7Gtgvt7yeROU8kfarYGGWbKGLZxIAqs6B0kNLknmtKmupDXSb2ufBq0vMuq2Uwv8DKpARPJpYGgeMxPcTpfVN5KlmnOOHNDku0ziHNA5KU5rXqMvgvy8Jn&X-Amz-Signature=4d07c7550cd2e485c87634f2da45db6703200e6cba597904e7d4d50a6d01a28b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATRPLS2%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeUMTodOJNZdCFmU7OWK3qKBGIh%2FJsKHNEpp%2FQAV6hAAiA9Nhc1Pj559inDBAZfV8%2BjP9tsyUlLANaCFAzLvnRFvir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM2ZsSKz4AYHjX%2BvFoKtwDCPQ5fF0GN1ZH%2Fd0Tv61aWnmVXdxf2I7ku2hrwNHNvx1qEgHkWqxAJyORKnjJHeGQ5%2BXu%2FZYzbxKLCoJS7lXpfk%2BP67G657H5J8aWj0Q3oWc9Gs1MZXY%2F8th9KXiRD0umzOsEPa%2FbmPgi%2BMwF0qwGmR%2BMKrU4ko5bcKkmRzt4cJZaNb6Tu5hrT1oxr%2B32n7%2F9xtoa9%2BVfUh2gizpNQB9Xqoh7erJd3sCws7Rz1afWzmNnOd4Ni6OpY5zY44HQWdJfy5o6XjrPne8nnCIZW2dtSLM8RGQsBrKvXYmiS0ezw%2FLAu7JYjWj7e5MB2nmTdCoNRybmYyC%2B7mRYHR4vFRjlLRQd%2BLzUV7zISDuTNiiuath2d5uUsCkjra2H601LBD2UY0yEzLqLa8hkPZm55ok0efNHlseZA1scE1rvFnWLUloNWBO%2Fy7Jp5m27UIIM0bS7C2UPHPusXWqh8mZcFLdPvrwv5B1XsmpiRSyyQnqMrYfHJyF56bAKrGp8xlOUzaa1kYEQxNUV9N2VvxT23Fc4mcgD5r92zYOthIvLgWND0j0HLZcC86mRSDhw364hPU8oRA3hABQKIKpenPtcmSNX57jToKzn7W2FVaJT8JOkihOoSmueyHJslifYMOwwlqfOyQY6pgHqg2KG7TIawIb5xU0WEuBTRkMVBcFomdoXlDdzGv1JYyaF%2BcWAjeNUDdiKUOsONKhLfubs%2F18%2BFKIAObjK9ELf9SNS7iO5tYzVnoSklp7Gtgvt7yeROU8kfarYGGWbKGLZxIAqs6B0kNLknmtKmupDXSb2ufBq0vMuq2Uwv8DKpARPJpYGgeMxPcTpfVN5KlmnOOHNDku0ziHNA5KU5rXqMvgvy8Jn&X-Amz-Signature=be8e37cabcafa36e8455b55c95828c8a178beac9174077a7dd19a16c903ff88c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATRPLS2%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeUMTodOJNZdCFmU7OWK3qKBGIh%2FJsKHNEpp%2FQAV6hAAiA9Nhc1Pj559inDBAZfV8%2BjP9tsyUlLANaCFAzLvnRFvir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM2ZsSKz4AYHjX%2BvFoKtwDCPQ5fF0GN1ZH%2Fd0Tv61aWnmVXdxf2I7ku2hrwNHNvx1qEgHkWqxAJyORKnjJHeGQ5%2BXu%2FZYzbxKLCoJS7lXpfk%2BP67G657H5J8aWj0Q3oWc9Gs1MZXY%2F8th9KXiRD0umzOsEPa%2FbmPgi%2BMwF0qwGmR%2BMKrU4ko5bcKkmRzt4cJZaNb6Tu5hrT1oxr%2B32n7%2F9xtoa9%2BVfUh2gizpNQB9Xqoh7erJd3sCws7Rz1afWzmNnOd4Ni6OpY5zY44HQWdJfy5o6XjrPne8nnCIZW2dtSLM8RGQsBrKvXYmiS0ezw%2FLAu7JYjWj7e5MB2nmTdCoNRybmYyC%2B7mRYHR4vFRjlLRQd%2BLzUV7zISDuTNiiuath2d5uUsCkjra2H601LBD2UY0yEzLqLa8hkPZm55ok0efNHlseZA1scE1rvFnWLUloNWBO%2Fy7Jp5m27UIIM0bS7C2UPHPusXWqh8mZcFLdPvrwv5B1XsmpiRSyyQnqMrYfHJyF56bAKrGp8xlOUzaa1kYEQxNUV9N2VvxT23Fc4mcgD5r92zYOthIvLgWND0j0HLZcC86mRSDhw364hPU8oRA3hABQKIKpenPtcmSNX57jToKzn7W2FVaJT8JOkihOoSmueyHJslifYMOwwlqfOyQY6pgHqg2KG7TIawIb5xU0WEuBTRkMVBcFomdoXlDdzGv1JYyaF%2BcWAjeNUDdiKUOsONKhLfubs%2F18%2BFKIAObjK9ELf9SNS7iO5tYzVnoSklp7Gtgvt7yeROU8kfarYGGWbKGLZxIAqs6B0kNLknmtKmupDXSb2ufBq0vMuq2Uwv8DKpARPJpYGgeMxPcTpfVN5KlmnOOHNDku0ziHNA5KU5rXqMvgvy8Jn&X-Amz-Signature=1555b4b724b268b40496b0737cc8b616cb371d8cc1c70954a3e192bd4416ebb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATRPLS2%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeUMTodOJNZdCFmU7OWK3qKBGIh%2FJsKHNEpp%2FQAV6hAAiA9Nhc1Pj559inDBAZfV8%2BjP9tsyUlLANaCFAzLvnRFvir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM2ZsSKz4AYHjX%2BvFoKtwDCPQ5fF0GN1ZH%2Fd0Tv61aWnmVXdxf2I7ku2hrwNHNvx1qEgHkWqxAJyORKnjJHeGQ5%2BXu%2FZYzbxKLCoJS7lXpfk%2BP67G657H5J8aWj0Q3oWc9Gs1MZXY%2F8th9KXiRD0umzOsEPa%2FbmPgi%2BMwF0qwGmR%2BMKrU4ko5bcKkmRzt4cJZaNb6Tu5hrT1oxr%2B32n7%2F9xtoa9%2BVfUh2gizpNQB9Xqoh7erJd3sCws7Rz1afWzmNnOd4Ni6OpY5zY44HQWdJfy5o6XjrPne8nnCIZW2dtSLM8RGQsBrKvXYmiS0ezw%2FLAu7JYjWj7e5MB2nmTdCoNRybmYyC%2B7mRYHR4vFRjlLRQd%2BLzUV7zISDuTNiiuath2d5uUsCkjra2H601LBD2UY0yEzLqLa8hkPZm55ok0efNHlseZA1scE1rvFnWLUloNWBO%2Fy7Jp5m27UIIM0bS7C2UPHPusXWqh8mZcFLdPvrwv5B1XsmpiRSyyQnqMrYfHJyF56bAKrGp8xlOUzaa1kYEQxNUV9N2VvxT23Fc4mcgD5r92zYOthIvLgWND0j0HLZcC86mRSDhw364hPU8oRA3hABQKIKpenPtcmSNX57jToKzn7W2FVaJT8JOkihOoSmueyHJslifYMOwwlqfOyQY6pgHqg2KG7TIawIb5xU0WEuBTRkMVBcFomdoXlDdzGv1JYyaF%2BcWAjeNUDdiKUOsONKhLfubs%2F18%2BFKIAObjK9ELf9SNS7iO5tYzVnoSklp7Gtgvt7yeROU8kfarYGGWbKGLZxIAqs6B0kNLknmtKmupDXSb2ufBq0vMuq2Uwv8DKpARPJpYGgeMxPcTpfVN5KlmnOOHNDku0ziHNA5KU5rXqMvgvy8Jn&X-Amz-Signature=e464db5c2d0fbaff58e88cccd9079b7e270d88b5cfe0e066b3cb779d9149abac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATRPLS2%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeUMTodOJNZdCFmU7OWK3qKBGIh%2FJsKHNEpp%2FQAV6hAAiA9Nhc1Pj559inDBAZfV8%2BjP9tsyUlLANaCFAzLvnRFvir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM2ZsSKz4AYHjX%2BvFoKtwDCPQ5fF0GN1ZH%2Fd0Tv61aWnmVXdxf2I7ku2hrwNHNvx1qEgHkWqxAJyORKnjJHeGQ5%2BXu%2FZYzbxKLCoJS7lXpfk%2BP67G657H5J8aWj0Q3oWc9Gs1MZXY%2F8th9KXiRD0umzOsEPa%2FbmPgi%2BMwF0qwGmR%2BMKrU4ko5bcKkmRzt4cJZaNb6Tu5hrT1oxr%2B32n7%2F9xtoa9%2BVfUh2gizpNQB9Xqoh7erJd3sCws7Rz1afWzmNnOd4Ni6OpY5zY44HQWdJfy5o6XjrPne8nnCIZW2dtSLM8RGQsBrKvXYmiS0ezw%2FLAu7JYjWj7e5MB2nmTdCoNRybmYyC%2B7mRYHR4vFRjlLRQd%2BLzUV7zISDuTNiiuath2d5uUsCkjra2H601LBD2UY0yEzLqLa8hkPZm55ok0efNHlseZA1scE1rvFnWLUloNWBO%2Fy7Jp5m27UIIM0bS7C2UPHPusXWqh8mZcFLdPvrwv5B1XsmpiRSyyQnqMrYfHJyF56bAKrGp8xlOUzaa1kYEQxNUV9N2VvxT23Fc4mcgD5r92zYOthIvLgWND0j0HLZcC86mRSDhw364hPU8oRA3hABQKIKpenPtcmSNX57jToKzn7W2FVaJT8JOkihOoSmueyHJslifYMOwwlqfOyQY6pgHqg2KG7TIawIb5xU0WEuBTRkMVBcFomdoXlDdzGv1JYyaF%2BcWAjeNUDdiKUOsONKhLfubs%2F18%2BFKIAObjK9ELf9SNS7iO5tYzVnoSklp7Gtgvt7yeROU8kfarYGGWbKGLZxIAqs6B0kNLknmtKmupDXSb2ufBq0vMuq2Uwv8DKpARPJpYGgeMxPcTpfVN5KlmnOOHNDku0ziHNA5KU5rXqMvgvy8Jn&X-Amz-Signature=134287b18e0531677c8af03a422edb66b13f543c27da7f11b8f8770f266bd98e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATRPLS2%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeUMTodOJNZdCFmU7OWK3qKBGIh%2FJsKHNEpp%2FQAV6hAAiA9Nhc1Pj559inDBAZfV8%2BjP9tsyUlLANaCFAzLvnRFvir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM2ZsSKz4AYHjX%2BvFoKtwDCPQ5fF0GN1ZH%2Fd0Tv61aWnmVXdxf2I7ku2hrwNHNvx1qEgHkWqxAJyORKnjJHeGQ5%2BXu%2FZYzbxKLCoJS7lXpfk%2BP67G657H5J8aWj0Q3oWc9Gs1MZXY%2F8th9KXiRD0umzOsEPa%2FbmPgi%2BMwF0qwGmR%2BMKrU4ko5bcKkmRzt4cJZaNb6Tu5hrT1oxr%2B32n7%2F9xtoa9%2BVfUh2gizpNQB9Xqoh7erJd3sCws7Rz1afWzmNnOd4Ni6OpY5zY44HQWdJfy5o6XjrPne8nnCIZW2dtSLM8RGQsBrKvXYmiS0ezw%2FLAu7JYjWj7e5MB2nmTdCoNRybmYyC%2B7mRYHR4vFRjlLRQd%2BLzUV7zISDuTNiiuath2d5uUsCkjra2H601LBD2UY0yEzLqLa8hkPZm55ok0efNHlseZA1scE1rvFnWLUloNWBO%2Fy7Jp5m27UIIM0bS7C2UPHPusXWqh8mZcFLdPvrwv5B1XsmpiRSyyQnqMrYfHJyF56bAKrGp8xlOUzaa1kYEQxNUV9N2VvxT23Fc4mcgD5r92zYOthIvLgWND0j0HLZcC86mRSDhw364hPU8oRA3hABQKIKpenPtcmSNX57jToKzn7W2FVaJT8JOkihOoSmueyHJslifYMOwwlqfOyQY6pgHqg2KG7TIawIb5xU0WEuBTRkMVBcFomdoXlDdzGv1JYyaF%2BcWAjeNUDdiKUOsONKhLfubs%2F18%2BFKIAObjK9ELf9SNS7iO5tYzVnoSklp7Gtgvt7yeROU8kfarYGGWbKGLZxIAqs6B0kNLknmtKmupDXSb2ufBq0vMuq2Uwv8DKpARPJpYGgeMxPcTpfVN5KlmnOOHNDku0ziHNA5KU5rXqMvgvy8Jn&X-Amz-Signature=7428a7901a4587eada62fe91d63a01ab696a4346e3e8eae8cfc88992f7b77ac4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATRPLS2%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeUMTodOJNZdCFmU7OWK3qKBGIh%2FJsKHNEpp%2FQAV6hAAiA9Nhc1Pj559inDBAZfV8%2BjP9tsyUlLANaCFAzLvnRFvir%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM2ZsSKz4AYHjX%2BvFoKtwDCPQ5fF0GN1ZH%2Fd0Tv61aWnmVXdxf2I7ku2hrwNHNvx1qEgHkWqxAJyORKnjJHeGQ5%2BXu%2FZYzbxKLCoJS7lXpfk%2BP67G657H5J8aWj0Q3oWc9Gs1MZXY%2F8th9KXiRD0umzOsEPa%2FbmPgi%2BMwF0qwGmR%2BMKrU4ko5bcKkmRzt4cJZaNb6Tu5hrT1oxr%2B32n7%2F9xtoa9%2BVfUh2gizpNQB9Xqoh7erJd3sCws7Rz1afWzmNnOd4Ni6OpY5zY44HQWdJfy5o6XjrPne8nnCIZW2dtSLM8RGQsBrKvXYmiS0ezw%2FLAu7JYjWj7e5MB2nmTdCoNRybmYyC%2B7mRYHR4vFRjlLRQd%2BLzUV7zISDuTNiiuath2d5uUsCkjra2H601LBD2UY0yEzLqLa8hkPZm55ok0efNHlseZA1scE1rvFnWLUloNWBO%2Fy7Jp5m27UIIM0bS7C2UPHPusXWqh8mZcFLdPvrwv5B1XsmpiRSyyQnqMrYfHJyF56bAKrGp8xlOUzaa1kYEQxNUV9N2VvxT23Fc4mcgD5r92zYOthIvLgWND0j0HLZcC86mRSDhw364hPU8oRA3hABQKIKpenPtcmSNX57jToKzn7W2FVaJT8JOkihOoSmueyHJslifYMOwwlqfOyQY6pgHqg2KG7TIawIb5xU0WEuBTRkMVBcFomdoXlDdzGv1JYyaF%2BcWAjeNUDdiKUOsONKhLfubs%2F18%2BFKIAObjK9ELf9SNS7iO5tYzVnoSklp7Gtgvt7yeROU8kfarYGGWbKGLZxIAqs6B0kNLknmtKmupDXSb2ufBq0vMuq2Uwv8DKpARPJpYGgeMxPcTpfVN5KlmnOOHNDku0ziHNA5KU5rXqMvgvy8Jn&X-Amz-Signature=e263acbab92b24eb04baa6f3e01f965e2cab250a45735d1502617dd3d4cff646&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

