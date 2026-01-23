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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAWOTT7%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHkNXyGoSOjzubp7TYm03lXQ7djzKcUR31mGc8%2BErQVqAiAKLT%2B%2FmONkhESRV7eejREBKjtLkEH5vpGvgMR%2BVyeC8SqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeZp%2F8WKL1wpGxJ%2FdKtwDOqUta1B3EkIt2J8hnXI%2BWz3CxejpkDEly40E6mGto5eNnqL%2FHJXGpyn2RvL2w3%2B1feKePvXU%2FHbuu9r%2Fq%2BsONvUL2Xg4zjSYOTyQXf9jMUFs0v491PWfSZKQ3ikxphL4ZiNUYQxXFkJNWt2hPW%2BlMopyT0DuZezJDuSzMg%2BAbktiwZuTzRVzebbjAlqw771ZL1TsAMORiAaF2%2FmEwzLfuhUvUnoaGqEgV%2BgUr9nlLZPjHDDNvqNnOluy8t3%2Fd4pJRGFA0e3qv7%2BvjpSwxz6ojMTmTSXko%2FwTdriM1Ezh8cjjqwfhDDzNWzacUMa2AfBYsbTESY1tmzd2zzOAGVhjLeeIgV5Fi52rfKqv9qpG4sVZ7sOIMKR4l1dJq0AVxnsFrQi%2BqmKMSmdsG320xGtkzQkuzcspuXAszCTmbQ7yI6Q3OpApWYrTLMUcYrsUx4%2B1rXYFC8dRcQCslKGvh4mLW58aQoKXxtWQu0mDLRRK8aC%2BTPmloV61BcPfpVU8JvoIBFztbVW48FDhXpJVLw9hJRNZ%2BaDDJw015QTxQHI%2BazA2JEMVWABW0r8Rf1kX6U7OkvIfFyqqKaZ9YSt0pSfOFnaiexjeFG0i%2FMFySq2JUOSS4N0uyRufKwn9QPwwxa%2FLywY6pgH2BJOVAvEUt3sPw58WFRvs69FVx%2BkizDPENesfxoBFCilm3PQXopQDrVJDw%2Fvpdp85Y%2FQ6SjNcsjeFquhSOAdFLumnKoM%2FhDSHBtYsoVpDlET%2BnjS%2BBicQDinwbNVcqzJUZV1EhezJjC9UJ5xCrgZ3o%2BBo3QwIGoLNj1wYMvB7AzYTiGASpqcbtf64%2FGmU78SyUMPODQquhI%2B0RqMtwtwn3l9gwwC4&X-Amz-Signature=f0ab094f7905128c8f5b88b995cc00f710d753bf90b168e7315f5a366ec0f4b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAWOTT7%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHkNXyGoSOjzubp7TYm03lXQ7djzKcUR31mGc8%2BErQVqAiAKLT%2B%2FmONkhESRV7eejREBKjtLkEH5vpGvgMR%2BVyeC8SqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeZp%2F8WKL1wpGxJ%2FdKtwDOqUta1B3EkIt2J8hnXI%2BWz3CxejpkDEly40E6mGto5eNnqL%2FHJXGpyn2RvL2w3%2B1feKePvXU%2FHbuu9r%2Fq%2BsONvUL2Xg4zjSYOTyQXf9jMUFs0v491PWfSZKQ3ikxphL4ZiNUYQxXFkJNWt2hPW%2BlMopyT0DuZezJDuSzMg%2BAbktiwZuTzRVzebbjAlqw771ZL1TsAMORiAaF2%2FmEwzLfuhUvUnoaGqEgV%2BgUr9nlLZPjHDDNvqNnOluy8t3%2Fd4pJRGFA0e3qv7%2BvjpSwxz6ojMTmTSXko%2FwTdriM1Ezh8cjjqwfhDDzNWzacUMa2AfBYsbTESY1tmzd2zzOAGVhjLeeIgV5Fi52rfKqv9qpG4sVZ7sOIMKR4l1dJq0AVxnsFrQi%2BqmKMSmdsG320xGtkzQkuzcspuXAszCTmbQ7yI6Q3OpApWYrTLMUcYrsUx4%2B1rXYFC8dRcQCslKGvh4mLW58aQoKXxtWQu0mDLRRK8aC%2BTPmloV61BcPfpVU8JvoIBFztbVW48FDhXpJVLw9hJRNZ%2BaDDJw015QTxQHI%2BazA2JEMVWABW0r8Rf1kX6U7OkvIfFyqqKaZ9YSt0pSfOFnaiexjeFG0i%2FMFySq2JUOSS4N0uyRufKwn9QPwwxa%2FLywY6pgH2BJOVAvEUt3sPw58WFRvs69FVx%2BkizDPENesfxoBFCilm3PQXopQDrVJDw%2Fvpdp85Y%2FQ6SjNcsjeFquhSOAdFLumnKoM%2FhDSHBtYsoVpDlET%2BnjS%2BBicQDinwbNVcqzJUZV1EhezJjC9UJ5xCrgZ3o%2BBo3QwIGoLNj1wYMvB7AzYTiGASpqcbtf64%2FGmU78SyUMPODQquhI%2B0RqMtwtwn3l9gwwC4&X-Amz-Signature=8997ba99e258b74215690215522a5935dea2d4475b840538bc664df171fcbf26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAWOTT7%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHkNXyGoSOjzubp7TYm03lXQ7djzKcUR31mGc8%2BErQVqAiAKLT%2B%2FmONkhESRV7eejREBKjtLkEH5vpGvgMR%2BVyeC8SqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeZp%2F8WKL1wpGxJ%2FdKtwDOqUta1B3EkIt2J8hnXI%2BWz3CxejpkDEly40E6mGto5eNnqL%2FHJXGpyn2RvL2w3%2B1feKePvXU%2FHbuu9r%2Fq%2BsONvUL2Xg4zjSYOTyQXf9jMUFs0v491PWfSZKQ3ikxphL4ZiNUYQxXFkJNWt2hPW%2BlMopyT0DuZezJDuSzMg%2BAbktiwZuTzRVzebbjAlqw771ZL1TsAMORiAaF2%2FmEwzLfuhUvUnoaGqEgV%2BgUr9nlLZPjHDDNvqNnOluy8t3%2Fd4pJRGFA0e3qv7%2BvjpSwxz6ojMTmTSXko%2FwTdriM1Ezh8cjjqwfhDDzNWzacUMa2AfBYsbTESY1tmzd2zzOAGVhjLeeIgV5Fi52rfKqv9qpG4sVZ7sOIMKR4l1dJq0AVxnsFrQi%2BqmKMSmdsG320xGtkzQkuzcspuXAszCTmbQ7yI6Q3OpApWYrTLMUcYrsUx4%2B1rXYFC8dRcQCslKGvh4mLW58aQoKXxtWQu0mDLRRK8aC%2BTPmloV61BcPfpVU8JvoIBFztbVW48FDhXpJVLw9hJRNZ%2BaDDJw015QTxQHI%2BazA2JEMVWABW0r8Rf1kX6U7OkvIfFyqqKaZ9YSt0pSfOFnaiexjeFG0i%2FMFySq2JUOSS4N0uyRufKwn9QPwwxa%2FLywY6pgH2BJOVAvEUt3sPw58WFRvs69FVx%2BkizDPENesfxoBFCilm3PQXopQDrVJDw%2Fvpdp85Y%2FQ6SjNcsjeFquhSOAdFLumnKoM%2FhDSHBtYsoVpDlET%2BnjS%2BBicQDinwbNVcqzJUZV1EhezJjC9UJ5xCrgZ3o%2BBo3QwIGoLNj1wYMvB7AzYTiGASpqcbtf64%2FGmU78SyUMPODQquhI%2B0RqMtwtwn3l9gwwC4&X-Amz-Signature=d747344f8ee02b75807a1a0fad58b5c1fe27fe58895800295e75c01f9d4f5fea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAWOTT7%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHkNXyGoSOjzubp7TYm03lXQ7djzKcUR31mGc8%2BErQVqAiAKLT%2B%2FmONkhESRV7eejREBKjtLkEH5vpGvgMR%2BVyeC8SqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeZp%2F8WKL1wpGxJ%2FdKtwDOqUta1B3EkIt2J8hnXI%2BWz3CxejpkDEly40E6mGto5eNnqL%2FHJXGpyn2RvL2w3%2B1feKePvXU%2FHbuu9r%2Fq%2BsONvUL2Xg4zjSYOTyQXf9jMUFs0v491PWfSZKQ3ikxphL4ZiNUYQxXFkJNWt2hPW%2BlMopyT0DuZezJDuSzMg%2BAbktiwZuTzRVzebbjAlqw771ZL1TsAMORiAaF2%2FmEwzLfuhUvUnoaGqEgV%2BgUr9nlLZPjHDDNvqNnOluy8t3%2Fd4pJRGFA0e3qv7%2BvjpSwxz6ojMTmTSXko%2FwTdriM1Ezh8cjjqwfhDDzNWzacUMa2AfBYsbTESY1tmzd2zzOAGVhjLeeIgV5Fi52rfKqv9qpG4sVZ7sOIMKR4l1dJq0AVxnsFrQi%2BqmKMSmdsG320xGtkzQkuzcspuXAszCTmbQ7yI6Q3OpApWYrTLMUcYrsUx4%2B1rXYFC8dRcQCslKGvh4mLW58aQoKXxtWQu0mDLRRK8aC%2BTPmloV61BcPfpVU8JvoIBFztbVW48FDhXpJVLw9hJRNZ%2BaDDJw015QTxQHI%2BazA2JEMVWABW0r8Rf1kX6U7OkvIfFyqqKaZ9YSt0pSfOFnaiexjeFG0i%2FMFySq2JUOSS4N0uyRufKwn9QPwwxa%2FLywY6pgH2BJOVAvEUt3sPw58WFRvs69FVx%2BkizDPENesfxoBFCilm3PQXopQDrVJDw%2Fvpdp85Y%2FQ6SjNcsjeFquhSOAdFLumnKoM%2FhDSHBtYsoVpDlET%2BnjS%2BBicQDinwbNVcqzJUZV1EhezJjC9UJ5xCrgZ3o%2BBo3QwIGoLNj1wYMvB7AzYTiGASpqcbtf64%2FGmU78SyUMPODQquhI%2B0RqMtwtwn3l9gwwC4&X-Amz-Signature=becefe24d2fb715cc6c167f8aa984df366208e8be916615d8dd36b6b71a8b839&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAWOTT7%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHkNXyGoSOjzubp7TYm03lXQ7djzKcUR31mGc8%2BErQVqAiAKLT%2B%2FmONkhESRV7eejREBKjtLkEH5vpGvgMR%2BVyeC8SqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeZp%2F8WKL1wpGxJ%2FdKtwDOqUta1B3EkIt2J8hnXI%2BWz3CxejpkDEly40E6mGto5eNnqL%2FHJXGpyn2RvL2w3%2B1feKePvXU%2FHbuu9r%2Fq%2BsONvUL2Xg4zjSYOTyQXf9jMUFs0v491PWfSZKQ3ikxphL4ZiNUYQxXFkJNWt2hPW%2BlMopyT0DuZezJDuSzMg%2BAbktiwZuTzRVzebbjAlqw771ZL1TsAMORiAaF2%2FmEwzLfuhUvUnoaGqEgV%2BgUr9nlLZPjHDDNvqNnOluy8t3%2Fd4pJRGFA0e3qv7%2BvjpSwxz6ojMTmTSXko%2FwTdriM1Ezh8cjjqwfhDDzNWzacUMa2AfBYsbTESY1tmzd2zzOAGVhjLeeIgV5Fi52rfKqv9qpG4sVZ7sOIMKR4l1dJq0AVxnsFrQi%2BqmKMSmdsG320xGtkzQkuzcspuXAszCTmbQ7yI6Q3OpApWYrTLMUcYrsUx4%2B1rXYFC8dRcQCslKGvh4mLW58aQoKXxtWQu0mDLRRK8aC%2BTPmloV61BcPfpVU8JvoIBFztbVW48FDhXpJVLw9hJRNZ%2BaDDJw015QTxQHI%2BazA2JEMVWABW0r8Rf1kX6U7OkvIfFyqqKaZ9YSt0pSfOFnaiexjeFG0i%2FMFySq2JUOSS4N0uyRufKwn9QPwwxa%2FLywY6pgH2BJOVAvEUt3sPw58WFRvs69FVx%2BkizDPENesfxoBFCilm3PQXopQDrVJDw%2Fvpdp85Y%2FQ6SjNcsjeFquhSOAdFLumnKoM%2FhDSHBtYsoVpDlET%2BnjS%2BBicQDinwbNVcqzJUZV1EhezJjC9UJ5xCrgZ3o%2BBo3QwIGoLNj1wYMvB7AzYTiGASpqcbtf64%2FGmU78SyUMPODQquhI%2B0RqMtwtwn3l9gwwC4&X-Amz-Signature=51690cdb54f0c59214e3799ff2373a0bb09e1d0a4b5ec6bec667dd4d2bd9c10d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAWOTT7%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHkNXyGoSOjzubp7TYm03lXQ7djzKcUR31mGc8%2BErQVqAiAKLT%2B%2FmONkhESRV7eejREBKjtLkEH5vpGvgMR%2BVyeC8SqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeZp%2F8WKL1wpGxJ%2FdKtwDOqUta1B3EkIt2J8hnXI%2BWz3CxejpkDEly40E6mGto5eNnqL%2FHJXGpyn2RvL2w3%2B1feKePvXU%2FHbuu9r%2Fq%2BsONvUL2Xg4zjSYOTyQXf9jMUFs0v491PWfSZKQ3ikxphL4ZiNUYQxXFkJNWt2hPW%2BlMopyT0DuZezJDuSzMg%2BAbktiwZuTzRVzebbjAlqw771ZL1TsAMORiAaF2%2FmEwzLfuhUvUnoaGqEgV%2BgUr9nlLZPjHDDNvqNnOluy8t3%2Fd4pJRGFA0e3qv7%2BvjpSwxz6ojMTmTSXko%2FwTdriM1Ezh8cjjqwfhDDzNWzacUMa2AfBYsbTESY1tmzd2zzOAGVhjLeeIgV5Fi52rfKqv9qpG4sVZ7sOIMKR4l1dJq0AVxnsFrQi%2BqmKMSmdsG320xGtkzQkuzcspuXAszCTmbQ7yI6Q3OpApWYrTLMUcYrsUx4%2B1rXYFC8dRcQCslKGvh4mLW58aQoKXxtWQu0mDLRRK8aC%2BTPmloV61BcPfpVU8JvoIBFztbVW48FDhXpJVLw9hJRNZ%2BaDDJw015QTxQHI%2BazA2JEMVWABW0r8Rf1kX6U7OkvIfFyqqKaZ9YSt0pSfOFnaiexjeFG0i%2FMFySq2JUOSS4N0uyRufKwn9QPwwxa%2FLywY6pgH2BJOVAvEUt3sPw58WFRvs69FVx%2BkizDPENesfxoBFCilm3PQXopQDrVJDw%2Fvpdp85Y%2FQ6SjNcsjeFquhSOAdFLumnKoM%2FhDSHBtYsoVpDlET%2BnjS%2BBicQDinwbNVcqzJUZV1EhezJjC9UJ5xCrgZ3o%2BBo3QwIGoLNj1wYMvB7AzYTiGASpqcbtf64%2FGmU78SyUMPODQquhI%2B0RqMtwtwn3l9gwwC4&X-Amz-Signature=01c0e8f7770c6354d493ce0e9f3acfed0904a6bd76a4330d271eacd82d0a14a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAWOTT7%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHkNXyGoSOjzubp7TYm03lXQ7djzKcUR31mGc8%2BErQVqAiAKLT%2B%2FmONkhESRV7eejREBKjtLkEH5vpGvgMR%2BVyeC8SqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeZp%2F8WKL1wpGxJ%2FdKtwDOqUta1B3EkIt2J8hnXI%2BWz3CxejpkDEly40E6mGto5eNnqL%2FHJXGpyn2RvL2w3%2B1feKePvXU%2FHbuu9r%2Fq%2BsONvUL2Xg4zjSYOTyQXf9jMUFs0v491PWfSZKQ3ikxphL4ZiNUYQxXFkJNWt2hPW%2BlMopyT0DuZezJDuSzMg%2BAbktiwZuTzRVzebbjAlqw771ZL1TsAMORiAaF2%2FmEwzLfuhUvUnoaGqEgV%2BgUr9nlLZPjHDDNvqNnOluy8t3%2Fd4pJRGFA0e3qv7%2BvjpSwxz6ojMTmTSXko%2FwTdriM1Ezh8cjjqwfhDDzNWzacUMa2AfBYsbTESY1tmzd2zzOAGVhjLeeIgV5Fi52rfKqv9qpG4sVZ7sOIMKR4l1dJq0AVxnsFrQi%2BqmKMSmdsG320xGtkzQkuzcspuXAszCTmbQ7yI6Q3OpApWYrTLMUcYrsUx4%2B1rXYFC8dRcQCslKGvh4mLW58aQoKXxtWQu0mDLRRK8aC%2BTPmloV61BcPfpVU8JvoIBFztbVW48FDhXpJVLw9hJRNZ%2BaDDJw015QTxQHI%2BazA2JEMVWABW0r8Rf1kX6U7OkvIfFyqqKaZ9YSt0pSfOFnaiexjeFG0i%2FMFySq2JUOSS4N0uyRufKwn9QPwwxa%2FLywY6pgH2BJOVAvEUt3sPw58WFRvs69FVx%2BkizDPENesfxoBFCilm3PQXopQDrVJDw%2Fvpdp85Y%2FQ6SjNcsjeFquhSOAdFLumnKoM%2FhDSHBtYsoVpDlET%2BnjS%2BBicQDinwbNVcqzJUZV1EhezJjC9UJ5xCrgZ3o%2BBo3QwIGoLNj1wYMvB7AzYTiGASpqcbtf64%2FGmU78SyUMPODQquhI%2B0RqMtwtwn3l9gwwC4&X-Amz-Signature=c7553a06d8e5a91da473918e9fcaa4f48284a3b6fea3b32fbcd683c35345fb93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAWOTT7%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHkNXyGoSOjzubp7TYm03lXQ7djzKcUR31mGc8%2BErQVqAiAKLT%2B%2FmONkhESRV7eejREBKjtLkEH5vpGvgMR%2BVyeC8SqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeZp%2F8WKL1wpGxJ%2FdKtwDOqUta1B3EkIt2J8hnXI%2BWz3CxejpkDEly40E6mGto5eNnqL%2FHJXGpyn2RvL2w3%2B1feKePvXU%2FHbuu9r%2Fq%2BsONvUL2Xg4zjSYOTyQXf9jMUFs0v491PWfSZKQ3ikxphL4ZiNUYQxXFkJNWt2hPW%2BlMopyT0DuZezJDuSzMg%2BAbktiwZuTzRVzebbjAlqw771ZL1TsAMORiAaF2%2FmEwzLfuhUvUnoaGqEgV%2BgUr9nlLZPjHDDNvqNnOluy8t3%2Fd4pJRGFA0e3qv7%2BvjpSwxz6ojMTmTSXko%2FwTdriM1Ezh8cjjqwfhDDzNWzacUMa2AfBYsbTESY1tmzd2zzOAGVhjLeeIgV5Fi52rfKqv9qpG4sVZ7sOIMKR4l1dJq0AVxnsFrQi%2BqmKMSmdsG320xGtkzQkuzcspuXAszCTmbQ7yI6Q3OpApWYrTLMUcYrsUx4%2B1rXYFC8dRcQCslKGvh4mLW58aQoKXxtWQu0mDLRRK8aC%2BTPmloV61BcPfpVU8JvoIBFztbVW48FDhXpJVLw9hJRNZ%2BaDDJw015QTxQHI%2BazA2JEMVWABW0r8Rf1kX6U7OkvIfFyqqKaZ9YSt0pSfOFnaiexjeFG0i%2FMFySq2JUOSS4N0uyRufKwn9QPwwxa%2FLywY6pgH2BJOVAvEUt3sPw58WFRvs69FVx%2BkizDPENesfxoBFCilm3PQXopQDrVJDw%2Fvpdp85Y%2FQ6SjNcsjeFquhSOAdFLumnKoM%2FhDSHBtYsoVpDlET%2BnjS%2BBicQDinwbNVcqzJUZV1EhezJjC9UJ5xCrgZ3o%2BBo3QwIGoLNj1wYMvB7AzYTiGASpqcbtf64%2FGmU78SyUMPODQquhI%2B0RqMtwtwn3l9gwwC4&X-Amz-Signature=9e3352dcd217df7f0da540ef79e385f4fca084fac8378f75a300220266064a82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAWOTT7%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHkNXyGoSOjzubp7TYm03lXQ7djzKcUR31mGc8%2BErQVqAiAKLT%2B%2FmONkhESRV7eejREBKjtLkEH5vpGvgMR%2BVyeC8SqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeZp%2F8WKL1wpGxJ%2FdKtwDOqUta1B3EkIt2J8hnXI%2BWz3CxejpkDEly40E6mGto5eNnqL%2FHJXGpyn2RvL2w3%2B1feKePvXU%2FHbuu9r%2Fq%2BsONvUL2Xg4zjSYOTyQXf9jMUFs0v491PWfSZKQ3ikxphL4ZiNUYQxXFkJNWt2hPW%2BlMopyT0DuZezJDuSzMg%2BAbktiwZuTzRVzebbjAlqw771ZL1TsAMORiAaF2%2FmEwzLfuhUvUnoaGqEgV%2BgUr9nlLZPjHDDNvqNnOluy8t3%2Fd4pJRGFA0e3qv7%2BvjpSwxz6ojMTmTSXko%2FwTdriM1Ezh8cjjqwfhDDzNWzacUMa2AfBYsbTESY1tmzd2zzOAGVhjLeeIgV5Fi52rfKqv9qpG4sVZ7sOIMKR4l1dJq0AVxnsFrQi%2BqmKMSmdsG320xGtkzQkuzcspuXAszCTmbQ7yI6Q3OpApWYrTLMUcYrsUx4%2B1rXYFC8dRcQCslKGvh4mLW58aQoKXxtWQu0mDLRRK8aC%2BTPmloV61BcPfpVU8JvoIBFztbVW48FDhXpJVLw9hJRNZ%2BaDDJw015QTxQHI%2BazA2JEMVWABW0r8Rf1kX6U7OkvIfFyqqKaZ9YSt0pSfOFnaiexjeFG0i%2FMFySq2JUOSS4N0uyRufKwn9QPwwxa%2FLywY6pgH2BJOVAvEUt3sPw58WFRvs69FVx%2BkizDPENesfxoBFCilm3PQXopQDrVJDw%2Fvpdp85Y%2FQ6SjNcsjeFquhSOAdFLumnKoM%2FhDSHBtYsoVpDlET%2BnjS%2BBicQDinwbNVcqzJUZV1EhezJjC9UJ5xCrgZ3o%2BBo3QwIGoLNj1wYMvB7AzYTiGASpqcbtf64%2FGmU78SyUMPODQquhI%2B0RqMtwtwn3l9gwwC4&X-Amz-Signature=5918ad8ecc7f9dafae07b6523e710232abc39671ce9f5009cd3bd63de37d854e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YAWOTT7%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIHkNXyGoSOjzubp7TYm03lXQ7djzKcUR31mGc8%2BErQVqAiAKLT%2B%2FmONkhESRV7eejREBKjtLkEH5vpGvgMR%2BVyeC8SqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeZp%2F8WKL1wpGxJ%2FdKtwDOqUta1B3EkIt2J8hnXI%2BWz3CxejpkDEly40E6mGto5eNnqL%2FHJXGpyn2RvL2w3%2B1feKePvXU%2FHbuu9r%2Fq%2BsONvUL2Xg4zjSYOTyQXf9jMUFs0v491PWfSZKQ3ikxphL4ZiNUYQxXFkJNWt2hPW%2BlMopyT0DuZezJDuSzMg%2BAbktiwZuTzRVzebbjAlqw771ZL1TsAMORiAaF2%2FmEwzLfuhUvUnoaGqEgV%2BgUr9nlLZPjHDDNvqNnOluy8t3%2Fd4pJRGFA0e3qv7%2BvjpSwxz6ojMTmTSXko%2FwTdriM1Ezh8cjjqwfhDDzNWzacUMa2AfBYsbTESY1tmzd2zzOAGVhjLeeIgV5Fi52rfKqv9qpG4sVZ7sOIMKR4l1dJq0AVxnsFrQi%2BqmKMSmdsG320xGtkzQkuzcspuXAszCTmbQ7yI6Q3OpApWYrTLMUcYrsUx4%2B1rXYFC8dRcQCslKGvh4mLW58aQoKXxtWQu0mDLRRK8aC%2BTPmloV61BcPfpVU8JvoIBFztbVW48FDhXpJVLw9hJRNZ%2BaDDJw015QTxQHI%2BazA2JEMVWABW0r8Rf1kX6U7OkvIfFyqqKaZ9YSt0pSfOFnaiexjeFG0i%2FMFySq2JUOSS4N0uyRufKwn9QPwwxa%2FLywY6pgH2BJOVAvEUt3sPw58WFRvs69FVx%2BkizDPENesfxoBFCilm3PQXopQDrVJDw%2Fvpdp85Y%2FQ6SjNcsjeFquhSOAdFLumnKoM%2FhDSHBtYsoVpDlET%2BnjS%2BBicQDinwbNVcqzJUZV1EhezJjC9UJ5xCrgZ3o%2BBo3QwIGoLNj1wYMvB7AzYTiGASpqcbtf64%2FGmU78SyUMPODQquhI%2B0RqMtwtwn3l9gwwC4&X-Amz-Signature=eca297c197712e34a7a395f6a27520514f13628c4b8c01586c274989af9a7882&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

