---
title: Dify私有化部署
date: '2024-11-15T09:08:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- Dify
categories:
- AI
---

# 1.创建服务器准备工作

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYQ2PMQI%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwHkDQaGE83dfsNVyz64imAtL27VlHPvPf5ulf4uk2KAiAo3qGRYdJ5cZ%2Bx%2FWQYMUIJxFCemUYklS32iixt14gGgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0HlNTE2J8VtB1OjKtwDtwMM7bSMu947zIgwhI5t2xZHL%2FcM40C205TbLT9ER7Na02FSw7s0l1wzlqpx4Sefv230rYJMpWQBWNBlwKO45%2FTsd0HvU%2FqzJCPNDXu%2FXbg25i7dfPnxujvuZ2unRcOnq90Xw0QdrBBi3cBv5BOe89mvx2DzRW8J28SWYuM84l8x1zyDrVDlzkLzGhQCUhi0ysCcSe%2B%2FrNtMu37P%2FPbNwAZBg5C%2BT%2BeG0od4VFOMM6LJmdzuwkaAr9Llb%2Ftf3DXhQ0R7njlmRHzj97P%2BKeUeqRjg%2B3Q2fTCW%2FCwQTfHD5B814o4AJNVPsUf0ulLbIKFNNFfljatThKNMSqVujCS%2BKU2f64dLIzMvOrhCybgJVZzZVYWTy0QOBRf0qd945BvPhHamnFtWdgJzemixbIxQ98O76c4qkECGIkj9RbVCIRa2E9SYQtjAnbBDwL7IVykcaF4982njVFCDMXUGR2dIrhXElUmEoOuPhRf9aKsqGi8HubaG2E4qduEFDhqNl0l0731hWO4lGoqoSaax01chgPa7K6Y%2B1%2BERoYUNgU4oYD2NtFmik2K4ZXpga%2FmzJwKodyjyled2ntMz3n1H3jPFRPeEtEHAn2KvO7EpX77n8wLR06hZ8dxgOR9YmuQwr6KsyAY6pgGSA19acgYLRdYEiGTCsC858SHubeVneX7GYCuV%2F%2BPYA1T1dvLAVNSTDCPaQj%2B0B1Uysg9T0WprP9O0K1IiTAYdUmSuBJsTFFotElbx2sNL1XoLbbziOMkbLbK%2FvsDRYToAMi9gmkS3HLgOPX6ii2W606sCSK%2BX1ioRe6ReKN%2BK%2BrboIIiv%2FR8TY2pxDU6phQhZg9sJbtTqAOaHMBT4V74cEvA3vGFx&X-Amz-Signature=53fc7935aee71a2b7d47b68b2a787627ebbe8ed93837811aa079dfeee793861f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYQ2PMQI%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwHkDQaGE83dfsNVyz64imAtL27VlHPvPf5ulf4uk2KAiAo3qGRYdJ5cZ%2Bx%2FWQYMUIJxFCemUYklS32iixt14gGgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0HlNTE2J8VtB1OjKtwDtwMM7bSMu947zIgwhI5t2xZHL%2FcM40C205TbLT9ER7Na02FSw7s0l1wzlqpx4Sefv230rYJMpWQBWNBlwKO45%2FTsd0HvU%2FqzJCPNDXu%2FXbg25i7dfPnxujvuZ2unRcOnq90Xw0QdrBBi3cBv5BOe89mvx2DzRW8J28SWYuM84l8x1zyDrVDlzkLzGhQCUhi0ysCcSe%2B%2FrNtMu37P%2FPbNwAZBg5C%2BT%2BeG0od4VFOMM6LJmdzuwkaAr9Llb%2Ftf3DXhQ0R7njlmRHzj97P%2BKeUeqRjg%2B3Q2fTCW%2FCwQTfHD5B814o4AJNVPsUf0ulLbIKFNNFfljatThKNMSqVujCS%2BKU2f64dLIzMvOrhCybgJVZzZVYWTy0QOBRf0qd945BvPhHamnFtWdgJzemixbIxQ98O76c4qkECGIkj9RbVCIRa2E9SYQtjAnbBDwL7IVykcaF4982njVFCDMXUGR2dIrhXElUmEoOuPhRf9aKsqGi8HubaG2E4qduEFDhqNl0l0731hWO4lGoqoSaax01chgPa7K6Y%2B1%2BERoYUNgU4oYD2NtFmik2K4ZXpga%2FmzJwKodyjyled2ntMz3n1H3jPFRPeEtEHAn2KvO7EpX77n8wLR06hZ8dxgOR9YmuQwr6KsyAY6pgGSA19acgYLRdYEiGTCsC858SHubeVneX7GYCuV%2F%2BPYA1T1dvLAVNSTDCPaQj%2B0B1Uysg9T0WprP9O0K1IiTAYdUmSuBJsTFFotElbx2sNL1XoLbbziOMkbLbK%2FvsDRYToAMi9gmkS3HLgOPX6ii2W606sCSK%2BX1ioRe6ReKN%2BK%2BrboIIiv%2FR8TY2pxDU6phQhZg9sJbtTqAOaHMBT4V74cEvA3vGFx&X-Amz-Signature=55fb5ac06a62069e8a17571d62994d2b86e415f35add7c1c1fe806a221f4545d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYQ2PMQI%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwHkDQaGE83dfsNVyz64imAtL27VlHPvPf5ulf4uk2KAiAo3qGRYdJ5cZ%2Bx%2FWQYMUIJxFCemUYklS32iixt14gGgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0HlNTE2J8VtB1OjKtwDtwMM7bSMu947zIgwhI5t2xZHL%2FcM40C205TbLT9ER7Na02FSw7s0l1wzlqpx4Sefv230rYJMpWQBWNBlwKO45%2FTsd0HvU%2FqzJCPNDXu%2FXbg25i7dfPnxujvuZ2unRcOnq90Xw0QdrBBi3cBv5BOe89mvx2DzRW8J28SWYuM84l8x1zyDrVDlzkLzGhQCUhi0ysCcSe%2B%2FrNtMu37P%2FPbNwAZBg5C%2BT%2BeG0od4VFOMM6LJmdzuwkaAr9Llb%2Ftf3DXhQ0R7njlmRHzj97P%2BKeUeqRjg%2B3Q2fTCW%2FCwQTfHD5B814o4AJNVPsUf0ulLbIKFNNFfljatThKNMSqVujCS%2BKU2f64dLIzMvOrhCybgJVZzZVYWTy0QOBRf0qd945BvPhHamnFtWdgJzemixbIxQ98O76c4qkECGIkj9RbVCIRa2E9SYQtjAnbBDwL7IVykcaF4982njVFCDMXUGR2dIrhXElUmEoOuPhRf9aKsqGi8HubaG2E4qduEFDhqNl0l0731hWO4lGoqoSaax01chgPa7K6Y%2B1%2BERoYUNgU4oYD2NtFmik2K4ZXpga%2FmzJwKodyjyled2ntMz3n1H3jPFRPeEtEHAn2KvO7EpX77n8wLR06hZ8dxgOR9YmuQwr6KsyAY6pgGSA19acgYLRdYEiGTCsC858SHubeVneX7GYCuV%2F%2BPYA1T1dvLAVNSTDCPaQj%2B0B1Uysg9T0WprP9O0K1IiTAYdUmSuBJsTFFotElbx2sNL1XoLbbziOMkbLbK%2FvsDRYToAMi9gmkS3HLgOPX6ii2W606sCSK%2BX1ioRe6ReKN%2BK%2BrboIIiv%2FR8TY2pxDU6phQhZg9sJbtTqAOaHMBT4V74cEvA3vGFx&X-Amz-Signature=5fb96007702d92b5cbe5ec176393291174b1c77d6df53cfa67027fc1e40f7ef5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYQ2PMQI%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwHkDQaGE83dfsNVyz64imAtL27VlHPvPf5ulf4uk2KAiAo3qGRYdJ5cZ%2Bx%2FWQYMUIJxFCemUYklS32iixt14gGgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0HlNTE2J8VtB1OjKtwDtwMM7bSMu947zIgwhI5t2xZHL%2FcM40C205TbLT9ER7Na02FSw7s0l1wzlqpx4Sefv230rYJMpWQBWNBlwKO45%2FTsd0HvU%2FqzJCPNDXu%2FXbg25i7dfPnxujvuZ2unRcOnq90Xw0QdrBBi3cBv5BOe89mvx2DzRW8J28SWYuM84l8x1zyDrVDlzkLzGhQCUhi0ysCcSe%2B%2FrNtMu37P%2FPbNwAZBg5C%2BT%2BeG0od4VFOMM6LJmdzuwkaAr9Llb%2Ftf3DXhQ0R7njlmRHzj97P%2BKeUeqRjg%2B3Q2fTCW%2FCwQTfHD5B814o4AJNVPsUf0ulLbIKFNNFfljatThKNMSqVujCS%2BKU2f64dLIzMvOrhCybgJVZzZVYWTy0QOBRf0qd945BvPhHamnFtWdgJzemixbIxQ98O76c4qkECGIkj9RbVCIRa2E9SYQtjAnbBDwL7IVykcaF4982njVFCDMXUGR2dIrhXElUmEoOuPhRf9aKsqGi8HubaG2E4qduEFDhqNl0l0731hWO4lGoqoSaax01chgPa7K6Y%2B1%2BERoYUNgU4oYD2NtFmik2K4ZXpga%2FmzJwKodyjyled2ntMz3n1H3jPFRPeEtEHAn2KvO7EpX77n8wLR06hZ8dxgOR9YmuQwr6KsyAY6pgGSA19acgYLRdYEiGTCsC858SHubeVneX7GYCuV%2F%2BPYA1T1dvLAVNSTDCPaQj%2B0B1Uysg9T0WprP9O0K1IiTAYdUmSuBJsTFFotElbx2sNL1XoLbbziOMkbLbK%2FvsDRYToAMi9gmkS3HLgOPX6ii2W606sCSK%2BX1ioRe6ReKN%2BK%2BrboIIiv%2FR8TY2pxDU6phQhZg9sJbtTqAOaHMBT4V74cEvA3vGFx&X-Amz-Signature=58f1ac100e8d45df750026caf6d2d1980b91d49458bf9c18f0ae94b4bf321a86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYQ2PMQI%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwHkDQaGE83dfsNVyz64imAtL27VlHPvPf5ulf4uk2KAiAo3qGRYdJ5cZ%2Bx%2FWQYMUIJxFCemUYklS32iixt14gGgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0HlNTE2J8VtB1OjKtwDtwMM7bSMu947zIgwhI5t2xZHL%2FcM40C205TbLT9ER7Na02FSw7s0l1wzlqpx4Sefv230rYJMpWQBWNBlwKO45%2FTsd0HvU%2FqzJCPNDXu%2FXbg25i7dfPnxujvuZ2unRcOnq90Xw0QdrBBi3cBv5BOe89mvx2DzRW8J28SWYuM84l8x1zyDrVDlzkLzGhQCUhi0ysCcSe%2B%2FrNtMu37P%2FPbNwAZBg5C%2BT%2BeG0od4VFOMM6LJmdzuwkaAr9Llb%2Ftf3DXhQ0R7njlmRHzj97P%2BKeUeqRjg%2B3Q2fTCW%2FCwQTfHD5B814o4AJNVPsUf0ulLbIKFNNFfljatThKNMSqVujCS%2BKU2f64dLIzMvOrhCybgJVZzZVYWTy0QOBRf0qd945BvPhHamnFtWdgJzemixbIxQ98O76c4qkECGIkj9RbVCIRa2E9SYQtjAnbBDwL7IVykcaF4982njVFCDMXUGR2dIrhXElUmEoOuPhRf9aKsqGi8HubaG2E4qduEFDhqNl0l0731hWO4lGoqoSaax01chgPa7K6Y%2B1%2BERoYUNgU4oYD2NtFmik2K4ZXpga%2FmzJwKodyjyled2ntMz3n1H3jPFRPeEtEHAn2KvO7EpX77n8wLR06hZ8dxgOR9YmuQwr6KsyAY6pgGSA19acgYLRdYEiGTCsC858SHubeVneX7GYCuV%2F%2BPYA1T1dvLAVNSTDCPaQj%2B0B1Uysg9T0WprP9O0K1IiTAYdUmSuBJsTFFotElbx2sNL1XoLbbziOMkbLbK%2FvsDRYToAMi9gmkS3HLgOPX6ii2W606sCSK%2BX1ioRe6ReKN%2BK%2BrboIIiv%2FR8TY2pxDU6phQhZg9sJbtTqAOaHMBT4V74cEvA3vGFx&X-Amz-Signature=8aa270dad1f4f9d2ff6f1862f293ea84a0bcf2bf0ce344d3d2cfeaa59c8d3329&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYQ2PMQI%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwHkDQaGE83dfsNVyz64imAtL27VlHPvPf5ulf4uk2KAiAo3qGRYdJ5cZ%2Bx%2FWQYMUIJxFCemUYklS32iixt14gGgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0HlNTE2J8VtB1OjKtwDtwMM7bSMu947zIgwhI5t2xZHL%2FcM40C205TbLT9ER7Na02FSw7s0l1wzlqpx4Sefv230rYJMpWQBWNBlwKO45%2FTsd0HvU%2FqzJCPNDXu%2FXbg25i7dfPnxujvuZ2unRcOnq90Xw0QdrBBi3cBv5BOe89mvx2DzRW8J28SWYuM84l8x1zyDrVDlzkLzGhQCUhi0ysCcSe%2B%2FrNtMu37P%2FPbNwAZBg5C%2BT%2BeG0od4VFOMM6LJmdzuwkaAr9Llb%2Ftf3DXhQ0R7njlmRHzj97P%2BKeUeqRjg%2B3Q2fTCW%2FCwQTfHD5B814o4AJNVPsUf0ulLbIKFNNFfljatThKNMSqVujCS%2BKU2f64dLIzMvOrhCybgJVZzZVYWTy0QOBRf0qd945BvPhHamnFtWdgJzemixbIxQ98O76c4qkECGIkj9RbVCIRa2E9SYQtjAnbBDwL7IVykcaF4982njVFCDMXUGR2dIrhXElUmEoOuPhRf9aKsqGi8HubaG2E4qduEFDhqNl0l0731hWO4lGoqoSaax01chgPa7K6Y%2B1%2BERoYUNgU4oYD2NtFmik2K4ZXpga%2FmzJwKodyjyled2ntMz3n1H3jPFRPeEtEHAn2KvO7EpX77n8wLR06hZ8dxgOR9YmuQwr6KsyAY6pgGSA19acgYLRdYEiGTCsC858SHubeVneX7GYCuV%2F%2BPYA1T1dvLAVNSTDCPaQj%2B0B1Uysg9T0WprP9O0K1IiTAYdUmSuBJsTFFotElbx2sNL1XoLbbziOMkbLbK%2FvsDRYToAMi9gmkS3HLgOPX6ii2W606sCSK%2BX1ioRe6ReKN%2BK%2BrboIIiv%2FR8TY2pxDU6phQhZg9sJbtTqAOaHMBT4V74cEvA3vGFx&X-Amz-Signature=b95aa1908f1b6118a805186a97c206083284f047f197ad37ece91ea5d7641aaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYQ2PMQI%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwHkDQaGE83dfsNVyz64imAtL27VlHPvPf5ulf4uk2KAiAo3qGRYdJ5cZ%2Bx%2FWQYMUIJxFCemUYklS32iixt14gGgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0HlNTE2J8VtB1OjKtwDtwMM7bSMu947zIgwhI5t2xZHL%2FcM40C205TbLT9ER7Na02FSw7s0l1wzlqpx4Sefv230rYJMpWQBWNBlwKO45%2FTsd0HvU%2FqzJCPNDXu%2FXbg25i7dfPnxujvuZ2unRcOnq90Xw0QdrBBi3cBv5BOe89mvx2DzRW8J28SWYuM84l8x1zyDrVDlzkLzGhQCUhi0ysCcSe%2B%2FrNtMu37P%2FPbNwAZBg5C%2BT%2BeG0od4VFOMM6LJmdzuwkaAr9Llb%2Ftf3DXhQ0R7njlmRHzj97P%2BKeUeqRjg%2B3Q2fTCW%2FCwQTfHD5B814o4AJNVPsUf0ulLbIKFNNFfljatThKNMSqVujCS%2BKU2f64dLIzMvOrhCybgJVZzZVYWTy0QOBRf0qd945BvPhHamnFtWdgJzemixbIxQ98O76c4qkECGIkj9RbVCIRa2E9SYQtjAnbBDwL7IVykcaF4982njVFCDMXUGR2dIrhXElUmEoOuPhRf9aKsqGi8HubaG2E4qduEFDhqNl0l0731hWO4lGoqoSaax01chgPa7K6Y%2B1%2BERoYUNgU4oYD2NtFmik2K4ZXpga%2FmzJwKodyjyled2ntMz3n1H3jPFRPeEtEHAn2KvO7EpX77n8wLR06hZ8dxgOR9YmuQwr6KsyAY6pgGSA19acgYLRdYEiGTCsC858SHubeVneX7GYCuV%2F%2BPYA1T1dvLAVNSTDCPaQj%2B0B1Uysg9T0WprP9O0K1IiTAYdUmSuBJsTFFotElbx2sNL1XoLbbziOMkbLbK%2FvsDRYToAMi9gmkS3HLgOPX6ii2W606sCSK%2BX1ioRe6ReKN%2BK%2BrboIIiv%2FR8TY2pxDU6phQhZg9sJbtTqAOaHMBT4V74cEvA3vGFx&X-Amz-Signature=0768535862dec4d481a200ab56eb7526b134ceb64490503e75e7d9122b9fffaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYQ2PMQI%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwHkDQaGE83dfsNVyz64imAtL27VlHPvPf5ulf4uk2KAiAo3qGRYdJ5cZ%2Bx%2FWQYMUIJxFCemUYklS32iixt14gGgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0HlNTE2J8VtB1OjKtwDtwMM7bSMu947zIgwhI5t2xZHL%2FcM40C205TbLT9ER7Na02FSw7s0l1wzlqpx4Sefv230rYJMpWQBWNBlwKO45%2FTsd0HvU%2FqzJCPNDXu%2FXbg25i7dfPnxujvuZ2unRcOnq90Xw0QdrBBi3cBv5BOe89mvx2DzRW8J28SWYuM84l8x1zyDrVDlzkLzGhQCUhi0ysCcSe%2B%2FrNtMu37P%2FPbNwAZBg5C%2BT%2BeG0od4VFOMM6LJmdzuwkaAr9Llb%2Ftf3DXhQ0R7njlmRHzj97P%2BKeUeqRjg%2B3Q2fTCW%2FCwQTfHD5B814o4AJNVPsUf0ulLbIKFNNFfljatThKNMSqVujCS%2BKU2f64dLIzMvOrhCybgJVZzZVYWTy0QOBRf0qd945BvPhHamnFtWdgJzemixbIxQ98O76c4qkECGIkj9RbVCIRa2E9SYQtjAnbBDwL7IVykcaF4982njVFCDMXUGR2dIrhXElUmEoOuPhRf9aKsqGi8HubaG2E4qduEFDhqNl0l0731hWO4lGoqoSaax01chgPa7K6Y%2B1%2BERoYUNgU4oYD2NtFmik2K4ZXpga%2FmzJwKodyjyled2ntMz3n1H3jPFRPeEtEHAn2KvO7EpX77n8wLR06hZ8dxgOR9YmuQwr6KsyAY6pgGSA19acgYLRdYEiGTCsC858SHubeVneX7GYCuV%2F%2BPYA1T1dvLAVNSTDCPaQj%2B0B1Uysg9T0WprP9O0K1IiTAYdUmSuBJsTFFotElbx2sNL1XoLbbziOMkbLbK%2FvsDRYToAMi9gmkS3HLgOPX6ii2W606sCSK%2BX1ioRe6ReKN%2BK%2BrboIIiv%2FR8TY2pxDU6phQhZg9sJbtTqAOaHMBT4V74cEvA3vGFx&X-Amz-Signature=c1b61f2607760a8c20bd0823a02d00e11a577835f60553bb8b0dad4140a1e5d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYQ2PMQI%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwHkDQaGE83dfsNVyz64imAtL27VlHPvPf5ulf4uk2KAiAo3qGRYdJ5cZ%2Bx%2FWQYMUIJxFCemUYklS32iixt14gGgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0HlNTE2J8VtB1OjKtwDtwMM7bSMu947zIgwhI5t2xZHL%2FcM40C205TbLT9ER7Na02FSw7s0l1wzlqpx4Sefv230rYJMpWQBWNBlwKO45%2FTsd0HvU%2FqzJCPNDXu%2FXbg25i7dfPnxujvuZ2unRcOnq90Xw0QdrBBi3cBv5BOe89mvx2DzRW8J28SWYuM84l8x1zyDrVDlzkLzGhQCUhi0ysCcSe%2B%2FrNtMu37P%2FPbNwAZBg5C%2BT%2BeG0od4VFOMM6LJmdzuwkaAr9Llb%2Ftf3DXhQ0R7njlmRHzj97P%2BKeUeqRjg%2B3Q2fTCW%2FCwQTfHD5B814o4AJNVPsUf0ulLbIKFNNFfljatThKNMSqVujCS%2BKU2f64dLIzMvOrhCybgJVZzZVYWTy0QOBRf0qd945BvPhHamnFtWdgJzemixbIxQ98O76c4qkECGIkj9RbVCIRa2E9SYQtjAnbBDwL7IVykcaF4982njVFCDMXUGR2dIrhXElUmEoOuPhRf9aKsqGi8HubaG2E4qduEFDhqNl0l0731hWO4lGoqoSaax01chgPa7K6Y%2B1%2BERoYUNgU4oYD2NtFmik2K4ZXpga%2FmzJwKodyjyled2ntMz3n1H3jPFRPeEtEHAn2KvO7EpX77n8wLR06hZ8dxgOR9YmuQwr6KsyAY6pgGSA19acgYLRdYEiGTCsC858SHubeVneX7GYCuV%2F%2BPYA1T1dvLAVNSTDCPaQj%2B0B1Uysg9T0WprP9O0K1IiTAYdUmSuBJsTFFotElbx2sNL1XoLbbziOMkbLbK%2FvsDRYToAMi9gmkS3HLgOPX6ii2W606sCSK%2BX1ioRe6ReKN%2BK%2BrboIIiv%2FR8TY2pxDU6phQhZg9sJbtTqAOaHMBT4V74cEvA3vGFx&X-Amz-Signature=05f74c1e46aad2bc55fe731f37523e95035c58b41a6ebc4ed104ed50b0826abe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYQ2PMQI%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwHkDQaGE83dfsNVyz64imAtL27VlHPvPf5ulf4uk2KAiAo3qGRYdJ5cZ%2Bx%2FWQYMUIJxFCemUYklS32iixt14gGgSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0HlNTE2J8VtB1OjKtwDtwMM7bSMu947zIgwhI5t2xZHL%2FcM40C205TbLT9ER7Na02FSw7s0l1wzlqpx4Sefv230rYJMpWQBWNBlwKO45%2FTsd0HvU%2FqzJCPNDXu%2FXbg25i7dfPnxujvuZ2unRcOnq90Xw0QdrBBi3cBv5BOe89mvx2DzRW8J28SWYuM84l8x1zyDrVDlzkLzGhQCUhi0ysCcSe%2B%2FrNtMu37P%2FPbNwAZBg5C%2BT%2BeG0od4VFOMM6LJmdzuwkaAr9Llb%2Ftf3DXhQ0R7njlmRHzj97P%2BKeUeqRjg%2B3Q2fTCW%2FCwQTfHD5B814o4AJNVPsUf0ulLbIKFNNFfljatThKNMSqVujCS%2BKU2f64dLIzMvOrhCybgJVZzZVYWTy0QOBRf0qd945BvPhHamnFtWdgJzemixbIxQ98O76c4qkECGIkj9RbVCIRa2E9SYQtjAnbBDwL7IVykcaF4982njVFCDMXUGR2dIrhXElUmEoOuPhRf9aKsqGi8HubaG2E4qduEFDhqNl0l0731hWO4lGoqoSaax01chgPa7K6Y%2B1%2BERoYUNgU4oYD2NtFmik2K4ZXpga%2FmzJwKodyjyled2ntMz3n1H3jPFRPeEtEHAn2KvO7EpX77n8wLR06hZ8dxgOR9YmuQwr6KsyAY6pgGSA19acgYLRdYEiGTCsC858SHubeVneX7GYCuV%2F%2BPYA1T1dvLAVNSTDCPaQj%2B0B1Uysg9T0WprP9O0K1IiTAYdUmSuBJsTFFotElbx2sNL1XoLbbziOMkbLbK%2FvsDRYToAMi9gmkS3HLgOPX6ii2W606sCSK%2BX1ioRe6ReKN%2BK%2BrboIIiv%2FR8TY2pxDU6phQhZg9sJbtTqAOaHMBT4V74cEvA3vGFx&X-Amz-Signature=f1d67a8823903d1435f5f74a6dc2115d0be408d1364d50f6f89f09b110ccf2c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

