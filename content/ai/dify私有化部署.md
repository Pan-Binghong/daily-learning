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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WBSDA2%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICF7y9zECvX2VQBFu8bgg7NXS%2FqXpPOygkykVSPmJheMAiArfEIB3kFEsAz6X6xsz%2BOJZ7XrXVsUyJlh1hveJQn7jCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRzYmbmH53e%2Bt9sC6KtwD0HSjPUfHGwdA%2FYVJzz5bI9x1GpSNnlXDYVlVprDEsXZ4vPNJEy9KwItG3r7uYUbuj18hw%2BN5ahA6EAjNMBz4g%2FlPfQf1ObKikghgbG%2Fm%2BKf%2BBbN%2FEDYAo5D7IChEA5LFezhlSfbAW2i%2FWB2SD0spufMn9MdrksF1oV3aYYlx1fd7Lix81AvfuEDTwwrzrZHHpYXBcmrSrr9Jjs2yHupLzbI%2BP1bi2vJQ%2BC%2BPKrlUBU8%2FDuiP%2B3pWFs6ejN565OijGWykfOGIlY39scaHYfoWkyoAHDn%2FX0gSInUBVfB1EYf0nq7SnPwwhIkwjp7DUVtK2XMQQ9ShjlWKmPFmBIUwHrU7Mn1xKDA%2BePNvqSRicESoC4qv0ZoprGUhPYKKnEN7HG3ZocNsEDdaXMpy2Z2FJ5wiEBjNYDLe35RECofVndmDiO9AMnj0BBdAXYVsL9h1NJMIqam%2FAqRbz0jMu2iewVW4px5ue%2BSU7atuu5NRAmbMqdj%2BkZM9MV1WNxFF1lgxtNblIwp3c5FAm%2BK4Ms898YeYQFNTiaPNe5NeyBCyGIg%2B6tDn27fLEYjl7p8JF23rLyoel8FrbvL8BfmClLeDFhGqWFmlQrhJqo%2F4wQChpmAjO%2Fs4zHP4ZtkC62ow%2B8C%2FzAY6pgFcPrtnai0lKMlx3FlTMDWs5dPLgXQz3%2Bo9Zn5GQJ8ghqAHzbeyglP1s%2FOPLcKrymlMyIduZrhpRSb%2FjG2UTb9lFPgcBuUfQhuRSx2v%2BL2p3LVOV9TT%2BWiA0%2BeVaJilB%2Bb%2FgfSXrR5Kp1Od7v41l8g63WPp%2F4hmhlhIepJJk%2BiJn93jA58VM1PsVEPsGYdcQQReIjnggXhn%2FBXFy%2FsJhwIj%2BTmbUQxG&X-Amz-Signature=76c172b86588f3257a487d18cb1ea3219c7184a8bc8163fd6d3a7a61a6a566a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WBSDA2%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICF7y9zECvX2VQBFu8bgg7NXS%2FqXpPOygkykVSPmJheMAiArfEIB3kFEsAz6X6xsz%2BOJZ7XrXVsUyJlh1hveJQn7jCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRzYmbmH53e%2Bt9sC6KtwD0HSjPUfHGwdA%2FYVJzz5bI9x1GpSNnlXDYVlVprDEsXZ4vPNJEy9KwItG3r7uYUbuj18hw%2BN5ahA6EAjNMBz4g%2FlPfQf1ObKikghgbG%2Fm%2BKf%2BBbN%2FEDYAo5D7IChEA5LFezhlSfbAW2i%2FWB2SD0spufMn9MdrksF1oV3aYYlx1fd7Lix81AvfuEDTwwrzrZHHpYXBcmrSrr9Jjs2yHupLzbI%2BP1bi2vJQ%2BC%2BPKrlUBU8%2FDuiP%2B3pWFs6ejN565OijGWykfOGIlY39scaHYfoWkyoAHDn%2FX0gSInUBVfB1EYf0nq7SnPwwhIkwjp7DUVtK2XMQQ9ShjlWKmPFmBIUwHrU7Mn1xKDA%2BePNvqSRicESoC4qv0ZoprGUhPYKKnEN7HG3ZocNsEDdaXMpy2Z2FJ5wiEBjNYDLe35RECofVndmDiO9AMnj0BBdAXYVsL9h1NJMIqam%2FAqRbz0jMu2iewVW4px5ue%2BSU7atuu5NRAmbMqdj%2BkZM9MV1WNxFF1lgxtNblIwp3c5FAm%2BK4Ms898YeYQFNTiaPNe5NeyBCyGIg%2B6tDn27fLEYjl7p8JF23rLyoel8FrbvL8BfmClLeDFhGqWFmlQrhJqo%2F4wQChpmAjO%2Fs4zHP4ZtkC62ow%2B8C%2FzAY6pgFcPrtnai0lKMlx3FlTMDWs5dPLgXQz3%2Bo9Zn5GQJ8ghqAHzbeyglP1s%2FOPLcKrymlMyIduZrhpRSb%2FjG2UTb9lFPgcBuUfQhuRSx2v%2BL2p3LVOV9TT%2BWiA0%2BeVaJilB%2Bb%2FgfSXrR5Kp1Od7v41l8g63WPp%2F4hmhlhIepJJk%2BiJn93jA58VM1PsVEPsGYdcQQReIjnggXhn%2FBXFy%2FsJhwIj%2BTmbUQxG&X-Amz-Signature=1b3f05e14a8bfc00f1defa00dc97a5b60a1119e980086cecf4deb7c741d4f012&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WBSDA2%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICF7y9zECvX2VQBFu8bgg7NXS%2FqXpPOygkykVSPmJheMAiArfEIB3kFEsAz6X6xsz%2BOJZ7XrXVsUyJlh1hveJQn7jCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRzYmbmH53e%2Bt9sC6KtwD0HSjPUfHGwdA%2FYVJzz5bI9x1GpSNnlXDYVlVprDEsXZ4vPNJEy9KwItG3r7uYUbuj18hw%2BN5ahA6EAjNMBz4g%2FlPfQf1ObKikghgbG%2Fm%2BKf%2BBbN%2FEDYAo5D7IChEA5LFezhlSfbAW2i%2FWB2SD0spufMn9MdrksF1oV3aYYlx1fd7Lix81AvfuEDTwwrzrZHHpYXBcmrSrr9Jjs2yHupLzbI%2BP1bi2vJQ%2BC%2BPKrlUBU8%2FDuiP%2B3pWFs6ejN565OijGWykfOGIlY39scaHYfoWkyoAHDn%2FX0gSInUBVfB1EYf0nq7SnPwwhIkwjp7DUVtK2XMQQ9ShjlWKmPFmBIUwHrU7Mn1xKDA%2BePNvqSRicESoC4qv0ZoprGUhPYKKnEN7HG3ZocNsEDdaXMpy2Z2FJ5wiEBjNYDLe35RECofVndmDiO9AMnj0BBdAXYVsL9h1NJMIqam%2FAqRbz0jMu2iewVW4px5ue%2BSU7atuu5NRAmbMqdj%2BkZM9MV1WNxFF1lgxtNblIwp3c5FAm%2BK4Ms898YeYQFNTiaPNe5NeyBCyGIg%2B6tDn27fLEYjl7p8JF23rLyoel8FrbvL8BfmClLeDFhGqWFmlQrhJqo%2F4wQChpmAjO%2Fs4zHP4ZtkC62ow%2B8C%2FzAY6pgFcPrtnai0lKMlx3FlTMDWs5dPLgXQz3%2Bo9Zn5GQJ8ghqAHzbeyglP1s%2FOPLcKrymlMyIduZrhpRSb%2FjG2UTb9lFPgcBuUfQhuRSx2v%2BL2p3LVOV9TT%2BWiA0%2BeVaJilB%2Bb%2FgfSXrR5Kp1Od7v41l8g63WPp%2F4hmhlhIepJJk%2BiJn93jA58VM1PsVEPsGYdcQQReIjnggXhn%2FBXFy%2FsJhwIj%2BTmbUQxG&X-Amz-Signature=eb510a89fcf2b5c67a5ab96f10c682a9d7fbd8dd1de301dab6d07a4897b9362b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WBSDA2%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICF7y9zECvX2VQBFu8bgg7NXS%2FqXpPOygkykVSPmJheMAiArfEIB3kFEsAz6X6xsz%2BOJZ7XrXVsUyJlh1hveJQn7jCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRzYmbmH53e%2Bt9sC6KtwD0HSjPUfHGwdA%2FYVJzz5bI9x1GpSNnlXDYVlVprDEsXZ4vPNJEy9KwItG3r7uYUbuj18hw%2BN5ahA6EAjNMBz4g%2FlPfQf1ObKikghgbG%2Fm%2BKf%2BBbN%2FEDYAo5D7IChEA5LFezhlSfbAW2i%2FWB2SD0spufMn9MdrksF1oV3aYYlx1fd7Lix81AvfuEDTwwrzrZHHpYXBcmrSrr9Jjs2yHupLzbI%2BP1bi2vJQ%2BC%2BPKrlUBU8%2FDuiP%2B3pWFs6ejN565OijGWykfOGIlY39scaHYfoWkyoAHDn%2FX0gSInUBVfB1EYf0nq7SnPwwhIkwjp7DUVtK2XMQQ9ShjlWKmPFmBIUwHrU7Mn1xKDA%2BePNvqSRicESoC4qv0ZoprGUhPYKKnEN7HG3ZocNsEDdaXMpy2Z2FJ5wiEBjNYDLe35RECofVndmDiO9AMnj0BBdAXYVsL9h1NJMIqam%2FAqRbz0jMu2iewVW4px5ue%2BSU7atuu5NRAmbMqdj%2BkZM9MV1WNxFF1lgxtNblIwp3c5FAm%2BK4Ms898YeYQFNTiaPNe5NeyBCyGIg%2B6tDn27fLEYjl7p8JF23rLyoel8FrbvL8BfmClLeDFhGqWFmlQrhJqo%2F4wQChpmAjO%2Fs4zHP4ZtkC62ow%2B8C%2FzAY6pgFcPrtnai0lKMlx3FlTMDWs5dPLgXQz3%2Bo9Zn5GQJ8ghqAHzbeyglP1s%2FOPLcKrymlMyIduZrhpRSb%2FjG2UTb9lFPgcBuUfQhuRSx2v%2BL2p3LVOV9TT%2BWiA0%2BeVaJilB%2Bb%2FgfSXrR5Kp1Od7v41l8g63WPp%2F4hmhlhIepJJk%2BiJn93jA58VM1PsVEPsGYdcQQReIjnggXhn%2FBXFy%2FsJhwIj%2BTmbUQxG&X-Amz-Signature=28aa6fffdcb9bb46c3c485640301510f91bcaef783f9e2a8efedce72149290bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WBSDA2%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICF7y9zECvX2VQBFu8bgg7NXS%2FqXpPOygkykVSPmJheMAiArfEIB3kFEsAz6X6xsz%2BOJZ7XrXVsUyJlh1hveJQn7jCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRzYmbmH53e%2Bt9sC6KtwD0HSjPUfHGwdA%2FYVJzz5bI9x1GpSNnlXDYVlVprDEsXZ4vPNJEy9KwItG3r7uYUbuj18hw%2BN5ahA6EAjNMBz4g%2FlPfQf1ObKikghgbG%2Fm%2BKf%2BBbN%2FEDYAo5D7IChEA5LFezhlSfbAW2i%2FWB2SD0spufMn9MdrksF1oV3aYYlx1fd7Lix81AvfuEDTwwrzrZHHpYXBcmrSrr9Jjs2yHupLzbI%2BP1bi2vJQ%2BC%2BPKrlUBU8%2FDuiP%2B3pWFs6ejN565OijGWykfOGIlY39scaHYfoWkyoAHDn%2FX0gSInUBVfB1EYf0nq7SnPwwhIkwjp7DUVtK2XMQQ9ShjlWKmPFmBIUwHrU7Mn1xKDA%2BePNvqSRicESoC4qv0ZoprGUhPYKKnEN7HG3ZocNsEDdaXMpy2Z2FJ5wiEBjNYDLe35RECofVndmDiO9AMnj0BBdAXYVsL9h1NJMIqam%2FAqRbz0jMu2iewVW4px5ue%2BSU7atuu5NRAmbMqdj%2BkZM9MV1WNxFF1lgxtNblIwp3c5FAm%2BK4Ms898YeYQFNTiaPNe5NeyBCyGIg%2B6tDn27fLEYjl7p8JF23rLyoel8FrbvL8BfmClLeDFhGqWFmlQrhJqo%2F4wQChpmAjO%2Fs4zHP4ZtkC62ow%2B8C%2FzAY6pgFcPrtnai0lKMlx3FlTMDWs5dPLgXQz3%2Bo9Zn5GQJ8ghqAHzbeyglP1s%2FOPLcKrymlMyIduZrhpRSb%2FjG2UTb9lFPgcBuUfQhuRSx2v%2BL2p3LVOV9TT%2BWiA0%2BeVaJilB%2Bb%2FgfSXrR5Kp1Od7v41l8g63WPp%2F4hmhlhIepJJk%2BiJn93jA58VM1PsVEPsGYdcQQReIjnggXhn%2FBXFy%2FsJhwIj%2BTmbUQxG&X-Amz-Signature=699e96ea3c0db94d572215be294de81ab58f25dfe41c5342f7946ed97efe37dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WBSDA2%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICF7y9zECvX2VQBFu8bgg7NXS%2FqXpPOygkykVSPmJheMAiArfEIB3kFEsAz6X6xsz%2BOJZ7XrXVsUyJlh1hveJQn7jCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRzYmbmH53e%2Bt9sC6KtwD0HSjPUfHGwdA%2FYVJzz5bI9x1GpSNnlXDYVlVprDEsXZ4vPNJEy9KwItG3r7uYUbuj18hw%2BN5ahA6EAjNMBz4g%2FlPfQf1ObKikghgbG%2Fm%2BKf%2BBbN%2FEDYAo5D7IChEA5LFezhlSfbAW2i%2FWB2SD0spufMn9MdrksF1oV3aYYlx1fd7Lix81AvfuEDTwwrzrZHHpYXBcmrSrr9Jjs2yHupLzbI%2BP1bi2vJQ%2BC%2BPKrlUBU8%2FDuiP%2B3pWFs6ejN565OijGWykfOGIlY39scaHYfoWkyoAHDn%2FX0gSInUBVfB1EYf0nq7SnPwwhIkwjp7DUVtK2XMQQ9ShjlWKmPFmBIUwHrU7Mn1xKDA%2BePNvqSRicESoC4qv0ZoprGUhPYKKnEN7HG3ZocNsEDdaXMpy2Z2FJ5wiEBjNYDLe35RECofVndmDiO9AMnj0BBdAXYVsL9h1NJMIqam%2FAqRbz0jMu2iewVW4px5ue%2BSU7atuu5NRAmbMqdj%2BkZM9MV1WNxFF1lgxtNblIwp3c5FAm%2BK4Ms898YeYQFNTiaPNe5NeyBCyGIg%2B6tDn27fLEYjl7p8JF23rLyoel8FrbvL8BfmClLeDFhGqWFmlQrhJqo%2F4wQChpmAjO%2Fs4zHP4ZtkC62ow%2B8C%2FzAY6pgFcPrtnai0lKMlx3FlTMDWs5dPLgXQz3%2Bo9Zn5GQJ8ghqAHzbeyglP1s%2FOPLcKrymlMyIduZrhpRSb%2FjG2UTb9lFPgcBuUfQhuRSx2v%2BL2p3LVOV9TT%2BWiA0%2BeVaJilB%2Bb%2FgfSXrR5Kp1Od7v41l8g63WPp%2F4hmhlhIepJJk%2BiJn93jA58VM1PsVEPsGYdcQQReIjnggXhn%2FBXFy%2FsJhwIj%2BTmbUQxG&X-Amz-Signature=87e7e862bd4db80c9a79eb0815a82a83d4a3cb25fcadeb3105c8c4d16009cd97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WBSDA2%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICF7y9zECvX2VQBFu8bgg7NXS%2FqXpPOygkykVSPmJheMAiArfEIB3kFEsAz6X6xsz%2BOJZ7XrXVsUyJlh1hveJQn7jCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRzYmbmH53e%2Bt9sC6KtwD0HSjPUfHGwdA%2FYVJzz5bI9x1GpSNnlXDYVlVprDEsXZ4vPNJEy9KwItG3r7uYUbuj18hw%2BN5ahA6EAjNMBz4g%2FlPfQf1ObKikghgbG%2Fm%2BKf%2BBbN%2FEDYAo5D7IChEA5LFezhlSfbAW2i%2FWB2SD0spufMn9MdrksF1oV3aYYlx1fd7Lix81AvfuEDTwwrzrZHHpYXBcmrSrr9Jjs2yHupLzbI%2BP1bi2vJQ%2BC%2BPKrlUBU8%2FDuiP%2B3pWFs6ejN565OijGWykfOGIlY39scaHYfoWkyoAHDn%2FX0gSInUBVfB1EYf0nq7SnPwwhIkwjp7DUVtK2XMQQ9ShjlWKmPFmBIUwHrU7Mn1xKDA%2BePNvqSRicESoC4qv0ZoprGUhPYKKnEN7HG3ZocNsEDdaXMpy2Z2FJ5wiEBjNYDLe35RECofVndmDiO9AMnj0BBdAXYVsL9h1NJMIqam%2FAqRbz0jMu2iewVW4px5ue%2BSU7atuu5NRAmbMqdj%2BkZM9MV1WNxFF1lgxtNblIwp3c5FAm%2BK4Ms898YeYQFNTiaPNe5NeyBCyGIg%2B6tDn27fLEYjl7p8JF23rLyoel8FrbvL8BfmClLeDFhGqWFmlQrhJqo%2F4wQChpmAjO%2Fs4zHP4ZtkC62ow%2B8C%2FzAY6pgFcPrtnai0lKMlx3FlTMDWs5dPLgXQz3%2Bo9Zn5GQJ8ghqAHzbeyglP1s%2FOPLcKrymlMyIduZrhpRSb%2FjG2UTb9lFPgcBuUfQhuRSx2v%2BL2p3LVOV9TT%2BWiA0%2BeVaJilB%2Bb%2FgfSXrR5Kp1Od7v41l8g63WPp%2F4hmhlhIepJJk%2BiJn93jA58VM1PsVEPsGYdcQQReIjnggXhn%2FBXFy%2FsJhwIj%2BTmbUQxG&X-Amz-Signature=e60561f244c817f25269bc174e91779232a50e16a5f77ccd11f0347610fee7cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WBSDA2%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICF7y9zECvX2VQBFu8bgg7NXS%2FqXpPOygkykVSPmJheMAiArfEIB3kFEsAz6X6xsz%2BOJZ7XrXVsUyJlh1hveJQn7jCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRzYmbmH53e%2Bt9sC6KtwD0HSjPUfHGwdA%2FYVJzz5bI9x1GpSNnlXDYVlVprDEsXZ4vPNJEy9KwItG3r7uYUbuj18hw%2BN5ahA6EAjNMBz4g%2FlPfQf1ObKikghgbG%2Fm%2BKf%2BBbN%2FEDYAo5D7IChEA5LFezhlSfbAW2i%2FWB2SD0spufMn9MdrksF1oV3aYYlx1fd7Lix81AvfuEDTwwrzrZHHpYXBcmrSrr9Jjs2yHupLzbI%2BP1bi2vJQ%2BC%2BPKrlUBU8%2FDuiP%2B3pWFs6ejN565OijGWykfOGIlY39scaHYfoWkyoAHDn%2FX0gSInUBVfB1EYf0nq7SnPwwhIkwjp7DUVtK2XMQQ9ShjlWKmPFmBIUwHrU7Mn1xKDA%2BePNvqSRicESoC4qv0ZoprGUhPYKKnEN7HG3ZocNsEDdaXMpy2Z2FJ5wiEBjNYDLe35RECofVndmDiO9AMnj0BBdAXYVsL9h1NJMIqam%2FAqRbz0jMu2iewVW4px5ue%2BSU7atuu5NRAmbMqdj%2BkZM9MV1WNxFF1lgxtNblIwp3c5FAm%2BK4Ms898YeYQFNTiaPNe5NeyBCyGIg%2B6tDn27fLEYjl7p8JF23rLyoel8FrbvL8BfmClLeDFhGqWFmlQrhJqo%2F4wQChpmAjO%2Fs4zHP4ZtkC62ow%2B8C%2FzAY6pgFcPrtnai0lKMlx3FlTMDWs5dPLgXQz3%2Bo9Zn5GQJ8ghqAHzbeyglP1s%2FOPLcKrymlMyIduZrhpRSb%2FjG2UTb9lFPgcBuUfQhuRSx2v%2BL2p3LVOV9TT%2BWiA0%2BeVaJilB%2Bb%2FgfSXrR5Kp1Od7v41l8g63WPp%2F4hmhlhIepJJk%2BiJn93jA58VM1PsVEPsGYdcQQReIjnggXhn%2FBXFy%2FsJhwIj%2BTmbUQxG&X-Amz-Signature=d66ab0ba366914e715a17d42b81704dd388260855189f3d21cfaa505e5767fc6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WBSDA2%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICF7y9zECvX2VQBFu8bgg7NXS%2FqXpPOygkykVSPmJheMAiArfEIB3kFEsAz6X6xsz%2BOJZ7XrXVsUyJlh1hveJQn7jCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRzYmbmH53e%2Bt9sC6KtwD0HSjPUfHGwdA%2FYVJzz5bI9x1GpSNnlXDYVlVprDEsXZ4vPNJEy9KwItG3r7uYUbuj18hw%2BN5ahA6EAjNMBz4g%2FlPfQf1ObKikghgbG%2Fm%2BKf%2BBbN%2FEDYAo5D7IChEA5LFezhlSfbAW2i%2FWB2SD0spufMn9MdrksF1oV3aYYlx1fd7Lix81AvfuEDTwwrzrZHHpYXBcmrSrr9Jjs2yHupLzbI%2BP1bi2vJQ%2BC%2BPKrlUBU8%2FDuiP%2B3pWFs6ejN565OijGWykfOGIlY39scaHYfoWkyoAHDn%2FX0gSInUBVfB1EYf0nq7SnPwwhIkwjp7DUVtK2XMQQ9ShjlWKmPFmBIUwHrU7Mn1xKDA%2BePNvqSRicESoC4qv0ZoprGUhPYKKnEN7HG3ZocNsEDdaXMpy2Z2FJ5wiEBjNYDLe35RECofVndmDiO9AMnj0BBdAXYVsL9h1NJMIqam%2FAqRbz0jMu2iewVW4px5ue%2BSU7atuu5NRAmbMqdj%2BkZM9MV1WNxFF1lgxtNblIwp3c5FAm%2BK4Ms898YeYQFNTiaPNe5NeyBCyGIg%2B6tDn27fLEYjl7p8JF23rLyoel8FrbvL8BfmClLeDFhGqWFmlQrhJqo%2F4wQChpmAjO%2Fs4zHP4ZtkC62ow%2B8C%2FzAY6pgFcPrtnai0lKMlx3FlTMDWs5dPLgXQz3%2Bo9Zn5GQJ8ghqAHzbeyglP1s%2FOPLcKrymlMyIduZrhpRSb%2FjG2UTb9lFPgcBuUfQhuRSx2v%2BL2p3LVOV9TT%2BWiA0%2BeVaJilB%2Bb%2FgfSXrR5Kp1Od7v41l8g63WPp%2F4hmhlhIepJJk%2BiJn93jA58VM1PsVEPsGYdcQQReIjnggXhn%2FBXFy%2FsJhwIj%2BTmbUQxG&X-Amz-Signature=bfc4236051b470b96949d4f6bcd265e6b746744e5faea3559c6e7f27d1a201a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657WBSDA2%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCICF7y9zECvX2VQBFu8bgg7NXS%2FqXpPOygkykVSPmJheMAiArfEIB3kFEsAz6X6xsz%2BOJZ7XrXVsUyJlh1hveJQn7jCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRzYmbmH53e%2Bt9sC6KtwD0HSjPUfHGwdA%2FYVJzz5bI9x1GpSNnlXDYVlVprDEsXZ4vPNJEy9KwItG3r7uYUbuj18hw%2BN5ahA6EAjNMBz4g%2FlPfQf1ObKikghgbG%2Fm%2BKf%2BBbN%2FEDYAo5D7IChEA5LFezhlSfbAW2i%2FWB2SD0spufMn9MdrksF1oV3aYYlx1fd7Lix81AvfuEDTwwrzrZHHpYXBcmrSrr9Jjs2yHupLzbI%2BP1bi2vJQ%2BC%2BPKrlUBU8%2FDuiP%2B3pWFs6ejN565OijGWykfOGIlY39scaHYfoWkyoAHDn%2FX0gSInUBVfB1EYf0nq7SnPwwhIkwjp7DUVtK2XMQQ9ShjlWKmPFmBIUwHrU7Mn1xKDA%2BePNvqSRicESoC4qv0ZoprGUhPYKKnEN7HG3ZocNsEDdaXMpy2Z2FJ5wiEBjNYDLe35RECofVndmDiO9AMnj0BBdAXYVsL9h1NJMIqam%2FAqRbz0jMu2iewVW4px5ue%2BSU7atuu5NRAmbMqdj%2BkZM9MV1WNxFF1lgxtNblIwp3c5FAm%2BK4Ms898YeYQFNTiaPNe5NeyBCyGIg%2B6tDn27fLEYjl7p8JF23rLyoel8FrbvL8BfmClLeDFhGqWFmlQrhJqo%2F4wQChpmAjO%2Fs4zHP4ZtkC62ow%2B8C%2FzAY6pgFcPrtnai0lKMlx3FlTMDWs5dPLgXQz3%2Bo9Zn5GQJ8ghqAHzbeyglP1s%2FOPLcKrymlMyIduZrhpRSb%2FjG2UTb9lFPgcBuUfQhuRSx2v%2BL2p3LVOV9TT%2BWiA0%2BeVaJilB%2Bb%2FgfSXrR5Kp1Od7v41l8g63WPp%2F4hmhlhIepJJk%2BiJn93jA58VM1PsVEPsGYdcQQReIjnggXhn%2FBXFy%2FsJhwIj%2BTmbUQxG&X-Amz-Signature=5ec8245a6be4e92ce9ba7ff47d061c7ba2325eea0dfb5fd3e01a0adffd493397&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

