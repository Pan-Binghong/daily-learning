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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WG47GE2%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSGZTUUt%2BMPyvPTyM6FfIbkDlCFXFl9xtei9t%2Bd0m%2F3wIhAMUHpOBqooaFkt%2FyrYKjpwshML5KYY%2F3IiU12brmM5qkKv8DCFsQABoMNjM3NDIzMTgzODA1Igz5VRknFzRlHvI8fBYq3AOA%2Bu4zToPP4BBa9FiSJlUXy%2FsW0bCfylR1Actlyr03UN4GVHJzSYIJsgVfsD%2BuAxhhtbXmMc5zZwgVtfxe5oGgJx09vVRAOiYqpSlUyB7WGAtZVSXjfQwmML9hiCUr8X%2FocobHh9%2BzezD7Ej4FzzAFn6eErOJc5o3SVJJnW5QUYScUsjKwMJohC4WRcTmHUC720rFzvMQZ8pV%2BN8PhvtjbKridMrPAOydAW8zKflNoR4vyKPtJwRaobfuT6tsJArgSQFPIgdAuUvsvyGQ5JjJBwkMoo0G0lvVM6ze1rY65Vyf37ortyELKGmvDhULYXazHcT23VgFJ7ObY7FRCW0Lq1bxsLiqMZqGp6NoMIemO5xfQVGmdJIQSIz2aFHAAFA%2BE0zKLoFSp4GvUsY%2FJVUE%2BcjyLl3UDqkqtGu36G7cnR5y6lJ74qYRA9u6NgJVL9D%2BmCxmdDRw5n9Y10QPWfmZ%2FiEITAw31hIahQPuTGVc%2BH1pn48iamqHovVsNxDwG%2FGxrojFYZPVD41jkz0nc7dmlCIDTJp8B4asgkjM17EdZJAlKX%2F53zDPd53kHKCT9%2BiclZBcEjfCYHsN%2FNckSGfHv5cqPTm5k%2B85Hqn5dHIFSCsRYD%2BQJ17%2FMGq3E3DDq0avLBjqkAcMNhp1ynCzKhY%2B09gyCfP1EToHAVc8Y%2BcbjGZvFHS%2BofUtMXAeEc7heXzOkMrAG3QzYgvHSrPBJ49pHiU1uro13Gq8kJXEzt1kSQjAe%2ByVHP6KTtZ%2BS3LD3epkb%2BVUUswzMwh%2Bxz7qZTMLEnHocE3xhPdVOb%2FNNTVk5U%2BP7KEBU2KGMgKcCrLBuxPqfhVHasDDeJFuO4xLyANPeFY3Udcd5RlgO&X-Amz-Signature=0ea396557d29b772f50c178450573b4d00f04fae0da4eaf19173674b976c74ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WG47GE2%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSGZTUUt%2BMPyvPTyM6FfIbkDlCFXFl9xtei9t%2Bd0m%2F3wIhAMUHpOBqooaFkt%2FyrYKjpwshML5KYY%2F3IiU12brmM5qkKv8DCFsQABoMNjM3NDIzMTgzODA1Igz5VRknFzRlHvI8fBYq3AOA%2Bu4zToPP4BBa9FiSJlUXy%2FsW0bCfylR1Actlyr03UN4GVHJzSYIJsgVfsD%2BuAxhhtbXmMc5zZwgVtfxe5oGgJx09vVRAOiYqpSlUyB7WGAtZVSXjfQwmML9hiCUr8X%2FocobHh9%2BzezD7Ej4FzzAFn6eErOJc5o3SVJJnW5QUYScUsjKwMJohC4WRcTmHUC720rFzvMQZ8pV%2BN8PhvtjbKridMrPAOydAW8zKflNoR4vyKPtJwRaobfuT6tsJArgSQFPIgdAuUvsvyGQ5JjJBwkMoo0G0lvVM6ze1rY65Vyf37ortyELKGmvDhULYXazHcT23VgFJ7ObY7FRCW0Lq1bxsLiqMZqGp6NoMIemO5xfQVGmdJIQSIz2aFHAAFA%2BE0zKLoFSp4GvUsY%2FJVUE%2BcjyLl3UDqkqtGu36G7cnR5y6lJ74qYRA9u6NgJVL9D%2BmCxmdDRw5n9Y10QPWfmZ%2FiEITAw31hIahQPuTGVc%2BH1pn48iamqHovVsNxDwG%2FGxrojFYZPVD41jkz0nc7dmlCIDTJp8B4asgkjM17EdZJAlKX%2F53zDPd53kHKCT9%2BiclZBcEjfCYHsN%2FNckSGfHv5cqPTm5k%2B85Hqn5dHIFSCsRYD%2BQJ17%2FMGq3E3DDq0avLBjqkAcMNhp1ynCzKhY%2B09gyCfP1EToHAVc8Y%2BcbjGZvFHS%2BofUtMXAeEc7heXzOkMrAG3QzYgvHSrPBJ49pHiU1uro13Gq8kJXEzt1kSQjAe%2ByVHP6KTtZ%2BS3LD3epkb%2BVUUswzMwh%2Bxz7qZTMLEnHocE3xhPdVOb%2FNNTVk5U%2BP7KEBU2KGMgKcCrLBuxPqfhVHasDDeJFuO4xLyANPeFY3Udcd5RlgO&X-Amz-Signature=60387e1532b30eee7681a18cdcc7ab4db960e2cde72eb85a7b9219d233894ebd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WG47GE2%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSGZTUUt%2BMPyvPTyM6FfIbkDlCFXFl9xtei9t%2Bd0m%2F3wIhAMUHpOBqooaFkt%2FyrYKjpwshML5KYY%2F3IiU12brmM5qkKv8DCFsQABoMNjM3NDIzMTgzODA1Igz5VRknFzRlHvI8fBYq3AOA%2Bu4zToPP4BBa9FiSJlUXy%2FsW0bCfylR1Actlyr03UN4GVHJzSYIJsgVfsD%2BuAxhhtbXmMc5zZwgVtfxe5oGgJx09vVRAOiYqpSlUyB7WGAtZVSXjfQwmML9hiCUr8X%2FocobHh9%2BzezD7Ej4FzzAFn6eErOJc5o3SVJJnW5QUYScUsjKwMJohC4WRcTmHUC720rFzvMQZ8pV%2BN8PhvtjbKridMrPAOydAW8zKflNoR4vyKPtJwRaobfuT6tsJArgSQFPIgdAuUvsvyGQ5JjJBwkMoo0G0lvVM6ze1rY65Vyf37ortyELKGmvDhULYXazHcT23VgFJ7ObY7FRCW0Lq1bxsLiqMZqGp6NoMIemO5xfQVGmdJIQSIz2aFHAAFA%2BE0zKLoFSp4GvUsY%2FJVUE%2BcjyLl3UDqkqtGu36G7cnR5y6lJ74qYRA9u6NgJVL9D%2BmCxmdDRw5n9Y10QPWfmZ%2FiEITAw31hIahQPuTGVc%2BH1pn48iamqHovVsNxDwG%2FGxrojFYZPVD41jkz0nc7dmlCIDTJp8B4asgkjM17EdZJAlKX%2F53zDPd53kHKCT9%2BiclZBcEjfCYHsN%2FNckSGfHv5cqPTm5k%2B85Hqn5dHIFSCsRYD%2BQJ17%2FMGq3E3DDq0avLBjqkAcMNhp1ynCzKhY%2B09gyCfP1EToHAVc8Y%2BcbjGZvFHS%2BofUtMXAeEc7heXzOkMrAG3QzYgvHSrPBJ49pHiU1uro13Gq8kJXEzt1kSQjAe%2ByVHP6KTtZ%2BS3LD3epkb%2BVUUswzMwh%2Bxz7qZTMLEnHocE3xhPdVOb%2FNNTVk5U%2BP7KEBU2KGMgKcCrLBuxPqfhVHasDDeJFuO4xLyANPeFY3Udcd5RlgO&X-Amz-Signature=77e2d22809366e1075330029eaa4674837f2c8d4c1dcd879e4f38a2d1ac69a93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WG47GE2%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSGZTUUt%2BMPyvPTyM6FfIbkDlCFXFl9xtei9t%2Bd0m%2F3wIhAMUHpOBqooaFkt%2FyrYKjpwshML5KYY%2F3IiU12brmM5qkKv8DCFsQABoMNjM3NDIzMTgzODA1Igz5VRknFzRlHvI8fBYq3AOA%2Bu4zToPP4BBa9FiSJlUXy%2FsW0bCfylR1Actlyr03UN4GVHJzSYIJsgVfsD%2BuAxhhtbXmMc5zZwgVtfxe5oGgJx09vVRAOiYqpSlUyB7WGAtZVSXjfQwmML9hiCUr8X%2FocobHh9%2BzezD7Ej4FzzAFn6eErOJc5o3SVJJnW5QUYScUsjKwMJohC4WRcTmHUC720rFzvMQZ8pV%2BN8PhvtjbKridMrPAOydAW8zKflNoR4vyKPtJwRaobfuT6tsJArgSQFPIgdAuUvsvyGQ5JjJBwkMoo0G0lvVM6ze1rY65Vyf37ortyELKGmvDhULYXazHcT23VgFJ7ObY7FRCW0Lq1bxsLiqMZqGp6NoMIemO5xfQVGmdJIQSIz2aFHAAFA%2BE0zKLoFSp4GvUsY%2FJVUE%2BcjyLl3UDqkqtGu36G7cnR5y6lJ74qYRA9u6NgJVL9D%2BmCxmdDRw5n9Y10QPWfmZ%2FiEITAw31hIahQPuTGVc%2BH1pn48iamqHovVsNxDwG%2FGxrojFYZPVD41jkz0nc7dmlCIDTJp8B4asgkjM17EdZJAlKX%2F53zDPd53kHKCT9%2BiclZBcEjfCYHsN%2FNckSGfHv5cqPTm5k%2B85Hqn5dHIFSCsRYD%2BQJ17%2FMGq3E3DDq0avLBjqkAcMNhp1ynCzKhY%2B09gyCfP1EToHAVc8Y%2BcbjGZvFHS%2BofUtMXAeEc7heXzOkMrAG3QzYgvHSrPBJ49pHiU1uro13Gq8kJXEzt1kSQjAe%2ByVHP6KTtZ%2BS3LD3epkb%2BVUUswzMwh%2Bxz7qZTMLEnHocE3xhPdVOb%2FNNTVk5U%2BP7KEBU2KGMgKcCrLBuxPqfhVHasDDeJFuO4xLyANPeFY3Udcd5RlgO&X-Amz-Signature=ca0cd1e6aea59a54ff16cfb0c51c97e1e97900024b6b3a25a65afb27cc8a4d97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WG47GE2%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSGZTUUt%2BMPyvPTyM6FfIbkDlCFXFl9xtei9t%2Bd0m%2F3wIhAMUHpOBqooaFkt%2FyrYKjpwshML5KYY%2F3IiU12brmM5qkKv8DCFsQABoMNjM3NDIzMTgzODA1Igz5VRknFzRlHvI8fBYq3AOA%2Bu4zToPP4BBa9FiSJlUXy%2FsW0bCfylR1Actlyr03UN4GVHJzSYIJsgVfsD%2BuAxhhtbXmMc5zZwgVtfxe5oGgJx09vVRAOiYqpSlUyB7WGAtZVSXjfQwmML9hiCUr8X%2FocobHh9%2BzezD7Ej4FzzAFn6eErOJc5o3SVJJnW5QUYScUsjKwMJohC4WRcTmHUC720rFzvMQZ8pV%2BN8PhvtjbKridMrPAOydAW8zKflNoR4vyKPtJwRaobfuT6tsJArgSQFPIgdAuUvsvyGQ5JjJBwkMoo0G0lvVM6ze1rY65Vyf37ortyELKGmvDhULYXazHcT23VgFJ7ObY7FRCW0Lq1bxsLiqMZqGp6NoMIemO5xfQVGmdJIQSIz2aFHAAFA%2BE0zKLoFSp4GvUsY%2FJVUE%2BcjyLl3UDqkqtGu36G7cnR5y6lJ74qYRA9u6NgJVL9D%2BmCxmdDRw5n9Y10QPWfmZ%2FiEITAw31hIahQPuTGVc%2BH1pn48iamqHovVsNxDwG%2FGxrojFYZPVD41jkz0nc7dmlCIDTJp8B4asgkjM17EdZJAlKX%2F53zDPd53kHKCT9%2BiclZBcEjfCYHsN%2FNckSGfHv5cqPTm5k%2B85Hqn5dHIFSCsRYD%2BQJ17%2FMGq3E3DDq0avLBjqkAcMNhp1ynCzKhY%2B09gyCfP1EToHAVc8Y%2BcbjGZvFHS%2BofUtMXAeEc7heXzOkMrAG3QzYgvHSrPBJ49pHiU1uro13Gq8kJXEzt1kSQjAe%2ByVHP6KTtZ%2BS3LD3epkb%2BVUUswzMwh%2Bxz7qZTMLEnHocE3xhPdVOb%2FNNTVk5U%2BP7KEBU2KGMgKcCrLBuxPqfhVHasDDeJFuO4xLyANPeFY3Udcd5RlgO&X-Amz-Signature=411e7a93a890bde2a95528f00dfa1f8be4c0b962c81b2dab249007e11876cfc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WG47GE2%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSGZTUUt%2BMPyvPTyM6FfIbkDlCFXFl9xtei9t%2Bd0m%2F3wIhAMUHpOBqooaFkt%2FyrYKjpwshML5KYY%2F3IiU12brmM5qkKv8DCFsQABoMNjM3NDIzMTgzODA1Igz5VRknFzRlHvI8fBYq3AOA%2Bu4zToPP4BBa9FiSJlUXy%2FsW0bCfylR1Actlyr03UN4GVHJzSYIJsgVfsD%2BuAxhhtbXmMc5zZwgVtfxe5oGgJx09vVRAOiYqpSlUyB7WGAtZVSXjfQwmML9hiCUr8X%2FocobHh9%2BzezD7Ej4FzzAFn6eErOJc5o3SVJJnW5QUYScUsjKwMJohC4WRcTmHUC720rFzvMQZ8pV%2BN8PhvtjbKridMrPAOydAW8zKflNoR4vyKPtJwRaobfuT6tsJArgSQFPIgdAuUvsvyGQ5JjJBwkMoo0G0lvVM6ze1rY65Vyf37ortyELKGmvDhULYXazHcT23VgFJ7ObY7FRCW0Lq1bxsLiqMZqGp6NoMIemO5xfQVGmdJIQSIz2aFHAAFA%2BE0zKLoFSp4GvUsY%2FJVUE%2BcjyLl3UDqkqtGu36G7cnR5y6lJ74qYRA9u6NgJVL9D%2BmCxmdDRw5n9Y10QPWfmZ%2FiEITAw31hIahQPuTGVc%2BH1pn48iamqHovVsNxDwG%2FGxrojFYZPVD41jkz0nc7dmlCIDTJp8B4asgkjM17EdZJAlKX%2F53zDPd53kHKCT9%2BiclZBcEjfCYHsN%2FNckSGfHv5cqPTm5k%2B85Hqn5dHIFSCsRYD%2BQJ17%2FMGq3E3DDq0avLBjqkAcMNhp1ynCzKhY%2B09gyCfP1EToHAVc8Y%2BcbjGZvFHS%2BofUtMXAeEc7heXzOkMrAG3QzYgvHSrPBJ49pHiU1uro13Gq8kJXEzt1kSQjAe%2ByVHP6KTtZ%2BS3LD3epkb%2BVUUswzMwh%2Bxz7qZTMLEnHocE3xhPdVOb%2FNNTVk5U%2BP7KEBU2KGMgKcCrLBuxPqfhVHasDDeJFuO4xLyANPeFY3Udcd5RlgO&X-Amz-Signature=0f453f9ebd1886a9bd195b1c6eacc280d32500599d38b8ea3772c7fa763235fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WG47GE2%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSGZTUUt%2BMPyvPTyM6FfIbkDlCFXFl9xtei9t%2Bd0m%2F3wIhAMUHpOBqooaFkt%2FyrYKjpwshML5KYY%2F3IiU12brmM5qkKv8DCFsQABoMNjM3NDIzMTgzODA1Igz5VRknFzRlHvI8fBYq3AOA%2Bu4zToPP4BBa9FiSJlUXy%2FsW0bCfylR1Actlyr03UN4GVHJzSYIJsgVfsD%2BuAxhhtbXmMc5zZwgVtfxe5oGgJx09vVRAOiYqpSlUyB7WGAtZVSXjfQwmML9hiCUr8X%2FocobHh9%2BzezD7Ej4FzzAFn6eErOJc5o3SVJJnW5QUYScUsjKwMJohC4WRcTmHUC720rFzvMQZ8pV%2BN8PhvtjbKridMrPAOydAW8zKflNoR4vyKPtJwRaobfuT6tsJArgSQFPIgdAuUvsvyGQ5JjJBwkMoo0G0lvVM6ze1rY65Vyf37ortyELKGmvDhULYXazHcT23VgFJ7ObY7FRCW0Lq1bxsLiqMZqGp6NoMIemO5xfQVGmdJIQSIz2aFHAAFA%2BE0zKLoFSp4GvUsY%2FJVUE%2BcjyLl3UDqkqtGu36G7cnR5y6lJ74qYRA9u6NgJVL9D%2BmCxmdDRw5n9Y10QPWfmZ%2FiEITAw31hIahQPuTGVc%2BH1pn48iamqHovVsNxDwG%2FGxrojFYZPVD41jkz0nc7dmlCIDTJp8B4asgkjM17EdZJAlKX%2F53zDPd53kHKCT9%2BiclZBcEjfCYHsN%2FNckSGfHv5cqPTm5k%2B85Hqn5dHIFSCsRYD%2BQJ17%2FMGq3E3DDq0avLBjqkAcMNhp1ynCzKhY%2B09gyCfP1EToHAVc8Y%2BcbjGZvFHS%2BofUtMXAeEc7heXzOkMrAG3QzYgvHSrPBJ49pHiU1uro13Gq8kJXEzt1kSQjAe%2ByVHP6KTtZ%2BS3LD3epkb%2BVUUswzMwh%2Bxz7qZTMLEnHocE3xhPdVOb%2FNNTVk5U%2BP7KEBU2KGMgKcCrLBuxPqfhVHasDDeJFuO4xLyANPeFY3Udcd5RlgO&X-Amz-Signature=738831ac12d5e7a6ab28d74b270c9af0c464c71075fc2de870f69faa5bafbf2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WG47GE2%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSGZTUUt%2BMPyvPTyM6FfIbkDlCFXFl9xtei9t%2Bd0m%2F3wIhAMUHpOBqooaFkt%2FyrYKjpwshML5KYY%2F3IiU12brmM5qkKv8DCFsQABoMNjM3NDIzMTgzODA1Igz5VRknFzRlHvI8fBYq3AOA%2Bu4zToPP4BBa9FiSJlUXy%2FsW0bCfylR1Actlyr03UN4GVHJzSYIJsgVfsD%2BuAxhhtbXmMc5zZwgVtfxe5oGgJx09vVRAOiYqpSlUyB7WGAtZVSXjfQwmML9hiCUr8X%2FocobHh9%2BzezD7Ej4FzzAFn6eErOJc5o3SVJJnW5QUYScUsjKwMJohC4WRcTmHUC720rFzvMQZ8pV%2BN8PhvtjbKridMrPAOydAW8zKflNoR4vyKPtJwRaobfuT6tsJArgSQFPIgdAuUvsvyGQ5JjJBwkMoo0G0lvVM6ze1rY65Vyf37ortyELKGmvDhULYXazHcT23VgFJ7ObY7FRCW0Lq1bxsLiqMZqGp6NoMIemO5xfQVGmdJIQSIz2aFHAAFA%2BE0zKLoFSp4GvUsY%2FJVUE%2BcjyLl3UDqkqtGu36G7cnR5y6lJ74qYRA9u6NgJVL9D%2BmCxmdDRw5n9Y10QPWfmZ%2FiEITAw31hIahQPuTGVc%2BH1pn48iamqHovVsNxDwG%2FGxrojFYZPVD41jkz0nc7dmlCIDTJp8B4asgkjM17EdZJAlKX%2F53zDPd53kHKCT9%2BiclZBcEjfCYHsN%2FNckSGfHv5cqPTm5k%2B85Hqn5dHIFSCsRYD%2BQJ17%2FMGq3E3DDq0avLBjqkAcMNhp1ynCzKhY%2B09gyCfP1EToHAVc8Y%2BcbjGZvFHS%2BofUtMXAeEc7heXzOkMrAG3QzYgvHSrPBJ49pHiU1uro13Gq8kJXEzt1kSQjAe%2ByVHP6KTtZ%2BS3LD3epkb%2BVUUswzMwh%2Bxz7qZTMLEnHocE3xhPdVOb%2FNNTVk5U%2BP7KEBU2KGMgKcCrLBuxPqfhVHasDDeJFuO4xLyANPeFY3Udcd5RlgO&X-Amz-Signature=4d8dc125a49ed44ed08c0d8b991d99b612805d5843466a4176b0b1aa3d3ac61e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WG47GE2%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSGZTUUt%2BMPyvPTyM6FfIbkDlCFXFl9xtei9t%2Bd0m%2F3wIhAMUHpOBqooaFkt%2FyrYKjpwshML5KYY%2F3IiU12brmM5qkKv8DCFsQABoMNjM3NDIzMTgzODA1Igz5VRknFzRlHvI8fBYq3AOA%2Bu4zToPP4BBa9FiSJlUXy%2FsW0bCfylR1Actlyr03UN4GVHJzSYIJsgVfsD%2BuAxhhtbXmMc5zZwgVtfxe5oGgJx09vVRAOiYqpSlUyB7WGAtZVSXjfQwmML9hiCUr8X%2FocobHh9%2BzezD7Ej4FzzAFn6eErOJc5o3SVJJnW5QUYScUsjKwMJohC4WRcTmHUC720rFzvMQZ8pV%2BN8PhvtjbKridMrPAOydAW8zKflNoR4vyKPtJwRaobfuT6tsJArgSQFPIgdAuUvsvyGQ5JjJBwkMoo0G0lvVM6ze1rY65Vyf37ortyELKGmvDhULYXazHcT23VgFJ7ObY7FRCW0Lq1bxsLiqMZqGp6NoMIemO5xfQVGmdJIQSIz2aFHAAFA%2BE0zKLoFSp4GvUsY%2FJVUE%2BcjyLl3UDqkqtGu36G7cnR5y6lJ74qYRA9u6NgJVL9D%2BmCxmdDRw5n9Y10QPWfmZ%2FiEITAw31hIahQPuTGVc%2BH1pn48iamqHovVsNxDwG%2FGxrojFYZPVD41jkz0nc7dmlCIDTJp8B4asgkjM17EdZJAlKX%2F53zDPd53kHKCT9%2BiclZBcEjfCYHsN%2FNckSGfHv5cqPTm5k%2B85Hqn5dHIFSCsRYD%2BQJ17%2FMGq3E3DDq0avLBjqkAcMNhp1ynCzKhY%2B09gyCfP1EToHAVc8Y%2BcbjGZvFHS%2BofUtMXAeEc7heXzOkMrAG3QzYgvHSrPBJ49pHiU1uro13Gq8kJXEzt1kSQjAe%2ByVHP6KTtZ%2BS3LD3epkb%2BVUUswzMwh%2Bxz7qZTMLEnHocE3xhPdVOb%2FNNTVk5U%2BP7KEBU2KGMgKcCrLBuxPqfhVHasDDeJFuO4xLyANPeFY3Udcd5RlgO&X-Amz-Signature=1cb2750f8729b99184471b22cb6bc090f63c59f45dde2e8a7ca1ee968f2066ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WG47GE2%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSGZTUUt%2BMPyvPTyM6FfIbkDlCFXFl9xtei9t%2Bd0m%2F3wIhAMUHpOBqooaFkt%2FyrYKjpwshML5KYY%2F3IiU12brmM5qkKv8DCFsQABoMNjM3NDIzMTgzODA1Igz5VRknFzRlHvI8fBYq3AOA%2Bu4zToPP4BBa9FiSJlUXy%2FsW0bCfylR1Actlyr03UN4GVHJzSYIJsgVfsD%2BuAxhhtbXmMc5zZwgVtfxe5oGgJx09vVRAOiYqpSlUyB7WGAtZVSXjfQwmML9hiCUr8X%2FocobHh9%2BzezD7Ej4FzzAFn6eErOJc5o3SVJJnW5QUYScUsjKwMJohC4WRcTmHUC720rFzvMQZ8pV%2BN8PhvtjbKridMrPAOydAW8zKflNoR4vyKPtJwRaobfuT6tsJArgSQFPIgdAuUvsvyGQ5JjJBwkMoo0G0lvVM6ze1rY65Vyf37ortyELKGmvDhULYXazHcT23VgFJ7ObY7FRCW0Lq1bxsLiqMZqGp6NoMIemO5xfQVGmdJIQSIz2aFHAAFA%2BE0zKLoFSp4GvUsY%2FJVUE%2BcjyLl3UDqkqtGu36G7cnR5y6lJ74qYRA9u6NgJVL9D%2BmCxmdDRw5n9Y10QPWfmZ%2FiEITAw31hIahQPuTGVc%2BH1pn48iamqHovVsNxDwG%2FGxrojFYZPVD41jkz0nc7dmlCIDTJp8B4asgkjM17EdZJAlKX%2F53zDPd53kHKCT9%2BiclZBcEjfCYHsN%2FNckSGfHv5cqPTm5k%2B85Hqn5dHIFSCsRYD%2BQJ17%2FMGq3E3DDq0avLBjqkAcMNhp1ynCzKhY%2B09gyCfP1EToHAVc8Y%2BcbjGZvFHS%2BofUtMXAeEc7heXzOkMrAG3QzYgvHSrPBJ49pHiU1uro13Gq8kJXEzt1kSQjAe%2ByVHP6KTtZ%2BS3LD3epkb%2BVUUswzMwh%2Bxz7qZTMLEnHocE3xhPdVOb%2FNNTVk5U%2BP7KEBU2KGMgKcCrLBuxPqfhVHasDDeJFuO4xLyANPeFY3Udcd5RlgO&X-Amz-Signature=74866f25d0adb65ad5ef4f66eae08d55ee7c2435debf146d5eeca45a82b0171e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

