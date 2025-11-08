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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MA3MUGS%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCFUWR0j%2BB%2BqSzrUOsnjAa1rqC8J1k3xiM4TfKf6LbnuwIgRzaHzUWvfzv35TM73Ae8OD6oMOu%2BcJ1ORRFe85QZ8hcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDSeO6a1MMai%2FOfBCrcA2yoMqWq9Z1PBMNuWj3oCHATmNbL9U6YDlef7uGGQp1X5ORTcPiJmmDYYa6B1D%2F%2FzPHI%2FKiad9yCriIcTpadkHIw8uLBBucxC0sIdd8X5JrE91bzhHcY2G2OVt0G9U7jHoYdbQvVG8jhMV7Qu%2BxCYtLJS3VOU5obbx8fnHdoVBFdTy%2BfsXKmM1hT4TuJ3ZGF0HkWwRUP5i8o2IA7tGP%2FsCiBgU8WLo6lmx1qYUDtbyhS2qoHKHuFHUAubFsIBNoTjPp7YGA%2FUH84Je1lQFyqofFemBFOAIMw1oczU9oH8BHq15Skyc8SeFWrnYFILP6KHPvgrdXNBjqCOLs1xTNxpmeGQuf4kxJh1hTTRTGyYAGRB9%2Fcd6kwGlt3IIdXBfkj7QpD1Wybm8nyK2u8P6KvTXdYRFI%2B7xrF0%2BvhAg4ozBeHFi8PbkPqljAgkGTWtzn8Cn5T6IGC9oUe3ZME0%2FUDNh3SCvfCw3yR304TCN%2FD%2BzfSTZvVv3Z0xg0b%2BzWhsFpys3Kd8MIInCKSpmQAk2eC50Ch6AIPKtj3UEfbwQcabHpw2hRh4F6KUD4%2FWtwQsj9D8p8gVeY8zctgqY6Qph8r0NPhgYGnhDEuufNsz2NKYNQpBNx%2BTHWOjREMdSJLMNTQusgGOqUB6vdrQky2Vz%2BW4rzZJPWg5PtIh%2BGDC4BIQD1PWCXyWRXQXXKxeRj8KCORmEoaGduX0Wl9iAqyXyj49TW9%2Fwu%2FfP6DVXywYFR5SSO5r8Gf%2FPtZuew3m%2FlrqVIZPsTTf4dxzn0ZvlvtSZ9pEwm6nPMtyXQTN66OGp68QU8jajRZ3FME0U4ixS%2FS9Uvpzm1%2BOJjczlGfA%2FbMATHHIfa4Yag6RhwUW2kV&X-Amz-Signature=7f75a942465e37085ebb951a8d706b379ca469d488bb1d6717501b328c7ab835&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MA3MUGS%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCFUWR0j%2BB%2BqSzrUOsnjAa1rqC8J1k3xiM4TfKf6LbnuwIgRzaHzUWvfzv35TM73Ae8OD6oMOu%2BcJ1ORRFe85QZ8hcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDSeO6a1MMai%2FOfBCrcA2yoMqWq9Z1PBMNuWj3oCHATmNbL9U6YDlef7uGGQp1X5ORTcPiJmmDYYa6B1D%2F%2FzPHI%2FKiad9yCriIcTpadkHIw8uLBBucxC0sIdd8X5JrE91bzhHcY2G2OVt0G9U7jHoYdbQvVG8jhMV7Qu%2BxCYtLJS3VOU5obbx8fnHdoVBFdTy%2BfsXKmM1hT4TuJ3ZGF0HkWwRUP5i8o2IA7tGP%2FsCiBgU8WLo6lmx1qYUDtbyhS2qoHKHuFHUAubFsIBNoTjPp7YGA%2FUH84Je1lQFyqofFemBFOAIMw1oczU9oH8BHq15Skyc8SeFWrnYFILP6KHPvgrdXNBjqCOLs1xTNxpmeGQuf4kxJh1hTTRTGyYAGRB9%2Fcd6kwGlt3IIdXBfkj7QpD1Wybm8nyK2u8P6KvTXdYRFI%2B7xrF0%2BvhAg4ozBeHFi8PbkPqljAgkGTWtzn8Cn5T6IGC9oUe3ZME0%2FUDNh3SCvfCw3yR304TCN%2FD%2BzfSTZvVv3Z0xg0b%2BzWhsFpys3Kd8MIInCKSpmQAk2eC50Ch6AIPKtj3UEfbwQcabHpw2hRh4F6KUD4%2FWtwQsj9D8p8gVeY8zctgqY6Qph8r0NPhgYGnhDEuufNsz2NKYNQpBNx%2BTHWOjREMdSJLMNTQusgGOqUB6vdrQky2Vz%2BW4rzZJPWg5PtIh%2BGDC4BIQD1PWCXyWRXQXXKxeRj8KCORmEoaGduX0Wl9iAqyXyj49TW9%2Fwu%2FfP6DVXywYFR5SSO5r8Gf%2FPtZuew3m%2FlrqVIZPsTTf4dxzn0ZvlvtSZ9pEwm6nPMtyXQTN66OGp68QU8jajRZ3FME0U4ixS%2FS9Uvpzm1%2BOJjczlGfA%2FbMATHHIfa4Yag6RhwUW2kV&X-Amz-Signature=e7a0e699478e77e3c2912d8b5a887c1c6da3cd7172c3b9a8d9a9525de12b4b3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MA3MUGS%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCFUWR0j%2BB%2BqSzrUOsnjAa1rqC8J1k3xiM4TfKf6LbnuwIgRzaHzUWvfzv35TM73Ae8OD6oMOu%2BcJ1ORRFe85QZ8hcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDSeO6a1MMai%2FOfBCrcA2yoMqWq9Z1PBMNuWj3oCHATmNbL9U6YDlef7uGGQp1X5ORTcPiJmmDYYa6B1D%2F%2FzPHI%2FKiad9yCriIcTpadkHIw8uLBBucxC0sIdd8X5JrE91bzhHcY2G2OVt0G9U7jHoYdbQvVG8jhMV7Qu%2BxCYtLJS3VOU5obbx8fnHdoVBFdTy%2BfsXKmM1hT4TuJ3ZGF0HkWwRUP5i8o2IA7tGP%2FsCiBgU8WLo6lmx1qYUDtbyhS2qoHKHuFHUAubFsIBNoTjPp7YGA%2FUH84Je1lQFyqofFemBFOAIMw1oczU9oH8BHq15Skyc8SeFWrnYFILP6KHPvgrdXNBjqCOLs1xTNxpmeGQuf4kxJh1hTTRTGyYAGRB9%2Fcd6kwGlt3IIdXBfkj7QpD1Wybm8nyK2u8P6KvTXdYRFI%2B7xrF0%2BvhAg4ozBeHFi8PbkPqljAgkGTWtzn8Cn5T6IGC9oUe3ZME0%2FUDNh3SCvfCw3yR304TCN%2FD%2BzfSTZvVv3Z0xg0b%2BzWhsFpys3Kd8MIInCKSpmQAk2eC50Ch6AIPKtj3UEfbwQcabHpw2hRh4F6KUD4%2FWtwQsj9D8p8gVeY8zctgqY6Qph8r0NPhgYGnhDEuufNsz2NKYNQpBNx%2BTHWOjREMdSJLMNTQusgGOqUB6vdrQky2Vz%2BW4rzZJPWg5PtIh%2BGDC4BIQD1PWCXyWRXQXXKxeRj8KCORmEoaGduX0Wl9iAqyXyj49TW9%2Fwu%2FfP6DVXywYFR5SSO5r8Gf%2FPtZuew3m%2FlrqVIZPsTTf4dxzn0ZvlvtSZ9pEwm6nPMtyXQTN66OGp68QU8jajRZ3FME0U4ixS%2FS9Uvpzm1%2BOJjczlGfA%2FbMATHHIfa4Yag6RhwUW2kV&X-Amz-Signature=f6bc39fbcfd0f47dd24ea2403c96cd590d068ccec1862823020a22578b50701c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MA3MUGS%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCFUWR0j%2BB%2BqSzrUOsnjAa1rqC8J1k3xiM4TfKf6LbnuwIgRzaHzUWvfzv35TM73Ae8OD6oMOu%2BcJ1ORRFe85QZ8hcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDSeO6a1MMai%2FOfBCrcA2yoMqWq9Z1PBMNuWj3oCHATmNbL9U6YDlef7uGGQp1X5ORTcPiJmmDYYa6B1D%2F%2FzPHI%2FKiad9yCriIcTpadkHIw8uLBBucxC0sIdd8X5JrE91bzhHcY2G2OVt0G9U7jHoYdbQvVG8jhMV7Qu%2BxCYtLJS3VOU5obbx8fnHdoVBFdTy%2BfsXKmM1hT4TuJ3ZGF0HkWwRUP5i8o2IA7tGP%2FsCiBgU8WLo6lmx1qYUDtbyhS2qoHKHuFHUAubFsIBNoTjPp7YGA%2FUH84Je1lQFyqofFemBFOAIMw1oczU9oH8BHq15Skyc8SeFWrnYFILP6KHPvgrdXNBjqCOLs1xTNxpmeGQuf4kxJh1hTTRTGyYAGRB9%2Fcd6kwGlt3IIdXBfkj7QpD1Wybm8nyK2u8P6KvTXdYRFI%2B7xrF0%2BvhAg4ozBeHFi8PbkPqljAgkGTWtzn8Cn5T6IGC9oUe3ZME0%2FUDNh3SCvfCw3yR304TCN%2FD%2BzfSTZvVv3Z0xg0b%2BzWhsFpys3Kd8MIInCKSpmQAk2eC50Ch6AIPKtj3UEfbwQcabHpw2hRh4F6KUD4%2FWtwQsj9D8p8gVeY8zctgqY6Qph8r0NPhgYGnhDEuufNsz2NKYNQpBNx%2BTHWOjREMdSJLMNTQusgGOqUB6vdrQky2Vz%2BW4rzZJPWg5PtIh%2BGDC4BIQD1PWCXyWRXQXXKxeRj8KCORmEoaGduX0Wl9iAqyXyj49TW9%2Fwu%2FfP6DVXywYFR5SSO5r8Gf%2FPtZuew3m%2FlrqVIZPsTTf4dxzn0ZvlvtSZ9pEwm6nPMtyXQTN66OGp68QU8jajRZ3FME0U4ixS%2FS9Uvpzm1%2BOJjczlGfA%2FbMATHHIfa4Yag6RhwUW2kV&X-Amz-Signature=c4af65e0329d72fe5a463b62759b71937f32268471f94b1630ab4c6eb77fce89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MA3MUGS%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCFUWR0j%2BB%2BqSzrUOsnjAa1rqC8J1k3xiM4TfKf6LbnuwIgRzaHzUWvfzv35TM73Ae8OD6oMOu%2BcJ1ORRFe85QZ8hcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDSeO6a1MMai%2FOfBCrcA2yoMqWq9Z1PBMNuWj3oCHATmNbL9U6YDlef7uGGQp1X5ORTcPiJmmDYYa6B1D%2F%2FzPHI%2FKiad9yCriIcTpadkHIw8uLBBucxC0sIdd8X5JrE91bzhHcY2G2OVt0G9U7jHoYdbQvVG8jhMV7Qu%2BxCYtLJS3VOU5obbx8fnHdoVBFdTy%2BfsXKmM1hT4TuJ3ZGF0HkWwRUP5i8o2IA7tGP%2FsCiBgU8WLo6lmx1qYUDtbyhS2qoHKHuFHUAubFsIBNoTjPp7YGA%2FUH84Je1lQFyqofFemBFOAIMw1oczU9oH8BHq15Skyc8SeFWrnYFILP6KHPvgrdXNBjqCOLs1xTNxpmeGQuf4kxJh1hTTRTGyYAGRB9%2Fcd6kwGlt3IIdXBfkj7QpD1Wybm8nyK2u8P6KvTXdYRFI%2B7xrF0%2BvhAg4ozBeHFi8PbkPqljAgkGTWtzn8Cn5T6IGC9oUe3ZME0%2FUDNh3SCvfCw3yR304TCN%2FD%2BzfSTZvVv3Z0xg0b%2BzWhsFpys3Kd8MIInCKSpmQAk2eC50Ch6AIPKtj3UEfbwQcabHpw2hRh4F6KUD4%2FWtwQsj9D8p8gVeY8zctgqY6Qph8r0NPhgYGnhDEuufNsz2NKYNQpBNx%2BTHWOjREMdSJLMNTQusgGOqUB6vdrQky2Vz%2BW4rzZJPWg5PtIh%2BGDC4BIQD1PWCXyWRXQXXKxeRj8KCORmEoaGduX0Wl9iAqyXyj49TW9%2Fwu%2FfP6DVXywYFR5SSO5r8Gf%2FPtZuew3m%2FlrqVIZPsTTf4dxzn0ZvlvtSZ9pEwm6nPMtyXQTN66OGp68QU8jajRZ3FME0U4ixS%2FS9Uvpzm1%2BOJjczlGfA%2FbMATHHIfa4Yag6RhwUW2kV&X-Amz-Signature=ff9d919dba8382a0561c115213b974b5cb1cc2aecb88de2b953a8c0026aadaf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MA3MUGS%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCFUWR0j%2BB%2BqSzrUOsnjAa1rqC8J1k3xiM4TfKf6LbnuwIgRzaHzUWvfzv35TM73Ae8OD6oMOu%2BcJ1ORRFe85QZ8hcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDSeO6a1MMai%2FOfBCrcA2yoMqWq9Z1PBMNuWj3oCHATmNbL9U6YDlef7uGGQp1X5ORTcPiJmmDYYa6B1D%2F%2FzPHI%2FKiad9yCriIcTpadkHIw8uLBBucxC0sIdd8X5JrE91bzhHcY2G2OVt0G9U7jHoYdbQvVG8jhMV7Qu%2BxCYtLJS3VOU5obbx8fnHdoVBFdTy%2BfsXKmM1hT4TuJ3ZGF0HkWwRUP5i8o2IA7tGP%2FsCiBgU8WLo6lmx1qYUDtbyhS2qoHKHuFHUAubFsIBNoTjPp7YGA%2FUH84Je1lQFyqofFemBFOAIMw1oczU9oH8BHq15Skyc8SeFWrnYFILP6KHPvgrdXNBjqCOLs1xTNxpmeGQuf4kxJh1hTTRTGyYAGRB9%2Fcd6kwGlt3IIdXBfkj7QpD1Wybm8nyK2u8P6KvTXdYRFI%2B7xrF0%2BvhAg4ozBeHFi8PbkPqljAgkGTWtzn8Cn5T6IGC9oUe3ZME0%2FUDNh3SCvfCw3yR304TCN%2FD%2BzfSTZvVv3Z0xg0b%2BzWhsFpys3Kd8MIInCKSpmQAk2eC50Ch6AIPKtj3UEfbwQcabHpw2hRh4F6KUD4%2FWtwQsj9D8p8gVeY8zctgqY6Qph8r0NPhgYGnhDEuufNsz2NKYNQpBNx%2BTHWOjREMdSJLMNTQusgGOqUB6vdrQky2Vz%2BW4rzZJPWg5PtIh%2BGDC4BIQD1PWCXyWRXQXXKxeRj8KCORmEoaGduX0Wl9iAqyXyj49TW9%2Fwu%2FfP6DVXywYFR5SSO5r8Gf%2FPtZuew3m%2FlrqVIZPsTTf4dxzn0ZvlvtSZ9pEwm6nPMtyXQTN66OGp68QU8jajRZ3FME0U4ixS%2FS9Uvpzm1%2BOJjczlGfA%2FbMATHHIfa4Yag6RhwUW2kV&X-Amz-Signature=f15441d070da44fa0cfcda3b3cc8a09bd5f682503b7b3e8f65a0ef3372364e90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MA3MUGS%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCFUWR0j%2BB%2BqSzrUOsnjAa1rqC8J1k3xiM4TfKf6LbnuwIgRzaHzUWvfzv35TM73Ae8OD6oMOu%2BcJ1ORRFe85QZ8hcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDSeO6a1MMai%2FOfBCrcA2yoMqWq9Z1PBMNuWj3oCHATmNbL9U6YDlef7uGGQp1X5ORTcPiJmmDYYa6B1D%2F%2FzPHI%2FKiad9yCriIcTpadkHIw8uLBBucxC0sIdd8X5JrE91bzhHcY2G2OVt0G9U7jHoYdbQvVG8jhMV7Qu%2BxCYtLJS3VOU5obbx8fnHdoVBFdTy%2BfsXKmM1hT4TuJ3ZGF0HkWwRUP5i8o2IA7tGP%2FsCiBgU8WLo6lmx1qYUDtbyhS2qoHKHuFHUAubFsIBNoTjPp7YGA%2FUH84Je1lQFyqofFemBFOAIMw1oczU9oH8BHq15Skyc8SeFWrnYFILP6KHPvgrdXNBjqCOLs1xTNxpmeGQuf4kxJh1hTTRTGyYAGRB9%2Fcd6kwGlt3IIdXBfkj7QpD1Wybm8nyK2u8P6KvTXdYRFI%2B7xrF0%2BvhAg4ozBeHFi8PbkPqljAgkGTWtzn8Cn5T6IGC9oUe3ZME0%2FUDNh3SCvfCw3yR304TCN%2FD%2BzfSTZvVv3Z0xg0b%2BzWhsFpys3Kd8MIInCKSpmQAk2eC50Ch6AIPKtj3UEfbwQcabHpw2hRh4F6KUD4%2FWtwQsj9D8p8gVeY8zctgqY6Qph8r0NPhgYGnhDEuufNsz2NKYNQpBNx%2BTHWOjREMdSJLMNTQusgGOqUB6vdrQky2Vz%2BW4rzZJPWg5PtIh%2BGDC4BIQD1PWCXyWRXQXXKxeRj8KCORmEoaGduX0Wl9iAqyXyj49TW9%2Fwu%2FfP6DVXywYFR5SSO5r8Gf%2FPtZuew3m%2FlrqVIZPsTTf4dxzn0ZvlvtSZ9pEwm6nPMtyXQTN66OGp68QU8jajRZ3FME0U4ixS%2FS9Uvpzm1%2BOJjczlGfA%2FbMATHHIfa4Yag6RhwUW2kV&X-Amz-Signature=05cfae6bdaeba8b19c1707aaf3ab25e8b6ffa3c22bd2914c4a57697a797ec28a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MA3MUGS%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCFUWR0j%2BB%2BqSzrUOsnjAa1rqC8J1k3xiM4TfKf6LbnuwIgRzaHzUWvfzv35TM73Ae8OD6oMOu%2BcJ1ORRFe85QZ8hcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDSeO6a1MMai%2FOfBCrcA2yoMqWq9Z1PBMNuWj3oCHATmNbL9U6YDlef7uGGQp1X5ORTcPiJmmDYYa6B1D%2F%2FzPHI%2FKiad9yCriIcTpadkHIw8uLBBucxC0sIdd8X5JrE91bzhHcY2G2OVt0G9U7jHoYdbQvVG8jhMV7Qu%2BxCYtLJS3VOU5obbx8fnHdoVBFdTy%2BfsXKmM1hT4TuJ3ZGF0HkWwRUP5i8o2IA7tGP%2FsCiBgU8WLo6lmx1qYUDtbyhS2qoHKHuFHUAubFsIBNoTjPp7YGA%2FUH84Je1lQFyqofFemBFOAIMw1oczU9oH8BHq15Skyc8SeFWrnYFILP6KHPvgrdXNBjqCOLs1xTNxpmeGQuf4kxJh1hTTRTGyYAGRB9%2Fcd6kwGlt3IIdXBfkj7QpD1Wybm8nyK2u8P6KvTXdYRFI%2B7xrF0%2BvhAg4ozBeHFi8PbkPqljAgkGTWtzn8Cn5T6IGC9oUe3ZME0%2FUDNh3SCvfCw3yR304TCN%2FD%2BzfSTZvVv3Z0xg0b%2BzWhsFpys3Kd8MIInCKSpmQAk2eC50Ch6AIPKtj3UEfbwQcabHpw2hRh4F6KUD4%2FWtwQsj9D8p8gVeY8zctgqY6Qph8r0NPhgYGnhDEuufNsz2NKYNQpBNx%2BTHWOjREMdSJLMNTQusgGOqUB6vdrQky2Vz%2BW4rzZJPWg5PtIh%2BGDC4BIQD1PWCXyWRXQXXKxeRj8KCORmEoaGduX0Wl9iAqyXyj49TW9%2Fwu%2FfP6DVXywYFR5SSO5r8Gf%2FPtZuew3m%2FlrqVIZPsTTf4dxzn0ZvlvtSZ9pEwm6nPMtyXQTN66OGp68QU8jajRZ3FME0U4ixS%2FS9Uvpzm1%2BOJjczlGfA%2FbMATHHIfa4Yag6RhwUW2kV&X-Amz-Signature=fb3feb2616579543abf5b14c42cbfdc6893542b59a5420e2240d5394f351aa93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MA3MUGS%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCFUWR0j%2BB%2BqSzrUOsnjAa1rqC8J1k3xiM4TfKf6LbnuwIgRzaHzUWvfzv35TM73Ae8OD6oMOu%2BcJ1ORRFe85QZ8hcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDSeO6a1MMai%2FOfBCrcA2yoMqWq9Z1PBMNuWj3oCHATmNbL9U6YDlef7uGGQp1X5ORTcPiJmmDYYa6B1D%2F%2FzPHI%2FKiad9yCriIcTpadkHIw8uLBBucxC0sIdd8X5JrE91bzhHcY2G2OVt0G9U7jHoYdbQvVG8jhMV7Qu%2BxCYtLJS3VOU5obbx8fnHdoVBFdTy%2BfsXKmM1hT4TuJ3ZGF0HkWwRUP5i8o2IA7tGP%2FsCiBgU8WLo6lmx1qYUDtbyhS2qoHKHuFHUAubFsIBNoTjPp7YGA%2FUH84Je1lQFyqofFemBFOAIMw1oczU9oH8BHq15Skyc8SeFWrnYFILP6KHPvgrdXNBjqCOLs1xTNxpmeGQuf4kxJh1hTTRTGyYAGRB9%2Fcd6kwGlt3IIdXBfkj7QpD1Wybm8nyK2u8P6KvTXdYRFI%2B7xrF0%2BvhAg4ozBeHFi8PbkPqljAgkGTWtzn8Cn5T6IGC9oUe3ZME0%2FUDNh3SCvfCw3yR304TCN%2FD%2BzfSTZvVv3Z0xg0b%2BzWhsFpys3Kd8MIInCKSpmQAk2eC50Ch6AIPKtj3UEfbwQcabHpw2hRh4F6KUD4%2FWtwQsj9D8p8gVeY8zctgqY6Qph8r0NPhgYGnhDEuufNsz2NKYNQpBNx%2BTHWOjREMdSJLMNTQusgGOqUB6vdrQky2Vz%2BW4rzZJPWg5PtIh%2BGDC4BIQD1PWCXyWRXQXXKxeRj8KCORmEoaGduX0Wl9iAqyXyj49TW9%2Fwu%2FfP6DVXywYFR5SSO5r8Gf%2FPtZuew3m%2FlrqVIZPsTTf4dxzn0ZvlvtSZ9pEwm6nPMtyXQTN66OGp68QU8jajRZ3FME0U4ixS%2FS9Uvpzm1%2BOJjczlGfA%2FbMATHHIfa4Yag6RhwUW2kV&X-Amz-Signature=aca391f2d519d308d29d7c293968bc2edf97224b09978e11d6e730a92065aab2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MA3MUGS%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCFUWR0j%2BB%2BqSzrUOsnjAa1rqC8J1k3xiM4TfKf6LbnuwIgRzaHzUWvfzv35TM73Ae8OD6oMOu%2BcJ1ORRFe85QZ8hcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDSeO6a1MMai%2FOfBCrcA2yoMqWq9Z1PBMNuWj3oCHATmNbL9U6YDlef7uGGQp1X5ORTcPiJmmDYYa6B1D%2F%2FzPHI%2FKiad9yCriIcTpadkHIw8uLBBucxC0sIdd8X5JrE91bzhHcY2G2OVt0G9U7jHoYdbQvVG8jhMV7Qu%2BxCYtLJS3VOU5obbx8fnHdoVBFdTy%2BfsXKmM1hT4TuJ3ZGF0HkWwRUP5i8o2IA7tGP%2FsCiBgU8WLo6lmx1qYUDtbyhS2qoHKHuFHUAubFsIBNoTjPp7YGA%2FUH84Je1lQFyqofFemBFOAIMw1oczU9oH8BHq15Skyc8SeFWrnYFILP6KHPvgrdXNBjqCOLs1xTNxpmeGQuf4kxJh1hTTRTGyYAGRB9%2Fcd6kwGlt3IIdXBfkj7QpD1Wybm8nyK2u8P6KvTXdYRFI%2B7xrF0%2BvhAg4ozBeHFi8PbkPqljAgkGTWtzn8Cn5T6IGC9oUe3ZME0%2FUDNh3SCvfCw3yR304TCN%2FD%2BzfSTZvVv3Z0xg0b%2BzWhsFpys3Kd8MIInCKSpmQAk2eC50Ch6AIPKtj3UEfbwQcabHpw2hRh4F6KUD4%2FWtwQsj9D8p8gVeY8zctgqY6Qph8r0NPhgYGnhDEuufNsz2NKYNQpBNx%2BTHWOjREMdSJLMNTQusgGOqUB6vdrQky2Vz%2BW4rzZJPWg5PtIh%2BGDC4BIQD1PWCXyWRXQXXKxeRj8KCORmEoaGduX0Wl9iAqyXyj49TW9%2Fwu%2FfP6DVXywYFR5SSO5r8Gf%2FPtZuew3m%2FlrqVIZPsTTf4dxzn0ZvlvtSZ9pEwm6nPMtyXQTN66OGp68QU8jajRZ3FME0U4ixS%2FS9Uvpzm1%2BOJjczlGfA%2FbMATHHIfa4Yag6RhwUW2kV&X-Amz-Signature=b45af810155e6aa27b817efe7abfa195988f22dad083a6f8ed0adba9e8f6e61c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

