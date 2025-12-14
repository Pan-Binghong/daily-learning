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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFIE4BMX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICUHKKotRQp2e3lqGGfp%2F2Bo%2F9%2FPnbuiWhPsSFRNjqKyAiB7L33dpg%2BeUVnq%2B11qM2gks4T29P5tUw2V%2BX8hCCyV7Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMhsULEOtWGTXJMpT%2BKtwDCda7%2FP4e1BG3ORa35AB7JCBdA36kFazuxOLW6SYVlCCyyE2KuEWGxUxlsUTuhaIW%2F2VvSILnjNBwjigUshFgoHALEKQSNx14L8TfHj0IxZx1YKM1sg4R%2FY5R2HlyRhpc9qPzjbW%2FL%2F6J2cCvLS6srG8T6S7Zj43jIQVjxZV5Jg29KF%2BOhtmYEYUQyzYX6AFuQ%2B87MvWYILDKXdDZeN9SmgIyzZsmS96KcvikQvAtXyvzIFptIJ7Nv1K5bvi12pW2sPpvnLdBAbfoLu9JnTZp09bIRpkT9s7fw0EpQ0mD2A6kpYYaNxR0T1Mp1KNPHqATD12TZDi1GUu4Qo0WD5iJNwmlj8LAEw%2Fa1EdkVWPgjsWgIQbgrjJAE%2FP%2Ftqc8NrrVS%2B3jrXBvK2g0UUib9LoFTSH6lU8PY%2FDXspNPHOXQRgkrQxQ2Gp6yVOJNxCtT0%2BKc0lGDumwwju40uJWcR1gIniUrkL0W19vdWT8AL1mpx7B7qYgu4PBUDMN8nBm8V6TzyeFw7V%2FM3230%2Fk3sM9Kw8uLyGV3%2BZAeYs8Qzj5wrjG5oknLiKUJCGy%2Bn%2BC61hI5Om62HWGa4vyDShOHD9Uv83Hjxzc0LvlXLdcrkupvPmiYGQjgRCITgZO4Qfm0wnbD4yQY6pgFWYuKAp%2F2qZS0MgdwNOMdNeCZ3ChjhLdtbv%2Fus9DCvZhNmXNF8%2BAqnXwE1b68QmSFL7%2FjeXHZzLBKWI17F9YHR2v3UsPZf8L7ktAWySipkK2EGRBHOqdEfdYHDFyc%2BccFXaqiFTK9Q85IWeNpfVIP%2BZDO1cEEUE9F6HuOKIedtBN71TD9cbH2FdcYppRY8DHNK07isfye%2BEVmiwCcA55txZ8F2snpR&X-Amz-Signature=a94d1b9e76ff554a4dc165a18224330d9edf06754d90386aa78c11434fa4cfd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFIE4BMX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICUHKKotRQp2e3lqGGfp%2F2Bo%2F9%2FPnbuiWhPsSFRNjqKyAiB7L33dpg%2BeUVnq%2B11qM2gks4T29P5tUw2V%2BX8hCCyV7Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMhsULEOtWGTXJMpT%2BKtwDCda7%2FP4e1BG3ORa35AB7JCBdA36kFazuxOLW6SYVlCCyyE2KuEWGxUxlsUTuhaIW%2F2VvSILnjNBwjigUshFgoHALEKQSNx14L8TfHj0IxZx1YKM1sg4R%2FY5R2HlyRhpc9qPzjbW%2FL%2F6J2cCvLS6srG8T6S7Zj43jIQVjxZV5Jg29KF%2BOhtmYEYUQyzYX6AFuQ%2B87MvWYILDKXdDZeN9SmgIyzZsmS96KcvikQvAtXyvzIFptIJ7Nv1K5bvi12pW2sPpvnLdBAbfoLu9JnTZp09bIRpkT9s7fw0EpQ0mD2A6kpYYaNxR0T1Mp1KNPHqATD12TZDi1GUu4Qo0WD5iJNwmlj8LAEw%2Fa1EdkVWPgjsWgIQbgrjJAE%2FP%2Ftqc8NrrVS%2B3jrXBvK2g0UUib9LoFTSH6lU8PY%2FDXspNPHOXQRgkrQxQ2Gp6yVOJNxCtT0%2BKc0lGDumwwju40uJWcR1gIniUrkL0W19vdWT8AL1mpx7B7qYgu4PBUDMN8nBm8V6TzyeFw7V%2FM3230%2Fk3sM9Kw8uLyGV3%2BZAeYs8Qzj5wrjG5oknLiKUJCGy%2Bn%2BC61hI5Om62HWGa4vyDShOHD9Uv83Hjxzc0LvlXLdcrkupvPmiYGQjgRCITgZO4Qfm0wnbD4yQY6pgFWYuKAp%2F2qZS0MgdwNOMdNeCZ3ChjhLdtbv%2Fus9DCvZhNmXNF8%2BAqnXwE1b68QmSFL7%2FjeXHZzLBKWI17F9YHR2v3UsPZf8L7ktAWySipkK2EGRBHOqdEfdYHDFyc%2BccFXaqiFTK9Q85IWeNpfVIP%2BZDO1cEEUE9F6HuOKIedtBN71TD9cbH2FdcYppRY8DHNK07isfye%2BEVmiwCcA55txZ8F2snpR&X-Amz-Signature=de8bb022f4f90c2137b790aa6c049795965d17e66f4ef7fc2bd9df1ad3c48585&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFIE4BMX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICUHKKotRQp2e3lqGGfp%2F2Bo%2F9%2FPnbuiWhPsSFRNjqKyAiB7L33dpg%2BeUVnq%2B11qM2gks4T29P5tUw2V%2BX8hCCyV7Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMhsULEOtWGTXJMpT%2BKtwDCda7%2FP4e1BG3ORa35AB7JCBdA36kFazuxOLW6SYVlCCyyE2KuEWGxUxlsUTuhaIW%2F2VvSILnjNBwjigUshFgoHALEKQSNx14L8TfHj0IxZx1YKM1sg4R%2FY5R2HlyRhpc9qPzjbW%2FL%2F6J2cCvLS6srG8T6S7Zj43jIQVjxZV5Jg29KF%2BOhtmYEYUQyzYX6AFuQ%2B87MvWYILDKXdDZeN9SmgIyzZsmS96KcvikQvAtXyvzIFptIJ7Nv1K5bvi12pW2sPpvnLdBAbfoLu9JnTZp09bIRpkT9s7fw0EpQ0mD2A6kpYYaNxR0T1Mp1KNPHqATD12TZDi1GUu4Qo0WD5iJNwmlj8LAEw%2Fa1EdkVWPgjsWgIQbgrjJAE%2FP%2Ftqc8NrrVS%2B3jrXBvK2g0UUib9LoFTSH6lU8PY%2FDXspNPHOXQRgkrQxQ2Gp6yVOJNxCtT0%2BKc0lGDumwwju40uJWcR1gIniUrkL0W19vdWT8AL1mpx7B7qYgu4PBUDMN8nBm8V6TzyeFw7V%2FM3230%2Fk3sM9Kw8uLyGV3%2BZAeYs8Qzj5wrjG5oknLiKUJCGy%2Bn%2BC61hI5Om62HWGa4vyDShOHD9Uv83Hjxzc0LvlXLdcrkupvPmiYGQjgRCITgZO4Qfm0wnbD4yQY6pgFWYuKAp%2F2qZS0MgdwNOMdNeCZ3ChjhLdtbv%2Fus9DCvZhNmXNF8%2BAqnXwE1b68QmSFL7%2FjeXHZzLBKWI17F9YHR2v3UsPZf8L7ktAWySipkK2EGRBHOqdEfdYHDFyc%2BccFXaqiFTK9Q85IWeNpfVIP%2BZDO1cEEUE9F6HuOKIedtBN71TD9cbH2FdcYppRY8DHNK07isfye%2BEVmiwCcA55txZ8F2snpR&X-Amz-Signature=27ae1f28576b3910e5796ba7fe3dc77e45ed06f39b77366d84fea9ac17c2207b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFIE4BMX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICUHKKotRQp2e3lqGGfp%2F2Bo%2F9%2FPnbuiWhPsSFRNjqKyAiB7L33dpg%2BeUVnq%2B11qM2gks4T29P5tUw2V%2BX8hCCyV7Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMhsULEOtWGTXJMpT%2BKtwDCda7%2FP4e1BG3ORa35AB7JCBdA36kFazuxOLW6SYVlCCyyE2KuEWGxUxlsUTuhaIW%2F2VvSILnjNBwjigUshFgoHALEKQSNx14L8TfHj0IxZx1YKM1sg4R%2FY5R2HlyRhpc9qPzjbW%2FL%2F6J2cCvLS6srG8T6S7Zj43jIQVjxZV5Jg29KF%2BOhtmYEYUQyzYX6AFuQ%2B87MvWYILDKXdDZeN9SmgIyzZsmS96KcvikQvAtXyvzIFptIJ7Nv1K5bvi12pW2sPpvnLdBAbfoLu9JnTZp09bIRpkT9s7fw0EpQ0mD2A6kpYYaNxR0T1Mp1KNPHqATD12TZDi1GUu4Qo0WD5iJNwmlj8LAEw%2Fa1EdkVWPgjsWgIQbgrjJAE%2FP%2Ftqc8NrrVS%2B3jrXBvK2g0UUib9LoFTSH6lU8PY%2FDXspNPHOXQRgkrQxQ2Gp6yVOJNxCtT0%2BKc0lGDumwwju40uJWcR1gIniUrkL0W19vdWT8AL1mpx7B7qYgu4PBUDMN8nBm8V6TzyeFw7V%2FM3230%2Fk3sM9Kw8uLyGV3%2BZAeYs8Qzj5wrjG5oknLiKUJCGy%2Bn%2BC61hI5Om62HWGa4vyDShOHD9Uv83Hjxzc0LvlXLdcrkupvPmiYGQjgRCITgZO4Qfm0wnbD4yQY6pgFWYuKAp%2F2qZS0MgdwNOMdNeCZ3ChjhLdtbv%2Fus9DCvZhNmXNF8%2BAqnXwE1b68QmSFL7%2FjeXHZzLBKWI17F9YHR2v3UsPZf8L7ktAWySipkK2EGRBHOqdEfdYHDFyc%2BccFXaqiFTK9Q85IWeNpfVIP%2BZDO1cEEUE9F6HuOKIedtBN71TD9cbH2FdcYppRY8DHNK07isfye%2BEVmiwCcA55txZ8F2snpR&X-Amz-Signature=febca860f258720e3507714d91cf2a72d1efad5c2c2db6256b5abb218620b8fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFIE4BMX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICUHKKotRQp2e3lqGGfp%2F2Bo%2F9%2FPnbuiWhPsSFRNjqKyAiB7L33dpg%2BeUVnq%2B11qM2gks4T29P5tUw2V%2BX8hCCyV7Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMhsULEOtWGTXJMpT%2BKtwDCda7%2FP4e1BG3ORa35AB7JCBdA36kFazuxOLW6SYVlCCyyE2KuEWGxUxlsUTuhaIW%2F2VvSILnjNBwjigUshFgoHALEKQSNx14L8TfHj0IxZx1YKM1sg4R%2FY5R2HlyRhpc9qPzjbW%2FL%2F6J2cCvLS6srG8T6S7Zj43jIQVjxZV5Jg29KF%2BOhtmYEYUQyzYX6AFuQ%2B87MvWYILDKXdDZeN9SmgIyzZsmS96KcvikQvAtXyvzIFptIJ7Nv1K5bvi12pW2sPpvnLdBAbfoLu9JnTZp09bIRpkT9s7fw0EpQ0mD2A6kpYYaNxR0T1Mp1KNPHqATD12TZDi1GUu4Qo0WD5iJNwmlj8LAEw%2Fa1EdkVWPgjsWgIQbgrjJAE%2FP%2Ftqc8NrrVS%2B3jrXBvK2g0UUib9LoFTSH6lU8PY%2FDXspNPHOXQRgkrQxQ2Gp6yVOJNxCtT0%2BKc0lGDumwwju40uJWcR1gIniUrkL0W19vdWT8AL1mpx7B7qYgu4PBUDMN8nBm8V6TzyeFw7V%2FM3230%2Fk3sM9Kw8uLyGV3%2BZAeYs8Qzj5wrjG5oknLiKUJCGy%2Bn%2BC61hI5Om62HWGa4vyDShOHD9Uv83Hjxzc0LvlXLdcrkupvPmiYGQjgRCITgZO4Qfm0wnbD4yQY6pgFWYuKAp%2F2qZS0MgdwNOMdNeCZ3ChjhLdtbv%2Fus9DCvZhNmXNF8%2BAqnXwE1b68QmSFL7%2FjeXHZzLBKWI17F9YHR2v3UsPZf8L7ktAWySipkK2EGRBHOqdEfdYHDFyc%2BccFXaqiFTK9Q85IWeNpfVIP%2BZDO1cEEUE9F6HuOKIedtBN71TD9cbH2FdcYppRY8DHNK07isfye%2BEVmiwCcA55txZ8F2snpR&X-Amz-Signature=f3efa535dc4e4feeb39ebc257b88961364108cbba5a996850da1d12251484b02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFIE4BMX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICUHKKotRQp2e3lqGGfp%2F2Bo%2F9%2FPnbuiWhPsSFRNjqKyAiB7L33dpg%2BeUVnq%2B11qM2gks4T29P5tUw2V%2BX8hCCyV7Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMhsULEOtWGTXJMpT%2BKtwDCda7%2FP4e1BG3ORa35AB7JCBdA36kFazuxOLW6SYVlCCyyE2KuEWGxUxlsUTuhaIW%2F2VvSILnjNBwjigUshFgoHALEKQSNx14L8TfHj0IxZx1YKM1sg4R%2FY5R2HlyRhpc9qPzjbW%2FL%2F6J2cCvLS6srG8T6S7Zj43jIQVjxZV5Jg29KF%2BOhtmYEYUQyzYX6AFuQ%2B87MvWYILDKXdDZeN9SmgIyzZsmS96KcvikQvAtXyvzIFptIJ7Nv1K5bvi12pW2sPpvnLdBAbfoLu9JnTZp09bIRpkT9s7fw0EpQ0mD2A6kpYYaNxR0T1Mp1KNPHqATD12TZDi1GUu4Qo0WD5iJNwmlj8LAEw%2Fa1EdkVWPgjsWgIQbgrjJAE%2FP%2Ftqc8NrrVS%2B3jrXBvK2g0UUib9LoFTSH6lU8PY%2FDXspNPHOXQRgkrQxQ2Gp6yVOJNxCtT0%2BKc0lGDumwwju40uJWcR1gIniUrkL0W19vdWT8AL1mpx7B7qYgu4PBUDMN8nBm8V6TzyeFw7V%2FM3230%2Fk3sM9Kw8uLyGV3%2BZAeYs8Qzj5wrjG5oknLiKUJCGy%2Bn%2BC61hI5Om62HWGa4vyDShOHD9Uv83Hjxzc0LvlXLdcrkupvPmiYGQjgRCITgZO4Qfm0wnbD4yQY6pgFWYuKAp%2F2qZS0MgdwNOMdNeCZ3ChjhLdtbv%2Fus9DCvZhNmXNF8%2BAqnXwE1b68QmSFL7%2FjeXHZzLBKWI17F9YHR2v3UsPZf8L7ktAWySipkK2EGRBHOqdEfdYHDFyc%2BccFXaqiFTK9Q85IWeNpfVIP%2BZDO1cEEUE9F6HuOKIedtBN71TD9cbH2FdcYppRY8DHNK07isfye%2BEVmiwCcA55txZ8F2snpR&X-Amz-Signature=848068c135be9b88ba56d1db89fa4d56d3ca9ab3df97a9baae91adce8ba68f3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFIE4BMX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICUHKKotRQp2e3lqGGfp%2F2Bo%2F9%2FPnbuiWhPsSFRNjqKyAiB7L33dpg%2BeUVnq%2B11qM2gks4T29P5tUw2V%2BX8hCCyV7Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMhsULEOtWGTXJMpT%2BKtwDCda7%2FP4e1BG3ORa35AB7JCBdA36kFazuxOLW6SYVlCCyyE2KuEWGxUxlsUTuhaIW%2F2VvSILnjNBwjigUshFgoHALEKQSNx14L8TfHj0IxZx1YKM1sg4R%2FY5R2HlyRhpc9qPzjbW%2FL%2F6J2cCvLS6srG8T6S7Zj43jIQVjxZV5Jg29KF%2BOhtmYEYUQyzYX6AFuQ%2B87MvWYILDKXdDZeN9SmgIyzZsmS96KcvikQvAtXyvzIFptIJ7Nv1K5bvi12pW2sPpvnLdBAbfoLu9JnTZp09bIRpkT9s7fw0EpQ0mD2A6kpYYaNxR0T1Mp1KNPHqATD12TZDi1GUu4Qo0WD5iJNwmlj8LAEw%2Fa1EdkVWPgjsWgIQbgrjJAE%2FP%2Ftqc8NrrVS%2B3jrXBvK2g0UUib9LoFTSH6lU8PY%2FDXspNPHOXQRgkrQxQ2Gp6yVOJNxCtT0%2BKc0lGDumwwju40uJWcR1gIniUrkL0W19vdWT8AL1mpx7B7qYgu4PBUDMN8nBm8V6TzyeFw7V%2FM3230%2Fk3sM9Kw8uLyGV3%2BZAeYs8Qzj5wrjG5oknLiKUJCGy%2Bn%2BC61hI5Om62HWGa4vyDShOHD9Uv83Hjxzc0LvlXLdcrkupvPmiYGQjgRCITgZO4Qfm0wnbD4yQY6pgFWYuKAp%2F2qZS0MgdwNOMdNeCZ3ChjhLdtbv%2Fus9DCvZhNmXNF8%2BAqnXwE1b68QmSFL7%2FjeXHZzLBKWI17F9YHR2v3UsPZf8L7ktAWySipkK2EGRBHOqdEfdYHDFyc%2BccFXaqiFTK9Q85IWeNpfVIP%2BZDO1cEEUE9F6HuOKIedtBN71TD9cbH2FdcYppRY8DHNK07isfye%2BEVmiwCcA55txZ8F2snpR&X-Amz-Signature=adecb7a34fffa85c7ebb343e7c12d0d25100df0d421ef221121bdeb0eb839220&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFIE4BMX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICUHKKotRQp2e3lqGGfp%2F2Bo%2F9%2FPnbuiWhPsSFRNjqKyAiB7L33dpg%2BeUVnq%2B11qM2gks4T29P5tUw2V%2BX8hCCyV7Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMhsULEOtWGTXJMpT%2BKtwDCda7%2FP4e1BG3ORa35AB7JCBdA36kFazuxOLW6SYVlCCyyE2KuEWGxUxlsUTuhaIW%2F2VvSILnjNBwjigUshFgoHALEKQSNx14L8TfHj0IxZx1YKM1sg4R%2FY5R2HlyRhpc9qPzjbW%2FL%2F6J2cCvLS6srG8T6S7Zj43jIQVjxZV5Jg29KF%2BOhtmYEYUQyzYX6AFuQ%2B87MvWYILDKXdDZeN9SmgIyzZsmS96KcvikQvAtXyvzIFptIJ7Nv1K5bvi12pW2sPpvnLdBAbfoLu9JnTZp09bIRpkT9s7fw0EpQ0mD2A6kpYYaNxR0T1Mp1KNPHqATD12TZDi1GUu4Qo0WD5iJNwmlj8LAEw%2Fa1EdkVWPgjsWgIQbgrjJAE%2FP%2Ftqc8NrrVS%2B3jrXBvK2g0UUib9LoFTSH6lU8PY%2FDXspNPHOXQRgkrQxQ2Gp6yVOJNxCtT0%2BKc0lGDumwwju40uJWcR1gIniUrkL0W19vdWT8AL1mpx7B7qYgu4PBUDMN8nBm8V6TzyeFw7V%2FM3230%2Fk3sM9Kw8uLyGV3%2BZAeYs8Qzj5wrjG5oknLiKUJCGy%2Bn%2BC61hI5Om62HWGa4vyDShOHD9Uv83Hjxzc0LvlXLdcrkupvPmiYGQjgRCITgZO4Qfm0wnbD4yQY6pgFWYuKAp%2F2qZS0MgdwNOMdNeCZ3ChjhLdtbv%2Fus9DCvZhNmXNF8%2BAqnXwE1b68QmSFL7%2FjeXHZzLBKWI17F9YHR2v3UsPZf8L7ktAWySipkK2EGRBHOqdEfdYHDFyc%2BccFXaqiFTK9Q85IWeNpfVIP%2BZDO1cEEUE9F6HuOKIedtBN71TD9cbH2FdcYppRY8DHNK07isfye%2BEVmiwCcA55txZ8F2snpR&X-Amz-Signature=fe9246561318716c5edb569bf34cb0d71b25f911c70b2cd80a060c27d048ab5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFIE4BMX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICUHKKotRQp2e3lqGGfp%2F2Bo%2F9%2FPnbuiWhPsSFRNjqKyAiB7L33dpg%2BeUVnq%2B11qM2gks4T29P5tUw2V%2BX8hCCyV7Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMhsULEOtWGTXJMpT%2BKtwDCda7%2FP4e1BG3ORa35AB7JCBdA36kFazuxOLW6SYVlCCyyE2KuEWGxUxlsUTuhaIW%2F2VvSILnjNBwjigUshFgoHALEKQSNx14L8TfHj0IxZx1YKM1sg4R%2FY5R2HlyRhpc9qPzjbW%2FL%2F6J2cCvLS6srG8T6S7Zj43jIQVjxZV5Jg29KF%2BOhtmYEYUQyzYX6AFuQ%2B87MvWYILDKXdDZeN9SmgIyzZsmS96KcvikQvAtXyvzIFptIJ7Nv1K5bvi12pW2sPpvnLdBAbfoLu9JnTZp09bIRpkT9s7fw0EpQ0mD2A6kpYYaNxR0T1Mp1KNPHqATD12TZDi1GUu4Qo0WD5iJNwmlj8LAEw%2Fa1EdkVWPgjsWgIQbgrjJAE%2FP%2Ftqc8NrrVS%2B3jrXBvK2g0UUib9LoFTSH6lU8PY%2FDXspNPHOXQRgkrQxQ2Gp6yVOJNxCtT0%2BKc0lGDumwwju40uJWcR1gIniUrkL0W19vdWT8AL1mpx7B7qYgu4PBUDMN8nBm8V6TzyeFw7V%2FM3230%2Fk3sM9Kw8uLyGV3%2BZAeYs8Qzj5wrjG5oknLiKUJCGy%2Bn%2BC61hI5Om62HWGa4vyDShOHD9Uv83Hjxzc0LvlXLdcrkupvPmiYGQjgRCITgZO4Qfm0wnbD4yQY6pgFWYuKAp%2F2qZS0MgdwNOMdNeCZ3ChjhLdtbv%2Fus9DCvZhNmXNF8%2BAqnXwE1b68QmSFL7%2FjeXHZzLBKWI17F9YHR2v3UsPZf8L7ktAWySipkK2EGRBHOqdEfdYHDFyc%2BccFXaqiFTK9Q85IWeNpfVIP%2BZDO1cEEUE9F6HuOKIedtBN71TD9cbH2FdcYppRY8DHNK07isfye%2BEVmiwCcA55txZ8F2snpR&X-Amz-Signature=537e557530b622ae168a37f6a9d922e544eb59110bf4044b448cea4eb86bb3d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFIE4BMX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCICUHKKotRQp2e3lqGGfp%2F2Bo%2F9%2FPnbuiWhPsSFRNjqKyAiB7L33dpg%2BeUVnq%2B11qM2gks4T29P5tUw2V%2BX8hCCyV7Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMhsULEOtWGTXJMpT%2BKtwDCda7%2FP4e1BG3ORa35AB7JCBdA36kFazuxOLW6SYVlCCyyE2KuEWGxUxlsUTuhaIW%2F2VvSILnjNBwjigUshFgoHALEKQSNx14L8TfHj0IxZx1YKM1sg4R%2FY5R2HlyRhpc9qPzjbW%2FL%2F6J2cCvLS6srG8T6S7Zj43jIQVjxZV5Jg29KF%2BOhtmYEYUQyzYX6AFuQ%2B87MvWYILDKXdDZeN9SmgIyzZsmS96KcvikQvAtXyvzIFptIJ7Nv1K5bvi12pW2sPpvnLdBAbfoLu9JnTZp09bIRpkT9s7fw0EpQ0mD2A6kpYYaNxR0T1Mp1KNPHqATD12TZDi1GUu4Qo0WD5iJNwmlj8LAEw%2Fa1EdkVWPgjsWgIQbgrjJAE%2FP%2Ftqc8NrrVS%2B3jrXBvK2g0UUib9LoFTSH6lU8PY%2FDXspNPHOXQRgkrQxQ2Gp6yVOJNxCtT0%2BKc0lGDumwwju40uJWcR1gIniUrkL0W19vdWT8AL1mpx7B7qYgu4PBUDMN8nBm8V6TzyeFw7V%2FM3230%2Fk3sM9Kw8uLyGV3%2BZAeYs8Qzj5wrjG5oknLiKUJCGy%2Bn%2BC61hI5Om62HWGa4vyDShOHD9Uv83Hjxzc0LvlXLdcrkupvPmiYGQjgRCITgZO4Qfm0wnbD4yQY6pgFWYuKAp%2F2qZS0MgdwNOMdNeCZ3ChjhLdtbv%2Fus9DCvZhNmXNF8%2BAqnXwE1b68QmSFL7%2FjeXHZzLBKWI17F9YHR2v3UsPZf8L7ktAWySipkK2EGRBHOqdEfdYHDFyc%2BccFXaqiFTK9Q85IWeNpfVIP%2BZDO1cEEUE9F6HuOKIedtBN71TD9cbH2FdcYppRY8DHNK07isfye%2BEVmiwCcA55txZ8F2snpR&X-Amz-Signature=2d9c926131d141f07b5d753264e16508dcfad022bd6d91b3544c0b665a54bccc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

