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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZMHYHJX%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwPhHDjU66lX23jCIJxnyYMIJz%2FzXfo%2FU6xm1b3wC3SAIgdJ2L9NrNmPNvwrEx5Yg%2BvTD4DF8kBw9CzaOKU6p2y2AqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2Eqrp1%2B4nkK89KLircA5FAUsPSXkZ2iTZB6wn92%2BXOPYw86CEWuCoftedTWbU0k6Vx1QWuaATp0Vfc%2BXCKpdEsLQ9lgl2%2BlB83AWQkYFWXxmVD2%2BqYLdg3OFqhCkIB8Ur%2FnZu3GOzqzib1iTmKr6ocbHKtxsySFcs0QzJ%2FVimb9KknpUip5l3%2BMERdtpsjO6ZZ0svy9hNMIDhb6NRXtE6YXGnWabrV2B%2BT%2FR2y3NqXHGQonLhA5jbqMLElykv7NvSaIzsJdUYEB6354EFiuHHDkUY%2F2u2RAyCPKQ9nMEBXCVi1VL7rN4UQPePZny1BUp0TSpKTBgVWOXdd%2F621Hb%2BOTW%2BEEeTTqpB24LHm7C%2BaCmXwJilD1DD%2FB43%2F3FWFAst2Z%2FdQZbhvxfmzWmJZnFfuY2wdA7jOdpbEvrKXLD7JiZel9%2B471bxOtOxhOJI%2B143kdo3QnsxfwItwjVNagtBX%2Fhrl4xyQvTaCn9fOM81nbYBVG8R8LrQhd1CTSDNHIQJAO2I%2Bv%2FHSI0UvBUrnyPhECPQgINSw2mzeeq2QPROqrrFIkvhyQW2iHosobqqAmduqdSaAHios76aQKtZiczOs%2B5Q8cKKQWsgekvuFYWMuisrG6%2F7bjGy7x%2BZHfeaAwDc5ySKdLxPaeieoMJD80coGOqUBmeyB7%2FyrlqTJrI%2BTHujMi3Ukxfb5lkWLhHfTqWXDM0849wvdU0L5fpvcJlBz884oxH3Pi98%2BlPMo78P5Ilysxm%2FLXO%2BAvYxvMlQqAQgF4UaovpTXIx7%2FCOHhb1mZ5oTYlGePOLErFzj34VDyOZIUJIu6q4iYTZOZgt9gyZZIjEVr6jNCizQc2H0lB5vmOBesyQf99SBuTY49vupyGIRgThurLU4M&X-Amz-Signature=a2cac55b7e9fd0dbf603a724baad501678d9d02db631bef26ccd432279eacf93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZMHYHJX%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwPhHDjU66lX23jCIJxnyYMIJz%2FzXfo%2FU6xm1b3wC3SAIgdJ2L9NrNmPNvwrEx5Yg%2BvTD4DF8kBw9CzaOKU6p2y2AqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2Eqrp1%2B4nkK89KLircA5FAUsPSXkZ2iTZB6wn92%2BXOPYw86CEWuCoftedTWbU0k6Vx1QWuaATp0Vfc%2BXCKpdEsLQ9lgl2%2BlB83AWQkYFWXxmVD2%2BqYLdg3OFqhCkIB8Ur%2FnZu3GOzqzib1iTmKr6ocbHKtxsySFcs0QzJ%2FVimb9KknpUip5l3%2BMERdtpsjO6ZZ0svy9hNMIDhb6NRXtE6YXGnWabrV2B%2BT%2FR2y3NqXHGQonLhA5jbqMLElykv7NvSaIzsJdUYEB6354EFiuHHDkUY%2F2u2RAyCPKQ9nMEBXCVi1VL7rN4UQPePZny1BUp0TSpKTBgVWOXdd%2F621Hb%2BOTW%2BEEeTTqpB24LHm7C%2BaCmXwJilD1DD%2FB43%2F3FWFAst2Z%2FdQZbhvxfmzWmJZnFfuY2wdA7jOdpbEvrKXLD7JiZel9%2B471bxOtOxhOJI%2B143kdo3QnsxfwItwjVNagtBX%2Fhrl4xyQvTaCn9fOM81nbYBVG8R8LrQhd1CTSDNHIQJAO2I%2Bv%2FHSI0UvBUrnyPhECPQgINSw2mzeeq2QPROqrrFIkvhyQW2iHosobqqAmduqdSaAHios76aQKtZiczOs%2B5Q8cKKQWsgekvuFYWMuisrG6%2F7bjGy7x%2BZHfeaAwDc5ySKdLxPaeieoMJD80coGOqUBmeyB7%2FyrlqTJrI%2BTHujMi3Ukxfb5lkWLhHfTqWXDM0849wvdU0L5fpvcJlBz884oxH3Pi98%2BlPMo78P5Ilysxm%2FLXO%2BAvYxvMlQqAQgF4UaovpTXIx7%2FCOHhb1mZ5oTYlGePOLErFzj34VDyOZIUJIu6q4iYTZOZgt9gyZZIjEVr6jNCizQc2H0lB5vmOBesyQf99SBuTY49vupyGIRgThurLU4M&X-Amz-Signature=0d6e9bb954fe962acf8b4bc87f02c66c4a2d0aeff8488606e102d408ebd4aeb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZMHYHJX%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwPhHDjU66lX23jCIJxnyYMIJz%2FzXfo%2FU6xm1b3wC3SAIgdJ2L9NrNmPNvwrEx5Yg%2BvTD4DF8kBw9CzaOKU6p2y2AqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2Eqrp1%2B4nkK89KLircA5FAUsPSXkZ2iTZB6wn92%2BXOPYw86CEWuCoftedTWbU0k6Vx1QWuaATp0Vfc%2BXCKpdEsLQ9lgl2%2BlB83AWQkYFWXxmVD2%2BqYLdg3OFqhCkIB8Ur%2FnZu3GOzqzib1iTmKr6ocbHKtxsySFcs0QzJ%2FVimb9KknpUip5l3%2BMERdtpsjO6ZZ0svy9hNMIDhb6NRXtE6YXGnWabrV2B%2BT%2FR2y3NqXHGQonLhA5jbqMLElykv7NvSaIzsJdUYEB6354EFiuHHDkUY%2F2u2RAyCPKQ9nMEBXCVi1VL7rN4UQPePZny1BUp0TSpKTBgVWOXdd%2F621Hb%2BOTW%2BEEeTTqpB24LHm7C%2BaCmXwJilD1DD%2FB43%2F3FWFAst2Z%2FdQZbhvxfmzWmJZnFfuY2wdA7jOdpbEvrKXLD7JiZel9%2B471bxOtOxhOJI%2B143kdo3QnsxfwItwjVNagtBX%2Fhrl4xyQvTaCn9fOM81nbYBVG8R8LrQhd1CTSDNHIQJAO2I%2Bv%2FHSI0UvBUrnyPhECPQgINSw2mzeeq2QPROqrrFIkvhyQW2iHosobqqAmduqdSaAHios76aQKtZiczOs%2B5Q8cKKQWsgekvuFYWMuisrG6%2F7bjGy7x%2BZHfeaAwDc5ySKdLxPaeieoMJD80coGOqUBmeyB7%2FyrlqTJrI%2BTHujMi3Ukxfb5lkWLhHfTqWXDM0849wvdU0L5fpvcJlBz884oxH3Pi98%2BlPMo78P5Ilysxm%2FLXO%2BAvYxvMlQqAQgF4UaovpTXIx7%2FCOHhb1mZ5oTYlGePOLErFzj34VDyOZIUJIu6q4iYTZOZgt9gyZZIjEVr6jNCizQc2H0lB5vmOBesyQf99SBuTY49vupyGIRgThurLU4M&X-Amz-Signature=ff493f4a95a02d8971920e3f065e45778d01d42c392fd5c60e26454e5ded0345&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZMHYHJX%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwPhHDjU66lX23jCIJxnyYMIJz%2FzXfo%2FU6xm1b3wC3SAIgdJ2L9NrNmPNvwrEx5Yg%2BvTD4DF8kBw9CzaOKU6p2y2AqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2Eqrp1%2B4nkK89KLircA5FAUsPSXkZ2iTZB6wn92%2BXOPYw86CEWuCoftedTWbU0k6Vx1QWuaATp0Vfc%2BXCKpdEsLQ9lgl2%2BlB83AWQkYFWXxmVD2%2BqYLdg3OFqhCkIB8Ur%2FnZu3GOzqzib1iTmKr6ocbHKtxsySFcs0QzJ%2FVimb9KknpUip5l3%2BMERdtpsjO6ZZ0svy9hNMIDhb6NRXtE6YXGnWabrV2B%2BT%2FR2y3NqXHGQonLhA5jbqMLElykv7NvSaIzsJdUYEB6354EFiuHHDkUY%2F2u2RAyCPKQ9nMEBXCVi1VL7rN4UQPePZny1BUp0TSpKTBgVWOXdd%2F621Hb%2BOTW%2BEEeTTqpB24LHm7C%2BaCmXwJilD1DD%2FB43%2F3FWFAst2Z%2FdQZbhvxfmzWmJZnFfuY2wdA7jOdpbEvrKXLD7JiZel9%2B471bxOtOxhOJI%2B143kdo3QnsxfwItwjVNagtBX%2Fhrl4xyQvTaCn9fOM81nbYBVG8R8LrQhd1CTSDNHIQJAO2I%2Bv%2FHSI0UvBUrnyPhECPQgINSw2mzeeq2QPROqrrFIkvhyQW2iHosobqqAmduqdSaAHios76aQKtZiczOs%2B5Q8cKKQWsgekvuFYWMuisrG6%2F7bjGy7x%2BZHfeaAwDc5ySKdLxPaeieoMJD80coGOqUBmeyB7%2FyrlqTJrI%2BTHujMi3Ukxfb5lkWLhHfTqWXDM0849wvdU0L5fpvcJlBz884oxH3Pi98%2BlPMo78P5Ilysxm%2FLXO%2BAvYxvMlQqAQgF4UaovpTXIx7%2FCOHhb1mZ5oTYlGePOLErFzj34VDyOZIUJIu6q4iYTZOZgt9gyZZIjEVr6jNCizQc2H0lB5vmOBesyQf99SBuTY49vupyGIRgThurLU4M&X-Amz-Signature=79907d7140e33433e7c57ab7178088c0d3c129c3bde826ada3b8d91f4be76251&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZMHYHJX%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwPhHDjU66lX23jCIJxnyYMIJz%2FzXfo%2FU6xm1b3wC3SAIgdJ2L9NrNmPNvwrEx5Yg%2BvTD4DF8kBw9CzaOKU6p2y2AqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2Eqrp1%2B4nkK89KLircA5FAUsPSXkZ2iTZB6wn92%2BXOPYw86CEWuCoftedTWbU0k6Vx1QWuaATp0Vfc%2BXCKpdEsLQ9lgl2%2BlB83AWQkYFWXxmVD2%2BqYLdg3OFqhCkIB8Ur%2FnZu3GOzqzib1iTmKr6ocbHKtxsySFcs0QzJ%2FVimb9KknpUip5l3%2BMERdtpsjO6ZZ0svy9hNMIDhb6NRXtE6YXGnWabrV2B%2BT%2FR2y3NqXHGQonLhA5jbqMLElykv7NvSaIzsJdUYEB6354EFiuHHDkUY%2F2u2RAyCPKQ9nMEBXCVi1VL7rN4UQPePZny1BUp0TSpKTBgVWOXdd%2F621Hb%2BOTW%2BEEeTTqpB24LHm7C%2BaCmXwJilD1DD%2FB43%2F3FWFAst2Z%2FdQZbhvxfmzWmJZnFfuY2wdA7jOdpbEvrKXLD7JiZel9%2B471bxOtOxhOJI%2B143kdo3QnsxfwItwjVNagtBX%2Fhrl4xyQvTaCn9fOM81nbYBVG8R8LrQhd1CTSDNHIQJAO2I%2Bv%2FHSI0UvBUrnyPhECPQgINSw2mzeeq2QPROqrrFIkvhyQW2iHosobqqAmduqdSaAHios76aQKtZiczOs%2B5Q8cKKQWsgekvuFYWMuisrG6%2F7bjGy7x%2BZHfeaAwDc5ySKdLxPaeieoMJD80coGOqUBmeyB7%2FyrlqTJrI%2BTHujMi3Ukxfb5lkWLhHfTqWXDM0849wvdU0L5fpvcJlBz884oxH3Pi98%2BlPMo78P5Ilysxm%2FLXO%2BAvYxvMlQqAQgF4UaovpTXIx7%2FCOHhb1mZ5oTYlGePOLErFzj34VDyOZIUJIu6q4iYTZOZgt9gyZZIjEVr6jNCizQc2H0lB5vmOBesyQf99SBuTY49vupyGIRgThurLU4M&X-Amz-Signature=d7db415bf934203198222c4257c9d761c7cb13e765edc3c07d20e40133d1158c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZMHYHJX%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwPhHDjU66lX23jCIJxnyYMIJz%2FzXfo%2FU6xm1b3wC3SAIgdJ2L9NrNmPNvwrEx5Yg%2BvTD4DF8kBw9CzaOKU6p2y2AqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2Eqrp1%2B4nkK89KLircA5FAUsPSXkZ2iTZB6wn92%2BXOPYw86CEWuCoftedTWbU0k6Vx1QWuaATp0Vfc%2BXCKpdEsLQ9lgl2%2BlB83AWQkYFWXxmVD2%2BqYLdg3OFqhCkIB8Ur%2FnZu3GOzqzib1iTmKr6ocbHKtxsySFcs0QzJ%2FVimb9KknpUip5l3%2BMERdtpsjO6ZZ0svy9hNMIDhb6NRXtE6YXGnWabrV2B%2BT%2FR2y3NqXHGQonLhA5jbqMLElykv7NvSaIzsJdUYEB6354EFiuHHDkUY%2F2u2RAyCPKQ9nMEBXCVi1VL7rN4UQPePZny1BUp0TSpKTBgVWOXdd%2F621Hb%2BOTW%2BEEeTTqpB24LHm7C%2BaCmXwJilD1DD%2FB43%2F3FWFAst2Z%2FdQZbhvxfmzWmJZnFfuY2wdA7jOdpbEvrKXLD7JiZel9%2B471bxOtOxhOJI%2B143kdo3QnsxfwItwjVNagtBX%2Fhrl4xyQvTaCn9fOM81nbYBVG8R8LrQhd1CTSDNHIQJAO2I%2Bv%2FHSI0UvBUrnyPhECPQgINSw2mzeeq2QPROqrrFIkvhyQW2iHosobqqAmduqdSaAHios76aQKtZiczOs%2B5Q8cKKQWsgekvuFYWMuisrG6%2F7bjGy7x%2BZHfeaAwDc5ySKdLxPaeieoMJD80coGOqUBmeyB7%2FyrlqTJrI%2BTHujMi3Ukxfb5lkWLhHfTqWXDM0849wvdU0L5fpvcJlBz884oxH3Pi98%2BlPMo78P5Ilysxm%2FLXO%2BAvYxvMlQqAQgF4UaovpTXIx7%2FCOHhb1mZ5oTYlGePOLErFzj34VDyOZIUJIu6q4iYTZOZgt9gyZZIjEVr6jNCizQc2H0lB5vmOBesyQf99SBuTY49vupyGIRgThurLU4M&X-Amz-Signature=5ae2a8a02b3197b1d86e5c3f7f1393bbbbdb74ad20c9c019b58053de6392acaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZMHYHJX%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwPhHDjU66lX23jCIJxnyYMIJz%2FzXfo%2FU6xm1b3wC3SAIgdJ2L9NrNmPNvwrEx5Yg%2BvTD4DF8kBw9CzaOKU6p2y2AqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2Eqrp1%2B4nkK89KLircA5FAUsPSXkZ2iTZB6wn92%2BXOPYw86CEWuCoftedTWbU0k6Vx1QWuaATp0Vfc%2BXCKpdEsLQ9lgl2%2BlB83AWQkYFWXxmVD2%2BqYLdg3OFqhCkIB8Ur%2FnZu3GOzqzib1iTmKr6ocbHKtxsySFcs0QzJ%2FVimb9KknpUip5l3%2BMERdtpsjO6ZZ0svy9hNMIDhb6NRXtE6YXGnWabrV2B%2BT%2FR2y3NqXHGQonLhA5jbqMLElykv7NvSaIzsJdUYEB6354EFiuHHDkUY%2F2u2RAyCPKQ9nMEBXCVi1VL7rN4UQPePZny1BUp0TSpKTBgVWOXdd%2F621Hb%2BOTW%2BEEeTTqpB24LHm7C%2BaCmXwJilD1DD%2FB43%2F3FWFAst2Z%2FdQZbhvxfmzWmJZnFfuY2wdA7jOdpbEvrKXLD7JiZel9%2B471bxOtOxhOJI%2B143kdo3QnsxfwItwjVNagtBX%2Fhrl4xyQvTaCn9fOM81nbYBVG8R8LrQhd1CTSDNHIQJAO2I%2Bv%2FHSI0UvBUrnyPhECPQgINSw2mzeeq2QPROqrrFIkvhyQW2iHosobqqAmduqdSaAHios76aQKtZiczOs%2B5Q8cKKQWsgekvuFYWMuisrG6%2F7bjGy7x%2BZHfeaAwDc5ySKdLxPaeieoMJD80coGOqUBmeyB7%2FyrlqTJrI%2BTHujMi3Ukxfb5lkWLhHfTqWXDM0849wvdU0L5fpvcJlBz884oxH3Pi98%2BlPMo78P5Ilysxm%2FLXO%2BAvYxvMlQqAQgF4UaovpTXIx7%2FCOHhb1mZ5oTYlGePOLErFzj34VDyOZIUJIu6q4iYTZOZgt9gyZZIjEVr6jNCizQc2H0lB5vmOBesyQf99SBuTY49vupyGIRgThurLU4M&X-Amz-Signature=866b876c4e1dca486fda12fc3a962754fe34fca0f2a36b5ce1d216bcdc8913eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZMHYHJX%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwPhHDjU66lX23jCIJxnyYMIJz%2FzXfo%2FU6xm1b3wC3SAIgdJ2L9NrNmPNvwrEx5Yg%2BvTD4DF8kBw9CzaOKU6p2y2AqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2Eqrp1%2B4nkK89KLircA5FAUsPSXkZ2iTZB6wn92%2BXOPYw86CEWuCoftedTWbU0k6Vx1QWuaATp0Vfc%2BXCKpdEsLQ9lgl2%2BlB83AWQkYFWXxmVD2%2BqYLdg3OFqhCkIB8Ur%2FnZu3GOzqzib1iTmKr6ocbHKtxsySFcs0QzJ%2FVimb9KknpUip5l3%2BMERdtpsjO6ZZ0svy9hNMIDhb6NRXtE6YXGnWabrV2B%2BT%2FR2y3NqXHGQonLhA5jbqMLElykv7NvSaIzsJdUYEB6354EFiuHHDkUY%2F2u2RAyCPKQ9nMEBXCVi1VL7rN4UQPePZny1BUp0TSpKTBgVWOXdd%2F621Hb%2BOTW%2BEEeTTqpB24LHm7C%2BaCmXwJilD1DD%2FB43%2F3FWFAst2Z%2FdQZbhvxfmzWmJZnFfuY2wdA7jOdpbEvrKXLD7JiZel9%2B471bxOtOxhOJI%2B143kdo3QnsxfwItwjVNagtBX%2Fhrl4xyQvTaCn9fOM81nbYBVG8R8LrQhd1CTSDNHIQJAO2I%2Bv%2FHSI0UvBUrnyPhECPQgINSw2mzeeq2QPROqrrFIkvhyQW2iHosobqqAmduqdSaAHios76aQKtZiczOs%2B5Q8cKKQWsgekvuFYWMuisrG6%2F7bjGy7x%2BZHfeaAwDc5ySKdLxPaeieoMJD80coGOqUBmeyB7%2FyrlqTJrI%2BTHujMi3Ukxfb5lkWLhHfTqWXDM0849wvdU0L5fpvcJlBz884oxH3Pi98%2BlPMo78P5Ilysxm%2FLXO%2BAvYxvMlQqAQgF4UaovpTXIx7%2FCOHhb1mZ5oTYlGePOLErFzj34VDyOZIUJIu6q4iYTZOZgt9gyZZIjEVr6jNCizQc2H0lB5vmOBesyQf99SBuTY49vupyGIRgThurLU4M&X-Amz-Signature=2f77d27e08f2907d5f73b8700771352f5938a577f7733745c0efb2b5125c2888&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZMHYHJX%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwPhHDjU66lX23jCIJxnyYMIJz%2FzXfo%2FU6xm1b3wC3SAIgdJ2L9NrNmPNvwrEx5Yg%2BvTD4DF8kBw9CzaOKU6p2y2AqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2Eqrp1%2B4nkK89KLircA5FAUsPSXkZ2iTZB6wn92%2BXOPYw86CEWuCoftedTWbU0k6Vx1QWuaATp0Vfc%2BXCKpdEsLQ9lgl2%2BlB83AWQkYFWXxmVD2%2BqYLdg3OFqhCkIB8Ur%2FnZu3GOzqzib1iTmKr6ocbHKtxsySFcs0QzJ%2FVimb9KknpUip5l3%2BMERdtpsjO6ZZ0svy9hNMIDhb6NRXtE6YXGnWabrV2B%2BT%2FR2y3NqXHGQonLhA5jbqMLElykv7NvSaIzsJdUYEB6354EFiuHHDkUY%2F2u2RAyCPKQ9nMEBXCVi1VL7rN4UQPePZny1BUp0TSpKTBgVWOXdd%2F621Hb%2BOTW%2BEEeTTqpB24LHm7C%2BaCmXwJilD1DD%2FB43%2F3FWFAst2Z%2FdQZbhvxfmzWmJZnFfuY2wdA7jOdpbEvrKXLD7JiZel9%2B471bxOtOxhOJI%2B143kdo3QnsxfwItwjVNagtBX%2Fhrl4xyQvTaCn9fOM81nbYBVG8R8LrQhd1CTSDNHIQJAO2I%2Bv%2FHSI0UvBUrnyPhECPQgINSw2mzeeq2QPROqrrFIkvhyQW2iHosobqqAmduqdSaAHios76aQKtZiczOs%2B5Q8cKKQWsgekvuFYWMuisrG6%2F7bjGy7x%2BZHfeaAwDc5ySKdLxPaeieoMJD80coGOqUBmeyB7%2FyrlqTJrI%2BTHujMi3Ukxfb5lkWLhHfTqWXDM0849wvdU0L5fpvcJlBz884oxH3Pi98%2BlPMo78P5Ilysxm%2FLXO%2BAvYxvMlQqAQgF4UaovpTXIx7%2FCOHhb1mZ5oTYlGePOLErFzj34VDyOZIUJIu6q4iYTZOZgt9gyZZIjEVr6jNCizQc2H0lB5vmOBesyQf99SBuTY49vupyGIRgThurLU4M&X-Amz-Signature=e0c43c3e5edee11f85dcc2dc811efcaf6ca39303d001ba09bc80d3a246a92753&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZMHYHJX%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwPhHDjU66lX23jCIJxnyYMIJz%2FzXfo%2FU6xm1b3wC3SAIgdJ2L9NrNmPNvwrEx5Yg%2BvTD4DF8kBw9CzaOKU6p2y2AqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2Eqrp1%2B4nkK89KLircA5FAUsPSXkZ2iTZB6wn92%2BXOPYw86CEWuCoftedTWbU0k6Vx1QWuaATp0Vfc%2BXCKpdEsLQ9lgl2%2BlB83AWQkYFWXxmVD2%2BqYLdg3OFqhCkIB8Ur%2FnZu3GOzqzib1iTmKr6ocbHKtxsySFcs0QzJ%2FVimb9KknpUip5l3%2BMERdtpsjO6ZZ0svy9hNMIDhb6NRXtE6YXGnWabrV2B%2BT%2FR2y3NqXHGQonLhA5jbqMLElykv7NvSaIzsJdUYEB6354EFiuHHDkUY%2F2u2RAyCPKQ9nMEBXCVi1VL7rN4UQPePZny1BUp0TSpKTBgVWOXdd%2F621Hb%2BOTW%2BEEeTTqpB24LHm7C%2BaCmXwJilD1DD%2FB43%2F3FWFAst2Z%2FdQZbhvxfmzWmJZnFfuY2wdA7jOdpbEvrKXLD7JiZel9%2B471bxOtOxhOJI%2B143kdo3QnsxfwItwjVNagtBX%2Fhrl4xyQvTaCn9fOM81nbYBVG8R8LrQhd1CTSDNHIQJAO2I%2Bv%2FHSI0UvBUrnyPhECPQgINSw2mzeeq2QPROqrrFIkvhyQW2iHosobqqAmduqdSaAHios76aQKtZiczOs%2B5Q8cKKQWsgekvuFYWMuisrG6%2F7bjGy7x%2BZHfeaAwDc5ySKdLxPaeieoMJD80coGOqUBmeyB7%2FyrlqTJrI%2BTHujMi3Ukxfb5lkWLhHfTqWXDM0849wvdU0L5fpvcJlBz884oxH3Pi98%2BlPMo78P5Ilysxm%2FLXO%2BAvYxvMlQqAQgF4UaovpTXIx7%2FCOHhb1mZ5oTYlGePOLErFzj34VDyOZIUJIu6q4iYTZOZgt9gyZZIjEVr6jNCizQc2H0lB5vmOBesyQf99SBuTY49vupyGIRgThurLU4M&X-Amz-Signature=06071d61e2db77977bad1f71a9fcdf9d7f9cebd15e490e0307cd1c27e51001b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

