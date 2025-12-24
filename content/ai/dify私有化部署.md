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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5MND5K6%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCV3aKS1N8HPUYRndTAFgvjwkYbqvwVDghkGXPVz9fXfwIhAM1aiJotiuGCHVtXgpwAnWp07WbLMdv%2FmcIT%2B%2BOvUzSlKv8DCBkQABoMNjM3NDIzMTgzODA1IgxrTKgdUTKrec9eivMq3AMk%2BTIWn%2BQfbtX6PTNCrBt%2BNbrJK5cbe0eoBflYVlL1dMSU8XKyNXK6STX2qKu7BtwpbdXZUA%2FiCSR5rgYUmy59hbsqdRJSjWBXhBZ9qNPf52ANAyBs9eSscwA9rYRYd7%2FWaEoUmPGF5HDCNggXfQqLZ8DxUVWYEek1kUQHQ6Xcri4RlprtL6eNir7%2BBEoYmyhKOIIBLKT6RWq9Dww4VgwW2UL4rNtvJtn%2Fv%2BH3desBOGqK3UpjFpY918jG5jFt4pubRVBkT8GB%2FYaDDFvH14%2F%2F0zilWB3QXbsukyFka6vYlX7moERm2BIFYPLYgzgmUYteMJhP3WyjJSWaO1DKJsHriRABs8jFdgpvJ1DFA35BmpqyceBNIbecJ5gTR28cnL%2F474hkJmysYP%2FqgIWzDJuqBVwxBFqTXZME%2FBqQDeCK2zTKl%2FygNUZ1hPtS28GjGXG3lK2TqoGE4e4Ak91DUA6Sf25vPOHyC7ffozhVsKMGZEF99UgT7A11N4BDLdiPSLghXjwkqJAwyYQcUXQJHa6sRbX58uP5Rtnr2LBPF7PAR88%2Bzm28H0fB%2B8jHj%2BkVFlJ52L%2BTSVqY0YU4JIN07eWu%2F8GA2jDlO0daQqkoGNfZ6JnDauznHK%2FSImYkujDH4KzKBjqkAYa43tTKhIoq5%2BjThvVhfcc1Qm8L%2FLqu1BRB6U%2FEK%2BekIHOzeruHAwlrFRokQIVqL3mzYnXljPqm3KB4M4c3mwyEO8XZbqDN0Imy92SsG%2BanXRrqGMdwI0QAMUvxPV1uwMUrFsx4cCXlxdjR2HtJAgCS%2B%2BzzyNwLXtR30iXUqNqUIojuhn7%2F5sjHXuYdkejmC6ktI4MW3upGPXQDo1f1Ns62F1ZR&X-Amz-Signature=b41920c53ff13156c9c363db3fc21d91a3d3ebed87163ee35264865f0a4797d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5MND5K6%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCV3aKS1N8HPUYRndTAFgvjwkYbqvwVDghkGXPVz9fXfwIhAM1aiJotiuGCHVtXgpwAnWp07WbLMdv%2FmcIT%2B%2BOvUzSlKv8DCBkQABoMNjM3NDIzMTgzODA1IgxrTKgdUTKrec9eivMq3AMk%2BTIWn%2BQfbtX6PTNCrBt%2BNbrJK5cbe0eoBflYVlL1dMSU8XKyNXK6STX2qKu7BtwpbdXZUA%2FiCSR5rgYUmy59hbsqdRJSjWBXhBZ9qNPf52ANAyBs9eSscwA9rYRYd7%2FWaEoUmPGF5HDCNggXfQqLZ8DxUVWYEek1kUQHQ6Xcri4RlprtL6eNir7%2BBEoYmyhKOIIBLKT6RWq9Dww4VgwW2UL4rNtvJtn%2Fv%2BH3desBOGqK3UpjFpY918jG5jFt4pubRVBkT8GB%2FYaDDFvH14%2F%2F0zilWB3QXbsukyFka6vYlX7moERm2BIFYPLYgzgmUYteMJhP3WyjJSWaO1DKJsHriRABs8jFdgpvJ1DFA35BmpqyceBNIbecJ5gTR28cnL%2F474hkJmysYP%2FqgIWzDJuqBVwxBFqTXZME%2FBqQDeCK2zTKl%2FygNUZ1hPtS28GjGXG3lK2TqoGE4e4Ak91DUA6Sf25vPOHyC7ffozhVsKMGZEF99UgT7A11N4BDLdiPSLghXjwkqJAwyYQcUXQJHa6sRbX58uP5Rtnr2LBPF7PAR88%2Bzm28H0fB%2B8jHj%2BkVFlJ52L%2BTSVqY0YU4JIN07eWu%2F8GA2jDlO0daQqkoGNfZ6JnDauznHK%2FSImYkujDH4KzKBjqkAYa43tTKhIoq5%2BjThvVhfcc1Qm8L%2FLqu1BRB6U%2FEK%2BekIHOzeruHAwlrFRokQIVqL3mzYnXljPqm3KB4M4c3mwyEO8XZbqDN0Imy92SsG%2BanXRrqGMdwI0QAMUvxPV1uwMUrFsx4cCXlxdjR2HtJAgCS%2B%2BzzyNwLXtR30iXUqNqUIojuhn7%2F5sjHXuYdkejmC6ktI4MW3upGPXQDo1f1Ns62F1ZR&X-Amz-Signature=943048bfe5cb53fb8decc6bc6bfd64515cda1f619d56dbdacee97f4d11a75e98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5MND5K6%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCV3aKS1N8HPUYRndTAFgvjwkYbqvwVDghkGXPVz9fXfwIhAM1aiJotiuGCHVtXgpwAnWp07WbLMdv%2FmcIT%2B%2BOvUzSlKv8DCBkQABoMNjM3NDIzMTgzODA1IgxrTKgdUTKrec9eivMq3AMk%2BTIWn%2BQfbtX6PTNCrBt%2BNbrJK5cbe0eoBflYVlL1dMSU8XKyNXK6STX2qKu7BtwpbdXZUA%2FiCSR5rgYUmy59hbsqdRJSjWBXhBZ9qNPf52ANAyBs9eSscwA9rYRYd7%2FWaEoUmPGF5HDCNggXfQqLZ8DxUVWYEek1kUQHQ6Xcri4RlprtL6eNir7%2BBEoYmyhKOIIBLKT6RWq9Dww4VgwW2UL4rNtvJtn%2Fv%2BH3desBOGqK3UpjFpY918jG5jFt4pubRVBkT8GB%2FYaDDFvH14%2F%2F0zilWB3QXbsukyFka6vYlX7moERm2BIFYPLYgzgmUYteMJhP3WyjJSWaO1DKJsHriRABs8jFdgpvJ1DFA35BmpqyceBNIbecJ5gTR28cnL%2F474hkJmysYP%2FqgIWzDJuqBVwxBFqTXZME%2FBqQDeCK2zTKl%2FygNUZ1hPtS28GjGXG3lK2TqoGE4e4Ak91DUA6Sf25vPOHyC7ffozhVsKMGZEF99UgT7A11N4BDLdiPSLghXjwkqJAwyYQcUXQJHa6sRbX58uP5Rtnr2LBPF7PAR88%2Bzm28H0fB%2B8jHj%2BkVFlJ52L%2BTSVqY0YU4JIN07eWu%2F8GA2jDlO0daQqkoGNfZ6JnDauznHK%2FSImYkujDH4KzKBjqkAYa43tTKhIoq5%2BjThvVhfcc1Qm8L%2FLqu1BRB6U%2FEK%2BekIHOzeruHAwlrFRokQIVqL3mzYnXljPqm3KB4M4c3mwyEO8XZbqDN0Imy92SsG%2BanXRrqGMdwI0QAMUvxPV1uwMUrFsx4cCXlxdjR2HtJAgCS%2B%2BzzyNwLXtR30iXUqNqUIojuhn7%2F5sjHXuYdkejmC6ktI4MW3upGPXQDo1f1Ns62F1ZR&X-Amz-Signature=53a40750ea8b4b91c754e76d13ae869e806a0d561ffba11ee28e8772bfc86da5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5MND5K6%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCV3aKS1N8HPUYRndTAFgvjwkYbqvwVDghkGXPVz9fXfwIhAM1aiJotiuGCHVtXgpwAnWp07WbLMdv%2FmcIT%2B%2BOvUzSlKv8DCBkQABoMNjM3NDIzMTgzODA1IgxrTKgdUTKrec9eivMq3AMk%2BTIWn%2BQfbtX6PTNCrBt%2BNbrJK5cbe0eoBflYVlL1dMSU8XKyNXK6STX2qKu7BtwpbdXZUA%2FiCSR5rgYUmy59hbsqdRJSjWBXhBZ9qNPf52ANAyBs9eSscwA9rYRYd7%2FWaEoUmPGF5HDCNggXfQqLZ8DxUVWYEek1kUQHQ6Xcri4RlprtL6eNir7%2BBEoYmyhKOIIBLKT6RWq9Dww4VgwW2UL4rNtvJtn%2Fv%2BH3desBOGqK3UpjFpY918jG5jFt4pubRVBkT8GB%2FYaDDFvH14%2F%2F0zilWB3QXbsukyFka6vYlX7moERm2BIFYPLYgzgmUYteMJhP3WyjJSWaO1DKJsHriRABs8jFdgpvJ1DFA35BmpqyceBNIbecJ5gTR28cnL%2F474hkJmysYP%2FqgIWzDJuqBVwxBFqTXZME%2FBqQDeCK2zTKl%2FygNUZ1hPtS28GjGXG3lK2TqoGE4e4Ak91DUA6Sf25vPOHyC7ffozhVsKMGZEF99UgT7A11N4BDLdiPSLghXjwkqJAwyYQcUXQJHa6sRbX58uP5Rtnr2LBPF7PAR88%2Bzm28H0fB%2B8jHj%2BkVFlJ52L%2BTSVqY0YU4JIN07eWu%2F8GA2jDlO0daQqkoGNfZ6JnDauznHK%2FSImYkujDH4KzKBjqkAYa43tTKhIoq5%2BjThvVhfcc1Qm8L%2FLqu1BRB6U%2FEK%2BekIHOzeruHAwlrFRokQIVqL3mzYnXljPqm3KB4M4c3mwyEO8XZbqDN0Imy92SsG%2BanXRrqGMdwI0QAMUvxPV1uwMUrFsx4cCXlxdjR2HtJAgCS%2B%2BzzyNwLXtR30iXUqNqUIojuhn7%2F5sjHXuYdkejmC6ktI4MW3upGPXQDo1f1Ns62F1ZR&X-Amz-Signature=0e7dbf0db46f33681859cb22f1a22e4621688a4f3493bf122c8bb4f7fa498477&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5MND5K6%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCV3aKS1N8HPUYRndTAFgvjwkYbqvwVDghkGXPVz9fXfwIhAM1aiJotiuGCHVtXgpwAnWp07WbLMdv%2FmcIT%2B%2BOvUzSlKv8DCBkQABoMNjM3NDIzMTgzODA1IgxrTKgdUTKrec9eivMq3AMk%2BTIWn%2BQfbtX6PTNCrBt%2BNbrJK5cbe0eoBflYVlL1dMSU8XKyNXK6STX2qKu7BtwpbdXZUA%2FiCSR5rgYUmy59hbsqdRJSjWBXhBZ9qNPf52ANAyBs9eSscwA9rYRYd7%2FWaEoUmPGF5HDCNggXfQqLZ8DxUVWYEek1kUQHQ6Xcri4RlprtL6eNir7%2BBEoYmyhKOIIBLKT6RWq9Dww4VgwW2UL4rNtvJtn%2Fv%2BH3desBOGqK3UpjFpY918jG5jFt4pubRVBkT8GB%2FYaDDFvH14%2F%2F0zilWB3QXbsukyFka6vYlX7moERm2BIFYPLYgzgmUYteMJhP3WyjJSWaO1DKJsHriRABs8jFdgpvJ1DFA35BmpqyceBNIbecJ5gTR28cnL%2F474hkJmysYP%2FqgIWzDJuqBVwxBFqTXZME%2FBqQDeCK2zTKl%2FygNUZ1hPtS28GjGXG3lK2TqoGE4e4Ak91DUA6Sf25vPOHyC7ffozhVsKMGZEF99UgT7A11N4BDLdiPSLghXjwkqJAwyYQcUXQJHa6sRbX58uP5Rtnr2LBPF7PAR88%2Bzm28H0fB%2B8jHj%2BkVFlJ52L%2BTSVqY0YU4JIN07eWu%2F8GA2jDlO0daQqkoGNfZ6JnDauznHK%2FSImYkujDH4KzKBjqkAYa43tTKhIoq5%2BjThvVhfcc1Qm8L%2FLqu1BRB6U%2FEK%2BekIHOzeruHAwlrFRokQIVqL3mzYnXljPqm3KB4M4c3mwyEO8XZbqDN0Imy92SsG%2BanXRrqGMdwI0QAMUvxPV1uwMUrFsx4cCXlxdjR2HtJAgCS%2B%2BzzyNwLXtR30iXUqNqUIojuhn7%2F5sjHXuYdkejmC6ktI4MW3upGPXQDo1f1Ns62F1ZR&X-Amz-Signature=ddeb58951d8f16f17274145727bc6be37a828bb3eedd6ac80d807e8f164b9292&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5MND5K6%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCV3aKS1N8HPUYRndTAFgvjwkYbqvwVDghkGXPVz9fXfwIhAM1aiJotiuGCHVtXgpwAnWp07WbLMdv%2FmcIT%2B%2BOvUzSlKv8DCBkQABoMNjM3NDIzMTgzODA1IgxrTKgdUTKrec9eivMq3AMk%2BTIWn%2BQfbtX6PTNCrBt%2BNbrJK5cbe0eoBflYVlL1dMSU8XKyNXK6STX2qKu7BtwpbdXZUA%2FiCSR5rgYUmy59hbsqdRJSjWBXhBZ9qNPf52ANAyBs9eSscwA9rYRYd7%2FWaEoUmPGF5HDCNggXfQqLZ8DxUVWYEek1kUQHQ6Xcri4RlprtL6eNir7%2BBEoYmyhKOIIBLKT6RWq9Dww4VgwW2UL4rNtvJtn%2Fv%2BH3desBOGqK3UpjFpY918jG5jFt4pubRVBkT8GB%2FYaDDFvH14%2F%2F0zilWB3QXbsukyFka6vYlX7moERm2BIFYPLYgzgmUYteMJhP3WyjJSWaO1DKJsHriRABs8jFdgpvJ1DFA35BmpqyceBNIbecJ5gTR28cnL%2F474hkJmysYP%2FqgIWzDJuqBVwxBFqTXZME%2FBqQDeCK2zTKl%2FygNUZ1hPtS28GjGXG3lK2TqoGE4e4Ak91DUA6Sf25vPOHyC7ffozhVsKMGZEF99UgT7A11N4BDLdiPSLghXjwkqJAwyYQcUXQJHa6sRbX58uP5Rtnr2LBPF7PAR88%2Bzm28H0fB%2B8jHj%2BkVFlJ52L%2BTSVqY0YU4JIN07eWu%2F8GA2jDlO0daQqkoGNfZ6JnDauznHK%2FSImYkujDH4KzKBjqkAYa43tTKhIoq5%2BjThvVhfcc1Qm8L%2FLqu1BRB6U%2FEK%2BekIHOzeruHAwlrFRokQIVqL3mzYnXljPqm3KB4M4c3mwyEO8XZbqDN0Imy92SsG%2BanXRrqGMdwI0QAMUvxPV1uwMUrFsx4cCXlxdjR2HtJAgCS%2B%2BzzyNwLXtR30iXUqNqUIojuhn7%2F5sjHXuYdkejmC6ktI4MW3upGPXQDo1f1Ns62F1ZR&X-Amz-Signature=c374b0fb483ea92e349787e0cb8fb4f9385e20e025dd0166a8ceb561ff86c84c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5MND5K6%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCV3aKS1N8HPUYRndTAFgvjwkYbqvwVDghkGXPVz9fXfwIhAM1aiJotiuGCHVtXgpwAnWp07WbLMdv%2FmcIT%2B%2BOvUzSlKv8DCBkQABoMNjM3NDIzMTgzODA1IgxrTKgdUTKrec9eivMq3AMk%2BTIWn%2BQfbtX6PTNCrBt%2BNbrJK5cbe0eoBflYVlL1dMSU8XKyNXK6STX2qKu7BtwpbdXZUA%2FiCSR5rgYUmy59hbsqdRJSjWBXhBZ9qNPf52ANAyBs9eSscwA9rYRYd7%2FWaEoUmPGF5HDCNggXfQqLZ8DxUVWYEek1kUQHQ6Xcri4RlprtL6eNir7%2BBEoYmyhKOIIBLKT6RWq9Dww4VgwW2UL4rNtvJtn%2Fv%2BH3desBOGqK3UpjFpY918jG5jFt4pubRVBkT8GB%2FYaDDFvH14%2F%2F0zilWB3QXbsukyFka6vYlX7moERm2BIFYPLYgzgmUYteMJhP3WyjJSWaO1DKJsHriRABs8jFdgpvJ1DFA35BmpqyceBNIbecJ5gTR28cnL%2F474hkJmysYP%2FqgIWzDJuqBVwxBFqTXZME%2FBqQDeCK2zTKl%2FygNUZ1hPtS28GjGXG3lK2TqoGE4e4Ak91DUA6Sf25vPOHyC7ffozhVsKMGZEF99UgT7A11N4BDLdiPSLghXjwkqJAwyYQcUXQJHa6sRbX58uP5Rtnr2LBPF7PAR88%2Bzm28H0fB%2B8jHj%2BkVFlJ52L%2BTSVqY0YU4JIN07eWu%2F8GA2jDlO0daQqkoGNfZ6JnDauznHK%2FSImYkujDH4KzKBjqkAYa43tTKhIoq5%2BjThvVhfcc1Qm8L%2FLqu1BRB6U%2FEK%2BekIHOzeruHAwlrFRokQIVqL3mzYnXljPqm3KB4M4c3mwyEO8XZbqDN0Imy92SsG%2BanXRrqGMdwI0QAMUvxPV1uwMUrFsx4cCXlxdjR2HtJAgCS%2B%2BzzyNwLXtR30iXUqNqUIojuhn7%2F5sjHXuYdkejmC6ktI4MW3upGPXQDo1f1Ns62F1ZR&X-Amz-Signature=038043d5f1f170a3e46f0568d9cb9c8376a3a3b13159e859485a97f82938a738&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5MND5K6%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCV3aKS1N8HPUYRndTAFgvjwkYbqvwVDghkGXPVz9fXfwIhAM1aiJotiuGCHVtXgpwAnWp07WbLMdv%2FmcIT%2B%2BOvUzSlKv8DCBkQABoMNjM3NDIzMTgzODA1IgxrTKgdUTKrec9eivMq3AMk%2BTIWn%2BQfbtX6PTNCrBt%2BNbrJK5cbe0eoBflYVlL1dMSU8XKyNXK6STX2qKu7BtwpbdXZUA%2FiCSR5rgYUmy59hbsqdRJSjWBXhBZ9qNPf52ANAyBs9eSscwA9rYRYd7%2FWaEoUmPGF5HDCNggXfQqLZ8DxUVWYEek1kUQHQ6Xcri4RlprtL6eNir7%2BBEoYmyhKOIIBLKT6RWq9Dww4VgwW2UL4rNtvJtn%2Fv%2BH3desBOGqK3UpjFpY918jG5jFt4pubRVBkT8GB%2FYaDDFvH14%2F%2F0zilWB3QXbsukyFka6vYlX7moERm2BIFYPLYgzgmUYteMJhP3WyjJSWaO1DKJsHriRABs8jFdgpvJ1DFA35BmpqyceBNIbecJ5gTR28cnL%2F474hkJmysYP%2FqgIWzDJuqBVwxBFqTXZME%2FBqQDeCK2zTKl%2FygNUZ1hPtS28GjGXG3lK2TqoGE4e4Ak91DUA6Sf25vPOHyC7ffozhVsKMGZEF99UgT7A11N4BDLdiPSLghXjwkqJAwyYQcUXQJHa6sRbX58uP5Rtnr2LBPF7PAR88%2Bzm28H0fB%2B8jHj%2BkVFlJ52L%2BTSVqY0YU4JIN07eWu%2F8GA2jDlO0daQqkoGNfZ6JnDauznHK%2FSImYkujDH4KzKBjqkAYa43tTKhIoq5%2BjThvVhfcc1Qm8L%2FLqu1BRB6U%2FEK%2BekIHOzeruHAwlrFRokQIVqL3mzYnXljPqm3KB4M4c3mwyEO8XZbqDN0Imy92SsG%2BanXRrqGMdwI0QAMUvxPV1uwMUrFsx4cCXlxdjR2HtJAgCS%2B%2BzzyNwLXtR30iXUqNqUIojuhn7%2F5sjHXuYdkejmC6ktI4MW3upGPXQDo1f1Ns62F1ZR&X-Amz-Signature=71936ac6cb434c88e5fba802041ff396c5aeb840d997dc65db8c51ffe5d722c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5MND5K6%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCV3aKS1N8HPUYRndTAFgvjwkYbqvwVDghkGXPVz9fXfwIhAM1aiJotiuGCHVtXgpwAnWp07WbLMdv%2FmcIT%2B%2BOvUzSlKv8DCBkQABoMNjM3NDIzMTgzODA1IgxrTKgdUTKrec9eivMq3AMk%2BTIWn%2BQfbtX6PTNCrBt%2BNbrJK5cbe0eoBflYVlL1dMSU8XKyNXK6STX2qKu7BtwpbdXZUA%2FiCSR5rgYUmy59hbsqdRJSjWBXhBZ9qNPf52ANAyBs9eSscwA9rYRYd7%2FWaEoUmPGF5HDCNggXfQqLZ8DxUVWYEek1kUQHQ6Xcri4RlprtL6eNir7%2BBEoYmyhKOIIBLKT6RWq9Dww4VgwW2UL4rNtvJtn%2Fv%2BH3desBOGqK3UpjFpY918jG5jFt4pubRVBkT8GB%2FYaDDFvH14%2F%2F0zilWB3QXbsukyFka6vYlX7moERm2BIFYPLYgzgmUYteMJhP3WyjJSWaO1DKJsHriRABs8jFdgpvJ1DFA35BmpqyceBNIbecJ5gTR28cnL%2F474hkJmysYP%2FqgIWzDJuqBVwxBFqTXZME%2FBqQDeCK2zTKl%2FygNUZ1hPtS28GjGXG3lK2TqoGE4e4Ak91DUA6Sf25vPOHyC7ffozhVsKMGZEF99UgT7A11N4BDLdiPSLghXjwkqJAwyYQcUXQJHa6sRbX58uP5Rtnr2LBPF7PAR88%2Bzm28H0fB%2B8jHj%2BkVFlJ52L%2BTSVqY0YU4JIN07eWu%2F8GA2jDlO0daQqkoGNfZ6JnDauznHK%2FSImYkujDH4KzKBjqkAYa43tTKhIoq5%2BjThvVhfcc1Qm8L%2FLqu1BRB6U%2FEK%2BekIHOzeruHAwlrFRokQIVqL3mzYnXljPqm3KB4M4c3mwyEO8XZbqDN0Imy92SsG%2BanXRrqGMdwI0QAMUvxPV1uwMUrFsx4cCXlxdjR2HtJAgCS%2B%2BzzyNwLXtR30iXUqNqUIojuhn7%2F5sjHXuYdkejmC6ktI4MW3upGPXQDo1f1Ns62F1ZR&X-Amz-Signature=ada972399217710df16c44b3cfb69bc46578b765774aef711aa5613cf0d86254&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5MND5K6%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCV3aKS1N8HPUYRndTAFgvjwkYbqvwVDghkGXPVz9fXfwIhAM1aiJotiuGCHVtXgpwAnWp07WbLMdv%2FmcIT%2B%2BOvUzSlKv8DCBkQABoMNjM3NDIzMTgzODA1IgxrTKgdUTKrec9eivMq3AMk%2BTIWn%2BQfbtX6PTNCrBt%2BNbrJK5cbe0eoBflYVlL1dMSU8XKyNXK6STX2qKu7BtwpbdXZUA%2FiCSR5rgYUmy59hbsqdRJSjWBXhBZ9qNPf52ANAyBs9eSscwA9rYRYd7%2FWaEoUmPGF5HDCNggXfQqLZ8DxUVWYEek1kUQHQ6Xcri4RlprtL6eNir7%2BBEoYmyhKOIIBLKT6RWq9Dww4VgwW2UL4rNtvJtn%2Fv%2BH3desBOGqK3UpjFpY918jG5jFt4pubRVBkT8GB%2FYaDDFvH14%2F%2F0zilWB3QXbsukyFka6vYlX7moERm2BIFYPLYgzgmUYteMJhP3WyjJSWaO1DKJsHriRABs8jFdgpvJ1DFA35BmpqyceBNIbecJ5gTR28cnL%2F474hkJmysYP%2FqgIWzDJuqBVwxBFqTXZME%2FBqQDeCK2zTKl%2FygNUZ1hPtS28GjGXG3lK2TqoGE4e4Ak91DUA6Sf25vPOHyC7ffozhVsKMGZEF99UgT7A11N4BDLdiPSLghXjwkqJAwyYQcUXQJHa6sRbX58uP5Rtnr2LBPF7PAR88%2Bzm28H0fB%2B8jHj%2BkVFlJ52L%2BTSVqY0YU4JIN07eWu%2F8GA2jDlO0daQqkoGNfZ6JnDauznHK%2FSImYkujDH4KzKBjqkAYa43tTKhIoq5%2BjThvVhfcc1Qm8L%2FLqu1BRB6U%2FEK%2BekIHOzeruHAwlrFRokQIVqL3mzYnXljPqm3KB4M4c3mwyEO8XZbqDN0Imy92SsG%2BanXRrqGMdwI0QAMUvxPV1uwMUrFsx4cCXlxdjR2HtJAgCS%2B%2BzzyNwLXtR30iXUqNqUIojuhn7%2F5sjHXuYdkejmC6ktI4MW3upGPXQDo1f1Ns62F1ZR&X-Amz-Signature=729a6e52840c036b9f0d4f4d75f8f6133a1e363307b8b3d8a3fea6038b4a8a12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

