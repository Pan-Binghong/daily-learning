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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWYOJM6%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzojYQAAXKrB6tCDZCYt3AslZC257%2Bwu1OiOOUxdc9hAiAxixy4kVKiiVa%2BVtzTH7L1%2Bz%2F9bIdpBTYYbmQszmjBPiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLcwqNpx4%2B7QEZWRsKtwDEUl4CUFAB4eFvf1jfoMym0ycbKJwuxyycnq4WM6iHXud7dxS9%2F7RJQrUZ%2FmmRLjXakQ9Oc4TBrp1ml%2BLshst4a4nVuZfKSLdRe0HrgxYiu4JKw6lNECGhR%2ForiRq8G00qRbeogm5cAMjvdXsjCNNv1qJPrckuLecX6I6TDesoi5lmP3HvRIMDarOG495cKaRublquaXD3fqgxTq1URpP7W%2BUOvluLkrxtGr0KJ%2FHN4MEw625420x5d2CVPU4NYFB%2FKXCDu11o3vkrToVc3iVL%2FuId1wmLkm1%2Bk3q2y3MPocSvvnCBGmNEmbxpnvVV63HbFyxGE2PUYACgXP%2FdYhrd%2Bg2yCKA7mt6PPk%2Bx6VWHD9uI9pfvGsCc4sjYG1%2BkMDOAokv8lT9OkU55UcTbfKh%2B7EfIpR5d0rCIx2LokedPp9T2WaOdeCKMdzin7aW9dwDGnG8JWGA5Uf3UWdo7mfO6UdEtybjrOS06FtDI2AoIpPX%2BzoALc0URwGd8q5YKf1VyZ2uNGUCCw0aRjGE9%2FbwQftu5aHxmzR6a6xOCl1XSt7QGCIN5drB%2FPw36FpxO1w9tklV1qp30SL4rBchcuja59yiYCGzo9qpZc%2B9JERDZexOmPwLs5hnb%2FfZVAUwuMqNygY6pgGpfgBoqMiuARPNCWkvCiu7k%2F8YeMgeA8gHFjrn6gKC8Ve2Bn2UeCfE8qUBfTmZRpsZge06kPRUul%2FWxBpOwlYllATo6qm82cjIvOQFfk2viGHCWpKrPnaaqd66cdypcyfN7z%2BJbq9UPbGg0ijhTmRMatQkLHNE0y9Vx9f8h1kabLu0%2FeDyyU5DG10iR6Iw2cF5UUeBnZ5d0%2FBFLKp3Iu7yUSMC6VzE&X-Amz-Signature=10675fdf29e6e55169eff6f4ad4756967c145352ce3086cd06e0152428c01cce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWYOJM6%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzojYQAAXKrB6tCDZCYt3AslZC257%2Bwu1OiOOUxdc9hAiAxixy4kVKiiVa%2BVtzTH7L1%2Bz%2F9bIdpBTYYbmQszmjBPiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLcwqNpx4%2B7QEZWRsKtwDEUl4CUFAB4eFvf1jfoMym0ycbKJwuxyycnq4WM6iHXud7dxS9%2F7RJQrUZ%2FmmRLjXakQ9Oc4TBrp1ml%2BLshst4a4nVuZfKSLdRe0HrgxYiu4JKw6lNECGhR%2ForiRq8G00qRbeogm5cAMjvdXsjCNNv1qJPrckuLecX6I6TDesoi5lmP3HvRIMDarOG495cKaRublquaXD3fqgxTq1URpP7W%2BUOvluLkrxtGr0KJ%2FHN4MEw625420x5d2CVPU4NYFB%2FKXCDu11o3vkrToVc3iVL%2FuId1wmLkm1%2Bk3q2y3MPocSvvnCBGmNEmbxpnvVV63HbFyxGE2PUYACgXP%2FdYhrd%2Bg2yCKA7mt6PPk%2Bx6VWHD9uI9pfvGsCc4sjYG1%2BkMDOAokv8lT9OkU55UcTbfKh%2B7EfIpR5d0rCIx2LokedPp9T2WaOdeCKMdzin7aW9dwDGnG8JWGA5Uf3UWdo7mfO6UdEtybjrOS06FtDI2AoIpPX%2BzoALc0URwGd8q5YKf1VyZ2uNGUCCw0aRjGE9%2FbwQftu5aHxmzR6a6xOCl1XSt7QGCIN5drB%2FPw36FpxO1w9tklV1qp30SL4rBchcuja59yiYCGzo9qpZc%2B9JERDZexOmPwLs5hnb%2FfZVAUwuMqNygY6pgGpfgBoqMiuARPNCWkvCiu7k%2F8YeMgeA8gHFjrn6gKC8Ve2Bn2UeCfE8qUBfTmZRpsZge06kPRUul%2FWxBpOwlYllATo6qm82cjIvOQFfk2viGHCWpKrPnaaqd66cdypcyfN7z%2BJbq9UPbGg0ijhTmRMatQkLHNE0y9Vx9f8h1kabLu0%2FeDyyU5DG10iR6Iw2cF5UUeBnZ5d0%2FBFLKp3Iu7yUSMC6VzE&X-Amz-Signature=d1f6f1cd13ea6ea71744d3fc1a09b792ec3bb89bf66c030f5a222c973687238d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWYOJM6%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzojYQAAXKrB6tCDZCYt3AslZC257%2Bwu1OiOOUxdc9hAiAxixy4kVKiiVa%2BVtzTH7L1%2Bz%2F9bIdpBTYYbmQszmjBPiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLcwqNpx4%2B7QEZWRsKtwDEUl4CUFAB4eFvf1jfoMym0ycbKJwuxyycnq4WM6iHXud7dxS9%2F7RJQrUZ%2FmmRLjXakQ9Oc4TBrp1ml%2BLshst4a4nVuZfKSLdRe0HrgxYiu4JKw6lNECGhR%2ForiRq8G00qRbeogm5cAMjvdXsjCNNv1qJPrckuLecX6I6TDesoi5lmP3HvRIMDarOG495cKaRublquaXD3fqgxTq1URpP7W%2BUOvluLkrxtGr0KJ%2FHN4MEw625420x5d2CVPU4NYFB%2FKXCDu11o3vkrToVc3iVL%2FuId1wmLkm1%2Bk3q2y3MPocSvvnCBGmNEmbxpnvVV63HbFyxGE2PUYACgXP%2FdYhrd%2Bg2yCKA7mt6PPk%2Bx6VWHD9uI9pfvGsCc4sjYG1%2BkMDOAokv8lT9OkU55UcTbfKh%2B7EfIpR5d0rCIx2LokedPp9T2WaOdeCKMdzin7aW9dwDGnG8JWGA5Uf3UWdo7mfO6UdEtybjrOS06FtDI2AoIpPX%2BzoALc0URwGd8q5YKf1VyZ2uNGUCCw0aRjGE9%2FbwQftu5aHxmzR6a6xOCl1XSt7QGCIN5drB%2FPw36FpxO1w9tklV1qp30SL4rBchcuja59yiYCGzo9qpZc%2B9JERDZexOmPwLs5hnb%2FfZVAUwuMqNygY6pgGpfgBoqMiuARPNCWkvCiu7k%2F8YeMgeA8gHFjrn6gKC8Ve2Bn2UeCfE8qUBfTmZRpsZge06kPRUul%2FWxBpOwlYllATo6qm82cjIvOQFfk2viGHCWpKrPnaaqd66cdypcyfN7z%2BJbq9UPbGg0ijhTmRMatQkLHNE0y9Vx9f8h1kabLu0%2FeDyyU5DG10iR6Iw2cF5UUeBnZ5d0%2FBFLKp3Iu7yUSMC6VzE&X-Amz-Signature=fb28014da253ef59d5397597e40333baf7fb255c745ff21b033d2a56d26cc59f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWYOJM6%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzojYQAAXKrB6tCDZCYt3AslZC257%2Bwu1OiOOUxdc9hAiAxixy4kVKiiVa%2BVtzTH7L1%2Bz%2F9bIdpBTYYbmQszmjBPiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLcwqNpx4%2B7QEZWRsKtwDEUl4CUFAB4eFvf1jfoMym0ycbKJwuxyycnq4WM6iHXud7dxS9%2F7RJQrUZ%2FmmRLjXakQ9Oc4TBrp1ml%2BLshst4a4nVuZfKSLdRe0HrgxYiu4JKw6lNECGhR%2ForiRq8G00qRbeogm5cAMjvdXsjCNNv1qJPrckuLecX6I6TDesoi5lmP3HvRIMDarOG495cKaRublquaXD3fqgxTq1URpP7W%2BUOvluLkrxtGr0KJ%2FHN4MEw625420x5d2CVPU4NYFB%2FKXCDu11o3vkrToVc3iVL%2FuId1wmLkm1%2Bk3q2y3MPocSvvnCBGmNEmbxpnvVV63HbFyxGE2PUYACgXP%2FdYhrd%2Bg2yCKA7mt6PPk%2Bx6VWHD9uI9pfvGsCc4sjYG1%2BkMDOAokv8lT9OkU55UcTbfKh%2B7EfIpR5d0rCIx2LokedPp9T2WaOdeCKMdzin7aW9dwDGnG8JWGA5Uf3UWdo7mfO6UdEtybjrOS06FtDI2AoIpPX%2BzoALc0URwGd8q5YKf1VyZ2uNGUCCw0aRjGE9%2FbwQftu5aHxmzR6a6xOCl1XSt7QGCIN5drB%2FPw36FpxO1w9tklV1qp30SL4rBchcuja59yiYCGzo9qpZc%2B9JERDZexOmPwLs5hnb%2FfZVAUwuMqNygY6pgGpfgBoqMiuARPNCWkvCiu7k%2F8YeMgeA8gHFjrn6gKC8Ve2Bn2UeCfE8qUBfTmZRpsZge06kPRUul%2FWxBpOwlYllATo6qm82cjIvOQFfk2viGHCWpKrPnaaqd66cdypcyfN7z%2BJbq9UPbGg0ijhTmRMatQkLHNE0y9Vx9f8h1kabLu0%2FeDyyU5DG10iR6Iw2cF5UUeBnZ5d0%2FBFLKp3Iu7yUSMC6VzE&X-Amz-Signature=2c4f240a7fc80ddc046493e1f621d2850e1c48808d6f8f2eb9a03bea9368c92d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWYOJM6%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzojYQAAXKrB6tCDZCYt3AslZC257%2Bwu1OiOOUxdc9hAiAxixy4kVKiiVa%2BVtzTH7L1%2Bz%2F9bIdpBTYYbmQszmjBPiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLcwqNpx4%2B7QEZWRsKtwDEUl4CUFAB4eFvf1jfoMym0ycbKJwuxyycnq4WM6iHXud7dxS9%2F7RJQrUZ%2FmmRLjXakQ9Oc4TBrp1ml%2BLshst4a4nVuZfKSLdRe0HrgxYiu4JKw6lNECGhR%2ForiRq8G00qRbeogm5cAMjvdXsjCNNv1qJPrckuLecX6I6TDesoi5lmP3HvRIMDarOG495cKaRublquaXD3fqgxTq1URpP7W%2BUOvluLkrxtGr0KJ%2FHN4MEw625420x5d2CVPU4NYFB%2FKXCDu11o3vkrToVc3iVL%2FuId1wmLkm1%2Bk3q2y3MPocSvvnCBGmNEmbxpnvVV63HbFyxGE2PUYACgXP%2FdYhrd%2Bg2yCKA7mt6PPk%2Bx6VWHD9uI9pfvGsCc4sjYG1%2BkMDOAokv8lT9OkU55UcTbfKh%2B7EfIpR5d0rCIx2LokedPp9T2WaOdeCKMdzin7aW9dwDGnG8JWGA5Uf3UWdo7mfO6UdEtybjrOS06FtDI2AoIpPX%2BzoALc0URwGd8q5YKf1VyZ2uNGUCCw0aRjGE9%2FbwQftu5aHxmzR6a6xOCl1XSt7QGCIN5drB%2FPw36FpxO1w9tklV1qp30SL4rBchcuja59yiYCGzo9qpZc%2B9JERDZexOmPwLs5hnb%2FfZVAUwuMqNygY6pgGpfgBoqMiuARPNCWkvCiu7k%2F8YeMgeA8gHFjrn6gKC8Ve2Bn2UeCfE8qUBfTmZRpsZge06kPRUul%2FWxBpOwlYllATo6qm82cjIvOQFfk2viGHCWpKrPnaaqd66cdypcyfN7z%2BJbq9UPbGg0ijhTmRMatQkLHNE0y9Vx9f8h1kabLu0%2FeDyyU5DG10iR6Iw2cF5UUeBnZ5d0%2FBFLKp3Iu7yUSMC6VzE&X-Amz-Signature=3734609d37afb5989fa82521f0e14cd905a32ae8ceba76a988065b87668ab88d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWYOJM6%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzojYQAAXKrB6tCDZCYt3AslZC257%2Bwu1OiOOUxdc9hAiAxixy4kVKiiVa%2BVtzTH7L1%2Bz%2F9bIdpBTYYbmQszmjBPiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLcwqNpx4%2B7QEZWRsKtwDEUl4CUFAB4eFvf1jfoMym0ycbKJwuxyycnq4WM6iHXud7dxS9%2F7RJQrUZ%2FmmRLjXakQ9Oc4TBrp1ml%2BLshst4a4nVuZfKSLdRe0HrgxYiu4JKw6lNECGhR%2ForiRq8G00qRbeogm5cAMjvdXsjCNNv1qJPrckuLecX6I6TDesoi5lmP3HvRIMDarOG495cKaRublquaXD3fqgxTq1URpP7W%2BUOvluLkrxtGr0KJ%2FHN4MEw625420x5d2CVPU4NYFB%2FKXCDu11o3vkrToVc3iVL%2FuId1wmLkm1%2Bk3q2y3MPocSvvnCBGmNEmbxpnvVV63HbFyxGE2PUYACgXP%2FdYhrd%2Bg2yCKA7mt6PPk%2Bx6VWHD9uI9pfvGsCc4sjYG1%2BkMDOAokv8lT9OkU55UcTbfKh%2B7EfIpR5d0rCIx2LokedPp9T2WaOdeCKMdzin7aW9dwDGnG8JWGA5Uf3UWdo7mfO6UdEtybjrOS06FtDI2AoIpPX%2BzoALc0URwGd8q5YKf1VyZ2uNGUCCw0aRjGE9%2FbwQftu5aHxmzR6a6xOCl1XSt7QGCIN5drB%2FPw36FpxO1w9tklV1qp30SL4rBchcuja59yiYCGzo9qpZc%2B9JERDZexOmPwLs5hnb%2FfZVAUwuMqNygY6pgGpfgBoqMiuARPNCWkvCiu7k%2F8YeMgeA8gHFjrn6gKC8Ve2Bn2UeCfE8qUBfTmZRpsZge06kPRUul%2FWxBpOwlYllATo6qm82cjIvOQFfk2viGHCWpKrPnaaqd66cdypcyfN7z%2BJbq9UPbGg0ijhTmRMatQkLHNE0y9Vx9f8h1kabLu0%2FeDyyU5DG10iR6Iw2cF5UUeBnZ5d0%2FBFLKp3Iu7yUSMC6VzE&X-Amz-Signature=43f09d1d0417c464c78f3d7ed42fec31b714b217b40417f423a672cf1cdbb021&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWYOJM6%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzojYQAAXKrB6tCDZCYt3AslZC257%2Bwu1OiOOUxdc9hAiAxixy4kVKiiVa%2BVtzTH7L1%2Bz%2F9bIdpBTYYbmQszmjBPiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLcwqNpx4%2B7QEZWRsKtwDEUl4CUFAB4eFvf1jfoMym0ycbKJwuxyycnq4WM6iHXud7dxS9%2F7RJQrUZ%2FmmRLjXakQ9Oc4TBrp1ml%2BLshst4a4nVuZfKSLdRe0HrgxYiu4JKw6lNECGhR%2ForiRq8G00qRbeogm5cAMjvdXsjCNNv1qJPrckuLecX6I6TDesoi5lmP3HvRIMDarOG495cKaRublquaXD3fqgxTq1URpP7W%2BUOvluLkrxtGr0KJ%2FHN4MEw625420x5d2CVPU4NYFB%2FKXCDu11o3vkrToVc3iVL%2FuId1wmLkm1%2Bk3q2y3MPocSvvnCBGmNEmbxpnvVV63HbFyxGE2PUYACgXP%2FdYhrd%2Bg2yCKA7mt6PPk%2Bx6VWHD9uI9pfvGsCc4sjYG1%2BkMDOAokv8lT9OkU55UcTbfKh%2B7EfIpR5d0rCIx2LokedPp9T2WaOdeCKMdzin7aW9dwDGnG8JWGA5Uf3UWdo7mfO6UdEtybjrOS06FtDI2AoIpPX%2BzoALc0URwGd8q5YKf1VyZ2uNGUCCw0aRjGE9%2FbwQftu5aHxmzR6a6xOCl1XSt7QGCIN5drB%2FPw36FpxO1w9tklV1qp30SL4rBchcuja59yiYCGzo9qpZc%2B9JERDZexOmPwLs5hnb%2FfZVAUwuMqNygY6pgGpfgBoqMiuARPNCWkvCiu7k%2F8YeMgeA8gHFjrn6gKC8Ve2Bn2UeCfE8qUBfTmZRpsZge06kPRUul%2FWxBpOwlYllATo6qm82cjIvOQFfk2viGHCWpKrPnaaqd66cdypcyfN7z%2BJbq9UPbGg0ijhTmRMatQkLHNE0y9Vx9f8h1kabLu0%2FeDyyU5DG10iR6Iw2cF5UUeBnZ5d0%2FBFLKp3Iu7yUSMC6VzE&X-Amz-Signature=39ef0dedaf86d3948272bf3d6561f3cae16cdbff12522c015acfec784e165e39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWYOJM6%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzojYQAAXKrB6tCDZCYt3AslZC257%2Bwu1OiOOUxdc9hAiAxixy4kVKiiVa%2BVtzTH7L1%2Bz%2F9bIdpBTYYbmQszmjBPiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLcwqNpx4%2B7QEZWRsKtwDEUl4CUFAB4eFvf1jfoMym0ycbKJwuxyycnq4WM6iHXud7dxS9%2F7RJQrUZ%2FmmRLjXakQ9Oc4TBrp1ml%2BLshst4a4nVuZfKSLdRe0HrgxYiu4JKw6lNECGhR%2ForiRq8G00qRbeogm5cAMjvdXsjCNNv1qJPrckuLecX6I6TDesoi5lmP3HvRIMDarOG495cKaRublquaXD3fqgxTq1URpP7W%2BUOvluLkrxtGr0KJ%2FHN4MEw625420x5d2CVPU4NYFB%2FKXCDu11o3vkrToVc3iVL%2FuId1wmLkm1%2Bk3q2y3MPocSvvnCBGmNEmbxpnvVV63HbFyxGE2PUYACgXP%2FdYhrd%2Bg2yCKA7mt6PPk%2Bx6VWHD9uI9pfvGsCc4sjYG1%2BkMDOAokv8lT9OkU55UcTbfKh%2B7EfIpR5d0rCIx2LokedPp9T2WaOdeCKMdzin7aW9dwDGnG8JWGA5Uf3UWdo7mfO6UdEtybjrOS06FtDI2AoIpPX%2BzoALc0URwGd8q5YKf1VyZ2uNGUCCw0aRjGE9%2FbwQftu5aHxmzR6a6xOCl1XSt7QGCIN5drB%2FPw36FpxO1w9tklV1qp30SL4rBchcuja59yiYCGzo9qpZc%2B9JERDZexOmPwLs5hnb%2FfZVAUwuMqNygY6pgGpfgBoqMiuARPNCWkvCiu7k%2F8YeMgeA8gHFjrn6gKC8Ve2Bn2UeCfE8qUBfTmZRpsZge06kPRUul%2FWxBpOwlYllATo6qm82cjIvOQFfk2viGHCWpKrPnaaqd66cdypcyfN7z%2BJbq9UPbGg0ijhTmRMatQkLHNE0y9Vx9f8h1kabLu0%2FeDyyU5DG10iR6Iw2cF5UUeBnZ5d0%2FBFLKp3Iu7yUSMC6VzE&X-Amz-Signature=408b756593f79c3976ade2f26652f1e990771e2b6b3866b50bdea644089938b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWYOJM6%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzojYQAAXKrB6tCDZCYt3AslZC257%2Bwu1OiOOUxdc9hAiAxixy4kVKiiVa%2BVtzTH7L1%2Bz%2F9bIdpBTYYbmQszmjBPiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLcwqNpx4%2B7QEZWRsKtwDEUl4CUFAB4eFvf1jfoMym0ycbKJwuxyycnq4WM6iHXud7dxS9%2F7RJQrUZ%2FmmRLjXakQ9Oc4TBrp1ml%2BLshst4a4nVuZfKSLdRe0HrgxYiu4JKw6lNECGhR%2ForiRq8G00qRbeogm5cAMjvdXsjCNNv1qJPrckuLecX6I6TDesoi5lmP3HvRIMDarOG495cKaRublquaXD3fqgxTq1URpP7W%2BUOvluLkrxtGr0KJ%2FHN4MEw625420x5d2CVPU4NYFB%2FKXCDu11o3vkrToVc3iVL%2FuId1wmLkm1%2Bk3q2y3MPocSvvnCBGmNEmbxpnvVV63HbFyxGE2PUYACgXP%2FdYhrd%2Bg2yCKA7mt6PPk%2Bx6VWHD9uI9pfvGsCc4sjYG1%2BkMDOAokv8lT9OkU55UcTbfKh%2B7EfIpR5d0rCIx2LokedPp9T2WaOdeCKMdzin7aW9dwDGnG8JWGA5Uf3UWdo7mfO6UdEtybjrOS06FtDI2AoIpPX%2BzoALc0URwGd8q5YKf1VyZ2uNGUCCw0aRjGE9%2FbwQftu5aHxmzR6a6xOCl1XSt7QGCIN5drB%2FPw36FpxO1w9tklV1qp30SL4rBchcuja59yiYCGzo9qpZc%2B9JERDZexOmPwLs5hnb%2FfZVAUwuMqNygY6pgGpfgBoqMiuARPNCWkvCiu7k%2F8YeMgeA8gHFjrn6gKC8Ve2Bn2UeCfE8qUBfTmZRpsZge06kPRUul%2FWxBpOwlYllATo6qm82cjIvOQFfk2viGHCWpKrPnaaqd66cdypcyfN7z%2BJbq9UPbGg0ijhTmRMatQkLHNE0y9Vx9f8h1kabLu0%2FeDyyU5DG10iR6Iw2cF5UUeBnZ5d0%2FBFLKp3Iu7yUSMC6VzE&X-Amz-Signature=9cc56e6e0262be0b192cfdc84e274ebed4afb69c2a25a37c0ee66e7f4c26c4fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXWYOJM6%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEzojYQAAXKrB6tCDZCYt3AslZC257%2Bwu1OiOOUxdc9hAiAxixy4kVKiiVa%2BVtzTH7L1%2Bz%2F9bIdpBTYYbmQszmjBPiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLcwqNpx4%2B7QEZWRsKtwDEUl4CUFAB4eFvf1jfoMym0ycbKJwuxyycnq4WM6iHXud7dxS9%2F7RJQrUZ%2FmmRLjXakQ9Oc4TBrp1ml%2BLshst4a4nVuZfKSLdRe0HrgxYiu4JKw6lNECGhR%2ForiRq8G00qRbeogm5cAMjvdXsjCNNv1qJPrckuLecX6I6TDesoi5lmP3HvRIMDarOG495cKaRublquaXD3fqgxTq1URpP7W%2BUOvluLkrxtGr0KJ%2FHN4MEw625420x5d2CVPU4NYFB%2FKXCDu11o3vkrToVc3iVL%2FuId1wmLkm1%2Bk3q2y3MPocSvvnCBGmNEmbxpnvVV63HbFyxGE2PUYACgXP%2FdYhrd%2Bg2yCKA7mt6PPk%2Bx6VWHD9uI9pfvGsCc4sjYG1%2BkMDOAokv8lT9OkU55UcTbfKh%2B7EfIpR5d0rCIx2LokedPp9T2WaOdeCKMdzin7aW9dwDGnG8JWGA5Uf3UWdo7mfO6UdEtybjrOS06FtDI2AoIpPX%2BzoALc0URwGd8q5YKf1VyZ2uNGUCCw0aRjGE9%2FbwQftu5aHxmzR6a6xOCl1XSt7QGCIN5drB%2FPw36FpxO1w9tklV1qp30SL4rBchcuja59yiYCGzo9qpZc%2B9JERDZexOmPwLs5hnb%2FfZVAUwuMqNygY6pgGpfgBoqMiuARPNCWkvCiu7k%2F8YeMgeA8gHFjrn6gKC8Ve2Bn2UeCfE8qUBfTmZRpsZge06kPRUul%2FWxBpOwlYllATo6qm82cjIvOQFfk2viGHCWpKrPnaaqd66cdypcyfN7z%2BJbq9UPbGg0ijhTmRMatQkLHNE0y9Vx9f8h1kabLu0%2FeDyyU5DG10iR6Iw2cF5UUeBnZ5d0%2FBFLKp3Iu7yUSMC6VzE&X-Amz-Signature=bfea774fb8aac7c1476bb48cf49c8c30b5e59e957f793fbbbd87511e943bda24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

