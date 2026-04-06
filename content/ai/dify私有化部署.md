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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDUAJIM%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLBK%2FBk%2BjcuF75KPDzP7Yfesj5BVA%2FVQyZvgJgbsH3oAiEAvoY7r6R55QKEB%2FQITHX%2Bj3e25Y9QzQ0zkHDGSUp2Fr8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC57iggRMfoPeQ0kNSrcAx4L0doBDTHmI24aPRy2tqx6KHNDywOG3HLb%2BB3J3vrPuRuQ3HvOF2%2BnNUcRax2Lbttunfemn8shrGz5hX8EDeVlZUZ17S1TnuIM2zlvPiUlfnlBZrfKWlBTDZXzfOgGgzI8O8gFkOR7nhgzi3snJqaYQerWW0F788FhO1Y7z%2B2yJ8otikHBHYy6R12ztAHx5SN1dtMNB9FgHY2qQOSTOwCSw9BRRof5%2F1gD12eXITsDoIuO%2FouwzNVN%2BpwqnAzWGluBkDxRus85BHAFWuVJ%2FfVaOmWscI1Ya4zEj9j%2By5BZeRWcknjIhG1nBPp8k9EMAcFH15K2HBbRv3Wh5m3chUhWI5c3vT62fKUA3QZLHacUnxSrVxNWpaiHjj2oMdv6Vqr4vZmQw2Pm8ETDFuUqDpvCk1pvQNCpkdREUWhnVTOZjfV9ib2F3eIbYnGi1%2FUGud03ZwsVND%2BNCkL2i%2FmuQcckhK%2FBOs1wEfLq7QjmVrpOtNC206bwlwEmrs4Rmn5ucICDi%2FtA0xEfgTYNK7zVZpJnub18xSGpu112QV8EUbPq10YzQBkaTq4St%2BPJjBa7H%2FEua61t%2BivAi9wIcFaT6M6nV3fHjbnznbQ4P%2BTSB7T5DkYR69iWzGuy9MdqMO6vzM4GOqUBt3uu00d9CAEgMWmfiMREYuPEAcHV7IFxZPnXtPYD3o%2B2cgfQp%2BbS4tWnndg%2F97CUB1ucmXrGx1d1KD4%2F%2FVWp3T6o%2F%2B%2FafdLV7f1usg5iIHS5j%2B0e4Cf5UuQYYrTnIEB8UUEq%2FRBSOnOdY7IaZZNtjEV8NCdHrwzsr9Ca%2FrOjUlASFJm50EcOIQASwK6wtUPSiB7mCnDrLiBL2C6y0JZtkK3Vh7gv&X-Amz-Signature=3e73c29da52aa0b8ddcc4db952b2178f9f728918b6728031fd482efd388f96dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDUAJIM%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLBK%2FBk%2BjcuF75KPDzP7Yfesj5BVA%2FVQyZvgJgbsH3oAiEAvoY7r6R55QKEB%2FQITHX%2Bj3e25Y9QzQ0zkHDGSUp2Fr8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC57iggRMfoPeQ0kNSrcAx4L0doBDTHmI24aPRy2tqx6KHNDywOG3HLb%2BB3J3vrPuRuQ3HvOF2%2BnNUcRax2Lbttunfemn8shrGz5hX8EDeVlZUZ17S1TnuIM2zlvPiUlfnlBZrfKWlBTDZXzfOgGgzI8O8gFkOR7nhgzi3snJqaYQerWW0F788FhO1Y7z%2B2yJ8otikHBHYy6R12ztAHx5SN1dtMNB9FgHY2qQOSTOwCSw9BRRof5%2F1gD12eXITsDoIuO%2FouwzNVN%2BpwqnAzWGluBkDxRus85BHAFWuVJ%2FfVaOmWscI1Ya4zEj9j%2By5BZeRWcknjIhG1nBPp8k9EMAcFH15K2HBbRv3Wh5m3chUhWI5c3vT62fKUA3QZLHacUnxSrVxNWpaiHjj2oMdv6Vqr4vZmQw2Pm8ETDFuUqDpvCk1pvQNCpkdREUWhnVTOZjfV9ib2F3eIbYnGi1%2FUGud03ZwsVND%2BNCkL2i%2FmuQcckhK%2FBOs1wEfLq7QjmVrpOtNC206bwlwEmrs4Rmn5ucICDi%2FtA0xEfgTYNK7zVZpJnub18xSGpu112QV8EUbPq10YzQBkaTq4St%2BPJjBa7H%2FEua61t%2BivAi9wIcFaT6M6nV3fHjbnznbQ4P%2BTSB7T5DkYR69iWzGuy9MdqMO6vzM4GOqUBt3uu00d9CAEgMWmfiMREYuPEAcHV7IFxZPnXtPYD3o%2B2cgfQp%2BbS4tWnndg%2F97CUB1ucmXrGx1d1KD4%2F%2FVWp3T6o%2F%2B%2FafdLV7f1usg5iIHS5j%2B0e4Cf5UuQYYrTnIEB8UUEq%2FRBSOnOdY7IaZZNtjEV8NCdHrwzsr9Ca%2FrOjUlASFJm50EcOIQASwK6wtUPSiB7mCnDrLiBL2C6y0JZtkK3Vh7gv&X-Amz-Signature=6789af7e6e7242806abe3f07d93bec882958000af1caf2ef10e849f5611f111a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDUAJIM%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLBK%2FBk%2BjcuF75KPDzP7Yfesj5BVA%2FVQyZvgJgbsH3oAiEAvoY7r6R55QKEB%2FQITHX%2Bj3e25Y9QzQ0zkHDGSUp2Fr8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC57iggRMfoPeQ0kNSrcAx4L0doBDTHmI24aPRy2tqx6KHNDywOG3HLb%2BB3J3vrPuRuQ3HvOF2%2BnNUcRax2Lbttunfemn8shrGz5hX8EDeVlZUZ17S1TnuIM2zlvPiUlfnlBZrfKWlBTDZXzfOgGgzI8O8gFkOR7nhgzi3snJqaYQerWW0F788FhO1Y7z%2B2yJ8otikHBHYy6R12ztAHx5SN1dtMNB9FgHY2qQOSTOwCSw9BRRof5%2F1gD12eXITsDoIuO%2FouwzNVN%2BpwqnAzWGluBkDxRus85BHAFWuVJ%2FfVaOmWscI1Ya4zEj9j%2By5BZeRWcknjIhG1nBPp8k9EMAcFH15K2HBbRv3Wh5m3chUhWI5c3vT62fKUA3QZLHacUnxSrVxNWpaiHjj2oMdv6Vqr4vZmQw2Pm8ETDFuUqDpvCk1pvQNCpkdREUWhnVTOZjfV9ib2F3eIbYnGi1%2FUGud03ZwsVND%2BNCkL2i%2FmuQcckhK%2FBOs1wEfLq7QjmVrpOtNC206bwlwEmrs4Rmn5ucICDi%2FtA0xEfgTYNK7zVZpJnub18xSGpu112QV8EUbPq10YzQBkaTq4St%2BPJjBa7H%2FEua61t%2BivAi9wIcFaT6M6nV3fHjbnznbQ4P%2BTSB7T5DkYR69iWzGuy9MdqMO6vzM4GOqUBt3uu00d9CAEgMWmfiMREYuPEAcHV7IFxZPnXtPYD3o%2B2cgfQp%2BbS4tWnndg%2F97CUB1ucmXrGx1d1KD4%2F%2FVWp3T6o%2F%2B%2FafdLV7f1usg5iIHS5j%2B0e4Cf5UuQYYrTnIEB8UUEq%2FRBSOnOdY7IaZZNtjEV8NCdHrwzsr9Ca%2FrOjUlASFJm50EcOIQASwK6wtUPSiB7mCnDrLiBL2C6y0JZtkK3Vh7gv&X-Amz-Signature=6303aa41ccec5c1823a63fb54d54ad7dcdb84f2512ba08af0a984108d8b453c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDUAJIM%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLBK%2FBk%2BjcuF75KPDzP7Yfesj5BVA%2FVQyZvgJgbsH3oAiEAvoY7r6R55QKEB%2FQITHX%2Bj3e25Y9QzQ0zkHDGSUp2Fr8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC57iggRMfoPeQ0kNSrcAx4L0doBDTHmI24aPRy2tqx6KHNDywOG3HLb%2BB3J3vrPuRuQ3HvOF2%2BnNUcRax2Lbttunfemn8shrGz5hX8EDeVlZUZ17S1TnuIM2zlvPiUlfnlBZrfKWlBTDZXzfOgGgzI8O8gFkOR7nhgzi3snJqaYQerWW0F788FhO1Y7z%2B2yJ8otikHBHYy6R12ztAHx5SN1dtMNB9FgHY2qQOSTOwCSw9BRRof5%2F1gD12eXITsDoIuO%2FouwzNVN%2BpwqnAzWGluBkDxRus85BHAFWuVJ%2FfVaOmWscI1Ya4zEj9j%2By5BZeRWcknjIhG1nBPp8k9EMAcFH15K2HBbRv3Wh5m3chUhWI5c3vT62fKUA3QZLHacUnxSrVxNWpaiHjj2oMdv6Vqr4vZmQw2Pm8ETDFuUqDpvCk1pvQNCpkdREUWhnVTOZjfV9ib2F3eIbYnGi1%2FUGud03ZwsVND%2BNCkL2i%2FmuQcckhK%2FBOs1wEfLq7QjmVrpOtNC206bwlwEmrs4Rmn5ucICDi%2FtA0xEfgTYNK7zVZpJnub18xSGpu112QV8EUbPq10YzQBkaTq4St%2BPJjBa7H%2FEua61t%2BivAi9wIcFaT6M6nV3fHjbnznbQ4P%2BTSB7T5DkYR69iWzGuy9MdqMO6vzM4GOqUBt3uu00d9CAEgMWmfiMREYuPEAcHV7IFxZPnXtPYD3o%2B2cgfQp%2BbS4tWnndg%2F97CUB1ucmXrGx1d1KD4%2F%2FVWp3T6o%2F%2B%2FafdLV7f1usg5iIHS5j%2B0e4Cf5UuQYYrTnIEB8UUEq%2FRBSOnOdY7IaZZNtjEV8NCdHrwzsr9Ca%2FrOjUlASFJm50EcOIQASwK6wtUPSiB7mCnDrLiBL2C6y0JZtkK3Vh7gv&X-Amz-Signature=8602ae79e798229f7469444e429effbb01ab2fcb1a7e5f03e55d9fad2edc7608&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDUAJIM%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLBK%2FBk%2BjcuF75KPDzP7Yfesj5BVA%2FVQyZvgJgbsH3oAiEAvoY7r6R55QKEB%2FQITHX%2Bj3e25Y9QzQ0zkHDGSUp2Fr8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC57iggRMfoPeQ0kNSrcAx4L0doBDTHmI24aPRy2tqx6KHNDywOG3HLb%2BB3J3vrPuRuQ3HvOF2%2BnNUcRax2Lbttunfemn8shrGz5hX8EDeVlZUZ17S1TnuIM2zlvPiUlfnlBZrfKWlBTDZXzfOgGgzI8O8gFkOR7nhgzi3snJqaYQerWW0F788FhO1Y7z%2B2yJ8otikHBHYy6R12ztAHx5SN1dtMNB9FgHY2qQOSTOwCSw9BRRof5%2F1gD12eXITsDoIuO%2FouwzNVN%2BpwqnAzWGluBkDxRus85BHAFWuVJ%2FfVaOmWscI1Ya4zEj9j%2By5BZeRWcknjIhG1nBPp8k9EMAcFH15K2HBbRv3Wh5m3chUhWI5c3vT62fKUA3QZLHacUnxSrVxNWpaiHjj2oMdv6Vqr4vZmQw2Pm8ETDFuUqDpvCk1pvQNCpkdREUWhnVTOZjfV9ib2F3eIbYnGi1%2FUGud03ZwsVND%2BNCkL2i%2FmuQcckhK%2FBOs1wEfLq7QjmVrpOtNC206bwlwEmrs4Rmn5ucICDi%2FtA0xEfgTYNK7zVZpJnub18xSGpu112QV8EUbPq10YzQBkaTq4St%2BPJjBa7H%2FEua61t%2BivAi9wIcFaT6M6nV3fHjbnznbQ4P%2BTSB7T5DkYR69iWzGuy9MdqMO6vzM4GOqUBt3uu00d9CAEgMWmfiMREYuPEAcHV7IFxZPnXtPYD3o%2B2cgfQp%2BbS4tWnndg%2F97CUB1ucmXrGx1d1KD4%2F%2FVWp3T6o%2F%2B%2FafdLV7f1usg5iIHS5j%2B0e4Cf5UuQYYrTnIEB8UUEq%2FRBSOnOdY7IaZZNtjEV8NCdHrwzsr9Ca%2FrOjUlASFJm50EcOIQASwK6wtUPSiB7mCnDrLiBL2C6y0JZtkK3Vh7gv&X-Amz-Signature=aff126d12dc6b8f2a7d8b40fa5805e2d6ad7bbc4f1e0c72f042b0c2f2741a6c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDUAJIM%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLBK%2FBk%2BjcuF75KPDzP7Yfesj5BVA%2FVQyZvgJgbsH3oAiEAvoY7r6R55QKEB%2FQITHX%2Bj3e25Y9QzQ0zkHDGSUp2Fr8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC57iggRMfoPeQ0kNSrcAx4L0doBDTHmI24aPRy2tqx6KHNDywOG3HLb%2BB3J3vrPuRuQ3HvOF2%2BnNUcRax2Lbttunfemn8shrGz5hX8EDeVlZUZ17S1TnuIM2zlvPiUlfnlBZrfKWlBTDZXzfOgGgzI8O8gFkOR7nhgzi3snJqaYQerWW0F788FhO1Y7z%2B2yJ8otikHBHYy6R12ztAHx5SN1dtMNB9FgHY2qQOSTOwCSw9BRRof5%2F1gD12eXITsDoIuO%2FouwzNVN%2BpwqnAzWGluBkDxRus85BHAFWuVJ%2FfVaOmWscI1Ya4zEj9j%2By5BZeRWcknjIhG1nBPp8k9EMAcFH15K2HBbRv3Wh5m3chUhWI5c3vT62fKUA3QZLHacUnxSrVxNWpaiHjj2oMdv6Vqr4vZmQw2Pm8ETDFuUqDpvCk1pvQNCpkdREUWhnVTOZjfV9ib2F3eIbYnGi1%2FUGud03ZwsVND%2BNCkL2i%2FmuQcckhK%2FBOs1wEfLq7QjmVrpOtNC206bwlwEmrs4Rmn5ucICDi%2FtA0xEfgTYNK7zVZpJnub18xSGpu112QV8EUbPq10YzQBkaTq4St%2BPJjBa7H%2FEua61t%2BivAi9wIcFaT6M6nV3fHjbnznbQ4P%2BTSB7T5DkYR69iWzGuy9MdqMO6vzM4GOqUBt3uu00d9CAEgMWmfiMREYuPEAcHV7IFxZPnXtPYD3o%2B2cgfQp%2BbS4tWnndg%2F97CUB1ucmXrGx1d1KD4%2F%2FVWp3T6o%2F%2B%2FafdLV7f1usg5iIHS5j%2B0e4Cf5UuQYYrTnIEB8UUEq%2FRBSOnOdY7IaZZNtjEV8NCdHrwzsr9Ca%2FrOjUlASFJm50EcOIQASwK6wtUPSiB7mCnDrLiBL2C6y0JZtkK3Vh7gv&X-Amz-Signature=b04ca371cfd0062ab0856428344313cad71723c14fdd296eec2af8d35bd91221&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDUAJIM%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLBK%2FBk%2BjcuF75KPDzP7Yfesj5BVA%2FVQyZvgJgbsH3oAiEAvoY7r6R55QKEB%2FQITHX%2Bj3e25Y9QzQ0zkHDGSUp2Fr8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC57iggRMfoPeQ0kNSrcAx4L0doBDTHmI24aPRy2tqx6KHNDywOG3HLb%2BB3J3vrPuRuQ3HvOF2%2BnNUcRax2Lbttunfemn8shrGz5hX8EDeVlZUZ17S1TnuIM2zlvPiUlfnlBZrfKWlBTDZXzfOgGgzI8O8gFkOR7nhgzi3snJqaYQerWW0F788FhO1Y7z%2B2yJ8otikHBHYy6R12ztAHx5SN1dtMNB9FgHY2qQOSTOwCSw9BRRof5%2F1gD12eXITsDoIuO%2FouwzNVN%2BpwqnAzWGluBkDxRus85BHAFWuVJ%2FfVaOmWscI1Ya4zEj9j%2By5BZeRWcknjIhG1nBPp8k9EMAcFH15K2HBbRv3Wh5m3chUhWI5c3vT62fKUA3QZLHacUnxSrVxNWpaiHjj2oMdv6Vqr4vZmQw2Pm8ETDFuUqDpvCk1pvQNCpkdREUWhnVTOZjfV9ib2F3eIbYnGi1%2FUGud03ZwsVND%2BNCkL2i%2FmuQcckhK%2FBOs1wEfLq7QjmVrpOtNC206bwlwEmrs4Rmn5ucICDi%2FtA0xEfgTYNK7zVZpJnub18xSGpu112QV8EUbPq10YzQBkaTq4St%2BPJjBa7H%2FEua61t%2BivAi9wIcFaT6M6nV3fHjbnznbQ4P%2BTSB7T5DkYR69iWzGuy9MdqMO6vzM4GOqUBt3uu00d9CAEgMWmfiMREYuPEAcHV7IFxZPnXtPYD3o%2B2cgfQp%2BbS4tWnndg%2F97CUB1ucmXrGx1d1KD4%2F%2FVWp3T6o%2F%2B%2FafdLV7f1usg5iIHS5j%2B0e4Cf5UuQYYrTnIEB8UUEq%2FRBSOnOdY7IaZZNtjEV8NCdHrwzsr9Ca%2FrOjUlASFJm50EcOIQASwK6wtUPSiB7mCnDrLiBL2C6y0JZtkK3Vh7gv&X-Amz-Signature=230714554e55435c074ee3fe60ed7856aa3381bd46601b466d40ce5c4af9777f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDUAJIM%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLBK%2FBk%2BjcuF75KPDzP7Yfesj5BVA%2FVQyZvgJgbsH3oAiEAvoY7r6R55QKEB%2FQITHX%2Bj3e25Y9QzQ0zkHDGSUp2Fr8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC57iggRMfoPeQ0kNSrcAx4L0doBDTHmI24aPRy2tqx6KHNDywOG3HLb%2BB3J3vrPuRuQ3HvOF2%2BnNUcRax2Lbttunfemn8shrGz5hX8EDeVlZUZ17S1TnuIM2zlvPiUlfnlBZrfKWlBTDZXzfOgGgzI8O8gFkOR7nhgzi3snJqaYQerWW0F788FhO1Y7z%2B2yJ8otikHBHYy6R12ztAHx5SN1dtMNB9FgHY2qQOSTOwCSw9BRRof5%2F1gD12eXITsDoIuO%2FouwzNVN%2BpwqnAzWGluBkDxRus85BHAFWuVJ%2FfVaOmWscI1Ya4zEj9j%2By5BZeRWcknjIhG1nBPp8k9EMAcFH15K2HBbRv3Wh5m3chUhWI5c3vT62fKUA3QZLHacUnxSrVxNWpaiHjj2oMdv6Vqr4vZmQw2Pm8ETDFuUqDpvCk1pvQNCpkdREUWhnVTOZjfV9ib2F3eIbYnGi1%2FUGud03ZwsVND%2BNCkL2i%2FmuQcckhK%2FBOs1wEfLq7QjmVrpOtNC206bwlwEmrs4Rmn5ucICDi%2FtA0xEfgTYNK7zVZpJnub18xSGpu112QV8EUbPq10YzQBkaTq4St%2BPJjBa7H%2FEua61t%2BivAi9wIcFaT6M6nV3fHjbnznbQ4P%2BTSB7T5DkYR69iWzGuy9MdqMO6vzM4GOqUBt3uu00d9CAEgMWmfiMREYuPEAcHV7IFxZPnXtPYD3o%2B2cgfQp%2BbS4tWnndg%2F97CUB1ucmXrGx1d1KD4%2F%2FVWp3T6o%2F%2B%2FafdLV7f1usg5iIHS5j%2B0e4Cf5UuQYYrTnIEB8UUEq%2FRBSOnOdY7IaZZNtjEV8NCdHrwzsr9Ca%2FrOjUlASFJm50EcOIQASwK6wtUPSiB7mCnDrLiBL2C6y0JZtkK3Vh7gv&X-Amz-Signature=2e0920e2149dece41591864e5a970845d4ea37ce83df9222cb535066599a2dcb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDUAJIM%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLBK%2FBk%2BjcuF75KPDzP7Yfesj5BVA%2FVQyZvgJgbsH3oAiEAvoY7r6R55QKEB%2FQITHX%2Bj3e25Y9QzQ0zkHDGSUp2Fr8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC57iggRMfoPeQ0kNSrcAx4L0doBDTHmI24aPRy2tqx6KHNDywOG3HLb%2BB3J3vrPuRuQ3HvOF2%2BnNUcRax2Lbttunfemn8shrGz5hX8EDeVlZUZ17S1TnuIM2zlvPiUlfnlBZrfKWlBTDZXzfOgGgzI8O8gFkOR7nhgzi3snJqaYQerWW0F788FhO1Y7z%2B2yJ8otikHBHYy6R12ztAHx5SN1dtMNB9FgHY2qQOSTOwCSw9BRRof5%2F1gD12eXITsDoIuO%2FouwzNVN%2BpwqnAzWGluBkDxRus85BHAFWuVJ%2FfVaOmWscI1Ya4zEj9j%2By5BZeRWcknjIhG1nBPp8k9EMAcFH15K2HBbRv3Wh5m3chUhWI5c3vT62fKUA3QZLHacUnxSrVxNWpaiHjj2oMdv6Vqr4vZmQw2Pm8ETDFuUqDpvCk1pvQNCpkdREUWhnVTOZjfV9ib2F3eIbYnGi1%2FUGud03ZwsVND%2BNCkL2i%2FmuQcckhK%2FBOs1wEfLq7QjmVrpOtNC206bwlwEmrs4Rmn5ucICDi%2FtA0xEfgTYNK7zVZpJnub18xSGpu112QV8EUbPq10YzQBkaTq4St%2BPJjBa7H%2FEua61t%2BivAi9wIcFaT6M6nV3fHjbnznbQ4P%2BTSB7T5DkYR69iWzGuy9MdqMO6vzM4GOqUBt3uu00d9CAEgMWmfiMREYuPEAcHV7IFxZPnXtPYD3o%2B2cgfQp%2BbS4tWnndg%2F97CUB1ucmXrGx1d1KD4%2F%2FVWp3T6o%2F%2B%2FafdLV7f1usg5iIHS5j%2B0e4Cf5UuQYYrTnIEB8UUEq%2FRBSOnOdY7IaZZNtjEV8NCdHrwzsr9Ca%2FrOjUlASFJm50EcOIQASwK6wtUPSiB7mCnDrLiBL2C6y0JZtkK3Vh7gv&X-Amz-Signature=5a6f2f9b432f1c3fc92e9ba33a65c1f6b34a059b5bcf629a1e7e519b10ea28c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPDUAJIM%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLBK%2FBk%2BjcuF75KPDzP7Yfesj5BVA%2FVQyZvgJgbsH3oAiEAvoY7r6R55QKEB%2FQITHX%2Bj3e25Y9QzQ0zkHDGSUp2Fr8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC57iggRMfoPeQ0kNSrcAx4L0doBDTHmI24aPRy2tqx6KHNDywOG3HLb%2BB3J3vrPuRuQ3HvOF2%2BnNUcRax2Lbttunfemn8shrGz5hX8EDeVlZUZ17S1TnuIM2zlvPiUlfnlBZrfKWlBTDZXzfOgGgzI8O8gFkOR7nhgzi3snJqaYQerWW0F788FhO1Y7z%2B2yJ8otikHBHYy6R12ztAHx5SN1dtMNB9FgHY2qQOSTOwCSw9BRRof5%2F1gD12eXITsDoIuO%2FouwzNVN%2BpwqnAzWGluBkDxRus85BHAFWuVJ%2FfVaOmWscI1Ya4zEj9j%2By5BZeRWcknjIhG1nBPp8k9EMAcFH15K2HBbRv3Wh5m3chUhWI5c3vT62fKUA3QZLHacUnxSrVxNWpaiHjj2oMdv6Vqr4vZmQw2Pm8ETDFuUqDpvCk1pvQNCpkdREUWhnVTOZjfV9ib2F3eIbYnGi1%2FUGud03ZwsVND%2BNCkL2i%2FmuQcckhK%2FBOs1wEfLq7QjmVrpOtNC206bwlwEmrs4Rmn5ucICDi%2FtA0xEfgTYNK7zVZpJnub18xSGpu112QV8EUbPq10YzQBkaTq4St%2BPJjBa7H%2FEua61t%2BivAi9wIcFaT6M6nV3fHjbnznbQ4P%2BTSB7T5DkYR69iWzGuy9MdqMO6vzM4GOqUBt3uu00d9CAEgMWmfiMREYuPEAcHV7IFxZPnXtPYD3o%2B2cgfQp%2BbS4tWnndg%2F97CUB1ucmXrGx1d1KD4%2F%2FVWp3T6o%2F%2B%2FafdLV7f1usg5iIHS5j%2B0e4Cf5UuQYYrTnIEB8UUEq%2FRBSOnOdY7IaZZNtjEV8NCdHrwzsr9Ca%2FrOjUlASFJm50EcOIQASwK6wtUPSiB7mCnDrLiBL2C6y0JZtkK3Vh7gv&X-Amz-Signature=f91a55a7c3d02e95b768136dd160b226d9de5459efa3b680d59b322066804608&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

