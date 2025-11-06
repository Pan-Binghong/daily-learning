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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YW7OZXM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQhvPTaskwjZR5XfqDpBEf%2FaDfnWMZRIeUlql2d7aztgIhAM4SxFzuVGjdu5Yfg5Xpeht9gn%2B3%2BfUXbuGV%2FBDogVQNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLmxaEaDWdEmrf0%2BEq3AOlzx2%2BEuno%2B%2FsBtXvvDDZ5GlCcaZB5rA5fAfaelUsiKlS0MCn4MX3HZw4U%2FkkDOxS%2BuPc2bsdEAnUCiWIB%2B0dJukq21p1LYHqJobY15DBEHCMfylgVZ0Bh1WdF0nzTPtCBFLE%2BdQT1uDaDzLs4HcBaW%2B7gw7VVroF%2BgfvVJltT%2BWV5ccHbn4mg94adYe7hS54Apk6m1uwVityWalP46FJLPP52h0a8Nv9wo3p5kDXjKO3Yj1wPlGW1EIapKXzBmiFaQ8R%2FXucHciHrTSHLTHNKfKedSlAd5z1LBtrtYi7nb2mn%2BP8AsddbnG2GjmNtq5Tckfa9JY2w5F4WUeEEMSot6RW3fVZlyYnWuEbhF5GMpfUdV0ZdOJ%2FqDlkuBWQPuXUfAwope9Oz0%2BIeVjHo2EFPuJ37i7n0h82ZZwSpDEKwSkAlRZ4ltpJt15CQAyFJq0TxSsqBVbzAfGeY8Wqohs0Qc6YT%2BLHJymQpYaw05%2B8Y%2BANeTpUZCvZx%2BAka5AuiAwXtDPEmOvr4AooYdMxHIe7hyyCTEnMF6VgbgFiKzyrCP3FsarKuLO4Rtu87X1pjhGE1kRpCNGZyyDTIM%2FJlEJ%2Ftn%2B4NM%2FJk%2BXaoPElJiE2siOFvpwDhrCuMHJOPzDCf8q%2FIBjqkASPtu5urfh5RJ6rDOL6SaUwdJxMy8sge31J22ERP1whSZvEtmnp6ynUJ15SJIJnZUsB7sPWKJy7l87ax2tnEOoAQTy8WHUWjDllQrSV7tpCrS0SNYG02Dm%2BBHvV1ICoQEBoMXHqrDO4cMwjzGLhbLu5FkanowB82u9staQwUKSAWODvPaIGri7cPM%2BhefyNAD7khHufJsIGrXBkQHd6hkXZ0xdO8&X-Amz-Signature=b332aab79a0851f6e964fb31fda03c6f1a4e52742671056c92d60ed192737620&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YW7OZXM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQhvPTaskwjZR5XfqDpBEf%2FaDfnWMZRIeUlql2d7aztgIhAM4SxFzuVGjdu5Yfg5Xpeht9gn%2B3%2BfUXbuGV%2FBDogVQNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLmxaEaDWdEmrf0%2BEq3AOlzx2%2BEuno%2B%2FsBtXvvDDZ5GlCcaZB5rA5fAfaelUsiKlS0MCn4MX3HZw4U%2FkkDOxS%2BuPc2bsdEAnUCiWIB%2B0dJukq21p1LYHqJobY15DBEHCMfylgVZ0Bh1WdF0nzTPtCBFLE%2BdQT1uDaDzLs4HcBaW%2B7gw7VVroF%2BgfvVJltT%2BWV5ccHbn4mg94adYe7hS54Apk6m1uwVityWalP46FJLPP52h0a8Nv9wo3p5kDXjKO3Yj1wPlGW1EIapKXzBmiFaQ8R%2FXucHciHrTSHLTHNKfKedSlAd5z1LBtrtYi7nb2mn%2BP8AsddbnG2GjmNtq5Tckfa9JY2w5F4WUeEEMSot6RW3fVZlyYnWuEbhF5GMpfUdV0ZdOJ%2FqDlkuBWQPuXUfAwope9Oz0%2BIeVjHo2EFPuJ37i7n0h82ZZwSpDEKwSkAlRZ4ltpJt15CQAyFJq0TxSsqBVbzAfGeY8Wqohs0Qc6YT%2BLHJymQpYaw05%2B8Y%2BANeTpUZCvZx%2BAka5AuiAwXtDPEmOvr4AooYdMxHIe7hyyCTEnMF6VgbgFiKzyrCP3FsarKuLO4Rtu87X1pjhGE1kRpCNGZyyDTIM%2FJlEJ%2Ftn%2B4NM%2FJk%2BXaoPElJiE2siOFvpwDhrCuMHJOPzDCf8q%2FIBjqkASPtu5urfh5RJ6rDOL6SaUwdJxMy8sge31J22ERP1whSZvEtmnp6ynUJ15SJIJnZUsB7sPWKJy7l87ax2tnEOoAQTy8WHUWjDllQrSV7tpCrS0SNYG02Dm%2BBHvV1ICoQEBoMXHqrDO4cMwjzGLhbLu5FkanowB82u9staQwUKSAWODvPaIGri7cPM%2BhefyNAD7khHufJsIGrXBkQHd6hkXZ0xdO8&X-Amz-Signature=d47b84393615955eb3c69d901a9ad71a9d668522317fb02d9ba13efd6ebb2305&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YW7OZXM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQhvPTaskwjZR5XfqDpBEf%2FaDfnWMZRIeUlql2d7aztgIhAM4SxFzuVGjdu5Yfg5Xpeht9gn%2B3%2BfUXbuGV%2FBDogVQNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLmxaEaDWdEmrf0%2BEq3AOlzx2%2BEuno%2B%2FsBtXvvDDZ5GlCcaZB5rA5fAfaelUsiKlS0MCn4MX3HZw4U%2FkkDOxS%2BuPc2bsdEAnUCiWIB%2B0dJukq21p1LYHqJobY15DBEHCMfylgVZ0Bh1WdF0nzTPtCBFLE%2BdQT1uDaDzLs4HcBaW%2B7gw7VVroF%2BgfvVJltT%2BWV5ccHbn4mg94adYe7hS54Apk6m1uwVityWalP46FJLPP52h0a8Nv9wo3p5kDXjKO3Yj1wPlGW1EIapKXzBmiFaQ8R%2FXucHciHrTSHLTHNKfKedSlAd5z1LBtrtYi7nb2mn%2BP8AsddbnG2GjmNtq5Tckfa9JY2w5F4WUeEEMSot6RW3fVZlyYnWuEbhF5GMpfUdV0ZdOJ%2FqDlkuBWQPuXUfAwope9Oz0%2BIeVjHo2EFPuJ37i7n0h82ZZwSpDEKwSkAlRZ4ltpJt15CQAyFJq0TxSsqBVbzAfGeY8Wqohs0Qc6YT%2BLHJymQpYaw05%2B8Y%2BANeTpUZCvZx%2BAka5AuiAwXtDPEmOvr4AooYdMxHIe7hyyCTEnMF6VgbgFiKzyrCP3FsarKuLO4Rtu87X1pjhGE1kRpCNGZyyDTIM%2FJlEJ%2Ftn%2B4NM%2FJk%2BXaoPElJiE2siOFvpwDhrCuMHJOPzDCf8q%2FIBjqkASPtu5urfh5RJ6rDOL6SaUwdJxMy8sge31J22ERP1whSZvEtmnp6ynUJ15SJIJnZUsB7sPWKJy7l87ax2tnEOoAQTy8WHUWjDllQrSV7tpCrS0SNYG02Dm%2BBHvV1ICoQEBoMXHqrDO4cMwjzGLhbLu5FkanowB82u9staQwUKSAWODvPaIGri7cPM%2BhefyNAD7khHufJsIGrXBkQHd6hkXZ0xdO8&X-Amz-Signature=2db91f61d42ae7f8ceefc5a7034431375d0d0da6fbe24c2f9d2c0f599442b538&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YW7OZXM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQhvPTaskwjZR5XfqDpBEf%2FaDfnWMZRIeUlql2d7aztgIhAM4SxFzuVGjdu5Yfg5Xpeht9gn%2B3%2BfUXbuGV%2FBDogVQNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLmxaEaDWdEmrf0%2BEq3AOlzx2%2BEuno%2B%2FsBtXvvDDZ5GlCcaZB5rA5fAfaelUsiKlS0MCn4MX3HZw4U%2FkkDOxS%2BuPc2bsdEAnUCiWIB%2B0dJukq21p1LYHqJobY15DBEHCMfylgVZ0Bh1WdF0nzTPtCBFLE%2BdQT1uDaDzLs4HcBaW%2B7gw7VVroF%2BgfvVJltT%2BWV5ccHbn4mg94adYe7hS54Apk6m1uwVityWalP46FJLPP52h0a8Nv9wo3p5kDXjKO3Yj1wPlGW1EIapKXzBmiFaQ8R%2FXucHciHrTSHLTHNKfKedSlAd5z1LBtrtYi7nb2mn%2BP8AsddbnG2GjmNtq5Tckfa9JY2w5F4WUeEEMSot6RW3fVZlyYnWuEbhF5GMpfUdV0ZdOJ%2FqDlkuBWQPuXUfAwope9Oz0%2BIeVjHo2EFPuJ37i7n0h82ZZwSpDEKwSkAlRZ4ltpJt15CQAyFJq0TxSsqBVbzAfGeY8Wqohs0Qc6YT%2BLHJymQpYaw05%2B8Y%2BANeTpUZCvZx%2BAka5AuiAwXtDPEmOvr4AooYdMxHIe7hyyCTEnMF6VgbgFiKzyrCP3FsarKuLO4Rtu87X1pjhGE1kRpCNGZyyDTIM%2FJlEJ%2Ftn%2B4NM%2FJk%2BXaoPElJiE2siOFvpwDhrCuMHJOPzDCf8q%2FIBjqkASPtu5urfh5RJ6rDOL6SaUwdJxMy8sge31J22ERP1whSZvEtmnp6ynUJ15SJIJnZUsB7sPWKJy7l87ax2tnEOoAQTy8WHUWjDllQrSV7tpCrS0SNYG02Dm%2BBHvV1ICoQEBoMXHqrDO4cMwjzGLhbLu5FkanowB82u9staQwUKSAWODvPaIGri7cPM%2BhefyNAD7khHufJsIGrXBkQHd6hkXZ0xdO8&X-Amz-Signature=1e64538112cca41d3da8c994258875e659a20e0f40b79154b17bc010bede24b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YW7OZXM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQhvPTaskwjZR5XfqDpBEf%2FaDfnWMZRIeUlql2d7aztgIhAM4SxFzuVGjdu5Yfg5Xpeht9gn%2B3%2BfUXbuGV%2FBDogVQNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLmxaEaDWdEmrf0%2BEq3AOlzx2%2BEuno%2B%2FsBtXvvDDZ5GlCcaZB5rA5fAfaelUsiKlS0MCn4MX3HZw4U%2FkkDOxS%2BuPc2bsdEAnUCiWIB%2B0dJukq21p1LYHqJobY15DBEHCMfylgVZ0Bh1WdF0nzTPtCBFLE%2BdQT1uDaDzLs4HcBaW%2B7gw7VVroF%2BgfvVJltT%2BWV5ccHbn4mg94adYe7hS54Apk6m1uwVityWalP46FJLPP52h0a8Nv9wo3p5kDXjKO3Yj1wPlGW1EIapKXzBmiFaQ8R%2FXucHciHrTSHLTHNKfKedSlAd5z1LBtrtYi7nb2mn%2BP8AsddbnG2GjmNtq5Tckfa9JY2w5F4WUeEEMSot6RW3fVZlyYnWuEbhF5GMpfUdV0ZdOJ%2FqDlkuBWQPuXUfAwope9Oz0%2BIeVjHo2EFPuJ37i7n0h82ZZwSpDEKwSkAlRZ4ltpJt15CQAyFJq0TxSsqBVbzAfGeY8Wqohs0Qc6YT%2BLHJymQpYaw05%2B8Y%2BANeTpUZCvZx%2BAka5AuiAwXtDPEmOvr4AooYdMxHIe7hyyCTEnMF6VgbgFiKzyrCP3FsarKuLO4Rtu87X1pjhGE1kRpCNGZyyDTIM%2FJlEJ%2Ftn%2B4NM%2FJk%2BXaoPElJiE2siOFvpwDhrCuMHJOPzDCf8q%2FIBjqkASPtu5urfh5RJ6rDOL6SaUwdJxMy8sge31J22ERP1whSZvEtmnp6ynUJ15SJIJnZUsB7sPWKJy7l87ax2tnEOoAQTy8WHUWjDllQrSV7tpCrS0SNYG02Dm%2BBHvV1ICoQEBoMXHqrDO4cMwjzGLhbLu5FkanowB82u9staQwUKSAWODvPaIGri7cPM%2BhefyNAD7khHufJsIGrXBkQHd6hkXZ0xdO8&X-Amz-Signature=226b0328773ee4800aef25da9423c1883abb3339b01f8bdf97b78a815fc32c57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YW7OZXM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQhvPTaskwjZR5XfqDpBEf%2FaDfnWMZRIeUlql2d7aztgIhAM4SxFzuVGjdu5Yfg5Xpeht9gn%2B3%2BfUXbuGV%2FBDogVQNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLmxaEaDWdEmrf0%2BEq3AOlzx2%2BEuno%2B%2FsBtXvvDDZ5GlCcaZB5rA5fAfaelUsiKlS0MCn4MX3HZw4U%2FkkDOxS%2BuPc2bsdEAnUCiWIB%2B0dJukq21p1LYHqJobY15DBEHCMfylgVZ0Bh1WdF0nzTPtCBFLE%2BdQT1uDaDzLs4HcBaW%2B7gw7VVroF%2BgfvVJltT%2BWV5ccHbn4mg94adYe7hS54Apk6m1uwVityWalP46FJLPP52h0a8Nv9wo3p5kDXjKO3Yj1wPlGW1EIapKXzBmiFaQ8R%2FXucHciHrTSHLTHNKfKedSlAd5z1LBtrtYi7nb2mn%2BP8AsddbnG2GjmNtq5Tckfa9JY2w5F4WUeEEMSot6RW3fVZlyYnWuEbhF5GMpfUdV0ZdOJ%2FqDlkuBWQPuXUfAwope9Oz0%2BIeVjHo2EFPuJ37i7n0h82ZZwSpDEKwSkAlRZ4ltpJt15CQAyFJq0TxSsqBVbzAfGeY8Wqohs0Qc6YT%2BLHJymQpYaw05%2B8Y%2BANeTpUZCvZx%2BAka5AuiAwXtDPEmOvr4AooYdMxHIe7hyyCTEnMF6VgbgFiKzyrCP3FsarKuLO4Rtu87X1pjhGE1kRpCNGZyyDTIM%2FJlEJ%2Ftn%2B4NM%2FJk%2BXaoPElJiE2siOFvpwDhrCuMHJOPzDCf8q%2FIBjqkASPtu5urfh5RJ6rDOL6SaUwdJxMy8sge31J22ERP1whSZvEtmnp6ynUJ15SJIJnZUsB7sPWKJy7l87ax2tnEOoAQTy8WHUWjDllQrSV7tpCrS0SNYG02Dm%2BBHvV1ICoQEBoMXHqrDO4cMwjzGLhbLu5FkanowB82u9staQwUKSAWODvPaIGri7cPM%2BhefyNAD7khHufJsIGrXBkQHd6hkXZ0xdO8&X-Amz-Signature=f04eb08bc1b6b0a17553c57210726e4b80f26ac55fce8538d21560be101c60b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YW7OZXM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQhvPTaskwjZR5XfqDpBEf%2FaDfnWMZRIeUlql2d7aztgIhAM4SxFzuVGjdu5Yfg5Xpeht9gn%2B3%2BfUXbuGV%2FBDogVQNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLmxaEaDWdEmrf0%2BEq3AOlzx2%2BEuno%2B%2FsBtXvvDDZ5GlCcaZB5rA5fAfaelUsiKlS0MCn4MX3HZw4U%2FkkDOxS%2BuPc2bsdEAnUCiWIB%2B0dJukq21p1LYHqJobY15DBEHCMfylgVZ0Bh1WdF0nzTPtCBFLE%2BdQT1uDaDzLs4HcBaW%2B7gw7VVroF%2BgfvVJltT%2BWV5ccHbn4mg94adYe7hS54Apk6m1uwVityWalP46FJLPP52h0a8Nv9wo3p5kDXjKO3Yj1wPlGW1EIapKXzBmiFaQ8R%2FXucHciHrTSHLTHNKfKedSlAd5z1LBtrtYi7nb2mn%2BP8AsddbnG2GjmNtq5Tckfa9JY2w5F4WUeEEMSot6RW3fVZlyYnWuEbhF5GMpfUdV0ZdOJ%2FqDlkuBWQPuXUfAwope9Oz0%2BIeVjHo2EFPuJ37i7n0h82ZZwSpDEKwSkAlRZ4ltpJt15CQAyFJq0TxSsqBVbzAfGeY8Wqohs0Qc6YT%2BLHJymQpYaw05%2B8Y%2BANeTpUZCvZx%2BAka5AuiAwXtDPEmOvr4AooYdMxHIe7hyyCTEnMF6VgbgFiKzyrCP3FsarKuLO4Rtu87X1pjhGE1kRpCNGZyyDTIM%2FJlEJ%2Ftn%2B4NM%2FJk%2BXaoPElJiE2siOFvpwDhrCuMHJOPzDCf8q%2FIBjqkASPtu5urfh5RJ6rDOL6SaUwdJxMy8sge31J22ERP1whSZvEtmnp6ynUJ15SJIJnZUsB7sPWKJy7l87ax2tnEOoAQTy8WHUWjDllQrSV7tpCrS0SNYG02Dm%2BBHvV1ICoQEBoMXHqrDO4cMwjzGLhbLu5FkanowB82u9staQwUKSAWODvPaIGri7cPM%2BhefyNAD7khHufJsIGrXBkQHd6hkXZ0xdO8&X-Amz-Signature=48f4a3563cbab533232805ae66fe0b167ed3ac75ebc17195005ac90bc2913906&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YW7OZXM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQhvPTaskwjZR5XfqDpBEf%2FaDfnWMZRIeUlql2d7aztgIhAM4SxFzuVGjdu5Yfg5Xpeht9gn%2B3%2BfUXbuGV%2FBDogVQNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLmxaEaDWdEmrf0%2BEq3AOlzx2%2BEuno%2B%2FsBtXvvDDZ5GlCcaZB5rA5fAfaelUsiKlS0MCn4MX3HZw4U%2FkkDOxS%2BuPc2bsdEAnUCiWIB%2B0dJukq21p1LYHqJobY15DBEHCMfylgVZ0Bh1WdF0nzTPtCBFLE%2BdQT1uDaDzLs4HcBaW%2B7gw7VVroF%2BgfvVJltT%2BWV5ccHbn4mg94adYe7hS54Apk6m1uwVityWalP46FJLPP52h0a8Nv9wo3p5kDXjKO3Yj1wPlGW1EIapKXzBmiFaQ8R%2FXucHciHrTSHLTHNKfKedSlAd5z1LBtrtYi7nb2mn%2BP8AsddbnG2GjmNtq5Tckfa9JY2w5F4WUeEEMSot6RW3fVZlyYnWuEbhF5GMpfUdV0ZdOJ%2FqDlkuBWQPuXUfAwope9Oz0%2BIeVjHo2EFPuJ37i7n0h82ZZwSpDEKwSkAlRZ4ltpJt15CQAyFJq0TxSsqBVbzAfGeY8Wqohs0Qc6YT%2BLHJymQpYaw05%2B8Y%2BANeTpUZCvZx%2BAka5AuiAwXtDPEmOvr4AooYdMxHIe7hyyCTEnMF6VgbgFiKzyrCP3FsarKuLO4Rtu87X1pjhGE1kRpCNGZyyDTIM%2FJlEJ%2Ftn%2B4NM%2FJk%2BXaoPElJiE2siOFvpwDhrCuMHJOPzDCf8q%2FIBjqkASPtu5urfh5RJ6rDOL6SaUwdJxMy8sge31J22ERP1whSZvEtmnp6ynUJ15SJIJnZUsB7sPWKJy7l87ax2tnEOoAQTy8WHUWjDllQrSV7tpCrS0SNYG02Dm%2BBHvV1ICoQEBoMXHqrDO4cMwjzGLhbLu5FkanowB82u9staQwUKSAWODvPaIGri7cPM%2BhefyNAD7khHufJsIGrXBkQHd6hkXZ0xdO8&X-Amz-Signature=d13aca35beec323003ca84ac8a1492546d583f2693eac0725683dfb2f7ad700b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YW7OZXM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQhvPTaskwjZR5XfqDpBEf%2FaDfnWMZRIeUlql2d7aztgIhAM4SxFzuVGjdu5Yfg5Xpeht9gn%2B3%2BfUXbuGV%2FBDogVQNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLmxaEaDWdEmrf0%2BEq3AOlzx2%2BEuno%2B%2FsBtXvvDDZ5GlCcaZB5rA5fAfaelUsiKlS0MCn4MX3HZw4U%2FkkDOxS%2BuPc2bsdEAnUCiWIB%2B0dJukq21p1LYHqJobY15DBEHCMfylgVZ0Bh1WdF0nzTPtCBFLE%2BdQT1uDaDzLs4HcBaW%2B7gw7VVroF%2BgfvVJltT%2BWV5ccHbn4mg94adYe7hS54Apk6m1uwVityWalP46FJLPP52h0a8Nv9wo3p5kDXjKO3Yj1wPlGW1EIapKXzBmiFaQ8R%2FXucHciHrTSHLTHNKfKedSlAd5z1LBtrtYi7nb2mn%2BP8AsddbnG2GjmNtq5Tckfa9JY2w5F4WUeEEMSot6RW3fVZlyYnWuEbhF5GMpfUdV0ZdOJ%2FqDlkuBWQPuXUfAwope9Oz0%2BIeVjHo2EFPuJ37i7n0h82ZZwSpDEKwSkAlRZ4ltpJt15CQAyFJq0TxSsqBVbzAfGeY8Wqohs0Qc6YT%2BLHJymQpYaw05%2B8Y%2BANeTpUZCvZx%2BAka5AuiAwXtDPEmOvr4AooYdMxHIe7hyyCTEnMF6VgbgFiKzyrCP3FsarKuLO4Rtu87X1pjhGE1kRpCNGZyyDTIM%2FJlEJ%2Ftn%2B4NM%2FJk%2BXaoPElJiE2siOFvpwDhrCuMHJOPzDCf8q%2FIBjqkASPtu5urfh5RJ6rDOL6SaUwdJxMy8sge31J22ERP1whSZvEtmnp6ynUJ15SJIJnZUsB7sPWKJy7l87ax2tnEOoAQTy8WHUWjDllQrSV7tpCrS0SNYG02Dm%2BBHvV1ICoQEBoMXHqrDO4cMwjzGLhbLu5FkanowB82u9staQwUKSAWODvPaIGri7cPM%2BhefyNAD7khHufJsIGrXBkQHd6hkXZ0xdO8&X-Amz-Signature=89c8ec9e4150bfedb0d3a1184e9f85409b6ae71c4a5354ba28a027d1de1d7593&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YW7OZXM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQhvPTaskwjZR5XfqDpBEf%2FaDfnWMZRIeUlql2d7aztgIhAM4SxFzuVGjdu5Yfg5Xpeht9gn%2B3%2BfUXbuGV%2FBDogVQNKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLmxaEaDWdEmrf0%2BEq3AOlzx2%2BEuno%2B%2FsBtXvvDDZ5GlCcaZB5rA5fAfaelUsiKlS0MCn4MX3HZw4U%2FkkDOxS%2BuPc2bsdEAnUCiWIB%2B0dJukq21p1LYHqJobY15DBEHCMfylgVZ0Bh1WdF0nzTPtCBFLE%2BdQT1uDaDzLs4HcBaW%2B7gw7VVroF%2BgfvVJltT%2BWV5ccHbn4mg94adYe7hS54Apk6m1uwVityWalP46FJLPP52h0a8Nv9wo3p5kDXjKO3Yj1wPlGW1EIapKXzBmiFaQ8R%2FXucHciHrTSHLTHNKfKedSlAd5z1LBtrtYi7nb2mn%2BP8AsddbnG2GjmNtq5Tckfa9JY2w5F4WUeEEMSot6RW3fVZlyYnWuEbhF5GMpfUdV0ZdOJ%2FqDlkuBWQPuXUfAwope9Oz0%2BIeVjHo2EFPuJ37i7n0h82ZZwSpDEKwSkAlRZ4ltpJt15CQAyFJq0TxSsqBVbzAfGeY8Wqohs0Qc6YT%2BLHJymQpYaw05%2B8Y%2BANeTpUZCvZx%2BAka5AuiAwXtDPEmOvr4AooYdMxHIe7hyyCTEnMF6VgbgFiKzyrCP3FsarKuLO4Rtu87X1pjhGE1kRpCNGZyyDTIM%2FJlEJ%2Ftn%2B4NM%2FJk%2BXaoPElJiE2siOFvpwDhrCuMHJOPzDCf8q%2FIBjqkASPtu5urfh5RJ6rDOL6SaUwdJxMy8sge31J22ERP1whSZvEtmnp6ynUJ15SJIJnZUsB7sPWKJy7l87ax2tnEOoAQTy8WHUWjDllQrSV7tpCrS0SNYG02Dm%2BBHvV1ICoQEBoMXHqrDO4cMwjzGLhbLu5FkanowB82u9staQwUKSAWODvPaIGri7cPM%2BhefyNAD7khHufJsIGrXBkQHd6hkXZ0xdO8&X-Amz-Signature=66554a09e15ec2f13c1803db94e941cdda20d1b4f0c1cc68cdd77242bb447981&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

