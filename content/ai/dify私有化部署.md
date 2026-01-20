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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAGJSEC%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2WkfW4%2Fa5GLZFkQWbXXBJfjs8lK5yFWA4QjOVmfZC3gIhANgaQXeHbQ%2FygSGnJ6L1K60gA%2Bwwr8VFvks0KZbrAcyIKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwregz0Bx1RmOsKJgYq3AMUCmzv8D5MlUCLay6fm%2FI5Wijy0vsr%2BJvicMw752eSlZUOsBbTFN2T3aJ%2BKCO219zbDbYw6q1v%2B5kXHAgMienpkxgvxsElVS854PoyzKDG2BvLRCThBCbek1WYHOBnZ7SZcoQ4OCl7jSZS2oCQtQ6sFrYgAWltX01HMq184C6yVenVslkqCel0xS3khSX%2F68hN%2Bukxu20yNlvEkSxZUYElnOnte5o80JJuR5xO54iuSC%2BISfvAKZruVIHcGyGXpiKv5Ayd%2BUsBlXKXHj7n8UiDgKRoFoFS67JtUTPuOoKt3G7pcLW0r9ViaPWo1TWo6aqmpOZy4uYcgDP7HTXhPzaIrWi9pP2TDii%2FTPy2sXL7Z1BU1%2FO2%2FehaLmwS4Esc%2FAWNYuNNsNtV6ZlT7dnOk7JT6qSjZyZPHS7hjb9y5jM7f2KvrjigZDnRLDSLl5hl4UB3OQNU819eOH2emA3ZzyQ%2BaIgvYSXrKCfMR6N3HD7x5OpWJi2Fg4YcB03rmcrYYRE11RcTPRQ6QWjynySbVKwvGFEXAWP5imn7RRuhPabi3tEi35PTz0ckKZ4zhJaCP2v%2FfrtJTpfKnEfuIXpbF%2B7PQ8msI1k1i9bbDHEpoHVkGv2oyWCV7wkTbRBl3jD59LrLBjqkAWvRhl8lT7PRXodzoVuxxLbkZxyNTOEw8mIeJY%2B%2B4PkGumcAxU7U9tohd3RSsABDIdHMj8pvDUtOdrpgh1Pnk%2BCeogYKrl5Ugc9BfqfrICSLDZZYQfE2GGVaNw1tgThqoJZqVIiuWZRXcOCHq4YNURPuebxbDT9ma%2Bq5lEi%2BH053EQxXN6rKEIKbXvL2laoxQwj8FNaLa068AbepSBSkmsk%2FvqjP&X-Amz-Signature=a1eeb41de6b6f3593b789088e220519605af410d70f5efa75e5e092ef56b7015&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAGJSEC%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2WkfW4%2Fa5GLZFkQWbXXBJfjs8lK5yFWA4QjOVmfZC3gIhANgaQXeHbQ%2FygSGnJ6L1K60gA%2Bwwr8VFvks0KZbrAcyIKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwregz0Bx1RmOsKJgYq3AMUCmzv8D5MlUCLay6fm%2FI5Wijy0vsr%2BJvicMw752eSlZUOsBbTFN2T3aJ%2BKCO219zbDbYw6q1v%2B5kXHAgMienpkxgvxsElVS854PoyzKDG2BvLRCThBCbek1WYHOBnZ7SZcoQ4OCl7jSZS2oCQtQ6sFrYgAWltX01HMq184C6yVenVslkqCel0xS3khSX%2F68hN%2Bukxu20yNlvEkSxZUYElnOnte5o80JJuR5xO54iuSC%2BISfvAKZruVIHcGyGXpiKv5Ayd%2BUsBlXKXHj7n8UiDgKRoFoFS67JtUTPuOoKt3G7pcLW0r9ViaPWo1TWo6aqmpOZy4uYcgDP7HTXhPzaIrWi9pP2TDii%2FTPy2sXL7Z1BU1%2FO2%2FehaLmwS4Esc%2FAWNYuNNsNtV6ZlT7dnOk7JT6qSjZyZPHS7hjb9y5jM7f2KvrjigZDnRLDSLl5hl4UB3OQNU819eOH2emA3ZzyQ%2BaIgvYSXrKCfMR6N3HD7x5OpWJi2Fg4YcB03rmcrYYRE11RcTPRQ6QWjynySbVKwvGFEXAWP5imn7RRuhPabi3tEi35PTz0ckKZ4zhJaCP2v%2FfrtJTpfKnEfuIXpbF%2B7PQ8msI1k1i9bbDHEpoHVkGv2oyWCV7wkTbRBl3jD59LrLBjqkAWvRhl8lT7PRXodzoVuxxLbkZxyNTOEw8mIeJY%2B%2B4PkGumcAxU7U9tohd3RSsABDIdHMj8pvDUtOdrpgh1Pnk%2BCeogYKrl5Ugc9BfqfrICSLDZZYQfE2GGVaNw1tgThqoJZqVIiuWZRXcOCHq4YNURPuebxbDT9ma%2Bq5lEi%2BH053EQxXN6rKEIKbXvL2laoxQwj8FNaLa068AbepSBSkmsk%2FvqjP&X-Amz-Signature=eaccd10f0c87863e2891754053881a3188dba353c4beb8e4b30690766f7a1b9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAGJSEC%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2WkfW4%2Fa5GLZFkQWbXXBJfjs8lK5yFWA4QjOVmfZC3gIhANgaQXeHbQ%2FygSGnJ6L1K60gA%2Bwwr8VFvks0KZbrAcyIKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwregz0Bx1RmOsKJgYq3AMUCmzv8D5MlUCLay6fm%2FI5Wijy0vsr%2BJvicMw752eSlZUOsBbTFN2T3aJ%2BKCO219zbDbYw6q1v%2B5kXHAgMienpkxgvxsElVS854PoyzKDG2BvLRCThBCbek1WYHOBnZ7SZcoQ4OCl7jSZS2oCQtQ6sFrYgAWltX01HMq184C6yVenVslkqCel0xS3khSX%2F68hN%2Bukxu20yNlvEkSxZUYElnOnte5o80JJuR5xO54iuSC%2BISfvAKZruVIHcGyGXpiKv5Ayd%2BUsBlXKXHj7n8UiDgKRoFoFS67JtUTPuOoKt3G7pcLW0r9ViaPWo1TWo6aqmpOZy4uYcgDP7HTXhPzaIrWi9pP2TDii%2FTPy2sXL7Z1BU1%2FO2%2FehaLmwS4Esc%2FAWNYuNNsNtV6ZlT7dnOk7JT6qSjZyZPHS7hjb9y5jM7f2KvrjigZDnRLDSLl5hl4UB3OQNU819eOH2emA3ZzyQ%2BaIgvYSXrKCfMR6N3HD7x5OpWJi2Fg4YcB03rmcrYYRE11RcTPRQ6QWjynySbVKwvGFEXAWP5imn7RRuhPabi3tEi35PTz0ckKZ4zhJaCP2v%2FfrtJTpfKnEfuIXpbF%2B7PQ8msI1k1i9bbDHEpoHVkGv2oyWCV7wkTbRBl3jD59LrLBjqkAWvRhl8lT7PRXodzoVuxxLbkZxyNTOEw8mIeJY%2B%2B4PkGumcAxU7U9tohd3RSsABDIdHMj8pvDUtOdrpgh1Pnk%2BCeogYKrl5Ugc9BfqfrICSLDZZYQfE2GGVaNw1tgThqoJZqVIiuWZRXcOCHq4YNURPuebxbDT9ma%2Bq5lEi%2BH053EQxXN6rKEIKbXvL2laoxQwj8FNaLa068AbepSBSkmsk%2FvqjP&X-Amz-Signature=5494b59e5d3c849a47cee569edd4a16052ebcd2472f810b20c6bda470de8e7be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAGJSEC%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2WkfW4%2Fa5GLZFkQWbXXBJfjs8lK5yFWA4QjOVmfZC3gIhANgaQXeHbQ%2FygSGnJ6L1K60gA%2Bwwr8VFvks0KZbrAcyIKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwregz0Bx1RmOsKJgYq3AMUCmzv8D5MlUCLay6fm%2FI5Wijy0vsr%2BJvicMw752eSlZUOsBbTFN2T3aJ%2BKCO219zbDbYw6q1v%2B5kXHAgMienpkxgvxsElVS854PoyzKDG2BvLRCThBCbek1WYHOBnZ7SZcoQ4OCl7jSZS2oCQtQ6sFrYgAWltX01HMq184C6yVenVslkqCel0xS3khSX%2F68hN%2Bukxu20yNlvEkSxZUYElnOnte5o80JJuR5xO54iuSC%2BISfvAKZruVIHcGyGXpiKv5Ayd%2BUsBlXKXHj7n8UiDgKRoFoFS67JtUTPuOoKt3G7pcLW0r9ViaPWo1TWo6aqmpOZy4uYcgDP7HTXhPzaIrWi9pP2TDii%2FTPy2sXL7Z1BU1%2FO2%2FehaLmwS4Esc%2FAWNYuNNsNtV6ZlT7dnOk7JT6qSjZyZPHS7hjb9y5jM7f2KvrjigZDnRLDSLl5hl4UB3OQNU819eOH2emA3ZzyQ%2BaIgvYSXrKCfMR6N3HD7x5OpWJi2Fg4YcB03rmcrYYRE11RcTPRQ6QWjynySbVKwvGFEXAWP5imn7RRuhPabi3tEi35PTz0ckKZ4zhJaCP2v%2FfrtJTpfKnEfuIXpbF%2B7PQ8msI1k1i9bbDHEpoHVkGv2oyWCV7wkTbRBl3jD59LrLBjqkAWvRhl8lT7PRXodzoVuxxLbkZxyNTOEw8mIeJY%2B%2B4PkGumcAxU7U9tohd3RSsABDIdHMj8pvDUtOdrpgh1Pnk%2BCeogYKrl5Ugc9BfqfrICSLDZZYQfE2GGVaNw1tgThqoJZqVIiuWZRXcOCHq4YNURPuebxbDT9ma%2Bq5lEi%2BH053EQxXN6rKEIKbXvL2laoxQwj8FNaLa068AbepSBSkmsk%2FvqjP&X-Amz-Signature=65c99d189f3c82fb088c84fe1486e37036bb8b96494db645d1d930b2e2d243d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAGJSEC%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2WkfW4%2Fa5GLZFkQWbXXBJfjs8lK5yFWA4QjOVmfZC3gIhANgaQXeHbQ%2FygSGnJ6L1K60gA%2Bwwr8VFvks0KZbrAcyIKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwregz0Bx1RmOsKJgYq3AMUCmzv8D5MlUCLay6fm%2FI5Wijy0vsr%2BJvicMw752eSlZUOsBbTFN2T3aJ%2BKCO219zbDbYw6q1v%2B5kXHAgMienpkxgvxsElVS854PoyzKDG2BvLRCThBCbek1WYHOBnZ7SZcoQ4OCl7jSZS2oCQtQ6sFrYgAWltX01HMq184C6yVenVslkqCel0xS3khSX%2F68hN%2Bukxu20yNlvEkSxZUYElnOnte5o80JJuR5xO54iuSC%2BISfvAKZruVIHcGyGXpiKv5Ayd%2BUsBlXKXHj7n8UiDgKRoFoFS67JtUTPuOoKt3G7pcLW0r9ViaPWo1TWo6aqmpOZy4uYcgDP7HTXhPzaIrWi9pP2TDii%2FTPy2sXL7Z1BU1%2FO2%2FehaLmwS4Esc%2FAWNYuNNsNtV6ZlT7dnOk7JT6qSjZyZPHS7hjb9y5jM7f2KvrjigZDnRLDSLl5hl4UB3OQNU819eOH2emA3ZzyQ%2BaIgvYSXrKCfMR6N3HD7x5OpWJi2Fg4YcB03rmcrYYRE11RcTPRQ6QWjynySbVKwvGFEXAWP5imn7RRuhPabi3tEi35PTz0ckKZ4zhJaCP2v%2FfrtJTpfKnEfuIXpbF%2B7PQ8msI1k1i9bbDHEpoHVkGv2oyWCV7wkTbRBl3jD59LrLBjqkAWvRhl8lT7PRXodzoVuxxLbkZxyNTOEw8mIeJY%2B%2B4PkGumcAxU7U9tohd3RSsABDIdHMj8pvDUtOdrpgh1Pnk%2BCeogYKrl5Ugc9BfqfrICSLDZZYQfE2GGVaNw1tgThqoJZqVIiuWZRXcOCHq4YNURPuebxbDT9ma%2Bq5lEi%2BH053EQxXN6rKEIKbXvL2laoxQwj8FNaLa068AbepSBSkmsk%2FvqjP&X-Amz-Signature=2776a392a68eff791f064a742c6a7e0095da1b4a0089c2b184501b1e2f46a3e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAGJSEC%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2WkfW4%2Fa5GLZFkQWbXXBJfjs8lK5yFWA4QjOVmfZC3gIhANgaQXeHbQ%2FygSGnJ6L1K60gA%2Bwwr8VFvks0KZbrAcyIKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwregz0Bx1RmOsKJgYq3AMUCmzv8D5MlUCLay6fm%2FI5Wijy0vsr%2BJvicMw752eSlZUOsBbTFN2T3aJ%2BKCO219zbDbYw6q1v%2B5kXHAgMienpkxgvxsElVS854PoyzKDG2BvLRCThBCbek1WYHOBnZ7SZcoQ4OCl7jSZS2oCQtQ6sFrYgAWltX01HMq184C6yVenVslkqCel0xS3khSX%2F68hN%2Bukxu20yNlvEkSxZUYElnOnte5o80JJuR5xO54iuSC%2BISfvAKZruVIHcGyGXpiKv5Ayd%2BUsBlXKXHj7n8UiDgKRoFoFS67JtUTPuOoKt3G7pcLW0r9ViaPWo1TWo6aqmpOZy4uYcgDP7HTXhPzaIrWi9pP2TDii%2FTPy2sXL7Z1BU1%2FO2%2FehaLmwS4Esc%2FAWNYuNNsNtV6ZlT7dnOk7JT6qSjZyZPHS7hjb9y5jM7f2KvrjigZDnRLDSLl5hl4UB3OQNU819eOH2emA3ZzyQ%2BaIgvYSXrKCfMR6N3HD7x5OpWJi2Fg4YcB03rmcrYYRE11RcTPRQ6QWjynySbVKwvGFEXAWP5imn7RRuhPabi3tEi35PTz0ckKZ4zhJaCP2v%2FfrtJTpfKnEfuIXpbF%2B7PQ8msI1k1i9bbDHEpoHVkGv2oyWCV7wkTbRBl3jD59LrLBjqkAWvRhl8lT7PRXodzoVuxxLbkZxyNTOEw8mIeJY%2B%2B4PkGumcAxU7U9tohd3RSsABDIdHMj8pvDUtOdrpgh1Pnk%2BCeogYKrl5Ugc9BfqfrICSLDZZYQfE2GGVaNw1tgThqoJZqVIiuWZRXcOCHq4YNURPuebxbDT9ma%2Bq5lEi%2BH053EQxXN6rKEIKbXvL2laoxQwj8FNaLa068AbepSBSkmsk%2FvqjP&X-Amz-Signature=ad991a949bdf8f216d055542029873e9f110c4ed2465906fba1a4f96e73a9872&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAGJSEC%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2WkfW4%2Fa5GLZFkQWbXXBJfjs8lK5yFWA4QjOVmfZC3gIhANgaQXeHbQ%2FygSGnJ6L1K60gA%2Bwwr8VFvks0KZbrAcyIKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwregz0Bx1RmOsKJgYq3AMUCmzv8D5MlUCLay6fm%2FI5Wijy0vsr%2BJvicMw752eSlZUOsBbTFN2T3aJ%2BKCO219zbDbYw6q1v%2B5kXHAgMienpkxgvxsElVS854PoyzKDG2BvLRCThBCbek1WYHOBnZ7SZcoQ4OCl7jSZS2oCQtQ6sFrYgAWltX01HMq184C6yVenVslkqCel0xS3khSX%2F68hN%2Bukxu20yNlvEkSxZUYElnOnte5o80JJuR5xO54iuSC%2BISfvAKZruVIHcGyGXpiKv5Ayd%2BUsBlXKXHj7n8UiDgKRoFoFS67JtUTPuOoKt3G7pcLW0r9ViaPWo1TWo6aqmpOZy4uYcgDP7HTXhPzaIrWi9pP2TDii%2FTPy2sXL7Z1BU1%2FO2%2FehaLmwS4Esc%2FAWNYuNNsNtV6ZlT7dnOk7JT6qSjZyZPHS7hjb9y5jM7f2KvrjigZDnRLDSLl5hl4UB3OQNU819eOH2emA3ZzyQ%2BaIgvYSXrKCfMR6N3HD7x5OpWJi2Fg4YcB03rmcrYYRE11RcTPRQ6QWjynySbVKwvGFEXAWP5imn7RRuhPabi3tEi35PTz0ckKZ4zhJaCP2v%2FfrtJTpfKnEfuIXpbF%2B7PQ8msI1k1i9bbDHEpoHVkGv2oyWCV7wkTbRBl3jD59LrLBjqkAWvRhl8lT7PRXodzoVuxxLbkZxyNTOEw8mIeJY%2B%2B4PkGumcAxU7U9tohd3RSsABDIdHMj8pvDUtOdrpgh1Pnk%2BCeogYKrl5Ugc9BfqfrICSLDZZYQfE2GGVaNw1tgThqoJZqVIiuWZRXcOCHq4YNURPuebxbDT9ma%2Bq5lEi%2BH053EQxXN6rKEIKbXvL2laoxQwj8FNaLa068AbepSBSkmsk%2FvqjP&X-Amz-Signature=d9baaac62f15cf35bcd45673a725f20d037e00f711049fa3a846a1db715ffe5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAGJSEC%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2WkfW4%2Fa5GLZFkQWbXXBJfjs8lK5yFWA4QjOVmfZC3gIhANgaQXeHbQ%2FygSGnJ6L1K60gA%2Bwwr8VFvks0KZbrAcyIKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwregz0Bx1RmOsKJgYq3AMUCmzv8D5MlUCLay6fm%2FI5Wijy0vsr%2BJvicMw752eSlZUOsBbTFN2T3aJ%2BKCO219zbDbYw6q1v%2B5kXHAgMienpkxgvxsElVS854PoyzKDG2BvLRCThBCbek1WYHOBnZ7SZcoQ4OCl7jSZS2oCQtQ6sFrYgAWltX01HMq184C6yVenVslkqCel0xS3khSX%2F68hN%2Bukxu20yNlvEkSxZUYElnOnte5o80JJuR5xO54iuSC%2BISfvAKZruVIHcGyGXpiKv5Ayd%2BUsBlXKXHj7n8UiDgKRoFoFS67JtUTPuOoKt3G7pcLW0r9ViaPWo1TWo6aqmpOZy4uYcgDP7HTXhPzaIrWi9pP2TDii%2FTPy2sXL7Z1BU1%2FO2%2FehaLmwS4Esc%2FAWNYuNNsNtV6ZlT7dnOk7JT6qSjZyZPHS7hjb9y5jM7f2KvrjigZDnRLDSLl5hl4UB3OQNU819eOH2emA3ZzyQ%2BaIgvYSXrKCfMR6N3HD7x5OpWJi2Fg4YcB03rmcrYYRE11RcTPRQ6QWjynySbVKwvGFEXAWP5imn7RRuhPabi3tEi35PTz0ckKZ4zhJaCP2v%2FfrtJTpfKnEfuIXpbF%2B7PQ8msI1k1i9bbDHEpoHVkGv2oyWCV7wkTbRBl3jD59LrLBjqkAWvRhl8lT7PRXodzoVuxxLbkZxyNTOEw8mIeJY%2B%2B4PkGumcAxU7U9tohd3RSsABDIdHMj8pvDUtOdrpgh1Pnk%2BCeogYKrl5Ugc9BfqfrICSLDZZYQfE2GGVaNw1tgThqoJZqVIiuWZRXcOCHq4YNURPuebxbDT9ma%2Bq5lEi%2BH053EQxXN6rKEIKbXvL2laoxQwj8FNaLa068AbepSBSkmsk%2FvqjP&X-Amz-Signature=bc01f51e02947eb47f070872cd749c986fa409622a42797aa10ccb9e7971e661&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAGJSEC%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2WkfW4%2Fa5GLZFkQWbXXBJfjs8lK5yFWA4QjOVmfZC3gIhANgaQXeHbQ%2FygSGnJ6L1K60gA%2Bwwr8VFvks0KZbrAcyIKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwregz0Bx1RmOsKJgYq3AMUCmzv8D5MlUCLay6fm%2FI5Wijy0vsr%2BJvicMw752eSlZUOsBbTFN2T3aJ%2BKCO219zbDbYw6q1v%2B5kXHAgMienpkxgvxsElVS854PoyzKDG2BvLRCThBCbek1WYHOBnZ7SZcoQ4OCl7jSZS2oCQtQ6sFrYgAWltX01HMq184C6yVenVslkqCel0xS3khSX%2F68hN%2Bukxu20yNlvEkSxZUYElnOnte5o80JJuR5xO54iuSC%2BISfvAKZruVIHcGyGXpiKv5Ayd%2BUsBlXKXHj7n8UiDgKRoFoFS67JtUTPuOoKt3G7pcLW0r9ViaPWo1TWo6aqmpOZy4uYcgDP7HTXhPzaIrWi9pP2TDii%2FTPy2sXL7Z1BU1%2FO2%2FehaLmwS4Esc%2FAWNYuNNsNtV6ZlT7dnOk7JT6qSjZyZPHS7hjb9y5jM7f2KvrjigZDnRLDSLl5hl4UB3OQNU819eOH2emA3ZzyQ%2BaIgvYSXrKCfMR6N3HD7x5OpWJi2Fg4YcB03rmcrYYRE11RcTPRQ6QWjynySbVKwvGFEXAWP5imn7RRuhPabi3tEi35PTz0ckKZ4zhJaCP2v%2FfrtJTpfKnEfuIXpbF%2B7PQ8msI1k1i9bbDHEpoHVkGv2oyWCV7wkTbRBl3jD59LrLBjqkAWvRhl8lT7PRXodzoVuxxLbkZxyNTOEw8mIeJY%2B%2B4PkGumcAxU7U9tohd3RSsABDIdHMj8pvDUtOdrpgh1Pnk%2BCeogYKrl5Ugc9BfqfrICSLDZZYQfE2GGVaNw1tgThqoJZqVIiuWZRXcOCHq4YNURPuebxbDT9ma%2Bq5lEi%2BH053EQxXN6rKEIKbXvL2laoxQwj8FNaLa068AbepSBSkmsk%2FvqjP&X-Amz-Signature=7c1bfa62d25996b3c88b15aadddc6d2572b1f57fc2bf095be851431ceda57a9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAGJSEC%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2WkfW4%2Fa5GLZFkQWbXXBJfjs8lK5yFWA4QjOVmfZC3gIhANgaQXeHbQ%2FygSGnJ6L1K60gA%2Bwwr8VFvks0KZbrAcyIKogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwregz0Bx1RmOsKJgYq3AMUCmzv8D5MlUCLay6fm%2FI5Wijy0vsr%2BJvicMw752eSlZUOsBbTFN2T3aJ%2BKCO219zbDbYw6q1v%2B5kXHAgMienpkxgvxsElVS854PoyzKDG2BvLRCThBCbek1WYHOBnZ7SZcoQ4OCl7jSZS2oCQtQ6sFrYgAWltX01HMq184C6yVenVslkqCel0xS3khSX%2F68hN%2Bukxu20yNlvEkSxZUYElnOnte5o80JJuR5xO54iuSC%2BISfvAKZruVIHcGyGXpiKv5Ayd%2BUsBlXKXHj7n8UiDgKRoFoFS67JtUTPuOoKt3G7pcLW0r9ViaPWo1TWo6aqmpOZy4uYcgDP7HTXhPzaIrWi9pP2TDii%2FTPy2sXL7Z1BU1%2FO2%2FehaLmwS4Esc%2FAWNYuNNsNtV6ZlT7dnOk7JT6qSjZyZPHS7hjb9y5jM7f2KvrjigZDnRLDSLl5hl4UB3OQNU819eOH2emA3ZzyQ%2BaIgvYSXrKCfMR6N3HD7x5OpWJi2Fg4YcB03rmcrYYRE11RcTPRQ6QWjynySbVKwvGFEXAWP5imn7RRuhPabi3tEi35PTz0ckKZ4zhJaCP2v%2FfrtJTpfKnEfuIXpbF%2B7PQ8msI1k1i9bbDHEpoHVkGv2oyWCV7wkTbRBl3jD59LrLBjqkAWvRhl8lT7PRXodzoVuxxLbkZxyNTOEw8mIeJY%2B%2B4PkGumcAxU7U9tohd3RSsABDIdHMj8pvDUtOdrpgh1Pnk%2BCeogYKrl5Ugc9BfqfrICSLDZZYQfE2GGVaNw1tgThqoJZqVIiuWZRXcOCHq4YNURPuebxbDT9ma%2Bq5lEi%2BH053EQxXN6rKEIKbXvL2laoxQwj8FNaLa068AbepSBSkmsk%2FvqjP&X-Amz-Signature=83367fb902a3d7963fccf5fdc90c3e29ad59aefaf32401a9adfa5c2a1c932d01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

