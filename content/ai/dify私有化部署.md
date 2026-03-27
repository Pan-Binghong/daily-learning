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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMIWLFHM%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDEWKn90so0Dy06Jo3%2BtiHkyFBXGwQK4tZkM%2FmCpHL91gIgPJDRZlNUHg6KNhc7QSIJUPC1vBQGTRhSYkCm2fLwbF4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ%2BHGUtF%2BC0bfvT%2FircA6VCbyKF%2B%2BfdERIMoxA%2Fs05Md13NbZjZ3BIKbJyqP07IzP97OkQjtDt38CpuoEqtu2ri4ozwJgSMv38qQEXwnWDUsPs6jHHDQ2BxY7EdMN4gy8z1aqrL31F7OpllY2r0tNqxNIE5KRlnwHTxZuBzS9SO%2BnpyXUezTCaqYEBYdbejl9dU26ZDbdPS5HaTiNeQGC7Wg2B9UUrRgRF1h2mf8lQXZjXgbCj21Vrqh2xcsw9DXnURaFzq6lEVRSn1DvMf%2FkTGfKubYUshvTZvInZJ7EHx440tLnQW3Nt42z66t%2F3AGIDYanS1Pz6ZVyi7ciEkCCooZHQfmSsrvCGSx8fuYdiwQgpJDtfTbw9CJuA%2Fo60CQbpRoStfVE6hFSnj8oVnzLRVen90QBF7IFSnnrFigZYBvsQxUInerR%2B%2BCzAEXseMkEQOcwwVJkDq8610gDM%2BahvHe7TF%2F7%2B7ut%2BeH95bL%2FdqAXRgWT4fA5cFvuKobqQXONYZXj8qWebM0E1%2BomUnOA%2BOimBF9s83LehHUEmsqki%2FaEck%2BCZ9aJdV3V6b60VjPnONgCeHf1ERVLCrAbPkTbQEU%2Fub0RTZyax3QayZeB9UfRlU9urzwVl0oTXOexMAoPsIT3yyFRou%2BMqYMNjzls4GOqUB1zmfkDI9do2DLtqr379JEUEaDd2r1kzJjFlbgtZJf6nbm0J6Df%2Bev%2BeaGi2cdJPNk3LJWo1yZci6vbMXPJncIs%2BbiOnHaypLKuHBsJUtEVWCqtl3aT7tBr96YXZ5GQ1QJCP6UBvy6qQpNqDfZYp9zY46MWq4kExfgnSozpv%2BsSeWP4lIK3eXFCEs9gAUKhse8mbUgO4QGlrTzOf2f9ZZtEeIP6ag&X-Amz-Signature=c139c258a2f3e10bf67dbfb5959e83911f9dcc93b7694d9393d622fd9407972c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMIWLFHM%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDEWKn90so0Dy06Jo3%2BtiHkyFBXGwQK4tZkM%2FmCpHL91gIgPJDRZlNUHg6KNhc7QSIJUPC1vBQGTRhSYkCm2fLwbF4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ%2BHGUtF%2BC0bfvT%2FircA6VCbyKF%2B%2BfdERIMoxA%2Fs05Md13NbZjZ3BIKbJyqP07IzP97OkQjtDt38CpuoEqtu2ri4ozwJgSMv38qQEXwnWDUsPs6jHHDQ2BxY7EdMN4gy8z1aqrL31F7OpllY2r0tNqxNIE5KRlnwHTxZuBzS9SO%2BnpyXUezTCaqYEBYdbejl9dU26ZDbdPS5HaTiNeQGC7Wg2B9UUrRgRF1h2mf8lQXZjXgbCj21Vrqh2xcsw9DXnURaFzq6lEVRSn1DvMf%2FkTGfKubYUshvTZvInZJ7EHx440tLnQW3Nt42z66t%2F3AGIDYanS1Pz6ZVyi7ciEkCCooZHQfmSsrvCGSx8fuYdiwQgpJDtfTbw9CJuA%2Fo60CQbpRoStfVE6hFSnj8oVnzLRVen90QBF7IFSnnrFigZYBvsQxUInerR%2B%2BCzAEXseMkEQOcwwVJkDq8610gDM%2BahvHe7TF%2F7%2B7ut%2BeH95bL%2FdqAXRgWT4fA5cFvuKobqQXONYZXj8qWebM0E1%2BomUnOA%2BOimBF9s83LehHUEmsqki%2FaEck%2BCZ9aJdV3V6b60VjPnONgCeHf1ERVLCrAbPkTbQEU%2Fub0RTZyax3QayZeB9UfRlU9urzwVl0oTXOexMAoPsIT3yyFRou%2BMqYMNjzls4GOqUB1zmfkDI9do2DLtqr379JEUEaDd2r1kzJjFlbgtZJf6nbm0J6Df%2Bev%2BeaGi2cdJPNk3LJWo1yZci6vbMXPJncIs%2BbiOnHaypLKuHBsJUtEVWCqtl3aT7tBr96YXZ5GQ1QJCP6UBvy6qQpNqDfZYp9zY46MWq4kExfgnSozpv%2BsSeWP4lIK3eXFCEs9gAUKhse8mbUgO4QGlrTzOf2f9ZZtEeIP6ag&X-Amz-Signature=e851aea6732a3287be011fb8f7c444d8d0d630223106bf129d9c6f62aedfc1a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMIWLFHM%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDEWKn90so0Dy06Jo3%2BtiHkyFBXGwQK4tZkM%2FmCpHL91gIgPJDRZlNUHg6KNhc7QSIJUPC1vBQGTRhSYkCm2fLwbF4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ%2BHGUtF%2BC0bfvT%2FircA6VCbyKF%2B%2BfdERIMoxA%2Fs05Md13NbZjZ3BIKbJyqP07IzP97OkQjtDt38CpuoEqtu2ri4ozwJgSMv38qQEXwnWDUsPs6jHHDQ2BxY7EdMN4gy8z1aqrL31F7OpllY2r0tNqxNIE5KRlnwHTxZuBzS9SO%2BnpyXUezTCaqYEBYdbejl9dU26ZDbdPS5HaTiNeQGC7Wg2B9UUrRgRF1h2mf8lQXZjXgbCj21Vrqh2xcsw9DXnURaFzq6lEVRSn1DvMf%2FkTGfKubYUshvTZvInZJ7EHx440tLnQW3Nt42z66t%2F3AGIDYanS1Pz6ZVyi7ciEkCCooZHQfmSsrvCGSx8fuYdiwQgpJDtfTbw9CJuA%2Fo60CQbpRoStfVE6hFSnj8oVnzLRVen90QBF7IFSnnrFigZYBvsQxUInerR%2B%2BCzAEXseMkEQOcwwVJkDq8610gDM%2BahvHe7TF%2F7%2B7ut%2BeH95bL%2FdqAXRgWT4fA5cFvuKobqQXONYZXj8qWebM0E1%2BomUnOA%2BOimBF9s83LehHUEmsqki%2FaEck%2BCZ9aJdV3V6b60VjPnONgCeHf1ERVLCrAbPkTbQEU%2Fub0RTZyax3QayZeB9UfRlU9urzwVl0oTXOexMAoPsIT3yyFRou%2BMqYMNjzls4GOqUB1zmfkDI9do2DLtqr379JEUEaDd2r1kzJjFlbgtZJf6nbm0J6Df%2Bev%2BeaGi2cdJPNk3LJWo1yZci6vbMXPJncIs%2BbiOnHaypLKuHBsJUtEVWCqtl3aT7tBr96YXZ5GQ1QJCP6UBvy6qQpNqDfZYp9zY46MWq4kExfgnSozpv%2BsSeWP4lIK3eXFCEs9gAUKhse8mbUgO4QGlrTzOf2f9ZZtEeIP6ag&X-Amz-Signature=a5b2b9259e547bbef6be9d2a93495ff711b4a6e5d3f2f390888abe7d943baaf6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMIWLFHM%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDEWKn90so0Dy06Jo3%2BtiHkyFBXGwQK4tZkM%2FmCpHL91gIgPJDRZlNUHg6KNhc7QSIJUPC1vBQGTRhSYkCm2fLwbF4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ%2BHGUtF%2BC0bfvT%2FircA6VCbyKF%2B%2BfdERIMoxA%2Fs05Md13NbZjZ3BIKbJyqP07IzP97OkQjtDt38CpuoEqtu2ri4ozwJgSMv38qQEXwnWDUsPs6jHHDQ2BxY7EdMN4gy8z1aqrL31F7OpllY2r0tNqxNIE5KRlnwHTxZuBzS9SO%2BnpyXUezTCaqYEBYdbejl9dU26ZDbdPS5HaTiNeQGC7Wg2B9UUrRgRF1h2mf8lQXZjXgbCj21Vrqh2xcsw9DXnURaFzq6lEVRSn1DvMf%2FkTGfKubYUshvTZvInZJ7EHx440tLnQW3Nt42z66t%2F3AGIDYanS1Pz6ZVyi7ciEkCCooZHQfmSsrvCGSx8fuYdiwQgpJDtfTbw9CJuA%2Fo60CQbpRoStfVE6hFSnj8oVnzLRVen90QBF7IFSnnrFigZYBvsQxUInerR%2B%2BCzAEXseMkEQOcwwVJkDq8610gDM%2BahvHe7TF%2F7%2B7ut%2BeH95bL%2FdqAXRgWT4fA5cFvuKobqQXONYZXj8qWebM0E1%2BomUnOA%2BOimBF9s83LehHUEmsqki%2FaEck%2BCZ9aJdV3V6b60VjPnONgCeHf1ERVLCrAbPkTbQEU%2Fub0RTZyax3QayZeB9UfRlU9urzwVl0oTXOexMAoPsIT3yyFRou%2BMqYMNjzls4GOqUB1zmfkDI9do2DLtqr379JEUEaDd2r1kzJjFlbgtZJf6nbm0J6Df%2Bev%2BeaGi2cdJPNk3LJWo1yZci6vbMXPJncIs%2BbiOnHaypLKuHBsJUtEVWCqtl3aT7tBr96YXZ5GQ1QJCP6UBvy6qQpNqDfZYp9zY46MWq4kExfgnSozpv%2BsSeWP4lIK3eXFCEs9gAUKhse8mbUgO4QGlrTzOf2f9ZZtEeIP6ag&X-Amz-Signature=1371dedc2872657aa6f271637a3323c4fa4e7a89924b4dac5a9082b9104838c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMIWLFHM%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDEWKn90so0Dy06Jo3%2BtiHkyFBXGwQK4tZkM%2FmCpHL91gIgPJDRZlNUHg6KNhc7QSIJUPC1vBQGTRhSYkCm2fLwbF4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ%2BHGUtF%2BC0bfvT%2FircA6VCbyKF%2B%2BfdERIMoxA%2Fs05Md13NbZjZ3BIKbJyqP07IzP97OkQjtDt38CpuoEqtu2ri4ozwJgSMv38qQEXwnWDUsPs6jHHDQ2BxY7EdMN4gy8z1aqrL31F7OpllY2r0tNqxNIE5KRlnwHTxZuBzS9SO%2BnpyXUezTCaqYEBYdbejl9dU26ZDbdPS5HaTiNeQGC7Wg2B9UUrRgRF1h2mf8lQXZjXgbCj21Vrqh2xcsw9DXnURaFzq6lEVRSn1DvMf%2FkTGfKubYUshvTZvInZJ7EHx440tLnQW3Nt42z66t%2F3AGIDYanS1Pz6ZVyi7ciEkCCooZHQfmSsrvCGSx8fuYdiwQgpJDtfTbw9CJuA%2Fo60CQbpRoStfVE6hFSnj8oVnzLRVen90QBF7IFSnnrFigZYBvsQxUInerR%2B%2BCzAEXseMkEQOcwwVJkDq8610gDM%2BahvHe7TF%2F7%2B7ut%2BeH95bL%2FdqAXRgWT4fA5cFvuKobqQXONYZXj8qWebM0E1%2BomUnOA%2BOimBF9s83LehHUEmsqki%2FaEck%2BCZ9aJdV3V6b60VjPnONgCeHf1ERVLCrAbPkTbQEU%2Fub0RTZyax3QayZeB9UfRlU9urzwVl0oTXOexMAoPsIT3yyFRou%2BMqYMNjzls4GOqUB1zmfkDI9do2DLtqr379JEUEaDd2r1kzJjFlbgtZJf6nbm0J6Df%2Bev%2BeaGi2cdJPNk3LJWo1yZci6vbMXPJncIs%2BbiOnHaypLKuHBsJUtEVWCqtl3aT7tBr96YXZ5GQ1QJCP6UBvy6qQpNqDfZYp9zY46MWq4kExfgnSozpv%2BsSeWP4lIK3eXFCEs9gAUKhse8mbUgO4QGlrTzOf2f9ZZtEeIP6ag&X-Amz-Signature=00edfd9f4fa00c0b579c32c04f517bf132de27ef274077737ae6fb8323b8dd86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMIWLFHM%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDEWKn90so0Dy06Jo3%2BtiHkyFBXGwQK4tZkM%2FmCpHL91gIgPJDRZlNUHg6KNhc7QSIJUPC1vBQGTRhSYkCm2fLwbF4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ%2BHGUtF%2BC0bfvT%2FircA6VCbyKF%2B%2BfdERIMoxA%2Fs05Md13NbZjZ3BIKbJyqP07IzP97OkQjtDt38CpuoEqtu2ri4ozwJgSMv38qQEXwnWDUsPs6jHHDQ2BxY7EdMN4gy8z1aqrL31F7OpllY2r0tNqxNIE5KRlnwHTxZuBzS9SO%2BnpyXUezTCaqYEBYdbejl9dU26ZDbdPS5HaTiNeQGC7Wg2B9UUrRgRF1h2mf8lQXZjXgbCj21Vrqh2xcsw9DXnURaFzq6lEVRSn1DvMf%2FkTGfKubYUshvTZvInZJ7EHx440tLnQW3Nt42z66t%2F3AGIDYanS1Pz6ZVyi7ciEkCCooZHQfmSsrvCGSx8fuYdiwQgpJDtfTbw9CJuA%2Fo60CQbpRoStfVE6hFSnj8oVnzLRVen90QBF7IFSnnrFigZYBvsQxUInerR%2B%2BCzAEXseMkEQOcwwVJkDq8610gDM%2BahvHe7TF%2F7%2B7ut%2BeH95bL%2FdqAXRgWT4fA5cFvuKobqQXONYZXj8qWebM0E1%2BomUnOA%2BOimBF9s83LehHUEmsqki%2FaEck%2BCZ9aJdV3V6b60VjPnONgCeHf1ERVLCrAbPkTbQEU%2Fub0RTZyax3QayZeB9UfRlU9urzwVl0oTXOexMAoPsIT3yyFRou%2BMqYMNjzls4GOqUB1zmfkDI9do2DLtqr379JEUEaDd2r1kzJjFlbgtZJf6nbm0J6Df%2Bev%2BeaGi2cdJPNk3LJWo1yZci6vbMXPJncIs%2BbiOnHaypLKuHBsJUtEVWCqtl3aT7tBr96YXZ5GQ1QJCP6UBvy6qQpNqDfZYp9zY46MWq4kExfgnSozpv%2BsSeWP4lIK3eXFCEs9gAUKhse8mbUgO4QGlrTzOf2f9ZZtEeIP6ag&X-Amz-Signature=932ed089c6c5dfacb054d950ef21547a6cb87f6e1e8acfae2e92430ad7c47f86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMIWLFHM%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDEWKn90so0Dy06Jo3%2BtiHkyFBXGwQK4tZkM%2FmCpHL91gIgPJDRZlNUHg6KNhc7QSIJUPC1vBQGTRhSYkCm2fLwbF4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ%2BHGUtF%2BC0bfvT%2FircA6VCbyKF%2B%2BfdERIMoxA%2Fs05Md13NbZjZ3BIKbJyqP07IzP97OkQjtDt38CpuoEqtu2ri4ozwJgSMv38qQEXwnWDUsPs6jHHDQ2BxY7EdMN4gy8z1aqrL31F7OpllY2r0tNqxNIE5KRlnwHTxZuBzS9SO%2BnpyXUezTCaqYEBYdbejl9dU26ZDbdPS5HaTiNeQGC7Wg2B9UUrRgRF1h2mf8lQXZjXgbCj21Vrqh2xcsw9DXnURaFzq6lEVRSn1DvMf%2FkTGfKubYUshvTZvInZJ7EHx440tLnQW3Nt42z66t%2F3AGIDYanS1Pz6ZVyi7ciEkCCooZHQfmSsrvCGSx8fuYdiwQgpJDtfTbw9CJuA%2Fo60CQbpRoStfVE6hFSnj8oVnzLRVen90QBF7IFSnnrFigZYBvsQxUInerR%2B%2BCzAEXseMkEQOcwwVJkDq8610gDM%2BahvHe7TF%2F7%2B7ut%2BeH95bL%2FdqAXRgWT4fA5cFvuKobqQXONYZXj8qWebM0E1%2BomUnOA%2BOimBF9s83LehHUEmsqki%2FaEck%2BCZ9aJdV3V6b60VjPnONgCeHf1ERVLCrAbPkTbQEU%2Fub0RTZyax3QayZeB9UfRlU9urzwVl0oTXOexMAoPsIT3yyFRou%2BMqYMNjzls4GOqUB1zmfkDI9do2DLtqr379JEUEaDd2r1kzJjFlbgtZJf6nbm0J6Df%2Bev%2BeaGi2cdJPNk3LJWo1yZci6vbMXPJncIs%2BbiOnHaypLKuHBsJUtEVWCqtl3aT7tBr96YXZ5GQ1QJCP6UBvy6qQpNqDfZYp9zY46MWq4kExfgnSozpv%2BsSeWP4lIK3eXFCEs9gAUKhse8mbUgO4QGlrTzOf2f9ZZtEeIP6ag&X-Amz-Signature=00ca1df4cb945fea408496c817701cdf475a4a3878785527f0faa8396f7d5faf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMIWLFHM%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDEWKn90so0Dy06Jo3%2BtiHkyFBXGwQK4tZkM%2FmCpHL91gIgPJDRZlNUHg6KNhc7QSIJUPC1vBQGTRhSYkCm2fLwbF4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ%2BHGUtF%2BC0bfvT%2FircA6VCbyKF%2B%2BfdERIMoxA%2Fs05Md13NbZjZ3BIKbJyqP07IzP97OkQjtDt38CpuoEqtu2ri4ozwJgSMv38qQEXwnWDUsPs6jHHDQ2BxY7EdMN4gy8z1aqrL31F7OpllY2r0tNqxNIE5KRlnwHTxZuBzS9SO%2BnpyXUezTCaqYEBYdbejl9dU26ZDbdPS5HaTiNeQGC7Wg2B9UUrRgRF1h2mf8lQXZjXgbCj21Vrqh2xcsw9DXnURaFzq6lEVRSn1DvMf%2FkTGfKubYUshvTZvInZJ7EHx440tLnQW3Nt42z66t%2F3AGIDYanS1Pz6ZVyi7ciEkCCooZHQfmSsrvCGSx8fuYdiwQgpJDtfTbw9CJuA%2Fo60CQbpRoStfVE6hFSnj8oVnzLRVen90QBF7IFSnnrFigZYBvsQxUInerR%2B%2BCzAEXseMkEQOcwwVJkDq8610gDM%2BahvHe7TF%2F7%2B7ut%2BeH95bL%2FdqAXRgWT4fA5cFvuKobqQXONYZXj8qWebM0E1%2BomUnOA%2BOimBF9s83LehHUEmsqki%2FaEck%2BCZ9aJdV3V6b60VjPnONgCeHf1ERVLCrAbPkTbQEU%2Fub0RTZyax3QayZeB9UfRlU9urzwVl0oTXOexMAoPsIT3yyFRou%2BMqYMNjzls4GOqUB1zmfkDI9do2DLtqr379JEUEaDd2r1kzJjFlbgtZJf6nbm0J6Df%2Bev%2BeaGi2cdJPNk3LJWo1yZci6vbMXPJncIs%2BbiOnHaypLKuHBsJUtEVWCqtl3aT7tBr96YXZ5GQ1QJCP6UBvy6qQpNqDfZYp9zY46MWq4kExfgnSozpv%2BsSeWP4lIK3eXFCEs9gAUKhse8mbUgO4QGlrTzOf2f9ZZtEeIP6ag&X-Amz-Signature=01e29337ced4c97313bddd78bb2433f27eefdcc18ef7dc3102b682302f7eb2b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMIWLFHM%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDEWKn90so0Dy06Jo3%2BtiHkyFBXGwQK4tZkM%2FmCpHL91gIgPJDRZlNUHg6KNhc7QSIJUPC1vBQGTRhSYkCm2fLwbF4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ%2BHGUtF%2BC0bfvT%2FircA6VCbyKF%2B%2BfdERIMoxA%2Fs05Md13NbZjZ3BIKbJyqP07IzP97OkQjtDt38CpuoEqtu2ri4ozwJgSMv38qQEXwnWDUsPs6jHHDQ2BxY7EdMN4gy8z1aqrL31F7OpllY2r0tNqxNIE5KRlnwHTxZuBzS9SO%2BnpyXUezTCaqYEBYdbejl9dU26ZDbdPS5HaTiNeQGC7Wg2B9UUrRgRF1h2mf8lQXZjXgbCj21Vrqh2xcsw9DXnURaFzq6lEVRSn1DvMf%2FkTGfKubYUshvTZvInZJ7EHx440tLnQW3Nt42z66t%2F3AGIDYanS1Pz6ZVyi7ciEkCCooZHQfmSsrvCGSx8fuYdiwQgpJDtfTbw9CJuA%2Fo60CQbpRoStfVE6hFSnj8oVnzLRVen90QBF7IFSnnrFigZYBvsQxUInerR%2B%2BCzAEXseMkEQOcwwVJkDq8610gDM%2BahvHe7TF%2F7%2B7ut%2BeH95bL%2FdqAXRgWT4fA5cFvuKobqQXONYZXj8qWebM0E1%2BomUnOA%2BOimBF9s83LehHUEmsqki%2FaEck%2BCZ9aJdV3V6b60VjPnONgCeHf1ERVLCrAbPkTbQEU%2Fub0RTZyax3QayZeB9UfRlU9urzwVl0oTXOexMAoPsIT3yyFRou%2BMqYMNjzls4GOqUB1zmfkDI9do2DLtqr379JEUEaDd2r1kzJjFlbgtZJf6nbm0J6Df%2Bev%2BeaGi2cdJPNk3LJWo1yZci6vbMXPJncIs%2BbiOnHaypLKuHBsJUtEVWCqtl3aT7tBr96YXZ5GQ1QJCP6UBvy6qQpNqDfZYp9zY46MWq4kExfgnSozpv%2BsSeWP4lIK3eXFCEs9gAUKhse8mbUgO4QGlrTzOf2f9ZZtEeIP6ag&X-Amz-Signature=2bc3b8efc5eecf0860e03f65b47debb7aee78658a23114e9aa5da94dd55fb459&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMIWLFHM%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDEWKn90so0Dy06Jo3%2BtiHkyFBXGwQK4tZkM%2FmCpHL91gIgPJDRZlNUHg6KNhc7QSIJUPC1vBQGTRhSYkCm2fLwbF4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQ%2BHGUtF%2BC0bfvT%2FircA6VCbyKF%2B%2BfdERIMoxA%2Fs05Md13NbZjZ3BIKbJyqP07IzP97OkQjtDt38CpuoEqtu2ri4ozwJgSMv38qQEXwnWDUsPs6jHHDQ2BxY7EdMN4gy8z1aqrL31F7OpllY2r0tNqxNIE5KRlnwHTxZuBzS9SO%2BnpyXUezTCaqYEBYdbejl9dU26ZDbdPS5HaTiNeQGC7Wg2B9UUrRgRF1h2mf8lQXZjXgbCj21Vrqh2xcsw9DXnURaFzq6lEVRSn1DvMf%2FkTGfKubYUshvTZvInZJ7EHx440tLnQW3Nt42z66t%2F3AGIDYanS1Pz6ZVyi7ciEkCCooZHQfmSsrvCGSx8fuYdiwQgpJDtfTbw9CJuA%2Fo60CQbpRoStfVE6hFSnj8oVnzLRVen90QBF7IFSnnrFigZYBvsQxUInerR%2B%2BCzAEXseMkEQOcwwVJkDq8610gDM%2BahvHe7TF%2F7%2B7ut%2BeH95bL%2FdqAXRgWT4fA5cFvuKobqQXONYZXj8qWebM0E1%2BomUnOA%2BOimBF9s83LehHUEmsqki%2FaEck%2BCZ9aJdV3V6b60VjPnONgCeHf1ERVLCrAbPkTbQEU%2Fub0RTZyax3QayZeB9UfRlU9urzwVl0oTXOexMAoPsIT3yyFRou%2BMqYMNjzls4GOqUB1zmfkDI9do2DLtqr379JEUEaDd2r1kzJjFlbgtZJf6nbm0J6Df%2Bev%2BeaGi2cdJPNk3LJWo1yZci6vbMXPJncIs%2BbiOnHaypLKuHBsJUtEVWCqtl3aT7tBr96YXZ5GQ1QJCP6UBvy6qQpNqDfZYp9zY46MWq4kExfgnSozpv%2BsSeWP4lIK3eXFCEs9gAUKhse8mbUgO4QGlrTzOf2f9ZZtEeIP6ag&X-Amz-Signature=18e687acbdcfc1d5dc935e5ece4e454c147b90c2cc8c9a81088a8bc2ca41da88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

