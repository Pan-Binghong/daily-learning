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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26AKWO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDfNJPUDg9JCDc1hCC9CjOe7AYLx8vPLsFKEWi9MOewDQIgIGTuzBnfUvxqwUAL2Uv5krgSPAEO%2BRPNUNprgOx0EQkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDC51%2F4%2B5tO6iFoSkIyrcA1H340nLh5kAGx15Ctfnw%2BqLXaHwyRCi88L%2BaZ2QSDDdvU5iH%2FRhY3SFbcTdLJGYXH2qlDVtthdeETs42JiYvbeoBoTzJF379DH1W8BOGInoH36TuTlT%2FsdEVPOvQU7NLzzds8IIN56LLumLIq4bdDEYianQzKHCzXmUsPUBJqBKoO%2BjgZf%2BwiGgJw0eqbF3FqpvpIPN8mAO0WaK0tVRHs36Rg8Hlty5LxAc62qY65%2BAaVLVhiKmUmnpDfEVTeH8AL0ikSZ4G3vvTGc6o%2F9w8y8HvdGefXdIU4u9RE1HCLCeDl%2F9wwQkCAaqSWvMuWM538OVlpK2db83z6%2BkkVxXA%2F5yusAme2LqVCD5ctBPx94NzPC5w8m5mbsIeYyjO0cqof2pg6qUF9oD5WAw0juvYulox%2BVqwG83TgW7bozCZKTbpjajuO0D3E4yfECV%2Fw9g8EDJd2lD5uCqSkNI%2FBMDWJuSk8lHacSyDJILpy2HubWpHz%2FFSJRhx2trxh8TkkvV7QTUCveQhUxHyhVaf%2Bxb%2BlQNr4rsYickucdYg4NLcRO0SBC2PTBbupaOVWtAgyIBJZ1lZBxNbJBSdewRq%2B%2BbS2gwdi08pFRF5xvUWHCRezdidj1oHY54DNl%2F6j3IMJqN88kGOqUBjT0GcZMGOsNswMvwRW4LwT%2Fckzt7OhrTGh6SjXxFOOOJ6Z2%2BETv72%2FRfeJEynb%2FSRpjB%2BYNiB7NmIkmJPqY%2FUfRGht56GXtceOQgk8kWpKIQrKe2v0LA4PApDNBt3Ol6AG%2FZcwzMV0%2BzfSRPxb3llf8jGw729iAwyed1zsWW84UVnxYE%2BWGI7LgRFNDJfI%2B9QKXfspb%2BhEEkUEYkMWu7F8DA8l4U&X-Amz-Signature=0831ebbb92b85dc676b81a733d91f158c92e83ecad61a451e264d8d2b79b72ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26AKWO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDfNJPUDg9JCDc1hCC9CjOe7AYLx8vPLsFKEWi9MOewDQIgIGTuzBnfUvxqwUAL2Uv5krgSPAEO%2BRPNUNprgOx0EQkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDC51%2F4%2B5tO6iFoSkIyrcA1H340nLh5kAGx15Ctfnw%2BqLXaHwyRCi88L%2BaZ2QSDDdvU5iH%2FRhY3SFbcTdLJGYXH2qlDVtthdeETs42JiYvbeoBoTzJF379DH1W8BOGInoH36TuTlT%2FsdEVPOvQU7NLzzds8IIN56LLumLIq4bdDEYianQzKHCzXmUsPUBJqBKoO%2BjgZf%2BwiGgJw0eqbF3FqpvpIPN8mAO0WaK0tVRHs36Rg8Hlty5LxAc62qY65%2BAaVLVhiKmUmnpDfEVTeH8AL0ikSZ4G3vvTGc6o%2F9w8y8HvdGefXdIU4u9RE1HCLCeDl%2F9wwQkCAaqSWvMuWM538OVlpK2db83z6%2BkkVxXA%2F5yusAme2LqVCD5ctBPx94NzPC5w8m5mbsIeYyjO0cqof2pg6qUF9oD5WAw0juvYulox%2BVqwG83TgW7bozCZKTbpjajuO0D3E4yfECV%2Fw9g8EDJd2lD5uCqSkNI%2FBMDWJuSk8lHacSyDJILpy2HubWpHz%2FFSJRhx2trxh8TkkvV7QTUCveQhUxHyhVaf%2Bxb%2BlQNr4rsYickucdYg4NLcRO0SBC2PTBbupaOVWtAgyIBJZ1lZBxNbJBSdewRq%2B%2BbS2gwdi08pFRF5xvUWHCRezdidj1oHY54DNl%2F6j3IMJqN88kGOqUBjT0GcZMGOsNswMvwRW4LwT%2Fckzt7OhrTGh6SjXxFOOOJ6Z2%2BETv72%2FRfeJEynb%2FSRpjB%2BYNiB7NmIkmJPqY%2FUfRGht56GXtceOQgk8kWpKIQrKe2v0LA4PApDNBt3Ol6AG%2FZcwzMV0%2BzfSRPxb3llf8jGw729iAwyed1zsWW84UVnxYE%2BWGI7LgRFNDJfI%2B9QKXfspb%2BhEEkUEYkMWu7F8DA8l4U&X-Amz-Signature=f7663801fcc489db5b3994381ce62746a965314920929c41e2690b339139b4fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26AKWO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDfNJPUDg9JCDc1hCC9CjOe7AYLx8vPLsFKEWi9MOewDQIgIGTuzBnfUvxqwUAL2Uv5krgSPAEO%2BRPNUNprgOx0EQkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDC51%2F4%2B5tO6iFoSkIyrcA1H340nLh5kAGx15Ctfnw%2BqLXaHwyRCi88L%2BaZ2QSDDdvU5iH%2FRhY3SFbcTdLJGYXH2qlDVtthdeETs42JiYvbeoBoTzJF379DH1W8BOGInoH36TuTlT%2FsdEVPOvQU7NLzzds8IIN56LLumLIq4bdDEYianQzKHCzXmUsPUBJqBKoO%2BjgZf%2BwiGgJw0eqbF3FqpvpIPN8mAO0WaK0tVRHs36Rg8Hlty5LxAc62qY65%2BAaVLVhiKmUmnpDfEVTeH8AL0ikSZ4G3vvTGc6o%2F9w8y8HvdGefXdIU4u9RE1HCLCeDl%2F9wwQkCAaqSWvMuWM538OVlpK2db83z6%2BkkVxXA%2F5yusAme2LqVCD5ctBPx94NzPC5w8m5mbsIeYyjO0cqof2pg6qUF9oD5WAw0juvYulox%2BVqwG83TgW7bozCZKTbpjajuO0D3E4yfECV%2Fw9g8EDJd2lD5uCqSkNI%2FBMDWJuSk8lHacSyDJILpy2HubWpHz%2FFSJRhx2trxh8TkkvV7QTUCveQhUxHyhVaf%2Bxb%2BlQNr4rsYickucdYg4NLcRO0SBC2PTBbupaOVWtAgyIBJZ1lZBxNbJBSdewRq%2B%2BbS2gwdi08pFRF5xvUWHCRezdidj1oHY54DNl%2F6j3IMJqN88kGOqUBjT0GcZMGOsNswMvwRW4LwT%2Fckzt7OhrTGh6SjXxFOOOJ6Z2%2BETv72%2FRfeJEynb%2FSRpjB%2BYNiB7NmIkmJPqY%2FUfRGht56GXtceOQgk8kWpKIQrKe2v0LA4PApDNBt3Ol6AG%2FZcwzMV0%2BzfSRPxb3llf8jGw729iAwyed1zsWW84UVnxYE%2BWGI7LgRFNDJfI%2B9QKXfspb%2BhEEkUEYkMWu7F8DA8l4U&X-Amz-Signature=c6fd2da0ccbac62d32ccefd71806b35b1da5a1f6872e3d9cf4ec34ec615e788d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26AKWO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDfNJPUDg9JCDc1hCC9CjOe7AYLx8vPLsFKEWi9MOewDQIgIGTuzBnfUvxqwUAL2Uv5krgSPAEO%2BRPNUNprgOx0EQkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDC51%2F4%2B5tO6iFoSkIyrcA1H340nLh5kAGx15Ctfnw%2BqLXaHwyRCi88L%2BaZ2QSDDdvU5iH%2FRhY3SFbcTdLJGYXH2qlDVtthdeETs42JiYvbeoBoTzJF379DH1W8BOGInoH36TuTlT%2FsdEVPOvQU7NLzzds8IIN56LLumLIq4bdDEYianQzKHCzXmUsPUBJqBKoO%2BjgZf%2BwiGgJw0eqbF3FqpvpIPN8mAO0WaK0tVRHs36Rg8Hlty5LxAc62qY65%2BAaVLVhiKmUmnpDfEVTeH8AL0ikSZ4G3vvTGc6o%2F9w8y8HvdGefXdIU4u9RE1HCLCeDl%2F9wwQkCAaqSWvMuWM538OVlpK2db83z6%2BkkVxXA%2F5yusAme2LqVCD5ctBPx94NzPC5w8m5mbsIeYyjO0cqof2pg6qUF9oD5WAw0juvYulox%2BVqwG83TgW7bozCZKTbpjajuO0D3E4yfECV%2Fw9g8EDJd2lD5uCqSkNI%2FBMDWJuSk8lHacSyDJILpy2HubWpHz%2FFSJRhx2trxh8TkkvV7QTUCveQhUxHyhVaf%2Bxb%2BlQNr4rsYickucdYg4NLcRO0SBC2PTBbupaOVWtAgyIBJZ1lZBxNbJBSdewRq%2B%2BbS2gwdi08pFRF5xvUWHCRezdidj1oHY54DNl%2F6j3IMJqN88kGOqUBjT0GcZMGOsNswMvwRW4LwT%2Fckzt7OhrTGh6SjXxFOOOJ6Z2%2BETv72%2FRfeJEynb%2FSRpjB%2BYNiB7NmIkmJPqY%2FUfRGht56GXtceOQgk8kWpKIQrKe2v0LA4PApDNBt3Ol6AG%2FZcwzMV0%2BzfSRPxb3llf8jGw729iAwyed1zsWW84UVnxYE%2BWGI7LgRFNDJfI%2B9QKXfspb%2BhEEkUEYkMWu7F8DA8l4U&X-Amz-Signature=3932be3f3045ce94653a659b4bb7eb3b7bb3b5498a915f94a1a85004e9e18d16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26AKWO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDfNJPUDg9JCDc1hCC9CjOe7AYLx8vPLsFKEWi9MOewDQIgIGTuzBnfUvxqwUAL2Uv5krgSPAEO%2BRPNUNprgOx0EQkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDC51%2F4%2B5tO6iFoSkIyrcA1H340nLh5kAGx15Ctfnw%2BqLXaHwyRCi88L%2BaZ2QSDDdvU5iH%2FRhY3SFbcTdLJGYXH2qlDVtthdeETs42JiYvbeoBoTzJF379DH1W8BOGInoH36TuTlT%2FsdEVPOvQU7NLzzds8IIN56LLumLIq4bdDEYianQzKHCzXmUsPUBJqBKoO%2BjgZf%2BwiGgJw0eqbF3FqpvpIPN8mAO0WaK0tVRHs36Rg8Hlty5LxAc62qY65%2BAaVLVhiKmUmnpDfEVTeH8AL0ikSZ4G3vvTGc6o%2F9w8y8HvdGefXdIU4u9RE1HCLCeDl%2F9wwQkCAaqSWvMuWM538OVlpK2db83z6%2BkkVxXA%2F5yusAme2LqVCD5ctBPx94NzPC5w8m5mbsIeYyjO0cqof2pg6qUF9oD5WAw0juvYulox%2BVqwG83TgW7bozCZKTbpjajuO0D3E4yfECV%2Fw9g8EDJd2lD5uCqSkNI%2FBMDWJuSk8lHacSyDJILpy2HubWpHz%2FFSJRhx2trxh8TkkvV7QTUCveQhUxHyhVaf%2Bxb%2BlQNr4rsYickucdYg4NLcRO0SBC2PTBbupaOVWtAgyIBJZ1lZBxNbJBSdewRq%2B%2BbS2gwdi08pFRF5xvUWHCRezdidj1oHY54DNl%2F6j3IMJqN88kGOqUBjT0GcZMGOsNswMvwRW4LwT%2Fckzt7OhrTGh6SjXxFOOOJ6Z2%2BETv72%2FRfeJEynb%2FSRpjB%2BYNiB7NmIkmJPqY%2FUfRGht56GXtceOQgk8kWpKIQrKe2v0LA4PApDNBt3Ol6AG%2FZcwzMV0%2BzfSRPxb3llf8jGw729iAwyed1zsWW84UVnxYE%2BWGI7LgRFNDJfI%2B9QKXfspb%2BhEEkUEYkMWu7F8DA8l4U&X-Amz-Signature=f7e8959c67233078af7306f5c828bdce6914b5830570d6d821777afe09fe3ba2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26AKWO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDfNJPUDg9JCDc1hCC9CjOe7AYLx8vPLsFKEWi9MOewDQIgIGTuzBnfUvxqwUAL2Uv5krgSPAEO%2BRPNUNprgOx0EQkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDC51%2F4%2B5tO6iFoSkIyrcA1H340nLh5kAGx15Ctfnw%2BqLXaHwyRCi88L%2BaZ2QSDDdvU5iH%2FRhY3SFbcTdLJGYXH2qlDVtthdeETs42JiYvbeoBoTzJF379DH1W8BOGInoH36TuTlT%2FsdEVPOvQU7NLzzds8IIN56LLumLIq4bdDEYianQzKHCzXmUsPUBJqBKoO%2BjgZf%2BwiGgJw0eqbF3FqpvpIPN8mAO0WaK0tVRHs36Rg8Hlty5LxAc62qY65%2BAaVLVhiKmUmnpDfEVTeH8AL0ikSZ4G3vvTGc6o%2F9w8y8HvdGefXdIU4u9RE1HCLCeDl%2F9wwQkCAaqSWvMuWM538OVlpK2db83z6%2BkkVxXA%2F5yusAme2LqVCD5ctBPx94NzPC5w8m5mbsIeYyjO0cqof2pg6qUF9oD5WAw0juvYulox%2BVqwG83TgW7bozCZKTbpjajuO0D3E4yfECV%2Fw9g8EDJd2lD5uCqSkNI%2FBMDWJuSk8lHacSyDJILpy2HubWpHz%2FFSJRhx2trxh8TkkvV7QTUCveQhUxHyhVaf%2Bxb%2BlQNr4rsYickucdYg4NLcRO0SBC2PTBbupaOVWtAgyIBJZ1lZBxNbJBSdewRq%2B%2BbS2gwdi08pFRF5xvUWHCRezdidj1oHY54DNl%2F6j3IMJqN88kGOqUBjT0GcZMGOsNswMvwRW4LwT%2Fckzt7OhrTGh6SjXxFOOOJ6Z2%2BETv72%2FRfeJEynb%2FSRpjB%2BYNiB7NmIkmJPqY%2FUfRGht56GXtceOQgk8kWpKIQrKe2v0LA4PApDNBt3Ol6AG%2FZcwzMV0%2BzfSRPxb3llf8jGw729iAwyed1zsWW84UVnxYE%2BWGI7LgRFNDJfI%2B9QKXfspb%2BhEEkUEYkMWu7F8DA8l4U&X-Amz-Signature=f30f0e66a5601d15c33b718df3b2febb953ea5b80868f581ab3c428dbc42d12e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26AKWO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDfNJPUDg9JCDc1hCC9CjOe7AYLx8vPLsFKEWi9MOewDQIgIGTuzBnfUvxqwUAL2Uv5krgSPAEO%2BRPNUNprgOx0EQkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDC51%2F4%2B5tO6iFoSkIyrcA1H340nLh5kAGx15Ctfnw%2BqLXaHwyRCi88L%2BaZ2QSDDdvU5iH%2FRhY3SFbcTdLJGYXH2qlDVtthdeETs42JiYvbeoBoTzJF379DH1W8BOGInoH36TuTlT%2FsdEVPOvQU7NLzzds8IIN56LLumLIq4bdDEYianQzKHCzXmUsPUBJqBKoO%2BjgZf%2BwiGgJw0eqbF3FqpvpIPN8mAO0WaK0tVRHs36Rg8Hlty5LxAc62qY65%2BAaVLVhiKmUmnpDfEVTeH8AL0ikSZ4G3vvTGc6o%2F9w8y8HvdGefXdIU4u9RE1HCLCeDl%2F9wwQkCAaqSWvMuWM538OVlpK2db83z6%2BkkVxXA%2F5yusAme2LqVCD5ctBPx94NzPC5w8m5mbsIeYyjO0cqof2pg6qUF9oD5WAw0juvYulox%2BVqwG83TgW7bozCZKTbpjajuO0D3E4yfECV%2Fw9g8EDJd2lD5uCqSkNI%2FBMDWJuSk8lHacSyDJILpy2HubWpHz%2FFSJRhx2trxh8TkkvV7QTUCveQhUxHyhVaf%2Bxb%2BlQNr4rsYickucdYg4NLcRO0SBC2PTBbupaOVWtAgyIBJZ1lZBxNbJBSdewRq%2B%2BbS2gwdi08pFRF5xvUWHCRezdidj1oHY54DNl%2F6j3IMJqN88kGOqUBjT0GcZMGOsNswMvwRW4LwT%2Fckzt7OhrTGh6SjXxFOOOJ6Z2%2BETv72%2FRfeJEynb%2FSRpjB%2BYNiB7NmIkmJPqY%2FUfRGht56GXtceOQgk8kWpKIQrKe2v0LA4PApDNBt3Ol6AG%2FZcwzMV0%2BzfSRPxb3llf8jGw729iAwyed1zsWW84UVnxYE%2BWGI7LgRFNDJfI%2B9QKXfspb%2BhEEkUEYkMWu7F8DA8l4U&X-Amz-Signature=1631f85bf0889b3b8f0a35421efaa81c799347150254395230bf971fcaa671dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26AKWO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDfNJPUDg9JCDc1hCC9CjOe7AYLx8vPLsFKEWi9MOewDQIgIGTuzBnfUvxqwUAL2Uv5krgSPAEO%2BRPNUNprgOx0EQkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDC51%2F4%2B5tO6iFoSkIyrcA1H340nLh5kAGx15Ctfnw%2BqLXaHwyRCi88L%2BaZ2QSDDdvU5iH%2FRhY3SFbcTdLJGYXH2qlDVtthdeETs42JiYvbeoBoTzJF379DH1W8BOGInoH36TuTlT%2FsdEVPOvQU7NLzzds8IIN56LLumLIq4bdDEYianQzKHCzXmUsPUBJqBKoO%2BjgZf%2BwiGgJw0eqbF3FqpvpIPN8mAO0WaK0tVRHs36Rg8Hlty5LxAc62qY65%2BAaVLVhiKmUmnpDfEVTeH8AL0ikSZ4G3vvTGc6o%2F9w8y8HvdGefXdIU4u9RE1HCLCeDl%2F9wwQkCAaqSWvMuWM538OVlpK2db83z6%2BkkVxXA%2F5yusAme2LqVCD5ctBPx94NzPC5w8m5mbsIeYyjO0cqof2pg6qUF9oD5WAw0juvYulox%2BVqwG83TgW7bozCZKTbpjajuO0D3E4yfECV%2Fw9g8EDJd2lD5uCqSkNI%2FBMDWJuSk8lHacSyDJILpy2HubWpHz%2FFSJRhx2trxh8TkkvV7QTUCveQhUxHyhVaf%2Bxb%2BlQNr4rsYickucdYg4NLcRO0SBC2PTBbupaOVWtAgyIBJZ1lZBxNbJBSdewRq%2B%2BbS2gwdi08pFRF5xvUWHCRezdidj1oHY54DNl%2F6j3IMJqN88kGOqUBjT0GcZMGOsNswMvwRW4LwT%2Fckzt7OhrTGh6SjXxFOOOJ6Z2%2BETv72%2FRfeJEynb%2FSRpjB%2BYNiB7NmIkmJPqY%2FUfRGht56GXtceOQgk8kWpKIQrKe2v0LA4PApDNBt3Ol6AG%2FZcwzMV0%2BzfSRPxb3llf8jGw729iAwyed1zsWW84UVnxYE%2BWGI7LgRFNDJfI%2B9QKXfspb%2BhEEkUEYkMWu7F8DA8l4U&X-Amz-Signature=29065af6fac6479cab1e12edac07ac504b82f36cb2d35dfc7758407d5aa72b73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26AKWO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDfNJPUDg9JCDc1hCC9CjOe7AYLx8vPLsFKEWi9MOewDQIgIGTuzBnfUvxqwUAL2Uv5krgSPAEO%2BRPNUNprgOx0EQkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDC51%2F4%2B5tO6iFoSkIyrcA1H340nLh5kAGx15Ctfnw%2BqLXaHwyRCi88L%2BaZ2QSDDdvU5iH%2FRhY3SFbcTdLJGYXH2qlDVtthdeETs42JiYvbeoBoTzJF379DH1W8BOGInoH36TuTlT%2FsdEVPOvQU7NLzzds8IIN56LLumLIq4bdDEYianQzKHCzXmUsPUBJqBKoO%2BjgZf%2BwiGgJw0eqbF3FqpvpIPN8mAO0WaK0tVRHs36Rg8Hlty5LxAc62qY65%2BAaVLVhiKmUmnpDfEVTeH8AL0ikSZ4G3vvTGc6o%2F9w8y8HvdGefXdIU4u9RE1HCLCeDl%2F9wwQkCAaqSWvMuWM538OVlpK2db83z6%2BkkVxXA%2F5yusAme2LqVCD5ctBPx94NzPC5w8m5mbsIeYyjO0cqof2pg6qUF9oD5WAw0juvYulox%2BVqwG83TgW7bozCZKTbpjajuO0D3E4yfECV%2Fw9g8EDJd2lD5uCqSkNI%2FBMDWJuSk8lHacSyDJILpy2HubWpHz%2FFSJRhx2trxh8TkkvV7QTUCveQhUxHyhVaf%2Bxb%2BlQNr4rsYickucdYg4NLcRO0SBC2PTBbupaOVWtAgyIBJZ1lZBxNbJBSdewRq%2B%2BbS2gwdi08pFRF5xvUWHCRezdidj1oHY54DNl%2F6j3IMJqN88kGOqUBjT0GcZMGOsNswMvwRW4LwT%2Fckzt7OhrTGh6SjXxFOOOJ6Z2%2BETv72%2FRfeJEynb%2FSRpjB%2BYNiB7NmIkmJPqY%2FUfRGht56GXtceOQgk8kWpKIQrKe2v0LA4PApDNBt3Ol6AG%2FZcwzMV0%2BzfSRPxb3llf8jGw729iAwyed1zsWW84UVnxYE%2BWGI7LgRFNDJfI%2B9QKXfspb%2BhEEkUEYkMWu7F8DA8l4U&X-Amz-Signature=ba03ed5b114d47fe374801d89e89ddd410998834518d6af38874296af219d1da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB26AKWO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDfNJPUDg9JCDc1hCC9CjOe7AYLx8vPLsFKEWi9MOewDQIgIGTuzBnfUvxqwUAL2Uv5krgSPAEO%2BRPNUNprgOx0EQkq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDC51%2F4%2B5tO6iFoSkIyrcA1H340nLh5kAGx15Ctfnw%2BqLXaHwyRCi88L%2BaZ2QSDDdvU5iH%2FRhY3SFbcTdLJGYXH2qlDVtthdeETs42JiYvbeoBoTzJF379DH1W8BOGInoH36TuTlT%2FsdEVPOvQU7NLzzds8IIN56LLumLIq4bdDEYianQzKHCzXmUsPUBJqBKoO%2BjgZf%2BwiGgJw0eqbF3FqpvpIPN8mAO0WaK0tVRHs36Rg8Hlty5LxAc62qY65%2BAaVLVhiKmUmnpDfEVTeH8AL0ikSZ4G3vvTGc6o%2F9w8y8HvdGefXdIU4u9RE1HCLCeDl%2F9wwQkCAaqSWvMuWM538OVlpK2db83z6%2BkkVxXA%2F5yusAme2LqVCD5ctBPx94NzPC5w8m5mbsIeYyjO0cqof2pg6qUF9oD5WAw0juvYulox%2BVqwG83TgW7bozCZKTbpjajuO0D3E4yfECV%2Fw9g8EDJd2lD5uCqSkNI%2FBMDWJuSk8lHacSyDJILpy2HubWpHz%2FFSJRhx2trxh8TkkvV7QTUCveQhUxHyhVaf%2Bxb%2BlQNr4rsYickucdYg4NLcRO0SBC2PTBbupaOVWtAgyIBJZ1lZBxNbJBSdewRq%2B%2BbS2gwdi08pFRF5xvUWHCRezdidj1oHY54DNl%2F6j3IMJqN88kGOqUBjT0GcZMGOsNswMvwRW4LwT%2Fckzt7OhrTGh6SjXxFOOOJ6Z2%2BETv72%2FRfeJEynb%2FSRpjB%2BYNiB7NmIkmJPqY%2FUfRGht56GXtceOQgk8kWpKIQrKe2v0LA4PApDNBt3Ol6AG%2FZcwzMV0%2BzfSRPxb3llf8jGw729iAwyed1zsWW84UVnxYE%2BWGI7LgRFNDJfI%2B9QKXfspb%2BhEEkUEYkMWu7F8DA8l4U&X-Amz-Signature=4ac8b97e2a12dc3904903d4a2d9f41f8faf37ce53c5dcbdf60b660567566731c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

