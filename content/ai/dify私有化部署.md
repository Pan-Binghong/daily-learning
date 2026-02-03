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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GG4WQM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIGxFXFYrfJB50by3jdi0sbB0f2WqUxTmwW1FK4ui6Bn4AiAQeL9WW%2FlZjwLGJQfFZCoUmj50sr5bVxuAIHkk9ii5WCqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf7EDfrr6TJM9njanKtwDv730SSD5KB0O9fUXuIWnrWlTwmMw%2Besug%2BkuTORDpQ%2FVBqieVoGXk2G%2FFo1pyb6IWZRugyVh%2Bqdw%2BLXPYfArER1h7U4h%2FUTp1s1l8TkQKCc9iuZxw4EQ0AFF%2Bp7lqLCpIEWmL%2Fk%2Fr%2BGRpX48RFMGyoNGTemz6Rob4c%2Bo7ib29%2Fqo0TJWf9%2FGmKxfDqy%2FD6rzjb30lN%2FAKG9mw9JqEMcs0X0X9a%2BLQKipVAHoj%2FprFNEYZwINxu96ZGoPYQpVgqxyMr1nLd%2Fx55jPih9uMb8bQ6dlvp%2FELWOSgOZWayyEB3333fXEXbXHvaVuv8CZcUOtfkpIEolkiBDuJmNBu7PjxyRGcUhse1YR3wj1H8q%2FdIyxO8UYd0SIJCks%2B3HLwnU2fUbixQkA0oGy0ugVw0wV%2BPpONJQiOI0nAgpumOx%2BhFLTibKU4yCxpL%2BWOzPVt8HUow04h1PnFikiDrpne4pX3gfaWxoMH2UBTWK2XdIni8UIv2vWGa47DcD%2Bs2vWmsTNYB2V4%2Bi4pLlaNkfWD0zei6a9Mlqyh8K%2Bqi1lxXMhWu%2B3sR8KHQZHJGwH8EbJ%2F6XiaBq%2F8OFPCXS7scF8UCyidYDc5UNDHhWF44mlMgVkgFiLHxxIC0529jHpWHMw5deFzAY6pgEHHpw%2F2%2BEvuxxY%2FeKwtgxA%2BR%2Bw%2Fyd%2FK7qePHPRMtDmCRIVNFkrNoSnN2E7IGlQQRVvnfyp53NELDUNklDLgV5jcUguMQRRPOO7BIX0yQvbFP8jsxG4tluLVUu4G2LldxCoWnAOqWmaHc4CRL5ip%2BzbcdNZtBSPktHLWoXo3ZYS%2BYHp7iQXFtnY%2FCdw8Zpzbwy7D%2FrUIiJxSBMzNvo2hWkgAcA14PUZ&X-Amz-Signature=f3d55cfe5d9fb6fc9f5c622be2335ecd4ba80f316613d26f6ba231c86c302f5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GG4WQM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIGxFXFYrfJB50by3jdi0sbB0f2WqUxTmwW1FK4ui6Bn4AiAQeL9WW%2FlZjwLGJQfFZCoUmj50sr5bVxuAIHkk9ii5WCqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf7EDfrr6TJM9njanKtwDv730SSD5KB0O9fUXuIWnrWlTwmMw%2Besug%2BkuTORDpQ%2FVBqieVoGXk2G%2FFo1pyb6IWZRugyVh%2Bqdw%2BLXPYfArER1h7U4h%2FUTp1s1l8TkQKCc9iuZxw4EQ0AFF%2Bp7lqLCpIEWmL%2Fk%2Fr%2BGRpX48RFMGyoNGTemz6Rob4c%2Bo7ib29%2Fqo0TJWf9%2FGmKxfDqy%2FD6rzjb30lN%2FAKG9mw9JqEMcs0X0X9a%2BLQKipVAHoj%2FprFNEYZwINxu96ZGoPYQpVgqxyMr1nLd%2Fx55jPih9uMb8bQ6dlvp%2FELWOSgOZWayyEB3333fXEXbXHvaVuv8CZcUOtfkpIEolkiBDuJmNBu7PjxyRGcUhse1YR3wj1H8q%2FdIyxO8UYd0SIJCks%2B3HLwnU2fUbixQkA0oGy0ugVw0wV%2BPpONJQiOI0nAgpumOx%2BhFLTibKU4yCxpL%2BWOzPVt8HUow04h1PnFikiDrpne4pX3gfaWxoMH2UBTWK2XdIni8UIv2vWGa47DcD%2Bs2vWmsTNYB2V4%2Bi4pLlaNkfWD0zei6a9Mlqyh8K%2Bqi1lxXMhWu%2B3sR8KHQZHJGwH8EbJ%2F6XiaBq%2F8OFPCXS7scF8UCyidYDc5UNDHhWF44mlMgVkgFiLHxxIC0529jHpWHMw5deFzAY6pgEHHpw%2F2%2BEvuxxY%2FeKwtgxA%2BR%2Bw%2Fyd%2FK7qePHPRMtDmCRIVNFkrNoSnN2E7IGlQQRVvnfyp53NELDUNklDLgV5jcUguMQRRPOO7BIX0yQvbFP8jsxG4tluLVUu4G2LldxCoWnAOqWmaHc4CRL5ip%2BzbcdNZtBSPktHLWoXo3ZYS%2BYHp7iQXFtnY%2FCdw8Zpzbwy7D%2FrUIiJxSBMzNvo2hWkgAcA14PUZ&X-Amz-Signature=0ddd490abb163702b9dd41d6963a60856c9644ba96c8c55c7f3b6bda9f069434&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GG4WQM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIGxFXFYrfJB50by3jdi0sbB0f2WqUxTmwW1FK4ui6Bn4AiAQeL9WW%2FlZjwLGJQfFZCoUmj50sr5bVxuAIHkk9ii5WCqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf7EDfrr6TJM9njanKtwDv730SSD5KB0O9fUXuIWnrWlTwmMw%2Besug%2BkuTORDpQ%2FVBqieVoGXk2G%2FFo1pyb6IWZRugyVh%2Bqdw%2BLXPYfArER1h7U4h%2FUTp1s1l8TkQKCc9iuZxw4EQ0AFF%2Bp7lqLCpIEWmL%2Fk%2Fr%2BGRpX48RFMGyoNGTemz6Rob4c%2Bo7ib29%2Fqo0TJWf9%2FGmKxfDqy%2FD6rzjb30lN%2FAKG9mw9JqEMcs0X0X9a%2BLQKipVAHoj%2FprFNEYZwINxu96ZGoPYQpVgqxyMr1nLd%2Fx55jPih9uMb8bQ6dlvp%2FELWOSgOZWayyEB3333fXEXbXHvaVuv8CZcUOtfkpIEolkiBDuJmNBu7PjxyRGcUhse1YR3wj1H8q%2FdIyxO8UYd0SIJCks%2B3HLwnU2fUbixQkA0oGy0ugVw0wV%2BPpONJQiOI0nAgpumOx%2BhFLTibKU4yCxpL%2BWOzPVt8HUow04h1PnFikiDrpne4pX3gfaWxoMH2UBTWK2XdIni8UIv2vWGa47DcD%2Bs2vWmsTNYB2V4%2Bi4pLlaNkfWD0zei6a9Mlqyh8K%2Bqi1lxXMhWu%2B3sR8KHQZHJGwH8EbJ%2F6XiaBq%2F8OFPCXS7scF8UCyidYDc5UNDHhWF44mlMgVkgFiLHxxIC0529jHpWHMw5deFzAY6pgEHHpw%2F2%2BEvuxxY%2FeKwtgxA%2BR%2Bw%2Fyd%2FK7qePHPRMtDmCRIVNFkrNoSnN2E7IGlQQRVvnfyp53NELDUNklDLgV5jcUguMQRRPOO7BIX0yQvbFP8jsxG4tluLVUu4G2LldxCoWnAOqWmaHc4CRL5ip%2BzbcdNZtBSPktHLWoXo3ZYS%2BYHp7iQXFtnY%2FCdw8Zpzbwy7D%2FrUIiJxSBMzNvo2hWkgAcA14PUZ&X-Amz-Signature=807ef97da7a6814ff5a59042f850fd07836172b7634259cdb2c0844e20ace306&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GG4WQM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIGxFXFYrfJB50by3jdi0sbB0f2WqUxTmwW1FK4ui6Bn4AiAQeL9WW%2FlZjwLGJQfFZCoUmj50sr5bVxuAIHkk9ii5WCqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf7EDfrr6TJM9njanKtwDv730SSD5KB0O9fUXuIWnrWlTwmMw%2Besug%2BkuTORDpQ%2FVBqieVoGXk2G%2FFo1pyb6IWZRugyVh%2Bqdw%2BLXPYfArER1h7U4h%2FUTp1s1l8TkQKCc9iuZxw4EQ0AFF%2Bp7lqLCpIEWmL%2Fk%2Fr%2BGRpX48RFMGyoNGTemz6Rob4c%2Bo7ib29%2Fqo0TJWf9%2FGmKxfDqy%2FD6rzjb30lN%2FAKG9mw9JqEMcs0X0X9a%2BLQKipVAHoj%2FprFNEYZwINxu96ZGoPYQpVgqxyMr1nLd%2Fx55jPih9uMb8bQ6dlvp%2FELWOSgOZWayyEB3333fXEXbXHvaVuv8CZcUOtfkpIEolkiBDuJmNBu7PjxyRGcUhse1YR3wj1H8q%2FdIyxO8UYd0SIJCks%2B3HLwnU2fUbixQkA0oGy0ugVw0wV%2BPpONJQiOI0nAgpumOx%2BhFLTibKU4yCxpL%2BWOzPVt8HUow04h1PnFikiDrpne4pX3gfaWxoMH2UBTWK2XdIni8UIv2vWGa47DcD%2Bs2vWmsTNYB2V4%2Bi4pLlaNkfWD0zei6a9Mlqyh8K%2Bqi1lxXMhWu%2B3sR8KHQZHJGwH8EbJ%2F6XiaBq%2F8OFPCXS7scF8UCyidYDc5UNDHhWF44mlMgVkgFiLHxxIC0529jHpWHMw5deFzAY6pgEHHpw%2F2%2BEvuxxY%2FeKwtgxA%2BR%2Bw%2Fyd%2FK7qePHPRMtDmCRIVNFkrNoSnN2E7IGlQQRVvnfyp53NELDUNklDLgV5jcUguMQRRPOO7BIX0yQvbFP8jsxG4tluLVUu4G2LldxCoWnAOqWmaHc4CRL5ip%2BzbcdNZtBSPktHLWoXo3ZYS%2BYHp7iQXFtnY%2FCdw8Zpzbwy7D%2FrUIiJxSBMzNvo2hWkgAcA14PUZ&X-Amz-Signature=728a608827e2435b133b04fdde9277327d0b5b2b8205921975ca78ea58aedcc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GG4WQM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIGxFXFYrfJB50by3jdi0sbB0f2WqUxTmwW1FK4ui6Bn4AiAQeL9WW%2FlZjwLGJQfFZCoUmj50sr5bVxuAIHkk9ii5WCqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf7EDfrr6TJM9njanKtwDv730SSD5KB0O9fUXuIWnrWlTwmMw%2Besug%2BkuTORDpQ%2FVBqieVoGXk2G%2FFo1pyb6IWZRugyVh%2Bqdw%2BLXPYfArER1h7U4h%2FUTp1s1l8TkQKCc9iuZxw4EQ0AFF%2Bp7lqLCpIEWmL%2Fk%2Fr%2BGRpX48RFMGyoNGTemz6Rob4c%2Bo7ib29%2Fqo0TJWf9%2FGmKxfDqy%2FD6rzjb30lN%2FAKG9mw9JqEMcs0X0X9a%2BLQKipVAHoj%2FprFNEYZwINxu96ZGoPYQpVgqxyMr1nLd%2Fx55jPih9uMb8bQ6dlvp%2FELWOSgOZWayyEB3333fXEXbXHvaVuv8CZcUOtfkpIEolkiBDuJmNBu7PjxyRGcUhse1YR3wj1H8q%2FdIyxO8UYd0SIJCks%2B3HLwnU2fUbixQkA0oGy0ugVw0wV%2BPpONJQiOI0nAgpumOx%2BhFLTibKU4yCxpL%2BWOzPVt8HUow04h1PnFikiDrpne4pX3gfaWxoMH2UBTWK2XdIni8UIv2vWGa47DcD%2Bs2vWmsTNYB2V4%2Bi4pLlaNkfWD0zei6a9Mlqyh8K%2Bqi1lxXMhWu%2B3sR8KHQZHJGwH8EbJ%2F6XiaBq%2F8OFPCXS7scF8UCyidYDc5UNDHhWF44mlMgVkgFiLHxxIC0529jHpWHMw5deFzAY6pgEHHpw%2F2%2BEvuxxY%2FeKwtgxA%2BR%2Bw%2Fyd%2FK7qePHPRMtDmCRIVNFkrNoSnN2E7IGlQQRVvnfyp53NELDUNklDLgV5jcUguMQRRPOO7BIX0yQvbFP8jsxG4tluLVUu4G2LldxCoWnAOqWmaHc4CRL5ip%2BzbcdNZtBSPktHLWoXo3ZYS%2BYHp7iQXFtnY%2FCdw8Zpzbwy7D%2FrUIiJxSBMzNvo2hWkgAcA14PUZ&X-Amz-Signature=483bfdfef136b6d76b085562e6e6caf423f440419023592125ac7081c0b1a400&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GG4WQM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIGxFXFYrfJB50by3jdi0sbB0f2WqUxTmwW1FK4ui6Bn4AiAQeL9WW%2FlZjwLGJQfFZCoUmj50sr5bVxuAIHkk9ii5WCqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf7EDfrr6TJM9njanKtwDv730SSD5KB0O9fUXuIWnrWlTwmMw%2Besug%2BkuTORDpQ%2FVBqieVoGXk2G%2FFo1pyb6IWZRugyVh%2Bqdw%2BLXPYfArER1h7U4h%2FUTp1s1l8TkQKCc9iuZxw4EQ0AFF%2Bp7lqLCpIEWmL%2Fk%2Fr%2BGRpX48RFMGyoNGTemz6Rob4c%2Bo7ib29%2Fqo0TJWf9%2FGmKxfDqy%2FD6rzjb30lN%2FAKG9mw9JqEMcs0X0X9a%2BLQKipVAHoj%2FprFNEYZwINxu96ZGoPYQpVgqxyMr1nLd%2Fx55jPih9uMb8bQ6dlvp%2FELWOSgOZWayyEB3333fXEXbXHvaVuv8CZcUOtfkpIEolkiBDuJmNBu7PjxyRGcUhse1YR3wj1H8q%2FdIyxO8UYd0SIJCks%2B3HLwnU2fUbixQkA0oGy0ugVw0wV%2BPpONJQiOI0nAgpumOx%2BhFLTibKU4yCxpL%2BWOzPVt8HUow04h1PnFikiDrpne4pX3gfaWxoMH2UBTWK2XdIni8UIv2vWGa47DcD%2Bs2vWmsTNYB2V4%2Bi4pLlaNkfWD0zei6a9Mlqyh8K%2Bqi1lxXMhWu%2B3sR8KHQZHJGwH8EbJ%2F6XiaBq%2F8OFPCXS7scF8UCyidYDc5UNDHhWF44mlMgVkgFiLHxxIC0529jHpWHMw5deFzAY6pgEHHpw%2F2%2BEvuxxY%2FeKwtgxA%2BR%2Bw%2Fyd%2FK7qePHPRMtDmCRIVNFkrNoSnN2E7IGlQQRVvnfyp53NELDUNklDLgV5jcUguMQRRPOO7BIX0yQvbFP8jsxG4tluLVUu4G2LldxCoWnAOqWmaHc4CRL5ip%2BzbcdNZtBSPktHLWoXo3ZYS%2BYHp7iQXFtnY%2FCdw8Zpzbwy7D%2FrUIiJxSBMzNvo2hWkgAcA14PUZ&X-Amz-Signature=cc90e6c4382006329e4b5ad19a4962f5ee0183dac59923cbdc8eed4f92628ef7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GG4WQM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIGxFXFYrfJB50by3jdi0sbB0f2WqUxTmwW1FK4ui6Bn4AiAQeL9WW%2FlZjwLGJQfFZCoUmj50sr5bVxuAIHkk9ii5WCqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf7EDfrr6TJM9njanKtwDv730SSD5KB0O9fUXuIWnrWlTwmMw%2Besug%2BkuTORDpQ%2FVBqieVoGXk2G%2FFo1pyb6IWZRugyVh%2Bqdw%2BLXPYfArER1h7U4h%2FUTp1s1l8TkQKCc9iuZxw4EQ0AFF%2Bp7lqLCpIEWmL%2Fk%2Fr%2BGRpX48RFMGyoNGTemz6Rob4c%2Bo7ib29%2Fqo0TJWf9%2FGmKxfDqy%2FD6rzjb30lN%2FAKG9mw9JqEMcs0X0X9a%2BLQKipVAHoj%2FprFNEYZwINxu96ZGoPYQpVgqxyMr1nLd%2Fx55jPih9uMb8bQ6dlvp%2FELWOSgOZWayyEB3333fXEXbXHvaVuv8CZcUOtfkpIEolkiBDuJmNBu7PjxyRGcUhse1YR3wj1H8q%2FdIyxO8UYd0SIJCks%2B3HLwnU2fUbixQkA0oGy0ugVw0wV%2BPpONJQiOI0nAgpumOx%2BhFLTibKU4yCxpL%2BWOzPVt8HUow04h1PnFikiDrpne4pX3gfaWxoMH2UBTWK2XdIni8UIv2vWGa47DcD%2Bs2vWmsTNYB2V4%2Bi4pLlaNkfWD0zei6a9Mlqyh8K%2Bqi1lxXMhWu%2B3sR8KHQZHJGwH8EbJ%2F6XiaBq%2F8OFPCXS7scF8UCyidYDc5UNDHhWF44mlMgVkgFiLHxxIC0529jHpWHMw5deFzAY6pgEHHpw%2F2%2BEvuxxY%2FeKwtgxA%2BR%2Bw%2Fyd%2FK7qePHPRMtDmCRIVNFkrNoSnN2E7IGlQQRVvnfyp53NELDUNklDLgV5jcUguMQRRPOO7BIX0yQvbFP8jsxG4tluLVUu4G2LldxCoWnAOqWmaHc4CRL5ip%2BzbcdNZtBSPktHLWoXo3ZYS%2BYHp7iQXFtnY%2FCdw8Zpzbwy7D%2FrUIiJxSBMzNvo2hWkgAcA14PUZ&X-Amz-Signature=239438b4dff79d1e07cc6d68c6d78419001fb55e3b4d8e5774e5ec6a118fe30f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GG4WQM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIGxFXFYrfJB50by3jdi0sbB0f2WqUxTmwW1FK4ui6Bn4AiAQeL9WW%2FlZjwLGJQfFZCoUmj50sr5bVxuAIHkk9ii5WCqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf7EDfrr6TJM9njanKtwDv730SSD5KB0O9fUXuIWnrWlTwmMw%2Besug%2BkuTORDpQ%2FVBqieVoGXk2G%2FFo1pyb6IWZRugyVh%2Bqdw%2BLXPYfArER1h7U4h%2FUTp1s1l8TkQKCc9iuZxw4EQ0AFF%2Bp7lqLCpIEWmL%2Fk%2Fr%2BGRpX48RFMGyoNGTemz6Rob4c%2Bo7ib29%2Fqo0TJWf9%2FGmKxfDqy%2FD6rzjb30lN%2FAKG9mw9JqEMcs0X0X9a%2BLQKipVAHoj%2FprFNEYZwINxu96ZGoPYQpVgqxyMr1nLd%2Fx55jPih9uMb8bQ6dlvp%2FELWOSgOZWayyEB3333fXEXbXHvaVuv8CZcUOtfkpIEolkiBDuJmNBu7PjxyRGcUhse1YR3wj1H8q%2FdIyxO8UYd0SIJCks%2B3HLwnU2fUbixQkA0oGy0ugVw0wV%2BPpONJQiOI0nAgpumOx%2BhFLTibKU4yCxpL%2BWOzPVt8HUow04h1PnFikiDrpne4pX3gfaWxoMH2UBTWK2XdIni8UIv2vWGa47DcD%2Bs2vWmsTNYB2V4%2Bi4pLlaNkfWD0zei6a9Mlqyh8K%2Bqi1lxXMhWu%2B3sR8KHQZHJGwH8EbJ%2F6XiaBq%2F8OFPCXS7scF8UCyidYDc5UNDHhWF44mlMgVkgFiLHxxIC0529jHpWHMw5deFzAY6pgEHHpw%2F2%2BEvuxxY%2FeKwtgxA%2BR%2Bw%2Fyd%2FK7qePHPRMtDmCRIVNFkrNoSnN2E7IGlQQRVvnfyp53NELDUNklDLgV5jcUguMQRRPOO7BIX0yQvbFP8jsxG4tluLVUu4G2LldxCoWnAOqWmaHc4CRL5ip%2BzbcdNZtBSPktHLWoXo3ZYS%2BYHp7iQXFtnY%2FCdw8Zpzbwy7D%2FrUIiJxSBMzNvo2hWkgAcA14PUZ&X-Amz-Signature=7a77480f4bb6cb5231d900d107b19563aaa3f580ea1bb2aca695017ea91774c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GG4WQM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIGxFXFYrfJB50by3jdi0sbB0f2WqUxTmwW1FK4ui6Bn4AiAQeL9WW%2FlZjwLGJQfFZCoUmj50sr5bVxuAIHkk9ii5WCqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf7EDfrr6TJM9njanKtwDv730SSD5KB0O9fUXuIWnrWlTwmMw%2Besug%2BkuTORDpQ%2FVBqieVoGXk2G%2FFo1pyb6IWZRugyVh%2Bqdw%2BLXPYfArER1h7U4h%2FUTp1s1l8TkQKCc9iuZxw4EQ0AFF%2Bp7lqLCpIEWmL%2Fk%2Fr%2BGRpX48RFMGyoNGTemz6Rob4c%2Bo7ib29%2Fqo0TJWf9%2FGmKxfDqy%2FD6rzjb30lN%2FAKG9mw9JqEMcs0X0X9a%2BLQKipVAHoj%2FprFNEYZwINxu96ZGoPYQpVgqxyMr1nLd%2Fx55jPih9uMb8bQ6dlvp%2FELWOSgOZWayyEB3333fXEXbXHvaVuv8CZcUOtfkpIEolkiBDuJmNBu7PjxyRGcUhse1YR3wj1H8q%2FdIyxO8UYd0SIJCks%2B3HLwnU2fUbixQkA0oGy0ugVw0wV%2BPpONJQiOI0nAgpumOx%2BhFLTibKU4yCxpL%2BWOzPVt8HUow04h1PnFikiDrpne4pX3gfaWxoMH2UBTWK2XdIni8UIv2vWGa47DcD%2Bs2vWmsTNYB2V4%2Bi4pLlaNkfWD0zei6a9Mlqyh8K%2Bqi1lxXMhWu%2B3sR8KHQZHJGwH8EbJ%2F6XiaBq%2F8OFPCXS7scF8UCyidYDc5UNDHhWF44mlMgVkgFiLHxxIC0529jHpWHMw5deFzAY6pgEHHpw%2F2%2BEvuxxY%2FeKwtgxA%2BR%2Bw%2Fyd%2FK7qePHPRMtDmCRIVNFkrNoSnN2E7IGlQQRVvnfyp53NELDUNklDLgV5jcUguMQRRPOO7BIX0yQvbFP8jsxG4tluLVUu4G2LldxCoWnAOqWmaHc4CRL5ip%2BzbcdNZtBSPktHLWoXo3ZYS%2BYHp7iQXFtnY%2FCdw8Zpzbwy7D%2FrUIiJxSBMzNvo2hWkgAcA14PUZ&X-Amz-Signature=a355c82a49c0f1a1ef96c92f47ca407dd262c48bb1eee76ddd434ce62d0c706e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644GG4WQM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIGxFXFYrfJB50by3jdi0sbB0f2WqUxTmwW1FK4ui6Bn4AiAQeL9WW%2FlZjwLGJQfFZCoUmj50sr5bVxuAIHkk9ii5WCqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf7EDfrr6TJM9njanKtwDv730SSD5KB0O9fUXuIWnrWlTwmMw%2Besug%2BkuTORDpQ%2FVBqieVoGXk2G%2FFo1pyb6IWZRugyVh%2Bqdw%2BLXPYfArER1h7U4h%2FUTp1s1l8TkQKCc9iuZxw4EQ0AFF%2Bp7lqLCpIEWmL%2Fk%2Fr%2BGRpX48RFMGyoNGTemz6Rob4c%2Bo7ib29%2Fqo0TJWf9%2FGmKxfDqy%2FD6rzjb30lN%2FAKG9mw9JqEMcs0X0X9a%2BLQKipVAHoj%2FprFNEYZwINxu96ZGoPYQpVgqxyMr1nLd%2Fx55jPih9uMb8bQ6dlvp%2FELWOSgOZWayyEB3333fXEXbXHvaVuv8CZcUOtfkpIEolkiBDuJmNBu7PjxyRGcUhse1YR3wj1H8q%2FdIyxO8UYd0SIJCks%2B3HLwnU2fUbixQkA0oGy0ugVw0wV%2BPpONJQiOI0nAgpumOx%2BhFLTibKU4yCxpL%2BWOzPVt8HUow04h1PnFikiDrpne4pX3gfaWxoMH2UBTWK2XdIni8UIv2vWGa47DcD%2Bs2vWmsTNYB2V4%2Bi4pLlaNkfWD0zei6a9Mlqyh8K%2Bqi1lxXMhWu%2B3sR8KHQZHJGwH8EbJ%2F6XiaBq%2F8OFPCXS7scF8UCyidYDc5UNDHhWF44mlMgVkgFiLHxxIC0529jHpWHMw5deFzAY6pgEHHpw%2F2%2BEvuxxY%2FeKwtgxA%2BR%2Bw%2Fyd%2FK7qePHPRMtDmCRIVNFkrNoSnN2E7IGlQQRVvnfyp53NELDUNklDLgV5jcUguMQRRPOO7BIX0yQvbFP8jsxG4tluLVUu4G2LldxCoWnAOqWmaHc4CRL5ip%2BzbcdNZtBSPktHLWoXo3ZYS%2BYHp7iQXFtnY%2FCdw8Zpzbwy7D%2FrUIiJxSBMzNvo2hWkgAcA14PUZ&X-Amz-Signature=77d2e463bc27a974f55dabd5d861ca0aac297a150779b35d769c6cd7e2cdc6bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

