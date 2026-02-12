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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKIBXXS6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHRoAmSBijrh9wjhw5uNnyHwAQXBARrA0Gw%2FM3NAI025AiBDqcRucLFZyc%2BpZ5vxk83RmMrTpj5fTs%2BFIKyDkWSSqSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvcWGvFZtf8M%2Bazu5KtwDX1Q7j%2FFQYu0qrD%2FCB4qAn8WQD94zJbSrqRuRbGZF3pc1gpnNTEa8x3TRFKYuEeIjos7VEbb28zq9StxFEW3nhTY6kUSIgK1zmOEl56wEMyRjboEX14ZwlIY15MRBooMHB4lH7Pk84bznTCTl6cEaMGkJhUJlnaeoxE2PRRbl0LYlh1ujlnP%2FWgf8MaR7J%2Fj6LsZUIyR7tHt%2BBJKRQvtTrhoZTjxmxfdutD0blwysdMWVZkroSGCXn%2BJxKZ3eMX9LcmwJbcStxMuT5B3h5opWbYJVGcoBbClvu%2FEpR3%2FImuTg1ebQVQSh1GXJTjrz1Dv2qM6ZprpVuEacIXIXIp6Q8a3aWdbY1i8kAvc%2B7PEBEuQCBqmePdLmxHiWbr79gVUGOJEgvHZ%2BdfHSVcJ63is66gxg2yDuVsUcik0tmM%2F87cI1SQLdWG2ZMLxaqA3HX9S92HLPRgVUgdOtdEJF0UGeEjsJjz8J6%2FfkEemKgYf60mzW2lNnZfpbqpK2FO6ZjKIftZI64dwJOf%2FgVzmA9aBU99g1GXpCjhVZbQNxD8HXzbQ7Q3QV2HvRZSjURZ1pDHY8oDYd56emFbNksUk7iyHpe7Ahn%2BBFn53uD%2Fz2TYGx%2BwVKsaN0RoEiICjdmwIw%2F5K1zAY6pgFjA5OtJkx2Q0rkih6WKl8reLGK2RrOwrdZIGeEwyoIsPOOStbHK8vWBJHDdMXuW%2Fex5Sj2fUAb2PSTJxT2e1o0gBtQ8PwLzL8RZ5gQlk7XfeyYFsdJlrd07ZqBY0QZGVPDuzcD6OIqZRIQQlkc3nfduJykzQnAE3k6qXdHw6d%2FcEnsXN9um4u1ELeYlpmg7VNBFEnb1yosjD7QhptYc6B%2FFYnIUP51&X-Amz-Signature=9134fdb9827447d64f55506e54fc50c19239785d7f758e91280c0425c407a958&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKIBXXS6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHRoAmSBijrh9wjhw5uNnyHwAQXBARrA0Gw%2FM3NAI025AiBDqcRucLFZyc%2BpZ5vxk83RmMrTpj5fTs%2BFIKyDkWSSqSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvcWGvFZtf8M%2Bazu5KtwDX1Q7j%2FFQYu0qrD%2FCB4qAn8WQD94zJbSrqRuRbGZF3pc1gpnNTEa8x3TRFKYuEeIjos7VEbb28zq9StxFEW3nhTY6kUSIgK1zmOEl56wEMyRjboEX14ZwlIY15MRBooMHB4lH7Pk84bznTCTl6cEaMGkJhUJlnaeoxE2PRRbl0LYlh1ujlnP%2FWgf8MaR7J%2Fj6LsZUIyR7tHt%2BBJKRQvtTrhoZTjxmxfdutD0blwysdMWVZkroSGCXn%2BJxKZ3eMX9LcmwJbcStxMuT5B3h5opWbYJVGcoBbClvu%2FEpR3%2FImuTg1ebQVQSh1GXJTjrz1Dv2qM6ZprpVuEacIXIXIp6Q8a3aWdbY1i8kAvc%2B7PEBEuQCBqmePdLmxHiWbr79gVUGOJEgvHZ%2BdfHSVcJ63is66gxg2yDuVsUcik0tmM%2F87cI1SQLdWG2ZMLxaqA3HX9S92HLPRgVUgdOtdEJF0UGeEjsJjz8J6%2FfkEemKgYf60mzW2lNnZfpbqpK2FO6ZjKIftZI64dwJOf%2FgVzmA9aBU99g1GXpCjhVZbQNxD8HXzbQ7Q3QV2HvRZSjURZ1pDHY8oDYd56emFbNksUk7iyHpe7Ahn%2BBFn53uD%2Fz2TYGx%2BwVKsaN0RoEiICjdmwIw%2F5K1zAY6pgFjA5OtJkx2Q0rkih6WKl8reLGK2RrOwrdZIGeEwyoIsPOOStbHK8vWBJHDdMXuW%2Fex5Sj2fUAb2PSTJxT2e1o0gBtQ8PwLzL8RZ5gQlk7XfeyYFsdJlrd07ZqBY0QZGVPDuzcD6OIqZRIQQlkc3nfduJykzQnAE3k6qXdHw6d%2FcEnsXN9um4u1ELeYlpmg7VNBFEnb1yosjD7QhptYc6B%2FFYnIUP51&X-Amz-Signature=369f914d15ca7009d421a8f2911df89d2fd5a4c469341172afd97737ea9f80f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKIBXXS6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHRoAmSBijrh9wjhw5uNnyHwAQXBARrA0Gw%2FM3NAI025AiBDqcRucLFZyc%2BpZ5vxk83RmMrTpj5fTs%2BFIKyDkWSSqSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvcWGvFZtf8M%2Bazu5KtwDX1Q7j%2FFQYu0qrD%2FCB4qAn8WQD94zJbSrqRuRbGZF3pc1gpnNTEa8x3TRFKYuEeIjos7VEbb28zq9StxFEW3nhTY6kUSIgK1zmOEl56wEMyRjboEX14ZwlIY15MRBooMHB4lH7Pk84bznTCTl6cEaMGkJhUJlnaeoxE2PRRbl0LYlh1ujlnP%2FWgf8MaR7J%2Fj6LsZUIyR7tHt%2BBJKRQvtTrhoZTjxmxfdutD0blwysdMWVZkroSGCXn%2BJxKZ3eMX9LcmwJbcStxMuT5B3h5opWbYJVGcoBbClvu%2FEpR3%2FImuTg1ebQVQSh1GXJTjrz1Dv2qM6ZprpVuEacIXIXIp6Q8a3aWdbY1i8kAvc%2B7PEBEuQCBqmePdLmxHiWbr79gVUGOJEgvHZ%2BdfHSVcJ63is66gxg2yDuVsUcik0tmM%2F87cI1SQLdWG2ZMLxaqA3HX9S92HLPRgVUgdOtdEJF0UGeEjsJjz8J6%2FfkEemKgYf60mzW2lNnZfpbqpK2FO6ZjKIftZI64dwJOf%2FgVzmA9aBU99g1GXpCjhVZbQNxD8HXzbQ7Q3QV2HvRZSjURZ1pDHY8oDYd56emFbNksUk7iyHpe7Ahn%2BBFn53uD%2Fz2TYGx%2BwVKsaN0RoEiICjdmwIw%2F5K1zAY6pgFjA5OtJkx2Q0rkih6WKl8reLGK2RrOwrdZIGeEwyoIsPOOStbHK8vWBJHDdMXuW%2Fex5Sj2fUAb2PSTJxT2e1o0gBtQ8PwLzL8RZ5gQlk7XfeyYFsdJlrd07ZqBY0QZGVPDuzcD6OIqZRIQQlkc3nfduJykzQnAE3k6qXdHw6d%2FcEnsXN9um4u1ELeYlpmg7VNBFEnb1yosjD7QhptYc6B%2FFYnIUP51&X-Amz-Signature=2cf795b4e5b31719bd8e9685a928c8511034983c284f1032aaa1bcee10e02e93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKIBXXS6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHRoAmSBijrh9wjhw5uNnyHwAQXBARrA0Gw%2FM3NAI025AiBDqcRucLFZyc%2BpZ5vxk83RmMrTpj5fTs%2BFIKyDkWSSqSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvcWGvFZtf8M%2Bazu5KtwDX1Q7j%2FFQYu0qrD%2FCB4qAn8WQD94zJbSrqRuRbGZF3pc1gpnNTEa8x3TRFKYuEeIjos7VEbb28zq9StxFEW3nhTY6kUSIgK1zmOEl56wEMyRjboEX14ZwlIY15MRBooMHB4lH7Pk84bznTCTl6cEaMGkJhUJlnaeoxE2PRRbl0LYlh1ujlnP%2FWgf8MaR7J%2Fj6LsZUIyR7tHt%2BBJKRQvtTrhoZTjxmxfdutD0blwysdMWVZkroSGCXn%2BJxKZ3eMX9LcmwJbcStxMuT5B3h5opWbYJVGcoBbClvu%2FEpR3%2FImuTg1ebQVQSh1GXJTjrz1Dv2qM6ZprpVuEacIXIXIp6Q8a3aWdbY1i8kAvc%2B7PEBEuQCBqmePdLmxHiWbr79gVUGOJEgvHZ%2BdfHSVcJ63is66gxg2yDuVsUcik0tmM%2F87cI1SQLdWG2ZMLxaqA3HX9S92HLPRgVUgdOtdEJF0UGeEjsJjz8J6%2FfkEemKgYf60mzW2lNnZfpbqpK2FO6ZjKIftZI64dwJOf%2FgVzmA9aBU99g1GXpCjhVZbQNxD8HXzbQ7Q3QV2HvRZSjURZ1pDHY8oDYd56emFbNksUk7iyHpe7Ahn%2BBFn53uD%2Fz2TYGx%2BwVKsaN0RoEiICjdmwIw%2F5K1zAY6pgFjA5OtJkx2Q0rkih6WKl8reLGK2RrOwrdZIGeEwyoIsPOOStbHK8vWBJHDdMXuW%2Fex5Sj2fUAb2PSTJxT2e1o0gBtQ8PwLzL8RZ5gQlk7XfeyYFsdJlrd07ZqBY0QZGVPDuzcD6OIqZRIQQlkc3nfduJykzQnAE3k6qXdHw6d%2FcEnsXN9um4u1ELeYlpmg7VNBFEnb1yosjD7QhptYc6B%2FFYnIUP51&X-Amz-Signature=3e3934be32f7979ae1848be58a81cb14a9734efd14ef87679bc187bbe426ed33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKIBXXS6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHRoAmSBijrh9wjhw5uNnyHwAQXBARrA0Gw%2FM3NAI025AiBDqcRucLFZyc%2BpZ5vxk83RmMrTpj5fTs%2BFIKyDkWSSqSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvcWGvFZtf8M%2Bazu5KtwDX1Q7j%2FFQYu0qrD%2FCB4qAn8WQD94zJbSrqRuRbGZF3pc1gpnNTEa8x3TRFKYuEeIjos7VEbb28zq9StxFEW3nhTY6kUSIgK1zmOEl56wEMyRjboEX14ZwlIY15MRBooMHB4lH7Pk84bznTCTl6cEaMGkJhUJlnaeoxE2PRRbl0LYlh1ujlnP%2FWgf8MaR7J%2Fj6LsZUIyR7tHt%2BBJKRQvtTrhoZTjxmxfdutD0blwysdMWVZkroSGCXn%2BJxKZ3eMX9LcmwJbcStxMuT5B3h5opWbYJVGcoBbClvu%2FEpR3%2FImuTg1ebQVQSh1GXJTjrz1Dv2qM6ZprpVuEacIXIXIp6Q8a3aWdbY1i8kAvc%2B7PEBEuQCBqmePdLmxHiWbr79gVUGOJEgvHZ%2BdfHSVcJ63is66gxg2yDuVsUcik0tmM%2F87cI1SQLdWG2ZMLxaqA3HX9S92HLPRgVUgdOtdEJF0UGeEjsJjz8J6%2FfkEemKgYf60mzW2lNnZfpbqpK2FO6ZjKIftZI64dwJOf%2FgVzmA9aBU99g1GXpCjhVZbQNxD8HXzbQ7Q3QV2HvRZSjURZ1pDHY8oDYd56emFbNksUk7iyHpe7Ahn%2BBFn53uD%2Fz2TYGx%2BwVKsaN0RoEiICjdmwIw%2F5K1zAY6pgFjA5OtJkx2Q0rkih6WKl8reLGK2RrOwrdZIGeEwyoIsPOOStbHK8vWBJHDdMXuW%2Fex5Sj2fUAb2PSTJxT2e1o0gBtQ8PwLzL8RZ5gQlk7XfeyYFsdJlrd07ZqBY0QZGVPDuzcD6OIqZRIQQlkc3nfduJykzQnAE3k6qXdHw6d%2FcEnsXN9um4u1ELeYlpmg7VNBFEnb1yosjD7QhptYc6B%2FFYnIUP51&X-Amz-Signature=654324ee631463b674c6af7ffa602f499e1f002912f56c01ebae5b42a3803c7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKIBXXS6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHRoAmSBijrh9wjhw5uNnyHwAQXBARrA0Gw%2FM3NAI025AiBDqcRucLFZyc%2BpZ5vxk83RmMrTpj5fTs%2BFIKyDkWSSqSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvcWGvFZtf8M%2Bazu5KtwDX1Q7j%2FFQYu0qrD%2FCB4qAn8WQD94zJbSrqRuRbGZF3pc1gpnNTEa8x3TRFKYuEeIjos7VEbb28zq9StxFEW3nhTY6kUSIgK1zmOEl56wEMyRjboEX14ZwlIY15MRBooMHB4lH7Pk84bznTCTl6cEaMGkJhUJlnaeoxE2PRRbl0LYlh1ujlnP%2FWgf8MaR7J%2Fj6LsZUIyR7tHt%2BBJKRQvtTrhoZTjxmxfdutD0blwysdMWVZkroSGCXn%2BJxKZ3eMX9LcmwJbcStxMuT5B3h5opWbYJVGcoBbClvu%2FEpR3%2FImuTg1ebQVQSh1GXJTjrz1Dv2qM6ZprpVuEacIXIXIp6Q8a3aWdbY1i8kAvc%2B7PEBEuQCBqmePdLmxHiWbr79gVUGOJEgvHZ%2BdfHSVcJ63is66gxg2yDuVsUcik0tmM%2F87cI1SQLdWG2ZMLxaqA3HX9S92HLPRgVUgdOtdEJF0UGeEjsJjz8J6%2FfkEemKgYf60mzW2lNnZfpbqpK2FO6ZjKIftZI64dwJOf%2FgVzmA9aBU99g1GXpCjhVZbQNxD8HXzbQ7Q3QV2HvRZSjURZ1pDHY8oDYd56emFbNksUk7iyHpe7Ahn%2BBFn53uD%2Fz2TYGx%2BwVKsaN0RoEiICjdmwIw%2F5K1zAY6pgFjA5OtJkx2Q0rkih6WKl8reLGK2RrOwrdZIGeEwyoIsPOOStbHK8vWBJHDdMXuW%2Fex5Sj2fUAb2PSTJxT2e1o0gBtQ8PwLzL8RZ5gQlk7XfeyYFsdJlrd07ZqBY0QZGVPDuzcD6OIqZRIQQlkc3nfduJykzQnAE3k6qXdHw6d%2FcEnsXN9um4u1ELeYlpmg7VNBFEnb1yosjD7QhptYc6B%2FFYnIUP51&X-Amz-Signature=effc06fee335e48880969981237c23df03182542792ec21d82fadad375793cca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKIBXXS6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHRoAmSBijrh9wjhw5uNnyHwAQXBARrA0Gw%2FM3NAI025AiBDqcRucLFZyc%2BpZ5vxk83RmMrTpj5fTs%2BFIKyDkWSSqSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvcWGvFZtf8M%2Bazu5KtwDX1Q7j%2FFQYu0qrD%2FCB4qAn8WQD94zJbSrqRuRbGZF3pc1gpnNTEa8x3TRFKYuEeIjos7VEbb28zq9StxFEW3nhTY6kUSIgK1zmOEl56wEMyRjboEX14ZwlIY15MRBooMHB4lH7Pk84bznTCTl6cEaMGkJhUJlnaeoxE2PRRbl0LYlh1ujlnP%2FWgf8MaR7J%2Fj6LsZUIyR7tHt%2BBJKRQvtTrhoZTjxmxfdutD0blwysdMWVZkroSGCXn%2BJxKZ3eMX9LcmwJbcStxMuT5B3h5opWbYJVGcoBbClvu%2FEpR3%2FImuTg1ebQVQSh1GXJTjrz1Dv2qM6ZprpVuEacIXIXIp6Q8a3aWdbY1i8kAvc%2B7PEBEuQCBqmePdLmxHiWbr79gVUGOJEgvHZ%2BdfHSVcJ63is66gxg2yDuVsUcik0tmM%2F87cI1SQLdWG2ZMLxaqA3HX9S92HLPRgVUgdOtdEJF0UGeEjsJjz8J6%2FfkEemKgYf60mzW2lNnZfpbqpK2FO6ZjKIftZI64dwJOf%2FgVzmA9aBU99g1GXpCjhVZbQNxD8HXzbQ7Q3QV2HvRZSjURZ1pDHY8oDYd56emFbNksUk7iyHpe7Ahn%2BBFn53uD%2Fz2TYGx%2BwVKsaN0RoEiICjdmwIw%2F5K1zAY6pgFjA5OtJkx2Q0rkih6WKl8reLGK2RrOwrdZIGeEwyoIsPOOStbHK8vWBJHDdMXuW%2Fex5Sj2fUAb2PSTJxT2e1o0gBtQ8PwLzL8RZ5gQlk7XfeyYFsdJlrd07ZqBY0QZGVPDuzcD6OIqZRIQQlkc3nfduJykzQnAE3k6qXdHw6d%2FcEnsXN9um4u1ELeYlpmg7VNBFEnb1yosjD7QhptYc6B%2FFYnIUP51&X-Amz-Signature=227e024107846684f93f54b049483562a771103c993fbaea45a3e07b9b5acabe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKIBXXS6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHRoAmSBijrh9wjhw5uNnyHwAQXBARrA0Gw%2FM3NAI025AiBDqcRucLFZyc%2BpZ5vxk83RmMrTpj5fTs%2BFIKyDkWSSqSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvcWGvFZtf8M%2Bazu5KtwDX1Q7j%2FFQYu0qrD%2FCB4qAn8WQD94zJbSrqRuRbGZF3pc1gpnNTEa8x3TRFKYuEeIjos7VEbb28zq9StxFEW3nhTY6kUSIgK1zmOEl56wEMyRjboEX14ZwlIY15MRBooMHB4lH7Pk84bznTCTl6cEaMGkJhUJlnaeoxE2PRRbl0LYlh1ujlnP%2FWgf8MaR7J%2Fj6LsZUIyR7tHt%2BBJKRQvtTrhoZTjxmxfdutD0blwysdMWVZkroSGCXn%2BJxKZ3eMX9LcmwJbcStxMuT5B3h5opWbYJVGcoBbClvu%2FEpR3%2FImuTg1ebQVQSh1GXJTjrz1Dv2qM6ZprpVuEacIXIXIp6Q8a3aWdbY1i8kAvc%2B7PEBEuQCBqmePdLmxHiWbr79gVUGOJEgvHZ%2BdfHSVcJ63is66gxg2yDuVsUcik0tmM%2F87cI1SQLdWG2ZMLxaqA3HX9S92HLPRgVUgdOtdEJF0UGeEjsJjz8J6%2FfkEemKgYf60mzW2lNnZfpbqpK2FO6ZjKIftZI64dwJOf%2FgVzmA9aBU99g1GXpCjhVZbQNxD8HXzbQ7Q3QV2HvRZSjURZ1pDHY8oDYd56emFbNksUk7iyHpe7Ahn%2BBFn53uD%2Fz2TYGx%2BwVKsaN0RoEiICjdmwIw%2F5K1zAY6pgFjA5OtJkx2Q0rkih6WKl8reLGK2RrOwrdZIGeEwyoIsPOOStbHK8vWBJHDdMXuW%2Fex5Sj2fUAb2PSTJxT2e1o0gBtQ8PwLzL8RZ5gQlk7XfeyYFsdJlrd07ZqBY0QZGVPDuzcD6OIqZRIQQlkc3nfduJykzQnAE3k6qXdHw6d%2FcEnsXN9um4u1ELeYlpmg7VNBFEnb1yosjD7QhptYc6B%2FFYnIUP51&X-Amz-Signature=26befb67580723e428b8bf26c6bcd5f746e018a253b4fd487c3e86a1e396e424&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKIBXXS6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHRoAmSBijrh9wjhw5uNnyHwAQXBARrA0Gw%2FM3NAI025AiBDqcRucLFZyc%2BpZ5vxk83RmMrTpj5fTs%2BFIKyDkWSSqSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvcWGvFZtf8M%2Bazu5KtwDX1Q7j%2FFQYu0qrD%2FCB4qAn8WQD94zJbSrqRuRbGZF3pc1gpnNTEa8x3TRFKYuEeIjos7VEbb28zq9StxFEW3nhTY6kUSIgK1zmOEl56wEMyRjboEX14ZwlIY15MRBooMHB4lH7Pk84bznTCTl6cEaMGkJhUJlnaeoxE2PRRbl0LYlh1ujlnP%2FWgf8MaR7J%2Fj6LsZUIyR7tHt%2BBJKRQvtTrhoZTjxmxfdutD0blwysdMWVZkroSGCXn%2BJxKZ3eMX9LcmwJbcStxMuT5B3h5opWbYJVGcoBbClvu%2FEpR3%2FImuTg1ebQVQSh1GXJTjrz1Dv2qM6ZprpVuEacIXIXIp6Q8a3aWdbY1i8kAvc%2B7PEBEuQCBqmePdLmxHiWbr79gVUGOJEgvHZ%2BdfHSVcJ63is66gxg2yDuVsUcik0tmM%2F87cI1SQLdWG2ZMLxaqA3HX9S92HLPRgVUgdOtdEJF0UGeEjsJjz8J6%2FfkEemKgYf60mzW2lNnZfpbqpK2FO6ZjKIftZI64dwJOf%2FgVzmA9aBU99g1GXpCjhVZbQNxD8HXzbQ7Q3QV2HvRZSjURZ1pDHY8oDYd56emFbNksUk7iyHpe7Ahn%2BBFn53uD%2Fz2TYGx%2BwVKsaN0RoEiICjdmwIw%2F5K1zAY6pgFjA5OtJkx2Q0rkih6WKl8reLGK2RrOwrdZIGeEwyoIsPOOStbHK8vWBJHDdMXuW%2Fex5Sj2fUAb2PSTJxT2e1o0gBtQ8PwLzL8RZ5gQlk7XfeyYFsdJlrd07ZqBY0QZGVPDuzcD6OIqZRIQQlkc3nfduJykzQnAE3k6qXdHw6d%2FcEnsXN9um4u1ELeYlpmg7VNBFEnb1yosjD7QhptYc6B%2FFYnIUP51&X-Amz-Signature=93835004646ed212511b6a56d389ec615cb71bda36239058c5470f5055f84dc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKIBXXS6%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIHRoAmSBijrh9wjhw5uNnyHwAQXBARrA0Gw%2FM3NAI025AiBDqcRucLFZyc%2BpZ5vxk83RmMrTpj5fTs%2BFIKyDkWSSqSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvcWGvFZtf8M%2Bazu5KtwDX1Q7j%2FFQYu0qrD%2FCB4qAn8WQD94zJbSrqRuRbGZF3pc1gpnNTEa8x3TRFKYuEeIjos7VEbb28zq9StxFEW3nhTY6kUSIgK1zmOEl56wEMyRjboEX14ZwlIY15MRBooMHB4lH7Pk84bznTCTl6cEaMGkJhUJlnaeoxE2PRRbl0LYlh1ujlnP%2FWgf8MaR7J%2Fj6LsZUIyR7tHt%2BBJKRQvtTrhoZTjxmxfdutD0blwysdMWVZkroSGCXn%2BJxKZ3eMX9LcmwJbcStxMuT5B3h5opWbYJVGcoBbClvu%2FEpR3%2FImuTg1ebQVQSh1GXJTjrz1Dv2qM6ZprpVuEacIXIXIp6Q8a3aWdbY1i8kAvc%2B7PEBEuQCBqmePdLmxHiWbr79gVUGOJEgvHZ%2BdfHSVcJ63is66gxg2yDuVsUcik0tmM%2F87cI1SQLdWG2ZMLxaqA3HX9S92HLPRgVUgdOtdEJF0UGeEjsJjz8J6%2FfkEemKgYf60mzW2lNnZfpbqpK2FO6ZjKIftZI64dwJOf%2FgVzmA9aBU99g1GXpCjhVZbQNxD8HXzbQ7Q3QV2HvRZSjURZ1pDHY8oDYd56emFbNksUk7iyHpe7Ahn%2BBFn53uD%2Fz2TYGx%2BwVKsaN0RoEiICjdmwIw%2F5K1zAY6pgFjA5OtJkx2Q0rkih6WKl8reLGK2RrOwrdZIGeEwyoIsPOOStbHK8vWBJHDdMXuW%2Fex5Sj2fUAb2PSTJxT2e1o0gBtQ8PwLzL8RZ5gQlk7XfeyYFsdJlrd07ZqBY0QZGVPDuzcD6OIqZRIQQlkc3nfduJykzQnAE3k6qXdHw6d%2FcEnsXN9um4u1ELeYlpmg7VNBFEnb1yosjD7QhptYc6B%2FFYnIUP51&X-Amz-Signature=13597c06b8bf517e9ffba67c3a67a5d8aecfe36b8230de2ef10bdf74093abd12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

