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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4PTXP%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMDja7JdrZylV8VAz0tScyrexgvtLG03O1DbdJxSjuoAiB%2B7X4Ly9Io1H7sDF%2BZXCH2oBje0k9%2FXEW0Pfv1rFKsNSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM2h7%2F7fg4JJ%2F3OOo%2BKtwD0wngmfBaCDN%2Fk5lOswR9LU4%2B36e2w1hfRq%2BLLVKCHdag9UJ8ewOgSye2mciYLi2z8H9uv9%2BVNinnDbqsg0heescUrHFW%2FmnCzZhJs4pMvyzBl58EWmkmUbzQnMuviPz067UMyHF7p%2FLb7Q8107dZ0cR1hjtoxm3a1%2BnrvWsMLCyAybvcVer1yEGDA5mkPSiXRQVTTM95tk8TBJCZA0DrdBD%2BiVdNypLIUZcv5OvaJsY1nDCjv%2BEOMNKyaFa8WaJMtZxSsChhMziNhYHKG%2FuhhKEeKEV1t4wEhioiAeOmriRXn1c7wkoNapDWRCS4ioOYhqn5zzS024vglYRc5FEcgKs2YXrggSNGh80NOpIb%2B9S4o9UsrVEp6p%2FXR3XwUEfjtJIl%2B164%2BYPNWDopEGs6eSpp%2FF8EdXRU27lUIQgopEtGCiNWhfQ3A1koG0XkL7pd13CRHjAKQYY1iRnhNLmqLn8vhIvN%2F0eQpGypcXKhDshA8sXfDi0tm57RBnVBh9MGRfKMxS2j6EzyX5EPegqPw6P74N9VFRM5SoX4a6w0RbXE%2FcsKBErTPYcbBC2yaHB3119LRV4R806cF0BS6B3RsgpI9kjuRiHbhbLNaXqyrC5liE7ILci%2Be0h4HGwwyrDxzgY6pgF%2Fx4oxl42HH3KZ6rQg8EWnpeLMA5W0iYOkjRC%2Ff%2FqieTYlWau%2BlAQBMZjj%2FYRNBnO7T9kZKtyZWz0JP5MewC3KC%2Film4rhqi%2B11gK2R0u8ETzb9tu6exsHbpJahMsyYSg%2B5anu3yqPABi%2Fs67Gha6ky2wjRlf397W4It8Tvjv9OeVMR3P7Ky9AWSXwgyOkzAN1%2FElLS7jElDjtxU94OsNnQ%2FRqGisZ&X-Amz-Signature=1c97c20409acd6babe6d8476df7bd194a57808be9703e89401f003bc2647c05f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4PTXP%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMDja7JdrZylV8VAz0tScyrexgvtLG03O1DbdJxSjuoAiB%2B7X4Ly9Io1H7sDF%2BZXCH2oBje0k9%2FXEW0Pfv1rFKsNSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM2h7%2F7fg4JJ%2F3OOo%2BKtwD0wngmfBaCDN%2Fk5lOswR9LU4%2B36e2w1hfRq%2BLLVKCHdag9UJ8ewOgSye2mciYLi2z8H9uv9%2BVNinnDbqsg0heescUrHFW%2FmnCzZhJs4pMvyzBl58EWmkmUbzQnMuviPz067UMyHF7p%2FLb7Q8107dZ0cR1hjtoxm3a1%2BnrvWsMLCyAybvcVer1yEGDA5mkPSiXRQVTTM95tk8TBJCZA0DrdBD%2BiVdNypLIUZcv5OvaJsY1nDCjv%2BEOMNKyaFa8WaJMtZxSsChhMziNhYHKG%2FuhhKEeKEV1t4wEhioiAeOmriRXn1c7wkoNapDWRCS4ioOYhqn5zzS024vglYRc5FEcgKs2YXrggSNGh80NOpIb%2B9S4o9UsrVEp6p%2FXR3XwUEfjtJIl%2B164%2BYPNWDopEGs6eSpp%2FF8EdXRU27lUIQgopEtGCiNWhfQ3A1koG0XkL7pd13CRHjAKQYY1iRnhNLmqLn8vhIvN%2F0eQpGypcXKhDshA8sXfDi0tm57RBnVBh9MGRfKMxS2j6EzyX5EPegqPw6P74N9VFRM5SoX4a6w0RbXE%2FcsKBErTPYcbBC2yaHB3119LRV4R806cF0BS6B3RsgpI9kjuRiHbhbLNaXqyrC5liE7ILci%2Be0h4HGwwyrDxzgY6pgF%2Fx4oxl42HH3KZ6rQg8EWnpeLMA5W0iYOkjRC%2Ff%2FqieTYlWau%2BlAQBMZjj%2FYRNBnO7T9kZKtyZWz0JP5MewC3KC%2Film4rhqi%2B11gK2R0u8ETzb9tu6exsHbpJahMsyYSg%2B5anu3yqPABi%2Fs67Gha6ky2wjRlf397W4It8Tvjv9OeVMR3P7Ky9AWSXwgyOkzAN1%2FElLS7jElDjtxU94OsNnQ%2FRqGisZ&X-Amz-Signature=a128d5849b0f1c0b227a755e0d4a5158a323e84df73dfe5f882e966ef1ef7b86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4PTXP%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMDja7JdrZylV8VAz0tScyrexgvtLG03O1DbdJxSjuoAiB%2B7X4Ly9Io1H7sDF%2BZXCH2oBje0k9%2FXEW0Pfv1rFKsNSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM2h7%2F7fg4JJ%2F3OOo%2BKtwD0wngmfBaCDN%2Fk5lOswR9LU4%2B36e2w1hfRq%2BLLVKCHdag9UJ8ewOgSye2mciYLi2z8H9uv9%2BVNinnDbqsg0heescUrHFW%2FmnCzZhJs4pMvyzBl58EWmkmUbzQnMuviPz067UMyHF7p%2FLb7Q8107dZ0cR1hjtoxm3a1%2BnrvWsMLCyAybvcVer1yEGDA5mkPSiXRQVTTM95tk8TBJCZA0DrdBD%2BiVdNypLIUZcv5OvaJsY1nDCjv%2BEOMNKyaFa8WaJMtZxSsChhMziNhYHKG%2FuhhKEeKEV1t4wEhioiAeOmriRXn1c7wkoNapDWRCS4ioOYhqn5zzS024vglYRc5FEcgKs2YXrggSNGh80NOpIb%2B9S4o9UsrVEp6p%2FXR3XwUEfjtJIl%2B164%2BYPNWDopEGs6eSpp%2FF8EdXRU27lUIQgopEtGCiNWhfQ3A1koG0XkL7pd13CRHjAKQYY1iRnhNLmqLn8vhIvN%2F0eQpGypcXKhDshA8sXfDi0tm57RBnVBh9MGRfKMxS2j6EzyX5EPegqPw6P74N9VFRM5SoX4a6w0RbXE%2FcsKBErTPYcbBC2yaHB3119LRV4R806cF0BS6B3RsgpI9kjuRiHbhbLNaXqyrC5liE7ILci%2Be0h4HGwwyrDxzgY6pgF%2Fx4oxl42HH3KZ6rQg8EWnpeLMA5W0iYOkjRC%2Ff%2FqieTYlWau%2BlAQBMZjj%2FYRNBnO7T9kZKtyZWz0JP5MewC3KC%2Film4rhqi%2B11gK2R0u8ETzb9tu6exsHbpJahMsyYSg%2B5anu3yqPABi%2Fs67Gha6ky2wjRlf397W4It8Tvjv9OeVMR3P7Ky9AWSXwgyOkzAN1%2FElLS7jElDjtxU94OsNnQ%2FRqGisZ&X-Amz-Signature=948386868741bf2d31861aa3e1f6957d842afb8d8fa8a04afa3e5ee0d24eb931&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4PTXP%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMDja7JdrZylV8VAz0tScyrexgvtLG03O1DbdJxSjuoAiB%2B7X4Ly9Io1H7sDF%2BZXCH2oBje0k9%2FXEW0Pfv1rFKsNSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM2h7%2F7fg4JJ%2F3OOo%2BKtwD0wngmfBaCDN%2Fk5lOswR9LU4%2B36e2w1hfRq%2BLLVKCHdag9UJ8ewOgSye2mciYLi2z8H9uv9%2BVNinnDbqsg0heescUrHFW%2FmnCzZhJs4pMvyzBl58EWmkmUbzQnMuviPz067UMyHF7p%2FLb7Q8107dZ0cR1hjtoxm3a1%2BnrvWsMLCyAybvcVer1yEGDA5mkPSiXRQVTTM95tk8TBJCZA0DrdBD%2BiVdNypLIUZcv5OvaJsY1nDCjv%2BEOMNKyaFa8WaJMtZxSsChhMziNhYHKG%2FuhhKEeKEV1t4wEhioiAeOmriRXn1c7wkoNapDWRCS4ioOYhqn5zzS024vglYRc5FEcgKs2YXrggSNGh80NOpIb%2B9S4o9UsrVEp6p%2FXR3XwUEfjtJIl%2B164%2BYPNWDopEGs6eSpp%2FF8EdXRU27lUIQgopEtGCiNWhfQ3A1koG0XkL7pd13CRHjAKQYY1iRnhNLmqLn8vhIvN%2F0eQpGypcXKhDshA8sXfDi0tm57RBnVBh9MGRfKMxS2j6EzyX5EPegqPw6P74N9VFRM5SoX4a6w0RbXE%2FcsKBErTPYcbBC2yaHB3119LRV4R806cF0BS6B3RsgpI9kjuRiHbhbLNaXqyrC5liE7ILci%2Be0h4HGwwyrDxzgY6pgF%2Fx4oxl42HH3KZ6rQg8EWnpeLMA5W0iYOkjRC%2Ff%2FqieTYlWau%2BlAQBMZjj%2FYRNBnO7T9kZKtyZWz0JP5MewC3KC%2Film4rhqi%2B11gK2R0u8ETzb9tu6exsHbpJahMsyYSg%2B5anu3yqPABi%2Fs67Gha6ky2wjRlf397W4It8Tvjv9OeVMR3P7Ky9AWSXwgyOkzAN1%2FElLS7jElDjtxU94OsNnQ%2FRqGisZ&X-Amz-Signature=e35f3b084328cd32d94e021e42519f705597890a0fc269e58ff87fed82c6079c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4PTXP%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMDja7JdrZylV8VAz0tScyrexgvtLG03O1DbdJxSjuoAiB%2B7X4Ly9Io1H7sDF%2BZXCH2oBje0k9%2FXEW0Pfv1rFKsNSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM2h7%2F7fg4JJ%2F3OOo%2BKtwD0wngmfBaCDN%2Fk5lOswR9LU4%2B36e2w1hfRq%2BLLVKCHdag9UJ8ewOgSye2mciYLi2z8H9uv9%2BVNinnDbqsg0heescUrHFW%2FmnCzZhJs4pMvyzBl58EWmkmUbzQnMuviPz067UMyHF7p%2FLb7Q8107dZ0cR1hjtoxm3a1%2BnrvWsMLCyAybvcVer1yEGDA5mkPSiXRQVTTM95tk8TBJCZA0DrdBD%2BiVdNypLIUZcv5OvaJsY1nDCjv%2BEOMNKyaFa8WaJMtZxSsChhMziNhYHKG%2FuhhKEeKEV1t4wEhioiAeOmriRXn1c7wkoNapDWRCS4ioOYhqn5zzS024vglYRc5FEcgKs2YXrggSNGh80NOpIb%2B9S4o9UsrVEp6p%2FXR3XwUEfjtJIl%2B164%2BYPNWDopEGs6eSpp%2FF8EdXRU27lUIQgopEtGCiNWhfQ3A1koG0XkL7pd13CRHjAKQYY1iRnhNLmqLn8vhIvN%2F0eQpGypcXKhDshA8sXfDi0tm57RBnVBh9MGRfKMxS2j6EzyX5EPegqPw6P74N9VFRM5SoX4a6w0RbXE%2FcsKBErTPYcbBC2yaHB3119LRV4R806cF0BS6B3RsgpI9kjuRiHbhbLNaXqyrC5liE7ILci%2Be0h4HGwwyrDxzgY6pgF%2Fx4oxl42HH3KZ6rQg8EWnpeLMA5W0iYOkjRC%2Ff%2FqieTYlWau%2BlAQBMZjj%2FYRNBnO7T9kZKtyZWz0JP5MewC3KC%2Film4rhqi%2B11gK2R0u8ETzb9tu6exsHbpJahMsyYSg%2B5anu3yqPABi%2Fs67Gha6ky2wjRlf397W4It8Tvjv9OeVMR3P7Ky9AWSXwgyOkzAN1%2FElLS7jElDjtxU94OsNnQ%2FRqGisZ&X-Amz-Signature=5a796a52e480fd0ad24586930fc1306f1fb0c31cb74fac2a2070e04a26a6a4de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4PTXP%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMDja7JdrZylV8VAz0tScyrexgvtLG03O1DbdJxSjuoAiB%2B7X4Ly9Io1H7sDF%2BZXCH2oBje0k9%2FXEW0Pfv1rFKsNSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM2h7%2F7fg4JJ%2F3OOo%2BKtwD0wngmfBaCDN%2Fk5lOswR9LU4%2B36e2w1hfRq%2BLLVKCHdag9UJ8ewOgSye2mciYLi2z8H9uv9%2BVNinnDbqsg0heescUrHFW%2FmnCzZhJs4pMvyzBl58EWmkmUbzQnMuviPz067UMyHF7p%2FLb7Q8107dZ0cR1hjtoxm3a1%2BnrvWsMLCyAybvcVer1yEGDA5mkPSiXRQVTTM95tk8TBJCZA0DrdBD%2BiVdNypLIUZcv5OvaJsY1nDCjv%2BEOMNKyaFa8WaJMtZxSsChhMziNhYHKG%2FuhhKEeKEV1t4wEhioiAeOmriRXn1c7wkoNapDWRCS4ioOYhqn5zzS024vglYRc5FEcgKs2YXrggSNGh80NOpIb%2B9S4o9UsrVEp6p%2FXR3XwUEfjtJIl%2B164%2BYPNWDopEGs6eSpp%2FF8EdXRU27lUIQgopEtGCiNWhfQ3A1koG0XkL7pd13CRHjAKQYY1iRnhNLmqLn8vhIvN%2F0eQpGypcXKhDshA8sXfDi0tm57RBnVBh9MGRfKMxS2j6EzyX5EPegqPw6P74N9VFRM5SoX4a6w0RbXE%2FcsKBErTPYcbBC2yaHB3119LRV4R806cF0BS6B3RsgpI9kjuRiHbhbLNaXqyrC5liE7ILci%2Be0h4HGwwyrDxzgY6pgF%2Fx4oxl42HH3KZ6rQg8EWnpeLMA5W0iYOkjRC%2Ff%2FqieTYlWau%2BlAQBMZjj%2FYRNBnO7T9kZKtyZWz0JP5MewC3KC%2Film4rhqi%2B11gK2R0u8ETzb9tu6exsHbpJahMsyYSg%2B5anu3yqPABi%2Fs67Gha6ky2wjRlf397W4It8Tvjv9OeVMR3P7Ky9AWSXwgyOkzAN1%2FElLS7jElDjtxU94OsNnQ%2FRqGisZ&X-Amz-Signature=d570e56a85caf840d5ac5c5c9217b0bc970246570885ec8f447a542e24ef9354&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4PTXP%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMDja7JdrZylV8VAz0tScyrexgvtLG03O1DbdJxSjuoAiB%2B7X4Ly9Io1H7sDF%2BZXCH2oBje0k9%2FXEW0Pfv1rFKsNSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM2h7%2F7fg4JJ%2F3OOo%2BKtwD0wngmfBaCDN%2Fk5lOswR9LU4%2B36e2w1hfRq%2BLLVKCHdag9UJ8ewOgSye2mciYLi2z8H9uv9%2BVNinnDbqsg0heescUrHFW%2FmnCzZhJs4pMvyzBl58EWmkmUbzQnMuviPz067UMyHF7p%2FLb7Q8107dZ0cR1hjtoxm3a1%2BnrvWsMLCyAybvcVer1yEGDA5mkPSiXRQVTTM95tk8TBJCZA0DrdBD%2BiVdNypLIUZcv5OvaJsY1nDCjv%2BEOMNKyaFa8WaJMtZxSsChhMziNhYHKG%2FuhhKEeKEV1t4wEhioiAeOmriRXn1c7wkoNapDWRCS4ioOYhqn5zzS024vglYRc5FEcgKs2YXrggSNGh80NOpIb%2B9S4o9UsrVEp6p%2FXR3XwUEfjtJIl%2B164%2BYPNWDopEGs6eSpp%2FF8EdXRU27lUIQgopEtGCiNWhfQ3A1koG0XkL7pd13CRHjAKQYY1iRnhNLmqLn8vhIvN%2F0eQpGypcXKhDshA8sXfDi0tm57RBnVBh9MGRfKMxS2j6EzyX5EPegqPw6P74N9VFRM5SoX4a6w0RbXE%2FcsKBErTPYcbBC2yaHB3119LRV4R806cF0BS6B3RsgpI9kjuRiHbhbLNaXqyrC5liE7ILci%2Be0h4HGwwyrDxzgY6pgF%2Fx4oxl42HH3KZ6rQg8EWnpeLMA5W0iYOkjRC%2Ff%2FqieTYlWau%2BlAQBMZjj%2FYRNBnO7T9kZKtyZWz0JP5MewC3KC%2Film4rhqi%2B11gK2R0u8ETzb9tu6exsHbpJahMsyYSg%2B5anu3yqPABi%2Fs67Gha6ky2wjRlf397W4It8Tvjv9OeVMR3P7Ky9AWSXwgyOkzAN1%2FElLS7jElDjtxU94OsNnQ%2FRqGisZ&X-Amz-Signature=29421cfdea8ce44d4e1c8715d564ea63e1c499e335ac4ed18f0876ced6479c05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4PTXP%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMDja7JdrZylV8VAz0tScyrexgvtLG03O1DbdJxSjuoAiB%2B7X4Ly9Io1H7sDF%2BZXCH2oBje0k9%2FXEW0Pfv1rFKsNSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM2h7%2F7fg4JJ%2F3OOo%2BKtwD0wngmfBaCDN%2Fk5lOswR9LU4%2B36e2w1hfRq%2BLLVKCHdag9UJ8ewOgSye2mciYLi2z8H9uv9%2BVNinnDbqsg0heescUrHFW%2FmnCzZhJs4pMvyzBl58EWmkmUbzQnMuviPz067UMyHF7p%2FLb7Q8107dZ0cR1hjtoxm3a1%2BnrvWsMLCyAybvcVer1yEGDA5mkPSiXRQVTTM95tk8TBJCZA0DrdBD%2BiVdNypLIUZcv5OvaJsY1nDCjv%2BEOMNKyaFa8WaJMtZxSsChhMziNhYHKG%2FuhhKEeKEV1t4wEhioiAeOmriRXn1c7wkoNapDWRCS4ioOYhqn5zzS024vglYRc5FEcgKs2YXrggSNGh80NOpIb%2B9S4o9UsrVEp6p%2FXR3XwUEfjtJIl%2B164%2BYPNWDopEGs6eSpp%2FF8EdXRU27lUIQgopEtGCiNWhfQ3A1koG0XkL7pd13CRHjAKQYY1iRnhNLmqLn8vhIvN%2F0eQpGypcXKhDshA8sXfDi0tm57RBnVBh9MGRfKMxS2j6EzyX5EPegqPw6P74N9VFRM5SoX4a6w0RbXE%2FcsKBErTPYcbBC2yaHB3119LRV4R806cF0BS6B3RsgpI9kjuRiHbhbLNaXqyrC5liE7ILci%2Be0h4HGwwyrDxzgY6pgF%2Fx4oxl42HH3KZ6rQg8EWnpeLMA5W0iYOkjRC%2Ff%2FqieTYlWau%2BlAQBMZjj%2FYRNBnO7T9kZKtyZWz0JP5MewC3KC%2Film4rhqi%2B11gK2R0u8ETzb9tu6exsHbpJahMsyYSg%2B5anu3yqPABi%2Fs67Gha6ky2wjRlf397W4It8Tvjv9OeVMR3P7Ky9AWSXwgyOkzAN1%2FElLS7jElDjtxU94OsNnQ%2FRqGisZ&X-Amz-Signature=c3559100995fc4375d1421e89183134fba1dc7c6a07995041e101db5a7b0e4a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4PTXP%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMDja7JdrZylV8VAz0tScyrexgvtLG03O1DbdJxSjuoAiB%2B7X4Ly9Io1H7sDF%2BZXCH2oBje0k9%2FXEW0Pfv1rFKsNSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM2h7%2F7fg4JJ%2F3OOo%2BKtwD0wngmfBaCDN%2Fk5lOswR9LU4%2B36e2w1hfRq%2BLLVKCHdag9UJ8ewOgSye2mciYLi2z8H9uv9%2BVNinnDbqsg0heescUrHFW%2FmnCzZhJs4pMvyzBl58EWmkmUbzQnMuviPz067UMyHF7p%2FLb7Q8107dZ0cR1hjtoxm3a1%2BnrvWsMLCyAybvcVer1yEGDA5mkPSiXRQVTTM95tk8TBJCZA0DrdBD%2BiVdNypLIUZcv5OvaJsY1nDCjv%2BEOMNKyaFa8WaJMtZxSsChhMziNhYHKG%2FuhhKEeKEV1t4wEhioiAeOmriRXn1c7wkoNapDWRCS4ioOYhqn5zzS024vglYRc5FEcgKs2YXrggSNGh80NOpIb%2B9S4o9UsrVEp6p%2FXR3XwUEfjtJIl%2B164%2BYPNWDopEGs6eSpp%2FF8EdXRU27lUIQgopEtGCiNWhfQ3A1koG0XkL7pd13CRHjAKQYY1iRnhNLmqLn8vhIvN%2F0eQpGypcXKhDshA8sXfDi0tm57RBnVBh9MGRfKMxS2j6EzyX5EPegqPw6P74N9VFRM5SoX4a6w0RbXE%2FcsKBErTPYcbBC2yaHB3119LRV4R806cF0BS6B3RsgpI9kjuRiHbhbLNaXqyrC5liE7ILci%2Be0h4HGwwyrDxzgY6pgF%2Fx4oxl42HH3KZ6rQg8EWnpeLMA5W0iYOkjRC%2Ff%2FqieTYlWau%2BlAQBMZjj%2FYRNBnO7T9kZKtyZWz0JP5MewC3KC%2Film4rhqi%2B11gK2R0u8ETzb9tu6exsHbpJahMsyYSg%2B5anu3yqPABi%2Fs67Gha6ky2wjRlf397W4It8Tvjv9OeVMR3P7Ky9AWSXwgyOkzAN1%2FElLS7jElDjtxU94OsNnQ%2FRqGisZ&X-Amz-Signature=3a88da38f6e33e58b1f61cfe33e5c2eb3e0ae1bf7d13806a6904af5b3a6cb8a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677T4PTXP%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMDja7JdrZylV8VAz0tScyrexgvtLG03O1DbdJxSjuoAiB%2B7X4Ly9Io1H7sDF%2BZXCH2oBje0k9%2FXEW0Pfv1rFKsNSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIM2h7%2F7fg4JJ%2F3OOo%2BKtwD0wngmfBaCDN%2Fk5lOswR9LU4%2B36e2w1hfRq%2BLLVKCHdag9UJ8ewOgSye2mciYLi2z8H9uv9%2BVNinnDbqsg0heescUrHFW%2FmnCzZhJs4pMvyzBl58EWmkmUbzQnMuviPz067UMyHF7p%2FLb7Q8107dZ0cR1hjtoxm3a1%2BnrvWsMLCyAybvcVer1yEGDA5mkPSiXRQVTTM95tk8TBJCZA0DrdBD%2BiVdNypLIUZcv5OvaJsY1nDCjv%2BEOMNKyaFa8WaJMtZxSsChhMziNhYHKG%2FuhhKEeKEV1t4wEhioiAeOmriRXn1c7wkoNapDWRCS4ioOYhqn5zzS024vglYRc5FEcgKs2YXrggSNGh80NOpIb%2B9S4o9UsrVEp6p%2FXR3XwUEfjtJIl%2B164%2BYPNWDopEGs6eSpp%2FF8EdXRU27lUIQgopEtGCiNWhfQ3A1koG0XkL7pd13CRHjAKQYY1iRnhNLmqLn8vhIvN%2F0eQpGypcXKhDshA8sXfDi0tm57RBnVBh9MGRfKMxS2j6EzyX5EPegqPw6P74N9VFRM5SoX4a6w0RbXE%2FcsKBErTPYcbBC2yaHB3119LRV4R806cF0BS6B3RsgpI9kjuRiHbhbLNaXqyrC5liE7ILci%2Be0h4HGwwyrDxzgY6pgF%2Fx4oxl42HH3KZ6rQg8EWnpeLMA5W0iYOkjRC%2Ff%2FqieTYlWau%2BlAQBMZjj%2FYRNBnO7T9kZKtyZWz0JP5MewC3KC%2Film4rhqi%2B11gK2R0u8ETzb9tu6exsHbpJahMsyYSg%2B5anu3yqPABi%2Fs67Gha6ky2wjRlf397W4It8Tvjv9OeVMR3P7Ky9AWSXwgyOkzAN1%2FElLS7jElDjtxU94OsNnQ%2FRqGisZ&X-Amz-Signature=ea7d5baebb411b9a36dd43e6b8b35698901bf35e154ddc6f0b77bc1bb644d96b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

