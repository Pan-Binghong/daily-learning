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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NKT4NHP%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCBevrUlgobFZ3a2OFdAgoxzIziGjDrFyyHsIHNU%2Ft35AIgW5WzRui4Gkqwu7jfmffD%2FBuYs%2BLi52gG%2FN1iDpeAXOMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNxGkH6ZoC%2BQ%2FYTFrCrcA6pBK%2FGnPHZM1YfTgxMjy44iuy8IVCLM57TzaqtbCdr2PfPS1SJt1Q4md4oBi1qAhCBhkxgrIy3n%2Fp7LhWrVIaXwfasL6ZBC1A9LvGLTjW6DSOfix%2F2cGzs36DHF9ZYCcfSM2a%2Fxgs8wyIeSYKP1mpvEfwF886NScKxwRWCMlGqHcYuFqWp1NuUKuvqqF68l8x9CZoXyTxwBe%2FuNB5SGeIEl78XYAi6KNIgjl82YhIw%2BNX%2Fd9fJ4EGDp8%2FVJtgGQoUIKYeTS8WA%2ByFe6wzpvN94zY7V4E7a%2BnopnzU5%2F16ZobcaDw0NFixc9y0njoi73DFywA2K0XyuNP5Tssi0qB1BBTYtQogXSmLaTDi2dosvuGnV1Mer0iBX45VRX7sYvVXnZAb06MrvXG6cdJ3jV%2FeUgHBfrgyDm5MJIxPkpY9Uf6d5efwX3as8jO5LFg9KP72xdN7kR6YJdzmjdroKihTdHOs%2BdcdJU35Aazow6BTfaSlMvskj7tp2vR%2FtxwVWFT70AXa7tXaMRRP9ldZ8Gj1Y7mbcYG5W%2FxMWhmy6VG%2FItZaZejl6mrek3GY5I30bl2ymnQhfoozOrrroim%2Fhg7Xg8Rh5fjZ985T1eEF6VtTby%2F%2Ff9QAFo9a2aMZn%2FMJDJp84GOqUBUkMKB6AAOQWmKc%2Fjqz2mpOTDSyz16H8o0YjBqj7JacCmrrVu%2FanKPF2GjkpKf2J5kyeVv8xR%2BujHHYKtHotMXKtSuvA2fw5mKPGXrRQ0NkOrsbM%2FS53Oc49ppEcmAFwS2GXrgvSmb2SKgjdcVgpqHo44rPV4oIvDD5%2FYiI2tzz85jxaAWuLGAYwfMzamqdBfm2DOIRWcpVP4NrBPUdxAEA1Ov2Zt&X-Amz-Signature=14be7cfbe19466e97207da18d494991e814f21f788d5476eb754f3a478037bf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NKT4NHP%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCBevrUlgobFZ3a2OFdAgoxzIziGjDrFyyHsIHNU%2Ft35AIgW5WzRui4Gkqwu7jfmffD%2FBuYs%2BLi52gG%2FN1iDpeAXOMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNxGkH6ZoC%2BQ%2FYTFrCrcA6pBK%2FGnPHZM1YfTgxMjy44iuy8IVCLM57TzaqtbCdr2PfPS1SJt1Q4md4oBi1qAhCBhkxgrIy3n%2Fp7LhWrVIaXwfasL6ZBC1A9LvGLTjW6DSOfix%2F2cGzs36DHF9ZYCcfSM2a%2Fxgs8wyIeSYKP1mpvEfwF886NScKxwRWCMlGqHcYuFqWp1NuUKuvqqF68l8x9CZoXyTxwBe%2FuNB5SGeIEl78XYAi6KNIgjl82YhIw%2BNX%2Fd9fJ4EGDp8%2FVJtgGQoUIKYeTS8WA%2ByFe6wzpvN94zY7V4E7a%2BnopnzU5%2F16ZobcaDw0NFixc9y0njoi73DFywA2K0XyuNP5Tssi0qB1BBTYtQogXSmLaTDi2dosvuGnV1Mer0iBX45VRX7sYvVXnZAb06MrvXG6cdJ3jV%2FeUgHBfrgyDm5MJIxPkpY9Uf6d5efwX3as8jO5LFg9KP72xdN7kR6YJdzmjdroKihTdHOs%2BdcdJU35Aazow6BTfaSlMvskj7tp2vR%2FtxwVWFT70AXa7tXaMRRP9ldZ8Gj1Y7mbcYG5W%2FxMWhmy6VG%2FItZaZejl6mrek3GY5I30bl2ymnQhfoozOrrroim%2Fhg7Xg8Rh5fjZ985T1eEF6VtTby%2F%2Ff9QAFo9a2aMZn%2FMJDJp84GOqUBUkMKB6AAOQWmKc%2Fjqz2mpOTDSyz16H8o0YjBqj7JacCmrrVu%2FanKPF2GjkpKf2J5kyeVv8xR%2BujHHYKtHotMXKtSuvA2fw5mKPGXrRQ0NkOrsbM%2FS53Oc49ppEcmAFwS2GXrgvSmb2SKgjdcVgpqHo44rPV4oIvDD5%2FYiI2tzz85jxaAWuLGAYwfMzamqdBfm2DOIRWcpVP4NrBPUdxAEA1Ov2Zt&X-Amz-Signature=45c3c1c499eb511dddd6592b37a7fb5715e4d2e10e97032f2007b4038f741de6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NKT4NHP%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCBevrUlgobFZ3a2OFdAgoxzIziGjDrFyyHsIHNU%2Ft35AIgW5WzRui4Gkqwu7jfmffD%2FBuYs%2BLi52gG%2FN1iDpeAXOMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNxGkH6ZoC%2BQ%2FYTFrCrcA6pBK%2FGnPHZM1YfTgxMjy44iuy8IVCLM57TzaqtbCdr2PfPS1SJt1Q4md4oBi1qAhCBhkxgrIy3n%2Fp7LhWrVIaXwfasL6ZBC1A9LvGLTjW6DSOfix%2F2cGzs36DHF9ZYCcfSM2a%2Fxgs8wyIeSYKP1mpvEfwF886NScKxwRWCMlGqHcYuFqWp1NuUKuvqqF68l8x9CZoXyTxwBe%2FuNB5SGeIEl78XYAi6KNIgjl82YhIw%2BNX%2Fd9fJ4EGDp8%2FVJtgGQoUIKYeTS8WA%2ByFe6wzpvN94zY7V4E7a%2BnopnzU5%2F16ZobcaDw0NFixc9y0njoi73DFywA2K0XyuNP5Tssi0qB1BBTYtQogXSmLaTDi2dosvuGnV1Mer0iBX45VRX7sYvVXnZAb06MrvXG6cdJ3jV%2FeUgHBfrgyDm5MJIxPkpY9Uf6d5efwX3as8jO5LFg9KP72xdN7kR6YJdzmjdroKihTdHOs%2BdcdJU35Aazow6BTfaSlMvskj7tp2vR%2FtxwVWFT70AXa7tXaMRRP9ldZ8Gj1Y7mbcYG5W%2FxMWhmy6VG%2FItZaZejl6mrek3GY5I30bl2ymnQhfoozOrrroim%2Fhg7Xg8Rh5fjZ985T1eEF6VtTby%2F%2Ff9QAFo9a2aMZn%2FMJDJp84GOqUBUkMKB6AAOQWmKc%2Fjqz2mpOTDSyz16H8o0YjBqj7JacCmrrVu%2FanKPF2GjkpKf2J5kyeVv8xR%2BujHHYKtHotMXKtSuvA2fw5mKPGXrRQ0NkOrsbM%2FS53Oc49ppEcmAFwS2GXrgvSmb2SKgjdcVgpqHo44rPV4oIvDD5%2FYiI2tzz85jxaAWuLGAYwfMzamqdBfm2DOIRWcpVP4NrBPUdxAEA1Ov2Zt&X-Amz-Signature=7ed7730fcefdcd08a4a3109527534c92ee299c1f2a9414c1eb207815646d6b8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NKT4NHP%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCBevrUlgobFZ3a2OFdAgoxzIziGjDrFyyHsIHNU%2Ft35AIgW5WzRui4Gkqwu7jfmffD%2FBuYs%2BLi52gG%2FN1iDpeAXOMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNxGkH6ZoC%2BQ%2FYTFrCrcA6pBK%2FGnPHZM1YfTgxMjy44iuy8IVCLM57TzaqtbCdr2PfPS1SJt1Q4md4oBi1qAhCBhkxgrIy3n%2Fp7LhWrVIaXwfasL6ZBC1A9LvGLTjW6DSOfix%2F2cGzs36DHF9ZYCcfSM2a%2Fxgs8wyIeSYKP1mpvEfwF886NScKxwRWCMlGqHcYuFqWp1NuUKuvqqF68l8x9CZoXyTxwBe%2FuNB5SGeIEl78XYAi6KNIgjl82YhIw%2BNX%2Fd9fJ4EGDp8%2FVJtgGQoUIKYeTS8WA%2ByFe6wzpvN94zY7V4E7a%2BnopnzU5%2F16ZobcaDw0NFixc9y0njoi73DFywA2K0XyuNP5Tssi0qB1BBTYtQogXSmLaTDi2dosvuGnV1Mer0iBX45VRX7sYvVXnZAb06MrvXG6cdJ3jV%2FeUgHBfrgyDm5MJIxPkpY9Uf6d5efwX3as8jO5LFg9KP72xdN7kR6YJdzmjdroKihTdHOs%2BdcdJU35Aazow6BTfaSlMvskj7tp2vR%2FtxwVWFT70AXa7tXaMRRP9ldZ8Gj1Y7mbcYG5W%2FxMWhmy6VG%2FItZaZejl6mrek3GY5I30bl2ymnQhfoozOrrroim%2Fhg7Xg8Rh5fjZ985T1eEF6VtTby%2F%2Ff9QAFo9a2aMZn%2FMJDJp84GOqUBUkMKB6AAOQWmKc%2Fjqz2mpOTDSyz16H8o0YjBqj7JacCmrrVu%2FanKPF2GjkpKf2J5kyeVv8xR%2BujHHYKtHotMXKtSuvA2fw5mKPGXrRQ0NkOrsbM%2FS53Oc49ppEcmAFwS2GXrgvSmb2SKgjdcVgpqHo44rPV4oIvDD5%2FYiI2tzz85jxaAWuLGAYwfMzamqdBfm2DOIRWcpVP4NrBPUdxAEA1Ov2Zt&X-Amz-Signature=08e344f0658b6fb05d2b9afa29465cfd3750d04aa24821e43d8f514b2ff0301f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NKT4NHP%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCBevrUlgobFZ3a2OFdAgoxzIziGjDrFyyHsIHNU%2Ft35AIgW5WzRui4Gkqwu7jfmffD%2FBuYs%2BLi52gG%2FN1iDpeAXOMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNxGkH6ZoC%2BQ%2FYTFrCrcA6pBK%2FGnPHZM1YfTgxMjy44iuy8IVCLM57TzaqtbCdr2PfPS1SJt1Q4md4oBi1qAhCBhkxgrIy3n%2Fp7LhWrVIaXwfasL6ZBC1A9LvGLTjW6DSOfix%2F2cGzs36DHF9ZYCcfSM2a%2Fxgs8wyIeSYKP1mpvEfwF886NScKxwRWCMlGqHcYuFqWp1NuUKuvqqF68l8x9CZoXyTxwBe%2FuNB5SGeIEl78XYAi6KNIgjl82YhIw%2BNX%2Fd9fJ4EGDp8%2FVJtgGQoUIKYeTS8WA%2ByFe6wzpvN94zY7V4E7a%2BnopnzU5%2F16ZobcaDw0NFixc9y0njoi73DFywA2K0XyuNP5Tssi0qB1BBTYtQogXSmLaTDi2dosvuGnV1Mer0iBX45VRX7sYvVXnZAb06MrvXG6cdJ3jV%2FeUgHBfrgyDm5MJIxPkpY9Uf6d5efwX3as8jO5LFg9KP72xdN7kR6YJdzmjdroKihTdHOs%2BdcdJU35Aazow6BTfaSlMvskj7tp2vR%2FtxwVWFT70AXa7tXaMRRP9ldZ8Gj1Y7mbcYG5W%2FxMWhmy6VG%2FItZaZejl6mrek3GY5I30bl2ymnQhfoozOrrroim%2Fhg7Xg8Rh5fjZ985T1eEF6VtTby%2F%2Ff9QAFo9a2aMZn%2FMJDJp84GOqUBUkMKB6AAOQWmKc%2Fjqz2mpOTDSyz16H8o0YjBqj7JacCmrrVu%2FanKPF2GjkpKf2J5kyeVv8xR%2BujHHYKtHotMXKtSuvA2fw5mKPGXrRQ0NkOrsbM%2FS53Oc49ppEcmAFwS2GXrgvSmb2SKgjdcVgpqHo44rPV4oIvDD5%2FYiI2tzz85jxaAWuLGAYwfMzamqdBfm2DOIRWcpVP4NrBPUdxAEA1Ov2Zt&X-Amz-Signature=75630d670b0383157b42ce0b180aa55c359c3f88c25b67e0095a133fb13b3c32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NKT4NHP%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCBevrUlgobFZ3a2OFdAgoxzIziGjDrFyyHsIHNU%2Ft35AIgW5WzRui4Gkqwu7jfmffD%2FBuYs%2BLi52gG%2FN1iDpeAXOMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNxGkH6ZoC%2BQ%2FYTFrCrcA6pBK%2FGnPHZM1YfTgxMjy44iuy8IVCLM57TzaqtbCdr2PfPS1SJt1Q4md4oBi1qAhCBhkxgrIy3n%2Fp7LhWrVIaXwfasL6ZBC1A9LvGLTjW6DSOfix%2F2cGzs36DHF9ZYCcfSM2a%2Fxgs8wyIeSYKP1mpvEfwF886NScKxwRWCMlGqHcYuFqWp1NuUKuvqqF68l8x9CZoXyTxwBe%2FuNB5SGeIEl78XYAi6KNIgjl82YhIw%2BNX%2Fd9fJ4EGDp8%2FVJtgGQoUIKYeTS8WA%2ByFe6wzpvN94zY7V4E7a%2BnopnzU5%2F16ZobcaDw0NFixc9y0njoi73DFywA2K0XyuNP5Tssi0qB1BBTYtQogXSmLaTDi2dosvuGnV1Mer0iBX45VRX7sYvVXnZAb06MrvXG6cdJ3jV%2FeUgHBfrgyDm5MJIxPkpY9Uf6d5efwX3as8jO5LFg9KP72xdN7kR6YJdzmjdroKihTdHOs%2BdcdJU35Aazow6BTfaSlMvskj7tp2vR%2FtxwVWFT70AXa7tXaMRRP9ldZ8Gj1Y7mbcYG5W%2FxMWhmy6VG%2FItZaZejl6mrek3GY5I30bl2ymnQhfoozOrrroim%2Fhg7Xg8Rh5fjZ985T1eEF6VtTby%2F%2Ff9QAFo9a2aMZn%2FMJDJp84GOqUBUkMKB6AAOQWmKc%2Fjqz2mpOTDSyz16H8o0YjBqj7JacCmrrVu%2FanKPF2GjkpKf2J5kyeVv8xR%2BujHHYKtHotMXKtSuvA2fw5mKPGXrRQ0NkOrsbM%2FS53Oc49ppEcmAFwS2GXrgvSmb2SKgjdcVgpqHo44rPV4oIvDD5%2FYiI2tzz85jxaAWuLGAYwfMzamqdBfm2DOIRWcpVP4NrBPUdxAEA1Ov2Zt&X-Amz-Signature=90e3d4e3827fc9221ffd906e5f7287183f46e524685c54952e2f57585be497da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NKT4NHP%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCBevrUlgobFZ3a2OFdAgoxzIziGjDrFyyHsIHNU%2Ft35AIgW5WzRui4Gkqwu7jfmffD%2FBuYs%2BLi52gG%2FN1iDpeAXOMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNxGkH6ZoC%2BQ%2FYTFrCrcA6pBK%2FGnPHZM1YfTgxMjy44iuy8IVCLM57TzaqtbCdr2PfPS1SJt1Q4md4oBi1qAhCBhkxgrIy3n%2Fp7LhWrVIaXwfasL6ZBC1A9LvGLTjW6DSOfix%2F2cGzs36DHF9ZYCcfSM2a%2Fxgs8wyIeSYKP1mpvEfwF886NScKxwRWCMlGqHcYuFqWp1NuUKuvqqF68l8x9CZoXyTxwBe%2FuNB5SGeIEl78XYAi6KNIgjl82YhIw%2BNX%2Fd9fJ4EGDp8%2FVJtgGQoUIKYeTS8WA%2ByFe6wzpvN94zY7V4E7a%2BnopnzU5%2F16ZobcaDw0NFixc9y0njoi73DFywA2K0XyuNP5Tssi0qB1BBTYtQogXSmLaTDi2dosvuGnV1Mer0iBX45VRX7sYvVXnZAb06MrvXG6cdJ3jV%2FeUgHBfrgyDm5MJIxPkpY9Uf6d5efwX3as8jO5LFg9KP72xdN7kR6YJdzmjdroKihTdHOs%2BdcdJU35Aazow6BTfaSlMvskj7tp2vR%2FtxwVWFT70AXa7tXaMRRP9ldZ8Gj1Y7mbcYG5W%2FxMWhmy6VG%2FItZaZejl6mrek3GY5I30bl2ymnQhfoozOrrroim%2Fhg7Xg8Rh5fjZ985T1eEF6VtTby%2F%2Ff9QAFo9a2aMZn%2FMJDJp84GOqUBUkMKB6AAOQWmKc%2Fjqz2mpOTDSyz16H8o0YjBqj7JacCmrrVu%2FanKPF2GjkpKf2J5kyeVv8xR%2BujHHYKtHotMXKtSuvA2fw5mKPGXrRQ0NkOrsbM%2FS53Oc49ppEcmAFwS2GXrgvSmb2SKgjdcVgpqHo44rPV4oIvDD5%2FYiI2tzz85jxaAWuLGAYwfMzamqdBfm2DOIRWcpVP4NrBPUdxAEA1Ov2Zt&X-Amz-Signature=67371cbf712119b4c7ce70f4d5291a398c4e8ab8d2ad66322fdda9fb4fbbbbaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NKT4NHP%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCBevrUlgobFZ3a2OFdAgoxzIziGjDrFyyHsIHNU%2Ft35AIgW5WzRui4Gkqwu7jfmffD%2FBuYs%2BLi52gG%2FN1iDpeAXOMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNxGkH6ZoC%2BQ%2FYTFrCrcA6pBK%2FGnPHZM1YfTgxMjy44iuy8IVCLM57TzaqtbCdr2PfPS1SJt1Q4md4oBi1qAhCBhkxgrIy3n%2Fp7LhWrVIaXwfasL6ZBC1A9LvGLTjW6DSOfix%2F2cGzs36DHF9ZYCcfSM2a%2Fxgs8wyIeSYKP1mpvEfwF886NScKxwRWCMlGqHcYuFqWp1NuUKuvqqF68l8x9CZoXyTxwBe%2FuNB5SGeIEl78XYAi6KNIgjl82YhIw%2BNX%2Fd9fJ4EGDp8%2FVJtgGQoUIKYeTS8WA%2ByFe6wzpvN94zY7V4E7a%2BnopnzU5%2F16ZobcaDw0NFixc9y0njoi73DFywA2K0XyuNP5Tssi0qB1BBTYtQogXSmLaTDi2dosvuGnV1Mer0iBX45VRX7sYvVXnZAb06MrvXG6cdJ3jV%2FeUgHBfrgyDm5MJIxPkpY9Uf6d5efwX3as8jO5LFg9KP72xdN7kR6YJdzmjdroKihTdHOs%2BdcdJU35Aazow6BTfaSlMvskj7tp2vR%2FtxwVWFT70AXa7tXaMRRP9ldZ8Gj1Y7mbcYG5W%2FxMWhmy6VG%2FItZaZejl6mrek3GY5I30bl2ymnQhfoozOrrroim%2Fhg7Xg8Rh5fjZ985T1eEF6VtTby%2F%2Ff9QAFo9a2aMZn%2FMJDJp84GOqUBUkMKB6AAOQWmKc%2Fjqz2mpOTDSyz16H8o0YjBqj7JacCmrrVu%2FanKPF2GjkpKf2J5kyeVv8xR%2BujHHYKtHotMXKtSuvA2fw5mKPGXrRQ0NkOrsbM%2FS53Oc49ppEcmAFwS2GXrgvSmb2SKgjdcVgpqHo44rPV4oIvDD5%2FYiI2tzz85jxaAWuLGAYwfMzamqdBfm2DOIRWcpVP4NrBPUdxAEA1Ov2Zt&X-Amz-Signature=3d2a164191a27a244e9234f4a050b770007fac43cbd2bbf9f37e1a6d17433829&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NKT4NHP%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCBevrUlgobFZ3a2OFdAgoxzIziGjDrFyyHsIHNU%2Ft35AIgW5WzRui4Gkqwu7jfmffD%2FBuYs%2BLi52gG%2FN1iDpeAXOMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNxGkH6ZoC%2BQ%2FYTFrCrcA6pBK%2FGnPHZM1YfTgxMjy44iuy8IVCLM57TzaqtbCdr2PfPS1SJt1Q4md4oBi1qAhCBhkxgrIy3n%2Fp7LhWrVIaXwfasL6ZBC1A9LvGLTjW6DSOfix%2F2cGzs36DHF9ZYCcfSM2a%2Fxgs8wyIeSYKP1mpvEfwF886NScKxwRWCMlGqHcYuFqWp1NuUKuvqqF68l8x9CZoXyTxwBe%2FuNB5SGeIEl78XYAi6KNIgjl82YhIw%2BNX%2Fd9fJ4EGDp8%2FVJtgGQoUIKYeTS8WA%2ByFe6wzpvN94zY7V4E7a%2BnopnzU5%2F16ZobcaDw0NFixc9y0njoi73DFywA2K0XyuNP5Tssi0qB1BBTYtQogXSmLaTDi2dosvuGnV1Mer0iBX45VRX7sYvVXnZAb06MrvXG6cdJ3jV%2FeUgHBfrgyDm5MJIxPkpY9Uf6d5efwX3as8jO5LFg9KP72xdN7kR6YJdzmjdroKihTdHOs%2BdcdJU35Aazow6BTfaSlMvskj7tp2vR%2FtxwVWFT70AXa7tXaMRRP9ldZ8Gj1Y7mbcYG5W%2FxMWhmy6VG%2FItZaZejl6mrek3GY5I30bl2ymnQhfoozOrrroim%2Fhg7Xg8Rh5fjZ985T1eEF6VtTby%2F%2Ff9QAFo9a2aMZn%2FMJDJp84GOqUBUkMKB6AAOQWmKc%2Fjqz2mpOTDSyz16H8o0YjBqj7JacCmrrVu%2FanKPF2GjkpKf2J5kyeVv8xR%2BujHHYKtHotMXKtSuvA2fw5mKPGXrRQ0NkOrsbM%2FS53Oc49ppEcmAFwS2GXrgvSmb2SKgjdcVgpqHo44rPV4oIvDD5%2FYiI2tzz85jxaAWuLGAYwfMzamqdBfm2DOIRWcpVP4NrBPUdxAEA1Ov2Zt&X-Amz-Signature=7d8d2bac7f9033d8006ded848340c5e0e22c084d722296b5cd7b365cb1ca3846&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NKT4NHP%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCBevrUlgobFZ3a2OFdAgoxzIziGjDrFyyHsIHNU%2Ft35AIgW5WzRui4Gkqwu7jfmffD%2FBuYs%2BLi52gG%2FN1iDpeAXOMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDNxGkH6ZoC%2BQ%2FYTFrCrcA6pBK%2FGnPHZM1YfTgxMjy44iuy8IVCLM57TzaqtbCdr2PfPS1SJt1Q4md4oBi1qAhCBhkxgrIy3n%2Fp7LhWrVIaXwfasL6ZBC1A9LvGLTjW6DSOfix%2F2cGzs36DHF9ZYCcfSM2a%2Fxgs8wyIeSYKP1mpvEfwF886NScKxwRWCMlGqHcYuFqWp1NuUKuvqqF68l8x9CZoXyTxwBe%2FuNB5SGeIEl78XYAi6KNIgjl82YhIw%2BNX%2Fd9fJ4EGDp8%2FVJtgGQoUIKYeTS8WA%2ByFe6wzpvN94zY7V4E7a%2BnopnzU5%2F16ZobcaDw0NFixc9y0njoi73DFywA2K0XyuNP5Tssi0qB1BBTYtQogXSmLaTDi2dosvuGnV1Mer0iBX45VRX7sYvVXnZAb06MrvXG6cdJ3jV%2FeUgHBfrgyDm5MJIxPkpY9Uf6d5efwX3as8jO5LFg9KP72xdN7kR6YJdzmjdroKihTdHOs%2BdcdJU35Aazow6BTfaSlMvskj7tp2vR%2FtxwVWFT70AXa7tXaMRRP9ldZ8Gj1Y7mbcYG5W%2FxMWhmy6VG%2FItZaZejl6mrek3GY5I30bl2ymnQhfoozOrrroim%2Fhg7Xg8Rh5fjZ985T1eEF6VtTby%2F%2Ff9QAFo9a2aMZn%2FMJDJp84GOqUBUkMKB6AAOQWmKc%2Fjqz2mpOTDSyz16H8o0YjBqj7JacCmrrVu%2FanKPF2GjkpKf2J5kyeVv8xR%2BujHHYKtHotMXKtSuvA2fw5mKPGXrRQ0NkOrsbM%2FS53Oc49ppEcmAFwS2GXrgvSmb2SKgjdcVgpqHo44rPV4oIvDD5%2FYiI2tzz85jxaAWuLGAYwfMzamqdBfm2DOIRWcpVP4NrBPUdxAEA1Ov2Zt&X-Amz-Signature=29f1e0c713940668d3c32eb7b9edfa667f17500f1d29ced65f7ee9e2bce90b5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

