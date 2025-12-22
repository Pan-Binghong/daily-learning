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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JHEMSI%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQD52RcDCKPFc6rZ1uL%2FbVGjPMDLWQxhjQUn6lUmbjTmAAIgR1uNt97eNtkPDgmtsJWwZxe4HwiNHRf0tLwrZj5iDskqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwu4opoBNoEGMieMSrcA%2FT4PXTHBfVYRp9cBxOioQWAXEkd%2FGLkp0F%2B0DWAU1LrawAzGYl30H%2F8lPCF4dwPWNH%2FlxSY6Sm2lXOI7pmA1uzJzzZpUSQLiOVJqWXWQewQnFGaEjcnz4O2yo5wBEiO%2Blwxc7tSWMF574jyuvJBBTjpxIzE2oklCsYdPPrtgmFELg70hH%2BQ3Mndvr6H3shQoW7bqwx38e1%2FxnByjmyCT18eMxKGt5AxXyb4A7oIUrsgflXEOXqoVfwEyeKkcqVYLNCjEJ1%2BqAViNBIllsyrfeBefEIUcw%2B%2Bp9Nl2StIU8xjG6aRKQDckLgMtpC3s24zYaOmmaO8yiQf4i2%2F4kgL6V1ZqvC5wydcBuhSugTuXP7hbxAosqIDlx9mYrO3FWm80ud5FxD3OmyXfa3qHhTqvJEcZnus4N31xE3wFxa%2BaN%2FwanO9gBqPbeGs5E2LWB5pQZi%2F%2FtET%2BkFu400HbTvLlrIRpr2tDjjZDfASN%2B7obYaL1Eb428%2FL8s1GZi5INYs6DLrfRYFPS3sh9iJ1Tbz%2F1qpGyLw7XZCmjA%2BrjZinZCad8iBC1ERzlLhWB%2Bc5MyRhl76cerpZ7EnrQS5cJ4Io9JM79qMvho%2BKqVYba09h%2BmWKCpkyyYNWUTZaosU5MOnkosoGOqUBnUx3D%2Fr83QGERwSkpdb3jfk1PbRAEGffbAvO3CCgtFIB0rkQBms%2FuvT1KxYaKyD%2BKAozBDrDy3l9h2XjcTkoIVts%2B9%2BCCzhrRlyv02JzY%2Bk834rMcSe%2FPzM9L7dQO%2BLz7rDecmVxmigYsBLqulPgygas7LO3DCmtv0NZ6Yu%2BbvjusbI9cIXuAeK5BZEOb1fgnatrrX8CW%2B8FtUh7tzlSFlqMkjP3&X-Amz-Signature=0ec12cd7250e10830e5815aca4540d367fb698858afc1ebbf080c747bd255044&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JHEMSI%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQD52RcDCKPFc6rZ1uL%2FbVGjPMDLWQxhjQUn6lUmbjTmAAIgR1uNt97eNtkPDgmtsJWwZxe4HwiNHRf0tLwrZj5iDskqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwu4opoBNoEGMieMSrcA%2FT4PXTHBfVYRp9cBxOioQWAXEkd%2FGLkp0F%2B0DWAU1LrawAzGYl30H%2F8lPCF4dwPWNH%2FlxSY6Sm2lXOI7pmA1uzJzzZpUSQLiOVJqWXWQewQnFGaEjcnz4O2yo5wBEiO%2Blwxc7tSWMF574jyuvJBBTjpxIzE2oklCsYdPPrtgmFELg70hH%2BQ3Mndvr6H3shQoW7bqwx38e1%2FxnByjmyCT18eMxKGt5AxXyb4A7oIUrsgflXEOXqoVfwEyeKkcqVYLNCjEJ1%2BqAViNBIllsyrfeBefEIUcw%2B%2Bp9Nl2StIU8xjG6aRKQDckLgMtpC3s24zYaOmmaO8yiQf4i2%2F4kgL6V1ZqvC5wydcBuhSugTuXP7hbxAosqIDlx9mYrO3FWm80ud5FxD3OmyXfa3qHhTqvJEcZnus4N31xE3wFxa%2BaN%2FwanO9gBqPbeGs5E2LWB5pQZi%2F%2FtET%2BkFu400HbTvLlrIRpr2tDjjZDfASN%2B7obYaL1Eb428%2FL8s1GZi5INYs6DLrfRYFPS3sh9iJ1Tbz%2F1qpGyLw7XZCmjA%2BrjZinZCad8iBC1ERzlLhWB%2Bc5MyRhl76cerpZ7EnrQS5cJ4Io9JM79qMvho%2BKqVYba09h%2BmWKCpkyyYNWUTZaosU5MOnkosoGOqUBnUx3D%2Fr83QGERwSkpdb3jfk1PbRAEGffbAvO3CCgtFIB0rkQBms%2FuvT1KxYaKyD%2BKAozBDrDy3l9h2XjcTkoIVts%2B9%2BCCzhrRlyv02JzY%2Bk834rMcSe%2FPzM9L7dQO%2BLz7rDecmVxmigYsBLqulPgygas7LO3DCmtv0NZ6Yu%2BbvjusbI9cIXuAeK5BZEOb1fgnatrrX8CW%2B8FtUh7tzlSFlqMkjP3&X-Amz-Signature=c34fa8d1f645262ca8501d4383e473fd4227124c7d0e6f9836b7538b6dd37e68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JHEMSI%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQD52RcDCKPFc6rZ1uL%2FbVGjPMDLWQxhjQUn6lUmbjTmAAIgR1uNt97eNtkPDgmtsJWwZxe4HwiNHRf0tLwrZj5iDskqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwu4opoBNoEGMieMSrcA%2FT4PXTHBfVYRp9cBxOioQWAXEkd%2FGLkp0F%2B0DWAU1LrawAzGYl30H%2F8lPCF4dwPWNH%2FlxSY6Sm2lXOI7pmA1uzJzzZpUSQLiOVJqWXWQewQnFGaEjcnz4O2yo5wBEiO%2Blwxc7tSWMF574jyuvJBBTjpxIzE2oklCsYdPPrtgmFELg70hH%2BQ3Mndvr6H3shQoW7bqwx38e1%2FxnByjmyCT18eMxKGt5AxXyb4A7oIUrsgflXEOXqoVfwEyeKkcqVYLNCjEJ1%2BqAViNBIllsyrfeBefEIUcw%2B%2Bp9Nl2StIU8xjG6aRKQDckLgMtpC3s24zYaOmmaO8yiQf4i2%2F4kgL6V1ZqvC5wydcBuhSugTuXP7hbxAosqIDlx9mYrO3FWm80ud5FxD3OmyXfa3qHhTqvJEcZnus4N31xE3wFxa%2BaN%2FwanO9gBqPbeGs5E2LWB5pQZi%2F%2FtET%2BkFu400HbTvLlrIRpr2tDjjZDfASN%2B7obYaL1Eb428%2FL8s1GZi5INYs6DLrfRYFPS3sh9iJ1Tbz%2F1qpGyLw7XZCmjA%2BrjZinZCad8iBC1ERzlLhWB%2Bc5MyRhl76cerpZ7EnrQS5cJ4Io9JM79qMvho%2BKqVYba09h%2BmWKCpkyyYNWUTZaosU5MOnkosoGOqUBnUx3D%2Fr83QGERwSkpdb3jfk1PbRAEGffbAvO3CCgtFIB0rkQBms%2FuvT1KxYaKyD%2BKAozBDrDy3l9h2XjcTkoIVts%2B9%2BCCzhrRlyv02JzY%2Bk834rMcSe%2FPzM9L7dQO%2BLz7rDecmVxmigYsBLqulPgygas7LO3DCmtv0NZ6Yu%2BbvjusbI9cIXuAeK5BZEOb1fgnatrrX8CW%2B8FtUh7tzlSFlqMkjP3&X-Amz-Signature=4663acaef4ff0260436dd34407f60ecc682ee05e416b52de53c974ac41e6d958&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JHEMSI%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQD52RcDCKPFc6rZ1uL%2FbVGjPMDLWQxhjQUn6lUmbjTmAAIgR1uNt97eNtkPDgmtsJWwZxe4HwiNHRf0tLwrZj5iDskqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwu4opoBNoEGMieMSrcA%2FT4PXTHBfVYRp9cBxOioQWAXEkd%2FGLkp0F%2B0DWAU1LrawAzGYl30H%2F8lPCF4dwPWNH%2FlxSY6Sm2lXOI7pmA1uzJzzZpUSQLiOVJqWXWQewQnFGaEjcnz4O2yo5wBEiO%2Blwxc7tSWMF574jyuvJBBTjpxIzE2oklCsYdPPrtgmFELg70hH%2BQ3Mndvr6H3shQoW7bqwx38e1%2FxnByjmyCT18eMxKGt5AxXyb4A7oIUrsgflXEOXqoVfwEyeKkcqVYLNCjEJ1%2BqAViNBIllsyrfeBefEIUcw%2B%2Bp9Nl2StIU8xjG6aRKQDckLgMtpC3s24zYaOmmaO8yiQf4i2%2F4kgL6V1ZqvC5wydcBuhSugTuXP7hbxAosqIDlx9mYrO3FWm80ud5FxD3OmyXfa3qHhTqvJEcZnus4N31xE3wFxa%2BaN%2FwanO9gBqPbeGs5E2LWB5pQZi%2F%2FtET%2BkFu400HbTvLlrIRpr2tDjjZDfASN%2B7obYaL1Eb428%2FL8s1GZi5INYs6DLrfRYFPS3sh9iJ1Tbz%2F1qpGyLw7XZCmjA%2BrjZinZCad8iBC1ERzlLhWB%2Bc5MyRhl76cerpZ7EnrQS5cJ4Io9JM79qMvho%2BKqVYba09h%2BmWKCpkyyYNWUTZaosU5MOnkosoGOqUBnUx3D%2Fr83QGERwSkpdb3jfk1PbRAEGffbAvO3CCgtFIB0rkQBms%2FuvT1KxYaKyD%2BKAozBDrDy3l9h2XjcTkoIVts%2B9%2BCCzhrRlyv02JzY%2Bk834rMcSe%2FPzM9L7dQO%2BLz7rDecmVxmigYsBLqulPgygas7LO3DCmtv0NZ6Yu%2BbvjusbI9cIXuAeK5BZEOb1fgnatrrX8CW%2B8FtUh7tzlSFlqMkjP3&X-Amz-Signature=0adaad5939c37bc60601811cb9f06b451bbbdfec224d06e942ace747aab34091&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JHEMSI%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQD52RcDCKPFc6rZ1uL%2FbVGjPMDLWQxhjQUn6lUmbjTmAAIgR1uNt97eNtkPDgmtsJWwZxe4HwiNHRf0tLwrZj5iDskqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwu4opoBNoEGMieMSrcA%2FT4PXTHBfVYRp9cBxOioQWAXEkd%2FGLkp0F%2B0DWAU1LrawAzGYl30H%2F8lPCF4dwPWNH%2FlxSY6Sm2lXOI7pmA1uzJzzZpUSQLiOVJqWXWQewQnFGaEjcnz4O2yo5wBEiO%2Blwxc7tSWMF574jyuvJBBTjpxIzE2oklCsYdPPrtgmFELg70hH%2BQ3Mndvr6H3shQoW7bqwx38e1%2FxnByjmyCT18eMxKGt5AxXyb4A7oIUrsgflXEOXqoVfwEyeKkcqVYLNCjEJ1%2BqAViNBIllsyrfeBefEIUcw%2B%2Bp9Nl2StIU8xjG6aRKQDckLgMtpC3s24zYaOmmaO8yiQf4i2%2F4kgL6V1ZqvC5wydcBuhSugTuXP7hbxAosqIDlx9mYrO3FWm80ud5FxD3OmyXfa3qHhTqvJEcZnus4N31xE3wFxa%2BaN%2FwanO9gBqPbeGs5E2LWB5pQZi%2F%2FtET%2BkFu400HbTvLlrIRpr2tDjjZDfASN%2B7obYaL1Eb428%2FL8s1GZi5INYs6DLrfRYFPS3sh9iJ1Tbz%2F1qpGyLw7XZCmjA%2BrjZinZCad8iBC1ERzlLhWB%2Bc5MyRhl76cerpZ7EnrQS5cJ4Io9JM79qMvho%2BKqVYba09h%2BmWKCpkyyYNWUTZaosU5MOnkosoGOqUBnUx3D%2Fr83QGERwSkpdb3jfk1PbRAEGffbAvO3CCgtFIB0rkQBms%2FuvT1KxYaKyD%2BKAozBDrDy3l9h2XjcTkoIVts%2B9%2BCCzhrRlyv02JzY%2Bk834rMcSe%2FPzM9L7dQO%2BLz7rDecmVxmigYsBLqulPgygas7LO3DCmtv0NZ6Yu%2BbvjusbI9cIXuAeK5BZEOb1fgnatrrX8CW%2B8FtUh7tzlSFlqMkjP3&X-Amz-Signature=16b8c030df4d861ef5784d8f8b9ef0b11cfc65ead713004a722d3bda0d6d019c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JHEMSI%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQD52RcDCKPFc6rZ1uL%2FbVGjPMDLWQxhjQUn6lUmbjTmAAIgR1uNt97eNtkPDgmtsJWwZxe4HwiNHRf0tLwrZj5iDskqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwu4opoBNoEGMieMSrcA%2FT4PXTHBfVYRp9cBxOioQWAXEkd%2FGLkp0F%2B0DWAU1LrawAzGYl30H%2F8lPCF4dwPWNH%2FlxSY6Sm2lXOI7pmA1uzJzzZpUSQLiOVJqWXWQewQnFGaEjcnz4O2yo5wBEiO%2Blwxc7tSWMF574jyuvJBBTjpxIzE2oklCsYdPPrtgmFELg70hH%2BQ3Mndvr6H3shQoW7bqwx38e1%2FxnByjmyCT18eMxKGt5AxXyb4A7oIUrsgflXEOXqoVfwEyeKkcqVYLNCjEJ1%2BqAViNBIllsyrfeBefEIUcw%2B%2Bp9Nl2StIU8xjG6aRKQDckLgMtpC3s24zYaOmmaO8yiQf4i2%2F4kgL6V1ZqvC5wydcBuhSugTuXP7hbxAosqIDlx9mYrO3FWm80ud5FxD3OmyXfa3qHhTqvJEcZnus4N31xE3wFxa%2BaN%2FwanO9gBqPbeGs5E2LWB5pQZi%2F%2FtET%2BkFu400HbTvLlrIRpr2tDjjZDfASN%2B7obYaL1Eb428%2FL8s1GZi5INYs6DLrfRYFPS3sh9iJ1Tbz%2F1qpGyLw7XZCmjA%2BrjZinZCad8iBC1ERzlLhWB%2Bc5MyRhl76cerpZ7EnrQS5cJ4Io9JM79qMvho%2BKqVYba09h%2BmWKCpkyyYNWUTZaosU5MOnkosoGOqUBnUx3D%2Fr83QGERwSkpdb3jfk1PbRAEGffbAvO3CCgtFIB0rkQBms%2FuvT1KxYaKyD%2BKAozBDrDy3l9h2XjcTkoIVts%2B9%2BCCzhrRlyv02JzY%2Bk834rMcSe%2FPzM9L7dQO%2BLz7rDecmVxmigYsBLqulPgygas7LO3DCmtv0NZ6Yu%2BbvjusbI9cIXuAeK5BZEOb1fgnatrrX8CW%2B8FtUh7tzlSFlqMkjP3&X-Amz-Signature=fc02930acd9abcbb7ce48008d7241a5fabfe379c09d38d765ef594b9f12f703c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JHEMSI%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQD52RcDCKPFc6rZ1uL%2FbVGjPMDLWQxhjQUn6lUmbjTmAAIgR1uNt97eNtkPDgmtsJWwZxe4HwiNHRf0tLwrZj5iDskqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwu4opoBNoEGMieMSrcA%2FT4PXTHBfVYRp9cBxOioQWAXEkd%2FGLkp0F%2B0DWAU1LrawAzGYl30H%2F8lPCF4dwPWNH%2FlxSY6Sm2lXOI7pmA1uzJzzZpUSQLiOVJqWXWQewQnFGaEjcnz4O2yo5wBEiO%2Blwxc7tSWMF574jyuvJBBTjpxIzE2oklCsYdPPrtgmFELg70hH%2BQ3Mndvr6H3shQoW7bqwx38e1%2FxnByjmyCT18eMxKGt5AxXyb4A7oIUrsgflXEOXqoVfwEyeKkcqVYLNCjEJ1%2BqAViNBIllsyrfeBefEIUcw%2B%2Bp9Nl2StIU8xjG6aRKQDckLgMtpC3s24zYaOmmaO8yiQf4i2%2F4kgL6V1ZqvC5wydcBuhSugTuXP7hbxAosqIDlx9mYrO3FWm80ud5FxD3OmyXfa3qHhTqvJEcZnus4N31xE3wFxa%2BaN%2FwanO9gBqPbeGs5E2LWB5pQZi%2F%2FtET%2BkFu400HbTvLlrIRpr2tDjjZDfASN%2B7obYaL1Eb428%2FL8s1GZi5INYs6DLrfRYFPS3sh9iJ1Tbz%2F1qpGyLw7XZCmjA%2BrjZinZCad8iBC1ERzlLhWB%2Bc5MyRhl76cerpZ7EnrQS5cJ4Io9JM79qMvho%2BKqVYba09h%2BmWKCpkyyYNWUTZaosU5MOnkosoGOqUBnUx3D%2Fr83QGERwSkpdb3jfk1PbRAEGffbAvO3CCgtFIB0rkQBms%2FuvT1KxYaKyD%2BKAozBDrDy3l9h2XjcTkoIVts%2B9%2BCCzhrRlyv02JzY%2Bk834rMcSe%2FPzM9L7dQO%2BLz7rDecmVxmigYsBLqulPgygas7LO3DCmtv0NZ6Yu%2BbvjusbI9cIXuAeK5BZEOb1fgnatrrX8CW%2B8FtUh7tzlSFlqMkjP3&X-Amz-Signature=771371b7945e714c13caa9f39cc0871288e7ff5e3cb11ff6af8ca36f0cc25a1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JHEMSI%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQD52RcDCKPFc6rZ1uL%2FbVGjPMDLWQxhjQUn6lUmbjTmAAIgR1uNt97eNtkPDgmtsJWwZxe4HwiNHRf0tLwrZj5iDskqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwu4opoBNoEGMieMSrcA%2FT4PXTHBfVYRp9cBxOioQWAXEkd%2FGLkp0F%2B0DWAU1LrawAzGYl30H%2F8lPCF4dwPWNH%2FlxSY6Sm2lXOI7pmA1uzJzzZpUSQLiOVJqWXWQewQnFGaEjcnz4O2yo5wBEiO%2Blwxc7tSWMF574jyuvJBBTjpxIzE2oklCsYdPPrtgmFELg70hH%2BQ3Mndvr6H3shQoW7bqwx38e1%2FxnByjmyCT18eMxKGt5AxXyb4A7oIUrsgflXEOXqoVfwEyeKkcqVYLNCjEJ1%2BqAViNBIllsyrfeBefEIUcw%2B%2Bp9Nl2StIU8xjG6aRKQDckLgMtpC3s24zYaOmmaO8yiQf4i2%2F4kgL6V1ZqvC5wydcBuhSugTuXP7hbxAosqIDlx9mYrO3FWm80ud5FxD3OmyXfa3qHhTqvJEcZnus4N31xE3wFxa%2BaN%2FwanO9gBqPbeGs5E2LWB5pQZi%2F%2FtET%2BkFu400HbTvLlrIRpr2tDjjZDfASN%2B7obYaL1Eb428%2FL8s1GZi5INYs6DLrfRYFPS3sh9iJ1Tbz%2F1qpGyLw7XZCmjA%2BrjZinZCad8iBC1ERzlLhWB%2Bc5MyRhl76cerpZ7EnrQS5cJ4Io9JM79qMvho%2BKqVYba09h%2BmWKCpkyyYNWUTZaosU5MOnkosoGOqUBnUx3D%2Fr83QGERwSkpdb3jfk1PbRAEGffbAvO3CCgtFIB0rkQBms%2FuvT1KxYaKyD%2BKAozBDrDy3l9h2XjcTkoIVts%2B9%2BCCzhrRlyv02JzY%2Bk834rMcSe%2FPzM9L7dQO%2BLz7rDecmVxmigYsBLqulPgygas7LO3DCmtv0NZ6Yu%2BbvjusbI9cIXuAeK5BZEOb1fgnatrrX8CW%2B8FtUh7tzlSFlqMkjP3&X-Amz-Signature=e20f326492617adb869acddb9466894135e6fd90c488a7716c5d4d9279836b83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JHEMSI%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQD52RcDCKPFc6rZ1uL%2FbVGjPMDLWQxhjQUn6lUmbjTmAAIgR1uNt97eNtkPDgmtsJWwZxe4HwiNHRf0tLwrZj5iDskqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwu4opoBNoEGMieMSrcA%2FT4PXTHBfVYRp9cBxOioQWAXEkd%2FGLkp0F%2B0DWAU1LrawAzGYl30H%2F8lPCF4dwPWNH%2FlxSY6Sm2lXOI7pmA1uzJzzZpUSQLiOVJqWXWQewQnFGaEjcnz4O2yo5wBEiO%2Blwxc7tSWMF574jyuvJBBTjpxIzE2oklCsYdPPrtgmFELg70hH%2BQ3Mndvr6H3shQoW7bqwx38e1%2FxnByjmyCT18eMxKGt5AxXyb4A7oIUrsgflXEOXqoVfwEyeKkcqVYLNCjEJ1%2BqAViNBIllsyrfeBefEIUcw%2B%2Bp9Nl2StIU8xjG6aRKQDckLgMtpC3s24zYaOmmaO8yiQf4i2%2F4kgL6V1ZqvC5wydcBuhSugTuXP7hbxAosqIDlx9mYrO3FWm80ud5FxD3OmyXfa3qHhTqvJEcZnus4N31xE3wFxa%2BaN%2FwanO9gBqPbeGs5E2LWB5pQZi%2F%2FtET%2BkFu400HbTvLlrIRpr2tDjjZDfASN%2B7obYaL1Eb428%2FL8s1GZi5INYs6DLrfRYFPS3sh9iJ1Tbz%2F1qpGyLw7XZCmjA%2BrjZinZCad8iBC1ERzlLhWB%2Bc5MyRhl76cerpZ7EnrQS5cJ4Io9JM79qMvho%2BKqVYba09h%2BmWKCpkyyYNWUTZaosU5MOnkosoGOqUBnUx3D%2Fr83QGERwSkpdb3jfk1PbRAEGffbAvO3CCgtFIB0rkQBms%2FuvT1KxYaKyD%2BKAozBDrDy3l9h2XjcTkoIVts%2B9%2BCCzhrRlyv02JzY%2Bk834rMcSe%2FPzM9L7dQO%2BLz7rDecmVxmigYsBLqulPgygas7LO3DCmtv0NZ6Yu%2BbvjusbI9cIXuAeK5BZEOb1fgnatrrX8CW%2B8FtUh7tzlSFlqMkjP3&X-Amz-Signature=23922cb78f655e05a23abec967d93d86f1bcb23f1fb47a79d240895034c3351d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JHEMSI%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQD52RcDCKPFc6rZ1uL%2FbVGjPMDLWQxhjQUn6lUmbjTmAAIgR1uNt97eNtkPDgmtsJWwZxe4HwiNHRf0tLwrZj5iDskqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFwu4opoBNoEGMieMSrcA%2FT4PXTHBfVYRp9cBxOioQWAXEkd%2FGLkp0F%2B0DWAU1LrawAzGYl30H%2F8lPCF4dwPWNH%2FlxSY6Sm2lXOI7pmA1uzJzzZpUSQLiOVJqWXWQewQnFGaEjcnz4O2yo5wBEiO%2Blwxc7tSWMF574jyuvJBBTjpxIzE2oklCsYdPPrtgmFELg70hH%2BQ3Mndvr6H3shQoW7bqwx38e1%2FxnByjmyCT18eMxKGt5AxXyb4A7oIUrsgflXEOXqoVfwEyeKkcqVYLNCjEJ1%2BqAViNBIllsyrfeBefEIUcw%2B%2Bp9Nl2StIU8xjG6aRKQDckLgMtpC3s24zYaOmmaO8yiQf4i2%2F4kgL6V1ZqvC5wydcBuhSugTuXP7hbxAosqIDlx9mYrO3FWm80ud5FxD3OmyXfa3qHhTqvJEcZnus4N31xE3wFxa%2BaN%2FwanO9gBqPbeGs5E2LWB5pQZi%2F%2FtET%2BkFu400HbTvLlrIRpr2tDjjZDfASN%2B7obYaL1Eb428%2FL8s1GZi5INYs6DLrfRYFPS3sh9iJ1Tbz%2F1qpGyLw7XZCmjA%2BrjZinZCad8iBC1ERzlLhWB%2Bc5MyRhl76cerpZ7EnrQS5cJ4Io9JM79qMvho%2BKqVYba09h%2BmWKCpkyyYNWUTZaosU5MOnkosoGOqUBnUx3D%2Fr83QGERwSkpdb3jfk1PbRAEGffbAvO3CCgtFIB0rkQBms%2FuvT1KxYaKyD%2BKAozBDrDy3l9h2XjcTkoIVts%2B9%2BCCzhrRlyv02JzY%2Bk834rMcSe%2FPzM9L7dQO%2BLz7rDecmVxmigYsBLqulPgygas7LO3DCmtv0NZ6Yu%2BbvjusbI9cIXuAeK5BZEOb1fgnatrrX8CW%2B8FtUh7tzlSFlqMkjP3&X-Amz-Signature=d26ad8a7edd26d2ec67b6994f29dbedf5a72f0c49fa03936503d1c7ceed1293e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

