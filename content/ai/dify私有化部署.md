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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2W2KHQ%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkxcWdlAZkqt5%2F5CF%2F0tWQrp8JNuFh%2Bfiqlqis5mcwkAiEAl0HIK1oWjIkZs8rT%2BNGEq3dzlfqrTs9EX7gK%2FiPN2%2FMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdO7RgOxkh5zmPRAyrcA2xxvLwC9pkveonDqEWooCJ3LXO1qsAWlfN1wy3%2BeSrh4dAyurd%2FS1F%2B7lsZAukvGJmmIaizSQjFAcgiRvfYXT02FHyLZSkXf35n%2B3ykxMrQQHvuSrFYeS8sfBasOC839wMBRpQb%2FFLh2IrH6IL52QUMAoL75mBAovUFLjr5iEtJTcetyUPPxIOP5e%2BBjXj%2F8TvBGo%2Fz%2BOTFPpAWyNe7EBXjd5oQk7U9cGQMZoN6vwMmZsBmu4QJK5b4hDPpqS%2B%2BgUd%2BSQebak6eYT21YmWJJpeTulj3BTM8ReOUqm6Nv%2FUy3sruQTbWPjyn2Z%2FujYW3FsGNN5F1QHJUPYp88twawXH6AKSumu%2FKg7fYXqqt3U4kO%2FVCtaGoJTukmMgjIYqyRDuF5GCrECugl5MGcCc%2BWI1TWF%2FF8XXeHAFYSF4ql0ao%2FjikJ9ZCU2zo29aNdXvsNiv9IFVDijzNc2fd2QKPPwZMXfVvbh7JLb0RluWFiyRYxNZ2jVtm%2BKmWNcOtE%2BIkbo%2FnBhmNtzCBa7aS1NMuVhi6bsKteNxupJa9MA%2BV9jESzr4UTsboNUiD0fipsfMquyTNjClnRrZT0ljBOh1Rjtgu8sF8j7H7EyNhXdIFv%2FDTR3XZcN%2F0x9IrUrgoMJGVns0GOqUBDvvyKxsx2f8QB2ezTxuAr95ooHblnsPJ4CypQbExVVZeB71HaBcsLudYvFH8vHTy97k8r6dgiRi0kx6wwBJAaav1VdLgfatoQR2445LIYPpjHuRvh%2BXljje7%2F7Uj0%2BcVi7C9IxgLsd3ndZIXtzYA1%2FPN6bt441HBpd6lqJIRdW9FaLs4%2Fglis%2FVVoWbfso%2BMeH73G%2FbIFfL8xzi%2Fj52gz0oqCXKg&X-Amz-Signature=8d1f25fbe6d864b1d51aa7530a6204369cde8316adf54ad8d7f13ab2a8fea860&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2W2KHQ%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkxcWdlAZkqt5%2F5CF%2F0tWQrp8JNuFh%2Bfiqlqis5mcwkAiEAl0HIK1oWjIkZs8rT%2BNGEq3dzlfqrTs9EX7gK%2FiPN2%2FMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdO7RgOxkh5zmPRAyrcA2xxvLwC9pkveonDqEWooCJ3LXO1qsAWlfN1wy3%2BeSrh4dAyurd%2FS1F%2B7lsZAukvGJmmIaizSQjFAcgiRvfYXT02FHyLZSkXf35n%2B3ykxMrQQHvuSrFYeS8sfBasOC839wMBRpQb%2FFLh2IrH6IL52QUMAoL75mBAovUFLjr5iEtJTcetyUPPxIOP5e%2BBjXj%2F8TvBGo%2Fz%2BOTFPpAWyNe7EBXjd5oQk7U9cGQMZoN6vwMmZsBmu4QJK5b4hDPpqS%2B%2BgUd%2BSQebak6eYT21YmWJJpeTulj3BTM8ReOUqm6Nv%2FUy3sruQTbWPjyn2Z%2FujYW3FsGNN5F1QHJUPYp88twawXH6AKSumu%2FKg7fYXqqt3U4kO%2FVCtaGoJTukmMgjIYqyRDuF5GCrECugl5MGcCc%2BWI1TWF%2FF8XXeHAFYSF4ql0ao%2FjikJ9ZCU2zo29aNdXvsNiv9IFVDijzNc2fd2QKPPwZMXfVvbh7JLb0RluWFiyRYxNZ2jVtm%2BKmWNcOtE%2BIkbo%2FnBhmNtzCBa7aS1NMuVhi6bsKteNxupJa9MA%2BV9jESzr4UTsboNUiD0fipsfMquyTNjClnRrZT0ljBOh1Rjtgu8sF8j7H7EyNhXdIFv%2FDTR3XZcN%2F0x9IrUrgoMJGVns0GOqUBDvvyKxsx2f8QB2ezTxuAr95ooHblnsPJ4CypQbExVVZeB71HaBcsLudYvFH8vHTy97k8r6dgiRi0kx6wwBJAaav1VdLgfatoQR2445LIYPpjHuRvh%2BXljje7%2F7Uj0%2BcVi7C9IxgLsd3ndZIXtzYA1%2FPN6bt441HBpd6lqJIRdW9FaLs4%2Fglis%2FVVoWbfso%2BMeH73G%2FbIFfL8xzi%2Fj52gz0oqCXKg&X-Amz-Signature=16433a2b08ccd225b6ee5406079fd7ccb91065a168481beee2d8775c032fb622&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2W2KHQ%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkxcWdlAZkqt5%2F5CF%2F0tWQrp8JNuFh%2Bfiqlqis5mcwkAiEAl0HIK1oWjIkZs8rT%2BNGEq3dzlfqrTs9EX7gK%2FiPN2%2FMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdO7RgOxkh5zmPRAyrcA2xxvLwC9pkveonDqEWooCJ3LXO1qsAWlfN1wy3%2BeSrh4dAyurd%2FS1F%2B7lsZAukvGJmmIaizSQjFAcgiRvfYXT02FHyLZSkXf35n%2B3ykxMrQQHvuSrFYeS8sfBasOC839wMBRpQb%2FFLh2IrH6IL52QUMAoL75mBAovUFLjr5iEtJTcetyUPPxIOP5e%2BBjXj%2F8TvBGo%2Fz%2BOTFPpAWyNe7EBXjd5oQk7U9cGQMZoN6vwMmZsBmu4QJK5b4hDPpqS%2B%2BgUd%2BSQebak6eYT21YmWJJpeTulj3BTM8ReOUqm6Nv%2FUy3sruQTbWPjyn2Z%2FujYW3FsGNN5F1QHJUPYp88twawXH6AKSumu%2FKg7fYXqqt3U4kO%2FVCtaGoJTukmMgjIYqyRDuF5GCrECugl5MGcCc%2BWI1TWF%2FF8XXeHAFYSF4ql0ao%2FjikJ9ZCU2zo29aNdXvsNiv9IFVDijzNc2fd2QKPPwZMXfVvbh7JLb0RluWFiyRYxNZ2jVtm%2BKmWNcOtE%2BIkbo%2FnBhmNtzCBa7aS1NMuVhi6bsKteNxupJa9MA%2BV9jESzr4UTsboNUiD0fipsfMquyTNjClnRrZT0ljBOh1Rjtgu8sF8j7H7EyNhXdIFv%2FDTR3XZcN%2F0x9IrUrgoMJGVns0GOqUBDvvyKxsx2f8QB2ezTxuAr95ooHblnsPJ4CypQbExVVZeB71HaBcsLudYvFH8vHTy97k8r6dgiRi0kx6wwBJAaav1VdLgfatoQR2445LIYPpjHuRvh%2BXljje7%2F7Uj0%2BcVi7C9IxgLsd3ndZIXtzYA1%2FPN6bt441HBpd6lqJIRdW9FaLs4%2Fglis%2FVVoWbfso%2BMeH73G%2FbIFfL8xzi%2Fj52gz0oqCXKg&X-Amz-Signature=94d3de3991dad81e007daeee5ebe2167be3ca414c66759dbd8a6cd2456797233&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2W2KHQ%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkxcWdlAZkqt5%2F5CF%2F0tWQrp8JNuFh%2Bfiqlqis5mcwkAiEAl0HIK1oWjIkZs8rT%2BNGEq3dzlfqrTs9EX7gK%2FiPN2%2FMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdO7RgOxkh5zmPRAyrcA2xxvLwC9pkveonDqEWooCJ3LXO1qsAWlfN1wy3%2BeSrh4dAyurd%2FS1F%2B7lsZAukvGJmmIaizSQjFAcgiRvfYXT02FHyLZSkXf35n%2B3ykxMrQQHvuSrFYeS8sfBasOC839wMBRpQb%2FFLh2IrH6IL52QUMAoL75mBAovUFLjr5iEtJTcetyUPPxIOP5e%2BBjXj%2F8TvBGo%2Fz%2BOTFPpAWyNe7EBXjd5oQk7U9cGQMZoN6vwMmZsBmu4QJK5b4hDPpqS%2B%2BgUd%2BSQebak6eYT21YmWJJpeTulj3BTM8ReOUqm6Nv%2FUy3sruQTbWPjyn2Z%2FujYW3FsGNN5F1QHJUPYp88twawXH6AKSumu%2FKg7fYXqqt3U4kO%2FVCtaGoJTukmMgjIYqyRDuF5GCrECugl5MGcCc%2BWI1TWF%2FF8XXeHAFYSF4ql0ao%2FjikJ9ZCU2zo29aNdXvsNiv9IFVDijzNc2fd2QKPPwZMXfVvbh7JLb0RluWFiyRYxNZ2jVtm%2BKmWNcOtE%2BIkbo%2FnBhmNtzCBa7aS1NMuVhi6bsKteNxupJa9MA%2BV9jESzr4UTsboNUiD0fipsfMquyTNjClnRrZT0ljBOh1Rjtgu8sF8j7H7EyNhXdIFv%2FDTR3XZcN%2F0x9IrUrgoMJGVns0GOqUBDvvyKxsx2f8QB2ezTxuAr95ooHblnsPJ4CypQbExVVZeB71HaBcsLudYvFH8vHTy97k8r6dgiRi0kx6wwBJAaav1VdLgfatoQR2445LIYPpjHuRvh%2BXljje7%2F7Uj0%2BcVi7C9IxgLsd3ndZIXtzYA1%2FPN6bt441HBpd6lqJIRdW9FaLs4%2Fglis%2FVVoWbfso%2BMeH73G%2FbIFfL8xzi%2Fj52gz0oqCXKg&X-Amz-Signature=2fc86ad35bc4fd0aaeb30d373c37cc8121bc40a8843f6545aae8f05f2431ac8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2W2KHQ%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkxcWdlAZkqt5%2F5CF%2F0tWQrp8JNuFh%2Bfiqlqis5mcwkAiEAl0HIK1oWjIkZs8rT%2BNGEq3dzlfqrTs9EX7gK%2FiPN2%2FMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdO7RgOxkh5zmPRAyrcA2xxvLwC9pkveonDqEWooCJ3LXO1qsAWlfN1wy3%2BeSrh4dAyurd%2FS1F%2B7lsZAukvGJmmIaizSQjFAcgiRvfYXT02FHyLZSkXf35n%2B3ykxMrQQHvuSrFYeS8sfBasOC839wMBRpQb%2FFLh2IrH6IL52QUMAoL75mBAovUFLjr5iEtJTcetyUPPxIOP5e%2BBjXj%2F8TvBGo%2Fz%2BOTFPpAWyNe7EBXjd5oQk7U9cGQMZoN6vwMmZsBmu4QJK5b4hDPpqS%2B%2BgUd%2BSQebak6eYT21YmWJJpeTulj3BTM8ReOUqm6Nv%2FUy3sruQTbWPjyn2Z%2FujYW3FsGNN5F1QHJUPYp88twawXH6AKSumu%2FKg7fYXqqt3U4kO%2FVCtaGoJTukmMgjIYqyRDuF5GCrECugl5MGcCc%2BWI1TWF%2FF8XXeHAFYSF4ql0ao%2FjikJ9ZCU2zo29aNdXvsNiv9IFVDijzNc2fd2QKPPwZMXfVvbh7JLb0RluWFiyRYxNZ2jVtm%2BKmWNcOtE%2BIkbo%2FnBhmNtzCBa7aS1NMuVhi6bsKteNxupJa9MA%2BV9jESzr4UTsboNUiD0fipsfMquyTNjClnRrZT0ljBOh1Rjtgu8sF8j7H7EyNhXdIFv%2FDTR3XZcN%2F0x9IrUrgoMJGVns0GOqUBDvvyKxsx2f8QB2ezTxuAr95ooHblnsPJ4CypQbExVVZeB71HaBcsLudYvFH8vHTy97k8r6dgiRi0kx6wwBJAaav1VdLgfatoQR2445LIYPpjHuRvh%2BXljje7%2F7Uj0%2BcVi7C9IxgLsd3ndZIXtzYA1%2FPN6bt441HBpd6lqJIRdW9FaLs4%2Fglis%2FVVoWbfso%2BMeH73G%2FbIFfL8xzi%2Fj52gz0oqCXKg&X-Amz-Signature=6b34fb7ed1f814f416bcf79c17acfabb6d5f89c8dde47c6d96b6400b920d0f3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2W2KHQ%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkxcWdlAZkqt5%2F5CF%2F0tWQrp8JNuFh%2Bfiqlqis5mcwkAiEAl0HIK1oWjIkZs8rT%2BNGEq3dzlfqrTs9EX7gK%2FiPN2%2FMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdO7RgOxkh5zmPRAyrcA2xxvLwC9pkveonDqEWooCJ3LXO1qsAWlfN1wy3%2BeSrh4dAyurd%2FS1F%2B7lsZAukvGJmmIaizSQjFAcgiRvfYXT02FHyLZSkXf35n%2B3ykxMrQQHvuSrFYeS8sfBasOC839wMBRpQb%2FFLh2IrH6IL52QUMAoL75mBAovUFLjr5iEtJTcetyUPPxIOP5e%2BBjXj%2F8TvBGo%2Fz%2BOTFPpAWyNe7EBXjd5oQk7U9cGQMZoN6vwMmZsBmu4QJK5b4hDPpqS%2B%2BgUd%2BSQebak6eYT21YmWJJpeTulj3BTM8ReOUqm6Nv%2FUy3sruQTbWPjyn2Z%2FujYW3FsGNN5F1QHJUPYp88twawXH6AKSumu%2FKg7fYXqqt3U4kO%2FVCtaGoJTukmMgjIYqyRDuF5GCrECugl5MGcCc%2BWI1TWF%2FF8XXeHAFYSF4ql0ao%2FjikJ9ZCU2zo29aNdXvsNiv9IFVDijzNc2fd2QKPPwZMXfVvbh7JLb0RluWFiyRYxNZ2jVtm%2BKmWNcOtE%2BIkbo%2FnBhmNtzCBa7aS1NMuVhi6bsKteNxupJa9MA%2BV9jESzr4UTsboNUiD0fipsfMquyTNjClnRrZT0ljBOh1Rjtgu8sF8j7H7EyNhXdIFv%2FDTR3XZcN%2F0x9IrUrgoMJGVns0GOqUBDvvyKxsx2f8QB2ezTxuAr95ooHblnsPJ4CypQbExVVZeB71HaBcsLudYvFH8vHTy97k8r6dgiRi0kx6wwBJAaav1VdLgfatoQR2445LIYPpjHuRvh%2BXljje7%2F7Uj0%2BcVi7C9IxgLsd3ndZIXtzYA1%2FPN6bt441HBpd6lqJIRdW9FaLs4%2Fglis%2FVVoWbfso%2BMeH73G%2FbIFfL8xzi%2Fj52gz0oqCXKg&X-Amz-Signature=6cac1cc2160f1812cb982294738503bcf7e2fafb389d01ee6a8ddf45eece45bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2W2KHQ%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkxcWdlAZkqt5%2F5CF%2F0tWQrp8JNuFh%2Bfiqlqis5mcwkAiEAl0HIK1oWjIkZs8rT%2BNGEq3dzlfqrTs9EX7gK%2FiPN2%2FMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdO7RgOxkh5zmPRAyrcA2xxvLwC9pkveonDqEWooCJ3LXO1qsAWlfN1wy3%2BeSrh4dAyurd%2FS1F%2B7lsZAukvGJmmIaizSQjFAcgiRvfYXT02FHyLZSkXf35n%2B3ykxMrQQHvuSrFYeS8sfBasOC839wMBRpQb%2FFLh2IrH6IL52QUMAoL75mBAovUFLjr5iEtJTcetyUPPxIOP5e%2BBjXj%2F8TvBGo%2Fz%2BOTFPpAWyNe7EBXjd5oQk7U9cGQMZoN6vwMmZsBmu4QJK5b4hDPpqS%2B%2BgUd%2BSQebak6eYT21YmWJJpeTulj3BTM8ReOUqm6Nv%2FUy3sruQTbWPjyn2Z%2FujYW3FsGNN5F1QHJUPYp88twawXH6AKSumu%2FKg7fYXqqt3U4kO%2FVCtaGoJTukmMgjIYqyRDuF5GCrECugl5MGcCc%2BWI1TWF%2FF8XXeHAFYSF4ql0ao%2FjikJ9ZCU2zo29aNdXvsNiv9IFVDijzNc2fd2QKPPwZMXfVvbh7JLb0RluWFiyRYxNZ2jVtm%2BKmWNcOtE%2BIkbo%2FnBhmNtzCBa7aS1NMuVhi6bsKteNxupJa9MA%2BV9jESzr4UTsboNUiD0fipsfMquyTNjClnRrZT0ljBOh1Rjtgu8sF8j7H7EyNhXdIFv%2FDTR3XZcN%2F0x9IrUrgoMJGVns0GOqUBDvvyKxsx2f8QB2ezTxuAr95ooHblnsPJ4CypQbExVVZeB71HaBcsLudYvFH8vHTy97k8r6dgiRi0kx6wwBJAaav1VdLgfatoQR2445LIYPpjHuRvh%2BXljje7%2F7Uj0%2BcVi7C9IxgLsd3ndZIXtzYA1%2FPN6bt441HBpd6lqJIRdW9FaLs4%2Fglis%2FVVoWbfso%2BMeH73G%2FbIFfL8xzi%2Fj52gz0oqCXKg&X-Amz-Signature=688ffa26f3f9e12f0848624816b7d79574be3dc29e7fca9e4d3452c559cd81e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2W2KHQ%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkxcWdlAZkqt5%2F5CF%2F0tWQrp8JNuFh%2Bfiqlqis5mcwkAiEAl0HIK1oWjIkZs8rT%2BNGEq3dzlfqrTs9EX7gK%2FiPN2%2FMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdO7RgOxkh5zmPRAyrcA2xxvLwC9pkveonDqEWooCJ3LXO1qsAWlfN1wy3%2BeSrh4dAyurd%2FS1F%2B7lsZAukvGJmmIaizSQjFAcgiRvfYXT02FHyLZSkXf35n%2B3ykxMrQQHvuSrFYeS8sfBasOC839wMBRpQb%2FFLh2IrH6IL52QUMAoL75mBAovUFLjr5iEtJTcetyUPPxIOP5e%2BBjXj%2F8TvBGo%2Fz%2BOTFPpAWyNe7EBXjd5oQk7U9cGQMZoN6vwMmZsBmu4QJK5b4hDPpqS%2B%2BgUd%2BSQebak6eYT21YmWJJpeTulj3BTM8ReOUqm6Nv%2FUy3sruQTbWPjyn2Z%2FujYW3FsGNN5F1QHJUPYp88twawXH6AKSumu%2FKg7fYXqqt3U4kO%2FVCtaGoJTukmMgjIYqyRDuF5GCrECugl5MGcCc%2BWI1TWF%2FF8XXeHAFYSF4ql0ao%2FjikJ9ZCU2zo29aNdXvsNiv9IFVDijzNc2fd2QKPPwZMXfVvbh7JLb0RluWFiyRYxNZ2jVtm%2BKmWNcOtE%2BIkbo%2FnBhmNtzCBa7aS1NMuVhi6bsKteNxupJa9MA%2BV9jESzr4UTsboNUiD0fipsfMquyTNjClnRrZT0ljBOh1Rjtgu8sF8j7H7EyNhXdIFv%2FDTR3XZcN%2F0x9IrUrgoMJGVns0GOqUBDvvyKxsx2f8QB2ezTxuAr95ooHblnsPJ4CypQbExVVZeB71HaBcsLudYvFH8vHTy97k8r6dgiRi0kx6wwBJAaav1VdLgfatoQR2445LIYPpjHuRvh%2BXljje7%2F7Uj0%2BcVi7C9IxgLsd3ndZIXtzYA1%2FPN6bt441HBpd6lqJIRdW9FaLs4%2Fglis%2FVVoWbfso%2BMeH73G%2FbIFfL8xzi%2Fj52gz0oqCXKg&X-Amz-Signature=3d15b634c245204b08c3bb5d3b3602f5ce19954ea7893519e0c0021b5b2e378f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2W2KHQ%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkxcWdlAZkqt5%2F5CF%2F0tWQrp8JNuFh%2Bfiqlqis5mcwkAiEAl0HIK1oWjIkZs8rT%2BNGEq3dzlfqrTs9EX7gK%2FiPN2%2FMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdO7RgOxkh5zmPRAyrcA2xxvLwC9pkveonDqEWooCJ3LXO1qsAWlfN1wy3%2BeSrh4dAyurd%2FS1F%2B7lsZAukvGJmmIaizSQjFAcgiRvfYXT02FHyLZSkXf35n%2B3ykxMrQQHvuSrFYeS8sfBasOC839wMBRpQb%2FFLh2IrH6IL52QUMAoL75mBAovUFLjr5iEtJTcetyUPPxIOP5e%2BBjXj%2F8TvBGo%2Fz%2BOTFPpAWyNe7EBXjd5oQk7U9cGQMZoN6vwMmZsBmu4QJK5b4hDPpqS%2B%2BgUd%2BSQebak6eYT21YmWJJpeTulj3BTM8ReOUqm6Nv%2FUy3sruQTbWPjyn2Z%2FujYW3FsGNN5F1QHJUPYp88twawXH6AKSumu%2FKg7fYXqqt3U4kO%2FVCtaGoJTukmMgjIYqyRDuF5GCrECugl5MGcCc%2BWI1TWF%2FF8XXeHAFYSF4ql0ao%2FjikJ9ZCU2zo29aNdXvsNiv9IFVDijzNc2fd2QKPPwZMXfVvbh7JLb0RluWFiyRYxNZ2jVtm%2BKmWNcOtE%2BIkbo%2FnBhmNtzCBa7aS1NMuVhi6bsKteNxupJa9MA%2BV9jESzr4UTsboNUiD0fipsfMquyTNjClnRrZT0ljBOh1Rjtgu8sF8j7H7EyNhXdIFv%2FDTR3XZcN%2F0x9IrUrgoMJGVns0GOqUBDvvyKxsx2f8QB2ezTxuAr95ooHblnsPJ4CypQbExVVZeB71HaBcsLudYvFH8vHTy97k8r6dgiRi0kx6wwBJAaav1VdLgfatoQR2445LIYPpjHuRvh%2BXljje7%2F7Uj0%2BcVi7C9IxgLsd3ndZIXtzYA1%2FPN6bt441HBpd6lqJIRdW9FaLs4%2Fglis%2FVVoWbfso%2BMeH73G%2FbIFfL8xzi%2Fj52gz0oqCXKg&X-Amz-Signature=0c3ef4ac0d5570372dbc8ee3bf16577ea413a8c1f0077493700f8e1667722194&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2W2KHQ%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkxcWdlAZkqt5%2F5CF%2F0tWQrp8JNuFh%2Bfiqlqis5mcwkAiEAl0HIK1oWjIkZs8rT%2BNGEq3dzlfqrTs9EX7gK%2FiPN2%2FMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCdO7RgOxkh5zmPRAyrcA2xxvLwC9pkveonDqEWooCJ3LXO1qsAWlfN1wy3%2BeSrh4dAyurd%2FS1F%2B7lsZAukvGJmmIaizSQjFAcgiRvfYXT02FHyLZSkXf35n%2B3ykxMrQQHvuSrFYeS8sfBasOC839wMBRpQb%2FFLh2IrH6IL52QUMAoL75mBAovUFLjr5iEtJTcetyUPPxIOP5e%2BBjXj%2F8TvBGo%2Fz%2BOTFPpAWyNe7EBXjd5oQk7U9cGQMZoN6vwMmZsBmu4QJK5b4hDPpqS%2B%2BgUd%2BSQebak6eYT21YmWJJpeTulj3BTM8ReOUqm6Nv%2FUy3sruQTbWPjyn2Z%2FujYW3FsGNN5F1QHJUPYp88twawXH6AKSumu%2FKg7fYXqqt3U4kO%2FVCtaGoJTukmMgjIYqyRDuF5GCrECugl5MGcCc%2BWI1TWF%2FF8XXeHAFYSF4ql0ao%2FjikJ9ZCU2zo29aNdXvsNiv9IFVDijzNc2fd2QKPPwZMXfVvbh7JLb0RluWFiyRYxNZ2jVtm%2BKmWNcOtE%2BIkbo%2FnBhmNtzCBa7aS1NMuVhi6bsKteNxupJa9MA%2BV9jESzr4UTsboNUiD0fipsfMquyTNjClnRrZT0ljBOh1Rjtgu8sF8j7H7EyNhXdIFv%2FDTR3XZcN%2F0x9IrUrgoMJGVns0GOqUBDvvyKxsx2f8QB2ezTxuAr95ooHblnsPJ4CypQbExVVZeB71HaBcsLudYvFH8vHTy97k8r6dgiRi0kx6wwBJAaav1VdLgfatoQR2445LIYPpjHuRvh%2BXljje7%2F7Uj0%2BcVi7C9IxgLsd3ndZIXtzYA1%2FPN6bt441HBpd6lqJIRdW9FaLs4%2Fglis%2FVVoWbfso%2BMeH73G%2FbIFfL8xzi%2Fj52gz0oqCXKg&X-Amz-Signature=18aaf566693737775835ad982f5f17ac380a97ee234f03c8383ead33c383976c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

