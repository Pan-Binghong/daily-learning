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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466736TNGFE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9895u2ETjhHRzEk5EkD%2Fc1E6g0kKzt95mTxnGg7iQFQIhAL5GT2jEjMS%2BBN9HceUU8s8fGGK1aRfqJ8DVfXhL%2BuHhKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG4FUoS0JNC%2BXT1Vgq3AMraNTh8Xcq2cOl8Y%2F05%2BJLY4sKN8GK74b%2BmqYTnmcDT3SMo7njh7bsqDUYJt4KN3Aye9Pvpajn%2BPR3HTqaqe436lsgv7L6JmTEo7YbbarmGHocc2O99ISAIxhLyadVeZNHJql1ogwv%2FNK3L15q3UbipQ0rUX0hKsDkOMGTfNmRNUD5%2FtX1eiBdHBorSiNte%2Fm2KsmIvjJNanP59peLdsCgQ%2FjbNnwJo6WYbA66XX4GfiAmQvCCBGWiSybM34oLRBVSd3FzNDm7AK6%2BumKEKX8%2B9v7J5v%2Bwpk94CI8JPAjsWFwH6UIsgkFepAPqkqLe8QSX6aQxwtkD5r%2FRKzTw6l%2FYWCnSe2gI37pH83Ye3a4zkeWjN5AQ2lcSC9Y%2Fx%2FGaj%2FYQIIgelNmOmLpV0%2BxD51qJ4bCTaWZL1JP%2FFYADEsrGM0Ok68D%2BeMPmhh3dkcyFd5OOTUoR6BhOau27mKTKyOmz6pA6jbf%2B%2FK0QmWkAsm5BNKJJNy34mddF2%2BNAZmD6KT7pD%2FdeD7Dp9xlNiZQn6%2F7najG4sFqwE6lcv6L0L09uOVgQPw1zk2LKzCOwZj3LeRw8es7nSi0i%2BXWt0vEzo76Ge7r9Net%2FubHN6AW66DVZxj4AorXxuQrwYpsi6DCs8a%2FIBjqkAa%2BJS0tV1JySNvP9ak%2BsK2%2FKBF0Zn%2Bhoz4EklkMSZA5OG3r%2Bf4ghghjNNbQfYltvphdwMDWps3Knffp%2BonMOjYKVzlKCbHNOKinqBy2vHr9PYNcP0rEx%2BSUnS7IaqDGs8fC1yweSgZufwM084ZJgwTdQd%2FLugyr4myU8MP0gWuJ2MDkb%2B%2F5SKkfNlRXvwp0pQ1WpKgzd8B64fF5ZqrDkqjEBpWDX&X-Amz-Signature=e993e5031aca85b00c19d965457c6b724eb93b722b3026bfba4729ec1e85cdea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466736TNGFE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9895u2ETjhHRzEk5EkD%2Fc1E6g0kKzt95mTxnGg7iQFQIhAL5GT2jEjMS%2BBN9HceUU8s8fGGK1aRfqJ8DVfXhL%2BuHhKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG4FUoS0JNC%2BXT1Vgq3AMraNTh8Xcq2cOl8Y%2F05%2BJLY4sKN8GK74b%2BmqYTnmcDT3SMo7njh7bsqDUYJt4KN3Aye9Pvpajn%2BPR3HTqaqe436lsgv7L6JmTEo7YbbarmGHocc2O99ISAIxhLyadVeZNHJql1ogwv%2FNK3L15q3UbipQ0rUX0hKsDkOMGTfNmRNUD5%2FtX1eiBdHBorSiNte%2Fm2KsmIvjJNanP59peLdsCgQ%2FjbNnwJo6WYbA66XX4GfiAmQvCCBGWiSybM34oLRBVSd3FzNDm7AK6%2BumKEKX8%2B9v7J5v%2Bwpk94CI8JPAjsWFwH6UIsgkFepAPqkqLe8QSX6aQxwtkD5r%2FRKzTw6l%2FYWCnSe2gI37pH83Ye3a4zkeWjN5AQ2lcSC9Y%2Fx%2FGaj%2FYQIIgelNmOmLpV0%2BxD51qJ4bCTaWZL1JP%2FFYADEsrGM0Ok68D%2BeMPmhh3dkcyFd5OOTUoR6BhOau27mKTKyOmz6pA6jbf%2B%2FK0QmWkAsm5BNKJJNy34mddF2%2BNAZmD6KT7pD%2FdeD7Dp9xlNiZQn6%2F7najG4sFqwE6lcv6L0L09uOVgQPw1zk2LKzCOwZj3LeRw8es7nSi0i%2BXWt0vEzo76Ge7r9Net%2FubHN6AW66DVZxj4AorXxuQrwYpsi6DCs8a%2FIBjqkAa%2BJS0tV1JySNvP9ak%2BsK2%2FKBF0Zn%2Bhoz4EklkMSZA5OG3r%2Bf4ghghjNNbQfYltvphdwMDWps3Knffp%2BonMOjYKVzlKCbHNOKinqBy2vHr9PYNcP0rEx%2BSUnS7IaqDGs8fC1yweSgZufwM084ZJgwTdQd%2FLugyr4myU8MP0gWuJ2MDkb%2B%2F5SKkfNlRXvwp0pQ1WpKgzd8B64fF5ZqrDkqjEBpWDX&X-Amz-Signature=f58e1e006352cdbbd7efaeebd0037d78b7e39204525e658e5ca0fc0c2d1952bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466736TNGFE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9895u2ETjhHRzEk5EkD%2Fc1E6g0kKzt95mTxnGg7iQFQIhAL5GT2jEjMS%2BBN9HceUU8s8fGGK1aRfqJ8DVfXhL%2BuHhKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG4FUoS0JNC%2BXT1Vgq3AMraNTh8Xcq2cOl8Y%2F05%2BJLY4sKN8GK74b%2BmqYTnmcDT3SMo7njh7bsqDUYJt4KN3Aye9Pvpajn%2BPR3HTqaqe436lsgv7L6JmTEo7YbbarmGHocc2O99ISAIxhLyadVeZNHJql1ogwv%2FNK3L15q3UbipQ0rUX0hKsDkOMGTfNmRNUD5%2FtX1eiBdHBorSiNte%2Fm2KsmIvjJNanP59peLdsCgQ%2FjbNnwJo6WYbA66XX4GfiAmQvCCBGWiSybM34oLRBVSd3FzNDm7AK6%2BumKEKX8%2B9v7J5v%2Bwpk94CI8JPAjsWFwH6UIsgkFepAPqkqLe8QSX6aQxwtkD5r%2FRKzTw6l%2FYWCnSe2gI37pH83Ye3a4zkeWjN5AQ2lcSC9Y%2Fx%2FGaj%2FYQIIgelNmOmLpV0%2BxD51qJ4bCTaWZL1JP%2FFYADEsrGM0Ok68D%2BeMPmhh3dkcyFd5OOTUoR6BhOau27mKTKyOmz6pA6jbf%2B%2FK0QmWkAsm5BNKJJNy34mddF2%2BNAZmD6KT7pD%2FdeD7Dp9xlNiZQn6%2F7najG4sFqwE6lcv6L0L09uOVgQPw1zk2LKzCOwZj3LeRw8es7nSi0i%2BXWt0vEzo76Ge7r9Net%2FubHN6AW66DVZxj4AorXxuQrwYpsi6DCs8a%2FIBjqkAa%2BJS0tV1JySNvP9ak%2BsK2%2FKBF0Zn%2Bhoz4EklkMSZA5OG3r%2Bf4ghghjNNbQfYltvphdwMDWps3Knffp%2BonMOjYKVzlKCbHNOKinqBy2vHr9PYNcP0rEx%2BSUnS7IaqDGs8fC1yweSgZufwM084ZJgwTdQd%2FLugyr4myU8MP0gWuJ2MDkb%2B%2F5SKkfNlRXvwp0pQ1WpKgzd8B64fF5ZqrDkqjEBpWDX&X-Amz-Signature=1f5d944f6d630854fde6569909039de08bb8de650c0f9398dd0993274dd59387&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466736TNGFE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9895u2ETjhHRzEk5EkD%2Fc1E6g0kKzt95mTxnGg7iQFQIhAL5GT2jEjMS%2BBN9HceUU8s8fGGK1aRfqJ8DVfXhL%2BuHhKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG4FUoS0JNC%2BXT1Vgq3AMraNTh8Xcq2cOl8Y%2F05%2BJLY4sKN8GK74b%2BmqYTnmcDT3SMo7njh7bsqDUYJt4KN3Aye9Pvpajn%2BPR3HTqaqe436lsgv7L6JmTEo7YbbarmGHocc2O99ISAIxhLyadVeZNHJql1ogwv%2FNK3L15q3UbipQ0rUX0hKsDkOMGTfNmRNUD5%2FtX1eiBdHBorSiNte%2Fm2KsmIvjJNanP59peLdsCgQ%2FjbNnwJo6WYbA66XX4GfiAmQvCCBGWiSybM34oLRBVSd3FzNDm7AK6%2BumKEKX8%2B9v7J5v%2Bwpk94CI8JPAjsWFwH6UIsgkFepAPqkqLe8QSX6aQxwtkD5r%2FRKzTw6l%2FYWCnSe2gI37pH83Ye3a4zkeWjN5AQ2lcSC9Y%2Fx%2FGaj%2FYQIIgelNmOmLpV0%2BxD51qJ4bCTaWZL1JP%2FFYADEsrGM0Ok68D%2BeMPmhh3dkcyFd5OOTUoR6BhOau27mKTKyOmz6pA6jbf%2B%2FK0QmWkAsm5BNKJJNy34mddF2%2BNAZmD6KT7pD%2FdeD7Dp9xlNiZQn6%2F7najG4sFqwE6lcv6L0L09uOVgQPw1zk2LKzCOwZj3LeRw8es7nSi0i%2BXWt0vEzo76Ge7r9Net%2FubHN6AW66DVZxj4AorXxuQrwYpsi6DCs8a%2FIBjqkAa%2BJS0tV1JySNvP9ak%2BsK2%2FKBF0Zn%2Bhoz4EklkMSZA5OG3r%2Bf4ghghjNNbQfYltvphdwMDWps3Knffp%2BonMOjYKVzlKCbHNOKinqBy2vHr9PYNcP0rEx%2BSUnS7IaqDGs8fC1yweSgZufwM084ZJgwTdQd%2FLugyr4myU8MP0gWuJ2MDkb%2B%2F5SKkfNlRXvwp0pQ1WpKgzd8B64fF5ZqrDkqjEBpWDX&X-Amz-Signature=3e072bf610fecfbcc636509a4b5f8769f1456e8d0843e06dd365dfff82c9fa21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466736TNGFE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9895u2ETjhHRzEk5EkD%2Fc1E6g0kKzt95mTxnGg7iQFQIhAL5GT2jEjMS%2BBN9HceUU8s8fGGK1aRfqJ8DVfXhL%2BuHhKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG4FUoS0JNC%2BXT1Vgq3AMraNTh8Xcq2cOl8Y%2F05%2BJLY4sKN8GK74b%2BmqYTnmcDT3SMo7njh7bsqDUYJt4KN3Aye9Pvpajn%2BPR3HTqaqe436lsgv7L6JmTEo7YbbarmGHocc2O99ISAIxhLyadVeZNHJql1ogwv%2FNK3L15q3UbipQ0rUX0hKsDkOMGTfNmRNUD5%2FtX1eiBdHBorSiNte%2Fm2KsmIvjJNanP59peLdsCgQ%2FjbNnwJo6WYbA66XX4GfiAmQvCCBGWiSybM34oLRBVSd3FzNDm7AK6%2BumKEKX8%2B9v7J5v%2Bwpk94CI8JPAjsWFwH6UIsgkFepAPqkqLe8QSX6aQxwtkD5r%2FRKzTw6l%2FYWCnSe2gI37pH83Ye3a4zkeWjN5AQ2lcSC9Y%2Fx%2FGaj%2FYQIIgelNmOmLpV0%2BxD51qJ4bCTaWZL1JP%2FFYADEsrGM0Ok68D%2BeMPmhh3dkcyFd5OOTUoR6BhOau27mKTKyOmz6pA6jbf%2B%2FK0QmWkAsm5BNKJJNy34mddF2%2BNAZmD6KT7pD%2FdeD7Dp9xlNiZQn6%2F7najG4sFqwE6lcv6L0L09uOVgQPw1zk2LKzCOwZj3LeRw8es7nSi0i%2BXWt0vEzo76Ge7r9Net%2FubHN6AW66DVZxj4AorXxuQrwYpsi6DCs8a%2FIBjqkAa%2BJS0tV1JySNvP9ak%2BsK2%2FKBF0Zn%2Bhoz4EklkMSZA5OG3r%2Bf4ghghjNNbQfYltvphdwMDWps3Knffp%2BonMOjYKVzlKCbHNOKinqBy2vHr9PYNcP0rEx%2BSUnS7IaqDGs8fC1yweSgZufwM084ZJgwTdQd%2FLugyr4myU8MP0gWuJ2MDkb%2B%2F5SKkfNlRXvwp0pQ1WpKgzd8B64fF5ZqrDkqjEBpWDX&X-Amz-Signature=32d758117ce3209f413bce28467be463d70d5567b615c03335f7f34a0ce9e391&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466736TNGFE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9895u2ETjhHRzEk5EkD%2Fc1E6g0kKzt95mTxnGg7iQFQIhAL5GT2jEjMS%2BBN9HceUU8s8fGGK1aRfqJ8DVfXhL%2BuHhKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG4FUoS0JNC%2BXT1Vgq3AMraNTh8Xcq2cOl8Y%2F05%2BJLY4sKN8GK74b%2BmqYTnmcDT3SMo7njh7bsqDUYJt4KN3Aye9Pvpajn%2BPR3HTqaqe436lsgv7L6JmTEo7YbbarmGHocc2O99ISAIxhLyadVeZNHJql1ogwv%2FNK3L15q3UbipQ0rUX0hKsDkOMGTfNmRNUD5%2FtX1eiBdHBorSiNte%2Fm2KsmIvjJNanP59peLdsCgQ%2FjbNnwJo6WYbA66XX4GfiAmQvCCBGWiSybM34oLRBVSd3FzNDm7AK6%2BumKEKX8%2B9v7J5v%2Bwpk94CI8JPAjsWFwH6UIsgkFepAPqkqLe8QSX6aQxwtkD5r%2FRKzTw6l%2FYWCnSe2gI37pH83Ye3a4zkeWjN5AQ2lcSC9Y%2Fx%2FGaj%2FYQIIgelNmOmLpV0%2BxD51qJ4bCTaWZL1JP%2FFYADEsrGM0Ok68D%2BeMPmhh3dkcyFd5OOTUoR6BhOau27mKTKyOmz6pA6jbf%2B%2FK0QmWkAsm5BNKJJNy34mddF2%2BNAZmD6KT7pD%2FdeD7Dp9xlNiZQn6%2F7najG4sFqwE6lcv6L0L09uOVgQPw1zk2LKzCOwZj3LeRw8es7nSi0i%2BXWt0vEzo76Ge7r9Net%2FubHN6AW66DVZxj4AorXxuQrwYpsi6DCs8a%2FIBjqkAa%2BJS0tV1JySNvP9ak%2BsK2%2FKBF0Zn%2Bhoz4EklkMSZA5OG3r%2Bf4ghghjNNbQfYltvphdwMDWps3Knffp%2BonMOjYKVzlKCbHNOKinqBy2vHr9PYNcP0rEx%2BSUnS7IaqDGs8fC1yweSgZufwM084ZJgwTdQd%2FLugyr4myU8MP0gWuJ2MDkb%2B%2F5SKkfNlRXvwp0pQ1WpKgzd8B64fF5ZqrDkqjEBpWDX&X-Amz-Signature=d287265168bcb2b60f82afb4b881395be18ace4c163405d78d379bb89500a593&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466736TNGFE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9895u2ETjhHRzEk5EkD%2Fc1E6g0kKzt95mTxnGg7iQFQIhAL5GT2jEjMS%2BBN9HceUU8s8fGGK1aRfqJ8DVfXhL%2BuHhKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG4FUoS0JNC%2BXT1Vgq3AMraNTh8Xcq2cOl8Y%2F05%2BJLY4sKN8GK74b%2BmqYTnmcDT3SMo7njh7bsqDUYJt4KN3Aye9Pvpajn%2BPR3HTqaqe436lsgv7L6JmTEo7YbbarmGHocc2O99ISAIxhLyadVeZNHJql1ogwv%2FNK3L15q3UbipQ0rUX0hKsDkOMGTfNmRNUD5%2FtX1eiBdHBorSiNte%2Fm2KsmIvjJNanP59peLdsCgQ%2FjbNnwJo6WYbA66XX4GfiAmQvCCBGWiSybM34oLRBVSd3FzNDm7AK6%2BumKEKX8%2B9v7J5v%2Bwpk94CI8JPAjsWFwH6UIsgkFepAPqkqLe8QSX6aQxwtkD5r%2FRKzTw6l%2FYWCnSe2gI37pH83Ye3a4zkeWjN5AQ2lcSC9Y%2Fx%2FGaj%2FYQIIgelNmOmLpV0%2BxD51qJ4bCTaWZL1JP%2FFYADEsrGM0Ok68D%2BeMPmhh3dkcyFd5OOTUoR6BhOau27mKTKyOmz6pA6jbf%2B%2FK0QmWkAsm5BNKJJNy34mddF2%2BNAZmD6KT7pD%2FdeD7Dp9xlNiZQn6%2F7najG4sFqwE6lcv6L0L09uOVgQPw1zk2LKzCOwZj3LeRw8es7nSi0i%2BXWt0vEzo76Ge7r9Net%2FubHN6AW66DVZxj4AorXxuQrwYpsi6DCs8a%2FIBjqkAa%2BJS0tV1JySNvP9ak%2BsK2%2FKBF0Zn%2Bhoz4EklkMSZA5OG3r%2Bf4ghghjNNbQfYltvphdwMDWps3Knffp%2BonMOjYKVzlKCbHNOKinqBy2vHr9PYNcP0rEx%2BSUnS7IaqDGs8fC1yweSgZufwM084ZJgwTdQd%2FLugyr4myU8MP0gWuJ2MDkb%2B%2F5SKkfNlRXvwp0pQ1WpKgzd8B64fF5ZqrDkqjEBpWDX&X-Amz-Signature=00b5d074aff7642e606983be14a93f5d23a8c21dceffa8abd46dcdc6e9402768&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466736TNGFE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9895u2ETjhHRzEk5EkD%2Fc1E6g0kKzt95mTxnGg7iQFQIhAL5GT2jEjMS%2BBN9HceUU8s8fGGK1aRfqJ8DVfXhL%2BuHhKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG4FUoS0JNC%2BXT1Vgq3AMraNTh8Xcq2cOl8Y%2F05%2BJLY4sKN8GK74b%2BmqYTnmcDT3SMo7njh7bsqDUYJt4KN3Aye9Pvpajn%2BPR3HTqaqe436lsgv7L6JmTEo7YbbarmGHocc2O99ISAIxhLyadVeZNHJql1ogwv%2FNK3L15q3UbipQ0rUX0hKsDkOMGTfNmRNUD5%2FtX1eiBdHBorSiNte%2Fm2KsmIvjJNanP59peLdsCgQ%2FjbNnwJo6WYbA66XX4GfiAmQvCCBGWiSybM34oLRBVSd3FzNDm7AK6%2BumKEKX8%2B9v7J5v%2Bwpk94CI8JPAjsWFwH6UIsgkFepAPqkqLe8QSX6aQxwtkD5r%2FRKzTw6l%2FYWCnSe2gI37pH83Ye3a4zkeWjN5AQ2lcSC9Y%2Fx%2FGaj%2FYQIIgelNmOmLpV0%2BxD51qJ4bCTaWZL1JP%2FFYADEsrGM0Ok68D%2BeMPmhh3dkcyFd5OOTUoR6BhOau27mKTKyOmz6pA6jbf%2B%2FK0QmWkAsm5BNKJJNy34mddF2%2BNAZmD6KT7pD%2FdeD7Dp9xlNiZQn6%2F7najG4sFqwE6lcv6L0L09uOVgQPw1zk2LKzCOwZj3LeRw8es7nSi0i%2BXWt0vEzo76Ge7r9Net%2FubHN6AW66DVZxj4AorXxuQrwYpsi6DCs8a%2FIBjqkAa%2BJS0tV1JySNvP9ak%2BsK2%2FKBF0Zn%2Bhoz4EklkMSZA5OG3r%2Bf4ghghjNNbQfYltvphdwMDWps3Knffp%2BonMOjYKVzlKCbHNOKinqBy2vHr9PYNcP0rEx%2BSUnS7IaqDGs8fC1yweSgZufwM084ZJgwTdQd%2FLugyr4myU8MP0gWuJ2MDkb%2B%2F5SKkfNlRXvwp0pQ1WpKgzd8B64fF5ZqrDkqjEBpWDX&X-Amz-Signature=e9a7a4efd1f223785bafcbaf999b08120ea0fb96fb277b8a9e6d6da0cbee3a8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466736TNGFE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9895u2ETjhHRzEk5EkD%2Fc1E6g0kKzt95mTxnGg7iQFQIhAL5GT2jEjMS%2BBN9HceUU8s8fGGK1aRfqJ8DVfXhL%2BuHhKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG4FUoS0JNC%2BXT1Vgq3AMraNTh8Xcq2cOl8Y%2F05%2BJLY4sKN8GK74b%2BmqYTnmcDT3SMo7njh7bsqDUYJt4KN3Aye9Pvpajn%2BPR3HTqaqe436lsgv7L6JmTEo7YbbarmGHocc2O99ISAIxhLyadVeZNHJql1ogwv%2FNK3L15q3UbipQ0rUX0hKsDkOMGTfNmRNUD5%2FtX1eiBdHBorSiNte%2Fm2KsmIvjJNanP59peLdsCgQ%2FjbNnwJo6WYbA66XX4GfiAmQvCCBGWiSybM34oLRBVSd3FzNDm7AK6%2BumKEKX8%2B9v7J5v%2Bwpk94CI8JPAjsWFwH6UIsgkFepAPqkqLe8QSX6aQxwtkD5r%2FRKzTw6l%2FYWCnSe2gI37pH83Ye3a4zkeWjN5AQ2lcSC9Y%2Fx%2FGaj%2FYQIIgelNmOmLpV0%2BxD51qJ4bCTaWZL1JP%2FFYADEsrGM0Ok68D%2BeMPmhh3dkcyFd5OOTUoR6BhOau27mKTKyOmz6pA6jbf%2B%2FK0QmWkAsm5BNKJJNy34mddF2%2BNAZmD6KT7pD%2FdeD7Dp9xlNiZQn6%2F7najG4sFqwE6lcv6L0L09uOVgQPw1zk2LKzCOwZj3LeRw8es7nSi0i%2BXWt0vEzo76Ge7r9Net%2FubHN6AW66DVZxj4AorXxuQrwYpsi6DCs8a%2FIBjqkAa%2BJS0tV1JySNvP9ak%2BsK2%2FKBF0Zn%2Bhoz4EklkMSZA5OG3r%2Bf4ghghjNNbQfYltvphdwMDWps3Knffp%2BonMOjYKVzlKCbHNOKinqBy2vHr9PYNcP0rEx%2BSUnS7IaqDGs8fC1yweSgZufwM084ZJgwTdQd%2FLugyr4myU8MP0gWuJ2MDkb%2B%2F5SKkfNlRXvwp0pQ1WpKgzd8B64fF5ZqrDkqjEBpWDX&X-Amz-Signature=4b8d36eb373666daf56eb4fc1b723372c4354fc57e73812dbe4d5260c74bc0a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466736TNGFE%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9895u2ETjhHRzEk5EkD%2Fc1E6g0kKzt95mTxnGg7iQFQIhAL5GT2jEjMS%2BBN9HceUU8s8fGGK1aRfqJ8DVfXhL%2BuHhKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG4FUoS0JNC%2BXT1Vgq3AMraNTh8Xcq2cOl8Y%2F05%2BJLY4sKN8GK74b%2BmqYTnmcDT3SMo7njh7bsqDUYJt4KN3Aye9Pvpajn%2BPR3HTqaqe436lsgv7L6JmTEo7YbbarmGHocc2O99ISAIxhLyadVeZNHJql1ogwv%2FNK3L15q3UbipQ0rUX0hKsDkOMGTfNmRNUD5%2FtX1eiBdHBorSiNte%2Fm2KsmIvjJNanP59peLdsCgQ%2FjbNnwJo6WYbA66XX4GfiAmQvCCBGWiSybM34oLRBVSd3FzNDm7AK6%2BumKEKX8%2B9v7J5v%2Bwpk94CI8JPAjsWFwH6UIsgkFepAPqkqLe8QSX6aQxwtkD5r%2FRKzTw6l%2FYWCnSe2gI37pH83Ye3a4zkeWjN5AQ2lcSC9Y%2Fx%2FGaj%2FYQIIgelNmOmLpV0%2BxD51qJ4bCTaWZL1JP%2FFYADEsrGM0Ok68D%2BeMPmhh3dkcyFd5OOTUoR6BhOau27mKTKyOmz6pA6jbf%2B%2FK0QmWkAsm5BNKJJNy34mddF2%2BNAZmD6KT7pD%2FdeD7Dp9xlNiZQn6%2F7najG4sFqwE6lcv6L0L09uOVgQPw1zk2LKzCOwZj3LeRw8es7nSi0i%2BXWt0vEzo76Ge7r9Net%2FubHN6AW66DVZxj4AorXxuQrwYpsi6DCs8a%2FIBjqkAa%2BJS0tV1JySNvP9ak%2BsK2%2FKBF0Zn%2Bhoz4EklkMSZA5OG3r%2Bf4ghghjNNbQfYltvphdwMDWps3Knffp%2BonMOjYKVzlKCbHNOKinqBy2vHr9PYNcP0rEx%2BSUnS7IaqDGs8fC1yweSgZufwM084ZJgwTdQd%2FLugyr4myU8MP0gWuJ2MDkb%2B%2F5SKkfNlRXvwp0pQ1WpKgzd8B64fF5ZqrDkqjEBpWDX&X-Amz-Signature=9307ff8ff87dfaf335d888df1b511ac525fdaad32d8b4a3590669c621e4cb47d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

