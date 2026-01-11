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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4EUR3L%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIFwA5A%2BDPZV7ygCaEOCBjc%2Bu8OWybMGLU1n5NbyaE5DAAiB8wkYGpqA4fKWGRGCLMFpn5qRGQpEKnR1VHesUeW1VTiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEFlD%2Bw1k0SnFBgqaKtwDDYoaMhRIGJnBYrVKjdI5xja6Bq6wpLahbELgmQhpi4LMg0Tew42hNcv0%2BF0kdTTSXN%2BS0lh%2F49D7y2AktHiMwVM5MxKhdc4GFzNFo0nfilJV%2F8wVyEPLT5lxU%2F9UkY3R40qkL%2BmTaQJFgWR6PJ2CTt5nlssPnbLoRkABSCrm8y5aL5Bv6F8bG5pcbWvb%2F4ha5H9Ncu23epBhhbFrWndmKG9kZ9IBEPj%2F8zMl15gs9th%2FNscz84hv98DQdF1J3wvud4kHhb0IyiwUVV5vkr2WXa%2Fbz42kp6qcZoMatAwNTcR%2FFRf8ReQPG3Tcx3%2B3USq8qouxLMZx75rrhPLaO5Qg3cv1WTZGREbtoLHl8Nf7OCgyD98T4%2BEIKMHQpXGIrwe9BwpTgCS5383GBqIqtWkeYoWMOshennJxZEclYeg2Mrehtv9SPmuRI18NRiR3IqI980l7adC%2Fcfx6jm4tvOOEAflW1fPUrDU48W0yoGciN1JzXGLoyCZrrnIxMRypW2adu%2BpoevfPLbqHIN5h3RSorNC%2FOC9hZUtfrUhljaDrW0cOY52PJrfWncsXkYueFM2Do87or04q9xawKbsdeRsrkrtOBgzouvD1BSyPsPxO53DqAeCHkhZnKz%2Ft%2BUcwsf6LywY6pgEj13kNdoPmBSz1%2BG%2Fm4UPj7Gidd920z7bIlWnnF01x%2Bq5zsIE17ENxJA0kx1m7GWJ0gm%2BN%2Bcy%2FqL52x2jFmxBOuloiwCMD87k8APPXvPfA9a3Fw2FN7hIssUkXa3LC%2FW%2F2fgTkNXGL02QoTQHjjJLBESH8RZIeNuvcsZZv8xnTCajINV%2Bp7z6asrMYuzNVemJmhU0RCyNWsX36iMLtmT5wVrN6UD2e&X-Amz-Signature=d2ff00c8e4864844e7ba9b8cbf1745376e79f5e7d97ed0ad3607b29adb596bd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4EUR3L%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIFwA5A%2BDPZV7ygCaEOCBjc%2Bu8OWybMGLU1n5NbyaE5DAAiB8wkYGpqA4fKWGRGCLMFpn5qRGQpEKnR1VHesUeW1VTiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEFlD%2Bw1k0SnFBgqaKtwDDYoaMhRIGJnBYrVKjdI5xja6Bq6wpLahbELgmQhpi4LMg0Tew42hNcv0%2BF0kdTTSXN%2BS0lh%2F49D7y2AktHiMwVM5MxKhdc4GFzNFo0nfilJV%2F8wVyEPLT5lxU%2F9UkY3R40qkL%2BmTaQJFgWR6PJ2CTt5nlssPnbLoRkABSCrm8y5aL5Bv6F8bG5pcbWvb%2F4ha5H9Ncu23epBhhbFrWndmKG9kZ9IBEPj%2F8zMl15gs9th%2FNscz84hv98DQdF1J3wvud4kHhb0IyiwUVV5vkr2WXa%2Fbz42kp6qcZoMatAwNTcR%2FFRf8ReQPG3Tcx3%2B3USq8qouxLMZx75rrhPLaO5Qg3cv1WTZGREbtoLHl8Nf7OCgyD98T4%2BEIKMHQpXGIrwe9BwpTgCS5383GBqIqtWkeYoWMOshennJxZEclYeg2Mrehtv9SPmuRI18NRiR3IqI980l7adC%2Fcfx6jm4tvOOEAflW1fPUrDU48W0yoGciN1JzXGLoyCZrrnIxMRypW2adu%2BpoevfPLbqHIN5h3RSorNC%2FOC9hZUtfrUhljaDrW0cOY52PJrfWncsXkYueFM2Do87or04q9xawKbsdeRsrkrtOBgzouvD1BSyPsPxO53DqAeCHkhZnKz%2Ft%2BUcwsf6LywY6pgEj13kNdoPmBSz1%2BG%2Fm4UPj7Gidd920z7bIlWnnF01x%2Bq5zsIE17ENxJA0kx1m7GWJ0gm%2BN%2Bcy%2FqL52x2jFmxBOuloiwCMD87k8APPXvPfA9a3Fw2FN7hIssUkXa3LC%2FW%2F2fgTkNXGL02QoTQHjjJLBESH8RZIeNuvcsZZv8xnTCajINV%2Bp7z6asrMYuzNVemJmhU0RCyNWsX36iMLtmT5wVrN6UD2e&X-Amz-Signature=047fd615e84a6a1d5ef94b6b7344f5782f95294d00efe664e2e01f0e3da7d84e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4EUR3L%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIFwA5A%2BDPZV7ygCaEOCBjc%2Bu8OWybMGLU1n5NbyaE5DAAiB8wkYGpqA4fKWGRGCLMFpn5qRGQpEKnR1VHesUeW1VTiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEFlD%2Bw1k0SnFBgqaKtwDDYoaMhRIGJnBYrVKjdI5xja6Bq6wpLahbELgmQhpi4LMg0Tew42hNcv0%2BF0kdTTSXN%2BS0lh%2F49D7y2AktHiMwVM5MxKhdc4GFzNFo0nfilJV%2F8wVyEPLT5lxU%2F9UkY3R40qkL%2BmTaQJFgWR6PJ2CTt5nlssPnbLoRkABSCrm8y5aL5Bv6F8bG5pcbWvb%2F4ha5H9Ncu23epBhhbFrWndmKG9kZ9IBEPj%2F8zMl15gs9th%2FNscz84hv98DQdF1J3wvud4kHhb0IyiwUVV5vkr2WXa%2Fbz42kp6qcZoMatAwNTcR%2FFRf8ReQPG3Tcx3%2B3USq8qouxLMZx75rrhPLaO5Qg3cv1WTZGREbtoLHl8Nf7OCgyD98T4%2BEIKMHQpXGIrwe9BwpTgCS5383GBqIqtWkeYoWMOshennJxZEclYeg2Mrehtv9SPmuRI18NRiR3IqI980l7adC%2Fcfx6jm4tvOOEAflW1fPUrDU48W0yoGciN1JzXGLoyCZrrnIxMRypW2adu%2BpoevfPLbqHIN5h3RSorNC%2FOC9hZUtfrUhljaDrW0cOY52PJrfWncsXkYueFM2Do87or04q9xawKbsdeRsrkrtOBgzouvD1BSyPsPxO53DqAeCHkhZnKz%2Ft%2BUcwsf6LywY6pgEj13kNdoPmBSz1%2BG%2Fm4UPj7Gidd920z7bIlWnnF01x%2Bq5zsIE17ENxJA0kx1m7GWJ0gm%2BN%2Bcy%2FqL52x2jFmxBOuloiwCMD87k8APPXvPfA9a3Fw2FN7hIssUkXa3LC%2FW%2F2fgTkNXGL02QoTQHjjJLBESH8RZIeNuvcsZZv8xnTCajINV%2Bp7z6asrMYuzNVemJmhU0RCyNWsX36iMLtmT5wVrN6UD2e&X-Amz-Signature=004ceea948ef5c1dc5cb8188a11663180df164757ab6a182d9d4129b03956309&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4EUR3L%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIFwA5A%2BDPZV7ygCaEOCBjc%2Bu8OWybMGLU1n5NbyaE5DAAiB8wkYGpqA4fKWGRGCLMFpn5qRGQpEKnR1VHesUeW1VTiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEFlD%2Bw1k0SnFBgqaKtwDDYoaMhRIGJnBYrVKjdI5xja6Bq6wpLahbELgmQhpi4LMg0Tew42hNcv0%2BF0kdTTSXN%2BS0lh%2F49D7y2AktHiMwVM5MxKhdc4GFzNFo0nfilJV%2F8wVyEPLT5lxU%2F9UkY3R40qkL%2BmTaQJFgWR6PJ2CTt5nlssPnbLoRkABSCrm8y5aL5Bv6F8bG5pcbWvb%2F4ha5H9Ncu23epBhhbFrWndmKG9kZ9IBEPj%2F8zMl15gs9th%2FNscz84hv98DQdF1J3wvud4kHhb0IyiwUVV5vkr2WXa%2Fbz42kp6qcZoMatAwNTcR%2FFRf8ReQPG3Tcx3%2B3USq8qouxLMZx75rrhPLaO5Qg3cv1WTZGREbtoLHl8Nf7OCgyD98T4%2BEIKMHQpXGIrwe9BwpTgCS5383GBqIqtWkeYoWMOshennJxZEclYeg2Mrehtv9SPmuRI18NRiR3IqI980l7adC%2Fcfx6jm4tvOOEAflW1fPUrDU48W0yoGciN1JzXGLoyCZrrnIxMRypW2adu%2BpoevfPLbqHIN5h3RSorNC%2FOC9hZUtfrUhljaDrW0cOY52PJrfWncsXkYueFM2Do87or04q9xawKbsdeRsrkrtOBgzouvD1BSyPsPxO53DqAeCHkhZnKz%2Ft%2BUcwsf6LywY6pgEj13kNdoPmBSz1%2BG%2Fm4UPj7Gidd920z7bIlWnnF01x%2Bq5zsIE17ENxJA0kx1m7GWJ0gm%2BN%2Bcy%2FqL52x2jFmxBOuloiwCMD87k8APPXvPfA9a3Fw2FN7hIssUkXa3LC%2FW%2F2fgTkNXGL02QoTQHjjJLBESH8RZIeNuvcsZZv8xnTCajINV%2Bp7z6asrMYuzNVemJmhU0RCyNWsX36iMLtmT5wVrN6UD2e&X-Amz-Signature=e2bb06d00a0e8aef0d6fe5cc526b1fadca1890195e70d39922321c9fc55f8dd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4EUR3L%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIFwA5A%2BDPZV7ygCaEOCBjc%2Bu8OWybMGLU1n5NbyaE5DAAiB8wkYGpqA4fKWGRGCLMFpn5qRGQpEKnR1VHesUeW1VTiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEFlD%2Bw1k0SnFBgqaKtwDDYoaMhRIGJnBYrVKjdI5xja6Bq6wpLahbELgmQhpi4LMg0Tew42hNcv0%2BF0kdTTSXN%2BS0lh%2F49D7y2AktHiMwVM5MxKhdc4GFzNFo0nfilJV%2F8wVyEPLT5lxU%2F9UkY3R40qkL%2BmTaQJFgWR6PJ2CTt5nlssPnbLoRkABSCrm8y5aL5Bv6F8bG5pcbWvb%2F4ha5H9Ncu23epBhhbFrWndmKG9kZ9IBEPj%2F8zMl15gs9th%2FNscz84hv98DQdF1J3wvud4kHhb0IyiwUVV5vkr2WXa%2Fbz42kp6qcZoMatAwNTcR%2FFRf8ReQPG3Tcx3%2B3USq8qouxLMZx75rrhPLaO5Qg3cv1WTZGREbtoLHl8Nf7OCgyD98T4%2BEIKMHQpXGIrwe9BwpTgCS5383GBqIqtWkeYoWMOshennJxZEclYeg2Mrehtv9SPmuRI18NRiR3IqI980l7adC%2Fcfx6jm4tvOOEAflW1fPUrDU48W0yoGciN1JzXGLoyCZrrnIxMRypW2adu%2BpoevfPLbqHIN5h3RSorNC%2FOC9hZUtfrUhljaDrW0cOY52PJrfWncsXkYueFM2Do87or04q9xawKbsdeRsrkrtOBgzouvD1BSyPsPxO53DqAeCHkhZnKz%2Ft%2BUcwsf6LywY6pgEj13kNdoPmBSz1%2BG%2Fm4UPj7Gidd920z7bIlWnnF01x%2Bq5zsIE17ENxJA0kx1m7GWJ0gm%2BN%2Bcy%2FqL52x2jFmxBOuloiwCMD87k8APPXvPfA9a3Fw2FN7hIssUkXa3LC%2FW%2F2fgTkNXGL02QoTQHjjJLBESH8RZIeNuvcsZZv8xnTCajINV%2Bp7z6asrMYuzNVemJmhU0RCyNWsX36iMLtmT5wVrN6UD2e&X-Amz-Signature=8da7353d944273c65ec9cf457dd4af479699a65978b1be7be7f8aeafd9920dbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4EUR3L%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIFwA5A%2BDPZV7ygCaEOCBjc%2Bu8OWybMGLU1n5NbyaE5DAAiB8wkYGpqA4fKWGRGCLMFpn5qRGQpEKnR1VHesUeW1VTiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEFlD%2Bw1k0SnFBgqaKtwDDYoaMhRIGJnBYrVKjdI5xja6Bq6wpLahbELgmQhpi4LMg0Tew42hNcv0%2BF0kdTTSXN%2BS0lh%2F49D7y2AktHiMwVM5MxKhdc4GFzNFo0nfilJV%2F8wVyEPLT5lxU%2F9UkY3R40qkL%2BmTaQJFgWR6PJ2CTt5nlssPnbLoRkABSCrm8y5aL5Bv6F8bG5pcbWvb%2F4ha5H9Ncu23epBhhbFrWndmKG9kZ9IBEPj%2F8zMl15gs9th%2FNscz84hv98DQdF1J3wvud4kHhb0IyiwUVV5vkr2WXa%2Fbz42kp6qcZoMatAwNTcR%2FFRf8ReQPG3Tcx3%2B3USq8qouxLMZx75rrhPLaO5Qg3cv1WTZGREbtoLHl8Nf7OCgyD98T4%2BEIKMHQpXGIrwe9BwpTgCS5383GBqIqtWkeYoWMOshennJxZEclYeg2Mrehtv9SPmuRI18NRiR3IqI980l7adC%2Fcfx6jm4tvOOEAflW1fPUrDU48W0yoGciN1JzXGLoyCZrrnIxMRypW2adu%2BpoevfPLbqHIN5h3RSorNC%2FOC9hZUtfrUhljaDrW0cOY52PJrfWncsXkYueFM2Do87or04q9xawKbsdeRsrkrtOBgzouvD1BSyPsPxO53DqAeCHkhZnKz%2Ft%2BUcwsf6LywY6pgEj13kNdoPmBSz1%2BG%2Fm4UPj7Gidd920z7bIlWnnF01x%2Bq5zsIE17ENxJA0kx1m7GWJ0gm%2BN%2Bcy%2FqL52x2jFmxBOuloiwCMD87k8APPXvPfA9a3Fw2FN7hIssUkXa3LC%2FW%2F2fgTkNXGL02QoTQHjjJLBESH8RZIeNuvcsZZv8xnTCajINV%2Bp7z6asrMYuzNVemJmhU0RCyNWsX36iMLtmT5wVrN6UD2e&X-Amz-Signature=06d8cd8f337ecf026ec83c5a8600ce78a462d007cc69b9896cb5273e6b13e839&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4EUR3L%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIFwA5A%2BDPZV7ygCaEOCBjc%2Bu8OWybMGLU1n5NbyaE5DAAiB8wkYGpqA4fKWGRGCLMFpn5qRGQpEKnR1VHesUeW1VTiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEFlD%2Bw1k0SnFBgqaKtwDDYoaMhRIGJnBYrVKjdI5xja6Bq6wpLahbELgmQhpi4LMg0Tew42hNcv0%2BF0kdTTSXN%2BS0lh%2F49D7y2AktHiMwVM5MxKhdc4GFzNFo0nfilJV%2F8wVyEPLT5lxU%2F9UkY3R40qkL%2BmTaQJFgWR6PJ2CTt5nlssPnbLoRkABSCrm8y5aL5Bv6F8bG5pcbWvb%2F4ha5H9Ncu23epBhhbFrWndmKG9kZ9IBEPj%2F8zMl15gs9th%2FNscz84hv98DQdF1J3wvud4kHhb0IyiwUVV5vkr2WXa%2Fbz42kp6qcZoMatAwNTcR%2FFRf8ReQPG3Tcx3%2B3USq8qouxLMZx75rrhPLaO5Qg3cv1WTZGREbtoLHl8Nf7OCgyD98T4%2BEIKMHQpXGIrwe9BwpTgCS5383GBqIqtWkeYoWMOshennJxZEclYeg2Mrehtv9SPmuRI18NRiR3IqI980l7adC%2Fcfx6jm4tvOOEAflW1fPUrDU48W0yoGciN1JzXGLoyCZrrnIxMRypW2adu%2BpoevfPLbqHIN5h3RSorNC%2FOC9hZUtfrUhljaDrW0cOY52PJrfWncsXkYueFM2Do87or04q9xawKbsdeRsrkrtOBgzouvD1BSyPsPxO53DqAeCHkhZnKz%2Ft%2BUcwsf6LywY6pgEj13kNdoPmBSz1%2BG%2Fm4UPj7Gidd920z7bIlWnnF01x%2Bq5zsIE17ENxJA0kx1m7GWJ0gm%2BN%2Bcy%2FqL52x2jFmxBOuloiwCMD87k8APPXvPfA9a3Fw2FN7hIssUkXa3LC%2FW%2F2fgTkNXGL02QoTQHjjJLBESH8RZIeNuvcsZZv8xnTCajINV%2Bp7z6asrMYuzNVemJmhU0RCyNWsX36iMLtmT5wVrN6UD2e&X-Amz-Signature=4574a6f7535bc528b3015830aec96197d018ec4475f9d7996aaeb55400f9c36b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4EUR3L%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIFwA5A%2BDPZV7ygCaEOCBjc%2Bu8OWybMGLU1n5NbyaE5DAAiB8wkYGpqA4fKWGRGCLMFpn5qRGQpEKnR1VHesUeW1VTiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEFlD%2Bw1k0SnFBgqaKtwDDYoaMhRIGJnBYrVKjdI5xja6Bq6wpLahbELgmQhpi4LMg0Tew42hNcv0%2BF0kdTTSXN%2BS0lh%2F49D7y2AktHiMwVM5MxKhdc4GFzNFo0nfilJV%2F8wVyEPLT5lxU%2F9UkY3R40qkL%2BmTaQJFgWR6PJ2CTt5nlssPnbLoRkABSCrm8y5aL5Bv6F8bG5pcbWvb%2F4ha5H9Ncu23epBhhbFrWndmKG9kZ9IBEPj%2F8zMl15gs9th%2FNscz84hv98DQdF1J3wvud4kHhb0IyiwUVV5vkr2WXa%2Fbz42kp6qcZoMatAwNTcR%2FFRf8ReQPG3Tcx3%2B3USq8qouxLMZx75rrhPLaO5Qg3cv1WTZGREbtoLHl8Nf7OCgyD98T4%2BEIKMHQpXGIrwe9BwpTgCS5383GBqIqtWkeYoWMOshennJxZEclYeg2Mrehtv9SPmuRI18NRiR3IqI980l7adC%2Fcfx6jm4tvOOEAflW1fPUrDU48W0yoGciN1JzXGLoyCZrrnIxMRypW2adu%2BpoevfPLbqHIN5h3RSorNC%2FOC9hZUtfrUhljaDrW0cOY52PJrfWncsXkYueFM2Do87or04q9xawKbsdeRsrkrtOBgzouvD1BSyPsPxO53DqAeCHkhZnKz%2Ft%2BUcwsf6LywY6pgEj13kNdoPmBSz1%2BG%2Fm4UPj7Gidd920z7bIlWnnF01x%2Bq5zsIE17ENxJA0kx1m7GWJ0gm%2BN%2Bcy%2FqL52x2jFmxBOuloiwCMD87k8APPXvPfA9a3Fw2FN7hIssUkXa3LC%2FW%2F2fgTkNXGL02QoTQHjjJLBESH8RZIeNuvcsZZv8xnTCajINV%2Bp7z6asrMYuzNVemJmhU0RCyNWsX36iMLtmT5wVrN6UD2e&X-Amz-Signature=a1321c8c682fdbd853c4587d4915e14bffdfe948df8b8385fd0016dcc77b46e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4EUR3L%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIFwA5A%2BDPZV7ygCaEOCBjc%2Bu8OWybMGLU1n5NbyaE5DAAiB8wkYGpqA4fKWGRGCLMFpn5qRGQpEKnR1VHesUeW1VTiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEFlD%2Bw1k0SnFBgqaKtwDDYoaMhRIGJnBYrVKjdI5xja6Bq6wpLahbELgmQhpi4LMg0Tew42hNcv0%2BF0kdTTSXN%2BS0lh%2F49D7y2AktHiMwVM5MxKhdc4GFzNFo0nfilJV%2F8wVyEPLT5lxU%2F9UkY3R40qkL%2BmTaQJFgWR6PJ2CTt5nlssPnbLoRkABSCrm8y5aL5Bv6F8bG5pcbWvb%2F4ha5H9Ncu23epBhhbFrWndmKG9kZ9IBEPj%2F8zMl15gs9th%2FNscz84hv98DQdF1J3wvud4kHhb0IyiwUVV5vkr2WXa%2Fbz42kp6qcZoMatAwNTcR%2FFRf8ReQPG3Tcx3%2B3USq8qouxLMZx75rrhPLaO5Qg3cv1WTZGREbtoLHl8Nf7OCgyD98T4%2BEIKMHQpXGIrwe9BwpTgCS5383GBqIqtWkeYoWMOshennJxZEclYeg2Mrehtv9SPmuRI18NRiR3IqI980l7adC%2Fcfx6jm4tvOOEAflW1fPUrDU48W0yoGciN1JzXGLoyCZrrnIxMRypW2adu%2BpoevfPLbqHIN5h3RSorNC%2FOC9hZUtfrUhljaDrW0cOY52PJrfWncsXkYueFM2Do87or04q9xawKbsdeRsrkrtOBgzouvD1BSyPsPxO53DqAeCHkhZnKz%2Ft%2BUcwsf6LywY6pgEj13kNdoPmBSz1%2BG%2Fm4UPj7Gidd920z7bIlWnnF01x%2Bq5zsIE17ENxJA0kx1m7GWJ0gm%2BN%2Bcy%2FqL52x2jFmxBOuloiwCMD87k8APPXvPfA9a3Fw2FN7hIssUkXa3LC%2FW%2F2fgTkNXGL02QoTQHjjJLBESH8RZIeNuvcsZZv8xnTCajINV%2Bp7z6asrMYuzNVemJmhU0RCyNWsX36iMLtmT5wVrN6UD2e&X-Amz-Signature=7d647af7915ea5c19787b9d3b80a996f8db46f26852cfcac7dd922636049a0ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP4EUR3L%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIFwA5A%2BDPZV7ygCaEOCBjc%2Bu8OWybMGLU1n5NbyaE5DAAiB8wkYGpqA4fKWGRGCLMFpn5qRGQpEKnR1VHesUeW1VTiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEFlD%2Bw1k0SnFBgqaKtwDDYoaMhRIGJnBYrVKjdI5xja6Bq6wpLahbELgmQhpi4LMg0Tew42hNcv0%2BF0kdTTSXN%2BS0lh%2F49D7y2AktHiMwVM5MxKhdc4GFzNFo0nfilJV%2F8wVyEPLT5lxU%2F9UkY3R40qkL%2BmTaQJFgWR6PJ2CTt5nlssPnbLoRkABSCrm8y5aL5Bv6F8bG5pcbWvb%2F4ha5H9Ncu23epBhhbFrWndmKG9kZ9IBEPj%2F8zMl15gs9th%2FNscz84hv98DQdF1J3wvud4kHhb0IyiwUVV5vkr2WXa%2Fbz42kp6qcZoMatAwNTcR%2FFRf8ReQPG3Tcx3%2B3USq8qouxLMZx75rrhPLaO5Qg3cv1WTZGREbtoLHl8Nf7OCgyD98T4%2BEIKMHQpXGIrwe9BwpTgCS5383GBqIqtWkeYoWMOshennJxZEclYeg2Mrehtv9SPmuRI18NRiR3IqI980l7adC%2Fcfx6jm4tvOOEAflW1fPUrDU48W0yoGciN1JzXGLoyCZrrnIxMRypW2adu%2BpoevfPLbqHIN5h3RSorNC%2FOC9hZUtfrUhljaDrW0cOY52PJrfWncsXkYueFM2Do87or04q9xawKbsdeRsrkrtOBgzouvD1BSyPsPxO53DqAeCHkhZnKz%2Ft%2BUcwsf6LywY6pgEj13kNdoPmBSz1%2BG%2Fm4UPj7Gidd920z7bIlWnnF01x%2Bq5zsIE17ENxJA0kx1m7GWJ0gm%2BN%2Bcy%2FqL52x2jFmxBOuloiwCMD87k8APPXvPfA9a3Fw2FN7hIssUkXa3LC%2FW%2F2fgTkNXGL02QoTQHjjJLBESH8RZIeNuvcsZZv8xnTCajINV%2Bp7z6asrMYuzNVemJmhU0RCyNWsX36iMLtmT5wVrN6UD2e&X-Amz-Signature=e33b072be0150fb07a73a42f30f45358a34014c253979bf5e10a3672d6b96780&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

