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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJUVK4W%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9sBes%2BB81dlpXj6Ln3oL7vbTy76VUEfoexrLkflVwVAiAuCpOzZ0Ie9JJmYDMV56AGJWA1dho%2Flpt45bgc9E%2Bq9CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbkiVoyK%2Byvtp3hCMKtwDuEc3hnOJ5GHdXfPZjyKIRowHd1AT1B0lBe%2BJZ440OI%2B5wInnjUFXIrepQgG5BB7QGT9tbDkl7%2FRfU1IlUr4FVJv7fvTBLyQc%2BR2zxP3db6PoRhz5NErU7rVI8G58HwDhFDSESExly5SoCEK32woIvGUoinCM5EiattIVftHOihk5ct2MotHMf4hkErTASBjeyua1YRb0wWtXLPbePfvCJucU22LuhQI%2Fsq30Eq9pyucMqaxM0KqLrfcDNY%2FDGP%2Fg6ME%2BLLNVFvEdra0BBpCC9hIF5kk65Az3JAHt66HOBCsM2ewdwjvUl2Ymbnr9gaarW7N4MrxBrCFXsPurN8rAVYqZ6TuIi1FYu4FwuL8rWgyO3f5%2BlN41PNREWd9dXVYvioK%2FjkfhzbNzc1ZHCF1xQ1OY9aBzgZnrsRXKK7b3S69QWAl%2FAPuWuZJ4tWCWpYzkomkJEnl9nLG43iCgpQvUOeKufVfAydKnBBWbap9ZO02YsUi8TrMAMPPusT8VgglLvUD9bzPPya9eNiNPDkyuyYLePIU8uDd0dS7%2FbJQmo5dnW5I%2FgAfBwIYz1uAIvey4UVQZA1KGbRfeozTryR%2BniKZcw8o4YC8FUygs6HWDNQ47mVtSKSdjfBffyEww59fAywY6pgGb%2BoHFkMetPs5qDbaEb%2FfEsVI256ijzZ%2Bw1v7XPGa5gMubpcj4gQeodaOAsbdVHH%2B9iy01BhWUruUWqZEQe8L0%2FsiFs9sKEcWPYAuyS6OHkMofB9dCsHb2AZW%2BliIZSO9sPXIiBHXgx7oUig%2FXN3JXWYz5xDaiF1n%2BHt4N3dtMR7L0MOAZ5RQ1gOIggOhC%2BTkhDW%2FLvx0bCnVs%2BvVTLQf%2FRH%2Facck3&X-Amz-Signature=2e97581b778e277613bf57799b14551b9dca6028a12cfed3ece1c0baafed2754&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJUVK4W%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9sBes%2BB81dlpXj6Ln3oL7vbTy76VUEfoexrLkflVwVAiAuCpOzZ0Ie9JJmYDMV56AGJWA1dho%2Flpt45bgc9E%2Bq9CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbkiVoyK%2Byvtp3hCMKtwDuEc3hnOJ5GHdXfPZjyKIRowHd1AT1B0lBe%2BJZ440OI%2B5wInnjUFXIrepQgG5BB7QGT9tbDkl7%2FRfU1IlUr4FVJv7fvTBLyQc%2BR2zxP3db6PoRhz5NErU7rVI8G58HwDhFDSESExly5SoCEK32woIvGUoinCM5EiattIVftHOihk5ct2MotHMf4hkErTASBjeyua1YRb0wWtXLPbePfvCJucU22LuhQI%2Fsq30Eq9pyucMqaxM0KqLrfcDNY%2FDGP%2Fg6ME%2BLLNVFvEdra0BBpCC9hIF5kk65Az3JAHt66HOBCsM2ewdwjvUl2Ymbnr9gaarW7N4MrxBrCFXsPurN8rAVYqZ6TuIi1FYu4FwuL8rWgyO3f5%2BlN41PNREWd9dXVYvioK%2FjkfhzbNzc1ZHCF1xQ1OY9aBzgZnrsRXKK7b3S69QWAl%2FAPuWuZJ4tWCWpYzkomkJEnl9nLG43iCgpQvUOeKufVfAydKnBBWbap9ZO02YsUi8TrMAMPPusT8VgglLvUD9bzPPya9eNiNPDkyuyYLePIU8uDd0dS7%2FbJQmo5dnW5I%2FgAfBwIYz1uAIvey4UVQZA1KGbRfeozTryR%2BniKZcw8o4YC8FUygs6HWDNQ47mVtSKSdjfBffyEww59fAywY6pgGb%2BoHFkMetPs5qDbaEb%2FfEsVI256ijzZ%2Bw1v7XPGa5gMubpcj4gQeodaOAsbdVHH%2B9iy01BhWUruUWqZEQe8L0%2FsiFs9sKEcWPYAuyS6OHkMofB9dCsHb2AZW%2BliIZSO9sPXIiBHXgx7oUig%2FXN3JXWYz5xDaiF1n%2BHt4N3dtMR7L0MOAZ5RQ1gOIggOhC%2BTkhDW%2FLvx0bCnVs%2BvVTLQf%2FRH%2Facck3&X-Amz-Signature=974e065cd9cbfcb6476881f655a7bfb07d8e7b78c8cc3ff7a2c18068d385e9b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJUVK4W%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9sBes%2BB81dlpXj6Ln3oL7vbTy76VUEfoexrLkflVwVAiAuCpOzZ0Ie9JJmYDMV56AGJWA1dho%2Flpt45bgc9E%2Bq9CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbkiVoyK%2Byvtp3hCMKtwDuEc3hnOJ5GHdXfPZjyKIRowHd1AT1B0lBe%2BJZ440OI%2B5wInnjUFXIrepQgG5BB7QGT9tbDkl7%2FRfU1IlUr4FVJv7fvTBLyQc%2BR2zxP3db6PoRhz5NErU7rVI8G58HwDhFDSESExly5SoCEK32woIvGUoinCM5EiattIVftHOihk5ct2MotHMf4hkErTASBjeyua1YRb0wWtXLPbePfvCJucU22LuhQI%2Fsq30Eq9pyucMqaxM0KqLrfcDNY%2FDGP%2Fg6ME%2BLLNVFvEdra0BBpCC9hIF5kk65Az3JAHt66HOBCsM2ewdwjvUl2Ymbnr9gaarW7N4MrxBrCFXsPurN8rAVYqZ6TuIi1FYu4FwuL8rWgyO3f5%2BlN41PNREWd9dXVYvioK%2FjkfhzbNzc1ZHCF1xQ1OY9aBzgZnrsRXKK7b3S69QWAl%2FAPuWuZJ4tWCWpYzkomkJEnl9nLG43iCgpQvUOeKufVfAydKnBBWbap9ZO02YsUi8TrMAMPPusT8VgglLvUD9bzPPya9eNiNPDkyuyYLePIU8uDd0dS7%2FbJQmo5dnW5I%2FgAfBwIYz1uAIvey4UVQZA1KGbRfeozTryR%2BniKZcw8o4YC8FUygs6HWDNQ47mVtSKSdjfBffyEww59fAywY6pgGb%2BoHFkMetPs5qDbaEb%2FfEsVI256ijzZ%2Bw1v7XPGa5gMubpcj4gQeodaOAsbdVHH%2B9iy01BhWUruUWqZEQe8L0%2FsiFs9sKEcWPYAuyS6OHkMofB9dCsHb2AZW%2BliIZSO9sPXIiBHXgx7oUig%2FXN3JXWYz5xDaiF1n%2BHt4N3dtMR7L0MOAZ5RQ1gOIggOhC%2BTkhDW%2FLvx0bCnVs%2BvVTLQf%2FRH%2Facck3&X-Amz-Signature=633c09fdc73bfcde5f18a60ba7d6c5c03a612d634902ddb8d11c452add546fc6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJUVK4W%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9sBes%2BB81dlpXj6Ln3oL7vbTy76VUEfoexrLkflVwVAiAuCpOzZ0Ie9JJmYDMV56AGJWA1dho%2Flpt45bgc9E%2Bq9CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbkiVoyK%2Byvtp3hCMKtwDuEc3hnOJ5GHdXfPZjyKIRowHd1AT1B0lBe%2BJZ440OI%2B5wInnjUFXIrepQgG5BB7QGT9tbDkl7%2FRfU1IlUr4FVJv7fvTBLyQc%2BR2zxP3db6PoRhz5NErU7rVI8G58HwDhFDSESExly5SoCEK32woIvGUoinCM5EiattIVftHOihk5ct2MotHMf4hkErTASBjeyua1YRb0wWtXLPbePfvCJucU22LuhQI%2Fsq30Eq9pyucMqaxM0KqLrfcDNY%2FDGP%2Fg6ME%2BLLNVFvEdra0BBpCC9hIF5kk65Az3JAHt66HOBCsM2ewdwjvUl2Ymbnr9gaarW7N4MrxBrCFXsPurN8rAVYqZ6TuIi1FYu4FwuL8rWgyO3f5%2BlN41PNREWd9dXVYvioK%2FjkfhzbNzc1ZHCF1xQ1OY9aBzgZnrsRXKK7b3S69QWAl%2FAPuWuZJ4tWCWpYzkomkJEnl9nLG43iCgpQvUOeKufVfAydKnBBWbap9ZO02YsUi8TrMAMPPusT8VgglLvUD9bzPPya9eNiNPDkyuyYLePIU8uDd0dS7%2FbJQmo5dnW5I%2FgAfBwIYz1uAIvey4UVQZA1KGbRfeozTryR%2BniKZcw8o4YC8FUygs6HWDNQ47mVtSKSdjfBffyEww59fAywY6pgGb%2BoHFkMetPs5qDbaEb%2FfEsVI256ijzZ%2Bw1v7XPGa5gMubpcj4gQeodaOAsbdVHH%2B9iy01BhWUruUWqZEQe8L0%2FsiFs9sKEcWPYAuyS6OHkMofB9dCsHb2AZW%2BliIZSO9sPXIiBHXgx7oUig%2FXN3JXWYz5xDaiF1n%2BHt4N3dtMR7L0MOAZ5RQ1gOIggOhC%2BTkhDW%2FLvx0bCnVs%2BvVTLQf%2FRH%2Facck3&X-Amz-Signature=fcb92d8c85630a32fab1881bcf7af6651ad5bdf60204b9d3a0b0f037fd8f5e4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJUVK4W%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9sBes%2BB81dlpXj6Ln3oL7vbTy76VUEfoexrLkflVwVAiAuCpOzZ0Ie9JJmYDMV56AGJWA1dho%2Flpt45bgc9E%2Bq9CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbkiVoyK%2Byvtp3hCMKtwDuEc3hnOJ5GHdXfPZjyKIRowHd1AT1B0lBe%2BJZ440OI%2B5wInnjUFXIrepQgG5BB7QGT9tbDkl7%2FRfU1IlUr4FVJv7fvTBLyQc%2BR2zxP3db6PoRhz5NErU7rVI8G58HwDhFDSESExly5SoCEK32woIvGUoinCM5EiattIVftHOihk5ct2MotHMf4hkErTASBjeyua1YRb0wWtXLPbePfvCJucU22LuhQI%2Fsq30Eq9pyucMqaxM0KqLrfcDNY%2FDGP%2Fg6ME%2BLLNVFvEdra0BBpCC9hIF5kk65Az3JAHt66HOBCsM2ewdwjvUl2Ymbnr9gaarW7N4MrxBrCFXsPurN8rAVYqZ6TuIi1FYu4FwuL8rWgyO3f5%2BlN41PNREWd9dXVYvioK%2FjkfhzbNzc1ZHCF1xQ1OY9aBzgZnrsRXKK7b3S69QWAl%2FAPuWuZJ4tWCWpYzkomkJEnl9nLG43iCgpQvUOeKufVfAydKnBBWbap9ZO02YsUi8TrMAMPPusT8VgglLvUD9bzPPya9eNiNPDkyuyYLePIU8uDd0dS7%2FbJQmo5dnW5I%2FgAfBwIYz1uAIvey4UVQZA1KGbRfeozTryR%2BniKZcw8o4YC8FUygs6HWDNQ47mVtSKSdjfBffyEww59fAywY6pgGb%2BoHFkMetPs5qDbaEb%2FfEsVI256ijzZ%2Bw1v7XPGa5gMubpcj4gQeodaOAsbdVHH%2B9iy01BhWUruUWqZEQe8L0%2FsiFs9sKEcWPYAuyS6OHkMofB9dCsHb2AZW%2BliIZSO9sPXIiBHXgx7oUig%2FXN3JXWYz5xDaiF1n%2BHt4N3dtMR7L0MOAZ5RQ1gOIggOhC%2BTkhDW%2FLvx0bCnVs%2BvVTLQf%2FRH%2Facck3&X-Amz-Signature=22d91b6d3c292fb37e51d0bbd13665ac09985e4e03ebc829b7cce02669c253f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJUVK4W%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9sBes%2BB81dlpXj6Ln3oL7vbTy76VUEfoexrLkflVwVAiAuCpOzZ0Ie9JJmYDMV56AGJWA1dho%2Flpt45bgc9E%2Bq9CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbkiVoyK%2Byvtp3hCMKtwDuEc3hnOJ5GHdXfPZjyKIRowHd1AT1B0lBe%2BJZ440OI%2B5wInnjUFXIrepQgG5BB7QGT9tbDkl7%2FRfU1IlUr4FVJv7fvTBLyQc%2BR2zxP3db6PoRhz5NErU7rVI8G58HwDhFDSESExly5SoCEK32woIvGUoinCM5EiattIVftHOihk5ct2MotHMf4hkErTASBjeyua1YRb0wWtXLPbePfvCJucU22LuhQI%2Fsq30Eq9pyucMqaxM0KqLrfcDNY%2FDGP%2Fg6ME%2BLLNVFvEdra0BBpCC9hIF5kk65Az3JAHt66HOBCsM2ewdwjvUl2Ymbnr9gaarW7N4MrxBrCFXsPurN8rAVYqZ6TuIi1FYu4FwuL8rWgyO3f5%2BlN41PNREWd9dXVYvioK%2FjkfhzbNzc1ZHCF1xQ1OY9aBzgZnrsRXKK7b3S69QWAl%2FAPuWuZJ4tWCWpYzkomkJEnl9nLG43iCgpQvUOeKufVfAydKnBBWbap9ZO02YsUi8TrMAMPPusT8VgglLvUD9bzPPya9eNiNPDkyuyYLePIU8uDd0dS7%2FbJQmo5dnW5I%2FgAfBwIYz1uAIvey4UVQZA1KGbRfeozTryR%2BniKZcw8o4YC8FUygs6HWDNQ47mVtSKSdjfBffyEww59fAywY6pgGb%2BoHFkMetPs5qDbaEb%2FfEsVI256ijzZ%2Bw1v7XPGa5gMubpcj4gQeodaOAsbdVHH%2B9iy01BhWUruUWqZEQe8L0%2FsiFs9sKEcWPYAuyS6OHkMofB9dCsHb2AZW%2BliIZSO9sPXIiBHXgx7oUig%2FXN3JXWYz5xDaiF1n%2BHt4N3dtMR7L0MOAZ5RQ1gOIggOhC%2BTkhDW%2FLvx0bCnVs%2BvVTLQf%2FRH%2Facck3&X-Amz-Signature=50a4ac35d7b8628d8dc2eb77a3a73b89cc0089ff67603edd4a6692d03bfd7d48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJUVK4W%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9sBes%2BB81dlpXj6Ln3oL7vbTy76VUEfoexrLkflVwVAiAuCpOzZ0Ie9JJmYDMV56AGJWA1dho%2Flpt45bgc9E%2Bq9CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbkiVoyK%2Byvtp3hCMKtwDuEc3hnOJ5GHdXfPZjyKIRowHd1AT1B0lBe%2BJZ440OI%2B5wInnjUFXIrepQgG5BB7QGT9tbDkl7%2FRfU1IlUr4FVJv7fvTBLyQc%2BR2zxP3db6PoRhz5NErU7rVI8G58HwDhFDSESExly5SoCEK32woIvGUoinCM5EiattIVftHOihk5ct2MotHMf4hkErTASBjeyua1YRb0wWtXLPbePfvCJucU22LuhQI%2Fsq30Eq9pyucMqaxM0KqLrfcDNY%2FDGP%2Fg6ME%2BLLNVFvEdra0BBpCC9hIF5kk65Az3JAHt66HOBCsM2ewdwjvUl2Ymbnr9gaarW7N4MrxBrCFXsPurN8rAVYqZ6TuIi1FYu4FwuL8rWgyO3f5%2BlN41PNREWd9dXVYvioK%2FjkfhzbNzc1ZHCF1xQ1OY9aBzgZnrsRXKK7b3S69QWAl%2FAPuWuZJ4tWCWpYzkomkJEnl9nLG43iCgpQvUOeKufVfAydKnBBWbap9ZO02YsUi8TrMAMPPusT8VgglLvUD9bzPPya9eNiNPDkyuyYLePIU8uDd0dS7%2FbJQmo5dnW5I%2FgAfBwIYz1uAIvey4UVQZA1KGbRfeozTryR%2BniKZcw8o4YC8FUygs6HWDNQ47mVtSKSdjfBffyEww59fAywY6pgGb%2BoHFkMetPs5qDbaEb%2FfEsVI256ijzZ%2Bw1v7XPGa5gMubpcj4gQeodaOAsbdVHH%2B9iy01BhWUruUWqZEQe8L0%2FsiFs9sKEcWPYAuyS6OHkMofB9dCsHb2AZW%2BliIZSO9sPXIiBHXgx7oUig%2FXN3JXWYz5xDaiF1n%2BHt4N3dtMR7L0MOAZ5RQ1gOIggOhC%2BTkhDW%2FLvx0bCnVs%2BvVTLQf%2FRH%2Facck3&X-Amz-Signature=276c29f0e7c4f4f174b19c4e5057bb247cecade95c023704cec2f585e95ef464&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJUVK4W%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9sBes%2BB81dlpXj6Ln3oL7vbTy76VUEfoexrLkflVwVAiAuCpOzZ0Ie9JJmYDMV56AGJWA1dho%2Flpt45bgc9E%2Bq9CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbkiVoyK%2Byvtp3hCMKtwDuEc3hnOJ5GHdXfPZjyKIRowHd1AT1B0lBe%2BJZ440OI%2B5wInnjUFXIrepQgG5BB7QGT9tbDkl7%2FRfU1IlUr4FVJv7fvTBLyQc%2BR2zxP3db6PoRhz5NErU7rVI8G58HwDhFDSESExly5SoCEK32woIvGUoinCM5EiattIVftHOihk5ct2MotHMf4hkErTASBjeyua1YRb0wWtXLPbePfvCJucU22LuhQI%2Fsq30Eq9pyucMqaxM0KqLrfcDNY%2FDGP%2Fg6ME%2BLLNVFvEdra0BBpCC9hIF5kk65Az3JAHt66HOBCsM2ewdwjvUl2Ymbnr9gaarW7N4MrxBrCFXsPurN8rAVYqZ6TuIi1FYu4FwuL8rWgyO3f5%2BlN41PNREWd9dXVYvioK%2FjkfhzbNzc1ZHCF1xQ1OY9aBzgZnrsRXKK7b3S69QWAl%2FAPuWuZJ4tWCWpYzkomkJEnl9nLG43iCgpQvUOeKufVfAydKnBBWbap9ZO02YsUi8TrMAMPPusT8VgglLvUD9bzPPya9eNiNPDkyuyYLePIU8uDd0dS7%2FbJQmo5dnW5I%2FgAfBwIYz1uAIvey4UVQZA1KGbRfeozTryR%2BniKZcw8o4YC8FUygs6HWDNQ47mVtSKSdjfBffyEww59fAywY6pgGb%2BoHFkMetPs5qDbaEb%2FfEsVI256ijzZ%2Bw1v7XPGa5gMubpcj4gQeodaOAsbdVHH%2B9iy01BhWUruUWqZEQe8L0%2FsiFs9sKEcWPYAuyS6OHkMofB9dCsHb2AZW%2BliIZSO9sPXIiBHXgx7oUig%2FXN3JXWYz5xDaiF1n%2BHt4N3dtMR7L0MOAZ5RQ1gOIggOhC%2BTkhDW%2FLvx0bCnVs%2BvVTLQf%2FRH%2Facck3&X-Amz-Signature=c2ebf0aef53305dc48b8639fdfabf411b41858471f40ec398f94cf818495acec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJUVK4W%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9sBes%2BB81dlpXj6Ln3oL7vbTy76VUEfoexrLkflVwVAiAuCpOzZ0Ie9JJmYDMV56AGJWA1dho%2Flpt45bgc9E%2Bq9CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbkiVoyK%2Byvtp3hCMKtwDuEc3hnOJ5GHdXfPZjyKIRowHd1AT1B0lBe%2BJZ440OI%2B5wInnjUFXIrepQgG5BB7QGT9tbDkl7%2FRfU1IlUr4FVJv7fvTBLyQc%2BR2zxP3db6PoRhz5NErU7rVI8G58HwDhFDSESExly5SoCEK32woIvGUoinCM5EiattIVftHOihk5ct2MotHMf4hkErTASBjeyua1YRb0wWtXLPbePfvCJucU22LuhQI%2Fsq30Eq9pyucMqaxM0KqLrfcDNY%2FDGP%2Fg6ME%2BLLNVFvEdra0BBpCC9hIF5kk65Az3JAHt66HOBCsM2ewdwjvUl2Ymbnr9gaarW7N4MrxBrCFXsPurN8rAVYqZ6TuIi1FYu4FwuL8rWgyO3f5%2BlN41PNREWd9dXVYvioK%2FjkfhzbNzc1ZHCF1xQ1OY9aBzgZnrsRXKK7b3S69QWAl%2FAPuWuZJ4tWCWpYzkomkJEnl9nLG43iCgpQvUOeKufVfAydKnBBWbap9ZO02YsUi8TrMAMPPusT8VgglLvUD9bzPPya9eNiNPDkyuyYLePIU8uDd0dS7%2FbJQmo5dnW5I%2FgAfBwIYz1uAIvey4UVQZA1KGbRfeozTryR%2BniKZcw8o4YC8FUygs6HWDNQ47mVtSKSdjfBffyEww59fAywY6pgGb%2BoHFkMetPs5qDbaEb%2FfEsVI256ijzZ%2Bw1v7XPGa5gMubpcj4gQeodaOAsbdVHH%2B9iy01BhWUruUWqZEQe8L0%2FsiFs9sKEcWPYAuyS6OHkMofB9dCsHb2AZW%2BliIZSO9sPXIiBHXgx7oUig%2FXN3JXWYz5xDaiF1n%2BHt4N3dtMR7L0MOAZ5RQ1gOIggOhC%2BTkhDW%2FLvx0bCnVs%2BvVTLQf%2FRH%2Facck3&X-Amz-Signature=70b046dc2b39f3b21dcaf3b5df9476000a2e08f217984eef2610875ec897eb03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXJUVK4W%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9sBes%2BB81dlpXj6Ln3oL7vbTy76VUEfoexrLkflVwVAiAuCpOzZ0Ie9JJmYDMV56AGJWA1dho%2Flpt45bgc9E%2Bq9CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbkiVoyK%2Byvtp3hCMKtwDuEc3hnOJ5GHdXfPZjyKIRowHd1AT1B0lBe%2BJZ440OI%2B5wInnjUFXIrepQgG5BB7QGT9tbDkl7%2FRfU1IlUr4FVJv7fvTBLyQc%2BR2zxP3db6PoRhz5NErU7rVI8G58HwDhFDSESExly5SoCEK32woIvGUoinCM5EiattIVftHOihk5ct2MotHMf4hkErTASBjeyua1YRb0wWtXLPbePfvCJucU22LuhQI%2Fsq30Eq9pyucMqaxM0KqLrfcDNY%2FDGP%2Fg6ME%2BLLNVFvEdra0BBpCC9hIF5kk65Az3JAHt66HOBCsM2ewdwjvUl2Ymbnr9gaarW7N4MrxBrCFXsPurN8rAVYqZ6TuIi1FYu4FwuL8rWgyO3f5%2BlN41PNREWd9dXVYvioK%2FjkfhzbNzc1ZHCF1xQ1OY9aBzgZnrsRXKK7b3S69QWAl%2FAPuWuZJ4tWCWpYzkomkJEnl9nLG43iCgpQvUOeKufVfAydKnBBWbap9ZO02YsUi8TrMAMPPusT8VgglLvUD9bzPPya9eNiNPDkyuyYLePIU8uDd0dS7%2FbJQmo5dnW5I%2FgAfBwIYz1uAIvey4UVQZA1KGbRfeozTryR%2BniKZcw8o4YC8FUygs6HWDNQ47mVtSKSdjfBffyEww59fAywY6pgGb%2BoHFkMetPs5qDbaEb%2FfEsVI256ijzZ%2Bw1v7XPGa5gMubpcj4gQeodaOAsbdVHH%2B9iy01BhWUruUWqZEQe8L0%2FsiFs9sKEcWPYAuyS6OHkMofB9dCsHb2AZW%2BliIZSO9sPXIiBHXgx7oUig%2FXN3JXWYz5xDaiF1n%2BHt4N3dtMR7L0MOAZ5RQ1gOIggOhC%2BTkhDW%2FLvx0bCnVs%2BvVTLQf%2FRH%2Facck3&X-Amz-Signature=00d4d04fe01e4e9831fd04314608b0de6e0c115816863cbda8ee48492d4d6d42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

