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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGMYSWT%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAvBiGrAaqTT8wf28qAo2%2FtGUswmLwJPBg9FB4PSjMT4AiBe30L6Ba%2BGPcEhYw1XsJ98r4xbm%2FclKJaaRBzSwSPZzyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMKSZmsVXOe%2FIyGoSFKtwDyUGMVUsudeUaho01n8VhNlJU0sD4ncVpDWV2JuPRCEpXHcaKAlpc4AbZLPi2iLMg4cnMw%2BLhTLWXouIvhpu9mKP%2FzsaB05LS4WxmVycGIrai%2FTTQyoziTC9Zx7pNvn%2FouzE5mxMoDiXcAlZaIpRs48RQDbn%2B1GMupBEBMTJz%2Fh0lyb5rui3ixhbG9LSIPdLNNZ3gR5HZ%2Bkd%2B5WN0wcfnU%2Flnvw9HYU%2BNspjNoxT5rrZFSmxfLe1fgjstWZp5EScKCk3GYqiLHMHDD5qtNUIQWfsPEtvgCFRh0X4q9jso7dhit%2BjZcTmZEPMeKmVSrNmgYYLDCM3kyuT8nGxXPIpuuNDkykAuLALjF1w3bV13xy3gVbU%2BUK%2BqUsxs9UU0Hm0PtfgIcXa1wWaG3%2F0hD1%2FodWVxO1sMg6Xh%2BnLWmsrlQm1phT01hDempuJn5Hf%2BNYC4v7tHG3KtvEN0Z4rFx4cFGj%2BmbxLNs8rnRhcxg0rI%2BN9FCdZmljIL6pvOhQv4Q%2BGLQTXNAgDjv%2BA7zRVuPdtIX0krkaSMsW8eRvLsS4m69DXCixC%2B%2FulGWGLddfEyzBc2aKEB1YpknW%2BYjWiRwmWPb55fm8taClllb5g3HO8%2BAlJKDGTxWQPw05zy6hEwgZXKzAY6pgFxrFgGZ804c4NuRzv6ZQPwZNHQw5ZRVHTzNKpD86GlDLpbCM%2FionuOIW%2BCYq%2FcKLKTilh8Z8I3yl2Jwyw26hB%2FOr15tI058kqnHlCMXumEIafgtHXilVfiVnFcAVZR39XuKWiEi%2BcIL%2BEmGma0XUebCnwq%2F4%2FWsHJmsbbzABGY4mDr9wFfaZ7xTHTKL1wBe3jCvJJRcapHrivnUfIb8gLRMUxahenr&X-Amz-Signature=39cdeb8e52887dc6cb4ba06ca5139625d3e1ae104fa883fa97d1e702a71235c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGMYSWT%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAvBiGrAaqTT8wf28qAo2%2FtGUswmLwJPBg9FB4PSjMT4AiBe30L6Ba%2BGPcEhYw1XsJ98r4xbm%2FclKJaaRBzSwSPZzyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMKSZmsVXOe%2FIyGoSFKtwDyUGMVUsudeUaho01n8VhNlJU0sD4ncVpDWV2JuPRCEpXHcaKAlpc4AbZLPi2iLMg4cnMw%2BLhTLWXouIvhpu9mKP%2FzsaB05LS4WxmVycGIrai%2FTTQyoziTC9Zx7pNvn%2FouzE5mxMoDiXcAlZaIpRs48RQDbn%2B1GMupBEBMTJz%2Fh0lyb5rui3ixhbG9LSIPdLNNZ3gR5HZ%2Bkd%2B5WN0wcfnU%2Flnvw9HYU%2BNspjNoxT5rrZFSmxfLe1fgjstWZp5EScKCk3GYqiLHMHDD5qtNUIQWfsPEtvgCFRh0X4q9jso7dhit%2BjZcTmZEPMeKmVSrNmgYYLDCM3kyuT8nGxXPIpuuNDkykAuLALjF1w3bV13xy3gVbU%2BUK%2BqUsxs9UU0Hm0PtfgIcXa1wWaG3%2F0hD1%2FodWVxO1sMg6Xh%2BnLWmsrlQm1phT01hDempuJn5Hf%2BNYC4v7tHG3KtvEN0Z4rFx4cFGj%2BmbxLNs8rnRhcxg0rI%2BN9FCdZmljIL6pvOhQv4Q%2BGLQTXNAgDjv%2BA7zRVuPdtIX0krkaSMsW8eRvLsS4m69DXCixC%2B%2FulGWGLddfEyzBc2aKEB1YpknW%2BYjWiRwmWPb55fm8taClllb5g3HO8%2BAlJKDGTxWQPw05zy6hEwgZXKzAY6pgFxrFgGZ804c4NuRzv6ZQPwZNHQw5ZRVHTzNKpD86GlDLpbCM%2FionuOIW%2BCYq%2FcKLKTilh8Z8I3yl2Jwyw26hB%2FOr15tI058kqnHlCMXumEIafgtHXilVfiVnFcAVZR39XuKWiEi%2BcIL%2BEmGma0XUebCnwq%2F4%2FWsHJmsbbzABGY4mDr9wFfaZ7xTHTKL1wBe3jCvJJRcapHrivnUfIb8gLRMUxahenr&X-Amz-Signature=813da7bfbdb854139521cc9d75d0532076979e98cf40f8547082edd9dc8a8c6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGMYSWT%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAvBiGrAaqTT8wf28qAo2%2FtGUswmLwJPBg9FB4PSjMT4AiBe30L6Ba%2BGPcEhYw1XsJ98r4xbm%2FclKJaaRBzSwSPZzyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMKSZmsVXOe%2FIyGoSFKtwDyUGMVUsudeUaho01n8VhNlJU0sD4ncVpDWV2JuPRCEpXHcaKAlpc4AbZLPi2iLMg4cnMw%2BLhTLWXouIvhpu9mKP%2FzsaB05LS4WxmVycGIrai%2FTTQyoziTC9Zx7pNvn%2FouzE5mxMoDiXcAlZaIpRs48RQDbn%2B1GMupBEBMTJz%2Fh0lyb5rui3ixhbG9LSIPdLNNZ3gR5HZ%2Bkd%2B5WN0wcfnU%2Flnvw9HYU%2BNspjNoxT5rrZFSmxfLe1fgjstWZp5EScKCk3GYqiLHMHDD5qtNUIQWfsPEtvgCFRh0X4q9jso7dhit%2BjZcTmZEPMeKmVSrNmgYYLDCM3kyuT8nGxXPIpuuNDkykAuLALjF1w3bV13xy3gVbU%2BUK%2BqUsxs9UU0Hm0PtfgIcXa1wWaG3%2F0hD1%2FodWVxO1sMg6Xh%2BnLWmsrlQm1phT01hDempuJn5Hf%2BNYC4v7tHG3KtvEN0Z4rFx4cFGj%2BmbxLNs8rnRhcxg0rI%2BN9FCdZmljIL6pvOhQv4Q%2BGLQTXNAgDjv%2BA7zRVuPdtIX0krkaSMsW8eRvLsS4m69DXCixC%2B%2FulGWGLddfEyzBc2aKEB1YpknW%2BYjWiRwmWPb55fm8taClllb5g3HO8%2BAlJKDGTxWQPw05zy6hEwgZXKzAY6pgFxrFgGZ804c4NuRzv6ZQPwZNHQw5ZRVHTzNKpD86GlDLpbCM%2FionuOIW%2BCYq%2FcKLKTilh8Z8I3yl2Jwyw26hB%2FOr15tI058kqnHlCMXumEIafgtHXilVfiVnFcAVZR39XuKWiEi%2BcIL%2BEmGma0XUebCnwq%2F4%2FWsHJmsbbzABGY4mDr9wFfaZ7xTHTKL1wBe3jCvJJRcapHrivnUfIb8gLRMUxahenr&X-Amz-Signature=e149d56ebd9d810294392c25ecd9f7c6ee83c0389b9fc064362a99e7daffdbf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGMYSWT%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAvBiGrAaqTT8wf28qAo2%2FtGUswmLwJPBg9FB4PSjMT4AiBe30L6Ba%2BGPcEhYw1XsJ98r4xbm%2FclKJaaRBzSwSPZzyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMKSZmsVXOe%2FIyGoSFKtwDyUGMVUsudeUaho01n8VhNlJU0sD4ncVpDWV2JuPRCEpXHcaKAlpc4AbZLPi2iLMg4cnMw%2BLhTLWXouIvhpu9mKP%2FzsaB05LS4WxmVycGIrai%2FTTQyoziTC9Zx7pNvn%2FouzE5mxMoDiXcAlZaIpRs48RQDbn%2B1GMupBEBMTJz%2Fh0lyb5rui3ixhbG9LSIPdLNNZ3gR5HZ%2Bkd%2B5WN0wcfnU%2Flnvw9HYU%2BNspjNoxT5rrZFSmxfLe1fgjstWZp5EScKCk3GYqiLHMHDD5qtNUIQWfsPEtvgCFRh0X4q9jso7dhit%2BjZcTmZEPMeKmVSrNmgYYLDCM3kyuT8nGxXPIpuuNDkykAuLALjF1w3bV13xy3gVbU%2BUK%2BqUsxs9UU0Hm0PtfgIcXa1wWaG3%2F0hD1%2FodWVxO1sMg6Xh%2BnLWmsrlQm1phT01hDempuJn5Hf%2BNYC4v7tHG3KtvEN0Z4rFx4cFGj%2BmbxLNs8rnRhcxg0rI%2BN9FCdZmljIL6pvOhQv4Q%2BGLQTXNAgDjv%2BA7zRVuPdtIX0krkaSMsW8eRvLsS4m69DXCixC%2B%2FulGWGLddfEyzBc2aKEB1YpknW%2BYjWiRwmWPb55fm8taClllb5g3HO8%2BAlJKDGTxWQPw05zy6hEwgZXKzAY6pgFxrFgGZ804c4NuRzv6ZQPwZNHQw5ZRVHTzNKpD86GlDLpbCM%2FionuOIW%2BCYq%2FcKLKTilh8Z8I3yl2Jwyw26hB%2FOr15tI058kqnHlCMXumEIafgtHXilVfiVnFcAVZR39XuKWiEi%2BcIL%2BEmGma0XUebCnwq%2F4%2FWsHJmsbbzABGY4mDr9wFfaZ7xTHTKL1wBe3jCvJJRcapHrivnUfIb8gLRMUxahenr&X-Amz-Signature=9cffd86bebfe1a0802632c6128122a1738c9ded5232ef3e5c25818f941994cc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGMYSWT%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAvBiGrAaqTT8wf28qAo2%2FtGUswmLwJPBg9FB4PSjMT4AiBe30L6Ba%2BGPcEhYw1XsJ98r4xbm%2FclKJaaRBzSwSPZzyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMKSZmsVXOe%2FIyGoSFKtwDyUGMVUsudeUaho01n8VhNlJU0sD4ncVpDWV2JuPRCEpXHcaKAlpc4AbZLPi2iLMg4cnMw%2BLhTLWXouIvhpu9mKP%2FzsaB05LS4WxmVycGIrai%2FTTQyoziTC9Zx7pNvn%2FouzE5mxMoDiXcAlZaIpRs48RQDbn%2B1GMupBEBMTJz%2Fh0lyb5rui3ixhbG9LSIPdLNNZ3gR5HZ%2Bkd%2B5WN0wcfnU%2Flnvw9HYU%2BNspjNoxT5rrZFSmxfLe1fgjstWZp5EScKCk3GYqiLHMHDD5qtNUIQWfsPEtvgCFRh0X4q9jso7dhit%2BjZcTmZEPMeKmVSrNmgYYLDCM3kyuT8nGxXPIpuuNDkykAuLALjF1w3bV13xy3gVbU%2BUK%2BqUsxs9UU0Hm0PtfgIcXa1wWaG3%2F0hD1%2FodWVxO1sMg6Xh%2BnLWmsrlQm1phT01hDempuJn5Hf%2BNYC4v7tHG3KtvEN0Z4rFx4cFGj%2BmbxLNs8rnRhcxg0rI%2BN9FCdZmljIL6pvOhQv4Q%2BGLQTXNAgDjv%2BA7zRVuPdtIX0krkaSMsW8eRvLsS4m69DXCixC%2B%2FulGWGLddfEyzBc2aKEB1YpknW%2BYjWiRwmWPb55fm8taClllb5g3HO8%2BAlJKDGTxWQPw05zy6hEwgZXKzAY6pgFxrFgGZ804c4NuRzv6ZQPwZNHQw5ZRVHTzNKpD86GlDLpbCM%2FionuOIW%2BCYq%2FcKLKTilh8Z8I3yl2Jwyw26hB%2FOr15tI058kqnHlCMXumEIafgtHXilVfiVnFcAVZR39XuKWiEi%2BcIL%2BEmGma0XUebCnwq%2F4%2FWsHJmsbbzABGY4mDr9wFfaZ7xTHTKL1wBe3jCvJJRcapHrivnUfIb8gLRMUxahenr&X-Amz-Signature=00bc533d75785630cb6a96df6a1eae8dd93efe15163eb4e53dbdce35fb322141&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGMYSWT%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAvBiGrAaqTT8wf28qAo2%2FtGUswmLwJPBg9FB4PSjMT4AiBe30L6Ba%2BGPcEhYw1XsJ98r4xbm%2FclKJaaRBzSwSPZzyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMKSZmsVXOe%2FIyGoSFKtwDyUGMVUsudeUaho01n8VhNlJU0sD4ncVpDWV2JuPRCEpXHcaKAlpc4AbZLPi2iLMg4cnMw%2BLhTLWXouIvhpu9mKP%2FzsaB05LS4WxmVycGIrai%2FTTQyoziTC9Zx7pNvn%2FouzE5mxMoDiXcAlZaIpRs48RQDbn%2B1GMupBEBMTJz%2Fh0lyb5rui3ixhbG9LSIPdLNNZ3gR5HZ%2Bkd%2B5WN0wcfnU%2Flnvw9HYU%2BNspjNoxT5rrZFSmxfLe1fgjstWZp5EScKCk3GYqiLHMHDD5qtNUIQWfsPEtvgCFRh0X4q9jso7dhit%2BjZcTmZEPMeKmVSrNmgYYLDCM3kyuT8nGxXPIpuuNDkykAuLALjF1w3bV13xy3gVbU%2BUK%2BqUsxs9UU0Hm0PtfgIcXa1wWaG3%2F0hD1%2FodWVxO1sMg6Xh%2BnLWmsrlQm1phT01hDempuJn5Hf%2BNYC4v7tHG3KtvEN0Z4rFx4cFGj%2BmbxLNs8rnRhcxg0rI%2BN9FCdZmljIL6pvOhQv4Q%2BGLQTXNAgDjv%2BA7zRVuPdtIX0krkaSMsW8eRvLsS4m69DXCixC%2B%2FulGWGLddfEyzBc2aKEB1YpknW%2BYjWiRwmWPb55fm8taClllb5g3HO8%2BAlJKDGTxWQPw05zy6hEwgZXKzAY6pgFxrFgGZ804c4NuRzv6ZQPwZNHQw5ZRVHTzNKpD86GlDLpbCM%2FionuOIW%2BCYq%2FcKLKTilh8Z8I3yl2Jwyw26hB%2FOr15tI058kqnHlCMXumEIafgtHXilVfiVnFcAVZR39XuKWiEi%2BcIL%2BEmGma0XUebCnwq%2F4%2FWsHJmsbbzABGY4mDr9wFfaZ7xTHTKL1wBe3jCvJJRcapHrivnUfIb8gLRMUxahenr&X-Amz-Signature=01119d33d2613d8822db15d23d8a2077afaac65638172a61a6de5ed237a9a4df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGMYSWT%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAvBiGrAaqTT8wf28qAo2%2FtGUswmLwJPBg9FB4PSjMT4AiBe30L6Ba%2BGPcEhYw1XsJ98r4xbm%2FclKJaaRBzSwSPZzyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMKSZmsVXOe%2FIyGoSFKtwDyUGMVUsudeUaho01n8VhNlJU0sD4ncVpDWV2JuPRCEpXHcaKAlpc4AbZLPi2iLMg4cnMw%2BLhTLWXouIvhpu9mKP%2FzsaB05LS4WxmVycGIrai%2FTTQyoziTC9Zx7pNvn%2FouzE5mxMoDiXcAlZaIpRs48RQDbn%2B1GMupBEBMTJz%2Fh0lyb5rui3ixhbG9LSIPdLNNZ3gR5HZ%2Bkd%2B5WN0wcfnU%2Flnvw9HYU%2BNspjNoxT5rrZFSmxfLe1fgjstWZp5EScKCk3GYqiLHMHDD5qtNUIQWfsPEtvgCFRh0X4q9jso7dhit%2BjZcTmZEPMeKmVSrNmgYYLDCM3kyuT8nGxXPIpuuNDkykAuLALjF1w3bV13xy3gVbU%2BUK%2BqUsxs9UU0Hm0PtfgIcXa1wWaG3%2F0hD1%2FodWVxO1sMg6Xh%2BnLWmsrlQm1phT01hDempuJn5Hf%2BNYC4v7tHG3KtvEN0Z4rFx4cFGj%2BmbxLNs8rnRhcxg0rI%2BN9FCdZmljIL6pvOhQv4Q%2BGLQTXNAgDjv%2BA7zRVuPdtIX0krkaSMsW8eRvLsS4m69DXCixC%2B%2FulGWGLddfEyzBc2aKEB1YpknW%2BYjWiRwmWPb55fm8taClllb5g3HO8%2BAlJKDGTxWQPw05zy6hEwgZXKzAY6pgFxrFgGZ804c4NuRzv6ZQPwZNHQw5ZRVHTzNKpD86GlDLpbCM%2FionuOIW%2BCYq%2FcKLKTilh8Z8I3yl2Jwyw26hB%2FOr15tI058kqnHlCMXumEIafgtHXilVfiVnFcAVZR39XuKWiEi%2BcIL%2BEmGma0XUebCnwq%2F4%2FWsHJmsbbzABGY4mDr9wFfaZ7xTHTKL1wBe3jCvJJRcapHrivnUfIb8gLRMUxahenr&X-Amz-Signature=841985dcc0b05964e062bc755a008a62c35e1340e0285311f73ac42ce9ff2f96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGMYSWT%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAvBiGrAaqTT8wf28qAo2%2FtGUswmLwJPBg9FB4PSjMT4AiBe30L6Ba%2BGPcEhYw1XsJ98r4xbm%2FclKJaaRBzSwSPZzyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMKSZmsVXOe%2FIyGoSFKtwDyUGMVUsudeUaho01n8VhNlJU0sD4ncVpDWV2JuPRCEpXHcaKAlpc4AbZLPi2iLMg4cnMw%2BLhTLWXouIvhpu9mKP%2FzsaB05LS4WxmVycGIrai%2FTTQyoziTC9Zx7pNvn%2FouzE5mxMoDiXcAlZaIpRs48RQDbn%2B1GMupBEBMTJz%2Fh0lyb5rui3ixhbG9LSIPdLNNZ3gR5HZ%2Bkd%2B5WN0wcfnU%2Flnvw9HYU%2BNspjNoxT5rrZFSmxfLe1fgjstWZp5EScKCk3GYqiLHMHDD5qtNUIQWfsPEtvgCFRh0X4q9jso7dhit%2BjZcTmZEPMeKmVSrNmgYYLDCM3kyuT8nGxXPIpuuNDkykAuLALjF1w3bV13xy3gVbU%2BUK%2BqUsxs9UU0Hm0PtfgIcXa1wWaG3%2F0hD1%2FodWVxO1sMg6Xh%2BnLWmsrlQm1phT01hDempuJn5Hf%2BNYC4v7tHG3KtvEN0Z4rFx4cFGj%2BmbxLNs8rnRhcxg0rI%2BN9FCdZmljIL6pvOhQv4Q%2BGLQTXNAgDjv%2BA7zRVuPdtIX0krkaSMsW8eRvLsS4m69DXCixC%2B%2FulGWGLddfEyzBc2aKEB1YpknW%2BYjWiRwmWPb55fm8taClllb5g3HO8%2BAlJKDGTxWQPw05zy6hEwgZXKzAY6pgFxrFgGZ804c4NuRzv6ZQPwZNHQw5ZRVHTzNKpD86GlDLpbCM%2FionuOIW%2BCYq%2FcKLKTilh8Z8I3yl2Jwyw26hB%2FOr15tI058kqnHlCMXumEIafgtHXilVfiVnFcAVZR39XuKWiEi%2BcIL%2BEmGma0XUebCnwq%2F4%2FWsHJmsbbzABGY4mDr9wFfaZ7xTHTKL1wBe3jCvJJRcapHrivnUfIb8gLRMUxahenr&X-Amz-Signature=f436bd6dd231d4d122b6c434eba89e2e93bd525daf2dab969121946a0e2b13ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGMYSWT%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAvBiGrAaqTT8wf28qAo2%2FtGUswmLwJPBg9FB4PSjMT4AiBe30L6Ba%2BGPcEhYw1XsJ98r4xbm%2FclKJaaRBzSwSPZzyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMKSZmsVXOe%2FIyGoSFKtwDyUGMVUsudeUaho01n8VhNlJU0sD4ncVpDWV2JuPRCEpXHcaKAlpc4AbZLPi2iLMg4cnMw%2BLhTLWXouIvhpu9mKP%2FzsaB05LS4WxmVycGIrai%2FTTQyoziTC9Zx7pNvn%2FouzE5mxMoDiXcAlZaIpRs48RQDbn%2B1GMupBEBMTJz%2Fh0lyb5rui3ixhbG9LSIPdLNNZ3gR5HZ%2Bkd%2B5WN0wcfnU%2Flnvw9HYU%2BNspjNoxT5rrZFSmxfLe1fgjstWZp5EScKCk3GYqiLHMHDD5qtNUIQWfsPEtvgCFRh0X4q9jso7dhit%2BjZcTmZEPMeKmVSrNmgYYLDCM3kyuT8nGxXPIpuuNDkykAuLALjF1w3bV13xy3gVbU%2BUK%2BqUsxs9UU0Hm0PtfgIcXa1wWaG3%2F0hD1%2FodWVxO1sMg6Xh%2BnLWmsrlQm1phT01hDempuJn5Hf%2BNYC4v7tHG3KtvEN0Z4rFx4cFGj%2BmbxLNs8rnRhcxg0rI%2BN9FCdZmljIL6pvOhQv4Q%2BGLQTXNAgDjv%2BA7zRVuPdtIX0krkaSMsW8eRvLsS4m69DXCixC%2B%2FulGWGLddfEyzBc2aKEB1YpknW%2BYjWiRwmWPb55fm8taClllb5g3HO8%2BAlJKDGTxWQPw05zy6hEwgZXKzAY6pgFxrFgGZ804c4NuRzv6ZQPwZNHQw5ZRVHTzNKpD86GlDLpbCM%2FionuOIW%2BCYq%2FcKLKTilh8Z8I3yl2Jwyw26hB%2FOr15tI058kqnHlCMXumEIafgtHXilVfiVnFcAVZR39XuKWiEi%2BcIL%2BEmGma0XUebCnwq%2F4%2FWsHJmsbbzABGY4mDr9wFfaZ7xTHTKL1wBe3jCvJJRcapHrivnUfIb8gLRMUxahenr&X-Amz-Signature=e185aa28cea12d340b468a7cdf10692b24e644908c990b50e49a85415d8a3b5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFGMYSWT%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAvBiGrAaqTT8wf28qAo2%2FtGUswmLwJPBg9FB4PSjMT4AiBe30L6Ba%2BGPcEhYw1XsJ98r4xbm%2FclKJaaRBzSwSPZzyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMKSZmsVXOe%2FIyGoSFKtwDyUGMVUsudeUaho01n8VhNlJU0sD4ncVpDWV2JuPRCEpXHcaKAlpc4AbZLPi2iLMg4cnMw%2BLhTLWXouIvhpu9mKP%2FzsaB05LS4WxmVycGIrai%2FTTQyoziTC9Zx7pNvn%2FouzE5mxMoDiXcAlZaIpRs48RQDbn%2B1GMupBEBMTJz%2Fh0lyb5rui3ixhbG9LSIPdLNNZ3gR5HZ%2Bkd%2B5WN0wcfnU%2Flnvw9HYU%2BNspjNoxT5rrZFSmxfLe1fgjstWZp5EScKCk3GYqiLHMHDD5qtNUIQWfsPEtvgCFRh0X4q9jso7dhit%2BjZcTmZEPMeKmVSrNmgYYLDCM3kyuT8nGxXPIpuuNDkykAuLALjF1w3bV13xy3gVbU%2BUK%2BqUsxs9UU0Hm0PtfgIcXa1wWaG3%2F0hD1%2FodWVxO1sMg6Xh%2BnLWmsrlQm1phT01hDempuJn5Hf%2BNYC4v7tHG3KtvEN0Z4rFx4cFGj%2BmbxLNs8rnRhcxg0rI%2BN9FCdZmljIL6pvOhQv4Q%2BGLQTXNAgDjv%2BA7zRVuPdtIX0krkaSMsW8eRvLsS4m69DXCixC%2B%2FulGWGLddfEyzBc2aKEB1YpknW%2BYjWiRwmWPb55fm8taClllb5g3HO8%2BAlJKDGTxWQPw05zy6hEwgZXKzAY6pgFxrFgGZ804c4NuRzv6ZQPwZNHQw5ZRVHTzNKpD86GlDLpbCM%2FionuOIW%2BCYq%2FcKLKTilh8Z8I3yl2Jwyw26hB%2FOr15tI058kqnHlCMXumEIafgtHXilVfiVnFcAVZR39XuKWiEi%2BcIL%2BEmGma0XUebCnwq%2F4%2FWsHJmsbbzABGY4mDr9wFfaZ7xTHTKL1wBe3jCvJJRcapHrivnUfIb8gLRMUxahenr&X-Amz-Signature=4fb8ce4adc93087fa3d17dc69457a8cbb45e4b7e2066cd0f12fa8e565c0c027e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

