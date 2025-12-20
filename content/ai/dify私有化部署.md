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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBSDKG6D%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs68s7NQhWc5sggyYrVXYBmE3BgMmDRmJgVTKxJ8SyOwIhALed9gWZSpaKMbh0ThzmK8GmjPRbdZXQ4N9j4F2pfdxbKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2bIi1irQO%2FKV5X8q3APD4V4NhjV%2FeoDLU%2Fl4EHrnM1A%2BQYWeDatwuQg5keSckABkEiUPV8viEQesd%2FRE%2FwgsCAdzbXdyyZ%2FEBcROHv1Jza%2BYtalk5l9YrAcGxViL%2Fo3C%2Brg1QrqQPXf36MxrVfS3wmr6gXqxT%2B1j%2BCcEI6l3xu8sjKxkaNkxlKmrkqLBXIRoQsNFOzc%2FHqaJ%2F%2FxgmFdXUf5Quo8xzp7QnC3RvettrnJ74uTCZ6f%2Fcve%2BoPangUGWGZ00a0lcdzYgUiIIkwfvDaqponMknCnY9Alvt5ub%2F8AZ8M8CLEss38BT8ZunPw35OT1rM2H9W3vlCuAfADU1MpaZeuIob9zqABlk%2FehRoJMC9M7UeuAfh19r35nUZS8MtHa1yHEjapjdrg%2BJXQcKXdrRhA9NU11LENqVoeaj3Fr2q6MpoqBhnu0aXScviu3KLbTdP6A23hGx22hQdsolrGQCngEYY3w5AmfBL4hBE3oQ%2FGgxHJC2ir8ppIDv8G5KXFmdHlQi9IRFo9p42hWm%2B467eUwnyrqAbouiUicVW6avtzCXJmZkUW%2FaevzOjAu6SXMxcR3H%2BvA6YJnAgx%2FPwztn1M%2F%2FECXady%2BKAJ38EVWu6CczFcfesiys4dFRAgU6qhsPipCvxomtWzDUhZjKBjqkARk2cATF8N7k7kldGgHaSgjl2kPLdNaMoMWzlXpRd5kxqtlNlAwYQiJBSe83YQ5r4Xsi%2Fc8pjqxv9gllHiRR4d21GVricQXRRVif57N40E3RP1e05WLA%2BXW3DNzIeJmvf1fBWHV19wKuhvNEgPKiki2zxc71zWCX6cQsbOARHDJx55Dk2RhqhiZvF9gYtyBVUWdHBNAmrvqVAh1Ztee5%2FDU3J3%2F1&X-Amz-Signature=11027f462b3940b2df28e2b959856488ad7e19a4ec63e860748f43cae2a86469&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBSDKG6D%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs68s7NQhWc5sggyYrVXYBmE3BgMmDRmJgVTKxJ8SyOwIhALed9gWZSpaKMbh0ThzmK8GmjPRbdZXQ4N9j4F2pfdxbKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2bIi1irQO%2FKV5X8q3APD4V4NhjV%2FeoDLU%2Fl4EHrnM1A%2BQYWeDatwuQg5keSckABkEiUPV8viEQesd%2FRE%2FwgsCAdzbXdyyZ%2FEBcROHv1Jza%2BYtalk5l9YrAcGxViL%2Fo3C%2Brg1QrqQPXf36MxrVfS3wmr6gXqxT%2B1j%2BCcEI6l3xu8sjKxkaNkxlKmrkqLBXIRoQsNFOzc%2FHqaJ%2F%2FxgmFdXUf5Quo8xzp7QnC3RvettrnJ74uTCZ6f%2Fcve%2BoPangUGWGZ00a0lcdzYgUiIIkwfvDaqponMknCnY9Alvt5ub%2F8AZ8M8CLEss38BT8ZunPw35OT1rM2H9W3vlCuAfADU1MpaZeuIob9zqABlk%2FehRoJMC9M7UeuAfh19r35nUZS8MtHa1yHEjapjdrg%2BJXQcKXdrRhA9NU11LENqVoeaj3Fr2q6MpoqBhnu0aXScviu3KLbTdP6A23hGx22hQdsolrGQCngEYY3w5AmfBL4hBE3oQ%2FGgxHJC2ir8ppIDv8G5KXFmdHlQi9IRFo9p42hWm%2B467eUwnyrqAbouiUicVW6avtzCXJmZkUW%2FaevzOjAu6SXMxcR3H%2BvA6YJnAgx%2FPwztn1M%2F%2FECXady%2BKAJ38EVWu6CczFcfesiys4dFRAgU6qhsPipCvxomtWzDUhZjKBjqkARk2cATF8N7k7kldGgHaSgjl2kPLdNaMoMWzlXpRd5kxqtlNlAwYQiJBSe83YQ5r4Xsi%2Fc8pjqxv9gllHiRR4d21GVricQXRRVif57N40E3RP1e05WLA%2BXW3DNzIeJmvf1fBWHV19wKuhvNEgPKiki2zxc71zWCX6cQsbOARHDJx55Dk2RhqhiZvF9gYtyBVUWdHBNAmrvqVAh1Ztee5%2FDU3J3%2F1&X-Amz-Signature=4910fbe6150c745076f61227754b36bad767683c05b5993816b5aca5d0dfb9da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBSDKG6D%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs68s7NQhWc5sggyYrVXYBmE3BgMmDRmJgVTKxJ8SyOwIhALed9gWZSpaKMbh0ThzmK8GmjPRbdZXQ4N9j4F2pfdxbKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2bIi1irQO%2FKV5X8q3APD4V4NhjV%2FeoDLU%2Fl4EHrnM1A%2BQYWeDatwuQg5keSckABkEiUPV8viEQesd%2FRE%2FwgsCAdzbXdyyZ%2FEBcROHv1Jza%2BYtalk5l9YrAcGxViL%2Fo3C%2Brg1QrqQPXf36MxrVfS3wmr6gXqxT%2B1j%2BCcEI6l3xu8sjKxkaNkxlKmrkqLBXIRoQsNFOzc%2FHqaJ%2F%2FxgmFdXUf5Quo8xzp7QnC3RvettrnJ74uTCZ6f%2Fcve%2BoPangUGWGZ00a0lcdzYgUiIIkwfvDaqponMknCnY9Alvt5ub%2F8AZ8M8CLEss38BT8ZunPw35OT1rM2H9W3vlCuAfADU1MpaZeuIob9zqABlk%2FehRoJMC9M7UeuAfh19r35nUZS8MtHa1yHEjapjdrg%2BJXQcKXdrRhA9NU11LENqVoeaj3Fr2q6MpoqBhnu0aXScviu3KLbTdP6A23hGx22hQdsolrGQCngEYY3w5AmfBL4hBE3oQ%2FGgxHJC2ir8ppIDv8G5KXFmdHlQi9IRFo9p42hWm%2B467eUwnyrqAbouiUicVW6avtzCXJmZkUW%2FaevzOjAu6SXMxcR3H%2BvA6YJnAgx%2FPwztn1M%2F%2FECXady%2BKAJ38EVWu6CczFcfesiys4dFRAgU6qhsPipCvxomtWzDUhZjKBjqkARk2cATF8N7k7kldGgHaSgjl2kPLdNaMoMWzlXpRd5kxqtlNlAwYQiJBSe83YQ5r4Xsi%2Fc8pjqxv9gllHiRR4d21GVricQXRRVif57N40E3RP1e05WLA%2BXW3DNzIeJmvf1fBWHV19wKuhvNEgPKiki2zxc71zWCX6cQsbOARHDJx55Dk2RhqhiZvF9gYtyBVUWdHBNAmrvqVAh1Ztee5%2FDU3J3%2F1&X-Amz-Signature=e2e8cb41837ee34c08423acf789545afb8125b14711caa56b010ea2f118c54a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBSDKG6D%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs68s7NQhWc5sggyYrVXYBmE3BgMmDRmJgVTKxJ8SyOwIhALed9gWZSpaKMbh0ThzmK8GmjPRbdZXQ4N9j4F2pfdxbKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2bIi1irQO%2FKV5X8q3APD4V4NhjV%2FeoDLU%2Fl4EHrnM1A%2BQYWeDatwuQg5keSckABkEiUPV8viEQesd%2FRE%2FwgsCAdzbXdyyZ%2FEBcROHv1Jza%2BYtalk5l9YrAcGxViL%2Fo3C%2Brg1QrqQPXf36MxrVfS3wmr6gXqxT%2B1j%2BCcEI6l3xu8sjKxkaNkxlKmrkqLBXIRoQsNFOzc%2FHqaJ%2F%2FxgmFdXUf5Quo8xzp7QnC3RvettrnJ74uTCZ6f%2Fcve%2BoPangUGWGZ00a0lcdzYgUiIIkwfvDaqponMknCnY9Alvt5ub%2F8AZ8M8CLEss38BT8ZunPw35OT1rM2H9W3vlCuAfADU1MpaZeuIob9zqABlk%2FehRoJMC9M7UeuAfh19r35nUZS8MtHa1yHEjapjdrg%2BJXQcKXdrRhA9NU11LENqVoeaj3Fr2q6MpoqBhnu0aXScviu3KLbTdP6A23hGx22hQdsolrGQCngEYY3w5AmfBL4hBE3oQ%2FGgxHJC2ir8ppIDv8G5KXFmdHlQi9IRFo9p42hWm%2B467eUwnyrqAbouiUicVW6avtzCXJmZkUW%2FaevzOjAu6SXMxcR3H%2BvA6YJnAgx%2FPwztn1M%2F%2FECXady%2BKAJ38EVWu6CczFcfesiys4dFRAgU6qhsPipCvxomtWzDUhZjKBjqkARk2cATF8N7k7kldGgHaSgjl2kPLdNaMoMWzlXpRd5kxqtlNlAwYQiJBSe83YQ5r4Xsi%2Fc8pjqxv9gllHiRR4d21GVricQXRRVif57N40E3RP1e05WLA%2BXW3DNzIeJmvf1fBWHV19wKuhvNEgPKiki2zxc71zWCX6cQsbOARHDJx55Dk2RhqhiZvF9gYtyBVUWdHBNAmrvqVAh1Ztee5%2FDU3J3%2F1&X-Amz-Signature=1d60dcc1b4adca49e1a0a76e3c6e0a1041bc31908cac27ad3846dce0cff5f16c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBSDKG6D%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs68s7NQhWc5sggyYrVXYBmE3BgMmDRmJgVTKxJ8SyOwIhALed9gWZSpaKMbh0ThzmK8GmjPRbdZXQ4N9j4F2pfdxbKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2bIi1irQO%2FKV5X8q3APD4V4NhjV%2FeoDLU%2Fl4EHrnM1A%2BQYWeDatwuQg5keSckABkEiUPV8viEQesd%2FRE%2FwgsCAdzbXdyyZ%2FEBcROHv1Jza%2BYtalk5l9YrAcGxViL%2Fo3C%2Brg1QrqQPXf36MxrVfS3wmr6gXqxT%2B1j%2BCcEI6l3xu8sjKxkaNkxlKmrkqLBXIRoQsNFOzc%2FHqaJ%2F%2FxgmFdXUf5Quo8xzp7QnC3RvettrnJ74uTCZ6f%2Fcve%2BoPangUGWGZ00a0lcdzYgUiIIkwfvDaqponMknCnY9Alvt5ub%2F8AZ8M8CLEss38BT8ZunPw35OT1rM2H9W3vlCuAfADU1MpaZeuIob9zqABlk%2FehRoJMC9M7UeuAfh19r35nUZS8MtHa1yHEjapjdrg%2BJXQcKXdrRhA9NU11LENqVoeaj3Fr2q6MpoqBhnu0aXScviu3KLbTdP6A23hGx22hQdsolrGQCngEYY3w5AmfBL4hBE3oQ%2FGgxHJC2ir8ppIDv8G5KXFmdHlQi9IRFo9p42hWm%2B467eUwnyrqAbouiUicVW6avtzCXJmZkUW%2FaevzOjAu6SXMxcR3H%2BvA6YJnAgx%2FPwztn1M%2F%2FECXady%2BKAJ38EVWu6CczFcfesiys4dFRAgU6qhsPipCvxomtWzDUhZjKBjqkARk2cATF8N7k7kldGgHaSgjl2kPLdNaMoMWzlXpRd5kxqtlNlAwYQiJBSe83YQ5r4Xsi%2Fc8pjqxv9gllHiRR4d21GVricQXRRVif57N40E3RP1e05WLA%2BXW3DNzIeJmvf1fBWHV19wKuhvNEgPKiki2zxc71zWCX6cQsbOARHDJx55Dk2RhqhiZvF9gYtyBVUWdHBNAmrvqVAh1Ztee5%2FDU3J3%2F1&X-Amz-Signature=5a11313f5adf0a99848fd6ae918c836ff28a59c36b9137ef48e36e643d7cabca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBSDKG6D%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs68s7NQhWc5sggyYrVXYBmE3BgMmDRmJgVTKxJ8SyOwIhALed9gWZSpaKMbh0ThzmK8GmjPRbdZXQ4N9j4F2pfdxbKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2bIi1irQO%2FKV5X8q3APD4V4NhjV%2FeoDLU%2Fl4EHrnM1A%2BQYWeDatwuQg5keSckABkEiUPV8viEQesd%2FRE%2FwgsCAdzbXdyyZ%2FEBcROHv1Jza%2BYtalk5l9YrAcGxViL%2Fo3C%2Brg1QrqQPXf36MxrVfS3wmr6gXqxT%2B1j%2BCcEI6l3xu8sjKxkaNkxlKmrkqLBXIRoQsNFOzc%2FHqaJ%2F%2FxgmFdXUf5Quo8xzp7QnC3RvettrnJ74uTCZ6f%2Fcve%2BoPangUGWGZ00a0lcdzYgUiIIkwfvDaqponMknCnY9Alvt5ub%2F8AZ8M8CLEss38BT8ZunPw35OT1rM2H9W3vlCuAfADU1MpaZeuIob9zqABlk%2FehRoJMC9M7UeuAfh19r35nUZS8MtHa1yHEjapjdrg%2BJXQcKXdrRhA9NU11LENqVoeaj3Fr2q6MpoqBhnu0aXScviu3KLbTdP6A23hGx22hQdsolrGQCngEYY3w5AmfBL4hBE3oQ%2FGgxHJC2ir8ppIDv8G5KXFmdHlQi9IRFo9p42hWm%2B467eUwnyrqAbouiUicVW6avtzCXJmZkUW%2FaevzOjAu6SXMxcR3H%2BvA6YJnAgx%2FPwztn1M%2F%2FECXady%2BKAJ38EVWu6CczFcfesiys4dFRAgU6qhsPipCvxomtWzDUhZjKBjqkARk2cATF8N7k7kldGgHaSgjl2kPLdNaMoMWzlXpRd5kxqtlNlAwYQiJBSe83YQ5r4Xsi%2Fc8pjqxv9gllHiRR4d21GVricQXRRVif57N40E3RP1e05WLA%2BXW3DNzIeJmvf1fBWHV19wKuhvNEgPKiki2zxc71zWCX6cQsbOARHDJx55Dk2RhqhiZvF9gYtyBVUWdHBNAmrvqVAh1Ztee5%2FDU3J3%2F1&X-Amz-Signature=e345b7210f06d8c6ac21f8ecb07197e98176fe11da52d37fb2ecabfb37803ffc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBSDKG6D%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs68s7NQhWc5sggyYrVXYBmE3BgMmDRmJgVTKxJ8SyOwIhALed9gWZSpaKMbh0ThzmK8GmjPRbdZXQ4N9j4F2pfdxbKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2bIi1irQO%2FKV5X8q3APD4V4NhjV%2FeoDLU%2Fl4EHrnM1A%2BQYWeDatwuQg5keSckABkEiUPV8viEQesd%2FRE%2FwgsCAdzbXdyyZ%2FEBcROHv1Jza%2BYtalk5l9YrAcGxViL%2Fo3C%2Brg1QrqQPXf36MxrVfS3wmr6gXqxT%2B1j%2BCcEI6l3xu8sjKxkaNkxlKmrkqLBXIRoQsNFOzc%2FHqaJ%2F%2FxgmFdXUf5Quo8xzp7QnC3RvettrnJ74uTCZ6f%2Fcve%2BoPangUGWGZ00a0lcdzYgUiIIkwfvDaqponMknCnY9Alvt5ub%2F8AZ8M8CLEss38BT8ZunPw35OT1rM2H9W3vlCuAfADU1MpaZeuIob9zqABlk%2FehRoJMC9M7UeuAfh19r35nUZS8MtHa1yHEjapjdrg%2BJXQcKXdrRhA9NU11LENqVoeaj3Fr2q6MpoqBhnu0aXScviu3KLbTdP6A23hGx22hQdsolrGQCngEYY3w5AmfBL4hBE3oQ%2FGgxHJC2ir8ppIDv8G5KXFmdHlQi9IRFo9p42hWm%2B467eUwnyrqAbouiUicVW6avtzCXJmZkUW%2FaevzOjAu6SXMxcR3H%2BvA6YJnAgx%2FPwztn1M%2F%2FECXady%2BKAJ38EVWu6CczFcfesiys4dFRAgU6qhsPipCvxomtWzDUhZjKBjqkARk2cATF8N7k7kldGgHaSgjl2kPLdNaMoMWzlXpRd5kxqtlNlAwYQiJBSe83YQ5r4Xsi%2Fc8pjqxv9gllHiRR4d21GVricQXRRVif57N40E3RP1e05WLA%2BXW3DNzIeJmvf1fBWHV19wKuhvNEgPKiki2zxc71zWCX6cQsbOARHDJx55Dk2RhqhiZvF9gYtyBVUWdHBNAmrvqVAh1Ztee5%2FDU3J3%2F1&X-Amz-Signature=875a8deaa9010db68b3f09e33e42f82cee54297e9ff2748154e970ca1200dee9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBSDKG6D%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs68s7NQhWc5sggyYrVXYBmE3BgMmDRmJgVTKxJ8SyOwIhALed9gWZSpaKMbh0ThzmK8GmjPRbdZXQ4N9j4F2pfdxbKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2bIi1irQO%2FKV5X8q3APD4V4NhjV%2FeoDLU%2Fl4EHrnM1A%2BQYWeDatwuQg5keSckABkEiUPV8viEQesd%2FRE%2FwgsCAdzbXdyyZ%2FEBcROHv1Jza%2BYtalk5l9YrAcGxViL%2Fo3C%2Brg1QrqQPXf36MxrVfS3wmr6gXqxT%2B1j%2BCcEI6l3xu8sjKxkaNkxlKmrkqLBXIRoQsNFOzc%2FHqaJ%2F%2FxgmFdXUf5Quo8xzp7QnC3RvettrnJ74uTCZ6f%2Fcve%2BoPangUGWGZ00a0lcdzYgUiIIkwfvDaqponMknCnY9Alvt5ub%2F8AZ8M8CLEss38BT8ZunPw35OT1rM2H9W3vlCuAfADU1MpaZeuIob9zqABlk%2FehRoJMC9M7UeuAfh19r35nUZS8MtHa1yHEjapjdrg%2BJXQcKXdrRhA9NU11LENqVoeaj3Fr2q6MpoqBhnu0aXScviu3KLbTdP6A23hGx22hQdsolrGQCngEYY3w5AmfBL4hBE3oQ%2FGgxHJC2ir8ppIDv8G5KXFmdHlQi9IRFo9p42hWm%2B467eUwnyrqAbouiUicVW6avtzCXJmZkUW%2FaevzOjAu6SXMxcR3H%2BvA6YJnAgx%2FPwztn1M%2F%2FECXady%2BKAJ38EVWu6CczFcfesiys4dFRAgU6qhsPipCvxomtWzDUhZjKBjqkARk2cATF8N7k7kldGgHaSgjl2kPLdNaMoMWzlXpRd5kxqtlNlAwYQiJBSe83YQ5r4Xsi%2Fc8pjqxv9gllHiRR4d21GVricQXRRVif57N40E3RP1e05WLA%2BXW3DNzIeJmvf1fBWHV19wKuhvNEgPKiki2zxc71zWCX6cQsbOARHDJx55Dk2RhqhiZvF9gYtyBVUWdHBNAmrvqVAh1Ztee5%2FDU3J3%2F1&X-Amz-Signature=aad945fc68d995da3f0e3feebc3551f6915e4841205c3650e3c6ec92244dc4d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBSDKG6D%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs68s7NQhWc5sggyYrVXYBmE3BgMmDRmJgVTKxJ8SyOwIhALed9gWZSpaKMbh0ThzmK8GmjPRbdZXQ4N9j4F2pfdxbKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2bIi1irQO%2FKV5X8q3APD4V4NhjV%2FeoDLU%2Fl4EHrnM1A%2BQYWeDatwuQg5keSckABkEiUPV8viEQesd%2FRE%2FwgsCAdzbXdyyZ%2FEBcROHv1Jza%2BYtalk5l9YrAcGxViL%2Fo3C%2Brg1QrqQPXf36MxrVfS3wmr6gXqxT%2B1j%2BCcEI6l3xu8sjKxkaNkxlKmrkqLBXIRoQsNFOzc%2FHqaJ%2F%2FxgmFdXUf5Quo8xzp7QnC3RvettrnJ74uTCZ6f%2Fcve%2BoPangUGWGZ00a0lcdzYgUiIIkwfvDaqponMknCnY9Alvt5ub%2F8AZ8M8CLEss38BT8ZunPw35OT1rM2H9W3vlCuAfADU1MpaZeuIob9zqABlk%2FehRoJMC9M7UeuAfh19r35nUZS8MtHa1yHEjapjdrg%2BJXQcKXdrRhA9NU11LENqVoeaj3Fr2q6MpoqBhnu0aXScviu3KLbTdP6A23hGx22hQdsolrGQCngEYY3w5AmfBL4hBE3oQ%2FGgxHJC2ir8ppIDv8G5KXFmdHlQi9IRFo9p42hWm%2B467eUwnyrqAbouiUicVW6avtzCXJmZkUW%2FaevzOjAu6SXMxcR3H%2BvA6YJnAgx%2FPwztn1M%2F%2FECXady%2BKAJ38EVWu6CczFcfesiys4dFRAgU6qhsPipCvxomtWzDUhZjKBjqkARk2cATF8N7k7kldGgHaSgjl2kPLdNaMoMWzlXpRd5kxqtlNlAwYQiJBSe83YQ5r4Xsi%2Fc8pjqxv9gllHiRR4d21GVricQXRRVif57N40E3RP1e05WLA%2BXW3DNzIeJmvf1fBWHV19wKuhvNEgPKiki2zxc71zWCX6cQsbOARHDJx55Dk2RhqhiZvF9gYtyBVUWdHBNAmrvqVAh1Ztee5%2FDU3J3%2F1&X-Amz-Signature=b211b6146f3b06af45a3c81820c01c57ef45a2c3ad27be326ef51f6f60b81319&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBSDKG6D%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs68s7NQhWc5sggyYrVXYBmE3BgMmDRmJgVTKxJ8SyOwIhALed9gWZSpaKMbh0ThzmK8GmjPRbdZXQ4N9j4F2pfdxbKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs2bIi1irQO%2FKV5X8q3APD4V4NhjV%2FeoDLU%2Fl4EHrnM1A%2BQYWeDatwuQg5keSckABkEiUPV8viEQesd%2FRE%2FwgsCAdzbXdyyZ%2FEBcROHv1Jza%2BYtalk5l9YrAcGxViL%2Fo3C%2Brg1QrqQPXf36MxrVfS3wmr6gXqxT%2B1j%2BCcEI6l3xu8sjKxkaNkxlKmrkqLBXIRoQsNFOzc%2FHqaJ%2F%2FxgmFdXUf5Quo8xzp7QnC3RvettrnJ74uTCZ6f%2Fcve%2BoPangUGWGZ00a0lcdzYgUiIIkwfvDaqponMknCnY9Alvt5ub%2F8AZ8M8CLEss38BT8ZunPw35OT1rM2H9W3vlCuAfADU1MpaZeuIob9zqABlk%2FehRoJMC9M7UeuAfh19r35nUZS8MtHa1yHEjapjdrg%2BJXQcKXdrRhA9NU11LENqVoeaj3Fr2q6MpoqBhnu0aXScviu3KLbTdP6A23hGx22hQdsolrGQCngEYY3w5AmfBL4hBE3oQ%2FGgxHJC2ir8ppIDv8G5KXFmdHlQi9IRFo9p42hWm%2B467eUwnyrqAbouiUicVW6avtzCXJmZkUW%2FaevzOjAu6SXMxcR3H%2BvA6YJnAgx%2FPwztn1M%2F%2FECXady%2BKAJ38EVWu6CczFcfesiys4dFRAgU6qhsPipCvxomtWzDUhZjKBjqkARk2cATF8N7k7kldGgHaSgjl2kPLdNaMoMWzlXpRd5kxqtlNlAwYQiJBSe83YQ5r4Xsi%2Fc8pjqxv9gllHiRR4d21GVricQXRRVif57N40E3RP1e05WLA%2BXW3DNzIeJmvf1fBWHV19wKuhvNEgPKiki2zxc71zWCX6cQsbOARHDJx55Dk2RhqhiZvF9gYtyBVUWdHBNAmrvqVAh1Ztee5%2FDU3J3%2F1&X-Amz-Signature=998e1bcf75bbf0aaba7ffc1f17129e1c1973b2c45d04d77fe9367b60a27ee017&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

