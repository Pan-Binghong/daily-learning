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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXHSD45%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQhQjTwZmbjF1H%2FGEvWznCyBqpnyXbxRGDi%2BAnj%2FpBlAiAoobRWDswd5NpI5rtJwKE06IxbXrinXX4Pvpar%2BcTF1Cr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR7ZErUCm%2BGcZe2ydKtwDgKzbBBDhZMqrfvSm6TKkTbpgE7XJ8CPTdoww%2BdyJ9sJz3hYYMm8d%2FZHEZG0Kf6Fv8sn3Su72iDoBPe5mmLzOkOfKynU5AeodelB90SNOxhX4%2BE0Mx%2F1OuiccVv4tRDQ225d%2BEvFI5gAtekftyXdrtZ2m3eDIe%2F4Ta7rsnCe74Ol3NrHfLifqKu76iEKHV%2BDcHFuKEyaybgh5rjAT9odtQDL0kvGxtqiJc5oXK4rloRyzZfxd%2FbmnlR%2BBZimJoMplVHb4HTFFwkFTUG4Pv53nfu3lBSZ10Qe0aI33WNPXHV0BVvmCdcURyBD2UjdfMgw6mO7XDUEGvnVezTv%2FDqUxHh1puX7iBESbS5zNZ%2FRdrVhD6vbn2vcrJ2Ykp3KaUIQtnyD5OW3a6oyb3OpThhnkHC1ZmEly3UYbZ5SryMhMvEqxbyOo60k4qRexoH1EXUfeBsFRC2Ke8ycb8Fvt2MLs%2BvxOOFcyXSPc8tYw7u%2BZvLoG2uB9sgoiFA5oXTfLqDgGgujveu4XrXwh5PwabSSoFbrZv4d6F4Yx7258DgbcEv5j8O4B8FwstwpMqDbw0T28VNt7NYxCtMGwzn7ZubXIfPJe3DayTlQ9ZMp2id5wRTisvcZ4IlcKnae0TSIw6JblywY6pgGPGWEABP0BxSg1qENdKoYOO7kjCK4vWkb71CYzA9JZ%2FGiUpFDmdHMKCAqCGcbF2YJPSrCqCOjPGsqu97v2Kwdoae80T948lYjTp%2BUI8iOYmHqFFHc0xixJrFqalvPw%2FWm8CD0RPv%2BP2lun7bE%2FHxs9b8tUZuPXHk%2FmXUgpIUwnXW7kflnd6xVAb9r24RFPWk2gruTa0R2CrJ4L4EyqSrLIZv8h4xSc&X-Amz-Signature=3a711427d257999cdf0b203415bd8da55d3401090427ab4124b8e16956fb1c21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXHSD45%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQhQjTwZmbjF1H%2FGEvWznCyBqpnyXbxRGDi%2BAnj%2FpBlAiAoobRWDswd5NpI5rtJwKE06IxbXrinXX4Pvpar%2BcTF1Cr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR7ZErUCm%2BGcZe2ydKtwDgKzbBBDhZMqrfvSm6TKkTbpgE7XJ8CPTdoww%2BdyJ9sJz3hYYMm8d%2FZHEZG0Kf6Fv8sn3Su72iDoBPe5mmLzOkOfKynU5AeodelB90SNOxhX4%2BE0Mx%2F1OuiccVv4tRDQ225d%2BEvFI5gAtekftyXdrtZ2m3eDIe%2F4Ta7rsnCe74Ol3NrHfLifqKu76iEKHV%2BDcHFuKEyaybgh5rjAT9odtQDL0kvGxtqiJc5oXK4rloRyzZfxd%2FbmnlR%2BBZimJoMplVHb4HTFFwkFTUG4Pv53nfu3lBSZ10Qe0aI33WNPXHV0BVvmCdcURyBD2UjdfMgw6mO7XDUEGvnVezTv%2FDqUxHh1puX7iBESbS5zNZ%2FRdrVhD6vbn2vcrJ2Ykp3KaUIQtnyD5OW3a6oyb3OpThhnkHC1ZmEly3UYbZ5SryMhMvEqxbyOo60k4qRexoH1EXUfeBsFRC2Ke8ycb8Fvt2MLs%2BvxOOFcyXSPc8tYw7u%2BZvLoG2uB9sgoiFA5oXTfLqDgGgujveu4XrXwh5PwabSSoFbrZv4d6F4Yx7258DgbcEv5j8O4B8FwstwpMqDbw0T28VNt7NYxCtMGwzn7ZubXIfPJe3DayTlQ9ZMp2id5wRTisvcZ4IlcKnae0TSIw6JblywY6pgGPGWEABP0BxSg1qENdKoYOO7kjCK4vWkb71CYzA9JZ%2FGiUpFDmdHMKCAqCGcbF2YJPSrCqCOjPGsqu97v2Kwdoae80T948lYjTp%2BUI8iOYmHqFFHc0xixJrFqalvPw%2FWm8CD0RPv%2BP2lun7bE%2FHxs9b8tUZuPXHk%2FmXUgpIUwnXW7kflnd6xVAb9r24RFPWk2gruTa0R2CrJ4L4EyqSrLIZv8h4xSc&X-Amz-Signature=a5de7d3cb91ff8ac29ff58a09dd87a736b10d13df99bec6d5b6c2abf932fa5c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXHSD45%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQhQjTwZmbjF1H%2FGEvWznCyBqpnyXbxRGDi%2BAnj%2FpBlAiAoobRWDswd5NpI5rtJwKE06IxbXrinXX4Pvpar%2BcTF1Cr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR7ZErUCm%2BGcZe2ydKtwDgKzbBBDhZMqrfvSm6TKkTbpgE7XJ8CPTdoww%2BdyJ9sJz3hYYMm8d%2FZHEZG0Kf6Fv8sn3Su72iDoBPe5mmLzOkOfKynU5AeodelB90SNOxhX4%2BE0Mx%2F1OuiccVv4tRDQ225d%2BEvFI5gAtekftyXdrtZ2m3eDIe%2F4Ta7rsnCe74Ol3NrHfLifqKu76iEKHV%2BDcHFuKEyaybgh5rjAT9odtQDL0kvGxtqiJc5oXK4rloRyzZfxd%2FbmnlR%2BBZimJoMplVHb4HTFFwkFTUG4Pv53nfu3lBSZ10Qe0aI33WNPXHV0BVvmCdcURyBD2UjdfMgw6mO7XDUEGvnVezTv%2FDqUxHh1puX7iBESbS5zNZ%2FRdrVhD6vbn2vcrJ2Ykp3KaUIQtnyD5OW3a6oyb3OpThhnkHC1ZmEly3UYbZ5SryMhMvEqxbyOo60k4qRexoH1EXUfeBsFRC2Ke8ycb8Fvt2MLs%2BvxOOFcyXSPc8tYw7u%2BZvLoG2uB9sgoiFA5oXTfLqDgGgujveu4XrXwh5PwabSSoFbrZv4d6F4Yx7258DgbcEv5j8O4B8FwstwpMqDbw0T28VNt7NYxCtMGwzn7ZubXIfPJe3DayTlQ9ZMp2id5wRTisvcZ4IlcKnae0TSIw6JblywY6pgGPGWEABP0BxSg1qENdKoYOO7kjCK4vWkb71CYzA9JZ%2FGiUpFDmdHMKCAqCGcbF2YJPSrCqCOjPGsqu97v2Kwdoae80T948lYjTp%2BUI8iOYmHqFFHc0xixJrFqalvPw%2FWm8CD0RPv%2BP2lun7bE%2FHxs9b8tUZuPXHk%2FmXUgpIUwnXW7kflnd6xVAb9r24RFPWk2gruTa0R2CrJ4L4EyqSrLIZv8h4xSc&X-Amz-Signature=364a0a86dd9c4c6fcfb7ae06c9fcf68c7003eaa110b3fcbcd1db21b4b8a8b4a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXHSD45%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQhQjTwZmbjF1H%2FGEvWznCyBqpnyXbxRGDi%2BAnj%2FpBlAiAoobRWDswd5NpI5rtJwKE06IxbXrinXX4Pvpar%2BcTF1Cr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR7ZErUCm%2BGcZe2ydKtwDgKzbBBDhZMqrfvSm6TKkTbpgE7XJ8CPTdoww%2BdyJ9sJz3hYYMm8d%2FZHEZG0Kf6Fv8sn3Su72iDoBPe5mmLzOkOfKynU5AeodelB90SNOxhX4%2BE0Mx%2F1OuiccVv4tRDQ225d%2BEvFI5gAtekftyXdrtZ2m3eDIe%2F4Ta7rsnCe74Ol3NrHfLifqKu76iEKHV%2BDcHFuKEyaybgh5rjAT9odtQDL0kvGxtqiJc5oXK4rloRyzZfxd%2FbmnlR%2BBZimJoMplVHb4HTFFwkFTUG4Pv53nfu3lBSZ10Qe0aI33WNPXHV0BVvmCdcURyBD2UjdfMgw6mO7XDUEGvnVezTv%2FDqUxHh1puX7iBESbS5zNZ%2FRdrVhD6vbn2vcrJ2Ykp3KaUIQtnyD5OW3a6oyb3OpThhnkHC1ZmEly3UYbZ5SryMhMvEqxbyOo60k4qRexoH1EXUfeBsFRC2Ke8ycb8Fvt2MLs%2BvxOOFcyXSPc8tYw7u%2BZvLoG2uB9sgoiFA5oXTfLqDgGgujveu4XrXwh5PwabSSoFbrZv4d6F4Yx7258DgbcEv5j8O4B8FwstwpMqDbw0T28VNt7NYxCtMGwzn7ZubXIfPJe3DayTlQ9ZMp2id5wRTisvcZ4IlcKnae0TSIw6JblywY6pgGPGWEABP0BxSg1qENdKoYOO7kjCK4vWkb71CYzA9JZ%2FGiUpFDmdHMKCAqCGcbF2YJPSrCqCOjPGsqu97v2Kwdoae80T948lYjTp%2BUI8iOYmHqFFHc0xixJrFqalvPw%2FWm8CD0RPv%2BP2lun7bE%2FHxs9b8tUZuPXHk%2FmXUgpIUwnXW7kflnd6xVAb9r24RFPWk2gruTa0R2CrJ4L4EyqSrLIZv8h4xSc&X-Amz-Signature=f79ec95a5728cd543ccc63a12d501d8cc81891b1065ce0a5df80c85474d8bd8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXHSD45%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQhQjTwZmbjF1H%2FGEvWznCyBqpnyXbxRGDi%2BAnj%2FpBlAiAoobRWDswd5NpI5rtJwKE06IxbXrinXX4Pvpar%2BcTF1Cr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR7ZErUCm%2BGcZe2ydKtwDgKzbBBDhZMqrfvSm6TKkTbpgE7XJ8CPTdoww%2BdyJ9sJz3hYYMm8d%2FZHEZG0Kf6Fv8sn3Su72iDoBPe5mmLzOkOfKynU5AeodelB90SNOxhX4%2BE0Mx%2F1OuiccVv4tRDQ225d%2BEvFI5gAtekftyXdrtZ2m3eDIe%2F4Ta7rsnCe74Ol3NrHfLifqKu76iEKHV%2BDcHFuKEyaybgh5rjAT9odtQDL0kvGxtqiJc5oXK4rloRyzZfxd%2FbmnlR%2BBZimJoMplVHb4HTFFwkFTUG4Pv53nfu3lBSZ10Qe0aI33WNPXHV0BVvmCdcURyBD2UjdfMgw6mO7XDUEGvnVezTv%2FDqUxHh1puX7iBESbS5zNZ%2FRdrVhD6vbn2vcrJ2Ykp3KaUIQtnyD5OW3a6oyb3OpThhnkHC1ZmEly3UYbZ5SryMhMvEqxbyOo60k4qRexoH1EXUfeBsFRC2Ke8ycb8Fvt2MLs%2BvxOOFcyXSPc8tYw7u%2BZvLoG2uB9sgoiFA5oXTfLqDgGgujveu4XrXwh5PwabSSoFbrZv4d6F4Yx7258DgbcEv5j8O4B8FwstwpMqDbw0T28VNt7NYxCtMGwzn7ZubXIfPJe3DayTlQ9ZMp2id5wRTisvcZ4IlcKnae0TSIw6JblywY6pgGPGWEABP0BxSg1qENdKoYOO7kjCK4vWkb71CYzA9JZ%2FGiUpFDmdHMKCAqCGcbF2YJPSrCqCOjPGsqu97v2Kwdoae80T948lYjTp%2BUI8iOYmHqFFHc0xixJrFqalvPw%2FWm8CD0RPv%2BP2lun7bE%2FHxs9b8tUZuPXHk%2FmXUgpIUwnXW7kflnd6xVAb9r24RFPWk2gruTa0R2CrJ4L4EyqSrLIZv8h4xSc&X-Amz-Signature=d874b7a690ee18da18e6c0ff9f6dce6527bea046915480f6918d0de2985ed270&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXHSD45%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQhQjTwZmbjF1H%2FGEvWznCyBqpnyXbxRGDi%2BAnj%2FpBlAiAoobRWDswd5NpI5rtJwKE06IxbXrinXX4Pvpar%2BcTF1Cr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR7ZErUCm%2BGcZe2ydKtwDgKzbBBDhZMqrfvSm6TKkTbpgE7XJ8CPTdoww%2BdyJ9sJz3hYYMm8d%2FZHEZG0Kf6Fv8sn3Su72iDoBPe5mmLzOkOfKynU5AeodelB90SNOxhX4%2BE0Mx%2F1OuiccVv4tRDQ225d%2BEvFI5gAtekftyXdrtZ2m3eDIe%2F4Ta7rsnCe74Ol3NrHfLifqKu76iEKHV%2BDcHFuKEyaybgh5rjAT9odtQDL0kvGxtqiJc5oXK4rloRyzZfxd%2FbmnlR%2BBZimJoMplVHb4HTFFwkFTUG4Pv53nfu3lBSZ10Qe0aI33WNPXHV0BVvmCdcURyBD2UjdfMgw6mO7XDUEGvnVezTv%2FDqUxHh1puX7iBESbS5zNZ%2FRdrVhD6vbn2vcrJ2Ykp3KaUIQtnyD5OW3a6oyb3OpThhnkHC1ZmEly3UYbZ5SryMhMvEqxbyOo60k4qRexoH1EXUfeBsFRC2Ke8ycb8Fvt2MLs%2BvxOOFcyXSPc8tYw7u%2BZvLoG2uB9sgoiFA5oXTfLqDgGgujveu4XrXwh5PwabSSoFbrZv4d6F4Yx7258DgbcEv5j8O4B8FwstwpMqDbw0T28VNt7NYxCtMGwzn7ZubXIfPJe3DayTlQ9ZMp2id5wRTisvcZ4IlcKnae0TSIw6JblywY6pgGPGWEABP0BxSg1qENdKoYOO7kjCK4vWkb71CYzA9JZ%2FGiUpFDmdHMKCAqCGcbF2YJPSrCqCOjPGsqu97v2Kwdoae80T948lYjTp%2BUI8iOYmHqFFHc0xixJrFqalvPw%2FWm8CD0RPv%2BP2lun7bE%2FHxs9b8tUZuPXHk%2FmXUgpIUwnXW7kflnd6xVAb9r24RFPWk2gruTa0R2CrJ4L4EyqSrLIZv8h4xSc&X-Amz-Signature=4b5e7dcad8606646a6269b03d49ab102277c2a84b3cdb6f1c0e78c5f4f187049&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXHSD45%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQhQjTwZmbjF1H%2FGEvWznCyBqpnyXbxRGDi%2BAnj%2FpBlAiAoobRWDswd5NpI5rtJwKE06IxbXrinXX4Pvpar%2BcTF1Cr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR7ZErUCm%2BGcZe2ydKtwDgKzbBBDhZMqrfvSm6TKkTbpgE7XJ8CPTdoww%2BdyJ9sJz3hYYMm8d%2FZHEZG0Kf6Fv8sn3Su72iDoBPe5mmLzOkOfKynU5AeodelB90SNOxhX4%2BE0Mx%2F1OuiccVv4tRDQ225d%2BEvFI5gAtekftyXdrtZ2m3eDIe%2F4Ta7rsnCe74Ol3NrHfLifqKu76iEKHV%2BDcHFuKEyaybgh5rjAT9odtQDL0kvGxtqiJc5oXK4rloRyzZfxd%2FbmnlR%2BBZimJoMplVHb4HTFFwkFTUG4Pv53nfu3lBSZ10Qe0aI33WNPXHV0BVvmCdcURyBD2UjdfMgw6mO7XDUEGvnVezTv%2FDqUxHh1puX7iBESbS5zNZ%2FRdrVhD6vbn2vcrJ2Ykp3KaUIQtnyD5OW3a6oyb3OpThhnkHC1ZmEly3UYbZ5SryMhMvEqxbyOo60k4qRexoH1EXUfeBsFRC2Ke8ycb8Fvt2MLs%2BvxOOFcyXSPc8tYw7u%2BZvLoG2uB9sgoiFA5oXTfLqDgGgujveu4XrXwh5PwabSSoFbrZv4d6F4Yx7258DgbcEv5j8O4B8FwstwpMqDbw0T28VNt7NYxCtMGwzn7ZubXIfPJe3DayTlQ9ZMp2id5wRTisvcZ4IlcKnae0TSIw6JblywY6pgGPGWEABP0BxSg1qENdKoYOO7kjCK4vWkb71CYzA9JZ%2FGiUpFDmdHMKCAqCGcbF2YJPSrCqCOjPGsqu97v2Kwdoae80T948lYjTp%2BUI8iOYmHqFFHc0xixJrFqalvPw%2FWm8CD0RPv%2BP2lun7bE%2FHxs9b8tUZuPXHk%2FmXUgpIUwnXW7kflnd6xVAb9r24RFPWk2gruTa0R2CrJ4L4EyqSrLIZv8h4xSc&X-Amz-Signature=b8961bf980f8c4a9ef624b4b45f5d3388f1b3396caf5fa362369597c72e659a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXHSD45%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQhQjTwZmbjF1H%2FGEvWznCyBqpnyXbxRGDi%2BAnj%2FpBlAiAoobRWDswd5NpI5rtJwKE06IxbXrinXX4Pvpar%2BcTF1Cr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR7ZErUCm%2BGcZe2ydKtwDgKzbBBDhZMqrfvSm6TKkTbpgE7XJ8CPTdoww%2BdyJ9sJz3hYYMm8d%2FZHEZG0Kf6Fv8sn3Su72iDoBPe5mmLzOkOfKynU5AeodelB90SNOxhX4%2BE0Mx%2F1OuiccVv4tRDQ225d%2BEvFI5gAtekftyXdrtZ2m3eDIe%2F4Ta7rsnCe74Ol3NrHfLifqKu76iEKHV%2BDcHFuKEyaybgh5rjAT9odtQDL0kvGxtqiJc5oXK4rloRyzZfxd%2FbmnlR%2BBZimJoMplVHb4HTFFwkFTUG4Pv53nfu3lBSZ10Qe0aI33WNPXHV0BVvmCdcURyBD2UjdfMgw6mO7XDUEGvnVezTv%2FDqUxHh1puX7iBESbS5zNZ%2FRdrVhD6vbn2vcrJ2Ykp3KaUIQtnyD5OW3a6oyb3OpThhnkHC1ZmEly3UYbZ5SryMhMvEqxbyOo60k4qRexoH1EXUfeBsFRC2Ke8ycb8Fvt2MLs%2BvxOOFcyXSPc8tYw7u%2BZvLoG2uB9sgoiFA5oXTfLqDgGgujveu4XrXwh5PwabSSoFbrZv4d6F4Yx7258DgbcEv5j8O4B8FwstwpMqDbw0T28VNt7NYxCtMGwzn7ZubXIfPJe3DayTlQ9ZMp2id5wRTisvcZ4IlcKnae0TSIw6JblywY6pgGPGWEABP0BxSg1qENdKoYOO7kjCK4vWkb71CYzA9JZ%2FGiUpFDmdHMKCAqCGcbF2YJPSrCqCOjPGsqu97v2Kwdoae80T948lYjTp%2BUI8iOYmHqFFHc0xixJrFqalvPw%2FWm8CD0RPv%2BP2lun7bE%2FHxs9b8tUZuPXHk%2FmXUgpIUwnXW7kflnd6xVAb9r24RFPWk2gruTa0R2CrJ4L4EyqSrLIZv8h4xSc&X-Amz-Signature=fcc0f76d08d3ec7a003b03b7589da3d609e9bb5970a41284684bf6834b0afcda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXHSD45%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQhQjTwZmbjF1H%2FGEvWznCyBqpnyXbxRGDi%2BAnj%2FpBlAiAoobRWDswd5NpI5rtJwKE06IxbXrinXX4Pvpar%2BcTF1Cr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR7ZErUCm%2BGcZe2ydKtwDgKzbBBDhZMqrfvSm6TKkTbpgE7XJ8CPTdoww%2BdyJ9sJz3hYYMm8d%2FZHEZG0Kf6Fv8sn3Su72iDoBPe5mmLzOkOfKynU5AeodelB90SNOxhX4%2BE0Mx%2F1OuiccVv4tRDQ225d%2BEvFI5gAtekftyXdrtZ2m3eDIe%2F4Ta7rsnCe74Ol3NrHfLifqKu76iEKHV%2BDcHFuKEyaybgh5rjAT9odtQDL0kvGxtqiJc5oXK4rloRyzZfxd%2FbmnlR%2BBZimJoMplVHb4HTFFwkFTUG4Pv53nfu3lBSZ10Qe0aI33WNPXHV0BVvmCdcURyBD2UjdfMgw6mO7XDUEGvnVezTv%2FDqUxHh1puX7iBESbS5zNZ%2FRdrVhD6vbn2vcrJ2Ykp3KaUIQtnyD5OW3a6oyb3OpThhnkHC1ZmEly3UYbZ5SryMhMvEqxbyOo60k4qRexoH1EXUfeBsFRC2Ke8ycb8Fvt2MLs%2BvxOOFcyXSPc8tYw7u%2BZvLoG2uB9sgoiFA5oXTfLqDgGgujveu4XrXwh5PwabSSoFbrZv4d6F4Yx7258DgbcEv5j8O4B8FwstwpMqDbw0T28VNt7NYxCtMGwzn7ZubXIfPJe3DayTlQ9ZMp2id5wRTisvcZ4IlcKnae0TSIw6JblywY6pgGPGWEABP0BxSg1qENdKoYOO7kjCK4vWkb71CYzA9JZ%2FGiUpFDmdHMKCAqCGcbF2YJPSrCqCOjPGsqu97v2Kwdoae80T948lYjTp%2BUI8iOYmHqFFHc0xixJrFqalvPw%2FWm8CD0RPv%2BP2lun7bE%2FHxs9b8tUZuPXHk%2FmXUgpIUwnXW7kflnd6xVAb9r24RFPWk2gruTa0R2CrJ4L4EyqSrLIZv8h4xSc&X-Amz-Signature=26bc5c547409c239d1a74d0f08c2b9b2daf06a8dd9e164f1badf5c1858d83535&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQXHSD45%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQhQjTwZmbjF1H%2FGEvWznCyBqpnyXbxRGDi%2BAnj%2FpBlAiAoobRWDswd5NpI5rtJwKE06IxbXrinXX4Pvpar%2BcTF1Cr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMR7ZErUCm%2BGcZe2ydKtwDgKzbBBDhZMqrfvSm6TKkTbpgE7XJ8CPTdoww%2BdyJ9sJz3hYYMm8d%2FZHEZG0Kf6Fv8sn3Su72iDoBPe5mmLzOkOfKynU5AeodelB90SNOxhX4%2BE0Mx%2F1OuiccVv4tRDQ225d%2BEvFI5gAtekftyXdrtZ2m3eDIe%2F4Ta7rsnCe74Ol3NrHfLifqKu76iEKHV%2BDcHFuKEyaybgh5rjAT9odtQDL0kvGxtqiJc5oXK4rloRyzZfxd%2FbmnlR%2BBZimJoMplVHb4HTFFwkFTUG4Pv53nfu3lBSZ10Qe0aI33WNPXHV0BVvmCdcURyBD2UjdfMgw6mO7XDUEGvnVezTv%2FDqUxHh1puX7iBESbS5zNZ%2FRdrVhD6vbn2vcrJ2Ykp3KaUIQtnyD5OW3a6oyb3OpThhnkHC1ZmEly3UYbZ5SryMhMvEqxbyOo60k4qRexoH1EXUfeBsFRC2Ke8ycb8Fvt2MLs%2BvxOOFcyXSPc8tYw7u%2BZvLoG2uB9sgoiFA5oXTfLqDgGgujveu4XrXwh5PwabSSoFbrZv4d6F4Yx7258DgbcEv5j8O4B8FwstwpMqDbw0T28VNt7NYxCtMGwzn7ZubXIfPJe3DayTlQ9ZMp2id5wRTisvcZ4IlcKnae0TSIw6JblywY6pgGPGWEABP0BxSg1qENdKoYOO7kjCK4vWkb71CYzA9JZ%2FGiUpFDmdHMKCAqCGcbF2YJPSrCqCOjPGsqu97v2Kwdoae80T948lYjTp%2BUI8iOYmHqFFHc0xixJrFqalvPw%2FWm8CD0RPv%2BP2lun7bE%2FHxs9b8tUZuPXHk%2FmXUgpIUwnXW7kflnd6xVAb9r24RFPWk2gruTa0R2CrJ4L4EyqSrLIZv8h4xSc&X-Amz-Signature=8005eefcd8ebc50dd25aa68dbd930ffe9c36cc04e681000b8538db62118c4605&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

