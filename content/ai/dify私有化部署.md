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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZABAODUR%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0Dzc2omxe6WAu%2FJtN8%2BLo9ygcaflcJunVhGTp810iwIhAMmSmL5qoTx3RyC0s1DUN9A25%2Fx3eIUFiYGIpHIpMpWTKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydyLHOBCIdc8FYhnYq3APu9VpQguZ5236SpW3PlDZs6EqyouMC3QYP7gsBlgUa209vooexKR0nkyz3Po0kL05Pzyqi15plRRwC%2BNp4MCvb84winmnM17mWvoFpHXD23aebTm9hFwpk%2BZWbBF6R%2FUmzl%2BOTgVb0WtXGvYQga9aQ47qhiIM%2FQNYeOftnf%2BJrjVkjGaqY2VS1su%2BwccRETCv%2Foc80ifcYznbbkUEBQ206%2F59VO%2Ftvf13DlkmucFh9DTbG7CRj%2BbroGP1MhWMLzx7EDyXPvzkBWTeegAWuSn2tmzdknJ2UL4XjpEdl7fz2yJB87is0iJZ6PohOJRneBKqjf6A68q1S6M8nN2ZZPltud174xY5I1rYiKxsh09QIc7ZD9B4yy55TJxX1T2XVCIAi9rv5gX%2BlWZXI2kEBrrpHJ98Aesnj1Pucd2L9tewfrw%2Fg%2BnBVRjOBwuBjTUBI%2FLSu0uFxapNXRvqrYdeToEv8t1p60pNhILvttbPiqq0trDJLCk9lzLMQnUZKBubKDS82Fb9xefkVXA59CXPrvP1EHah6MEB4eOJMZuPZKz0EG5uXqJloOSJ7JHovYZHPdzpLVVEabrkNywnKzGM%2BeDWCkcwLKLRrzxCSyNghNOJjxkP5l3C2OHH3UWYwZzDvn8fOBjqkAf0x28%2BJ8GQjGVM%2FY0bW53FfKmG7owRsfZCQtodFQkSuq6pGrClcWcUWkl%2FpLVBStU9T7Xn3vSutft8s3wQwVpU9k9mbzlSzWRq0WKL%2BwefmppDHusNOHT1wpoKUL8sENPydEntrXHHfXRmazK3vh0KLKml7Yu5bpnMlxlv46Ju3GQqq4ycR%2FvuUxEnTAp%2BhHDuggWrwDzAu8E%2B7ior%2F0Q4MsiMN&X-Amz-Signature=b8f4d2f00d535353e3b5626e4a622ea40b1411b0ed46d86c6c4730b7661bf4f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZABAODUR%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0Dzc2omxe6WAu%2FJtN8%2BLo9ygcaflcJunVhGTp810iwIhAMmSmL5qoTx3RyC0s1DUN9A25%2Fx3eIUFiYGIpHIpMpWTKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydyLHOBCIdc8FYhnYq3APu9VpQguZ5236SpW3PlDZs6EqyouMC3QYP7gsBlgUa209vooexKR0nkyz3Po0kL05Pzyqi15plRRwC%2BNp4MCvb84winmnM17mWvoFpHXD23aebTm9hFwpk%2BZWbBF6R%2FUmzl%2BOTgVb0WtXGvYQga9aQ47qhiIM%2FQNYeOftnf%2BJrjVkjGaqY2VS1su%2BwccRETCv%2Foc80ifcYznbbkUEBQ206%2F59VO%2Ftvf13DlkmucFh9DTbG7CRj%2BbroGP1MhWMLzx7EDyXPvzkBWTeegAWuSn2tmzdknJ2UL4XjpEdl7fz2yJB87is0iJZ6PohOJRneBKqjf6A68q1S6M8nN2ZZPltud174xY5I1rYiKxsh09QIc7ZD9B4yy55TJxX1T2XVCIAi9rv5gX%2BlWZXI2kEBrrpHJ98Aesnj1Pucd2L9tewfrw%2Fg%2BnBVRjOBwuBjTUBI%2FLSu0uFxapNXRvqrYdeToEv8t1p60pNhILvttbPiqq0trDJLCk9lzLMQnUZKBubKDS82Fb9xefkVXA59CXPrvP1EHah6MEB4eOJMZuPZKz0EG5uXqJloOSJ7JHovYZHPdzpLVVEabrkNywnKzGM%2BeDWCkcwLKLRrzxCSyNghNOJjxkP5l3C2OHH3UWYwZzDvn8fOBjqkAf0x28%2BJ8GQjGVM%2FY0bW53FfKmG7owRsfZCQtodFQkSuq6pGrClcWcUWkl%2FpLVBStU9T7Xn3vSutft8s3wQwVpU9k9mbzlSzWRq0WKL%2BwefmppDHusNOHT1wpoKUL8sENPydEntrXHHfXRmazK3vh0KLKml7Yu5bpnMlxlv46Ju3GQqq4ycR%2FvuUxEnTAp%2BhHDuggWrwDzAu8E%2B7ior%2F0Q4MsiMN&X-Amz-Signature=003689ea2031b7e924155d8454a9cc0e49cedfbabede78df34a3528fd4600db1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZABAODUR%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0Dzc2omxe6WAu%2FJtN8%2BLo9ygcaflcJunVhGTp810iwIhAMmSmL5qoTx3RyC0s1DUN9A25%2Fx3eIUFiYGIpHIpMpWTKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydyLHOBCIdc8FYhnYq3APu9VpQguZ5236SpW3PlDZs6EqyouMC3QYP7gsBlgUa209vooexKR0nkyz3Po0kL05Pzyqi15plRRwC%2BNp4MCvb84winmnM17mWvoFpHXD23aebTm9hFwpk%2BZWbBF6R%2FUmzl%2BOTgVb0WtXGvYQga9aQ47qhiIM%2FQNYeOftnf%2BJrjVkjGaqY2VS1su%2BwccRETCv%2Foc80ifcYznbbkUEBQ206%2F59VO%2Ftvf13DlkmucFh9DTbG7CRj%2BbroGP1MhWMLzx7EDyXPvzkBWTeegAWuSn2tmzdknJ2UL4XjpEdl7fz2yJB87is0iJZ6PohOJRneBKqjf6A68q1S6M8nN2ZZPltud174xY5I1rYiKxsh09QIc7ZD9B4yy55TJxX1T2XVCIAi9rv5gX%2BlWZXI2kEBrrpHJ98Aesnj1Pucd2L9tewfrw%2Fg%2BnBVRjOBwuBjTUBI%2FLSu0uFxapNXRvqrYdeToEv8t1p60pNhILvttbPiqq0trDJLCk9lzLMQnUZKBubKDS82Fb9xefkVXA59CXPrvP1EHah6MEB4eOJMZuPZKz0EG5uXqJloOSJ7JHovYZHPdzpLVVEabrkNywnKzGM%2BeDWCkcwLKLRrzxCSyNghNOJjxkP5l3C2OHH3UWYwZzDvn8fOBjqkAf0x28%2BJ8GQjGVM%2FY0bW53FfKmG7owRsfZCQtodFQkSuq6pGrClcWcUWkl%2FpLVBStU9T7Xn3vSutft8s3wQwVpU9k9mbzlSzWRq0WKL%2BwefmppDHusNOHT1wpoKUL8sENPydEntrXHHfXRmazK3vh0KLKml7Yu5bpnMlxlv46Ju3GQqq4ycR%2FvuUxEnTAp%2BhHDuggWrwDzAu8E%2B7ior%2F0Q4MsiMN&X-Amz-Signature=04f2ba4ad1d25c6989cedaae752d7ece083395cfb33e25659f4b772b5dc61d30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZABAODUR%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0Dzc2omxe6WAu%2FJtN8%2BLo9ygcaflcJunVhGTp810iwIhAMmSmL5qoTx3RyC0s1DUN9A25%2Fx3eIUFiYGIpHIpMpWTKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydyLHOBCIdc8FYhnYq3APu9VpQguZ5236SpW3PlDZs6EqyouMC3QYP7gsBlgUa209vooexKR0nkyz3Po0kL05Pzyqi15plRRwC%2BNp4MCvb84winmnM17mWvoFpHXD23aebTm9hFwpk%2BZWbBF6R%2FUmzl%2BOTgVb0WtXGvYQga9aQ47qhiIM%2FQNYeOftnf%2BJrjVkjGaqY2VS1su%2BwccRETCv%2Foc80ifcYznbbkUEBQ206%2F59VO%2Ftvf13DlkmucFh9DTbG7CRj%2BbroGP1MhWMLzx7EDyXPvzkBWTeegAWuSn2tmzdknJ2UL4XjpEdl7fz2yJB87is0iJZ6PohOJRneBKqjf6A68q1S6M8nN2ZZPltud174xY5I1rYiKxsh09QIc7ZD9B4yy55TJxX1T2XVCIAi9rv5gX%2BlWZXI2kEBrrpHJ98Aesnj1Pucd2L9tewfrw%2Fg%2BnBVRjOBwuBjTUBI%2FLSu0uFxapNXRvqrYdeToEv8t1p60pNhILvttbPiqq0trDJLCk9lzLMQnUZKBubKDS82Fb9xefkVXA59CXPrvP1EHah6MEB4eOJMZuPZKz0EG5uXqJloOSJ7JHovYZHPdzpLVVEabrkNywnKzGM%2BeDWCkcwLKLRrzxCSyNghNOJjxkP5l3C2OHH3UWYwZzDvn8fOBjqkAf0x28%2BJ8GQjGVM%2FY0bW53FfKmG7owRsfZCQtodFQkSuq6pGrClcWcUWkl%2FpLVBStU9T7Xn3vSutft8s3wQwVpU9k9mbzlSzWRq0WKL%2BwefmppDHusNOHT1wpoKUL8sENPydEntrXHHfXRmazK3vh0KLKml7Yu5bpnMlxlv46Ju3GQqq4ycR%2FvuUxEnTAp%2BhHDuggWrwDzAu8E%2B7ior%2F0Q4MsiMN&X-Amz-Signature=ea0b63fe85d3dacd8e1781d32369a0f36f2cc1e6fd91e7f27fbac582181398d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZABAODUR%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0Dzc2omxe6WAu%2FJtN8%2BLo9ygcaflcJunVhGTp810iwIhAMmSmL5qoTx3RyC0s1DUN9A25%2Fx3eIUFiYGIpHIpMpWTKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydyLHOBCIdc8FYhnYq3APu9VpQguZ5236SpW3PlDZs6EqyouMC3QYP7gsBlgUa209vooexKR0nkyz3Po0kL05Pzyqi15plRRwC%2BNp4MCvb84winmnM17mWvoFpHXD23aebTm9hFwpk%2BZWbBF6R%2FUmzl%2BOTgVb0WtXGvYQga9aQ47qhiIM%2FQNYeOftnf%2BJrjVkjGaqY2VS1su%2BwccRETCv%2Foc80ifcYznbbkUEBQ206%2F59VO%2Ftvf13DlkmucFh9DTbG7CRj%2BbroGP1MhWMLzx7EDyXPvzkBWTeegAWuSn2tmzdknJ2UL4XjpEdl7fz2yJB87is0iJZ6PohOJRneBKqjf6A68q1S6M8nN2ZZPltud174xY5I1rYiKxsh09QIc7ZD9B4yy55TJxX1T2XVCIAi9rv5gX%2BlWZXI2kEBrrpHJ98Aesnj1Pucd2L9tewfrw%2Fg%2BnBVRjOBwuBjTUBI%2FLSu0uFxapNXRvqrYdeToEv8t1p60pNhILvttbPiqq0trDJLCk9lzLMQnUZKBubKDS82Fb9xefkVXA59CXPrvP1EHah6MEB4eOJMZuPZKz0EG5uXqJloOSJ7JHovYZHPdzpLVVEabrkNywnKzGM%2BeDWCkcwLKLRrzxCSyNghNOJjxkP5l3C2OHH3UWYwZzDvn8fOBjqkAf0x28%2BJ8GQjGVM%2FY0bW53FfKmG7owRsfZCQtodFQkSuq6pGrClcWcUWkl%2FpLVBStU9T7Xn3vSutft8s3wQwVpU9k9mbzlSzWRq0WKL%2BwefmppDHusNOHT1wpoKUL8sENPydEntrXHHfXRmazK3vh0KLKml7Yu5bpnMlxlv46Ju3GQqq4ycR%2FvuUxEnTAp%2BhHDuggWrwDzAu8E%2B7ior%2F0Q4MsiMN&X-Amz-Signature=e3735371e08d36956e8063ab69f46dd455b1a369effd478c5be642806fbf74e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZABAODUR%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0Dzc2omxe6WAu%2FJtN8%2BLo9ygcaflcJunVhGTp810iwIhAMmSmL5qoTx3RyC0s1DUN9A25%2Fx3eIUFiYGIpHIpMpWTKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydyLHOBCIdc8FYhnYq3APu9VpQguZ5236SpW3PlDZs6EqyouMC3QYP7gsBlgUa209vooexKR0nkyz3Po0kL05Pzyqi15plRRwC%2BNp4MCvb84winmnM17mWvoFpHXD23aebTm9hFwpk%2BZWbBF6R%2FUmzl%2BOTgVb0WtXGvYQga9aQ47qhiIM%2FQNYeOftnf%2BJrjVkjGaqY2VS1su%2BwccRETCv%2Foc80ifcYznbbkUEBQ206%2F59VO%2Ftvf13DlkmucFh9DTbG7CRj%2BbroGP1MhWMLzx7EDyXPvzkBWTeegAWuSn2tmzdknJ2UL4XjpEdl7fz2yJB87is0iJZ6PohOJRneBKqjf6A68q1S6M8nN2ZZPltud174xY5I1rYiKxsh09QIc7ZD9B4yy55TJxX1T2XVCIAi9rv5gX%2BlWZXI2kEBrrpHJ98Aesnj1Pucd2L9tewfrw%2Fg%2BnBVRjOBwuBjTUBI%2FLSu0uFxapNXRvqrYdeToEv8t1p60pNhILvttbPiqq0trDJLCk9lzLMQnUZKBubKDS82Fb9xefkVXA59CXPrvP1EHah6MEB4eOJMZuPZKz0EG5uXqJloOSJ7JHovYZHPdzpLVVEabrkNywnKzGM%2BeDWCkcwLKLRrzxCSyNghNOJjxkP5l3C2OHH3UWYwZzDvn8fOBjqkAf0x28%2BJ8GQjGVM%2FY0bW53FfKmG7owRsfZCQtodFQkSuq6pGrClcWcUWkl%2FpLVBStU9T7Xn3vSutft8s3wQwVpU9k9mbzlSzWRq0WKL%2BwefmppDHusNOHT1wpoKUL8sENPydEntrXHHfXRmazK3vh0KLKml7Yu5bpnMlxlv46Ju3GQqq4ycR%2FvuUxEnTAp%2BhHDuggWrwDzAu8E%2B7ior%2F0Q4MsiMN&X-Amz-Signature=d5f55977c4b83f76009f2623953f60ba93fb0347cb3bf201a022753acfb17540&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZABAODUR%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0Dzc2omxe6WAu%2FJtN8%2BLo9ygcaflcJunVhGTp810iwIhAMmSmL5qoTx3RyC0s1DUN9A25%2Fx3eIUFiYGIpHIpMpWTKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydyLHOBCIdc8FYhnYq3APu9VpQguZ5236SpW3PlDZs6EqyouMC3QYP7gsBlgUa209vooexKR0nkyz3Po0kL05Pzyqi15plRRwC%2BNp4MCvb84winmnM17mWvoFpHXD23aebTm9hFwpk%2BZWbBF6R%2FUmzl%2BOTgVb0WtXGvYQga9aQ47qhiIM%2FQNYeOftnf%2BJrjVkjGaqY2VS1su%2BwccRETCv%2Foc80ifcYznbbkUEBQ206%2F59VO%2Ftvf13DlkmucFh9DTbG7CRj%2BbroGP1MhWMLzx7EDyXPvzkBWTeegAWuSn2tmzdknJ2UL4XjpEdl7fz2yJB87is0iJZ6PohOJRneBKqjf6A68q1S6M8nN2ZZPltud174xY5I1rYiKxsh09QIc7ZD9B4yy55TJxX1T2XVCIAi9rv5gX%2BlWZXI2kEBrrpHJ98Aesnj1Pucd2L9tewfrw%2Fg%2BnBVRjOBwuBjTUBI%2FLSu0uFxapNXRvqrYdeToEv8t1p60pNhILvttbPiqq0trDJLCk9lzLMQnUZKBubKDS82Fb9xefkVXA59CXPrvP1EHah6MEB4eOJMZuPZKz0EG5uXqJloOSJ7JHovYZHPdzpLVVEabrkNywnKzGM%2BeDWCkcwLKLRrzxCSyNghNOJjxkP5l3C2OHH3UWYwZzDvn8fOBjqkAf0x28%2BJ8GQjGVM%2FY0bW53FfKmG7owRsfZCQtodFQkSuq6pGrClcWcUWkl%2FpLVBStU9T7Xn3vSutft8s3wQwVpU9k9mbzlSzWRq0WKL%2BwefmppDHusNOHT1wpoKUL8sENPydEntrXHHfXRmazK3vh0KLKml7Yu5bpnMlxlv46Ju3GQqq4ycR%2FvuUxEnTAp%2BhHDuggWrwDzAu8E%2B7ior%2F0Q4MsiMN&X-Amz-Signature=528282c8b01570d771fa31dc5f4246882f09e86a2bd50ea839ecfb3a3526b1dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZABAODUR%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0Dzc2omxe6WAu%2FJtN8%2BLo9ygcaflcJunVhGTp810iwIhAMmSmL5qoTx3RyC0s1DUN9A25%2Fx3eIUFiYGIpHIpMpWTKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydyLHOBCIdc8FYhnYq3APu9VpQguZ5236SpW3PlDZs6EqyouMC3QYP7gsBlgUa209vooexKR0nkyz3Po0kL05Pzyqi15plRRwC%2BNp4MCvb84winmnM17mWvoFpHXD23aebTm9hFwpk%2BZWbBF6R%2FUmzl%2BOTgVb0WtXGvYQga9aQ47qhiIM%2FQNYeOftnf%2BJrjVkjGaqY2VS1su%2BwccRETCv%2Foc80ifcYznbbkUEBQ206%2F59VO%2Ftvf13DlkmucFh9DTbG7CRj%2BbroGP1MhWMLzx7EDyXPvzkBWTeegAWuSn2tmzdknJ2UL4XjpEdl7fz2yJB87is0iJZ6PohOJRneBKqjf6A68q1S6M8nN2ZZPltud174xY5I1rYiKxsh09QIc7ZD9B4yy55TJxX1T2XVCIAi9rv5gX%2BlWZXI2kEBrrpHJ98Aesnj1Pucd2L9tewfrw%2Fg%2BnBVRjOBwuBjTUBI%2FLSu0uFxapNXRvqrYdeToEv8t1p60pNhILvttbPiqq0trDJLCk9lzLMQnUZKBubKDS82Fb9xefkVXA59CXPrvP1EHah6MEB4eOJMZuPZKz0EG5uXqJloOSJ7JHovYZHPdzpLVVEabrkNywnKzGM%2BeDWCkcwLKLRrzxCSyNghNOJjxkP5l3C2OHH3UWYwZzDvn8fOBjqkAf0x28%2BJ8GQjGVM%2FY0bW53FfKmG7owRsfZCQtodFQkSuq6pGrClcWcUWkl%2FpLVBStU9T7Xn3vSutft8s3wQwVpU9k9mbzlSzWRq0WKL%2BwefmppDHusNOHT1wpoKUL8sENPydEntrXHHfXRmazK3vh0KLKml7Yu5bpnMlxlv46Ju3GQqq4ycR%2FvuUxEnTAp%2BhHDuggWrwDzAu8E%2B7ior%2F0Q4MsiMN&X-Amz-Signature=f98fbfb3a1268808141fba9c4bfe1b1eeb73488a33566e78970291a546326df2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZABAODUR%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0Dzc2omxe6WAu%2FJtN8%2BLo9ygcaflcJunVhGTp810iwIhAMmSmL5qoTx3RyC0s1DUN9A25%2Fx3eIUFiYGIpHIpMpWTKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydyLHOBCIdc8FYhnYq3APu9VpQguZ5236SpW3PlDZs6EqyouMC3QYP7gsBlgUa209vooexKR0nkyz3Po0kL05Pzyqi15plRRwC%2BNp4MCvb84winmnM17mWvoFpHXD23aebTm9hFwpk%2BZWbBF6R%2FUmzl%2BOTgVb0WtXGvYQga9aQ47qhiIM%2FQNYeOftnf%2BJrjVkjGaqY2VS1su%2BwccRETCv%2Foc80ifcYznbbkUEBQ206%2F59VO%2Ftvf13DlkmucFh9DTbG7CRj%2BbroGP1MhWMLzx7EDyXPvzkBWTeegAWuSn2tmzdknJ2UL4XjpEdl7fz2yJB87is0iJZ6PohOJRneBKqjf6A68q1S6M8nN2ZZPltud174xY5I1rYiKxsh09QIc7ZD9B4yy55TJxX1T2XVCIAi9rv5gX%2BlWZXI2kEBrrpHJ98Aesnj1Pucd2L9tewfrw%2Fg%2BnBVRjOBwuBjTUBI%2FLSu0uFxapNXRvqrYdeToEv8t1p60pNhILvttbPiqq0trDJLCk9lzLMQnUZKBubKDS82Fb9xefkVXA59CXPrvP1EHah6MEB4eOJMZuPZKz0EG5uXqJloOSJ7JHovYZHPdzpLVVEabrkNywnKzGM%2BeDWCkcwLKLRrzxCSyNghNOJjxkP5l3C2OHH3UWYwZzDvn8fOBjqkAf0x28%2BJ8GQjGVM%2FY0bW53FfKmG7owRsfZCQtodFQkSuq6pGrClcWcUWkl%2FpLVBStU9T7Xn3vSutft8s3wQwVpU9k9mbzlSzWRq0WKL%2BwefmppDHusNOHT1wpoKUL8sENPydEntrXHHfXRmazK3vh0KLKml7Yu5bpnMlxlv46Ju3GQqq4ycR%2FvuUxEnTAp%2BhHDuggWrwDzAu8E%2B7ior%2F0Q4MsiMN&X-Amz-Signature=6a1941eeaffb373b53f8a3352e567efca6bde731163c63647f21eab02cd51814&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZABAODUR%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0Dzc2omxe6WAu%2FJtN8%2BLo9ygcaflcJunVhGTp810iwIhAMmSmL5qoTx3RyC0s1DUN9A25%2Fx3eIUFiYGIpHIpMpWTKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydyLHOBCIdc8FYhnYq3APu9VpQguZ5236SpW3PlDZs6EqyouMC3QYP7gsBlgUa209vooexKR0nkyz3Po0kL05Pzyqi15plRRwC%2BNp4MCvb84winmnM17mWvoFpHXD23aebTm9hFwpk%2BZWbBF6R%2FUmzl%2BOTgVb0WtXGvYQga9aQ47qhiIM%2FQNYeOftnf%2BJrjVkjGaqY2VS1su%2BwccRETCv%2Foc80ifcYznbbkUEBQ206%2F59VO%2Ftvf13DlkmucFh9DTbG7CRj%2BbroGP1MhWMLzx7EDyXPvzkBWTeegAWuSn2tmzdknJ2UL4XjpEdl7fz2yJB87is0iJZ6PohOJRneBKqjf6A68q1S6M8nN2ZZPltud174xY5I1rYiKxsh09QIc7ZD9B4yy55TJxX1T2XVCIAi9rv5gX%2BlWZXI2kEBrrpHJ98Aesnj1Pucd2L9tewfrw%2Fg%2BnBVRjOBwuBjTUBI%2FLSu0uFxapNXRvqrYdeToEv8t1p60pNhILvttbPiqq0trDJLCk9lzLMQnUZKBubKDS82Fb9xefkVXA59CXPrvP1EHah6MEB4eOJMZuPZKz0EG5uXqJloOSJ7JHovYZHPdzpLVVEabrkNywnKzGM%2BeDWCkcwLKLRrzxCSyNghNOJjxkP5l3C2OHH3UWYwZzDvn8fOBjqkAf0x28%2BJ8GQjGVM%2FY0bW53FfKmG7owRsfZCQtodFQkSuq6pGrClcWcUWkl%2FpLVBStU9T7Xn3vSutft8s3wQwVpU9k9mbzlSzWRq0WKL%2BwefmppDHusNOHT1wpoKUL8sENPydEntrXHHfXRmazK3vh0KLKml7Yu5bpnMlxlv46Ju3GQqq4ycR%2FvuUxEnTAp%2BhHDuggWrwDzAu8E%2B7ior%2F0Q4MsiMN&X-Amz-Signature=62b0e71e9403cae8292dd69a820c152c365ead882e1f8d7c5a9f8bfcbfb00192&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

