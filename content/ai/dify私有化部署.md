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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DJPHOBL%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FF0KtbphfYt4DvmE18cDrCikWUk11tgD1RMgy%2BJCAmAIgWtb6gpY2u5J6eqJKUVYOUkjpgixuCtjagQ5OwLozF6Qq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFDLGUmimfRB7hVTbircA6MiLHB1%2FsJW1hVTc72emoPygKxlZ8AYj16hgostKYsKO6AA4DbQBJ40QTSoOIEKL8YHm2Ytn61OVFGXl87ugGRXmtnufaZWU7DZULcdae1fP%2B3TyWCRoS3yljgtd3keTI60MNivcwc4QcMYU6K0XzbMF8mqTttCLPSm46YOOCKmotAIJwnfcuVqdZF28S9SLr3w16xgrSLre0Dzw9wuL2DLwbL9rpxuRIDx2AzMqfsbv%2FSNtMyyVsPkHuYggW45c53z2E2ou0PqYtXov557hC%2BmcD1%2F6bcnlxwAoWCDZm3LICArx%2FG3LG5KaLWOAMgXZXDkYHFGbhwdY2pnQDluZwT8iRej%2B5SOv%2Fr1Yyl0Y7ako0O6sdcu6gMI%2FXCfVjUoxNfKY0BaZsFKuNVyPhvYMwN5WTPqx6%2FXByfkKQf259C5j2QhCxP8u5OyXtF7ho6JWIpgXTGgbJqR3HW%2BjgDLxH6ZpKQBKiUi0g0mWBsjm1XMVRsRBO9%2FcmnXEESnFYhBermrHQg9Qi5zaNMCF4RIBiKxu1st9Sk1uteVpgwKQmIrvQ6RleRKDtum7rXGPxHEzdPKpQZvx1b2626GCgcTpuOEeoDEcFkvXjIJqGxk%2BkGXDJugjC%2F%2FIcYcAbVOMLStq88GOqUBeWIm4MfK39UhwwBMDOCcqrgVTdMXv4nLeSJrqfQxvzWBRCdqdDX9G1QMHsJFF10BRAY%2FgyNPoy6dFQmPJSAZAGruTA7wF4h89WCIusFIydAcsWZ7hth%2B1ZwIawwjyrV0BFsho7WMTRPx4DJPSZuwXglHByHYQB1WXTGdaz5gvLsFK4TkfWunrgeDKw%2Bip3sc5nfhHXMk6MCni5uCBQUUq7aT5oy5&X-Amz-Signature=3853760de6b71d9293ceab14b7cffb4f86daff552d6629009d05e9618f621e85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DJPHOBL%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FF0KtbphfYt4DvmE18cDrCikWUk11tgD1RMgy%2BJCAmAIgWtb6gpY2u5J6eqJKUVYOUkjpgixuCtjagQ5OwLozF6Qq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFDLGUmimfRB7hVTbircA6MiLHB1%2FsJW1hVTc72emoPygKxlZ8AYj16hgostKYsKO6AA4DbQBJ40QTSoOIEKL8YHm2Ytn61OVFGXl87ugGRXmtnufaZWU7DZULcdae1fP%2B3TyWCRoS3yljgtd3keTI60MNivcwc4QcMYU6K0XzbMF8mqTttCLPSm46YOOCKmotAIJwnfcuVqdZF28S9SLr3w16xgrSLre0Dzw9wuL2DLwbL9rpxuRIDx2AzMqfsbv%2FSNtMyyVsPkHuYggW45c53z2E2ou0PqYtXov557hC%2BmcD1%2F6bcnlxwAoWCDZm3LICArx%2FG3LG5KaLWOAMgXZXDkYHFGbhwdY2pnQDluZwT8iRej%2B5SOv%2Fr1Yyl0Y7ako0O6sdcu6gMI%2FXCfVjUoxNfKY0BaZsFKuNVyPhvYMwN5WTPqx6%2FXByfkKQf259C5j2QhCxP8u5OyXtF7ho6JWIpgXTGgbJqR3HW%2BjgDLxH6ZpKQBKiUi0g0mWBsjm1XMVRsRBO9%2FcmnXEESnFYhBermrHQg9Qi5zaNMCF4RIBiKxu1st9Sk1uteVpgwKQmIrvQ6RleRKDtum7rXGPxHEzdPKpQZvx1b2626GCgcTpuOEeoDEcFkvXjIJqGxk%2BkGXDJugjC%2F%2FIcYcAbVOMLStq88GOqUBeWIm4MfK39UhwwBMDOCcqrgVTdMXv4nLeSJrqfQxvzWBRCdqdDX9G1QMHsJFF10BRAY%2FgyNPoy6dFQmPJSAZAGruTA7wF4h89WCIusFIydAcsWZ7hth%2B1ZwIawwjyrV0BFsho7WMTRPx4DJPSZuwXglHByHYQB1WXTGdaz5gvLsFK4TkfWunrgeDKw%2Bip3sc5nfhHXMk6MCni5uCBQUUq7aT5oy5&X-Amz-Signature=b83e123603392ef9cf35bc65607e64a78ef6390135f5929b544c5138ad1f6d66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DJPHOBL%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FF0KtbphfYt4DvmE18cDrCikWUk11tgD1RMgy%2BJCAmAIgWtb6gpY2u5J6eqJKUVYOUkjpgixuCtjagQ5OwLozF6Qq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFDLGUmimfRB7hVTbircA6MiLHB1%2FsJW1hVTc72emoPygKxlZ8AYj16hgostKYsKO6AA4DbQBJ40QTSoOIEKL8YHm2Ytn61OVFGXl87ugGRXmtnufaZWU7DZULcdae1fP%2B3TyWCRoS3yljgtd3keTI60MNivcwc4QcMYU6K0XzbMF8mqTttCLPSm46YOOCKmotAIJwnfcuVqdZF28S9SLr3w16xgrSLre0Dzw9wuL2DLwbL9rpxuRIDx2AzMqfsbv%2FSNtMyyVsPkHuYggW45c53z2E2ou0PqYtXov557hC%2BmcD1%2F6bcnlxwAoWCDZm3LICArx%2FG3LG5KaLWOAMgXZXDkYHFGbhwdY2pnQDluZwT8iRej%2B5SOv%2Fr1Yyl0Y7ako0O6sdcu6gMI%2FXCfVjUoxNfKY0BaZsFKuNVyPhvYMwN5WTPqx6%2FXByfkKQf259C5j2QhCxP8u5OyXtF7ho6JWIpgXTGgbJqR3HW%2BjgDLxH6ZpKQBKiUi0g0mWBsjm1XMVRsRBO9%2FcmnXEESnFYhBermrHQg9Qi5zaNMCF4RIBiKxu1st9Sk1uteVpgwKQmIrvQ6RleRKDtum7rXGPxHEzdPKpQZvx1b2626GCgcTpuOEeoDEcFkvXjIJqGxk%2BkGXDJugjC%2F%2FIcYcAbVOMLStq88GOqUBeWIm4MfK39UhwwBMDOCcqrgVTdMXv4nLeSJrqfQxvzWBRCdqdDX9G1QMHsJFF10BRAY%2FgyNPoy6dFQmPJSAZAGruTA7wF4h89WCIusFIydAcsWZ7hth%2B1ZwIawwjyrV0BFsho7WMTRPx4DJPSZuwXglHByHYQB1WXTGdaz5gvLsFK4TkfWunrgeDKw%2Bip3sc5nfhHXMk6MCni5uCBQUUq7aT5oy5&X-Amz-Signature=1c7d5a9699917a57d2187a7f643c47d9e3145985250608a3ecf23e6636adab57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DJPHOBL%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FF0KtbphfYt4DvmE18cDrCikWUk11tgD1RMgy%2BJCAmAIgWtb6gpY2u5J6eqJKUVYOUkjpgixuCtjagQ5OwLozF6Qq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFDLGUmimfRB7hVTbircA6MiLHB1%2FsJW1hVTc72emoPygKxlZ8AYj16hgostKYsKO6AA4DbQBJ40QTSoOIEKL8YHm2Ytn61OVFGXl87ugGRXmtnufaZWU7DZULcdae1fP%2B3TyWCRoS3yljgtd3keTI60MNivcwc4QcMYU6K0XzbMF8mqTttCLPSm46YOOCKmotAIJwnfcuVqdZF28S9SLr3w16xgrSLre0Dzw9wuL2DLwbL9rpxuRIDx2AzMqfsbv%2FSNtMyyVsPkHuYggW45c53z2E2ou0PqYtXov557hC%2BmcD1%2F6bcnlxwAoWCDZm3LICArx%2FG3LG5KaLWOAMgXZXDkYHFGbhwdY2pnQDluZwT8iRej%2B5SOv%2Fr1Yyl0Y7ako0O6sdcu6gMI%2FXCfVjUoxNfKY0BaZsFKuNVyPhvYMwN5WTPqx6%2FXByfkKQf259C5j2QhCxP8u5OyXtF7ho6JWIpgXTGgbJqR3HW%2BjgDLxH6ZpKQBKiUi0g0mWBsjm1XMVRsRBO9%2FcmnXEESnFYhBermrHQg9Qi5zaNMCF4RIBiKxu1st9Sk1uteVpgwKQmIrvQ6RleRKDtum7rXGPxHEzdPKpQZvx1b2626GCgcTpuOEeoDEcFkvXjIJqGxk%2BkGXDJugjC%2F%2FIcYcAbVOMLStq88GOqUBeWIm4MfK39UhwwBMDOCcqrgVTdMXv4nLeSJrqfQxvzWBRCdqdDX9G1QMHsJFF10BRAY%2FgyNPoy6dFQmPJSAZAGruTA7wF4h89WCIusFIydAcsWZ7hth%2B1ZwIawwjyrV0BFsho7WMTRPx4DJPSZuwXglHByHYQB1WXTGdaz5gvLsFK4TkfWunrgeDKw%2Bip3sc5nfhHXMk6MCni5uCBQUUq7aT5oy5&X-Amz-Signature=24e883d39a5947a124c1e27029c1c6ed999f033f42640140851d015b4f70c294&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DJPHOBL%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FF0KtbphfYt4DvmE18cDrCikWUk11tgD1RMgy%2BJCAmAIgWtb6gpY2u5J6eqJKUVYOUkjpgixuCtjagQ5OwLozF6Qq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFDLGUmimfRB7hVTbircA6MiLHB1%2FsJW1hVTc72emoPygKxlZ8AYj16hgostKYsKO6AA4DbQBJ40QTSoOIEKL8YHm2Ytn61OVFGXl87ugGRXmtnufaZWU7DZULcdae1fP%2B3TyWCRoS3yljgtd3keTI60MNivcwc4QcMYU6K0XzbMF8mqTttCLPSm46YOOCKmotAIJwnfcuVqdZF28S9SLr3w16xgrSLre0Dzw9wuL2DLwbL9rpxuRIDx2AzMqfsbv%2FSNtMyyVsPkHuYggW45c53z2E2ou0PqYtXov557hC%2BmcD1%2F6bcnlxwAoWCDZm3LICArx%2FG3LG5KaLWOAMgXZXDkYHFGbhwdY2pnQDluZwT8iRej%2B5SOv%2Fr1Yyl0Y7ako0O6sdcu6gMI%2FXCfVjUoxNfKY0BaZsFKuNVyPhvYMwN5WTPqx6%2FXByfkKQf259C5j2QhCxP8u5OyXtF7ho6JWIpgXTGgbJqR3HW%2BjgDLxH6ZpKQBKiUi0g0mWBsjm1XMVRsRBO9%2FcmnXEESnFYhBermrHQg9Qi5zaNMCF4RIBiKxu1st9Sk1uteVpgwKQmIrvQ6RleRKDtum7rXGPxHEzdPKpQZvx1b2626GCgcTpuOEeoDEcFkvXjIJqGxk%2BkGXDJugjC%2F%2FIcYcAbVOMLStq88GOqUBeWIm4MfK39UhwwBMDOCcqrgVTdMXv4nLeSJrqfQxvzWBRCdqdDX9G1QMHsJFF10BRAY%2FgyNPoy6dFQmPJSAZAGruTA7wF4h89WCIusFIydAcsWZ7hth%2B1ZwIawwjyrV0BFsho7WMTRPx4DJPSZuwXglHByHYQB1WXTGdaz5gvLsFK4TkfWunrgeDKw%2Bip3sc5nfhHXMk6MCni5uCBQUUq7aT5oy5&X-Amz-Signature=4666be3c0696318869d97e352d7e31a143d6158808c04d3f22ee750cca227575&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DJPHOBL%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FF0KtbphfYt4DvmE18cDrCikWUk11tgD1RMgy%2BJCAmAIgWtb6gpY2u5J6eqJKUVYOUkjpgixuCtjagQ5OwLozF6Qq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFDLGUmimfRB7hVTbircA6MiLHB1%2FsJW1hVTc72emoPygKxlZ8AYj16hgostKYsKO6AA4DbQBJ40QTSoOIEKL8YHm2Ytn61OVFGXl87ugGRXmtnufaZWU7DZULcdae1fP%2B3TyWCRoS3yljgtd3keTI60MNivcwc4QcMYU6K0XzbMF8mqTttCLPSm46YOOCKmotAIJwnfcuVqdZF28S9SLr3w16xgrSLre0Dzw9wuL2DLwbL9rpxuRIDx2AzMqfsbv%2FSNtMyyVsPkHuYggW45c53z2E2ou0PqYtXov557hC%2BmcD1%2F6bcnlxwAoWCDZm3LICArx%2FG3LG5KaLWOAMgXZXDkYHFGbhwdY2pnQDluZwT8iRej%2B5SOv%2Fr1Yyl0Y7ako0O6sdcu6gMI%2FXCfVjUoxNfKY0BaZsFKuNVyPhvYMwN5WTPqx6%2FXByfkKQf259C5j2QhCxP8u5OyXtF7ho6JWIpgXTGgbJqR3HW%2BjgDLxH6ZpKQBKiUi0g0mWBsjm1XMVRsRBO9%2FcmnXEESnFYhBermrHQg9Qi5zaNMCF4RIBiKxu1st9Sk1uteVpgwKQmIrvQ6RleRKDtum7rXGPxHEzdPKpQZvx1b2626GCgcTpuOEeoDEcFkvXjIJqGxk%2BkGXDJugjC%2F%2FIcYcAbVOMLStq88GOqUBeWIm4MfK39UhwwBMDOCcqrgVTdMXv4nLeSJrqfQxvzWBRCdqdDX9G1QMHsJFF10BRAY%2FgyNPoy6dFQmPJSAZAGruTA7wF4h89WCIusFIydAcsWZ7hth%2B1ZwIawwjyrV0BFsho7WMTRPx4DJPSZuwXglHByHYQB1WXTGdaz5gvLsFK4TkfWunrgeDKw%2Bip3sc5nfhHXMk6MCni5uCBQUUq7aT5oy5&X-Amz-Signature=ae37aebea6bf19cfe61257052a9a3fda9027a70cbc1efecb56a2c8563bd263b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DJPHOBL%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FF0KtbphfYt4DvmE18cDrCikWUk11tgD1RMgy%2BJCAmAIgWtb6gpY2u5J6eqJKUVYOUkjpgixuCtjagQ5OwLozF6Qq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFDLGUmimfRB7hVTbircA6MiLHB1%2FsJW1hVTc72emoPygKxlZ8AYj16hgostKYsKO6AA4DbQBJ40QTSoOIEKL8YHm2Ytn61OVFGXl87ugGRXmtnufaZWU7DZULcdae1fP%2B3TyWCRoS3yljgtd3keTI60MNivcwc4QcMYU6K0XzbMF8mqTttCLPSm46YOOCKmotAIJwnfcuVqdZF28S9SLr3w16xgrSLre0Dzw9wuL2DLwbL9rpxuRIDx2AzMqfsbv%2FSNtMyyVsPkHuYggW45c53z2E2ou0PqYtXov557hC%2BmcD1%2F6bcnlxwAoWCDZm3LICArx%2FG3LG5KaLWOAMgXZXDkYHFGbhwdY2pnQDluZwT8iRej%2B5SOv%2Fr1Yyl0Y7ako0O6sdcu6gMI%2FXCfVjUoxNfKY0BaZsFKuNVyPhvYMwN5WTPqx6%2FXByfkKQf259C5j2QhCxP8u5OyXtF7ho6JWIpgXTGgbJqR3HW%2BjgDLxH6ZpKQBKiUi0g0mWBsjm1XMVRsRBO9%2FcmnXEESnFYhBermrHQg9Qi5zaNMCF4RIBiKxu1st9Sk1uteVpgwKQmIrvQ6RleRKDtum7rXGPxHEzdPKpQZvx1b2626GCgcTpuOEeoDEcFkvXjIJqGxk%2BkGXDJugjC%2F%2FIcYcAbVOMLStq88GOqUBeWIm4MfK39UhwwBMDOCcqrgVTdMXv4nLeSJrqfQxvzWBRCdqdDX9G1QMHsJFF10BRAY%2FgyNPoy6dFQmPJSAZAGruTA7wF4h89WCIusFIydAcsWZ7hth%2B1ZwIawwjyrV0BFsho7WMTRPx4DJPSZuwXglHByHYQB1WXTGdaz5gvLsFK4TkfWunrgeDKw%2Bip3sc5nfhHXMk6MCni5uCBQUUq7aT5oy5&X-Amz-Signature=13bd819a1a94e27bf49d7e250c54a2d9056eb81ed60d4b7d1af46096a9d08ff6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DJPHOBL%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FF0KtbphfYt4DvmE18cDrCikWUk11tgD1RMgy%2BJCAmAIgWtb6gpY2u5J6eqJKUVYOUkjpgixuCtjagQ5OwLozF6Qq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFDLGUmimfRB7hVTbircA6MiLHB1%2FsJW1hVTc72emoPygKxlZ8AYj16hgostKYsKO6AA4DbQBJ40QTSoOIEKL8YHm2Ytn61OVFGXl87ugGRXmtnufaZWU7DZULcdae1fP%2B3TyWCRoS3yljgtd3keTI60MNivcwc4QcMYU6K0XzbMF8mqTttCLPSm46YOOCKmotAIJwnfcuVqdZF28S9SLr3w16xgrSLre0Dzw9wuL2DLwbL9rpxuRIDx2AzMqfsbv%2FSNtMyyVsPkHuYggW45c53z2E2ou0PqYtXov557hC%2BmcD1%2F6bcnlxwAoWCDZm3LICArx%2FG3LG5KaLWOAMgXZXDkYHFGbhwdY2pnQDluZwT8iRej%2B5SOv%2Fr1Yyl0Y7ako0O6sdcu6gMI%2FXCfVjUoxNfKY0BaZsFKuNVyPhvYMwN5WTPqx6%2FXByfkKQf259C5j2QhCxP8u5OyXtF7ho6JWIpgXTGgbJqR3HW%2BjgDLxH6ZpKQBKiUi0g0mWBsjm1XMVRsRBO9%2FcmnXEESnFYhBermrHQg9Qi5zaNMCF4RIBiKxu1st9Sk1uteVpgwKQmIrvQ6RleRKDtum7rXGPxHEzdPKpQZvx1b2626GCgcTpuOEeoDEcFkvXjIJqGxk%2BkGXDJugjC%2F%2FIcYcAbVOMLStq88GOqUBeWIm4MfK39UhwwBMDOCcqrgVTdMXv4nLeSJrqfQxvzWBRCdqdDX9G1QMHsJFF10BRAY%2FgyNPoy6dFQmPJSAZAGruTA7wF4h89WCIusFIydAcsWZ7hth%2B1ZwIawwjyrV0BFsho7WMTRPx4DJPSZuwXglHByHYQB1WXTGdaz5gvLsFK4TkfWunrgeDKw%2Bip3sc5nfhHXMk6MCni5uCBQUUq7aT5oy5&X-Amz-Signature=4056f7a0696d29caaea12d090b453b1bbbe58c4dd488171437d777f4e6f87cc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DJPHOBL%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FF0KtbphfYt4DvmE18cDrCikWUk11tgD1RMgy%2BJCAmAIgWtb6gpY2u5J6eqJKUVYOUkjpgixuCtjagQ5OwLozF6Qq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFDLGUmimfRB7hVTbircA6MiLHB1%2FsJW1hVTc72emoPygKxlZ8AYj16hgostKYsKO6AA4DbQBJ40QTSoOIEKL8YHm2Ytn61OVFGXl87ugGRXmtnufaZWU7DZULcdae1fP%2B3TyWCRoS3yljgtd3keTI60MNivcwc4QcMYU6K0XzbMF8mqTttCLPSm46YOOCKmotAIJwnfcuVqdZF28S9SLr3w16xgrSLre0Dzw9wuL2DLwbL9rpxuRIDx2AzMqfsbv%2FSNtMyyVsPkHuYggW45c53z2E2ou0PqYtXov557hC%2BmcD1%2F6bcnlxwAoWCDZm3LICArx%2FG3LG5KaLWOAMgXZXDkYHFGbhwdY2pnQDluZwT8iRej%2B5SOv%2Fr1Yyl0Y7ako0O6sdcu6gMI%2FXCfVjUoxNfKY0BaZsFKuNVyPhvYMwN5WTPqx6%2FXByfkKQf259C5j2QhCxP8u5OyXtF7ho6JWIpgXTGgbJqR3HW%2BjgDLxH6ZpKQBKiUi0g0mWBsjm1XMVRsRBO9%2FcmnXEESnFYhBermrHQg9Qi5zaNMCF4RIBiKxu1st9Sk1uteVpgwKQmIrvQ6RleRKDtum7rXGPxHEzdPKpQZvx1b2626GCgcTpuOEeoDEcFkvXjIJqGxk%2BkGXDJugjC%2F%2FIcYcAbVOMLStq88GOqUBeWIm4MfK39UhwwBMDOCcqrgVTdMXv4nLeSJrqfQxvzWBRCdqdDX9G1QMHsJFF10BRAY%2FgyNPoy6dFQmPJSAZAGruTA7wF4h89WCIusFIydAcsWZ7hth%2B1ZwIawwjyrV0BFsho7WMTRPx4DJPSZuwXglHByHYQB1WXTGdaz5gvLsFK4TkfWunrgeDKw%2Bip3sc5nfhHXMk6MCni5uCBQUUq7aT5oy5&X-Amz-Signature=9226f4cc32352de0abeca313b28c068cc620e1bc95292b0d0b08b7cd6fafe9c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DJPHOBL%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FF0KtbphfYt4DvmE18cDrCikWUk11tgD1RMgy%2BJCAmAIgWtb6gpY2u5J6eqJKUVYOUkjpgixuCtjagQ5OwLozF6Qq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDFDLGUmimfRB7hVTbircA6MiLHB1%2FsJW1hVTc72emoPygKxlZ8AYj16hgostKYsKO6AA4DbQBJ40QTSoOIEKL8YHm2Ytn61OVFGXl87ugGRXmtnufaZWU7DZULcdae1fP%2B3TyWCRoS3yljgtd3keTI60MNivcwc4QcMYU6K0XzbMF8mqTttCLPSm46YOOCKmotAIJwnfcuVqdZF28S9SLr3w16xgrSLre0Dzw9wuL2DLwbL9rpxuRIDx2AzMqfsbv%2FSNtMyyVsPkHuYggW45c53z2E2ou0PqYtXov557hC%2BmcD1%2F6bcnlxwAoWCDZm3LICArx%2FG3LG5KaLWOAMgXZXDkYHFGbhwdY2pnQDluZwT8iRej%2B5SOv%2Fr1Yyl0Y7ako0O6sdcu6gMI%2FXCfVjUoxNfKY0BaZsFKuNVyPhvYMwN5WTPqx6%2FXByfkKQf259C5j2QhCxP8u5OyXtF7ho6JWIpgXTGgbJqR3HW%2BjgDLxH6ZpKQBKiUi0g0mWBsjm1XMVRsRBO9%2FcmnXEESnFYhBermrHQg9Qi5zaNMCF4RIBiKxu1st9Sk1uteVpgwKQmIrvQ6RleRKDtum7rXGPxHEzdPKpQZvx1b2626GCgcTpuOEeoDEcFkvXjIJqGxk%2BkGXDJugjC%2F%2FIcYcAbVOMLStq88GOqUBeWIm4MfK39UhwwBMDOCcqrgVTdMXv4nLeSJrqfQxvzWBRCdqdDX9G1QMHsJFF10BRAY%2FgyNPoy6dFQmPJSAZAGruTA7wF4h89WCIusFIydAcsWZ7hth%2B1ZwIawwjyrV0BFsho7WMTRPx4DJPSZuwXglHByHYQB1WXTGdaz5gvLsFK4TkfWunrgeDKw%2Bip3sc5nfhHXMk6MCni5uCBQUUq7aT5oy5&X-Amz-Signature=f40158b8f7cbbd28543b8e51e64db15f66daca4b355bce28ed583d94aa3c74ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

