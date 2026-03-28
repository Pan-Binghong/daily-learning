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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SIMXGP4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCpCEhQAIC0fJ3WNj%2F0dTHTIXIi8T4A%2Buq9bOyvjroHqAIgWRecHsiFCzFwADYIxcNv%2FIj5PsOYqbNCHmAU6q6slh4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGq%2FgRhayuTfQ3CQSrcA3PHegc9DnHbuS4l5ZQ7F1%2BT5TBMek%2BvCjYBpwo5ZqqRRZNbhtJUvDjpxMoVLm5QjhqMddFSIrq4jq%2BE6mTrZjF0vxul0nev5EPdtp71R0QfgDOKuAKQcpmuDTX0oUb3Bu1336Qnves1i2H9V2%2Bv4AyGNPiYVRslA4aUB73J1wmUaAuO1tnIxQb48wJFsEK6%2Fm%2BA0b2rEYAiM00AQxaIg7Ih6bVtuzrfabchQl6u5TjMRFLCMp3tPlmZtDJlLLbExzKw8P8RpyBQ6hsN%2BVFsR%2BDVaIsmb10UuDNJWqW6CHj0eo5UJen8BoNBK5cHbTP2%2BrPnIYpsfckYM16f7rhXzC98LX7Z2D58AD8JUZwG%2Bmv2Ec7QfpdxADA6tQErDmtP10odopS0oqJn3h5ney%2FWI65viixJUeVDw%2FQOZesS%2BHXT6LJ7MtjtKm2Kue67aLsprYap9quVr%2FD7%2FO2EJArV66YaBphBv%2BrUce4111yXJLCO%2BROSewAuRfigs%2Br0PR4qjfkVl5FDCE%2BStb6E0VnxHznVY1Hi6NIYcIFF%2BMzG8juKWhjklWrAXOmwghY3mz88rAA9AU1GkK0gGvjusEHdeOIFJCss%2BFsqVX63L%2BOVnCJxhDsN%2BtylRZFJMrVdMJDtnM4GOqUB3SKkgn7pjA%2Fv4sGsvbabJivK0hUmi1rTSvWo7GpwXk2C7mgYjLrD67TmGrnmMHG5ggOGGX5InXeIDm6Ju%2FMHtN%2BTUmyRMXefYDVRs%2FmaRqvLZBbUdrueKrWs%2FT7lV2tWyJVpLa0ZEzG85%2BFKfZauOz8%2FIeGIVunWOuw7kqfyu9uQPqIC2ChCzR31UwQThdllWGee8to3nWpj0WCu77KPvWF6XSW1&X-Amz-Signature=f58c63722897d44df2a194029b233817c4b78d18fb9ee538addd64d1f665c1d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SIMXGP4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCpCEhQAIC0fJ3WNj%2F0dTHTIXIi8T4A%2Buq9bOyvjroHqAIgWRecHsiFCzFwADYIxcNv%2FIj5PsOYqbNCHmAU6q6slh4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGq%2FgRhayuTfQ3CQSrcA3PHegc9DnHbuS4l5ZQ7F1%2BT5TBMek%2BvCjYBpwo5ZqqRRZNbhtJUvDjpxMoVLm5QjhqMddFSIrq4jq%2BE6mTrZjF0vxul0nev5EPdtp71R0QfgDOKuAKQcpmuDTX0oUb3Bu1336Qnves1i2H9V2%2Bv4AyGNPiYVRslA4aUB73J1wmUaAuO1tnIxQb48wJFsEK6%2Fm%2BA0b2rEYAiM00AQxaIg7Ih6bVtuzrfabchQl6u5TjMRFLCMp3tPlmZtDJlLLbExzKw8P8RpyBQ6hsN%2BVFsR%2BDVaIsmb10UuDNJWqW6CHj0eo5UJen8BoNBK5cHbTP2%2BrPnIYpsfckYM16f7rhXzC98LX7Z2D58AD8JUZwG%2Bmv2Ec7QfpdxADA6tQErDmtP10odopS0oqJn3h5ney%2FWI65viixJUeVDw%2FQOZesS%2BHXT6LJ7MtjtKm2Kue67aLsprYap9quVr%2FD7%2FO2EJArV66YaBphBv%2BrUce4111yXJLCO%2BROSewAuRfigs%2Br0PR4qjfkVl5FDCE%2BStb6E0VnxHznVY1Hi6NIYcIFF%2BMzG8juKWhjklWrAXOmwghY3mz88rAA9AU1GkK0gGvjusEHdeOIFJCss%2BFsqVX63L%2BOVnCJxhDsN%2BtylRZFJMrVdMJDtnM4GOqUB3SKkgn7pjA%2Fv4sGsvbabJivK0hUmi1rTSvWo7GpwXk2C7mgYjLrD67TmGrnmMHG5ggOGGX5InXeIDm6Ju%2FMHtN%2BTUmyRMXefYDVRs%2FmaRqvLZBbUdrueKrWs%2FT7lV2tWyJVpLa0ZEzG85%2BFKfZauOz8%2FIeGIVunWOuw7kqfyu9uQPqIC2ChCzR31UwQThdllWGee8to3nWpj0WCu77KPvWF6XSW1&X-Amz-Signature=65f40d54720d941f6ae173de1caf15989c025434307ec5b7798259b15f1d686d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SIMXGP4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCpCEhQAIC0fJ3WNj%2F0dTHTIXIi8T4A%2Buq9bOyvjroHqAIgWRecHsiFCzFwADYIxcNv%2FIj5PsOYqbNCHmAU6q6slh4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGq%2FgRhayuTfQ3CQSrcA3PHegc9DnHbuS4l5ZQ7F1%2BT5TBMek%2BvCjYBpwo5ZqqRRZNbhtJUvDjpxMoVLm5QjhqMddFSIrq4jq%2BE6mTrZjF0vxul0nev5EPdtp71R0QfgDOKuAKQcpmuDTX0oUb3Bu1336Qnves1i2H9V2%2Bv4AyGNPiYVRslA4aUB73J1wmUaAuO1tnIxQb48wJFsEK6%2Fm%2BA0b2rEYAiM00AQxaIg7Ih6bVtuzrfabchQl6u5TjMRFLCMp3tPlmZtDJlLLbExzKw8P8RpyBQ6hsN%2BVFsR%2BDVaIsmb10UuDNJWqW6CHj0eo5UJen8BoNBK5cHbTP2%2BrPnIYpsfckYM16f7rhXzC98LX7Z2D58AD8JUZwG%2Bmv2Ec7QfpdxADA6tQErDmtP10odopS0oqJn3h5ney%2FWI65viixJUeVDw%2FQOZesS%2BHXT6LJ7MtjtKm2Kue67aLsprYap9quVr%2FD7%2FO2EJArV66YaBphBv%2BrUce4111yXJLCO%2BROSewAuRfigs%2Br0PR4qjfkVl5FDCE%2BStb6E0VnxHznVY1Hi6NIYcIFF%2BMzG8juKWhjklWrAXOmwghY3mz88rAA9AU1GkK0gGvjusEHdeOIFJCss%2BFsqVX63L%2BOVnCJxhDsN%2BtylRZFJMrVdMJDtnM4GOqUB3SKkgn7pjA%2Fv4sGsvbabJivK0hUmi1rTSvWo7GpwXk2C7mgYjLrD67TmGrnmMHG5ggOGGX5InXeIDm6Ju%2FMHtN%2BTUmyRMXefYDVRs%2FmaRqvLZBbUdrueKrWs%2FT7lV2tWyJVpLa0ZEzG85%2BFKfZauOz8%2FIeGIVunWOuw7kqfyu9uQPqIC2ChCzR31UwQThdllWGee8to3nWpj0WCu77KPvWF6XSW1&X-Amz-Signature=919482ff1b8aa7358b294f88ab35809969c7cb44a106bc9f1a7137cf1b1c11b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SIMXGP4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCpCEhQAIC0fJ3WNj%2F0dTHTIXIi8T4A%2Buq9bOyvjroHqAIgWRecHsiFCzFwADYIxcNv%2FIj5PsOYqbNCHmAU6q6slh4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGq%2FgRhayuTfQ3CQSrcA3PHegc9DnHbuS4l5ZQ7F1%2BT5TBMek%2BvCjYBpwo5ZqqRRZNbhtJUvDjpxMoVLm5QjhqMddFSIrq4jq%2BE6mTrZjF0vxul0nev5EPdtp71R0QfgDOKuAKQcpmuDTX0oUb3Bu1336Qnves1i2H9V2%2Bv4AyGNPiYVRslA4aUB73J1wmUaAuO1tnIxQb48wJFsEK6%2Fm%2BA0b2rEYAiM00AQxaIg7Ih6bVtuzrfabchQl6u5TjMRFLCMp3tPlmZtDJlLLbExzKw8P8RpyBQ6hsN%2BVFsR%2BDVaIsmb10UuDNJWqW6CHj0eo5UJen8BoNBK5cHbTP2%2BrPnIYpsfckYM16f7rhXzC98LX7Z2D58AD8JUZwG%2Bmv2Ec7QfpdxADA6tQErDmtP10odopS0oqJn3h5ney%2FWI65viixJUeVDw%2FQOZesS%2BHXT6LJ7MtjtKm2Kue67aLsprYap9quVr%2FD7%2FO2EJArV66YaBphBv%2BrUce4111yXJLCO%2BROSewAuRfigs%2Br0PR4qjfkVl5FDCE%2BStb6E0VnxHznVY1Hi6NIYcIFF%2BMzG8juKWhjklWrAXOmwghY3mz88rAA9AU1GkK0gGvjusEHdeOIFJCss%2BFsqVX63L%2BOVnCJxhDsN%2BtylRZFJMrVdMJDtnM4GOqUB3SKkgn7pjA%2Fv4sGsvbabJivK0hUmi1rTSvWo7GpwXk2C7mgYjLrD67TmGrnmMHG5ggOGGX5InXeIDm6Ju%2FMHtN%2BTUmyRMXefYDVRs%2FmaRqvLZBbUdrueKrWs%2FT7lV2tWyJVpLa0ZEzG85%2BFKfZauOz8%2FIeGIVunWOuw7kqfyu9uQPqIC2ChCzR31UwQThdllWGee8to3nWpj0WCu77KPvWF6XSW1&X-Amz-Signature=546b57a28a07154b235d1a5fc884a098600a1e2d586999a4e41e6b9d0fd90d6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SIMXGP4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCpCEhQAIC0fJ3WNj%2F0dTHTIXIi8T4A%2Buq9bOyvjroHqAIgWRecHsiFCzFwADYIxcNv%2FIj5PsOYqbNCHmAU6q6slh4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGq%2FgRhayuTfQ3CQSrcA3PHegc9DnHbuS4l5ZQ7F1%2BT5TBMek%2BvCjYBpwo5ZqqRRZNbhtJUvDjpxMoVLm5QjhqMddFSIrq4jq%2BE6mTrZjF0vxul0nev5EPdtp71R0QfgDOKuAKQcpmuDTX0oUb3Bu1336Qnves1i2H9V2%2Bv4AyGNPiYVRslA4aUB73J1wmUaAuO1tnIxQb48wJFsEK6%2Fm%2BA0b2rEYAiM00AQxaIg7Ih6bVtuzrfabchQl6u5TjMRFLCMp3tPlmZtDJlLLbExzKw8P8RpyBQ6hsN%2BVFsR%2BDVaIsmb10UuDNJWqW6CHj0eo5UJen8BoNBK5cHbTP2%2BrPnIYpsfckYM16f7rhXzC98LX7Z2D58AD8JUZwG%2Bmv2Ec7QfpdxADA6tQErDmtP10odopS0oqJn3h5ney%2FWI65viixJUeVDw%2FQOZesS%2BHXT6LJ7MtjtKm2Kue67aLsprYap9quVr%2FD7%2FO2EJArV66YaBphBv%2BrUce4111yXJLCO%2BROSewAuRfigs%2Br0PR4qjfkVl5FDCE%2BStb6E0VnxHznVY1Hi6NIYcIFF%2BMzG8juKWhjklWrAXOmwghY3mz88rAA9AU1GkK0gGvjusEHdeOIFJCss%2BFsqVX63L%2BOVnCJxhDsN%2BtylRZFJMrVdMJDtnM4GOqUB3SKkgn7pjA%2Fv4sGsvbabJivK0hUmi1rTSvWo7GpwXk2C7mgYjLrD67TmGrnmMHG5ggOGGX5InXeIDm6Ju%2FMHtN%2BTUmyRMXefYDVRs%2FmaRqvLZBbUdrueKrWs%2FT7lV2tWyJVpLa0ZEzG85%2BFKfZauOz8%2FIeGIVunWOuw7kqfyu9uQPqIC2ChCzR31UwQThdllWGee8to3nWpj0WCu77KPvWF6XSW1&X-Amz-Signature=e031e640b5d25637591881536529163b6c4a231d6a0467c79a957befa92745b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SIMXGP4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCpCEhQAIC0fJ3WNj%2F0dTHTIXIi8T4A%2Buq9bOyvjroHqAIgWRecHsiFCzFwADYIxcNv%2FIj5PsOYqbNCHmAU6q6slh4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGq%2FgRhayuTfQ3CQSrcA3PHegc9DnHbuS4l5ZQ7F1%2BT5TBMek%2BvCjYBpwo5ZqqRRZNbhtJUvDjpxMoVLm5QjhqMddFSIrq4jq%2BE6mTrZjF0vxul0nev5EPdtp71R0QfgDOKuAKQcpmuDTX0oUb3Bu1336Qnves1i2H9V2%2Bv4AyGNPiYVRslA4aUB73J1wmUaAuO1tnIxQb48wJFsEK6%2Fm%2BA0b2rEYAiM00AQxaIg7Ih6bVtuzrfabchQl6u5TjMRFLCMp3tPlmZtDJlLLbExzKw8P8RpyBQ6hsN%2BVFsR%2BDVaIsmb10UuDNJWqW6CHj0eo5UJen8BoNBK5cHbTP2%2BrPnIYpsfckYM16f7rhXzC98LX7Z2D58AD8JUZwG%2Bmv2Ec7QfpdxADA6tQErDmtP10odopS0oqJn3h5ney%2FWI65viixJUeVDw%2FQOZesS%2BHXT6LJ7MtjtKm2Kue67aLsprYap9quVr%2FD7%2FO2EJArV66YaBphBv%2BrUce4111yXJLCO%2BROSewAuRfigs%2Br0PR4qjfkVl5FDCE%2BStb6E0VnxHznVY1Hi6NIYcIFF%2BMzG8juKWhjklWrAXOmwghY3mz88rAA9AU1GkK0gGvjusEHdeOIFJCss%2BFsqVX63L%2BOVnCJxhDsN%2BtylRZFJMrVdMJDtnM4GOqUB3SKkgn7pjA%2Fv4sGsvbabJivK0hUmi1rTSvWo7GpwXk2C7mgYjLrD67TmGrnmMHG5ggOGGX5InXeIDm6Ju%2FMHtN%2BTUmyRMXefYDVRs%2FmaRqvLZBbUdrueKrWs%2FT7lV2tWyJVpLa0ZEzG85%2BFKfZauOz8%2FIeGIVunWOuw7kqfyu9uQPqIC2ChCzR31UwQThdllWGee8to3nWpj0WCu77KPvWF6XSW1&X-Amz-Signature=2caa60fc2242795ac6512043f7733c4847ccab69921eaf79c8ea0d2e42d51e58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SIMXGP4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCpCEhQAIC0fJ3WNj%2F0dTHTIXIi8T4A%2Buq9bOyvjroHqAIgWRecHsiFCzFwADYIxcNv%2FIj5PsOYqbNCHmAU6q6slh4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGq%2FgRhayuTfQ3CQSrcA3PHegc9DnHbuS4l5ZQ7F1%2BT5TBMek%2BvCjYBpwo5ZqqRRZNbhtJUvDjpxMoVLm5QjhqMddFSIrq4jq%2BE6mTrZjF0vxul0nev5EPdtp71R0QfgDOKuAKQcpmuDTX0oUb3Bu1336Qnves1i2H9V2%2Bv4AyGNPiYVRslA4aUB73J1wmUaAuO1tnIxQb48wJFsEK6%2Fm%2BA0b2rEYAiM00AQxaIg7Ih6bVtuzrfabchQl6u5TjMRFLCMp3tPlmZtDJlLLbExzKw8P8RpyBQ6hsN%2BVFsR%2BDVaIsmb10UuDNJWqW6CHj0eo5UJen8BoNBK5cHbTP2%2BrPnIYpsfckYM16f7rhXzC98LX7Z2D58AD8JUZwG%2Bmv2Ec7QfpdxADA6tQErDmtP10odopS0oqJn3h5ney%2FWI65viixJUeVDw%2FQOZesS%2BHXT6LJ7MtjtKm2Kue67aLsprYap9quVr%2FD7%2FO2EJArV66YaBphBv%2BrUce4111yXJLCO%2BROSewAuRfigs%2Br0PR4qjfkVl5FDCE%2BStb6E0VnxHznVY1Hi6NIYcIFF%2BMzG8juKWhjklWrAXOmwghY3mz88rAA9AU1GkK0gGvjusEHdeOIFJCss%2BFsqVX63L%2BOVnCJxhDsN%2BtylRZFJMrVdMJDtnM4GOqUB3SKkgn7pjA%2Fv4sGsvbabJivK0hUmi1rTSvWo7GpwXk2C7mgYjLrD67TmGrnmMHG5ggOGGX5InXeIDm6Ju%2FMHtN%2BTUmyRMXefYDVRs%2FmaRqvLZBbUdrueKrWs%2FT7lV2tWyJVpLa0ZEzG85%2BFKfZauOz8%2FIeGIVunWOuw7kqfyu9uQPqIC2ChCzR31UwQThdllWGee8to3nWpj0WCu77KPvWF6XSW1&X-Amz-Signature=c8dfc1759a16a8d69e43b9160699a4393a7bf97af4a87b4e3f47c67c1838f414&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SIMXGP4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCpCEhQAIC0fJ3WNj%2F0dTHTIXIi8T4A%2Buq9bOyvjroHqAIgWRecHsiFCzFwADYIxcNv%2FIj5PsOYqbNCHmAU6q6slh4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGq%2FgRhayuTfQ3CQSrcA3PHegc9DnHbuS4l5ZQ7F1%2BT5TBMek%2BvCjYBpwo5ZqqRRZNbhtJUvDjpxMoVLm5QjhqMddFSIrq4jq%2BE6mTrZjF0vxul0nev5EPdtp71R0QfgDOKuAKQcpmuDTX0oUb3Bu1336Qnves1i2H9V2%2Bv4AyGNPiYVRslA4aUB73J1wmUaAuO1tnIxQb48wJFsEK6%2Fm%2BA0b2rEYAiM00AQxaIg7Ih6bVtuzrfabchQl6u5TjMRFLCMp3tPlmZtDJlLLbExzKw8P8RpyBQ6hsN%2BVFsR%2BDVaIsmb10UuDNJWqW6CHj0eo5UJen8BoNBK5cHbTP2%2BrPnIYpsfckYM16f7rhXzC98LX7Z2D58AD8JUZwG%2Bmv2Ec7QfpdxADA6tQErDmtP10odopS0oqJn3h5ney%2FWI65viixJUeVDw%2FQOZesS%2BHXT6LJ7MtjtKm2Kue67aLsprYap9quVr%2FD7%2FO2EJArV66YaBphBv%2BrUce4111yXJLCO%2BROSewAuRfigs%2Br0PR4qjfkVl5FDCE%2BStb6E0VnxHznVY1Hi6NIYcIFF%2BMzG8juKWhjklWrAXOmwghY3mz88rAA9AU1GkK0gGvjusEHdeOIFJCss%2BFsqVX63L%2BOVnCJxhDsN%2BtylRZFJMrVdMJDtnM4GOqUB3SKkgn7pjA%2Fv4sGsvbabJivK0hUmi1rTSvWo7GpwXk2C7mgYjLrD67TmGrnmMHG5ggOGGX5InXeIDm6Ju%2FMHtN%2BTUmyRMXefYDVRs%2FmaRqvLZBbUdrueKrWs%2FT7lV2tWyJVpLa0ZEzG85%2BFKfZauOz8%2FIeGIVunWOuw7kqfyu9uQPqIC2ChCzR31UwQThdllWGee8to3nWpj0WCu77KPvWF6XSW1&X-Amz-Signature=c92b304aac8ddc2c2296d496ee9a41fd1ee64f579719435e2429f544bf7aebc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SIMXGP4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCpCEhQAIC0fJ3WNj%2F0dTHTIXIi8T4A%2Buq9bOyvjroHqAIgWRecHsiFCzFwADYIxcNv%2FIj5PsOYqbNCHmAU6q6slh4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGq%2FgRhayuTfQ3CQSrcA3PHegc9DnHbuS4l5ZQ7F1%2BT5TBMek%2BvCjYBpwo5ZqqRRZNbhtJUvDjpxMoVLm5QjhqMddFSIrq4jq%2BE6mTrZjF0vxul0nev5EPdtp71R0QfgDOKuAKQcpmuDTX0oUb3Bu1336Qnves1i2H9V2%2Bv4AyGNPiYVRslA4aUB73J1wmUaAuO1tnIxQb48wJFsEK6%2Fm%2BA0b2rEYAiM00AQxaIg7Ih6bVtuzrfabchQl6u5TjMRFLCMp3tPlmZtDJlLLbExzKw8P8RpyBQ6hsN%2BVFsR%2BDVaIsmb10UuDNJWqW6CHj0eo5UJen8BoNBK5cHbTP2%2BrPnIYpsfckYM16f7rhXzC98LX7Z2D58AD8JUZwG%2Bmv2Ec7QfpdxADA6tQErDmtP10odopS0oqJn3h5ney%2FWI65viixJUeVDw%2FQOZesS%2BHXT6LJ7MtjtKm2Kue67aLsprYap9quVr%2FD7%2FO2EJArV66YaBphBv%2BrUce4111yXJLCO%2BROSewAuRfigs%2Br0PR4qjfkVl5FDCE%2BStb6E0VnxHznVY1Hi6NIYcIFF%2BMzG8juKWhjklWrAXOmwghY3mz88rAA9AU1GkK0gGvjusEHdeOIFJCss%2BFsqVX63L%2BOVnCJxhDsN%2BtylRZFJMrVdMJDtnM4GOqUB3SKkgn7pjA%2Fv4sGsvbabJivK0hUmi1rTSvWo7GpwXk2C7mgYjLrD67TmGrnmMHG5ggOGGX5InXeIDm6Ju%2FMHtN%2BTUmyRMXefYDVRs%2FmaRqvLZBbUdrueKrWs%2FT7lV2tWyJVpLa0ZEzG85%2BFKfZauOz8%2FIeGIVunWOuw7kqfyu9uQPqIC2ChCzR31UwQThdllWGee8to3nWpj0WCu77KPvWF6XSW1&X-Amz-Signature=f2171a4f6a98ca23fc5f6d67d92357c7c05a0eca6623cfa82fb3d0b8d6617513&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SIMXGP4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCpCEhQAIC0fJ3WNj%2F0dTHTIXIi8T4A%2Buq9bOyvjroHqAIgWRecHsiFCzFwADYIxcNv%2FIj5PsOYqbNCHmAU6q6slh4qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBGq%2FgRhayuTfQ3CQSrcA3PHegc9DnHbuS4l5ZQ7F1%2BT5TBMek%2BvCjYBpwo5ZqqRRZNbhtJUvDjpxMoVLm5QjhqMddFSIrq4jq%2BE6mTrZjF0vxul0nev5EPdtp71R0QfgDOKuAKQcpmuDTX0oUb3Bu1336Qnves1i2H9V2%2Bv4AyGNPiYVRslA4aUB73J1wmUaAuO1tnIxQb48wJFsEK6%2Fm%2BA0b2rEYAiM00AQxaIg7Ih6bVtuzrfabchQl6u5TjMRFLCMp3tPlmZtDJlLLbExzKw8P8RpyBQ6hsN%2BVFsR%2BDVaIsmb10UuDNJWqW6CHj0eo5UJen8BoNBK5cHbTP2%2BrPnIYpsfckYM16f7rhXzC98LX7Z2D58AD8JUZwG%2Bmv2Ec7QfpdxADA6tQErDmtP10odopS0oqJn3h5ney%2FWI65viixJUeVDw%2FQOZesS%2BHXT6LJ7MtjtKm2Kue67aLsprYap9quVr%2FD7%2FO2EJArV66YaBphBv%2BrUce4111yXJLCO%2BROSewAuRfigs%2Br0PR4qjfkVl5FDCE%2BStb6E0VnxHznVY1Hi6NIYcIFF%2BMzG8juKWhjklWrAXOmwghY3mz88rAA9AU1GkK0gGvjusEHdeOIFJCss%2BFsqVX63L%2BOVnCJxhDsN%2BtylRZFJMrVdMJDtnM4GOqUB3SKkgn7pjA%2Fv4sGsvbabJivK0hUmi1rTSvWo7GpwXk2C7mgYjLrD67TmGrnmMHG5ggOGGX5InXeIDm6Ju%2FMHtN%2BTUmyRMXefYDVRs%2FmaRqvLZBbUdrueKrWs%2FT7lV2tWyJVpLa0ZEzG85%2BFKfZauOz8%2FIeGIVunWOuw7kqfyu9uQPqIC2ChCzR31UwQThdllWGee8to3nWpj0WCu77KPvWF6XSW1&X-Amz-Signature=38d3ec90c5c43c5ad25c1585fbcc825c3a625d4e43c50991bc436098f22cd833&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

