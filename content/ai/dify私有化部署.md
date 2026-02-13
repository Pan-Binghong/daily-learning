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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ7Z6PM2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC%2F07HZPzHyDb5asRCytJjtShBsTXimXgY56ABiBmLPGAiAyHKYWHti%2BiNqb%2B%2BuQ9ntrKuTPKrz0Waym3B4%2BhsbqsCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSaNustepMF%2F4jEeKtwD1PpiTunZO0ZPfnpoUiMoxwF9xuMi4gDdkiv1RoJbZemwW7752S2Y9s5PgsSFuByfphDvshtLXsKbJrQlq5Q%2BQmtkog%2FFUBpEf59VQnK%2B78FPsgWyvmmleq4In4IkjEhmUGdQXX9TS3yHHmJ%2BAFFysY1w5LESPzLgPhQWLUOUlcAe6kwDVFnW2e%2BP9oiHlIb1NqktsLy6rnOIOz4myz8cGs8N7YN5Rh4Nlz8lPbpxf3M%2FRpJcNfXeaEx5HT0M5GkRyHyHfaMZjkJzE51aW%2BBV1XsaKmPN%2F61oA7IcmlUK5%2BJsPEr5L8%2F1OSiJGOVi9PdTpwBIcEb%2FKboPdUgBEfBdV%2FES6S1%2FeHpK64w2MBhehJ5F5H9oj14cmf03CUe87e2uFlCPnHpe8mcNxJD3F5uIOPtidiTHJfnbmNz8fMVae1VjSewqtXaX510i0FWkO00KiKQ5FSY13JYBCg3A7xWDz0k9rA6lZ7KlVp3fwrL7GOAXW3%2Flzvz2UA9INUHwDDvJHP8YUZsiFu471haCSYKXMCN3WEPRVdDVkaLlkOV%2BIbjHnXBpthSD8RMBd85pp3EFcDIqgckh95pXzb4mQB8%2F%2FS8delO27m1YxV2mm7sPCk3vhKnXwXsexUsTDOMwiZO6zAY6pgF9yWAb9PvEgXPPwiLJZ9%2FZPT8pkZENOBl7rUVfKoGuQkcDWo9kxK7nGbOfPdAPbeSkOherfO8wkLy4sqYMsavfmZ%2FJKHUsCFtGFfbQUCjFJIw6QukNy8Y0xk4WNsF5OMMmGmqxvHT5IxkA8ItmyIAnqewPXEWyDXzGbY7cH8OanN2tl0xLCqmSoJMJiBCVnXLto32lKsy7tUlsBd58YnedMR89Axiu&X-Amz-Signature=82c4c98481546eac979a0e4dc8a93f5c8d97e061216487bc5002dd62816f4337&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ7Z6PM2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC%2F07HZPzHyDb5asRCytJjtShBsTXimXgY56ABiBmLPGAiAyHKYWHti%2BiNqb%2B%2BuQ9ntrKuTPKrz0Waym3B4%2BhsbqsCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSaNustepMF%2F4jEeKtwD1PpiTunZO0ZPfnpoUiMoxwF9xuMi4gDdkiv1RoJbZemwW7752S2Y9s5PgsSFuByfphDvshtLXsKbJrQlq5Q%2BQmtkog%2FFUBpEf59VQnK%2B78FPsgWyvmmleq4In4IkjEhmUGdQXX9TS3yHHmJ%2BAFFysY1w5LESPzLgPhQWLUOUlcAe6kwDVFnW2e%2BP9oiHlIb1NqktsLy6rnOIOz4myz8cGs8N7YN5Rh4Nlz8lPbpxf3M%2FRpJcNfXeaEx5HT0M5GkRyHyHfaMZjkJzE51aW%2BBV1XsaKmPN%2F61oA7IcmlUK5%2BJsPEr5L8%2F1OSiJGOVi9PdTpwBIcEb%2FKboPdUgBEfBdV%2FES6S1%2FeHpK64w2MBhehJ5F5H9oj14cmf03CUe87e2uFlCPnHpe8mcNxJD3F5uIOPtidiTHJfnbmNz8fMVae1VjSewqtXaX510i0FWkO00KiKQ5FSY13JYBCg3A7xWDz0k9rA6lZ7KlVp3fwrL7GOAXW3%2Flzvz2UA9INUHwDDvJHP8YUZsiFu471haCSYKXMCN3WEPRVdDVkaLlkOV%2BIbjHnXBpthSD8RMBd85pp3EFcDIqgckh95pXzb4mQB8%2F%2FS8delO27m1YxV2mm7sPCk3vhKnXwXsexUsTDOMwiZO6zAY6pgF9yWAb9PvEgXPPwiLJZ9%2FZPT8pkZENOBl7rUVfKoGuQkcDWo9kxK7nGbOfPdAPbeSkOherfO8wkLy4sqYMsavfmZ%2FJKHUsCFtGFfbQUCjFJIw6QukNy8Y0xk4WNsF5OMMmGmqxvHT5IxkA8ItmyIAnqewPXEWyDXzGbY7cH8OanN2tl0xLCqmSoJMJiBCVnXLto32lKsy7tUlsBd58YnedMR89Axiu&X-Amz-Signature=10381afdc0ff6f7c29f2fbdfb08ff7ea6716c3d909adb8a27b84b21a12bf61da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ7Z6PM2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC%2F07HZPzHyDb5asRCytJjtShBsTXimXgY56ABiBmLPGAiAyHKYWHti%2BiNqb%2B%2BuQ9ntrKuTPKrz0Waym3B4%2BhsbqsCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSaNustepMF%2F4jEeKtwD1PpiTunZO0ZPfnpoUiMoxwF9xuMi4gDdkiv1RoJbZemwW7752S2Y9s5PgsSFuByfphDvshtLXsKbJrQlq5Q%2BQmtkog%2FFUBpEf59VQnK%2B78FPsgWyvmmleq4In4IkjEhmUGdQXX9TS3yHHmJ%2BAFFysY1w5LESPzLgPhQWLUOUlcAe6kwDVFnW2e%2BP9oiHlIb1NqktsLy6rnOIOz4myz8cGs8N7YN5Rh4Nlz8lPbpxf3M%2FRpJcNfXeaEx5HT0M5GkRyHyHfaMZjkJzE51aW%2BBV1XsaKmPN%2F61oA7IcmlUK5%2BJsPEr5L8%2F1OSiJGOVi9PdTpwBIcEb%2FKboPdUgBEfBdV%2FES6S1%2FeHpK64w2MBhehJ5F5H9oj14cmf03CUe87e2uFlCPnHpe8mcNxJD3F5uIOPtidiTHJfnbmNz8fMVae1VjSewqtXaX510i0FWkO00KiKQ5FSY13JYBCg3A7xWDz0k9rA6lZ7KlVp3fwrL7GOAXW3%2Flzvz2UA9INUHwDDvJHP8YUZsiFu471haCSYKXMCN3WEPRVdDVkaLlkOV%2BIbjHnXBpthSD8RMBd85pp3EFcDIqgckh95pXzb4mQB8%2F%2FS8delO27m1YxV2mm7sPCk3vhKnXwXsexUsTDOMwiZO6zAY6pgF9yWAb9PvEgXPPwiLJZ9%2FZPT8pkZENOBl7rUVfKoGuQkcDWo9kxK7nGbOfPdAPbeSkOherfO8wkLy4sqYMsavfmZ%2FJKHUsCFtGFfbQUCjFJIw6QukNy8Y0xk4WNsF5OMMmGmqxvHT5IxkA8ItmyIAnqewPXEWyDXzGbY7cH8OanN2tl0xLCqmSoJMJiBCVnXLto32lKsy7tUlsBd58YnedMR89Axiu&X-Amz-Signature=ebc7e275cb7efa2155970abdcf623420b3ec60191b8a29f2d883653d396cc447&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ7Z6PM2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC%2F07HZPzHyDb5asRCytJjtShBsTXimXgY56ABiBmLPGAiAyHKYWHti%2BiNqb%2B%2BuQ9ntrKuTPKrz0Waym3B4%2BhsbqsCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSaNustepMF%2F4jEeKtwD1PpiTunZO0ZPfnpoUiMoxwF9xuMi4gDdkiv1RoJbZemwW7752S2Y9s5PgsSFuByfphDvshtLXsKbJrQlq5Q%2BQmtkog%2FFUBpEf59VQnK%2B78FPsgWyvmmleq4In4IkjEhmUGdQXX9TS3yHHmJ%2BAFFysY1w5LESPzLgPhQWLUOUlcAe6kwDVFnW2e%2BP9oiHlIb1NqktsLy6rnOIOz4myz8cGs8N7YN5Rh4Nlz8lPbpxf3M%2FRpJcNfXeaEx5HT0M5GkRyHyHfaMZjkJzE51aW%2BBV1XsaKmPN%2F61oA7IcmlUK5%2BJsPEr5L8%2F1OSiJGOVi9PdTpwBIcEb%2FKboPdUgBEfBdV%2FES6S1%2FeHpK64w2MBhehJ5F5H9oj14cmf03CUe87e2uFlCPnHpe8mcNxJD3F5uIOPtidiTHJfnbmNz8fMVae1VjSewqtXaX510i0FWkO00KiKQ5FSY13JYBCg3A7xWDz0k9rA6lZ7KlVp3fwrL7GOAXW3%2Flzvz2UA9INUHwDDvJHP8YUZsiFu471haCSYKXMCN3WEPRVdDVkaLlkOV%2BIbjHnXBpthSD8RMBd85pp3EFcDIqgckh95pXzb4mQB8%2F%2FS8delO27m1YxV2mm7sPCk3vhKnXwXsexUsTDOMwiZO6zAY6pgF9yWAb9PvEgXPPwiLJZ9%2FZPT8pkZENOBl7rUVfKoGuQkcDWo9kxK7nGbOfPdAPbeSkOherfO8wkLy4sqYMsavfmZ%2FJKHUsCFtGFfbQUCjFJIw6QukNy8Y0xk4WNsF5OMMmGmqxvHT5IxkA8ItmyIAnqewPXEWyDXzGbY7cH8OanN2tl0xLCqmSoJMJiBCVnXLto32lKsy7tUlsBd58YnedMR89Axiu&X-Amz-Signature=95395f779068f35d0af409aae239b53564796db96acacf6861e4df3a5148ace9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ7Z6PM2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC%2F07HZPzHyDb5asRCytJjtShBsTXimXgY56ABiBmLPGAiAyHKYWHti%2BiNqb%2B%2BuQ9ntrKuTPKrz0Waym3B4%2BhsbqsCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSaNustepMF%2F4jEeKtwD1PpiTunZO0ZPfnpoUiMoxwF9xuMi4gDdkiv1RoJbZemwW7752S2Y9s5PgsSFuByfphDvshtLXsKbJrQlq5Q%2BQmtkog%2FFUBpEf59VQnK%2B78FPsgWyvmmleq4In4IkjEhmUGdQXX9TS3yHHmJ%2BAFFysY1w5LESPzLgPhQWLUOUlcAe6kwDVFnW2e%2BP9oiHlIb1NqktsLy6rnOIOz4myz8cGs8N7YN5Rh4Nlz8lPbpxf3M%2FRpJcNfXeaEx5HT0M5GkRyHyHfaMZjkJzE51aW%2BBV1XsaKmPN%2F61oA7IcmlUK5%2BJsPEr5L8%2F1OSiJGOVi9PdTpwBIcEb%2FKboPdUgBEfBdV%2FES6S1%2FeHpK64w2MBhehJ5F5H9oj14cmf03CUe87e2uFlCPnHpe8mcNxJD3F5uIOPtidiTHJfnbmNz8fMVae1VjSewqtXaX510i0FWkO00KiKQ5FSY13JYBCg3A7xWDz0k9rA6lZ7KlVp3fwrL7GOAXW3%2Flzvz2UA9INUHwDDvJHP8YUZsiFu471haCSYKXMCN3WEPRVdDVkaLlkOV%2BIbjHnXBpthSD8RMBd85pp3EFcDIqgckh95pXzb4mQB8%2F%2FS8delO27m1YxV2mm7sPCk3vhKnXwXsexUsTDOMwiZO6zAY6pgF9yWAb9PvEgXPPwiLJZ9%2FZPT8pkZENOBl7rUVfKoGuQkcDWo9kxK7nGbOfPdAPbeSkOherfO8wkLy4sqYMsavfmZ%2FJKHUsCFtGFfbQUCjFJIw6QukNy8Y0xk4WNsF5OMMmGmqxvHT5IxkA8ItmyIAnqewPXEWyDXzGbY7cH8OanN2tl0xLCqmSoJMJiBCVnXLto32lKsy7tUlsBd58YnedMR89Axiu&X-Amz-Signature=cc19e01c69820b57cd7da27239463b2895deea9b3acd7470c2c7497335cbfa09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ7Z6PM2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC%2F07HZPzHyDb5asRCytJjtShBsTXimXgY56ABiBmLPGAiAyHKYWHti%2BiNqb%2B%2BuQ9ntrKuTPKrz0Waym3B4%2BhsbqsCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSaNustepMF%2F4jEeKtwD1PpiTunZO0ZPfnpoUiMoxwF9xuMi4gDdkiv1RoJbZemwW7752S2Y9s5PgsSFuByfphDvshtLXsKbJrQlq5Q%2BQmtkog%2FFUBpEf59VQnK%2B78FPsgWyvmmleq4In4IkjEhmUGdQXX9TS3yHHmJ%2BAFFysY1w5LESPzLgPhQWLUOUlcAe6kwDVFnW2e%2BP9oiHlIb1NqktsLy6rnOIOz4myz8cGs8N7YN5Rh4Nlz8lPbpxf3M%2FRpJcNfXeaEx5HT0M5GkRyHyHfaMZjkJzE51aW%2BBV1XsaKmPN%2F61oA7IcmlUK5%2BJsPEr5L8%2F1OSiJGOVi9PdTpwBIcEb%2FKboPdUgBEfBdV%2FES6S1%2FeHpK64w2MBhehJ5F5H9oj14cmf03CUe87e2uFlCPnHpe8mcNxJD3F5uIOPtidiTHJfnbmNz8fMVae1VjSewqtXaX510i0FWkO00KiKQ5FSY13JYBCg3A7xWDz0k9rA6lZ7KlVp3fwrL7GOAXW3%2Flzvz2UA9INUHwDDvJHP8YUZsiFu471haCSYKXMCN3WEPRVdDVkaLlkOV%2BIbjHnXBpthSD8RMBd85pp3EFcDIqgckh95pXzb4mQB8%2F%2FS8delO27m1YxV2mm7sPCk3vhKnXwXsexUsTDOMwiZO6zAY6pgF9yWAb9PvEgXPPwiLJZ9%2FZPT8pkZENOBl7rUVfKoGuQkcDWo9kxK7nGbOfPdAPbeSkOherfO8wkLy4sqYMsavfmZ%2FJKHUsCFtGFfbQUCjFJIw6QukNy8Y0xk4WNsF5OMMmGmqxvHT5IxkA8ItmyIAnqewPXEWyDXzGbY7cH8OanN2tl0xLCqmSoJMJiBCVnXLto32lKsy7tUlsBd58YnedMR89Axiu&X-Amz-Signature=595896f1d44cf9e833672cb870732c5302cf9efbab7a86b1077485eb60ce9ba8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ7Z6PM2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC%2F07HZPzHyDb5asRCytJjtShBsTXimXgY56ABiBmLPGAiAyHKYWHti%2BiNqb%2B%2BuQ9ntrKuTPKrz0Waym3B4%2BhsbqsCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSaNustepMF%2F4jEeKtwD1PpiTunZO0ZPfnpoUiMoxwF9xuMi4gDdkiv1RoJbZemwW7752S2Y9s5PgsSFuByfphDvshtLXsKbJrQlq5Q%2BQmtkog%2FFUBpEf59VQnK%2B78FPsgWyvmmleq4In4IkjEhmUGdQXX9TS3yHHmJ%2BAFFysY1w5LESPzLgPhQWLUOUlcAe6kwDVFnW2e%2BP9oiHlIb1NqktsLy6rnOIOz4myz8cGs8N7YN5Rh4Nlz8lPbpxf3M%2FRpJcNfXeaEx5HT0M5GkRyHyHfaMZjkJzE51aW%2BBV1XsaKmPN%2F61oA7IcmlUK5%2BJsPEr5L8%2F1OSiJGOVi9PdTpwBIcEb%2FKboPdUgBEfBdV%2FES6S1%2FeHpK64w2MBhehJ5F5H9oj14cmf03CUe87e2uFlCPnHpe8mcNxJD3F5uIOPtidiTHJfnbmNz8fMVae1VjSewqtXaX510i0FWkO00KiKQ5FSY13JYBCg3A7xWDz0k9rA6lZ7KlVp3fwrL7GOAXW3%2Flzvz2UA9INUHwDDvJHP8YUZsiFu471haCSYKXMCN3WEPRVdDVkaLlkOV%2BIbjHnXBpthSD8RMBd85pp3EFcDIqgckh95pXzb4mQB8%2F%2FS8delO27m1YxV2mm7sPCk3vhKnXwXsexUsTDOMwiZO6zAY6pgF9yWAb9PvEgXPPwiLJZ9%2FZPT8pkZENOBl7rUVfKoGuQkcDWo9kxK7nGbOfPdAPbeSkOherfO8wkLy4sqYMsavfmZ%2FJKHUsCFtGFfbQUCjFJIw6QukNy8Y0xk4WNsF5OMMmGmqxvHT5IxkA8ItmyIAnqewPXEWyDXzGbY7cH8OanN2tl0xLCqmSoJMJiBCVnXLto32lKsy7tUlsBd58YnedMR89Axiu&X-Amz-Signature=73680f1d596008bf5b9a154d41e3282008d5a20ec4e0caa2e37c6303f25d1d7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ7Z6PM2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC%2F07HZPzHyDb5asRCytJjtShBsTXimXgY56ABiBmLPGAiAyHKYWHti%2BiNqb%2B%2BuQ9ntrKuTPKrz0Waym3B4%2BhsbqsCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSaNustepMF%2F4jEeKtwD1PpiTunZO0ZPfnpoUiMoxwF9xuMi4gDdkiv1RoJbZemwW7752S2Y9s5PgsSFuByfphDvshtLXsKbJrQlq5Q%2BQmtkog%2FFUBpEf59VQnK%2B78FPsgWyvmmleq4In4IkjEhmUGdQXX9TS3yHHmJ%2BAFFysY1w5LESPzLgPhQWLUOUlcAe6kwDVFnW2e%2BP9oiHlIb1NqktsLy6rnOIOz4myz8cGs8N7YN5Rh4Nlz8lPbpxf3M%2FRpJcNfXeaEx5HT0M5GkRyHyHfaMZjkJzE51aW%2BBV1XsaKmPN%2F61oA7IcmlUK5%2BJsPEr5L8%2F1OSiJGOVi9PdTpwBIcEb%2FKboPdUgBEfBdV%2FES6S1%2FeHpK64w2MBhehJ5F5H9oj14cmf03CUe87e2uFlCPnHpe8mcNxJD3F5uIOPtidiTHJfnbmNz8fMVae1VjSewqtXaX510i0FWkO00KiKQ5FSY13JYBCg3A7xWDz0k9rA6lZ7KlVp3fwrL7GOAXW3%2Flzvz2UA9INUHwDDvJHP8YUZsiFu471haCSYKXMCN3WEPRVdDVkaLlkOV%2BIbjHnXBpthSD8RMBd85pp3EFcDIqgckh95pXzb4mQB8%2F%2FS8delO27m1YxV2mm7sPCk3vhKnXwXsexUsTDOMwiZO6zAY6pgF9yWAb9PvEgXPPwiLJZ9%2FZPT8pkZENOBl7rUVfKoGuQkcDWo9kxK7nGbOfPdAPbeSkOherfO8wkLy4sqYMsavfmZ%2FJKHUsCFtGFfbQUCjFJIw6QukNy8Y0xk4WNsF5OMMmGmqxvHT5IxkA8ItmyIAnqewPXEWyDXzGbY7cH8OanN2tl0xLCqmSoJMJiBCVnXLto32lKsy7tUlsBd58YnedMR89Axiu&X-Amz-Signature=8974d86f17c0e5291bde9c45dca5bcfdef437a7e5d33f3c571e7633479e993b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ7Z6PM2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC%2F07HZPzHyDb5asRCytJjtShBsTXimXgY56ABiBmLPGAiAyHKYWHti%2BiNqb%2B%2BuQ9ntrKuTPKrz0Waym3B4%2BhsbqsCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSaNustepMF%2F4jEeKtwD1PpiTunZO0ZPfnpoUiMoxwF9xuMi4gDdkiv1RoJbZemwW7752S2Y9s5PgsSFuByfphDvshtLXsKbJrQlq5Q%2BQmtkog%2FFUBpEf59VQnK%2B78FPsgWyvmmleq4In4IkjEhmUGdQXX9TS3yHHmJ%2BAFFysY1w5LESPzLgPhQWLUOUlcAe6kwDVFnW2e%2BP9oiHlIb1NqktsLy6rnOIOz4myz8cGs8N7YN5Rh4Nlz8lPbpxf3M%2FRpJcNfXeaEx5HT0M5GkRyHyHfaMZjkJzE51aW%2BBV1XsaKmPN%2F61oA7IcmlUK5%2BJsPEr5L8%2F1OSiJGOVi9PdTpwBIcEb%2FKboPdUgBEfBdV%2FES6S1%2FeHpK64w2MBhehJ5F5H9oj14cmf03CUe87e2uFlCPnHpe8mcNxJD3F5uIOPtidiTHJfnbmNz8fMVae1VjSewqtXaX510i0FWkO00KiKQ5FSY13JYBCg3A7xWDz0k9rA6lZ7KlVp3fwrL7GOAXW3%2Flzvz2UA9INUHwDDvJHP8YUZsiFu471haCSYKXMCN3WEPRVdDVkaLlkOV%2BIbjHnXBpthSD8RMBd85pp3EFcDIqgckh95pXzb4mQB8%2F%2FS8delO27m1YxV2mm7sPCk3vhKnXwXsexUsTDOMwiZO6zAY6pgF9yWAb9PvEgXPPwiLJZ9%2FZPT8pkZENOBl7rUVfKoGuQkcDWo9kxK7nGbOfPdAPbeSkOherfO8wkLy4sqYMsavfmZ%2FJKHUsCFtGFfbQUCjFJIw6QukNy8Y0xk4WNsF5OMMmGmqxvHT5IxkA8ItmyIAnqewPXEWyDXzGbY7cH8OanN2tl0xLCqmSoJMJiBCVnXLto32lKsy7tUlsBd58YnedMR89Axiu&X-Amz-Signature=224f1e8130a5ce1d729bfe84ca4d25cd74f0a8d3b77f8b69a654f86a5b21073e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ7Z6PM2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIC%2F07HZPzHyDb5asRCytJjtShBsTXimXgY56ABiBmLPGAiAyHKYWHti%2BiNqb%2B%2BuQ9ntrKuTPKrz0Waym3B4%2BhsbqsCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSaNustepMF%2F4jEeKtwD1PpiTunZO0ZPfnpoUiMoxwF9xuMi4gDdkiv1RoJbZemwW7752S2Y9s5PgsSFuByfphDvshtLXsKbJrQlq5Q%2BQmtkog%2FFUBpEf59VQnK%2B78FPsgWyvmmleq4In4IkjEhmUGdQXX9TS3yHHmJ%2BAFFysY1w5LESPzLgPhQWLUOUlcAe6kwDVFnW2e%2BP9oiHlIb1NqktsLy6rnOIOz4myz8cGs8N7YN5Rh4Nlz8lPbpxf3M%2FRpJcNfXeaEx5HT0M5GkRyHyHfaMZjkJzE51aW%2BBV1XsaKmPN%2F61oA7IcmlUK5%2BJsPEr5L8%2F1OSiJGOVi9PdTpwBIcEb%2FKboPdUgBEfBdV%2FES6S1%2FeHpK64w2MBhehJ5F5H9oj14cmf03CUe87e2uFlCPnHpe8mcNxJD3F5uIOPtidiTHJfnbmNz8fMVae1VjSewqtXaX510i0FWkO00KiKQ5FSY13JYBCg3A7xWDz0k9rA6lZ7KlVp3fwrL7GOAXW3%2Flzvz2UA9INUHwDDvJHP8YUZsiFu471haCSYKXMCN3WEPRVdDVkaLlkOV%2BIbjHnXBpthSD8RMBd85pp3EFcDIqgckh95pXzb4mQB8%2F%2FS8delO27m1YxV2mm7sPCk3vhKnXwXsexUsTDOMwiZO6zAY6pgF9yWAb9PvEgXPPwiLJZ9%2FZPT8pkZENOBl7rUVfKoGuQkcDWo9kxK7nGbOfPdAPbeSkOherfO8wkLy4sqYMsavfmZ%2FJKHUsCFtGFfbQUCjFJIw6QukNy8Y0xk4WNsF5OMMmGmqxvHT5IxkA8ItmyIAnqewPXEWyDXzGbY7cH8OanN2tl0xLCqmSoJMJiBCVnXLto32lKsy7tUlsBd58YnedMR89Axiu&X-Amz-Signature=3eea5e51349af6cf796dc965f3fdd5fae3b2e17b951c6f6049966a948c5e34f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

