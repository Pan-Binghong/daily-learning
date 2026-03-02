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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHDKWKWN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDBZLaYOPcdCSGjVWHdhtlWDin8xpyDHOFKUApLYwxFvAiB5yAsyNyZVzU3decEClki1LZmqqVDSLDinZ5rVDTHZmir%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMByYgHVy%2Br3EctcbjKtwDhk5WSP5xqYDH4nfAEzwLq4oOVE79ubXBQR7uLdRnKZktM%2FWsdfpSMbfpPo208XkEUcUcq%2FEALv8kUwT7U2nhG7DsAhAzdTRcy7oXndsNBafEbxEEtC0hzPQZAXFBS8NOgmUyfPoF08%2BGQu1L%2FjwhJ4RjxFeydaaFtptRLMHbX9t8hrkZc2Vx4tQXMQXMUKuQYtUXToPxQWCsFD5RL8hbAjkPvBlW0%2BiJGAO4wFCcf60sc%2FmGw6Ep9olEUyl1nK3VF4uo9p5YOZi6f5Die95OlP%2FXpS1Clt%2Fg3J7cVJX3U9gew7BZsQkjA6IeFsxnWdh1tb9QZKv0WHW3Jue%2Fu1qqdtBkBrwXKjwnWikqnW0qNYLEUhTZ9XuQ8IhVcl3Pbpj%2FyWJG%2BBVRqNku64ILCgOguUHxwgNgQHzX%2FhZ53Ki7aJQ0qRwBfswT3Kw3L6ReOd9E%2Bz%2B1XEJqCb8wqfVFwrb%2BEX8K1JPLVByFfGBQDnLoQmN6nvgzg3mP9crCPX7iS5yVdfiPSC9Ipm1O01K0luMCZQCO3RiSNKCBdXz5kEY3YiCm7UgbQ9oPub66D2C2UAb%2FIPa%2FHHf2btAvhGOGQ3%2BSzU0toKDjdhNErtyxlRlVtdPzT%2BeA0O%2FbiPZHctkw%2F%2FyTzQY6pgGHzW8pzpWzXrL%2Fs3RSzb3i0rCm3pGQbf1atZc2mpMP2k0w5vUv5Mfpuy7yAh%2B5DI0Wfypc2XjUP3CLJSWFHB%2Bp1PStO9mdaMCL%2BGGHt1E2RAjUGdrRkmerVeJuA5cL99%2BYK46wJGFW884VwpTBzGJJ5OP%2BcG6yNfK%2F5AuMKxk7yhUyFYv1%2F%2F8CVlqFVhAftkGrBAEDSXbkgpfO%2Fbu8vdJtAcfSOLdI&X-Amz-Signature=1a14e807cde11e5e9995bd4078a878ef21ee993461a2a0933ea8eb4582b7bb5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHDKWKWN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDBZLaYOPcdCSGjVWHdhtlWDin8xpyDHOFKUApLYwxFvAiB5yAsyNyZVzU3decEClki1LZmqqVDSLDinZ5rVDTHZmir%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMByYgHVy%2Br3EctcbjKtwDhk5WSP5xqYDH4nfAEzwLq4oOVE79ubXBQR7uLdRnKZktM%2FWsdfpSMbfpPo208XkEUcUcq%2FEALv8kUwT7U2nhG7DsAhAzdTRcy7oXndsNBafEbxEEtC0hzPQZAXFBS8NOgmUyfPoF08%2BGQu1L%2FjwhJ4RjxFeydaaFtptRLMHbX9t8hrkZc2Vx4tQXMQXMUKuQYtUXToPxQWCsFD5RL8hbAjkPvBlW0%2BiJGAO4wFCcf60sc%2FmGw6Ep9olEUyl1nK3VF4uo9p5YOZi6f5Die95OlP%2FXpS1Clt%2Fg3J7cVJX3U9gew7BZsQkjA6IeFsxnWdh1tb9QZKv0WHW3Jue%2Fu1qqdtBkBrwXKjwnWikqnW0qNYLEUhTZ9XuQ8IhVcl3Pbpj%2FyWJG%2BBVRqNku64ILCgOguUHxwgNgQHzX%2FhZ53Ki7aJQ0qRwBfswT3Kw3L6ReOd9E%2Bz%2B1XEJqCb8wqfVFwrb%2BEX8K1JPLVByFfGBQDnLoQmN6nvgzg3mP9crCPX7iS5yVdfiPSC9Ipm1O01K0luMCZQCO3RiSNKCBdXz5kEY3YiCm7UgbQ9oPub66D2C2UAb%2FIPa%2FHHf2btAvhGOGQ3%2BSzU0toKDjdhNErtyxlRlVtdPzT%2BeA0O%2FbiPZHctkw%2F%2FyTzQY6pgGHzW8pzpWzXrL%2Fs3RSzb3i0rCm3pGQbf1atZc2mpMP2k0w5vUv5Mfpuy7yAh%2B5DI0Wfypc2XjUP3CLJSWFHB%2Bp1PStO9mdaMCL%2BGGHt1E2RAjUGdrRkmerVeJuA5cL99%2BYK46wJGFW884VwpTBzGJJ5OP%2BcG6yNfK%2F5AuMKxk7yhUyFYv1%2F%2F8CVlqFVhAftkGrBAEDSXbkgpfO%2Fbu8vdJtAcfSOLdI&X-Amz-Signature=135a39677e926e8d649a57082334520f5297ee90f66b69f2ffc8b87254f5242a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHDKWKWN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDBZLaYOPcdCSGjVWHdhtlWDin8xpyDHOFKUApLYwxFvAiB5yAsyNyZVzU3decEClki1LZmqqVDSLDinZ5rVDTHZmir%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMByYgHVy%2Br3EctcbjKtwDhk5WSP5xqYDH4nfAEzwLq4oOVE79ubXBQR7uLdRnKZktM%2FWsdfpSMbfpPo208XkEUcUcq%2FEALv8kUwT7U2nhG7DsAhAzdTRcy7oXndsNBafEbxEEtC0hzPQZAXFBS8NOgmUyfPoF08%2BGQu1L%2FjwhJ4RjxFeydaaFtptRLMHbX9t8hrkZc2Vx4tQXMQXMUKuQYtUXToPxQWCsFD5RL8hbAjkPvBlW0%2BiJGAO4wFCcf60sc%2FmGw6Ep9olEUyl1nK3VF4uo9p5YOZi6f5Die95OlP%2FXpS1Clt%2Fg3J7cVJX3U9gew7BZsQkjA6IeFsxnWdh1tb9QZKv0WHW3Jue%2Fu1qqdtBkBrwXKjwnWikqnW0qNYLEUhTZ9XuQ8IhVcl3Pbpj%2FyWJG%2BBVRqNku64ILCgOguUHxwgNgQHzX%2FhZ53Ki7aJQ0qRwBfswT3Kw3L6ReOd9E%2Bz%2B1XEJqCb8wqfVFwrb%2BEX8K1JPLVByFfGBQDnLoQmN6nvgzg3mP9crCPX7iS5yVdfiPSC9Ipm1O01K0luMCZQCO3RiSNKCBdXz5kEY3YiCm7UgbQ9oPub66D2C2UAb%2FIPa%2FHHf2btAvhGOGQ3%2BSzU0toKDjdhNErtyxlRlVtdPzT%2BeA0O%2FbiPZHctkw%2F%2FyTzQY6pgGHzW8pzpWzXrL%2Fs3RSzb3i0rCm3pGQbf1atZc2mpMP2k0w5vUv5Mfpuy7yAh%2B5DI0Wfypc2XjUP3CLJSWFHB%2Bp1PStO9mdaMCL%2BGGHt1E2RAjUGdrRkmerVeJuA5cL99%2BYK46wJGFW884VwpTBzGJJ5OP%2BcG6yNfK%2F5AuMKxk7yhUyFYv1%2F%2F8CVlqFVhAftkGrBAEDSXbkgpfO%2Fbu8vdJtAcfSOLdI&X-Amz-Signature=d640d0c5d8c358f9fbd1146bef02d9d15da7060449a561e6b60c57fb6532089b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHDKWKWN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDBZLaYOPcdCSGjVWHdhtlWDin8xpyDHOFKUApLYwxFvAiB5yAsyNyZVzU3decEClki1LZmqqVDSLDinZ5rVDTHZmir%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMByYgHVy%2Br3EctcbjKtwDhk5WSP5xqYDH4nfAEzwLq4oOVE79ubXBQR7uLdRnKZktM%2FWsdfpSMbfpPo208XkEUcUcq%2FEALv8kUwT7U2nhG7DsAhAzdTRcy7oXndsNBafEbxEEtC0hzPQZAXFBS8NOgmUyfPoF08%2BGQu1L%2FjwhJ4RjxFeydaaFtptRLMHbX9t8hrkZc2Vx4tQXMQXMUKuQYtUXToPxQWCsFD5RL8hbAjkPvBlW0%2BiJGAO4wFCcf60sc%2FmGw6Ep9olEUyl1nK3VF4uo9p5YOZi6f5Die95OlP%2FXpS1Clt%2Fg3J7cVJX3U9gew7BZsQkjA6IeFsxnWdh1tb9QZKv0WHW3Jue%2Fu1qqdtBkBrwXKjwnWikqnW0qNYLEUhTZ9XuQ8IhVcl3Pbpj%2FyWJG%2BBVRqNku64ILCgOguUHxwgNgQHzX%2FhZ53Ki7aJQ0qRwBfswT3Kw3L6ReOd9E%2Bz%2B1XEJqCb8wqfVFwrb%2BEX8K1JPLVByFfGBQDnLoQmN6nvgzg3mP9crCPX7iS5yVdfiPSC9Ipm1O01K0luMCZQCO3RiSNKCBdXz5kEY3YiCm7UgbQ9oPub66D2C2UAb%2FIPa%2FHHf2btAvhGOGQ3%2BSzU0toKDjdhNErtyxlRlVtdPzT%2BeA0O%2FbiPZHctkw%2F%2FyTzQY6pgGHzW8pzpWzXrL%2Fs3RSzb3i0rCm3pGQbf1atZc2mpMP2k0w5vUv5Mfpuy7yAh%2B5DI0Wfypc2XjUP3CLJSWFHB%2Bp1PStO9mdaMCL%2BGGHt1E2RAjUGdrRkmerVeJuA5cL99%2BYK46wJGFW884VwpTBzGJJ5OP%2BcG6yNfK%2F5AuMKxk7yhUyFYv1%2F%2F8CVlqFVhAftkGrBAEDSXbkgpfO%2Fbu8vdJtAcfSOLdI&X-Amz-Signature=347821bfa698acd6be4dc394e60b2ff37939e027d17e5acc71e456ec6e776837&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHDKWKWN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDBZLaYOPcdCSGjVWHdhtlWDin8xpyDHOFKUApLYwxFvAiB5yAsyNyZVzU3decEClki1LZmqqVDSLDinZ5rVDTHZmir%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMByYgHVy%2Br3EctcbjKtwDhk5WSP5xqYDH4nfAEzwLq4oOVE79ubXBQR7uLdRnKZktM%2FWsdfpSMbfpPo208XkEUcUcq%2FEALv8kUwT7U2nhG7DsAhAzdTRcy7oXndsNBafEbxEEtC0hzPQZAXFBS8NOgmUyfPoF08%2BGQu1L%2FjwhJ4RjxFeydaaFtptRLMHbX9t8hrkZc2Vx4tQXMQXMUKuQYtUXToPxQWCsFD5RL8hbAjkPvBlW0%2BiJGAO4wFCcf60sc%2FmGw6Ep9olEUyl1nK3VF4uo9p5YOZi6f5Die95OlP%2FXpS1Clt%2Fg3J7cVJX3U9gew7BZsQkjA6IeFsxnWdh1tb9QZKv0WHW3Jue%2Fu1qqdtBkBrwXKjwnWikqnW0qNYLEUhTZ9XuQ8IhVcl3Pbpj%2FyWJG%2BBVRqNku64ILCgOguUHxwgNgQHzX%2FhZ53Ki7aJQ0qRwBfswT3Kw3L6ReOd9E%2Bz%2B1XEJqCb8wqfVFwrb%2BEX8K1JPLVByFfGBQDnLoQmN6nvgzg3mP9crCPX7iS5yVdfiPSC9Ipm1O01K0luMCZQCO3RiSNKCBdXz5kEY3YiCm7UgbQ9oPub66D2C2UAb%2FIPa%2FHHf2btAvhGOGQ3%2BSzU0toKDjdhNErtyxlRlVtdPzT%2BeA0O%2FbiPZHctkw%2F%2FyTzQY6pgGHzW8pzpWzXrL%2Fs3RSzb3i0rCm3pGQbf1atZc2mpMP2k0w5vUv5Mfpuy7yAh%2B5DI0Wfypc2XjUP3CLJSWFHB%2Bp1PStO9mdaMCL%2BGGHt1E2RAjUGdrRkmerVeJuA5cL99%2BYK46wJGFW884VwpTBzGJJ5OP%2BcG6yNfK%2F5AuMKxk7yhUyFYv1%2F%2F8CVlqFVhAftkGrBAEDSXbkgpfO%2Fbu8vdJtAcfSOLdI&X-Amz-Signature=89ddb829a9279c0f940d3175a3caf66f09f8ddd8b956c62221652b1b8cce6b67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHDKWKWN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDBZLaYOPcdCSGjVWHdhtlWDin8xpyDHOFKUApLYwxFvAiB5yAsyNyZVzU3decEClki1LZmqqVDSLDinZ5rVDTHZmir%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMByYgHVy%2Br3EctcbjKtwDhk5WSP5xqYDH4nfAEzwLq4oOVE79ubXBQR7uLdRnKZktM%2FWsdfpSMbfpPo208XkEUcUcq%2FEALv8kUwT7U2nhG7DsAhAzdTRcy7oXndsNBafEbxEEtC0hzPQZAXFBS8NOgmUyfPoF08%2BGQu1L%2FjwhJ4RjxFeydaaFtptRLMHbX9t8hrkZc2Vx4tQXMQXMUKuQYtUXToPxQWCsFD5RL8hbAjkPvBlW0%2BiJGAO4wFCcf60sc%2FmGw6Ep9olEUyl1nK3VF4uo9p5YOZi6f5Die95OlP%2FXpS1Clt%2Fg3J7cVJX3U9gew7BZsQkjA6IeFsxnWdh1tb9QZKv0WHW3Jue%2Fu1qqdtBkBrwXKjwnWikqnW0qNYLEUhTZ9XuQ8IhVcl3Pbpj%2FyWJG%2BBVRqNku64ILCgOguUHxwgNgQHzX%2FhZ53Ki7aJQ0qRwBfswT3Kw3L6ReOd9E%2Bz%2B1XEJqCb8wqfVFwrb%2BEX8K1JPLVByFfGBQDnLoQmN6nvgzg3mP9crCPX7iS5yVdfiPSC9Ipm1O01K0luMCZQCO3RiSNKCBdXz5kEY3YiCm7UgbQ9oPub66D2C2UAb%2FIPa%2FHHf2btAvhGOGQ3%2BSzU0toKDjdhNErtyxlRlVtdPzT%2BeA0O%2FbiPZHctkw%2F%2FyTzQY6pgGHzW8pzpWzXrL%2Fs3RSzb3i0rCm3pGQbf1atZc2mpMP2k0w5vUv5Mfpuy7yAh%2B5DI0Wfypc2XjUP3CLJSWFHB%2Bp1PStO9mdaMCL%2BGGHt1E2RAjUGdrRkmerVeJuA5cL99%2BYK46wJGFW884VwpTBzGJJ5OP%2BcG6yNfK%2F5AuMKxk7yhUyFYv1%2F%2F8CVlqFVhAftkGrBAEDSXbkgpfO%2Fbu8vdJtAcfSOLdI&X-Amz-Signature=fa6e033488fca69b1847a817af8bf7186a47e2d8aff7870a5406930ae087bd3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHDKWKWN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDBZLaYOPcdCSGjVWHdhtlWDin8xpyDHOFKUApLYwxFvAiB5yAsyNyZVzU3decEClki1LZmqqVDSLDinZ5rVDTHZmir%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMByYgHVy%2Br3EctcbjKtwDhk5WSP5xqYDH4nfAEzwLq4oOVE79ubXBQR7uLdRnKZktM%2FWsdfpSMbfpPo208XkEUcUcq%2FEALv8kUwT7U2nhG7DsAhAzdTRcy7oXndsNBafEbxEEtC0hzPQZAXFBS8NOgmUyfPoF08%2BGQu1L%2FjwhJ4RjxFeydaaFtptRLMHbX9t8hrkZc2Vx4tQXMQXMUKuQYtUXToPxQWCsFD5RL8hbAjkPvBlW0%2BiJGAO4wFCcf60sc%2FmGw6Ep9olEUyl1nK3VF4uo9p5YOZi6f5Die95OlP%2FXpS1Clt%2Fg3J7cVJX3U9gew7BZsQkjA6IeFsxnWdh1tb9QZKv0WHW3Jue%2Fu1qqdtBkBrwXKjwnWikqnW0qNYLEUhTZ9XuQ8IhVcl3Pbpj%2FyWJG%2BBVRqNku64ILCgOguUHxwgNgQHzX%2FhZ53Ki7aJQ0qRwBfswT3Kw3L6ReOd9E%2Bz%2B1XEJqCb8wqfVFwrb%2BEX8K1JPLVByFfGBQDnLoQmN6nvgzg3mP9crCPX7iS5yVdfiPSC9Ipm1O01K0luMCZQCO3RiSNKCBdXz5kEY3YiCm7UgbQ9oPub66D2C2UAb%2FIPa%2FHHf2btAvhGOGQ3%2BSzU0toKDjdhNErtyxlRlVtdPzT%2BeA0O%2FbiPZHctkw%2F%2FyTzQY6pgGHzW8pzpWzXrL%2Fs3RSzb3i0rCm3pGQbf1atZc2mpMP2k0w5vUv5Mfpuy7yAh%2B5DI0Wfypc2XjUP3CLJSWFHB%2Bp1PStO9mdaMCL%2BGGHt1E2RAjUGdrRkmerVeJuA5cL99%2BYK46wJGFW884VwpTBzGJJ5OP%2BcG6yNfK%2F5AuMKxk7yhUyFYv1%2F%2F8CVlqFVhAftkGrBAEDSXbkgpfO%2Fbu8vdJtAcfSOLdI&X-Amz-Signature=52419c8619314834e2e69c3f5340ab42756697bbc7513708fb39c8ba8b9c9d29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHDKWKWN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDBZLaYOPcdCSGjVWHdhtlWDin8xpyDHOFKUApLYwxFvAiB5yAsyNyZVzU3decEClki1LZmqqVDSLDinZ5rVDTHZmir%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMByYgHVy%2Br3EctcbjKtwDhk5WSP5xqYDH4nfAEzwLq4oOVE79ubXBQR7uLdRnKZktM%2FWsdfpSMbfpPo208XkEUcUcq%2FEALv8kUwT7U2nhG7DsAhAzdTRcy7oXndsNBafEbxEEtC0hzPQZAXFBS8NOgmUyfPoF08%2BGQu1L%2FjwhJ4RjxFeydaaFtptRLMHbX9t8hrkZc2Vx4tQXMQXMUKuQYtUXToPxQWCsFD5RL8hbAjkPvBlW0%2BiJGAO4wFCcf60sc%2FmGw6Ep9olEUyl1nK3VF4uo9p5YOZi6f5Die95OlP%2FXpS1Clt%2Fg3J7cVJX3U9gew7BZsQkjA6IeFsxnWdh1tb9QZKv0WHW3Jue%2Fu1qqdtBkBrwXKjwnWikqnW0qNYLEUhTZ9XuQ8IhVcl3Pbpj%2FyWJG%2BBVRqNku64ILCgOguUHxwgNgQHzX%2FhZ53Ki7aJQ0qRwBfswT3Kw3L6ReOd9E%2Bz%2B1XEJqCb8wqfVFwrb%2BEX8K1JPLVByFfGBQDnLoQmN6nvgzg3mP9crCPX7iS5yVdfiPSC9Ipm1O01K0luMCZQCO3RiSNKCBdXz5kEY3YiCm7UgbQ9oPub66D2C2UAb%2FIPa%2FHHf2btAvhGOGQ3%2BSzU0toKDjdhNErtyxlRlVtdPzT%2BeA0O%2FbiPZHctkw%2F%2FyTzQY6pgGHzW8pzpWzXrL%2Fs3RSzb3i0rCm3pGQbf1atZc2mpMP2k0w5vUv5Mfpuy7yAh%2B5DI0Wfypc2XjUP3CLJSWFHB%2Bp1PStO9mdaMCL%2BGGHt1E2RAjUGdrRkmerVeJuA5cL99%2BYK46wJGFW884VwpTBzGJJ5OP%2BcG6yNfK%2F5AuMKxk7yhUyFYv1%2F%2F8CVlqFVhAftkGrBAEDSXbkgpfO%2Fbu8vdJtAcfSOLdI&X-Amz-Signature=2b9d736732744af0d8ad7542c97318cce25a956add0453d15ee4d57bbc112ad1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHDKWKWN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDBZLaYOPcdCSGjVWHdhtlWDin8xpyDHOFKUApLYwxFvAiB5yAsyNyZVzU3decEClki1LZmqqVDSLDinZ5rVDTHZmir%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMByYgHVy%2Br3EctcbjKtwDhk5WSP5xqYDH4nfAEzwLq4oOVE79ubXBQR7uLdRnKZktM%2FWsdfpSMbfpPo208XkEUcUcq%2FEALv8kUwT7U2nhG7DsAhAzdTRcy7oXndsNBafEbxEEtC0hzPQZAXFBS8NOgmUyfPoF08%2BGQu1L%2FjwhJ4RjxFeydaaFtptRLMHbX9t8hrkZc2Vx4tQXMQXMUKuQYtUXToPxQWCsFD5RL8hbAjkPvBlW0%2BiJGAO4wFCcf60sc%2FmGw6Ep9olEUyl1nK3VF4uo9p5YOZi6f5Die95OlP%2FXpS1Clt%2Fg3J7cVJX3U9gew7BZsQkjA6IeFsxnWdh1tb9QZKv0WHW3Jue%2Fu1qqdtBkBrwXKjwnWikqnW0qNYLEUhTZ9XuQ8IhVcl3Pbpj%2FyWJG%2BBVRqNku64ILCgOguUHxwgNgQHzX%2FhZ53Ki7aJQ0qRwBfswT3Kw3L6ReOd9E%2Bz%2B1XEJqCb8wqfVFwrb%2BEX8K1JPLVByFfGBQDnLoQmN6nvgzg3mP9crCPX7iS5yVdfiPSC9Ipm1O01K0luMCZQCO3RiSNKCBdXz5kEY3YiCm7UgbQ9oPub66D2C2UAb%2FIPa%2FHHf2btAvhGOGQ3%2BSzU0toKDjdhNErtyxlRlVtdPzT%2BeA0O%2FbiPZHctkw%2F%2FyTzQY6pgGHzW8pzpWzXrL%2Fs3RSzb3i0rCm3pGQbf1atZc2mpMP2k0w5vUv5Mfpuy7yAh%2B5DI0Wfypc2XjUP3CLJSWFHB%2Bp1PStO9mdaMCL%2BGGHt1E2RAjUGdrRkmerVeJuA5cL99%2BYK46wJGFW884VwpTBzGJJ5OP%2BcG6yNfK%2F5AuMKxk7yhUyFYv1%2F%2F8CVlqFVhAftkGrBAEDSXbkgpfO%2Fbu8vdJtAcfSOLdI&X-Amz-Signature=0561c0412d35840b5132e1c9539e3af39a3a6452fd068cb0a136600b1abd8338&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHDKWKWN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDBZLaYOPcdCSGjVWHdhtlWDin8xpyDHOFKUApLYwxFvAiB5yAsyNyZVzU3decEClki1LZmqqVDSLDinZ5rVDTHZmir%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMByYgHVy%2Br3EctcbjKtwDhk5WSP5xqYDH4nfAEzwLq4oOVE79ubXBQR7uLdRnKZktM%2FWsdfpSMbfpPo208XkEUcUcq%2FEALv8kUwT7U2nhG7DsAhAzdTRcy7oXndsNBafEbxEEtC0hzPQZAXFBS8NOgmUyfPoF08%2BGQu1L%2FjwhJ4RjxFeydaaFtptRLMHbX9t8hrkZc2Vx4tQXMQXMUKuQYtUXToPxQWCsFD5RL8hbAjkPvBlW0%2BiJGAO4wFCcf60sc%2FmGw6Ep9olEUyl1nK3VF4uo9p5YOZi6f5Die95OlP%2FXpS1Clt%2Fg3J7cVJX3U9gew7BZsQkjA6IeFsxnWdh1tb9QZKv0WHW3Jue%2Fu1qqdtBkBrwXKjwnWikqnW0qNYLEUhTZ9XuQ8IhVcl3Pbpj%2FyWJG%2BBVRqNku64ILCgOguUHxwgNgQHzX%2FhZ53Ki7aJQ0qRwBfswT3Kw3L6ReOd9E%2Bz%2B1XEJqCb8wqfVFwrb%2BEX8K1JPLVByFfGBQDnLoQmN6nvgzg3mP9crCPX7iS5yVdfiPSC9Ipm1O01K0luMCZQCO3RiSNKCBdXz5kEY3YiCm7UgbQ9oPub66D2C2UAb%2FIPa%2FHHf2btAvhGOGQ3%2BSzU0toKDjdhNErtyxlRlVtdPzT%2BeA0O%2FbiPZHctkw%2F%2FyTzQY6pgGHzW8pzpWzXrL%2Fs3RSzb3i0rCm3pGQbf1atZc2mpMP2k0w5vUv5Mfpuy7yAh%2B5DI0Wfypc2XjUP3CLJSWFHB%2Bp1PStO9mdaMCL%2BGGHt1E2RAjUGdrRkmerVeJuA5cL99%2BYK46wJGFW884VwpTBzGJJ5OP%2BcG6yNfK%2F5AuMKxk7yhUyFYv1%2F%2F8CVlqFVhAftkGrBAEDSXbkgpfO%2Fbu8vdJtAcfSOLdI&X-Amz-Signature=acffb38dd3edceb856da0b89740244bec2981cfa7f8ec0a68d3612df05bfc7a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

