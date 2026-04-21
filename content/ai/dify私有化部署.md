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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WVJDWU%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGagWfImSyBWiSM%2FSpZrEqKhqUkFxw%2BhzJx3S1TWNtYkAiBfpklLoMxlY%2B0NlQkta9ebDFXqZC85vtBqLeZBnUBjxSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNioMB83ja2Ze%2B5uYKtwDwkw2ZUpUNeS37LmkgD2bvCVTPCooAABfnRxQel3qOoPDfN607hcBkp9YryhHA9Omk47l%2FL0q6LVsZQI8q0%2F5NUHmgOdPw56cCuhxU8T6h1%2FsVQhaS8a9ec%2BkMOQqmXSSCNp31wzkpdf7ctixhADIs%2Fm%2FOjNchta5QJE%2FGbl2nD3HyUaoivQxT52VhpECEk%2BcWqqjPqb7VEJ3Rn1a0gmb4yLs712d0mE4Ua1YBegBj0qQknDK0UgR01BpvRmiiQ%2B80w5o5z0x0dalutBByxknFUfWrC4iBMFoYsw9Yjb0%2By8vLUcdCfp%2FCjDKJwIujO8xB%2BdbAARUPxC6ILQckBftWLoJyINjU2TCn%2BY8JzzOTukFRim18KDpMiJdagjrrfC4krca457k0LRLiZGSLuX8nqF5go1X0j2EgOL7VVIZYka8Xosog9Dlq3%2FE9igHp3F84AXzMqKx0yKdOntoYkXHJLQdFvWx1ps6iF42LT47C%2BPABhFn7qHbAQBTe6j%2BntqJc2OgsrHOHlZpYn3ffe8Rdr1Ew%2FFdeUrnEwMyx%2Fxy0kMJ5I1Yo7TKs41nZKgw7qQNaEj1Db8uP4wWN%2FWkASIAWrFckuFEOwvZ9X7cCYmQY9dpDTTHCiKLXqvXEN4w39WbzwY6pgGgTatjGgJ%2BTwBB6GvPEuW7puL%2FunEDjhTqxmFmPPBl72jw%2FEc2d0ZdkplRopqWb5jgd0Z5tnbFKayxheITQUjB0INBJGi8Xi%2BZIDYWYGP6XtNXRs2QRAXLGF6j3ngxOM0rS1cTzu7x2AIbdqfsXn3AeSC4hLrvpja7Jo8vg%2F3Dk8RbWJpi3NOGVIqoklDIK2KuWvX%2BTQjru3jhNQS%2FIQ8Eh7oaZXfn&X-Amz-Signature=ff1405eb23a4c4426df9ca1e532702f27d0c36a8ff9c5ab58029e60fb12a95f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WVJDWU%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGagWfImSyBWiSM%2FSpZrEqKhqUkFxw%2BhzJx3S1TWNtYkAiBfpklLoMxlY%2B0NlQkta9ebDFXqZC85vtBqLeZBnUBjxSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNioMB83ja2Ze%2B5uYKtwDwkw2ZUpUNeS37LmkgD2bvCVTPCooAABfnRxQel3qOoPDfN607hcBkp9YryhHA9Omk47l%2FL0q6LVsZQI8q0%2F5NUHmgOdPw56cCuhxU8T6h1%2FsVQhaS8a9ec%2BkMOQqmXSSCNp31wzkpdf7ctixhADIs%2Fm%2FOjNchta5QJE%2FGbl2nD3HyUaoivQxT52VhpECEk%2BcWqqjPqb7VEJ3Rn1a0gmb4yLs712d0mE4Ua1YBegBj0qQknDK0UgR01BpvRmiiQ%2B80w5o5z0x0dalutBByxknFUfWrC4iBMFoYsw9Yjb0%2By8vLUcdCfp%2FCjDKJwIujO8xB%2BdbAARUPxC6ILQckBftWLoJyINjU2TCn%2BY8JzzOTukFRim18KDpMiJdagjrrfC4krca457k0LRLiZGSLuX8nqF5go1X0j2EgOL7VVIZYka8Xosog9Dlq3%2FE9igHp3F84AXzMqKx0yKdOntoYkXHJLQdFvWx1ps6iF42LT47C%2BPABhFn7qHbAQBTe6j%2BntqJc2OgsrHOHlZpYn3ffe8Rdr1Ew%2FFdeUrnEwMyx%2Fxy0kMJ5I1Yo7TKs41nZKgw7qQNaEj1Db8uP4wWN%2FWkASIAWrFckuFEOwvZ9X7cCYmQY9dpDTTHCiKLXqvXEN4w39WbzwY6pgGgTatjGgJ%2BTwBB6GvPEuW7puL%2FunEDjhTqxmFmPPBl72jw%2FEc2d0ZdkplRopqWb5jgd0Z5tnbFKayxheITQUjB0INBJGi8Xi%2BZIDYWYGP6XtNXRs2QRAXLGF6j3ngxOM0rS1cTzu7x2AIbdqfsXn3AeSC4hLrvpja7Jo8vg%2F3Dk8RbWJpi3NOGVIqoklDIK2KuWvX%2BTQjru3jhNQS%2FIQ8Eh7oaZXfn&X-Amz-Signature=3a4cb152697a2708950c56c8ab04e620208e354a76657a13840a1f1076abe7b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WVJDWU%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGagWfImSyBWiSM%2FSpZrEqKhqUkFxw%2BhzJx3S1TWNtYkAiBfpklLoMxlY%2B0NlQkta9ebDFXqZC85vtBqLeZBnUBjxSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNioMB83ja2Ze%2B5uYKtwDwkw2ZUpUNeS37LmkgD2bvCVTPCooAABfnRxQel3qOoPDfN607hcBkp9YryhHA9Omk47l%2FL0q6LVsZQI8q0%2F5NUHmgOdPw56cCuhxU8T6h1%2FsVQhaS8a9ec%2BkMOQqmXSSCNp31wzkpdf7ctixhADIs%2Fm%2FOjNchta5QJE%2FGbl2nD3HyUaoivQxT52VhpECEk%2BcWqqjPqb7VEJ3Rn1a0gmb4yLs712d0mE4Ua1YBegBj0qQknDK0UgR01BpvRmiiQ%2B80w5o5z0x0dalutBByxknFUfWrC4iBMFoYsw9Yjb0%2By8vLUcdCfp%2FCjDKJwIujO8xB%2BdbAARUPxC6ILQckBftWLoJyINjU2TCn%2BY8JzzOTukFRim18KDpMiJdagjrrfC4krca457k0LRLiZGSLuX8nqF5go1X0j2EgOL7VVIZYka8Xosog9Dlq3%2FE9igHp3F84AXzMqKx0yKdOntoYkXHJLQdFvWx1ps6iF42LT47C%2BPABhFn7qHbAQBTe6j%2BntqJc2OgsrHOHlZpYn3ffe8Rdr1Ew%2FFdeUrnEwMyx%2Fxy0kMJ5I1Yo7TKs41nZKgw7qQNaEj1Db8uP4wWN%2FWkASIAWrFckuFEOwvZ9X7cCYmQY9dpDTTHCiKLXqvXEN4w39WbzwY6pgGgTatjGgJ%2BTwBB6GvPEuW7puL%2FunEDjhTqxmFmPPBl72jw%2FEc2d0ZdkplRopqWb5jgd0Z5tnbFKayxheITQUjB0INBJGi8Xi%2BZIDYWYGP6XtNXRs2QRAXLGF6j3ngxOM0rS1cTzu7x2AIbdqfsXn3AeSC4hLrvpja7Jo8vg%2F3Dk8RbWJpi3NOGVIqoklDIK2KuWvX%2BTQjru3jhNQS%2FIQ8Eh7oaZXfn&X-Amz-Signature=b290eb163ccac1d78da2383a888c87e454c48ea9363892a38c9be8ef42070d77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WVJDWU%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGagWfImSyBWiSM%2FSpZrEqKhqUkFxw%2BhzJx3S1TWNtYkAiBfpklLoMxlY%2B0NlQkta9ebDFXqZC85vtBqLeZBnUBjxSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNioMB83ja2Ze%2B5uYKtwDwkw2ZUpUNeS37LmkgD2bvCVTPCooAABfnRxQel3qOoPDfN607hcBkp9YryhHA9Omk47l%2FL0q6LVsZQI8q0%2F5NUHmgOdPw56cCuhxU8T6h1%2FsVQhaS8a9ec%2BkMOQqmXSSCNp31wzkpdf7ctixhADIs%2Fm%2FOjNchta5QJE%2FGbl2nD3HyUaoivQxT52VhpECEk%2BcWqqjPqb7VEJ3Rn1a0gmb4yLs712d0mE4Ua1YBegBj0qQknDK0UgR01BpvRmiiQ%2B80w5o5z0x0dalutBByxknFUfWrC4iBMFoYsw9Yjb0%2By8vLUcdCfp%2FCjDKJwIujO8xB%2BdbAARUPxC6ILQckBftWLoJyINjU2TCn%2BY8JzzOTukFRim18KDpMiJdagjrrfC4krca457k0LRLiZGSLuX8nqF5go1X0j2EgOL7VVIZYka8Xosog9Dlq3%2FE9igHp3F84AXzMqKx0yKdOntoYkXHJLQdFvWx1ps6iF42LT47C%2BPABhFn7qHbAQBTe6j%2BntqJc2OgsrHOHlZpYn3ffe8Rdr1Ew%2FFdeUrnEwMyx%2Fxy0kMJ5I1Yo7TKs41nZKgw7qQNaEj1Db8uP4wWN%2FWkASIAWrFckuFEOwvZ9X7cCYmQY9dpDTTHCiKLXqvXEN4w39WbzwY6pgGgTatjGgJ%2BTwBB6GvPEuW7puL%2FunEDjhTqxmFmPPBl72jw%2FEc2d0ZdkplRopqWb5jgd0Z5tnbFKayxheITQUjB0INBJGi8Xi%2BZIDYWYGP6XtNXRs2QRAXLGF6j3ngxOM0rS1cTzu7x2AIbdqfsXn3AeSC4hLrvpja7Jo8vg%2F3Dk8RbWJpi3NOGVIqoklDIK2KuWvX%2BTQjru3jhNQS%2FIQ8Eh7oaZXfn&X-Amz-Signature=967911a624e42c88f570694b360a97a500aed6879aeaf13b3a2ca2161ccb1757&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WVJDWU%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGagWfImSyBWiSM%2FSpZrEqKhqUkFxw%2BhzJx3S1TWNtYkAiBfpklLoMxlY%2B0NlQkta9ebDFXqZC85vtBqLeZBnUBjxSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNioMB83ja2Ze%2B5uYKtwDwkw2ZUpUNeS37LmkgD2bvCVTPCooAABfnRxQel3qOoPDfN607hcBkp9YryhHA9Omk47l%2FL0q6LVsZQI8q0%2F5NUHmgOdPw56cCuhxU8T6h1%2FsVQhaS8a9ec%2BkMOQqmXSSCNp31wzkpdf7ctixhADIs%2Fm%2FOjNchta5QJE%2FGbl2nD3HyUaoivQxT52VhpECEk%2BcWqqjPqb7VEJ3Rn1a0gmb4yLs712d0mE4Ua1YBegBj0qQknDK0UgR01BpvRmiiQ%2B80w5o5z0x0dalutBByxknFUfWrC4iBMFoYsw9Yjb0%2By8vLUcdCfp%2FCjDKJwIujO8xB%2BdbAARUPxC6ILQckBftWLoJyINjU2TCn%2BY8JzzOTukFRim18KDpMiJdagjrrfC4krca457k0LRLiZGSLuX8nqF5go1X0j2EgOL7VVIZYka8Xosog9Dlq3%2FE9igHp3F84AXzMqKx0yKdOntoYkXHJLQdFvWx1ps6iF42LT47C%2BPABhFn7qHbAQBTe6j%2BntqJc2OgsrHOHlZpYn3ffe8Rdr1Ew%2FFdeUrnEwMyx%2Fxy0kMJ5I1Yo7TKs41nZKgw7qQNaEj1Db8uP4wWN%2FWkASIAWrFckuFEOwvZ9X7cCYmQY9dpDTTHCiKLXqvXEN4w39WbzwY6pgGgTatjGgJ%2BTwBB6GvPEuW7puL%2FunEDjhTqxmFmPPBl72jw%2FEc2d0ZdkplRopqWb5jgd0Z5tnbFKayxheITQUjB0INBJGi8Xi%2BZIDYWYGP6XtNXRs2QRAXLGF6j3ngxOM0rS1cTzu7x2AIbdqfsXn3AeSC4hLrvpja7Jo8vg%2F3Dk8RbWJpi3NOGVIqoklDIK2KuWvX%2BTQjru3jhNQS%2FIQ8Eh7oaZXfn&X-Amz-Signature=be4b6c0908bf16851e108d19db5b1cce59480217fc0c0d72426ef5499b18ac00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WVJDWU%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGagWfImSyBWiSM%2FSpZrEqKhqUkFxw%2BhzJx3S1TWNtYkAiBfpklLoMxlY%2B0NlQkta9ebDFXqZC85vtBqLeZBnUBjxSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNioMB83ja2Ze%2B5uYKtwDwkw2ZUpUNeS37LmkgD2bvCVTPCooAABfnRxQel3qOoPDfN607hcBkp9YryhHA9Omk47l%2FL0q6LVsZQI8q0%2F5NUHmgOdPw56cCuhxU8T6h1%2FsVQhaS8a9ec%2BkMOQqmXSSCNp31wzkpdf7ctixhADIs%2Fm%2FOjNchta5QJE%2FGbl2nD3HyUaoivQxT52VhpECEk%2BcWqqjPqb7VEJ3Rn1a0gmb4yLs712d0mE4Ua1YBegBj0qQknDK0UgR01BpvRmiiQ%2B80w5o5z0x0dalutBByxknFUfWrC4iBMFoYsw9Yjb0%2By8vLUcdCfp%2FCjDKJwIujO8xB%2BdbAARUPxC6ILQckBftWLoJyINjU2TCn%2BY8JzzOTukFRim18KDpMiJdagjrrfC4krca457k0LRLiZGSLuX8nqF5go1X0j2EgOL7VVIZYka8Xosog9Dlq3%2FE9igHp3F84AXzMqKx0yKdOntoYkXHJLQdFvWx1ps6iF42LT47C%2BPABhFn7qHbAQBTe6j%2BntqJc2OgsrHOHlZpYn3ffe8Rdr1Ew%2FFdeUrnEwMyx%2Fxy0kMJ5I1Yo7TKs41nZKgw7qQNaEj1Db8uP4wWN%2FWkASIAWrFckuFEOwvZ9X7cCYmQY9dpDTTHCiKLXqvXEN4w39WbzwY6pgGgTatjGgJ%2BTwBB6GvPEuW7puL%2FunEDjhTqxmFmPPBl72jw%2FEc2d0ZdkplRopqWb5jgd0Z5tnbFKayxheITQUjB0INBJGi8Xi%2BZIDYWYGP6XtNXRs2QRAXLGF6j3ngxOM0rS1cTzu7x2AIbdqfsXn3AeSC4hLrvpja7Jo8vg%2F3Dk8RbWJpi3NOGVIqoklDIK2KuWvX%2BTQjru3jhNQS%2FIQ8Eh7oaZXfn&X-Amz-Signature=e0f80c108f7b02d48a559d70c7424d65a88f8fa11d36bc74e4101d7624aa1614&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WVJDWU%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGagWfImSyBWiSM%2FSpZrEqKhqUkFxw%2BhzJx3S1TWNtYkAiBfpklLoMxlY%2B0NlQkta9ebDFXqZC85vtBqLeZBnUBjxSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNioMB83ja2Ze%2B5uYKtwDwkw2ZUpUNeS37LmkgD2bvCVTPCooAABfnRxQel3qOoPDfN607hcBkp9YryhHA9Omk47l%2FL0q6LVsZQI8q0%2F5NUHmgOdPw56cCuhxU8T6h1%2FsVQhaS8a9ec%2BkMOQqmXSSCNp31wzkpdf7ctixhADIs%2Fm%2FOjNchta5QJE%2FGbl2nD3HyUaoivQxT52VhpECEk%2BcWqqjPqb7VEJ3Rn1a0gmb4yLs712d0mE4Ua1YBegBj0qQknDK0UgR01BpvRmiiQ%2B80w5o5z0x0dalutBByxknFUfWrC4iBMFoYsw9Yjb0%2By8vLUcdCfp%2FCjDKJwIujO8xB%2BdbAARUPxC6ILQckBftWLoJyINjU2TCn%2BY8JzzOTukFRim18KDpMiJdagjrrfC4krca457k0LRLiZGSLuX8nqF5go1X0j2EgOL7VVIZYka8Xosog9Dlq3%2FE9igHp3F84AXzMqKx0yKdOntoYkXHJLQdFvWx1ps6iF42LT47C%2BPABhFn7qHbAQBTe6j%2BntqJc2OgsrHOHlZpYn3ffe8Rdr1Ew%2FFdeUrnEwMyx%2Fxy0kMJ5I1Yo7TKs41nZKgw7qQNaEj1Db8uP4wWN%2FWkASIAWrFckuFEOwvZ9X7cCYmQY9dpDTTHCiKLXqvXEN4w39WbzwY6pgGgTatjGgJ%2BTwBB6GvPEuW7puL%2FunEDjhTqxmFmPPBl72jw%2FEc2d0ZdkplRopqWb5jgd0Z5tnbFKayxheITQUjB0INBJGi8Xi%2BZIDYWYGP6XtNXRs2QRAXLGF6j3ngxOM0rS1cTzu7x2AIbdqfsXn3AeSC4hLrvpja7Jo8vg%2F3Dk8RbWJpi3NOGVIqoklDIK2KuWvX%2BTQjru3jhNQS%2FIQ8Eh7oaZXfn&X-Amz-Signature=c47789c8d80d11a53dafb449aaddcee1236f79d93d79718cecdd8ceb530496bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WVJDWU%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGagWfImSyBWiSM%2FSpZrEqKhqUkFxw%2BhzJx3S1TWNtYkAiBfpklLoMxlY%2B0NlQkta9ebDFXqZC85vtBqLeZBnUBjxSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNioMB83ja2Ze%2B5uYKtwDwkw2ZUpUNeS37LmkgD2bvCVTPCooAABfnRxQel3qOoPDfN607hcBkp9YryhHA9Omk47l%2FL0q6LVsZQI8q0%2F5NUHmgOdPw56cCuhxU8T6h1%2FsVQhaS8a9ec%2BkMOQqmXSSCNp31wzkpdf7ctixhADIs%2Fm%2FOjNchta5QJE%2FGbl2nD3HyUaoivQxT52VhpECEk%2BcWqqjPqb7VEJ3Rn1a0gmb4yLs712d0mE4Ua1YBegBj0qQknDK0UgR01BpvRmiiQ%2B80w5o5z0x0dalutBByxknFUfWrC4iBMFoYsw9Yjb0%2By8vLUcdCfp%2FCjDKJwIujO8xB%2BdbAARUPxC6ILQckBftWLoJyINjU2TCn%2BY8JzzOTukFRim18KDpMiJdagjrrfC4krca457k0LRLiZGSLuX8nqF5go1X0j2EgOL7VVIZYka8Xosog9Dlq3%2FE9igHp3F84AXzMqKx0yKdOntoYkXHJLQdFvWx1ps6iF42LT47C%2BPABhFn7qHbAQBTe6j%2BntqJc2OgsrHOHlZpYn3ffe8Rdr1Ew%2FFdeUrnEwMyx%2Fxy0kMJ5I1Yo7TKs41nZKgw7qQNaEj1Db8uP4wWN%2FWkASIAWrFckuFEOwvZ9X7cCYmQY9dpDTTHCiKLXqvXEN4w39WbzwY6pgGgTatjGgJ%2BTwBB6GvPEuW7puL%2FunEDjhTqxmFmPPBl72jw%2FEc2d0ZdkplRopqWb5jgd0Z5tnbFKayxheITQUjB0INBJGi8Xi%2BZIDYWYGP6XtNXRs2QRAXLGF6j3ngxOM0rS1cTzu7x2AIbdqfsXn3AeSC4hLrvpja7Jo8vg%2F3Dk8RbWJpi3NOGVIqoklDIK2KuWvX%2BTQjru3jhNQS%2FIQ8Eh7oaZXfn&X-Amz-Signature=1671354dfae5c7650aa87beb5149498abe5e932478713845f7752854c2991d07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WVJDWU%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGagWfImSyBWiSM%2FSpZrEqKhqUkFxw%2BhzJx3S1TWNtYkAiBfpklLoMxlY%2B0NlQkta9ebDFXqZC85vtBqLeZBnUBjxSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNioMB83ja2Ze%2B5uYKtwDwkw2ZUpUNeS37LmkgD2bvCVTPCooAABfnRxQel3qOoPDfN607hcBkp9YryhHA9Omk47l%2FL0q6LVsZQI8q0%2F5NUHmgOdPw56cCuhxU8T6h1%2FsVQhaS8a9ec%2BkMOQqmXSSCNp31wzkpdf7ctixhADIs%2Fm%2FOjNchta5QJE%2FGbl2nD3HyUaoivQxT52VhpECEk%2BcWqqjPqb7VEJ3Rn1a0gmb4yLs712d0mE4Ua1YBegBj0qQknDK0UgR01BpvRmiiQ%2B80w5o5z0x0dalutBByxknFUfWrC4iBMFoYsw9Yjb0%2By8vLUcdCfp%2FCjDKJwIujO8xB%2BdbAARUPxC6ILQckBftWLoJyINjU2TCn%2BY8JzzOTukFRim18KDpMiJdagjrrfC4krca457k0LRLiZGSLuX8nqF5go1X0j2EgOL7VVIZYka8Xosog9Dlq3%2FE9igHp3F84AXzMqKx0yKdOntoYkXHJLQdFvWx1ps6iF42LT47C%2BPABhFn7qHbAQBTe6j%2BntqJc2OgsrHOHlZpYn3ffe8Rdr1Ew%2FFdeUrnEwMyx%2Fxy0kMJ5I1Yo7TKs41nZKgw7qQNaEj1Db8uP4wWN%2FWkASIAWrFckuFEOwvZ9X7cCYmQY9dpDTTHCiKLXqvXEN4w39WbzwY6pgGgTatjGgJ%2BTwBB6GvPEuW7puL%2FunEDjhTqxmFmPPBl72jw%2FEc2d0ZdkplRopqWb5jgd0Z5tnbFKayxheITQUjB0INBJGi8Xi%2BZIDYWYGP6XtNXRs2QRAXLGF6j3ngxOM0rS1cTzu7x2AIbdqfsXn3AeSC4hLrvpja7Jo8vg%2F3Dk8RbWJpi3NOGVIqoklDIK2KuWvX%2BTQjru3jhNQS%2FIQ8Eh7oaZXfn&X-Amz-Signature=f8c4252589538c1300628dc850cd03d4da9b0252321dbfaf6209d712c31888ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WVJDWU%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGagWfImSyBWiSM%2FSpZrEqKhqUkFxw%2BhzJx3S1TWNtYkAiBfpklLoMxlY%2B0NlQkta9ebDFXqZC85vtBqLeZBnUBjxSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNioMB83ja2Ze%2B5uYKtwDwkw2ZUpUNeS37LmkgD2bvCVTPCooAABfnRxQel3qOoPDfN607hcBkp9YryhHA9Omk47l%2FL0q6LVsZQI8q0%2F5NUHmgOdPw56cCuhxU8T6h1%2FsVQhaS8a9ec%2BkMOQqmXSSCNp31wzkpdf7ctixhADIs%2Fm%2FOjNchta5QJE%2FGbl2nD3HyUaoivQxT52VhpECEk%2BcWqqjPqb7VEJ3Rn1a0gmb4yLs712d0mE4Ua1YBegBj0qQknDK0UgR01BpvRmiiQ%2B80w5o5z0x0dalutBByxknFUfWrC4iBMFoYsw9Yjb0%2By8vLUcdCfp%2FCjDKJwIujO8xB%2BdbAARUPxC6ILQckBftWLoJyINjU2TCn%2BY8JzzOTukFRim18KDpMiJdagjrrfC4krca457k0LRLiZGSLuX8nqF5go1X0j2EgOL7VVIZYka8Xosog9Dlq3%2FE9igHp3F84AXzMqKx0yKdOntoYkXHJLQdFvWx1ps6iF42LT47C%2BPABhFn7qHbAQBTe6j%2BntqJc2OgsrHOHlZpYn3ffe8Rdr1Ew%2FFdeUrnEwMyx%2Fxy0kMJ5I1Yo7TKs41nZKgw7qQNaEj1Db8uP4wWN%2FWkASIAWrFckuFEOwvZ9X7cCYmQY9dpDTTHCiKLXqvXEN4w39WbzwY6pgGgTatjGgJ%2BTwBB6GvPEuW7puL%2FunEDjhTqxmFmPPBl72jw%2FEc2d0ZdkplRopqWb5jgd0Z5tnbFKayxheITQUjB0INBJGi8Xi%2BZIDYWYGP6XtNXRs2QRAXLGF6j3ngxOM0rS1cTzu7x2AIbdqfsXn3AeSC4hLrvpja7Jo8vg%2F3Dk8RbWJpi3NOGVIqoklDIK2KuWvX%2BTQjru3jhNQS%2FIQ8Eh7oaZXfn&X-Amz-Signature=dcd853b0d86c76acc37c1e6217fb79aa9445b414fd169f1801e2c9b148808e37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

