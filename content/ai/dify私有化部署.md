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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XACRYF%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNdZ13GXNWaS6H6gP%2B%2Fyye9PJ34TrEFUhTt0rV6R5j0QIgCoMQijy37jIQ87muJ6GCBFKsC%2BctI%2FRjFdddgup%2FCgIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMe7LhwppHzcg%2FrlFCrcA%2B4mdhMEYvVBF1trR3r0Fr%2Bs0T1run1%2FrmypQlGyLWhmaeXVKxr%2FBUvGYjGufOkSojW%2Fkj9NjinV4jK15CoMT%2BckQV3N%2BjotUB9LIf6zZDAo7D3yASRLmiE2FqApi0jPDg6N33vFcWtW6nsFDxcPOWjz3GpLYXQI%2BDj8hv3j7tVbPptFWkBmrcFnZz04dauC3lYb%2FlUEwc8oPjqmELsPuk%2FEy99scQ0boDzAnBMPKUvvO5A836SNw6y11KftWetg%2B2%2Bv5Pl9VtgtxfS3ysRNsejaCWIFX6SkmI4KQSv%2FKi1h5V5ZLr7V4j%2Fgi%2FKvzmr28QtLjqRmy4O03h0G83zqABNvzxSiylWXcOx8gxQ1hXjKSWnwOW0fDHSkmhsVWA6%2FX4tzppJWM1x%2Fjr5jIhDr51%2Fzq%2BNJAeInUVofGY%2BH%2FdOsRjnDcA5pW5avYPdNpKiDCnCJL6auZb31oH%2B3ZYkkEZfW7tSrrA7eaItDfEuY9MaO25vFPdhOPlzEDfu%2FKjPUdRspXrfQUR5YOuJ0%2BwXsPqeWi9sZjOWMn1oFK%2BdhCyf0NmeyFgfMj24GuxSzuKfgyXCAajmNhOa10CaRlCJC%2F0w4JVKIzHQJlrBD0O4FaHJub4rOulvJDUQd44%2BRMP%2B85MwGOqUBdc52hyw5Pt2tnNufI8i%2FtEOxT8XpphfDg4RtTUlD8GGQxRIQ%2FQVI%2BssJEYyqFKIcjuxKAcEPonOpZB2G8hq0E9MgHdSZt3kFc1%2BtNZPeRb%2FDn2X6Jb2HrJP6dv3eQ26qaMnLLoisXFKXXCnIxFIDUeHFZnV5%2B2JzZifIIAyerAYDmN1HoYuSJpoAND89B3NEp%2BzvvvoQBDabXVQCxKbCRrl1IQxX&X-Amz-Signature=538e5cf4a5fd35b9d5d9329ea7ee9893183b5488dd4cc32bbbc751134e7daeb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XACRYF%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNdZ13GXNWaS6H6gP%2B%2Fyye9PJ34TrEFUhTt0rV6R5j0QIgCoMQijy37jIQ87muJ6GCBFKsC%2BctI%2FRjFdddgup%2FCgIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMe7LhwppHzcg%2FrlFCrcA%2B4mdhMEYvVBF1trR3r0Fr%2Bs0T1run1%2FrmypQlGyLWhmaeXVKxr%2FBUvGYjGufOkSojW%2Fkj9NjinV4jK15CoMT%2BckQV3N%2BjotUB9LIf6zZDAo7D3yASRLmiE2FqApi0jPDg6N33vFcWtW6nsFDxcPOWjz3GpLYXQI%2BDj8hv3j7tVbPptFWkBmrcFnZz04dauC3lYb%2FlUEwc8oPjqmELsPuk%2FEy99scQ0boDzAnBMPKUvvO5A836SNw6y11KftWetg%2B2%2Bv5Pl9VtgtxfS3ysRNsejaCWIFX6SkmI4KQSv%2FKi1h5V5ZLr7V4j%2Fgi%2FKvzmr28QtLjqRmy4O03h0G83zqABNvzxSiylWXcOx8gxQ1hXjKSWnwOW0fDHSkmhsVWA6%2FX4tzppJWM1x%2Fjr5jIhDr51%2Fzq%2BNJAeInUVofGY%2BH%2FdOsRjnDcA5pW5avYPdNpKiDCnCJL6auZb31oH%2B3ZYkkEZfW7tSrrA7eaItDfEuY9MaO25vFPdhOPlzEDfu%2FKjPUdRspXrfQUR5YOuJ0%2BwXsPqeWi9sZjOWMn1oFK%2BdhCyf0NmeyFgfMj24GuxSzuKfgyXCAajmNhOa10CaRlCJC%2F0w4JVKIzHQJlrBD0O4FaHJub4rOulvJDUQd44%2BRMP%2B85MwGOqUBdc52hyw5Pt2tnNufI8i%2FtEOxT8XpphfDg4RtTUlD8GGQxRIQ%2FQVI%2BssJEYyqFKIcjuxKAcEPonOpZB2G8hq0E9MgHdSZt3kFc1%2BtNZPeRb%2FDn2X6Jb2HrJP6dv3eQ26qaMnLLoisXFKXXCnIxFIDUeHFZnV5%2B2JzZifIIAyerAYDmN1HoYuSJpoAND89B3NEp%2BzvvvoQBDabXVQCxKbCRrl1IQxX&X-Amz-Signature=d97051b35de43b8ce5524e467b8d858db305c3801e11f95037ef1c0ba1041ac9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XACRYF%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNdZ13GXNWaS6H6gP%2B%2Fyye9PJ34TrEFUhTt0rV6R5j0QIgCoMQijy37jIQ87muJ6GCBFKsC%2BctI%2FRjFdddgup%2FCgIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMe7LhwppHzcg%2FrlFCrcA%2B4mdhMEYvVBF1trR3r0Fr%2Bs0T1run1%2FrmypQlGyLWhmaeXVKxr%2FBUvGYjGufOkSojW%2Fkj9NjinV4jK15CoMT%2BckQV3N%2BjotUB9LIf6zZDAo7D3yASRLmiE2FqApi0jPDg6N33vFcWtW6nsFDxcPOWjz3GpLYXQI%2BDj8hv3j7tVbPptFWkBmrcFnZz04dauC3lYb%2FlUEwc8oPjqmELsPuk%2FEy99scQ0boDzAnBMPKUvvO5A836SNw6y11KftWetg%2B2%2Bv5Pl9VtgtxfS3ysRNsejaCWIFX6SkmI4KQSv%2FKi1h5V5ZLr7V4j%2Fgi%2FKvzmr28QtLjqRmy4O03h0G83zqABNvzxSiylWXcOx8gxQ1hXjKSWnwOW0fDHSkmhsVWA6%2FX4tzppJWM1x%2Fjr5jIhDr51%2Fzq%2BNJAeInUVofGY%2BH%2FdOsRjnDcA5pW5avYPdNpKiDCnCJL6auZb31oH%2B3ZYkkEZfW7tSrrA7eaItDfEuY9MaO25vFPdhOPlzEDfu%2FKjPUdRspXrfQUR5YOuJ0%2BwXsPqeWi9sZjOWMn1oFK%2BdhCyf0NmeyFgfMj24GuxSzuKfgyXCAajmNhOa10CaRlCJC%2F0w4JVKIzHQJlrBD0O4FaHJub4rOulvJDUQd44%2BRMP%2B85MwGOqUBdc52hyw5Pt2tnNufI8i%2FtEOxT8XpphfDg4RtTUlD8GGQxRIQ%2FQVI%2BssJEYyqFKIcjuxKAcEPonOpZB2G8hq0E9MgHdSZt3kFc1%2BtNZPeRb%2FDn2X6Jb2HrJP6dv3eQ26qaMnLLoisXFKXXCnIxFIDUeHFZnV5%2B2JzZifIIAyerAYDmN1HoYuSJpoAND89B3NEp%2BzvvvoQBDabXVQCxKbCRrl1IQxX&X-Amz-Signature=3246b41d2b183e55fa0d54f818600862376e07647615d38d36a29bcec8f2f438&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XACRYF%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNdZ13GXNWaS6H6gP%2B%2Fyye9PJ34TrEFUhTt0rV6R5j0QIgCoMQijy37jIQ87muJ6GCBFKsC%2BctI%2FRjFdddgup%2FCgIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMe7LhwppHzcg%2FrlFCrcA%2B4mdhMEYvVBF1trR3r0Fr%2Bs0T1run1%2FrmypQlGyLWhmaeXVKxr%2FBUvGYjGufOkSojW%2Fkj9NjinV4jK15CoMT%2BckQV3N%2BjotUB9LIf6zZDAo7D3yASRLmiE2FqApi0jPDg6N33vFcWtW6nsFDxcPOWjz3GpLYXQI%2BDj8hv3j7tVbPptFWkBmrcFnZz04dauC3lYb%2FlUEwc8oPjqmELsPuk%2FEy99scQ0boDzAnBMPKUvvO5A836SNw6y11KftWetg%2B2%2Bv5Pl9VtgtxfS3ysRNsejaCWIFX6SkmI4KQSv%2FKi1h5V5ZLr7V4j%2Fgi%2FKvzmr28QtLjqRmy4O03h0G83zqABNvzxSiylWXcOx8gxQ1hXjKSWnwOW0fDHSkmhsVWA6%2FX4tzppJWM1x%2Fjr5jIhDr51%2Fzq%2BNJAeInUVofGY%2BH%2FdOsRjnDcA5pW5avYPdNpKiDCnCJL6auZb31oH%2B3ZYkkEZfW7tSrrA7eaItDfEuY9MaO25vFPdhOPlzEDfu%2FKjPUdRspXrfQUR5YOuJ0%2BwXsPqeWi9sZjOWMn1oFK%2BdhCyf0NmeyFgfMj24GuxSzuKfgyXCAajmNhOa10CaRlCJC%2F0w4JVKIzHQJlrBD0O4FaHJub4rOulvJDUQd44%2BRMP%2B85MwGOqUBdc52hyw5Pt2tnNufI8i%2FtEOxT8XpphfDg4RtTUlD8GGQxRIQ%2FQVI%2BssJEYyqFKIcjuxKAcEPonOpZB2G8hq0E9MgHdSZt3kFc1%2BtNZPeRb%2FDn2X6Jb2HrJP6dv3eQ26qaMnLLoisXFKXXCnIxFIDUeHFZnV5%2B2JzZifIIAyerAYDmN1HoYuSJpoAND89B3NEp%2BzvvvoQBDabXVQCxKbCRrl1IQxX&X-Amz-Signature=6e9a7a9fa44758d49f0d896f85f408a7300322c6173c5a0b3b3a5a66c037ab8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XACRYF%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNdZ13GXNWaS6H6gP%2B%2Fyye9PJ34TrEFUhTt0rV6R5j0QIgCoMQijy37jIQ87muJ6GCBFKsC%2BctI%2FRjFdddgup%2FCgIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMe7LhwppHzcg%2FrlFCrcA%2B4mdhMEYvVBF1trR3r0Fr%2Bs0T1run1%2FrmypQlGyLWhmaeXVKxr%2FBUvGYjGufOkSojW%2Fkj9NjinV4jK15CoMT%2BckQV3N%2BjotUB9LIf6zZDAo7D3yASRLmiE2FqApi0jPDg6N33vFcWtW6nsFDxcPOWjz3GpLYXQI%2BDj8hv3j7tVbPptFWkBmrcFnZz04dauC3lYb%2FlUEwc8oPjqmELsPuk%2FEy99scQ0boDzAnBMPKUvvO5A836SNw6y11KftWetg%2B2%2Bv5Pl9VtgtxfS3ysRNsejaCWIFX6SkmI4KQSv%2FKi1h5V5ZLr7V4j%2Fgi%2FKvzmr28QtLjqRmy4O03h0G83zqABNvzxSiylWXcOx8gxQ1hXjKSWnwOW0fDHSkmhsVWA6%2FX4tzppJWM1x%2Fjr5jIhDr51%2Fzq%2BNJAeInUVofGY%2BH%2FdOsRjnDcA5pW5avYPdNpKiDCnCJL6auZb31oH%2B3ZYkkEZfW7tSrrA7eaItDfEuY9MaO25vFPdhOPlzEDfu%2FKjPUdRspXrfQUR5YOuJ0%2BwXsPqeWi9sZjOWMn1oFK%2BdhCyf0NmeyFgfMj24GuxSzuKfgyXCAajmNhOa10CaRlCJC%2F0w4JVKIzHQJlrBD0O4FaHJub4rOulvJDUQd44%2BRMP%2B85MwGOqUBdc52hyw5Pt2tnNufI8i%2FtEOxT8XpphfDg4RtTUlD8GGQxRIQ%2FQVI%2BssJEYyqFKIcjuxKAcEPonOpZB2G8hq0E9MgHdSZt3kFc1%2BtNZPeRb%2FDn2X6Jb2HrJP6dv3eQ26qaMnLLoisXFKXXCnIxFIDUeHFZnV5%2B2JzZifIIAyerAYDmN1HoYuSJpoAND89B3NEp%2BzvvvoQBDabXVQCxKbCRrl1IQxX&X-Amz-Signature=c7e7f98af019f81eb4195b460b72efbbe076f90550a4cdb1372137da3f396612&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XACRYF%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNdZ13GXNWaS6H6gP%2B%2Fyye9PJ34TrEFUhTt0rV6R5j0QIgCoMQijy37jIQ87muJ6GCBFKsC%2BctI%2FRjFdddgup%2FCgIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMe7LhwppHzcg%2FrlFCrcA%2B4mdhMEYvVBF1trR3r0Fr%2Bs0T1run1%2FrmypQlGyLWhmaeXVKxr%2FBUvGYjGufOkSojW%2Fkj9NjinV4jK15CoMT%2BckQV3N%2BjotUB9LIf6zZDAo7D3yASRLmiE2FqApi0jPDg6N33vFcWtW6nsFDxcPOWjz3GpLYXQI%2BDj8hv3j7tVbPptFWkBmrcFnZz04dauC3lYb%2FlUEwc8oPjqmELsPuk%2FEy99scQ0boDzAnBMPKUvvO5A836SNw6y11KftWetg%2B2%2Bv5Pl9VtgtxfS3ysRNsejaCWIFX6SkmI4KQSv%2FKi1h5V5ZLr7V4j%2Fgi%2FKvzmr28QtLjqRmy4O03h0G83zqABNvzxSiylWXcOx8gxQ1hXjKSWnwOW0fDHSkmhsVWA6%2FX4tzppJWM1x%2Fjr5jIhDr51%2Fzq%2BNJAeInUVofGY%2BH%2FdOsRjnDcA5pW5avYPdNpKiDCnCJL6auZb31oH%2B3ZYkkEZfW7tSrrA7eaItDfEuY9MaO25vFPdhOPlzEDfu%2FKjPUdRspXrfQUR5YOuJ0%2BwXsPqeWi9sZjOWMn1oFK%2BdhCyf0NmeyFgfMj24GuxSzuKfgyXCAajmNhOa10CaRlCJC%2F0w4JVKIzHQJlrBD0O4FaHJub4rOulvJDUQd44%2BRMP%2B85MwGOqUBdc52hyw5Pt2tnNufI8i%2FtEOxT8XpphfDg4RtTUlD8GGQxRIQ%2FQVI%2BssJEYyqFKIcjuxKAcEPonOpZB2G8hq0E9MgHdSZt3kFc1%2BtNZPeRb%2FDn2X6Jb2HrJP6dv3eQ26qaMnLLoisXFKXXCnIxFIDUeHFZnV5%2B2JzZifIIAyerAYDmN1HoYuSJpoAND89B3NEp%2BzvvvoQBDabXVQCxKbCRrl1IQxX&X-Amz-Signature=8e7cefe4418258428c738bda6398daad79288a99324e49e5074ad13a36001a4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XACRYF%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNdZ13GXNWaS6H6gP%2B%2Fyye9PJ34TrEFUhTt0rV6R5j0QIgCoMQijy37jIQ87muJ6GCBFKsC%2BctI%2FRjFdddgup%2FCgIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMe7LhwppHzcg%2FrlFCrcA%2B4mdhMEYvVBF1trR3r0Fr%2Bs0T1run1%2FrmypQlGyLWhmaeXVKxr%2FBUvGYjGufOkSojW%2Fkj9NjinV4jK15CoMT%2BckQV3N%2BjotUB9LIf6zZDAo7D3yASRLmiE2FqApi0jPDg6N33vFcWtW6nsFDxcPOWjz3GpLYXQI%2BDj8hv3j7tVbPptFWkBmrcFnZz04dauC3lYb%2FlUEwc8oPjqmELsPuk%2FEy99scQ0boDzAnBMPKUvvO5A836SNw6y11KftWetg%2B2%2Bv5Pl9VtgtxfS3ysRNsejaCWIFX6SkmI4KQSv%2FKi1h5V5ZLr7V4j%2Fgi%2FKvzmr28QtLjqRmy4O03h0G83zqABNvzxSiylWXcOx8gxQ1hXjKSWnwOW0fDHSkmhsVWA6%2FX4tzppJWM1x%2Fjr5jIhDr51%2Fzq%2BNJAeInUVofGY%2BH%2FdOsRjnDcA5pW5avYPdNpKiDCnCJL6auZb31oH%2B3ZYkkEZfW7tSrrA7eaItDfEuY9MaO25vFPdhOPlzEDfu%2FKjPUdRspXrfQUR5YOuJ0%2BwXsPqeWi9sZjOWMn1oFK%2BdhCyf0NmeyFgfMj24GuxSzuKfgyXCAajmNhOa10CaRlCJC%2F0w4JVKIzHQJlrBD0O4FaHJub4rOulvJDUQd44%2BRMP%2B85MwGOqUBdc52hyw5Pt2tnNufI8i%2FtEOxT8XpphfDg4RtTUlD8GGQxRIQ%2FQVI%2BssJEYyqFKIcjuxKAcEPonOpZB2G8hq0E9MgHdSZt3kFc1%2BtNZPeRb%2FDn2X6Jb2HrJP6dv3eQ26qaMnLLoisXFKXXCnIxFIDUeHFZnV5%2B2JzZifIIAyerAYDmN1HoYuSJpoAND89B3NEp%2BzvvvoQBDabXVQCxKbCRrl1IQxX&X-Amz-Signature=2c6769b4b65f0ce959b661fbcbb8481a778efaa107d7a03ee57b7c2f9263fcbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XACRYF%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNdZ13GXNWaS6H6gP%2B%2Fyye9PJ34TrEFUhTt0rV6R5j0QIgCoMQijy37jIQ87muJ6GCBFKsC%2BctI%2FRjFdddgup%2FCgIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMe7LhwppHzcg%2FrlFCrcA%2B4mdhMEYvVBF1trR3r0Fr%2Bs0T1run1%2FrmypQlGyLWhmaeXVKxr%2FBUvGYjGufOkSojW%2Fkj9NjinV4jK15CoMT%2BckQV3N%2BjotUB9LIf6zZDAo7D3yASRLmiE2FqApi0jPDg6N33vFcWtW6nsFDxcPOWjz3GpLYXQI%2BDj8hv3j7tVbPptFWkBmrcFnZz04dauC3lYb%2FlUEwc8oPjqmELsPuk%2FEy99scQ0boDzAnBMPKUvvO5A836SNw6y11KftWetg%2B2%2Bv5Pl9VtgtxfS3ysRNsejaCWIFX6SkmI4KQSv%2FKi1h5V5ZLr7V4j%2Fgi%2FKvzmr28QtLjqRmy4O03h0G83zqABNvzxSiylWXcOx8gxQ1hXjKSWnwOW0fDHSkmhsVWA6%2FX4tzppJWM1x%2Fjr5jIhDr51%2Fzq%2BNJAeInUVofGY%2BH%2FdOsRjnDcA5pW5avYPdNpKiDCnCJL6auZb31oH%2B3ZYkkEZfW7tSrrA7eaItDfEuY9MaO25vFPdhOPlzEDfu%2FKjPUdRspXrfQUR5YOuJ0%2BwXsPqeWi9sZjOWMn1oFK%2BdhCyf0NmeyFgfMj24GuxSzuKfgyXCAajmNhOa10CaRlCJC%2F0w4JVKIzHQJlrBD0O4FaHJub4rOulvJDUQd44%2BRMP%2B85MwGOqUBdc52hyw5Pt2tnNufI8i%2FtEOxT8XpphfDg4RtTUlD8GGQxRIQ%2FQVI%2BssJEYyqFKIcjuxKAcEPonOpZB2G8hq0E9MgHdSZt3kFc1%2BtNZPeRb%2FDn2X6Jb2HrJP6dv3eQ26qaMnLLoisXFKXXCnIxFIDUeHFZnV5%2B2JzZifIIAyerAYDmN1HoYuSJpoAND89B3NEp%2BzvvvoQBDabXVQCxKbCRrl1IQxX&X-Amz-Signature=4bf722882983f38f7d4b279cf2e0c2f51e009a872ea632602f9b3c1a4ebc886b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XACRYF%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNdZ13GXNWaS6H6gP%2B%2Fyye9PJ34TrEFUhTt0rV6R5j0QIgCoMQijy37jIQ87muJ6GCBFKsC%2BctI%2FRjFdddgup%2FCgIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMe7LhwppHzcg%2FrlFCrcA%2B4mdhMEYvVBF1trR3r0Fr%2Bs0T1run1%2FrmypQlGyLWhmaeXVKxr%2FBUvGYjGufOkSojW%2Fkj9NjinV4jK15CoMT%2BckQV3N%2BjotUB9LIf6zZDAo7D3yASRLmiE2FqApi0jPDg6N33vFcWtW6nsFDxcPOWjz3GpLYXQI%2BDj8hv3j7tVbPptFWkBmrcFnZz04dauC3lYb%2FlUEwc8oPjqmELsPuk%2FEy99scQ0boDzAnBMPKUvvO5A836SNw6y11KftWetg%2B2%2Bv5Pl9VtgtxfS3ysRNsejaCWIFX6SkmI4KQSv%2FKi1h5V5ZLr7V4j%2Fgi%2FKvzmr28QtLjqRmy4O03h0G83zqABNvzxSiylWXcOx8gxQ1hXjKSWnwOW0fDHSkmhsVWA6%2FX4tzppJWM1x%2Fjr5jIhDr51%2Fzq%2BNJAeInUVofGY%2BH%2FdOsRjnDcA5pW5avYPdNpKiDCnCJL6auZb31oH%2B3ZYkkEZfW7tSrrA7eaItDfEuY9MaO25vFPdhOPlzEDfu%2FKjPUdRspXrfQUR5YOuJ0%2BwXsPqeWi9sZjOWMn1oFK%2BdhCyf0NmeyFgfMj24GuxSzuKfgyXCAajmNhOa10CaRlCJC%2F0w4JVKIzHQJlrBD0O4FaHJub4rOulvJDUQd44%2BRMP%2B85MwGOqUBdc52hyw5Pt2tnNufI8i%2FtEOxT8XpphfDg4RtTUlD8GGQxRIQ%2FQVI%2BssJEYyqFKIcjuxKAcEPonOpZB2G8hq0E9MgHdSZt3kFc1%2BtNZPeRb%2FDn2X6Jb2HrJP6dv3eQ26qaMnLLoisXFKXXCnIxFIDUeHFZnV5%2B2JzZifIIAyerAYDmN1HoYuSJpoAND89B3NEp%2BzvvvoQBDabXVQCxKbCRrl1IQxX&X-Amz-Signature=e62201698a839bed65f59f024b14a82e21b3171b508980f3c65c0e8d0608c45a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6XACRYF%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNdZ13GXNWaS6H6gP%2B%2Fyye9PJ34TrEFUhTt0rV6R5j0QIgCoMQijy37jIQ87muJ6GCBFKsC%2BctI%2FRjFdddgup%2FCgIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMe7LhwppHzcg%2FrlFCrcA%2B4mdhMEYvVBF1trR3r0Fr%2Bs0T1run1%2FrmypQlGyLWhmaeXVKxr%2FBUvGYjGufOkSojW%2Fkj9NjinV4jK15CoMT%2BckQV3N%2BjotUB9LIf6zZDAo7D3yASRLmiE2FqApi0jPDg6N33vFcWtW6nsFDxcPOWjz3GpLYXQI%2BDj8hv3j7tVbPptFWkBmrcFnZz04dauC3lYb%2FlUEwc8oPjqmELsPuk%2FEy99scQ0boDzAnBMPKUvvO5A836SNw6y11KftWetg%2B2%2Bv5Pl9VtgtxfS3ysRNsejaCWIFX6SkmI4KQSv%2FKi1h5V5ZLr7V4j%2Fgi%2FKvzmr28QtLjqRmy4O03h0G83zqABNvzxSiylWXcOx8gxQ1hXjKSWnwOW0fDHSkmhsVWA6%2FX4tzppJWM1x%2Fjr5jIhDr51%2Fzq%2BNJAeInUVofGY%2BH%2FdOsRjnDcA5pW5avYPdNpKiDCnCJL6auZb31oH%2B3ZYkkEZfW7tSrrA7eaItDfEuY9MaO25vFPdhOPlzEDfu%2FKjPUdRspXrfQUR5YOuJ0%2BwXsPqeWi9sZjOWMn1oFK%2BdhCyf0NmeyFgfMj24GuxSzuKfgyXCAajmNhOa10CaRlCJC%2F0w4JVKIzHQJlrBD0O4FaHJub4rOulvJDUQd44%2BRMP%2B85MwGOqUBdc52hyw5Pt2tnNufI8i%2FtEOxT8XpphfDg4RtTUlD8GGQxRIQ%2FQVI%2BssJEYyqFKIcjuxKAcEPonOpZB2G8hq0E9MgHdSZt3kFc1%2BtNZPeRb%2FDn2X6Jb2HrJP6dv3eQ26qaMnLLoisXFKXXCnIxFIDUeHFZnV5%2B2JzZifIIAyerAYDmN1HoYuSJpoAND89B3NEp%2BzvvvoQBDabXVQCxKbCRrl1IQxX&X-Amz-Signature=7e4e457864a0809510ff7a577fa430ae92438877f478e8532f5f3a6f55b11876&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

