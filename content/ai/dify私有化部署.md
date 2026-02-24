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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GIINS5S%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAU5BeHLQwodSUpg%2BqycfFW%2BBnJbh7eZodzP%2BwpJ5Bg%2BAiAHYizLIzUNacVVmH8cZG7%2BRTbJIe6boYYRum4C0%2BTNUCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4jtJfyMMHHR2p5BxKtwDddR8X9%2Fqye0%2Bi5%2F2feFvkZkcqEGX6essIFX%2FXr9yJMHd1uvRntLyGlO8koWo7uzqBmRdrCY2NsyqLkZwAZrEdmsQzWvciCg9mrTuaS82AONpT3HM1hSRMnsj9fhaumue6Utnnh0nysw8CkrkyGIw62L9y7YecyDv%2B2KjwDevr3IzFAVeS7DnGeKQziezffYpXjX%2FvXFyGsYcN9nO1hGUJ7f6pu5XBH7oDNkXGHIpok7KglIEihqj%2BoM4f4jHngtKOLMCA26QEor0at0sYIy9%2FbIdxkBWjihjTQ4BqrwjttYlrc5DLXzoz3kUSCb5nz0suULFOhjRXDiqj0OyKsOJnQ9ifW9MEZzIjB%2F3Mzw%2FYCSOg%2F3HKOkpLHBKP%2BLu%2BblRO3XenuHBwDHHymlTTKNfr8rKhzqlC3aoVsoKDmD7Ln1y4ZHgFTe31YPq0F7eddvJrcVkxVyFEqXIUxkqYOzLtY%2FKp4mXe2go8cvnnk%2BXz27vguEW%2BGdJE2fm3Ppq58ymBbgZrNglNfAzocD%2BlzFp1wXHdfAkPD63D5tv9b3MPSzF6Eq8JfHhgYxqgikSwJL4ZpfsO9tWlsriNxLz01dKp67Ee2Uqo%2BZ3OGehs3xQzIjU%2FkTJvJ1luwFthhgwhrb0zAY6pgFKWpRJ5vUkZWynSfTc11YqOWzaUPgWMgy%2BDJ1vNJ2OzXlGYEdtS0%2FiKuKqbDiWfXp5nkInJvvvyvfaIKX%2FN%2BA6U%2BNsi%2Foah5QG8vljfuNdHODp9qaKB9a%2F7hCvMyKJAsEg2Q%2FvNv0jrFNPzajoEgSJn3CvVxnOxgIa176gxUtul7r3X02bbnJ11FTmQE%2FMNj04z4CxWlVyekG8%2BDDX5Pr%2BgOxBcWQe&X-Amz-Signature=19344865763562311d04c4fb9625943a8338dc8b6b066ce4a8cdef2ba0da6198&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GIINS5S%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAU5BeHLQwodSUpg%2BqycfFW%2BBnJbh7eZodzP%2BwpJ5Bg%2BAiAHYizLIzUNacVVmH8cZG7%2BRTbJIe6boYYRum4C0%2BTNUCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4jtJfyMMHHR2p5BxKtwDddR8X9%2Fqye0%2Bi5%2F2feFvkZkcqEGX6essIFX%2FXr9yJMHd1uvRntLyGlO8koWo7uzqBmRdrCY2NsyqLkZwAZrEdmsQzWvciCg9mrTuaS82AONpT3HM1hSRMnsj9fhaumue6Utnnh0nysw8CkrkyGIw62L9y7YecyDv%2B2KjwDevr3IzFAVeS7DnGeKQziezffYpXjX%2FvXFyGsYcN9nO1hGUJ7f6pu5XBH7oDNkXGHIpok7KglIEihqj%2BoM4f4jHngtKOLMCA26QEor0at0sYIy9%2FbIdxkBWjihjTQ4BqrwjttYlrc5DLXzoz3kUSCb5nz0suULFOhjRXDiqj0OyKsOJnQ9ifW9MEZzIjB%2F3Mzw%2FYCSOg%2F3HKOkpLHBKP%2BLu%2BblRO3XenuHBwDHHymlTTKNfr8rKhzqlC3aoVsoKDmD7Ln1y4ZHgFTe31YPq0F7eddvJrcVkxVyFEqXIUxkqYOzLtY%2FKp4mXe2go8cvnnk%2BXz27vguEW%2BGdJE2fm3Ppq58ymBbgZrNglNfAzocD%2BlzFp1wXHdfAkPD63D5tv9b3MPSzF6Eq8JfHhgYxqgikSwJL4ZpfsO9tWlsriNxLz01dKp67Ee2Uqo%2BZ3OGehs3xQzIjU%2FkTJvJ1luwFthhgwhrb0zAY6pgFKWpRJ5vUkZWynSfTc11YqOWzaUPgWMgy%2BDJ1vNJ2OzXlGYEdtS0%2FiKuKqbDiWfXp5nkInJvvvyvfaIKX%2FN%2BA6U%2BNsi%2Foah5QG8vljfuNdHODp9qaKB9a%2F7hCvMyKJAsEg2Q%2FvNv0jrFNPzajoEgSJn3CvVxnOxgIa176gxUtul7r3X02bbnJ11FTmQE%2FMNj04z4CxWlVyekG8%2BDDX5Pr%2BgOxBcWQe&X-Amz-Signature=e1b0816ed2de02b671b6fca49d3efc1c372a97a7243e2fa54ff286f226a3a4f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GIINS5S%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAU5BeHLQwodSUpg%2BqycfFW%2BBnJbh7eZodzP%2BwpJ5Bg%2BAiAHYizLIzUNacVVmH8cZG7%2BRTbJIe6boYYRum4C0%2BTNUCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4jtJfyMMHHR2p5BxKtwDddR8X9%2Fqye0%2Bi5%2F2feFvkZkcqEGX6essIFX%2FXr9yJMHd1uvRntLyGlO8koWo7uzqBmRdrCY2NsyqLkZwAZrEdmsQzWvciCg9mrTuaS82AONpT3HM1hSRMnsj9fhaumue6Utnnh0nysw8CkrkyGIw62L9y7YecyDv%2B2KjwDevr3IzFAVeS7DnGeKQziezffYpXjX%2FvXFyGsYcN9nO1hGUJ7f6pu5XBH7oDNkXGHIpok7KglIEihqj%2BoM4f4jHngtKOLMCA26QEor0at0sYIy9%2FbIdxkBWjihjTQ4BqrwjttYlrc5DLXzoz3kUSCb5nz0suULFOhjRXDiqj0OyKsOJnQ9ifW9MEZzIjB%2F3Mzw%2FYCSOg%2F3HKOkpLHBKP%2BLu%2BblRO3XenuHBwDHHymlTTKNfr8rKhzqlC3aoVsoKDmD7Ln1y4ZHgFTe31YPq0F7eddvJrcVkxVyFEqXIUxkqYOzLtY%2FKp4mXe2go8cvnnk%2BXz27vguEW%2BGdJE2fm3Ppq58ymBbgZrNglNfAzocD%2BlzFp1wXHdfAkPD63D5tv9b3MPSzF6Eq8JfHhgYxqgikSwJL4ZpfsO9tWlsriNxLz01dKp67Ee2Uqo%2BZ3OGehs3xQzIjU%2FkTJvJ1luwFthhgwhrb0zAY6pgFKWpRJ5vUkZWynSfTc11YqOWzaUPgWMgy%2BDJ1vNJ2OzXlGYEdtS0%2FiKuKqbDiWfXp5nkInJvvvyvfaIKX%2FN%2BA6U%2BNsi%2Foah5QG8vljfuNdHODp9qaKB9a%2F7hCvMyKJAsEg2Q%2FvNv0jrFNPzajoEgSJn3CvVxnOxgIa176gxUtul7r3X02bbnJ11FTmQE%2FMNj04z4CxWlVyekG8%2BDDX5Pr%2BgOxBcWQe&X-Amz-Signature=1f6f9434d1f018b49ea8b8e64fe1edb798e9d297adbf5fc0a44149386d7fcdcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GIINS5S%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAU5BeHLQwodSUpg%2BqycfFW%2BBnJbh7eZodzP%2BwpJ5Bg%2BAiAHYizLIzUNacVVmH8cZG7%2BRTbJIe6boYYRum4C0%2BTNUCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4jtJfyMMHHR2p5BxKtwDddR8X9%2Fqye0%2Bi5%2F2feFvkZkcqEGX6essIFX%2FXr9yJMHd1uvRntLyGlO8koWo7uzqBmRdrCY2NsyqLkZwAZrEdmsQzWvciCg9mrTuaS82AONpT3HM1hSRMnsj9fhaumue6Utnnh0nysw8CkrkyGIw62L9y7YecyDv%2B2KjwDevr3IzFAVeS7DnGeKQziezffYpXjX%2FvXFyGsYcN9nO1hGUJ7f6pu5XBH7oDNkXGHIpok7KglIEihqj%2BoM4f4jHngtKOLMCA26QEor0at0sYIy9%2FbIdxkBWjihjTQ4BqrwjttYlrc5DLXzoz3kUSCb5nz0suULFOhjRXDiqj0OyKsOJnQ9ifW9MEZzIjB%2F3Mzw%2FYCSOg%2F3HKOkpLHBKP%2BLu%2BblRO3XenuHBwDHHymlTTKNfr8rKhzqlC3aoVsoKDmD7Ln1y4ZHgFTe31YPq0F7eddvJrcVkxVyFEqXIUxkqYOzLtY%2FKp4mXe2go8cvnnk%2BXz27vguEW%2BGdJE2fm3Ppq58ymBbgZrNglNfAzocD%2BlzFp1wXHdfAkPD63D5tv9b3MPSzF6Eq8JfHhgYxqgikSwJL4ZpfsO9tWlsriNxLz01dKp67Ee2Uqo%2BZ3OGehs3xQzIjU%2FkTJvJ1luwFthhgwhrb0zAY6pgFKWpRJ5vUkZWynSfTc11YqOWzaUPgWMgy%2BDJ1vNJ2OzXlGYEdtS0%2FiKuKqbDiWfXp5nkInJvvvyvfaIKX%2FN%2BA6U%2BNsi%2Foah5QG8vljfuNdHODp9qaKB9a%2F7hCvMyKJAsEg2Q%2FvNv0jrFNPzajoEgSJn3CvVxnOxgIa176gxUtul7r3X02bbnJ11FTmQE%2FMNj04z4CxWlVyekG8%2BDDX5Pr%2BgOxBcWQe&X-Amz-Signature=283e6f45c16c399021413afa734611df1789a11e8ece295d6785bc993cdba461&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GIINS5S%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAU5BeHLQwodSUpg%2BqycfFW%2BBnJbh7eZodzP%2BwpJ5Bg%2BAiAHYizLIzUNacVVmH8cZG7%2BRTbJIe6boYYRum4C0%2BTNUCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4jtJfyMMHHR2p5BxKtwDddR8X9%2Fqye0%2Bi5%2F2feFvkZkcqEGX6essIFX%2FXr9yJMHd1uvRntLyGlO8koWo7uzqBmRdrCY2NsyqLkZwAZrEdmsQzWvciCg9mrTuaS82AONpT3HM1hSRMnsj9fhaumue6Utnnh0nysw8CkrkyGIw62L9y7YecyDv%2B2KjwDevr3IzFAVeS7DnGeKQziezffYpXjX%2FvXFyGsYcN9nO1hGUJ7f6pu5XBH7oDNkXGHIpok7KglIEihqj%2BoM4f4jHngtKOLMCA26QEor0at0sYIy9%2FbIdxkBWjihjTQ4BqrwjttYlrc5DLXzoz3kUSCb5nz0suULFOhjRXDiqj0OyKsOJnQ9ifW9MEZzIjB%2F3Mzw%2FYCSOg%2F3HKOkpLHBKP%2BLu%2BblRO3XenuHBwDHHymlTTKNfr8rKhzqlC3aoVsoKDmD7Ln1y4ZHgFTe31YPq0F7eddvJrcVkxVyFEqXIUxkqYOzLtY%2FKp4mXe2go8cvnnk%2BXz27vguEW%2BGdJE2fm3Ppq58ymBbgZrNglNfAzocD%2BlzFp1wXHdfAkPD63D5tv9b3MPSzF6Eq8JfHhgYxqgikSwJL4ZpfsO9tWlsriNxLz01dKp67Ee2Uqo%2BZ3OGehs3xQzIjU%2FkTJvJ1luwFthhgwhrb0zAY6pgFKWpRJ5vUkZWynSfTc11YqOWzaUPgWMgy%2BDJ1vNJ2OzXlGYEdtS0%2FiKuKqbDiWfXp5nkInJvvvyvfaIKX%2FN%2BA6U%2BNsi%2Foah5QG8vljfuNdHODp9qaKB9a%2F7hCvMyKJAsEg2Q%2FvNv0jrFNPzajoEgSJn3CvVxnOxgIa176gxUtul7r3X02bbnJ11FTmQE%2FMNj04z4CxWlVyekG8%2BDDX5Pr%2BgOxBcWQe&X-Amz-Signature=ebaf5b3f39a84f5e6797acfe881e94214109d4946f0fbd3ae5045ab96ffbeabf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GIINS5S%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAU5BeHLQwodSUpg%2BqycfFW%2BBnJbh7eZodzP%2BwpJ5Bg%2BAiAHYizLIzUNacVVmH8cZG7%2BRTbJIe6boYYRum4C0%2BTNUCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4jtJfyMMHHR2p5BxKtwDddR8X9%2Fqye0%2Bi5%2F2feFvkZkcqEGX6essIFX%2FXr9yJMHd1uvRntLyGlO8koWo7uzqBmRdrCY2NsyqLkZwAZrEdmsQzWvciCg9mrTuaS82AONpT3HM1hSRMnsj9fhaumue6Utnnh0nysw8CkrkyGIw62L9y7YecyDv%2B2KjwDevr3IzFAVeS7DnGeKQziezffYpXjX%2FvXFyGsYcN9nO1hGUJ7f6pu5XBH7oDNkXGHIpok7KglIEihqj%2BoM4f4jHngtKOLMCA26QEor0at0sYIy9%2FbIdxkBWjihjTQ4BqrwjttYlrc5DLXzoz3kUSCb5nz0suULFOhjRXDiqj0OyKsOJnQ9ifW9MEZzIjB%2F3Mzw%2FYCSOg%2F3HKOkpLHBKP%2BLu%2BblRO3XenuHBwDHHymlTTKNfr8rKhzqlC3aoVsoKDmD7Ln1y4ZHgFTe31YPq0F7eddvJrcVkxVyFEqXIUxkqYOzLtY%2FKp4mXe2go8cvnnk%2BXz27vguEW%2BGdJE2fm3Ppq58ymBbgZrNglNfAzocD%2BlzFp1wXHdfAkPD63D5tv9b3MPSzF6Eq8JfHhgYxqgikSwJL4ZpfsO9tWlsriNxLz01dKp67Ee2Uqo%2BZ3OGehs3xQzIjU%2FkTJvJ1luwFthhgwhrb0zAY6pgFKWpRJ5vUkZWynSfTc11YqOWzaUPgWMgy%2BDJ1vNJ2OzXlGYEdtS0%2FiKuKqbDiWfXp5nkInJvvvyvfaIKX%2FN%2BA6U%2BNsi%2Foah5QG8vljfuNdHODp9qaKB9a%2F7hCvMyKJAsEg2Q%2FvNv0jrFNPzajoEgSJn3CvVxnOxgIa176gxUtul7r3X02bbnJ11FTmQE%2FMNj04z4CxWlVyekG8%2BDDX5Pr%2BgOxBcWQe&X-Amz-Signature=6beb049bb9fdde5040a1c5911a08555cd229ee287b5375341e0bda0acc05ea1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GIINS5S%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAU5BeHLQwodSUpg%2BqycfFW%2BBnJbh7eZodzP%2BwpJ5Bg%2BAiAHYizLIzUNacVVmH8cZG7%2BRTbJIe6boYYRum4C0%2BTNUCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4jtJfyMMHHR2p5BxKtwDddR8X9%2Fqye0%2Bi5%2F2feFvkZkcqEGX6essIFX%2FXr9yJMHd1uvRntLyGlO8koWo7uzqBmRdrCY2NsyqLkZwAZrEdmsQzWvciCg9mrTuaS82AONpT3HM1hSRMnsj9fhaumue6Utnnh0nysw8CkrkyGIw62L9y7YecyDv%2B2KjwDevr3IzFAVeS7DnGeKQziezffYpXjX%2FvXFyGsYcN9nO1hGUJ7f6pu5XBH7oDNkXGHIpok7KglIEihqj%2BoM4f4jHngtKOLMCA26QEor0at0sYIy9%2FbIdxkBWjihjTQ4BqrwjttYlrc5DLXzoz3kUSCb5nz0suULFOhjRXDiqj0OyKsOJnQ9ifW9MEZzIjB%2F3Mzw%2FYCSOg%2F3HKOkpLHBKP%2BLu%2BblRO3XenuHBwDHHymlTTKNfr8rKhzqlC3aoVsoKDmD7Ln1y4ZHgFTe31YPq0F7eddvJrcVkxVyFEqXIUxkqYOzLtY%2FKp4mXe2go8cvnnk%2BXz27vguEW%2BGdJE2fm3Ppq58ymBbgZrNglNfAzocD%2BlzFp1wXHdfAkPD63D5tv9b3MPSzF6Eq8JfHhgYxqgikSwJL4ZpfsO9tWlsriNxLz01dKp67Ee2Uqo%2BZ3OGehs3xQzIjU%2FkTJvJ1luwFthhgwhrb0zAY6pgFKWpRJ5vUkZWynSfTc11YqOWzaUPgWMgy%2BDJ1vNJ2OzXlGYEdtS0%2FiKuKqbDiWfXp5nkInJvvvyvfaIKX%2FN%2BA6U%2BNsi%2Foah5QG8vljfuNdHODp9qaKB9a%2F7hCvMyKJAsEg2Q%2FvNv0jrFNPzajoEgSJn3CvVxnOxgIa176gxUtul7r3X02bbnJ11FTmQE%2FMNj04z4CxWlVyekG8%2BDDX5Pr%2BgOxBcWQe&X-Amz-Signature=e700dbebbf5b8ae4f4aba4ec067daa934fac2ab2dd8e9e84e34df5177dfb10f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GIINS5S%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAU5BeHLQwodSUpg%2BqycfFW%2BBnJbh7eZodzP%2BwpJ5Bg%2BAiAHYizLIzUNacVVmH8cZG7%2BRTbJIe6boYYRum4C0%2BTNUCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4jtJfyMMHHR2p5BxKtwDddR8X9%2Fqye0%2Bi5%2F2feFvkZkcqEGX6essIFX%2FXr9yJMHd1uvRntLyGlO8koWo7uzqBmRdrCY2NsyqLkZwAZrEdmsQzWvciCg9mrTuaS82AONpT3HM1hSRMnsj9fhaumue6Utnnh0nysw8CkrkyGIw62L9y7YecyDv%2B2KjwDevr3IzFAVeS7DnGeKQziezffYpXjX%2FvXFyGsYcN9nO1hGUJ7f6pu5XBH7oDNkXGHIpok7KglIEihqj%2BoM4f4jHngtKOLMCA26QEor0at0sYIy9%2FbIdxkBWjihjTQ4BqrwjttYlrc5DLXzoz3kUSCb5nz0suULFOhjRXDiqj0OyKsOJnQ9ifW9MEZzIjB%2F3Mzw%2FYCSOg%2F3HKOkpLHBKP%2BLu%2BblRO3XenuHBwDHHymlTTKNfr8rKhzqlC3aoVsoKDmD7Ln1y4ZHgFTe31YPq0F7eddvJrcVkxVyFEqXIUxkqYOzLtY%2FKp4mXe2go8cvnnk%2BXz27vguEW%2BGdJE2fm3Ppq58ymBbgZrNglNfAzocD%2BlzFp1wXHdfAkPD63D5tv9b3MPSzF6Eq8JfHhgYxqgikSwJL4ZpfsO9tWlsriNxLz01dKp67Ee2Uqo%2BZ3OGehs3xQzIjU%2FkTJvJ1luwFthhgwhrb0zAY6pgFKWpRJ5vUkZWynSfTc11YqOWzaUPgWMgy%2BDJ1vNJ2OzXlGYEdtS0%2FiKuKqbDiWfXp5nkInJvvvyvfaIKX%2FN%2BA6U%2BNsi%2Foah5QG8vljfuNdHODp9qaKB9a%2F7hCvMyKJAsEg2Q%2FvNv0jrFNPzajoEgSJn3CvVxnOxgIa176gxUtul7r3X02bbnJ11FTmQE%2FMNj04z4CxWlVyekG8%2BDDX5Pr%2BgOxBcWQe&X-Amz-Signature=8958bbe91404e435419b0a9529ff8b589c6f120af188d3a33a8be630a4073fc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GIINS5S%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAU5BeHLQwodSUpg%2BqycfFW%2BBnJbh7eZodzP%2BwpJ5Bg%2BAiAHYizLIzUNacVVmH8cZG7%2BRTbJIe6boYYRum4C0%2BTNUCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4jtJfyMMHHR2p5BxKtwDddR8X9%2Fqye0%2Bi5%2F2feFvkZkcqEGX6essIFX%2FXr9yJMHd1uvRntLyGlO8koWo7uzqBmRdrCY2NsyqLkZwAZrEdmsQzWvciCg9mrTuaS82AONpT3HM1hSRMnsj9fhaumue6Utnnh0nysw8CkrkyGIw62L9y7YecyDv%2B2KjwDevr3IzFAVeS7DnGeKQziezffYpXjX%2FvXFyGsYcN9nO1hGUJ7f6pu5XBH7oDNkXGHIpok7KglIEihqj%2BoM4f4jHngtKOLMCA26QEor0at0sYIy9%2FbIdxkBWjihjTQ4BqrwjttYlrc5DLXzoz3kUSCb5nz0suULFOhjRXDiqj0OyKsOJnQ9ifW9MEZzIjB%2F3Mzw%2FYCSOg%2F3HKOkpLHBKP%2BLu%2BblRO3XenuHBwDHHymlTTKNfr8rKhzqlC3aoVsoKDmD7Ln1y4ZHgFTe31YPq0F7eddvJrcVkxVyFEqXIUxkqYOzLtY%2FKp4mXe2go8cvnnk%2BXz27vguEW%2BGdJE2fm3Ppq58ymBbgZrNglNfAzocD%2BlzFp1wXHdfAkPD63D5tv9b3MPSzF6Eq8JfHhgYxqgikSwJL4ZpfsO9tWlsriNxLz01dKp67Ee2Uqo%2BZ3OGehs3xQzIjU%2FkTJvJ1luwFthhgwhrb0zAY6pgFKWpRJ5vUkZWynSfTc11YqOWzaUPgWMgy%2BDJ1vNJ2OzXlGYEdtS0%2FiKuKqbDiWfXp5nkInJvvvyvfaIKX%2FN%2BA6U%2BNsi%2Foah5QG8vljfuNdHODp9qaKB9a%2F7hCvMyKJAsEg2Q%2FvNv0jrFNPzajoEgSJn3CvVxnOxgIa176gxUtul7r3X02bbnJ11FTmQE%2FMNj04z4CxWlVyekG8%2BDDX5Pr%2BgOxBcWQe&X-Amz-Signature=3380bd0aecae3fa29df1b0c69c1a20fc30710966400fc1044237d3bae6db27c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GIINS5S%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIAU5BeHLQwodSUpg%2BqycfFW%2BBnJbh7eZodzP%2BwpJ5Bg%2BAiAHYizLIzUNacVVmH8cZG7%2BRTbJIe6boYYRum4C0%2BTNUCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4jtJfyMMHHR2p5BxKtwDddR8X9%2Fqye0%2Bi5%2F2feFvkZkcqEGX6essIFX%2FXr9yJMHd1uvRntLyGlO8koWo7uzqBmRdrCY2NsyqLkZwAZrEdmsQzWvciCg9mrTuaS82AONpT3HM1hSRMnsj9fhaumue6Utnnh0nysw8CkrkyGIw62L9y7YecyDv%2B2KjwDevr3IzFAVeS7DnGeKQziezffYpXjX%2FvXFyGsYcN9nO1hGUJ7f6pu5XBH7oDNkXGHIpok7KglIEihqj%2BoM4f4jHngtKOLMCA26QEor0at0sYIy9%2FbIdxkBWjihjTQ4BqrwjttYlrc5DLXzoz3kUSCb5nz0suULFOhjRXDiqj0OyKsOJnQ9ifW9MEZzIjB%2F3Mzw%2FYCSOg%2F3HKOkpLHBKP%2BLu%2BblRO3XenuHBwDHHymlTTKNfr8rKhzqlC3aoVsoKDmD7Ln1y4ZHgFTe31YPq0F7eddvJrcVkxVyFEqXIUxkqYOzLtY%2FKp4mXe2go8cvnnk%2BXz27vguEW%2BGdJE2fm3Ppq58ymBbgZrNglNfAzocD%2BlzFp1wXHdfAkPD63D5tv9b3MPSzF6Eq8JfHhgYxqgikSwJL4ZpfsO9tWlsriNxLz01dKp67Ee2Uqo%2BZ3OGehs3xQzIjU%2FkTJvJ1luwFthhgwhrb0zAY6pgFKWpRJ5vUkZWynSfTc11YqOWzaUPgWMgy%2BDJ1vNJ2OzXlGYEdtS0%2FiKuKqbDiWfXp5nkInJvvvyvfaIKX%2FN%2BA6U%2BNsi%2Foah5QG8vljfuNdHODp9qaKB9a%2F7hCvMyKJAsEg2Q%2FvNv0jrFNPzajoEgSJn3CvVxnOxgIa176gxUtul7r3X02bbnJ11FTmQE%2FMNj04z4CxWlVyekG8%2BDDX5Pr%2BgOxBcWQe&X-Amz-Signature=e450b5b7feb1343515712ea4fba9284edff55166ffd50142d86783dfdb60a97b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

