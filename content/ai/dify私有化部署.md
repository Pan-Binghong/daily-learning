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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWPOAZC4%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnADMXWD72v7TtV4R2nUfJc4CvQcoBg9JVRH0w5dxilQIhAP2%2F3rJNkfEqlk9uiI%2BWqJvZv8phD0QCsbLSDPmhakGbKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5iFftYQt682JgG%2BQq3AOy5gHJ48Yv3ZVjlDH4uboJOj1LWFLr7L3juxjnzv3RuvfIjjAMH2YMEA%2BgBomwG9rA5wGa29QqlV881Y0ap3IkGGr9ta2aSdrSbu%2BfBGeUr4AOLgjCSsPSKZ2JxcaRsdKnnB8rG6qC%2BpH8PKFjVkTG8peNTZfz8ZyRoK3H2VkBbD56Q5gP55KSWTMNbBE1ESwCn4ZQfYYgz76lfDFuWmYYsGJilEvYNp6J6niA4pIivU4V8ntxYxcrz0lfg5Ran10Rv9JVUr3Jc0BCYjUMoe8hJipW0b9hLuF0cyTSWXNshUr39cPf9Yun1WnGSaa4zUzgGpoXN0TRiw9KAWD3SUrGr5d4lw4X%2FQ5oEBYbGBM22QxD%2FrjwfLeq5ai0ZLIAGK9K0sHBMnSuxZOEXx1vjj9uFdWQUoLSpF45tS46jbqF9oboTG8WhgRcfKhMhZZT9lpOrXQNSM6BWoJ9HgrH0llMelD1NzdAQsfY0ZpD0%2BTKfWh6WNR0hz8xMaP%2BzoxYWu%2B86WBJ95VFrN%2BrB0xOc6ZC73xiRA5zMWGL1G%2F734PZd%2FJ9slc5CQhVzfRe5PFj0RG6iTqxSia0WEWNszKd%2BVsrsBTWBcKnAzp7rBOOwGrahnRDamvuwlUrzqLYKjC1yfDLBjqkAUkslVv4cDiJvScBbtuZ9cnsrN%2Bw6tsR7ZshO0LTfAMoT1DSwkshoTlTY6YZN03RZaJJswhEhPtHRswjV4CYVugPal5XEykJE5v7DJCm0LadTCTQUE5182T6YJCXo%2BQDSVHtJuxfsy1KYJMbl8j33g66Pm7%2B2me6Y%2FJJVUHpvxxVisqnMR2hk1AAq0sQYaHZ0ulgd7G6ri748QvC7dRRpWnkeh6J&X-Amz-Signature=96f34da419502e33ff1f57a1a9a4db30ad059439221d993c9bbbc25101c6aba9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWPOAZC4%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnADMXWD72v7TtV4R2nUfJc4CvQcoBg9JVRH0w5dxilQIhAP2%2F3rJNkfEqlk9uiI%2BWqJvZv8phD0QCsbLSDPmhakGbKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5iFftYQt682JgG%2BQq3AOy5gHJ48Yv3ZVjlDH4uboJOj1LWFLr7L3juxjnzv3RuvfIjjAMH2YMEA%2BgBomwG9rA5wGa29QqlV881Y0ap3IkGGr9ta2aSdrSbu%2BfBGeUr4AOLgjCSsPSKZ2JxcaRsdKnnB8rG6qC%2BpH8PKFjVkTG8peNTZfz8ZyRoK3H2VkBbD56Q5gP55KSWTMNbBE1ESwCn4ZQfYYgz76lfDFuWmYYsGJilEvYNp6J6niA4pIivU4V8ntxYxcrz0lfg5Ran10Rv9JVUr3Jc0BCYjUMoe8hJipW0b9hLuF0cyTSWXNshUr39cPf9Yun1WnGSaa4zUzgGpoXN0TRiw9KAWD3SUrGr5d4lw4X%2FQ5oEBYbGBM22QxD%2FrjwfLeq5ai0ZLIAGK9K0sHBMnSuxZOEXx1vjj9uFdWQUoLSpF45tS46jbqF9oboTG8WhgRcfKhMhZZT9lpOrXQNSM6BWoJ9HgrH0llMelD1NzdAQsfY0ZpD0%2BTKfWh6WNR0hz8xMaP%2BzoxYWu%2B86WBJ95VFrN%2BrB0xOc6ZC73xiRA5zMWGL1G%2F734PZd%2FJ9slc5CQhVzfRe5PFj0RG6iTqxSia0WEWNszKd%2BVsrsBTWBcKnAzp7rBOOwGrahnRDamvuwlUrzqLYKjC1yfDLBjqkAUkslVv4cDiJvScBbtuZ9cnsrN%2Bw6tsR7ZshO0LTfAMoT1DSwkshoTlTY6YZN03RZaJJswhEhPtHRswjV4CYVugPal5XEykJE5v7DJCm0LadTCTQUE5182T6YJCXo%2BQDSVHtJuxfsy1KYJMbl8j33g66Pm7%2B2me6Y%2FJJVUHpvxxVisqnMR2hk1AAq0sQYaHZ0ulgd7G6ri748QvC7dRRpWnkeh6J&X-Amz-Signature=7425893eebd623ebb2ebe8804423a5c1e10de56c71088d99a646af319141988a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWPOAZC4%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnADMXWD72v7TtV4R2nUfJc4CvQcoBg9JVRH0w5dxilQIhAP2%2F3rJNkfEqlk9uiI%2BWqJvZv8phD0QCsbLSDPmhakGbKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5iFftYQt682JgG%2BQq3AOy5gHJ48Yv3ZVjlDH4uboJOj1LWFLr7L3juxjnzv3RuvfIjjAMH2YMEA%2BgBomwG9rA5wGa29QqlV881Y0ap3IkGGr9ta2aSdrSbu%2BfBGeUr4AOLgjCSsPSKZ2JxcaRsdKnnB8rG6qC%2BpH8PKFjVkTG8peNTZfz8ZyRoK3H2VkBbD56Q5gP55KSWTMNbBE1ESwCn4ZQfYYgz76lfDFuWmYYsGJilEvYNp6J6niA4pIivU4V8ntxYxcrz0lfg5Ran10Rv9JVUr3Jc0BCYjUMoe8hJipW0b9hLuF0cyTSWXNshUr39cPf9Yun1WnGSaa4zUzgGpoXN0TRiw9KAWD3SUrGr5d4lw4X%2FQ5oEBYbGBM22QxD%2FrjwfLeq5ai0ZLIAGK9K0sHBMnSuxZOEXx1vjj9uFdWQUoLSpF45tS46jbqF9oboTG8WhgRcfKhMhZZT9lpOrXQNSM6BWoJ9HgrH0llMelD1NzdAQsfY0ZpD0%2BTKfWh6WNR0hz8xMaP%2BzoxYWu%2B86WBJ95VFrN%2BrB0xOc6ZC73xiRA5zMWGL1G%2F734PZd%2FJ9slc5CQhVzfRe5PFj0RG6iTqxSia0WEWNszKd%2BVsrsBTWBcKnAzp7rBOOwGrahnRDamvuwlUrzqLYKjC1yfDLBjqkAUkslVv4cDiJvScBbtuZ9cnsrN%2Bw6tsR7ZshO0LTfAMoT1DSwkshoTlTY6YZN03RZaJJswhEhPtHRswjV4CYVugPal5XEykJE5v7DJCm0LadTCTQUE5182T6YJCXo%2BQDSVHtJuxfsy1KYJMbl8j33g66Pm7%2B2me6Y%2FJJVUHpvxxVisqnMR2hk1AAq0sQYaHZ0ulgd7G6ri748QvC7dRRpWnkeh6J&X-Amz-Signature=e8405149257d8aaf4aa543983f1ac010c5da9834983add65695ee1b9f8109e2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWPOAZC4%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnADMXWD72v7TtV4R2nUfJc4CvQcoBg9JVRH0w5dxilQIhAP2%2F3rJNkfEqlk9uiI%2BWqJvZv8phD0QCsbLSDPmhakGbKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5iFftYQt682JgG%2BQq3AOy5gHJ48Yv3ZVjlDH4uboJOj1LWFLr7L3juxjnzv3RuvfIjjAMH2YMEA%2BgBomwG9rA5wGa29QqlV881Y0ap3IkGGr9ta2aSdrSbu%2BfBGeUr4AOLgjCSsPSKZ2JxcaRsdKnnB8rG6qC%2BpH8PKFjVkTG8peNTZfz8ZyRoK3H2VkBbD56Q5gP55KSWTMNbBE1ESwCn4ZQfYYgz76lfDFuWmYYsGJilEvYNp6J6niA4pIivU4V8ntxYxcrz0lfg5Ran10Rv9JVUr3Jc0BCYjUMoe8hJipW0b9hLuF0cyTSWXNshUr39cPf9Yun1WnGSaa4zUzgGpoXN0TRiw9KAWD3SUrGr5d4lw4X%2FQ5oEBYbGBM22QxD%2FrjwfLeq5ai0ZLIAGK9K0sHBMnSuxZOEXx1vjj9uFdWQUoLSpF45tS46jbqF9oboTG8WhgRcfKhMhZZT9lpOrXQNSM6BWoJ9HgrH0llMelD1NzdAQsfY0ZpD0%2BTKfWh6WNR0hz8xMaP%2BzoxYWu%2B86WBJ95VFrN%2BrB0xOc6ZC73xiRA5zMWGL1G%2F734PZd%2FJ9slc5CQhVzfRe5PFj0RG6iTqxSia0WEWNszKd%2BVsrsBTWBcKnAzp7rBOOwGrahnRDamvuwlUrzqLYKjC1yfDLBjqkAUkslVv4cDiJvScBbtuZ9cnsrN%2Bw6tsR7ZshO0LTfAMoT1DSwkshoTlTY6YZN03RZaJJswhEhPtHRswjV4CYVugPal5XEykJE5v7DJCm0LadTCTQUE5182T6YJCXo%2BQDSVHtJuxfsy1KYJMbl8j33g66Pm7%2B2me6Y%2FJJVUHpvxxVisqnMR2hk1AAq0sQYaHZ0ulgd7G6ri748QvC7dRRpWnkeh6J&X-Amz-Signature=9e25fa00a97747f8032f3c91900951a2d0758d3c112301081bc5d2b26fb8f097&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWPOAZC4%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnADMXWD72v7TtV4R2nUfJc4CvQcoBg9JVRH0w5dxilQIhAP2%2F3rJNkfEqlk9uiI%2BWqJvZv8phD0QCsbLSDPmhakGbKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5iFftYQt682JgG%2BQq3AOy5gHJ48Yv3ZVjlDH4uboJOj1LWFLr7L3juxjnzv3RuvfIjjAMH2YMEA%2BgBomwG9rA5wGa29QqlV881Y0ap3IkGGr9ta2aSdrSbu%2BfBGeUr4AOLgjCSsPSKZ2JxcaRsdKnnB8rG6qC%2BpH8PKFjVkTG8peNTZfz8ZyRoK3H2VkBbD56Q5gP55KSWTMNbBE1ESwCn4ZQfYYgz76lfDFuWmYYsGJilEvYNp6J6niA4pIivU4V8ntxYxcrz0lfg5Ran10Rv9JVUr3Jc0BCYjUMoe8hJipW0b9hLuF0cyTSWXNshUr39cPf9Yun1WnGSaa4zUzgGpoXN0TRiw9KAWD3SUrGr5d4lw4X%2FQ5oEBYbGBM22QxD%2FrjwfLeq5ai0ZLIAGK9K0sHBMnSuxZOEXx1vjj9uFdWQUoLSpF45tS46jbqF9oboTG8WhgRcfKhMhZZT9lpOrXQNSM6BWoJ9HgrH0llMelD1NzdAQsfY0ZpD0%2BTKfWh6WNR0hz8xMaP%2BzoxYWu%2B86WBJ95VFrN%2BrB0xOc6ZC73xiRA5zMWGL1G%2F734PZd%2FJ9slc5CQhVzfRe5PFj0RG6iTqxSia0WEWNszKd%2BVsrsBTWBcKnAzp7rBOOwGrahnRDamvuwlUrzqLYKjC1yfDLBjqkAUkslVv4cDiJvScBbtuZ9cnsrN%2Bw6tsR7ZshO0LTfAMoT1DSwkshoTlTY6YZN03RZaJJswhEhPtHRswjV4CYVugPal5XEykJE5v7DJCm0LadTCTQUE5182T6YJCXo%2BQDSVHtJuxfsy1KYJMbl8j33g66Pm7%2B2me6Y%2FJJVUHpvxxVisqnMR2hk1AAq0sQYaHZ0ulgd7G6ri748QvC7dRRpWnkeh6J&X-Amz-Signature=c114d4afe6f4f4f8fdcf2c7ddedd099e931e1b54ee7b945b982d1ec1ef1d53e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWPOAZC4%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnADMXWD72v7TtV4R2nUfJc4CvQcoBg9JVRH0w5dxilQIhAP2%2F3rJNkfEqlk9uiI%2BWqJvZv8phD0QCsbLSDPmhakGbKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5iFftYQt682JgG%2BQq3AOy5gHJ48Yv3ZVjlDH4uboJOj1LWFLr7L3juxjnzv3RuvfIjjAMH2YMEA%2BgBomwG9rA5wGa29QqlV881Y0ap3IkGGr9ta2aSdrSbu%2BfBGeUr4AOLgjCSsPSKZ2JxcaRsdKnnB8rG6qC%2BpH8PKFjVkTG8peNTZfz8ZyRoK3H2VkBbD56Q5gP55KSWTMNbBE1ESwCn4ZQfYYgz76lfDFuWmYYsGJilEvYNp6J6niA4pIivU4V8ntxYxcrz0lfg5Ran10Rv9JVUr3Jc0BCYjUMoe8hJipW0b9hLuF0cyTSWXNshUr39cPf9Yun1WnGSaa4zUzgGpoXN0TRiw9KAWD3SUrGr5d4lw4X%2FQ5oEBYbGBM22QxD%2FrjwfLeq5ai0ZLIAGK9K0sHBMnSuxZOEXx1vjj9uFdWQUoLSpF45tS46jbqF9oboTG8WhgRcfKhMhZZT9lpOrXQNSM6BWoJ9HgrH0llMelD1NzdAQsfY0ZpD0%2BTKfWh6WNR0hz8xMaP%2BzoxYWu%2B86WBJ95VFrN%2BrB0xOc6ZC73xiRA5zMWGL1G%2F734PZd%2FJ9slc5CQhVzfRe5PFj0RG6iTqxSia0WEWNszKd%2BVsrsBTWBcKnAzp7rBOOwGrahnRDamvuwlUrzqLYKjC1yfDLBjqkAUkslVv4cDiJvScBbtuZ9cnsrN%2Bw6tsR7ZshO0LTfAMoT1DSwkshoTlTY6YZN03RZaJJswhEhPtHRswjV4CYVugPal5XEykJE5v7DJCm0LadTCTQUE5182T6YJCXo%2BQDSVHtJuxfsy1KYJMbl8j33g66Pm7%2B2me6Y%2FJJVUHpvxxVisqnMR2hk1AAq0sQYaHZ0ulgd7G6ri748QvC7dRRpWnkeh6J&X-Amz-Signature=3f5948fb4504461fa1985cee6567079907d6ba77f45b27a20ca5ebd7a09206d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWPOAZC4%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnADMXWD72v7TtV4R2nUfJc4CvQcoBg9JVRH0w5dxilQIhAP2%2F3rJNkfEqlk9uiI%2BWqJvZv8phD0QCsbLSDPmhakGbKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5iFftYQt682JgG%2BQq3AOy5gHJ48Yv3ZVjlDH4uboJOj1LWFLr7L3juxjnzv3RuvfIjjAMH2YMEA%2BgBomwG9rA5wGa29QqlV881Y0ap3IkGGr9ta2aSdrSbu%2BfBGeUr4AOLgjCSsPSKZ2JxcaRsdKnnB8rG6qC%2BpH8PKFjVkTG8peNTZfz8ZyRoK3H2VkBbD56Q5gP55KSWTMNbBE1ESwCn4ZQfYYgz76lfDFuWmYYsGJilEvYNp6J6niA4pIivU4V8ntxYxcrz0lfg5Ran10Rv9JVUr3Jc0BCYjUMoe8hJipW0b9hLuF0cyTSWXNshUr39cPf9Yun1WnGSaa4zUzgGpoXN0TRiw9KAWD3SUrGr5d4lw4X%2FQ5oEBYbGBM22QxD%2FrjwfLeq5ai0ZLIAGK9K0sHBMnSuxZOEXx1vjj9uFdWQUoLSpF45tS46jbqF9oboTG8WhgRcfKhMhZZT9lpOrXQNSM6BWoJ9HgrH0llMelD1NzdAQsfY0ZpD0%2BTKfWh6WNR0hz8xMaP%2BzoxYWu%2B86WBJ95VFrN%2BrB0xOc6ZC73xiRA5zMWGL1G%2F734PZd%2FJ9slc5CQhVzfRe5PFj0RG6iTqxSia0WEWNszKd%2BVsrsBTWBcKnAzp7rBOOwGrahnRDamvuwlUrzqLYKjC1yfDLBjqkAUkslVv4cDiJvScBbtuZ9cnsrN%2Bw6tsR7ZshO0LTfAMoT1DSwkshoTlTY6YZN03RZaJJswhEhPtHRswjV4CYVugPal5XEykJE5v7DJCm0LadTCTQUE5182T6YJCXo%2BQDSVHtJuxfsy1KYJMbl8j33g66Pm7%2B2me6Y%2FJJVUHpvxxVisqnMR2hk1AAq0sQYaHZ0ulgd7G6ri748QvC7dRRpWnkeh6J&X-Amz-Signature=b9b4ea9c7172b87d5145c21e13e3fad611088c645588cc6ed7306653310acf86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWPOAZC4%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnADMXWD72v7TtV4R2nUfJc4CvQcoBg9JVRH0w5dxilQIhAP2%2F3rJNkfEqlk9uiI%2BWqJvZv8phD0QCsbLSDPmhakGbKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5iFftYQt682JgG%2BQq3AOy5gHJ48Yv3ZVjlDH4uboJOj1LWFLr7L3juxjnzv3RuvfIjjAMH2YMEA%2BgBomwG9rA5wGa29QqlV881Y0ap3IkGGr9ta2aSdrSbu%2BfBGeUr4AOLgjCSsPSKZ2JxcaRsdKnnB8rG6qC%2BpH8PKFjVkTG8peNTZfz8ZyRoK3H2VkBbD56Q5gP55KSWTMNbBE1ESwCn4ZQfYYgz76lfDFuWmYYsGJilEvYNp6J6niA4pIivU4V8ntxYxcrz0lfg5Ran10Rv9JVUr3Jc0BCYjUMoe8hJipW0b9hLuF0cyTSWXNshUr39cPf9Yun1WnGSaa4zUzgGpoXN0TRiw9KAWD3SUrGr5d4lw4X%2FQ5oEBYbGBM22QxD%2FrjwfLeq5ai0ZLIAGK9K0sHBMnSuxZOEXx1vjj9uFdWQUoLSpF45tS46jbqF9oboTG8WhgRcfKhMhZZT9lpOrXQNSM6BWoJ9HgrH0llMelD1NzdAQsfY0ZpD0%2BTKfWh6WNR0hz8xMaP%2BzoxYWu%2B86WBJ95VFrN%2BrB0xOc6ZC73xiRA5zMWGL1G%2F734PZd%2FJ9slc5CQhVzfRe5PFj0RG6iTqxSia0WEWNszKd%2BVsrsBTWBcKnAzp7rBOOwGrahnRDamvuwlUrzqLYKjC1yfDLBjqkAUkslVv4cDiJvScBbtuZ9cnsrN%2Bw6tsR7ZshO0LTfAMoT1DSwkshoTlTY6YZN03RZaJJswhEhPtHRswjV4CYVugPal5XEykJE5v7DJCm0LadTCTQUE5182T6YJCXo%2BQDSVHtJuxfsy1KYJMbl8j33g66Pm7%2B2me6Y%2FJJVUHpvxxVisqnMR2hk1AAq0sQYaHZ0ulgd7G6ri748QvC7dRRpWnkeh6J&X-Amz-Signature=558f4205d323b41561b8de7ed8473f3d57ddc3151a62bbf55f151a91f0d9624d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWPOAZC4%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnADMXWD72v7TtV4R2nUfJc4CvQcoBg9JVRH0w5dxilQIhAP2%2F3rJNkfEqlk9uiI%2BWqJvZv8phD0QCsbLSDPmhakGbKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5iFftYQt682JgG%2BQq3AOy5gHJ48Yv3ZVjlDH4uboJOj1LWFLr7L3juxjnzv3RuvfIjjAMH2YMEA%2BgBomwG9rA5wGa29QqlV881Y0ap3IkGGr9ta2aSdrSbu%2BfBGeUr4AOLgjCSsPSKZ2JxcaRsdKnnB8rG6qC%2BpH8PKFjVkTG8peNTZfz8ZyRoK3H2VkBbD56Q5gP55KSWTMNbBE1ESwCn4ZQfYYgz76lfDFuWmYYsGJilEvYNp6J6niA4pIivU4V8ntxYxcrz0lfg5Ran10Rv9JVUr3Jc0BCYjUMoe8hJipW0b9hLuF0cyTSWXNshUr39cPf9Yun1WnGSaa4zUzgGpoXN0TRiw9KAWD3SUrGr5d4lw4X%2FQ5oEBYbGBM22QxD%2FrjwfLeq5ai0ZLIAGK9K0sHBMnSuxZOEXx1vjj9uFdWQUoLSpF45tS46jbqF9oboTG8WhgRcfKhMhZZT9lpOrXQNSM6BWoJ9HgrH0llMelD1NzdAQsfY0ZpD0%2BTKfWh6WNR0hz8xMaP%2BzoxYWu%2B86WBJ95VFrN%2BrB0xOc6ZC73xiRA5zMWGL1G%2F734PZd%2FJ9slc5CQhVzfRe5PFj0RG6iTqxSia0WEWNszKd%2BVsrsBTWBcKnAzp7rBOOwGrahnRDamvuwlUrzqLYKjC1yfDLBjqkAUkslVv4cDiJvScBbtuZ9cnsrN%2Bw6tsR7ZshO0LTfAMoT1DSwkshoTlTY6YZN03RZaJJswhEhPtHRswjV4CYVugPal5XEykJE5v7DJCm0LadTCTQUE5182T6YJCXo%2BQDSVHtJuxfsy1KYJMbl8j33g66Pm7%2B2me6Y%2FJJVUHpvxxVisqnMR2hk1AAq0sQYaHZ0ulgd7G6ri748QvC7dRRpWnkeh6J&X-Amz-Signature=e1d0b890e1a4a76fb40359acb3ced9192c60cdfb4cedbe0e061eefee545d8bb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWPOAZC4%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnADMXWD72v7TtV4R2nUfJc4CvQcoBg9JVRH0w5dxilQIhAP2%2F3rJNkfEqlk9uiI%2BWqJvZv8phD0QCsbLSDPmhakGbKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5iFftYQt682JgG%2BQq3AOy5gHJ48Yv3ZVjlDH4uboJOj1LWFLr7L3juxjnzv3RuvfIjjAMH2YMEA%2BgBomwG9rA5wGa29QqlV881Y0ap3IkGGr9ta2aSdrSbu%2BfBGeUr4AOLgjCSsPSKZ2JxcaRsdKnnB8rG6qC%2BpH8PKFjVkTG8peNTZfz8ZyRoK3H2VkBbD56Q5gP55KSWTMNbBE1ESwCn4ZQfYYgz76lfDFuWmYYsGJilEvYNp6J6niA4pIivU4V8ntxYxcrz0lfg5Ran10Rv9JVUr3Jc0BCYjUMoe8hJipW0b9hLuF0cyTSWXNshUr39cPf9Yun1WnGSaa4zUzgGpoXN0TRiw9KAWD3SUrGr5d4lw4X%2FQ5oEBYbGBM22QxD%2FrjwfLeq5ai0ZLIAGK9K0sHBMnSuxZOEXx1vjj9uFdWQUoLSpF45tS46jbqF9oboTG8WhgRcfKhMhZZT9lpOrXQNSM6BWoJ9HgrH0llMelD1NzdAQsfY0ZpD0%2BTKfWh6WNR0hz8xMaP%2BzoxYWu%2B86WBJ95VFrN%2BrB0xOc6ZC73xiRA5zMWGL1G%2F734PZd%2FJ9slc5CQhVzfRe5PFj0RG6iTqxSia0WEWNszKd%2BVsrsBTWBcKnAzp7rBOOwGrahnRDamvuwlUrzqLYKjC1yfDLBjqkAUkslVv4cDiJvScBbtuZ9cnsrN%2Bw6tsR7ZshO0LTfAMoT1DSwkshoTlTY6YZN03RZaJJswhEhPtHRswjV4CYVugPal5XEykJE5v7DJCm0LadTCTQUE5182T6YJCXo%2BQDSVHtJuxfsy1KYJMbl8j33g66Pm7%2B2me6Y%2FJJVUHpvxxVisqnMR2hk1AAq0sQYaHZ0ulgd7G6ri748QvC7dRRpWnkeh6J&X-Amz-Signature=4d85728b231aa051bde3b082d3d33efd71e3678e56110a10c2878d1d3dca3a29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

