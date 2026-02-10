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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X26WFBJL%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzuhExZ6uJote%2FcGLGXrIEM9r5jjixKgZx%2BNLuNiaBdAiEA3O4kko3yL%2FHkgjtvf6V6UpxVrpRCoI%2BatOi7jG1aGTYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6dbWxqZTJcg2hJJCrcA3cGHGUCNnbujhw5cKa0cWwzdUDePNjb4M9jL1FNSeAOY%2BaqzLRcoqddhEYqK4i5oatj3svLGWcfgLPD%2FLYcTDxNdM%2Fad7gLZupjD63%2FTjBzxhG6RN%2FvJaA9yQh%2Ba4TlQNBTLKPWlyMbF3xiuE%2FbveAUq%2B0WbFVaQu3%2FNCxQQo%2FKy3u2TTcfCvFvOgYPEcgyGAlSr1eRwavfCdLP5Zd5Lj7ogy%2FYJODQLW3mJB4HQ5GQg%2Fk8g2oq8ljm2q76tUR%2FAIdmKTdE086D0jGjA06gkGaCIpNOI3XtylYWeXNz7StzU9YXdvLDwCoK9nmbFl9ZPzxila50In8QM0ijCZ%2BKtpbMxTgYADNFpLSn83h5QqWYblFCDbK%2FeIrEhf2J5bifFrGorJthYkqheCfDh6TBU32Ex16ddTKo3NHJlHAsPIg%2B9q0VRd%2Bt5QEUXTk68nJSWee9NQzGomkbVhdL0fA6YZcQTdMfT5LytlDgeZeb%2B4z0DD8IVeSJ4JKDf2ZV7NH0EWRgiDEcTBr5MeNnjECU%2FdQXEb1jWwiRhmbrr8AIi7hfHSn0uXOSz2uXoHN1NKCoX4ggTxhHYL6ERTmZPlY6jpLS0AF73fyyGQo90anVIRQZ7Yyt6B0OBo9VbsErMLjDqswGOqUBx5RmY1HIMQZlzqYIPqvul19HksLZCK1ZVVLjz5zktNAKuefhPXIYeIP6pKDzjr8f8EWrQHNiFP7H74gxFcBCDM7aYnTVxtAehKuIxQ1qlqhOdi%2Fx7FLBP8ZcxTl%2BmAdPrDBeDaBv0byt2u%2FheGvqJdVnWQvLyfBC94pMW5DgvU4imIXwJBr%2FhCBe9pYl%2FWOdGZoI1QdqZifovc671O9csggN6j0E&X-Amz-Signature=272e98049afd69e8da002b93fda8e0de7f3fb9322bb4fae7f767e0c7d6abfc9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X26WFBJL%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzuhExZ6uJote%2FcGLGXrIEM9r5jjixKgZx%2BNLuNiaBdAiEA3O4kko3yL%2FHkgjtvf6V6UpxVrpRCoI%2BatOi7jG1aGTYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6dbWxqZTJcg2hJJCrcA3cGHGUCNnbujhw5cKa0cWwzdUDePNjb4M9jL1FNSeAOY%2BaqzLRcoqddhEYqK4i5oatj3svLGWcfgLPD%2FLYcTDxNdM%2Fad7gLZupjD63%2FTjBzxhG6RN%2FvJaA9yQh%2Ba4TlQNBTLKPWlyMbF3xiuE%2FbveAUq%2B0WbFVaQu3%2FNCxQQo%2FKy3u2TTcfCvFvOgYPEcgyGAlSr1eRwavfCdLP5Zd5Lj7ogy%2FYJODQLW3mJB4HQ5GQg%2Fk8g2oq8ljm2q76tUR%2FAIdmKTdE086D0jGjA06gkGaCIpNOI3XtylYWeXNz7StzU9YXdvLDwCoK9nmbFl9ZPzxila50In8QM0ijCZ%2BKtpbMxTgYADNFpLSn83h5QqWYblFCDbK%2FeIrEhf2J5bifFrGorJthYkqheCfDh6TBU32Ex16ddTKo3NHJlHAsPIg%2B9q0VRd%2Bt5QEUXTk68nJSWee9NQzGomkbVhdL0fA6YZcQTdMfT5LytlDgeZeb%2B4z0DD8IVeSJ4JKDf2ZV7NH0EWRgiDEcTBr5MeNnjECU%2FdQXEb1jWwiRhmbrr8AIi7hfHSn0uXOSz2uXoHN1NKCoX4ggTxhHYL6ERTmZPlY6jpLS0AF73fyyGQo90anVIRQZ7Yyt6B0OBo9VbsErMLjDqswGOqUBx5RmY1HIMQZlzqYIPqvul19HksLZCK1ZVVLjz5zktNAKuefhPXIYeIP6pKDzjr8f8EWrQHNiFP7H74gxFcBCDM7aYnTVxtAehKuIxQ1qlqhOdi%2Fx7FLBP8ZcxTl%2BmAdPrDBeDaBv0byt2u%2FheGvqJdVnWQvLyfBC94pMW5DgvU4imIXwJBr%2FhCBe9pYl%2FWOdGZoI1QdqZifovc671O9csggN6j0E&X-Amz-Signature=409e8835263b4d1c6ace41b2ac6e3dd46e25395b199b01a3a93c44561993c591&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X26WFBJL%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzuhExZ6uJote%2FcGLGXrIEM9r5jjixKgZx%2BNLuNiaBdAiEA3O4kko3yL%2FHkgjtvf6V6UpxVrpRCoI%2BatOi7jG1aGTYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6dbWxqZTJcg2hJJCrcA3cGHGUCNnbujhw5cKa0cWwzdUDePNjb4M9jL1FNSeAOY%2BaqzLRcoqddhEYqK4i5oatj3svLGWcfgLPD%2FLYcTDxNdM%2Fad7gLZupjD63%2FTjBzxhG6RN%2FvJaA9yQh%2Ba4TlQNBTLKPWlyMbF3xiuE%2FbveAUq%2B0WbFVaQu3%2FNCxQQo%2FKy3u2TTcfCvFvOgYPEcgyGAlSr1eRwavfCdLP5Zd5Lj7ogy%2FYJODQLW3mJB4HQ5GQg%2Fk8g2oq8ljm2q76tUR%2FAIdmKTdE086D0jGjA06gkGaCIpNOI3XtylYWeXNz7StzU9YXdvLDwCoK9nmbFl9ZPzxila50In8QM0ijCZ%2BKtpbMxTgYADNFpLSn83h5QqWYblFCDbK%2FeIrEhf2J5bifFrGorJthYkqheCfDh6TBU32Ex16ddTKo3NHJlHAsPIg%2B9q0VRd%2Bt5QEUXTk68nJSWee9NQzGomkbVhdL0fA6YZcQTdMfT5LytlDgeZeb%2B4z0DD8IVeSJ4JKDf2ZV7NH0EWRgiDEcTBr5MeNnjECU%2FdQXEb1jWwiRhmbrr8AIi7hfHSn0uXOSz2uXoHN1NKCoX4ggTxhHYL6ERTmZPlY6jpLS0AF73fyyGQo90anVIRQZ7Yyt6B0OBo9VbsErMLjDqswGOqUBx5RmY1HIMQZlzqYIPqvul19HksLZCK1ZVVLjz5zktNAKuefhPXIYeIP6pKDzjr8f8EWrQHNiFP7H74gxFcBCDM7aYnTVxtAehKuIxQ1qlqhOdi%2Fx7FLBP8ZcxTl%2BmAdPrDBeDaBv0byt2u%2FheGvqJdVnWQvLyfBC94pMW5DgvU4imIXwJBr%2FhCBe9pYl%2FWOdGZoI1QdqZifovc671O9csggN6j0E&X-Amz-Signature=c474461637b30d22685cae767ecef0a9ab8d50026e4fd33cb8e2ee6c1765eddc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X26WFBJL%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzuhExZ6uJote%2FcGLGXrIEM9r5jjixKgZx%2BNLuNiaBdAiEA3O4kko3yL%2FHkgjtvf6V6UpxVrpRCoI%2BatOi7jG1aGTYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6dbWxqZTJcg2hJJCrcA3cGHGUCNnbujhw5cKa0cWwzdUDePNjb4M9jL1FNSeAOY%2BaqzLRcoqddhEYqK4i5oatj3svLGWcfgLPD%2FLYcTDxNdM%2Fad7gLZupjD63%2FTjBzxhG6RN%2FvJaA9yQh%2Ba4TlQNBTLKPWlyMbF3xiuE%2FbveAUq%2B0WbFVaQu3%2FNCxQQo%2FKy3u2TTcfCvFvOgYPEcgyGAlSr1eRwavfCdLP5Zd5Lj7ogy%2FYJODQLW3mJB4HQ5GQg%2Fk8g2oq8ljm2q76tUR%2FAIdmKTdE086D0jGjA06gkGaCIpNOI3XtylYWeXNz7StzU9YXdvLDwCoK9nmbFl9ZPzxila50In8QM0ijCZ%2BKtpbMxTgYADNFpLSn83h5QqWYblFCDbK%2FeIrEhf2J5bifFrGorJthYkqheCfDh6TBU32Ex16ddTKo3NHJlHAsPIg%2B9q0VRd%2Bt5QEUXTk68nJSWee9NQzGomkbVhdL0fA6YZcQTdMfT5LytlDgeZeb%2B4z0DD8IVeSJ4JKDf2ZV7NH0EWRgiDEcTBr5MeNnjECU%2FdQXEb1jWwiRhmbrr8AIi7hfHSn0uXOSz2uXoHN1NKCoX4ggTxhHYL6ERTmZPlY6jpLS0AF73fyyGQo90anVIRQZ7Yyt6B0OBo9VbsErMLjDqswGOqUBx5RmY1HIMQZlzqYIPqvul19HksLZCK1ZVVLjz5zktNAKuefhPXIYeIP6pKDzjr8f8EWrQHNiFP7H74gxFcBCDM7aYnTVxtAehKuIxQ1qlqhOdi%2Fx7FLBP8ZcxTl%2BmAdPrDBeDaBv0byt2u%2FheGvqJdVnWQvLyfBC94pMW5DgvU4imIXwJBr%2FhCBe9pYl%2FWOdGZoI1QdqZifovc671O9csggN6j0E&X-Amz-Signature=09fe8cc521b0b677e9b175c00b17947b6597b170b06443bcc78e3d506a75c869&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X26WFBJL%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzuhExZ6uJote%2FcGLGXrIEM9r5jjixKgZx%2BNLuNiaBdAiEA3O4kko3yL%2FHkgjtvf6V6UpxVrpRCoI%2BatOi7jG1aGTYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6dbWxqZTJcg2hJJCrcA3cGHGUCNnbujhw5cKa0cWwzdUDePNjb4M9jL1FNSeAOY%2BaqzLRcoqddhEYqK4i5oatj3svLGWcfgLPD%2FLYcTDxNdM%2Fad7gLZupjD63%2FTjBzxhG6RN%2FvJaA9yQh%2Ba4TlQNBTLKPWlyMbF3xiuE%2FbveAUq%2B0WbFVaQu3%2FNCxQQo%2FKy3u2TTcfCvFvOgYPEcgyGAlSr1eRwavfCdLP5Zd5Lj7ogy%2FYJODQLW3mJB4HQ5GQg%2Fk8g2oq8ljm2q76tUR%2FAIdmKTdE086D0jGjA06gkGaCIpNOI3XtylYWeXNz7StzU9YXdvLDwCoK9nmbFl9ZPzxila50In8QM0ijCZ%2BKtpbMxTgYADNFpLSn83h5QqWYblFCDbK%2FeIrEhf2J5bifFrGorJthYkqheCfDh6TBU32Ex16ddTKo3NHJlHAsPIg%2B9q0VRd%2Bt5QEUXTk68nJSWee9NQzGomkbVhdL0fA6YZcQTdMfT5LytlDgeZeb%2B4z0DD8IVeSJ4JKDf2ZV7NH0EWRgiDEcTBr5MeNnjECU%2FdQXEb1jWwiRhmbrr8AIi7hfHSn0uXOSz2uXoHN1NKCoX4ggTxhHYL6ERTmZPlY6jpLS0AF73fyyGQo90anVIRQZ7Yyt6B0OBo9VbsErMLjDqswGOqUBx5RmY1HIMQZlzqYIPqvul19HksLZCK1ZVVLjz5zktNAKuefhPXIYeIP6pKDzjr8f8EWrQHNiFP7H74gxFcBCDM7aYnTVxtAehKuIxQ1qlqhOdi%2Fx7FLBP8ZcxTl%2BmAdPrDBeDaBv0byt2u%2FheGvqJdVnWQvLyfBC94pMW5DgvU4imIXwJBr%2FhCBe9pYl%2FWOdGZoI1QdqZifovc671O9csggN6j0E&X-Amz-Signature=b2bb92c97ce278d7ef08b566b1a2c684cbfa721189b7034cb50ab43af611e136&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X26WFBJL%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzuhExZ6uJote%2FcGLGXrIEM9r5jjixKgZx%2BNLuNiaBdAiEA3O4kko3yL%2FHkgjtvf6V6UpxVrpRCoI%2BatOi7jG1aGTYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6dbWxqZTJcg2hJJCrcA3cGHGUCNnbujhw5cKa0cWwzdUDePNjb4M9jL1FNSeAOY%2BaqzLRcoqddhEYqK4i5oatj3svLGWcfgLPD%2FLYcTDxNdM%2Fad7gLZupjD63%2FTjBzxhG6RN%2FvJaA9yQh%2Ba4TlQNBTLKPWlyMbF3xiuE%2FbveAUq%2B0WbFVaQu3%2FNCxQQo%2FKy3u2TTcfCvFvOgYPEcgyGAlSr1eRwavfCdLP5Zd5Lj7ogy%2FYJODQLW3mJB4HQ5GQg%2Fk8g2oq8ljm2q76tUR%2FAIdmKTdE086D0jGjA06gkGaCIpNOI3XtylYWeXNz7StzU9YXdvLDwCoK9nmbFl9ZPzxila50In8QM0ijCZ%2BKtpbMxTgYADNFpLSn83h5QqWYblFCDbK%2FeIrEhf2J5bifFrGorJthYkqheCfDh6TBU32Ex16ddTKo3NHJlHAsPIg%2B9q0VRd%2Bt5QEUXTk68nJSWee9NQzGomkbVhdL0fA6YZcQTdMfT5LytlDgeZeb%2B4z0DD8IVeSJ4JKDf2ZV7NH0EWRgiDEcTBr5MeNnjECU%2FdQXEb1jWwiRhmbrr8AIi7hfHSn0uXOSz2uXoHN1NKCoX4ggTxhHYL6ERTmZPlY6jpLS0AF73fyyGQo90anVIRQZ7Yyt6B0OBo9VbsErMLjDqswGOqUBx5RmY1HIMQZlzqYIPqvul19HksLZCK1ZVVLjz5zktNAKuefhPXIYeIP6pKDzjr8f8EWrQHNiFP7H74gxFcBCDM7aYnTVxtAehKuIxQ1qlqhOdi%2Fx7FLBP8ZcxTl%2BmAdPrDBeDaBv0byt2u%2FheGvqJdVnWQvLyfBC94pMW5DgvU4imIXwJBr%2FhCBe9pYl%2FWOdGZoI1QdqZifovc671O9csggN6j0E&X-Amz-Signature=9516405a121f6ba8f9a91bd118243335a0dde85e26d25a9c4e8afe854ada35d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X26WFBJL%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzuhExZ6uJote%2FcGLGXrIEM9r5jjixKgZx%2BNLuNiaBdAiEA3O4kko3yL%2FHkgjtvf6V6UpxVrpRCoI%2BatOi7jG1aGTYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6dbWxqZTJcg2hJJCrcA3cGHGUCNnbujhw5cKa0cWwzdUDePNjb4M9jL1FNSeAOY%2BaqzLRcoqddhEYqK4i5oatj3svLGWcfgLPD%2FLYcTDxNdM%2Fad7gLZupjD63%2FTjBzxhG6RN%2FvJaA9yQh%2Ba4TlQNBTLKPWlyMbF3xiuE%2FbveAUq%2B0WbFVaQu3%2FNCxQQo%2FKy3u2TTcfCvFvOgYPEcgyGAlSr1eRwavfCdLP5Zd5Lj7ogy%2FYJODQLW3mJB4HQ5GQg%2Fk8g2oq8ljm2q76tUR%2FAIdmKTdE086D0jGjA06gkGaCIpNOI3XtylYWeXNz7StzU9YXdvLDwCoK9nmbFl9ZPzxila50In8QM0ijCZ%2BKtpbMxTgYADNFpLSn83h5QqWYblFCDbK%2FeIrEhf2J5bifFrGorJthYkqheCfDh6TBU32Ex16ddTKo3NHJlHAsPIg%2B9q0VRd%2Bt5QEUXTk68nJSWee9NQzGomkbVhdL0fA6YZcQTdMfT5LytlDgeZeb%2B4z0DD8IVeSJ4JKDf2ZV7NH0EWRgiDEcTBr5MeNnjECU%2FdQXEb1jWwiRhmbrr8AIi7hfHSn0uXOSz2uXoHN1NKCoX4ggTxhHYL6ERTmZPlY6jpLS0AF73fyyGQo90anVIRQZ7Yyt6B0OBo9VbsErMLjDqswGOqUBx5RmY1HIMQZlzqYIPqvul19HksLZCK1ZVVLjz5zktNAKuefhPXIYeIP6pKDzjr8f8EWrQHNiFP7H74gxFcBCDM7aYnTVxtAehKuIxQ1qlqhOdi%2Fx7FLBP8ZcxTl%2BmAdPrDBeDaBv0byt2u%2FheGvqJdVnWQvLyfBC94pMW5DgvU4imIXwJBr%2FhCBe9pYl%2FWOdGZoI1QdqZifovc671O9csggN6j0E&X-Amz-Signature=75d1f2927ab67ea3ecabbc676195273180cfc88c0a210c31d713868d980ecb3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X26WFBJL%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzuhExZ6uJote%2FcGLGXrIEM9r5jjixKgZx%2BNLuNiaBdAiEA3O4kko3yL%2FHkgjtvf6V6UpxVrpRCoI%2BatOi7jG1aGTYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6dbWxqZTJcg2hJJCrcA3cGHGUCNnbujhw5cKa0cWwzdUDePNjb4M9jL1FNSeAOY%2BaqzLRcoqddhEYqK4i5oatj3svLGWcfgLPD%2FLYcTDxNdM%2Fad7gLZupjD63%2FTjBzxhG6RN%2FvJaA9yQh%2Ba4TlQNBTLKPWlyMbF3xiuE%2FbveAUq%2B0WbFVaQu3%2FNCxQQo%2FKy3u2TTcfCvFvOgYPEcgyGAlSr1eRwavfCdLP5Zd5Lj7ogy%2FYJODQLW3mJB4HQ5GQg%2Fk8g2oq8ljm2q76tUR%2FAIdmKTdE086D0jGjA06gkGaCIpNOI3XtylYWeXNz7StzU9YXdvLDwCoK9nmbFl9ZPzxila50In8QM0ijCZ%2BKtpbMxTgYADNFpLSn83h5QqWYblFCDbK%2FeIrEhf2J5bifFrGorJthYkqheCfDh6TBU32Ex16ddTKo3NHJlHAsPIg%2B9q0VRd%2Bt5QEUXTk68nJSWee9NQzGomkbVhdL0fA6YZcQTdMfT5LytlDgeZeb%2B4z0DD8IVeSJ4JKDf2ZV7NH0EWRgiDEcTBr5MeNnjECU%2FdQXEb1jWwiRhmbrr8AIi7hfHSn0uXOSz2uXoHN1NKCoX4ggTxhHYL6ERTmZPlY6jpLS0AF73fyyGQo90anVIRQZ7Yyt6B0OBo9VbsErMLjDqswGOqUBx5RmY1HIMQZlzqYIPqvul19HksLZCK1ZVVLjz5zktNAKuefhPXIYeIP6pKDzjr8f8EWrQHNiFP7H74gxFcBCDM7aYnTVxtAehKuIxQ1qlqhOdi%2Fx7FLBP8ZcxTl%2BmAdPrDBeDaBv0byt2u%2FheGvqJdVnWQvLyfBC94pMW5DgvU4imIXwJBr%2FhCBe9pYl%2FWOdGZoI1QdqZifovc671O9csggN6j0E&X-Amz-Signature=764320db8295013d31922764bf58a17c43379b88ca2c59c68f4b87fe6261b363&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X26WFBJL%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzuhExZ6uJote%2FcGLGXrIEM9r5jjixKgZx%2BNLuNiaBdAiEA3O4kko3yL%2FHkgjtvf6V6UpxVrpRCoI%2BatOi7jG1aGTYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6dbWxqZTJcg2hJJCrcA3cGHGUCNnbujhw5cKa0cWwzdUDePNjb4M9jL1FNSeAOY%2BaqzLRcoqddhEYqK4i5oatj3svLGWcfgLPD%2FLYcTDxNdM%2Fad7gLZupjD63%2FTjBzxhG6RN%2FvJaA9yQh%2Ba4TlQNBTLKPWlyMbF3xiuE%2FbveAUq%2B0WbFVaQu3%2FNCxQQo%2FKy3u2TTcfCvFvOgYPEcgyGAlSr1eRwavfCdLP5Zd5Lj7ogy%2FYJODQLW3mJB4HQ5GQg%2Fk8g2oq8ljm2q76tUR%2FAIdmKTdE086D0jGjA06gkGaCIpNOI3XtylYWeXNz7StzU9YXdvLDwCoK9nmbFl9ZPzxila50In8QM0ijCZ%2BKtpbMxTgYADNFpLSn83h5QqWYblFCDbK%2FeIrEhf2J5bifFrGorJthYkqheCfDh6TBU32Ex16ddTKo3NHJlHAsPIg%2B9q0VRd%2Bt5QEUXTk68nJSWee9NQzGomkbVhdL0fA6YZcQTdMfT5LytlDgeZeb%2B4z0DD8IVeSJ4JKDf2ZV7NH0EWRgiDEcTBr5MeNnjECU%2FdQXEb1jWwiRhmbrr8AIi7hfHSn0uXOSz2uXoHN1NKCoX4ggTxhHYL6ERTmZPlY6jpLS0AF73fyyGQo90anVIRQZ7Yyt6B0OBo9VbsErMLjDqswGOqUBx5RmY1HIMQZlzqYIPqvul19HksLZCK1ZVVLjz5zktNAKuefhPXIYeIP6pKDzjr8f8EWrQHNiFP7H74gxFcBCDM7aYnTVxtAehKuIxQ1qlqhOdi%2Fx7FLBP8ZcxTl%2BmAdPrDBeDaBv0byt2u%2FheGvqJdVnWQvLyfBC94pMW5DgvU4imIXwJBr%2FhCBe9pYl%2FWOdGZoI1QdqZifovc671O9csggN6j0E&X-Amz-Signature=c27eac9645a00da821df6522f2b87bfe9396adf02706faaaaaa711072af67887&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X26WFBJL%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzuhExZ6uJote%2FcGLGXrIEM9r5jjixKgZx%2BNLuNiaBdAiEA3O4kko3yL%2FHkgjtvf6V6UpxVrpRCoI%2BatOi7jG1aGTYqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6dbWxqZTJcg2hJJCrcA3cGHGUCNnbujhw5cKa0cWwzdUDePNjb4M9jL1FNSeAOY%2BaqzLRcoqddhEYqK4i5oatj3svLGWcfgLPD%2FLYcTDxNdM%2Fad7gLZupjD63%2FTjBzxhG6RN%2FvJaA9yQh%2Ba4TlQNBTLKPWlyMbF3xiuE%2FbveAUq%2B0WbFVaQu3%2FNCxQQo%2FKy3u2TTcfCvFvOgYPEcgyGAlSr1eRwavfCdLP5Zd5Lj7ogy%2FYJODQLW3mJB4HQ5GQg%2Fk8g2oq8ljm2q76tUR%2FAIdmKTdE086D0jGjA06gkGaCIpNOI3XtylYWeXNz7StzU9YXdvLDwCoK9nmbFl9ZPzxila50In8QM0ijCZ%2BKtpbMxTgYADNFpLSn83h5QqWYblFCDbK%2FeIrEhf2J5bifFrGorJthYkqheCfDh6TBU32Ex16ddTKo3NHJlHAsPIg%2B9q0VRd%2Bt5QEUXTk68nJSWee9NQzGomkbVhdL0fA6YZcQTdMfT5LytlDgeZeb%2B4z0DD8IVeSJ4JKDf2ZV7NH0EWRgiDEcTBr5MeNnjECU%2FdQXEb1jWwiRhmbrr8AIi7hfHSn0uXOSz2uXoHN1NKCoX4ggTxhHYL6ERTmZPlY6jpLS0AF73fyyGQo90anVIRQZ7Yyt6B0OBo9VbsErMLjDqswGOqUBx5RmY1HIMQZlzqYIPqvul19HksLZCK1ZVVLjz5zktNAKuefhPXIYeIP6pKDzjr8f8EWrQHNiFP7H74gxFcBCDM7aYnTVxtAehKuIxQ1qlqhOdi%2Fx7FLBP8ZcxTl%2BmAdPrDBeDaBv0byt2u%2FheGvqJdVnWQvLyfBC94pMW5DgvU4imIXwJBr%2FhCBe9pYl%2FWOdGZoI1QdqZifovc671O9csggN6j0E&X-Amz-Signature=fd64ba505fe34dbe7eb9fc7d33712687c12100efedb37793f248de8da4eb4885&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

