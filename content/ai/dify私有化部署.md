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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLJ24DL4%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCATaevt7V%2B9zG7C12FDpgWDlqGjFWdhT50Bv4DSDenbwIgOc6%2FLp2H7MhmdZ72mm7%2FCZWKp4eUW1%2BZe1bAlZUluOgq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJy4IUlOsEZ26YTt6CrcA2QTmg3rUkxNU5ZJkHnscQNHXxojvRn6D43%2FwhWe%2B5aDTKd7pqI14ezb1IkBy1LpyxLpoPFUXIFL2be%2FHL9IQRn73YbOa3IZZ2VekRscKhOGMQDenp%2BslIaJsiqv%2FZx%2BNLwq44PfiMjkMA%2B35h8TziDGYSs7v8QQwrKLKRpQsAUaS09%2FP4zQnvzWB0%2Fg8CJlk7Pv13MpfOd%2FjSfNgYbm3WMinIlPIQrt4IsKiCgBRv%2BS69hso6VwjODza77fZAHW5V61tb1zd%2BwRDaP4OBK5fiKDD51%2B7BcsWxGbcXTveiOViwZLi%2FKaCutamy7rWZ2%2FW0PuGxF6xceKTqz877sFs3RnI83GS5k0WKeMpJWqNgWTVisefaLRfj8INzNz0kqg9fTAg3uBrbgH%2BkzxzPCwGUhMOS9dyEXCgh5eM9ULngrZLDUzbK8pvkZ2%2Fq83Kd%2BDbFp7NUZm3gTB%2FsyJHmDjwHkQXsGebxm3dqqlUMmHaWGVq8fbaOmSnbeP1Z%2BF01VgyCxXZ3Gb%2BzAprsebxb6SiEfz76O%2FiL915wMkXAIGFodhb1X5H9OJwyiEKnYNJQhC81HBZ9sAUuSGxtUG11tRTFtSlxuZb2gnZFiOjkDKsW%2F2pub3hiETjchbeSG%2FMOTurM4GOqUBCm%2BNfOrLLWuD4Gu6LOvd47LeJEFsNyOKbP3kgPjde0SIDrPpbmEeUai90iUaOORTCVqkQEqZbDA8RB27MBEC77SGYqBVbw7pBnsCJois2JmuMuxL%2BEbf91gCtXNsxeXiHsX1exyyg63znFNS482MU8Hs14giVR9CvHEI98Hsj%2FbAi2Z6KswCBs394c%2Fvh0Fy6Sbcs%2FdkhwkUO7uBQcY9dgcYb5d4&X-Amz-Signature=c41f759af3f18d979e4b6f35344c9a57c68b7b244b52a3804c13c066fd43079b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLJ24DL4%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCATaevt7V%2B9zG7C12FDpgWDlqGjFWdhT50Bv4DSDenbwIgOc6%2FLp2H7MhmdZ72mm7%2FCZWKp4eUW1%2BZe1bAlZUluOgq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJy4IUlOsEZ26YTt6CrcA2QTmg3rUkxNU5ZJkHnscQNHXxojvRn6D43%2FwhWe%2B5aDTKd7pqI14ezb1IkBy1LpyxLpoPFUXIFL2be%2FHL9IQRn73YbOa3IZZ2VekRscKhOGMQDenp%2BslIaJsiqv%2FZx%2BNLwq44PfiMjkMA%2B35h8TziDGYSs7v8QQwrKLKRpQsAUaS09%2FP4zQnvzWB0%2Fg8CJlk7Pv13MpfOd%2FjSfNgYbm3WMinIlPIQrt4IsKiCgBRv%2BS69hso6VwjODza77fZAHW5V61tb1zd%2BwRDaP4OBK5fiKDD51%2B7BcsWxGbcXTveiOViwZLi%2FKaCutamy7rWZ2%2FW0PuGxF6xceKTqz877sFs3RnI83GS5k0WKeMpJWqNgWTVisefaLRfj8INzNz0kqg9fTAg3uBrbgH%2BkzxzPCwGUhMOS9dyEXCgh5eM9ULngrZLDUzbK8pvkZ2%2Fq83Kd%2BDbFp7NUZm3gTB%2FsyJHmDjwHkQXsGebxm3dqqlUMmHaWGVq8fbaOmSnbeP1Z%2BF01VgyCxXZ3Gb%2BzAprsebxb6SiEfz76O%2FiL915wMkXAIGFodhb1X5H9OJwyiEKnYNJQhC81HBZ9sAUuSGxtUG11tRTFtSlxuZb2gnZFiOjkDKsW%2F2pub3hiETjchbeSG%2FMOTurM4GOqUBCm%2BNfOrLLWuD4Gu6LOvd47LeJEFsNyOKbP3kgPjde0SIDrPpbmEeUai90iUaOORTCVqkQEqZbDA8RB27MBEC77SGYqBVbw7pBnsCJois2JmuMuxL%2BEbf91gCtXNsxeXiHsX1exyyg63znFNS482MU8Hs14giVR9CvHEI98Hsj%2FbAi2Z6KswCBs394c%2Fvh0Fy6Sbcs%2FdkhwkUO7uBQcY9dgcYb5d4&X-Amz-Signature=45c092029fa8b3575a82dbb92e83836be71945af6efb233e14d9ad539eb38b35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLJ24DL4%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCATaevt7V%2B9zG7C12FDpgWDlqGjFWdhT50Bv4DSDenbwIgOc6%2FLp2H7MhmdZ72mm7%2FCZWKp4eUW1%2BZe1bAlZUluOgq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJy4IUlOsEZ26YTt6CrcA2QTmg3rUkxNU5ZJkHnscQNHXxojvRn6D43%2FwhWe%2B5aDTKd7pqI14ezb1IkBy1LpyxLpoPFUXIFL2be%2FHL9IQRn73YbOa3IZZ2VekRscKhOGMQDenp%2BslIaJsiqv%2FZx%2BNLwq44PfiMjkMA%2B35h8TziDGYSs7v8QQwrKLKRpQsAUaS09%2FP4zQnvzWB0%2Fg8CJlk7Pv13MpfOd%2FjSfNgYbm3WMinIlPIQrt4IsKiCgBRv%2BS69hso6VwjODza77fZAHW5V61tb1zd%2BwRDaP4OBK5fiKDD51%2B7BcsWxGbcXTveiOViwZLi%2FKaCutamy7rWZ2%2FW0PuGxF6xceKTqz877sFs3RnI83GS5k0WKeMpJWqNgWTVisefaLRfj8INzNz0kqg9fTAg3uBrbgH%2BkzxzPCwGUhMOS9dyEXCgh5eM9ULngrZLDUzbK8pvkZ2%2Fq83Kd%2BDbFp7NUZm3gTB%2FsyJHmDjwHkQXsGebxm3dqqlUMmHaWGVq8fbaOmSnbeP1Z%2BF01VgyCxXZ3Gb%2BzAprsebxb6SiEfz76O%2FiL915wMkXAIGFodhb1X5H9OJwyiEKnYNJQhC81HBZ9sAUuSGxtUG11tRTFtSlxuZb2gnZFiOjkDKsW%2F2pub3hiETjchbeSG%2FMOTurM4GOqUBCm%2BNfOrLLWuD4Gu6LOvd47LeJEFsNyOKbP3kgPjde0SIDrPpbmEeUai90iUaOORTCVqkQEqZbDA8RB27MBEC77SGYqBVbw7pBnsCJois2JmuMuxL%2BEbf91gCtXNsxeXiHsX1exyyg63znFNS482MU8Hs14giVR9CvHEI98Hsj%2FbAi2Z6KswCBs394c%2Fvh0Fy6Sbcs%2FdkhwkUO7uBQcY9dgcYb5d4&X-Amz-Signature=fba108aa0be343d0b464ce4522ebfa8a67dd362e2944bc2f94a57424f4b94f28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLJ24DL4%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCATaevt7V%2B9zG7C12FDpgWDlqGjFWdhT50Bv4DSDenbwIgOc6%2FLp2H7MhmdZ72mm7%2FCZWKp4eUW1%2BZe1bAlZUluOgq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJy4IUlOsEZ26YTt6CrcA2QTmg3rUkxNU5ZJkHnscQNHXxojvRn6D43%2FwhWe%2B5aDTKd7pqI14ezb1IkBy1LpyxLpoPFUXIFL2be%2FHL9IQRn73YbOa3IZZ2VekRscKhOGMQDenp%2BslIaJsiqv%2FZx%2BNLwq44PfiMjkMA%2B35h8TziDGYSs7v8QQwrKLKRpQsAUaS09%2FP4zQnvzWB0%2Fg8CJlk7Pv13MpfOd%2FjSfNgYbm3WMinIlPIQrt4IsKiCgBRv%2BS69hso6VwjODza77fZAHW5V61tb1zd%2BwRDaP4OBK5fiKDD51%2B7BcsWxGbcXTveiOViwZLi%2FKaCutamy7rWZ2%2FW0PuGxF6xceKTqz877sFs3RnI83GS5k0WKeMpJWqNgWTVisefaLRfj8INzNz0kqg9fTAg3uBrbgH%2BkzxzPCwGUhMOS9dyEXCgh5eM9ULngrZLDUzbK8pvkZ2%2Fq83Kd%2BDbFp7NUZm3gTB%2FsyJHmDjwHkQXsGebxm3dqqlUMmHaWGVq8fbaOmSnbeP1Z%2BF01VgyCxXZ3Gb%2BzAprsebxb6SiEfz76O%2FiL915wMkXAIGFodhb1X5H9OJwyiEKnYNJQhC81HBZ9sAUuSGxtUG11tRTFtSlxuZb2gnZFiOjkDKsW%2F2pub3hiETjchbeSG%2FMOTurM4GOqUBCm%2BNfOrLLWuD4Gu6LOvd47LeJEFsNyOKbP3kgPjde0SIDrPpbmEeUai90iUaOORTCVqkQEqZbDA8RB27MBEC77SGYqBVbw7pBnsCJois2JmuMuxL%2BEbf91gCtXNsxeXiHsX1exyyg63znFNS482MU8Hs14giVR9CvHEI98Hsj%2FbAi2Z6KswCBs394c%2Fvh0Fy6Sbcs%2FdkhwkUO7uBQcY9dgcYb5d4&X-Amz-Signature=f9b13c40920927f37fc304212dda2292fdcef6bd037c830eef6c8fd3fe7ae4bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLJ24DL4%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCATaevt7V%2B9zG7C12FDpgWDlqGjFWdhT50Bv4DSDenbwIgOc6%2FLp2H7MhmdZ72mm7%2FCZWKp4eUW1%2BZe1bAlZUluOgq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJy4IUlOsEZ26YTt6CrcA2QTmg3rUkxNU5ZJkHnscQNHXxojvRn6D43%2FwhWe%2B5aDTKd7pqI14ezb1IkBy1LpyxLpoPFUXIFL2be%2FHL9IQRn73YbOa3IZZ2VekRscKhOGMQDenp%2BslIaJsiqv%2FZx%2BNLwq44PfiMjkMA%2B35h8TziDGYSs7v8QQwrKLKRpQsAUaS09%2FP4zQnvzWB0%2Fg8CJlk7Pv13MpfOd%2FjSfNgYbm3WMinIlPIQrt4IsKiCgBRv%2BS69hso6VwjODza77fZAHW5V61tb1zd%2BwRDaP4OBK5fiKDD51%2B7BcsWxGbcXTveiOViwZLi%2FKaCutamy7rWZ2%2FW0PuGxF6xceKTqz877sFs3RnI83GS5k0WKeMpJWqNgWTVisefaLRfj8INzNz0kqg9fTAg3uBrbgH%2BkzxzPCwGUhMOS9dyEXCgh5eM9ULngrZLDUzbK8pvkZ2%2Fq83Kd%2BDbFp7NUZm3gTB%2FsyJHmDjwHkQXsGebxm3dqqlUMmHaWGVq8fbaOmSnbeP1Z%2BF01VgyCxXZ3Gb%2BzAprsebxb6SiEfz76O%2FiL915wMkXAIGFodhb1X5H9OJwyiEKnYNJQhC81HBZ9sAUuSGxtUG11tRTFtSlxuZb2gnZFiOjkDKsW%2F2pub3hiETjchbeSG%2FMOTurM4GOqUBCm%2BNfOrLLWuD4Gu6LOvd47LeJEFsNyOKbP3kgPjde0SIDrPpbmEeUai90iUaOORTCVqkQEqZbDA8RB27MBEC77SGYqBVbw7pBnsCJois2JmuMuxL%2BEbf91gCtXNsxeXiHsX1exyyg63znFNS482MU8Hs14giVR9CvHEI98Hsj%2FbAi2Z6KswCBs394c%2Fvh0Fy6Sbcs%2FdkhwkUO7uBQcY9dgcYb5d4&X-Amz-Signature=55b13bf6ad5c1c46716c05257d2aaa5f75f65359b1a6703d63bed7027ff939fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLJ24DL4%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCATaevt7V%2B9zG7C12FDpgWDlqGjFWdhT50Bv4DSDenbwIgOc6%2FLp2H7MhmdZ72mm7%2FCZWKp4eUW1%2BZe1bAlZUluOgq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJy4IUlOsEZ26YTt6CrcA2QTmg3rUkxNU5ZJkHnscQNHXxojvRn6D43%2FwhWe%2B5aDTKd7pqI14ezb1IkBy1LpyxLpoPFUXIFL2be%2FHL9IQRn73YbOa3IZZ2VekRscKhOGMQDenp%2BslIaJsiqv%2FZx%2BNLwq44PfiMjkMA%2B35h8TziDGYSs7v8QQwrKLKRpQsAUaS09%2FP4zQnvzWB0%2Fg8CJlk7Pv13MpfOd%2FjSfNgYbm3WMinIlPIQrt4IsKiCgBRv%2BS69hso6VwjODza77fZAHW5V61tb1zd%2BwRDaP4OBK5fiKDD51%2B7BcsWxGbcXTveiOViwZLi%2FKaCutamy7rWZ2%2FW0PuGxF6xceKTqz877sFs3RnI83GS5k0WKeMpJWqNgWTVisefaLRfj8INzNz0kqg9fTAg3uBrbgH%2BkzxzPCwGUhMOS9dyEXCgh5eM9ULngrZLDUzbK8pvkZ2%2Fq83Kd%2BDbFp7NUZm3gTB%2FsyJHmDjwHkQXsGebxm3dqqlUMmHaWGVq8fbaOmSnbeP1Z%2BF01VgyCxXZ3Gb%2BzAprsebxb6SiEfz76O%2FiL915wMkXAIGFodhb1X5H9OJwyiEKnYNJQhC81HBZ9sAUuSGxtUG11tRTFtSlxuZb2gnZFiOjkDKsW%2F2pub3hiETjchbeSG%2FMOTurM4GOqUBCm%2BNfOrLLWuD4Gu6LOvd47LeJEFsNyOKbP3kgPjde0SIDrPpbmEeUai90iUaOORTCVqkQEqZbDA8RB27MBEC77SGYqBVbw7pBnsCJois2JmuMuxL%2BEbf91gCtXNsxeXiHsX1exyyg63znFNS482MU8Hs14giVR9CvHEI98Hsj%2FbAi2Z6KswCBs394c%2Fvh0Fy6Sbcs%2FdkhwkUO7uBQcY9dgcYb5d4&X-Amz-Signature=135128e4c5e01bc6d01153448d7d46af80833db055efa6b4c0b27e386cd551e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLJ24DL4%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCATaevt7V%2B9zG7C12FDpgWDlqGjFWdhT50Bv4DSDenbwIgOc6%2FLp2H7MhmdZ72mm7%2FCZWKp4eUW1%2BZe1bAlZUluOgq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJy4IUlOsEZ26YTt6CrcA2QTmg3rUkxNU5ZJkHnscQNHXxojvRn6D43%2FwhWe%2B5aDTKd7pqI14ezb1IkBy1LpyxLpoPFUXIFL2be%2FHL9IQRn73YbOa3IZZ2VekRscKhOGMQDenp%2BslIaJsiqv%2FZx%2BNLwq44PfiMjkMA%2B35h8TziDGYSs7v8QQwrKLKRpQsAUaS09%2FP4zQnvzWB0%2Fg8CJlk7Pv13MpfOd%2FjSfNgYbm3WMinIlPIQrt4IsKiCgBRv%2BS69hso6VwjODza77fZAHW5V61tb1zd%2BwRDaP4OBK5fiKDD51%2B7BcsWxGbcXTveiOViwZLi%2FKaCutamy7rWZ2%2FW0PuGxF6xceKTqz877sFs3RnI83GS5k0WKeMpJWqNgWTVisefaLRfj8INzNz0kqg9fTAg3uBrbgH%2BkzxzPCwGUhMOS9dyEXCgh5eM9ULngrZLDUzbK8pvkZ2%2Fq83Kd%2BDbFp7NUZm3gTB%2FsyJHmDjwHkQXsGebxm3dqqlUMmHaWGVq8fbaOmSnbeP1Z%2BF01VgyCxXZ3Gb%2BzAprsebxb6SiEfz76O%2FiL915wMkXAIGFodhb1X5H9OJwyiEKnYNJQhC81HBZ9sAUuSGxtUG11tRTFtSlxuZb2gnZFiOjkDKsW%2F2pub3hiETjchbeSG%2FMOTurM4GOqUBCm%2BNfOrLLWuD4Gu6LOvd47LeJEFsNyOKbP3kgPjde0SIDrPpbmEeUai90iUaOORTCVqkQEqZbDA8RB27MBEC77SGYqBVbw7pBnsCJois2JmuMuxL%2BEbf91gCtXNsxeXiHsX1exyyg63znFNS482MU8Hs14giVR9CvHEI98Hsj%2FbAi2Z6KswCBs394c%2Fvh0Fy6Sbcs%2FdkhwkUO7uBQcY9dgcYb5d4&X-Amz-Signature=c2be1d6ae8255fc3583cd87debe4c1a12ce494afd7d93005706e922a4c26c6f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLJ24DL4%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCATaevt7V%2B9zG7C12FDpgWDlqGjFWdhT50Bv4DSDenbwIgOc6%2FLp2H7MhmdZ72mm7%2FCZWKp4eUW1%2BZe1bAlZUluOgq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJy4IUlOsEZ26YTt6CrcA2QTmg3rUkxNU5ZJkHnscQNHXxojvRn6D43%2FwhWe%2B5aDTKd7pqI14ezb1IkBy1LpyxLpoPFUXIFL2be%2FHL9IQRn73YbOa3IZZ2VekRscKhOGMQDenp%2BslIaJsiqv%2FZx%2BNLwq44PfiMjkMA%2B35h8TziDGYSs7v8QQwrKLKRpQsAUaS09%2FP4zQnvzWB0%2Fg8CJlk7Pv13MpfOd%2FjSfNgYbm3WMinIlPIQrt4IsKiCgBRv%2BS69hso6VwjODza77fZAHW5V61tb1zd%2BwRDaP4OBK5fiKDD51%2B7BcsWxGbcXTveiOViwZLi%2FKaCutamy7rWZ2%2FW0PuGxF6xceKTqz877sFs3RnI83GS5k0WKeMpJWqNgWTVisefaLRfj8INzNz0kqg9fTAg3uBrbgH%2BkzxzPCwGUhMOS9dyEXCgh5eM9ULngrZLDUzbK8pvkZ2%2Fq83Kd%2BDbFp7NUZm3gTB%2FsyJHmDjwHkQXsGebxm3dqqlUMmHaWGVq8fbaOmSnbeP1Z%2BF01VgyCxXZ3Gb%2BzAprsebxb6SiEfz76O%2FiL915wMkXAIGFodhb1X5H9OJwyiEKnYNJQhC81HBZ9sAUuSGxtUG11tRTFtSlxuZb2gnZFiOjkDKsW%2F2pub3hiETjchbeSG%2FMOTurM4GOqUBCm%2BNfOrLLWuD4Gu6LOvd47LeJEFsNyOKbP3kgPjde0SIDrPpbmEeUai90iUaOORTCVqkQEqZbDA8RB27MBEC77SGYqBVbw7pBnsCJois2JmuMuxL%2BEbf91gCtXNsxeXiHsX1exyyg63znFNS482MU8Hs14giVR9CvHEI98Hsj%2FbAi2Z6KswCBs394c%2Fvh0Fy6Sbcs%2FdkhwkUO7uBQcY9dgcYb5d4&X-Amz-Signature=190560075b5ac01f6ba519c407c00e7654ebadc1eb22010219493fca3afc116e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLJ24DL4%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCATaevt7V%2B9zG7C12FDpgWDlqGjFWdhT50Bv4DSDenbwIgOc6%2FLp2H7MhmdZ72mm7%2FCZWKp4eUW1%2BZe1bAlZUluOgq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJy4IUlOsEZ26YTt6CrcA2QTmg3rUkxNU5ZJkHnscQNHXxojvRn6D43%2FwhWe%2B5aDTKd7pqI14ezb1IkBy1LpyxLpoPFUXIFL2be%2FHL9IQRn73YbOa3IZZ2VekRscKhOGMQDenp%2BslIaJsiqv%2FZx%2BNLwq44PfiMjkMA%2B35h8TziDGYSs7v8QQwrKLKRpQsAUaS09%2FP4zQnvzWB0%2Fg8CJlk7Pv13MpfOd%2FjSfNgYbm3WMinIlPIQrt4IsKiCgBRv%2BS69hso6VwjODza77fZAHW5V61tb1zd%2BwRDaP4OBK5fiKDD51%2B7BcsWxGbcXTveiOViwZLi%2FKaCutamy7rWZ2%2FW0PuGxF6xceKTqz877sFs3RnI83GS5k0WKeMpJWqNgWTVisefaLRfj8INzNz0kqg9fTAg3uBrbgH%2BkzxzPCwGUhMOS9dyEXCgh5eM9ULngrZLDUzbK8pvkZ2%2Fq83Kd%2BDbFp7NUZm3gTB%2FsyJHmDjwHkQXsGebxm3dqqlUMmHaWGVq8fbaOmSnbeP1Z%2BF01VgyCxXZ3Gb%2BzAprsebxb6SiEfz76O%2FiL915wMkXAIGFodhb1X5H9OJwyiEKnYNJQhC81HBZ9sAUuSGxtUG11tRTFtSlxuZb2gnZFiOjkDKsW%2F2pub3hiETjchbeSG%2FMOTurM4GOqUBCm%2BNfOrLLWuD4Gu6LOvd47LeJEFsNyOKbP3kgPjde0SIDrPpbmEeUai90iUaOORTCVqkQEqZbDA8RB27MBEC77SGYqBVbw7pBnsCJois2JmuMuxL%2BEbf91gCtXNsxeXiHsX1exyyg63znFNS482MU8Hs14giVR9CvHEI98Hsj%2FbAi2Z6KswCBs394c%2Fvh0Fy6Sbcs%2FdkhwkUO7uBQcY9dgcYb5d4&X-Amz-Signature=fd794192f4c662395d2ed16f04e61ab01471755e86b995d3d453d121ee0dbd03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLJ24DL4%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCATaevt7V%2B9zG7C12FDpgWDlqGjFWdhT50Bv4DSDenbwIgOc6%2FLp2H7MhmdZ72mm7%2FCZWKp4eUW1%2BZe1bAlZUluOgq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJy4IUlOsEZ26YTt6CrcA2QTmg3rUkxNU5ZJkHnscQNHXxojvRn6D43%2FwhWe%2B5aDTKd7pqI14ezb1IkBy1LpyxLpoPFUXIFL2be%2FHL9IQRn73YbOa3IZZ2VekRscKhOGMQDenp%2BslIaJsiqv%2FZx%2BNLwq44PfiMjkMA%2B35h8TziDGYSs7v8QQwrKLKRpQsAUaS09%2FP4zQnvzWB0%2Fg8CJlk7Pv13MpfOd%2FjSfNgYbm3WMinIlPIQrt4IsKiCgBRv%2BS69hso6VwjODza77fZAHW5V61tb1zd%2BwRDaP4OBK5fiKDD51%2B7BcsWxGbcXTveiOViwZLi%2FKaCutamy7rWZ2%2FW0PuGxF6xceKTqz877sFs3RnI83GS5k0WKeMpJWqNgWTVisefaLRfj8INzNz0kqg9fTAg3uBrbgH%2BkzxzPCwGUhMOS9dyEXCgh5eM9ULngrZLDUzbK8pvkZ2%2Fq83Kd%2BDbFp7NUZm3gTB%2FsyJHmDjwHkQXsGebxm3dqqlUMmHaWGVq8fbaOmSnbeP1Z%2BF01VgyCxXZ3Gb%2BzAprsebxb6SiEfz76O%2FiL915wMkXAIGFodhb1X5H9OJwyiEKnYNJQhC81HBZ9sAUuSGxtUG11tRTFtSlxuZb2gnZFiOjkDKsW%2F2pub3hiETjchbeSG%2FMOTurM4GOqUBCm%2BNfOrLLWuD4Gu6LOvd47LeJEFsNyOKbP3kgPjde0SIDrPpbmEeUai90iUaOORTCVqkQEqZbDA8RB27MBEC77SGYqBVbw7pBnsCJois2JmuMuxL%2BEbf91gCtXNsxeXiHsX1exyyg63znFNS482MU8Hs14giVR9CvHEI98Hsj%2FbAi2Z6KswCBs394c%2Fvh0Fy6Sbcs%2FdkhwkUO7uBQcY9dgcYb5d4&X-Amz-Signature=7c94423c503c1bac2095be250e8cac799156e450eac6095bbd12c34c618d3ee1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

