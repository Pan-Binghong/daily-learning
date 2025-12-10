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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VYCVYXZ%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIClz0zEhV5b80U7HGREJP6vsdfCh4Bkf2%2BtAIbAS0roJAiBEU5pGqJkzWgQ%2FAifqBtLREOngdUlQy4rEIojtIbNS7iqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlCqz9BX8ScvZP0ZKtwDgY0OR4wOs2he0tLoN57SiMv4R266duAS7BgFJmn0EXWyRFk92Zvx%2FCK2%2FYUyEBe%2FgtSUpQxhlG1poLSkC4jo%2BtVbjyKRj0Rfwi3EhbLODzS0Crpdo%2FW46Z%2FYsjs68ElGAeGvMElDz5VZgbRxx4UaehGGS0p%2FdssuUKH6%2BcLN7QA9Hgp%2FIqlhgGeIf1mtN%2FXTN%2FkpT%2Bt9SJqIhux3cZLhfUAMBF7zC%2BnPfsTbxg%2FrMsy4S%2Fi%2BfJN0IdJNWnwprM4vRiDg95I643zevzco53yn54%2FSkVJppMsRio8Q8kH3kjaxSaY4DKx8sVMughFvZl7Ls9Yh91IxkBOn%2F%2FgIm%2Fa5BZVg2KkfQ0Ie25%2BHJNF%2BTfm%2BGVjhPPXhSHb6rXj0ZIccuzFB1T9YaV3GcHfRZpYnkJ%2BxoIqAyvfsCAx7YxhAu5XrjxK%2BomgCM1lkeV5fzOzVOU9HSmSQmVFlorOql2ACd9vsuOdxorhlBYX4OGkI5yAV1RS9fOCOY0XKnJInvPXNwhvGY2htxns%2FTa9ccI71sDjnKHFX6H20ie8l7dzadeqbEHQI3jXRVYZkDqhz4OjwMjp%2FA%2FRzpNIWeBm9gboUc89liAvYy%2BCTYLPM%2FO9u3qqGjETiPqpTbnO%2FCX4wiMDjyQY6pgFEzayQz9rEnIsMbFgiyWsEzKRDXIltQJeIH7AN4B7rFN0sZwCnCOrqTXhtZes5bvAtvKASNLSoG6IwF91cZ61YRFJJvGjHKbGPegKLnBVdrAsm7M8q%2F99DgkaoVn12k6%2FljJZbnfuJ9kb8UL4JSfhA4kAE%2BN9kAjQyzXMABRPeY6bmeJ36mAh%2BDGj1uPYZSrj%2F8Tx%2FqEsUfBSykZgiDTHCKx%2BQSYwP&X-Amz-Signature=0056f04c626f02b46be4fbc8c586788804160287e085bfac44f99782c382797d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VYCVYXZ%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIClz0zEhV5b80U7HGREJP6vsdfCh4Bkf2%2BtAIbAS0roJAiBEU5pGqJkzWgQ%2FAifqBtLREOngdUlQy4rEIojtIbNS7iqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlCqz9BX8ScvZP0ZKtwDgY0OR4wOs2he0tLoN57SiMv4R266duAS7BgFJmn0EXWyRFk92Zvx%2FCK2%2FYUyEBe%2FgtSUpQxhlG1poLSkC4jo%2BtVbjyKRj0Rfwi3EhbLODzS0Crpdo%2FW46Z%2FYsjs68ElGAeGvMElDz5VZgbRxx4UaehGGS0p%2FdssuUKH6%2BcLN7QA9Hgp%2FIqlhgGeIf1mtN%2FXTN%2FkpT%2Bt9SJqIhux3cZLhfUAMBF7zC%2BnPfsTbxg%2FrMsy4S%2Fi%2BfJN0IdJNWnwprM4vRiDg95I643zevzco53yn54%2FSkVJppMsRio8Q8kH3kjaxSaY4DKx8sVMughFvZl7Ls9Yh91IxkBOn%2F%2FgIm%2Fa5BZVg2KkfQ0Ie25%2BHJNF%2BTfm%2BGVjhPPXhSHb6rXj0ZIccuzFB1T9YaV3GcHfRZpYnkJ%2BxoIqAyvfsCAx7YxhAu5XrjxK%2BomgCM1lkeV5fzOzVOU9HSmSQmVFlorOql2ACd9vsuOdxorhlBYX4OGkI5yAV1RS9fOCOY0XKnJInvPXNwhvGY2htxns%2FTa9ccI71sDjnKHFX6H20ie8l7dzadeqbEHQI3jXRVYZkDqhz4OjwMjp%2FA%2FRzpNIWeBm9gboUc89liAvYy%2BCTYLPM%2FO9u3qqGjETiPqpTbnO%2FCX4wiMDjyQY6pgFEzayQz9rEnIsMbFgiyWsEzKRDXIltQJeIH7AN4B7rFN0sZwCnCOrqTXhtZes5bvAtvKASNLSoG6IwF91cZ61YRFJJvGjHKbGPegKLnBVdrAsm7M8q%2F99DgkaoVn12k6%2FljJZbnfuJ9kb8UL4JSfhA4kAE%2BN9kAjQyzXMABRPeY6bmeJ36mAh%2BDGj1uPYZSrj%2F8Tx%2FqEsUfBSykZgiDTHCKx%2BQSYwP&X-Amz-Signature=410815f424e5d9dd035f1a6504ddf0c74146a1537426bf6c6a4aa09704c9f450&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VYCVYXZ%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIClz0zEhV5b80U7HGREJP6vsdfCh4Bkf2%2BtAIbAS0roJAiBEU5pGqJkzWgQ%2FAifqBtLREOngdUlQy4rEIojtIbNS7iqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlCqz9BX8ScvZP0ZKtwDgY0OR4wOs2he0tLoN57SiMv4R266duAS7BgFJmn0EXWyRFk92Zvx%2FCK2%2FYUyEBe%2FgtSUpQxhlG1poLSkC4jo%2BtVbjyKRj0Rfwi3EhbLODzS0Crpdo%2FW46Z%2FYsjs68ElGAeGvMElDz5VZgbRxx4UaehGGS0p%2FdssuUKH6%2BcLN7QA9Hgp%2FIqlhgGeIf1mtN%2FXTN%2FkpT%2Bt9SJqIhux3cZLhfUAMBF7zC%2BnPfsTbxg%2FrMsy4S%2Fi%2BfJN0IdJNWnwprM4vRiDg95I643zevzco53yn54%2FSkVJppMsRio8Q8kH3kjaxSaY4DKx8sVMughFvZl7Ls9Yh91IxkBOn%2F%2FgIm%2Fa5BZVg2KkfQ0Ie25%2BHJNF%2BTfm%2BGVjhPPXhSHb6rXj0ZIccuzFB1T9YaV3GcHfRZpYnkJ%2BxoIqAyvfsCAx7YxhAu5XrjxK%2BomgCM1lkeV5fzOzVOU9HSmSQmVFlorOql2ACd9vsuOdxorhlBYX4OGkI5yAV1RS9fOCOY0XKnJInvPXNwhvGY2htxns%2FTa9ccI71sDjnKHFX6H20ie8l7dzadeqbEHQI3jXRVYZkDqhz4OjwMjp%2FA%2FRzpNIWeBm9gboUc89liAvYy%2BCTYLPM%2FO9u3qqGjETiPqpTbnO%2FCX4wiMDjyQY6pgFEzayQz9rEnIsMbFgiyWsEzKRDXIltQJeIH7AN4B7rFN0sZwCnCOrqTXhtZes5bvAtvKASNLSoG6IwF91cZ61YRFJJvGjHKbGPegKLnBVdrAsm7M8q%2F99DgkaoVn12k6%2FljJZbnfuJ9kb8UL4JSfhA4kAE%2BN9kAjQyzXMABRPeY6bmeJ36mAh%2BDGj1uPYZSrj%2F8Tx%2FqEsUfBSykZgiDTHCKx%2BQSYwP&X-Amz-Signature=9eca490009e9883069ae9a8fedd065af891b4b334245cd704501abc8d5f93f58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VYCVYXZ%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIClz0zEhV5b80U7HGREJP6vsdfCh4Bkf2%2BtAIbAS0roJAiBEU5pGqJkzWgQ%2FAifqBtLREOngdUlQy4rEIojtIbNS7iqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlCqz9BX8ScvZP0ZKtwDgY0OR4wOs2he0tLoN57SiMv4R266duAS7BgFJmn0EXWyRFk92Zvx%2FCK2%2FYUyEBe%2FgtSUpQxhlG1poLSkC4jo%2BtVbjyKRj0Rfwi3EhbLODzS0Crpdo%2FW46Z%2FYsjs68ElGAeGvMElDz5VZgbRxx4UaehGGS0p%2FdssuUKH6%2BcLN7QA9Hgp%2FIqlhgGeIf1mtN%2FXTN%2FkpT%2Bt9SJqIhux3cZLhfUAMBF7zC%2BnPfsTbxg%2FrMsy4S%2Fi%2BfJN0IdJNWnwprM4vRiDg95I643zevzco53yn54%2FSkVJppMsRio8Q8kH3kjaxSaY4DKx8sVMughFvZl7Ls9Yh91IxkBOn%2F%2FgIm%2Fa5BZVg2KkfQ0Ie25%2BHJNF%2BTfm%2BGVjhPPXhSHb6rXj0ZIccuzFB1T9YaV3GcHfRZpYnkJ%2BxoIqAyvfsCAx7YxhAu5XrjxK%2BomgCM1lkeV5fzOzVOU9HSmSQmVFlorOql2ACd9vsuOdxorhlBYX4OGkI5yAV1RS9fOCOY0XKnJInvPXNwhvGY2htxns%2FTa9ccI71sDjnKHFX6H20ie8l7dzadeqbEHQI3jXRVYZkDqhz4OjwMjp%2FA%2FRzpNIWeBm9gboUc89liAvYy%2BCTYLPM%2FO9u3qqGjETiPqpTbnO%2FCX4wiMDjyQY6pgFEzayQz9rEnIsMbFgiyWsEzKRDXIltQJeIH7AN4B7rFN0sZwCnCOrqTXhtZes5bvAtvKASNLSoG6IwF91cZ61YRFJJvGjHKbGPegKLnBVdrAsm7M8q%2F99DgkaoVn12k6%2FljJZbnfuJ9kb8UL4JSfhA4kAE%2BN9kAjQyzXMABRPeY6bmeJ36mAh%2BDGj1uPYZSrj%2F8Tx%2FqEsUfBSykZgiDTHCKx%2BQSYwP&X-Amz-Signature=397e5134eeb635642b96e12112234f8013e04e1ddb4e94c59c237c60f6904510&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VYCVYXZ%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIClz0zEhV5b80U7HGREJP6vsdfCh4Bkf2%2BtAIbAS0roJAiBEU5pGqJkzWgQ%2FAifqBtLREOngdUlQy4rEIojtIbNS7iqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlCqz9BX8ScvZP0ZKtwDgY0OR4wOs2he0tLoN57SiMv4R266duAS7BgFJmn0EXWyRFk92Zvx%2FCK2%2FYUyEBe%2FgtSUpQxhlG1poLSkC4jo%2BtVbjyKRj0Rfwi3EhbLODzS0Crpdo%2FW46Z%2FYsjs68ElGAeGvMElDz5VZgbRxx4UaehGGS0p%2FdssuUKH6%2BcLN7QA9Hgp%2FIqlhgGeIf1mtN%2FXTN%2FkpT%2Bt9SJqIhux3cZLhfUAMBF7zC%2BnPfsTbxg%2FrMsy4S%2Fi%2BfJN0IdJNWnwprM4vRiDg95I643zevzco53yn54%2FSkVJppMsRio8Q8kH3kjaxSaY4DKx8sVMughFvZl7Ls9Yh91IxkBOn%2F%2FgIm%2Fa5BZVg2KkfQ0Ie25%2BHJNF%2BTfm%2BGVjhPPXhSHb6rXj0ZIccuzFB1T9YaV3GcHfRZpYnkJ%2BxoIqAyvfsCAx7YxhAu5XrjxK%2BomgCM1lkeV5fzOzVOU9HSmSQmVFlorOql2ACd9vsuOdxorhlBYX4OGkI5yAV1RS9fOCOY0XKnJInvPXNwhvGY2htxns%2FTa9ccI71sDjnKHFX6H20ie8l7dzadeqbEHQI3jXRVYZkDqhz4OjwMjp%2FA%2FRzpNIWeBm9gboUc89liAvYy%2BCTYLPM%2FO9u3qqGjETiPqpTbnO%2FCX4wiMDjyQY6pgFEzayQz9rEnIsMbFgiyWsEzKRDXIltQJeIH7AN4B7rFN0sZwCnCOrqTXhtZes5bvAtvKASNLSoG6IwF91cZ61YRFJJvGjHKbGPegKLnBVdrAsm7M8q%2F99DgkaoVn12k6%2FljJZbnfuJ9kb8UL4JSfhA4kAE%2BN9kAjQyzXMABRPeY6bmeJ36mAh%2BDGj1uPYZSrj%2F8Tx%2FqEsUfBSykZgiDTHCKx%2BQSYwP&X-Amz-Signature=67d546de4a5e42148a40b024e8379134df56e9332c01353de74a4bf84882ab24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VYCVYXZ%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIClz0zEhV5b80U7HGREJP6vsdfCh4Bkf2%2BtAIbAS0roJAiBEU5pGqJkzWgQ%2FAifqBtLREOngdUlQy4rEIojtIbNS7iqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlCqz9BX8ScvZP0ZKtwDgY0OR4wOs2he0tLoN57SiMv4R266duAS7BgFJmn0EXWyRFk92Zvx%2FCK2%2FYUyEBe%2FgtSUpQxhlG1poLSkC4jo%2BtVbjyKRj0Rfwi3EhbLODzS0Crpdo%2FW46Z%2FYsjs68ElGAeGvMElDz5VZgbRxx4UaehGGS0p%2FdssuUKH6%2BcLN7QA9Hgp%2FIqlhgGeIf1mtN%2FXTN%2FkpT%2Bt9SJqIhux3cZLhfUAMBF7zC%2BnPfsTbxg%2FrMsy4S%2Fi%2BfJN0IdJNWnwprM4vRiDg95I643zevzco53yn54%2FSkVJppMsRio8Q8kH3kjaxSaY4DKx8sVMughFvZl7Ls9Yh91IxkBOn%2F%2FgIm%2Fa5BZVg2KkfQ0Ie25%2BHJNF%2BTfm%2BGVjhPPXhSHb6rXj0ZIccuzFB1T9YaV3GcHfRZpYnkJ%2BxoIqAyvfsCAx7YxhAu5XrjxK%2BomgCM1lkeV5fzOzVOU9HSmSQmVFlorOql2ACd9vsuOdxorhlBYX4OGkI5yAV1RS9fOCOY0XKnJInvPXNwhvGY2htxns%2FTa9ccI71sDjnKHFX6H20ie8l7dzadeqbEHQI3jXRVYZkDqhz4OjwMjp%2FA%2FRzpNIWeBm9gboUc89liAvYy%2BCTYLPM%2FO9u3qqGjETiPqpTbnO%2FCX4wiMDjyQY6pgFEzayQz9rEnIsMbFgiyWsEzKRDXIltQJeIH7AN4B7rFN0sZwCnCOrqTXhtZes5bvAtvKASNLSoG6IwF91cZ61YRFJJvGjHKbGPegKLnBVdrAsm7M8q%2F99DgkaoVn12k6%2FljJZbnfuJ9kb8UL4JSfhA4kAE%2BN9kAjQyzXMABRPeY6bmeJ36mAh%2BDGj1uPYZSrj%2F8Tx%2FqEsUfBSykZgiDTHCKx%2BQSYwP&X-Amz-Signature=ec940b469d1ca13f93e562e8ab8e19e00c31b89a2e9d5222446fffa6948da55a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VYCVYXZ%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIClz0zEhV5b80U7HGREJP6vsdfCh4Bkf2%2BtAIbAS0roJAiBEU5pGqJkzWgQ%2FAifqBtLREOngdUlQy4rEIojtIbNS7iqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlCqz9BX8ScvZP0ZKtwDgY0OR4wOs2he0tLoN57SiMv4R266duAS7BgFJmn0EXWyRFk92Zvx%2FCK2%2FYUyEBe%2FgtSUpQxhlG1poLSkC4jo%2BtVbjyKRj0Rfwi3EhbLODzS0Crpdo%2FW46Z%2FYsjs68ElGAeGvMElDz5VZgbRxx4UaehGGS0p%2FdssuUKH6%2BcLN7QA9Hgp%2FIqlhgGeIf1mtN%2FXTN%2FkpT%2Bt9SJqIhux3cZLhfUAMBF7zC%2BnPfsTbxg%2FrMsy4S%2Fi%2BfJN0IdJNWnwprM4vRiDg95I643zevzco53yn54%2FSkVJppMsRio8Q8kH3kjaxSaY4DKx8sVMughFvZl7Ls9Yh91IxkBOn%2F%2FgIm%2Fa5BZVg2KkfQ0Ie25%2BHJNF%2BTfm%2BGVjhPPXhSHb6rXj0ZIccuzFB1T9YaV3GcHfRZpYnkJ%2BxoIqAyvfsCAx7YxhAu5XrjxK%2BomgCM1lkeV5fzOzVOU9HSmSQmVFlorOql2ACd9vsuOdxorhlBYX4OGkI5yAV1RS9fOCOY0XKnJInvPXNwhvGY2htxns%2FTa9ccI71sDjnKHFX6H20ie8l7dzadeqbEHQI3jXRVYZkDqhz4OjwMjp%2FA%2FRzpNIWeBm9gboUc89liAvYy%2BCTYLPM%2FO9u3qqGjETiPqpTbnO%2FCX4wiMDjyQY6pgFEzayQz9rEnIsMbFgiyWsEzKRDXIltQJeIH7AN4B7rFN0sZwCnCOrqTXhtZes5bvAtvKASNLSoG6IwF91cZ61YRFJJvGjHKbGPegKLnBVdrAsm7M8q%2F99DgkaoVn12k6%2FljJZbnfuJ9kb8UL4JSfhA4kAE%2BN9kAjQyzXMABRPeY6bmeJ36mAh%2BDGj1uPYZSrj%2F8Tx%2FqEsUfBSykZgiDTHCKx%2BQSYwP&X-Amz-Signature=ebac225636961da5f8b5002e7da4d5a612ec471a7389da8302d6d25d3acd8e76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VYCVYXZ%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIClz0zEhV5b80U7HGREJP6vsdfCh4Bkf2%2BtAIbAS0roJAiBEU5pGqJkzWgQ%2FAifqBtLREOngdUlQy4rEIojtIbNS7iqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlCqz9BX8ScvZP0ZKtwDgY0OR4wOs2he0tLoN57SiMv4R266duAS7BgFJmn0EXWyRFk92Zvx%2FCK2%2FYUyEBe%2FgtSUpQxhlG1poLSkC4jo%2BtVbjyKRj0Rfwi3EhbLODzS0Crpdo%2FW46Z%2FYsjs68ElGAeGvMElDz5VZgbRxx4UaehGGS0p%2FdssuUKH6%2BcLN7QA9Hgp%2FIqlhgGeIf1mtN%2FXTN%2FkpT%2Bt9SJqIhux3cZLhfUAMBF7zC%2BnPfsTbxg%2FrMsy4S%2Fi%2BfJN0IdJNWnwprM4vRiDg95I643zevzco53yn54%2FSkVJppMsRio8Q8kH3kjaxSaY4DKx8sVMughFvZl7Ls9Yh91IxkBOn%2F%2FgIm%2Fa5BZVg2KkfQ0Ie25%2BHJNF%2BTfm%2BGVjhPPXhSHb6rXj0ZIccuzFB1T9YaV3GcHfRZpYnkJ%2BxoIqAyvfsCAx7YxhAu5XrjxK%2BomgCM1lkeV5fzOzVOU9HSmSQmVFlorOql2ACd9vsuOdxorhlBYX4OGkI5yAV1RS9fOCOY0XKnJInvPXNwhvGY2htxns%2FTa9ccI71sDjnKHFX6H20ie8l7dzadeqbEHQI3jXRVYZkDqhz4OjwMjp%2FA%2FRzpNIWeBm9gboUc89liAvYy%2BCTYLPM%2FO9u3qqGjETiPqpTbnO%2FCX4wiMDjyQY6pgFEzayQz9rEnIsMbFgiyWsEzKRDXIltQJeIH7AN4B7rFN0sZwCnCOrqTXhtZes5bvAtvKASNLSoG6IwF91cZ61YRFJJvGjHKbGPegKLnBVdrAsm7M8q%2F99DgkaoVn12k6%2FljJZbnfuJ9kb8UL4JSfhA4kAE%2BN9kAjQyzXMABRPeY6bmeJ36mAh%2BDGj1uPYZSrj%2F8Tx%2FqEsUfBSykZgiDTHCKx%2BQSYwP&X-Amz-Signature=b21e02f94f975b73bf5827d3783ae1900e90e4f7380c52c1d2e83f35101a2ce0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VYCVYXZ%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIClz0zEhV5b80U7HGREJP6vsdfCh4Bkf2%2BtAIbAS0roJAiBEU5pGqJkzWgQ%2FAifqBtLREOngdUlQy4rEIojtIbNS7iqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlCqz9BX8ScvZP0ZKtwDgY0OR4wOs2he0tLoN57SiMv4R266duAS7BgFJmn0EXWyRFk92Zvx%2FCK2%2FYUyEBe%2FgtSUpQxhlG1poLSkC4jo%2BtVbjyKRj0Rfwi3EhbLODzS0Crpdo%2FW46Z%2FYsjs68ElGAeGvMElDz5VZgbRxx4UaehGGS0p%2FdssuUKH6%2BcLN7QA9Hgp%2FIqlhgGeIf1mtN%2FXTN%2FkpT%2Bt9SJqIhux3cZLhfUAMBF7zC%2BnPfsTbxg%2FrMsy4S%2Fi%2BfJN0IdJNWnwprM4vRiDg95I643zevzco53yn54%2FSkVJppMsRio8Q8kH3kjaxSaY4DKx8sVMughFvZl7Ls9Yh91IxkBOn%2F%2FgIm%2Fa5BZVg2KkfQ0Ie25%2BHJNF%2BTfm%2BGVjhPPXhSHb6rXj0ZIccuzFB1T9YaV3GcHfRZpYnkJ%2BxoIqAyvfsCAx7YxhAu5XrjxK%2BomgCM1lkeV5fzOzVOU9HSmSQmVFlorOql2ACd9vsuOdxorhlBYX4OGkI5yAV1RS9fOCOY0XKnJInvPXNwhvGY2htxns%2FTa9ccI71sDjnKHFX6H20ie8l7dzadeqbEHQI3jXRVYZkDqhz4OjwMjp%2FA%2FRzpNIWeBm9gboUc89liAvYy%2BCTYLPM%2FO9u3qqGjETiPqpTbnO%2FCX4wiMDjyQY6pgFEzayQz9rEnIsMbFgiyWsEzKRDXIltQJeIH7AN4B7rFN0sZwCnCOrqTXhtZes5bvAtvKASNLSoG6IwF91cZ61YRFJJvGjHKbGPegKLnBVdrAsm7M8q%2F99DgkaoVn12k6%2FljJZbnfuJ9kb8UL4JSfhA4kAE%2BN9kAjQyzXMABRPeY6bmeJ36mAh%2BDGj1uPYZSrj%2F8Tx%2FqEsUfBSykZgiDTHCKx%2BQSYwP&X-Amz-Signature=71b452c3c103325f28c08bc3f7d0fa88f64d1b298931f15bac4945b0bcec8385&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VYCVYXZ%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIClz0zEhV5b80U7HGREJP6vsdfCh4Bkf2%2BtAIbAS0roJAiBEU5pGqJkzWgQ%2FAifqBtLREOngdUlQy4rEIojtIbNS7iqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlCqz9BX8ScvZP0ZKtwDgY0OR4wOs2he0tLoN57SiMv4R266duAS7BgFJmn0EXWyRFk92Zvx%2FCK2%2FYUyEBe%2FgtSUpQxhlG1poLSkC4jo%2BtVbjyKRj0Rfwi3EhbLODzS0Crpdo%2FW46Z%2FYsjs68ElGAeGvMElDz5VZgbRxx4UaehGGS0p%2FdssuUKH6%2BcLN7QA9Hgp%2FIqlhgGeIf1mtN%2FXTN%2FkpT%2Bt9SJqIhux3cZLhfUAMBF7zC%2BnPfsTbxg%2FrMsy4S%2Fi%2BfJN0IdJNWnwprM4vRiDg95I643zevzco53yn54%2FSkVJppMsRio8Q8kH3kjaxSaY4DKx8sVMughFvZl7Ls9Yh91IxkBOn%2F%2FgIm%2Fa5BZVg2KkfQ0Ie25%2BHJNF%2BTfm%2BGVjhPPXhSHb6rXj0ZIccuzFB1T9YaV3GcHfRZpYnkJ%2BxoIqAyvfsCAx7YxhAu5XrjxK%2BomgCM1lkeV5fzOzVOU9HSmSQmVFlorOql2ACd9vsuOdxorhlBYX4OGkI5yAV1RS9fOCOY0XKnJInvPXNwhvGY2htxns%2FTa9ccI71sDjnKHFX6H20ie8l7dzadeqbEHQI3jXRVYZkDqhz4OjwMjp%2FA%2FRzpNIWeBm9gboUc89liAvYy%2BCTYLPM%2FO9u3qqGjETiPqpTbnO%2FCX4wiMDjyQY6pgFEzayQz9rEnIsMbFgiyWsEzKRDXIltQJeIH7AN4B7rFN0sZwCnCOrqTXhtZes5bvAtvKASNLSoG6IwF91cZ61YRFJJvGjHKbGPegKLnBVdrAsm7M8q%2F99DgkaoVn12k6%2FljJZbnfuJ9kb8UL4JSfhA4kAE%2BN9kAjQyzXMABRPeY6bmeJ36mAh%2BDGj1uPYZSrj%2F8Tx%2FqEsUfBSykZgiDTHCKx%2BQSYwP&X-Amz-Signature=e9a64138028c56b8d56b95eee6105f162c87ba17bc68e4dac0f82a8146c85bc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

