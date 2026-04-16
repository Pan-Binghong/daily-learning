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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZKUHF3P%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FaAIhAXQ%2BWzeU0fig3VxrOfDEIo74SAVNcvaF3UdDqAiAeXwdGytkH3jR0bbdY%2FPb16zqpG0WRXZt7K%2FmD9D0BjyqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc82LuQnt8tJKgv0RKtwDb3kizHnTykbLkmkNHsb1kj0hkvIStWNKWsmWvf1YmkjjkJUJ17x%2FomAhr4bL3EQOmgMkdCwj%2FZsRmBIbmxkaQlw%2FiWrsztipXN9TO0R7dX9D8dAQwo8AtVUzjCNNCkI9lYKhhcr8IfnAI2rDxOVJbeS6hKeGjsBaN56eFNLehP1rWHKGkO2Hkm8E3bBabyihW2p6pImp6fqlJlfAJVJBWxtEqUrDNqdYzPFnOKNhJOvJ7dr0i1lDAakRu5dND3B7K3loM0VyWHoobd7Y2Jfp1tl%2BxfhS9p5LhI%2BSQLwP1DfodRlnkfQaTRvJe7kGsyE6%2FAaFFwr8DnRJ9fw5Mxf41UGm9kKtXgsMZxQ9e8WeoqhTrkQX2CdL%2FIXccjGtOQdig9H1dh91y8GVHZkS2wTeIIxpgEBoRzWmtOLRMXjgMR5VvbTNDJYR6Kx2%2BH8xtbv9KeX7R0Onmj4u9vXqtw5FLY7GI5M5ELCYhmfqBVLYxWyTre%2FAKlYY51A%2BVB%2FLWBkl9ZX6%2B%2BAnh%2BaekOzkzbcPE58jSvje6XHeb0RV52BWvQ2Vd7DabAzjOvkJaXU1M3Bcx3ue5pOTbBmiHaEYgfiUPi%2FPRBIN4oLoZUuNT80pJac6Y%2BocX0XXHn40Uzkw77SBzwY6pgEU%2F1tLG5l8zRLOFfwpm8HNDhrquZ75h8egwZ%2Bz3%2BAtPJQYleZom%2F0HBhP21Y0QVBiyv69TZEJ0ejti5VByrAVl4z%2BDy3PTAk%2BQ1%2B2qF%2BdQWHUGT8odfWA5J%2FYkhxBR043RK8X6u2cWsfBR0%2BW9UN7aslFBhx%2BRWw8WsNN4PANBD9YJkclNnNfBu8EY1L8lF9fqmMVnOsiMemICog8z7p5fpPDX%2BArp&X-Amz-Signature=722ed224ca3abad15e049bd08ecbdd2a08b1b2e6a3fd50cb3e67170daf2a6c3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZKUHF3P%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FaAIhAXQ%2BWzeU0fig3VxrOfDEIo74SAVNcvaF3UdDqAiAeXwdGytkH3jR0bbdY%2FPb16zqpG0WRXZt7K%2FmD9D0BjyqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc82LuQnt8tJKgv0RKtwDb3kizHnTykbLkmkNHsb1kj0hkvIStWNKWsmWvf1YmkjjkJUJ17x%2FomAhr4bL3EQOmgMkdCwj%2FZsRmBIbmxkaQlw%2FiWrsztipXN9TO0R7dX9D8dAQwo8AtVUzjCNNCkI9lYKhhcr8IfnAI2rDxOVJbeS6hKeGjsBaN56eFNLehP1rWHKGkO2Hkm8E3bBabyihW2p6pImp6fqlJlfAJVJBWxtEqUrDNqdYzPFnOKNhJOvJ7dr0i1lDAakRu5dND3B7K3loM0VyWHoobd7Y2Jfp1tl%2BxfhS9p5LhI%2BSQLwP1DfodRlnkfQaTRvJe7kGsyE6%2FAaFFwr8DnRJ9fw5Mxf41UGm9kKtXgsMZxQ9e8WeoqhTrkQX2CdL%2FIXccjGtOQdig9H1dh91y8GVHZkS2wTeIIxpgEBoRzWmtOLRMXjgMR5VvbTNDJYR6Kx2%2BH8xtbv9KeX7R0Onmj4u9vXqtw5FLY7GI5M5ELCYhmfqBVLYxWyTre%2FAKlYY51A%2BVB%2FLWBkl9ZX6%2B%2BAnh%2BaekOzkzbcPE58jSvje6XHeb0RV52BWvQ2Vd7DabAzjOvkJaXU1M3Bcx3ue5pOTbBmiHaEYgfiUPi%2FPRBIN4oLoZUuNT80pJac6Y%2BocX0XXHn40Uzkw77SBzwY6pgEU%2F1tLG5l8zRLOFfwpm8HNDhrquZ75h8egwZ%2Bz3%2BAtPJQYleZom%2F0HBhP21Y0QVBiyv69TZEJ0ejti5VByrAVl4z%2BDy3PTAk%2BQ1%2B2qF%2BdQWHUGT8odfWA5J%2FYkhxBR043RK8X6u2cWsfBR0%2BW9UN7aslFBhx%2BRWw8WsNN4PANBD9YJkclNnNfBu8EY1L8lF9fqmMVnOsiMemICog8z7p5fpPDX%2BArp&X-Amz-Signature=f7312b7f24d04e39c9b8bc561cdce0d8b5d1c66d233a763ce50443e291e1fbdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZKUHF3P%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FaAIhAXQ%2BWzeU0fig3VxrOfDEIo74SAVNcvaF3UdDqAiAeXwdGytkH3jR0bbdY%2FPb16zqpG0WRXZt7K%2FmD9D0BjyqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc82LuQnt8tJKgv0RKtwDb3kizHnTykbLkmkNHsb1kj0hkvIStWNKWsmWvf1YmkjjkJUJ17x%2FomAhr4bL3EQOmgMkdCwj%2FZsRmBIbmxkaQlw%2FiWrsztipXN9TO0R7dX9D8dAQwo8AtVUzjCNNCkI9lYKhhcr8IfnAI2rDxOVJbeS6hKeGjsBaN56eFNLehP1rWHKGkO2Hkm8E3bBabyihW2p6pImp6fqlJlfAJVJBWxtEqUrDNqdYzPFnOKNhJOvJ7dr0i1lDAakRu5dND3B7K3loM0VyWHoobd7Y2Jfp1tl%2BxfhS9p5LhI%2BSQLwP1DfodRlnkfQaTRvJe7kGsyE6%2FAaFFwr8DnRJ9fw5Mxf41UGm9kKtXgsMZxQ9e8WeoqhTrkQX2CdL%2FIXccjGtOQdig9H1dh91y8GVHZkS2wTeIIxpgEBoRzWmtOLRMXjgMR5VvbTNDJYR6Kx2%2BH8xtbv9KeX7R0Onmj4u9vXqtw5FLY7GI5M5ELCYhmfqBVLYxWyTre%2FAKlYY51A%2BVB%2FLWBkl9ZX6%2B%2BAnh%2BaekOzkzbcPE58jSvje6XHeb0RV52BWvQ2Vd7DabAzjOvkJaXU1M3Bcx3ue5pOTbBmiHaEYgfiUPi%2FPRBIN4oLoZUuNT80pJac6Y%2BocX0XXHn40Uzkw77SBzwY6pgEU%2F1tLG5l8zRLOFfwpm8HNDhrquZ75h8egwZ%2Bz3%2BAtPJQYleZom%2F0HBhP21Y0QVBiyv69TZEJ0ejti5VByrAVl4z%2BDy3PTAk%2BQ1%2B2qF%2BdQWHUGT8odfWA5J%2FYkhxBR043RK8X6u2cWsfBR0%2BW9UN7aslFBhx%2BRWw8WsNN4PANBD9YJkclNnNfBu8EY1L8lF9fqmMVnOsiMemICog8z7p5fpPDX%2BArp&X-Amz-Signature=262b798691865cba058f29cd00deeb1bf46122e1a9d88691f19591a8b7e18382&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZKUHF3P%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FaAIhAXQ%2BWzeU0fig3VxrOfDEIo74SAVNcvaF3UdDqAiAeXwdGytkH3jR0bbdY%2FPb16zqpG0WRXZt7K%2FmD9D0BjyqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc82LuQnt8tJKgv0RKtwDb3kizHnTykbLkmkNHsb1kj0hkvIStWNKWsmWvf1YmkjjkJUJ17x%2FomAhr4bL3EQOmgMkdCwj%2FZsRmBIbmxkaQlw%2FiWrsztipXN9TO0R7dX9D8dAQwo8AtVUzjCNNCkI9lYKhhcr8IfnAI2rDxOVJbeS6hKeGjsBaN56eFNLehP1rWHKGkO2Hkm8E3bBabyihW2p6pImp6fqlJlfAJVJBWxtEqUrDNqdYzPFnOKNhJOvJ7dr0i1lDAakRu5dND3B7K3loM0VyWHoobd7Y2Jfp1tl%2BxfhS9p5LhI%2BSQLwP1DfodRlnkfQaTRvJe7kGsyE6%2FAaFFwr8DnRJ9fw5Mxf41UGm9kKtXgsMZxQ9e8WeoqhTrkQX2CdL%2FIXccjGtOQdig9H1dh91y8GVHZkS2wTeIIxpgEBoRzWmtOLRMXjgMR5VvbTNDJYR6Kx2%2BH8xtbv9KeX7R0Onmj4u9vXqtw5FLY7GI5M5ELCYhmfqBVLYxWyTre%2FAKlYY51A%2BVB%2FLWBkl9ZX6%2B%2BAnh%2BaekOzkzbcPE58jSvje6XHeb0RV52BWvQ2Vd7DabAzjOvkJaXU1M3Bcx3ue5pOTbBmiHaEYgfiUPi%2FPRBIN4oLoZUuNT80pJac6Y%2BocX0XXHn40Uzkw77SBzwY6pgEU%2F1tLG5l8zRLOFfwpm8HNDhrquZ75h8egwZ%2Bz3%2BAtPJQYleZom%2F0HBhP21Y0QVBiyv69TZEJ0ejti5VByrAVl4z%2BDy3PTAk%2BQ1%2B2qF%2BdQWHUGT8odfWA5J%2FYkhxBR043RK8X6u2cWsfBR0%2BW9UN7aslFBhx%2BRWw8WsNN4PANBD9YJkclNnNfBu8EY1L8lF9fqmMVnOsiMemICog8z7p5fpPDX%2BArp&X-Amz-Signature=720119178f5213c668d123d02a24520b2785d4a9aa9650d932c98b59f70748b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZKUHF3P%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FaAIhAXQ%2BWzeU0fig3VxrOfDEIo74SAVNcvaF3UdDqAiAeXwdGytkH3jR0bbdY%2FPb16zqpG0WRXZt7K%2FmD9D0BjyqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc82LuQnt8tJKgv0RKtwDb3kizHnTykbLkmkNHsb1kj0hkvIStWNKWsmWvf1YmkjjkJUJ17x%2FomAhr4bL3EQOmgMkdCwj%2FZsRmBIbmxkaQlw%2FiWrsztipXN9TO0R7dX9D8dAQwo8AtVUzjCNNCkI9lYKhhcr8IfnAI2rDxOVJbeS6hKeGjsBaN56eFNLehP1rWHKGkO2Hkm8E3bBabyihW2p6pImp6fqlJlfAJVJBWxtEqUrDNqdYzPFnOKNhJOvJ7dr0i1lDAakRu5dND3B7K3loM0VyWHoobd7Y2Jfp1tl%2BxfhS9p5LhI%2BSQLwP1DfodRlnkfQaTRvJe7kGsyE6%2FAaFFwr8DnRJ9fw5Mxf41UGm9kKtXgsMZxQ9e8WeoqhTrkQX2CdL%2FIXccjGtOQdig9H1dh91y8GVHZkS2wTeIIxpgEBoRzWmtOLRMXjgMR5VvbTNDJYR6Kx2%2BH8xtbv9KeX7R0Onmj4u9vXqtw5FLY7GI5M5ELCYhmfqBVLYxWyTre%2FAKlYY51A%2BVB%2FLWBkl9ZX6%2B%2BAnh%2BaekOzkzbcPE58jSvje6XHeb0RV52BWvQ2Vd7DabAzjOvkJaXU1M3Bcx3ue5pOTbBmiHaEYgfiUPi%2FPRBIN4oLoZUuNT80pJac6Y%2BocX0XXHn40Uzkw77SBzwY6pgEU%2F1tLG5l8zRLOFfwpm8HNDhrquZ75h8egwZ%2Bz3%2BAtPJQYleZom%2F0HBhP21Y0QVBiyv69TZEJ0ejti5VByrAVl4z%2BDy3PTAk%2BQ1%2B2qF%2BdQWHUGT8odfWA5J%2FYkhxBR043RK8X6u2cWsfBR0%2BW9UN7aslFBhx%2BRWw8WsNN4PANBD9YJkclNnNfBu8EY1L8lF9fqmMVnOsiMemICog8z7p5fpPDX%2BArp&X-Amz-Signature=1ecb23646fdb18edbe731e0acd7c6569bf307141db25308c6c2421d3888c09b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZKUHF3P%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FaAIhAXQ%2BWzeU0fig3VxrOfDEIo74SAVNcvaF3UdDqAiAeXwdGytkH3jR0bbdY%2FPb16zqpG0WRXZt7K%2FmD9D0BjyqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc82LuQnt8tJKgv0RKtwDb3kizHnTykbLkmkNHsb1kj0hkvIStWNKWsmWvf1YmkjjkJUJ17x%2FomAhr4bL3EQOmgMkdCwj%2FZsRmBIbmxkaQlw%2FiWrsztipXN9TO0R7dX9D8dAQwo8AtVUzjCNNCkI9lYKhhcr8IfnAI2rDxOVJbeS6hKeGjsBaN56eFNLehP1rWHKGkO2Hkm8E3bBabyihW2p6pImp6fqlJlfAJVJBWxtEqUrDNqdYzPFnOKNhJOvJ7dr0i1lDAakRu5dND3B7K3loM0VyWHoobd7Y2Jfp1tl%2BxfhS9p5LhI%2BSQLwP1DfodRlnkfQaTRvJe7kGsyE6%2FAaFFwr8DnRJ9fw5Mxf41UGm9kKtXgsMZxQ9e8WeoqhTrkQX2CdL%2FIXccjGtOQdig9H1dh91y8GVHZkS2wTeIIxpgEBoRzWmtOLRMXjgMR5VvbTNDJYR6Kx2%2BH8xtbv9KeX7R0Onmj4u9vXqtw5FLY7GI5M5ELCYhmfqBVLYxWyTre%2FAKlYY51A%2BVB%2FLWBkl9ZX6%2B%2BAnh%2BaekOzkzbcPE58jSvje6XHeb0RV52BWvQ2Vd7DabAzjOvkJaXU1M3Bcx3ue5pOTbBmiHaEYgfiUPi%2FPRBIN4oLoZUuNT80pJac6Y%2BocX0XXHn40Uzkw77SBzwY6pgEU%2F1tLG5l8zRLOFfwpm8HNDhrquZ75h8egwZ%2Bz3%2BAtPJQYleZom%2F0HBhP21Y0QVBiyv69TZEJ0ejti5VByrAVl4z%2BDy3PTAk%2BQ1%2B2qF%2BdQWHUGT8odfWA5J%2FYkhxBR043RK8X6u2cWsfBR0%2BW9UN7aslFBhx%2BRWw8WsNN4PANBD9YJkclNnNfBu8EY1L8lF9fqmMVnOsiMemICog8z7p5fpPDX%2BArp&X-Amz-Signature=03466b586dcb4c1c14f381943d1dbf47715c049f11149f30eadca217d9734d11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZKUHF3P%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FaAIhAXQ%2BWzeU0fig3VxrOfDEIo74SAVNcvaF3UdDqAiAeXwdGytkH3jR0bbdY%2FPb16zqpG0WRXZt7K%2FmD9D0BjyqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc82LuQnt8tJKgv0RKtwDb3kizHnTykbLkmkNHsb1kj0hkvIStWNKWsmWvf1YmkjjkJUJ17x%2FomAhr4bL3EQOmgMkdCwj%2FZsRmBIbmxkaQlw%2FiWrsztipXN9TO0R7dX9D8dAQwo8AtVUzjCNNCkI9lYKhhcr8IfnAI2rDxOVJbeS6hKeGjsBaN56eFNLehP1rWHKGkO2Hkm8E3bBabyihW2p6pImp6fqlJlfAJVJBWxtEqUrDNqdYzPFnOKNhJOvJ7dr0i1lDAakRu5dND3B7K3loM0VyWHoobd7Y2Jfp1tl%2BxfhS9p5LhI%2BSQLwP1DfodRlnkfQaTRvJe7kGsyE6%2FAaFFwr8DnRJ9fw5Mxf41UGm9kKtXgsMZxQ9e8WeoqhTrkQX2CdL%2FIXccjGtOQdig9H1dh91y8GVHZkS2wTeIIxpgEBoRzWmtOLRMXjgMR5VvbTNDJYR6Kx2%2BH8xtbv9KeX7R0Onmj4u9vXqtw5FLY7GI5M5ELCYhmfqBVLYxWyTre%2FAKlYY51A%2BVB%2FLWBkl9ZX6%2B%2BAnh%2BaekOzkzbcPE58jSvje6XHeb0RV52BWvQ2Vd7DabAzjOvkJaXU1M3Bcx3ue5pOTbBmiHaEYgfiUPi%2FPRBIN4oLoZUuNT80pJac6Y%2BocX0XXHn40Uzkw77SBzwY6pgEU%2F1tLG5l8zRLOFfwpm8HNDhrquZ75h8egwZ%2Bz3%2BAtPJQYleZom%2F0HBhP21Y0QVBiyv69TZEJ0ejti5VByrAVl4z%2BDy3PTAk%2BQ1%2B2qF%2BdQWHUGT8odfWA5J%2FYkhxBR043RK8X6u2cWsfBR0%2BW9UN7aslFBhx%2BRWw8WsNN4PANBD9YJkclNnNfBu8EY1L8lF9fqmMVnOsiMemICog8z7p5fpPDX%2BArp&X-Amz-Signature=ef0424e19d7c3bca424ed1194ed4a469dcab0f0d41ebad3ebad074d0acb2a1fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZKUHF3P%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FaAIhAXQ%2BWzeU0fig3VxrOfDEIo74SAVNcvaF3UdDqAiAeXwdGytkH3jR0bbdY%2FPb16zqpG0WRXZt7K%2FmD9D0BjyqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc82LuQnt8tJKgv0RKtwDb3kizHnTykbLkmkNHsb1kj0hkvIStWNKWsmWvf1YmkjjkJUJ17x%2FomAhr4bL3EQOmgMkdCwj%2FZsRmBIbmxkaQlw%2FiWrsztipXN9TO0R7dX9D8dAQwo8AtVUzjCNNCkI9lYKhhcr8IfnAI2rDxOVJbeS6hKeGjsBaN56eFNLehP1rWHKGkO2Hkm8E3bBabyihW2p6pImp6fqlJlfAJVJBWxtEqUrDNqdYzPFnOKNhJOvJ7dr0i1lDAakRu5dND3B7K3loM0VyWHoobd7Y2Jfp1tl%2BxfhS9p5LhI%2BSQLwP1DfodRlnkfQaTRvJe7kGsyE6%2FAaFFwr8DnRJ9fw5Mxf41UGm9kKtXgsMZxQ9e8WeoqhTrkQX2CdL%2FIXccjGtOQdig9H1dh91y8GVHZkS2wTeIIxpgEBoRzWmtOLRMXjgMR5VvbTNDJYR6Kx2%2BH8xtbv9KeX7R0Onmj4u9vXqtw5FLY7GI5M5ELCYhmfqBVLYxWyTre%2FAKlYY51A%2BVB%2FLWBkl9ZX6%2B%2BAnh%2BaekOzkzbcPE58jSvje6XHeb0RV52BWvQ2Vd7DabAzjOvkJaXU1M3Bcx3ue5pOTbBmiHaEYgfiUPi%2FPRBIN4oLoZUuNT80pJac6Y%2BocX0XXHn40Uzkw77SBzwY6pgEU%2F1tLG5l8zRLOFfwpm8HNDhrquZ75h8egwZ%2Bz3%2BAtPJQYleZom%2F0HBhP21Y0QVBiyv69TZEJ0ejti5VByrAVl4z%2BDy3PTAk%2BQ1%2B2qF%2BdQWHUGT8odfWA5J%2FYkhxBR043RK8X6u2cWsfBR0%2BW9UN7aslFBhx%2BRWw8WsNN4PANBD9YJkclNnNfBu8EY1L8lF9fqmMVnOsiMemICog8z7p5fpPDX%2BArp&X-Amz-Signature=61a535cb9702b721973b1a61ff77a8dd94629d59680a892f4019140b5408a259&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZKUHF3P%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FaAIhAXQ%2BWzeU0fig3VxrOfDEIo74SAVNcvaF3UdDqAiAeXwdGytkH3jR0bbdY%2FPb16zqpG0WRXZt7K%2FmD9D0BjyqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc82LuQnt8tJKgv0RKtwDb3kizHnTykbLkmkNHsb1kj0hkvIStWNKWsmWvf1YmkjjkJUJ17x%2FomAhr4bL3EQOmgMkdCwj%2FZsRmBIbmxkaQlw%2FiWrsztipXN9TO0R7dX9D8dAQwo8AtVUzjCNNCkI9lYKhhcr8IfnAI2rDxOVJbeS6hKeGjsBaN56eFNLehP1rWHKGkO2Hkm8E3bBabyihW2p6pImp6fqlJlfAJVJBWxtEqUrDNqdYzPFnOKNhJOvJ7dr0i1lDAakRu5dND3B7K3loM0VyWHoobd7Y2Jfp1tl%2BxfhS9p5LhI%2BSQLwP1DfodRlnkfQaTRvJe7kGsyE6%2FAaFFwr8DnRJ9fw5Mxf41UGm9kKtXgsMZxQ9e8WeoqhTrkQX2CdL%2FIXccjGtOQdig9H1dh91y8GVHZkS2wTeIIxpgEBoRzWmtOLRMXjgMR5VvbTNDJYR6Kx2%2BH8xtbv9KeX7R0Onmj4u9vXqtw5FLY7GI5M5ELCYhmfqBVLYxWyTre%2FAKlYY51A%2BVB%2FLWBkl9ZX6%2B%2BAnh%2BaekOzkzbcPE58jSvje6XHeb0RV52BWvQ2Vd7DabAzjOvkJaXU1M3Bcx3ue5pOTbBmiHaEYgfiUPi%2FPRBIN4oLoZUuNT80pJac6Y%2BocX0XXHn40Uzkw77SBzwY6pgEU%2F1tLG5l8zRLOFfwpm8HNDhrquZ75h8egwZ%2Bz3%2BAtPJQYleZom%2F0HBhP21Y0QVBiyv69TZEJ0ejti5VByrAVl4z%2BDy3PTAk%2BQ1%2B2qF%2BdQWHUGT8odfWA5J%2FYkhxBR043RK8X6u2cWsfBR0%2BW9UN7aslFBhx%2BRWw8WsNN4PANBD9YJkclNnNfBu8EY1L8lF9fqmMVnOsiMemICog8z7p5fpPDX%2BArp&X-Amz-Signature=6dcd535af9a5aa978f8eff3d1d13a8c6689da95fc89bfbdfc7d3053b89f146d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZKUHF3P%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2FaAIhAXQ%2BWzeU0fig3VxrOfDEIo74SAVNcvaF3UdDqAiAeXwdGytkH3jR0bbdY%2FPb16zqpG0WRXZt7K%2FmD9D0BjyqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc82LuQnt8tJKgv0RKtwDb3kizHnTykbLkmkNHsb1kj0hkvIStWNKWsmWvf1YmkjjkJUJ17x%2FomAhr4bL3EQOmgMkdCwj%2FZsRmBIbmxkaQlw%2FiWrsztipXN9TO0R7dX9D8dAQwo8AtVUzjCNNCkI9lYKhhcr8IfnAI2rDxOVJbeS6hKeGjsBaN56eFNLehP1rWHKGkO2Hkm8E3bBabyihW2p6pImp6fqlJlfAJVJBWxtEqUrDNqdYzPFnOKNhJOvJ7dr0i1lDAakRu5dND3B7K3loM0VyWHoobd7Y2Jfp1tl%2BxfhS9p5LhI%2BSQLwP1DfodRlnkfQaTRvJe7kGsyE6%2FAaFFwr8DnRJ9fw5Mxf41UGm9kKtXgsMZxQ9e8WeoqhTrkQX2CdL%2FIXccjGtOQdig9H1dh91y8GVHZkS2wTeIIxpgEBoRzWmtOLRMXjgMR5VvbTNDJYR6Kx2%2BH8xtbv9KeX7R0Onmj4u9vXqtw5FLY7GI5M5ELCYhmfqBVLYxWyTre%2FAKlYY51A%2BVB%2FLWBkl9ZX6%2B%2BAnh%2BaekOzkzbcPE58jSvje6XHeb0RV52BWvQ2Vd7DabAzjOvkJaXU1M3Bcx3ue5pOTbBmiHaEYgfiUPi%2FPRBIN4oLoZUuNT80pJac6Y%2BocX0XXHn40Uzkw77SBzwY6pgEU%2F1tLG5l8zRLOFfwpm8HNDhrquZ75h8egwZ%2Bz3%2BAtPJQYleZom%2F0HBhP21Y0QVBiyv69TZEJ0ejti5VByrAVl4z%2BDy3PTAk%2BQ1%2B2qF%2BdQWHUGT8odfWA5J%2FYkhxBR043RK8X6u2cWsfBR0%2BW9UN7aslFBhx%2BRWw8WsNN4PANBD9YJkclNnNfBu8EY1L8lF9fqmMVnOsiMemICog8z7p5fpPDX%2BArp&X-Amz-Signature=45f97bfb005594b9a095eac4e8b13c9ea3efd11dc7014cd892f4d55033270635&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

