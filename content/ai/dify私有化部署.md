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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GYSGHD7%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCaV%2BoP6Z8WQpUGsP8ZTB9m1hlPLTMWkMFQOhB%2Fv6fwzgIgOEIAu%2BhWMHv0SG6x3pHvYOSdKGvT%2BkSVNPqNHKzfl78q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDHUWct%2FelulWprH%2B2CrcA88AMNw84o8lIimdEbIPvAd0YCBijM%2Fp7Xz77M9xQ4z9nR%2FOjD4XBpyQlGNGRRfJHjNzoaQxa5sljoVK6BMQNGKErR9Tm9%2B8rw6AbS41Wa1o7TD0BaG5h5d%2FRHJqsbvOtGu9xJUE8Col6S7X7wkMIiMI5y8iZyJvS24wkPAdhfOzvGXM0OiXQT4wgb2uXAAAHsdZwDvgrFybAFMqoKNQovTIyk2H0vXOZvGWnhfYILlOGyQeogRGwVQYUASwpQeQ%2F4eDIWG5NfKfdWt1dp0IvyciMXHOG84XX3ee6KqxeJq3gK6%2BbqsQ0i9sc%2FDh%2BB7E1SW222V9ufYGYMfW40A8HgC1n2HvqcQ54nb%2FfCFInkHaw0E8co1yJEtiZoN0exN6N6nz7eNSfiqkyP64Yp3WYdpWaj1WdIEhkQi7TNsfV8cjpVK41ad5RAOZ5ATSbNNarZcXJo8fPNFYoDzVRRSo4Nv1ar4O8GuxeIpRAmiHJDLbyq2yi%2FemtIJyV0o6DJr2ka%2FtD3z1dZWO17wOrqIENR0fC50Smr8ETjXpKlR99IS7u9qs3ldSM5w6dKPKu0xRjU%2FyJyCwKDCsPub8hq52GSu0fsA3Cni3fj%2BEfZf6ESEQCpehaOW33ZCE%2F%2F5DMMnb%2FMkGOqUBWTE20PwjqEi9WeCCBEyAXCL5Pa9Qb4Kiyot12hXy78kTGfyTU5Vg6I04ZAHctSTjy%2FoQ8jUz9nhTdYOyJKohr3D01cHrbiu5dFrw%2Bu7as%2Bdvb1%2BkxFMbf7yI%2BmsHX8d8W8snTBhC5geKpKRC2X853l%2BHgUyP4f2jwVqUST97bU%2F9C2H8e20KSmj4RDgRIK9961lKw6PytTJGpkIH2zgNSTpuE%2FHN&X-Amz-Signature=aecfdf6f212e5fa613247e711d3685e5259b4aff6a8902c186a0fef19814e659&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GYSGHD7%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCaV%2BoP6Z8WQpUGsP8ZTB9m1hlPLTMWkMFQOhB%2Fv6fwzgIgOEIAu%2BhWMHv0SG6x3pHvYOSdKGvT%2BkSVNPqNHKzfl78q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDHUWct%2FelulWprH%2B2CrcA88AMNw84o8lIimdEbIPvAd0YCBijM%2Fp7Xz77M9xQ4z9nR%2FOjD4XBpyQlGNGRRfJHjNzoaQxa5sljoVK6BMQNGKErR9Tm9%2B8rw6AbS41Wa1o7TD0BaG5h5d%2FRHJqsbvOtGu9xJUE8Col6S7X7wkMIiMI5y8iZyJvS24wkPAdhfOzvGXM0OiXQT4wgb2uXAAAHsdZwDvgrFybAFMqoKNQovTIyk2H0vXOZvGWnhfYILlOGyQeogRGwVQYUASwpQeQ%2F4eDIWG5NfKfdWt1dp0IvyciMXHOG84XX3ee6KqxeJq3gK6%2BbqsQ0i9sc%2FDh%2BB7E1SW222V9ufYGYMfW40A8HgC1n2HvqcQ54nb%2FfCFInkHaw0E8co1yJEtiZoN0exN6N6nz7eNSfiqkyP64Yp3WYdpWaj1WdIEhkQi7TNsfV8cjpVK41ad5RAOZ5ATSbNNarZcXJo8fPNFYoDzVRRSo4Nv1ar4O8GuxeIpRAmiHJDLbyq2yi%2FemtIJyV0o6DJr2ka%2FtD3z1dZWO17wOrqIENR0fC50Smr8ETjXpKlR99IS7u9qs3ldSM5w6dKPKu0xRjU%2FyJyCwKDCsPub8hq52GSu0fsA3Cni3fj%2BEfZf6ESEQCpehaOW33ZCE%2F%2F5DMMnb%2FMkGOqUBWTE20PwjqEi9WeCCBEyAXCL5Pa9Qb4Kiyot12hXy78kTGfyTU5Vg6I04ZAHctSTjy%2FoQ8jUz9nhTdYOyJKohr3D01cHrbiu5dFrw%2Bu7as%2Bdvb1%2BkxFMbf7yI%2BmsHX8d8W8snTBhC5geKpKRC2X853l%2BHgUyP4f2jwVqUST97bU%2F9C2H8e20KSmj4RDgRIK9961lKw6PytTJGpkIH2zgNSTpuE%2FHN&X-Amz-Signature=2c25119dd44dd31011b0a5bcff073e9762a1ed240fc4958e33652607dce8e4b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GYSGHD7%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCaV%2BoP6Z8WQpUGsP8ZTB9m1hlPLTMWkMFQOhB%2Fv6fwzgIgOEIAu%2BhWMHv0SG6x3pHvYOSdKGvT%2BkSVNPqNHKzfl78q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDHUWct%2FelulWprH%2B2CrcA88AMNw84o8lIimdEbIPvAd0YCBijM%2Fp7Xz77M9xQ4z9nR%2FOjD4XBpyQlGNGRRfJHjNzoaQxa5sljoVK6BMQNGKErR9Tm9%2B8rw6AbS41Wa1o7TD0BaG5h5d%2FRHJqsbvOtGu9xJUE8Col6S7X7wkMIiMI5y8iZyJvS24wkPAdhfOzvGXM0OiXQT4wgb2uXAAAHsdZwDvgrFybAFMqoKNQovTIyk2H0vXOZvGWnhfYILlOGyQeogRGwVQYUASwpQeQ%2F4eDIWG5NfKfdWt1dp0IvyciMXHOG84XX3ee6KqxeJq3gK6%2BbqsQ0i9sc%2FDh%2BB7E1SW222V9ufYGYMfW40A8HgC1n2HvqcQ54nb%2FfCFInkHaw0E8co1yJEtiZoN0exN6N6nz7eNSfiqkyP64Yp3WYdpWaj1WdIEhkQi7TNsfV8cjpVK41ad5RAOZ5ATSbNNarZcXJo8fPNFYoDzVRRSo4Nv1ar4O8GuxeIpRAmiHJDLbyq2yi%2FemtIJyV0o6DJr2ka%2FtD3z1dZWO17wOrqIENR0fC50Smr8ETjXpKlR99IS7u9qs3ldSM5w6dKPKu0xRjU%2FyJyCwKDCsPub8hq52GSu0fsA3Cni3fj%2BEfZf6ESEQCpehaOW33ZCE%2F%2F5DMMnb%2FMkGOqUBWTE20PwjqEi9WeCCBEyAXCL5Pa9Qb4Kiyot12hXy78kTGfyTU5Vg6I04ZAHctSTjy%2FoQ8jUz9nhTdYOyJKohr3D01cHrbiu5dFrw%2Bu7as%2Bdvb1%2BkxFMbf7yI%2BmsHX8d8W8snTBhC5geKpKRC2X853l%2BHgUyP4f2jwVqUST97bU%2F9C2H8e20KSmj4RDgRIK9961lKw6PytTJGpkIH2zgNSTpuE%2FHN&X-Amz-Signature=5845ed006e1eb7ae2cfa532a9414c7ce103963c4837ef3f54d4df11e198340f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GYSGHD7%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCaV%2BoP6Z8WQpUGsP8ZTB9m1hlPLTMWkMFQOhB%2Fv6fwzgIgOEIAu%2BhWMHv0SG6x3pHvYOSdKGvT%2BkSVNPqNHKzfl78q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDHUWct%2FelulWprH%2B2CrcA88AMNw84o8lIimdEbIPvAd0YCBijM%2Fp7Xz77M9xQ4z9nR%2FOjD4XBpyQlGNGRRfJHjNzoaQxa5sljoVK6BMQNGKErR9Tm9%2B8rw6AbS41Wa1o7TD0BaG5h5d%2FRHJqsbvOtGu9xJUE8Col6S7X7wkMIiMI5y8iZyJvS24wkPAdhfOzvGXM0OiXQT4wgb2uXAAAHsdZwDvgrFybAFMqoKNQovTIyk2H0vXOZvGWnhfYILlOGyQeogRGwVQYUASwpQeQ%2F4eDIWG5NfKfdWt1dp0IvyciMXHOG84XX3ee6KqxeJq3gK6%2BbqsQ0i9sc%2FDh%2BB7E1SW222V9ufYGYMfW40A8HgC1n2HvqcQ54nb%2FfCFInkHaw0E8co1yJEtiZoN0exN6N6nz7eNSfiqkyP64Yp3WYdpWaj1WdIEhkQi7TNsfV8cjpVK41ad5RAOZ5ATSbNNarZcXJo8fPNFYoDzVRRSo4Nv1ar4O8GuxeIpRAmiHJDLbyq2yi%2FemtIJyV0o6DJr2ka%2FtD3z1dZWO17wOrqIENR0fC50Smr8ETjXpKlR99IS7u9qs3ldSM5w6dKPKu0xRjU%2FyJyCwKDCsPub8hq52GSu0fsA3Cni3fj%2BEfZf6ESEQCpehaOW33ZCE%2F%2F5DMMnb%2FMkGOqUBWTE20PwjqEi9WeCCBEyAXCL5Pa9Qb4Kiyot12hXy78kTGfyTU5Vg6I04ZAHctSTjy%2FoQ8jUz9nhTdYOyJKohr3D01cHrbiu5dFrw%2Bu7as%2Bdvb1%2BkxFMbf7yI%2BmsHX8d8W8snTBhC5geKpKRC2X853l%2BHgUyP4f2jwVqUST97bU%2F9C2H8e20KSmj4RDgRIK9961lKw6PytTJGpkIH2zgNSTpuE%2FHN&X-Amz-Signature=4c948101b5fadf1ae7f7fc89d0d84a542e816f477b3e5b27ab2eb44311d5fc9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GYSGHD7%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCaV%2BoP6Z8WQpUGsP8ZTB9m1hlPLTMWkMFQOhB%2Fv6fwzgIgOEIAu%2BhWMHv0SG6x3pHvYOSdKGvT%2BkSVNPqNHKzfl78q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDHUWct%2FelulWprH%2B2CrcA88AMNw84o8lIimdEbIPvAd0YCBijM%2Fp7Xz77M9xQ4z9nR%2FOjD4XBpyQlGNGRRfJHjNzoaQxa5sljoVK6BMQNGKErR9Tm9%2B8rw6AbS41Wa1o7TD0BaG5h5d%2FRHJqsbvOtGu9xJUE8Col6S7X7wkMIiMI5y8iZyJvS24wkPAdhfOzvGXM0OiXQT4wgb2uXAAAHsdZwDvgrFybAFMqoKNQovTIyk2H0vXOZvGWnhfYILlOGyQeogRGwVQYUASwpQeQ%2F4eDIWG5NfKfdWt1dp0IvyciMXHOG84XX3ee6KqxeJq3gK6%2BbqsQ0i9sc%2FDh%2BB7E1SW222V9ufYGYMfW40A8HgC1n2HvqcQ54nb%2FfCFInkHaw0E8co1yJEtiZoN0exN6N6nz7eNSfiqkyP64Yp3WYdpWaj1WdIEhkQi7TNsfV8cjpVK41ad5RAOZ5ATSbNNarZcXJo8fPNFYoDzVRRSo4Nv1ar4O8GuxeIpRAmiHJDLbyq2yi%2FemtIJyV0o6DJr2ka%2FtD3z1dZWO17wOrqIENR0fC50Smr8ETjXpKlR99IS7u9qs3ldSM5w6dKPKu0xRjU%2FyJyCwKDCsPub8hq52GSu0fsA3Cni3fj%2BEfZf6ESEQCpehaOW33ZCE%2F%2F5DMMnb%2FMkGOqUBWTE20PwjqEi9WeCCBEyAXCL5Pa9Qb4Kiyot12hXy78kTGfyTU5Vg6I04ZAHctSTjy%2FoQ8jUz9nhTdYOyJKohr3D01cHrbiu5dFrw%2Bu7as%2Bdvb1%2BkxFMbf7yI%2BmsHX8d8W8snTBhC5geKpKRC2X853l%2BHgUyP4f2jwVqUST97bU%2F9C2H8e20KSmj4RDgRIK9961lKw6PytTJGpkIH2zgNSTpuE%2FHN&X-Amz-Signature=27ef680a53757eb98b3297a46b8ab9b49e59546dd66a4a329ac59a9dd72073d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GYSGHD7%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCaV%2BoP6Z8WQpUGsP8ZTB9m1hlPLTMWkMFQOhB%2Fv6fwzgIgOEIAu%2BhWMHv0SG6x3pHvYOSdKGvT%2BkSVNPqNHKzfl78q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDHUWct%2FelulWprH%2B2CrcA88AMNw84o8lIimdEbIPvAd0YCBijM%2Fp7Xz77M9xQ4z9nR%2FOjD4XBpyQlGNGRRfJHjNzoaQxa5sljoVK6BMQNGKErR9Tm9%2B8rw6AbS41Wa1o7TD0BaG5h5d%2FRHJqsbvOtGu9xJUE8Col6S7X7wkMIiMI5y8iZyJvS24wkPAdhfOzvGXM0OiXQT4wgb2uXAAAHsdZwDvgrFybAFMqoKNQovTIyk2H0vXOZvGWnhfYILlOGyQeogRGwVQYUASwpQeQ%2F4eDIWG5NfKfdWt1dp0IvyciMXHOG84XX3ee6KqxeJq3gK6%2BbqsQ0i9sc%2FDh%2BB7E1SW222V9ufYGYMfW40A8HgC1n2HvqcQ54nb%2FfCFInkHaw0E8co1yJEtiZoN0exN6N6nz7eNSfiqkyP64Yp3WYdpWaj1WdIEhkQi7TNsfV8cjpVK41ad5RAOZ5ATSbNNarZcXJo8fPNFYoDzVRRSo4Nv1ar4O8GuxeIpRAmiHJDLbyq2yi%2FemtIJyV0o6DJr2ka%2FtD3z1dZWO17wOrqIENR0fC50Smr8ETjXpKlR99IS7u9qs3ldSM5w6dKPKu0xRjU%2FyJyCwKDCsPub8hq52GSu0fsA3Cni3fj%2BEfZf6ESEQCpehaOW33ZCE%2F%2F5DMMnb%2FMkGOqUBWTE20PwjqEi9WeCCBEyAXCL5Pa9Qb4Kiyot12hXy78kTGfyTU5Vg6I04ZAHctSTjy%2FoQ8jUz9nhTdYOyJKohr3D01cHrbiu5dFrw%2Bu7as%2Bdvb1%2BkxFMbf7yI%2BmsHX8d8W8snTBhC5geKpKRC2X853l%2BHgUyP4f2jwVqUST97bU%2F9C2H8e20KSmj4RDgRIK9961lKw6PytTJGpkIH2zgNSTpuE%2FHN&X-Amz-Signature=d9f5dcb00fc4d347135689ed2fc0783b6c072a31a91c30447a478f395e70adc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GYSGHD7%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCaV%2BoP6Z8WQpUGsP8ZTB9m1hlPLTMWkMFQOhB%2Fv6fwzgIgOEIAu%2BhWMHv0SG6x3pHvYOSdKGvT%2BkSVNPqNHKzfl78q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDHUWct%2FelulWprH%2B2CrcA88AMNw84o8lIimdEbIPvAd0YCBijM%2Fp7Xz77M9xQ4z9nR%2FOjD4XBpyQlGNGRRfJHjNzoaQxa5sljoVK6BMQNGKErR9Tm9%2B8rw6AbS41Wa1o7TD0BaG5h5d%2FRHJqsbvOtGu9xJUE8Col6S7X7wkMIiMI5y8iZyJvS24wkPAdhfOzvGXM0OiXQT4wgb2uXAAAHsdZwDvgrFybAFMqoKNQovTIyk2H0vXOZvGWnhfYILlOGyQeogRGwVQYUASwpQeQ%2F4eDIWG5NfKfdWt1dp0IvyciMXHOG84XX3ee6KqxeJq3gK6%2BbqsQ0i9sc%2FDh%2BB7E1SW222V9ufYGYMfW40A8HgC1n2HvqcQ54nb%2FfCFInkHaw0E8co1yJEtiZoN0exN6N6nz7eNSfiqkyP64Yp3WYdpWaj1WdIEhkQi7TNsfV8cjpVK41ad5RAOZ5ATSbNNarZcXJo8fPNFYoDzVRRSo4Nv1ar4O8GuxeIpRAmiHJDLbyq2yi%2FemtIJyV0o6DJr2ka%2FtD3z1dZWO17wOrqIENR0fC50Smr8ETjXpKlR99IS7u9qs3ldSM5w6dKPKu0xRjU%2FyJyCwKDCsPub8hq52GSu0fsA3Cni3fj%2BEfZf6ESEQCpehaOW33ZCE%2F%2F5DMMnb%2FMkGOqUBWTE20PwjqEi9WeCCBEyAXCL5Pa9Qb4Kiyot12hXy78kTGfyTU5Vg6I04ZAHctSTjy%2FoQ8jUz9nhTdYOyJKohr3D01cHrbiu5dFrw%2Bu7as%2Bdvb1%2BkxFMbf7yI%2BmsHX8d8W8snTBhC5geKpKRC2X853l%2BHgUyP4f2jwVqUST97bU%2F9C2H8e20KSmj4RDgRIK9961lKw6PytTJGpkIH2zgNSTpuE%2FHN&X-Amz-Signature=acd3df3bd2a472e2fb2d2c9661c5ee05fb6046bb368339248bc6d0c5d563ebba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GYSGHD7%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCaV%2BoP6Z8WQpUGsP8ZTB9m1hlPLTMWkMFQOhB%2Fv6fwzgIgOEIAu%2BhWMHv0SG6x3pHvYOSdKGvT%2BkSVNPqNHKzfl78q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDHUWct%2FelulWprH%2B2CrcA88AMNw84o8lIimdEbIPvAd0YCBijM%2Fp7Xz77M9xQ4z9nR%2FOjD4XBpyQlGNGRRfJHjNzoaQxa5sljoVK6BMQNGKErR9Tm9%2B8rw6AbS41Wa1o7TD0BaG5h5d%2FRHJqsbvOtGu9xJUE8Col6S7X7wkMIiMI5y8iZyJvS24wkPAdhfOzvGXM0OiXQT4wgb2uXAAAHsdZwDvgrFybAFMqoKNQovTIyk2H0vXOZvGWnhfYILlOGyQeogRGwVQYUASwpQeQ%2F4eDIWG5NfKfdWt1dp0IvyciMXHOG84XX3ee6KqxeJq3gK6%2BbqsQ0i9sc%2FDh%2BB7E1SW222V9ufYGYMfW40A8HgC1n2HvqcQ54nb%2FfCFInkHaw0E8co1yJEtiZoN0exN6N6nz7eNSfiqkyP64Yp3WYdpWaj1WdIEhkQi7TNsfV8cjpVK41ad5RAOZ5ATSbNNarZcXJo8fPNFYoDzVRRSo4Nv1ar4O8GuxeIpRAmiHJDLbyq2yi%2FemtIJyV0o6DJr2ka%2FtD3z1dZWO17wOrqIENR0fC50Smr8ETjXpKlR99IS7u9qs3ldSM5w6dKPKu0xRjU%2FyJyCwKDCsPub8hq52GSu0fsA3Cni3fj%2BEfZf6ESEQCpehaOW33ZCE%2F%2F5DMMnb%2FMkGOqUBWTE20PwjqEi9WeCCBEyAXCL5Pa9Qb4Kiyot12hXy78kTGfyTU5Vg6I04ZAHctSTjy%2FoQ8jUz9nhTdYOyJKohr3D01cHrbiu5dFrw%2Bu7as%2Bdvb1%2BkxFMbf7yI%2BmsHX8d8W8snTBhC5geKpKRC2X853l%2BHgUyP4f2jwVqUST97bU%2F9C2H8e20KSmj4RDgRIK9961lKw6PytTJGpkIH2zgNSTpuE%2FHN&X-Amz-Signature=53e33414edafd235464f5b1dc6e461e4ed065b5d910fcc0af2ab8825dce6f0e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GYSGHD7%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCaV%2BoP6Z8WQpUGsP8ZTB9m1hlPLTMWkMFQOhB%2Fv6fwzgIgOEIAu%2BhWMHv0SG6x3pHvYOSdKGvT%2BkSVNPqNHKzfl78q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDHUWct%2FelulWprH%2B2CrcA88AMNw84o8lIimdEbIPvAd0YCBijM%2Fp7Xz77M9xQ4z9nR%2FOjD4XBpyQlGNGRRfJHjNzoaQxa5sljoVK6BMQNGKErR9Tm9%2B8rw6AbS41Wa1o7TD0BaG5h5d%2FRHJqsbvOtGu9xJUE8Col6S7X7wkMIiMI5y8iZyJvS24wkPAdhfOzvGXM0OiXQT4wgb2uXAAAHsdZwDvgrFybAFMqoKNQovTIyk2H0vXOZvGWnhfYILlOGyQeogRGwVQYUASwpQeQ%2F4eDIWG5NfKfdWt1dp0IvyciMXHOG84XX3ee6KqxeJq3gK6%2BbqsQ0i9sc%2FDh%2BB7E1SW222V9ufYGYMfW40A8HgC1n2HvqcQ54nb%2FfCFInkHaw0E8co1yJEtiZoN0exN6N6nz7eNSfiqkyP64Yp3WYdpWaj1WdIEhkQi7TNsfV8cjpVK41ad5RAOZ5ATSbNNarZcXJo8fPNFYoDzVRRSo4Nv1ar4O8GuxeIpRAmiHJDLbyq2yi%2FemtIJyV0o6DJr2ka%2FtD3z1dZWO17wOrqIENR0fC50Smr8ETjXpKlR99IS7u9qs3ldSM5w6dKPKu0xRjU%2FyJyCwKDCsPub8hq52GSu0fsA3Cni3fj%2BEfZf6ESEQCpehaOW33ZCE%2F%2F5DMMnb%2FMkGOqUBWTE20PwjqEi9WeCCBEyAXCL5Pa9Qb4Kiyot12hXy78kTGfyTU5Vg6I04ZAHctSTjy%2FoQ8jUz9nhTdYOyJKohr3D01cHrbiu5dFrw%2Bu7as%2Bdvb1%2BkxFMbf7yI%2BmsHX8d8W8snTBhC5geKpKRC2X853l%2BHgUyP4f2jwVqUST97bU%2F9C2H8e20KSmj4RDgRIK9961lKw6PytTJGpkIH2zgNSTpuE%2FHN&X-Amz-Signature=581e8812433445f72baec7cf1290a70581201f7bab6abd7fb74a526e02a466f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GYSGHD7%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCaV%2BoP6Z8WQpUGsP8ZTB9m1hlPLTMWkMFQOhB%2Fv6fwzgIgOEIAu%2BhWMHv0SG6x3pHvYOSdKGvT%2BkSVNPqNHKzfl78q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDHUWct%2FelulWprH%2B2CrcA88AMNw84o8lIimdEbIPvAd0YCBijM%2Fp7Xz77M9xQ4z9nR%2FOjD4XBpyQlGNGRRfJHjNzoaQxa5sljoVK6BMQNGKErR9Tm9%2B8rw6AbS41Wa1o7TD0BaG5h5d%2FRHJqsbvOtGu9xJUE8Col6S7X7wkMIiMI5y8iZyJvS24wkPAdhfOzvGXM0OiXQT4wgb2uXAAAHsdZwDvgrFybAFMqoKNQovTIyk2H0vXOZvGWnhfYILlOGyQeogRGwVQYUASwpQeQ%2F4eDIWG5NfKfdWt1dp0IvyciMXHOG84XX3ee6KqxeJq3gK6%2BbqsQ0i9sc%2FDh%2BB7E1SW222V9ufYGYMfW40A8HgC1n2HvqcQ54nb%2FfCFInkHaw0E8co1yJEtiZoN0exN6N6nz7eNSfiqkyP64Yp3WYdpWaj1WdIEhkQi7TNsfV8cjpVK41ad5RAOZ5ATSbNNarZcXJo8fPNFYoDzVRRSo4Nv1ar4O8GuxeIpRAmiHJDLbyq2yi%2FemtIJyV0o6DJr2ka%2FtD3z1dZWO17wOrqIENR0fC50Smr8ETjXpKlR99IS7u9qs3ldSM5w6dKPKu0xRjU%2FyJyCwKDCsPub8hq52GSu0fsA3Cni3fj%2BEfZf6ESEQCpehaOW33ZCE%2F%2F5DMMnb%2FMkGOqUBWTE20PwjqEi9WeCCBEyAXCL5Pa9Qb4Kiyot12hXy78kTGfyTU5Vg6I04ZAHctSTjy%2FoQ8jUz9nhTdYOyJKohr3D01cHrbiu5dFrw%2Bu7as%2Bdvb1%2BkxFMbf7yI%2BmsHX8d8W8snTBhC5geKpKRC2X853l%2BHgUyP4f2jwVqUST97bU%2F9C2H8e20KSmj4RDgRIK9961lKw6PytTJGpkIH2zgNSTpuE%2FHN&X-Amz-Signature=c2098973eafa95df6edd27db359b3355fe364214b7b78ae3a2cf8da15553fba8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

