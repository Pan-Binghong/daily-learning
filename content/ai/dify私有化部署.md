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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWYLWJ2O%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuMdcvpcucOOWJE7%2BEbioNMGBDoOitCVeCGt9lIvufAiEAuv0MtZrd0JUjLH5meXJw7s9gcqEDxvfTPFckIW77BVYq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDES5CUg5BNpX6uUWsircA4OP6susdSv%2B9OXMGevO%2BwBTlVVWYYy3JfmcyYr2dGiaOjKvjOmFJE6yr2BaLl5Hvwr3H3Jn2ByfHASYwZ2%2BfRtKWZwooZGrnw8bzWAr%2FqdOlrGYEwR7rVixlc3%2FqWxVcyyerNpkSskXAH5qKiQJXwNrl5XInQadZ42pC14rcRn%2BZz7OJywkvoNCoXfy%2FqLFEIq5hmN69S75yosqpomStuj24UQEsuTSU2eM9d8INEdjoQzv3hzMeJgmPE%2FFGDl1388S7zypoNJUzKN3Gvwe%2FGIoKrNfh%2Bj9rmFpEWTyd9n%2BMrSvUohQl4RQ4y0yhUx21EkO1gZH%2BRlZBwy1dr%2FZc5IierVzYBvvQE2%2Fr%2FjFDT12QPwaEXbfm1sFZnOC3qksTpmZ8sLg9Sm%2Bq13t%2F5Wd%2B3%2BrbnouUiGfXYnzHKtN%2FfN%2BuWk52BX2Ay0kYFKuLlQoePMVBFrouKu%2FFeGhfafj6SWeB4vnhArQyx6b4Nu35cBiOXCmNBvoWNoc%2B6BsvYRIDTRJrHKIDlIMDoD6S5KY3qSbb6iLr3NnopkjsBQ6nRKp%2FdCIVVQ%2BnGvxfZqMQyZk9FBgvuhB%2F3bOwILEcVl6L5QLqXahDTK28ziLriojpveQOfTaLPbJ2oMeW3h0MM%2BWic0GOqUBdtCtEoHWmCmqBM9xmX5l64y%2BXyfqZP%2F6A%2B44Scir%2B3i9qXFSLRYwjb%2Bs3vz0dDQR0Am2AfdGNh%2BJ4haKq3jbhzr3NOvc4sZNsb8hYWRtTerln2XSQZpK%2F7GtwnX1eEQQlVh9GPGjCL0Ua86u4M6eI0x5lfSkfIVl1mIavfpqJWd6GwIfMHmmWopvyOueQfxjDq84RgtwfL2JAa8hBwbaAcSzndCG&X-Amz-Signature=caf57c5bdc2dcce3e9b42f3c392d65d9461e9f6120018be85667f74986d93324&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWYLWJ2O%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuMdcvpcucOOWJE7%2BEbioNMGBDoOitCVeCGt9lIvufAiEAuv0MtZrd0JUjLH5meXJw7s9gcqEDxvfTPFckIW77BVYq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDES5CUg5BNpX6uUWsircA4OP6susdSv%2B9OXMGevO%2BwBTlVVWYYy3JfmcyYr2dGiaOjKvjOmFJE6yr2BaLl5Hvwr3H3Jn2ByfHASYwZ2%2BfRtKWZwooZGrnw8bzWAr%2FqdOlrGYEwR7rVixlc3%2FqWxVcyyerNpkSskXAH5qKiQJXwNrl5XInQadZ42pC14rcRn%2BZz7OJywkvoNCoXfy%2FqLFEIq5hmN69S75yosqpomStuj24UQEsuTSU2eM9d8INEdjoQzv3hzMeJgmPE%2FFGDl1388S7zypoNJUzKN3Gvwe%2FGIoKrNfh%2Bj9rmFpEWTyd9n%2BMrSvUohQl4RQ4y0yhUx21EkO1gZH%2BRlZBwy1dr%2FZc5IierVzYBvvQE2%2Fr%2FjFDT12QPwaEXbfm1sFZnOC3qksTpmZ8sLg9Sm%2Bq13t%2F5Wd%2B3%2BrbnouUiGfXYnzHKtN%2FfN%2BuWk52BX2Ay0kYFKuLlQoePMVBFrouKu%2FFeGhfafj6SWeB4vnhArQyx6b4Nu35cBiOXCmNBvoWNoc%2B6BsvYRIDTRJrHKIDlIMDoD6S5KY3qSbb6iLr3NnopkjsBQ6nRKp%2FdCIVVQ%2BnGvxfZqMQyZk9FBgvuhB%2F3bOwILEcVl6L5QLqXahDTK28ziLriojpveQOfTaLPbJ2oMeW3h0MM%2BWic0GOqUBdtCtEoHWmCmqBM9xmX5l64y%2BXyfqZP%2F6A%2B44Scir%2B3i9qXFSLRYwjb%2Bs3vz0dDQR0Am2AfdGNh%2BJ4haKq3jbhzr3NOvc4sZNsb8hYWRtTerln2XSQZpK%2F7GtwnX1eEQQlVh9GPGjCL0Ua86u4M6eI0x5lfSkfIVl1mIavfpqJWd6GwIfMHmmWopvyOueQfxjDq84RgtwfL2JAa8hBwbaAcSzndCG&X-Amz-Signature=0d23f7cc9541f0ef0028b9700e779abd6415a8819408a4d2d86539f486b00bed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWYLWJ2O%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuMdcvpcucOOWJE7%2BEbioNMGBDoOitCVeCGt9lIvufAiEAuv0MtZrd0JUjLH5meXJw7s9gcqEDxvfTPFckIW77BVYq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDES5CUg5BNpX6uUWsircA4OP6susdSv%2B9OXMGevO%2BwBTlVVWYYy3JfmcyYr2dGiaOjKvjOmFJE6yr2BaLl5Hvwr3H3Jn2ByfHASYwZ2%2BfRtKWZwooZGrnw8bzWAr%2FqdOlrGYEwR7rVixlc3%2FqWxVcyyerNpkSskXAH5qKiQJXwNrl5XInQadZ42pC14rcRn%2BZz7OJywkvoNCoXfy%2FqLFEIq5hmN69S75yosqpomStuj24UQEsuTSU2eM9d8INEdjoQzv3hzMeJgmPE%2FFGDl1388S7zypoNJUzKN3Gvwe%2FGIoKrNfh%2Bj9rmFpEWTyd9n%2BMrSvUohQl4RQ4y0yhUx21EkO1gZH%2BRlZBwy1dr%2FZc5IierVzYBvvQE2%2Fr%2FjFDT12QPwaEXbfm1sFZnOC3qksTpmZ8sLg9Sm%2Bq13t%2F5Wd%2B3%2BrbnouUiGfXYnzHKtN%2FfN%2BuWk52BX2Ay0kYFKuLlQoePMVBFrouKu%2FFeGhfafj6SWeB4vnhArQyx6b4Nu35cBiOXCmNBvoWNoc%2B6BsvYRIDTRJrHKIDlIMDoD6S5KY3qSbb6iLr3NnopkjsBQ6nRKp%2FdCIVVQ%2BnGvxfZqMQyZk9FBgvuhB%2F3bOwILEcVl6L5QLqXahDTK28ziLriojpveQOfTaLPbJ2oMeW3h0MM%2BWic0GOqUBdtCtEoHWmCmqBM9xmX5l64y%2BXyfqZP%2F6A%2B44Scir%2B3i9qXFSLRYwjb%2Bs3vz0dDQR0Am2AfdGNh%2BJ4haKq3jbhzr3NOvc4sZNsb8hYWRtTerln2XSQZpK%2F7GtwnX1eEQQlVh9GPGjCL0Ua86u4M6eI0x5lfSkfIVl1mIavfpqJWd6GwIfMHmmWopvyOueQfxjDq84RgtwfL2JAa8hBwbaAcSzndCG&X-Amz-Signature=ded6ecbd7c820f5b26c90480949844c7d9bb589e9c383f227dd7ac716530b0c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWYLWJ2O%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuMdcvpcucOOWJE7%2BEbioNMGBDoOitCVeCGt9lIvufAiEAuv0MtZrd0JUjLH5meXJw7s9gcqEDxvfTPFckIW77BVYq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDES5CUg5BNpX6uUWsircA4OP6susdSv%2B9OXMGevO%2BwBTlVVWYYy3JfmcyYr2dGiaOjKvjOmFJE6yr2BaLl5Hvwr3H3Jn2ByfHASYwZ2%2BfRtKWZwooZGrnw8bzWAr%2FqdOlrGYEwR7rVixlc3%2FqWxVcyyerNpkSskXAH5qKiQJXwNrl5XInQadZ42pC14rcRn%2BZz7OJywkvoNCoXfy%2FqLFEIq5hmN69S75yosqpomStuj24UQEsuTSU2eM9d8INEdjoQzv3hzMeJgmPE%2FFGDl1388S7zypoNJUzKN3Gvwe%2FGIoKrNfh%2Bj9rmFpEWTyd9n%2BMrSvUohQl4RQ4y0yhUx21EkO1gZH%2BRlZBwy1dr%2FZc5IierVzYBvvQE2%2Fr%2FjFDT12QPwaEXbfm1sFZnOC3qksTpmZ8sLg9Sm%2Bq13t%2F5Wd%2B3%2BrbnouUiGfXYnzHKtN%2FfN%2BuWk52BX2Ay0kYFKuLlQoePMVBFrouKu%2FFeGhfafj6SWeB4vnhArQyx6b4Nu35cBiOXCmNBvoWNoc%2B6BsvYRIDTRJrHKIDlIMDoD6S5KY3qSbb6iLr3NnopkjsBQ6nRKp%2FdCIVVQ%2BnGvxfZqMQyZk9FBgvuhB%2F3bOwILEcVl6L5QLqXahDTK28ziLriojpveQOfTaLPbJ2oMeW3h0MM%2BWic0GOqUBdtCtEoHWmCmqBM9xmX5l64y%2BXyfqZP%2F6A%2B44Scir%2B3i9qXFSLRYwjb%2Bs3vz0dDQR0Am2AfdGNh%2BJ4haKq3jbhzr3NOvc4sZNsb8hYWRtTerln2XSQZpK%2F7GtwnX1eEQQlVh9GPGjCL0Ua86u4M6eI0x5lfSkfIVl1mIavfpqJWd6GwIfMHmmWopvyOueQfxjDq84RgtwfL2JAa8hBwbaAcSzndCG&X-Amz-Signature=73e9267b889ffa1e239c89d3bc82f266d7571f6d50d30a09dd18946b14f812e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWYLWJ2O%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuMdcvpcucOOWJE7%2BEbioNMGBDoOitCVeCGt9lIvufAiEAuv0MtZrd0JUjLH5meXJw7s9gcqEDxvfTPFckIW77BVYq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDES5CUg5BNpX6uUWsircA4OP6susdSv%2B9OXMGevO%2BwBTlVVWYYy3JfmcyYr2dGiaOjKvjOmFJE6yr2BaLl5Hvwr3H3Jn2ByfHASYwZ2%2BfRtKWZwooZGrnw8bzWAr%2FqdOlrGYEwR7rVixlc3%2FqWxVcyyerNpkSskXAH5qKiQJXwNrl5XInQadZ42pC14rcRn%2BZz7OJywkvoNCoXfy%2FqLFEIq5hmN69S75yosqpomStuj24UQEsuTSU2eM9d8INEdjoQzv3hzMeJgmPE%2FFGDl1388S7zypoNJUzKN3Gvwe%2FGIoKrNfh%2Bj9rmFpEWTyd9n%2BMrSvUohQl4RQ4y0yhUx21EkO1gZH%2BRlZBwy1dr%2FZc5IierVzYBvvQE2%2Fr%2FjFDT12QPwaEXbfm1sFZnOC3qksTpmZ8sLg9Sm%2Bq13t%2F5Wd%2B3%2BrbnouUiGfXYnzHKtN%2FfN%2BuWk52BX2Ay0kYFKuLlQoePMVBFrouKu%2FFeGhfafj6SWeB4vnhArQyx6b4Nu35cBiOXCmNBvoWNoc%2B6BsvYRIDTRJrHKIDlIMDoD6S5KY3qSbb6iLr3NnopkjsBQ6nRKp%2FdCIVVQ%2BnGvxfZqMQyZk9FBgvuhB%2F3bOwILEcVl6L5QLqXahDTK28ziLriojpveQOfTaLPbJ2oMeW3h0MM%2BWic0GOqUBdtCtEoHWmCmqBM9xmX5l64y%2BXyfqZP%2F6A%2B44Scir%2B3i9qXFSLRYwjb%2Bs3vz0dDQR0Am2AfdGNh%2BJ4haKq3jbhzr3NOvc4sZNsb8hYWRtTerln2XSQZpK%2F7GtwnX1eEQQlVh9GPGjCL0Ua86u4M6eI0x5lfSkfIVl1mIavfpqJWd6GwIfMHmmWopvyOueQfxjDq84RgtwfL2JAa8hBwbaAcSzndCG&X-Amz-Signature=f9251c3f417574e167e7dba8a405cf69aeafcfb900ab374f265f3afd31dfd8e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWYLWJ2O%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuMdcvpcucOOWJE7%2BEbioNMGBDoOitCVeCGt9lIvufAiEAuv0MtZrd0JUjLH5meXJw7s9gcqEDxvfTPFckIW77BVYq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDES5CUg5BNpX6uUWsircA4OP6susdSv%2B9OXMGevO%2BwBTlVVWYYy3JfmcyYr2dGiaOjKvjOmFJE6yr2BaLl5Hvwr3H3Jn2ByfHASYwZ2%2BfRtKWZwooZGrnw8bzWAr%2FqdOlrGYEwR7rVixlc3%2FqWxVcyyerNpkSskXAH5qKiQJXwNrl5XInQadZ42pC14rcRn%2BZz7OJywkvoNCoXfy%2FqLFEIq5hmN69S75yosqpomStuj24UQEsuTSU2eM9d8INEdjoQzv3hzMeJgmPE%2FFGDl1388S7zypoNJUzKN3Gvwe%2FGIoKrNfh%2Bj9rmFpEWTyd9n%2BMrSvUohQl4RQ4y0yhUx21EkO1gZH%2BRlZBwy1dr%2FZc5IierVzYBvvQE2%2Fr%2FjFDT12QPwaEXbfm1sFZnOC3qksTpmZ8sLg9Sm%2Bq13t%2F5Wd%2B3%2BrbnouUiGfXYnzHKtN%2FfN%2BuWk52BX2Ay0kYFKuLlQoePMVBFrouKu%2FFeGhfafj6SWeB4vnhArQyx6b4Nu35cBiOXCmNBvoWNoc%2B6BsvYRIDTRJrHKIDlIMDoD6S5KY3qSbb6iLr3NnopkjsBQ6nRKp%2FdCIVVQ%2BnGvxfZqMQyZk9FBgvuhB%2F3bOwILEcVl6L5QLqXahDTK28ziLriojpveQOfTaLPbJ2oMeW3h0MM%2BWic0GOqUBdtCtEoHWmCmqBM9xmX5l64y%2BXyfqZP%2F6A%2B44Scir%2B3i9qXFSLRYwjb%2Bs3vz0dDQR0Am2AfdGNh%2BJ4haKq3jbhzr3NOvc4sZNsb8hYWRtTerln2XSQZpK%2F7GtwnX1eEQQlVh9GPGjCL0Ua86u4M6eI0x5lfSkfIVl1mIavfpqJWd6GwIfMHmmWopvyOueQfxjDq84RgtwfL2JAa8hBwbaAcSzndCG&X-Amz-Signature=19ea9bdeff3a4b28afb5ce65e35a0fc62542ad2ac0921b0942a0ceeb9adcf1b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWYLWJ2O%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuMdcvpcucOOWJE7%2BEbioNMGBDoOitCVeCGt9lIvufAiEAuv0MtZrd0JUjLH5meXJw7s9gcqEDxvfTPFckIW77BVYq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDES5CUg5BNpX6uUWsircA4OP6susdSv%2B9OXMGevO%2BwBTlVVWYYy3JfmcyYr2dGiaOjKvjOmFJE6yr2BaLl5Hvwr3H3Jn2ByfHASYwZ2%2BfRtKWZwooZGrnw8bzWAr%2FqdOlrGYEwR7rVixlc3%2FqWxVcyyerNpkSskXAH5qKiQJXwNrl5XInQadZ42pC14rcRn%2BZz7OJywkvoNCoXfy%2FqLFEIq5hmN69S75yosqpomStuj24UQEsuTSU2eM9d8INEdjoQzv3hzMeJgmPE%2FFGDl1388S7zypoNJUzKN3Gvwe%2FGIoKrNfh%2Bj9rmFpEWTyd9n%2BMrSvUohQl4RQ4y0yhUx21EkO1gZH%2BRlZBwy1dr%2FZc5IierVzYBvvQE2%2Fr%2FjFDT12QPwaEXbfm1sFZnOC3qksTpmZ8sLg9Sm%2Bq13t%2F5Wd%2B3%2BrbnouUiGfXYnzHKtN%2FfN%2BuWk52BX2Ay0kYFKuLlQoePMVBFrouKu%2FFeGhfafj6SWeB4vnhArQyx6b4Nu35cBiOXCmNBvoWNoc%2B6BsvYRIDTRJrHKIDlIMDoD6S5KY3qSbb6iLr3NnopkjsBQ6nRKp%2FdCIVVQ%2BnGvxfZqMQyZk9FBgvuhB%2F3bOwILEcVl6L5QLqXahDTK28ziLriojpveQOfTaLPbJ2oMeW3h0MM%2BWic0GOqUBdtCtEoHWmCmqBM9xmX5l64y%2BXyfqZP%2F6A%2B44Scir%2B3i9qXFSLRYwjb%2Bs3vz0dDQR0Am2AfdGNh%2BJ4haKq3jbhzr3NOvc4sZNsb8hYWRtTerln2XSQZpK%2F7GtwnX1eEQQlVh9GPGjCL0Ua86u4M6eI0x5lfSkfIVl1mIavfpqJWd6GwIfMHmmWopvyOueQfxjDq84RgtwfL2JAa8hBwbaAcSzndCG&X-Amz-Signature=d321501ef68d7b9a2b22d116d9b9808a92cd4d3f9e15b5ffb16e1a9310f75056&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWYLWJ2O%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuMdcvpcucOOWJE7%2BEbioNMGBDoOitCVeCGt9lIvufAiEAuv0MtZrd0JUjLH5meXJw7s9gcqEDxvfTPFckIW77BVYq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDES5CUg5BNpX6uUWsircA4OP6susdSv%2B9OXMGevO%2BwBTlVVWYYy3JfmcyYr2dGiaOjKvjOmFJE6yr2BaLl5Hvwr3H3Jn2ByfHASYwZ2%2BfRtKWZwooZGrnw8bzWAr%2FqdOlrGYEwR7rVixlc3%2FqWxVcyyerNpkSskXAH5qKiQJXwNrl5XInQadZ42pC14rcRn%2BZz7OJywkvoNCoXfy%2FqLFEIq5hmN69S75yosqpomStuj24UQEsuTSU2eM9d8INEdjoQzv3hzMeJgmPE%2FFGDl1388S7zypoNJUzKN3Gvwe%2FGIoKrNfh%2Bj9rmFpEWTyd9n%2BMrSvUohQl4RQ4y0yhUx21EkO1gZH%2BRlZBwy1dr%2FZc5IierVzYBvvQE2%2Fr%2FjFDT12QPwaEXbfm1sFZnOC3qksTpmZ8sLg9Sm%2Bq13t%2F5Wd%2B3%2BrbnouUiGfXYnzHKtN%2FfN%2BuWk52BX2Ay0kYFKuLlQoePMVBFrouKu%2FFeGhfafj6SWeB4vnhArQyx6b4Nu35cBiOXCmNBvoWNoc%2B6BsvYRIDTRJrHKIDlIMDoD6S5KY3qSbb6iLr3NnopkjsBQ6nRKp%2FdCIVVQ%2BnGvxfZqMQyZk9FBgvuhB%2F3bOwILEcVl6L5QLqXahDTK28ziLriojpveQOfTaLPbJ2oMeW3h0MM%2BWic0GOqUBdtCtEoHWmCmqBM9xmX5l64y%2BXyfqZP%2F6A%2B44Scir%2B3i9qXFSLRYwjb%2Bs3vz0dDQR0Am2AfdGNh%2BJ4haKq3jbhzr3NOvc4sZNsb8hYWRtTerln2XSQZpK%2F7GtwnX1eEQQlVh9GPGjCL0Ua86u4M6eI0x5lfSkfIVl1mIavfpqJWd6GwIfMHmmWopvyOueQfxjDq84RgtwfL2JAa8hBwbaAcSzndCG&X-Amz-Signature=8e377696c6e2543b48ee4fe7e8da02b21a9bd48085a71589e3d3ed23943fbcd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWYLWJ2O%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuMdcvpcucOOWJE7%2BEbioNMGBDoOitCVeCGt9lIvufAiEAuv0MtZrd0JUjLH5meXJw7s9gcqEDxvfTPFckIW77BVYq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDES5CUg5BNpX6uUWsircA4OP6susdSv%2B9OXMGevO%2BwBTlVVWYYy3JfmcyYr2dGiaOjKvjOmFJE6yr2BaLl5Hvwr3H3Jn2ByfHASYwZ2%2BfRtKWZwooZGrnw8bzWAr%2FqdOlrGYEwR7rVixlc3%2FqWxVcyyerNpkSskXAH5qKiQJXwNrl5XInQadZ42pC14rcRn%2BZz7OJywkvoNCoXfy%2FqLFEIq5hmN69S75yosqpomStuj24UQEsuTSU2eM9d8INEdjoQzv3hzMeJgmPE%2FFGDl1388S7zypoNJUzKN3Gvwe%2FGIoKrNfh%2Bj9rmFpEWTyd9n%2BMrSvUohQl4RQ4y0yhUx21EkO1gZH%2BRlZBwy1dr%2FZc5IierVzYBvvQE2%2Fr%2FjFDT12QPwaEXbfm1sFZnOC3qksTpmZ8sLg9Sm%2Bq13t%2F5Wd%2B3%2BrbnouUiGfXYnzHKtN%2FfN%2BuWk52BX2Ay0kYFKuLlQoePMVBFrouKu%2FFeGhfafj6SWeB4vnhArQyx6b4Nu35cBiOXCmNBvoWNoc%2B6BsvYRIDTRJrHKIDlIMDoD6S5KY3qSbb6iLr3NnopkjsBQ6nRKp%2FdCIVVQ%2BnGvxfZqMQyZk9FBgvuhB%2F3bOwILEcVl6L5QLqXahDTK28ziLriojpveQOfTaLPbJ2oMeW3h0MM%2BWic0GOqUBdtCtEoHWmCmqBM9xmX5l64y%2BXyfqZP%2F6A%2B44Scir%2B3i9qXFSLRYwjb%2Bs3vz0dDQR0Am2AfdGNh%2BJ4haKq3jbhzr3NOvc4sZNsb8hYWRtTerln2XSQZpK%2F7GtwnX1eEQQlVh9GPGjCL0Ua86u4M6eI0x5lfSkfIVl1mIavfpqJWd6GwIfMHmmWopvyOueQfxjDq84RgtwfL2JAa8hBwbaAcSzndCG&X-Amz-Signature=d668a2a09ace790f69614517293b23b9a43a8e32007944786f3832500c4532ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWYLWJ2O%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBVuMdcvpcucOOWJE7%2BEbioNMGBDoOitCVeCGt9lIvufAiEAuv0MtZrd0JUjLH5meXJw7s9gcqEDxvfTPFckIW77BVYq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDES5CUg5BNpX6uUWsircA4OP6susdSv%2B9OXMGevO%2BwBTlVVWYYy3JfmcyYr2dGiaOjKvjOmFJE6yr2BaLl5Hvwr3H3Jn2ByfHASYwZ2%2BfRtKWZwooZGrnw8bzWAr%2FqdOlrGYEwR7rVixlc3%2FqWxVcyyerNpkSskXAH5qKiQJXwNrl5XInQadZ42pC14rcRn%2BZz7OJywkvoNCoXfy%2FqLFEIq5hmN69S75yosqpomStuj24UQEsuTSU2eM9d8INEdjoQzv3hzMeJgmPE%2FFGDl1388S7zypoNJUzKN3Gvwe%2FGIoKrNfh%2Bj9rmFpEWTyd9n%2BMrSvUohQl4RQ4y0yhUx21EkO1gZH%2BRlZBwy1dr%2FZc5IierVzYBvvQE2%2Fr%2FjFDT12QPwaEXbfm1sFZnOC3qksTpmZ8sLg9Sm%2Bq13t%2F5Wd%2B3%2BrbnouUiGfXYnzHKtN%2FfN%2BuWk52BX2Ay0kYFKuLlQoePMVBFrouKu%2FFeGhfafj6SWeB4vnhArQyx6b4Nu35cBiOXCmNBvoWNoc%2B6BsvYRIDTRJrHKIDlIMDoD6S5KY3qSbb6iLr3NnopkjsBQ6nRKp%2FdCIVVQ%2BnGvxfZqMQyZk9FBgvuhB%2F3bOwILEcVl6L5QLqXahDTK28ziLriojpveQOfTaLPbJ2oMeW3h0MM%2BWic0GOqUBdtCtEoHWmCmqBM9xmX5l64y%2BXyfqZP%2F6A%2B44Scir%2B3i9qXFSLRYwjb%2Bs3vz0dDQR0Am2AfdGNh%2BJ4haKq3jbhzr3NOvc4sZNsb8hYWRtTerln2XSQZpK%2F7GtwnX1eEQQlVh9GPGjCL0Ua86u4M6eI0x5lfSkfIVl1mIavfpqJWd6GwIfMHmmWopvyOueQfxjDq84RgtwfL2JAa8hBwbaAcSzndCG&X-Amz-Signature=6834281d67e7f04a778f69ddcba43f23fdd96ecace8c3ce8a946190f26071c82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

