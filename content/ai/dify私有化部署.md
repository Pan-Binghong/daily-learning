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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECXWHVV%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKtEEE5G8CS62uX1%2BYfI6c0X82ez10ENAffnSN2WSQcAiEA%2BKm3yshKsqaGk2%2FcwAgf2f6rUKVrjx6wKiC7KkZU7SEqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKr0EI%2B5hlAtPTS%2FMCrcA4TD%2FGK%2BdtHCcgiM9fIkc4FMTZFaUJWCZxKU8L%2BHSwBXDY28Ofjgf19eLIcP8d10GE8btGJk2XAlVqnFtwU1sxO%2FEGG4VX%2BGto20tizMOrCsFbrRyVNuE1ns5GoFJFPoVD1EOUSZi7XmOcM6eE5UeguDuNCPKn39K0jnz%2B72goeey37Ax2FxSYCPOlz42afgOvl55UYY0BqM6ycG5a7ND90YUGZeS%2FBsY5xIlpHOPYKoc7C%2FpbX6lwXfxo3vzJtVVcb9Rw6WI66UDu%2FwVQBdBmw81mXf4NCxtbxKSmeCHSNoOs63o8cjkEReQLOWkonxxfuyPl02UAH7fJ1n9AglDmHofpgUz1n8nKM5%2Bb8LoCIdWmqjmEkw4RjQBJKKg2M2EQGv2%2F5AAvxM5Vd5%2BqEIIMsGGHYweDjTESNO3Kte23KhxSzksmwUBNu1eeMg4ixoG8jK4%2BOHAUh65%2F%2Fc4LKtHPtoBl2%2BWRktTIBvuGdbHoOZqptgq%2B9oV1X3hC2Pqj1S2Gxhx%2FsXLfQFaN6LGpOtLyyCcDEtDxEO7cpKmhN9q2ZO7ifrNvhDv%2Bw7MeZgMgJeR0n7sVwIoWyv1KYUMlOnw2q45dtWD3%2FFrDNjVTReFGw0upFiZygnNnFeaPoYMKyUqckGOqUBp%2F%2FoozPMMTTYfM75SamYVOthQ26gBb7SelGaBYa704p57GaJhwIT9aRSBJhZkYruJ1G2Bt04KSk4nsIcsOnEqStH9q8LbmM2uKq09%2BJ0aMEqvacVcsupOfT2qklnL8iVjIzazWXcMMf6aHhPgE9ReQAEnotgDLoRWKyysANTFKY6dEMHKtG2iU8i7lNaN2naV%2BflFURq%2BYqOiPHuVwoX44TmBvao&X-Amz-Signature=1c9b91fa53a0c5190d025da14fd08298dab3a9c1a5de9b388763f7ae4977859b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECXWHVV%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKtEEE5G8CS62uX1%2BYfI6c0X82ez10ENAffnSN2WSQcAiEA%2BKm3yshKsqaGk2%2FcwAgf2f6rUKVrjx6wKiC7KkZU7SEqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKr0EI%2B5hlAtPTS%2FMCrcA4TD%2FGK%2BdtHCcgiM9fIkc4FMTZFaUJWCZxKU8L%2BHSwBXDY28Ofjgf19eLIcP8d10GE8btGJk2XAlVqnFtwU1sxO%2FEGG4VX%2BGto20tizMOrCsFbrRyVNuE1ns5GoFJFPoVD1EOUSZi7XmOcM6eE5UeguDuNCPKn39K0jnz%2B72goeey37Ax2FxSYCPOlz42afgOvl55UYY0BqM6ycG5a7ND90YUGZeS%2FBsY5xIlpHOPYKoc7C%2FpbX6lwXfxo3vzJtVVcb9Rw6WI66UDu%2FwVQBdBmw81mXf4NCxtbxKSmeCHSNoOs63o8cjkEReQLOWkonxxfuyPl02UAH7fJ1n9AglDmHofpgUz1n8nKM5%2Bb8LoCIdWmqjmEkw4RjQBJKKg2M2EQGv2%2F5AAvxM5Vd5%2BqEIIMsGGHYweDjTESNO3Kte23KhxSzksmwUBNu1eeMg4ixoG8jK4%2BOHAUh65%2F%2Fc4LKtHPtoBl2%2BWRktTIBvuGdbHoOZqptgq%2B9oV1X3hC2Pqj1S2Gxhx%2FsXLfQFaN6LGpOtLyyCcDEtDxEO7cpKmhN9q2ZO7ifrNvhDv%2Bw7MeZgMgJeR0n7sVwIoWyv1KYUMlOnw2q45dtWD3%2FFrDNjVTReFGw0upFiZygnNnFeaPoYMKyUqckGOqUBp%2F%2FoozPMMTTYfM75SamYVOthQ26gBb7SelGaBYa704p57GaJhwIT9aRSBJhZkYruJ1G2Bt04KSk4nsIcsOnEqStH9q8LbmM2uKq09%2BJ0aMEqvacVcsupOfT2qklnL8iVjIzazWXcMMf6aHhPgE9ReQAEnotgDLoRWKyysANTFKY6dEMHKtG2iU8i7lNaN2naV%2BflFURq%2BYqOiPHuVwoX44TmBvao&X-Amz-Signature=1d2b50422d05b5918b5527eac4caab62e04cd5b2c9de4b2d0e5b5aef7849069e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECXWHVV%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKtEEE5G8CS62uX1%2BYfI6c0X82ez10ENAffnSN2WSQcAiEA%2BKm3yshKsqaGk2%2FcwAgf2f6rUKVrjx6wKiC7KkZU7SEqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKr0EI%2B5hlAtPTS%2FMCrcA4TD%2FGK%2BdtHCcgiM9fIkc4FMTZFaUJWCZxKU8L%2BHSwBXDY28Ofjgf19eLIcP8d10GE8btGJk2XAlVqnFtwU1sxO%2FEGG4VX%2BGto20tizMOrCsFbrRyVNuE1ns5GoFJFPoVD1EOUSZi7XmOcM6eE5UeguDuNCPKn39K0jnz%2B72goeey37Ax2FxSYCPOlz42afgOvl55UYY0BqM6ycG5a7ND90YUGZeS%2FBsY5xIlpHOPYKoc7C%2FpbX6lwXfxo3vzJtVVcb9Rw6WI66UDu%2FwVQBdBmw81mXf4NCxtbxKSmeCHSNoOs63o8cjkEReQLOWkonxxfuyPl02UAH7fJ1n9AglDmHofpgUz1n8nKM5%2Bb8LoCIdWmqjmEkw4RjQBJKKg2M2EQGv2%2F5AAvxM5Vd5%2BqEIIMsGGHYweDjTESNO3Kte23KhxSzksmwUBNu1eeMg4ixoG8jK4%2BOHAUh65%2F%2Fc4LKtHPtoBl2%2BWRktTIBvuGdbHoOZqptgq%2B9oV1X3hC2Pqj1S2Gxhx%2FsXLfQFaN6LGpOtLyyCcDEtDxEO7cpKmhN9q2ZO7ifrNvhDv%2Bw7MeZgMgJeR0n7sVwIoWyv1KYUMlOnw2q45dtWD3%2FFrDNjVTReFGw0upFiZygnNnFeaPoYMKyUqckGOqUBp%2F%2FoozPMMTTYfM75SamYVOthQ26gBb7SelGaBYa704p57GaJhwIT9aRSBJhZkYruJ1G2Bt04KSk4nsIcsOnEqStH9q8LbmM2uKq09%2BJ0aMEqvacVcsupOfT2qklnL8iVjIzazWXcMMf6aHhPgE9ReQAEnotgDLoRWKyysANTFKY6dEMHKtG2iU8i7lNaN2naV%2BflFURq%2BYqOiPHuVwoX44TmBvao&X-Amz-Signature=57ea049949fc85b74617b8f38b45845a2ff809967b063dacdb3b4bffebf86469&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECXWHVV%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKtEEE5G8CS62uX1%2BYfI6c0X82ez10ENAffnSN2WSQcAiEA%2BKm3yshKsqaGk2%2FcwAgf2f6rUKVrjx6wKiC7KkZU7SEqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKr0EI%2B5hlAtPTS%2FMCrcA4TD%2FGK%2BdtHCcgiM9fIkc4FMTZFaUJWCZxKU8L%2BHSwBXDY28Ofjgf19eLIcP8d10GE8btGJk2XAlVqnFtwU1sxO%2FEGG4VX%2BGto20tizMOrCsFbrRyVNuE1ns5GoFJFPoVD1EOUSZi7XmOcM6eE5UeguDuNCPKn39K0jnz%2B72goeey37Ax2FxSYCPOlz42afgOvl55UYY0BqM6ycG5a7ND90YUGZeS%2FBsY5xIlpHOPYKoc7C%2FpbX6lwXfxo3vzJtVVcb9Rw6WI66UDu%2FwVQBdBmw81mXf4NCxtbxKSmeCHSNoOs63o8cjkEReQLOWkonxxfuyPl02UAH7fJ1n9AglDmHofpgUz1n8nKM5%2Bb8LoCIdWmqjmEkw4RjQBJKKg2M2EQGv2%2F5AAvxM5Vd5%2BqEIIMsGGHYweDjTESNO3Kte23KhxSzksmwUBNu1eeMg4ixoG8jK4%2BOHAUh65%2F%2Fc4LKtHPtoBl2%2BWRktTIBvuGdbHoOZqptgq%2B9oV1X3hC2Pqj1S2Gxhx%2FsXLfQFaN6LGpOtLyyCcDEtDxEO7cpKmhN9q2ZO7ifrNvhDv%2Bw7MeZgMgJeR0n7sVwIoWyv1KYUMlOnw2q45dtWD3%2FFrDNjVTReFGw0upFiZygnNnFeaPoYMKyUqckGOqUBp%2F%2FoozPMMTTYfM75SamYVOthQ26gBb7SelGaBYa704p57GaJhwIT9aRSBJhZkYruJ1G2Bt04KSk4nsIcsOnEqStH9q8LbmM2uKq09%2BJ0aMEqvacVcsupOfT2qklnL8iVjIzazWXcMMf6aHhPgE9ReQAEnotgDLoRWKyysANTFKY6dEMHKtG2iU8i7lNaN2naV%2BflFURq%2BYqOiPHuVwoX44TmBvao&X-Amz-Signature=cb931bc7cab59c75a8dc1e8880000c87d8dbc64ade57b0048d8ac1446e5c04c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECXWHVV%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKtEEE5G8CS62uX1%2BYfI6c0X82ez10ENAffnSN2WSQcAiEA%2BKm3yshKsqaGk2%2FcwAgf2f6rUKVrjx6wKiC7KkZU7SEqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKr0EI%2B5hlAtPTS%2FMCrcA4TD%2FGK%2BdtHCcgiM9fIkc4FMTZFaUJWCZxKU8L%2BHSwBXDY28Ofjgf19eLIcP8d10GE8btGJk2XAlVqnFtwU1sxO%2FEGG4VX%2BGto20tizMOrCsFbrRyVNuE1ns5GoFJFPoVD1EOUSZi7XmOcM6eE5UeguDuNCPKn39K0jnz%2B72goeey37Ax2FxSYCPOlz42afgOvl55UYY0BqM6ycG5a7ND90YUGZeS%2FBsY5xIlpHOPYKoc7C%2FpbX6lwXfxo3vzJtVVcb9Rw6WI66UDu%2FwVQBdBmw81mXf4NCxtbxKSmeCHSNoOs63o8cjkEReQLOWkonxxfuyPl02UAH7fJ1n9AglDmHofpgUz1n8nKM5%2Bb8LoCIdWmqjmEkw4RjQBJKKg2M2EQGv2%2F5AAvxM5Vd5%2BqEIIMsGGHYweDjTESNO3Kte23KhxSzksmwUBNu1eeMg4ixoG8jK4%2BOHAUh65%2F%2Fc4LKtHPtoBl2%2BWRktTIBvuGdbHoOZqptgq%2B9oV1X3hC2Pqj1S2Gxhx%2FsXLfQFaN6LGpOtLyyCcDEtDxEO7cpKmhN9q2ZO7ifrNvhDv%2Bw7MeZgMgJeR0n7sVwIoWyv1KYUMlOnw2q45dtWD3%2FFrDNjVTReFGw0upFiZygnNnFeaPoYMKyUqckGOqUBp%2F%2FoozPMMTTYfM75SamYVOthQ26gBb7SelGaBYa704p57GaJhwIT9aRSBJhZkYruJ1G2Bt04KSk4nsIcsOnEqStH9q8LbmM2uKq09%2BJ0aMEqvacVcsupOfT2qklnL8iVjIzazWXcMMf6aHhPgE9ReQAEnotgDLoRWKyysANTFKY6dEMHKtG2iU8i7lNaN2naV%2BflFURq%2BYqOiPHuVwoX44TmBvao&X-Amz-Signature=5f7266b6dc05e2fafede3eaed407a715e86bf2b7d29110eefb1c8f41fb268e16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECXWHVV%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKtEEE5G8CS62uX1%2BYfI6c0X82ez10ENAffnSN2WSQcAiEA%2BKm3yshKsqaGk2%2FcwAgf2f6rUKVrjx6wKiC7KkZU7SEqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKr0EI%2B5hlAtPTS%2FMCrcA4TD%2FGK%2BdtHCcgiM9fIkc4FMTZFaUJWCZxKU8L%2BHSwBXDY28Ofjgf19eLIcP8d10GE8btGJk2XAlVqnFtwU1sxO%2FEGG4VX%2BGto20tizMOrCsFbrRyVNuE1ns5GoFJFPoVD1EOUSZi7XmOcM6eE5UeguDuNCPKn39K0jnz%2B72goeey37Ax2FxSYCPOlz42afgOvl55UYY0BqM6ycG5a7ND90YUGZeS%2FBsY5xIlpHOPYKoc7C%2FpbX6lwXfxo3vzJtVVcb9Rw6WI66UDu%2FwVQBdBmw81mXf4NCxtbxKSmeCHSNoOs63o8cjkEReQLOWkonxxfuyPl02UAH7fJ1n9AglDmHofpgUz1n8nKM5%2Bb8LoCIdWmqjmEkw4RjQBJKKg2M2EQGv2%2F5AAvxM5Vd5%2BqEIIMsGGHYweDjTESNO3Kte23KhxSzksmwUBNu1eeMg4ixoG8jK4%2BOHAUh65%2F%2Fc4LKtHPtoBl2%2BWRktTIBvuGdbHoOZqptgq%2B9oV1X3hC2Pqj1S2Gxhx%2FsXLfQFaN6LGpOtLyyCcDEtDxEO7cpKmhN9q2ZO7ifrNvhDv%2Bw7MeZgMgJeR0n7sVwIoWyv1KYUMlOnw2q45dtWD3%2FFrDNjVTReFGw0upFiZygnNnFeaPoYMKyUqckGOqUBp%2F%2FoozPMMTTYfM75SamYVOthQ26gBb7SelGaBYa704p57GaJhwIT9aRSBJhZkYruJ1G2Bt04KSk4nsIcsOnEqStH9q8LbmM2uKq09%2BJ0aMEqvacVcsupOfT2qklnL8iVjIzazWXcMMf6aHhPgE9ReQAEnotgDLoRWKyysANTFKY6dEMHKtG2iU8i7lNaN2naV%2BflFURq%2BYqOiPHuVwoX44TmBvao&X-Amz-Signature=fa680a6bd9a52aba943560e2b9560dc0a923ad090ed4a8f0aedfed9aad170b7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECXWHVV%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKtEEE5G8CS62uX1%2BYfI6c0X82ez10ENAffnSN2WSQcAiEA%2BKm3yshKsqaGk2%2FcwAgf2f6rUKVrjx6wKiC7KkZU7SEqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKr0EI%2B5hlAtPTS%2FMCrcA4TD%2FGK%2BdtHCcgiM9fIkc4FMTZFaUJWCZxKU8L%2BHSwBXDY28Ofjgf19eLIcP8d10GE8btGJk2XAlVqnFtwU1sxO%2FEGG4VX%2BGto20tizMOrCsFbrRyVNuE1ns5GoFJFPoVD1EOUSZi7XmOcM6eE5UeguDuNCPKn39K0jnz%2B72goeey37Ax2FxSYCPOlz42afgOvl55UYY0BqM6ycG5a7ND90YUGZeS%2FBsY5xIlpHOPYKoc7C%2FpbX6lwXfxo3vzJtVVcb9Rw6WI66UDu%2FwVQBdBmw81mXf4NCxtbxKSmeCHSNoOs63o8cjkEReQLOWkonxxfuyPl02UAH7fJ1n9AglDmHofpgUz1n8nKM5%2Bb8LoCIdWmqjmEkw4RjQBJKKg2M2EQGv2%2F5AAvxM5Vd5%2BqEIIMsGGHYweDjTESNO3Kte23KhxSzksmwUBNu1eeMg4ixoG8jK4%2BOHAUh65%2F%2Fc4LKtHPtoBl2%2BWRktTIBvuGdbHoOZqptgq%2B9oV1X3hC2Pqj1S2Gxhx%2FsXLfQFaN6LGpOtLyyCcDEtDxEO7cpKmhN9q2ZO7ifrNvhDv%2Bw7MeZgMgJeR0n7sVwIoWyv1KYUMlOnw2q45dtWD3%2FFrDNjVTReFGw0upFiZygnNnFeaPoYMKyUqckGOqUBp%2F%2FoozPMMTTYfM75SamYVOthQ26gBb7SelGaBYa704p57GaJhwIT9aRSBJhZkYruJ1G2Bt04KSk4nsIcsOnEqStH9q8LbmM2uKq09%2BJ0aMEqvacVcsupOfT2qklnL8iVjIzazWXcMMf6aHhPgE9ReQAEnotgDLoRWKyysANTFKY6dEMHKtG2iU8i7lNaN2naV%2BflFURq%2BYqOiPHuVwoX44TmBvao&X-Amz-Signature=bb2bf79025a8331cc9fffee7c6aecb7eccf7b82c7fc59f927ac8145084b2612a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECXWHVV%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKtEEE5G8CS62uX1%2BYfI6c0X82ez10ENAffnSN2WSQcAiEA%2BKm3yshKsqaGk2%2FcwAgf2f6rUKVrjx6wKiC7KkZU7SEqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKr0EI%2B5hlAtPTS%2FMCrcA4TD%2FGK%2BdtHCcgiM9fIkc4FMTZFaUJWCZxKU8L%2BHSwBXDY28Ofjgf19eLIcP8d10GE8btGJk2XAlVqnFtwU1sxO%2FEGG4VX%2BGto20tizMOrCsFbrRyVNuE1ns5GoFJFPoVD1EOUSZi7XmOcM6eE5UeguDuNCPKn39K0jnz%2B72goeey37Ax2FxSYCPOlz42afgOvl55UYY0BqM6ycG5a7ND90YUGZeS%2FBsY5xIlpHOPYKoc7C%2FpbX6lwXfxo3vzJtVVcb9Rw6WI66UDu%2FwVQBdBmw81mXf4NCxtbxKSmeCHSNoOs63o8cjkEReQLOWkonxxfuyPl02UAH7fJ1n9AglDmHofpgUz1n8nKM5%2Bb8LoCIdWmqjmEkw4RjQBJKKg2M2EQGv2%2F5AAvxM5Vd5%2BqEIIMsGGHYweDjTESNO3Kte23KhxSzksmwUBNu1eeMg4ixoG8jK4%2BOHAUh65%2F%2Fc4LKtHPtoBl2%2BWRktTIBvuGdbHoOZqptgq%2B9oV1X3hC2Pqj1S2Gxhx%2FsXLfQFaN6LGpOtLyyCcDEtDxEO7cpKmhN9q2ZO7ifrNvhDv%2Bw7MeZgMgJeR0n7sVwIoWyv1KYUMlOnw2q45dtWD3%2FFrDNjVTReFGw0upFiZygnNnFeaPoYMKyUqckGOqUBp%2F%2FoozPMMTTYfM75SamYVOthQ26gBb7SelGaBYa704p57GaJhwIT9aRSBJhZkYruJ1G2Bt04KSk4nsIcsOnEqStH9q8LbmM2uKq09%2BJ0aMEqvacVcsupOfT2qklnL8iVjIzazWXcMMf6aHhPgE9ReQAEnotgDLoRWKyysANTFKY6dEMHKtG2iU8i7lNaN2naV%2BflFURq%2BYqOiPHuVwoX44TmBvao&X-Amz-Signature=40d9b18526accb9722bb0c7d42bfacc222289f53026802be6082570bcc99deff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECXWHVV%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKtEEE5G8CS62uX1%2BYfI6c0X82ez10ENAffnSN2WSQcAiEA%2BKm3yshKsqaGk2%2FcwAgf2f6rUKVrjx6wKiC7KkZU7SEqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKr0EI%2B5hlAtPTS%2FMCrcA4TD%2FGK%2BdtHCcgiM9fIkc4FMTZFaUJWCZxKU8L%2BHSwBXDY28Ofjgf19eLIcP8d10GE8btGJk2XAlVqnFtwU1sxO%2FEGG4VX%2BGto20tizMOrCsFbrRyVNuE1ns5GoFJFPoVD1EOUSZi7XmOcM6eE5UeguDuNCPKn39K0jnz%2B72goeey37Ax2FxSYCPOlz42afgOvl55UYY0BqM6ycG5a7ND90YUGZeS%2FBsY5xIlpHOPYKoc7C%2FpbX6lwXfxo3vzJtVVcb9Rw6WI66UDu%2FwVQBdBmw81mXf4NCxtbxKSmeCHSNoOs63o8cjkEReQLOWkonxxfuyPl02UAH7fJ1n9AglDmHofpgUz1n8nKM5%2Bb8LoCIdWmqjmEkw4RjQBJKKg2M2EQGv2%2F5AAvxM5Vd5%2BqEIIMsGGHYweDjTESNO3Kte23KhxSzksmwUBNu1eeMg4ixoG8jK4%2BOHAUh65%2F%2Fc4LKtHPtoBl2%2BWRktTIBvuGdbHoOZqptgq%2B9oV1X3hC2Pqj1S2Gxhx%2FsXLfQFaN6LGpOtLyyCcDEtDxEO7cpKmhN9q2ZO7ifrNvhDv%2Bw7MeZgMgJeR0n7sVwIoWyv1KYUMlOnw2q45dtWD3%2FFrDNjVTReFGw0upFiZygnNnFeaPoYMKyUqckGOqUBp%2F%2FoozPMMTTYfM75SamYVOthQ26gBb7SelGaBYa704p57GaJhwIT9aRSBJhZkYruJ1G2Bt04KSk4nsIcsOnEqStH9q8LbmM2uKq09%2BJ0aMEqvacVcsupOfT2qklnL8iVjIzazWXcMMf6aHhPgE9ReQAEnotgDLoRWKyysANTFKY6dEMHKtG2iU8i7lNaN2naV%2BflFURq%2BYqOiPHuVwoX44TmBvao&X-Amz-Signature=e3a1a4fcec373b220a570a0e131bae2c1118a8de5b46dc6fe90faea5dd3f7f49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SECXWHVV%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKtEEE5G8CS62uX1%2BYfI6c0X82ez10ENAffnSN2WSQcAiEA%2BKm3yshKsqaGk2%2FcwAgf2f6rUKVrjx6wKiC7KkZU7SEqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKr0EI%2B5hlAtPTS%2FMCrcA4TD%2FGK%2BdtHCcgiM9fIkc4FMTZFaUJWCZxKU8L%2BHSwBXDY28Ofjgf19eLIcP8d10GE8btGJk2XAlVqnFtwU1sxO%2FEGG4VX%2BGto20tizMOrCsFbrRyVNuE1ns5GoFJFPoVD1EOUSZi7XmOcM6eE5UeguDuNCPKn39K0jnz%2B72goeey37Ax2FxSYCPOlz42afgOvl55UYY0BqM6ycG5a7ND90YUGZeS%2FBsY5xIlpHOPYKoc7C%2FpbX6lwXfxo3vzJtVVcb9Rw6WI66UDu%2FwVQBdBmw81mXf4NCxtbxKSmeCHSNoOs63o8cjkEReQLOWkonxxfuyPl02UAH7fJ1n9AglDmHofpgUz1n8nKM5%2Bb8LoCIdWmqjmEkw4RjQBJKKg2M2EQGv2%2F5AAvxM5Vd5%2BqEIIMsGGHYweDjTESNO3Kte23KhxSzksmwUBNu1eeMg4ixoG8jK4%2BOHAUh65%2F%2Fc4LKtHPtoBl2%2BWRktTIBvuGdbHoOZqptgq%2B9oV1X3hC2Pqj1S2Gxhx%2FsXLfQFaN6LGpOtLyyCcDEtDxEO7cpKmhN9q2ZO7ifrNvhDv%2Bw7MeZgMgJeR0n7sVwIoWyv1KYUMlOnw2q45dtWD3%2FFrDNjVTReFGw0upFiZygnNnFeaPoYMKyUqckGOqUBp%2F%2FoozPMMTTYfM75SamYVOthQ26gBb7SelGaBYa704p57GaJhwIT9aRSBJhZkYruJ1G2Bt04KSk4nsIcsOnEqStH9q8LbmM2uKq09%2BJ0aMEqvacVcsupOfT2qklnL8iVjIzazWXcMMf6aHhPgE9ReQAEnotgDLoRWKyysANTFKY6dEMHKtG2iU8i7lNaN2naV%2BflFURq%2BYqOiPHuVwoX44TmBvao&X-Amz-Signature=5ab850d18ce3dec93c0c7d6c2f8d41e0dfe3b7f81351184697b940171a2ed968&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

