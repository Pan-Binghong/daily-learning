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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJMO2D6T%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8WuBYG0ydz5sJGZBJJIttobEYCT8Qin2Bt6%2Bzduxe0gIgL1PcROjzOuEgPisp4VJgB9z5PPmHEFJ5hUp2AdOr3bgqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBXvuN7NRjQeWH%2FwZSrcA70cLLEllWlX8VqNyHNBLZlDanQ1jP5PaVUU77AotDEH7ZSyO5iDofNFUbJq5DwXcbSkyE3A6ImOX%2BNvtYkNSjOIK%2FpBaZ8qRZVRfHEWUoPk3%2FRtmgvJk6xE9hge7bjcG5jsqxLGCEXpkT30zDawVCtUpkicWbezHe7k7xjbCF72E0DN9ObrABhQr4olPJHDeeGv5LgxWeb62EhzlknngTqF6Rnp3YYTNJ%2BVDM2RyojRGnI91TkstDkTRQpe0kyC2ewLee8ep1v2k43J9ZhTUJM%2FBM9v1hlWrGdvvpt0FCsv7beRbv5spM8fwhbsICMKFsYiGyKwhcluScMQ8L7GXjj9YLRJSB%2BXvnEkKtb86WP854ZrwCXapJmMSm%2FS4jWPCnArwtnbcmVJW%2BbLv5UPmXERqnfW1d0IbC8gRPhmTkalC6iAzW47bGwWS%2F9I9JKfIzoSmJ03y6z8D5fZjHluoOyGn3RoqTQ1xgZg1v%2BEvy7dkbEiIyWQw1B2l%2FjeKvutp5sotw9zJljLt6KxuLyCvVSXiPZihkWPr32f75EOGbzg9F5PcBDTOJJay0PvB%2FNUBVAoenlGjCPPizp3Vg%2FlkL29RTMalrAtCGjq2iwAQGE3XOICjhwfNC%2FNBg5ZMJ7ZzMoGOqUBpVE14za21YNk7muRysNjz0TiERH5ozT51EKhkKkdwyxk4h9u%2F9EcIRh8%2FiQjkaCs5lNquq%2FwUbKrSOoHaNJGAM%2F1pVP14Q4JqdFgiUBvALa9mkePxw9IifOKQ7M5Msz7hPuoBVa4rtwqp9DMCB9KUDhefMJfPIfr8v50xfVB4G2CjLCmB6%2FqUF3r0IK3F%2FEd%2B%2BzfYN26B2VZGE7uB2XqsDDch%2BnV&X-Amz-Signature=200c06a90232baca9456028ca34393766755878484b2580e50004dfc88504506&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJMO2D6T%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8WuBYG0ydz5sJGZBJJIttobEYCT8Qin2Bt6%2Bzduxe0gIgL1PcROjzOuEgPisp4VJgB9z5PPmHEFJ5hUp2AdOr3bgqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBXvuN7NRjQeWH%2FwZSrcA70cLLEllWlX8VqNyHNBLZlDanQ1jP5PaVUU77AotDEH7ZSyO5iDofNFUbJq5DwXcbSkyE3A6ImOX%2BNvtYkNSjOIK%2FpBaZ8qRZVRfHEWUoPk3%2FRtmgvJk6xE9hge7bjcG5jsqxLGCEXpkT30zDawVCtUpkicWbezHe7k7xjbCF72E0DN9ObrABhQr4olPJHDeeGv5LgxWeb62EhzlknngTqF6Rnp3YYTNJ%2BVDM2RyojRGnI91TkstDkTRQpe0kyC2ewLee8ep1v2k43J9ZhTUJM%2FBM9v1hlWrGdvvpt0FCsv7beRbv5spM8fwhbsICMKFsYiGyKwhcluScMQ8L7GXjj9YLRJSB%2BXvnEkKtb86WP854ZrwCXapJmMSm%2FS4jWPCnArwtnbcmVJW%2BbLv5UPmXERqnfW1d0IbC8gRPhmTkalC6iAzW47bGwWS%2F9I9JKfIzoSmJ03y6z8D5fZjHluoOyGn3RoqTQ1xgZg1v%2BEvy7dkbEiIyWQw1B2l%2FjeKvutp5sotw9zJljLt6KxuLyCvVSXiPZihkWPr32f75EOGbzg9F5PcBDTOJJay0PvB%2FNUBVAoenlGjCPPizp3Vg%2FlkL29RTMalrAtCGjq2iwAQGE3XOICjhwfNC%2FNBg5ZMJ7ZzMoGOqUBpVE14za21YNk7muRysNjz0TiERH5ozT51EKhkKkdwyxk4h9u%2F9EcIRh8%2FiQjkaCs5lNquq%2FwUbKrSOoHaNJGAM%2F1pVP14Q4JqdFgiUBvALa9mkePxw9IifOKQ7M5Msz7hPuoBVa4rtwqp9DMCB9KUDhefMJfPIfr8v50xfVB4G2CjLCmB6%2FqUF3r0IK3F%2FEd%2B%2BzfYN26B2VZGE7uB2XqsDDch%2BnV&X-Amz-Signature=d402b2eb5e9c0b469e7f3305ded72508389473eddf09a271f25fb8569c9396aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJMO2D6T%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8WuBYG0ydz5sJGZBJJIttobEYCT8Qin2Bt6%2Bzduxe0gIgL1PcROjzOuEgPisp4VJgB9z5PPmHEFJ5hUp2AdOr3bgqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBXvuN7NRjQeWH%2FwZSrcA70cLLEllWlX8VqNyHNBLZlDanQ1jP5PaVUU77AotDEH7ZSyO5iDofNFUbJq5DwXcbSkyE3A6ImOX%2BNvtYkNSjOIK%2FpBaZ8qRZVRfHEWUoPk3%2FRtmgvJk6xE9hge7bjcG5jsqxLGCEXpkT30zDawVCtUpkicWbezHe7k7xjbCF72E0DN9ObrABhQr4olPJHDeeGv5LgxWeb62EhzlknngTqF6Rnp3YYTNJ%2BVDM2RyojRGnI91TkstDkTRQpe0kyC2ewLee8ep1v2k43J9ZhTUJM%2FBM9v1hlWrGdvvpt0FCsv7beRbv5spM8fwhbsICMKFsYiGyKwhcluScMQ8L7GXjj9YLRJSB%2BXvnEkKtb86WP854ZrwCXapJmMSm%2FS4jWPCnArwtnbcmVJW%2BbLv5UPmXERqnfW1d0IbC8gRPhmTkalC6iAzW47bGwWS%2F9I9JKfIzoSmJ03y6z8D5fZjHluoOyGn3RoqTQ1xgZg1v%2BEvy7dkbEiIyWQw1B2l%2FjeKvutp5sotw9zJljLt6KxuLyCvVSXiPZihkWPr32f75EOGbzg9F5PcBDTOJJay0PvB%2FNUBVAoenlGjCPPizp3Vg%2FlkL29RTMalrAtCGjq2iwAQGE3XOICjhwfNC%2FNBg5ZMJ7ZzMoGOqUBpVE14za21YNk7muRysNjz0TiERH5ozT51EKhkKkdwyxk4h9u%2F9EcIRh8%2FiQjkaCs5lNquq%2FwUbKrSOoHaNJGAM%2F1pVP14Q4JqdFgiUBvALa9mkePxw9IifOKQ7M5Msz7hPuoBVa4rtwqp9DMCB9KUDhefMJfPIfr8v50xfVB4G2CjLCmB6%2FqUF3r0IK3F%2FEd%2B%2BzfYN26B2VZGE7uB2XqsDDch%2BnV&X-Amz-Signature=dcf206a31a1a7a8c41f1aa956277e2885985172ead6f7ae0e348d34dfdfc0083&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJMO2D6T%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8WuBYG0ydz5sJGZBJJIttobEYCT8Qin2Bt6%2Bzduxe0gIgL1PcROjzOuEgPisp4VJgB9z5PPmHEFJ5hUp2AdOr3bgqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBXvuN7NRjQeWH%2FwZSrcA70cLLEllWlX8VqNyHNBLZlDanQ1jP5PaVUU77AotDEH7ZSyO5iDofNFUbJq5DwXcbSkyE3A6ImOX%2BNvtYkNSjOIK%2FpBaZ8qRZVRfHEWUoPk3%2FRtmgvJk6xE9hge7bjcG5jsqxLGCEXpkT30zDawVCtUpkicWbezHe7k7xjbCF72E0DN9ObrABhQr4olPJHDeeGv5LgxWeb62EhzlknngTqF6Rnp3YYTNJ%2BVDM2RyojRGnI91TkstDkTRQpe0kyC2ewLee8ep1v2k43J9ZhTUJM%2FBM9v1hlWrGdvvpt0FCsv7beRbv5spM8fwhbsICMKFsYiGyKwhcluScMQ8L7GXjj9YLRJSB%2BXvnEkKtb86WP854ZrwCXapJmMSm%2FS4jWPCnArwtnbcmVJW%2BbLv5UPmXERqnfW1d0IbC8gRPhmTkalC6iAzW47bGwWS%2F9I9JKfIzoSmJ03y6z8D5fZjHluoOyGn3RoqTQ1xgZg1v%2BEvy7dkbEiIyWQw1B2l%2FjeKvutp5sotw9zJljLt6KxuLyCvVSXiPZihkWPr32f75EOGbzg9F5PcBDTOJJay0PvB%2FNUBVAoenlGjCPPizp3Vg%2FlkL29RTMalrAtCGjq2iwAQGE3XOICjhwfNC%2FNBg5ZMJ7ZzMoGOqUBpVE14za21YNk7muRysNjz0TiERH5ozT51EKhkKkdwyxk4h9u%2F9EcIRh8%2FiQjkaCs5lNquq%2FwUbKrSOoHaNJGAM%2F1pVP14Q4JqdFgiUBvALa9mkePxw9IifOKQ7M5Msz7hPuoBVa4rtwqp9DMCB9KUDhefMJfPIfr8v50xfVB4G2CjLCmB6%2FqUF3r0IK3F%2FEd%2B%2BzfYN26B2VZGE7uB2XqsDDch%2BnV&X-Amz-Signature=8d0822f3798d99ade49677dea1062c6f8eb758ad7bbb413d0d74cfd057af8f12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJMO2D6T%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8WuBYG0ydz5sJGZBJJIttobEYCT8Qin2Bt6%2Bzduxe0gIgL1PcROjzOuEgPisp4VJgB9z5PPmHEFJ5hUp2AdOr3bgqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBXvuN7NRjQeWH%2FwZSrcA70cLLEllWlX8VqNyHNBLZlDanQ1jP5PaVUU77AotDEH7ZSyO5iDofNFUbJq5DwXcbSkyE3A6ImOX%2BNvtYkNSjOIK%2FpBaZ8qRZVRfHEWUoPk3%2FRtmgvJk6xE9hge7bjcG5jsqxLGCEXpkT30zDawVCtUpkicWbezHe7k7xjbCF72E0DN9ObrABhQr4olPJHDeeGv5LgxWeb62EhzlknngTqF6Rnp3YYTNJ%2BVDM2RyojRGnI91TkstDkTRQpe0kyC2ewLee8ep1v2k43J9ZhTUJM%2FBM9v1hlWrGdvvpt0FCsv7beRbv5spM8fwhbsICMKFsYiGyKwhcluScMQ8L7GXjj9YLRJSB%2BXvnEkKtb86WP854ZrwCXapJmMSm%2FS4jWPCnArwtnbcmVJW%2BbLv5UPmXERqnfW1d0IbC8gRPhmTkalC6iAzW47bGwWS%2F9I9JKfIzoSmJ03y6z8D5fZjHluoOyGn3RoqTQ1xgZg1v%2BEvy7dkbEiIyWQw1B2l%2FjeKvutp5sotw9zJljLt6KxuLyCvVSXiPZihkWPr32f75EOGbzg9F5PcBDTOJJay0PvB%2FNUBVAoenlGjCPPizp3Vg%2FlkL29RTMalrAtCGjq2iwAQGE3XOICjhwfNC%2FNBg5ZMJ7ZzMoGOqUBpVE14za21YNk7muRysNjz0TiERH5ozT51EKhkKkdwyxk4h9u%2F9EcIRh8%2FiQjkaCs5lNquq%2FwUbKrSOoHaNJGAM%2F1pVP14Q4JqdFgiUBvALa9mkePxw9IifOKQ7M5Msz7hPuoBVa4rtwqp9DMCB9KUDhefMJfPIfr8v50xfVB4G2CjLCmB6%2FqUF3r0IK3F%2FEd%2B%2BzfYN26B2VZGE7uB2XqsDDch%2BnV&X-Amz-Signature=5a110fe7ced5d5657340f2887b6b9c19cd15cd7ed1d288dd32c06037b126d1bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJMO2D6T%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8WuBYG0ydz5sJGZBJJIttobEYCT8Qin2Bt6%2Bzduxe0gIgL1PcROjzOuEgPisp4VJgB9z5PPmHEFJ5hUp2AdOr3bgqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBXvuN7NRjQeWH%2FwZSrcA70cLLEllWlX8VqNyHNBLZlDanQ1jP5PaVUU77AotDEH7ZSyO5iDofNFUbJq5DwXcbSkyE3A6ImOX%2BNvtYkNSjOIK%2FpBaZ8qRZVRfHEWUoPk3%2FRtmgvJk6xE9hge7bjcG5jsqxLGCEXpkT30zDawVCtUpkicWbezHe7k7xjbCF72E0DN9ObrABhQr4olPJHDeeGv5LgxWeb62EhzlknngTqF6Rnp3YYTNJ%2BVDM2RyojRGnI91TkstDkTRQpe0kyC2ewLee8ep1v2k43J9ZhTUJM%2FBM9v1hlWrGdvvpt0FCsv7beRbv5spM8fwhbsICMKFsYiGyKwhcluScMQ8L7GXjj9YLRJSB%2BXvnEkKtb86WP854ZrwCXapJmMSm%2FS4jWPCnArwtnbcmVJW%2BbLv5UPmXERqnfW1d0IbC8gRPhmTkalC6iAzW47bGwWS%2F9I9JKfIzoSmJ03y6z8D5fZjHluoOyGn3RoqTQ1xgZg1v%2BEvy7dkbEiIyWQw1B2l%2FjeKvutp5sotw9zJljLt6KxuLyCvVSXiPZihkWPr32f75EOGbzg9F5PcBDTOJJay0PvB%2FNUBVAoenlGjCPPizp3Vg%2FlkL29RTMalrAtCGjq2iwAQGE3XOICjhwfNC%2FNBg5ZMJ7ZzMoGOqUBpVE14za21YNk7muRysNjz0TiERH5ozT51EKhkKkdwyxk4h9u%2F9EcIRh8%2FiQjkaCs5lNquq%2FwUbKrSOoHaNJGAM%2F1pVP14Q4JqdFgiUBvALa9mkePxw9IifOKQ7M5Msz7hPuoBVa4rtwqp9DMCB9KUDhefMJfPIfr8v50xfVB4G2CjLCmB6%2FqUF3r0IK3F%2FEd%2B%2BzfYN26B2VZGE7uB2XqsDDch%2BnV&X-Amz-Signature=ce546c22a0d1a58ec1d4e8656836dd747390410f6058acef0dc2985fa5fd8974&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJMO2D6T%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8WuBYG0ydz5sJGZBJJIttobEYCT8Qin2Bt6%2Bzduxe0gIgL1PcROjzOuEgPisp4VJgB9z5PPmHEFJ5hUp2AdOr3bgqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBXvuN7NRjQeWH%2FwZSrcA70cLLEllWlX8VqNyHNBLZlDanQ1jP5PaVUU77AotDEH7ZSyO5iDofNFUbJq5DwXcbSkyE3A6ImOX%2BNvtYkNSjOIK%2FpBaZ8qRZVRfHEWUoPk3%2FRtmgvJk6xE9hge7bjcG5jsqxLGCEXpkT30zDawVCtUpkicWbezHe7k7xjbCF72E0DN9ObrABhQr4olPJHDeeGv5LgxWeb62EhzlknngTqF6Rnp3YYTNJ%2BVDM2RyojRGnI91TkstDkTRQpe0kyC2ewLee8ep1v2k43J9ZhTUJM%2FBM9v1hlWrGdvvpt0FCsv7beRbv5spM8fwhbsICMKFsYiGyKwhcluScMQ8L7GXjj9YLRJSB%2BXvnEkKtb86WP854ZrwCXapJmMSm%2FS4jWPCnArwtnbcmVJW%2BbLv5UPmXERqnfW1d0IbC8gRPhmTkalC6iAzW47bGwWS%2F9I9JKfIzoSmJ03y6z8D5fZjHluoOyGn3RoqTQ1xgZg1v%2BEvy7dkbEiIyWQw1B2l%2FjeKvutp5sotw9zJljLt6KxuLyCvVSXiPZihkWPr32f75EOGbzg9F5PcBDTOJJay0PvB%2FNUBVAoenlGjCPPizp3Vg%2FlkL29RTMalrAtCGjq2iwAQGE3XOICjhwfNC%2FNBg5ZMJ7ZzMoGOqUBpVE14za21YNk7muRysNjz0TiERH5ozT51EKhkKkdwyxk4h9u%2F9EcIRh8%2FiQjkaCs5lNquq%2FwUbKrSOoHaNJGAM%2F1pVP14Q4JqdFgiUBvALa9mkePxw9IifOKQ7M5Msz7hPuoBVa4rtwqp9DMCB9KUDhefMJfPIfr8v50xfVB4G2CjLCmB6%2FqUF3r0IK3F%2FEd%2B%2BzfYN26B2VZGE7uB2XqsDDch%2BnV&X-Amz-Signature=d1f6a6726a582dd1ccf5eeabf36f5e6bc3665afa1c2e7b23a65763b4ed8cd800&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJMO2D6T%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8WuBYG0ydz5sJGZBJJIttobEYCT8Qin2Bt6%2Bzduxe0gIgL1PcROjzOuEgPisp4VJgB9z5PPmHEFJ5hUp2AdOr3bgqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBXvuN7NRjQeWH%2FwZSrcA70cLLEllWlX8VqNyHNBLZlDanQ1jP5PaVUU77AotDEH7ZSyO5iDofNFUbJq5DwXcbSkyE3A6ImOX%2BNvtYkNSjOIK%2FpBaZ8qRZVRfHEWUoPk3%2FRtmgvJk6xE9hge7bjcG5jsqxLGCEXpkT30zDawVCtUpkicWbezHe7k7xjbCF72E0DN9ObrABhQr4olPJHDeeGv5LgxWeb62EhzlknngTqF6Rnp3YYTNJ%2BVDM2RyojRGnI91TkstDkTRQpe0kyC2ewLee8ep1v2k43J9ZhTUJM%2FBM9v1hlWrGdvvpt0FCsv7beRbv5spM8fwhbsICMKFsYiGyKwhcluScMQ8L7GXjj9YLRJSB%2BXvnEkKtb86WP854ZrwCXapJmMSm%2FS4jWPCnArwtnbcmVJW%2BbLv5UPmXERqnfW1d0IbC8gRPhmTkalC6iAzW47bGwWS%2F9I9JKfIzoSmJ03y6z8D5fZjHluoOyGn3RoqTQ1xgZg1v%2BEvy7dkbEiIyWQw1B2l%2FjeKvutp5sotw9zJljLt6KxuLyCvVSXiPZihkWPr32f75EOGbzg9F5PcBDTOJJay0PvB%2FNUBVAoenlGjCPPizp3Vg%2FlkL29RTMalrAtCGjq2iwAQGE3XOICjhwfNC%2FNBg5ZMJ7ZzMoGOqUBpVE14za21YNk7muRysNjz0TiERH5ozT51EKhkKkdwyxk4h9u%2F9EcIRh8%2FiQjkaCs5lNquq%2FwUbKrSOoHaNJGAM%2F1pVP14Q4JqdFgiUBvALa9mkePxw9IifOKQ7M5Msz7hPuoBVa4rtwqp9DMCB9KUDhefMJfPIfr8v50xfVB4G2CjLCmB6%2FqUF3r0IK3F%2FEd%2B%2BzfYN26B2VZGE7uB2XqsDDch%2BnV&X-Amz-Signature=9c34a9d08dc819aa58991dc49dbc7a06f6cca2db5fecd12c89ea907150f81a3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJMO2D6T%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8WuBYG0ydz5sJGZBJJIttobEYCT8Qin2Bt6%2Bzduxe0gIgL1PcROjzOuEgPisp4VJgB9z5PPmHEFJ5hUp2AdOr3bgqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBXvuN7NRjQeWH%2FwZSrcA70cLLEllWlX8VqNyHNBLZlDanQ1jP5PaVUU77AotDEH7ZSyO5iDofNFUbJq5DwXcbSkyE3A6ImOX%2BNvtYkNSjOIK%2FpBaZ8qRZVRfHEWUoPk3%2FRtmgvJk6xE9hge7bjcG5jsqxLGCEXpkT30zDawVCtUpkicWbezHe7k7xjbCF72E0DN9ObrABhQr4olPJHDeeGv5LgxWeb62EhzlknngTqF6Rnp3YYTNJ%2BVDM2RyojRGnI91TkstDkTRQpe0kyC2ewLee8ep1v2k43J9ZhTUJM%2FBM9v1hlWrGdvvpt0FCsv7beRbv5spM8fwhbsICMKFsYiGyKwhcluScMQ8L7GXjj9YLRJSB%2BXvnEkKtb86WP854ZrwCXapJmMSm%2FS4jWPCnArwtnbcmVJW%2BbLv5UPmXERqnfW1d0IbC8gRPhmTkalC6iAzW47bGwWS%2F9I9JKfIzoSmJ03y6z8D5fZjHluoOyGn3RoqTQ1xgZg1v%2BEvy7dkbEiIyWQw1B2l%2FjeKvutp5sotw9zJljLt6KxuLyCvVSXiPZihkWPr32f75EOGbzg9F5PcBDTOJJay0PvB%2FNUBVAoenlGjCPPizp3Vg%2FlkL29RTMalrAtCGjq2iwAQGE3XOICjhwfNC%2FNBg5ZMJ7ZzMoGOqUBpVE14za21YNk7muRysNjz0TiERH5ozT51EKhkKkdwyxk4h9u%2F9EcIRh8%2FiQjkaCs5lNquq%2FwUbKrSOoHaNJGAM%2F1pVP14Q4JqdFgiUBvALa9mkePxw9IifOKQ7M5Msz7hPuoBVa4rtwqp9DMCB9KUDhefMJfPIfr8v50xfVB4G2CjLCmB6%2FqUF3r0IK3F%2FEd%2B%2BzfYN26B2VZGE7uB2XqsDDch%2BnV&X-Amz-Signature=0d19ca667e37d731e69c3caba42bff172f4a3cb429be321930e9925eec5ebf7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJMO2D6T%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8WuBYG0ydz5sJGZBJJIttobEYCT8Qin2Bt6%2Bzduxe0gIgL1PcROjzOuEgPisp4VJgB9z5PPmHEFJ5hUp2AdOr3bgqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBXvuN7NRjQeWH%2FwZSrcA70cLLEllWlX8VqNyHNBLZlDanQ1jP5PaVUU77AotDEH7ZSyO5iDofNFUbJq5DwXcbSkyE3A6ImOX%2BNvtYkNSjOIK%2FpBaZ8qRZVRfHEWUoPk3%2FRtmgvJk6xE9hge7bjcG5jsqxLGCEXpkT30zDawVCtUpkicWbezHe7k7xjbCF72E0DN9ObrABhQr4olPJHDeeGv5LgxWeb62EhzlknngTqF6Rnp3YYTNJ%2BVDM2RyojRGnI91TkstDkTRQpe0kyC2ewLee8ep1v2k43J9ZhTUJM%2FBM9v1hlWrGdvvpt0FCsv7beRbv5spM8fwhbsICMKFsYiGyKwhcluScMQ8L7GXjj9YLRJSB%2BXvnEkKtb86WP854ZrwCXapJmMSm%2FS4jWPCnArwtnbcmVJW%2BbLv5UPmXERqnfW1d0IbC8gRPhmTkalC6iAzW47bGwWS%2F9I9JKfIzoSmJ03y6z8D5fZjHluoOyGn3RoqTQ1xgZg1v%2BEvy7dkbEiIyWQw1B2l%2FjeKvutp5sotw9zJljLt6KxuLyCvVSXiPZihkWPr32f75EOGbzg9F5PcBDTOJJay0PvB%2FNUBVAoenlGjCPPizp3Vg%2FlkL29RTMalrAtCGjq2iwAQGE3XOICjhwfNC%2FNBg5ZMJ7ZzMoGOqUBpVE14za21YNk7muRysNjz0TiERH5ozT51EKhkKkdwyxk4h9u%2F9EcIRh8%2FiQjkaCs5lNquq%2FwUbKrSOoHaNJGAM%2F1pVP14Q4JqdFgiUBvALa9mkePxw9IifOKQ7M5Msz7hPuoBVa4rtwqp9DMCB9KUDhefMJfPIfr8v50xfVB4G2CjLCmB6%2FqUF3r0IK3F%2FEd%2B%2BzfYN26B2VZGE7uB2XqsDDch%2BnV&X-Amz-Signature=804a85a958cc96b4c620d49a8d78bc5a995e439487a17c01dde4b60d4ed3eb8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

