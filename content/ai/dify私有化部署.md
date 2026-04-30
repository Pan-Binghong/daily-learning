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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPM7OFB%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCS0BIzVtaKAOoxjjOIrKWeBd%2BTPOlCoTHQKegYjOiFjgIhAPteAFbABsyxFiJZWca%2Bu0DLFVpmHNCOEz5PhrW3%2B5HfKv8DCAkQABoMNjM3NDIzMTgzODA1IgxootMJo2J6x0SMNYwq3AMhwIqu8M%2BC8o2XdO6dqxdG5UWhI2huGzStlL%2FP36kp4f3y8ZAQwnzt8clH6Xbv6WOxMQGcaN8l96DBfaMWYA6iQ1Zpm8kEC3EPqKS6RqVuMiuZCmJP2RziHhCOQJO54g4jK7ijF3O5IWJyjk6qc0qTjfXlvHjgMmp7tBo3FZTlThB4jdTF9rmOfu5m9OI670vJhH7IGWJfwwHOYeEwPB3E1WqiNaG%2FhPPFtKbOMpKiVrv7SM3xwjjfYnRY4x8j7PROEhyaZ380CQGOMVAmjzBB26q%2BbGfxpWdKHwTBBhRQLVhPFCJlF9W7uG3t7M0MqVXOOnKLqsbhGN%2BsOFs9dha0ULgsL3mPZAa6cbH%2FZQnramv7RPNF%2BFetjKFGgU918Qf6HQBysLbkgF85QB%2FST%2F%2F3xVhPqlGHXWj%2BTTqQYTqUISGFCJ87uHmRQfM2NzL1w9xBbDkmdPgphxCyX1GPD9NI1LPOSGVtyor6Pue2xQBwv53%2FapbZqmJhIR%2BVZ374AZpnyb5qNOPkvO3tQvUK2w2zbEhFkgeutXLLXu%2BWv%2BpwxCTq%2Fb9wk7krTqEJwe2MA%2BNLs55pcpuqsLKkUAzYxZThcA3ImzeZLwjGMX3JVjpx8J4hC41x2q0ByF1QKDDKnMzPBjqkAeuScRfg4fB9iuzQ2HBO4XfpLKH38%2FOQWk%2BWFyI72gMtDSuRMtoavz5WpoKzBKB9Ez4MItgSYuKchMfuQcrPmllzQM6UcUar2RDS1MBnu6MjQrrXztfR%2BE0Sbifa4VMJjc6rFSLWCeWbjLQ%2FwzVeYj7lVzM0XpWx4hyI6eeXsDlyOpAPw8hzQwbh5U%2B%2B7ymowpnBdpi%2FkU5Zu2Le7yHSSGA2wLq%2F&X-Amz-Signature=73343671e279fd9d0fb54ceb5f20c67a6e3ae8e154e12b6eddd877b1fb407acd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPM7OFB%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCS0BIzVtaKAOoxjjOIrKWeBd%2BTPOlCoTHQKegYjOiFjgIhAPteAFbABsyxFiJZWca%2Bu0DLFVpmHNCOEz5PhrW3%2B5HfKv8DCAkQABoMNjM3NDIzMTgzODA1IgxootMJo2J6x0SMNYwq3AMhwIqu8M%2BC8o2XdO6dqxdG5UWhI2huGzStlL%2FP36kp4f3y8ZAQwnzt8clH6Xbv6WOxMQGcaN8l96DBfaMWYA6iQ1Zpm8kEC3EPqKS6RqVuMiuZCmJP2RziHhCOQJO54g4jK7ijF3O5IWJyjk6qc0qTjfXlvHjgMmp7tBo3FZTlThB4jdTF9rmOfu5m9OI670vJhH7IGWJfwwHOYeEwPB3E1WqiNaG%2FhPPFtKbOMpKiVrv7SM3xwjjfYnRY4x8j7PROEhyaZ380CQGOMVAmjzBB26q%2BbGfxpWdKHwTBBhRQLVhPFCJlF9W7uG3t7M0MqVXOOnKLqsbhGN%2BsOFs9dha0ULgsL3mPZAa6cbH%2FZQnramv7RPNF%2BFetjKFGgU918Qf6HQBysLbkgF85QB%2FST%2F%2F3xVhPqlGHXWj%2BTTqQYTqUISGFCJ87uHmRQfM2NzL1w9xBbDkmdPgphxCyX1GPD9NI1LPOSGVtyor6Pue2xQBwv53%2FapbZqmJhIR%2BVZ374AZpnyb5qNOPkvO3tQvUK2w2zbEhFkgeutXLLXu%2BWv%2BpwxCTq%2Fb9wk7krTqEJwe2MA%2BNLs55pcpuqsLKkUAzYxZThcA3ImzeZLwjGMX3JVjpx8J4hC41x2q0ByF1QKDDKnMzPBjqkAeuScRfg4fB9iuzQ2HBO4XfpLKH38%2FOQWk%2BWFyI72gMtDSuRMtoavz5WpoKzBKB9Ez4MItgSYuKchMfuQcrPmllzQM6UcUar2RDS1MBnu6MjQrrXztfR%2BE0Sbifa4VMJjc6rFSLWCeWbjLQ%2FwzVeYj7lVzM0XpWx4hyI6eeXsDlyOpAPw8hzQwbh5U%2B%2B7ymowpnBdpi%2FkU5Zu2Le7yHSSGA2wLq%2F&X-Amz-Signature=6ab41790f47373b1b518f182a6bdbda246d5b92cbb372d026498c7ad67dc871c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPM7OFB%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCS0BIzVtaKAOoxjjOIrKWeBd%2BTPOlCoTHQKegYjOiFjgIhAPteAFbABsyxFiJZWca%2Bu0DLFVpmHNCOEz5PhrW3%2B5HfKv8DCAkQABoMNjM3NDIzMTgzODA1IgxootMJo2J6x0SMNYwq3AMhwIqu8M%2BC8o2XdO6dqxdG5UWhI2huGzStlL%2FP36kp4f3y8ZAQwnzt8clH6Xbv6WOxMQGcaN8l96DBfaMWYA6iQ1Zpm8kEC3EPqKS6RqVuMiuZCmJP2RziHhCOQJO54g4jK7ijF3O5IWJyjk6qc0qTjfXlvHjgMmp7tBo3FZTlThB4jdTF9rmOfu5m9OI670vJhH7IGWJfwwHOYeEwPB3E1WqiNaG%2FhPPFtKbOMpKiVrv7SM3xwjjfYnRY4x8j7PROEhyaZ380CQGOMVAmjzBB26q%2BbGfxpWdKHwTBBhRQLVhPFCJlF9W7uG3t7M0MqVXOOnKLqsbhGN%2BsOFs9dha0ULgsL3mPZAa6cbH%2FZQnramv7RPNF%2BFetjKFGgU918Qf6HQBysLbkgF85QB%2FST%2F%2F3xVhPqlGHXWj%2BTTqQYTqUISGFCJ87uHmRQfM2NzL1w9xBbDkmdPgphxCyX1GPD9NI1LPOSGVtyor6Pue2xQBwv53%2FapbZqmJhIR%2BVZ374AZpnyb5qNOPkvO3tQvUK2w2zbEhFkgeutXLLXu%2BWv%2BpwxCTq%2Fb9wk7krTqEJwe2MA%2BNLs55pcpuqsLKkUAzYxZThcA3ImzeZLwjGMX3JVjpx8J4hC41x2q0ByF1QKDDKnMzPBjqkAeuScRfg4fB9iuzQ2HBO4XfpLKH38%2FOQWk%2BWFyI72gMtDSuRMtoavz5WpoKzBKB9Ez4MItgSYuKchMfuQcrPmllzQM6UcUar2RDS1MBnu6MjQrrXztfR%2BE0Sbifa4VMJjc6rFSLWCeWbjLQ%2FwzVeYj7lVzM0XpWx4hyI6eeXsDlyOpAPw8hzQwbh5U%2B%2B7ymowpnBdpi%2FkU5Zu2Le7yHSSGA2wLq%2F&X-Amz-Signature=e0b9e50d95bd2ebac4e96d5328cfb0b3a5b52c696ecc73d5f140809f6dfe651c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPM7OFB%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCS0BIzVtaKAOoxjjOIrKWeBd%2BTPOlCoTHQKegYjOiFjgIhAPteAFbABsyxFiJZWca%2Bu0DLFVpmHNCOEz5PhrW3%2B5HfKv8DCAkQABoMNjM3NDIzMTgzODA1IgxootMJo2J6x0SMNYwq3AMhwIqu8M%2BC8o2XdO6dqxdG5UWhI2huGzStlL%2FP36kp4f3y8ZAQwnzt8clH6Xbv6WOxMQGcaN8l96DBfaMWYA6iQ1Zpm8kEC3EPqKS6RqVuMiuZCmJP2RziHhCOQJO54g4jK7ijF3O5IWJyjk6qc0qTjfXlvHjgMmp7tBo3FZTlThB4jdTF9rmOfu5m9OI670vJhH7IGWJfwwHOYeEwPB3E1WqiNaG%2FhPPFtKbOMpKiVrv7SM3xwjjfYnRY4x8j7PROEhyaZ380CQGOMVAmjzBB26q%2BbGfxpWdKHwTBBhRQLVhPFCJlF9W7uG3t7M0MqVXOOnKLqsbhGN%2BsOFs9dha0ULgsL3mPZAa6cbH%2FZQnramv7RPNF%2BFetjKFGgU918Qf6HQBysLbkgF85QB%2FST%2F%2F3xVhPqlGHXWj%2BTTqQYTqUISGFCJ87uHmRQfM2NzL1w9xBbDkmdPgphxCyX1GPD9NI1LPOSGVtyor6Pue2xQBwv53%2FapbZqmJhIR%2BVZ374AZpnyb5qNOPkvO3tQvUK2w2zbEhFkgeutXLLXu%2BWv%2BpwxCTq%2Fb9wk7krTqEJwe2MA%2BNLs55pcpuqsLKkUAzYxZThcA3ImzeZLwjGMX3JVjpx8J4hC41x2q0ByF1QKDDKnMzPBjqkAeuScRfg4fB9iuzQ2HBO4XfpLKH38%2FOQWk%2BWFyI72gMtDSuRMtoavz5WpoKzBKB9Ez4MItgSYuKchMfuQcrPmllzQM6UcUar2RDS1MBnu6MjQrrXztfR%2BE0Sbifa4VMJjc6rFSLWCeWbjLQ%2FwzVeYj7lVzM0XpWx4hyI6eeXsDlyOpAPw8hzQwbh5U%2B%2B7ymowpnBdpi%2FkU5Zu2Le7yHSSGA2wLq%2F&X-Amz-Signature=912e63ad37cab6b8787411c41ded06db4880886684df8e08c205b7a234c6defb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPM7OFB%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCS0BIzVtaKAOoxjjOIrKWeBd%2BTPOlCoTHQKegYjOiFjgIhAPteAFbABsyxFiJZWca%2Bu0DLFVpmHNCOEz5PhrW3%2B5HfKv8DCAkQABoMNjM3NDIzMTgzODA1IgxootMJo2J6x0SMNYwq3AMhwIqu8M%2BC8o2XdO6dqxdG5UWhI2huGzStlL%2FP36kp4f3y8ZAQwnzt8clH6Xbv6WOxMQGcaN8l96DBfaMWYA6iQ1Zpm8kEC3EPqKS6RqVuMiuZCmJP2RziHhCOQJO54g4jK7ijF3O5IWJyjk6qc0qTjfXlvHjgMmp7tBo3FZTlThB4jdTF9rmOfu5m9OI670vJhH7IGWJfwwHOYeEwPB3E1WqiNaG%2FhPPFtKbOMpKiVrv7SM3xwjjfYnRY4x8j7PROEhyaZ380CQGOMVAmjzBB26q%2BbGfxpWdKHwTBBhRQLVhPFCJlF9W7uG3t7M0MqVXOOnKLqsbhGN%2BsOFs9dha0ULgsL3mPZAa6cbH%2FZQnramv7RPNF%2BFetjKFGgU918Qf6HQBysLbkgF85QB%2FST%2F%2F3xVhPqlGHXWj%2BTTqQYTqUISGFCJ87uHmRQfM2NzL1w9xBbDkmdPgphxCyX1GPD9NI1LPOSGVtyor6Pue2xQBwv53%2FapbZqmJhIR%2BVZ374AZpnyb5qNOPkvO3tQvUK2w2zbEhFkgeutXLLXu%2BWv%2BpwxCTq%2Fb9wk7krTqEJwe2MA%2BNLs55pcpuqsLKkUAzYxZThcA3ImzeZLwjGMX3JVjpx8J4hC41x2q0ByF1QKDDKnMzPBjqkAeuScRfg4fB9iuzQ2HBO4XfpLKH38%2FOQWk%2BWFyI72gMtDSuRMtoavz5WpoKzBKB9Ez4MItgSYuKchMfuQcrPmllzQM6UcUar2RDS1MBnu6MjQrrXztfR%2BE0Sbifa4VMJjc6rFSLWCeWbjLQ%2FwzVeYj7lVzM0XpWx4hyI6eeXsDlyOpAPw8hzQwbh5U%2B%2B7ymowpnBdpi%2FkU5Zu2Le7yHSSGA2wLq%2F&X-Amz-Signature=e8618c602dfbe17b48187963375617fffbdb6e5151ad663c4ec14a644c8f6610&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPM7OFB%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCS0BIzVtaKAOoxjjOIrKWeBd%2BTPOlCoTHQKegYjOiFjgIhAPteAFbABsyxFiJZWca%2Bu0DLFVpmHNCOEz5PhrW3%2B5HfKv8DCAkQABoMNjM3NDIzMTgzODA1IgxootMJo2J6x0SMNYwq3AMhwIqu8M%2BC8o2XdO6dqxdG5UWhI2huGzStlL%2FP36kp4f3y8ZAQwnzt8clH6Xbv6WOxMQGcaN8l96DBfaMWYA6iQ1Zpm8kEC3EPqKS6RqVuMiuZCmJP2RziHhCOQJO54g4jK7ijF3O5IWJyjk6qc0qTjfXlvHjgMmp7tBo3FZTlThB4jdTF9rmOfu5m9OI670vJhH7IGWJfwwHOYeEwPB3E1WqiNaG%2FhPPFtKbOMpKiVrv7SM3xwjjfYnRY4x8j7PROEhyaZ380CQGOMVAmjzBB26q%2BbGfxpWdKHwTBBhRQLVhPFCJlF9W7uG3t7M0MqVXOOnKLqsbhGN%2BsOFs9dha0ULgsL3mPZAa6cbH%2FZQnramv7RPNF%2BFetjKFGgU918Qf6HQBysLbkgF85QB%2FST%2F%2F3xVhPqlGHXWj%2BTTqQYTqUISGFCJ87uHmRQfM2NzL1w9xBbDkmdPgphxCyX1GPD9NI1LPOSGVtyor6Pue2xQBwv53%2FapbZqmJhIR%2BVZ374AZpnyb5qNOPkvO3tQvUK2w2zbEhFkgeutXLLXu%2BWv%2BpwxCTq%2Fb9wk7krTqEJwe2MA%2BNLs55pcpuqsLKkUAzYxZThcA3ImzeZLwjGMX3JVjpx8J4hC41x2q0ByF1QKDDKnMzPBjqkAeuScRfg4fB9iuzQ2HBO4XfpLKH38%2FOQWk%2BWFyI72gMtDSuRMtoavz5WpoKzBKB9Ez4MItgSYuKchMfuQcrPmllzQM6UcUar2RDS1MBnu6MjQrrXztfR%2BE0Sbifa4VMJjc6rFSLWCeWbjLQ%2FwzVeYj7lVzM0XpWx4hyI6eeXsDlyOpAPw8hzQwbh5U%2B%2B7ymowpnBdpi%2FkU5Zu2Le7yHSSGA2wLq%2F&X-Amz-Signature=ec66c7b2d6fd5a0f3b36b3e153624e6b37fa6246ee10f8df46e90610dfa36bae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPM7OFB%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCS0BIzVtaKAOoxjjOIrKWeBd%2BTPOlCoTHQKegYjOiFjgIhAPteAFbABsyxFiJZWca%2Bu0DLFVpmHNCOEz5PhrW3%2B5HfKv8DCAkQABoMNjM3NDIzMTgzODA1IgxootMJo2J6x0SMNYwq3AMhwIqu8M%2BC8o2XdO6dqxdG5UWhI2huGzStlL%2FP36kp4f3y8ZAQwnzt8clH6Xbv6WOxMQGcaN8l96DBfaMWYA6iQ1Zpm8kEC3EPqKS6RqVuMiuZCmJP2RziHhCOQJO54g4jK7ijF3O5IWJyjk6qc0qTjfXlvHjgMmp7tBo3FZTlThB4jdTF9rmOfu5m9OI670vJhH7IGWJfwwHOYeEwPB3E1WqiNaG%2FhPPFtKbOMpKiVrv7SM3xwjjfYnRY4x8j7PROEhyaZ380CQGOMVAmjzBB26q%2BbGfxpWdKHwTBBhRQLVhPFCJlF9W7uG3t7M0MqVXOOnKLqsbhGN%2BsOFs9dha0ULgsL3mPZAa6cbH%2FZQnramv7RPNF%2BFetjKFGgU918Qf6HQBysLbkgF85QB%2FST%2F%2F3xVhPqlGHXWj%2BTTqQYTqUISGFCJ87uHmRQfM2NzL1w9xBbDkmdPgphxCyX1GPD9NI1LPOSGVtyor6Pue2xQBwv53%2FapbZqmJhIR%2BVZ374AZpnyb5qNOPkvO3tQvUK2w2zbEhFkgeutXLLXu%2BWv%2BpwxCTq%2Fb9wk7krTqEJwe2MA%2BNLs55pcpuqsLKkUAzYxZThcA3ImzeZLwjGMX3JVjpx8J4hC41x2q0ByF1QKDDKnMzPBjqkAeuScRfg4fB9iuzQ2HBO4XfpLKH38%2FOQWk%2BWFyI72gMtDSuRMtoavz5WpoKzBKB9Ez4MItgSYuKchMfuQcrPmllzQM6UcUar2RDS1MBnu6MjQrrXztfR%2BE0Sbifa4VMJjc6rFSLWCeWbjLQ%2FwzVeYj7lVzM0XpWx4hyI6eeXsDlyOpAPw8hzQwbh5U%2B%2B7ymowpnBdpi%2FkU5Zu2Le7yHSSGA2wLq%2F&X-Amz-Signature=15905660022ed567d428be7ae65f16baec46f4bf64978af706efa8b2924d2e7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPM7OFB%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCS0BIzVtaKAOoxjjOIrKWeBd%2BTPOlCoTHQKegYjOiFjgIhAPteAFbABsyxFiJZWca%2Bu0DLFVpmHNCOEz5PhrW3%2B5HfKv8DCAkQABoMNjM3NDIzMTgzODA1IgxootMJo2J6x0SMNYwq3AMhwIqu8M%2BC8o2XdO6dqxdG5UWhI2huGzStlL%2FP36kp4f3y8ZAQwnzt8clH6Xbv6WOxMQGcaN8l96DBfaMWYA6iQ1Zpm8kEC3EPqKS6RqVuMiuZCmJP2RziHhCOQJO54g4jK7ijF3O5IWJyjk6qc0qTjfXlvHjgMmp7tBo3FZTlThB4jdTF9rmOfu5m9OI670vJhH7IGWJfwwHOYeEwPB3E1WqiNaG%2FhPPFtKbOMpKiVrv7SM3xwjjfYnRY4x8j7PROEhyaZ380CQGOMVAmjzBB26q%2BbGfxpWdKHwTBBhRQLVhPFCJlF9W7uG3t7M0MqVXOOnKLqsbhGN%2BsOFs9dha0ULgsL3mPZAa6cbH%2FZQnramv7RPNF%2BFetjKFGgU918Qf6HQBysLbkgF85QB%2FST%2F%2F3xVhPqlGHXWj%2BTTqQYTqUISGFCJ87uHmRQfM2NzL1w9xBbDkmdPgphxCyX1GPD9NI1LPOSGVtyor6Pue2xQBwv53%2FapbZqmJhIR%2BVZ374AZpnyb5qNOPkvO3tQvUK2w2zbEhFkgeutXLLXu%2BWv%2BpwxCTq%2Fb9wk7krTqEJwe2MA%2BNLs55pcpuqsLKkUAzYxZThcA3ImzeZLwjGMX3JVjpx8J4hC41x2q0ByF1QKDDKnMzPBjqkAeuScRfg4fB9iuzQ2HBO4XfpLKH38%2FOQWk%2BWFyI72gMtDSuRMtoavz5WpoKzBKB9Ez4MItgSYuKchMfuQcrPmllzQM6UcUar2RDS1MBnu6MjQrrXztfR%2BE0Sbifa4VMJjc6rFSLWCeWbjLQ%2FwzVeYj7lVzM0XpWx4hyI6eeXsDlyOpAPw8hzQwbh5U%2B%2B7ymowpnBdpi%2FkU5Zu2Le7yHSSGA2wLq%2F&X-Amz-Signature=9bc93958c212da87b753a69e65d3073829d57a67ac9bc40bf2ec78a7230af40a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPM7OFB%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCS0BIzVtaKAOoxjjOIrKWeBd%2BTPOlCoTHQKegYjOiFjgIhAPteAFbABsyxFiJZWca%2Bu0DLFVpmHNCOEz5PhrW3%2B5HfKv8DCAkQABoMNjM3NDIzMTgzODA1IgxootMJo2J6x0SMNYwq3AMhwIqu8M%2BC8o2XdO6dqxdG5UWhI2huGzStlL%2FP36kp4f3y8ZAQwnzt8clH6Xbv6WOxMQGcaN8l96DBfaMWYA6iQ1Zpm8kEC3EPqKS6RqVuMiuZCmJP2RziHhCOQJO54g4jK7ijF3O5IWJyjk6qc0qTjfXlvHjgMmp7tBo3FZTlThB4jdTF9rmOfu5m9OI670vJhH7IGWJfwwHOYeEwPB3E1WqiNaG%2FhPPFtKbOMpKiVrv7SM3xwjjfYnRY4x8j7PROEhyaZ380CQGOMVAmjzBB26q%2BbGfxpWdKHwTBBhRQLVhPFCJlF9W7uG3t7M0MqVXOOnKLqsbhGN%2BsOFs9dha0ULgsL3mPZAa6cbH%2FZQnramv7RPNF%2BFetjKFGgU918Qf6HQBysLbkgF85QB%2FST%2F%2F3xVhPqlGHXWj%2BTTqQYTqUISGFCJ87uHmRQfM2NzL1w9xBbDkmdPgphxCyX1GPD9NI1LPOSGVtyor6Pue2xQBwv53%2FapbZqmJhIR%2BVZ374AZpnyb5qNOPkvO3tQvUK2w2zbEhFkgeutXLLXu%2BWv%2BpwxCTq%2Fb9wk7krTqEJwe2MA%2BNLs55pcpuqsLKkUAzYxZThcA3ImzeZLwjGMX3JVjpx8J4hC41x2q0ByF1QKDDKnMzPBjqkAeuScRfg4fB9iuzQ2HBO4XfpLKH38%2FOQWk%2BWFyI72gMtDSuRMtoavz5WpoKzBKB9Ez4MItgSYuKchMfuQcrPmllzQM6UcUar2RDS1MBnu6MjQrrXztfR%2BE0Sbifa4VMJjc6rFSLWCeWbjLQ%2FwzVeYj7lVzM0XpWx4hyI6eeXsDlyOpAPw8hzQwbh5U%2B%2B7ymowpnBdpi%2FkU5Zu2Le7yHSSGA2wLq%2F&X-Amz-Signature=6c182d7e27c11a2abdf8990cff8179772614592a80f5f4c83593a092995d230a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPM7OFB%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCS0BIzVtaKAOoxjjOIrKWeBd%2BTPOlCoTHQKegYjOiFjgIhAPteAFbABsyxFiJZWca%2Bu0DLFVpmHNCOEz5PhrW3%2B5HfKv8DCAkQABoMNjM3NDIzMTgzODA1IgxootMJo2J6x0SMNYwq3AMhwIqu8M%2BC8o2XdO6dqxdG5UWhI2huGzStlL%2FP36kp4f3y8ZAQwnzt8clH6Xbv6WOxMQGcaN8l96DBfaMWYA6iQ1Zpm8kEC3EPqKS6RqVuMiuZCmJP2RziHhCOQJO54g4jK7ijF3O5IWJyjk6qc0qTjfXlvHjgMmp7tBo3FZTlThB4jdTF9rmOfu5m9OI670vJhH7IGWJfwwHOYeEwPB3E1WqiNaG%2FhPPFtKbOMpKiVrv7SM3xwjjfYnRY4x8j7PROEhyaZ380CQGOMVAmjzBB26q%2BbGfxpWdKHwTBBhRQLVhPFCJlF9W7uG3t7M0MqVXOOnKLqsbhGN%2BsOFs9dha0ULgsL3mPZAa6cbH%2FZQnramv7RPNF%2BFetjKFGgU918Qf6HQBysLbkgF85QB%2FST%2F%2F3xVhPqlGHXWj%2BTTqQYTqUISGFCJ87uHmRQfM2NzL1w9xBbDkmdPgphxCyX1GPD9NI1LPOSGVtyor6Pue2xQBwv53%2FapbZqmJhIR%2BVZ374AZpnyb5qNOPkvO3tQvUK2w2zbEhFkgeutXLLXu%2BWv%2BpwxCTq%2Fb9wk7krTqEJwe2MA%2BNLs55pcpuqsLKkUAzYxZThcA3ImzeZLwjGMX3JVjpx8J4hC41x2q0ByF1QKDDKnMzPBjqkAeuScRfg4fB9iuzQ2HBO4XfpLKH38%2FOQWk%2BWFyI72gMtDSuRMtoavz5WpoKzBKB9Ez4MItgSYuKchMfuQcrPmllzQM6UcUar2RDS1MBnu6MjQrrXztfR%2BE0Sbifa4VMJjc6rFSLWCeWbjLQ%2FwzVeYj7lVzM0XpWx4hyI6eeXsDlyOpAPw8hzQwbh5U%2B%2B7ymowpnBdpi%2FkU5Zu2Le7yHSSGA2wLq%2F&X-Amz-Signature=dc407e82d79ba0e10dc1e5c0d84f7229df3a082e748574e3b567caebfad65a7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

