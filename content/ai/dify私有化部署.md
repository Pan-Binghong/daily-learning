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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIFLS43T%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwC7TviyqVXKU%2BkQooZ2fMzkmOYj%2BlMmpZh6UXRpm2kAiAIq7mCKHt4oUobv%2BvyKD5pmnLjSzBwnZlSxAJIGbcuyyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMgU6xUG5Pp2n4ah6zKtwDQUro9q0Q3HXF%2FxLwjjVVDmDu1SCcqNqcWRVWdaTvHEssynUZAB5d501OOHsnYXHfi4Yy2P%2B5re2KHiN2ZVq6YAeFBQ%2BdVN%2FNp6GSB5b5YvG0%2FaiXXbjO2c5Nu1QjrL22ytWjHCFYbx3xcZynCaalxNHbRQMIHgnFZmPGZPZtogBQcoow7lZmRyWVC2I2bEcIhcE4YGmf0UQRunS00quXQR%2BkPjZ2ex9UBoJNJLPZXvxrh8GC%2FORCk49atxo8pb1i7gSWHLr6JW0%2FDO3e0zr2E58y6%2FENsxDf1TzAs6GjzRS4dk6WFqhgZ7asn2MkZdFG%2FfU%2FFjNAYwSsrTFcJnt1%2BTllpdimSQc4yLsOIkAtyWw%2FvmyL5iQgw%2B47S%2FzFXgr9BadNWcQ72XO1A3sBQPeaMZ2Xs8sCog2yvp9wqjIDx0mk%2FfGLT3NlGq3wD3okHbS1%2B6%2FmcLfSdzqvvs7BA2Al8JF0ytSp0FvpkWVp%2FO1CDVoGkjtGffGR90fVh%2BR5IhljNKtMwKjSzROmqIMwcJbr1Jgv5L7D661%2Fi9Em1f7gu60a3a8HT2TlXWzk8kddP8MW0i3PPHdjSbpQP4hCqcBbQexJYw38eF9efVmLQvLT3j%2FF7x0EUgqsxewVFpUwj%2BC8ygY6pgFb5aljC%2BmjnVsO3%2BO3SJafyUZnow2MPgAGyVw0HwSEae6rgQVjvG7fxoB%2F0457CZ2i%2BHV%2Fnt7pnU%2Bz51bcL7XiOrsASWU7Ul%2FSNQgU1qkUlpeNQCoDIQPGuvDl5ekAESHPtPWypB3517O4fWHWSoBpJQW5nJp7gkDdWk4Sfbwy4%2Fmu7%2FMS98z%2Bx%2FeyLt0qBn%2F6sxg67Qz3TDauYLTembjc5KrXJ8nX&X-Amz-Signature=3c85d9fc992d9f3697763832bb95fe448d1d6950edd61b600e7e351957026b83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIFLS43T%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwC7TviyqVXKU%2BkQooZ2fMzkmOYj%2BlMmpZh6UXRpm2kAiAIq7mCKHt4oUobv%2BvyKD5pmnLjSzBwnZlSxAJIGbcuyyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMgU6xUG5Pp2n4ah6zKtwDQUro9q0Q3HXF%2FxLwjjVVDmDu1SCcqNqcWRVWdaTvHEssynUZAB5d501OOHsnYXHfi4Yy2P%2B5re2KHiN2ZVq6YAeFBQ%2BdVN%2FNp6GSB5b5YvG0%2FaiXXbjO2c5Nu1QjrL22ytWjHCFYbx3xcZynCaalxNHbRQMIHgnFZmPGZPZtogBQcoow7lZmRyWVC2I2bEcIhcE4YGmf0UQRunS00quXQR%2BkPjZ2ex9UBoJNJLPZXvxrh8GC%2FORCk49atxo8pb1i7gSWHLr6JW0%2FDO3e0zr2E58y6%2FENsxDf1TzAs6GjzRS4dk6WFqhgZ7asn2MkZdFG%2FfU%2FFjNAYwSsrTFcJnt1%2BTllpdimSQc4yLsOIkAtyWw%2FvmyL5iQgw%2B47S%2FzFXgr9BadNWcQ72XO1A3sBQPeaMZ2Xs8sCog2yvp9wqjIDx0mk%2FfGLT3NlGq3wD3okHbS1%2B6%2FmcLfSdzqvvs7BA2Al8JF0ytSp0FvpkWVp%2FO1CDVoGkjtGffGR90fVh%2BR5IhljNKtMwKjSzROmqIMwcJbr1Jgv5L7D661%2Fi9Em1f7gu60a3a8HT2TlXWzk8kddP8MW0i3PPHdjSbpQP4hCqcBbQexJYw38eF9efVmLQvLT3j%2FF7x0EUgqsxewVFpUwj%2BC8ygY6pgFb5aljC%2BmjnVsO3%2BO3SJafyUZnow2MPgAGyVw0HwSEae6rgQVjvG7fxoB%2F0457CZ2i%2BHV%2Fnt7pnU%2Bz51bcL7XiOrsASWU7Ul%2FSNQgU1qkUlpeNQCoDIQPGuvDl5ekAESHPtPWypB3517O4fWHWSoBpJQW5nJp7gkDdWk4Sfbwy4%2Fmu7%2FMS98z%2Bx%2FeyLt0qBn%2F6sxg67Qz3TDauYLTembjc5KrXJ8nX&X-Amz-Signature=dbc04cd16c593778acae594e91aa47b1584ea2d393de3b00a2538bea8639bcbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIFLS43T%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwC7TviyqVXKU%2BkQooZ2fMzkmOYj%2BlMmpZh6UXRpm2kAiAIq7mCKHt4oUobv%2BvyKD5pmnLjSzBwnZlSxAJIGbcuyyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMgU6xUG5Pp2n4ah6zKtwDQUro9q0Q3HXF%2FxLwjjVVDmDu1SCcqNqcWRVWdaTvHEssynUZAB5d501OOHsnYXHfi4Yy2P%2B5re2KHiN2ZVq6YAeFBQ%2BdVN%2FNp6GSB5b5YvG0%2FaiXXbjO2c5Nu1QjrL22ytWjHCFYbx3xcZynCaalxNHbRQMIHgnFZmPGZPZtogBQcoow7lZmRyWVC2I2bEcIhcE4YGmf0UQRunS00quXQR%2BkPjZ2ex9UBoJNJLPZXvxrh8GC%2FORCk49atxo8pb1i7gSWHLr6JW0%2FDO3e0zr2E58y6%2FENsxDf1TzAs6GjzRS4dk6WFqhgZ7asn2MkZdFG%2FfU%2FFjNAYwSsrTFcJnt1%2BTllpdimSQc4yLsOIkAtyWw%2FvmyL5iQgw%2B47S%2FzFXgr9BadNWcQ72XO1A3sBQPeaMZ2Xs8sCog2yvp9wqjIDx0mk%2FfGLT3NlGq3wD3okHbS1%2B6%2FmcLfSdzqvvs7BA2Al8JF0ytSp0FvpkWVp%2FO1CDVoGkjtGffGR90fVh%2BR5IhljNKtMwKjSzROmqIMwcJbr1Jgv5L7D661%2Fi9Em1f7gu60a3a8HT2TlXWzk8kddP8MW0i3PPHdjSbpQP4hCqcBbQexJYw38eF9efVmLQvLT3j%2FF7x0EUgqsxewVFpUwj%2BC8ygY6pgFb5aljC%2BmjnVsO3%2BO3SJafyUZnow2MPgAGyVw0HwSEae6rgQVjvG7fxoB%2F0457CZ2i%2BHV%2Fnt7pnU%2Bz51bcL7XiOrsASWU7Ul%2FSNQgU1qkUlpeNQCoDIQPGuvDl5ekAESHPtPWypB3517O4fWHWSoBpJQW5nJp7gkDdWk4Sfbwy4%2Fmu7%2FMS98z%2Bx%2FeyLt0qBn%2F6sxg67Qz3TDauYLTembjc5KrXJ8nX&X-Amz-Signature=1c5bb8dc83f789eb719bdbbb7b6ff665adba6b5295c784b408116d6d98d5150d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIFLS43T%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwC7TviyqVXKU%2BkQooZ2fMzkmOYj%2BlMmpZh6UXRpm2kAiAIq7mCKHt4oUobv%2BvyKD5pmnLjSzBwnZlSxAJIGbcuyyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMgU6xUG5Pp2n4ah6zKtwDQUro9q0Q3HXF%2FxLwjjVVDmDu1SCcqNqcWRVWdaTvHEssynUZAB5d501OOHsnYXHfi4Yy2P%2B5re2KHiN2ZVq6YAeFBQ%2BdVN%2FNp6GSB5b5YvG0%2FaiXXbjO2c5Nu1QjrL22ytWjHCFYbx3xcZynCaalxNHbRQMIHgnFZmPGZPZtogBQcoow7lZmRyWVC2I2bEcIhcE4YGmf0UQRunS00quXQR%2BkPjZ2ex9UBoJNJLPZXvxrh8GC%2FORCk49atxo8pb1i7gSWHLr6JW0%2FDO3e0zr2E58y6%2FENsxDf1TzAs6GjzRS4dk6WFqhgZ7asn2MkZdFG%2FfU%2FFjNAYwSsrTFcJnt1%2BTllpdimSQc4yLsOIkAtyWw%2FvmyL5iQgw%2B47S%2FzFXgr9BadNWcQ72XO1A3sBQPeaMZ2Xs8sCog2yvp9wqjIDx0mk%2FfGLT3NlGq3wD3okHbS1%2B6%2FmcLfSdzqvvs7BA2Al8JF0ytSp0FvpkWVp%2FO1CDVoGkjtGffGR90fVh%2BR5IhljNKtMwKjSzROmqIMwcJbr1Jgv5L7D661%2Fi9Em1f7gu60a3a8HT2TlXWzk8kddP8MW0i3PPHdjSbpQP4hCqcBbQexJYw38eF9efVmLQvLT3j%2FF7x0EUgqsxewVFpUwj%2BC8ygY6pgFb5aljC%2BmjnVsO3%2BO3SJafyUZnow2MPgAGyVw0HwSEae6rgQVjvG7fxoB%2F0457CZ2i%2BHV%2Fnt7pnU%2Bz51bcL7XiOrsASWU7Ul%2FSNQgU1qkUlpeNQCoDIQPGuvDl5ekAESHPtPWypB3517O4fWHWSoBpJQW5nJp7gkDdWk4Sfbwy4%2Fmu7%2FMS98z%2Bx%2FeyLt0qBn%2F6sxg67Qz3TDauYLTembjc5KrXJ8nX&X-Amz-Signature=60178ae85872967b2d0e5def0abf6d5c52dae940b87ede3e7c4ba27e284d0e75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIFLS43T%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwC7TviyqVXKU%2BkQooZ2fMzkmOYj%2BlMmpZh6UXRpm2kAiAIq7mCKHt4oUobv%2BvyKD5pmnLjSzBwnZlSxAJIGbcuyyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMgU6xUG5Pp2n4ah6zKtwDQUro9q0Q3HXF%2FxLwjjVVDmDu1SCcqNqcWRVWdaTvHEssynUZAB5d501OOHsnYXHfi4Yy2P%2B5re2KHiN2ZVq6YAeFBQ%2BdVN%2FNp6GSB5b5YvG0%2FaiXXbjO2c5Nu1QjrL22ytWjHCFYbx3xcZynCaalxNHbRQMIHgnFZmPGZPZtogBQcoow7lZmRyWVC2I2bEcIhcE4YGmf0UQRunS00quXQR%2BkPjZ2ex9UBoJNJLPZXvxrh8GC%2FORCk49atxo8pb1i7gSWHLr6JW0%2FDO3e0zr2E58y6%2FENsxDf1TzAs6GjzRS4dk6WFqhgZ7asn2MkZdFG%2FfU%2FFjNAYwSsrTFcJnt1%2BTllpdimSQc4yLsOIkAtyWw%2FvmyL5iQgw%2B47S%2FzFXgr9BadNWcQ72XO1A3sBQPeaMZ2Xs8sCog2yvp9wqjIDx0mk%2FfGLT3NlGq3wD3okHbS1%2B6%2FmcLfSdzqvvs7BA2Al8JF0ytSp0FvpkWVp%2FO1CDVoGkjtGffGR90fVh%2BR5IhljNKtMwKjSzROmqIMwcJbr1Jgv5L7D661%2Fi9Em1f7gu60a3a8HT2TlXWzk8kddP8MW0i3PPHdjSbpQP4hCqcBbQexJYw38eF9efVmLQvLT3j%2FF7x0EUgqsxewVFpUwj%2BC8ygY6pgFb5aljC%2BmjnVsO3%2BO3SJafyUZnow2MPgAGyVw0HwSEae6rgQVjvG7fxoB%2F0457CZ2i%2BHV%2Fnt7pnU%2Bz51bcL7XiOrsASWU7Ul%2FSNQgU1qkUlpeNQCoDIQPGuvDl5ekAESHPtPWypB3517O4fWHWSoBpJQW5nJp7gkDdWk4Sfbwy4%2Fmu7%2FMS98z%2Bx%2FeyLt0qBn%2F6sxg67Qz3TDauYLTembjc5KrXJ8nX&X-Amz-Signature=1bf2bf64c7d1d3fa749a818f7e840395fc57edd4e4becaabd7114661574462f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIFLS43T%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwC7TviyqVXKU%2BkQooZ2fMzkmOYj%2BlMmpZh6UXRpm2kAiAIq7mCKHt4oUobv%2BvyKD5pmnLjSzBwnZlSxAJIGbcuyyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMgU6xUG5Pp2n4ah6zKtwDQUro9q0Q3HXF%2FxLwjjVVDmDu1SCcqNqcWRVWdaTvHEssynUZAB5d501OOHsnYXHfi4Yy2P%2B5re2KHiN2ZVq6YAeFBQ%2BdVN%2FNp6GSB5b5YvG0%2FaiXXbjO2c5Nu1QjrL22ytWjHCFYbx3xcZynCaalxNHbRQMIHgnFZmPGZPZtogBQcoow7lZmRyWVC2I2bEcIhcE4YGmf0UQRunS00quXQR%2BkPjZ2ex9UBoJNJLPZXvxrh8GC%2FORCk49atxo8pb1i7gSWHLr6JW0%2FDO3e0zr2E58y6%2FENsxDf1TzAs6GjzRS4dk6WFqhgZ7asn2MkZdFG%2FfU%2FFjNAYwSsrTFcJnt1%2BTllpdimSQc4yLsOIkAtyWw%2FvmyL5iQgw%2B47S%2FzFXgr9BadNWcQ72XO1A3sBQPeaMZ2Xs8sCog2yvp9wqjIDx0mk%2FfGLT3NlGq3wD3okHbS1%2B6%2FmcLfSdzqvvs7BA2Al8JF0ytSp0FvpkWVp%2FO1CDVoGkjtGffGR90fVh%2BR5IhljNKtMwKjSzROmqIMwcJbr1Jgv5L7D661%2Fi9Em1f7gu60a3a8HT2TlXWzk8kddP8MW0i3PPHdjSbpQP4hCqcBbQexJYw38eF9efVmLQvLT3j%2FF7x0EUgqsxewVFpUwj%2BC8ygY6pgFb5aljC%2BmjnVsO3%2BO3SJafyUZnow2MPgAGyVw0HwSEae6rgQVjvG7fxoB%2F0457CZ2i%2BHV%2Fnt7pnU%2Bz51bcL7XiOrsASWU7Ul%2FSNQgU1qkUlpeNQCoDIQPGuvDl5ekAESHPtPWypB3517O4fWHWSoBpJQW5nJp7gkDdWk4Sfbwy4%2Fmu7%2FMS98z%2Bx%2FeyLt0qBn%2F6sxg67Qz3TDauYLTembjc5KrXJ8nX&X-Amz-Signature=1b7eb6da665296fca7dfd45ed14b128084fc203ecb625e5ca40dcabc120380fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIFLS43T%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwC7TviyqVXKU%2BkQooZ2fMzkmOYj%2BlMmpZh6UXRpm2kAiAIq7mCKHt4oUobv%2BvyKD5pmnLjSzBwnZlSxAJIGbcuyyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMgU6xUG5Pp2n4ah6zKtwDQUro9q0Q3HXF%2FxLwjjVVDmDu1SCcqNqcWRVWdaTvHEssynUZAB5d501OOHsnYXHfi4Yy2P%2B5re2KHiN2ZVq6YAeFBQ%2BdVN%2FNp6GSB5b5YvG0%2FaiXXbjO2c5Nu1QjrL22ytWjHCFYbx3xcZynCaalxNHbRQMIHgnFZmPGZPZtogBQcoow7lZmRyWVC2I2bEcIhcE4YGmf0UQRunS00quXQR%2BkPjZ2ex9UBoJNJLPZXvxrh8GC%2FORCk49atxo8pb1i7gSWHLr6JW0%2FDO3e0zr2E58y6%2FENsxDf1TzAs6GjzRS4dk6WFqhgZ7asn2MkZdFG%2FfU%2FFjNAYwSsrTFcJnt1%2BTllpdimSQc4yLsOIkAtyWw%2FvmyL5iQgw%2B47S%2FzFXgr9BadNWcQ72XO1A3sBQPeaMZ2Xs8sCog2yvp9wqjIDx0mk%2FfGLT3NlGq3wD3okHbS1%2B6%2FmcLfSdzqvvs7BA2Al8JF0ytSp0FvpkWVp%2FO1CDVoGkjtGffGR90fVh%2BR5IhljNKtMwKjSzROmqIMwcJbr1Jgv5L7D661%2Fi9Em1f7gu60a3a8HT2TlXWzk8kddP8MW0i3PPHdjSbpQP4hCqcBbQexJYw38eF9efVmLQvLT3j%2FF7x0EUgqsxewVFpUwj%2BC8ygY6pgFb5aljC%2BmjnVsO3%2BO3SJafyUZnow2MPgAGyVw0HwSEae6rgQVjvG7fxoB%2F0457CZ2i%2BHV%2Fnt7pnU%2Bz51bcL7XiOrsASWU7Ul%2FSNQgU1qkUlpeNQCoDIQPGuvDl5ekAESHPtPWypB3517O4fWHWSoBpJQW5nJp7gkDdWk4Sfbwy4%2Fmu7%2FMS98z%2Bx%2FeyLt0qBn%2F6sxg67Qz3TDauYLTembjc5KrXJ8nX&X-Amz-Signature=abc50e9a088a9bbf5bc7b1b6816fcb2a5384e5fe03ee92e15bef84d068cc1b16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIFLS43T%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwC7TviyqVXKU%2BkQooZ2fMzkmOYj%2BlMmpZh6UXRpm2kAiAIq7mCKHt4oUobv%2BvyKD5pmnLjSzBwnZlSxAJIGbcuyyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMgU6xUG5Pp2n4ah6zKtwDQUro9q0Q3HXF%2FxLwjjVVDmDu1SCcqNqcWRVWdaTvHEssynUZAB5d501OOHsnYXHfi4Yy2P%2B5re2KHiN2ZVq6YAeFBQ%2BdVN%2FNp6GSB5b5YvG0%2FaiXXbjO2c5Nu1QjrL22ytWjHCFYbx3xcZynCaalxNHbRQMIHgnFZmPGZPZtogBQcoow7lZmRyWVC2I2bEcIhcE4YGmf0UQRunS00quXQR%2BkPjZ2ex9UBoJNJLPZXvxrh8GC%2FORCk49atxo8pb1i7gSWHLr6JW0%2FDO3e0zr2E58y6%2FENsxDf1TzAs6GjzRS4dk6WFqhgZ7asn2MkZdFG%2FfU%2FFjNAYwSsrTFcJnt1%2BTllpdimSQc4yLsOIkAtyWw%2FvmyL5iQgw%2B47S%2FzFXgr9BadNWcQ72XO1A3sBQPeaMZ2Xs8sCog2yvp9wqjIDx0mk%2FfGLT3NlGq3wD3okHbS1%2B6%2FmcLfSdzqvvs7BA2Al8JF0ytSp0FvpkWVp%2FO1CDVoGkjtGffGR90fVh%2BR5IhljNKtMwKjSzROmqIMwcJbr1Jgv5L7D661%2Fi9Em1f7gu60a3a8HT2TlXWzk8kddP8MW0i3PPHdjSbpQP4hCqcBbQexJYw38eF9efVmLQvLT3j%2FF7x0EUgqsxewVFpUwj%2BC8ygY6pgFb5aljC%2BmjnVsO3%2BO3SJafyUZnow2MPgAGyVw0HwSEae6rgQVjvG7fxoB%2F0457CZ2i%2BHV%2Fnt7pnU%2Bz51bcL7XiOrsASWU7Ul%2FSNQgU1qkUlpeNQCoDIQPGuvDl5ekAESHPtPWypB3517O4fWHWSoBpJQW5nJp7gkDdWk4Sfbwy4%2Fmu7%2FMS98z%2Bx%2FeyLt0qBn%2F6sxg67Qz3TDauYLTembjc5KrXJ8nX&X-Amz-Signature=3d9795b2b1e65b2baf945238e6de5a25a56512640c2163241a29e64c8a0b31b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIFLS43T%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwC7TviyqVXKU%2BkQooZ2fMzkmOYj%2BlMmpZh6UXRpm2kAiAIq7mCKHt4oUobv%2BvyKD5pmnLjSzBwnZlSxAJIGbcuyyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMgU6xUG5Pp2n4ah6zKtwDQUro9q0Q3HXF%2FxLwjjVVDmDu1SCcqNqcWRVWdaTvHEssynUZAB5d501OOHsnYXHfi4Yy2P%2B5re2KHiN2ZVq6YAeFBQ%2BdVN%2FNp6GSB5b5YvG0%2FaiXXbjO2c5Nu1QjrL22ytWjHCFYbx3xcZynCaalxNHbRQMIHgnFZmPGZPZtogBQcoow7lZmRyWVC2I2bEcIhcE4YGmf0UQRunS00quXQR%2BkPjZ2ex9UBoJNJLPZXvxrh8GC%2FORCk49atxo8pb1i7gSWHLr6JW0%2FDO3e0zr2E58y6%2FENsxDf1TzAs6GjzRS4dk6WFqhgZ7asn2MkZdFG%2FfU%2FFjNAYwSsrTFcJnt1%2BTllpdimSQc4yLsOIkAtyWw%2FvmyL5iQgw%2B47S%2FzFXgr9BadNWcQ72XO1A3sBQPeaMZ2Xs8sCog2yvp9wqjIDx0mk%2FfGLT3NlGq3wD3okHbS1%2B6%2FmcLfSdzqvvs7BA2Al8JF0ytSp0FvpkWVp%2FO1CDVoGkjtGffGR90fVh%2BR5IhljNKtMwKjSzROmqIMwcJbr1Jgv5L7D661%2Fi9Em1f7gu60a3a8HT2TlXWzk8kddP8MW0i3PPHdjSbpQP4hCqcBbQexJYw38eF9efVmLQvLT3j%2FF7x0EUgqsxewVFpUwj%2BC8ygY6pgFb5aljC%2BmjnVsO3%2BO3SJafyUZnow2MPgAGyVw0HwSEae6rgQVjvG7fxoB%2F0457CZ2i%2BHV%2Fnt7pnU%2Bz51bcL7XiOrsASWU7Ul%2FSNQgU1qkUlpeNQCoDIQPGuvDl5ekAESHPtPWypB3517O4fWHWSoBpJQW5nJp7gkDdWk4Sfbwy4%2Fmu7%2FMS98z%2Bx%2FeyLt0qBn%2F6sxg67Qz3TDauYLTembjc5KrXJ8nX&X-Amz-Signature=5d9461a5d4bc77b7a86f9081ec82ee8ce9e465932db76289cbdd7a3e369945df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIFLS43T%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFwC7TviyqVXKU%2BkQooZ2fMzkmOYj%2BlMmpZh6UXRpm2kAiAIq7mCKHt4oUobv%2BvyKD5pmnLjSzBwnZlSxAJIGbcuyyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMgU6xUG5Pp2n4ah6zKtwDQUro9q0Q3HXF%2FxLwjjVVDmDu1SCcqNqcWRVWdaTvHEssynUZAB5d501OOHsnYXHfi4Yy2P%2B5re2KHiN2ZVq6YAeFBQ%2BdVN%2FNp6GSB5b5YvG0%2FaiXXbjO2c5Nu1QjrL22ytWjHCFYbx3xcZynCaalxNHbRQMIHgnFZmPGZPZtogBQcoow7lZmRyWVC2I2bEcIhcE4YGmf0UQRunS00quXQR%2BkPjZ2ex9UBoJNJLPZXvxrh8GC%2FORCk49atxo8pb1i7gSWHLr6JW0%2FDO3e0zr2E58y6%2FENsxDf1TzAs6GjzRS4dk6WFqhgZ7asn2MkZdFG%2FfU%2FFjNAYwSsrTFcJnt1%2BTllpdimSQc4yLsOIkAtyWw%2FvmyL5iQgw%2B47S%2FzFXgr9BadNWcQ72XO1A3sBQPeaMZ2Xs8sCog2yvp9wqjIDx0mk%2FfGLT3NlGq3wD3okHbS1%2B6%2FmcLfSdzqvvs7BA2Al8JF0ytSp0FvpkWVp%2FO1CDVoGkjtGffGR90fVh%2BR5IhljNKtMwKjSzROmqIMwcJbr1Jgv5L7D661%2Fi9Em1f7gu60a3a8HT2TlXWzk8kddP8MW0i3PPHdjSbpQP4hCqcBbQexJYw38eF9efVmLQvLT3j%2FF7x0EUgqsxewVFpUwj%2BC8ygY6pgFb5aljC%2BmjnVsO3%2BO3SJafyUZnow2MPgAGyVw0HwSEae6rgQVjvG7fxoB%2F0457CZ2i%2BHV%2Fnt7pnU%2Bz51bcL7XiOrsASWU7Ul%2FSNQgU1qkUlpeNQCoDIQPGuvDl5ekAESHPtPWypB3517O4fWHWSoBpJQW5nJp7gkDdWk4Sfbwy4%2Fmu7%2FMS98z%2Bx%2FeyLt0qBn%2F6sxg67Qz3TDauYLTembjc5KrXJ8nX&X-Amz-Signature=076a2d68f0bc943ff4780197f1da81a723ce27ca177b6571fbbad175c3ffba6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

