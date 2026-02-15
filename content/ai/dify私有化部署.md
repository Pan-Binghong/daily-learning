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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAHKWSV%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQD8fgkJPdNg%2FAOqwl9jdDre4zW6ki6PT7LEK%2F18Yu1KOwIganY3UDQac6hpZBjsRL0Pb7KYFvHBxpkmtCuV%2BNV1c%2Bcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLIpKdD42WawZUxyDyrcA9Pul8vYXmMBka1DxWRCqjhYjW1kJ8ewMC9UlLa9hOwN2XqD5unae%2B%2BHJrTtM6p0ZZ7wFgEJwdakC1UEFP%2FZ3dAfAIZezYNMSNvg2GJGE7JdI8iB7LULQLn1LOUm4JZgbR26qSFaLajxD%2B1Jm%2FGEeS6WFv8kPzeAiitiCFBQ3b8Ha8mQBVb9uEopWxw%2FQKdqwEreCYuCkQV0lHDx%2Fq67i4cY%2B52h8Z0d4WVbU9892J3G%2B34XZNKLzsGxBv1dztSsYFyPELEhkc%2B%2FOOkPRZWUvdwaAuUiee0sh3RLATtq8ikfefTsfnOTqrMLdAIf47zXq9HNNxQYOastVozIPoyyj%2B8ZabF47iE6dsl%2BIy9AafWoWalX68tuAqi04BjQF%2FI1TeEJyI%2FH2afOGW%2FfdEn0kQwtNhyWBlQ%2B3tEpUWJ9tVNBeyzAbY%2BuaDK3plYAcsY4wCsDy4MTnOkyB1782g2FIxqbLbOPHZgxSIzeGREo4lSlT5rDwy%2BJWOzOx7Oiix9qNiXTwpCtOAbbOafZWrfYblfkfHLfzuuJR4ij2cQM0E%2FrJxgkNxD1X41RA%2Buz9pbFGUh3WYOeXxkMWXLh0A4xP513IgV7QSD8xQr7Y69qKhOzCvUslKaRvdwGtC%2F7MPydxMwGOqUBF%2FXRAm3iYUw4lqn%2FCyL1gM4HkzKNeapLrifYrHLzY7WcosUcTxaLE2kOt%2BDRiHaVf%2FH%2FLZ9G9XvBTBfa2llBwcOsiERN3huC3AO3HT3NP9ZiNbS9sm66%2FBfowy0FbcawII%2B%2FpNlKH9oVlHK3xGZ5rXebFGnuqau1%2Fm6Ezyj7RIaX1XiDjPhafRYZ7zkZYB8CZ6Cqfyru2comKqqjDNz8ldEMjxy5&X-Amz-Signature=53b598528be83d5e24056f5db3a69666ba2f66261eeb745d8a57591052eb9319&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAHKWSV%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQD8fgkJPdNg%2FAOqwl9jdDre4zW6ki6PT7LEK%2F18Yu1KOwIganY3UDQac6hpZBjsRL0Pb7KYFvHBxpkmtCuV%2BNV1c%2Bcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLIpKdD42WawZUxyDyrcA9Pul8vYXmMBka1DxWRCqjhYjW1kJ8ewMC9UlLa9hOwN2XqD5unae%2B%2BHJrTtM6p0ZZ7wFgEJwdakC1UEFP%2FZ3dAfAIZezYNMSNvg2GJGE7JdI8iB7LULQLn1LOUm4JZgbR26qSFaLajxD%2B1Jm%2FGEeS6WFv8kPzeAiitiCFBQ3b8Ha8mQBVb9uEopWxw%2FQKdqwEreCYuCkQV0lHDx%2Fq67i4cY%2B52h8Z0d4WVbU9892J3G%2B34XZNKLzsGxBv1dztSsYFyPELEhkc%2B%2FOOkPRZWUvdwaAuUiee0sh3RLATtq8ikfefTsfnOTqrMLdAIf47zXq9HNNxQYOastVozIPoyyj%2B8ZabF47iE6dsl%2BIy9AafWoWalX68tuAqi04BjQF%2FI1TeEJyI%2FH2afOGW%2FfdEn0kQwtNhyWBlQ%2B3tEpUWJ9tVNBeyzAbY%2BuaDK3plYAcsY4wCsDy4MTnOkyB1782g2FIxqbLbOPHZgxSIzeGREo4lSlT5rDwy%2BJWOzOx7Oiix9qNiXTwpCtOAbbOafZWrfYblfkfHLfzuuJR4ij2cQM0E%2FrJxgkNxD1X41RA%2Buz9pbFGUh3WYOeXxkMWXLh0A4xP513IgV7QSD8xQr7Y69qKhOzCvUslKaRvdwGtC%2F7MPydxMwGOqUBF%2FXRAm3iYUw4lqn%2FCyL1gM4HkzKNeapLrifYrHLzY7WcosUcTxaLE2kOt%2BDRiHaVf%2FH%2FLZ9G9XvBTBfa2llBwcOsiERN3huC3AO3HT3NP9ZiNbS9sm66%2FBfowy0FbcawII%2B%2FpNlKH9oVlHK3xGZ5rXebFGnuqau1%2Fm6Ezyj7RIaX1XiDjPhafRYZ7zkZYB8CZ6Cqfyru2comKqqjDNz8ldEMjxy5&X-Amz-Signature=f6abf4fd4ec3123c2c7500b479386631ce7f423dbc56c15ed2fdfa062222ddca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAHKWSV%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQD8fgkJPdNg%2FAOqwl9jdDre4zW6ki6PT7LEK%2F18Yu1KOwIganY3UDQac6hpZBjsRL0Pb7KYFvHBxpkmtCuV%2BNV1c%2Bcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLIpKdD42WawZUxyDyrcA9Pul8vYXmMBka1DxWRCqjhYjW1kJ8ewMC9UlLa9hOwN2XqD5unae%2B%2BHJrTtM6p0ZZ7wFgEJwdakC1UEFP%2FZ3dAfAIZezYNMSNvg2GJGE7JdI8iB7LULQLn1LOUm4JZgbR26qSFaLajxD%2B1Jm%2FGEeS6WFv8kPzeAiitiCFBQ3b8Ha8mQBVb9uEopWxw%2FQKdqwEreCYuCkQV0lHDx%2Fq67i4cY%2B52h8Z0d4WVbU9892J3G%2B34XZNKLzsGxBv1dztSsYFyPELEhkc%2B%2FOOkPRZWUvdwaAuUiee0sh3RLATtq8ikfefTsfnOTqrMLdAIf47zXq9HNNxQYOastVozIPoyyj%2B8ZabF47iE6dsl%2BIy9AafWoWalX68tuAqi04BjQF%2FI1TeEJyI%2FH2afOGW%2FfdEn0kQwtNhyWBlQ%2B3tEpUWJ9tVNBeyzAbY%2BuaDK3plYAcsY4wCsDy4MTnOkyB1782g2FIxqbLbOPHZgxSIzeGREo4lSlT5rDwy%2BJWOzOx7Oiix9qNiXTwpCtOAbbOafZWrfYblfkfHLfzuuJR4ij2cQM0E%2FrJxgkNxD1X41RA%2Buz9pbFGUh3WYOeXxkMWXLh0A4xP513IgV7QSD8xQr7Y69qKhOzCvUslKaRvdwGtC%2F7MPydxMwGOqUBF%2FXRAm3iYUw4lqn%2FCyL1gM4HkzKNeapLrifYrHLzY7WcosUcTxaLE2kOt%2BDRiHaVf%2FH%2FLZ9G9XvBTBfa2llBwcOsiERN3huC3AO3HT3NP9ZiNbS9sm66%2FBfowy0FbcawII%2B%2FpNlKH9oVlHK3xGZ5rXebFGnuqau1%2Fm6Ezyj7RIaX1XiDjPhafRYZ7zkZYB8CZ6Cqfyru2comKqqjDNz8ldEMjxy5&X-Amz-Signature=4c2100f26e5c5997788b5456bfc64bdb820dd4466782a024ee3b19ef094e5966&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAHKWSV%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQD8fgkJPdNg%2FAOqwl9jdDre4zW6ki6PT7LEK%2F18Yu1KOwIganY3UDQac6hpZBjsRL0Pb7KYFvHBxpkmtCuV%2BNV1c%2Bcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLIpKdD42WawZUxyDyrcA9Pul8vYXmMBka1DxWRCqjhYjW1kJ8ewMC9UlLa9hOwN2XqD5unae%2B%2BHJrTtM6p0ZZ7wFgEJwdakC1UEFP%2FZ3dAfAIZezYNMSNvg2GJGE7JdI8iB7LULQLn1LOUm4JZgbR26qSFaLajxD%2B1Jm%2FGEeS6WFv8kPzeAiitiCFBQ3b8Ha8mQBVb9uEopWxw%2FQKdqwEreCYuCkQV0lHDx%2Fq67i4cY%2B52h8Z0d4WVbU9892J3G%2B34XZNKLzsGxBv1dztSsYFyPELEhkc%2B%2FOOkPRZWUvdwaAuUiee0sh3RLATtq8ikfefTsfnOTqrMLdAIf47zXq9HNNxQYOastVozIPoyyj%2B8ZabF47iE6dsl%2BIy9AafWoWalX68tuAqi04BjQF%2FI1TeEJyI%2FH2afOGW%2FfdEn0kQwtNhyWBlQ%2B3tEpUWJ9tVNBeyzAbY%2BuaDK3plYAcsY4wCsDy4MTnOkyB1782g2FIxqbLbOPHZgxSIzeGREo4lSlT5rDwy%2BJWOzOx7Oiix9qNiXTwpCtOAbbOafZWrfYblfkfHLfzuuJR4ij2cQM0E%2FrJxgkNxD1X41RA%2Buz9pbFGUh3WYOeXxkMWXLh0A4xP513IgV7QSD8xQr7Y69qKhOzCvUslKaRvdwGtC%2F7MPydxMwGOqUBF%2FXRAm3iYUw4lqn%2FCyL1gM4HkzKNeapLrifYrHLzY7WcosUcTxaLE2kOt%2BDRiHaVf%2FH%2FLZ9G9XvBTBfa2llBwcOsiERN3huC3AO3HT3NP9ZiNbS9sm66%2FBfowy0FbcawII%2B%2FpNlKH9oVlHK3xGZ5rXebFGnuqau1%2Fm6Ezyj7RIaX1XiDjPhafRYZ7zkZYB8CZ6Cqfyru2comKqqjDNz8ldEMjxy5&X-Amz-Signature=bf9d9e9115ed9fae8d1759e5e112f27ed8b7537a33233241811d049587f82ce2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAHKWSV%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQD8fgkJPdNg%2FAOqwl9jdDre4zW6ki6PT7LEK%2F18Yu1KOwIganY3UDQac6hpZBjsRL0Pb7KYFvHBxpkmtCuV%2BNV1c%2Bcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLIpKdD42WawZUxyDyrcA9Pul8vYXmMBka1DxWRCqjhYjW1kJ8ewMC9UlLa9hOwN2XqD5unae%2B%2BHJrTtM6p0ZZ7wFgEJwdakC1UEFP%2FZ3dAfAIZezYNMSNvg2GJGE7JdI8iB7LULQLn1LOUm4JZgbR26qSFaLajxD%2B1Jm%2FGEeS6WFv8kPzeAiitiCFBQ3b8Ha8mQBVb9uEopWxw%2FQKdqwEreCYuCkQV0lHDx%2Fq67i4cY%2B52h8Z0d4WVbU9892J3G%2B34XZNKLzsGxBv1dztSsYFyPELEhkc%2B%2FOOkPRZWUvdwaAuUiee0sh3RLATtq8ikfefTsfnOTqrMLdAIf47zXq9HNNxQYOastVozIPoyyj%2B8ZabF47iE6dsl%2BIy9AafWoWalX68tuAqi04BjQF%2FI1TeEJyI%2FH2afOGW%2FfdEn0kQwtNhyWBlQ%2B3tEpUWJ9tVNBeyzAbY%2BuaDK3plYAcsY4wCsDy4MTnOkyB1782g2FIxqbLbOPHZgxSIzeGREo4lSlT5rDwy%2BJWOzOx7Oiix9qNiXTwpCtOAbbOafZWrfYblfkfHLfzuuJR4ij2cQM0E%2FrJxgkNxD1X41RA%2Buz9pbFGUh3WYOeXxkMWXLh0A4xP513IgV7QSD8xQr7Y69qKhOzCvUslKaRvdwGtC%2F7MPydxMwGOqUBF%2FXRAm3iYUw4lqn%2FCyL1gM4HkzKNeapLrifYrHLzY7WcosUcTxaLE2kOt%2BDRiHaVf%2FH%2FLZ9G9XvBTBfa2llBwcOsiERN3huC3AO3HT3NP9ZiNbS9sm66%2FBfowy0FbcawII%2B%2FpNlKH9oVlHK3xGZ5rXebFGnuqau1%2Fm6Ezyj7RIaX1XiDjPhafRYZ7zkZYB8CZ6Cqfyru2comKqqjDNz8ldEMjxy5&X-Amz-Signature=b6ee255b0b40470a9f859cc82f0422e4a25a3491a7650a167b5a5f3d3986e3c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAHKWSV%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQD8fgkJPdNg%2FAOqwl9jdDre4zW6ki6PT7LEK%2F18Yu1KOwIganY3UDQac6hpZBjsRL0Pb7KYFvHBxpkmtCuV%2BNV1c%2Bcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLIpKdD42WawZUxyDyrcA9Pul8vYXmMBka1DxWRCqjhYjW1kJ8ewMC9UlLa9hOwN2XqD5unae%2B%2BHJrTtM6p0ZZ7wFgEJwdakC1UEFP%2FZ3dAfAIZezYNMSNvg2GJGE7JdI8iB7LULQLn1LOUm4JZgbR26qSFaLajxD%2B1Jm%2FGEeS6WFv8kPzeAiitiCFBQ3b8Ha8mQBVb9uEopWxw%2FQKdqwEreCYuCkQV0lHDx%2Fq67i4cY%2B52h8Z0d4WVbU9892J3G%2B34XZNKLzsGxBv1dztSsYFyPELEhkc%2B%2FOOkPRZWUvdwaAuUiee0sh3RLATtq8ikfefTsfnOTqrMLdAIf47zXq9HNNxQYOastVozIPoyyj%2B8ZabF47iE6dsl%2BIy9AafWoWalX68tuAqi04BjQF%2FI1TeEJyI%2FH2afOGW%2FfdEn0kQwtNhyWBlQ%2B3tEpUWJ9tVNBeyzAbY%2BuaDK3plYAcsY4wCsDy4MTnOkyB1782g2FIxqbLbOPHZgxSIzeGREo4lSlT5rDwy%2BJWOzOx7Oiix9qNiXTwpCtOAbbOafZWrfYblfkfHLfzuuJR4ij2cQM0E%2FrJxgkNxD1X41RA%2Buz9pbFGUh3WYOeXxkMWXLh0A4xP513IgV7QSD8xQr7Y69qKhOzCvUslKaRvdwGtC%2F7MPydxMwGOqUBF%2FXRAm3iYUw4lqn%2FCyL1gM4HkzKNeapLrifYrHLzY7WcosUcTxaLE2kOt%2BDRiHaVf%2FH%2FLZ9G9XvBTBfa2llBwcOsiERN3huC3AO3HT3NP9ZiNbS9sm66%2FBfowy0FbcawII%2B%2FpNlKH9oVlHK3xGZ5rXebFGnuqau1%2Fm6Ezyj7RIaX1XiDjPhafRYZ7zkZYB8CZ6Cqfyru2comKqqjDNz8ldEMjxy5&X-Amz-Signature=63d593eec6be23644614c3ac7e50b10fa4c268057b223b36df5c988e59e69409&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAHKWSV%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQD8fgkJPdNg%2FAOqwl9jdDre4zW6ki6PT7LEK%2F18Yu1KOwIganY3UDQac6hpZBjsRL0Pb7KYFvHBxpkmtCuV%2BNV1c%2Bcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLIpKdD42WawZUxyDyrcA9Pul8vYXmMBka1DxWRCqjhYjW1kJ8ewMC9UlLa9hOwN2XqD5unae%2B%2BHJrTtM6p0ZZ7wFgEJwdakC1UEFP%2FZ3dAfAIZezYNMSNvg2GJGE7JdI8iB7LULQLn1LOUm4JZgbR26qSFaLajxD%2B1Jm%2FGEeS6WFv8kPzeAiitiCFBQ3b8Ha8mQBVb9uEopWxw%2FQKdqwEreCYuCkQV0lHDx%2Fq67i4cY%2B52h8Z0d4WVbU9892J3G%2B34XZNKLzsGxBv1dztSsYFyPELEhkc%2B%2FOOkPRZWUvdwaAuUiee0sh3RLATtq8ikfefTsfnOTqrMLdAIf47zXq9HNNxQYOastVozIPoyyj%2B8ZabF47iE6dsl%2BIy9AafWoWalX68tuAqi04BjQF%2FI1TeEJyI%2FH2afOGW%2FfdEn0kQwtNhyWBlQ%2B3tEpUWJ9tVNBeyzAbY%2BuaDK3plYAcsY4wCsDy4MTnOkyB1782g2FIxqbLbOPHZgxSIzeGREo4lSlT5rDwy%2BJWOzOx7Oiix9qNiXTwpCtOAbbOafZWrfYblfkfHLfzuuJR4ij2cQM0E%2FrJxgkNxD1X41RA%2Buz9pbFGUh3WYOeXxkMWXLh0A4xP513IgV7QSD8xQr7Y69qKhOzCvUslKaRvdwGtC%2F7MPydxMwGOqUBF%2FXRAm3iYUw4lqn%2FCyL1gM4HkzKNeapLrifYrHLzY7WcosUcTxaLE2kOt%2BDRiHaVf%2FH%2FLZ9G9XvBTBfa2llBwcOsiERN3huC3AO3HT3NP9ZiNbS9sm66%2FBfowy0FbcawII%2B%2FpNlKH9oVlHK3xGZ5rXebFGnuqau1%2Fm6Ezyj7RIaX1XiDjPhafRYZ7zkZYB8CZ6Cqfyru2comKqqjDNz8ldEMjxy5&X-Amz-Signature=9ec2d7f935394b293d084bccd07c91d6008982d6668dbac92d7cea5ebbf8b246&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAHKWSV%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQD8fgkJPdNg%2FAOqwl9jdDre4zW6ki6PT7LEK%2F18Yu1KOwIganY3UDQac6hpZBjsRL0Pb7KYFvHBxpkmtCuV%2BNV1c%2Bcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLIpKdD42WawZUxyDyrcA9Pul8vYXmMBka1DxWRCqjhYjW1kJ8ewMC9UlLa9hOwN2XqD5unae%2B%2BHJrTtM6p0ZZ7wFgEJwdakC1UEFP%2FZ3dAfAIZezYNMSNvg2GJGE7JdI8iB7LULQLn1LOUm4JZgbR26qSFaLajxD%2B1Jm%2FGEeS6WFv8kPzeAiitiCFBQ3b8Ha8mQBVb9uEopWxw%2FQKdqwEreCYuCkQV0lHDx%2Fq67i4cY%2B52h8Z0d4WVbU9892J3G%2B34XZNKLzsGxBv1dztSsYFyPELEhkc%2B%2FOOkPRZWUvdwaAuUiee0sh3RLATtq8ikfefTsfnOTqrMLdAIf47zXq9HNNxQYOastVozIPoyyj%2B8ZabF47iE6dsl%2BIy9AafWoWalX68tuAqi04BjQF%2FI1TeEJyI%2FH2afOGW%2FfdEn0kQwtNhyWBlQ%2B3tEpUWJ9tVNBeyzAbY%2BuaDK3plYAcsY4wCsDy4MTnOkyB1782g2FIxqbLbOPHZgxSIzeGREo4lSlT5rDwy%2BJWOzOx7Oiix9qNiXTwpCtOAbbOafZWrfYblfkfHLfzuuJR4ij2cQM0E%2FrJxgkNxD1X41RA%2Buz9pbFGUh3WYOeXxkMWXLh0A4xP513IgV7QSD8xQr7Y69qKhOzCvUslKaRvdwGtC%2F7MPydxMwGOqUBF%2FXRAm3iYUw4lqn%2FCyL1gM4HkzKNeapLrifYrHLzY7WcosUcTxaLE2kOt%2BDRiHaVf%2FH%2FLZ9G9XvBTBfa2llBwcOsiERN3huC3AO3HT3NP9ZiNbS9sm66%2FBfowy0FbcawII%2B%2FpNlKH9oVlHK3xGZ5rXebFGnuqau1%2Fm6Ezyj7RIaX1XiDjPhafRYZ7zkZYB8CZ6Cqfyru2comKqqjDNz8ldEMjxy5&X-Amz-Signature=c3027e1141e2efe7f0eef19be86d1a135f811a667377758ce25137b64e8ce7c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAHKWSV%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQD8fgkJPdNg%2FAOqwl9jdDre4zW6ki6PT7LEK%2F18Yu1KOwIganY3UDQac6hpZBjsRL0Pb7KYFvHBxpkmtCuV%2BNV1c%2Bcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLIpKdD42WawZUxyDyrcA9Pul8vYXmMBka1DxWRCqjhYjW1kJ8ewMC9UlLa9hOwN2XqD5unae%2B%2BHJrTtM6p0ZZ7wFgEJwdakC1UEFP%2FZ3dAfAIZezYNMSNvg2GJGE7JdI8iB7LULQLn1LOUm4JZgbR26qSFaLajxD%2B1Jm%2FGEeS6WFv8kPzeAiitiCFBQ3b8Ha8mQBVb9uEopWxw%2FQKdqwEreCYuCkQV0lHDx%2Fq67i4cY%2B52h8Z0d4WVbU9892J3G%2B34XZNKLzsGxBv1dztSsYFyPELEhkc%2B%2FOOkPRZWUvdwaAuUiee0sh3RLATtq8ikfefTsfnOTqrMLdAIf47zXq9HNNxQYOastVozIPoyyj%2B8ZabF47iE6dsl%2BIy9AafWoWalX68tuAqi04BjQF%2FI1TeEJyI%2FH2afOGW%2FfdEn0kQwtNhyWBlQ%2B3tEpUWJ9tVNBeyzAbY%2BuaDK3plYAcsY4wCsDy4MTnOkyB1782g2FIxqbLbOPHZgxSIzeGREo4lSlT5rDwy%2BJWOzOx7Oiix9qNiXTwpCtOAbbOafZWrfYblfkfHLfzuuJR4ij2cQM0E%2FrJxgkNxD1X41RA%2Buz9pbFGUh3WYOeXxkMWXLh0A4xP513IgV7QSD8xQr7Y69qKhOzCvUslKaRvdwGtC%2F7MPydxMwGOqUBF%2FXRAm3iYUw4lqn%2FCyL1gM4HkzKNeapLrifYrHLzY7WcosUcTxaLE2kOt%2BDRiHaVf%2FH%2FLZ9G9XvBTBfa2llBwcOsiERN3huC3AO3HT3NP9ZiNbS9sm66%2FBfowy0FbcawII%2B%2FpNlKH9oVlHK3xGZ5rXebFGnuqau1%2Fm6Ezyj7RIaX1XiDjPhafRYZ7zkZYB8CZ6Cqfyru2comKqqjDNz8ldEMjxy5&X-Amz-Signature=224b98681f95fef15307e8269978a7b637846d56b2c1f94de26d1d7750c8267d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAHKWSV%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQD8fgkJPdNg%2FAOqwl9jdDre4zW6ki6PT7LEK%2F18Yu1KOwIganY3UDQac6hpZBjsRL0Pb7KYFvHBxpkmtCuV%2BNV1c%2Bcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLIpKdD42WawZUxyDyrcA9Pul8vYXmMBka1DxWRCqjhYjW1kJ8ewMC9UlLa9hOwN2XqD5unae%2B%2BHJrTtM6p0ZZ7wFgEJwdakC1UEFP%2FZ3dAfAIZezYNMSNvg2GJGE7JdI8iB7LULQLn1LOUm4JZgbR26qSFaLajxD%2B1Jm%2FGEeS6WFv8kPzeAiitiCFBQ3b8Ha8mQBVb9uEopWxw%2FQKdqwEreCYuCkQV0lHDx%2Fq67i4cY%2B52h8Z0d4WVbU9892J3G%2B34XZNKLzsGxBv1dztSsYFyPELEhkc%2B%2FOOkPRZWUvdwaAuUiee0sh3RLATtq8ikfefTsfnOTqrMLdAIf47zXq9HNNxQYOastVozIPoyyj%2B8ZabF47iE6dsl%2BIy9AafWoWalX68tuAqi04BjQF%2FI1TeEJyI%2FH2afOGW%2FfdEn0kQwtNhyWBlQ%2B3tEpUWJ9tVNBeyzAbY%2BuaDK3plYAcsY4wCsDy4MTnOkyB1782g2FIxqbLbOPHZgxSIzeGREo4lSlT5rDwy%2BJWOzOx7Oiix9qNiXTwpCtOAbbOafZWrfYblfkfHLfzuuJR4ij2cQM0E%2FrJxgkNxD1X41RA%2Buz9pbFGUh3WYOeXxkMWXLh0A4xP513IgV7QSD8xQr7Y69qKhOzCvUslKaRvdwGtC%2F7MPydxMwGOqUBF%2FXRAm3iYUw4lqn%2FCyL1gM4HkzKNeapLrifYrHLzY7WcosUcTxaLE2kOt%2BDRiHaVf%2FH%2FLZ9G9XvBTBfa2llBwcOsiERN3huC3AO3HT3NP9ZiNbS9sm66%2FBfowy0FbcawII%2B%2FpNlKH9oVlHK3xGZ5rXebFGnuqau1%2Fm6Ezyj7RIaX1XiDjPhafRYZ7zkZYB8CZ6Cqfyru2comKqqjDNz8ldEMjxy5&X-Amz-Signature=1de42894a597688ae32087ac7b827f3a03d7a7984c8fa033446ed61e0c963ca5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

