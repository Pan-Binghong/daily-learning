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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4XTFXSZ%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUI09Z3kACqaEerl%2BUJziR%2FL0XQXs%2FsubIfI5pUIHGzAiBVRp3SvY4W1r7CnGhSshH%2Bkb3SUvRWapmNDI48ECfmDSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSTiPRNDdNGjVqa8dKtwDcU%2FrNIl1PL2KQQ8VryK%2B16tZ7j8uF30Kiirjboj878BOG1KzcOuV07Nl0lyPlJsK5tPhdXnGd2lGTZ6f1YhHO%2FR9%2FCQhR33VAGVGoK4UAb1lZg%2FFpwIZUOpS6fSTz2CaA79KXdmlOmSi75%2FQzh8UjLIJpsDTBRyUP%2BTmGLaeqtrPdShrMDJQbhwSZBmUYA7eCnOMQC4jv0uHytb66KAmrFvawWkJ7UMOqznv3drEqxP56%2FUpIAqJwe%2B6h17Qwj1tcygILNKdfU4QuNoIa0qFcdyTfFtcl7EEbXSBKw0cwNSk8t6alZEzsB%2FXqP7luidTtr3En9C4AxB2tAOcnGDGOeB4VIdZblCgDSrPjDgwvjZSC%2Bz4VxtNWxklvbRqLokzGdLI0Ur9JKLaEBjY%2F%2BYzgVBwI7OThZBfl3f5KHROx7pqSE0FhwbfpTchxQ24GDFfZGSHVsLz70%2BCD3ZG5NbB0mt5lg2lM3wMHgOfOaPTEoHd2ak8YiCnYLzNaBwVEFOGoE0%2Bqm3bdlSKTSszw1hFlf1O9ob%2FWU36Z5Hop%2FCGL0oJrpO8F385d33w0pLIWPHqsw7p7hLDS2rfOzzQPPrnN%2FVA%2F0SINs1dnrDUBrnAwbmRmwAKuENTLA%2FLOYcwzbfNzQY6pgHXk4JRygrZuLbnb%2BoD3xNGyWOXQW50GR2zJEldPdyfkMwDPOD2Vg06TjGZZDzWlSXWYLhNX8dVs4EmS6ZfCH7GY3ye%2BrZk7nX6TNZWC8I0t2N9FjvRiRc6F%2B60e1YbgLhTA2LAsyaN%2BAu1HFInh7IJWv%2BrjcF1GRPUr3Hz85INcQvoceniEQOCtfV2Lc2XSisqVaDyDf3NkiTzkXd8zGioZFyjqP2W&X-Amz-Signature=0d5d2cc32313131c68e1976f69dbfdd1072cdf4120d5b8536138ae66eba00bd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4XTFXSZ%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUI09Z3kACqaEerl%2BUJziR%2FL0XQXs%2FsubIfI5pUIHGzAiBVRp3SvY4W1r7CnGhSshH%2Bkb3SUvRWapmNDI48ECfmDSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSTiPRNDdNGjVqa8dKtwDcU%2FrNIl1PL2KQQ8VryK%2B16tZ7j8uF30Kiirjboj878BOG1KzcOuV07Nl0lyPlJsK5tPhdXnGd2lGTZ6f1YhHO%2FR9%2FCQhR33VAGVGoK4UAb1lZg%2FFpwIZUOpS6fSTz2CaA79KXdmlOmSi75%2FQzh8UjLIJpsDTBRyUP%2BTmGLaeqtrPdShrMDJQbhwSZBmUYA7eCnOMQC4jv0uHytb66KAmrFvawWkJ7UMOqznv3drEqxP56%2FUpIAqJwe%2B6h17Qwj1tcygILNKdfU4QuNoIa0qFcdyTfFtcl7EEbXSBKw0cwNSk8t6alZEzsB%2FXqP7luidTtr3En9C4AxB2tAOcnGDGOeB4VIdZblCgDSrPjDgwvjZSC%2Bz4VxtNWxklvbRqLokzGdLI0Ur9JKLaEBjY%2F%2BYzgVBwI7OThZBfl3f5KHROx7pqSE0FhwbfpTchxQ24GDFfZGSHVsLz70%2BCD3ZG5NbB0mt5lg2lM3wMHgOfOaPTEoHd2ak8YiCnYLzNaBwVEFOGoE0%2Bqm3bdlSKTSszw1hFlf1O9ob%2FWU36Z5Hop%2FCGL0oJrpO8F385d33w0pLIWPHqsw7p7hLDS2rfOzzQPPrnN%2FVA%2F0SINs1dnrDUBrnAwbmRmwAKuENTLA%2FLOYcwzbfNzQY6pgHXk4JRygrZuLbnb%2BoD3xNGyWOXQW50GR2zJEldPdyfkMwDPOD2Vg06TjGZZDzWlSXWYLhNX8dVs4EmS6ZfCH7GY3ye%2BrZk7nX6TNZWC8I0t2N9FjvRiRc6F%2B60e1YbgLhTA2LAsyaN%2BAu1HFInh7IJWv%2BrjcF1GRPUr3Hz85INcQvoceniEQOCtfV2Lc2XSisqVaDyDf3NkiTzkXd8zGioZFyjqP2W&X-Amz-Signature=813e9bf4d628f8ab55a1201873e3b3250b298e0f8eb5209af5db004482cd587c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4XTFXSZ%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUI09Z3kACqaEerl%2BUJziR%2FL0XQXs%2FsubIfI5pUIHGzAiBVRp3SvY4W1r7CnGhSshH%2Bkb3SUvRWapmNDI48ECfmDSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSTiPRNDdNGjVqa8dKtwDcU%2FrNIl1PL2KQQ8VryK%2B16tZ7j8uF30Kiirjboj878BOG1KzcOuV07Nl0lyPlJsK5tPhdXnGd2lGTZ6f1YhHO%2FR9%2FCQhR33VAGVGoK4UAb1lZg%2FFpwIZUOpS6fSTz2CaA79KXdmlOmSi75%2FQzh8UjLIJpsDTBRyUP%2BTmGLaeqtrPdShrMDJQbhwSZBmUYA7eCnOMQC4jv0uHytb66KAmrFvawWkJ7UMOqznv3drEqxP56%2FUpIAqJwe%2B6h17Qwj1tcygILNKdfU4QuNoIa0qFcdyTfFtcl7EEbXSBKw0cwNSk8t6alZEzsB%2FXqP7luidTtr3En9C4AxB2tAOcnGDGOeB4VIdZblCgDSrPjDgwvjZSC%2Bz4VxtNWxklvbRqLokzGdLI0Ur9JKLaEBjY%2F%2BYzgVBwI7OThZBfl3f5KHROx7pqSE0FhwbfpTchxQ24GDFfZGSHVsLz70%2BCD3ZG5NbB0mt5lg2lM3wMHgOfOaPTEoHd2ak8YiCnYLzNaBwVEFOGoE0%2Bqm3bdlSKTSszw1hFlf1O9ob%2FWU36Z5Hop%2FCGL0oJrpO8F385d33w0pLIWPHqsw7p7hLDS2rfOzzQPPrnN%2FVA%2F0SINs1dnrDUBrnAwbmRmwAKuENTLA%2FLOYcwzbfNzQY6pgHXk4JRygrZuLbnb%2BoD3xNGyWOXQW50GR2zJEldPdyfkMwDPOD2Vg06TjGZZDzWlSXWYLhNX8dVs4EmS6ZfCH7GY3ye%2BrZk7nX6TNZWC8I0t2N9FjvRiRc6F%2B60e1YbgLhTA2LAsyaN%2BAu1HFInh7IJWv%2BrjcF1GRPUr3Hz85INcQvoceniEQOCtfV2Lc2XSisqVaDyDf3NkiTzkXd8zGioZFyjqP2W&X-Amz-Signature=86149b75c448b849bde274ddc75df7212bba38594cb88806029adfdc14294b60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4XTFXSZ%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUI09Z3kACqaEerl%2BUJziR%2FL0XQXs%2FsubIfI5pUIHGzAiBVRp3SvY4W1r7CnGhSshH%2Bkb3SUvRWapmNDI48ECfmDSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSTiPRNDdNGjVqa8dKtwDcU%2FrNIl1PL2KQQ8VryK%2B16tZ7j8uF30Kiirjboj878BOG1KzcOuV07Nl0lyPlJsK5tPhdXnGd2lGTZ6f1YhHO%2FR9%2FCQhR33VAGVGoK4UAb1lZg%2FFpwIZUOpS6fSTz2CaA79KXdmlOmSi75%2FQzh8UjLIJpsDTBRyUP%2BTmGLaeqtrPdShrMDJQbhwSZBmUYA7eCnOMQC4jv0uHytb66KAmrFvawWkJ7UMOqznv3drEqxP56%2FUpIAqJwe%2B6h17Qwj1tcygILNKdfU4QuNoIa0qFcdyTfFtcl7EEbXSBKw0cwNSk8t6alZEzsB%2FXqP7luidTtr3En9C4AxB2tAOcnGDGOeB4VIdZblCgDSrPjDgwvjZSC%2Bz4VxtNWxklvbRqLokzGdLI0Ur9JKLaEBjY%2F%2BYzgVBwI7OThZBfl3f5KHROx7pqSE0FhwbfpTchxQ24GDFfZGSHVsLz70%2BCD3ZG5NbB0mt5lg2lM3wMHgOfOaPTEoHd2ak8YiCnYLzNaBwVEFOGoE0%2Bqm3bdlSKTSszw1hFlf1O9ob%2FWU36Z5Hop%2FCGL0oJrpO8F385d33w0pLIWPHqsw7p7hLDS2rfOzzQPPrnN%2FVA%2F0SINs1dnrDUBrnAwbmRmwAKuENTLA%2FLOYcwzbfNzQY6pgHXk4JRygrZuLbnb%2BoD3xNGyWOXQW50GR2zJEldPdyfkMwDPOD2Vg06TjGZZDzWlSXWYLhNX8dVs4EmS6ZfCH7GY3ye%2BrZk7nX6TNZWC8I0t2N9FjvRiRc6F%2B60e1YbgLhTA2LAsyaN%2BAu1HFInh7IJWv%2BrjcF1GRPUr3Hz85INcQvoceniEQOCtfV2Lc2XSisqVaDyDf3NkiTzkXd8zGioZFyjqP2W&X-Amz-Signature=8139ff51264077a4533e8b2869547760df45750f0a654d63143252cba4ccd6d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4XTFXSZ%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUI09Z3kACqaEerl%2BUJziR%2FL0XQXs%2FsubIfI5pUIHGzAiBVRp3SvY4W1r7CnGhSshH%2Bkb3SUvRWapmNDI48ECfmDSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSTiPRNDdNGjVqa8dKtwDcU%2FrNIl1PL2KQQ8VryK%2B16tZ7j8uF30Kiirjboj878BOG1KzcOuV07Nl0lyPlJsK5tPhdXnGd2lGTZ6f1YhHO%2FR9%2FCQhR33VAGVGoK4UAb1lZg%2FFpwIZUOpS6fSTz2CaA79KXdmlOmSi75%2FQzh8UjLIJpsDTBRyUP%2BTmGLaeqtrPdShrMDJQbhwSZBmUYA7eCnOMQC4jv0uHytb66KAmrFvawWkJ7UMOqznv3drEqxP56%2FUpIAqJwe%2B6h17Qwj1tcygILNKdfU4QuNoIa0qFcdyTfFtcl7EEbXSBKw0cwNSk8t6alZEzsB%2FXqP7luidTtr3En9C4AxB2tAOcnGDGOeB4VIdZblCgDSrPjDgwvjZSC%2Bz4VxtNWxklvbRqLokzGdLI0Ur9JKLaEBjY%2F%2BYzgVBwI7OThZBfl3f5KHROx7pqSE0FhwbfpTchxQ24GDFfZGSHVsLz70%2BCD3ZG5NbB0mt5lg2lM3wMHgOfOaPTEoHd2ak8YiCnYLzNaBwVEFOGoE0%2Bqm3bdlSKTSszw1hFlf1O9ob%2FWU36Z5Hop%2FCGL0oJrpO8F385d33w0pLIWPHqsw7p7hLDS2rfOzzQPPrnN%2FVA%2F0SINs1dnrDUBrnAwbmRmwAKuENTLA%2FLOYcwzbfNzQY6pgHXk4JRygrZuLbnb%2BoD3xNGyWOXQW50GR2zJEldPdyfkMwDPOD2Vg06TjGZZDzWlSXWYLhNX8dVs4EmS6ZfCH7GY3ye%2BrZk7nX6TNZWC8I0t2N9FjvRiRc6F%2B60e1YbgLhTA2LAsyaN%2BAu1HFInh7IJWv%2BrjcF1GRPUr3Hz85INcQvoceniEQOCtfV2Lc2XSisqVaDyDf3NkiTzkXd8zGioZFyjqP2W&X-Amz-Signature=abea6845cc57f40052a426ef217c8b6b0bcd636832a3c1a939739d076bebe342&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4XTFXSZ%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUI09Z3kACqaEerl%2BUJziR%2FL0XQXs%2FsubIfI5pUIHGzAiBVRp3SvY4W1r7CnGhSshH%2Bkb3SUvRWapmNDI48ECfmDSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSTiPRNDdNGjVqa8dKtwDcU%2FrNIl1PL2KQQ8VryK%2B16tZ7j8uF30Kiirjboj878BOG1KzcOuV07Nl0lyPlJsK5tPhdXnGd2lGTZ6f1YhHO%2FR9%2FCQhR33VAGVGoK4UAb1lZg%2FFpwIZUOpS6fSTz2CaA79KXdmlOmSi75%2FQzh8UjLIJpsDTBRyUP%2BTmGLaeqtrPdShrMDJQbhwSZBmUYA7eCnOMQC4jv0uHytb66KAmrFvawWkJ7UMOqznv3drEqxP56%2FUpIAqJwe%2B6h17Qwj1tcygILNKdfU4QuNoIa0qFcdyTfFtcl7EEbXSBKw0cwNSk8t6alZEzsB%2FXqP7luidTtr3En9C4AxB2tAOcnGDGOeB4VIdZblCgDSrPjDgwvjZSC%2Bz4VxtNWxklvbRqLokzGdLI0Ur9JKLaEBjY%2F%2BYzgVBwI7OThZBfl3f5KHROx7pqSE0FhwbfpTchxQ24GDFfZGSHVsLz70%2BCD3ZG5NbB0mt5lg2lM3wMHgOfOaPTEoHd2ak8YiCnYLzNaBwVEFOGoE0%2Bqm3bdlSKTSszw1hFlf1O9ob%2FWU36Z5Hop%2FCGL0oJrpO8F385d33w0pLIWPHqsw7p7hLDS2rfOzzQPPrnN%2FVA%2F0SINs1dnrDUBrnAwbmRmwAKuENTLA%2FLOYcwzbfNzQY6pgHXk4JRygrZuLbnb%2BoD3xNGyWOXQW50GR2zJEldPdyfkMwDPOD2Vg06TjGZZDzWlSXWYLhNX8dVs4EmS6ZfCH7GY3ye%2BrZk7nX6TNZWC8I0t2N9FjvRiRc6F%2B60e1YbgLhTA2LAsyaN%2BAu1HFInh7IJWv%2BrjcF1GRPUr3Hz85INcQvoceniEQOCtfV2Lc2XSisqVaDyDf3NkiTzkXd8zGioZFyjqP2W&X-Amz-Signature=4a4eadd01d60c7e9132371bb52d8e29b849fde5397d5118e79a3c9407016f22d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4XTFXSZ%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUI09Z3kACqaEerl%2BUJziR%2FL0XQXs%2FsubIfI5pUIHGzAiBVRp3SvY4W1r7CnGhSshH%2Bkb3SUvRWapmNDI48ECfmDSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSTiPRNDdNGjVqa8dKtwDcU%2FrNIl1PL2KQQ8VryK%2B16tZ7j8uF30Kiirjboj878BOG1KzcOuV07Nl0lyPlJsK5tPhdXnGd2lGTZ6f1YhHO%2FR9%2FCQhR33VAGVGoK4UAb1lZg%2FFpwIZUOpS6fSTz2CaA79KXdmlOmSi75%2FQzh8UjLIJpsDTBRyUP%2BTmGLaeqtrPdShrMDJQbhwSZBmUYA7eCnOMQC4jv0uHytb66KAmrFvawWkJ7UMOqznv3drEqxP56%2FUpIAqJwe%2B6h17Qwj1tcygILNKdfU4QuNoIa0qFcdyTfFtcl7EEbXSBKw0cwNSk8t6alZEzsB%2FXqP7luidTtr3En9C4AxB2tAOcnGDGOeB4VIdZblCgDSrPjDgwvjZSC%2Bz4VxtNWxklvbRqLokzGdLI0Ur9JKLaEBjY%2F%2BYzgVBwI7OThZBfl3f5KHROx7pqSE0FhwbfpTchxQ24GDFfZGSHVsLz70%2BCD3ZG5NbB0mt5lg2lM3wMHgOfOaPTEoHd2ak8YiCnYLzNaBwVEFOGoE0%2Bqm3bdlSKTSszw1hFlf1O9ob%2FWU36Z5Hop%2FCGL0oJrpO8F385d33w0pLIWPHqsw7p7hLDS2rfOzzQPPrnN%2FVA%2F0SINs1dnrDUBrnAwbmRmwAKuENTLA%2FLOYcwzbfNzQY6pgHXk4JRygrZuLbnb%2BoD3xNGyWOXQW50GR2zJEldPdyfkMwDPOD2Vg06TjGZZDzWlSXWYLhNX8dVs4EmS6ZfCH7GY3ye%2BrZk7nX6TNZWC8I0t2N9FjvRiRc6F%2B60e1YbgLhTA2LAsyaN%2BAu1HFInh7IJWv%2BrjcF1GRPUr3Hz85INcQvoceniEQOCtfV2Lc2XSisqVaDyDf3NkiTzkXd8zGioZFyjqP2W&X-Amz-Signature=25544ce02016129fba875dd4a83e192efee973f8db293b60e5e98b5b792d63b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4XTFXSZ%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUI09Z3kACqaEerl%2BUJziR%2FL0XQXs%2FsubIfI5pUIHGzAiBVRp3SvY4W1r7CnGhSshH%2Bkb3SUvRWapmNDI48ECfmDSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSTiPRNDdNGjVqa8dKtwDcU%2FrNIl1PL2KQQ8VryK%2B16tZ7j8uF30Kiirjboj878BOG1KzcOuV07Nl0lyPlJsK5tPhdXnGd2lGTZ6f1YhHO%2FR9%2FCQhR33VAGVGoK4UAb1lZg%2FFpwIZUOpS6fSTz2CaA79KXdmlOmSi75%2FQzh8UjLIJpsDTBRyUP%2BTmGLaeqtrPdShrMDJQbhwSZBmUYA7eCnOMQC4jv0uHytb66KAmrFvawWkJ7UMOqznv3drEqxP56%2FUpIAqJwe%2B6h17Qwj1tcygILNKdfU4QuNoIa0qFcdyTfFtcl7EEbXSBKw0cwNSk8t6alZEzsB%2FXqP7luidTtr3En9C4AxB2tAOcnGDGOeB4VIdZblCgDSrPjDgwvjZSC%2Bz4VxtNWxklvbRqLokzGdLI0Ur9JKLaEBjY%2F%2BYzgVBwI7OThZBfl3f5KHROx7pqSE0FhwbfpTchxQ24GDFfZGSHVsLz70%2BCD3ZG5NbB0mt5lg2lM3wMHgOfOaPTEoHd2ak8YiCnYLzNaBwVEFOGoE0%2Bqm3bdlSKTSszw1hFlf1O9ob%2FWU36Z5Hop%2FCGL0oJrpO8F385d33w0pLIWPHqsw7p7hLDS2rfOzzQPPrnN%2FVA%2F0SINs1dnrDUBrnAwbmRmwAKuENTLA%2FLOYcwzbfNzQY6pgHXk4JRygrZuLbnb%2BoD3xNGyWOXQW50GR2zJEldPdyfkMwDPOD2Vg06TjGZZDzWlSXWYLhNX8dVs4EmS6ZfCH7GY3ye%2BrZk7nX6TNZWC8I0t2N9FjvRiRc6F%2B60e1YbgLhTA2LAsyaN%2BAu1HFInh7IJWv%2BrjcF1GRPUr3Hz85INcQvoceniEQOCtfV2Lc2XSisqVaDyDf3NkiTzkXd8zGioZFyjqP2W&X-Amz-Signature=46d00b1ec2fd92b71165f509e327902b51a654198b894bb955a81a58e68bcaa7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4XTFXSZ%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUI09Z3kACqaEerl%2BUJziR%2FL0XQXs%2FsubIfI5pUIHGzAiBVRp3SvY4W1r7CnGhSshH%2Bkb3SUvRWapmNDI48ECfmDSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSTiPRNDdNGjVqa8dKtwDcU%2FrNIl1PL2KQQ8VryK%2B16tZ7j8uF30Kiirjboj878BOG1KzcOuV07Nl0lyPlJsK5tPhdXnGd2lGTZ6f1YhHO%2FR9%2FCQhR33VAGVGoK4UAb1lZg%2FFpwIZUOpS6fSTz2CaA79KXdmlOmSi75%2FQzh8UjLIJpsDTBRyUP%2BTmGLaeqtrPdShrMDJQbhwSZBmUYA7eCnOMQC4jv0uHytb66KAmrFvawWkJ7UMOqznv3drEqxP56%2FUpIAqJwe%2B6h17Qwj1tcygILNKdfU4QuNoIa0qFcdyTfFtcl7EEbXSBKw0cwNSk8t6alZEzsB%2FXqP7luidTtr3En9C4AxB2tAOcnGDGOeB4VIdZblCgDSrPjDgwvjZSC%2Bz4VxtNWxklvbRqLokzGdLI0Ur9JKLaEBjY%2F%2BYzgVBwI7OThZBfl3f5KHROx7pqSE0FhwbfpTchxQ24GDFfZGSHVsLz70%2BCD3ZG5NbB0mt5lg2lM3wMHgOfOaPTEoHd2ak8YiCnYLzNaBwVEFOGoE0%2Bqm3bdlSKTSszw1hFlf1O9ob%2FWU36Z5Hop%2FCGL0oJrpO8F385d33w0pLIWPHqsw7p7hLDS2rfOzzQPPrnN%2FVA%2F0SINs1dnrDUBrnAwbmRmwAKuENTLA%2FLOYcwzbfNzQY6pgHXk4JRygrZuLbnb%2BoD3xNGyWOXQW50GR2zJEldPdyfkMwDPOD2Vg06TjGZZDzWlSXWYLhNX8dVs4EmS6ZfCH7GY3ye%2BrZk7nX6TNZWC8I0t2N9FjvRiRc6F%2B60e1YbgLhTA2LAsyaN%2BAu1HFInh7IJWv%2BrjcF1GRPUr3Hz85INcQvoceniEQOCtfV2Lc2XSisqVaDyDf3NkiTzkXd8zGioZFyjqP2W&X-Amz-Signature=6d212d22a3ccbef1bb86ab99d9e420350acbb4d4ece0fcf44f18d32a3f1da265&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4XTFXSZ%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHUI09Z3kACqaEerl%2BUJziR%2FL0XQXs%2FsubIfI5pUIHGzAiBVRp3SvY4W1r7CnGhSshH%2Bkb3SUvRWapmNDI48ECfmDSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSTiPRNDdNGjVqa8dKtwDcU%2FrNIl1PL2KQQ8VryK%2B16tZ7j8uF30Kiirjboj878BOG1KzcOuV07Nl0lyPlJsK5tPhdXnGd2lGTZ6f1YhHO%2FR9%2FCQhR33VAGVGoK4UAb1lZg%2FFpwIZUOpS6fSTz2CaA79KXdmlOmSi75%2FQzh8UjLIJpsDTBRyUP%2BTmGLaeqtrPdShrMDJQbhwSZBmUYA7eCnOMQC4jv0uHytb66KAmrFvawWkJ7UMOqznv3drEqxP56%2FUpIAqJwe%2B6h17Qwj1tcygILNKdfU4QuNoIa0qFcdyTfFtcl7EEbXSBKw0cwNSk8t6alZEzsB%2FXqP7luidTtr3En9C4AxB2tAOcnGDGOeB4VIdZblCgDSrPjDgwvjZSC%2Bz4VxtNWxklvbRqLokzGdLI0Ur9JKLaEBjY%2F%2BYzgVBwI7OThZBfl3f5KHROx7pqSE0FhwbfpTchxQ24GDFfZGSHVsLz70%2BCD3ZG5NbB0mt5lg2lM3wMHgOfOaPTEoHd2ak8YiCnYLzNaBwVEFOGoE0%2Bqm3bdlSKTSszw1hFlf1O9ob%2FWU36Z5Hop%2FCGL0oJrpO8F385d33w0pLIWPHqsw7p7hLDS2rfOzzQPPrnN%2FVA%2F0SINs1dnrDUBrnAwbmRmwAKuENTLA%2FLOYcwzbfNzQY6pgHXk4JRygrZuLbnb%2BoD3xNGyWOXQW50GR2zJEldPdyfkMwDPOD2Vg06TjGZZDzWlSXWYLhNX8dVs4EmS6ZfCH7GY3ye%2BrZk7nX6TNZWC8I0t2N9FjvRiRc6F%2B60e1YbgLhTA2LAsyaN%2BAu1HFInh7IJWv%2BrjcF1GRPUr3Hz85INcQvoceniEQOCtfV2Lc2XSisqVaDyDf3NkiTzkXd8zGioZFyjqP2W&X-Amz-Signature=652bb7369ad73f4fb426e99a8fcfe9aa02ec570658d5e720b4371fa9aab49724&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

