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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3H746C%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2aoPr6ZrRm1VYl%2BToyR86kbDjvb%2BN6o6jV6%2F38jy9QwIhAJu%2BQtajdTzMzyXwWti5v8DC3jSuOwOJQbr8UELmABxpKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyglhVKYHeXlhmHf5Qq3AOAmJQHmJS5aCaYLGprJWotoFA53LUdK%2FTvAazrlZpDaLy1wZBFc0PSEhbKW8OwSi1k%2FnIcuwtL8lsJiltsmbz%2BNQp4dbAu%2FMIbn7JI17dy2Sbz52E0SGjYl%2BmWwAz2XtG8tn2QwpgqhFJjN6CNPg8bvBH1rMz0pLhahLLGeDvWErZAHwqwzJz%2FQB%2BeEMM0N%2FyWo2vxLRmnjItg3k7fysf98CufTzcu20ZP1VDMDDYIf%2BE78sCM2wBaFYEzBcz%2FvoTqZMLN9GP%2BF%2FMOgol7SyDYT%2Fy7ZtdO5wA7GI0NpjSqz3WbcvxTDV7WuaN9%2BE%2F9cTOsax4Cmr1Pac%2FZe8X9ekgUIDT7WNMl0ElQo0BttgIW%2BMlCtOFEpVv6RW7KMNbTwuPsbyTml133e4PF4bI8jaWJHA%2F5TAHyBQVpILqATlVjrNTwKZDiPu%2Fnp8rby%2BPzd4tODHS%2Fmqfszr8MJws8xpiIliyRT9QbgH655w17GUu6ZHX%2FHxljTc1JGN4ij7uEB09eWsnII2jZDxcP7X1Yh3RJnNDGY5mZnE%2BXByGpMJg0W2cC5Au71EJHzpMFABVEXK%2Fy8L0WATPD98AqYTzLVL8lwOyOIuNLDnrJ0Y3N%2BTZ7nCfF2YDA9KHA5EElJDCT457JBjqkAZ5Mfplfqh%2BR8t9tdIhw5xQg6Fq7is78Qdk9yez2lRGNl4zk74A5fd2PZycbOl978RnVXFgdIPEvDRPWnYpU%2FkoheBPboW2vE0sZv%2BGBtkDeEHxytqD92n9XCX30%2BvYi20l%2FHuwB1FzKKQ30BA%2FMBz51%2BC9RP6GpBhUuJD2160q%2FjWSVUjGSCkaYb1KdjfgSZTco%2B0CRxSMJew1S6q%2FKuO2oM4t3&X-Amz-Signature=155d075bf8d0f238cf78352d19234ef73e1e8f66ff50f7ebd8d046ce1553eac9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3H746C%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2aoPr6ZrRm1VYl%2BToyR86kbDjvb%2BN6o6jV6%2F38jy9QwIhAJu%2BQtajdTzMzyXwWti5v8DC3jSuOwOJQbr8UELmABxpKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyglhVKYHeXlhmHf5Qq3AOAmJQHmJS5aCaYLGprJWotoFA53LUdK%2FTvAazrlZpDaLy1wZBFc0PSEhbKW8OwSi1k%2FnIcuwtL8lsJiltsmbz%2BNQp4dbAu%2FMIbn7JI17dy2Sbz52E0SGjYl%2BmWwAz2XtG8tn2QwpgqhFJjN6CNPg8bvBH1rMz0pLhahLLGeDvWErZAHwqwzJz%2FQB%2BeEMM0N%2FyWo2vxLRmnjItg3k7fysf98CufTzcu20ZP1VDMDDYIf%2BE78sCM2wBaFYEzBcz%2FvoTqZMLN9GP%2BF%2FMOgol7SyDYT%2Fy7ZtdO5wA7GI0NpjSqz3WbcvxTDV7WuaN9%2BE%2F9cTOsax4Cmr1Pac%2FZe8X9ekgUIDT7WNMl0ElQo0BttgIW%2BMlCtOFEpVv6RW7KMNbTwuPsbyTml133e4PF4bI8jaWJHA%2F5TAHyBQVpILqATlVjrNTwKZDiPu%2Fnp8rby%2BPzd4tODHS%2Fmqfszr8MJws8xpiIliyRT9QbgH655w17GUu6ZHX%2FHxljTc1JGN4ij7uEB09eWsnII2jZDxcP7X1Yh3RJnNDGY5mZnE%2BXByGpMJg0W2cC5Au71EJHzpMFABVEXK%2Fy8L0WATPD98AqYTzLVL8lwOyOIuNLDnrJ0Y3N%2BTZ7nCfF2YDA9KHA5EElJDCT457JBjqkAZ5Mfplfqh%2BR8t9tdIhw5xQg6Fq7is78Qdk9yez2lRGNl4zk74A5fd2PZycbOl978RnVXFgdIPEvDRPWnYpU%2FkoheBPboW2vE0sZv%2BGBtkDeEHxytqD92n9XCX30%2BvYi20l%2FHuwB1FzKKQ30BA%2FMBz51%2BC9RP6GpBhUuJD2160q%2FjWSVUjGSCkaYb1KdjfgSZTco%2B0CRxSMJew1S6q%2FKuO2oM4t3&X-Amz-Signature=d9a4571b12e3d476e6ccaddfb4038a93b9a80b1a24c7f9faf3188df4c58d79bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3H746C%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2aoPr6ZrRm1VYl%2BToyR86kbDjvb%2BN6o6jV6%2F38jy9QwIhAJu%2BQtajdTzMzyXwWti5v8DC3jSuOwOJQbr8UELmABxpKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyglhVKYHeXlhmHf5Qq3AOAmJQHmJS5aCaYLGprJWotoFA53LUdK%2FTvAazrlZpDaLy1wZBFc0PSEhbKW8OwSi1k%2FnIcuwtL8lsJiltsmbz%2BNQp4dbAu%2FMIbn7JI17dy2Sbz52E0SGjYl%2BmWwAz2XtG8tn2QwpgqhFJjN6CNPg8bvBH1rMz0pLhahLLGeDvWErZAHwqwzJz%2FQB%2BeEMM0N%2FyWo2vxLRmnjItg3k7fysf98CufTzcu20ZP1VDMDDYIf%2BE78sCM2wBaFYEzBcz%2FvoTqZMLN9GP%2BF%2FMOgol7SyDYT%2Fy7ZtdO5wA7GI0NpjSqz3WbcvxTDV7WuaN9%2BE%2F9cTOsax4Cmr1Pac%2FZe8X9ekgUIDT7WNMl0ElQo0BttgIW%2BMlCtOFEpVv6RW7KMNbTwuPsbyTml133e4PF4bI8jaWJHA%2F5TAHyBQVpILqATlVjrNTwKZDiPu%2Fnp8rby%2BPzd4tODHS%2Fmqfszr8MJws8xpiIliyRT9QbgH655w17GUu6ZHX%2FHxljTc1JGN4ij7uEB09eWsnII2jZDxcP7X1Yh3RJnNDGY5mZnE%2BXByGpMJg0W2cC5Au71EJHzpMFABVEXK%2Fy8L0WATPD98AqYTzLVL8lwOyOIuNLDnrJ0Y3N%2BTZ7nCfF2YDA9KHA5EElJDCT457JBjqkAZ5Mfplfqh%2BR8t9tdIhw5xQg6Fq7is78Qdk9yez2lRGNl4zk74A5fd2PZycbOl978RnVXFgdIPEvDRPWnYpU%2FkoheBPboW2vE0sZv%2BGBtkDeEHxytqD92n9XCX30%2BvYi20l%2FHuwB1FzKKQ30BA%2FMBz51%2BC9RP6GpBhUuJD2160q%2FjWSVUjGSCkaYb1KdjfgSZTco%2B0CRxSMJew1S6q%2FKuO2oM4t3&X-Amz-Signature=3c7b6b1e334b10b1209a9a3dcd77ce2be8a3ea8a7513b02e443c7401c221a7f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3H746C%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2aoPr6ZrRm1VYl%2BToyR86kbDjvb%2BN6o6jV6%2F38jy9QwIhAJu%2BQtajdTzMzyXwWti5v8DC3jSuOwOJQbr8UELmABxpKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyglhVKYHeXlhmHf5Qq3AOAmJQHmJS5aCaYLGprJWotoFA53LUdK%2FTvAazrlZpDaLy1wZBFc0PSEhbKW8OwSi1k%2FnIcuwtL8lsJiltsmbz%2BNQp4dbAu%2FMIbn7JI17dy2Sbz52E0SGjYl%2BmWwAz2XtG8tn2QwpgqhFJjN6CNPg8bvBH1rMz0pLhahLLGeDvWErZAHwqwzJz%2FQB%2BeEMM0N%2FyWo2vxLRmnjItg3k7fysf98CufTzcu20ZP1VDMDDYIf%2BE78sCM2wBaFYEzBcz%2FvoTqZMLN9GP%2BF%2FMOgol7SyDYT%2Fy7ZtdO5wA7GI0NpjSqz3WbcvxTDV7WuaN9%2BE%2F9cTOsax4Cmr1Pac%2FZe8X9ekgUIDT7WNMl0ElQo0BttgIW%2BMlCtOFEpVv6RW7KMNbTwuPsbyTml133e4PF4bI8jaWJHA%2F5TAHyBQVpILqATlVjrNTwKZDiPu%2Fnp8rby%2BPzd4tODHS%2Fmqfszr8MJws8xpiIliyRT9QbgH655w17GUu6ZHX%2FHxljTc1JGN4ij7uEB09eWsnII2jZDxcP7X1Yh3RJnNDGY5mZnE%2BXByGpMJg0W2cC5Au71EJHzpMFABVEXK%2Fy8L0WATPD98AqYTzLVL8lwOyOIuNLDnrJ0Y3N%2BTZ7nCfF2YDA9KHA5EElJDCT457JBjqkAZ5Mfplfqh%2BR8t9tdIhw5xQg6Fq7is78Qdk9yez2lRGNl4zk74A5fd2PZycbOl978RnVXFgdIPEvDRPWnYpU%2FkoheBPboW2vE0sZv%2BGBtkDeEHxytqD92n9XCX30%2BvYi20l%2FHuwB1FzKKQ30BA%2FMBz51%2BC9RP6GpBhUuJD2160q%2FjWSVUjGSCkaYb1KdjfgSZTco%2B0CRxSMJew1S6q%2FKuO2oM4t3&X-Amz-Signature=7760004e783a502a56041960cb385b91afa5fe69922ced265eb6d6a1d18cf0b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3H746C%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2aoPr6ZrRm1VYl%2BToyR86kbDjvb%2BN6o6jV6%2F38jy9QwIhAJu%2BQtajdTzMzyXwWti5v8DC3jSuOwOJQbr8UELmABxpKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyglhVKYHeXlhmHf5Qq3AOAmJQHmJS5aCaYLGprJWotoFA53LUdK%2FTvAazrlZpDaLy1wZBFc0PSEhbKW8OwSi1k%2FnIcuwtL8lsJiltsmbz%2BNQp4dbAu%2FMIbn7JI17dy2Sbz52E0SGjYl%2BmWwAz2XtG8tn2QwpgqhFJjN6CNPg8bvBH1rMz0pLhahLLGeDvWErZAHwqwzJz%2FQB%2BeEMM0N%2FyWo2vxLRmnjItg3k7fysf98CufTzcu20ZP1VDMDDYIf%2BE78sCM2wBaFYEzBcz%2FvoTqZMLN9GP%2BF%2FMOgol7SyDYT%2Fy7ZtdO5wA7GI0NpjSqz3WbcvxTDV7WuaN9%2BE%2F9cTOsax4Cmr1Pac%2FZe8X9ekgUIDT7WNMl0ElQo0BttgIW%2BMlCtOFEpVv6RW7KMNbTwuPsbyTml133e4PF4bI8jaWJHA%2F5TAHyBQVpILqATlVjrNTwKZDiPu%2Fnp8rby%2BPzd4tODHS%2Fmqfszr8MJws8xpiIliyRT9QbgH655w17GUu6ZHX%2FHxljTc1JGN4ij7uEB09eWsnII2jZDxcP7X1Yh3RJnNDGY5mZnE%2BXByGpMJg0W2cC5Au71EJHzpMFABVEXK%2Fy8L0WATPD98AqYTzLVL8lwOyOIuNLDnrJ0Y3N%2BTZ7nCfF2YDA9KHA5EElJDCT457JBjqkAZ5Mfplfqh%2BR8t9tdIhw5xQg6Fq7is78Qdk9yez2lRGNl4zk74A5fd2PZycbOl978RnVXFgdIPEvDRPWnYpU%2FkoheBPboW2vE0sZv%2BGBtkDeEHxytqD92n9XCX30%2BvYi20l%2FHuwB1FzKKQ30BA%2FMBz51%2BC9RP6GpBhUuJD2160q%2FjWSVUjGSCkaYb1KdjfgSZTco%2B0CRxSMJew1S6q%2FKuO2oM4t3&X-Amz-Signature=410730586ad8e8deb63ddab61acf4cd1055df1ee373d10890b00a9067c9af573&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3H746C%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2aoPr6ZrRm1VYl%2BToyR86kbDjvb%2BN6o6jV6%2F38jy9QwIhAJu%2BQtajdTzMzyXwWti5v8DC3jSuOwOJQbr8UELmABxpKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyglhVKYHeXlhmHf5Qq3AOAmJQHmJS5aCaYLGprJWotoFA53LUdK%2FTvAazrlZpDaLy1wZBFc0PSEhbKW8OwSi1k%2FnIcuwtL8lsJiltsmbz%2BNQp4dbAu%2FMIbn7JI17dy2Sbz52E0SGjYl%2BmWwAz2XtG8tn2QwpgqhFJjN6CNPg8bvBH1rMz0pLhahLLGeDvWErZAHwqwzJz%2FQB%2BeEMM0N%2FyWo2vxLRmnjItg3k7fysf98CufTzcu20ZP1VDMDDYIf%2BE78sCM2wBaFYEzBcz%2FvoTqZMLN9GP%2BF%2FMOgol7SyDYT%2Fy7ZtdO5wA7GI0NpjSqz3WbcvxTDV7WuaN9%2BE%2F9cTOsax4Cmr1Pac%2FZe8X9ekgUIDT7WNMl0ElQo0BttgIW%2BMlCtOFEpVv6RW7KMNbTwuPsbyTml133e4PF4bI8jaWJHA%2F5TAHyBQVpILqATlVjrNTwKZDiPu%2Fnp8rby%2BPzd4tODHS%2Fmqfszr8MJws8xpiIliyRT9QbgH655w17GUu6ZHX%2FHxljTc1JGN4ij7uEB09eWsnII2jZDxcP7X1Yh3RJnNDGY5mZnE%2BXByGpMJg0W2cC5Au71EJHzpMFABVEXK%2Fy8L0WATPD98AqYTzLVL8lwOyOIuNLDnrJ0Y3N%2BTZ7nCfF2YDA9KHA5EElJDCT457JBjqkAZ5Mfplfqh%2BR8t9tdIhw5xQg6Fq7is78Qdk9yez2lRGNl4zk74A5fd2PZycbOl978RnVXFgdIPEvDRPWnYpU%2FkoheBPboW2vE0sZv%2BGBtkDeEHxytqD92n9XCX30%2BvYi20l%2FHuwB1FzKKQ30BA%2FMBz51%2BC9RP6GpBhUuJD2160q%2FjWSVUjGSCkaYb1KdjfgSZTco%2B0CRxSMJew1S6q%2FKuO2oM4t3&X-Amz-Signature=46178fbfd71a01d0d7acefaeeea7d38f0eb6ca985d277a8269510f3e45b561cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3H746C%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2aoPr6ZrRm1VYl%2BToyR86kbDjvb%2BN6o6jV6%2F38jy9QwIhAJu%2BQtajdTzMzyXwWti5v8DC3jSuOwOJQbr8UELmABxpKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyglhVKYHeXlhmHf5Qq3AOAmJQHmJS5aCaYLGprJWotoFA53LUdK%2FTvAazrlZpDaLy1wZBFc0PSEhbKW8OwSi1k%2FnIcuwtL8lsJiltsmbz%2BNQp4dbAu%2FMIbn7JI17dy2Sbz52E0SGjYl%2BmWwAz2XtG8tn2QwpgqhFJjN6CNPg8bvBH1rMz0pLhahLLGeDvWErZAHwqwzJz%2FQB%2BeEMM0N%2FyWo2vxLRmnjItg3k7fysf98CufTzcu20ZP1VDMDDYIf%2BE78sCM2wBaFYEzBcz%2FvoTqZMLN9GP%2BF%2FMOgol7SyDYT%2Fy7ZtdO5wA7GI0NpjSqz3WbcvxTDV7WuaN9%2BE%2F9cTOsax4Cmr1Pac%2FZe8X9ekgUIDT7WNMl0ElQo0BttgIW%2BMlCtOFEpVv6RW7KMNbTwuPsbyTml133e4PF4bI8jaWJHA%2F5TAHyBQVpILqATlVjrNTwKZDiPu%2Fnp8rby%2BPzd4tODHS%2Fmqfszr8MJws8xpiIliyRT9QbgH655w17GUu6ZHX%2FHxljTc1JGN4ij7uEB09eWsnII2jZDxcP7X1Yh3RJnNDGY5mZnE%2BXByGpMJg0W2cC5Au71EJHzpMFABVEXK%2Fy8L0WATPD98AqYTzLVL8lwOyOIuNLDnrJ0Y3N%2BTZ7nCfF2YDA9KHA5EElJDCT457JBjqkAZ5Mfplfqh%2BR8t9tdIhw5xQg6Fq7is78Qdk9yez2lRGNl4zk74A5fd2PZycbOl978RnVXFgdIPEvDRPWnYpU%2FkoheBPboW2vE0sZv%2BGBtkDeEHxytqD92n9XCX30%2BvYi20l%2FHuwB1FzKKQ30BA%2FMBz51%2BC9RP6GpBhUuJD2160q%2FjWSVUjGSCkaYb1KdjfgSZTco%2B0CRxSMJew1S6q%2FKuO2oM4t3&X-Amz-Signature=cb063e808c29e9f184ec5908b47172d31fd37cbed7d198d980e285763d51f8b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3H746C%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2aoPr6ZrRm1VYl%2BToyR86kbDjvb%2BN6o6jV6%2F38jy9QwIhAJu%2BQtajdTzMzyXwWti5v8DC3jSuOwOJQbr8UELmABxpKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyglhVKYHeXlhmHf5Qq3AOAmJQHmJS5aCaYLGprJWotoFA53LUdK%2FTvAazrlZpDaLy1wZBFc0PSEhbKW8OwSi1k%2FnIcuwtL8lsJiltsmbz%2BNQp4dbAu%2FMIbn7JI17dy2Sbz52E0SGjYl%2BmWwAz2XtG8tn2QwpgqhFJjN6CNPg8bvBH1rMz0pLhahLLGeDvWErZAHwqwzJz%2FQB%2BeEMM0N%2FyWo2vxLRmnjItg3k7fysf98CufTzcu20ZP1VDMDDYIf%2BE78sCM2wBaFYEzBcz%2FvoTqZMLN9GP%2BF%2FMOgol7SyDYT%2Fy7ZtdO5wA7GI0NpjSqz3WbcvxTDV7WuaN9%2BE%2F9cTOsax4Cmr1Pac%2FZe8X9ekgUIDT7WNMl0ElQo0BttgIW%2BMlCtOFEpVv6RW7KMNbTwuPsbyTml133e4PF4bI8jaWJHA%2F5TAHyBQVpILqATlVjrNTwKZDiPu%2Fnp8rby%2BPzd4tODHS%2Fmqfszr8MJws8xpiIliyRT9QbgH655w17GUu6ZHX%2FHxljTc1JGN4ij7uEB09eWsnII2jZDxcP7X1Yh3RJnNDGY5mZnE%2BXByGpMJg0W2cC5Au71EJHzpMFABVEXK%2Fy8L0WATPD98AqYTzLVL8lwOyOIuNLDnrJ0Y3N%2BTZ7nCfF2YDA9KHA5EElJDCT457JBjqkAZ5Mfplfqh%2BR8t9tdIhw5xQg6Fq7is78Qdk9yez2lRGNl4zk74A5fd2PZycbOl978RnVXFgdIPEvDRPWnYpU%2FkoheBPboW2vE0sZv%2BGBtkDeEHxytqD92n9XCX30%2BvYi20l%2FHuwB1FzKKQ30BA%2FMBz51%2BC9RP6GpBhUuJD2160q%2FjWSVUjGSCkaYb1KdjfgSZTco%2B0CRxSMJew1S6q%2FKuO2oM4t3&X-Amz-Signature=2e4396969ce95d798f84a39eb078c6783c126695361174563915b6e415822368&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3H746C%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2aoPr6ZrRm1VYl%2BToyR86kbDjvb%2BN6o6jV6%2F38jy9QwIhAJu%2BQtajdTzMzyXwWti5v8DC3jSuOwOJQbr8UELmABxpKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyglhVKYHeXlhmHf5Qq3AOAmJQHmJS5aCaYLGprJWotoFA53LUdK%2FTvAazrlZpDaLy1wZBFc0PSEhbKW8OwSi1k%2FnIcuwtL8lsJiltsmbz%2BNQp4dbAu%2FMIbn7JI17dy2Sbz52E0SGjYl%2BmWwAz2XtG8tn2QwpgqhFJjN6CNPg8bvBH1rMz0pLhahLLGeDvWErZAHwqwzJz%2FQB%2BeEMM0N%2FyWo2vxLRmnjItg3k7fysf98CufTzcu20ZP1VDMDDYIf%2BE78sCM2wBaFYEzBcz%2FvoTqZMLN9GP%2BF%2FMOgol7SyDYT%2Fy7ZtdO5wA7GI0NpjSqz3WbcvxTDV7WuaN9%2BE%2F9cTOsax4Cmr1Pac%2FZe8X9ekgUIDT7WNMl0ElQo0BttgIW%2BMlCtOFEpVv6RW7KMNbTwuPsbyTml133e4PF4bI8jaWJHA%2F5TAHyBQVpILqATlVjrNTwKZDiPu%2Fnp8rby%2BPzd4tODHS%2Fmqfszr8MJws8xpiIliyRT9QbgH655w17GUu6ZHX%2FHxljTc1JGN4ij7uEB09eWsnII2jZDxcP7X1Yh3RJnNDGY5mZnE%2BXByGpMJg0W2cC5Au71EJHzpMFABVEXK%2Fy8L0WATPD98AqYTzLVL8lwOyOIuNLDnrJ0Y3N%2BTZ7nCfF2YDA9KHA5EElJDCT457JBjqkAZ5Mfplfqh%2BR8t9tdIhw5xQg6Fq7is78Qdk9yez2lRGNl4zk74A5fd2PZycbOl978RnVXFgdIPEvDRPWnYpU%2FkoheBPboW2vE0sZv%2BGBtkDeEHxytqD92n9XCX30%2BvYi20l%2FHuwB1FzKKQ30BA%2FMBz51%2BC9RP6GpBhUuJD2160q%2FjWSVUjGSCkaYb1KdjfgSZTco%2B0CRxSMJew1S6q%2FKuO2oM4t3&X-Amz-Signature=b746666b073386a367f7814aa5a6ffffd22fc22dd50ce38372e344fbbc02d520&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ3H746C%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2aoPr6ZrRm1VYl%2BToyR86kbDjvb%2BN6o6jV6%2F38jy9QwIhAJu%2BQtajdTzMzyXwWti5v8DC3jSuOwOJQbr8UELmABxpKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyglhVKYHeXlhmHf5Qq3AOAmJQHmJS5aCaYLGprJWotoFA53LUdK%2FTvAazrlZpDaLy1wZBFc0PSEhbKW8OwSi1k%2FnIcuwtL8lsJiltsmbz%2BNQp4dbAu%2FMIbn7JI17dy2Sbz52E0SGjYl%2BmWwAz2XtG8tn2QwpgqhFJjN6CNPg8bvBH1rMz0pLhahLLGeDvWErZAHwqwzJz%2FQB%2BeEMM0N%2FyWo2vxLRmnjItg3k7fysf98CufTzcu20ZP1VDMDDYIf%2BE78sCM2wBaFYEzBcz%2FvoTqZMLN9GP%2BF%2FMOgol7SyDYT%2Fy7ZtdO5wA7GI0NpjSqz3WbcvxTDV7WuaN9%2BE%2F9cTOsax4Cmr1Pac%2FZe8X9ekgUIDT7WNMl0ElQo0BttgIW%2BMlCtOFEpVv6RW7KMNbTwuPsbyTml133e4PF4bI8jaWJHA%2F5TAHyBQVpILqATlVjrNTwKZDiPu%2Fnp8rby%2BPzd4tODHS%2Fmqfszr8MJws8xpiIliyRT9QbgH655w17GUu6ZHX%2FHxljTc1JGN4ij7uEB09eWsnII2jZDxcP7X1Yh3RJnNDGY5mZnE%2BXByGpMJg0W2cC5Au71EJHzpMFABVEXK%2Fy8L0WATPD98AqYTzLVL8lwOyOIuNLDnrJ0Y3N%2BTZ7nCfF2YDA9KHA5EElJDCT457JBjqkAZ5Mfplfqh%2BR8t9tdIhw5xQg6Fq7is78Qdk9yez2lRGNl4zk74A5fd2PZycbOl978RnVXFgdIPEvDRPWnYpU%2FkoheBPboW2vE0sZv%2BGBtkDeEHxytqD92n9XCX30%2BvYi20l%2FHuwB1FzKKQ30BA%2FMBz51%2BC9RP6GpBhUuJD2160q%2FjWSVUjGSCkaYb1KdjfgSZTco%2B0CRxSMJew1S6q%2FKuO2oM4t3&X-Amz-Signature=ba929115ed769ec76a31702f8ace686a6001cfdfd8e7e1a5f31fe990b57aef53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

