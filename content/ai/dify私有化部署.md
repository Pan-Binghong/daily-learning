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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFLDOSF%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIB4z6E%2FNS%2B%2BwQpQpGb5vv9S6z5X1pNZxBr%2FP%2BO3GGhKQAiEAqPV5k0UeofC%2FJ3Ws3iS2sh%2B5Pda4icQuo%2BzCsWaT72wq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCUY2oo%2B9TSiWtqDMSrcA81vUfh90TZJuo%2Fw%2BBSNrmxSBngILZaeppb%2Bd8qXKkFi3MeZX50VeVAMt%2BmWaUKST4UddBhBNbh2Da6E0cQ3tsZtt6%2BxpJGgUSt6EjwAye8mhD5isDXBNlloqsWzrY%2BtdBjxjDd%2B605GWlCQjQXTqTRzcGRj%2BZBHhHYxQTlLiWdjYfkOZsoO9s3ewzQrD%2Bb4m2fp4lzvu%2B7J6GnMVA4tIRzTgJZJDeUPdmvJNhOMH1WUU6ElLvF89SU3pCyC0dEjU%2FJuI%2F%2F%2F1UYDjZpDcIeFM69fB6%2FLxCyWxnJbero%2BrQnJgeW75tkKsbm5%2FGNGecwuGt64XifYaYQKCgE5cm9qcGC%2FdJ9vY5b4LNCZf9j5TPjRd54naj8cBL6RljPQC3qpBoJuRH19IuddIRD2tWJwxTiqCNV4gOsjHsENYFaWQdITBifFFr0cPFeJO0EunJy%2BCskVbmcGsY7%2FMLHbPmjKcsh1HO0b0ZvEjdzqP5EEBwe4QJAzoF6oxedzpPo3Tpo6ua1cd0%2FpWfCPF0ZQ68GAGvvkuObZleKXtMwi9OJNbrTUT1%2FbRQLlzIFSNxLWJkecD0pCNl2DCtcwecb%2Bl7kLtjut34LqoGmwLM03us5IKQG70KYii3btLfB2DL4gMP71%2FswGOqUBDNL2nwv4ME%2FEwCE5Ns8r4xUsrIvGlCh2QJ0pi5FDXA6gRLmLHSBBcgcML68clvDeOXXouMAYq%2Bg76At6OK21mOcPVNnH6A3m8J2PaOfIre8JJsQ7EcnPp%2B1SWyF1b4fx1QCOhBUoIC%2BebTXAhAQprpW%2BDVeq%2FWsb%2Fd9Ww%2BJQOHk7t1gVYUqyPp0XXQZ0OWGe0bgBdb0pjwIRVxZRjJBjap5%2FggpE&X-Amz-Signature=92c7b21362d8abda0d76775515cf64127933b1da29fe2b56b8fc4a2b513c9c09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFLDOSF%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIB4z6E%2FNS%2B%2BwQpQpGb5vv9S6z5X1pNZxBr%2FP%2BO3GGhKQAiEAqPV5k0UeofC%2FJ3Ws3iS2sh%2B5Pda4icQuo%2BzCsWaT72wq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCUY2oo%2B9TSiWtqDMSrcA81vUfh90TZJuo%2Fw%2BBSNrmxSBngILZaeppb%2Bd8qXKkFi3MeZX50VeVAMt%2BmWaUKST4UddBhBNbh2Da6E0cQ3tsZtt6%2BxpJGgUSt6EjwAye8mhD5isDXBNlloqsWzrY%2BtdBjxjDd%2B605GWlCQjQXTqTRzcGRj%2BZBHhHYxQTlLiWdjYfkOZsoO9s3ewzQrD%2Bb4m2fp4lzvu%2B7J6GnMVA4tIRzTgJZJDeUPdmvJNhOMH1WUU6ElLvF89SU3pCyC0dEjU%2FJuI%2F%2F%2F1UYDjZpDcIeFM69fB6%2FLxCyWxnJbero%2BrQnJgeW75tkKsbm5%2FGNGecwuGt64XifYaYQKCgE5cm9qcGC%2FdJ9vY5b4LNCZf9j5TPjRd54naj8cBL6RljPQC3qpBoJuRH19IuddIRD2tWJwxTiqCNV4gOsjHsENYFaWQdITBifFFr0cPFeJO0EunJy%2BCskVbmcGsY7%2FMLHbPmjKcsh1HO0b0ZvEjdzqP5EEBwe4QJAzoF6oxedzpPo3Tpo6ua1cd0%2FpWfCPF0ZQ68GAGvvkuObZleKXtMwi9OJNbrTUT1%2FbRQLlzIFSNxLWJkecD0pCNl2DCtcwecb%2Bl7kLtjut34LqoGmwLM03us5IKQG70KYii3btLfB2DL4gMP71%2FswGOqUBDNL2nwv4ME%2FEwCE5Ns8r4xUsrIvGlCh2QJ0pi5FDXA6gRLmLHSBBcgcML68clvDeOXXouMAYq%2Bg76At6OK21mOcPVNnH6A3m8J2PaOfIre8JJsQ7EcnPp%2B1SWyF1b4fx1QCOhBUoIC%2BebTXAhAQprpW%2BDVeq%2FWsb%2Fd9Ww%2BJQOHk7t1gVYUqyPp0XXQZ0OWGe0bgBdb0pjwIRVxZRjJBjap5%2FggpE&X-Amz-Signature=c3d6edde1385f996c388115bbeb694a32a26a66238b0b5b082d83a4006fade04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFLDOSF%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIB4z6E%2FNS%2B%2BwQpQpGb5vv9S6z5X1pNZxBr%2FP%2BO3GGhKQAiEAqPV5k0UeofC%2FJ3Ws3iS2sh%2B5Pda4icQuo%2BzCsWaT72wq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCUY2oo%2B9TSiWtqDMSrcA81vUfh90TZJuo%2Fw%2BBSNrmxSBngILZaeppb%2Bd8qXKkFi3MeZX50VeVAMt%2BmWaUKST4UddBhBNbh2Da6E0cQ3tsZtt6%2BxpJGgUSt6EjwAye8mhD5isDXBNlloqsWzrY%2BtdBjxjDd%2B605GWlCQjQXTqTRzcGRj%2BZBHhHYxQTlLiWdjYfkOZsoO9s3ewzQrD%2Bb4m2fp4lzvu%2B7J6GnMVA4tIRzTgJZJDeUPdmvJNhOMH1WUU6ElLvF89SU3pCyC0dEjU%2FJuI%2F%2F%2F1UYDjZpDcIeFM69fB6%2FLxCyWxnJbero%2BrQnJgeW75tkKsbm5%2FGNGecwuGt64XifYaYQKCgE5cm9qcGC%2FdJ9vY5b4LNCZf9j5TPjRd54naj8cBL6RljPQC3qpBoJuRH19IuddIRD2tWJwxTiqCNV4gOsjHsENYFaWQdITBifFFr0cPFeJO0EunJy%2BCskVbmcGsY7%2FMLHbPmjKcsh1HO0b0ZvEjdzqP5EEBwe4QJAzoF6oxedzpPo3Tpo6ua1cd0%2FpWfCPF0ZQ68GAGvvkuObZleKXtMwi9OJNbrTUT1%2FbRQLlzIFSNxLWJkecD0pCNl2DCtcwecb%2Bl7kLtjut34LqoGmwLM03us5IKQG70KYii3btLfB2DL4gMP71%2FswGOqUBDNL2nwv4ME%2FEwCE5Ns8r4xUsrIvGlCh2QJ0pi5FDXA6gRLmLHSBBcgcML68clvDeOXXouMAYq%2Bg76At6OK21mOcPVNnH6A3m8J2PaOfIre8JJsQ7EcnPp%2B1SWyF1b4fx1QCOhBUoIC%2BebTXAhAQprpW%2BDVeq%2FWsb%2Fd9Ww%2BJQOHk7t1gVYUqyPp0XXQZ0OWGe0bgBdb0pjwIRVxZRjJBjap5%2FggpE&X-Amz-Signature=a280fd9b5cc5168dec7dc0f55d5954ed104c849f7ad9929e1721aa78e7dc78bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFLDOSF%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIB4z6E%2FNS%2B%2BwQpQpGb5vv9S6z5X1pNZxBr%2FP%2BO3GGhKQAiEAqPV5k0UeofC%2FJ3Ws3iS2sh%2B5Pda4icQuo%2BzCsWaT72wq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCUY2oo%2B9TSiWtqDMSrcA81vUfh90TZJuo%2Fw%2BBSNrmxSBngILZaeppb%2Bd8qXKkFi3MeZX50VeVAMt%2BmWaUKST4UddBhBNbh2Da6E0cQ3tsZtt6%2BxpJGgUSt6EjwAye8mhD5isDXBNlloqsWzrY%2BtdBjxjDd%2B605GWlCQjQXTqTRzcGRj%2BZBHhHYxQTlLiWdjYfkOZsoO9s3ewzQrD%2Bb4m2fp4lzvu%2B7J6GnMVA4tIRzTgJZJDeUPdmvJNhOMH1WUU6ElLvF89SU3pCyC0dEjU%2FJuI%2F%2F%2F1UYDjZpDcIeFM69fB6%2FLxCyWxnJbero%2BrQnJgeW75tkKsbm5%2FGNGecwuGt64XifYaYQKCgE5cm9qcGC%2FdJ9vY5b4LNCZf9j5TPjRd54naj8cBL6RljPQC3qpBoJuRH19IuddIRD2tWJwxTiqCNV4gOsjHsENYFaWQdITBifFFr0cPFeJO0EunJy%2BCskVbmcGsY7%2FMLHbPmjKcsh1HO0b0ZvEjdzqP5EEBwe4QJAzoF6oxedzpPo3Tpo6ua1cd0%2FpWfCPF0ZQ68GAGvvkuObZleKXtMwi9OJNbrTUT1%2FbRQLlzIFSNxLWJkecD0pCNl2DCtcwecb%2Bl7kLtjut34LqoGmwLM03us5IKQG70KYii3btLfB2DL4gMP71%2FswGOqUBDNL2nwv4ME%2FEwCE5Ns8r4xUsrIvGlCh2QJ0pi5FDXA6gRLmLHSBBcgcML68clvDeOXXouMAYq%2Bg76At6OK21mOcPVNnH6A3m8J2PaOfIre8JJsQ7EcnPp%2B1SWyF1b4fx1QCOhBUoIC%2BebTXAhAQprpW%2BDVeq%2FWsb%2Fd9Ww%2BJQOHk7t1gVYUqyPp0XXQZ0OWGe0bgBdb0pjwIRVxZRjJBjap5%2FggpE&X-Amz-Signature=5d690020fe6d049dafed07b6234e65923c388b6755c5f6268611ee20b273c2f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFLDOSF%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIB4z6E%2FNS%2B%2BwQpQpGb5vv9S6z5X1pNZxBr%2FP%2BO3GGhKQAiEAqPV5k0UeofC%2FJ3Ws3iS2sh%2B5Pda4icQuo%2BzCsWaT72wq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCUY2oo%2B9TSiWtqDMSrcA81vUfh90TZJuo%2Fw%2BBSNrmxSBngILZaeppb%2Bd8qXKkFi3MeZX50VeVAMt%2BmWaUKST4UddBhBNbh2Da6E0cQ3tsZtt6%2BxpJGgUSt6EjwAye8mhD5isDXBNlloqsWzrY%2BtdBjxjDd%2B605GWlCQjQXTqTRzcGRj%2BZBHhHYxQTlLiWdjYfkOZsoO9s3ewzQrD%2Bb4m2fp4lzvu%2B7J6GnMVA4tIRzTgJZJDeUPdmvJNhOMH1WUU6ElLvF89SU3pCyC0dEjU%2FJuI%2F%2F%2F1UYDjZpDcIeFM69fB6%2FLxCyWxnJbero%2BrQnJgeW75tkKsbm5%2FGNGecwuGt64XifYaYQKCgE5cm9qcGC%2FdJ9vY5b4LNCZf9j5TPjRd54naj8cBL6RljPQC3qpBoJuRH19IuddIRD2tWJwxTiqCNV4gOsjHsENYFaWQdITBifFFr0cPFeJO0EunJy%2BCskVbmcGsY7%2FMLHbPmjKcsh1HO0b0ZvEjdzqP5EEBwe4QJAzoF6oxedzpPo3Tpo6ua1cd0%2FpWfCPF0ZQ68GAGvvkuObZleKXtMwi9OJNbrTUT1%2FbRQLlzIFSNxLWJkecD0pCNl2DCtcwecb%2Bl7kLtjut34LqoGmwLM03us5IKQG70KYii3btLfB2DL4gMP71%2FswGOqUBDNL2nwv4ME%2FEwCE5Ns8r4xUsrIvGlCh2QJ0pi5FDXA6gRLmLHSBBcgcML68clvDeOXXouMAYq%2Bg76At6OK21mOcPVNnH6A3m8J2PaOfIre8JJsQ7EcnPp%2B1SWyF1b4fx1QCOhBUoIC%2BebTXAhAQprpW%2BDVeq%2FWsb%2Fd9Ww%2BJQOHk7t1gVYUqyPp0XXQZ0OWGe0bgBdb0pjwIRVxZRjJBjap5%2FggpE&X-Amz-Signature=58399f4bcec57c5161ae4510b3e6e51609727ef8e9088880632b68c8501a2d09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFLDOSF%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIB4z6E%2FNS%2B%2BwQpQpGb5vv9S6z5X1pNZxBr%2FP%2BO3GGhKQAiEAqPV5k0UeofC%2FJ3Ws3iS2sh%2B5Pda4icQuo%2BzCsWaT72wq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCUY2oo%2B9TSiWtqDMSrcA81vUfh90TZJuo%2Fw%2BBSNrmxSBngILZaeppb%2Bd8qXKkFi3MeZX50VeVAMt%2BmWaUKST4UddBhBNbh2Da6E0cQ3tsZtt6%2BxpJGgUSt6EjwAye8mhD5isDXBNlloqsWzrY%2BtdBjxjDd%2B605GWlCQjQXTqTRzcGRj%2BZBHhHYxQTlLiWdjYfkOZsoO9s3ewzQrD%2Bb4m2fp4lzvu%2B7J6GnMVA4tIRzTgJZJDeUPdmvJNhOMH1WUU6ElLvF89SU3pCyC0dEjU%2FJuI%2F%2F%2F1UYDjZpDcIeFM69fB6%2FLxCyWxnJbero%2BrQnJgeW75tkKsbm5%2FGNGecwuGt64XifYaYQKCgE5cm9qcGC%2FdJ9vY5b4LNCZf9j5TPjRd54naj8cBL6RljPQC3qpBoJuRH19IuddIRD2tWJwxTiqCNV4gOsjHsENYFaWQdITBifFFr0cPFeJO0EunJy%2BCskVbmcGsY7%2FMLHbPmjKcsh1HO0b0ZvEjdzqP5EEBwe4QJAzoF6oxedzpPo3Tpo6ua1cd0%2FpWfCPF0ZQ68GAGvvkuObZleKXtMwi9OJNbrTUT1%2FbRQLlzIFSNxLWJkecD0pCNl2DCtcwecb%2Bl7kLtjut34LqoGmwLM03us5IKQG70KYii3btLfB2DL4gMP71%2FswGOqUBDNL2nwv4ME%2FEwCE5Ns8r4xUsrIvGlCh2QJ0pi5FDXA6gRLmLHSBBcgcML68clvDeOXXouMAYq%2Bg76At6OK21mOcPVNnH6A3m8J2PaOfIre8JJsQ7EcnPp%2B1SWyF1b4fx1QCOhBUoIC%2BebTXAhAQprpW%2BDVeq%2FWsb%2Fd9Ww%2BJQOHk7t1gVYUqyPp0XXQZ0OWGe0bgBdb0pjwIRVxZRjJBjap5%2FggpE&X-Amz-Signature=81d9fd8997d60a8b6776fc74d09c5ea085c1e0805e00a00d43613f838d3b6350&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFLDOSF%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIB4z6E%2FNS%2B%2BwQpQpGb5vv9S6z5X1pNZxBr%2FP%2BO3GGhKQAiEAqPV5k0UeofC%2FJ3Ws3iS2sh%2B5Pda4icQuo%2BzCsWaT72wq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCUY2oo%2B9TSiWtqDMSrcA81vUfh90TZJuo%2Fw%2BBSNrmxSBngILZaeppb%2Bd8qXKkFi3MeZX50VeVAMt%2BmWaUKST4UddBhBNbh2Da6E0cQ3tsZtt6%2BxpJGgUSt6EjwAye8mhD5isDXBNlloqsWzrY%2BtdBjxjDd%2B605GWlCQjQXTqTRzcGRj%2BZBHhHYxQTlLiWdjYfkOZsoO9s3ewzQrD%2Bb4m2fp4lzvu%2B7J6GnMVA4tIRzTgJZJDeUPdmvJNhOMH1WUU6ElLvF89SU3pCyC0dEjU%2FJuI%2F%2F%2F1UYDjZpDcIeFM69fB6%2FLxCyWxnJbero%2BrQnJgeW75tkKsbm5%2FGNGecwuGt64XifYaYQKCgE5cm9qcGC%2FdJ9vY5b4LNCZf9j5TPjRd54naj8cBL6RljPQC3qpBoJuRH19IuddIRD2tWJwxTiqCNV4gOsjHsENYFaWQdITBifFFr0cPFeJO0EunJy%2BCskVbmcGsY7%2FMLHbPmjKcsh1HO0b0ZvEjdzqP5EEBwe4QJAzoF6oxedzpPo3Tpo6ua1cd0%2FpWfCPF0ZQ68GAGvvkuObZleKXtMwi9OJNbrTUT1%2FbRQLlzIFSNxLWJkecD0pCNl2DCtcwecb%2Bl7kLtjut34LqoGmwLM03us5IKQG70KYii3btLfB2DL4gMP71%2FswGOqUBDNL2nwv4ME%2FEwCE5Ns8r4xUsrIvGlCh2QJ0pi5FDXA6gRLmLHSBBcgcML68clvDeOXXouMAYq%2Bg76At6OK21mOcPVNnH6A3m8J2PaOfIre8JJsQ7EcnPp%2B1SWyF1b4fx1QCOhBUoIC%2BebTXAhAQprpW%2BDVeq%2FWsb%2Fd9Ww%2BJQOHk7t1gVYUqyPp0XXQZ0OWGe0bgBdb0pjwIRVxZRjJBjap5%2FggpE&X-Amz-Signature=794e8102096c9834129e219c75b100b7b70b1d866e4c52439e5a0a8cb320f0de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFLDOSF%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIB4z6E%2FNS%2B%2BwQpQpGb5vv9S6z5X1pNZxBr%2FP%2BO3GGhKQAiEAqPV5k0UeofC%2FJ3Ws3iS2sh%2B5Pda4icQuo%2BzCsWaT72wq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCUY2oo%2B9TSiWtqDMSrcA81vUfh90TZJuo%2Fw%2BBSNrmxSBngILZaeppb%2Bd8qXKkFi3MeZX50VeVAMt%2BmWaUKST4UddBhBNbh2Da6E0cQ3tsZtt6%2BxpJGgUSt6EjwAye8mhD5isDXBNlloqsWzrY%2BtdBjxjDd%2B605GWlCQjQXTqTRzcGRj%2BZBHhHYxQTlLiWdjYfkOZsoO9s3ewzQrD%2Bb4m2fp4lzvu%2B7J6GnMVA4tIRzTgJZJDeUPdmvJNhOMH1WUU6ElLvF89SU3pCyC0dEjU%2FJuI%2F%2F%2F1UYDjZpDcIeFM69fB6%2FLxCyWxnJbero%2BrQnJgeW75tkKsbm5%2FGNGecwuGt64XifYaYQKCgE5cm9qcGC%2FdJ9vY5b4LNCZf9j5TPjRd54naj8cBL6RljPQC3qpBoJuRH19IuddIRD2tWJwxTiqCNV4gOsjHsENYFaWQdITBifFFr0cPFeJO0EunJy%2BCskVbmcGsY7%2FMLHbPmjKcsh1HO0b0ZvEjdzqP5EEBwe4QJAzoF6oxedzpPo3Tpo6ua1cd0%2FpWfCPF0ZQ68GAGvvkuObZleKXtMwi9OJNbrTUT1%2FbRQLlzIFSNxLWJkecD0pCNl2DCtcwecb%2Bl7kLtjut34LqoGmwLM03us5IKQG70KYii3btLfB2DL4gMP71%2FswGOqUBDNL2nwv4ME%2FEwCE5Ns8r4xUsrIvGlCh2QJ0pi5FDXA6gRLmLHSBBcgcML68clvDeOXXouMAYq%2Bg76At6OK21mOcPVNnH6A3m8J2PaOfIre8JJsQ7EcnPp%2B1SWyF1b4fx1QCOhBUoIC%2BebTXAhAQprpW%2BDVeq%2FWsb%2Fd9Ww%2BJQOHk7t1gVYUqyPp0XXQZ0OWGe0bgBdb0pjwIRVxZRjJBjap5%2FggpE&X-Amz-Signature=d9979dcd6c625f39e059ec9251e284a8d0f688ff9491ebd99c5b3e3c173a4fb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFLDOSF%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIB4z6E%2FNS%2B%2BwQpQpGb5vv9S6z5X1pNZxBr%2FP%2BO3GGhKQAiEAqPV5k0UeofC%2FJ3Ws3iS2sh%2B5Pda4icQuo%2BzCsWaT72wq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCUY2oo%2B9TSiWtqDMSrcA81vUfh90TZJuo%2Fw%2BBSNrmxSBngILZaeppb%2Bd8qXKkFi3MeZX50VeVAMt%2BmWaUKST4UddBhBNbh2Da6E0cQ3tsZtt6%2BxpJGgUSt6EjwAye8mhD5isDXBNlloqsWzrY%2BtdBjxjDd%2B605GWlCQjQXTqTRzcGRj%2BZBHhHYxQTlLiWdjYfkOZsoO9s3ewzQrD%2Bb4m2fp4lzvu%2B7J6GnMVA4tIRzTgJZJDeUPdmvJNhOMH1WUU6ElLvF89SU3pCyC0dEjU%2FJuI%2F%2F%2F1UYDjZpDcIeFM69fB6%2FLxCyWxnJbero%2BrQnJgeW75tkKsbm5%2FGNGecwuGt64XifYaYQKCgE5cm9qcGC%2FdJ9vY5b4LNCZf9j5TPjRd54naj8cBL6RljPQC3qpBoJuRH19IuddIRD2tWJwxTiqCNV4gOsjHsENYFaWQdITBifFFr0cPFeJO0EunJy%2BCskVbmcGsY7%2FMLHbPmjKcsh1HO0b0ZvEjdzqP5EEBwe4QJAzoF6oxedzpPo3Tpo6ua1cd0%2FpWfCPF0ZQ68GAGvvkuObZleKXtMwi9OJNbrTUT1%2FbRQLlzIFSNxLWJkecD0pCNl2DCtcwecb%2Bl7kLtjut34LqoGmwLM03us5IKQG70KYii3btLfB2DL4gMP71%2FswGOqUBDNL2nwv4ME%2FEwCE5Ns8r4xUsrIvGlCh2QJ0pi5FDXA6gRLmLHSBBcgcML68clvDeOXXouMAYq%2Bg76At6OK21mOcPVNnH6A3m8J2PaOfIre8JJsQ7EcnPp%2B1SWyF1b4fx1QCOhBUoIC%2BebTXAhAQprpW%2BDVeq%2FWsb%2Fd9Ww%2BJQOHk7t1gVYUqyPp0XXQZ0OWGe0bgBdb0pjwIRVxZRjJBjap5%2FggpE&X-Amz-Signature=0123e2d891afd66a89fbb4b625458db6f1b9bd8cc6e627ef6cb78cec29df0551&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLFLDOSF%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIB4z6E%2FNS%2B%2BwQpQpGb5vv9S6z5X1pNZxBr%2FP%2BO3GGhKQAiEAqPV5k0UeofC%2FJ3Ws3iS2sh%2B5Pda4icQuo%2BzCsWaT72wq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCUY2oo%2B9TSiWtqDMSrcA81vUfh90TZJuo%2Fw%2BBSNrmxSBngILZaeppb%2Bd8qXKkFi3MeZX50VeVAMt%2BmWaUKST4UddBhBNbh2Da6E0cQ3tsZtt6%2BxpJGgUSt6EjwAye8mhD5isDXBNlloqsWzrY%2BtdBjxjDd%2B605GWlCQjQXTqTRzcGRj%2BZBHhHYxQTlLiWdjYfkOZsoO9s3ewzQrD%2Bb4m2fp4lzvu%2B7J6GnMVA4tIRzTgJZJDeUPdmvJNhOMH1WUU6ElLvF89SU3pCyC0dEjU%2FJuI%2F%2F%2F1UYDjZpDcIeFM69fB6%2FLxCyWxnJbero%2BrQnJgeW75tkKsbm5%2FGNGecwuGt64XifYaYQKCgE5cm9qcGC%2FdJ9vY5b4LNCZf9j5TPjRd54naj8cBL6RljPQC3qpBoJuRH19IuddIRD2tWJwxTiqCNV4gOsjHsENYFaWQdITBifFFr0cPFeJO0EunJy%2BCskVbmcGsY7%2FMLHbPmjKcsh1HO0b0ZvEjdzqP5EEBwe4QJAzoF6oxedzpPo3Tpo6ua1cd0%2FpWfCPF0ZQ68GAGvvkuObZleKXtMwi9OJNbrTUT1%2FbRQLlzIFSNxLWJkecD0pCNl2DCtcwecb%2Bl7kLtjut34LqoGmwLM03us5IKQG70KYii3btLfB2DL4gMP71%2FswGOqUBDNL2nwv4ME%2FEwCE5Ns8r4xUsrIvGlCh2QJ0pi5FDXA6gRLmLHSBBcgcML68clvDeOXXouMAYq%2Bg76At6OK21mOcPVNnH6A3m8J2PaOfIre8JJsQ7EcnPp%2B1SWyF1b4fx1QCOhBUoIC%2BebTXAhAQprpW%2BDVeq%2FWsb%2Fd9Ww%2BJQOHk7t1gVYUqyPp0XXQZ0OWGe0bgBdb0pjwIRVxZRjJBjap5%2FggpE&X-Amz-Signature=a1f7689029f068823cb8c039a59d42bbd715fd1b1109fc7c36f767ef272e4f2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

