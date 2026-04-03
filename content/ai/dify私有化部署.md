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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4OPW2KY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAclszQBPUCXlqoi%2FXeC707ZSvvQBgvfevKBChTguIhAIhALcC0q%2Bv5pGF%2Bm6QX4l%2Fk4E%2BbHe8bgZ5zfdqZqWqM3n8Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwagqMtjkgZgNfXu%2Fgq3APAbyCLHUm2AmYb0av79BylsR3sdDku41ftUdqrP6j1Xfrl2%2BdWvqEpcFlYiMzxRPoCGsqybKwRKYq5RWDpd5woXZ04MBL5eoGU7mUVVeVFQEd8AeoRauiJo%2BlXHrDRDZ%2F6KPhzFZI5oX1%2FGfF7shUfj7G9S9LV3Zihvtw5QlSDVl2ENxkS4QMnhd2yVGrmFQHDmVv6u5wt5WlBm3yobWAIE1CnD0LyGqiYWSSoFwMpMNOxmBmaZbEkOtZP53Hk1xO4BDAaGrFRLYIOENuWiRjfA8CeeZRsrEotzMV5mzYnsED3XrjIhwGsRKNjolLRjOLh%2FWMWr24iQqN9FoEoD2%2B%2FUorBr6Hm4r3%2FfhaxSpET8hdQou7bvkkPdUERKNe%2F1RnlO%2FiGBHE%2Bz4TzVbpheh1%2Bn%2F%2BCrvUJFT4vvJya%2B2ZyfPBaT0UCEiL6hV%2BkMz32LpLDkqXuOtj%2BcFaMRWB5%2B5fpOhgHAWVULJXJzCSvmhuBIUbu1nM20mgCuHhwkk4NLnWda3l31mf65sf9gb6I6fagAEsELmaKJgi0oM7yiairUkPviku2y7Kol9TZs4FoIJZ6P0YQkrKx2ooxOu%2Bc04sKWMbvWGGM2%2F8x0NnyVgfziHddbLWO42npR6x3%2BjCBrL3OBjqkAekvVMA8DWhNCJPbyVeifQrvtyPAZARFjVnIL568usTysVs5s9JvhlA4kW4sh0%2BoJDOgU05Ahzlpz5jvBR7Jh88igk6TFxybaZBOlLYkFLGneVFfkl2TbASabUa3T3Ull4X2Ujt7SnuZ9IptnbnJLzE8OLvj2u2vANyonbiVORFDXgEAHrkesEVdvG2v6z%2FHGH96d9Zx1yLV6QLIG4fG3Ix2OaZV&X-Amz-Signature=bd55657075d76b5992a22644819c2f588a622057e913bb3ca7c61252c53b5eaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4OPW2KY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAclszQBPUCXlqoi%2FXeC707ZSvvQBgvfevKBChTguIhAIhALcC0q%2Bv5pGF%2Bm6QX4l%2Fk4E%2BbHe8bgZ5zfdqZqWqM3n8Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwagqMtjkgZgNfXu%2Fgq3APAbyCLHUm2AmYb0av79BylsR3sdDku41ftUdqrP6j1Xfrl2%2BdWvqEpcFlYiMzxRPoCGsqybKwRKYq5RWDpd5woXZ04MBL5eoGU7mUVVeVFQEd8AeoRauiJo%2BlXHrDRDZ%2F6KPhzFZI5oX1%2FGfF7shUfj7G9S9LV3Zihvtw5QlSDVl2ENxkS4QMnhd2yVGrmFQHDmVv6u5wt5WlBm3yobWAIE1CnD0LyGqiYWSSoFwMpMNOxmBmaZbEkOtZP53Hk1xO4BDAaGrFRLYIOENuWiRjfA8CeeZRsrEotzMV5mzYnsED3XrjIhwGsRKNjolLRjOLh%2FWMWr24iQqN9FoEoD2%2B%2FUorBr6Hm4r3%2FfhaxSpET8hdQou7bvkkPdUERKNe%2F1RnlO%2FiGBHE%2Bz4TzVbpheh1%2Bn%2F%2BCrvUJFT4vvJya%2B2ZyfPBaT0UCEiL6hV%2BkMz32LpLDkqXuOtj%2BcFaMRWB5%2B5fpOhgHAWVULJXJzCSvmhuBIUbu1nM20mgCuHhwkk4NLnWda3l31mf65sf9gb6I6fagAEsELmaKJgi0oM7yiairUkPviku2y7Kol9TZs4FoIJZ6P0YQkrKx2ooxOu%2Bc04sKWMbvWGGM2%2F8x0NnyVgfziHddbLWO42npR6x3%2BjCBrL3OBjqkAekvVMA8DWhNCJPbyVeifQrvtyPAZARFjVnIL568usTysVs5s9JvhlA4kW4sh0%2BoJDOgU05Ahzlpz5jvBR7Jh88igk6TFxybaZBOlLYkFLGneVFfkl2TbASabUa3T3Ull4X2Ujt7SnuZ9IptnbnJLzE8OLvj2u2vANyonbiVORFDXgEAHrkesEVdvG2v6z%2FHGH96d9Zx1yLV6QLIG4fG3Ix2OaZV&X-Amz-Signature=9fb4a4baf98a44cbcf630ed5517434ca9fea8815c3c626146cd4952b383367c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4OPW2KY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAclszQBPUCXlqoi%2FXeC707ZSvvQBgvfevKBChTguIhAIhALcC0q%2Bv5pGF%2Bm6QX4l%2Fk4E%2BbHe8bgZ5zfdqZqWqM3n8Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwagqMtjkgZgNfXu%2Fgq3APAbyCLHUm2AmYb0av79BylsR3sdDku41ftUdqrP6j1Xfrl2%2BdWvqEpcFlYiMzxRPoCGsqybKwRKYq5RWDpd5woXZ04MBL5eoGU7mUVVeVFQEd8AeoRauiJo%2BlXHrDRDZ%2F6KPhzFZI5oX1%2FGfF7shUfj7G9S9LV3Zihvtw5QlSDVl2ENxkS4QMnhd2yVGrmFQHDmVv6u5wt5WlBm3yobWAIE1CnD0LyGqiYWSSoFwMpMNOxmBmaZbEkOtZP53Hk1xO4BDAaGrFRLYIOENuWiRjfA8CeeZRsrEotzMV5mzYnsED3XrjIhwGsRKNjolLRjOLh%2FWMWr24iQqN9FoEoD2%2B%2FUorBr6Hm4r3%2FfhaxSpET8hdQou7bvkkPdUERKNe%2F1RnlO%2FiGBHE%2Bz4TzVbpheh1%2Bn%2F%2BCrvUJFT4vvJya%2B2ZyfPBaT0UCEiL6hV%2BkMz32LpLDkqXuOtj%2BcFaMRWB5%2B5fpOhgHAWVULJXJzCSvmhuBIUbu1nM20mgCuHhwkk4NLnWda3l31mf65sf9gb6I6fagAEsELmaKJgi0oM7yiairUkPviku2y7Kol9TZs4FoIJZ6P0YQkrKx2ooxOu%2Bc04sKWMbvWGGM2%2F8x0NnyVgfziHddbLWO42npR6x3%2BjCBrL3OBjqkAekvVMA8DWhNCJPbyVeifQrvtyPAZARFjVnIL568usTysVs5s9JvhlA4kW4sh0%2BoJDOgU05Ahzlpz5jvBR7Jh88igk6TFxybaZBOlLYkFLGneVFfkl2TbASabUa3T3Ull4X2Ujt7SnuZ9IptnbnJLzE8OLvj2u2vANyonbiVORFDXgEAHrkesEVdvG2v6z%2FHGH96d9Zx1yLV6QLIG4fG3Ix2OaZV&X-Amz-Signature=0d108e5393cec42789d0c633cb593828da408e8972e190d7926bda3460d564e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4OPW2KY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAclszQBPUCXlqoi%2FXeC707ZSvvQBgvfevKBChTguIhAIhALcC0q%2Bv5pGF%2Bm6QX4l%2Fk4E%2BbHe8bgZ5zfdqZqWqM3n8Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwagqMtjkgZgNfXu%2Fgq3APAbyCLHUm2AmYb0av79BylsR3sdDku41ftUdqrP6j1Xfrl2%2BdWvqEpcFlYiMzxRPoCGsqybKwRKYq5RWDpd5woXZ04MBL5eoGU7mUVVeVFQEd8AeoRauiJo%2BlXHrDRDZ%2F6KPhzFZI5oX1%2FGfF7shUfj7G9S9LV3Zihvtw5QlSDVl2ENxkS4QMnhd2yVGrmFQHDmVv6u5wt5WlBm3yobWAIE1CnD0LyGqiYWSSoFwMpMNOxmBmaZbEkOtZP53Hk1xO4BDAaGrFRLYIOENuWiRjfA8CeeZRsrEotzMV5mzYnsED3XrjIhwGsRKNjolLRjOLh%2FWMWr24iQqN9FoEoD2%2B%2FUorBr6Hm4r3%2FfhaxSpET8hdQou7bvkkPdUERKNe%2F1RnlO%2FiGBHE%2Bz4TzVbpheh1%2Bn%2F%2BCrvUJFT4vvJya%2B2ZyfPBaT0UCEiL6hV%2BkMz32LpLDkqXuOtj%2BcFaMRWB5%2B5fpOhgHAWVULJXJzCSvmhuBIUbu1nM20mgCuHhwkk4NLnWda3l31mf65sf9gb6I6fagAEsELmaKJgi0oM7yiairUkPviku2y7Kol9TZs4FoIJZ6P0YQkrKx2ooxOu%2Bc04sKWMbvWGGM2%2F8x0NnyVgfziHddbLWO42npR6x3%2BjCBrL3OBjqkAekvVMA8DWhNCJPbyVeifQrvtyPAZARFjVnIL568usTysVs5s9JvhlA4kW4sh0%2BoJDOgU05Ahzlpz5jvBR7Jh88igk6TFxybaZBOlLYkFLGneVFfkl2TbASabUa3T3Ull4X2Ujt7SnuZ9IptnbnJLzE8OLvj2u2vANyonbiVORFDXgEAHrkesEVdvG2v6z%2FHGH96d9Zx1yLV6QLIG4fG3Ix2OaZV&X-Amz-Signature=4a7c992b84acae2b0e9362c3802fb095ef51ba00bcf320d848361e702b2d8427&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4OPW2KY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAclszQBPUCXlqoi%2FXeC707ZSvvQBgvfevKBChTguIhAIhALcC0q%2Bv5pGF%2Bm6QX4l%2Fk4E%2BbHe8bgZ5zfdqZqWqM3n8Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwagqMtjkgZgNfXu%2Fgq3APAbyCLHUm2AmYb0av79BylsR3sdDku41ftUdqrP6j1Xfrl2%2BdWvqEpcFlYiMzxRPoCGsqybKwRKYq5RWDpd5woXZ04MBL5eoGU7mUVVeVFQEd8AeoRauiJo%2BlXHrDRDZ%2F6KPhzFZI5oX1%2FGfF7shUfj7G9S9LV3Zihvtw5QlSDVl2ENxkS4QMnhd2yVGrmFQHDmVv6u5wt5WlBm3yobWAIE1CnD0LyGqiYWSSoFwMpMNOxmBmaZbEkOtZP53Hk1xO4BDAaGrFRLYIOENuWiRjfA8CeeZRsrEotzMV5mzYnsED3XrjIhwGsRKNjolLRjOLh%2FWMWr24iQqN9FoEoD2%2B%2FUorBr6Hm4r3%2FfhaxSpET8hdQou7bvkkPdUERKNe%2F1RnlO%2FiGBHE%2Bz4TzVbpheh1%2Bn%2F%2BCrvUJFT4vvJya%2B2ZyfPBaT0UCEiL6hV%2BkMz32LpLDkqXuOtj%2BcFaMRWB5%2B5fpOhgHAWVULJXJzCSvmhuBIUbu1nM20mgCuHhwkk4NLnWda3l31mf65sf9gb6I6fagAEsELmaKJgi0oM7yiairUkPviku2y7Kol9TZs4FoIJZ6P0YQkrKx2ooxOu%2Bc04sKWMbvWGGM2%2F8x0NnyVgfziHddbLWO42npR6x3%2BjCBrL3OBjqkAekvVMA8DWhNCJPbyVeifQrvtyPAZARFjVnIL568usTysVs5s9JvhlA4kW4sh0%2BoJDOgU05Ahzlpz5jvBR7Jh88igk6TFxybaZBOlLYkFLGneVFfkl2TbASabUa3T3Ull4X2Ujt7SnuZ9IptnbnJLzE8OLvj2u2vANyonbiVORFDXgEAHrkesEVdvG2v6z%2FHGH96d9Zx1yLV6QLIG4fG3Ix2OaZV&X-Amz-Signature=9a54c0f4f427208b9b67b95070168abc75211b09354bbe0a89cdead8333ce7c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4OPW2KY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAclszQBPUCXlqoi%2FXeC707ZSvvQBgvfevKBChTguIhAIhALcC0q%2Bv5pGF%2Bm6QX4l%2Fk4E%2BbHe8bgZ5zfdqZqWqM3n8Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwagqMtjkgZgNfXu%2Fgq3APAbyCLHUm2AmYb0av79BylsR3sdDku41ftUdqrP6j1Xfrl2%2BdWvqEpcFlYiMzxRPoCGsqybKwRKYq5RWDpd5woXZ04MBL5eoGU7mUVVeVFQEd8AeoRauiJo%2BlXHrDRDZ%2F6KPhzFZI5oX1%2FGfF7shUfj7G9S9LV3Zihvtw5QlSDVl2ENxkS4QMnhd2yVGrmFQHDmVv6u5wt5WlBm3yobWAIE1CnD0LyGqiYWSSoFwMpMNOxmBmaZbEkOtZP53Hk1xO4BDAaGrFRLYIOENuWiRjfA8CeeZRsrEotzMV5mzYnsED3XrjIhwGsRKNjolLRjOLh%2FWMWr24iQqN9FoEoD2%2B%2FUorBr6Hm4r3%2FfhaxSpET8hdQou7bvkkPdUERKNe%2F1RnlO%2FiGBHE%2Bz4TzVbpheh1%2Bn%2F%2BCrvUJFT4vvJya%2B2ZyfPBaT0UCEiL6hV%2BkMz32LpLDkqXuOtj%2BcFaMRWB5%2B5fpOhgHAWVULJXJzCSvmhuBIUbu1nM20mgCuHhwkk4NLnWda3l31mf65sf9gb6I6fagAEsELmaKJgi0oM7yiairUkPviku2y7Kol9TZs4FoIJZ6P0YQkrKx2ooxOu%2Bc04sKWMbvWGGM2%2F8x0NnyVgfziHddbLWO42npR6x3%2BjCBrL3OBjqkAekvVMA8DWhNCJPbyVeifQrvtyPAZARFjVnIL568usTysVs5s9JvhlA4kW4sh0%2BoJDOgU05Ahzlpz5jvBR7Jh88igk6TFxybaZBOlLYkFLGneVFfkl2TbASabUa3T3Ull4X2Ujt7SnuZ9IptnbnJLzE8OLvj2u2vANyonbiVORFDXgEAHrkesEVdvG2v6z%2FHGH96d9Zx1yLV6QLIG4fG3Ix2OaZV&X-Amz-Signature=2901dabf00f5adb614d0b4b4fe9b4878a6749a7232be5f80138282a16cbccd84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4OPW2KY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAclszQBPUCXlqoi%2FXeC707ZSvvQBgvfevKBChTguIhAIhALcC0q%2Bv5pGF%2Bm6QX4l%2Fk4E%2BbHe8bgZ5zfdqZqWqM3n8Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwagqMtjkgZgNfXu%2Fgq3APAbyCLHUm2AmYb0av79BylsR3sdDku41ftUdqrP6j1Xfrl2%2BdWvqEpcFlYiMzxRPoCGsqybKwRKYq5RWDpd5woXZ04MBL5eoGU7mUVVeVFQEd8AeoRauiJo%2BlXHrDRDZ%2F6KPhzFZI5oX1%2FGfF7shUfj7G9S9LV3Zihvtw5QlSDVl2ENxkS4QMnhd2yVGrmFQHDmVv6u5wt5WlBm3yobWAIE1CnD0LyGqiYWSSoFwMpMNOxmBmaZbEkOtZP53Hk1xO4BDAaGrFRLYIOENuWiRjfA8CeeZRsrEotzMV5mzYnsED3XrjIhwGsRKNjolLRjOLh%2FWMWr24iQqN9FoEoD2%2B%2FUorBr6Hm4r3%2FfhaxSpET8hdQou7bvkkPdUERKNe%2F1RnlO%2FiGBHE%2Bz4TzVbpheh1%2Bn%2F%2BCrvUJFT4vvJya%2B2ZyfPBaT0UCEiL6hV%2BkMz32LpLDkqXuOtj%2BcFaMRWB5%2B5fpOhgHAWVULJXJzCSvmhuBIUbu1nM20mgCuHhwkk4NLnWda3l31mf65sf9gb6I6fagAEsELmaKJgi0oM7yiairUkPviku2y7Kol9TZs4FoIJZ6P0YQkrKx2ooxOu%2Bc04sKWMbvWGGM2%2F8x0NnyVgfziHddbLWO42npR6x3%2BjCBrL3OBjqkAekvVMA8DWhNCJPbyVeifQrvtyPAZARFjVnIL568usTysVs5s9JvhlA4kW4sh0%2BoJDOgU05Ahzlpz5jvBR7Jh88igk6TFxybaZBOlLYkFLGneVFfkl2TbASabUa3T3Ull4X2Ujt7SnuZ9IptnbnJLzE8OLvj2u2vANyonbiVORFDXgEAHrkesEVdvG2v6z%2FHGH96d9Zx1yLV6QLIG4fG3Ix2OaZV&X-Amz-Signature=142382307533df94ad157649afa32397171c17545f8921e7799b1ce481cca11e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4OPW2KY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAclszQBPUCXlqoi%2FXeC707ZSvvQBgvfevKBChTguIhAIhALcC0q%2Bv5pGF%2Bm6QX4l%2Fk4E%2BbHe8bgZ5zfdqZqWqM3n8Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwagqMtjkgZgNfXu%2Fgq3APAbyCLHUm2AmYb0av79BylsR3sdDku41ftUdqrP6j1Xfrl2%2BdWvqEpcFlYiMzxRPoCGsqybKwRKYq5RWDpd5woXZ04MBL5eoGU7mUVVeVFQEd8AeoRauiJo%2BlXHrDRDZ%2F6KPhzFZI5oX1%2FGfF7shUfj7G9S9LV3Zihvtw5QlSDVl2ENxkS4QMnhd2yVGrmFQHDmVv6u5wt5WlBm3yobWAIE1CnD0LyGqiYWSSoFwMpMNOxmBmaZbEkOtZP53Hk1xO4BDAaGrFRLYIOENuWiRjfA8CeeZRsrEotzMV5mzYnsED3XrjIhwGsRKNjolLRjOLh%2FWMWr24iQqN9FoEoD2%2B%2FUorBr6Hm4r3%2FfhaxSpET8hdQou7bvkkPdUERKNe%2F1RnlO%2FiGBHE%2Bz4TzVbpheh1%2Bn%2F%2BCrvUJFT4vvJya%2B2ZyfPBaT0UCEiL6hV%2BkMz32LpLDkqXuOtj%2BcFaMRWB5%2B5fpOhgHAWVULJXJzCSvmhuBIUbu1nM20mgCuHhwkk4NLnWda3l31mf65sf9gb6I6fagAEsELmaKJgi0oM7yiairUkPviku2y7Kol9TZs4FoIJZ6P0YQkrKx2ooxOu%2Bc04sKWMbvWGGM2%2F8x0NnyVgfziHddbLWO42npR6x3%2BjCBrL3OBjqkAekvVMA8DWhNCJPbyVeifQrvtyPAZARFjVnIL568usTysVs5s9JvhlA4kW4sh0%2BoJDOgU05Ahzlpz5jvBR7Jh88igk6TFxybaZBOlLYkFLGneVFfkl2TbASabUa3T3Ull4X2Ujt7SnuZ9IptnbnJLzE8OLvj2u2vANyonbiVORFDXgEAHrkesEVdvG2v6z%2FHGH96d9Zx1yLV6QLIG4fG3Ix2OaZV&X-Amz-Signature=691a13e17b54f6e3a5f06b1431035799cb359dffbd43cbb55c7b2c944721295b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4OPW2KY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAclszQBPUCXlqoi%2FXeC707ZSvvQBgvfevKBChTguIhAIhALcC0q%2Bv5pGF%2Bm6QX4l%2Fk4E%2BbHe8bgZ5zfdqZqWqM3n8Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwagqMtjkgZgNfXu%2Fgq3APAbyCLHUm2AmYb0av79BylsR3sdDku41ftUdqrP6j1Xfrl2%2BdWvqEpcFlYiMzxRPoCGsqybKwRKYq5RWDpd5woXZ04MBL5eoGU7mUVVeVFQEd8AeoRauiJo%2BlXHrDRDZ%2F6KPhzFZI5oX1%2FGfF7shUfj7G9S9LV3Zihvtw5QlSDVl2ENxkS4QMnhd2yVGrmFQHDmVv6u5wt5WlBm3yobWAIE1CnD0LyGqiYWSSoFwMpMNOxmBmaZbEkOtZP53Hk1xO4BDAaGrFRLYIOENuWiRjfA8CeeZRsrEotzMV5mzYnsED3XrjIhwGsRKNjolLRjOLh%2FWMWr24iQqN9FoEoD2%2B%2FUorBr6Hm4r3%2FfhaxSpET8hdQou7bvkkPdUERKNe%2F1RnlO%2FiGBHE%2Bz4TzVbpheh1%2Bn%2F%2BCrvUJFT4vvJya%2B2ZyfPBaT0UCEiL6hV%2BkMz32LpLDkqXuOtj%2BcFaMRWB5%2B5fpOhgHAWVULJXJzCSvmhuBIUbu1nM20mgCuHhwkk4NLnWda3l31mf65sf9gb6I6fagAEsELmaKJgi0oM7yiairUkPviku2y7Kol9TZs4FoIJZ6P0YQkrKx2ooxOu%2Bc04sKWMbvWGGM2%2F8x0NnyVgfziHddbLWO42npR6x3%2BjCBrL3OBjqkAekvVMA8DWhNCJPbyVeifQrvtyPAZARFjVnIL568usTysVs5s9JvhlA4kW4sh0%2BoJDOgU05Ahzlpz5jvBR7Jh88igk6TFxybaZBOlLYkFLGneVFfkl2TbASabUa3T3Ull4X2Ujt7SnuZ9IptnbnJLzE8OLvj2u2vANyonbiVORFDXgEAHrkesEVdvG2v6z%2FHGH96d9Zx1yLV6QLIG4fG3Ix2OaZV&X-Amz-Signature=fa7ae8d4cdf5de49fd15d466791bd6b33bd2d809c6d85a57e4d415bc6fda8ea1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4OPW2KY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAclszQBPUCXlqoi%2FXeC707ZSvvQBgvfevKBChTguIhAIhALcC0q%2Bv5pGF%2Bm6QX4l%2Fk4E%2BbHe8bgZ5zfdqZqWqM3n8Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwagqMtjkgZgNfXu%2Fgq3APAbyCLHUm2AmYb0av79BylsR3sdDku41ftUdqrP6j1Xfrl2%2BdWvqEpcFlYiMzxRPoCGsqybKwRKYq5RWDpd5woXZ04MBL5eoGU7mUVVeVFQEd8AeoRauiJo%2BlXHrDRDZ%2F6KPhzFZI5oX1%2FGfF7shUfj7G9S9LV3Zihvtw5QlSDVl2ENxkS4QMnhd2yVGrmFQHDmVv6u5wt5WlBm3yobWAIE1CnD0LyGqiYWSSoFwMpMNOxmBmaZbEkOtZP53Hk1xO4BDAaGrFRLYIOENuWiRjfA8CeeZRsrEotzMV5mzYnsED3XrjIhwGsRKNjolLRjOLh%2FWMWr24iQqN9FoEoD2%2B%2FUorBr6Hm4r3%2FfhaxSpET8hdQou7bvkkPdUERKNe%2F1RnlO%2FiGBHE%2Bz4TzVbpheh1%2Bn%2F%2BCrvUJFT4vvJya%2B2ZyfPBaT0UCEiL6hV%2BkMz32LpLDkqXuOtj%2BcFaMRWB5%2B5fpOhgHAWVULJXJzCSvmhuBIUbu1nM20mgCuHhwkk4NLnWda3l31mf65sf9gb6I6fagAEsELmaKJgi0oM7yiairUkPviku2y7Kol9TZs4FoIJZ6P0YQkrKx2ooxOu%2Bc04sKWMbvWGGM2%2F8x0NnyVgfziHddbLWO42npR6x3%2BjCBrL3OBjqkAekvVMA8DWhNCJPbyVeifQrvtyPAZARFjVnIL568usTysVs5s9JvhlA4kW4sh0%2BoJDOgU05Ahzlpz5jvBR7Jh88igk6TFxybaZBOlLYkFLGneVFfkl2TbASabUa3T3Ull4X2Ujt7SnuZ9IptnbnJLzE8OLvj2u2vANyonbiVORFDXgEAHrkesEVdvG2v6z%2FHGH96d9Zx1yLV6QLIG4fG3Ix2OaZV&X-Amz-Signature=5213ad038e1de99e8fb1d6cebce2c081cc767ff6f3af14bbd354c034b3f973ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

