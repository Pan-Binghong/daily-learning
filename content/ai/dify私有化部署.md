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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFDSM45G%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNMQzcVtgeQ%2BcO4GXr%2FJrWLpaUt2UFFqWbxX6v9v0KdAiAfatrTLtG3b5D14fld%2BnB4ta%2BTYe44qyFjl07bwQGT3iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMz5BBhOop0HtmMDOKtwDcdGtNFMgS05R9FDcbWfZv8pTXhun02ousSdWoIvFV9dgkPbqASmEHbRqeTuDduGECjD6Zr7N5alXwmF4nZeDgGf4Ew%2FY%2B1u2p%2BNdrHSudvMphBfSqas5qAM%2FANRG%2FHfvHd5hjDu9gfuetAqN9DSWh%2FVHzY5ajHpgZoYkTl%2FH5Fq4P8Y%2BwRRdW3qZKtfkUALWSm97ygO93RHR7JjykSpQ4leVhrgchxVSvXtxqNIvgSH30mP%2Fxz0ocLem6Ib6xrzDElA3TMX5%2B%2Foj6JvcEfwELHnkb3Gf2WGucHF%2F7kme7Uh8vBd9zKTZy39yAGEB4IqXUn1BotjhHtxrReOhzCR90eJr4xhPBzUXl6CgWBvl2aAtxS2CSxGRQksJHEuQ7f8CM1YYhy0k3w3AdClMv%2BC5dWG1%2F8oUzPqUwgohPN2ceo5R6A6mTbnubctdZ2TVo%2FMmzWE06FvkjZeEL1diJu5K0diiHNXriewQ%2FBpmtEqmxwZREXiygMVwUAEEEhBKx%2BYEBOL%2BxFmCX293wCB7gLYMcwkGKQnh4kS1O2RWlgcfDF4JIOO4nR7%2BSsH4ZGAEsBQQ1n1EqoPpEYznLyEye%2BhPB%2BIAmkfSp2KeYDipA3WIwm%2FOfc8tUtiEn5v%2BUjMwio%2FeyQY6pgG2b9jZM0KuDvcvXa7dpmL9NpsXrpEJGE9WOwL9EDuKhxCPSwfzGt4VDfkLe027RR9TL4oKvSphPmfAR%2Fnw6VewqOWtQdEcbf7hk%2FbmLdeI%2BLzhyF4tuH6eEhcxVH5GsFq7zbEz6XYqnG97R71eikR4y8ZtSgA8TBiHoMUSlk0pnBeMaxfQSc4und1qSpw%2Bd3JgSqGkeKpN29PnNuHeaa6QR4wAM1kt&X-Amz-Signature=63453aa7f16c1f2c43b4acff13b4ab6eaa71e1aab19148c63072e3605ba788f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFDSM45G%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNMQzcVtgeQ%2BcO4GXr%2FJrWLpaUt2UFFqWbxX6v9v0KdAiAfatrTLtG3b5D14fld%2BnB4ta%2BTYe44qyFjl07bwQGT3iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMz5BBhOop0HtmMDOKtwDcdGtNFMgS05R9FDcbWfZv8pTXhun02ousSdWoIvFV9dgkPbqASmEHbRqeTuDduGECjD6Zr7N5alXwmF4nZeDgGf4Ew%2FY%2B1u2p%2BNdrHSudvMphBfSqas5qAM%2FANRG%2FHfvHd5hjDu9gfuetAqN9DSWh%2FVHzY5ajHpgZoYkTl%2FH5Fq4P8Y%2BwRRdW3qZKtfkUALWSm97ygO93RHR7JjykSpQ4leVhrgchxVSvXtxqNIvgSH30mP%2Fxz0ocLem6Ib6xrzDElA3TMX5%2B%2Foj6JvcEfwELHnkb3Gf2WGucHF%2F7kme7Uh8vBd9zKTZy39yAGEB4IqXUn1BotjhHtxrReOhzCR90eJr4xhPBzUXl6CgWBvl2aAtxS2CSxGRQksJHEuQ7f8CM1YYhy0k3w3AdClMv%2BC5dWG1%2F8oUzPqUwgohPN2ceo5R6A6mTbnubctdZ2TVo%2FMmzWE06FvkjZeEL1diJu5K0diiHNXriewQ%2FBpmtEqmxwZREXiygMVwUAEEEhBKx%2BYEBOL%2BxFmCX293wCB7gLYMcwkGKQnh4kS1O2RWlgcfDF4JIOO4nR7%2BSsH4ZGAEsBQQ1n1EqoPpEYznLyEye%2BhPB%2BIAmkfSp2KeYDipA3WIwm%2FOfc8tUtiEn5v%2BUjMwio%2FeyQY6pgG2b9jZM0KuDvcvXa7dpmL9NpsXrpEJGE9WOwL9EDuKhxCPSwfzGt4VDfkLe027RR9TL4oKvSphPmfAR%2Fnw6VewqOWtQdEcbf7hk%2FbmLdeI%2BLzhyF4tuH6eEhcxVH5GsFq7zbEz6XYqnG97R71eikR4y8ZtSgA8TBiHoMUSlk0pnBeMaxfQSc4und1qSpw%2Bd3JgSqGkeKpN29PnNuHeaa6QR4wAM1kt&X-Amz-Signature=8dc26e427a2ba9c5f150e3b70ef37cd0852581614b0c9a67057f6ac465565b51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFDSM45G%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNMQzcVtgeQ%2BcO4GXr%2FJrWLpaUt2UFFqWbxX6v9v0KdAiAfatrTLtG3b5D14fld%2BnB4ta%2BTYe44qyFjl07bwQGT3iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMz5BBhOop0HtmMDOKtwDcdGtNFMgS05R9FDcbWfZv8pTXhun02ousSdWoIvFV9dgkPbqASmEHbRqeTuDduGECjD6Zr7N5alXwmF4nZeDgGf4Ew%2FY%2B1u2p%2BNdrHSudvMphBfSqas5qAM%2FANRG%2FHfvHd5hjDu9gfuetAqN9DSWh%2FVHzY5ajHpgZoYkTl%2FH5Fq4P8Y%2BwRRdW3qZKtfkUALWSm97ygO93RHR7JjykSpQ4leVhrgchxVSvXtxqNIvgSH30mP%2Fxz0ocLem6Ib6xrzDElA3TMX5%2B%2Foj6JvcEfwELHnkb3Gf2WGucHF%2F7kme7Uh8vBd9zKTZy39yAGEB4IqXUn1BotjhHtxrReOhzCR90eJr4xhPBzUXl6CgWBvl2aAtxS2CSxGRQksJHEuQ7f8CM1YYhy0k3w3AdClMv%2BC5dWG1%2F8oUzPqUwgohPN2ceo5R6A6mTbnubctdZ2TVo%2FMmzWE06FvkjZeEL1diJu5K0diiHNXriewQ%2FBpmtEqmxwZREXiygMVwUAEEEhBKx%2BYEBOL%2BxFmCX293wCB7gLYMcwkGKQnh4kS1O2RWlgcfDF4JIOO4nR7%2BSsH4ZGAEsBQQ1n1EqoPpEYznLyEye%2BhPB%2BIAmkfSp2KeYDipA3WIwm%2FOfc8tUtiEn5v%2BUjMwio%2FeyQY6pgG2b9jZM0KuDvcvXa7dpmL9NpsXrpEJGE9WOwL9EDuKhxCPSwfzGt4VDfkLe027RR9TL4oKvSphPmfAR%2Fnw6VewqOWtQdEcbf7hk%2FbmLdeI%2BLzhyF4tuH6eEhcxVH5GsFq7zbEz6XYqnG97R71eikR4y8ZtSgA8TBiHoMUSlk0pnBeMaxfQSc4und1qSpw%2Bd3JgSqGkeKpN29PnNuHeaa6QR4wAM1kt&X-Amz-Signature=93b11775c7371a73fcc19c8e44f4bf9f62ac886d83b0b84369ee670985f736e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFDSM45G%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNMQzcVtgeQ%2BcO4GXr%2FJrWLpaUt2UFFqWbxX6v9v0KdAiAfatrTLtG3b5D14fld%2BnB4ta%2BTYe44qyFjl07bwQGT3iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMz5BBhOop0HtmMDOKtwDcdGtNFMgS05R9FDcbWfZv8pTXhun02ousSdWoIvFV9dgkPbqASmEHbRqeTuDduGECjD6Zr7N5alXwmF4nZeDgGf4Ew%2FY%2B1u2p%2BNdrHSudvMphBfSqas5qAM%2FANRG%2FHfvHd5hjDu9gfuetAqN9DSWh%2FVHzY5ajHpgZoYkTl%2FH5Fq4P8Y%2BwRRdW3qZKtfkUALWSm97ygO93RHR7JjykSpQ4leVhrgchxVSvXtxqNIvgSH30mP%2Fxz0ocLem6Ib6xrzDElA3TMX5%2B%2Foj6JvcEfwELHnkb3Gf2WGucHF%2F7kme7Uh8vBd9zKTZy39yAGEB4IqXUn1BotjhHtxrReOhzCR90eJr4xhPBzUXl6CgWBvl2aAtxS2CSxGRQksJHEuQ7f8CM1YYhy0k3w3AdClMv%2BC5dWG1%2F8oUzPqUwgohPN2ceo5R6A6mTbnubctdZ2TVo%2FMmzWE06FvkjZeEL1diJu5K0diiHNXriewQ%2FBpmtEqmxwZREXiygMVwUAEEEhBKx%2BYEBOL%2BxFmCX293wCB7gLYMcwkGKQnh4kS1O2RWlgcfDF4JIOO4nR7%2BSsH4ZGAEsBQQ1n1EqoPpEYznLyEye%2BhPB%2BIAmkfSp2KeYDipA3WIwm%2FOfc8tUtiEn5v%2BUjMwio%2FeyQY6pgG2b9jZM0KuDvcvXa7dpmL9NpsXrpEJGE9WOwL9EDuKhxCPSwfzGt4VDfkLe027RR9TL4oKvSphPmfAR%2Fnw6VewqOWtQdEcbf7hk%2FbmLdeI%2BLzhyF4tuH6eEhcxVH5GsFq7zbEz6XYqnG97R71eikR4y8ZtSgA8TBiHoMUSlk0pnBeMaxfQSc4und1qSpw%2Bd3JgSqGkeKpN29PnNuHeaa6QR4wAM1kt&X-Amz-Signature=2e2c875b37f5a1fbdf2b7749c034738550676a2b74222aa18392e2b86b3473a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFDSM45G%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNMQzcVtgeQ%2BcO4GXr%2FJrWLpaUt2UFFqWbxX6v9v0KdAiAfatrTLtG3b5D14fld%2BnB4ta%2BTYe44qyFjl07bwQGT3iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMz5BBhOop0HtmMDOKtwDcdGtNFMgS05R9FDcbWfZv8pTXhun02ousSdWoIvFV9dgkPbqASmEHbRqeTuDduGECjD6Zr7N5alXwmF4nZeDgGf4Ew%2FY%2B1u2p%2BNdrHSudvMphBfSqas5qAM%2FANRG%2FHfvHd5hjDu9gfuetAqN9DSWh%2FVHzY5ajHpgZoYkTl%2FH5Fq4P8Y%2BwRRdW3qZKtfkUALWSm97ygO93RHR7JjykSpQ4leVhrgchxVSvXtxqNIvgSH30mP%2Fxz0ocLem6Ib6xrzDElA3TMX5%2B%2Foj6JvcEfwELHnkb3Gf2WGucHF%2F7kme7Uh8vBd9zKTZy39yAGEB4IqXUn1BotjhHtxrReOhzCR90eJr4xhPBzUXl6CgWBvl2aAtxS2CSxGRQksJHEuQ7f8CM1YYhy0k3w3AdClMv%2BC5dWG1%2F8oUzPqUwgohPN2ceo5R6A6mTbnubctdZ2TVo%2FMmzWE06FvkjZeEL1diJu5K0diiHNXriewQ%2FBpmtEqmxwZREXiygMVwUAEEEhBKx%2BYEBOL%2BxFmCX293wCB7gLYMcwkGKQnh4kS1O2RWlgcfDF4JIOO4nR7%2BSsH4ZGAEsBQQ1n1EqoPpEYznLyEye%2BhPB%2BIAmkfSp2KeYDipA3WIwm%2FOfc8tUtiEn5v%2BUjMwio%2FeyQY6pgG2b9jZM0KuDvcvXa7dpmL9NpsXrpEJGE9WOwL9EDuKhxCPSwfzGt4VDfkLe027RR9TL4oKvSphPmfAR%2Fnw6VewqOWtQdEcbf7hk%2FbmLdeI%2BLzhyF4tuH6eEhcxVH5GsFq7zbEz6XYqnG97R71eikR4y8ZtSgA8TBiHoMUSlk0pnBeMaxfQSc4und1qSpw%2Bd3JgSqGkeKpN29PnNuHeaa6QR4wAM1kt&X-Amz-Signature=4622b19d140d351b8b00429450f5045262223013d124307b10f18f086c78c17f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFDSM45G%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNMQzcVtgeQ%2BcO4GXr%2FJrWLpaUt2UFFqWbxX6v9v0KdAiAfatrTLtG3b5D14fld%2BnB4ta%2BTYe44qyFjl07bwQGT3iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMz5BBhOop0HtmMDOKtwDcdGtNFMgS05R9FDcbWfZv8pTXhun02ousSdWoIvFV9dgkPbqASmEHbRqeTuDduGECjD6Zr7N5alXwmF4nZeDgGf4Ew%2FY%2B1u2p%2BNdrHSudvMphBfSqas5qAM%2FANRG%2FHfvHd5hjDu9gfuetAqN9DSWh%2FVHzY5ajHpgZoYkTl%2FH5Fq4P8Y%2BwRRdW3qZKtfkUALWSm97ygO93RHR7JjykSpQ4leVhrgchxVSvXtxqNIvgSH30mP%2Fxz0ocLem6Ib6xrzDElA3TMX5%2B%2Foj6JvcEfwELHnkb3Gf2WGucHF%2F7kme7Uh8vBd9zKTZy39yAGEB4IqXUn1BotjhHtxrReOhzCR90eJr4xhPBzUXl6CgWBvl2aAtxS2CSxGRQksJHEuQ7f8CM1YYhy0k3w3AdClMv%2BC5dWG1%2F8oUzPqUwgohPN2ceo5R6A6mTbnubctdZ2TVo%2FMmzWE06FvkjZeEL1diJu5K0diiHNXriewQ%2FBpmtEqmxwZREXiygMVwUAEEEhBKx%2BYEBOL%2BxFmCX293wCB7gLYMcwkGKQnh4kS1O2RWlgcfDF4JIOO4nR7%2BSsH4ZGAEsBQQ1n1EqoPpEYznLyEye%2BhPB%2BIAmkfSp2KeYDipA3WIwm%2FOfc8tUtiEn5v%2BUjMwio%2FeyQY6pgG2b9jZM0KuDvcvXa7dpmL9NpsXrpEJGE9WOwL9EDuKhxCPSwfzGt4VDfkLe027RR9TL4oKvSphPmfAR%2Fnw6VewqOWtQdEcbf7hk%2FbmLdeI%2BLzhyF4tuH6eEhcxVH5GsFq7zbEz6XYqnG97R71eikR4y8ZtSgA8TBiHoMUSlk0pnBeMaxfQSc4und1qSpw%2Bd3JgSqGkeKpN29PnNuHeaa6QR4wAM1kt&X-Amz-Signature=5c1be6521e8d473550c96122e3b3cb49a24d82a8b87be83c9a7518c34f400960&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFDSM45G%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNMQzcVtgeQ%2BcO4GXr%2FJrWLpaUt2UFFqWbxX6v9v0KdAiAfatrTLtG3b5D14fld%2BnB4ta%2BTYe44qyFjl07bwQGT3iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMz5BBhOop0HtmMDOKtwDcdGtNFMgS05R9FDcbWfZv8pTXhun02ousSdWoIvFV9dgkPbqASmEHbRqeTuDduGECjD6Zr7N5alXwmF4nZeDgGf4Ew%2FY%2B1u2p%2BNdrHSudvMphBfSqas5qAM%2FANRG%2FHfvHd5hjDu9gfuetAqN9DSWh%2FVHzY5ajHpgZoYkTl%2FH5Fq4P8Y%2BwRRdW3qZKtfkUALWSm97ygO93RHR7JjykSpQ4leVhrgchxVSvXtxqNIvgSH30mP%2Fxz0ocLem6Ib6xrzDElA3TMX5%2B%2Foj6JvcEfwELHnkb3Gf2WGucHF%2F7kme7Uh8vBd9zKTZy39yAGEB4IqXUn1BotjhHtxrReOhzCR90eJr4xhPBzUXl6CgWBvl2aAtxS2CSxGRQksJHEuQ7f8CM1YYhy0k3w3AdClMv%2BC5dWG1%2F8oUzPqUwgohPN2ceo5R6A6mTbnubctdZ2TVo%2FMmzWE06FvkjZeEL1diJu5K0diiHNXriewQ%2FBpmtEqmxwZREXiygMVwUAEEEhBKx%2BYEBOL%2BxFmCX293wCB7gLYMcwkGKQnh4kS1O2RWlgcfDF4JIOO4nR7%2BSsH4ZGAEsBQQ1n1EqoPpEYznLyEye%2BhPB%2BIAmkfSp2KeYDipA3WIwm%2FOfc8tUtiEn5v%2BUjMwio%2FeyQY6pgG2b9jZM0KuDvcvXa7dpmL9NpsXrpEJGE9WOwL9EDuKhxCPSwfzGt4VDfkLe027RR9TL4oKvSphPmfAR%2Fnw6VewqOWtQdEcbf7hk%2FbmLdeI%2BLzhyF4tuH6eEhcxVH5GsFq7zbEz6XYqnG97R71eikR4y8ZtSgA8TBiHoMUSlk0pnBeMaxfQSc4und1qSpw%2Bd3JgSqGkeKpN29PnNuHeaa6QR4wAM1kt&X-Amz-Signature=43388e3c267f020779dbecf52628adb0d1597d99b3994283dd0bc65e65d9c68e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFDSM45G%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNMQzcVtgeQ%2BcO4GXr%2FJrWLpaUt2UFFqWbxX6v9v0KdAiAfatrTLtG3b5D14fld%2BnB4ta%2BTYe44qyFjl07bwQGT3iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMz5BBhOop0HtmMDOKtwDcdGtNFMgS05R9FDcbWfZv8pTXhun02ousSdWoIvFV9dgkPbqASmEHbRqeTuDduGECjD6Zr7N5alXwmF4nZeDgGf4Ew%2FY%2B1u2p%2BNdrHSudvMphBfSqas5qAM%2FANRG%2FHfvHd5hjDu9gfuetAqN9DSWh%2FVHzY5ajHpgZoYkTl%2FH5Fq4P8Y%2BwRRdW3qZKtfkUALWSm97ygO93RHR7JjykSpQ4leVhrgchxVSvXtxqNIvgSH30mP%2Fxz0ocLem6Ib6xrzDElA3TMX5%2B%2Foj6JvcEfwELHnkb3Gf2WGucHF%2F7kme7Uh8vBd9zKTZy39yAGEB4IqXUn1BotjhHtxrReOhzCR90eJr4xhPBzUXl6CgWBvl2aAtxS2CSxGRQksJHEuQ7f8CM1YYhy0k3w3AdClMv%2BC5dWG1%2F8oUzPqUwgohPN2ceo5R6A6mTbnubctdZ2TVo%2FMmzWE06FvkjZeEL1diJu5K0diiHNXriewQ%2FBpmtEqmxwZREXiygMVwUAEEEhBKx%2BYEBOL%2BxFmCX293wCB7gLYMcwkGKQnh4kS1O2RWlgcfDF4JIOO4nR7%2BSsH4ZGAEsBQQ1n1EqoPpEYznLyEye%2BhPB%2BIAmkfSp2KeYDipA3WIwm%2FOfc8tUtiEn5v%2BUjMwio%2FeyQY6pgG2b9jZM0KuDvcvXa7dpmL9NpsXrpEJGE9WOwL9EDuKhxCPSwfzGt4VDfkLe027RR9TL4oKvSphPmfAR%2Fnw6VewqOWtQdEcbf7hk%2FbmLdeI%2BLzhyF4tuH6eEhcxVH5GsFq7zbEz6XYqnG97R71eikR4y8ZtSgA8TBiHoMUSlk0pnBeMaxfQSc4und1qSpw%2Bd3JgSqGkeKpN29PnNuHeaa6QR4wAM1kt&X-Amz-Signature=5ea7824f0acc76b729b5833fef10866a4ddc531bcf793fff32371c5c9e9fe9c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFDSM45G%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNMQzcVtgeQ%2BcO4GXr%2FJrWLpaUt2UFFqWbxX6v9v0KdAiAfatrTLtG3b5D14fld%2BnB4ta%2BTYe44qyFjl07bwQGT3iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMz5BBhOop0HtmMDOKtwDcdGtNFMgS05R9FDcbWfZv8pTXhun02ousSdWoIvFV9dgkPbqASmEHbRqeTuDduGECjD6Zr7N5alXwmF4nZeDgGf4Ew%2FY%2B1u2p%2BNdrHSudvMphBfSqas5qAM%2FANRG%2FHfvHd5hjDu9gfuetAqN9DSWh%2FVHzY5ajHpgZoYkTl%2FH5Fq4P8Y%2BwRRdW3qZKtfkUALWSm97ygO93RHR7JjykSpQ4leVhrgchxVSvXtxqNIvgSH30mP%2Fxz0ocLem6Ib6xrzDElA3TMX5%2B%2Foj6JvcEfwELHnkb3Gf2WGucHF%2F7kme7Uh8vBd9zKTZy39yAGEB4IqXUn1BotjhHtxrReOhzCR90eJr4xhPBzUXl6CgWBvl2aAtxS2CSxGRQksJHEuQ7f8CM1YYhy0k3w3AdClMv%2BC5dWG1%2F8oUzPqUwgohPN2ceo5R6A6mTbnubctdZ2TVo%2FMmzWE06FvkjZeEL1diJu5K0diiHNXriewQ%2FBpmtEqmxwZREXiygMVwUAEEEhBKx%2BYEBOL%2BxFmCX293wCB7gLYMcwkGKQnh4kS1O2RWlgcfDF4JIOO4nR7%2BSsH4ZGAEsBQQ1n1EqoPpEYznLyEye%2BhPB%2BIAmkfSp2KeYDipA3WIwm%2FOfc8tUtiEn5v%2BUjMwio%2FeyQY6pgG2b9jZM0KuDvcvXa7dpmL9NpsXrpEJGE9WOwL9EDuKhxCPSwfzGt4VDfkLe027RR9TL4oKvSphPmfAR%2Fnw6VewqOWtQdEcbf7hk%2FbmLdeI%2BLzhyF4tuH6eEhcxVH5GsFq7zbEz6XYqnG97R71eikR4y8ZtSgA8TBiHoMUSlk0pnBeMaxfQSc4und1qSpw%2Bd3JgSqGkeKpN29PnNuHeaa6QR4wAM1kt&X-Amz-Signature=53d4f7469e408b387430f92303ee5df4a6eb82d7192bb835e432d74d40cfe606&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFDSM45G%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNMQzcVtgeQ%2BcO4GXr%2FJrWLpaUt2UFFqWbxX6v9v0KdAiAfatrTLtG3b5D14fld%2BnB4ta%2BTYe44qyFjl07bwQGT3iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMz5BBhOop0HtmMDOKtwDcdGtNFMgS05R9FDcbWfZv8pTXhun02ousSdWoIvFV9dgkPbqASmEHbRqeTuDduGECjD6Zr7N5alXwmF4nZeDgGf4Ew%2FY%2B1u2p%2BNdrHSudvMphBfSqas5qAM%2FANRG%2FHfvHd5hjDu9gfuetAqN9DSWh%2FVHzY5ajHpgZoYkTl%2FH5Fq4P8Y%2BwRRdW3qZKtfkUALWSm97ygO93RHR7JjykSpQ4leVhrgchxVSvXtxqNIvgSH30mP%2Fxz0ocLem6Ib6xrzDElA3TMX5%2B%2Foj6JvcEfwELHnkb3Gf2WGucHF%2F7kme7Uh8vBd9zKTZy39yAGEB4IqXUn1BotjhHtxrReOhzCR90eJr4xhPBzUXl6CgWBvl2aAtxS2CSxGRQksJHEuQ7f8CM1YYhy0k3w3AdClMv%2BC5dWG1%2F8oUzPqUwgohPN2ceo5R6A6mTbnubctdZ2TVo%2FMmzWE06FvkjZeEL1diJu5K0diiHNXriewQ%2FBpmtEqmxwZREXiygMVwUAEEEhBKx%2BYEBOL%2BxFmCX293wCB7gLYMcwkGKQnh4kS1O2RWlgcfDF4JIOO4nR7%2BSsH4ZGAEsBQQ1n1EqoPpEYznLyEye%2BhPB%2BIAmkfSp2KeYDipA3WIwm%2FOfc8tUtiEn5v%2BUjMwio%2FeyQY6pgG2b9jZM0KuDvcvXa7dpmL9NpsXrpEJGE9WOwL9EDuKhxCPSwfzGt4VDfkLe027RR9TL4oKvSphPmfAR%2Fnw6VewqOWtQdEcbf7hk%2FbmLdeI%2BLzhyF4tuH6eEhcxVH5GsFq7zbEz6XYqnG97R71eikR4y8ZtSgA8TBiHoMUSlk0pnBeMaxfQSc4und1qSpw%2Bd3JgSqGkeKpN29PnNuHeaa6QR4wAM1kt&X-Amz-Signature=e6835dd73fd2f7bf84ef27b6fec2caebd36e03302cc0bfb66de51d621e333081&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

