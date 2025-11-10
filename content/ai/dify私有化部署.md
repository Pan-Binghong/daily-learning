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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSELROG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGVc%2B5PzvjBHeL6AsrYk%2BoIf2KMNU3oC4bh6CBre0ifHAiEA7ewrsn4FC9WM8A6MyKTVdfD0GOZ82I8U1AyHDXsu7vYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrU6%2B5XOl%2FMwh8pzCrcA3lp37r5DvrU1wORQh3KLEORh%2BfXeB53qf2HP5FDT85l1rVEdXtn8JgMALJpDy2WvVl46fbkeVqhwwg17POgg2EkenT2HlwJbjcKs78nEO5Pxp3XzXMAZBaYOqTaxzizGZoAFMo1id6VgOHzTihLVLGhcXh%2Fs9cgDf0gNatYtY8YbDQAAyJ9SvvC76BigmDoiSTy2F2zAwcyk5CCajy3epdEe06aEMKp9%2FG2hokc6erk60OrrpXVEA2ydyN6iJtvaB5riXLLxSq6SHKW3b7JCejJLYm%2B183yqefQhusbXWzh5KhvIAz%2BrJtSJZrKIQzlYO8boMPzRFWiPiWcqO8Px6v964DRSYL6AL9pURXoh7PYBIFctW5DLVP8lxr0bLv6WPvAMkezHEcyDI8fXyK81dcG1Ekv5bXr%2FCM%2FBHkUrfXwYTEppHQZqp0XPCzpzBVG%2Fd5vs1arS1YltZ5UXngIw%2B3sHaT%2FURTybD%2Bmgw7Vy3IKcXRLAT7tdjWq89MlprO1RV%2BFA6gfFonuDxw%2FyJjxXCApNumMpMvEXaIpMfMfSqs26%2FTFBQbwrVr9pNI7s9h9emLw8lUoQocgykbzUlKW1WOoYKrdXruGKfOIGNlND0K%2BdSlNWSKrjwjC%2BCG0MNS3xMgGOqUBXtn7n0ds9nVqQRCqG5ZvxdUiAvll%2Bx%2F1KOKM089%2BNbh6%2Be6BPU2k%2FI5rKZOcSZIHONc7SWAv4KD7R8xxRO93sKLMHzIBnj1IUg5p%2B%2F8J%2BO%2BKA8eMlcMcofGDCoEbE%2B1FmfvcdvW6atY9ZyfR4GGIsPqr99pDDashamz2O7z96ZZF%2FoqJThNmk2NStc%2FnwUgxdMphLvepbdVYvLMJ%2Bx6tsx9opFkC&X-Amz-Signature=95bc46326abbcc09a383f1bf751579d3501b12b9b3b94959a60c4e185eece555&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSELROG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGVc%2B5PzvjBHeL6AsrYk%2BoIf2KMNU3oC4bh6CBre0ifHAiEA7ewrsn4FC9WM8A6MyKTVdfD0GOZ82I8U1AyHDXsu7vYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrU6%2B5XOl%2FMwh8pzCrcA3lp37r5DvrU1wORQh3KLEORh%2BfXeB53qf2HP5FDT85l1rVEdXtn8JgMALJpDy2WvVl46fbkeVqhwwg17POgg2EkenT2HlwJbjcKs78nEO5Pxp3XzXMAZBaYOqTaxzizGZoAFMo1id6VgOHzTihLVLGhcXh%2Fs9cgDf0gNatYtY8YbDQAAyJ9SvvC76BigmDoiSTy2F2zAwcyk5CCajy3epdEe06aEMKp9%2FG2hokc6erk60OrrpXVEA2ydyN6iJtvaB5riXLLxSq6SHKW3b7JCejJLYm%2B183yqefQhusbXWzh5KhvIAz%2BrJtSJZrKIQzlYO8boMPzRFWiPiWcqO8Px6v964DRSYL6AL9pURXoh7PYBIFctW5DLVP8lxr0bLv6WPvAMkezHEcyDI8fXyK81dcG1Ekv5bXr%2FCM%2FBHkUrfXwYTEppHQZqp0XPCzpzBVG%2Fd5vs1arS1YltZ5UXngIw%2B3sHaT%2FURTybD%2Bmgw7Vy3IKcXRLAT7tdjWq89MlprO1RV%2BFA6gfFonuDxw%2FyJjxXCApNumMpMvEXaIpMfMfSqs26%2FTFBQbwrVr9pNI7s9h9emLw8lUoQocgykbzUlKW1WOoYKrdXruGKfOIGNlND0K%2BdSlNWSKrjwjC%2BCG0MNS3xMgGOqUBXtn7n0ds9nVqQRCqG5ZvxdUiAvll%2Bx%2F1KOKM089%2BNbh6%2Be6BPU2k%2FI5rKZOcSZIHONc7SWAv4KD7R8xxRO93sKLMHzIBnj1IUg5p%2B%2F8J%2BO%2BKA8eMlcMcofGDCoEbE%2B1FmfvcdvW6atY9ZyfR4GGIsPqr99pDDashamz2O7z96ZZF%2FoqJThNmk2NStc%2FnwUgxdMphLvepbdVYvLMJ%2Bx6tsx9opFkC&X-Amz-Signature=c2e46bf70855c5e0e5be243ffe51383bedfcfdb73b1e1ea2390b1a1674571694&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSELROG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGVc%2B5PzvjBHeL6AsrYk%2BoIf2KMNU3oC4bh6CBre0ifHAiEA7ewrsn4FC9WM8A6MyKTVdfD0GOZ82I8U1AyHDXsu7vYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrU6%2B5XOl%2FMwh8pzCrcA3lp37r5DvrU1wORQh3KLEORh%2BfXeB53qf2HP5FDT85l1rVEdXtn8JgMALJpDy2WvVl46fbkeVqhwwg17POgg2EkenT2HlwJbjcKs78nEO5Pxp3XzXMAZBaYOqTaxzizGZoAFMo1id6VgOHzTihLVLGhcXh%2Fs9cgDf0gNatYtY8YbDQAAyJ9SvvC76BigmDoiSTy2F2zAwcyk5CCajy3epdEe06aEMKp9%2FG2hokc6erk60OrrpXVEA2ydyN6iJtvaB5riXLLxSq6SHKW3b7JCejJLYm%2B183yqefQhusbXWzh5KhvIAz%2BrJtSJZrKIQzlYO8boMPzRFWiPiWcqO8Px6v964DRSYL6AL9pURXoh7PYBIFctW5DLVP8lxr0bLv6WPvAMkezHEcyDI8fXyK81dcG1Ekv5bXr%2FCM%2FBHkUrfXwYTEppHQZqp0XPCzpzBVG%2Fd5vs1arS1YltZ5UXngIw%2B3sHaT%2FURTybD%2Bmgw7Vy3IKcXRLAT7tdjWq89MlprO1RV%2BFA6gfFonuDxw%2FyJjxXCApNumMpMvEXaIpMfMfSqs26%2FTFBQbwrVr9pNI7s9h9emLw8lUoQocgykbzUlKW1WOoYKrdXruGKfOIGNlND0K%2BdSlNWSKrjwjC%2BCG0MNS3xMgGOqUBXtn7n0ds9nVqQRCqG5ZvxdUiAvll%2Bx%2F1KOKM089%2BNbh6%2Be6BPU2k%2FI5rKZOcSZIHONc7SWAv4KD7R8xxRO93sKLMHzIBnj1IUg5p%2B%2F8J%2BO%2BKA8eMlcMcofGDCoEbE%2B1FmfvcdvW6atY9ZyfR4GGIsPqr99pDDashamz2O7z96ZZF%2FoqJThNmk2NStc%2FnwUgxdMphLvepbdVYvLMJ%2Bx6tsx9opFkC&X-Amz-Signature=2291ab3318d2603e0df122da32036cafacb3359b8614f4b80cfe9477249aef15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSELROG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGVc%2B5PzvjBHeL6AsrYk%2BoIf2KMNU3oC4bh6CBre0ifHAiEA7ewrsn4FC9WM8A6MyKTVdfD0GOZ82I8U1AyHDXsu7vYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrU6%2B5XOl%2FMwh8pzCrcA3lp37r5DvrU1wORQh3KLEORh%2BfXeB53qf2HP5FDT85l1rVEdXtn8JgMALJpDy2WvVl46fbkeVqhwwg17POgg2EkenT2HlwJbjcKs78nEO5Pxp3XzXMAZBaYOqTaxzizGZoAFMo1id6VgOHzTihLVLGhcXh%2Fs9cgDf0gNatYtY8YbDQAAyJ9SvvC76BigmDoiSTy2F2zAwcyk5CCajy3epdEe06aEMKp9%2FG2hokc6erk60OrrpXVEA2ydyN6iJtvaB5riXLLxSq6SHKW3b7JCejJLYm%2B183yqefQhusbXWzh5KhvIAz%2BrJtSJZrKIQzlYO8boMPzRFWiPiWcqO8Px6v964DRSYL6AL9pURXoh7PYBIFctW5DLVP8lxr0bLv6WPvAMkezHEcyDI8fXyK81dcG1Ekv5bXr%2FCM%2FBHkUrfXwYTEppHQZqp0XPCzpzBVG%2Fd5vs1arS1YltZ5UXngIw%2B3sHaT%2FURTybD%2Bmgw7Vy3IKcXRLAT7tdjWq89MlprO1RV%2BFA6gfFonuDxw%2FyJjxXCApNumMpMvEXaIpMfMfSqs26%2FTFBQbwrVr9pNI7s9h9emLw8lUoQocgykbzUlKW1WOoYKrdXruGKfOIGNlND0K%2BdSlNWSKrjwjC%2BCG0MNS3xMgGOqUBXtn7n0ds9nVqQRCqG5ZvxdUiAvll%2Bx%2F1KOKM089%2BNbh6%2Be6BPU2k%2FI5rKZOcSZIHONc7SWAv4KD7R8xxRO93sKLMHzIBnj1IUg5p%2B%2F8J%2BO%2BKA8eMlcMcofGDCoEbE%2B1FmfvcdvW6atY9ZyfR4GGIsPqr99pDDashamz2O7z96ZZF%2FoqJThNmk2NStc%2FnwUgxdMphLvepbdVYvLMJ%2Bx6tsx9opFkC&X-Amz-Signature=1a6ef252fbac5ecf89571f2f4fb45ad79c6ddbdd033ccdaa4ce7b2b2387fd4cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSELROG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGVc%2B5PzvjBHeL6AsrYk%2BoIf2KMNU3oC4bh6CBre0ifHAiEA7ewrsn4FC9WM8A6MyKTVdfD0GOZ82I8U1AyHDXsu7vYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrU6%2B5XOl%2FMwh8pzCrcA3lp37r5DvrU1wORQh3KLEORh%2BfXeB53qf2HP5FDT85l1rVEdXtn8JgMALJpDy2WvVl46fbkeVqhwwg17POgg2EkenT2HlwJbjcKs78nEO5Pxp3XzXMAZBaYOqTaxzizGZoAFMo1id6VgOHzTihLVLGhcXh%2Fs9cgDf0gNatYtY8YbDQAAyJ9SvvC76BigmDoiSTy2F2zAwcyk5CCajy3epdEe06aEMKp9%2FG2hokc6erk60OrrpXVEA2ydyN6iJtvaB5riXLLxSq6SHKW3b7JCejJLYm%2B183yqefQhusbXWzh5KhvIAz%2BrJtSJZrKIQzlYO8boMPzRFWiPiWcqO8Px6v964DRSYL6AL9pURXoh7PYBIFctW5DLVP8lxr0bLv6WPvAMkezHEcyDI8fXyK81dcG1Ekv5bXr%2FCM%2FBHkUrfXwYTEppHQZqp0XPCzpzBVG%2Fd5vs1arS1YltZ5UXngIw%2B3sHaT%2FURTybD%2Bmgw7Vy3IKcXRLAT7tdjWq89MlprO1RV%2BFA6gfFonuDxw%2FyJjxXCApNumMpMvEXaIpMfMfSqs26%2FTFBQbwrVr9pNI7s9h9emLw8lUoQocgykbzUlKW1WOoYKrdXruGKfOIGNlND0K%2BdSlNWSKrjwjC%2BCG0MNS3xMgGOqUBXtn7n0ds9nVqQRCqG5ZvxdUiAvll%2Bx%2F1KOKM089%2BNbh6%2Be6BPU2k%2FI5rKZOcSZIHONc7SWAv4KD7R8xxRO93sKLMHzIBnj1IUg5p%2B%2F8J%2BO%2BKA8eMlcMcofGDCoEbE%2B1FmfvcdvW6atY9ZyfR4GGIsPqr99pDDashamz2O7z96ZZF%2FoqJThNmk2NStc%2FnwUgxdMphLvepbdVYvLMJ%2Bx6tsx9opFkC&X-Amz-Signature=038654bd7375bc82c9513d5496538cf31dde5b4e424dfd06a3f83f7355eae11f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSELROG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGVc%2B5PzvjBHeL6AsrYk%2BoIf2KMNU3oC4bh6CBre0ifHAiEA7ewrsn4FC9WM8A6MyKTVdfD0GOZ82I8U1AyHDXsu7vYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrU6%2B5XOl%2FMwh8pzCrcA3lp37r5DvrU1wORQh3KLEORh%2BfXeB53qf2HP5FDT85l1rVEdXtn8JgMALJpDy2WvVl46fbkeVqhwwg17POgg2EkenT2HlwJbjcKs78nEO5Pxp3XzXMAZBaYOqTaxzizGZoAFMo1id6VgOHzTihLVLGhcXh%2Fs9cgDf0gNatYtY8YbDQAAyJ9SvvC76BigmDoiSTy2F2zAwcyk5CCajy3epdEe06aEMKp9%2FG2hokc6erk60OrrpXVEA2ydyN6iJtvaB5riXLLxSq6SHKW3b7JCejJLYm%2B183yqefQhusbXWzh5KhvIAz%2BrJtSJZrKIQzlYO8boMPzRFWiPiWcqO8Px6v964DRSYL6AL9pURXoh7PYBIFctW5DLVP8lxr0bLv6WPvAMkezHEcyDI8fXyK81dcG1Ekv5bXr%2FCM%2FBHkUrfXwYTEppHQZqp0XPCzpzBVG%2Fd5vs1arS1YltZ5UXngIw%2B3sHaT%2FURTybD%2Bmgw7Vy3IKcXRLAT7tdjWq89MlprO1RV%2BFA6gfFonuDxw%2FyJjxXCApNumMpMvEXaIpMfMfSqs26%2FTFBQbwrVr9pNI7s9h9emLw8lUoQocgykbzUlKW1WOoYKrdXruGKfOIGNlND0K%2BdSlNWSKrjwjC%2BCG0MNS3xMgGOqUBXtn7n0ds9nVqQRCqG5ZvxdUiAvll%2Bx%2F1KOKM089%2BNbh6%2Be6BPU2k%2FI5rKZOcSZIHONc7SWAv4KD7R8xxRO93sKLMHzIBnj1IUg5p%2B%2F8J%2BO%2BKA8eMlcMcofGDCoEbE%2B1FmfvcdvW6atY9ZyfR4GGIsPqr99pDDashamz2O7z96ZZF%2FoqJThNmk2NStc%2FnwUgxdMphLvepbdVYvLMJ%2Bx6tsx9opFkC&X-Amz-Signature=c2485d00e37e54740847c2a6a15b38876e9b5ed7651f5e7ea5dd297094255a01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSELROG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGVc%2B5PzvjBHeL6AsrYk%2BoIf2KMNU3oC4bh6CBre0ifHAiEA7ewrsn4FC9WM8A6MyKTVdfD0GOZ82I8U1AyHDXsu7vYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrU6%2B5XOl%2FMwh8pzCrcA3lp37r5DvrU1wORQh3KLEORh%2BfXeB53qf2HP5FDT85l1rVEdXtn8JgMALJpDy2WvVl46fbkeVqhwwg17POgg2EkenT2HlwJbjcKs78nEO5Pxp3XzXMAZBaYOqTaxzizGZoAFMo1id6VgOHzTihLVLGhcXh%2Fs9cgDf0gNatYtY8YbDQAAyJ9SvvC76BigmDoiSTy2F2zAwcyk5CCajy3epdEe06aEMKp9%2FG2hokc6erk60OrrpXVEA2ydyN6iJtvaB5riXLLxSq6SHKW3b7JCejJLYm%2B183yqefQhusbXWzh5KhvIAz%2BrJtSJZrKIQzlYO8boMPzRFWiPiWcqO8Px6v964DRSYL6AL9pURXoh7PYBIFctW5DLVP8lxr0bLv6WPvAMkezHEcyDI8fXyK81dcG1Ekv5bXr%2FCM%2FBHkUrfXwYTEppHQZqp0XPCzpzBVG%2Fd5vs1arS1YltZ5UXngIw%2B3sHaT%2FURTybD%2Bmgw7Vy3IKcXRLAT7tdjWq89MlprO1RV%2BFA6gfFonuDxw%2FyJjxXCApNumMpMvEXaIpMfMfSqs26%2FTFBQbwrVr9pNI7s9h9emLw8lUoQocgykbzUlKW1WOoYKrdXruGKfOIGNlND0K%2BdSlNWSKrjwjC%2BCG0MNS3xMgGOqUBXtn7n0ds9nVqQRCqG5ZvxdUiAvll%2Bx%2F1KOKM089%2BNbh6%2Be6BPU2k%2FI5rKZOcSZIHONc7SWAv4KD7R8xxRO93sKLMHzIBnj1IUg5p%2B%2F8J%2BO%2BKA8eMlcMcofGDCoEbE%2B1FmfvcdvW6atY9ZyfR4GGIsPqr99pDDashamz2O7z96ZZF%2FoqJThNmk2NStc%2FnwUgxdMphLvepbdVYvLMJ%2Bx6tsx9opFkC&X-Amz-Signature=a3fd132ad193290baaa9c9b52a72b619ed117493c3ec597966fa0fb0f4ffd615&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSELROG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGVc%2B5PzvjBHeL6AsrYk%2BoIf2KMNU3oC4bh6CBre0ifHAiEA7ewrsn4FC9WM8A6MyKTVdfD0GOZ82I8U1AyHDXsu7vYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrU6%2B5XOl%2FMwh8pzCrcA3lp37r5DvrU1wORQh3KLEORh%2BfXeB53qf2HP5FDT85l1rVEdXtn8JgMALJpDy2WvVl46fbkeVqhwwg17POgg2EkenT2HlwJbjcKs78nEO5Pxp3XzXMAZBaYOqTaxzizGZoAFMo1id6VgOHzTihLVLGhcXh%2Fs9cgDf0gNatYtY8YbDQAAyJ9SvvC76BigmDoiSTy2F2zAwcyk5CCajy3epdEe06aEMKp9%2FG2hokc6erk60OrrpXVEA2ydyN6iJtvaB5riXLLxSq6SHKW3b7JCejJLYm%2B183yqefQhusbXWzh5KhvIAz%2BrJtSJZrKIQzlYO8boMPzRFWiPiWcqO8Px6v964DRSYL6AL9pURXoh7PYBIFctW5DLVP8lxr0bLv6WPvAMkezHEcyDI8fXyK81dcG1Ekv5bXr%2FCM%2FBHkUrfXwYTEppHQZqp0XPCzpzBVG%2Fd5vs1arS1YltZ5UXngIw%2B3sHaT%2FURTybD%2Bmgw7Vy3IKcXRLAT7tdjWq89MlprO1RV%2BFA6gfFonuDxw%2FyJjxXCApNumMpMvEXaIpMfMfSqs26%2FTFBQbwrVr9pNI7s9h9emLw8lUoQocgykbzUlKW1WOoYKrdXruGKfOIGNlND0K%2BdSlNWSKrjwjC%2BCG0MNS3xMgGOqUBXtn7n0ds9nVqQRCqG5ZvxdUiAvll%2Bx%2F1KOKM089%2BNbh6%2Be6BPU2k%2FI5rKZOcSZIHONc7SWAv4KD7R8xxRO93sKLMHzIBnj1IUg5p%2B%2F8J%2BO%2BKA8eMlcMcofGDCoEbE%2B1FmfvcdvW6atY9ZyfR4GGIsPqr99pDDashamz2O7z96ZZF%2FoqJThNmk2NStc%2FnwUgxdMphLvepbdVYvLMJ%2Bx6tsx9opFkC&X-Amz-Signature=816a603add5b85d5d931180ad5cba6374bda913822462274a321d9750517a94a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSELROG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGVc%2B5PzvjBHeL6AsrYk%2BoIf2KMNU3oC4bh6CBre0ifHAiEA7ewrsn4FC9WM8A6MyKTVdfD0GOZ82I8U1AyHDXsu7vYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrU6%2B5XOl%2FMwh8pzCrcA3lp37r5DvrU1wORQh3KLEORh%2BfXeB53qf2HP5FDT85l1rVEdXtn8JgMALJpDy2WvVl46fbkeVqhwwg17POgg2EkenT2HlwJbjcKs78nEO5Pxp3XzXMAZBaYOqTaxzizGZoAFMo1id6VgOHzTihLVLGhcXh%2Fs9cgDf0gNatYtY8YbDQAAyJ9SvvC76BigmDoiSTy2F2zAwcyk5CCajy3epdEe06aEMKp9%2FG2hokc6erk60OrrpXVEA2ydyN6iJtvaB5riXLLxSq6SHKW3b7JCejJLYm%2B183yqefQhusbXWzh5KhvIAz%2BrJtSJZrKIQzlYO8boMPzRFWiPiWcqO8Px6v964DRSYL6AL9pURXoh7PYBIFctW5DLVP8lxr0bLv6WPvAMkezHEcyDI8fXyK81dcG1Ekv5bXr%2FCM%2FBHkUrfXwYTEppHQZqp0XPCzpzBVG%2Fd5vs1arS1YltZ5UXngIw%2B3sHaT%2FURTybD%2Bmgw7Vy3IKcXRLAT7tdjWq89MlprO1RV%2BFA6gfFonuDxw%2FyJjxXCApNumMpMvEXaIpMfMfSqs26%2FTFBQbwrVr9pNI7s9h9emLw8lUoQocgykbzUlKW1WOoYKrdXruGKfOIGNlND0K%2BdSlNWSKrjwjC%2BCG0MNS3xMgGOqUBXtn7n0ds9nVqQRCqG5ZvxdUiAvll%2Bx%2F1KOKM089%2BNbh6%2Be6BPU2k%2FI5rKZOcSZIHONc7SWAv4KD7R8xxRO93sKLMHzIBnj1IUg5p%2B%2F8J%2BO%2BKA8eMlcMcofGDCoEbE%2B1FmfvcdvW6atY9ZyfR4GGIsPqr99pDDashamz2O7z96ZZF%2FoqJThNmk2NStc%2FnwUgxdMphLvepbdVYvLMJ%2Bx6tsx9opFkC&X-Amz-Signature=c3696ea6caa5be14679591b76e9b81d0eb66809e306774944c3653d03ffc02df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFSELROG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIGVc%2B5PzvjBHeL6AsrYk%2BoIf2KMNU3oC4bh6CBre0ifHAiEA7ewrsn4FC9WM8A6MyKTVdfD0GOZ82I8U1AyHDXsu7vYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKrU6%2B5XOl%2FMwh8pzCrcA3lp37r5DvrU1wORQh3KLEORh%2BfXeB53qf2HP5FDT85l1rVEdXtn8JgMALJpDy2WvVl46fbkeVqhwwg17POgg2EkenT2HlwJbjcKs78nEO5Pxp3XzXMAZBaYOqTaxzizGZoAFMo1id6VgOHzTihLVLGhcXh%2Fs9cgDf0gNatYtY8YbDQAAyJ9SvvC76BigmDoiSTy2F2zAwcyk5CCajy3epdEe06aEMKp9%2FG2hokc6erk60OrrpXVEA2ydyN6iJtvaB5riXLLxSq6SHKW3b7JCejJLYm%2B183yqefQhusbXWzh5KhvIAz%2BrJtSJZrKIQzlYO8boMPzRFWiPiWcqO8Px6v964DRSYL6AL9pURXoh7PYBIFctW5DLVP8lxr0bLv6WPvAMkezHEcyDI8fXyK81dcG1Ekv5bXr%2FCM%2FBHkUrfXwYTEppHQZqp0XPCzpzBVG%2Fd5vs1arS1YltZ5UXngIw%2B3sHaT%2FURTybD%2Bmgw7Vy3IKcXRLAT7tdjWq89MlprO1RV%2BFA6gfFonuDxw%2FyJjxXCApNumMpMvEXaIpMfMfSqs26%2FTFBQbwrVr9pNI7s9h9emLw8lUoQocgykbzUlKW1WOoYKrdXruGKfOIGNlND0K%2BdSlNWSKrjwjC%2BCG0MNS3xMgGOqUBXtn7n0ds9nVqQRCqG5ZvxdUiAvll%2Bx%2F1KOKM089%2BNbh6%2Be6BPU2k%2FI5rKZOcSZIHONc7SWAv4KD7R8xxRO93sKLMHzIBnj1IUg5p%2B%2F8J%2BO%2BKA8eMlcMcofGDCoEbE%2B1FmfvcdvW6atY9ZyfR4GGIsPqr99pDDashamz2O7z96ZZF%2FoqJThNmk2NStc%2FnwUgxdMphLvepbdVYvLMJ%2Bx6tsx9opFkC&X-Amz-Signature=a8aa5cbafe37a8ed1cbd9bc435bffa3f69554af3d30e279cf395561225bafa41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

