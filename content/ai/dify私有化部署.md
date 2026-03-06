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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JYQP4NX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDYV1lrCRnRWTwBuV5XDBgm%2FEqvq5F16gcIbKULAP%2BEKAIgZ4Lzxo7dkyiJBaoW%2FfjSy%2FgVPxeuKPmfhcb9V06m3hoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5ZvLcw7RerSLOGyCrcA7xHRd6doQFslCYYZiB4G5HCR%2FSg208eKHGDp9gOduPwZ0EdOLBWwFHofP85zbsods3XaOUUqahMKWvlg%2FEqUYq8cLc4awsAoGoQgBLR%2FKR5lZwrPdBEBpQ6A1EnKiDwyMqv651KBslz291dDHn%2Fsl9hJOffS7hAe0b7bx0g4fCqlVptUJv1dWnjfiDWLbX1CKhD037DGc0P%2FuoxDtgUqzr69UKL8TFihaTUepIuPu3AK%2FUxCGwwR3XfzgKW9rwFpKo2M7OQpFKjyH3FnqBs8Lkv4Wo0HyJuFwVxIxtBRvIjQMtmDGsc9lnrnv04OHF1JSNM%2FtjPth9AB1td1fO2Ub9mKEwokehHrg2VE9zkxUUeMS%2BNUVtetx6VO%2FnkxokLJvwblfNZ4mZe2Fy9HXu3RY752c%2BIvBlcaTuQqeqXKQFEoDSoHZV%2FSVEdnKam3pCNoBRaw%2F2QKsNH%2FFXg08TyED9IrVAK0YftaimIQzN%2BkscK5UsLP3992IhCu%2FNYu4vA6gIw8zZ9VCcBmFDvz%2B6cUWJMbqxa7KpW623RNBT65Y7BrjmWWfcLCSrWYLsbyOPn6aJGq8M2OVCZXTAj2ih47CZ5sxd8L7ba7tT2RYH00kXB32%2BjT3c7ULksmN7NMOLOqM0GOqUBIeP%2FqvuWWVh7db%2FJb%2FI3gmQD0zGH1su5vKf4MwO69bhop9rNT1ImoQHCiv5qIVy2nifL%2F9Iywry4aVJAjSK9TZYIood77dgN49NmhqfUg8uHwidd00llxgZ9rz8t1FfJn5Wf7mc5GCAV8gd6fM3252T91siM3tLbTza5HqFEYkNTRC%2BuHp4Jaji8n3YJnFGrfx4KahWXRj6I14f%2B3TYmsszWcFTr&X-Amz-Signature=71c8da13ac3608ea74441e340b6427bc43c3f21c090723b373e0259860ca8553&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JYQP4NX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDYV1lrCRnRWTwBuV5XDBgm%2FEqvq5F16gcIbKULAP%2BEKAIgZ4Lzxo7dkyiJBaoW%2FfjSy%2FgVPxeuKPmfhcb9V06m3hoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5ZvLcw7RerSLOGyCrcA7xHRd6doQFslCYYZiB4G5HCR%2FSg208eKHGDp9gOduPwZ0EdOLBWwFHofP85zbsods3XaOUUqahMKWvlg%2FEqUYq8cLc4awsAoGoQgBLR%2FKR5lZwrPdBEBpQ6A1EnKiDwyMqv651KBslz291dDHn%2Fsl9hJOffS7hAe0b7bx0g4fCqlVptUJv1dWnjfiDWLbX1CKhD037DGc0P%2FuoxDtgUqzr69UKL8TFihaTUepIuPu3AK%2FUxCGwwR3XfzgKW9rwFpKo2M7OQpFKjyH3FnqBs8Lkv4Wo0HyJuFwVxIxtBRvIjQMtmDGsc9lnrnv04OHF1JSNM%2FtjPth9AB1td1fO2Ub9mKEwokehHrg2VE9zkxUUeMS%2BNUVtetx6VO%2FnkxokLJvwblfNZ4mZe2Fy9HXu3RY752c%2BIvBlcaTuQqeqXKQFEoDSoHZV%2FSVEdnKam3pCNoBRaw%2F2QKsNH%2FFXg08TyED9IrVAK0YftaimIQzN%2BkscK5UsLP3992IhCu%2FNYu4vA6gIw8zZ9VCcBmFDvz%2B6cUWJMbqxa7KpW623RNBT65Y7BrjmWWfcLCSrWYLsbyOPn6aJGq8M2OVCZXTAj2ih47CZ5sxd8L7ba7tT2RYH00kXB32%2BjT3c7ULksmN7NMOLOqM0GOqUBIeP%2FqvuWWVh7db%2FJb%2FI3gmQD0zGH1su5vKf4MwO69bhop9rNT1ImoQHCiv5qIVy2nifL%2F9Iywry4aVJAjSK9TZYIood77dgN49NmhqfUg8uHwidd00llxgZ9rz8t1FfJn5Wf7mc5GCAV8gd6fM3252T91siM3tLbTza5HqFEYkNTRC%2BuHp4Jaji8n3YJnFGrfx4KahWXRj6I14f%2B3TYmsszWcFTr&X-Amz-Signature=c546abd7ec2aed59aae3aa46e3ad6d57f2eefe3239ea0beec312eb599351efbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JYQP4NX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDYV1lrCRnRWTwBuV5XDBgm%2FEqvq5F16gcIbKULAP%2BEKAIgZ4Lzxo7dkyiJBaoW%2FfjSy%2FgVPxeuKPmfhcb9V06m3hoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5ZvLcw7RerSLOGyCrcA7xHRd6doQFslCYYZiB4G5HCR%2FSg208eKHGDp9gOduPwZ0EdOLBWwFHofP85zbsods3XaOUUqahMKWvlg%2FEqUYq8cLc4awsAoGoQgBLR%2FKR5lZwrPdBEBpQ6A1EnKiDwyMqv651KBslz291dDHn%2Fsl9hJOffS7hAe0b7bx0g4fCqlVptUJv1dWnjfiDWLbX1CKhD037DGc0P%2FuoxDtgUqzr69UKL8TFihaTUepIuPu3AK%2FUxCGwwR3XfzgKW9rwFpKo2M7OQpFKjyH3FnqBs8Lkv4Wo0HyJuFwVxIxtBRvIjQMtmDGsc9lnrnv04OHF1JSNM%2FtjPth9AB1td1fO2Ub9mKEwokehHrg2VE9zkxUUeMS%2BNUVtetx6VO%2FnkxokLJvwblfNZ4mZe2Fy9HXu3RY752c%2BIvBlcaTuQqeqXKQFEoDSoHZV%2FSVEdnKam3pCNoBRaw%2F2QKsNH%2FFXg08TyED9IrVAK0YftaimIQzN%2BkscK5UsLP3992IhCu%2FNYu4vA6gIw8zZ9VCcBmFDvz%2B6cUWJMbqxa7KpW623RNBT65Y7BrjmWWfcLCSrWYLsbyOPn6aJGq8M2OVCZXTAj2ih47CZ5sxd8L7ba7tT2RYH00kXB32%2BjT3c7ULksmN7NMOLOqM0GOqUBIeP%2FqvuWWVh7db%2FJb%2FI3gmQD0zGH1su5vKf4MwO69bhop9rNT1ImoQHCiv5qIVy2nifL%2F9Iywry4aVJAjSK9TZYIood77dgN49NmhqfUg8uHwidd00llxgZ9rz8t1FfJn5Wf7mc5GCAV8gd6fM3252T91siM3tLbTza5HqFEYkNTRC%2BuHp4Jaji8n3YJnFGrfx4KahWXRj6I14f%2B3TYmsszWcFTr&X-Amz-Signature=01350964081544d8238c831b3f82feb9e0ea9b8d77fdcbcd2ad263ba0ac3271c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JYQP4NX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDYV1lrCRnRWTwBuV5XDBgm%2FEqvq5F16gcIbKULAP%2BEKAIgZ4Lzxo7dkyiJBaoW%2FfjSy%2FgVPxeuKPmfhcb9V06m3hoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5ZvLcw7RerSLOGyCrcA7xHRd6doQFslCYYZiB4G5HCR%2FSg208eKHGDp9gOduPwZ0EdOLBWwFHofP85zbsods3XaOUUqahMKWvlg%2FEqUYq8cLc4awsAoGoQgBLR%2FKR5lZwrPdBEBpQ6A1EnKiDwyMqv651KBslz291dDHn%2Fsl9hJOffS7hAe0b7bx0g4fCqlVptUJv1dWnjfiDWLbX1CKhD037DGc0P%2FuoxDtgUqzr69UKL8TFihaTUepIuPu3AK%2FUxCGwwR3XfzgKW9rwFpKo2M7OQpFKjyH3FnqBs8Lkv4Wo0HyJuFwVxIxtBRvIjQMtmDGsc9lnrnv04OHF1JSNM%2FtjPth9AB1td1fO2Ub9mKEwokehHrg2VE9zkxUUeMS%2BNUVtetx6VO%2FnkxokLJvwblfNZ4mZe2Fy9HXu3RY752c%2BIvBlcaTuQqeqXKQFEoDSoHZV%2FSVEdnKam3pCNoBRaw%2F2QKsNH%2FFXg08TyED9IrVAK0YftaimIQzN%2BkscK5UsLP3992IhCu%2FNYu4vA6gIw8zZ9VCcBmFDvz%2B6cUWJMbqxa7KpW623RNBT65Y7BrjmWWfcLCSrWYLsbyOPn6aJGq8M2OVCZXTAj2ih47CZ5sxd8L7ba7tT2RYH00kXB32%2BjT3c7ULksmN7NMOLOqM0GOqUBIeP%2FqvuWWVh7db%2FJb%2FI3gmQD0zGH1su5vKf4MwO69bhop9rNT1ImoQHCiv5qIVy2nifL%2F9Iywry4aVJAjSK9TZYIood77dgN49NmhqfUg8uHwidd00llxgZ9rz8t1FfJn5Wf7mc5GCAV8gd6fM3252T91siM3tLbTza5HqFEYkNTRC%2BuHp4Jaji8n3YJnFGrfx4KahWXRj6I14f%2B3TYmsszWcFTr&X-Amz-Signature=20c7b0234a7bac301acd01356949419af9e683aa7e817d4f31fca15601dcdd04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JYQP4NX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDYV1lrCRnRWTwBuV5XDBgm%2FEqvq5F16gcIbKULAP%2BEKAIgZ4Lzxo7dkyiJBaoW%2FfjSy%2FgVPxeuKPmfhcb9V06m3hoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5ZvLcw7RerSLOGyCrcA7xHRd6doQFslCYYZiB4G5HCR%2FSg208eKHGDp9gOduPwZ0EdOLBWwFHofP85zbsods3XaOUUqahMKWvlg%2FEqUYq8cLc4awsAoGoQgBLR%2FKR5lZwrPdBEBpQ6A1EnKiDwyMqv651KBslz291dDHn%2Fsl9hJOffS7hAe0b7bx0g4fCqlVptUJv1dWnjfiDWLbX1CKhD037DGc0P%2FuoxDtgUqzr69UKL8TFihaTUepIuPu3AK%2FUxCGwwR3XfzgKW9rwFpKo2M7OQpFKjyH3FnqBs8Lkv4Wo0HyJuFwVxIxtBRvIjQMtmDGsc9lnrnv04OHF1JSNM%2FtjPth9AB1td1fO2Ub9mKEwokehHrg2VE9zkxUUeMS%2BNUVtetx6VO%2FnkxokLJvwblfNZ4mZe2Fy9HXu3RY752c%2BIvBlcaTuQqeqXKQFEoDSoHZV%2FSVEdnKam3pCNoBRaw%2F2QKsNH%2FFXg08TyED9IrVAK0YftaimIQzN%2BkscK5UsLP3992IhCu%2FNYu4vA6gIw8zZ9VCcBmFDvz%2B6cUWJMbqxa7KpW623RNBT65Y7BrjmWWfcLCSrWYLsbyOPn6aJGq8M2OVCZXTAj2ih47CZ5sxd8L7ba7tT2RYH00kXB32%2BjT3c7ULksmN7NMOLOqM0GOqUBIeP%2FqvuWWVh7db%2FJb%2FI3gmQD0zGH1su5vKf4MwO69bhop9rNT1ImoQHCiv5qIVy2nifL%2F9Iywry4aVJAjSK9TZYIood77dgN49NmhqfUg8uHwidd00llxgZ9rz8t1FfJn5Wf7mc5GCAV8gd6fM3252T91siM3tLbTza5HqFEYkNTRC%2BuHp4Jaji8n3YJnFGrfx4KahWXRj6I14f%2B3TYmsszWcFTr&X-Amz-Signature=a64e6ea45625f437110cf0fbdfca472f415983eab1ea181b6f13e01a85c6be8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JYQP4NX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDYV1lrCRnRWTwBuV5XDBgm%2FEqvq5F16gcIbKULAP%2BEKAIgZ4Lzxo7dkyiJBaoW%2FfjSy%2FgVPxeuKPmfhcb9V06m3hoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5ZvLcw7RerSLOGyCrcA7xHRd6doQFslCYYZiB4G5HCR%2FSg208eKHGDp9gOduPwZ0EdOLBWwFHofP85zbsods3XaOUUqahMKWvlg%2FEqUYq8cLc4awsAoGoQgBLR%2FKR5lZwrPdBEBpQ6A1EnKiDwyMqv651KBslz291dDHn%2Fsl9hJOffS7hAe0b7bx0g4fCqlVptUJv1dWnjfiDWLbX1CKhD037DGc0P%2FuoxDtgUqzr69UKL8TFihaTUepIuPu3AK%2FUxCGwwR3XfzgKW9rwFpKo2M7OQpFKjyH3FnqBs8Lkv4Wo0HyJuFwVxIxtBRvIjQMtmDGsc9lnrnv04OHF1JSNM%2FtjPth9AB1td1fO2Ub9mKEwokehHrg2VE9zkxUUeMS%2BNUVtetx6VO%2FnkxokLJvwblfNZ4mZe2Fy9HXu3RY752c%2BIvBlcaTuQqeqXKQFEoDSoHZV%2FSVEdnKam3pCNoBRaw%2F2QKsNH%2FFXg08TyED9IrVAK0YftaimIQzN%2BkscK5UsLP3992IhCu%2FNYu4vA6gIw8zZ9VCcBmFDvz%2B6cUWJMbqxa7KpW623RNBT65Y7BrjmWWfcLCSrWYLsbyOPn6aJGq8M2OVCZXTAj2ih47CZ5sxd8L7ba7tT2RYH00kXB32%2BjT3c7ULksmN7NMOLOqM0GOqUBIeP%2FqvuWWVh7db%2FJb%2FI3gmQD0zGH1su5vKf4MwO69bhop9rNT1ImoQHCiv5qIVy2nifL%2F9Iywry4aVJAjSK9TZYIood77dgN49NmhqfUg8uHwidd00llxgZ9rz8t1FfJn5Wf7mc5GCAV8gd6fM3252T91siM3tLbTza5HqFEYkNTRC%2BuHp4Jaji8n3YJnFGrfx4KahWXRj6I14f%2B3TYmsszWcFTr&X-Amz-Signature=9021f2b6d7b3e6b3bae5e0bf0b22c4c2accecc5d4614d704826c0df848f8cc5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JYQP4NX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDYV1lrCRnRWTwBuV5XDBgm%2FEqvq5F16gcIbKULAP%2BEKAIgZ4Lzxo7dkyiJBaoW%2FfjSy%2FgVPxeuKPmfhcb9V06m3hoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5ZvLcw7RerSLOGyCrcA7xHRd6doQFslCYYZiB4G5HCR%2FSg208eKHGDp9gOduPwZ0EdOLBWwFHofP85zbsods3XaOUUqahMKWvlg%2FEqUYq8cLc4awsAoGoQgBLR%2FKR5lZwrPdBEBpQ6A1EnKiDwyMqv651KBslz291dDHn%2Fsl9hJOffS7hAe0b7bx0g4fCqlVptUJv1dWnjfiDWLbX1CKhD037DGc0P%2FuoxDtgUqzr69UKL8TFihaTUepIuPu3AK%2FUxCGwwR3XfzgKW9rwFpKo2M7OQpFKjyH3FnqBs8Lkv4Wo0HyJuFwVxIxtBRvIjQMtmDGsc9lnrnv04OHF1JSNM%2FtjPth9AB1td1fO2Ub9mKEwokehHrg2VE9zkxUUeMS%2BNUVtetx6VO%2FnkxokLJvwblfNZ4mZe2Fy9HXu3RY752c%2BIvBlcaTuQqeqXKQFEoDSoHZV%2FSVEdnKam3pCNoBRaw%2F2QKsNH%2FFXg08TyED9IrVAK0YftaimIQzN%2BkscK5UsLP3992IhCu%2FNYu4vA6gIw8zZ9VCcBmFDvz%2B6cUWJMbqxa7KpW623RNBT65Y7BrjmWWfcLCSrWYLsbyOPn6aJGq8M2OVCZXTAj2ih47CZ5sxd8L7ba7tT2RYH00kXB32%2BjT3c7ULksmN7NMOLOqM0GOqUBIeP%2FqvuWWVh7db%2FJb%2FI3gmQD0zGH1su5vKf4MwO69bhop9rNT1ImoQHCiv5qIVy2nifL%2F9Iywry4aVJAjSK9TZYIood77dgN49NmhqfUg8uHwidd00llxgZ9rz8t1FfJn5Wf7mc5GCAV8gd6fM3252T91siM3tLbTza5HqFEYkNTRC%2BuHp4Jaji8n3YJnFGrfx4KahWXRj6I14f%2B3TYmsszWcFTr&X-Amz-Signature=545c8747ed528499ce1e2af76b5fd192ccdeb21dd1fac0669b673a8e6220b8c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JYQP4NX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDYV1lrCRnRWTwBuV5XDBgm%2FEqvq5F16gcIbKULAP%2BEKAIgZ4Lzxo7dkyiJBaoW%2FfjSy%2FgVPxeuKPmfhcb9V06m3hoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5ZvLcw7RerSLOGyCrcA7xHRd6doQFslCYYZiB4G5HCR%2FSg208eKHGDp9gOduPwZ0EdOLBWwFHofP85zbsods3XaOUUqahMKWvlg%2FEqUYq8cLc4awsAoGoQgBLR%2FKR5lZwrPdBEBpQ6A1EnKiDwyMqv651KBslz291dDHn%2Fsl9hJOffS7hAe0b7bx0g4fCqlVptUJv1dWnjfiDWLbX1CKhD037DGc0P%2FuoxDtgUqzr69UKL8TFihaTUepIuPu3AK%2FUxCGwwR3XfzgKW9rwFpKo2M7OQpFKjyH3FnqBs8Lkv4Wo0HyJuFwVxIxtBRvIjQMtmDGsc9lnrnv04OHF1JSNM%2FtjPth9AB1td1fO2Ub9mKEwokehHrg2VE9zkxUUeMS%2BNUVtetx6VO%2FnkxokLJvwblfNZ4mZe2Fy9HXu3RY752c%2BIvBlcaTuQqeqXKQFEoDSoHZV%2FSVEdnKam3pCNoBRaw%2F2QKsNH%2FFXg08TyED9IrVAK0YftaimIQzN%2BkscK5UsLP3992IhCu%2FNYu4vA6gIw8zZ9VCcBmFDvz%2B6cUWJMbqxa7KpW623RNBT65Y7BrjmWWfcLCSrWYLsbyOPn6aJGq8M2OVCZXTAj2ih47CZ5sxd8L7ba7tT2RYH00kXB32%2BjT3c7ULksmN7NMOLOqM0GOqUBIeP%2FqvuWWVh7db%2FJb%2FI3gmQD0zGH1su5vKf4MwO69bhop9rNT1ImoQHCiv5qIVy2nifL%2F9Iywry4aVJAjSK9TZYIood77dgN49NmhqfUg8uHwidd00llxgZ9rz8t1FfJn5Wf7mc5GCAV8gd6fM3252T91siM3tLbTza5HqFEYkNTRC%2BuHp4Jaji8n3YJnFGrfx4KahWXRj6I14f%2B3TYmsszWcFTr&X-Amz-Signature=f9183109e4f2ca1839a916d9a7c7a7f799469055adfff03cbe4eefed922161b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JYQP4NX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDYV1lrCRnRWTwBuV5XDBgm%2FEqvq5F16gcIbKULAP%2BEKAIgZ4Lzxo7dkyiJBaoW%2FfjSy%2FgVPxeuKPmfhcb9V06m3hoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5ZvLcw7RerSLOGyCrcA7xHRd6doQFslCYYZiB4G5HCR%2FSg208eKHGDp9gOduPwZ0EdOLBWwFHofP85zbsods3XaOUUqahMKWvlg%2FEqUYq8cLc4awsAoGoQgBLR%2FKR5lZwrPdBEBpQ6A1EnKiDwyMqv651KBslz291dDHn%2Fsl9hJOffS7hAe0b7bx0g4fCqlVptUJv1dWnjfiDWLbX1CKhD037DGc0P%2FuoxDtgUqzr69UKL8TFihaTUepIuPu3AK%2FUxCGwwR3XfzgKW9rwFpKo2M7OQpFKjyH3FnqBs8Lkv4Wo0HyJuFwVxIxtBRvIjQMtmDGsc9lnrnv04OHF1JSNM%2FtjPth9AB1td1fO2Ub9mKEwokehHrg2VE9zkxUUeMS%2BNUVtetx6VO%2FnkxokLJvwblfNZ4mZe2Fy9HXu3RY752c%2BIvBlcaTuQqeqXKQFEoDSoHZV%2FSVEdnKam3pCNoBRaw%2F2QKsNH%2FFXg08TyED9IrVAK0YftaimIQzN%2BkscK5UsLP3992IhCu%2FNYu4vA6gIw8zZ9VCcBmFDvz%2B6cUWJMbqxa7KpW623RNBT65Y7BrjmWWfcLCSrWYLsbyOPn6aJGq8M2OVCZXTAj2ih47CZ5sxd8L7ba7tT2RYH00kXB32%2BjT3c7ULksmN7NMOLOqM0GOqUBIeP%2FqvuWWVh7db%2FJb%2FI3gmQD0zGH1su5vKf4MwO69bhop9rNT1ImoQHCiv5qIVy2nifL%2F9Iywry4aVJAjSK9TZYIood77dgN49NmhqfUg8uHwidd00llxgZ9rz8t1FfJn5Wf7mc5GCAV8gd6fM3252T91siM3tLbTza5HqFEYkNTRC%2BuHp4Jaji8n3YJnFGrfx4KahWXRj6I14f%2B3TYmsszWcFTr&X-Amz-Signature=5fc5f6fab177a0eda71c0441aa25bc9ee7ec7d4778a2c0515f717817db181423&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JYQP4NX%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDYV1lrCRnRWTwBuV5XDBgm%2FEqvq5F16gcIbKULAP%2BEKAIgZ4Lzxo7dkyiJBaoW%2FfjSy%2FgVPxeuKPmfhcb9V06m3hoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5ZvLcw7RerSLOGyCrcA7xHRd6doQFslCYYZiB4G5HCR%2FSg208eKHGDp9gOduPwZ0EdOLBWwFHofP85zbsods3XaOUUqahMKWvlg%2FEqUYq8cLc4awsAoGoQgBLR%2FKR5lZwrPdBEBpQ6A1EnKiDwyMqv651KBslz291dDHn%2Fsl9hJOffS7hAe0b7bx0g4fCqlVptUJv1dWnjfiDWLbX1CKhD037DGc0P%2FuoxDtgUqzr69UKL8TFihaTUepIuPu3AK%2FUxCGwwR3XfzgKW9rwFpKo2M7OQpFKjyH3FnqBs8Lkv4Wo0HyJuFwVxIxtBRvIjQMtmDGsc9lnrnv04OHF1JSNM%2FtjPth9AB1td1fO2Ub9mKEwokehHrg2VE9zkxUUeMS%2BNUVtetx6VO%2FnkxokLJvwblfNZ4mZe2Fy9HXu3RY752c%2BIvBlcaTuQqeqXKQFEoDSoHZV%2FSVEdnKam3pCNoBRaw%2F2QKsNH%2FFXg08TyED9IrVAK0YftaimIQzN%2BkscK5UsLP3992IhCu%2FNYu4vA6gIw8zZ9VCcBmFDvz%2B6cUWJMbqxa7KpW623RNBT65Y7BrjmWWfcLCSrWYLsbyOPn6aJGq8M2OVCZXTAj2ih47CZ5sxd8L7ba7tT2RYH00kXB32%2BjT3c7ULksmN7NMOLOqM0GOqUBIeP%2FqvuWWVh7db%2FJb%2FI3gmQD0zGH1su5vKf4MwO69bhop9rNT1ImoQHCiv5qIVy2nifL%2F9Iywry4aVJAjSK9TZYIood77dgN49NmhqfUg8uHwidd00llxgZ9rz8t1FfJn5Wf7mc5GCAV8gd6fM3252T91siM3tLbTza5HqFEYkNTRC%2BuHp4Jaji8n3YJnFGrfx4KahWXRj6I14f%2B3TYmsszWcFTr&X-Amz-Signature=f524909a47556abe4330df6af78d3017c73a74f8a3310708ad979ce9c8e6e623&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

