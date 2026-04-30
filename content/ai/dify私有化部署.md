<<<<<<< HEAD
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

=======
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIC3SNKF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHgc9VNrJR40Y8BzrDPjz%2BYR%2FxHeTGHDt06qbtoItrZ%2BAiBz%2BJ3RhwJCGSNoH10rRN77kXIJYa5t41IUfwsqv5ASJCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMXrwiYHQm2gQpsj%2BvKtwDO4110%2BP7VVZFkLQTYeHY4HYxuBG6vlnHaQonPcrwkxwOMiXulK%2BFyCybvIzz8KGcadTM4zKI0Mj6IIW9NSs14%2Fowiqu3ML99ju09tyao6F8H3ee23NsnNAZpI3pWzwltN2kQLz1dFetC%2BXydXI8iliO6l6neyS5cigzUa8tm6whLuzWA%2FNl2qOJolGHJa9tWq9yGy5amPkojzUepPRUvmkhyngirvjsDhZeV%2F8%2BZ%2FDSgxXKWVZUigYeBv1acavEmYuBnU9En9fWaq%2BT1AfrKALjm8i%2F5rOwuII%2F6P8WzvZvVE4H0CBtXc3aQtrPuwPcJry5kaDDo6NSMmyRQ8qW8fzmz96P6icbuwoIKGOfgP5nGlE50ItzHRyRCMzGJ%2BO0FLyG9QL3TFmVb0XjVYfgCAYcfBguYCI91MsSebZH8mYBns2IA6XB9nCoQc0skQ%2Fda%2FmXWZtIlG0XrvjlGjUnVLRcNN687VEn6SE0pk2%2B23DoXoyJJnL0KIcb5Z%2Btf3p08jne5%2FzaJo8RCeUQ%2FMPqInRxKuCWxOqFmB2jHllqqU8qGzXbdZnkSZVGXh7K149NwvvivS%2FalBEvFLBBllfOicJbrbA9C7lOJacawZ3c4B8NC3w8WcSbu6%2B53ZWswgp3MzwY6pgFwlN9AalBHzN5M3JJf%2BOjH2QomU2HvWgkMaDiFIbQSIHxM%2Bv8QGxQD9RS97JZ%2BNY3aYEnmw%2BV8ct%2BV3cRaLNW1PwyQ9F1HIBznaPV7fGpDcSRtlEPtb2ejJSpLphuzTam9%2FUsVbbAeE24%2FeW2z6IEUJx9%2Bz56BqxkszesiHbfDyolKOj%2BAwCeRPR5lfOw5E%2FC1AB7afM63nzkDf4q93memwYt83AaQ&X-Amz-Signature=2922d083add8d637907ac20d3ec6af96e5e03c9c0c04e40f813b06a6efb40509&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIC3SNKF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHgc9VNrJR40Y8BzrDPjz%2BYR%2FxHeTGHDt06qbtoItrZ%2BAiBz%2BJ3RhwJCGSNoH10rRN77kXIJYa5t41IUfwsqv5ASJCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMXrwiYHQm2gQpsj%2BvKtwDO4110%2BP7VVZFkLQTYeHY4HYxuBG6vlnHaQonPcrwkxwOMiXulK%2BFyCybvIzz8KGcadTM4zKI0Mj6IIW9NSs14%2Fowiqu3ML99ju09tyao6F8H3ee23NsnNAZpI3pWzwltN2kQLz1dFetC%2BXydXI8iliO6l6neyS5cigzUa8tm6whLuzWA%2FNl2qOJolGHJa9tWq9yGy5amPkojzUepPRUvmkhyngirvjsDhZeV%2F8%2BZ%2FDSgxXKWVZUigYeBv1acavEmYuBnU9En9fWaq%2BT1AfrKALjm8i%2F5rOwuII%2F6P8WzvZvVE4H0CBtXc3aQtrPuwPcJry5kaDDo6NSMmyRQ8qW8fzmz96P6icbuwoIKGOfgP5nGlE50ItzHRyRCMzGJ%2BO0FLyG9QL3TFmVb0XjVYfgCAYcfBguYCI91MsSebZH8mYBns2IA6XB9nCoQc0skQ%2Fda%2FmXWZtIlG0XrvjlGjUnVLRcNN687VEn6SE0pk2%2B23DoXoyJJnL0KIcb5Z%2Btf3p08jne5%2FzaJo8RCeUQ%2FMPqInRxKuCWxOqFmB2jHllqqU8qGzXbdZnkSZVGXh7K149NwvvivS%2FalBEvFLBBllfOicJbrbA9C7lOJacawZ3c4B8NC3w8WcSbu6%2B53ZWswgp3MzwY6pgFwlN9AalBHzN5M3JJf%2BOjH2QomU2HvWgkMaDiFIbQSIHxM%2Bv8QGxQD9RS97JZ%2BNY3aYEnmw%2BV8ct%2BV3cRaLNW1PwyQ9F1HIBznaPV7fGpDcSRtlEPtb2ejJSpLphuzTam9%2FUsVbbAeE24%2FeW2z6IEUJx9%2Bz56BqxkszesiHbfDyolKOj%2BAwCeRPR5lfOw5E%2FC1AB7afM63nzkDf4q93memwYt83AaQ&X-Amz-Signature=dca4a168e90a3a7b3bfd6c54df73294b33776cc5490db230e16ec4606c239709&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIC3SNKF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHgc9VNrJR40Y8BzrDPjz%2BYR%2FxHeTGHDt06qbtoItrZ%2BAiBz%2BJ3RhwJCGSNoH10rRN77kXIJYa5t41IUfwsqv5ASJCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMXrwiYHQm2gQpsj%2BvKtwDO4110%2BP7VVZFkLQTYeHY4HYxuBG6vlnHaQonPcrwkxwOMiXulK%2BFyCybvIzz8KGcadTM4zKI0Mj6IIW9NSs14%2Fowiqu3ML99ju09tyao6F8H3ee23NsnNAZpI3pWzwltN2kQLz1dFetC%2BXydXI8iliO6l6neyS5cigzUa8tm6whLuzWA%2FNl2qOJolGHJa9tWq9yGy5amPkojzUepPRUvmkhyngirvjsDhZeV%2F8%2BZ%2FDSgxXKWVZUigYeBv1acavEmYuBnU9En9fWaq%2BT1AfrKALjm8i%2F5rOwuII%2F6P8WzvZvVE4H0CBtXc3aQtrPuwPcJry5kaDDo6NSMmyRQ8qW8fzmz96P6icbuwoIKGOfgP5nGlE50ItzHRyRCMzGJ%2BO0FLyG9QL3TFmVb0XjVYfgCAYcfBguYCI91MsSebZH8mYBns2IA6XB9nCoQc0skQ%2Fda%2FmXWZtIlG0XrvjlGjUnVLRcNN687VEn6SE0pk2%2B23DoXoyJJnL0KIcb5Z%2Btf3p08jne5%2FzaJo8RCeUQ%2FMPqInRxKuCWxOqFmB2jHllqqU8qGzXbdZnkSZVGXh7K149NwvvivS%2FalBEvFLBBllfOicJbrbA9C7lOJacawZ3c4B8NC3w8WcSbu6%2B53ZWswgp3MzwY6pgFwlN9AalBHzN5M3JJf%2BOjH2QomU2HvWgkMaDiFIbQSIHxM%2Bv8QGxQD9RS97JZ%2BNY3aYEnmw%2BV8ct%2BV3cRaLNW1PwyQ9F1HIBznaPV7fGpDcSRtlEPtb2ejJSpLphuzTam9%2FUsVbbAeE24%2FeW2z6IEUJx9%2Bz56BqxkszesiHbfDyolKOj%2BAwCeRPR5lfOw5E%2FC1AB7afM63nzkDf4q93memwYt83AaQ&X-Amz-Signature=74fba1fa686c2b81e36261e7012a699b99eb3195f38144c4b509ad6ee9b242e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIC3SNKF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHgc9VNrJR40Y8BzrDPjz%2BYR%2FxHeTGHDt06qbtoItrZ%2BAiBz%2BJ3RhwJCGSNoH10rRN77kXIJYa5t41IUfwsqv5ASJCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMXrwiYHQm2gQpsj%2BvKtwDO4110%2BP7VVZFkLQTYeHY4HYxuBG6vlnHaQonPcrwkxwOMiXulK%2BFyCybvIzz8KGcadTM4zKI0Mj6IIW9NSs14%2Fowiqu3ML99ju09tyao6F8H3ee23NsnNAZpI3pWzwltN2kQLz1dFetC%2BXydXI8iliO6l6neyS5cigzUa8tm6whLuzWA%2FNl2qOJolGHJa9tWq9yGy5amPkojzUepPRUvmkhyngirvjsDhZeV%2F8%2BZ%2FDSgxXKWVZUigYeBv1acavEmYuBnU9En9fWaq%2BT1AfrKALjm8i%2F5rOwuII%2F6P8WzvZvVE4H0CBtXc3aQtrPuwPcJry5kaDDo6NSMmyRQ8qW8fzmz96P6icbuwoIKGOfgP5nGlE50ItzHRyRCMzGJ%2BO0FLyG9QL3TFmVb0XjVYfgCAYcfBguYCI91MsSebZH8mYBns2IA6XB9nCoQc0skQ%2Fda%2FmXWZtIlG0XrvjlGjUnVLRcNN687VEn6SE0pk2%2B23DoXoyJJnL0KIcb5Z%2Btf3p08jne5%2FzaJo8RCeUQ%2FMPqInRxKuCWxOqFmB2jHllqqU8qGzXbdZnkSZVGXh7K149NwvvivS%2FalBEvFLBBllfOicJbrbA9C7lOJacawZ3c4B8NC3w8WcSbu6%2B53ZWswgp3MzwY6pgFwlN9AalBHzN5M3JJf%2BOjH2QomU2HvWgkMaDiFIbQSIHxM%2Bv8QGxQD9RS97JZ%2BNY3aYEnmw%2BV8ct%2BV3cRaLNW1PwyQ9F1HIBznaPV7fGpDcSRtlEPtb2ejJSpLphuzTam9%2FUsVbbAeE24%2FeW2z6IEUJx9%2Bz56BqxkszesiHbfDyolKOj%2BAwCeRPR5lfOw5E%2FC1AB7afM63nzkDf4q93memwYt83AaQ&X-Amz-Signature=ccdbc552e1af4b52ba518d152caff31d22c6eb14bd45c1c8e250ba52a48a4b05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIC3SNKF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHgc9VNrJR40Y8BzrDPjz%2BYR%2FxHeTGHDt06qbtoItrZ%2BAiBz%2BJ3RhwJCGSNoH10rRN77kXIJYa5t41IUfwsqv5ASJCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMXrwiYHQm2gQpsj%2BvKtwDO4110%2BP7VVZFkLQTYeHY4HYxuBG6vlnHaQonPcrwkxwOMiXulK%2BFyCybvIzz8KGcadTM4zKI0Mj6IIW9NSs14%2Fowiqu3ML99ju09tyao6F8H3ee23NsnNAZpI3pWzwltN2kQLz1dFetC%2BXydXI8iliO6l6neyS5cigzUa8tm6whLuzWA%2FNl2qOJolGHJa9tWq9yGy5amPkojzUepPRUvmkhyngirvjsDhZeV%2F8%2BZ%2FDSgxXKWVZUigYeBv1acavEmYuBnU9En9fWaq%2BT1AfrKALjm8i%2F5rOwuII%2F6P8WzvZvVE4H0CBtXc3aQtrPuwPcJry5kaDDo6NSMmyRQ8qW8fzmz96P6icbuwoIKGOfgP5nGlE50ItzHRyRCMzGJ%2BO0FLyG9QL3TFmVb0XjVYfgCAYcfBguYCI91MsSebZH8mYBns2IA6XB9nCoQc0skQ%2Fda%2FmXWZtIlG0XrvjlGjUnVLRcNN687VEn6SE0pk2%2B23DoXoyJJnL0KIcb5Z%2Btf3p08jne5%2FzaJo8RCeUQ%2FMPqInRxKuCWxOqFmB2jHllqqU8qGzXbdZnkSZVGXh7K149NwvvivS%2FalBEvFLBBllfOicJbrbA9C7lOJacawZ3c4B8NC3w8WcSbu6%2B53ZWswgp3MzwY6pgFwlN9AalBHzN5M3JJf%2BOjH2QomU2HvWgkMaDiFIbQSIHxM%2Bv8QGxQD9RS97JZ%2BNY3aYEnmw%2BV8ct%2BV3cRaLNW1PwyQ9F1HIBznaPV7fGpDcSRtlEPtb2ejJSpLphuzTam9%2FUsVbbAeE24%2FeW2z6IEUJx9%2Bz56BqxkszesiHbfDyolKOj%2BAwCeRPR5lfOw5E%2FC1AB7afM63nzkDf4q93memwYt83AaQ&X-Amz-Signature=dede8771c3277c4964fea2412ecde4b61261b01eb518a2450428f6b2d22a8deb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIC3SNKF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHgc9VNrJR40Y8BzrDPjz%2BYR%2FxHeTGHDt06qbtoItrZ%2BAiBz%2BJ3RhwJCGSNoH10rRN77kXIJYa5t41IUfwsqv5ASJCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMXrwiYHQm2gQpsj%2BvKtwDO4110%2BP7VVZFkLQTYeHY4HYxuBG6vlnHaQonPcrwkxwOMiXulK%2BFyCybvIzz8KGcadTM4zKI0Mj6IIW9NSs14%2Fowiqu3ML99ju09tyao6F8H3ee23NsnNAZpI3pWzwltN2kQLz1dFetC%2BXydXI8iliO6l6neyS5cigzUa8tm6whLuzWA%2FNl2qOJolGHJa9tWq9yGy5amPkojzUepPRUvmkhyngirvjsDhZeV%2F8%2BZ%2FDSgxXKWVZUigYeBv1acavEmYuBnU9En9fWaq%2BT1AfrKALjm8i%2F5rOwuII%2F6P8WzvZvVE4H0CBtXc3aQtrPuwPcJry5kaDDo6NSMmyRQ8qW8fzmz96P6icbuwoIKGOfgP5nGlE50ItzHRyRCMzGJ%2BO0FLyG9QL3TFmVb0XjVYfgCAYcfBguYCI91MsSebZH8mYBns2IA6XB9nCoQc0skQ%2Fda%2FmXWZtIlG0XrvjlGjUnVLRcNN687VEn6SE0pk2%2B23DoXoyJJnL0KIcb5Z%2Btf3p08jne5%2FzaJo8RCeUQ%2FMPqInRxKuCWxOqFmB2jHllqqU8qGzXbdZnkSZVGXh7K149NwvvivS%2FalBEvFLBBllfOicJbrbA9C7lOJacawZ3c4B8NC3w8WcSbu6%2B53ZWswgp3MzwY6pgFwlN9AalBHzN5M3JJf%2BOjH2QomU2HvWgkMaDiFIbQSIHxM%2Bv8QGxQD9RS97JZ%2BNY3aYEnmw%2BV8ct%2BV3cRaLNW1PwyQ9F1HIBznaPV7fGpDcSRtlEPtb2ejJSpLphuzTam9%2FUsVbbAeE24%2FeW2z6IEUJx9%2Bz56BqxkszesiHbfDyolKOj%2BAwCeRPR5lfOw5E%2FC1AB7afM63nzkDf4q93memwYt83AaQ&X-Amz-Signature=a3efa3e816cde25bd9a514ef1bf82546ab2508bf5f0038d218bb7474c1930f8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIC3SNKF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHgc9VNrJR40Y8BzrDPjz%2BYR%2FxHeTGHDt06qbtoItrZ%2BAiBz%2BJ3RhwJCGSNoH10rRN77kXIJYa5t41IUfwsqv5ASJCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMXrwiYHQm2gQpsj%2BvKtwDO4110%2BP7VVZFkLQTYeHY4HYxuBG6vlnHaQonPcrwkxwOMiXulK%2BFyCybvIzz8KGcadTM4zKI0Mj6IIW9NSs14%2Fowiqu3ML99ju09tyao6F8H3ee23NsnNAZpI3pWzwltN2kQLz1dFetC%2BXydXI8iliO6l6neyS5cigzUa8tm6whLuzWA%2FNl2qOJolGHJa9tWq9yGy5amPkojzUepPRUvmkhyngirvjsDhZeV%2F8%2BZ%2FDSgxXKWVZUigYeBv1acavEmYuBnU9En9fWaq%2BT1AfrKALjm8i%2F5rOwuII%2F6P8WzvZvVE4H0CBtXc3aQtrPuwPcJry5kaDDo6NSMmyRQ8qW8fzmz96P6icbuwoIKGOfgP5nGlE50ItzHRyRCMzGJ%2BO0FLyG9QL3TFmVb0XjVYfgCAYcfBguYCI91MsSebZH8mYBns2IA6XB9nCoQc0skQ%2Fda%2FmXWZtIlG0XrvjlGjUnVLRcNN687VEn6SE0pk2%2B23DoXoyJJnL0KIcb5Z%2Btf3p08jne5%2FzaJo8RCeUQ%2FMPqInRxKuCWxOqFmB2jHllqqU8qGzXbdZnkSZVGXh7K149NwvvivS%2FalBEvFLBBllfOicJbrbA9C7lOJacawZ3c4B8NC3w8WcSbu6%2B53ZWswgp3MzwY6pgFwlN9AalBHzN5M3JJf%2BOjH2QomU2HvWgkMaDiFIbQSIHxM%2Bv8QGxQD9RS97JZ%2BNY3aYEnmw%2BV8ct%2BV3cRaLNW1PwyQ9F1HIBznaPV7fGpDcSRtlEPtb2ejJSpLphuzTam9%2FUsVbbAeE24%2FeW2z6IEUJx9%2Bz56BqxkszesiHbfDyolKOj%2BAwCeRPR5lfOw5E%2FC1AB7afM63nzkDf4q93memwYt83AaQ&X-Amz-Signature=8207609c13e186094fc01af7f9c33fe2f3d0f9b991b3efbee1f39270a8582704&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIC3SNKF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHgc9VNrJR40Y8BzrDPjz%2BYR%2FxHeTGHDt06qbtoItrZ%2BAiBz%2BJ3RhwJCGSNoH10rRN77kXIJYa5t41IUfwsqv5ASJCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMXrwiYHQm2gQpsj%2BvKtwDO4110%2BP7VVZFkLQTYeHY4HYxuBG6vlnHaQonPcrwkxwOMiXulK%2BFyCybvIzz8KGcadTM4zKI0Mj6IIW9NSs14%2Fowiqu3ML99ju09tyao6F8H3ee23NsnNAZpI3pWzwltN2kQLz1dFetC%2BXydXI8iliO6l6neyS5cigzUa8tm6whLuzWA%2FNl2qOJolGHJa9tWq9yGy5amPkojzUepPRUvmkhyngirvjsDhZeV%2F8%2BZ%2FDSgxXKWVZUigYeBv1acavEmYuBnU9En9fWaq%2BT1AfrKALjm8i%2F5rOwuII%2F6P8WzvZvVE4H0CBtXc3aQtrPuwPcJry5kaDDo6NSMmyRQ8qW8fzmz96P6icbuwoIKGOfgP5nGlE50ItzHRyRCMzGJ%2BO0FLyG9QL3TFmVb0XjVYfgCAYcfBguYCI91MsSebZH8mYBns2IA6XB9nCoQc0skQ%2Fda%2FmXWZtIlG0XrvjlGjUnVLRcNN687VEn6SE0pk2%2B23DoXoyJJnL0KIcb5Z%2Btf3p08jne5%2FzaJo8RCeUQ%2FMPqInRxKuCWxOqFmB2jHllqqU8qGzXbdZnkSZVGXh7K149NwvvivS%2FalBEvFLBBllfOicJbrbA9C7lOJacawZ3c4B8NC3w8WcSbu6%2B53ZWswgp3MzwY6pgFwlN9AalBHzN5M3JJf%2BOjH2QomU2HvWgkMaDiFIbQSIHxM%2Bv8QGxQD9RS97JZ%2BNY3aYEnmw%2BV8ct%2BV3cRaLNW1PwyQ9F1HIBznaPV7fGpDcSRtlEPtb2ejJSpLphuzTam9%2FUsVbbAeE24%2FeW2z6IEUJx9%2Bz56BqxkszesiHbfDyolKOj%2BAwCeRPR5lfOw5E%2FC1AB7afM63nzkDf4q93memwYt83AaQ&X-Amz-Signature=059a3bb16a8b2b60ac5b3e08e4f47dad32c12128904aec4770d335d116d7883f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIC3SNKF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHgc9VNrJR40Y8BzrDPjz%2BYR%2FxHeTGHDt06qbtoItrZ%2BAiBz%2BJ3RhwJCGSNoH10rRN77kXIJYa5t41IUfwsqv5ASJCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMXrwiYHQm2gQpsj%2BvKtwDO4110%2BP7VVZFkLQTYeHY4HYxuBG6vlnHaQonPcrwkxwOMiXulK%2BFyCybvIzz8KGcadTM4zKI0Mj6IIW9NSs14%2Fowiqu3ML99ju09tyao6F8H3ee23NsnNAZpI3pWzwltN2kQLz1dFetC%2BXydXI8iliO6l6neyS5cigzUa8tm6whLuzWA%2FNl2qOJolGHJa9tWq9yGy5amPkojzUepPRUvmkhyngirvjsDhZeV%2F8%2BZ%2FDSgxXKWVZUigYeBv1acavEmYuBnU9En9fWaq%2BT1AfrKALjm8i%2F5rOwuII%2F6P8WzvZvVE4H0CBtXc3aQtrPuwPcJry5kaDDo6NSMmyRQ8qW8fzmz96P6icbuwoIKGOfgP5nGlE50ItzHRyRCMzGJ%2BO0FLyG9QL3TFmVb0XjVYfgCAYcfBguYCI91MsSebZH8mYBns2IA6XB9nCoQc0skQ%2Fda%2FmXWZtIlG0XrvjlGjUnVLRcNN687VEn6SE0pk2%2B23DoXoyJJnL0KIcb5Z%2Btf3p08jne5%2FzaJo8RCeUQ%2FMPqInRxKuCWxOqFmB2jHllqqU8qGzXbdZnkSZVGXh7K149NwvvivS%2FalBEvFLBBllfOicJbrbA9C7lOJacawZ3c4B8NC3w8WcSbu6%2B53ZWswgp3MzwY6pgFwlN9AalBHzN5M3JJf%2BOjH2QomU2HvWgkMaDiFIbQSIHxM%2Bv8QGxQD9RS97JZ%2BNY3aYEnmw%2BV8ct%2BV3cRaLNW1PwyQ9F1HIBznaPV7fGpDcSRtlEPtb2ejJSpLphuzTam9%2FUsVbbAeE24%2FeW2z6IEUJx9%2Bz56BqxkszesiHbfDyolKOj%2BAwCeRPR5lfOw5E%2FC1AB7afM63nzkDf4q93memwYt83AaQ&X-Amz-Signature=cd39213c70f404b599ad658fb846605f290679fe5863d5b08d1d04a3a7bc330e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIC3SNKF%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIHgc9VNrJR40Y8BzrDPjz%2BYR%2FxHeTGHDt06qbtoItrZ%2BAiBz%2BJ3RhwJCGSNoH10rRN77kXIJYa5t41IUfwsqv5ASJCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMXrwiYHQm2gQpsj%2BvKtwDO4110%2BP7VVZFkLQTYeHY4HYxuBG6vlnHaQonPcrwkxwOMiXulK%2BFyCybvIzz8KGcadTM4zKI0Mj6IIW9NSs14%2Fowiqu3ML99ju09tyao6F8H3ee23NsnNAZpI3pWzwltN2kQLz1dFetC%2BXydXI8iliO6l6neyS5cigzUa8tm6whLuzWA%2FNl2qOJolGHJa9tWq9yGy5amPkojzUepPRUvmkhyngirvjsDhZeV%2F8%2BZ%2FDSgxXKWVZUigYeBv1acavEmYuBnU9En9fWaq%2BT1AfrKALjm8i%2F5rOwuII%2F6P8WzvZvVE4H0CBtXc3aQtrPuwPcJry5kaDDo6NSMmyRQ8qW8fzmz96P6icbuwoIKGOfgP5nGlE50ItzHRyRCMzGJ%2BO0FLyG9QL3TFmVb0XjVYfgCAYcfBguYCI91MsSebZH8mYBns2IA6XB9nCoQc0skQ%2Fda%2FmXWZtIlG0XrvjlGjUnVLRcNN687VEn6SE0pk2%2B23DoXoyJJnL0KIcb5Z%2Btf3p08jne5%2FzaJo8RCeUQ%2FMPqInRxKuCWxOqFmB2jHllqqU8qGzXbdZnkSZVGXh7K149NwvvivS%2FalBEvFLBBllfOicJbrbA9C7lOJacawZ3c4B8NC3w8WcSbu6%2B53ZWswgp3MzwY6pgFwlN9AalBHzN5M3JJf%2BOjH2QomU2HvWgkMaDiFIbQSIHxM%2Bv8QGxQD9RS97JZ%2BNY3aYEnmw%2BV8ct%2BV3cRaLNW1PwyQ9F1HIBznaPV7fGpDcSRtlEPtb2ejJSpLphuzTam9%2FUsVbbAeE24%2FeW2z6IEUJx9%2Bz56BqxkszesiHbfDyolKOj%2BAwCeRPR5lfOw5E%2FC1AB7afM63nzkDf4q93memwYt83AaQ&X-Amz-Signature=84acd413f6885b9e38b12cdd4285cd56fb77a0f589fb9cbf02a2af48ff373357&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

>>>>>>> 67e2e8ba81abbca0065a5254fe8b7b646ead6176
