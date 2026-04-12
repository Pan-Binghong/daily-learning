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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGSLDJG%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtlqoyuT%2FJLZNA79mel63yoKAzl%2BLXLRX7Mr%2FmN7KukAiB6fKxocWA7nCInpYIohr8%2B%2B42KiYdEF0Je3N0J0%2BLJSir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM%2FL1yds%2Bte%2F8pu8aAKtwDQVCeaUS8gM%2FFzTRuoMvv8ki7ScBhKLkqdva63Xhpnmx3z%2BxpmHK3QuZ5P%2BJTuvalRyFQzTFdzW882bDntXlgKvoFXpPGtF4UhQiIdMtmgSzujE8iiBvFpJ8tf%2BWpIXS8TZI8dvkD0cs0id6iJ%2BXjol%2Bsu%2FXs70khoaNrqPbn%2FCW2QLx%2BJ8GsX80NaMlwR7G6f%2FaFtXlTneBrqPVjfb3WbsgetDkoFDvd35KH0KQDQhzALx5GuZFOByvHdUhPSMGXG9UtDDMLQVQulEtlzMCcaCHJj2YAxk95ogl3Df7wZXM9SJuXVD5xqUT%2BBF73tTFKbj4rxzqAD2Ax2ENBWvdIjxR2QHT0KkPXt4E8sXBwKiLZmkc%2B80UdN4mGHCCrPbAEP6eAMDIia9Z2Jdyg8qwoiqsoQ0a0D5Hq7cS4KJdXLkePTGgZSclhrEwlatZnJrhwaehkhCBHFHz6CFdqlLJ6PFmxlYLbR7DIF9KIPee6VhhmEfuQr0lbt0v1%2BfoVgor%2FGdUgLsWgFMiZvMMVdeAD4LVoAxl4rJGB1hrEXl%2FI5042mBTe3S2tDWkdJR7DXCk3D8n8WTtSuZCRRJPSxy3%2FOmyShTDXKUJCKtAfttYjBlkK6OyPiunm%2B9x1fdUwjYnszgY6pgEMKeTAz4YJTk62moZNRPSAc293rI6iAHQZ%2BSv4yxPAH10Pv6sE01bx%2FAAAd%2FG4QFHv%2Bp6hEQh9Qdp31glWTd14X7PuIv3M2FsYxgh4VlR2s%2FzB1CxSJaIPa2QeOCAZnIsqo2G2v%2FSwUo3zgjWGpjxFvTibBaIvs%2B4VHwYl%2BjHTKRCJN2Y0Fhu%2B2GUxCdNeJPKj4ZfEum49xjBklx3j7OrUo3bi70KD&X-Amz-Signature=46bbbfc44aec2d4e5b2804388981d8f82fc300d827001bd05f8d1e7b863ff4f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGSLDJG%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtlqoyuT%2FJLZNA79mel63yoKAzl%2BLXLRX7Mr%2FmN7KukAiB6fKxocWA7nCInpYIohr8%2B%2B42KiYdEF0Je3N0J0%2BLJSir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM%2FL1yds%2Bte%2F8pu8aAKtwDQVCeaUS8gM%2FFzTRuoMvv8ki7ScBhKLkqdva63Xhpnmx3z%2BxpmHK3QuZ5P%2BJTuvalRyFQzTFdzW882bDntXlgKvoFXpPGtF4UhQiIdMtmgSzujE8iiBvFpJ8tf%2BWpIXS8TZI8dvkD0cs0id6iJ%2BXjol%2Bsu%2FXs70khoaNrqPbn%2FCW2QLx%2BJ8GsX80NaMlwR7G6f%2FaFtXlTneBrqPVjfb3WbsgetDkoFDvd35KH0KQDQhzALx5GuZFOByvHdUhPSMGXG9UtDDMLQVQulEtlzMCcaCHJj2YAxk95ogl3Df7wZXM9SJuXVD5xqUT%2BBF73tTFKbj4rxzqAD2Ax2ENBWvdIjxR2QHT0KkPXt4E8sXBwKiLZmkc%2B80UdN4mGHCCrPbAEP6eAMDIia9Z2Jdyg8qwoiqsoQ0a0D5Hq7cS4KJdXLkePTGgZSclhrEwlatZnJrhwaehkhCBHFHz6CFdqlLJ6PFmxlYLbR7DIF9KIPee6VhhmEfuQr0lbt0v1%2BfoVgor%2FGdUgLsWgFMiZvMMVdeAD4LVoAxl4rJGB1hrEXl%2FI5042mBTe3S2tDWkdJR7DXCk3D8n8WTtSuZCRRJPSxy3%2FOmyShTDXKUJCKtAfttYjBlkK6OyPiunm%2B9x1fdUwjYnszgY6pgEMKeTAz4YJTk62moZNRPSAc293rI6iAHQZ%2BSv4yxPAH10Pv6sE01bx%2FAAAd%2FG4QFHv%2Bp6hEQh9Qdp31glWTd14X7PuIv3M2FsYxgh4VlR2s%2FzB1CxSJaIPa2QeOCAZnIsqo2G2v%2FSwUo3zgjWGpjxFvTibBaIvs%2B4VHwYl%2BjHTKRCJN2Y0Fhu%2B2GUxCdNeJPKj4ZfEum49xjBklx3j7OrUo3bi70KD&X-Amz-Signature=edaf5157dca0707dca27c912ec3568361bdbde5a1ee05e0169b65e4effa43d79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGSLDJG%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtlqoyuT%2FJLZNA79mel63yoKAzl%2BLXLRX7Mr%2FmN7KukAiB6fKxocWA7nCInpYIohr8%2B%2B42KiYdEF0Je3N0J0%2BLJSir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM%2FL1yds%2Bte%2F8pu8aAKtwDQVCeaUS8gM%2FFzTRuoMvv8ki7ScBhKLkqdva63Xhpnmx3z%2BxpmHK3QuZ5P%2BJTuvalRyFQzTFdzW882bDntXlgKvoFXpPGtF4UhQiIdMtmgSzujE8iiBvFpJ8tf%2BWpIXS8TZI8dvkD0cs0id6iJ%2BXjol%2Bsu%2FXs70khoaNrqPbn%2FCW2QLx%2BJ8GsX80NaMlwR7G6f%2FaFtXlTneBrqPVjfb3WbsgetDkoFDvd35KH0KQDQhzALx5GuZFOByvHdUhPSMGXG9UtDDMLQVQulEtlzMCcaCHJj2YAxk95ogl3Df7wZXM9SJuXVD5xqUT%2BBF73tTFKbj4rxzqAD2Ax2ENBWvdIjxR2QHT0KkPXt4E8sXBwKiLZmkc%2B80UdN4mGHCCrPbAEP6eAMDIia9Z2Jdyg8qwoiqsoQ0a0D5Hq7cS4KJdXLkePTGgZSclhrEwlatZnJrhwaehkhCBHFHz6CFdqlLJ6PFmxlYLbR7DIF9KIPee6VhhmEfuQr0lbt0v1%2BfoVgor%2FGdUgLsWgFMiZvMMVdeAD4LVoAxl4rJGB1hrEXl%2FI5042mBTe3S2tDWkdJR7DXCk3D8n8WTtSuZCRRJPSxy3%2FOmyShTDXKUJCKtAfttYjBlkK6OyPiunm%2B9x1fdUwjYnszgY6pgEMKeTAz4YJTk62moZNRPSAc293rI6iAHQZ%2BSv4yxPAH10Pv6sE01bx%2FAAAd%2FG4QFHv%2Bp6hEQh9Qdp31glWTd14X7PuIv3M2FsYxgh4VlR2s%2FzB1CxSJaIPa2QeOCAZnIsqo2G2v%2FSwUo3zgjWGpjxFvTibBaIvs%2B4VHwYl%2BjHTKRCJN2Y0Fhu%2B2GUxCdNeJPKj4ZfEum49xjBklx3j7OrUo3bi70KD&X-Amz-Signature=8aa69e91e7f61a54ce6f222146e2cac0f9f236ef8e0db3553c9938d8eb4c0117&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGSLDJG%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtlqoyuT%2FJLZNA79mel63yoKAzl%2BLXLRX7Mr%2FmN7KukAiB6fKxocWA7nCInpYIohr8%2B%2B42KiYdEF0Je3N0J0%2BLJSir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM%2FL1yds%2Bte%2F8pu8aAKtwDQVCeaUS8gM%2FFzTRuoMvv8ki7ScBhKLkqdva63Xhpnmx3z%2BxpmHK3QuZ5P%2BJTuvalRyFQzTFdzW882bDntXlgKvoFXpPGtF4UhQiIdMtmgSzujE8iiBvFpJ8tf%2BWpIXS8TZI8dvkD0cs0id6iJ%2BXjol%2Bsu%2FXs70khoaNrqPbn%2FCW2QLx%2BJ8GsX80NaMlwR7G6f%2FaFtXlTneBrqPVjfb3WbsgetDkoFDvd35KH0KQDQhzALx5GuZFOByvHdUhPSMGXG9UtDDMLQVQulEtlzMCcaCHJj2YAxk95ogl3Df7wZXM9SJuXVD5xqUT%2BBF73tTFKbj4rxzqAD2Ax2ENBWvdIjxR2QHT0KkPXt4E8sXBwKiLZmkc%2B80UdN4mGHCCrPbAEP6eAMDIia9Z2Jdyg8qwoiqsoQ0a0D5Hq7cS4KJdXLkePTGgZSclhrEwlatZnJrhwaehkhCBHFHz6CFdqlLJ6PFmxlYLbR7DIF9KIPee6VhhmEfuQr0lbt0v1%2BfoVgor%2FGdUgLsWgFMiZvMMVdeAD4LVoAxl4rJGB1hrEXl%2FI5042mBTe3S2tDWkdJR7DXCk3D8n8WTtSuZCRRJPSxy3%2FOmyShTDXKUJCKtAfttYjBlkK6OyPiunm%2B9x1fdUwjYnszgY6pgEMKeTAz4YJTk62moZNRPSAc293rI6iAHQZ%2BSv4yxPAH10Pv6sE01bx%2FAAAd%2FG4QFHv%2Bp6hEQh9Qdp31glWTd14X7PuIv3M2FsYxgh4VlR2s%2FzB1CxSJaIPa2QeOCAZnIsqo2G2v%2FSwUo3zgjWGpjxFvTibBaIvs%2B4VHwYl%2BjHTKRCJN2Y0Fhu%2B2GUxCdNeJPKj4ZfEum49xjBklx3j7OrUo3bi70KD&X-Amz-Signature=bf6e4d9998d5c71cbd984be79b2cd2e625f1cb22e56aae262ee5f03a2c8221f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGSLDJG%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtlqoyuT%2FJLZNA79mel63yoKAzl%2BLXLRX7Mr%2FmN7KukAiB6fKxocWA7nCInpYIohr8%2B%2B42KiYdEF0Je3N0J0%2BLJSir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM%2FL1yds%2Bte%2F8pu8aAKtwDQVCeaUS8gM%2FFzTRuoMvv8ki7ScBhKLkqdva63Xhpnmx3z%2BxpmHK3QuZ5P%2BJTuvalRyFQzTFdzW882bDntXlgKvoFXpPGtF4UhQiIdMtmgSzujE8iiBvFpJ8tf%2BWpIXS8TZI8dvkD0cs0id6iJ%2BXjol%2Bsu%2FXs70khoaNrqPbn%2FCW2QLx%2BJ8GsX80NaMlwR7G6f%2FaFtXlTneBrqPVjfb3WbsgetDkoFDvd35KH0KQDQhzALx5GuZFOByvHdUhPSMGXG9UtDDMLQVQulEtlzMCcaCHJj2YAxk95ogl3Df7wZXM9SJuXVD5xqUT%2BBF73tTFKbj4rxzqAD2Ax2ENBWvdIjxR2QHT0KkPXt4E8sXBwKiLZmkc%2B80UdN4mGHCCrPbAEP6eAMDIia9Z2Jdyg8qwoiqsoQ0a0D5Hq7cS4KJdXLkePTGgZSclhrEwlatZnJrhwaehkhCBHFHz6CFdqlLJ6PFmxlYLbR7DIF9KIPee6VhhmEfuQr0lbt0v1%2BfoVgor%2FGdUgLsWgFMiZvMMVdeAD4LVoAxl4rJGB1hrEXl%2FI5042mBTe3S2tDWkdJR7DXCk3D8n8WTtSuZCRRJPSxy3%2FOmyShTDXKUJCKtAfttYjBlkK6OyPiunm%2B9x1fdUwjYnszgY6pgEMKeTAz4YJTk62moZNRPSAc293rI6iAHQZ%2BSv4yxPAH10Pv6sE01bx%2FAAAd%2FG4QFHv%2Bp6hEQh9Qdp31glWTd14X7PuIv3M2FsYxgh4VlR2s%2FzB1CxSJaIPa2QeOCAZnIsqo2G2v%2FSwUo3zgjWGpjxFvTibBaIvs%2B4VHwYl%2BjHTKRCJN2Y0Fhu%2B2GUxCdNeJPKj4ZfEum49xjBklx3j7OrUo3bi70KD&X-Amz-Signature=1e1a2bd5cffc6a5d73b17a5c225e05a11d600fd259e1b3bcc02da9bbb1e076be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGSLDJG%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtlqoyuT%2FJLZNA79mel63yoKAzl%2BLXLRX7Mr%2FmN7KukAiB6fKxocWA7nCInpYIohr8%2B%2B42KiYdEF0Je3N0J0%2BLJSir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM%2FL1yds%2Bte%2F8pu8aAKtwDQVCeaUS8gM%2FFzTRuoMvv8ki7ScBhKLkqdva63Xhpnmx3z%2BxpmHK3QuZ5P%2BJTuvalRyFQzTFdzW882bDntXlgKvoFXpPGtF4UhQiIdMtmgSzujE8iiBvFpJ8tf%2BWpIXS8TZI8dvkD0cs0id6iJ%2BXjol%2Bsu%2FXs70khoaNrqPbn%2FCW2QLx%2BJ8GsX80NaMlwR7G6f%2FaFtXlTneBrqPVjfb3WbsgetDkoFDvd35KH0KQDQhzALx5GuZFOByvHdUhPSMGXG9UtDDMLQVQulEtlzMCcaCHJj2YAxk95ogl3Df7wZXM9SJuXVD5xqUT%2BBF73tTFKbj4rxzqAD2Ax2ENBWvdIjxR2QHT0KkPXt4E8sXBwKiLZmkc%2B80UdN4mGHCCrPbAEP6eAMDIia9Z2Jdyg8qwoiqsoQ0a0D5Hq7cS4KJdXLkePTGgZSclhrEwlatZnJrhwaehkhCBHFHz6CFdqlLJ6PFmxlYLbR7DIF9KIPee6VhhmEfuQr0lbt0v1%2BfoVgor%2FGdUgLsWgFMiZvMMVdeAD4LVoAxl4rJGB1hrEXl%2FI5042mBTe3S2tDWkdJR7DXCk3D8n8WTtSuZCRRJPSxy3%2FOmyShTDXKUJCKtAfttYjBlkK6OyPiunm%2B9x1fdUwjYnszgY6pgEMKeTAz4YJTk62moZNRPSAc293rI6iAHQZ%2BSv4yxPAH10Pv6sE01bx%2FAAAd%2FG4QFHv%2Bp6hEQh9Qdp31glWTd14X7PuIv3M2FsYxgh4VlR2s%2FzB1CxSJaIPa2QeOCAZnIsqo2G2v%2FSwUo3zgjWGpjxFvTibBaIvs%2B4VHwYl%2BjHTKRCJN2Y0Fhu%2B2GUxCdNeJPKj4ZfEum49xjBklx3j7OrUo3bi70KD&X-Amz-Signature=942b456b9f10f6713e89e64fe2044728e777cdee97a8d3c3547bd5d27199c4be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGSLDJG%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtlqoyuT%2FJLZNA79mel63yoKAzl%2BLXLRX7Mr%2FmN7KukAiB6fKxocWA7nCInpYIohr8%2B%2B42KiYdEF0Je3N0J0%2BLJSir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM%2FL1yds%2Bte%2F8pu8aAKtwDQVCeaUS8gM%2FFzTRuoMvv8ki7ScBhKLkqdva63Xhpnmx3z%2BxpmHK3QuZ5P%2BJTuvalRyFQzTFdzW882bDntXlgKvoFXpPGtF4UhQiIdMtmgSzujE8iiBvFpJ8tf%2BWpIXS8TZI8dvkD0cs0id6iJ%2BXjol%2Bsu%2FXs70khoaNrqPbn%2FCW2QLx%2BJ8GsX80NaMlwR7G6f%2FaFtXlTneBrqPVjfb3WbsgetDkoFDvd35KH0KQDQhzALx5GuZFOByvHdUhPSMGXG9UtDDMLQVQulEtlzMCcaCHJj2YAxk95ogl3Df7wZXM9SJuXVD5xqUT%2BBF73tTFKbj4rxzqAD2Ax2ENBWvdIjxR2QHT0KkPXt4E8sXBwKiLZmkc%2B80UdN4mGHCCrPbAEP6eAMDIia9Z2Jdyg8qwoiqsoQ0a0D5Hq7cS4KJdXLkePTGgZSclhrEwlatZnJrhwaehkhCBHFHz6CFdqlLJ6PFmxlYLbR7DIF9KIPee6VhhmEfuQr0lbt0v1%2BfoVgor%2FGdUgLsWgFMiZvMMVdeAD4LVoAxl4rJGB1hrEXl%2FI5042mBTe3S2tDWkdJR7DXCk3D8n8WTtSuZCRRJPSxy3%2FOmyShTDXKUJCKtAfttYjBlkK6OyPiunm%2B9x1fdUwjYnszgY6pgEMKeTAz4YJTk62moZNRPSAc293rI6iAHQZ%2BSv4yxPAH10Pv6sE01bx%2FAAAd%2FG4QFHv%2Bp6hEQh9Qdp31glWTd14X7PuIv3M2FsYxgh4VlR2s%2FzB1CxSJaIPa2QeOCAZnIsqo2G2v%2FSwUo3zgjWGpjxFvTibBaIvs%2B4VHwYl%2BjHTKRCJN2Y0Fhu%2B2GUxCdNeJPKj4ZfEum49xjBklx3j7OrUo3bi70KD&X-Amz-Signature=b272e3e9eec6e76d90439eea0f2e43a051173c4ff043a40d5239f818c368079a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGSLDJG%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtlqoyuT%2FJLZNA79mel63yoKAzl%2BLXLRX7Mr%2FmN7KukAiB6fKxocWA7nCInpYIohr8%2B%2B42KiYdEF0Je3N0J0%2BLJSir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM%2FL1yds%2Bte%2F8pu8aAKtwDQVCeaUS8gM%2FFzTRuoMvv8ki7ScBhKLkqdva63Xhpnmx3z%2BxpmHK3QuZ5P%2BJTuvalRyFQzTFdzW882bDntXlgKvoFXpPGtF4UhQiIdMtmgSzujE8iiBvFpJ8tf%2BWpIXS8TZI8dvkD0cs0id6iJ%2BXjol%2Bsu%2FXs70khoaNrqPbn%2FCW2QLx%2BJ8GsX80NaMlwR7G6f%2FaFtXlTneBrqPVjfb3WbsgetDkoFDvd35KH0KQDQhzALx5GuZFOByvHdUhPSMGXG9UtDDMLQVQulEtlzMCcaCHJj2YAxk95ogl3Df7wZXM9SJuXVD5xqUT%2BBF73tTFKbj4rxzqAD2Ax2ENBWvdIjxR2QHT0KkPXt4E8sXBwKiLZmkc%2B80UdN4mGHCCrPbAEP6eAMDIia9Z2Jdyg8qwoiqsoQ0a0D5Hq7cS4KJdXLkePTGgZSclhrEwlatZnJrhwaehkhCBHFHz6CFdqlLJ6PFmxlYLbR7DIF9KIPee6VhhmEfuQr0lbt0v1%2BfoVgor%2FGdUgLsWgFMiZvMMVdeAD4LVoAxl4rJGB1hrEXl%2FI5042mBTe3S2tDWkdJR7DXCk3D8n8WTtSuZCRRJPSxy3%2FOmyShTDXKUJCKtAfttYjBlkK6OyPiunm%2B9x1fdUwjYnszgY6pgEMKeTAz4YJTk62moZNRPSAc293rI6iAHQZ%2BSv4yxPAH10Pv6sE01bx%2FAAAd%2FG4QFHv%2Bp6hEQh9Qdp31glWTd14X7PuIv3M2FsYxgh4VlR2s%2FzB1CxSJaIPa2QeOCAZnIsqo2G2v%2FSwUo3zgjWGpjxFvTibBaIvs%2B4VHwYl%2BjHTKRCJN2Y0Fhu%2B2GUxCdNeJPKj4ZfEum49xjBklx3j7OrUo3bi70KD&X-Amz-Signature=5d3039a6f8455d8e54f48414d7ab83f6519a4d3c90c40175a694ef703425f854&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGSLDJG%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtlqoyuT%2FJLZNA79mel63yoKAzl%2BLXLRX7Mr%2FmN7KukAiB6fKxocWA7nCInpYIohr8%2B%2B42KiYdEF0Je3N0J0%2BLJSir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM%2FL1yds%2Bte%2F8pu8aAKtwDQVCeaUS8gM%2FFzTRuoMvv8ki7ScBhKLkqdva63Xhpnmx3z%2BxpmHK3QuZ5P%2BJTuvalRyFQzTFdzW882bDntXlgKvoFXpPGtF4UhQiIdMtmgSzujE8iiBvFpJ8tf%2BWpIXS8TZI8dvkD0cs0id6iJ%2BXjol%2Bsu%2FXs70khoaNrqPbn%2FCW2QLx%2BJ8GsX80NaMlwR7G6f%2FaFtXlTneBrqPVjfb3WbsgetDkoFDvd35KH0KQDQhzALx5GuZFOByvHdUhPSMGXG9UtDDMLQVQulEtlzMCcaCHJj2YAxk95ogl3Df7wZXM9SJuXVD5xqUT%2BBF73tTFKbj4rxzqAD2Ax2ENBWvdIjxR2QHT0KkPXt4E8sXBwKiLZmkc%2B80UdN4mGHCCrPbAEP6eAMDIia9Z2Jdyg8qwoiqsoQ0a0D5Hq7cS4KJdXLkePTGgZSclhrEwlatZnJrhwaehkhCBHFHz6CFdqlLJ6PFmxlYLbR7DIF9KIPee6VhhmEfuQr0lbt0v1%2BfoVgor%2FGdUgLsWgFMiZvMMVdeAD4LVoAxl4rJGB1hrEXl%2FI5042mBTe3S2tDWkdJR7DXCk3D8n8WTtSuZCRRJPSxy3%2FOmyShTDXKUJCKtAfttYjBlkK6OyPiunm%2B9x1fdUwjYnszgY6pgEMKeTAz4YJTk62moZNRPSAc293rI6iAHQZ%2BSv4yxPAH10Pv6sE01bx%2FAAAd%2FG4QFHv%2Bp6hEQh9Qdp31glWTd14X7PuIv3M2FsYxgh4VlR2s%2FzB1CxSJaIPa2QeOCAZnIsqo2G2v%2FSwUo3zgjWGpjxFvTibBaIvs%2B4VHwYl%2BjHTKRCJN2Y0Fhu%2B2GUxCdNeJPKj4ZfEum49xjBklx3j7OrUo3bi70KD&X-Amz-Signature=98035883e27dc6cdd43d7158e31240b8f2c024d0cd7dd2087ddd6bc370d08cdd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGSLDJG%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtlqoyuT%2FJLZNA79mel63yoKAzl%2BLXLRX7Mr%2FmN7KukAiB6fKxocWA7nCInpYIohr8%2B%2B42KiYdEF0Je3N0J0%2BLJSir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIM%2FL1yds%2Bte%2F8pu8aAKtwDQVCeaUS8gM%2FFzTRuoMvv8ki7ScBhKLkqdva63Xhpnmx3z%2BxpmHK3QuZ5P%2BJTuvalRyFQzTFdzW882bDntXlgKvoFXpPGtF4UhQiIdMtmgSzujE8iiBvFpJ8tf%2BWpIXS8TZI8dvkD0cs0id6iJ%2BXjol%2Bsu%2FXs70khoaNrqPbn%2FCW2QLx%2BJ8GsX80NaMlwR7G6f%2FaFtXlTneBrqPVjfb3WbsgetDkoFDvd35KH0KQDQhzALx5GuZFOByvHdUhPSMGXG9UtDDMLQVQulEtlzMCcaCHJj2YAxk95ogl3Df7wZXM9SJuXVD5xqUT%2BBF73tTFKbj4rxzqAD2Ax2ENBWvdIjxR2QHT0KkPXt4E8sXBwKiLZmkc%2B80UdN4mGHCCrPbAEP6eAMDIia9Z2Jdyg8qwoiqsoQ0a0D5Hq7cS4KJdXLkePTGgZSclhrEwlatZnJrhwaehkhCBHFHz6CFdqlLJ6PFmxlYLbR7DIF9KIPee6VhhmEfuQr0lbt0v1%2BfoVgor%2FGdUgLsWgFMiZvMMVdeAD4LVoAxl4rJGB1hrEXl%2FI5042mBTe3S2tDWkdJR7DXCk3D8n8WTtSuZCRRJPSxy3%2FOmyShTDXKUJCKtAfttYjBlkK6OyPiunm%2B9x1fdUwjYnszgY6pgEMKeTAz4YJTk62moZNRPSAc293rI6iAHQZ%2BSv4yxPAH10Pv6sE01bx%2FAAAd%2FG4QFHv%2Bp6hEQh9Qdp31glWTd14X7PuIv3M2FsYxgh4VlR2s%2FzB1CxSJaIPa2QeOCAZnIsqo2G2v%2FSwUo3zgjWGpjxFvTibBaIvs%2B4VHwYl%2BjHTKRCJN2Y0Fhu%2B2GUxCdNeJPKj4ZfEum49xjBklx3j7OrUo3bi70KD&X-Amz-Signature=93f62a901bf12a9401093c5b1a049069a7d64e549467543a38c6f7bc7fd11940&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

