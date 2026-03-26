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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RW65UTT%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDt4goligjfxYSYTMdHJlraadPAdlFDnr3kmFaKCC0MzAIgbJ9zwjKVoHR3vmkcfWpIqBqwqMbkVoGp6iPAfD7sr04qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHYRgd%2B2lOJstwMoyrcA1%2Fz7roksnvZcTA6xRbnclnP7Ir%2FBbXMxbiqazhaNZAJqS6Pb7iHLBq05z8oEDii36JfdPMsskC7NQmPr5NtC1B7H0Saf9clKZyTATfjewLGGqTjEnhIME7aj%2BTiw3G0UQmvOj809YWgmrhLBMuHby5mopOQRxOqwdQpqiCQwSHEofSviluWkc0JpmT8RK2VvIxeIbeeZp0DoiRETITCmQq1lkwFMpiIzUDxs3HbAL%2B43In8wDWg7xCVIXIhxbThtC40f5rtBQNI5HcRV2f9rItrnCOfBau7LVtYtGwxh9VhZaItRJlgVGi5nOQx5P4SEakLat8TG6zmSF%2B85%2BRPyYTFRRHbyHVGKxZ4%2FWClkdcG9fe%2BKp6KcjsESONDJnXnzIox01TMIuAue5Jy%2BP96uwc85qsHgBoVtlaWoLZYyYScpv0BWUdAQEzU%2FcVxwEyP30CfvUF%2FIVe2quyubClJTddcsYg%2F1h6%2BNqJWpGVh2itkkMxAkCXOa4qgAB5BuLVq5C57C%2BEQa3Y8APbqQ8nuxfdEDi10mOYI18xft9DgIx7ZFPpJjrkGq3e9jtCKn86NBz%2Fj8afw8iYXOFqEbJaRohxcp0O4pNFCVKlRsoFl4zpydamjs%2BvC1cf0ni%2BuMIzKks4GOqUBPEJf96kKVeGIvAEhGEnfpI5JxGXwX3HpsCc6d49J5jj5ZuCRIZJPeqq1G7QViBqAk%2FY2mkk6jCWARMCP64drLUkUY9eNNrZ890Rthb%2FQlKIh3zKnFdDuIN%2F8%2BcOeOi0F%2FKbx24mKB3g6xh9EAf27fjkg0eDdgqOfARr99fgtT8jSs0huqAy6JFuxO8lR16jc486gNu5PmD18dzXHgknXWwro9Gs1&X-Amz-Signature=8962af8be3a9419af094c5c187b1286220513f3f695131d336bfde2222b40749&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RW65UTT%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDt4goligjfxYSYTMdHJlraadPAdlFDnr3kmFaKCC0MzAIgbJ9zwjKVoHR3vmkcfWpIqBqwqMbkVoGp6iPAfD7sr04qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHYRgd%2B2lOJstwMoyrcA1%2Fz7roksnvZcTA6xRbnclnP7Ir%2FBbXMxbiqazhaNZAJqS6Pb7iHLBq05z8oEDii36JfdPMsskC7NQmPr5NtC1B7H0Saf9clKZyTATfjewLGGqTjEnhIME7aj%2BTiw3G0UQmvOj809YWgmrhLBMuHby5mopOQRxOqwdQpqiCQwSHEofSviluWkc0JpmT8RK2VvIxeIbeeZp0DoiRETITCmQq1lkwFMpiIzUDxs3HbAL%2B43In8wDWg7xCVIXIhxbThtC40f5rtBQNI5HcRV2f9rItrnCOfBau7LVtYtGwxh9VhZaItRJlgVGi5nOQx5P4SEakLat8TG6zmSF%2B85%2BRPyYTFRRHbyHVGKxZ4%2FWClkdcG9fe%2BKp6KcjsESONDJnXnzIox01TMIuAue5Jy%2BP96uwc85qsHgBoVtlaWoLZYyYScpv0BWUdAQEzU%2FcVxwEyP30CfvUF%2FIVe2quyubClJTddcsYg%2F1h6%2BNqJWpGVh2itkkMxAkCXOa4qgAB5BuLVq5C57C%2BEQa3Y8APbqQ8nuxfdEDi10mOYI18xft9DgIx7ZFPpJjrkGq3e9jtCKn86NBz%2Fj8afw8iYXOFqEbJaRohxcp0O4pNFCVKlRsoFl4zpydamjs%2BvC1cf0ni%2BuMIzKks4GOqUBPEJf96kKVeGIvAEhGEnfpI5JxGXwX3HpsCc6d49J5jj5ZuCRIZJPeqq1G7QViBqAk%2FY2mkk6jCWARMCP64drLUkUY9eNNrZ890Rthb%2FQlKIh3zKnFdDuIN%2F8%2BcOeOi0F%2FKbx24mKB3g6xh9EAf27fjkg0eDdgqOfARr99fgtT8jSs0huqAy6JFuxO8lR16jc486gNu5PmD18dzXHgknXWwro9Gs1&X-Amz-Signature=0636055e6a1d39d4439ee711e52b0ac5afb4c7d7693c16367f8897a7b6a69ea4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RW65UTT%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDt4goligjfxYSYTMdHJlraadPAdlFDnr3kmFaKCC0MzAIgbJ9zwjKVoHR3vmkcfWpIqBqwqMbkVoGp6iPAfD7sr04qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHYRgd%2B2lOJstwMoyrcA1%2Fz7roksnvZcTA6xRbnclnP7Ir%2FBbXMxbiqazhaNZAJqS6Pb7iHLBq05z8oEDii36JfdPMsskC7NQmPr5NtC1B7H0Saf9clKZyTATfjewLGGqTjEnhIME7aj%2BTiw3G0UQmvOj809YWgmrhLBMuHby5mopOQRxOqwdQpqiCQwSHEofSviluWkc0JpmT8RK2VvIxeIbeeZp0DoiRETITCmQq1lkwFMpiIzUDxs3HbAL%2B43In8wDWg7xCVIXIhxbThtC40f5rtBQNI5HcRV2f9rItrnCOfBau7LVtYtGwxh9VhZaItRJlgVGi5nOQx5P4SEakLat8TG6zmSF%2B85%2BRPyYTFRRHbyHVGKxZ4%2FWClkdcG9fe%2BKp6KcjsESONDJnXnzIox01TMIuAue5Jy%2BP96uwc85qsHgBoVtlaWoLZYyYScpv0BWUdAQEzU%2FcVxwEyP30CfvUF%2FIVe2quyubClJTddcsYg%2F1h6%2BNqJWpGVh2itkkMxAkCXOa4qgAB5BuLVq5C57C%2BEQa3Y8APbqQ8nuxfdEDi10mOYI18xft9DgIx7ZFPpJjrkGq3e9jtCKn86NBz%2Fj8afw8iYXOFqEbJaRohxcp0O4pNFCVKlRsoFl4zpydamjs%2BvC1cf0ni%2BuMIzKks4GOqUBPEJf96kKVeGIvAEhGEnfpI5JxGXwX3HpsCc6d49J5jj5ZuCRIZJPeqq1G7QViBqAk%2FY2mkk6jCWARMCP64drLUkUY9eNNrZ890Rthb%2FQlKIh3zKnFdDuIN%2F8%2BcOeOi0F%2FKbx24mKB3g6xh9EAf27fjkg0eDdgqOfARr99fgtT8jSs0huqAy6JFuxO8lR16jc486gNu5PmD18dzXHgknXWwro9Gs1&X-Amz-Signature=b3198eb9b2b5bfb0a015217aec1b25ce145b8fdf1ea783bf0b2b3cae2628690f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RW65UTT%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDt4goligjfxYSYTMdHJlraadPAdlFDnr3kmFaKCC0MzAIgbJ9zwjKVoHR3vmkcfWpIqBqwqMbkVoGp6iPAfD7sr04qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHYRgd%2B2lOJstwMoyrcA1%2Fz7roksnvZcTA6xRbnclnP7Ir%2FBbXMxbiqazhaNZAJqS6Pb7iHLBq05z8oEDii36JfdPMsskC7NQmPr5NtC1B7H0Saf9clKZyTATfjewLGGqTjEnhIME7aj%2BTiw3G0UQmvOj809YWgmrhLBMuHby5mopOQRxOqwdQpqiCQwSHEofSviluWkc0JpmT8RK2VvIxeIbeeZp0DoiRETITCmQq1lkwFMpiIzUDxs3HbAL%2B43In8wDWg7xCVIXIhxbThtC40f5rtBQNI5HcRV2f9rItrnCOfBau7LVtYtGwxh9VhZaItRJlgVGi5nOQx5P4SEakLat8TG6zmSF%2B85%2BRPyYTFRRHbyHVGKxZ4%2FWClkdcG9fe%2BKp6KcjsESONDJnXnzIox01TMIuAue5Jy%2BP96uwc85qsHgBoVtlaWoLZYyYScpv0BWUdAQEzU%2FcVxwEyP30CfvUF%2FIVe2quyubClJTddcsYg%2F1h6%2BNqJWpGVh2itkkMxAkCXOa4qgAB5BuLVq5C57C%2BEQa3Y8APbqQ8nuxfdEDi10mOYI18xft9DgIx7ZFPpJjrkGq3e9jtCKn86NBz%2Fj8afw8iYXOFqEbJaRohxcp0O4pNFCVKlRsoFl4zpydamjs%2BvC1cf0ni%2BuMIzKks4GOqUBPEJf96kKVeGIvAEhGEnfpI5JxGXwX3HpsCc6d49J5jj5ZuCRIZJPeqq1G7QViBqAk%2FY2mkk6jCWARMCP64drLUkUY9eNNrZ890Rthb%2FQlKIh3zKnFdDuIN%2F8%2BcOeOi0F%2FKbx24mKB3g6xh9EAf27fjkg0eDdgqOfARr99fgtT8jSs0huqAy6JFuxO8lR16jc486gNu5PmD18dzXHgknXWwro9Gs1&X-Amz-Signature=99b26f747053a17db7e5d6c0b627688dcba68b1a03b9221acec10fa01286bd70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RW65UTT%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDt4goligjfxYSYTMdHJlraadPAdlFDnr3kmFaKCC0MzAIgbJ9zwjKVoHR3vmkcfWpIqBqwqMbkVoGp6iPAfD7sr04qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHYRgd%2B2lOJstwMoyrcA1%2Fz7roksnvZcTA6xRbnclnP7Ir%2FBbXMxbiqazhaNZAJqS6Pb7iHLBq05z8oEDii36JfdPMsskC7NQmPr5NtC1B7H0Saf9clKZyTATfjewLGGqTjEnhIME7aj%2BTiw3G0UQmvOj809YWgmrhLBMuHby5mopOQRxOqwdQpqiCQwSHEofSviluWkc0JpmT8RK2VvIxeIbeeZp0DoiRETITCmQq1lkwFMpiIzUDxs3HbAL%2B43In8wDWg7xCVIXIhxbThtC40f5rtBQNI5HcRV2f9rItrnCOfBau7LVtYtGwxh9VhZaItRJlgVGi5nOQx5P4SEakLat8TG6zmSF%2B85%2BRPyYTFRRHbyHVGKxZ4%2FWClkdcG9fe%2BKp6KcjsESONDJnXnzIox01TMIuAue5Jy%2BP96uwc85qsHgBoVtlaWoLZYyYScpv0BWUdAQEzU%2FcVxwEyP30CfvUF%2FIVe2quyubClJTddcsYg%2F1h6%2BNqJWpGVh2itkkMxAkCXOa4qgAB5BuLVq5C57C%2BEQa3Y8APbqQ8nuxfdEDi10mOYI18xft9DgIx7ZFPpJjrkGq3e9jtCKn86NBz%2Fj8afw8iYXOFqEbJaRohxcp0O4pNFCVKlRsoFl4zpydamjs%2BvC1cf0ni%2BuMIzKks4GOqUBPEJf96kKVeGIvAEhGEnfpI5JxGXwX3HpsCc6d49J5jj5ZuCRIZJPeqq1G7QViBqAk%2FY2mkk6jCWARMCP64drLUkUY9eNNrZ890Rthb%2FQlKIh3zKnFdDuIN%2F8%2BcOeOi0F%2FKbx24mKB3g6xh9EAf27fjkg0eDdgqOfARr99fgtT8jSs0huqAy6JFuxO8lR16jc486gNu5PmD18dzXHgknXWwro9Gs1&X-Amz-Signature=a69e393d86bbb939e21008f0145209ba510909bd3bda7bdc90393aa3fffde53a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RW65UTT%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDt4goligjfxYSYTMdHJlraadPAdlFDnr3kmFaKCC0MzAIgbJ9zwjKVoHR3vmkcfWpIqBqwqMbkVoGp6iPAfD7sr04qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHYRgd%2B2lOJstwMoyrcA1%2Fz7roksnvZcTA6xRbnclnP7Ir%2FBbXMxbiqazhaNZAJqS6Pb7iHLBq05z8oEDii36JfdPMsskC7NQmPr5NtC1B7H0Saf9clKZyTATfjewLGGqTjEnhIME7aj%2BTiw3G0UQmvOj809YWgmrhLBMuHby5mopOQRxOqwdQpqiCQwSHEofSviluWkc0JpmT8RK2VvIxeIbeeZp0DoiRETITCmQq1lkwFMpiIzUDxs3HbAL%2B43In8wDWg7xCVIXIhxbThtC40f5rtBQNI5HcRV2f9rItrnCOfBau7LVtYtGwxh9VhZaItRJlgVGi5nOQx5P4SEakLat8TG6zmSF%2B85%2BRPyYTFRRHbyHVGKxZ4%2FWClkdcG9fe%2BKp6KcjsESONDJnXnzIox01TMIuAue5Jy%2BP96uwc85qsHgBoVtlaWoLZYyYScpv0BWUdAQEzU%2FcVxwEyP30CfvUF%2FIVe2quyubClJTddcsYg%2F1h6%2BNqJWpGVh2itkkMxAkCXOa4qgAB5BuLVq5C57C%2BEQa3Y8APbqQ8nuxfdEDi10mOYI18xft9DgIx7ZFPpJjrkGq3e9jtCKn86NBz%2Fj8afw8iYXOFqEbJaRohxcp0O4pNFCVKlRsoFl4zpydamjs%2BvC1cf0ni%2BuMIzKks4GOqUBPEJf96kKVeGIvAEhGEnfpI5JxGXwX3HpsCc6d49J5jj5ZuCRIZJPeqq1G7QViBqAk%2FY2mkk6jCWARMCP64drLUkUY9eNNrZ890Rthb%2FQlKIh3zKnFdDuIN%2F8%2BcOeOi0F%2FKbx24mKB3g6xh9EAf27fjkg0eDdgqOfARr99fgtT8jSs0huqAy6JFuxO8lR16jc486gNu5PmD18dzXHgknXWwro9Gs1&X-Amz-Signature=7675cee4433089826504cedacd8107d49d5fa8a5ae1bad3e01cded7d7700259c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RW65UTT%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDt4goligjfxYSYTMdHJlraadPAdlFDnr3kmFaKCC0MzAIgbJ9zwjKVoHR3vmkcfWpIqBqwqMbkVoGp6iPAfD7sr04qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHYRgd%2B2lOJstwMoyrcA1%2Fz7roksnvZcTA6xRbnclnP7Ir%2FBbXMxbiqazhaNZAJqS6Pb7iHLBq05z8oEDii36JfdPMsskC7NQmPr5NtC1B7H0Saf9clKZyTATfjewLGGqTjEnhIME7aj%2BTiw3G0UQmvOj809YWgmrhLBMuHby5mopOQRxOqwdQpqiCQwSHEofSviluWkc0JpmT8RK2VvIxeIbeeZp0DoiRETITCmQq1lkwFMpiIzUDxs3HbAL%2B43In8wDWg7xCVIXIhxbThtC40f5rtBQNI5HcRV2f9rItrnCOfBau7LVtYtGwxh9VhZaItRJlgVGi5nOQx5P4SEakLat8TG6zmSF%2B85%2BRPyYTFRRHbyHVGKxZ4%2FWClkdcG9fe%2BKp6KcjsESONDJnXnzIox01TMIuAue5Jy%2BP96uwc85qsHgBoVtlaWoLZYyYScpv0BWUdAQEzU%2FcVxwEyP30CfvUF%2FIVe2quyubClJTddcsYg%2F1h6%2BNqJWpGVh2itkkMxAkCXOa4qgAB5BuLVq5C57C%2BEQa3Y8APbqQ8nuxfdEDi10mOYI18xft9DgIx7ZFPpJjrkGq3e9jtCKn86NBz%2Fj8afw8iYXOFqEbJaRohxcp0O4pNFCVKlRsoFl4zpydamjs%2BvC1cf0ni%2BuMIzKks4GOqUBPEJf96kKVeGIvAEhGEnfpI5JxGXwX3HpsCc6d49J5jj5ZuCRIZJPeqq1G7QViBqAk%2FY2mkk6jCWARMCP64drLUkUY9eNNrZ890Rthb%2FQlKIh3zKnFdDuIN%2F8%2BcOeOi0F%2FKbx24mKB3g6xh9EAf27fjkg0eDdgqOfARr99fgtT8jSs0huqAy6JFuxO8lR16jc486gNu5PmD18dzXHgknXWwro9Gs1&X-Amz-Signature=7e8b1107508f7de53adb912cb80c53cbeab01a5784516aa1668fd805425c5a26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RW65UTT%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDt4goligjfxYSYTMdHJlraadPAdlFDnr3kmFaKCC0MzAIgbJ9zwjKVoHR3vmkcfWpIqBqwqMbkVoGp6iPAfD7sr04qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHYRgd%2B2lOJstwMoyrcA1%2Fz7roksnvZcTA6xRbnclnP7Ir%2FBbXMxbiqazhaNZAJqS6Pb7iHLBq05z8oEDii36JfdPMsskC7NQmPr5NtC1B7H0Saf9clKZyTATfjewLGGqTjEnhIME7aj%2BTiw3G0UQmvOj809YWgmrhLBMuHby5mopOQRxOqwdQpqiCQwSHEofSviluWkc0JpmT8RK2VvIxeIbeeZp0DoiRETITCmQq1lkwFMpiIzUDxs3HbAL%2B43In8wDWg7xCVIXIhxbThtC40f5rtBQNI5HcRV2f9rItrnCOfBau7LVtYtGwxh9VhZaItRJlgVGi5nOQx5P4SEakLat8TG6zmSF%2B85%2BRPyYTFRRHbyHVGKxZ4%2FWClkdcG9fe%2BKp6KcjsESONDJnXnzIox01TMIuAue5Jy%2BP96uwc85qsHgBoVtlaWoLZYyYScpv0BWUdAQEzU%2FcVxwEyP30CfvUF%2FIVe2quyubClJTddcsYg%2F1h6%2BNqJWpGVh2itkkMxAkCXOa4qgAB5BuLVq5C57C%2BEQa3Y8APbqQ8nuxfdEDi10mOYI18xft9DgIx7ZFPpJjrkGq3e9jtCKn86NBz%2Fj8afw8iYXOFqEbJaRohxcp0O4pNFCVKlRsoFl4zpydamjs%2BvC1cf0ni%2BuMIzKks4GOqUBPEJf96kKVeGIvAEhGEnfpI5JxGXwX3HpsCc6d49J5jj5ZuCRIZJPeqq1G7QViBqAk%2FY2mkk6jCWARMCP64drLUkUY9eNNrZ890Rthb%2FQlKIh3zKnFdDuIN%2F8%2BcOeOi0F%2FKbx24mKB3g6xh9EAf27fjkg0eDdgqOfARr99fgtT8jSs0huqAy6JFuxO8lR16jc486gNu5PmD18dzXHgknXWwro9Gs1&X-Amz-Signature=e69f0c824a4ad65f52ad84bc0e90fd2637e84d1a01494a17245447de65035cea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RW65UTT%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDt4goligjfxYSYTMdHJlraadPAdlFDnr3kmFaKCC0MzAIgbJ9zwjKVoHR3vmkcfWpIqBqwqMbkVoGp6iPAfD7sr04qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHYRgd%2B2lOJstwMoyrcA1%2Fz7roksnvZcTA6xRbnclnP7Ir%2FBbXMxbiqazhaNZAJqS6Pb7iHLBq05z8oEDii36JfdPMsskC7NQmPr5NtC1B7H0Saf9clKZyTATfjewLGGqTjEnhIME7aj%2BTiw3G0UQmvOj809YWgmrhLBMuHby5mopOQRxOqwdQpqiCQwSHEofSviluWkc0JpmT8RK2VvIxeIbeeZp0DoiRETITCmQq1lkwFMpiIzUDxs3HbAL%2B43In8wDWg7xCVIXIhxbThtC40f5rtBQNI5HcRV2f9rItrnCOfBau7LVtYtGwxh9VhZaItRJlgVGi5nOQx5P4SEakLat8TG6zmSF%2B85%2BRPyYTFRRHbyHVGKxZ4%2FWClkdcG9fe%2BKp6KcjsESONDJnXnzIox01TMIuAue5Jy%2BP96uwc85qsHgBoVtlaWoLZYyYScpv0BWUdAQEzU%2FcVxwEyP30CfvUF%2FIVe2quyubClJTddcsYg%2F1h6%2BNqJWpGVh2itkkMxAkCXOa4qgAB5BuLVq5C57C%2BEQa3Y8APbqQ8nuxfdEDi10mOYI18xft9DgIx7ZFPpJjrkGq3e9jtCKn86NBz%2Fj8afw8iYXOFqEbJaRohxcp0O4pNFCVKlRsoFl4zpydamjs%2BvC1cf0ni%2BuMIzKks4GOqUBPEJf96kKVeGIvAEhGEnfpI5JxGXwX3HpsCc6d49J5jj5ZuCRIZJPeqq1G7QViBqAk%2FY2mkk6jCWARMCP64drLUkUY9eNNrZ890Rthb%2FQlKIh3zKnFdDuIN%2F8%2BcOeOi0F%2FKbx24mKB3g6xh9EAf27fjkg0eDdgqOfARr99fgtT8jSs0huqAy6JFuxO8lR16jc486gNu5PmD18dzXHgknXWwro9Gs1&X-Amz-Signature=08ad90f46bd722d6421a9a51520469865ea5d7ca672fae6d474a2191f9875b4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RW65UTT%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDt4goligjfxYSYTMdHJlraadPAdlFDnr3kmFaKCC0MzAIgbJ9zwjKVoHR3vmkcfWpIqBqwqMbkVoGp6iPAfD7sr04qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHYRgd%2B2lOJstwMoyrcA1%2Fz7roksnvZcTA6xRbnclnP7Ir%2FBbXMxbiqazhaNZAJqS6Pb7iHLBq05z8oEDii36JfdPMsskC7NQmPr5NtC1B7H0Saf9clKZyTATfjewLGGqTjEnhIME7aj%2BTiw3G0UQmvOj809YWgmrhLBMuHby5mopOQRxOqwdQpqiCQwSHEofSviluWkc0JpmT8RK2VvIxeIbeeZp0DoiRETITCmQq1lkwFMpiIzUDxs3HbAL%2B43In8wDWg7xCVIXIhxbThtC40f5rtBQNI5HcRV2f9rItrnCOfBau7LVtYtGwxh9VhZaItRJlgVGi5nOQx5P4SEakLat8TG6zmSF%2B85%2BRPyYTFRRHbyHVGKxZ4%2FWClkdcG9fe%2BKp6KcjsESONDJnXnzIox01TMIuAue5Jy%2BP96uwc85qsHgBoVtlaWoLZYyYScpv0BWUdAQEzU%2FcVxwEyP30CfvUF%2FIVe2quyubClJTddcsYg%2F1h6%2BNqJWpGVh2itkkMxAkCXOa4qgAB5BuLVq5C57C%2BEQa3Y8APbqQ8nuxfdEDi10mOYI18xft9DgIx7ZFPpJjrkGq3e9jtCKn86NBz%2Fj8afw8iYXOFqEbJaRohxcp0O4pNFCVKlRsoFl4zpydamjs%2BvC1cf0ni%2BuMIzKks4GOqUBPEJf96kKVeGIvAEhGEnfpI5JxGXwX3HpsCc6d49J5jj5ZuCRIZJPeqq1G7QViBqAk%2FY2mkk6jCWARMCP64drLUkUY9eNNrZ890Rthb%2FQlKIh3zKnFdDuIN%2F8%2BcOeOi0F%2FKbx24mKB3g6xh9EAf27fjkg0eDdgqOfARr99fgtT8jSs0huqAy6JFuxO8lR16jc486gNu5PmD18dzXHgknXWwro9Gs1&X-Amz-Signature=9f4543c23d6f3ef97a6676e49feabfebac18d0e051932e28b8413b1f4004c943&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

