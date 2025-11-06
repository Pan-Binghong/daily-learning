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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROHO6O2L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8kQJsc15LKKrF5%2FLYCcsH%2B21tVZzPDVNIqMeYzcAoHAiBeIksitvi%2BGuEjG52VqM3lP%2FiNY9H3row1paPDr%2BzDUSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0P2sr%2Fv3UphVJ94eKtwDHVMbM6YuTAbe7PDYEdkW4IkFDBnRJHkHr2yxcV8YbW7Z6u27D%2FaB5hg3Xp98Bga42vBHxTSJH%2FJgBf4A66WGK4f6kwLm8skTFkcnctij0BrddhASgVCyk7wq8zqFBgTBfXhzk4kd6C9FIWtQSyrw8xSKg1tVN5osZHyt%2BdSB3aeA04Az%2BGFXAn1RK4%2Fem0ZgXtfFPYcssd12pv9tUWSVLiKZCTNYZJoYK6Uo5b1fRXKneq%2Bkn4SoFCjCRUJ5i0EaEsiy%2BBk1Ab60HDiKhO4XhzMkUQqRbj8h6oEPQF4HLjrfnz97ESfT%2BzpAtCcbRjCO9uNut%2F98bYMPczUyywJYoTLAMyxI9gGUA5tC3K0vkTfYNIQRruyKowvYDIffL15fpYkHm97nf69tr1aTgTIOpMwtTXokB0sai8nzwcdPgunOStcOl%2BzAO%2F%2Bd8CzMwfK5Sfw01eHIoMD%2FucY1dv1sdaEX231lD7O%2ByawoBHJMhjOXpMNVBaxzJ384Cml84Co%2F68wRxpSa%2FYOXm1UIuTZ7vauF8hpXCePJvn9epV9QpljtLlYAuuxEIIXPXpyP8w87nuc8CG2jlml9PBHv7FARcCR59YofOQtdJ2HEnIF8etWx88umeAdPd8pfjqYw3fCvyAY6pgGlh%2FHgouT6n6X12Q9SH0Tk5CJAqkFbssLShddj7B63pCJki5ylAA39b369L8Co5yA%2FXxXRq4PIsxsM6U7JrlHCuSpg4h2YfLfl2Ywb8Nlo%2F8aMtWe8NI7AKyT1hQQ%2BZgmXdjh0OX8tUhbr72pAg8thikzExgqPJM4D8ILc7ToXj7dzHrwqHUV9kh5Xo0ncFhRnLFA%2FHrY%2B%2BRafQLcnocm4C%2Fpu4GGJ&X-Amz-Signature=ad674af4c773a749d2654dea0d2af455cd649164ec05d1b5b9b82a06a0381220&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROHO6O2L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8kQJsc15LKKrF5%2FLYCcsH%2B21tVZzPDVNIqMeYzcAoHAiBeIksitvi%2BGuEjG52VqM3lP%2FiNY9H3row1paPDr%2BzDUSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0P2sr%2Fv3UphVJ94eKtwDHVMbM6YuTAbe7PDYEdkW4IkFDBnRJHkHr2yxcV8YbW7Z6u27D%2FaB5hg3Xp98Bga42vBHxTSJH%2FJgBf4A66WGK4f6kwLm8skTFkcnctij0BrddhASgVCyk7wq8zqFBgTBfXhzk4kd6C9FIWtQSyrw8xSKg1tVN5osZHyt%2BdSB3aeA04Az%2BGFXAn1RK4%2Fem0ZgXtfFPYcssd12pv9tUWSVLiKZCTNYZJoYK6Uo5b1fRXKneq%2Bkn4SoFCjCRUJ5i0EaEsiy%2BBk1Ab60HDiKhO4XhzMkUQqRbj8h6oEPQF4HLjrfnz97ESfT%2BzpAtCcbRjCO9uNut%2F98bYMPczUyywJYoTLAMyxI9gGUA5tC3K0vkTfYNIQRruyKowvYDIffL15fpYkHm97nf69tr1aTgTIOpMwtTXokB0sai8nzwcdPgunOStcOl%2BzAO%2F%2Bd8CzMwfK5Sfw01eHIoMD%2FucY1dv1sdaEX231lD7O%2ByawoBHJMhjOXpMNVBaxzJ384Cml84Co%2F68wRxpSa%2FYOXm1UIuTZ7vauF8hpXCePJvn9epV9QpljtLlYAuuxEIIXPXpyP8w87nuc8CG2jlml9PBHv7FARcCR59YofOQtdJ2HEnIF8etWx88umeAdPd8pfjqYw3fCvyAY6pgGlh%2FHgouT6n6X12Q9SH0Tk5CJAqkFbssLShddj7B63pCJki5ylAA39b369L8Co5yA%2FXxXRq4PIsxsM6U7JrlHCuSpg4h2YfLfl2Ywb8Nlo%2F8aMtWe8NI7AKyT1hQQ%2BZgmXdjh0OX8tUhbr72pAg8thikzExgqPJM4D8ILc7ToXj7dzHrwqHUV9kh5Xo0ncFhRnLFA%2FHrY%2B%2BRafQLcnocm4C%2Fpu4GGJ&X-Amz-Signature=1af2cd6421867e240036eb6259f025becbe1de9f80d61011f2c73a229cc3bec1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROHO6O2L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8kQJsc15LKKrF5%2FLYCcsH%2B21tVZzPDVNIqMeYzcAoHAiBeIksitvi%2BGuEjG52VqM3lP%2FiNY9H3row1paPDr%2BzDUSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0P2sr%2Fv3UphVJ94eKtwDHVMbM6YuTAbe7PDYEdkW4IkFDBnRJHkHr2yxcV8YbW7Z6u27D%2FaB5hg3Xp98Bga42vBHxTSJH%2FJgBf4A66WGK4f6kwLm8skTFkcnctij0BrddhASgVCyk7wq8zqFBgTBfXhzk4kd6C9FIWtQSyrw8xSKg1tVN5osZHyt%2BdSB3aeA04Az%2BGFXAn1RK4%2Fem0ZgXtfFPYcssd12pv9tUWSVLiKZCTNYZJoYK6Uo5b1fRXKneq%2Bkn4SoFCjCRUJ5i0EaEsiy%2BBk1Ab60HDiKhO4XhzMkUQqRbj8h6oEPQF4HLjrfnz97ESfT%2BzpAtCcbRjCO9uNut%2F98bYMPczUyywJYoTLAMyxI9gGUA5tC3K0vkTfYNIQRruyKowvYDIffL15fpYkHm97nf69tr1aTgTIOpMwtTXokB0sai8nzwcdPgunOStcOl%2BzAO%2F%2Bd8CzMwfK5Sfw01eHIoMD%2FucY1dv1sdaEX231lD7O%2ByawoBHJMhjOXpMNVBaxzJ384Cml84Co%2F68wRxpSa%2FYOXm1UIuTZ7vauF8hpXCePJvn9epV9QpljtLlYAuuxEIIXPXpyP8w87nuc8CG2jlml9PBHv7FARcCR59YofOQtdJ2HEnIF8etWx88umeAdPd8pfjqYw3fCvyAY6pgGlh%2FHgouT6n6X12Q9SH0Tk5CJAqkFbssLShddj7B63pCJki5ylAA39b369L8Co5yA%2FXxXRq4PIsxsM6U7JrlHCuSpg4h2YfLfl2Ywb8Nlo%2F8aMtWe8NI7AKyT1hQQ%2BZgmXdjh0OX8tUhbr72pAg8thikzExgqPJM4D8ILc7ToXj7dzHrwqHUV9kh5Xo0ncFhRnLFA%2FHrY%2B%2BRafQLcnocm4C%2Fpu4GGJ&X-Amz-Signature=1045bd8141212223923c82bb82a488598c8d0b556eef4492699a7c4a69ed1d97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROHO6O2L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8kQJsc15LKKrF5%2FLYCcsH%2B21tVZzPDVNIqMeYzcAoHAiBeIksitvi%2BGuEjG52VqM3lP%2FiNY9H3row1paPDr%2BzDUSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0P2sr%2Fv3UphVJ94eKtwDHVMbM6YuTAbe7PDYEdkW4IkFDBnRJHkHr2yxcV8YbW7Z6u27D%2FaB5hg3Xp98Bga42vBHxTSJH%2FJgBf4A66WGK4f6kwLm8skTFkcnctij0BrddhASgVCyk7wq8zqFBgTBfXhzk4kd6C9FIWtQSyrw8xSKg1tVN5osZHyt%2BdSB3aeA04Az%2BGFXAn1RK4%2Fem0ZgXtfFPYcssd12pv9tUWSVLiKZCTNYZJoYK6Uo5b1fRXKneq%2Bkn4SoFCjCRUJ5i0EaEsiy%2BBk1Ab60HDiKhO4XhzMkUQqRbj8h6oEPQF4HLjrfnz97ESfT%2BzpAtCcbRjCO9uNut%2F98bYMPczUyywJYoTLAMyxI9gGUA5tC3K0vkTfYNIQRruyKowvYDIffL15fpYkHm97nf69tr1aTgTIOpMwtTXokB0sai8nzwcdPgunOStcOl%2BzAO%2F%2Bd8CzMwfK5Sfw01eHIoMD%2FucY1dv1sdaEX231lD7O%2ByawoBHJMhjOXpMNVBaxzJ384Cml84Co%2F68wRxpSa%2FYOXm1UIuTZ7vauF8hpXCePJvn9epV9QpljtLlYAuuxEIIXPXpyP8w87nuc8CG2jlml9PBHv7FARcCR59YofOQtdJ2HEnIF8etWx88umeAdPd8pfjqYw3fCvyAY6pgGlh%2FHgouT6n6X12Q9SH0Tk5CJAqkFbssLShddj7B63pCJki5ylAA39b369L8Co5yA%2FXxXRq4PIsxsM6U7JrlHCuSpg4h2YfLfl2Ywb8Nlo%2F8aMtWe8NI7AKyT1hQQ%2BZgmXdjh0OX8tUhbr72pAg8thikzExgqPJM4D8ILc7ToXj7dzHrwqHUV9kh5Xo0ncFhRnLFA%2FHrY%2B%2BRafQLcnocm4C%2Fpu4GGJ&X-Amz-Signature=e37a21af30ff177245ecb077caa6506e51dc9f8aebc1e5ebf0ae257ec068a514&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROHO6O2L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8kQJsc15LKKrF5%2FLYCcsH%2B21tVZzPDVNIqMeYzcAoHAiBeIksitvi%2BGuEjG52VqM3lP%2FiNY9H3row1paPDr%2BzDUSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0P2sr%2Fv3UphVJ94eKtwDHVMbM6YuTAbe7PDYEdkW4IkFDBnRJHkHr2yxcV8YbW7Z6u27D%2FaB5hg3Xp98Bga42vBHxTSJH%2FJgBf4A66WGK4f6kwLm8skTFkcnctij0BrddhASgVCyk7wq8zqFBgTBfXhzk4kd6C9FIWtQSyrw8xSKg1tVN5osZHyt%2BdSB3aeA04Az%2BGFXAn1RK4%2Fem0ZgXtfFPYcssd12pv9tUWSVLiKZCTNYZJoYK6Uo5b1fRXKneq%2Bkn4SoFCjCRUJ5i0EaEsiy%2BBk1Ab60HDiKhO4XhzMkUQqRbj8h6oEPQF4HLjrfnz97ESfT%2BzpAtCcbRjCO9uNut%2F98bYMPczUyywJYoTLAMyxI9gGUA5tC3K0vkTfYNIQRruyKowvYDIffL15fpYkHm97nf69tr1aTgTIOpMwtTXokB0sai8nzwcdPgunOStcOl%2BzAO%2F%2Bd8CzMwfK5Sfw01eHIoMD%2FucY1dv1sdaEX231lD7O%2ByawoBHJMhjOXpMNVBaxzJ384Cml84Co%2F68wRxpSa%2FYOXm1UIuTZ7vauF8hpXCePJvn9epV9QpljtLlYAuuxEIIXPXpyP8w87nuc8CG2jlml9PBHv7FARcCR59YofOQtdJ2HEnIF8etWx88umeAdPd8pfjqYw3fCvyAY6pgGlh%2FHgouT6n6X12Q9SH0Tk5CJAqkFbssLShddj7B63pCJki5ylAA39b369L8Co5yA%2FXxXRq4PIsxsM6U7JrlHCuSpg4h2YfLfl2Ywb8Nlo%2F8aMtWe8NI7AKyT1hQQ%2BZgmXdjh0OX8tUhbr72pAg8thikzExgqPJM4D8ILc7ToXj7dzHrwqHUV9kh5Xo0ncFhRnLFA%2FHrY%2B%2BRafQLcnocm4C%2Fpu4GGJ&X-Amz-Signature=76dccd2a60ef0c3b8e9740eb09cc0f3e371917a022539ebca467b267698f3c0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROHO6O2L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8kQJsc15LKKrF5%2FLYCcsH%2B21tVZzPDVNIqMeYzcAoHAiBeIksitvi%2BGuEjG52VqM3lP%2FiNY9H3row1paPDr%2BzDUSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0P2sr%2Fv3UphVJ94eKtwDHVMbM6YuTAbe7PDYEdkW4IkFDBnRJHkHr2yxcV8YbW7Z6u27D%2FaB5hg3Xp98Bga42vBHxTSJH%2FJgBf4A66WGK4f6kwLm8skTFkcnctij0BrddhASgVCyk7wq8zqFBgTBfXhzk4kd6C9FIWtQSyrw8xSKg1tVN5osZHyt%2BdSB3aeA04Az%2BGFXAn1RK4%2Fem0ZgXtfFPYcssd12pv9tUWSVLiKZCTNYZJoYK6Uo5b1fRXKneq%2Bkn4SoFCjCRUJ5i0EaEsiy%2BBk1Ab60HDiKhO4XhzMkUQqRbj8h6oEPQF4HLjrfnz97ESfT%2BzpAtCcbRjCO9uNut%2F98bYMPczUyywJYoTLAMyxI9gGUA5tC3K0vkTfYNIQRruyKowvYDIffL15fpYkHm97nf69tr1aTgTIOpMwtTXokB0sai8nzwcdPgunOStcOl%2BzAO%2F%2Bd8CzMwfK5Sfw01eHIoMD%2FucY1dv1sdaEX231lD7O%2ByawoBHJMhjOXpMNVBaxzJ384Cml84Co%2F68wRxpSa%2FYOXm1UIuTZ7vauF8hpXCePJvn9epV9QpljtLlYAuuxEIIXPXpyP8w87nuc8CG2jlml9PBHv7FARcCR59YofOQtdJ2HEnIF8etWx88umeAdPd8pfjqYw3fCvyAY6pgGlh%2FHgouT6n6X12Q9SH0Tk5CJAqkFbssLShddj7B63pCJki5ylAA39b369L8Co5yA%2FXxXRq4PIsxsM6U7JrlHCuSpg4h2YfLfl2Ywb8Nlo%2F8aMtWe8NI7AKyT1hQQ%2BZgmXdjh0OX8tUhbr72pAg8thikzExgqPJM4D8ILc7ToXj7dzHrwqHUV9kh5Xo0ncFhRnLFA%2FHrY%2B%2BRafQLcnocm4C%2Fpu4GGJ&X-Amz-Signature=ebfd6f7806e16f6ce7b9435966aecf7922f092455541ad7cd9118af53eeaaf61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROHO6O2L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8kQJsc15LKKrF5%2FLYCcsH%2B21tVZzPDVNIqMeYzcAoHAiBeIksitvi%2BGuEjG52VqM3lP%2FiNY9H3row1paPDr%2BzDUSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0P2sr%2Fv3UphVJ94eKtwDHVMbM6YuTAbe7PDYEdkW4IkFDBnRJHkHr2yxcV8YbW7Z6u27D%2FaB5hg3Xp98Bga42vBHxTSJH%2FJgBf4A66WGK4f6kwLm8skTFkcnctij0BrddhASgVCyk7wq8zqFBgTBfXhzk4kd6C9FIWtQSyrw8xSKg1tVN5osZHyt%2BdSB3aeA04Az%2BGFXAn1RK4%2Fem0ZgXtfFPYcssd12pv9tUWSVLiKZCTNYZJoYK6Uo5b1fRXKneq%2Bkn4SoFCjCRUJ5i0EaEsiy%2BBk1Ab60HDiKhO4XhzMkUQqRbj8h6oEPQF4HLjrfnz97ESfT%2BzpAtCcbRjCO9uNut%2F98bYMPczUyywJYoTLAMyxI9gGUA5tC3K0vkTfYNIQRruyKowvYDIffL15fpYkHm97nf69tr1aTgTIOpMwtTXokB0sai8nzwcdPgunOStcOl%2BzAO%2F%2Bd8CzMwfK5Sfw01eHIoMD%2FucY1dv1sdaEX231lD7O%2ByawoBHJMhjOXpMNVBaxzJ384Cml84Co%2F68wRxpSa%2FYOXm1UIuTZ7vauF8hpXCePJvn9epV9QpljtLlYAuuxEIIXPXpyP8w87nuc8CG2jlml9PBHv7FARcCR59YofOQtdJ2HEnIF8etWx88umeAdPd8pfjqYw3fCvyAY6pgGlh%2FHgouT6n6X12Q9SH0Tk5CJAqkFbssLShddj7B63pCJki5ylAA39b369L8Co5yA%2FXxXRq4PIsxsM6U7JrlHCuSpg4h2YfLfl2Ywb8Nlo%2F8aMtWe8NI7AKyT1hQQ%2BZgmXdjh0OX8tUhbr72pAg8thikzExgqPJM4D8ILc7ToXj7dzHrwqHUV9kh5Xo0ncFhRnLFA%2FHrY%2B%2BRafQLcnocm4C%2Fpu4GGJ&X-Amz-Signature=ec41f364330d4025dbfd252b7ef20b8d1b362d04edb756734bcd747afc2e2639&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROHO6O2L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8kQJsc15LKKrF5%2FLYCcsH%2B21tVZzPDVNIqMeYzcAoHAiBeIksitvi%2BGuEjG52VqM3lP%2FiNY9H3row1paPDr%2BzDUSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0P2sr%2Fv3UphVJ94eKtwDHVMbM6YuTAbe7PDYEdkW4IkFDBnRJHkHr2yxcV8YbW7Z6u27D%2FaB5hg3Xp98Bga42vBHxTSJH%2FJgBf4A66WGK4f6kwLm8skTFkcnctij0BrddhASgVCyk7wq8zqFBgTBfXhzk4kd6C9FIWtQSyrw8xSKg1tVN5osZHyt%2BdSB3aeA04Az%2BGFXAn1RK4%2Fem0ZgXtfFPYcssd12pv9tUWSVLiKZCTNYZJoYK6Uo5b1fRXKneq%2Bkn4SoFCjCRUJ5i0EaEsiy%2BBk1Ab60HDiKhO4XhzMkUQqRbj8h6oEPQF4HLjrfnz97ESfT%2BzpAtCcbRjCO9uNut%2F98bYMPczUyywJYoTLAMyxI9gGUA5tC3K0vkTfYNIQRruyKowvYDIffL15fpYkHm97nf69tr1aTgTIOpMwtTXokB0sai8nzwcdPgunOStcOl%2BzAO%2F%2Bd8CzMwfK5Sfw01eHIoMD%2FucY1dv1sdaEX231lD7O%2ByawoBHJMhjOXpMNVBaxzJ384Cml84Co%2F68wRxpSa%2FYOXm1UIuTZ7vauF8hpXCePJvn9epV9QpljtLlYAuuxEIIXPXpyP8w87nuc8CG2jlml9PBHv7FARcCR59YofOQtdJ2HEnIF8etWx88umeAdPd8pfjqYw3fCvyAY6pgGlh%2FHgouT6n6X12Q9SH0Tk5CJAqkFbssLShddj7B63pCJki5ylAA39b369L8Co5yA%2FXxXRq4PIsxsM6U7JrlHCuSpg4h2YfLfl2Ywb8Nlo%2F8aMtWe8NI7AKyT1hQQ%2BZgmXdjh0OX8tUhbr72pAg8thikzExgqPJM4D8ILc7ToXj7dzHrwqHUV9kh5Xo0ncFhRnLFA%2FHrY%2B%2BRafQLcnocm4C%2Fpu4GGJ&X-Amz-Signature=829fd5e006676a643def5b1a8181b2f9d22532a1d2398f148e1140ed4cf27c3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROHO6O2L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8kQJsc15LKKrF5%2FLYCcsH%2B21tVZzPDVNIqMeYzcAoHAiBeIksitvi%2BGuEjG52VqM3lP%2FiNY9H3row1paPDr%2BzDUSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0P2sr%2Fv3UphVJ94eKtwDHVMbM6YuTAbe7PDYEdkW4IkFDBnRJHkHr2yxcV8YbW7Z6u27D%2FaB5hg3Xp98Bga42vBHxTSJH%2FJgBf4A66WGK4f6kwLm8skTFkcnctij0BrddhASgVCyk7wq8zqFBgTBfXhzk4kd6C9FIWtQSyrw8xSKg1tVN5osZHyt%2BdSB3aeA04Az%2BGFXAn1RK4%2Fem0ZgXtfFPYcssd12pv9tUWSVLiKZCTNYZJoYK6Uo5b1fRXKneq%2Bkn4SoFCjCRUJ5i0EaEsiy%2BBk1Ab60HDiKhO4XhzMkUQqRbj8h6oEPQF4HLjrfnz97ESfT%2BzpAtCcbRjCO9uNut%2F98bYMPczUyywJYoTLAMyxI9gGUA5tC3K0vkTfYNIQRruyKowvYDIffL15fpYkHm97nf69tr1aTgTIOpMwtTXokB0sai8nzwcdPgunOStcOl%2BzAO%2F%2Bd8CzMwfK5Sfw01eHIoMD%2FucY1dv1sdaEX231lD7O%2ByawoBHJMhjOXpMNVBaxzJ384Cml84Co%2F68wRxpSa%2FYOXm1UIuTZ7vauF8hpXCePJvn9epV9QpljtLlYAuuxEIIXPXpyP8w87nuc8CG2jlml9PBHv7FARcCR59YofOQtdJ2HEnIF8etWx88umeAdPd8pfjqYw3fCvyAY6pgGlh%2FHgouT6n6X12Q9SH0Tk5CJAqkFbssLShddj7B63pCJki5ylAA39b369L8Co5yA%2FXxXRq4PIsxsM6U7JrlHCuSpg4h2YfLfl2Ywb8Nlo%2F8aMtWe8NI7AKyT1hQQ%2BZgmXdjh0OX8tUhbr72pAg8thikzExgqPJM4D8ILc7ToXj7dzHrwqHUV9kh5Xo0ncFhRnLFA%2FHrY%2B%2BRafQLcnocm4C%2Fpu4GGJ&X-Amz-Signature=cb90ca5ff22339eebf53b17af993a563ee256cbe1197a5a419f0dde9aaafda21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROHO6O2L%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8kQJsc15LKKrF5%2FLYCcsH%2B21tVZzPDVNIqMeYzcAoHAiBeIksitvi%2BGuEjG52VqM3lP%2FiNY9H3row1paPDr%2BzDUSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0P2sr%2Fv3UphVJ94eKtwDHVMbM6YuTAbe7PDYEdkW4IkFDBnRJHkHr2yxcV8YbW7Z6u27D%2FaB5hg3Xp98Bga42vBHxTSJH%2FJgBf4A66WGK4f6kwLm8skTFkcnctij0BrddhASgVCyk7wq8zqFBgTBfXhzk4kd6C9FIWtQSyrw8xSKg1tVN5osZHyt%2BdSB3aeA04Az%2BGFXAn1RK4%2Fem0ZgXtfFPYcssd12pv9tUWSVLiKZCTNYZJoYK6Uo5b1fRXKneq%2Bkn4SoFCjCRUJ5i0EaEsiy%2BBk1Ab60HDiKhO4XhzMkUQqRbj8h6oEPQF4HLjrfnz97ESfT%2BzpAtCcbRjCO9uNut%2F98bYMPczUyywJYoTLAMyxI9gGUA5tC3K0vkTfYNIQRruyKowvYDIffL15fpYkHm97nf69tr1aTgTIOpMwtTXokB0sai8nzwcdPgunOStcOl%2BzAO%2F%2Bd8CzMwfK5Sfw01eHIoMD%2FucY1dv1sdaEX231lD7O%2ByawoBHJMhjOXpMNVBaxzJ384Cml84Co%2F68wRxpSa%2FYOXm1UIuTZ7vauF8hpXCePJvn9epV9QpljtLlYAuuxEIIXPXpyP8w87nuc8CG2jlml9PBHv7FARcCR59YofOQtdJ2HEnIF8etWx88umeAdPd8pfjqYw3fCvyAY6pgGlh%2FHgouT6n6X12Q9SH0Tk5CJAqkFbssLShddj7B63pCJki5ylAA39b369L8Co5yA%2FXxXRq4PIsxsM6U7JrlHCuSpg4h2YfLfl2Ywb8Nlo%2F8aMtWe8NI7AKyT1hQQ%2BZgmXdjh0OX8tUhbr72pAg8thikzExgqPJM4D8ILc7ToXj7dzHrwqHUV9kh5Xo0ncFhRnLFA%2FHrY%2B%2BRafQLcnocm4C%2Fpu4GGJ&X-Amz-Signature=9643acf6b0b0e55b459dcf2b349a1a6ee6b95d7513c0375c5f8ffd5f823904f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

