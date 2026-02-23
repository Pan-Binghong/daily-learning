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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LPY4O6T%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDH1LpeddXvMaBN86l%2F1jyG%2BniSLJq3bypqHI%2Bh1rRVtAIgalTFdfDJl67we9Ud6lIGGQVYjq35NKeq%2FlJZ5gXbnqkqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZOY1car22JVNyABCrcA4FS0J2C3JWAbb%2FFPdG4wzIf2%2BggocUzPUMek4VNgD7%2FAtJPkQ30tMd%2B5mTSVFvTN2jg2MaqQ9hGb77ZzyD5tdJyet8bZ8uQ4g%2BmhXE%2BAMHdJP67jhmz7QY8ecNuQBBzwinIMNMjuZXxL1gLytVcrgyOinYvJSJMraHmpp264kuhOvcHOXtoHysnkuYqNJ1LGGLDlh9rshGmWhvsVAiW8rSO1dz5vdj2kKxqFhDf4tvCU%2Bxe8o7meP6jYLJ9lWdTOQguDUPhsq%2Br51pJfLlqZKZvvHqqXXQmLYxZsPdF0NhEf7q3pYl401UhnFVYDSlHJIfJdF1Yf5%2BYwCh5x2QcMMtyOzx2q2hP9WqSFSFpumGi3G6eKjOxuSp9N082ySHD%2FhC31g%2BeCzlcNr0lIw07cr625JysKZjMmf3l%2F92lhOctE3XR2UjiecGKoEaYLMjGNi%2Bs0VgOvGmcDWmw9tqJjalooJKDLlRJzUu8SzmID0FNISuF9ERltViA1RL4dYBwg7InUqerPuNv8wtZZfuxo9y70otmzfQsbiAqMpI6pLKYB%2Frxn7HNVWHDsB47DO%2FXNC1%2Fy%2FQpZb193dcatTENt82H84O5nUkUm7kOV9g1Hm7zKw2n6GYA%2FBUdkmAIMNyT78wGOqUBzWqevMb6bo3mydzhSnqkE%2FLr9b2Qyu88%2BeEOuxuNhn4pbJxm2kLaaoqET9GY6dpep2Is7BgB3IMDDjr5esxo9qckvCAVrpmRWIpgtgXR7Hl6Hq3oXVO9rrAdes7OpCNNh1XA%2FFVQ3NA%2FC9twToGGH6sy86%2FoHOidTfLgaW87s6jLI0Cg%2B73o1c%2Fl8ABCz1tSVoATrdjUdEgK2vRHYb%2BxUaS%2Bioio&X-Amz-Signature=1990a3efd3ce9a87951cdd834f63da464e26fcc14bfad39ce51622100e05875b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LPY4O6T%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDH1LpeddXvMaBN86l%2F1jyG%2BniSLJq3bypqHI%2Bh1rRVtAIgalTFdfDJl67we9Ud6lIGGQVYjq35NKeq%2FlJZ5gXbnqkqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZOY1car22JVNyABCrcA4FS0J2C3JWAbb%2FFPdG4wzIf2%2BggocUzPUMek4VNgD7%2FAtJPkQ30tMd%2B5mTSVFvTN2jg2MaqQ9hGb77ZzyD5tdJyet8bZ8uQ4g%2BmhXE%2BAMHdJP67jhmz7QY8ecNuQBBzwinIMNMjuZXxL1gLytVcrgyOinYvJSJMraHmpp264kuhOvcHOXtoHysnkuYqNJ1LGGLDlh9rshGmWhvsVAiW8rSO1dz5vdj2kKxqFhDf4tvCU%2Bxe8o7meP6jYLJ9lWdTOQguDUPhsq%2Br51pJfLlqZKZvvHqqXXQmLYxZsPdF0NhEf7q3pYl401UhnFVYDSlHJIfJdF1Yf5%2BYwCh5x2QcMMtyOzx2q2hP9WqSFSFpumGi3G6eKjOxuSp9N082ySHD%2FhC31g%2BeCzlcNr0lIw07cr625JysKZjMmf3l%2F92lhOctE3XR2UjiecGKoEaYLMjGNi%2Bs0VgOvGmcDWmw9tqJjalooJKDLlRJzUu8SzmID0FNISuF9ERltViA1RL4dYBwg7InUqerPuNv8wtZZfuxo9y70otmzfQsbiAqMpI6pLKYB%2Frxn7HNVWHDsB47DO%2FXNC1%2Fy%2FQpZb193dcatTENt82H84O5nUkUm7kOV9g1Hm7zKw2n6GYA%2FBUdkmAIMNyT78wGOqUBzWqevMb6bo3mydzhSnqkE%2FLr9b2Qyu88%2BeEOuxuNhn4pbJxm2kLaaoqET9GY6dpep2Is7BgB3IMDDjr5esxo9qckvCAVrpmRWIpgtgXR7Hl6Hq3oXVO9rrAdes7OpCNNh1XA%2FFVQ3NA%2FC9twToGGH6sy86%2FoHOidTfLgaW87s6jLI0Cg%2B73o1c%2Fl8ABCz1tSVoATrdjUdEgK2vRHYb%2BxUaS%2Bioio&X-Amz-Signature=fa7208f9ed17ae2f118a1488be1af64c8eed1205cf6684e962922085becb913a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LPY4O6T%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDH1LpeddXvMaBN86l%2F1jyG%2BniSLJq3bypqHI%2Bh1rRVtAIgalTFdfDJl67we9Ud6lIGGQVYjq35NKeq%2FlJZ5gXbnqkqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZOY1car22JVNyABCrcA4FS0J2C3JWAbb%2FFPdG4wzIf2%2BggocUzPUMek4VNgD7%2FAtJPkQ30tMd%2B5mTSVFvTN2jg2MaqQ9hGb77ZzyD5tdJyet8bZ8uQ4g%2BmhXE%2BAMHdJP67jhmz7QY8ecNuQBBzwinIMNMjuZXxL1gLytVcrgyOinYvJSJMraHmpp264kuhOvcHOXtoHysnkuYqNJ1LGGLDlh9rshGmWhvsVAiW8rSO1dz5vdj2kKxqFhDf4tvCU%2Bxe8o7meP6jYLJ9lWdTOQguDUPhsq%2Br51pJfLlqZKZvvHqqXXQmLYxZsPdF0NhEf7q3pYl401UhnFVYDSlHJIfJdF1Yf5%2BYwCh5x2QcMMtyOzx2q2hP9WqSFSFpumGi3G6eKjOxuSp9N082ySHD%2FhC31g%2BeCzlcNr0lIw07cr625JysKZjMmf3l%2F92lhOctE3XR2UjiecGKoEaYLMjGNi%2Bs0VgOvGmcDWmw9tqJjalooJKDLlRJzUu8SzmID0FNISuF9ERltViA1RL4dYBwg7InUqerPuNv8wtZZfuxo9y70otmzfQsbiAqMpI6pLKYB%2Frxn7HNVWHDsB47DO%2FXNC1%2Fy%2FQpZb193dcatTENt82H84O5nUkUm7kOV9g1Hm7zKw2n6GYA%2FBUdkmAIMNyT78wGOqUBzWqevMb6bo3mydzhSnqkE%2FLr9b2Qyu88%2BeEOuxuNhn4pbJxm2kLaaoqET9GY6dpep2Is7BgB3IMDDjr5esxo9qckvCAVrpmRWIpgtgXR7Hl6Hq3oXVO9rrAdes7OpCNNh1XA%2FFVQ3NA%2FC9twToGGH6sy86%2FoHOidTfLgaW87s6jLI0Cg%2B73o1c%2Fl8ABCz1tSVoATrdjUdEgK2vRHYb%2BxUaS%2Bioio&X-Amz-Signature=eaf0bbb00391be12186504a4fa6a5535f654f440a412fa19845e40e619fec92b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LPY4O6T%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDH1LpeddXvMaBN86l%2F1jyG%2BniSLJq3bypqHI%2Bh1rRVtAIgalTFdfDJl67we9Ud6lIGGQVYjq35NKeq%2FlJZ5gXbnqkqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZOY1car22JVNyABCrcA4FS0J2C3JWAbb%2FFPdG4wzIf2%2BggocUzPUMek4VNgD7%2FAtJPkQ30tMd%2B5mTSVFvTN2jg2MaqQ9hGb77ZzyD5tdJyet8bZ8uQ4g%2BmhXE%2BAMHdJP67jhmz7QY8ecNuQBBzwinIMNMjuZXxL1gLytVcrgyOinYvJSJMraHmpp264kuhOvcHOXtoHysnkuYqNJ1LGGLDlh9rshGmWhvsVAiW8rSO1dz5vdj2kKxqFhDf4tvCU%2Bxe8o7meP6jYLJ9lWdTOQguDUPhsq%2Br51pJfLlqZKZvvHqqXXQmLYxZsPdF0NhEf7q3pYl401UhnFVYDSlHJIfJdF1Yf5%2BYwCh5x2QcMMtyOzx2q2hP9WqSFSFpumGi3G6eKjOxuSp9N082ySHD%2FhC31g%2BeCzlcNr0lIw07cr625JysKZjMmf3l%2F92lhOctE3XR2UjiecGKoEaYLMjGNi%2Bs0VgOvGmcDWmw9tqJjalooJKDLlRJzUu8SzmID0FNISuF9ERltViA1RL4dYBwg7InUqerPuNv8wtZZfuxo9y70otmzfQsbiAqMpI6pLKYB%2Frxn7HNVWHDsB47DO%2FXNC1%2Fy%2FQpZb193dcatTENt82H84O5nUkUm7kOV9g1Hm7zKw2n6GYA%2FBUdkmAIMNyT78wGOqUBzWqevMb6bo3mydzhSnqkE%2FLr9b2Qyu88%2BeEOuxuNhn4pbJxm2kLaaoqET9GY6dpep2Is7BgB3IMDDjr5esxo9qckvCAVrpmRWIpgtgXR7Hl6Hq3oXVO9rrAdes7OpCNNh1XA%2FFVQ3NA%2FC9twToGGH6sy86%2FoHOidTfLgaW87s6jLI0Cg%2B73o1c%2Fl8ABCz1tSVoATrdjUdEgK2vRHYb%2BxUaS%2Bioio&X-Amz-Signature=4d4ab958f8611aa7e22edd9d2e270a17962a1a5dd2316ac178e368b77b43773d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LPY4O6T%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDH1LpeddXvMaBN86l%2F1jyG%2BniSLJq3bypqHI%2Bh1rRVtAIgalTFdfDJl67we9Ud6lIGGQVYjq35NKeq%2FlJZ5gXbnqkqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZOY1car22JVNyABCrcA4FS0J2C3JWAbb%2FFPdG4wzIf2%2BggocUzPUMek4VNgD7%2FAtJPkQ30tMd%2B5mTSVFvTN2jg2MaqQ9hGb77ZzyD5tdJyet8bZ8uQ4g%2BmhXE%2BAMHdJP67jhmz7QY8ecNuQBBzwinIMNMjuZXxL1gLytVcrgyOinYvJSJMraHmpp264kuhOvcHOXtoHysnkuYqNJ1LGGLDlh9rshGmWhvsVAiW8rSO1dz5vdj2kKxqFhDf4tvCU%2Bxe8o7meP6jYLJ9lWdTOQguDUPhsq%2Br51pJfLlqZKZvvHqqXXQmLYxZsPdF0NhEf7q3pYl401UhnFVYDSlHJIfJdF1Yf5%2BYwCh5x2QcMMtyOzx2q2hP9WqSFSFpumGi3G6eKjOxuSp9N082ySHD%2FhC31g%2BeCzlcNr0lIw07cr625JysKZjMmf3l%2F92lhOctE3XR2UjiecGKoEaYLMjGNi%2Bs0VgOvGmcDWmw9tqJjalooJKDLlRJzUu8SzmID0FNISuF9ERltViA1RL4dYBwg7InUqerPuNv8wtZZfuxo9y70otmzfQsbiAqMpI6pLKYB%2Frxn7HNVWHDsB47DO%2FXNC1%2Fy%2FQpZb193dcatTENt82H84O5nUkUm7kOV9g1Hm7zKw2n6GYA%2FBUdkmAIMNyT78wGOqUBzWqevMb6bo3mydzhSnqkE%2FLr9b2Qyu88%2BeEOuxuNhn4pbJxm2kLaaoqET9GY6dpep2Is7BgB3IMDDjr5esxo9qckvCAVrpmRWIpgtgXR7Hl6Hq3oXVO9rrAdes7OpCNNh1XA%2FFVQ3NA%2FC9twToGGH6sy86%2FoHOidTfLgaW87s6jLI0Cg%2B73o1c%2Fl8ABCz1tSVoATrdjUdEgK2vRHYb%2BxUaS%2Bioio&X-Amz-Signature=28aa9fe432e8f14a8fb1a18b1b474140a1e58ceb57cf7f70bbe3fd6f6a66c5a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LPY4O6T%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDH1LpeddXvMaBN86l%2F1jyG%2BniSLJq3bypqHI%2Bh1rRVtAIgalTFdfDJl67we9Ud6lIGGQVYjq35NKeq%2FlJZ5gXbnqkqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZOY1car22JVNyABCrcA4FS0J2C3JWAbb%2FFPdG4wzIf2%2BggocUzPUMek4VNgD7%2FAtJPkQ30tMd%2B5mTSVFvTN2jg2MaqQ9hGb77ZzyD5tdJyet8bZ8uQ4g%2BmhXE%2BAMHdJP67jhmz7QY8ecNuQBBzwinIMNMjuZXxL1gLytVcrgyOinYvJSJMraHmpp264kuhOvcHOXtoHysnkuYqNJ1LGGLDlh9rshGmWhvsVAiW8rSO1dz5vdj2kKxqFhDf4tvCU%2Bxe8o7meP6jYLJ9lWdTOQguDUPhsq%2Br51pJfLlqZKZvvHqqXXQmLYxZsPdF0NhEf7q3pYl401UhnFVYDSlHJIfJdF1Yf5%2BYwCh5x2QcMMtyOzx2q2hP9WqSFSFpumGi3G6eKjOxuSp9N082ySHD%2FhC31g%2BeCzlcNr0lIw07cr625JysKZjMmf3l%2F92lhOctE3XR2UjiecGKoEaYLMjGNi%2Bs0VgOvGmcDWmw9tqJjalooJKDLlRJzUu8SzmID0FNISuF9ERltViA1RL4dYBwg7InUqerPuNv8wtZZfuxo9y70otmzfQsbiAqMpI6pLKYB%2Frxn7HNVWHDsB47DO%2FXNC1%2Fy%2FQpZb193dcatTENt82H84O5nUkUm7kOV9g1Hm7zKw2n6GYA%2FBUdkmAIMNyT78wGOqUBzWqevMb6bo3mydzhSnqkE%2FLr9b2Qyu88%2BeEOuxuNhn4pbJxm2kLaaoqET9GY6dpep2Is7BgB3IMDDjr5esxo9qckvCAVrpmRWIpgtgXR7Hl6Hq3oXVO9rrAdes7OpCNNh1XA%2FFVQ3NA%2FC9twToGGH6sy86%2FoHOidTfLgaW87s6jLI0Cg%2B73o1c%2Fl8ABCz1tSVoATrdjUdEgK2vRHYb%2BxUaS%2Bioio&X-Amz-Signature=c5b2de7d20371464a3285a1ccedae25b27c9cf4fe1d005d8a8300d70e7bce0d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LPY4O6T%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDH1LpeddXvMaBN86l%2F1jyG%2BniSLJq3bypqHI%2Bh1rRVtAIgalTFdfDJl67we9Ud6lIGGQVYjq35NKeq%2FlJZ5gXbnqkqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZOY1car22JVNyABCrcA4FS0J2C3JWAbb%2FFPdG4wzIf2%2BggocUzPUMek4VNgD7%2FAtJPkQ30tMd%2B5mTSVFvTN2jg2MaqQ9hGb77ZzyD5tdJyet8bZ8uQ4g%2BmhXE%2BAMHdJP67jhmz7QY8ecNuQBBzwinIMNMjuZXxL1gLytVcrgyOinYvJSJMraHmpp264kuhOvcHOXtoHysnkuYqNJ1LGGLDlh9rshGmWhvsVAiW8rSO1dz5vdj2kKxqFhDf4tvCU%2Bxe8o7meP6jYLJ9lWdTOQguDUPhsq%2Br51pJfLlqZKZvvHqqXXQmLYxZsPdF0NhEf7q3pYl401UhnFVYDSlHJIfJdF1Yf5%2BYwCh5x2QcMMtyOzx2q2hP9WqSFSFpumGi3G6eKjOxuSp9N082ySHD%2FhC31g%2BeCzlcNr0lIw07cr625JysKZjMmf3l%2F92lhOctE3XR2UjiecGKoEaYLMjGNi%2Bs0VgOvGmcDWmw9tqJjalooJKDLlRJzUu8SzmID0FNISuF9ERltViA1RL4dYBwg7InUqerPuNv8wtZZfuxo9y70otmzfQsbiAqMpI6pLKYB%2Frxn7HNVWHDsB47DO%2FXNC1%2Fy%2FQpZb193dcatTENt82H84O5nUkUm7kOV9g1Hm7zKw2n6GYA%2FBUdkmAIMNyT78wGOqUBzWqevMb6bo3mydzhSnqkE%2FLr9b2Qyu88%2BeEOuxuNhn4pbJxm2kLaaoqET9GY6dpep2Is7BgB3IMDDjr5esxo9qckvCAVrpmRWIpgtgXR7Hl6Hq3oXVO9rrAdes7OpCNNh1XA%2FFVQ3NA%2FC9twToGGH6sy86%2FoHOidTfLgaW87s6jLI0Cg%2B73o1c%2Fl8ABCz1tSVoATrdjUdEgK2vRHYb%2BxUaS%2Bioio&X-Amz-Signature=e3af39326c4358f52df2dac091e8c69193fe7051d6f77fa319d2d941364dcb14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LPY4O6T%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDH1LpeddXvMaBN86l%2F1jyG%2BniSLJq3bypqHI%2Bh1rRVtAIgalTFdfDJl67we9Ud6lIGGQVYjq35NKeq%2FlJZ5gXbnqkqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZOY1car22JVNyABCrcA4FS0J2C3JWAbb%2FFPdG4wzIf2%2BggocUzPUMek4VNgD7%2FAtJPkQ30tMd%2B5mTSVFvTN2jg2MaqQ9hGb77ZzyD5tdJyet8bZ8uQ4g%2BmhXE%2BAMHdJP67jhmz7QY8ecNuQBBzwinIMNMjuZXxL1gLytVcrgyOinYvJSJMraHmpp264kuhOvcHOXtoHysnkuYqNJ1LGGLDlh9rshGmWhvsVAiW8rSO1dz5vdj2kKxqFhDf4tvCU%2Bxe8o7meP6jYLJ9lWdTOQguDUPhsq%2Br51pJfLlqZKZvvHqqXXQmLYxZsPdF0NhEf7q3pYl401UhnFVYDSlHJIfJdF1Yf5%2BYwCh5x2QcMMtyOzx2q2hP9WqSFSFpumGi3G6eKjOxuSp9N082ySHD%2FhC31g%2BeCzlcNr0lIw07cr625JysKZjMmf3l%2F92lhOctE3XR2UjiecGKoEaYLMjGNi%2Bs0VgOvGmcDWmw9tqJjalooJKDLlRJzUu8SzmID0FNISuF9ERltViA1RL4dYBwg7InUqerPuNv8wtZZfuxo9y70otmzfQsbiAqMpI6pLKYB%2Frxn7HNVWHDsB47DO%2FXNC1%2Fy%2FQpZb193dcatTENt82H84O5nUkUm7kOV9g1Hm7zKw2n6GYA%2FBUdkmAIMNyT78wGOqUBzWqevMb6bo3mydzhSnqkE%2FLr9b2Qyu88%2BeEOuxuNhn4pbJxm2kLaaoqET9GY6dpep2Is7BgB3IMDDjr5esxo9qckvCAVrpmRWIpgtgXR7Hl6Hq3oXVO9rrAdes7OpCNNh1XA%2FFVQ3NA%2FC9twToGGH6sy86%2FoHOidTfLgaW87s6jLI0Cg%2B73o1c%2Fl8ABCz1tSVoATrdjUdEgK2vRHYb%2BxUaS%2Bioio&X-Amz-Signature=0a1557368ce83cb170ba4e6697652306dd319e22300bd00c916d513bbee8d203&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LPY4O6T%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDH1LpeddXvMaBN86l%2F1jyG%2BniSLJq3bypqHI%2Bh1rRVtAIgalTFdfDJl67we9Ud6lIGGQVYjq35NKeq%2FlJZ5gXbnqkqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZOY1car22JVNyABCrcA4FS0J2C3JWAbb%2FFPdG4wzIf2%2BggocUzPUMek4VNgD7%2FAtJPkQ30tMd%2B5mTSVFvTN2jg2MaqQ9hGb77ZzyD5tdJyet8bZ8uQ4g%2BmhXE%2BAMHdJP67jhmz7QY8ecNuQBBzwinIMNMjuZXxL1gLytVcrgyOinYvJSJMraHmpp264kuhOvcHOXtoHysnkuYqNJ1LGGLDlh9rshGmWhvsVAiW8rSO1dz5vdj2kKxqFhDf4tvCU%2Bxe8o7meP6jYLJ9lWdTOQguDUPhsq%2Br51pJfLlqZKZvvHqqXXQmLYxZsPdF0NhEf7q3pYl401UhnFVYDSlHJIfJdF1Yf5%2BYwCh5x2QcMMtyOzx2q2hP9WqSFSFpumGi3G6eKjOxuSp9N082ySHD%2FhC31g%2BeCzlcNr0lIw07cr625JysKZjMmf3l%2F92lhOctE3XR2UjiecGKoEaYLMjGNi%2Bs0VgOvGmcDWmw9tqJjalooJKDLlRJzUu8SzmID0FNISuF9ERltViA1RL4dYBwg7InUqerPuNv8wtZZfuxo9y70otmzfQsbiAqMpI6pLKYB%2Frxn7HNVWHDsB47DO%2FXNC1%2Fy%2FQpZb193dcatTENt82H84O5nUkUm7kOV9g1Hm7zKw2n6GYA%2FBUdkmAIMNyT78wGOqUBzWqevMb6bo3mydzhSnqkE%2FLr9b2Qyu88%2BeEOuxuNhn4pbJxm2kLaaoqET9GY6dpep2Is7BgB3IMDDjr5esxo9qckvCAVrpmRWIpgtgXR7Hl6Hq3oXVO9rrAdes7OpCNNh1XA%2FFVQ3NA%2FC9twToGGH6sy86%2FoHOidTfLgaW87s6jLI0Cg%2B73o1c%2Fl8ABCz1tSVoATrdjUdEgK2vRHYb%2BxUaS%2Bioio&X-Amz-Signature=c159527ec296f2b324901bed44028e992a1077c5c9410e170ecf2d47d30902a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LPY4O6T%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDH1LpeddXvMaBN86l%2F1jyG%2BniSLJq3bypqHI%2Bh1rRVtAIgalTFdfDJl67we9Ud6lIGGQVYjq35NKeq%2FlJZ5gXbnqkqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFZOY1car22JVNyABCrcA4FS0J2C3JWAbb%2FFPdG4wzIf2%2BggocUzPUMek4VNgD7%2FAtJPkQ30tMd%2B5mTSVFvTN2jg2MaqQ9hGb77ZzyD5tdJyet8bZ8uQ4g%2BmhXE%2BAMHdJP67jhmz7QY8ecNuQBBzwinIMNMjuZXxL1gLytVcrgyOinYvJSJMraHmpp264kuhOvcHOXtoHysnkuYqNJ1LGGLDlh9rshGmWhvsVAiW8rSO1dz5vdj2kKxqFhDf4tvCU%2Bxe8o7meP6jYLJ9lWdTOQguDUPhsq%2Br51pJfLlqZKZvvHqqXXQmLYxZsPdF0NhEf7q3pYl401UhnFVYDSlHJIfJdF1Yf5%2BYwCh5x2QcMMtyOzx2q2hP9WqSFSFpumGi3G6eKjOxuSp9N082ySHD%2FhC31g%2BeCzlcNr0lIw07cr625JysKZjMmf3l%2F92lhOctE3XR2UjiecGKoEaYLMjGNi%2Bs0VgOvGmcDWmw9tqJjalooJKDLlRJzUu8SzmID0FNISuF9ERltViA1RL4dYBwg7InUqerPuNv8wtZZfuxo9y70otmzfQsbiAqMpI6pLKYB%2Frxn7HNVWHDsB47DO%2FXNC1%2Fy%2FQpZb193dcatTENt82H84O5nUkUm7kOV9g1Hm7zKw2n6GYA%2FBUdkmAIMNyT78wGOqUBzWqevMb6bo3mydzhSnqkE%2FLr9b2Qyu88%2BeEOuxuNhn4pbJxm2kLaaoqET9GY6dpep2Is7BgB3IMDDjr5esxo9qckvCAVrpmRWIpgtgXR7Hl6Hq3oXVO9rrAdes7OpCNNh1XA%2FFVQ3NA%2FC9twToGGH6sy86%2FoHOidTfLgaW87s6jLI0Cg%2B73o1c%2Fl8ABCz1tSVoATrdjUdEgK2vRHYb%2BxUaS%2Bioio&X-Amz-Signature=7dda57210ddb035ff91dd5800bda62afb70d4254fc72103c427bbb7aa23ff3ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

