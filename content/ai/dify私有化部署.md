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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTILPN26%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRHvhBuQAs%2BjH6F%2FhFcASUnJSRnDdS%2F4%2FXn99cgQNMzAIhAOnUzTC%2Bfu2y7UWtrIL4M27NDYN3Ooo7iVJZdEZ7qQvjKv8DCFQQABoMNjM3NDIzMTgzODA1Igz9iSW7Wn7G8yXTiGoq3AOdbHmFRN6xZtwKnS9HcMUDCmbMzvo6IHg%2FLfEcRCXEJc5eYOf73aOQy2OJ8qZoHhnS5anNN4rdeUReWj5YSUcwqy6wwqjAGNd%2B7MOh%2FVfE%2BIvogxqXdZDRnE73heuMeUG3tv2bD0SX3CSOX60Q0qoMIOC5NKTEj%2FOdHjtXo4uB85KZ9MlQMDQ%2FuFgvdpBkwxSFsP7jgk%2FkEV%2BxCnp9zwJjBGcNKpem%2Bp2MKJ1mg5f92IDmFf6AWjPBdPu8CbZP7hq99kQr8wqhLPM3l%2Bc14EnIzLypMqJbjjAKc%2FoXKXSkc5lrP%2F5wQi4YvTftTinJjbUWIFq3e5iz35CLT%2BTlDu12rXX4YIcPxHKEZ2UaNCyo5CMWaDpUUooTvfM3ffVviMQW7PKBlpgoFe80gzSNAENFk3Fr9O38oM069xRXUTzMuJFOkKramwN8CuWeO9NqnkS8k2WeN0NIARoXKn7iHoHlE5hEIusJFpyHLOp2pxUv7aM0%2FMlXB4QR5xNhUaMf3gE5jO8A6PY6xlddxlaSNNn4eNE3DtLKReFBi2hhi5b0%2F8UwZG4es33Ef7M3cXCbPr%2Bjt6sIspoTXPpQK39UJqqiuUJv0I%2FT3ou5DHilU61DhFUF0kSTN8wnyy8pfzCAwcPNBjqkAXhONneSHoCL212q0HD0hy6LY5YPDSbrrbb%2FHiYpuuNYjRaQF3Ly0RqaP80FAJcngOgqCxQj4%2BiaOTQ2RHKJ1kGRS4zIqUU9UjWDGN8g96vKCinuojlVpsKYwtGYdG4Bh5hQAaEfAxwGwO2AxGpb4YUfQcTc8Ifv60R%2FZ1hI%2FeZilMt%2BRVUZFiM1RQ0IAVD%2F0%2BZ2vj0yyOk0jDbsrWMZVhJa0hAs&X-Amz-Signature=84f856a66c861733f74cc554aab9006b50f1459499c61e6da671c093dda8f631&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTILPN26%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRHvhBuQAs%2BjH6F%2FhFcASUnJSRnDdS%2F4%2FXn99cgQNMzAIhAOnUzTC%2Bfu2y7UWtrIL4M27NDYN3Ooo7iVJZdEZ7qQvjKv8DCFQQABoMNjM3NDIzMTgzODA1Igz9iSW7Wn7G8yXTiGoq3AOdbHmFRN6xZtwKnS9HcMUDCmbMzvo6IHg%2FLfEcRCXEJc5eYOf73aOQy2OJ8qZoHhnS5anNN4rdeUReWj5YSUcwqy6wwqjAGNd%2B7MOh%2FVfE%2BIvogxqXdZDRnE73heuMeUG3tv2bD0SX3CSOX60Q0qoMIOC5NKTEj%2FOdHjtXo4uB85KZ9MlQMDQ%2FuFgvdpBkwxSFsP7jgk%2FkEV%2BxCnp9zwJjBGcNKpem%2Bp2MKJ1mg5f92IDmFf6AWjPBdPu8CbZP7hq99kQr8wqhLPM3l%2Bc14EnIzLypMqJbjjAKc%2FoXKXSkc5lrP%2F5wQi4YvTftTinJjbUWIFq3e5iz35CLT%2BTlDu12rXX4YIcPxHKEZ2UaNCyo5CMWaDpUUooTvfM3ffVviMQW7PKBlpgoFe80gzSNAENFk3Fr9O38oM069xRXUTzMuJFOkKramwN8CuWeO9NqnkS8k2WeN0NIARoXKn7iHoHlE5hEIusJFpyHLOp2pxUv7aM0%2FMlXB4QR5xNhUaMf3gE5jO8A6PY6xlddxlaSNNn4eNE3DtLKReFBi2hhi5b0%2F8UwZG4es33Ef7M3cXCbPr%2Bjt6sIspoTXPpQK39UJqqiuUJv0I%2FT3ou5DHilU61DhFUF0kSTN8wnyy8pfzCAwcPNBjqkAXhONneSHoCL212q0HD0hy6LY5YPDSbrrbb%2FHiYpuuNYjRaQF3Ly0RqaP80FAJcngOgqCxQj4%2BiaOTQ2RHKJ1kGRS4zIqUU9UjWDGN8g96vKCinuojlVpsKYwtGYdG4Bh5hQAaEfAxwGwO2AxGpb4YUfQcTc8Ifv60R%2FZ1hI%2FeZilMt%2BRVUZFiM1RQ0IAVD%2F0%2BZ2vj0yyOk0jDbsrWMZVhJa0hAs&X-Amz-Signature=4148f447c69f3b9f436a10c296096aeb19fd8e69e41b9d8f13676b159347401c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTILPN26%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRHvhBuQAs%2BjH6F%2FhFcASUnJSRnDdS%2F4%2FXn99cgQNMzAIhAOnUzTC%2Bfu2y7UWtrIL4M27NDYN3Ooo7iVJZdEZ7qQvjKv8DCFQQABoMNjM3NDIzMTgzODA1Igz9iSW7Wn7G8yXTiGoq3AOdbHmFRN6xZtwKnS9HcMUDCmbMzvo6IHg%2FLfEcRCXEJc5eYOf73aOQy2OJ8qZoHhnS5anNN4rdeUReWj5YSUcwqy6wwqjAGNd%2B7MOh%2FVfE%2BIvogxqXdZDRnE73heuMeUG3tv2bD0SX3CSOX60Q0qoMIOC5NKTEj%2FOdHjtXo4uB85KZ9MlQMDQ%2FuFgvdpBkwxSFsP7jgk%2FkEV%2BxCnp9zwJjBGcNKpem%2Bp2MKJ1mg5f92IDmFf6AWjPBdPu8CbZP7hq99kQr8wqhLPM3l%2Bc14EnIzLypMqJbjjAKc%2FoXKXSkc5lrP%2F5wQi4YvTftTinJjbUWIFq3e5iz35CLT%2BTlDu12rXX4YIcPxHKEZ2UaNCyo5CMWaDpUUooTvfM3ffVviMQW7PKBlpgoFe80gzSNAENFk3Fr9O38oM069xRXUTzMuJFOkKramwN8CuWeO9NqnkS8k2WeN0NIARoXKn7iHoHlE5hEIusJFpyHLOp2pxUv7aM0%2FMlXB4QR5xNhUaMf3gE5jO8A6PY6xlddxlaSNNn4eNE3DtLKReFBi2hhi5b0%2F8UwZG4es33Ef7M3cXCbPr%2Bjt6sIspoTXPpQK39UJqqiuUJv0I%2FT3ou5DHilU61DhFUF0kSTN8wnyy8pfzCAwcPNBjqkAXhONneSHoCL212q0HD0hy6LY5YPDSbrrbb%2FHiYpuuNYjRaQF3Ly0RqaP80FAJcngOgqCxQj4%2BiaOTQ2RHKJ1kGRS4zIqUU9UjWDGN8g96vKCinuojlVpsKYwtGYdG4Bh5hQAaEfAxwGwO2AxGpb4YUfQcTc8Ifv60R%2FZ1hI%2FeZilMt%2BRVUZFiM1RQ0IAVD%2F0%2BZ2vj0yyOk0jDbsrWMZVhJa0hAs&X-Amz-Signature=95ab75f9e47250800869fe1d70c9caed925a9b7d4274d82b3cb3e357b7c61024&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTILPN26%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRHvhBuQAs%2BjH6F%2FhFcASUnJSRnDdS%2F4%2FXn99cgQNMzAIhAOnUzTC%2Bfu2y7UWtrIL4M27NDYN3Ooo7iVJZdEZ7qQvjKv8DCFQQABoMNjM3NDIzMTgzODA1Igz9iSW7Wn7G8yXTiGoq3AOdbHmFRN6xZtwKnS9HcMUDCmbMzvo6IHg%2FLfEcRCXEJc5eYOf73aOQy2OJ8qZoHhnS5anNN4rdeUReWj5YSUcwqy6wwqjAGNd%2B7MOh%2FVfE%2BIvogxqXdZDRnE73heuMeUG3tv2bD0SX3CSOX60Q0qoMIOC5NKTEj%2FOdHjtXo4uB85KZ9MlQMDQ%2FuFgvdpBkwxSFsP7jgk%2FkEV%2BxCnp9zwJjBGcNKpem%2Bp2MKJ1mg5f92IDmFf6AWjPBdPu8CbZP7hq99kQr8wqhLPM3l%2Bc14EnIzLypMqJbjjAKc%2FoXKXSkc5lrP%2F5wQi4YvTftTinJjbUWIFq3e5iz35CLT%2BTlDu12rXX4YIcPxHKEZ2UaNCyo5CMWaDpUUooTvfM3ffVviMQW7PKBlpgoFe80gzSNAENFk3Fr9O38oM069xRXUTzMuJFOkKramwN8CuWeO9NqnkS8k2WeN0NIARoXKn7iHoHlE5hEIusJFpyHLOp2pxUv7aM0%2FMlXB4QR5xNhUaMf3gE5jO8A6PY6xlddxlaSNNn4eNE3DtLKReFBi2hhi5b0%2F8UwZG4es33Ef7M3cXCbPr%2Bjt6sIspoTXPpQK39UJqqiuUJv0I%2FT3ou5DHilU61DhFUF0kSTN8wnyy8pfzCAwcPNBjqkAXhONneSHoCL212q0HD0hy6LY5YPDSbrrbb%2FHiYpuuNYjRaQF3Ly0RqaP80FAJcngOgqCxQj4%2BiaOTQ2RHKJ1kGRS4zIqUU9UjWDGN8g96vKCinuojlVpsKYwtGYdG4Bh5hQAaEfAxwGwO2AxGpb4YUfQcTc8Ifv60R%2FZ1hI%2FeZilMt%2BRVUZFiM1RQ0IAVD%2F0%2BZ2vj0yyOk0jDbsrWMZVhJa0hAs&X-Amz-Signature=3cbeccaff3d2caa2127d47925b0e96cc1a9d8a7819f3b3a8fc0e7adef227df91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTILPN26%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRHvhBuQAs%2BjH6F%2FhFcASUnJSRnDdS%2F4%2FXn99cgQNMzAIhAOnUzTC%2Bfu2y7UWtrIL4M27NDYN3Ooo7iVJZdEZ7qQvjKv8DCFQQABoMNjM3NDIzMTgzODA1Igz9iSW7Wn7G8yXTiGoq3AOdbHmFRN6xZtwKnS9HcMUDCmbMzvo6IHg%2FLfEcRCXEJc5eYOf73aOQy2OJ8qZoHhnS5anNN4rdeUReWj5YSUcwqy6wwqjAGNd%2B7MOh%2FVfE%2BIvogxqXdZDRnE73heuMeUG3tv2bD0SX3CSOX60Q0qoMIOC5NKTEj%2FOdHjtXo4uB85KZ9MlQMDQ%2FuFgvdpBkwxSFsP7jgk%2FkEV%2BxCnp9zwJjBGcNKpem%2Bp2MKJ1mg5f92IDmFf6AWjPBdPu8CbZP7hq99kQr8wqhLPM3l%2Bc14EnIzLypMqJbjjAKc%2FoXKXSkc5lrP%2F5wQi4YvTftTinJjbUWIFq3e5iz35CLT%2BTlDu12rXX4YIcPxHKEZ2UaNCyo5CMWaDpUUooTvfM3ffVviMQW7PKBlpgoFe80gzSNAENFk3Fr9O38oM069xRXUTzMuJFOkKramwN8CuWeO9NqnkS8k2WeN0NIARoXKn7iHoHlE5hEIusJFpyHLOp2pxUv7aM0%2FMlXB4QR5xNhUaMf3gE5jO8A6PY6xlddxlaSNNn4eNE3DtLKReFBi2hhi5b0%2F8UwZG4es33Ef7M3cXCbPr%2Bjt6sIspoTXPpQK39UJqqiuUJv0I%2FT3ou5DHilU61DhFUF0kSTN8wnyy8pfzCAwcPNBjqkAXhONneSHoCL212q0HD0hy6LY5YPDSbrrbb%2FHiYpuuNYjRaQF3Ly0RqaP80FAJcngOgqCxQj4%2BiaOTQ2RHKJ1kGRS4zIqUU9UjWDGN8g96vKCinuojlVpsKYwtGYdG4Bh5hQAaEfAxwGwO2AxGpb4YUfQcTc8Ifv60R%2FZ1hI%2FeZilMt%2BRVUZFiM1RQ0IAVD%2F0%2BZ2vj0yyOk0jDbsrWMZVhJa0hAs&X-Amz-Signature=e59130f645da0314ab20613710a53391c26839b56dbf883a03b671d2ec1235f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTILPN26%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRHvhBuQAs%2BjH6F%2FhFcASUnJSRnDdS%2F4%2FXn99cgQNMzAIhAOnUzTC%2Bfu2y7UWtrIL4M27NDYN3Ooo7iVJZdEZ7qQvjKv8DCFQQABoMNjM3NDIzMTgzODA1Igz9iSW7Wn7G8yXTiGoq3AOdbHmFRN6xZtwKnS9HcMUDCmbMzvo6IHg%2FLfEcRCXEJc5eYOf73aOQy2OJ8qZoHhnS5anNN4rdeUReWj5YSUcwqy6wwqjAGNd%2B7MOh%2FVfE%2BIvogxqXdZDRnE73heuMeUG3tv2bD0SX3CSOX60Q0qoMIOC5NKTEj%2FOdHjtXo4uB85KZ9MlQMDQ%2FuFgvdpBkwxSFsP7jgk%2FkEV%2BxCnp9zwJjBGcNKpem%2Bp2MKJ1mg5f92IDmFf6AWjPBdPu8CbZP7hq99kQr8wqhLPM3l%2Bc14EnIzLypMqJbjjAKc%2FoXKXSkc5lrP%2F5wQi4YvTftTinJjbUWIFq3e5iz35CLT%2BTlDu12rXX4YIcPxHKEZ2UaNCyo5CMWaDpUUooTvfM3ffVviMQW7PKBlpgoFe80gzSNAENFk3Fr9O38oM069xRXUTzMuJFOkKramwN8CuWeO9NqnkS8k2WeN0NIARoXKn7iHoHlE5hEIusJFpyHLOp2pxUv7aM0%2FMlXB4QR5xNhUaMf3gE5jO8A6PY6xlddxlaSNNn4eNE3DtLKReFBi2hhi5b0%2F8UwZG4es33Ef7M3cXCbPr%2Bjt6sIspoTXPpQK39UJqqiuUJv0I%2FT3ou5DHilU61DhFUF0kSTN8wnyy8pfzCAwcPNBjqkAXhONneSHoCL212q0HD0hy6LY5YPDSbrrbb%2FHiYpuuNYjRaQF3Ly0RqaP80FAJcngOgqCxQj4%2BiaOTQ2RHKJ1kGRS4zIqUU9UjWDGN8g96vKCinuojlVpsKYwtGYdG4Bh5hQAaEfAxwGwO2AxGpb4YUfQcTc8Ifv60R%2FZ1hI%2FeZilMt%2BRVUZFiM1RQ0IAVD%2F0%2BZ2vj0yyOk0jDbsrWMZVhJa0hAs&X-Amz-Signature=316f9be7b31c74a22451b91bd18bcb790f487220f1994523576b9419680c5f1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTILPN26%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRHvhBuQAs%2BjH6F%2FhFcASUnJSRnDdS%2F4%2FXn99cgQNMzAIhAOnUzTC%2Bfu2y7UWtrIL4M27NDYN3Ooo7iVJZdEZ7qQvjKv8DCFQQABoMNjM3NDIzMTgzODA1Igz9iSW7Wn7G8yXTiGoq3AOdbHmFRN6xZtwKnS9HcMUDCmbMzvo6IHg%2FLfEcRCXEJc5eYOf73aOQy2OJ8qZoHhnS5anNN4rdeUReWj5YSUcwqy6wwqjAGNd%2B7MOh%2FVfE%2BIvogxqXdZDRnE73heuMeUG3tv2bD0SX3CSOX60Q0qoMIOC5NKTEj%2FOdHjtXo4uB85KZ9MlQMDQ%2FuFgvdpBkwxSFsP7jgk%2FkEV%2BxCnp9zwJjBGcNKpem%2Bp2MKJ1mg5f92IDmFf6AWjPBdPu8CbZP7hq99kQr8wqhLPM3l%2Bc14EnIzLypMqJbjjAKc%2FoXKXSkc5lrP%2F5wQi4YvTftTinJjbUWIFq3e5iz35CLT%2BTlDu12rXX4YIcPxHKEZ2UaNCyo5CMWaDpUUooTvfM3ffVviMQW7PKBlpgoFe80gzSNAENFk3Fr9O38oM069xRXUTzMuJFOkKramwN8CuWeO9NqnkS8k2WeN0NIARoXKn7iHoHlE5hEIusJFpyHLOp2pxUv7aM0%2FMlXB4QR5xNhUaMf3gE5jO8A6PY6xlddxlaSNNn4eNE3DtLKReFBi2hhi5b0%2F8UwZG4es33Ef7M3cXCbPr%2Bjt6sIspoTXPpQK39UJqqiuUJv0I%2FT3ou5DHilU61DhFUF0kSTN8wnyy8pfzCAwcPNBjqkAXhONneSHoCL212q0HD0hy6LY5YPDSbrrbb%2FHiYpuuNYjRaQF3Ly0RqaP80FAJcngOgqCxQj4%2BiaOTQ2RHKJ1kGRS4zIqUU9UjWDGN8g96vKCinuojlVpsKYwtGYdG4Bh5hQAaEfAxwGwO2AxGpb4YUfQcTc8Ifv60R%2FZ1hI%2FeZilMt%2BRVUZFiM1RQ0IAVD%2F0%2BZ2vj0yyOk0jDbsrWMZVhJa0hAs&X-Amz-Signature=2b8648aa704233dfcf1a5a34b2457baf3ec2d6e90d5deffa1d14543dfd2a8c72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTILPN26%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRHvhBuQAs%2BjH6F%2FhFcASUnJSRnDdS%2F4%2FXn99cgQNMzAIhAOnUzTC%2Bfu2y7UWtrIL4M27NDYN3Ooo7iVJZdEZ7qQvjKv8DCFQQABoMNjM3NDIzMTgzODA1Igz9iSW7Wn7G8yXTiGoq3AOdbHmFRN6xZtwKnS9HcMUDCmbMzvo6IHg%2FLfEcRCXEJc5eYOf73aOQy2OJ8qZoHhnS5anNN4rdeUReWj5YSUcwqy6wwqjAGNd%2B7MOh%2FVfE%2BIvogxqXdZDRnE73heuMeUG3tv2bD0SX3CSOX60Q0qoMIOC5NKTEj%2FOdHjtXo4uB85KZ9MlQMDQ%2FuFgvdpBkwxSFsP7jgk%2FkEV%2BxCnp9zwJjBGcNKpem%2Bp2MKJ1mg5f92IDmFf6AWjPBdPu8CbZP7hq99kQr8wqhLPM3l%2Bc14EnIzLypMqJbjjAKc%2FoXKXSkc5lrP%2F5wQi4YvTftTinJjbUWIFq3e5iz35CLT%2BTlDu12rXX4YIcPxHKEZ2UaNCyo5CMWaDpUUooTvfM3ffVviMQW7PKBlpgoFe80gzSNAENFk3Fr9O38oM069xRXUTzMuJFOkKramwN8CuWeO9NqnkS8k2WeN0NIARoXKn7iHoHlE5hEIusJFpyHLOp2pxUv7aM0%2FMlXB4QR5xNhUaMf3gE5jO8A6PY6xlddxlaSNNn4eNE3DtLKReFBi2hhi5b0%2F8UwZG4es33Ef7M3cXCbPr%2Bjt6sIspoTXPpQK39UJqqiuUJv0I%2FT3ou5DHilU61DhFUF0kSTN8wnyy8pfzCAwcPNBjqkAXhONneSHoCL212q0HD0hy6LY5YPDSbrrbb%2FHiYpuuNYjRaQF3Ly0RqaP80FAJcngOgqCxQj4%2BiaOTQ2RHKJ1kGRS4zIqUU9UjWDGN8g96vKCinuojlVpsKYwtGYdG4Bh5hQAaEfAxwGwO2AxGpb4YUfQcTc8Ifv60R%2FZ1hI%2FeZilMt%2BRVUZFiM1RQ0IAVD%2F0%2BZ2vj0yyOk0jDbsrWMZVhJa0hAs&X-Amz-Signature=4ee5713b87aeafd760faf3a808c13f2c0a8aaf0b4d9a1ea89f77e839bd7be1ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTILPN26%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRHvhBuQAs%2BjH6F%2FhFcASUnJSRnDdS%2F4%2FXn99cgQNMzAIhAOnUzTC%2Bfu2y7UWtrIL4M27NDYN3Ooo7iVJZdEZ7qQvjKv8DCFQQABoMNjM3NDIzMTgzODA1Igz9iSW7Wn7G8yXTiGoq3AOdbHmFRN6xZtwKnS9HcMUDCmbMzvo6IHg%2FLfEcRCXEJc5eYOf73aOQy2OJ8qZoHhnS5anNN4rdeUReWj5YSUcwqy6wwqjAGNd%2B7MOh%2FVfE%2BIvogxqXdZDRnE73heuMeUG3tv2bD0SX3CSOX60Q0qoMIOC5NKTEj%2FOdHjtXo4uB85KZ9MlQMDQ%2FuFgvdpBkwxSFsP7jgk%2FkEV%2BxCnp9zwJjBGcNKpem%2Bp2MKJ1mg5f92IDmFf6AWjPBdPu8CbZP7hq99kQr8wqhLPM3l%2Bc14EnIzLypMqJbjjAKc%2FoXKXSkc5lrP%2F5wQi4YvTftTinJjbUWIFq3e5iz35CLT%2BTlDu12rXX4YIcPxHKEZ2UaNCyo5CMWaDpUUooTvfM3ffVviMQW7PKBlpgoFe80gzSNAENFk3Fr9O38oM069xRXUTzMuJFOkKramwN8CuWeO9NqnkS8k2WeN0NIARoXKn7iHoHlE5hEIusJFpyHLOp2pxUv7aM0%2FMlXB4QR5xNhUaMf3gE5jO8A6PY6xlddxlaSNNn4eNE3DtLKReFBi2hhi5b0%2F8UwZG4es33Ef7M3cXCbPr%2Bjt6sIspoTXPpQK39UJqqiuUJv0I%2FT3ou5DHilU61DhFUF0kSTN8wnyy8pfzCAwcPNBjqkAXhONneSHoCL212q0HD0hy6LY5YPDSbrrbb%2FHiYpuuNYjRaQF3Ly0RqaP80FAJcngOgqCxQj4%2BiaOTQ2RHKJ1kGRS4zIqUU9UjWDGN8g96vKCinuojlVpsKYwtGYdG4Bh5hQAaEfAxwGwO2AxGpb4YUfQcTc8Ifv60R%2FZ1hI%2FeZilMt%2BRVUZFiM1RQ0IAVD%2F0%2BZ2vj0yyOk0jDbsrWMZVhJa0hAs&X-Amz-Signature=7af8c9baf2b8ac0e8d4bcba94de8c902e672166554c472cfe220a7d6a746cb05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTILPN26%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRHvhBuQAs%2BjH6F%2FhFcASUnJSRnDdS%2F4%2FXn99cgQNMzAIhAOnUzTC%2Bfu2y7UWtrIL4M27NDYN3Ooo7iVJZdEZ7qQvjKv8DCFQQABoMNjM3NDIzMTgzODA1Igz9iSW7Wn7G8yXTiGoq3AOdbHmFRN6xZtwKnS9HcMUDCmbMzvo6IHg%2FLfEcRCXEJc5eYOf73aOQy2OJ8qZoHhnS5anNN4rdeUReWj5YSUcwqy6wwqjAGNd%2B7MOh%2FVfE%2BIvogxqXdZDRnE73heuMeUG3tv2bD0SX3CSOX60Q0qoMIOC5NKTEj%2FOdHjtXo4uB85KZ9MlQMDQ%2FuFgvdpBkwxSFsP7jgk%2FkEV%2BxCnp9zwJjBGcNKpem%2Bp2MKJ1mg5f92IDmFf6AWjPBdPu8CbZP7hq99kQr8wqhLPM3l%2Bc14EnIzLypMqJbjjAKc%2FoXKXSkc5lrP%2F5wQi4YvTftTinJjbUWIFq3e5iz35CLT%2BTlDu12rXX4YIcPxHKEZ2UaNCyo5CMWaDpUUooTvfM3ffVviMQW7PKBlpgoFe80gzSNAENFk3Fr9O38oM069xRXUTzMuJFOkKramwN8CuWeO9NqnkS8k2WeN0NIARoXKn7iHoHlE5hEIusJFpyHLOp2pxUv7aM0%2FMlXB4QR5xNhUaMf3gE5jO8A6PY6xlddxlaSNNn4eNE3DtLKReFBi2hhi5b0%2F8UwZG4es33Ef7M3cXCbPr%2Bjt6sIspoTXPpQK39UJqqiuUJv0I%2FT3ou5DHilU61DhFUF0kSTN8wnyy8pfzCAwcPNBjqkAXhONneSHoCL212q0HD0hy6LY5YPDSbrrbb%2FHiYpuuNYjRaQF3Ly0RqaP80FAJcngOgqCxQj4%2BiaOTQ2RHKJ1kGRS4zIqUU9UjWDGN8g96vKCinuojlVpsKYwtGYdG4Bh5hQAaEfAxwGwO2AxGpb4YUfQcTc8Ifv60R%2FZ1hI%2FeZilMt%2BRVUZFiM1RQ0IAVD%2F0%2BZ2vj0yyOk0jDbsrWMZVhJa0hAs&X-Amz-Signature=7c232a5293bc0821fed4f9e8f5ac553102e70cbc810a2628605e130126624cdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

