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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652VSTHU6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyB3%2F7Sldc4O6MRuE7qQc37aUFm0iQFFL304jZ7sKoTgIhAKTQChB0thebQ5HYTwAx4adrunnnHAMyeMRGfyfLBtr7Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxs%2Ftkt34q95%2B1qeS8q3AO7v%2BntMG4W2QhBa2y9JC%2B7w%2BYSy49PNiTck1D%2BiA9FLtVZEy%2BQwmlOE5HE9auff3dcYbo0yW6HqzBj%2FOD3Ks434kIJnOyykN%2Bf54NMPuscLgRYDXKr7q0DDAMhoANP69HddXThSoyvgLnhwLdMZBmR5CxpGrSB7zibN5%2B0oKPJLcx13oeQmvqIZVTtlxpte%2Bt1OCz%2Frp3OljayRbqagxtPPYB1UpiKzxChhYNUH999XLPOCnj75hJuTU16QS95ndLDnzuF5XavZ1Jq7FEMPxxmaDWij9PktbbwSTX%2FncYg6wI08ScTnjsg3imPFqZ%2B%2FHWKwWi19laVd0B%2FAibt7h4jLmrYT2chut6ck%2FsoQY65Vf0rbdo1daXiKWCwlnogRNF0UCMu1cO79tBvtQFm1zjeUDlN7TPGVvrbhkf4pMPowJH4R1cNSc5Qr0UfhFIkmZc2%2BtTXC9CGiwzRlmGtF8SY74sUtjfGimFu7HN2TYFWMe31ROy9l2TtfFWBbyaaVub%2BL6qTeaHfsyT%2F2qRumakWvEGUKqLhBWsLvTygv45a1hgnIcS1k5TNr5HQR%2BK6Ic9D8GjTQPJO6Hoc9XPuiieodV%2FvqX%2B8McBORG6fNflE%2FEGlHYdoRbIYHo2rcDDgrb3OBjqkAULmL3%2Fd3rpuRFvESAdoXts4MHkIA3Cjjplgyh8%2Bry4nAdz7vgFfhjA4tvILTJSyf5kGjegjtkCS850ZeVPcrRwWcgy6gmbU%2BsgrOa7O5Ew6vcq9yLhPeR73zbraq%2F5pP7i7URfxH13jvwOMwb6XKmatHw7ZUEthyEk6Q0z2l8ZkSLDoaXpPHYFsUou8XQpD%2BgX0J6jsz%2FhMYkD%2B8coeHLY15oEr&X-Amz-Signature=1d8f70a8c43cc6b79fe06f1a04f7b73a352ce4e74cb70778f1f1b4fa42ada340&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652VSTHU6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyB3%2F7Sldc4O6MRuE7qQc37aUFm0iQFFL304jZ7sKoTgIhAKTQChB0thebQ5HYTwAx4adrunnnHAMyeMRGfyfLBtr7Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxs%2Ftkt34q95%2B1qeS8q3AO7v%2BntMG4W2QhBa2y9JC%2B7w%2BYSy49PNiTck1D%2BiA9FLtVZEy%2BQwmlOE5HE9auff3dcYbo0yW6HqzBj%2FOD3Ks434kIJnOyykN%2Bf54NMPuscLgRYDXKr7q0DDAMhoANP69HddXThSoyvgLnhwLdMZBmR5CxpGrSB7zibN5%2B0oKPJLcx13oeQmvqIZVTtlxpte%2Bt1OCz%2Frp3OljayRbqagxtPPYB1UpiKzxChhYNUH999XLPOCnj75hJuTU16QS95ndLDnzuF5XavZ1Jq7FEMPxxmaDWij9PktbbwSTX%2FncYg6wI08ScTnjsg3imPFqZ%2B%2FHWKwWi19laVd0B%2FAibt7h4jLmrYT2chut6ck%2FsoQY65Vf0rbdo1daXiKWCwlnogRNF0UCMu1cO79tBvtQFm1zjeUDlN7TPGVvrbhkf4pMPowJH4R1cNSc5Qr0UfhFIkmZc2%2BtTXC9CGiwzRlmGtF8SY74sUtjfGimFu7HN2TYFWMe31ROy9l2TtfFWBbyaaVub%2BL6qTeaHfsyT%2F2qRumakWvEGUKqLhBWsLvTygv45a1hgnIcS1k5TNr5HQR%2BK6Ic9D8GjTQPJO6Hoc9XPuiieodV%2FvqX%2B8McBORG6fNflE%2FEGlHYdoRbIYHo2rcDDgrb3OBjqkAULmL3%2Fd3rpuRFvESAdoXts4MHkIA3Cjjplgyh8%2Bry4nAdz7vgFfhjA4tvILTJSyf5kGjegjtkCS850ZeVPcrRwWcgy6gmbU%2BsgrOa7O5Ew6vcq9yLhPeR73zbraq%2F5pP7i7URfxH13jvwOMwb6XKmatHw7ZUEthyEk6Q0z2l8ZkSLDoaXpPHYFsUou8XQpD%2BgX0J6jsz%2FhMYkD%2B8coeHLY15oEr&X-Amz-Signature=6fda149093811e52c6ab8db341db4604cd2f6e02e974a785e62239a655175f6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652VSTHU6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyB3%2F7Sldc4O6MRuE7qQc37aUFm0iQFFL304jZ7sKoTgIhAKTQChB0thebQ5HYTwAx4adrunnnHAMyeMRGfyfLBtr7Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxs%2Ftkt34q95%2B1qeS8q3AO7v%2BntMG4W2QhBa2y9JC%2B7w%2BYSy49PNiTck1D%2BiA9FLtVZEy%2BQwmlOE5HE9auff3dcYbo0yW6HqzBj%2FOD3Ks434kIJnOyykN%2Bf54NMPuscLgRYDXKr7q0DDAMhoANP69HddXThSoyvgLnhwLdMZBmR5CxpGrSB7zibN5%2B0oKPJLcx13oeQmvqIZVTtlxpte%2Bt1OCz%2Frp3OljayRbqagxtPPYB1UpiKzxChhYNUH999XLPOCnj75hJuTU16QS95ndLDnzuF5XavZ1Jq7FEMPxxmaDWij9PktbbwSTX%2FncYg6wI08ScTnjsg3imPFqZ%2B%2FHWKwWi19laVd0B%2FAibt7h4jLmrYT2chut6ck%2FsoQY65Vf0rbdo1daXiKWCwlnogRNF0UCMu1cO79tBvtQFm1zjeUDlN7TPGVvrbhkf4pMPowJH4R1cNSc5Qr0UfhFIkmZc2%2BtTXC9CGiwzRlmGtF8SY74sUtjfGimFu7HN2TYFWMe31ROy9l2TtfFWBbyaaVub%2BL6qTeaHfsyT%2F2qRumakWvEGUKqLhBWsLvTygv45a1hgnIcS1k5TNr5HQR%2BK6Ic9D8GjTQPJO6Hoc9XPuiieodV%2FvqX%2B8McBORG6fNflE%2FEGlHYdoRbIYHo2rcDDgrb3OBjqkAULmL3%2Fd3rpuRFvESAdoXts4MHkIA3Cjjplgyh8%2Bry4nAdz7vgFfhjA4tvILTJSyf5kGjegjtkCS850ZeVPcrRwWcgy6gmbU%2BsgrOa7O5Ew6vcq9yLhPeR73zbraq%2F5pP7i7URfxH13jvwOMwb6XKmatHw7ZUEthyEk6Q0z2l8ZkSLDoaXpPHYFsUou8XQpD%2BgX0J6jsz%2FhMYkD%2B8coeHLY15oEr&X-Amz-Signature=b666250dc5b9169e024969789c4913be2c0e241a9af4c7c32ade29f87c3eb722&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652VSTHU6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyB3%2F7Sldc4O6MRuE7qQc37aUFm0iQFFL304jZ7sKoTgIhAKTQChB0thebQ5HYTwAx4adrunnnHAMyeMRGfyfLBtr7Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxs%2Ftkt34q95%2B1qeS8q3AO7v%2BntMG4W2QhBa2y9JC%2B7w%2BYSy49PNiTck1D%2BiA9FLtVZEy%2BQwmlOE5HE9auff3dcYbo0yW6HqzBj%2FOD3Ks434kIJnOyykN%2Bf54NMPuscLgRYDXKr7q0DDAMhoANP69HddXThSoyvgLnhwLdMZBmR5CxpGrSB7zibN5%2B0oKPJLcx13oeQmvqIZVTtlxpte%2Bt1OCz%2Frp3OljayRbqagxtPPYB1UpiKzxChhYNUH999XLPOCnj75hJuTU16QS95ndLDnzuF5XavZ1Jq7FEMPxxmaDWij9PktbbwSTX%2FncYg6wI08ScTnjsg3imPFqZ%2B%2FHWKwWi19laVd0B%2FAibt7h4jLmrYT2chut6ck%2FsoQY65Vf0rbdo1daXiKWCwlnogRNF0UCMu1cO79tBvtQFm1zjeUDlN7TPGVvrbhkf4pMPowJH4R1cNSc5Qr0UfhFIkmZc2%2BtTXC9CGiwzRlmGtF8SY74sUtjfGimFu7HN2TYFWMe31ROy9l2TtfFWBbyaaVub%2BL6qTeaHfsyT%2F2qRumakWvEGUKqLhBWsLvTygv45a1hgnIcS1k5TNr5HQR%2BK6Ic9D8GjTQPJO6Hoc9XPuiieodV%2FvqX%2B8McBORG6fNflE%2FEGlHYdoRbIYHo2rcDDgrb3OBjqkAULmL3%2Fd3rpuRFvESAdoXts4MHkIA3Cjjplgyh8%2Bry4nAdz7vgFfhjA4tvILTJSyf5kGjegjtkCS850ZeVPcrRwWcgy6gmbU%2BsgrOa7O5Ew6vcq9yLhPeR73zbraq%2F5pP7i7URfxH13jvwOMwb6XKmatHw7ZUEthyEk6Q0z2l8ZkSLDoaXpPHYFsUou8XQpD%2BgX0J6jsz%2FhMYkD%2B8coeHLY15oEr&X-Amz-Signature=46d1cba423b22923bedccfbe43d51e2793fae090f567d42233b500b1eb5bd519&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652VSTHU6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyB3%2F7Sldc4O6MRuE7qQc37aUFm0iQFFL304jZ7sKoTgIhAKTQChB0thebQ5HYTwAx4adrunnnHAMyeMRGfyfLBtr7Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxs%2Ftkt34q95%2B1qeS8q3AO7v%2BntMG4W2QhBa2y9JC%2B7w%2BYSy49PNiTck1D%2BiA9FLtVZEy%2BQwmlOE5HE9auff3dcYbo0yW6HqzBj%2FOD3Ks434kIJnOyykN%2Bf54NMPuscLgRYDXKr7q0DDAMhoANP69HddXThSoyvgLnhwLdMZBmR5CxpGrSB7zibN5%2B0oKPJLcx13oeQmvqIZVTtlxpte%2Bt1OCz%2Frp3OljayRbqagxtPPYB1UpiKzxChhYNUH999XLPOCnj75hJuTU16QS95ndLDnzuF5XavZ1Jq7FEMPxxmaDWij9PktbbwSTX%2FncYg6wI08ScTnjsg3imPFqZ%2B%2FHWKwWi19laVd0B%2FAibt7h4jLmrYT2chut6ck%2FsoQY65Vf0rbdo1daXiKWCwlnogRNF0UCMu1cO79tBvtQFm1zjeUDlN7TPGVvrbhkf4pMPowJH4R1cNSc5Qr0UfhFIkmZc2%2BtTXC9CGiwzRlmGtF8SY74sUtjfGimFu7HN2TYFWMe31ROy9l2TtfFWBbyaaVub%2BL6qTeaHfsyT%2F2qRumakWvEGUKqLhBWsLvTygv45a1hgnIcS1k5TNr5HQR%2BK6Ic9D8GjTQPJO6Hoc9XPuiieodV%2FvqX%2B8McBORG6fNflE%2FEGlHYdoRbIYHo2rcDDgrb3OBjqkAULmL3%2Fd3rpuRFvESAdoXts4MHkIA3Cjjplgyh8%2Bry4nAdz7vgFfhjA4tvILTJSyf5kGjegjtkCS850ZeVPcrRwWcgy6gmbU%2BsgrOa7O5Ew6vcq9yLhPeR73zbraq%2F5pP7i7URfxH13jvwOMwb6XKmatHw7ZUEthyEk6Q0z2l8ZkSLDoaXpPHYFsUou8XQpD%2BgX0J6jsz%2FhMYkD%2B8coeHLY15oEr&X-Amz-Signature=3345879cd5fe0f1a180cd755d08ab238508d9bfc5ea2cb1efea01ae789d2b5dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652VSTHU6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyB3%2F7Sldc4O6MRuE7qQc37aUFm0iQFFL304jZ7sKoTgIhAKTQChB0thebQ5HYTwAx4adrunnnHAMyeMRGfyfLBtr7Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxs%2Ftkt34q95%2B1qeS8q3AO7v%2BntMG4W2QhBa2y9JC%2B7w%2BYSy49PNiTck1D%2BiA9FLtVZEy%2BQwmlOE5HE9auff3dcYbo0yW6HqzBj%2FOD3Ks434kIJnOyykN%2Bf54NMPuscLgRYDXKr7q0DDAMhoANP69HddXThSoyvgLnhwLdMZBmR5CxpGrSB7zibN5%2B0oKPJLcx13oeQmvqIZVTtlxpte%2Bt1OCz%2Frp3OljayRbqagxtPPYB1UpiKzxChhYNUH999XLPOCnj75hJuTU16QS95ndLDnzuF5XavZ1Jq7FEMPxxmaDWij9PktbbwSTX%2FncYg6wI08ScTnjsg3imPFqZ%2B%2FHWKwWi19laVd0B%2FAibt7h4jLmrYT2chut6ck%2FsoQY65Vf0rbdo1daXiKWCwlnogRNF0UCMu1cO79tBvtQFm1zjeUDlN7TPGVvrbhkf4pMPowJH4R1cNSc5Qr0UfhFIkmZc2%2BtTXC9CGiwzRlmGtF8SY74sUtjfGimFu7HN2TYFWMe31ROy9l2TtfFWBbyaaVub%2BL6qTeaHfsyT%2F2qRumakWvEGUKqLhBWsLvTygv45a1hgnIcS1k5TNr5HQR%2BK6Ic9D8GjTQPJO6Hoc9XPuiieodV%2FvqX%2B8McBORG6fNflE%2FEGlHYdoRbIYHo2rcDDgrb3OBjqkAULmL3%2Fd3rpuRFvESAdoXts4MHkIA3Cjjplgyh8%2Bry4nAdz7vgFfhjA4tvILTJSyf5kGjegjtkCS850ZeVPcrRwWcgy6gmbU%2BsgrOa7O5Ew6vcq9yLhPeR73zbraq%2F5pP7i7URfxH13jvwOMwb6XKmatHw7ZUEthyEk6Q0z2l8ZkSLDoaXpPHYFsUou8XQpD%2BgX0J6jsz%2FhMYkD%2B8coeHLY15oEr&X-Amz-Signature=9a1e5c13747b9bdcdc3cce75c0ff89e2ed06b963b7c416d7a8fbf4f7d62fd1b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652VSTHU6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyB3%2F7Sldc4O6MRuE7qQc37aUFm0iQFFL304jZ7sKoTgIhAKTQChB0thebQ5HYTwAx4adrunnnHAMyeMRGfyfLBtr7Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxs%2Ftkt34q95%2B1qeS8q3AO7v%2BntMG4W2QhBa2y9JC%2B7w%2BYSy49PNiTck1D%2BiA9FLtVZEy%2BQwmlOE5HE9auff3dcYbo0yW6HqzBj%2FOD3Ks434kIJnOyykN%2Bf54NMPuscLgRYDXKr7q0DDAMhoANP69HddXThSoyvgLnhwLdMZBmR5CxpGrSB7zibN5%2B0oKPJLcx13oeQmvqIZVTtlxpte%2Bt1OCz%2Frp3OljayRbqagxtPPYB1UpiKzxChhYNUH999XLPOCnj75hJuTU16QS95ndLDnzuF5XavZ1Jq7FEMPxxmaDWij9PktbbwSTX%2FncYg6wI08ScTnjsg3imPFqZ%2B%2FHWKwWi19laVd0B%2FAibt7h4jLmrYT2chut6ck%2FsoQY65Vf0rbdo1daXiKWCwlnogRNF0UCMu1cO79tBvtQFm1zjeUDlN7TPGVvrbhkf4pMPowJH4R1cNSc5Qr0UfhFIkmZc2%2BtTXC9CGiwzRlmGtF8SY74sUtjfGimFu7HN2TYFWMe31ROy9l2TtfFWBbyaaVub%2BL6qTeaHfsyT%2F2qRumakWvEGUKqLhBWsLvTygv45a1hgnIcS1k5TNr5HQR%2BK6Ic9D8GjTQPJO6Hoc9XPuiieodV%2FvqX%2B8McBORG6fNflE%2FEGlHYdoRbIYHo2rcDDgrb3OBjqkAULmL3%2Fd3rpuRFvESAdoXts4MHkIA3Cjjplgyh8%2Bry4nAdz7vgFfhjA4tvILTJSyf5kGjegjtkCS850ZeVPcrRwWcgy6gmbU%2BsgrOa7O5Ew6vcq9yLhPeR73zbraq%2F5pP7i7URfxH13jvwOMwb6XKmatHw7ZUEthyEk6Q0z2l8ZkSLDoaXpPHYFsUou8XQpD%2BgX0J6jsz%2FhMYkD%2B8coeHLY15oEr&X-Amz-Signature=64ad1cd8f92ce3ac2a984fa0f8de9f7724c5c86475a19dcad1a7aa23c3c1c7d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652VSTHU6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyB3%2F7Sldc4O6MRuE7qQc37aUFm0iQFFL304jZ7sKoTgIhAKTQChB0thebQ5HYTwAx4adrunnnHAMyeMRGfyfLBtr7Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxs%2Ftkt34q95%2B1qeS8q3AO7v%2BntMG4W2QhBa2y9JC%2B7w%2BYSy49PNiTck1D%2BiA9FLtVZEy%2BQwmlOE5HE9auff3dcYbo0yW6HqzBj%2FOD3Ks434kIJnOyykN%2Bf54NMPuscLgRYDXKr7q0DDAMhoANP69HddXThSoyvgLnhwLdMZBmR5CxpGrSB7zibN5%2B0oKPJLcx13oeQmvqIZVTtlxpte%2Bt1OCz%2Frp3OljayRbqagxtPPYB1UpiKzxChhYNUH999XLPOCnj75hJuTU16QS95ndLDnzuF5XavZ1Jq7FEMPxxmaDWij9PktbbwSTX%2FncYg6wI08ScTnjsg3imPFqZ%2B%2FHWKwWi19laVd0B%2FAibt7h4jLmrYT2chut6ck%2FsoQY65Vf0rbdo1daXiKWCwlnogRNF0UCMu1cO79tBvtQFm1zjeUDlN7TPGVvrbhkf4pMPowJH4R1cNSc5Qr0UfhFIkmZc2%2BtTXC9CGiwzRlmGtF8SY74sUtjfGimFu7HN2TYFWMe31ROy9l2TtfFWBbyaaVub%2BL6qTeaHfsyT%2F2qRumakWvEGUKqLhBWsLvTygv45a1hgnIcS1k5TNr5HQR%2BK6Ic9D8GjTQPJO6Hoc9XPuiieodV%2FvqX%2B8McBORG6fNflE%2FEGlHYdoRbIYHo2rcDDgrb3OBjqkAULmL3%2Fd3rpuRFvESAdoXts4MHkIA3Cjjplgyh8%2Bry4nAdz7vgFfhjA4tvILTJSyf5kGjegjtkCS850ZeVPcrRwWcgy6gmbU%2BsgrOa7O5Ew6vcq9yLhPeR73zbraq%2F5pP7i7URfxH13jvwOMwb6XKmatHw7ZUEthyEk6Q0z2l8ZkSLDoaXpPHYFsUou8XQpD%2BgX0J6jsz%2FhMYkD%2B8coeHLY15oEr&X-Amz-Signature=f874387fe2411d50034ffac516b9982c38faf1ee5de72a5ffebc6514a490bcc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652VSTHU6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyB3%2F7Sldc4O6MRuE7qQc37aUFm0iQFFL304jZ7sKoTgIhAKTQChB0thebQ5HYTwAx4adrunnnHAMyeMRGfyfLBtr7Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxs%2Ftkt34q95%2B1qeS8q3AO7v%2BntMG4W2QhBa2y9JC%2B7w%2BYSy49PNiTck1D%2BiA9FLtVZEy%2BQwmlOE5HE9auff3dcYbo0yW6HqzBj%2FOD3Ks434kIJnOyykN%2Bf54NMPuscLgRYDXKr7q0DDAMhoANP69HddXThSoyvgLnhwLdMZBmR5CxpGrSB7zibN5%2B0oKPJLcx13oeQmvqIZVTtlxpte%2Bt1OCz%2Frp3OljayRbqagxtPPYB1UpiKzxChhYNUH999XLPOCnj75hJuTU16QS95ndLDnzuF5XavZ1Jq7FEMPxxmaDWij9PktbbwSTX%2FncYg6wI08ScTnjsg3imPFqZ%2B%2FHWKwWi19laVd0B%2FAibt7h4jLmrYT2chut6ck%2FsoQY65Vf0rbdo1daXiKWCwlnogRNF0UCMu1cO79tBvtQFm1zjeUDlN7TPGVvrbhkf4pMPowJH4R1cNSc5Qr0UfhFIkmZc2%2BtTXC9CGiwzRlmGtF8SY74sUtjfGimFu7HN2TYFWMe31ROy9l2TtfFWBbyaaVub%2BL6qTeaHfsyT%2F2qRumakWvEGUKqLhBWsLvTygv45a1hgnIcS1k5TNr5HQR%2BK6Ic9D8GjTQPJO6Hoc9XPuiieodV%2FvqX%2B8McBORG6fNflE%2FEGlHYdoRbIYHo2rcDDgrb3OBjqkAULmL3%2Fd3rpuRFvESAdoXts4MHkIA3Cjjplgyh8%2Bry4nAdz7vgFfhjA4tvILTJSyf5kGjegjtkCS850ZeVPcrRwWcgy6gmbU%2BsgrOa7O5Ew6vcq9yLhPeR73zbraq%2F5pP7i7URfxH13jvwOMwb6XKmatHw7ZUEthyEk6Q0z2l8ZkSLDoaXpPHYFsUou8XQpD%2BgX0J6jsz%2FhMYkD%2B8coeHLY15oEr&X-Amz-Signature=20eba66a1ff1107a6a48187d5f383c4e81e56cc839048abf54277ec0c1e06394&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652VSTHU6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyB3%2F7Sldc4O6MRuE7qQc37aUFm0iQFFL304jZ7sKoTgIhAKTQChB0thebQ5HYTwAx4adrunnnHAMyeMRGfyfLBtr7Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxs%2Ftkt34q95%2B1qeS8q3AO7v%2BntMG4W2QhBa2y9JC%2B7w%2BYSy49PNiTck1D%2BiA9FLtVZEy%2BQwmlOE5HE9auff3dcYbo0yW6HqzBj%2FOD3Ks434kIJnOyykN%2Bf54NMPuscLgRYDXKr7q0DDAMhoANP69HddXThSoyvgLnhwLdMZBmR5CxpGrSB7zibN5%2B0oKPJLcx13oeQmvqIZVTtlxpte%2Bt1OCz%2Frp3OljayRbqagxtPPYB1UpiKzxChhYNUH999XLPOCnj75hJuTU16QS95ndLDnzuF5XavZ1Jq7FEMPxxmaDWij9PktbbwSTX%2FncYg6wI08ScTnjsg3imPFqZ%2B%2FHWKwWi19laVd0B%2FAibt7h4jLmrYT2chut6ck%2FsoQY65Vf0rbdo1daXiKWCwlnogRNF0UCMu1cO79tBvtQFm1zjeUDlN7TPGVvrbhkf4pMPowJH4R1cNSc5Qr0UfhFIkmZc2%2BtTXC9CGiwzRlmGtF8SY74sUtjfGimFu7HN2TYFWMe31ROy9l2TtfFWBbyaaVub%2BL6qTeaHfsyT%2F2qRumakWvEGUKqLhBWsLvTygv45a1hgnIcS1k5TNr5HQR%2BK6Ic9D8GjTQPJO6Hoc9XPuiieodV%2FvqX%2B8McBORG6fNflE%2FEGlHYdoRbIYHo2rcDDgrb3OBjqkAULmL3%2Fd3rpuRFvESAdoXts4MHkIA3Cjjplgyh8%2Bry4nAdz7vgFfhjA4tvILTJSyf5kGjegjtkCS850ZeVPcrRwWcgy6gmbU%2BsgrOa7O5Ew6vcq9yLhPeR73zbraq%2F5pP7i7URfxH13jvwOMwb6XKmatHw7ZUEthyEk6Q0z2l8ZkSLDoaXpPHYFsUou8XQpD%2BgX0J6jsz%2FhMYkD%2B8coeHLY15oEr&X-Amz-Signature=e4b8b63a088337f3dcf2c9d6c517ba03a956df673370060952ff3c7baeef8222&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

