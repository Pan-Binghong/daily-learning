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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWZYHML%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUd%2B3SkPOMlpMerqEFGlkfToRh9GkI2yqtoiusF1UbqAiB4T3qFTK3zaMZtIhh2xbMyQW81IQ2aePOPB8GAAL6PZCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrU5q811NqOxeX9PpKtwDhDwye5BlW2x6Rbh8DNdXysPa6RXf3y2V2Ht%2Fsuco9sQ01QpJ5JR5KL00Nd8E3o3d7Cnj%2BgyD0mpxVRFzHrIq5Sf4W8Q907KfrL%2FAvSbY2kmGq7gdieuCiW%2Fa6MNLtJIAizQY%2Baoxua2nUN49KcaDfI028xHLgI1iPGKgPOOKKPmYi6zvJ6o4zPB7OgRFJNnhrZQESsrIW9tAz39FK212qJ2Qb0m5bRJoL88mBXbr9hcvvok7XMsfAwobRSR9WeVywWruLiQJ6hpQufxreu7rNSR%2FiQ7kGpTU4y6tRaFAO60M5jiBODdH%2BZJVp5rx4e70F13J%2FPd6h6JfIcG4TKIH5zQpuyJdpXVfKHF3sbsq9EIVtehDhhY20CC1I8gGK8XLKuljag3527GLIU6%2Fwt7bbHcfnQPzM1ql1koNkoVMjmckbcAntjPph%2Btvg%2B216XoZfFOBGgElUd88TOtVt6cxAc6bKezFEhPtjZecxvVL6esHOYZn8oS%2FuI81akd4ReOp1VDz1B1pAnJ1Y80SPHBOyFaIeAil%2F2VT0D29cuiubIVujkV77HpR6nvkTjlUS0IfwlXQvJfT617hL3340ymQsCVeBUSe%2FSl8OUVTwoTHEAbywd%2FxAlKrO8aXM%2Fcw4%2B%2FYyQY6pgEZv39fepMOWkgnM%2F1lm44tqct8AdsLvClbPlWCscpaq9XpVad501EiISzmhdueC%2FjvG9ymOfuH4yDMnXX6G2CXWspgzwli9bg1DIuhG%2FAzhrAsAve0mRoQG%2F6FOeE%2FoGJDzWP%2BI8aKPlP7iNrxQjMhOe8iTADcruHTchF96XD8RhTkrGTAkk6K1GvcGyPFa9ATXg7l%2Bs2rXhsdy7OPAvRWdCN1cZzz&X-Amz-Signature=c8fe8af408322ef4f51f7956dcbfcc8c5c9f1369fe06d975117ac77e818892a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWZYHML%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUd%2B3SkPOMlpMerqEFGlkfToRh9GkI2yqtoiusF1UbqAiB4T3qFTK3zaMZtIhh2xbMyQW81IQ2aePOPB8GAAL6PZCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrU5q811NqOxeX9PpKtwDhDwye5BlW2x6Rbh8DNdXysPa6RXf3y2V2Ht%2Fsuco9sQ01QpJ5JR5KL00Nd8E3o3d7Cnj%2BgyD0mpxVRFzHrIq5Sf4W8Q907KfrL%2FAvSbY2kmGq7gdieuCiW%2Fa6MNLtJIAizQY%2Baoxua2nUN49KcaDfI028xHLgI1iPGKgPOOKKPmYi6zvJ6o4zPB7OgRFJNnhrZQESsrIW9tAz39FK212qJ2Qb0m5bRJoL88mBXbr9hcvvok7XMsfAwobRSR9WeVywWruLiQJ6hpQufxreu7rNSR%2FiQ7kGpTU4y6tRaFAO60M5jiBODdH%2BZJVp5rx4e70F13J%2FPd6h6JfIcG4TKIH5zQpuyJdpXVfKHF3sbsq9EIVtehDhhY20CC1I8gGK8XLKuljag3527GLIU6%2Fwt7bbHcfnQPzM1ql1koNkoVMjmckbcAntjPph%2Btvg%2B216XoZfFOBGgElUd88TOtVt6cxAc6bKezFEhPtjZecxvVL6esHOYZn8oS%2FuI81akd4ReOp1VDz1B1pAnJ1Y80SPHBOyFaIeAil%2F2VT0D29cuiubIVujkV77HpR6nvkTjlUS0IfwlXQvJfT617hL3340ymQsCVeBUSe%2FSl8OUVTwoTHEAbywd%2FxAlKrO8aXM%2Fcw4%2B%2FYyQY6pgEZv39fepMOWkgnM%2F1lm44tqct8AdsLvClbPlWCscpaq9XpVad501EiISzmhdueC%2FjvG9ymOfuH4yDMnXX6G2CXWspgzwli9bg1DIuhG%2FAzhrAsAve0mRoQG%2F6FOeE%2FoGJDzWP%2BI8aKPlP7iNrxQjMhOe8iTADcruHTchF96XD8RhTkrGTAkk6K1GvcGyPFa9ATXg7l%2Bs2rXhsdy7OPAvRWdCN1cZzz&X-Amz-Signature=1fc497c36e9141c6dbbc26941a7ec66adfa0aede25e3e3086b9f98efa3e35b6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWZYHML%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUd%2B3SkPOMlpMerqEFGlkfToRh9GkI2yqtoiusF1UbqAiB4T3qFTK3zaMZtIhh2xbMyQW81IQ2aePOPB8GAAL6PZCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrU5q811NqOxeX9PpKtwDhDwye5BlW2x6Rbh8DNdXysPa6RXf3y2V2Ht%2Fsuco9sQ01QpJ5JR5KL00Nd8E3o3d7Cnj%2BgyD0mpxVRFzHrIq5Sf4W8Q907KfrL%2FAvSbY2kmGq7gdieuCiW%2Fa6MNLtJIAizQY%2Baoxua2nUN49KcaDfI028xHLgI1iPGKgPOOKKPmYi6zvJ6o4zPB7OgRFJNnhrZQESsrIW9tAz39FK212qJ2Qb0m5bRJoL88mBXbr9hcvvok7XMsfAwobRSR9WeVywWruLiQJ6hpQufxreu7rNSR%2FiQ7kGpTU4y6tRaFAO60M5jiBODdH%2BZJVp5rx4e70F13J%2FPd6h6JfIcG4TKIH5zQpuyJdpXVfKHF3sbsq9EIVtehDhhY20CC1I8gGK8XLKuljag3527GLIU6%2Fwt7bbHcfnQPzM1ql1koNkoVMjmckbcAntjPph%2Btvg%2B216XoZfFOBGgElUd88TOtVt6cxAc6bKezFEhPtjZecxvVL6esHOYZn8oS%2FuI81akd4ReOp1VDz1B1pAnJ1Y80SPHBOyFaIeAil%2F2VT0D29cuiubIVujkV77HpR6nvkTjlUS0IfwlXQvJfT617hL3340ymQsCVeBUSe%2FSl8OUVTwoTHEAbywd%2FxAlKrO8aXM%2Fcw4%2B%2FYyQY6pgEZv39fepMOWkgnM%2F1lm44tqct8AdsLvClbPlWCscpaq9XpVad501EiISzmhdueC%2FjvG9ymOfuH4yDMnXX6G2CXWspgzwli9bg1DIuhG%2FAzhrAsAve0mRoQG%2F6FOeE%2FoGJDzWP%2BI8aKPlP7iNrxQjMhOe8iTADcruHTchF96XD8RhTkrGTAkk6K1GvcGyPFa9ATXg7l%2Bs2rXhsdy7OPAvRWdCN1cZzz&X-Amz-Signature=9c162bc7625491744c170f6bb173135cbeaf035ddc850bb8b6dc3df936a81f0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWZYHML%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUd%2B3SkPOMlpMerqEFGlkfToRh9GkI2yqtoiusF1UbqAiB4T3qFTK3zaMZtIhh2xbMyQW81IQ2aePOPB8GAAL6PZCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrU5q811NqOxeX9PpKtwDhDwye5BlW2x6Rbh8DNdXysPa6RXf3y2V2Ht%2Fsuco9sQ01QpJ5JR5KL00Nd8E3o3d7Cnj%2BgyD0mpxVRFzHrIq5Sf4W8Q907KfrL%2FAvSbY2kmGq7gdieuCiW%2Fa6MNLtJIAizQY%2Baoxua2nUN49KcaDfI028xHLgI1iPGKgPOOKKPmYi6zvJ6o4zPB7OgRFJNnhrZQESsrIW9tAz39FK212qJ2Qb0m5bRJoL88mBXbr9hcvvok7XMsfAwobRSR9WeVywWruLiQJ6hpQufxreu7rNSR%2FiQ7kGpTU4y6tRaFAO60M5jiBODdH%2BZJVp5rx4e70F13J%2FPd6h6JfIcG4TKIH5zQpuyJdpXVfKHF3sbsq9EIVtehDhhY20CC1I8gGK8XLKuljag3527GLIU6%2Fwt7bbHcfnQPzM1ql1koNkoVMjmckbcAntjPph%2Btvg%2B216XoZfFOBGgElUd88TOtVt6cxAc6bKezFEhPtjZecxvVL6esHOYZn8oS%2FuI81akd4ReOp1VDz1B1pAnJ1Y80SPHBOyFaIeAil%2F2VT0D29cuiubIVujkV77HpR6nvkTjlUS0IfwlXQvJfT617hL3340ymQsCVeBUSe%2FSl8OUVTwoTHEAbywd%2FxAlKrO8aXM%2Fcw4%2B%2FYyQY6pgEZv39fepMOWkgnM%2F1lm44tqct8AdsLvClbPlWCscpaq9XpVad501EiISzmhdueC%2FjvG9ymOfuH4yDMnXX6G2CXWspgzwli9bg1DIuhG%2FAzhrAsAve0mRoQG%2F6FOeE%2FoGJDzWP%2BI8aKPlP7iNrxQjMhOe8iTADcruHTchF96XD8RhTkrGTAkk6K1GvcGyPFa9ATXg7l%2Bs2rXhsdy7OPAvRWdCN1cZzz&X-Amz-Signature=27b8c303ba3b6686395228a07d98afaf05c4104fab2c8454ef93ffc01a1f3803&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWZYHML%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUd%2B3SkPOMlpMerqEFGlkfToRh9GkI2yqtoiusF1UbqAiB4T3qFTK3zaMZtIhh2xbMyQW81IQ2aePOPB8GAAL6PZCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrU5q811NqOxeX9PpKtwDhDwye5BlW2x6Rbh8DNdXysPa6RXf3y2V2Ht%2Fsuco9sQ01QpJ5JR5KL00Nd8E3o3d7Cnj%2BgyD0mpxVRFzHrIq5Sf4W8Q907KfrL%2FAvSbY2kmGq7gdieuCiW%2Fa6MNLtJIAizQY%2Baoxua2nUN49KcaDfI028xHLgI1iPGKgPOOKKPmYi6zvJ6o4zPB7OgRFJNnhrZQESsrIW9tAz39FK212qJ2Qb0m5bRJoL88mBXbr9hcvvok7XMsfAwobRSR9WeVywWruLiQJ6hpQufxreu7rNSR%2FiQ7kGpTU4y6tRaFAO60M5jiBODdH%2BZJVp5rx4e70F13J%2FPd6h6JfIcG4TKIH5zQpuyJdpXVfKHF3sbsq9EIVtehDhhY20CC1I8gGK8XLKuljag3527GLIU6%2Fwt7bbHcfnQPzM1ql1koNkoVMjmckbcAntjPph%2Btvg%2B216XoZfFOBGgElUd88TOtVt6cxAc6bKezFEhPtjZecxvVL6esHOYZn8oS%2FuI81akd4ReOp1VDz1B1pAnJ1Y80SPHBOyFaIeAil%2F2VT0D29cuiubIVujkV77HpR6nvkTjlUS0IfwlXQvJfT617hL3340ymQsCVeBUSe%2FSl8OUVTwoTHEAbywd%2FxAlKrO8aXM%2Fcw4%2B%2FYyQY6pgEZv39fepMOWkgnM%2F1lm44tqct8AdsLvClbPlWCscpaq9XpVad501EiISzmhdueC%2FjvG9ymOfuH4yDMnXX6G2CXWspgzwli9bg1DIuhG%2FAzhrAsAve0mRoQG%2F6FOeE%2FoGJDzWP%2BI8aKPlP7iNrxQjMhOe8iTADcruHTchF96XD8RhTkrGTAkk6K1GvcGyPFa9ATXg7l%2Bs2rXhsdy7OPAvRWdCN1cZzz&X-Amz-Signature=f1b1f5e8f64df8b4dab1a05328e3dd004a5e698038d271f127b16ef5cb6c3d1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWZYHML%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUd%2B3SkPOMlpMerqEFGlkfToRh9GkI2yqtoiusF1UbqAiB4T3qFTK3zaMZtIhh2xbMyQW81IQ2aePOPB8GAAL6PZCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrU5q811NqOxeX9PpKtwDhDwye5BlW2x6Rbh8DNdXysPa6RXf3y2V2Ht%2Fsuco9sQ01QpJ5JR5KL00Nd8E3o3d7Cnj%2BgyD0mpxVRFzHrIq5Sf4W8Q907KfrL%2FAvSbY2kmGq7gdieuCiW%2Fa6MNLtJIAizQY%2Baoxua2nUN49KcaDfI028xHLgI1iPGKgPOOKKPmYi6zvJ6o4zPB7OgRFJNnhrZQESsrIW9tAz39FK212qJ2Qb0m5bRJoL88mBXbr9hcvvok7XMsfAwobRSR9WeVywWruLiQJ6hpQufxreu7rNSR%2FiQ7kGpTU4y6tRaFAO60M5jiBODdH%2BZJVp5rx4e70F13J%2FPd6h6JfIcG4TKIH5zQpuyJdpXVfKHF3sbsq9EIVtehDhhY20CC1I8gGK8XLKuljag3527GLIU6%2Fwt7bbHcfnQPzM1ql1koNkoVMjmckbcAntjPph%2Btvg%2B216XoZfFOBGgElUd88TOtVt6cxAc6bKezFEhPtjZecxvVL6esHOYZn8oS%2FuI81akd4ReOp1VDz1B1pAnJ1Y80SPHBOyFaIeAil%2F2VT0D29cuiubIVujkV77HpR6nvkTjlUS0IfwlXQvJfT617hL3340ymQsCVeBUSe%2FSl8OUVTwoTHEAbywd%2FxAlKrO8aXM%2Fcw4%2B%2FYyQY6pgEZv39fepMOWkgnM%2F1lm44tqct8AdsLvClbPlWCscpaq9XpVad501EiISzmhdueC%2FjvG9ymOfuH4yDMnXX6G2CXWspgzwli9bg1DIuhG%2FAzhrAsAve0mRoQG%2F6FOeE%2FoGJDzWP%2BI8aKPlP7iNrxQjMhOe8iTADcruHTchF96XD8RhTkrGTAkk6K1GvcGyPFa9ATXg7l%2Bs2rXhsdy7OPAvRWdCN1cZzz&X-Amz-Signature=9844ead31913c44c71b5174c705cf56ca5491dad8e36500ae1ad927ade2ae9d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWZYHML%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUd%2B3SkPOMlpMerqEFGlkfToRh9GkI2yqtoiusF1UbqAiB4T3qFTK3zaMZtIhh2xbMyQW81IQ2aePOPB8GAAL6PZCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrU5q811NqOxeX9PpKtwDhDwye5BlW2x6Rbh8DNdXysPa6RXf3y2V2Ht%2Fsuco9sQ01QpJ5JR5KL00Nd8E3o3d7Cnj%2BgyD0mpxVRFzHrIq5Sf4W8Q907KfrL%2FAvSbY2kmGq7gdieuCiW%2Fa6MNLtJIAizQY%2Baoxua2nUN49KcaDfI028xHLgI1iPGKgPOOKKPmYi6zvJ6o4zPB7OgRFJNnhrZQESsrIW9tAz39FK212qJ2Qb0m5bRJoL88mBXbr9hcvvok7XMsfAwobRSR9WeVywWruLiQJ6hpQufxreu7rNSR%2FiQ7kGpTU4y6tRaFAO60M5jiBODdH%2BZJVp5rx4e70F13J%2FPd6h6JfIcG4TKIH5zQpuyJdpXVfKHF3sbsq9EIVtehDhhY20CC1I8gGK8XLKuljag3527GLIU6%2Fwt7bbHcfnQPzM1ql1koNkoVMjmckbcAntjPph%2Btvg%2B216XoZfFOBGgElUd88TOtVt6cxAc6bKezFEhPtjZecxvVL6esHOYZn8oS%2FuI81akd4ReOp1VDz1B1pAnJ1Y80SPHBOyFaIeAil%2F2VT0D29cuiubIVujkV77HpR6nvkTjlUS0IfwlXQvJfT617hL3340ymQsCVeBUSe%2FSl8OUVTwoTHEAbywd%2FxAlKrO8aXM%2Fcw4%2B%2FYyQY6pgEZv39fepMOWkgnM%2F1lm44tqct8AdsLvClbPlWCscpaq9XpVad501EiISzmhdueC%2FjvG9ymOfuH4yDMnXX6G2CXWspgzwli9bg1DIuhG%2FAzhrAsAve0mRoQG%2F6FOeE%2FoGJDzWP%2BI8aKPlP7iNrxQjMhOe8iTADcruHTchF96XD8RhTkrGTAkk6K1GvcGyPFa9ATXg7l%2Bs2rXhsdy7OPAvRWdCN1cZzz&X-Amz-Signature=fd4701486c0d292e07b0e33d01e71cb3ff282e852f294275870a9158ef97ee98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWZYHML%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUd%2B3SkPOMlpMerqEFGlkfToRh9GkI2yqtoiusF1UbqAiB4T3qFTK3zaMZtIhh2xbMyQW81IQ2aePOPB8GAAL6PZCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrU5q811NqOxeX9PpKtwDhDwye5BlW2x6Rbh8DNdXysPa6RXf3y2V2Ht%2Fsuco9sQ01QpJ5JR5KL00Nd8E3o3d7Cnj%2BgyD0mpxVRFzHrIq5Sf4W8Q907KfrL%2FAvSbY2kmGq7gdieuCiW%2Fa6MNLtJIAizQY%2Baoxua2nUN49KcaDfI028xHLgI1iPGKgPOOKKPmYi6zvJ6o4zPB7OgRFJNnhrZQESsrIW9tAz39FK212qJ2Qb0m5bRJoL88mBXbr9hcvvok7XMsfAwobRSR9WeVywWruLiQJ6hpQufxreu7rNSR%2FiQ7kGpTU4y6tRaFAO60M5jiBODdH%2BZJVp5rx4e70F13J%2FPd6h6JfIcG4TKIH5zQpuyJdpXVfKHF3sbsq9EIVtehDhhY20CC1I8gGK8XLKuljag3527GLIU6%2Fwt7bbHcfnQPzM1ql1koNkoVMjmckbcAntjPph%2Btvg%2B216XoZfFOBGgElUd88TOtVt6cxAc6bKezFEhPtjZecxvVL6esHOYZn8oS%2FuI81akd4ReOp1VDz1B1pAnJ1Y80SPHBOyFaIeAil%2F2VT0D29cuiubIVujkV77HpR6nvkTjlUS0IfwlXQvJfT617hL3340ymQsCVeBUSe%2FSl8OUVTwoTHEAbywd%2FxAlKrO8aXM%2Fcw4%2B%2FYyQY6pgEZv39fepMOWkgnM%2F1lm44tqct8AdsLvClbPlWCscpaq9XpVad501EiISzmhdueC%2FjvG9ymOfuH4yDMnXX6G2CXWspgzwli9bg1DIuhG%2FAzhrAsAve0mRoQG%2F6FOeE%2FoGJDzWP%2BI8aKPlP7iNrxQjMhOe8iTADcruHTchF96XD8RhTkrGTAkk6K1GvcGyPFa9ATXg7l%2Bs2rXhsdy7OPAvRWdCN1cZzz&X-Amz-Signature=ad804dbf9daa46d1f44d5cb976588ad9f45334d617bda4a99f4a2221188264de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWZYHML%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUd%2B3SkPOMlpMerqEFGlkfToRh9GkI2yqtoiusF1UbqAiB4T3qFTK3zaMZtIhh2xbMyQW81IQ2aePOPB8GAAL6PZCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrU5q811NqOxeX9PpKtwDhDwye5BlW2x6Rbh8DNdXysPa6RXf3y2V2Ht%2Fsuco9sQ01QpJ5JR5KL00Nd8E3o3d7Cnj%2BgyD0mpxVRFzHrIq5Sf4W8Q907KfrL%2FAvSbY2kmGq7gdieuCiW%2Fa6MNLtJIAizQY%2Baoxua2nUN49KcaDfI028xHLgI1iPGKgPOOKKPmYi6zvJ6o4zPB7OgRFJNnhrZQESsrIW9tAz39FK212qJ2Qb0m5bRJoL88mBXbr9hcvvok7XMsfAwobRSR9WeVywWruLiQJ6hpQufxreu7rNSR%2FiQ7kGpTU4y6tRaFAO60M5jiBODdH%2BZJVp5rx4e70F13J%2FPd6h6JfIcG4TKIH5zQpuyJdpXVfKHF3sbsq9EIVtehDhhY20CC1I8gGK8XLKuljag3527GLIU6%2Fwt7bbHcfnQPzM1ql1koNkoVMjmckbcAntjPph%2Btvg%2B216XoZfFOBGgElUd88TOtVt6cxAc6bKezFEhPtjZecxvVL6esHOYZn8oS%2FuI81akd4ReOp1VDz1B1pAnJ1Y80SPHBOyFaIeAil%2F2VT0D29cuiubIVujkV77HpR6nvkTjlUS0IfwlXQvJfT617hL3340ymQsCVeBUSe%2FSl8OUVTwoTHEAbywd%2FxAlKrO8aXM%2Fcw4%2B%2FYyQY6pgEZv39fepMOWkgnM%2F1lm44tqct8AdsLvClbPlWCscpaq9XpVad501EiISzmhdueC%2FjvG9ymOfuH4yDMnXX6G2CXWspgzwli9bg1DIuhG%2FAzhrAsAve0mRoQG%2F6FOeE%2FoGJDzWP%2BI8aKPlP7iNrxQjMhOe8iTADcruHTchF96XD8RhTkrGTAkk6K1GvcGyPFa9ATXg7l%2Bs2rXhsdy7OPAvRWdCN1cZzz&X-Amz-Signature=8691406d6c3bb26df4e73303c555ac6afe815d7e50714178ff77f96fc188f1aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWZYHML%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUd%2B3SkPOMlpMerqEFGlkfToRh9GkI2yqtoiusF1UbqAiB4T3qFTK3zaMZtIhh2xbMyQW81IQ2aePOPB8GAAL6PZCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrU5q811NqOxeX9PpKtwDhDwye5BlW2x6Rbh8DNdXysPa6RXf3y2V2Ht%2Fsuco9sQ01QpJ5JR5KL00Nd8E3o3d7Cnj%2BgyD0mpxVRFzHrIq5Sf4W8Q907KfrL%2FAvSbY2kmGq7gdieuCiW%2Fa6MNLtJIAizQY%2Baoxua2nUN49KcaDfI028xHLgI1iPGKgPOOKKPmYi6zvJ6o4zPB7OgRFJNnhrZQESsrIW9tAz39FK212qJ2Qb0m5bRJoL88mBXbr9hcvvok7XMsfAwobRSR9WeVywWruLiQJ6hpQufxreu7rNSR%2FiQ7kGpTU4y6tRaFAO60M5jiBODdH%2BZJVp5rx4e70F13J%2FPd6h6JfIcG4TKIH5zQpuyJdpXVfKHF3sbsq9EIVtehDhhY20CC1I8gGK8XLKuljag3527GLIU6%2Fwt7bbHcfnQPzM1ql1koNkoVMjmckbcAntjPph%2Btvg%2B216XoZfFOBGgElUd88TOtVt6cxAc6bKezFEhPtjZecxvVL6esHOYZn8oS%2FuI81akd4ReOp1VDz1B1pAnJ1Y80SPHBOyFaIeAil%2F2VT0D29cuiubIVujkV77HpR6nvkTjlUS0IfwlXQvJfT617hL3340ymQsCVeBUSe%2FSl8OUVTwoTHEAbywd%2FxAlKrO8aXM%2Fcw4%2B%2FYyQY6pgEZv39fepMOWkgnM%2F1lm44tqct8AdsLvClbPlWCscpaq9XpVad501EiISzmhdueC%2FjvG9ymOfuH4yDMnXX6G2CXWspgzwli9bg1DIuhG%2FAzhrAsAve0mRoQG%2F6FOeE%2FoGJDzWP%2BI8aKPlP7iNrxQjMhOe8iTADcruHTchF96XD8RhTkrGTAkk6K1GvcGyPFa9ATXg7l%2Bs2rXhsdy7OPAvRWdCN1cZzz&X-Amz-Signature=140012e30e50960864d9cdea85222d012a0e1b66529475a496832aaec4f1fbc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

