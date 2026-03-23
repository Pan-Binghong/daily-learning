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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F43CG3E%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIlDhbC%2Fq676EiBaEL2jdMRKfqQxyCuHnni9ORsGAZjQIhAMndWLKXnld0uqyz9f810MGS%2BZPHvfECAVhhqXErR%2FVbKv8DCHQQABoMNjM3NDIzMTgzODA1Igw2%2B8RXVpbSQt%2F7O8kq3AMzhTFVS2MIWdo6UQQvDKI8rMA%2BjjlTbnkaEhurrQCAIczKKL7ksV8KRYVdPh49RFQOiOUJ2Eag8MkOJ63bRb1u0lJ1%2Fb2nCYw8qAs%2BU6AD7SqmZE2ZDls5dDpPNgmv9zcbOghGe7SznPAyXxCZMgOD1CwbxSmknBmPnLWm00uy05qZmqSzqiERl1b4sSvvnVXPBsBJkYG2fkiH51mo6GpiTiy2VOYps%2FWQaFDOplPE8Hi4ufOcEQGjU8hO5vOlSjnsWhXPEqXMlB3xmN%2FQxhEtTfOy2GDo96xrC66yJ%2FqnmOWr4pTVQb%2BPtYGiJU3DeymbzDebJwclCl4d3aAZRyOeuvmIzsOkS5BI1XDqmaLJ6w5W2u%2Fdf9JU4vcrhyKrAVpFzMN9f6uGQfMWAgg5cNe31K8f1CBE7p4i9e9ilPW5KWwnsG394pGzSw1tBlScAvArDbTWeKNemSLTXSOgUYhLyxy2V5qO0E09dd0HMKSsaMhuMJqBconNPEw9nssVxdHDESG5rU4%2BamEFmW8VC5bpkI8VwYgViF1v5N%2FCTttWOJ7rgz%2BNkFEEUNjQmG6nNukT2cWLmMYyPv%2FFfcLyPJ6XaJ0bCjX%2B8OPKaJ9LCkiR%2B3lijONljPIYXxYDRTDJ44LOBjqkAfly%2FfjlF58ynwEQKmhNhkix3H4fl4DrbUz%2BpkhYKj4M2J%2BJHetYRXWlsmsoaak9nnLenulND2GpKF5aoqbYsKadhmszQQ5JpJ21nSXXXdU7YlesCKqRG5g%2BaNO1NQOiTZSgH7XXH%2BHvRfb0b27U0l%2BKLJVKqKKB%2Fr2nAUBrGalXpz2upuetkO2zP1A26LcH2oPqhSCcIZKHRJluA1aMwcXU%2F2Yy&X-Amz-Signature=8d87274631156d5661ee259443dad6aab0e7e13533c4fd714440864bd3b928f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F43CG3E%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIlDhbC%2Fq676EiBaEL2jdMRKfqQxyCuHnni9ORsGAZjQIhAMndWLKXnld0uqyz9f810MGS%2BZPHvfECAVhhqXErR%2FVbKv8DCHQQABoMNjM3NDIzMTgzODA1Igw2%2B8RXVpbSQt%2F7O8kq3AMzhTFVS2MIWdo6UQQvDKI8rMA%2BjjlTbnkaEhurrQCAIczKKL7ksV8KRYVdPh49RFQOiOUJ2Eag8MkOJ63bRb1u0lJ1%2Fb2nCYw8qAs%2BU6AD7SqmZE2ZDls5dDpPNgmv9zcbOghGe7SznPAyXxCZMgOD1CwbxSmknBmPnLWm00uy05qZmqSzqiERl1b4sSvvnVXPBsBJkYG2fkiH51mo6GpiTiy2VOYps%2FWQaFDOplPE8Hi4ufOcEQGjU8hO5vOlSjnsWhXPEqXMlB3xmN%2FQxhEtTfOy2GDo96xrC66yJ%2FqnmOWr4pTVQb%2BPtYGiJU3DeymbzDebJwclCl4d3aAZRyOeuvmIzsOkS5BI1XDqmaLJ6w5W2u%2Fdf9JU4vcrhyKrAVpFzMN9f6uGQfMWAgg5cNe31K8f1CBE7p4i9e9ilPW5KWwnsG394pGzSw1tBlScAvArDbTWeKNemSLTXSOgUYhLyxy2V5qO0E09dd0HMKSsaMhuMJqBconNPEw9nssVxdHDESG5rU4%2BamEFmW8VC5bpkI8VwYgViF1v5N%2FCTttWOJ7rgz%2BNkFEEUNjQmG6nNukT2cWLmMYyPv%2FFfcLyPJ6XaJ0bCjX%2B8OPKaJ9LCkiR%2B3lijONljPIYXxYDRTDJ44LOBjqkAfly%2FfjlF58ynwEQKmhNhkix3H4fl4DrbUz%2BpkhYKj4M2J%2BJHetYRXWlsmsoaak9nnLenulND2GpKF5aoqbYsKadhmszQQ5JpJ21nSXXXdU7YlesCKqRG5g%2BaNO1NQOiTZSgH7XXH%2BHvRfb0b27U0l%2BKLJVKqKKB%2Fr2nAUBrGalXpz2upuetkO2zP1A26LcH2oPqhSCcIZKHRJluA1aMwcXU%2F2Yy&X-Amz-Signature=48e53b5f43d70efb96302af9e336ae6361f6aab0107db068064a56826ac8e8ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F43CG3E%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIlDhbC%2Fq676EiBaEL2jdMRKfqQxyCuHnni9ORsGAZjQIhAMndWLKXnld0uqyz9f810MGS%2BZPHvfECAVhhqXErR%2FVbKv8DCHQQABoMNjM3NDIzMTgzODA1Igw2%2B8RXVpbSQt%2F7O8kq3AMzhTFVS2MIWdo6UQQvDKI8rMA%2BjjlTbnkaEhurrQCAIczKKL7ksV8KRYVdPh49RFQOiOUJ2Eag8MkOJ63bRb1u0lJ1%2Fb2nCYw8qAs%2BU6AD7SqmZE2ZDls5dDpPNgmv9zcbOghGe7SznPAyXxCZMgOD1CwbxSmknBmPnLWm00uy05qZmqSzqiERl1b4sSvvnVXPBsBJkYG2fkiH51mo6GpiTiy2VOYps%2FWQaFDOplPE8Hi4ufOcEQGjU8hO5vOlSjnsWhXPEqXMlB3xmN%2FQxhEtTfOy2GDo96xrC66yJ%2FqnmOWr4pTVQb%2BPtYGiJU3DeymbzDebJwclCl4d3aAZRyOeuvmIzsOkS5BI1XDqmaLJ6w5W2u%2Fdf9JU4vcrhyKrAVpFzMN9f6uGQfMWAgg5cNe31K8f1CBE7p4i9e9ilPW5KWwnsG394pGzSw1tBlScAvArDbTWeKNemSLTXSOgUYhLyxy2V5qO0E09dd0HMKSsaMhuMJqBconNPEw9nssVxdHDESG5rU4%2BamEFmW8VC5bpkI8VwYgViF1v5N%2FCTttWOJ7rgz%2BNkFEEUNjQmG6nNukT2cWLmMYyPv%2FFfcLyPJ6XaJ0bCjX%2B8OPKaJ9LCkiR%2B3lijONljPIYXxYDRTDJ44LOBjqkAfly%2FfjlF58ynwEQKmhNhkix3H4fl4DrbUz%2BpkhYKj4M2J%2BJHetYRXWlsmsoaak9nnLenulND2GpKF5aoqbYsKadhmszQQ5JpJ21nSXXXdU7YlesCKqRG5g%2BaNO1NQOiTZSgH7XXH%2BHvRfb0b27U0l%2BKLJVKqKKB%2Fr2nAUBrGalXpz2upuetkO2zP1A26LcH2oPqhSCcIZKHRJluA1aMwcXU%2F2Yy&X-Amz-Signature=af8a91373afa943e1cf0dc82eff9c4a0a762fbcf9c913fd8d8c125508f8525e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F43CG3E%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIlDhbC%2Fq676EiBaEL2jdMRKfqQxyCuHnni9ORsGAZjQIhAMndWLKXnld0uqyz9f810MGS%2BZPHvfECAVhhqXErR%2FVbKv8DCHQQABoMNjM3NDIzMTgzODA1Igw2%2B8RXVpbSQt%2F7O8kq3AMzhTFVS2MIWdo6UQQvDKI8rMA%2BjjlTbnkaEhurrQCAIczKKL7ksV8KRYVdPh49RFQOiOUJ2Eag8MkOJ63bRb1u0lJ1%2Fb2nCYw8qAs%2BU6AD7SqmZE2ZDls5dDpPNgmv9zcbOghGe7SznPAyXxCZMgOD1CwbxSmknBmPnLWm00uy05qZmqSzqiERl1b4sSvvnVXPBsBJkYG2fkiH51mo6GpiTiy2VOYps%2FWQaFDOplPE8Hi4ufOcEQGjU8hO5vOlSjnsWhXPEqXMlB3xmN%2FQxhEtTfOy2GDo96xrC66yJ%2FqnmOWr4pTVQb%2BPtYGiJU3DeymbzDebJwclCl4d3aAZRyOeuvmIzsOkS5BI1XDqmaLJ6w5W2u%2Fdf9JU4vcrhyKrAVpFzMN9f6uGQfMWAgg5cNe31K8f1CBE7p4i9e9ilPW5KWwnsG394pGzSw1tBlScAvArDbTWeKNemSLTXSOgUYhLyxy2V5qO0E09dd0HMKSsaMhuMJqBconNPEw9nssVxdHDESG5rU4%2BamEFmW8VC5bpkI8VwYgViF1v5N%2FCTttWOJ7rgz%2BNkFEEUNjQmG6nNukT2cWLmMYyPv%2FFfcLyPJ6XaJ0bCjX%2B8OPKaJ9LCkiR%2B3lijONljPIYXxYDRTDJ44LOBjqkAfly%2FfjlF58ynwEQKmhNhkix3H4fl4DrbUz%2BpkhYKj4M2J%2BJHetYRXWlsmsoaak9nnLenulND2GpKF5aoqbYsKadhmszQQ5JpJ21nSXXXdU7YlesCKqRG5g%2BaNO1NQOiTZSgH7XXH%2BHvRfb0b27U0l%2BKLJVKqKKB%2Fr2nAUBrGalXpz2upuetkO2zP1A26LcH2oPqhSCcIZKHRJluA1aMwcXU%2F2Yy&X-Amz-Signature=c3ce78a91b071d499d891ae866a2723cfbcaec22305cec5631b1ddaa67c206a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F43CG3E%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIlDhbC%2Fq676EiBaEL2jdMRKfqQxyCuHnni9ORsGAZjQIhAMndWLKXnld0uqyz9f810MGS%2BZPHvfECAVhhqXErR%2FVbKv8DCHQQABoMNjM3NDIzMTgzODA1Igw2%2B8RXVpbSQt%2F7O8kq3AMzhTFVS2MIWdo6UQQvDKI8rMA%2BjjlTbnkaEhurrQCAIczKKL7ksV8KRYVdPh49RFQOiOUJ2Eag8MkOJ63bRb1u0lJ1%2Fb2nCYw8qAs%2BU6AD7SqmZE2ZDls5dDpPNgmv9zcbOghGe7SznPAyXxCZMgOD1CwbxSmknBmPnLWm00uy05qZmqSzqiERl1b4sSvvnVXPBsBJkYG2fkiH51mo6GpiTiy2VOYps%2FWQaFDOplPE8Hi4ufOcEQGjU8hO5vOlSjnsWhXPEqXMlB3xmN%2FQxhEtTfOy2GDo96xrC66yJ%2FqnmOWr4pTVQb%2BPtYGiJU3DeymbzDebJwclCl4d3aAZRyOeuvmIzsOkS5BI1XDqmaLJ6w5W2u%2Fdf9JU4vcrhyKrAVpFzMN9f6uGQfMWAgg5cNe31K8f1CBE7p4i9e9ilPW5KWwnsG394pGzSw1tBlScAvArDbTWeKNemSLTXSOgUYhLyxy2V5qO0E09dd0HMKSsaMhuMJqBconNPEw9nssVxdHDESG5rU4%2BamEFmW8VC5bpkI8VwYgViF1v5N%2FCTttWOJ7rgz%2BNkFEEUNjQmG6nNukT2cWLmMYyPv%2FFfcLyPJ6XaJ0bCjX%2B8OPKaJ9LCkiR%2B3lijONljPIYXxYDRTDJ44LOBjqkAfly%2FfjlF58ynwEQKmhNhkix3H4fl4DrbUz%2BpkhYKj4M2J%2BJHetYRXWlsmsoaak9nnLenulND2GpKF5aoqbYsKadhmszQQ5JpJ21nSXXXdU7YlesCKqRG5g%2BaNO1NQOiTZSgH7XXH%2BHvRfb0b27U0l%2BKLJVKqKKB%2Fr2nAUBrGalXpz2upuetkO2zP1A26LcH2oPqhSCcIZKHRJluA1aMwcXU%2F2Yy&X-Amz-Signature=eabc344d41cddb99fcca6b68d0424e7f81bfb3b5aca9669d88d8f11c73410f7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F43CG3E%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIlDhbC%2Fq676EiBaEL2jdMRKfqQxyCuHnni9ORsGAZjQIhAMndWLKXnld0uqyz9f810MGS%2BZPHvfECAVhhqXErR%2FVbKv8DCHQQABoMNjM3NDIzMTgzODA1Igw2%2B8RXVpbSQt%2F7O8kq3AMzhTFVS2MIWdo6UQQvDKI8rMA%2BjjlTbnkaEhurrQCAIczKKL7ksV8KRYVdPh49RFQOiOUJ2Eag8MkOJ63bRb1u0lJ1%2Fb2nCYw8qAs%2BU6AD7SqmZE2ZDls5dDpPNgmv9zcbOghGe7SznPAyXxCZMgOD1CwbxSmknBmPnLWm00uy05qZmqSzqiERl1b4sSvvnVXPBsBJkYG2fkiH51mo6GpiTiy2VOYps%2FWQaFDOplPE8Hi4ufOcEQGjU8hO5vOlSjnsWhXPEqXMlB3xmN%2FQxhEtTfOy2GDo96xrC66yJ%2FqnmOWr4pTVQb%2BPtYGiJU3DeymbzDebJwclCl4d3aAZRyOeuvmIzsOkS5BI1XDqmaLJ6w5W2u%2Fdf9JU4vcrhyKrAVpFzMN9f6uGQfMWAgg5cNe31K8f1CBE7p4i9e9ilPW5KWwnsG394pGzSw1tBlScAvArDbTWeKNemSLTXSOgUYhLyxy2V5qO0E09dd0HMKSsaMhuMJqBconNPEw9nssVxdHDESG5rU4%2BamEFmW8VC5bpkI8VwYgViF1v5N%2FCTttWOJ7rgz%2BNkFEEUNjQmG6nNukT2cWLmMYyPv%2FFfcLyPJ6XaJ0bCjX%2B8OPKaJ9LCkiR%2B3lijONljPIYXxYDRTDJ44LOBjqkAfly%2FfjlF58ynwEQKmhNhkix3H4fl4DrbUz%2BpkhYKj4M2J%2BJHetYRXWlsmsoaak9nnLenulND2GpKF5aoqbYsKadhmszQQ5JpJ21nSXXXdU7YlesCKqRG5g%2BaNO1NQOiTZSgH7XXH%2BHvRfb0b27U0l%2BKLJVKqKKB%2Fr2nAUBrGalXpz2upuetkO2zP1A26LcH2oPqhSCcIZKHRJluA1aMwcXU%2F2Yy&X-Amz-Signature=21b5318143b8a5bbc1e0eb074a3fdd383f4b67704e467d36088020164574725a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F43CG3E%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIlDhbC%2Fq676EiBaEL2jdMRKfqQxyCuHnni9ORsGAZjQIhAMndWLKXnld0uqyz9f810MGS%2BZPHvfECAVhhqXErR%2FVbKv8DCHQQABoMNjM3NDIzMTgzODA1Igw2%2B8RXVpbSQt%2F7O8kq3AMzhTFVS2MIWdo6UQQvDKI8rMA%2BjjlTbnkaEhurrQCAIczKKL7ksV8KRYVdPh49RFQOiOUJ2Eag8MkOJ63bRb1u0lJ1%2Fb2nCYw8qAs%2BU6AD7SqmZE2ZDls5dDpPNgmv9zcbOghGe7SznPAyXxCZMgOD1CwbxSmknBmPnLWm00uy05qZmqSzqiERl1b4sSvvnVXPBsBJkYG2fkiH51mo6GpiTiy2VOYps%2FWQaFDOplPE8Hi4ufOcEQGjU8hO5vOlSjnsWhXPEqXMlB3xmN%2FQxhEtTfOy2GDo96xrC66yJ%2FqnmOWr4pTVQb%2BPtYGiJU3DeymbzDebJwclCl4d3aAZRyOeuvmIzsOkS5BI1XDqmaLJ6w5W2u%2Fdf9JU4vcrhyKrAVpFzMN9f6uGQfMWAgg5cNe31K8f1CBE7p4i9e9ilPW5KWwnsG394pGzSw1tBlScAvArDbTWeKNemSLTXSOgUYhLyxy2V5qO0E09dd0HMKSsaMhuMJqBconNPEw9nssVxdHDESG5rU4%2BamEFmW8VC5bpkI8VwYgViF1v5N%2FCTttWOJ7rgz%2BNkFEEUNjQmG6nNukT2cWLmMYyPv%2FFfcLyPJ6XaJ0bCjX%2B8OPKaJ9LCkiR%2B3lijONljPIYXxYDRTDJ44LOBjqkAfly%2FfjlF58ynwEQKmhNhkix3H4fl4DrbUz%2BpkhYKj4M2J%2BJHetYRXWlsmsoaak9nnLenulND2GpKF5aoqbYsKadhmszQQ5JpJ21nSXXXdU7YlesCKqRG5g%2BaNO1NQOiTZSgH7XXH%2BHvRfb0b27U0l%2BKLJVKqKKB%2Fr2nAUBrGalXpz2upuetkO2zP1A26LcH2oPqhSCcIZKHRJluA1aMwcXU%2F2Yy&X-Amz-Signature=16f7a5c6f95387ef33c312039edc18bf194229ef6a7ffcf1e24c23846a3a6830&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F43CG3E%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIlDhbC%2Fq676EiBaEL2jdMRKfqQxyCuHnni9ORsGAZjQIhAMndWLKXnld0uqyz9f810MGS%2BZPHvfECAVhhqXErR%2FVbKv8DCHQQABoMNjM3NDIzMTgzODA1Igw2%2B8RXVpbSQt%2F7O8kq3AMzhTFVS2MIWdo6UQQvDKI8rMA%2BjjlTbnkaEhurrQCAIczKKL7ksV8KRYVdPh49RFQOiOUJ2Eag8MkOJ63bRb1u0lJ1%2Fb2nCYw8qAs%2BU6AD7SqmZE2ZDls5dDpPNgmv9zcbOghGe7SznPAyXxCZMgOD1CwbxSmknBmPnLWm00uy05qZmqSzqiERl1b4sSvvnVXPBsBJkYG2fkiH51mo6GpiTiy2VOYps%2FWQaFDOplPE8Hi4ufOcEQGjU8hO5vOlSjnsWhXPEqXMlB3xmN%2FQxhEtTfOy2GDo96xrC66yJ%2FqnmOWr4pTVQb%2BPtYGiJU3DeymbzDebJwclCl4d3aAZRyOeuvmIzsOkS5BI1XDqmaLJ6w5W2u%2Fdf9JU4vcrhyKrAVpFzMN9f6uGQfMWAgg5cNe31K8f1CBE7p4i9e9ilPW5KWwnsG394pGzSw1tBlScAvArDbTWeKNemSLTXSOgUYhLyxy2V5qO0E09dd0HMKSsaMhuMJqBconNPEw9nssVxdHDESG5rU4%2BamEFmW8VC5bpkI8VwYgViF1v5N%2FCTttWOJ7rgz%2BNkFEEUNjQmG6nNukT2cWLmMYyPv%2FFfcLyPJ6XaJ0bCjX%2B8OPKaJ9LCkiR%2B3lijONljPIYXxYDRTDJ44LOBjqkAfly%2FfjlF58ynwEQKmhNhkix3H4fl4DrbUz%2BpkhYKj4M2J%2BJHetYRXWlsmsoaak9nnLenulND2GpKF5aoqbYsKadhmszQQ5JpJ21nSXXXdU7YlesCKqRG5g%2BaNO1NQOiTZSgH7XXH%2BHvRfb0b27U0l%2BKLJVKqKKB%2Fr2nAUBrGalXpz2upuetkO2zP1A26LcH2oPqhSCcIZKHRJluA1aMwcXU%2F2Yy&X-Amz-Signature=1e9a59b1b19001ba3c4e6e924386e56f662074aca0dd5759432eab9551099fb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F43CG3E%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIlDhbC%2Fq676EiBaEL2jdMRKfqQxyCuHnni9ORsGAZjQIhAMndWLKXnld0uqyz9f810MGS%2BZPHvfECAVhhqXErR%2FVbKv8DCHQQABoMNjM3NDIzMTgzODA1Igw2%2B8RXVpbSQt%2F7O8kq3AMzhTFVS2MIWdo6UQQvDKI8rMA%2BjjlTbnkaEhurrQCAIczKKL7ksV8KRYVdPh49RFQOiOUJ2Eag8MkOJ63bRb1u0lJ1%2Fb2nCYw8qAs%2BU6AD7SqmZE2ZDls5dDpPNgmv9zcbOghGe7SznPAyXxCZMgOD1CwbxSmknBmPnLWm00uy05qZmqSzqiERl1b4sSvvnVXPBsBJkYG2fkiH51mo6GpiTiy2VOYps%2FWQaFDOplPE8Hi4ufOcEQGjU8hO5vOlSjnsWhXPEqXMlB3xmN%2FQxhEtTfOy2GDo96xrC66yJ%2FqnmOWr4pTVQb%2BPtYGiJU3DeymbzDebJwclCl4d3aAZRyOeuvmIzsOkS5BI1XDqmaLJ6w5W2u%2Fdf9JU4vcrhyKrAVpFzMN9f6uGQfMWAgg5cNe31K8f1CBE7p4i9e9ilPW5KWwnsG394pGzSw1tBlScAvArDbTWeKNemSLTXSOgUYhLyxy2V5qO0E09dd0HMKSsaMhuMJqBconNPEw9nssVxdHDESG5rU4%2BamEFmW8VC5bpkI8VwYgViF1v5N%2FCTttWOJ7rgz%2BNkFEEUNjQmG6nNukT2cWLmMYyPv%2FFfcLyPJ6XaJ0bCjX%2B8OPKaJ9LCkiR%2B3lijONljPIYXxYDRTDJ44LOBjqkAfly%2FfjlF58ynwEQKmhNhkix3H4fl4DrbUz%2BpkhYKj4M2J%2BJHetYRXWlsmsoaak9nnLenulND2GpKF5aoqbYsKadhmszQQ5JpJ21nSXXXdU7YlesCKqRG5g%2BaNO1NQOiTZSgH7XXH%2BHvRfb0b27U0l%2BKLJVKqKKB%2Fr2nAUBrGalXpz2upuetkO2zP1A26LcH2oPqhSCcIZKHRJluA1aMwcXU%2F2Yy&X-Amz-Signature=902dfdc802b0fa39c0e0fe9af4e6c3c9d0a50d40f8b35730fcf5b6c7079ef095&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F43CG3E%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIlDhbC%2Fq676EiBaEL2jdMRKfqQxyCuHnni9ORsGAZjQIhAMndWLKXnld0uqyz9f810MGS%2BZPHvfECAVhhqXErR%2FVbKv8DCHQQABoMNjM3NDIzMTgzODA1Igw2%2B8RXVpbSQt%2F7O8kq3AMzhTFVS2MIWdo6UQQvDKI8rMA%2BjjlTbnkaEhurrQCAIczKKL7ksV8KRYVdPh49RFQOiOUJ2Eag8MkOJ63bRb1u0lJ1%2Fb2nCYw8qAs%2BU6AD7SqmZE2ZDls5dDpPNgmv9zcbOghGe7SznPAyXxCZMgOD1CwbxSmknBmPnLWm00uy05qZmqSzqiERl1b4sSvvnVXPBsBJkYG2fkiH51mo6GpiTiy2VOYps%2FWQaFDOplPE8Hi4ufOcEQGjU8hO5vOlSjnsWhXPEqXMlB3xmN%2FQxhEtTfOy2GDo96xrC66yJ%2FqnmOWr4pTVQb%2BPtYGiJU3DeymbzDebJwclCl4d3aAZRyOeuvmIzsOkS5BI1XDqmaLJ6w5W2u%2Fdf9JU4vcrhyKrAVpFzMN9f6uGQfMWAgg5cNe31K8f1CBE7p4i9e9ilPW5KWwnsG394pGzSw1tBlScAvArDbTWeKNemSLTXSOgUYhLyxy2V5qO0E09dd0HMKSsaMhuMJqBconNPEw9nssVxdHDESG5rU4%2BamEFmW8VC5bpkI8VwYgViF1v5N%2FCTttWOJ7rgz%2BNkFEEUNjQmG6nNukT2cWLmMYyPv%2FFfcLyPJ6XaJ0bCjX%2B8OPKaJ9LCkiR%2B3lijONljPIYXxYDRTDJ44LOBjqkAfly%2FfjlF58ynwEQKmhNhkix3H4fl4DrbUz%2BpkhYKj4M2J%2BJHetYRXWlsmsoaak9nnLenulND2GpKF5aoqbYsKadhmszQQ5JpJ21nSXXXdU7YlesCKqRG5g%2BaNO1NQOiTZSgH7XXH%2BHvRfb0b27U0l%2BKLJVKqKKB%2Fr2nAUBrGalXpz2upuetkO2zP1A26LcH2oPqhSCcIZKHRJluA1aMwcXU%2F2Yy&X-Amz-Signature=e88e1d7366c777beb8eb799d8e0f8f456436807a63e277e5b289c889b81a0d0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

