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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROA6CZVW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCEblmbVQZqbTvD8K2hMOqZDPQkRn6Cnwep2XNUCnD1kAIgMxEW8x%2FI6nvdA3I9eOGEEjPtHdc4D74u8F3c%2F8yoWggqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISZGczsOSE9RUzWTSrcA5c5MHj41tNOvoTqgDnYFa3GcAUfHpDeyTgRCYQvASAIeNIO9VBeJ85F1%2Bet9VqwUSmqW9R5JEWD2MCDWXJUPqNtWkREQ4%2BDRZ8sE8LjovUfxzu%2BaC7%2F3tVBInPaX%2BEUd2D02KDvN78C4XuKVULvabxOtm0DHU%2FCx5X8UtHIjBPxrvSF2Xcm8ahD31kL0wFDIgXRhaf4%2BQPdEe317FFZ6mZUh%2BlPbSzf96YjtxFmCJ8LTISe33ej5zL8zwLGKB1YJpnS3id4m%2BOqk%2FFQYdfYJYIBMtNuBMc3ZKyr5Rt%2B%2F6O4D7rpXpi0UDasr3NgdszqjVAFjX%2BNVMfskqeKeIi3hPmft4si8K8%2Ftrziac10sCk%2F2GsxF1AXVZEXWoqkA9DktC3q0ziqjNxkkLzRkj%2F%2B8qVARC3MfMOzAozSO3LqdRmKA7n%2BfWa4tL5bOATNP4npUS8FqbEvvtM7YeYF2yx4rKBKi4%2BbwSPPztD3iAESrBqWqRnh8J0UTGF4siJHcLulgVAp3v%2BjL89e67%2BuqYxi7O623fsK1uKOX7j6tq8iRDUvO590yxefGwlrHVcgAOiKhYluDe8mEI6TmWPwu891WxTYwAJ4qnScRMaTAdFw6uONk3CqtnBN6qY1gey7MPrU7ckGOqUBrywrLNNGFjGVAIV%2Bc98dhbgJkd6U3caljrqVu667PpOsrl7IpQizRgw1GHVvEDcDmnSPoa8yy%2BpfqwMEP8BS%2Fbd1mBNjyCociwZJIwKNNFnXlLU%2B0X1A2zL0QgQZCeo5YFDFiS3M2IDy1OqcXlK1dQlkEZh0HVpCuBw1NKB01mdM20LpvMcS6vnuW%2BHNe1PDhPo8gUcVlXH%2BoYR5Dma%2B6GhtiDN%2F&X-Amz-Signature=133bcdd43a34e0863c42e48a583c390a8a9b71c688e9f136ff7cdba07789662b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROA6CZVW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCEblmbVQZqbTvD8K2hMOqZDPQkRn6Cnwep2XNUCnD1kAIgMxEW8x%2FI6nvdA3I9eOGEEjPtHdc4D74u8F3c%2F8yoWggqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISZGczsOSE9RUzWTSrcA5c5MHj41tNOvoTqgDnYFa3GcAUfHpDeyTgRCYQvASAIeNIO9VBeJ85F1%2Bet9VqwUSmqW9R5JEWD2MCDWXJUPqNtWkREQ4%2BDRZ8sE8LjovUfxzu%2BaC7%2F3tVBInPaX%2BEUd2D02KDvN78C4XuKVULvabxOtm0DHU%2FCx5X8UtHIjBPxrvSF2Xcm8ahD31kL0wFDIgXRhaf4%2BQPdEe317FFZ6mZUh%2BlPbSzf96YjtxFmCJ8LTISe33ej5zL8zwLGKB1YJpnS3id4m%2BOqk%2FFQYdfYJYIBMtNuBMc3ZKyr5Rt%2B%2F6O4D7rpXpi0UDasr3NgdszqjVAFjX%2BNVMfskqeKeIi3hPmft4si8K8%2Ftrziac10sCk%2F2GsxF1AXVZEXWoqkA9DktC3q0ziqjNxkkLzRkj%2F%2B8qVARC3MfMOzAozSO3LqdRmKA7n%2BfWa4tL5bOATNP4npUS8FqbEvvtM7YeYF2yx4rKBKi4%2BbwSPPztD3iAESrBqWqRnh8J0UTGF4siJHcLulgVAp3v%2BjL89e67%2BuqYxi7O623fsK1uKOX7j6tq8iRDUvO590yxefGwlrHVcgAOiKhYluDe8mEI6TmWPwu891WxTYwAJ4qnScRMaTAdFw6uONk3CqtnBN6qY1gey7MPrU7ckGOqUBrywrLNNGFjGVAIV%2Bc98dhbgJkd6U3caljrqVu667PpOsrl7IpQizRgw1GHVvEDcDmnSPoa8yy%2BpfqwMEP8BS%2Fbd1mBNjyCociwZJIwKNNFnXlLU%2B0X1A2zL0QgQZCeo5YFDFiS3M2IDy1OqcXlK1dQlkEZh0HVpCuBw1NKB01mdM20LpvMcS6vnuW%2BHNe1PDhPo8gUcVlXH%2BoYR5Dma%2B6GhtiDN%2F&X-Amz-Signature=c3ee6122d05685e383ab78c7a67877e279a4247778be12c1a350588fbee14f52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROA6CZVW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCEblmbVQZqbTvD8K2hMOqZDPQkRn6Cnwep2XNUCnD1kAIgMxEW8x%2FI6nvdA3I9eOGEEjPtHdc4D74u8F3c%2F8yoWggqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISZGczsOSE9RUzWTSrcA5c5MHj41tNOvoTqgDnYFa3GcAUfHpDeyTgRCYQvASAIeNIO9VBeJ85F1%2Bet9VqwUSmqW9R5JEWD2MCDWXJUPqNtWkREQ4%2BDRZ8sE8LjovUfxzu%2BaC7%2F3tVBInPaX%2BEUd2D02KDvN78C4XuKVULvabxOtm0DHU%2FCx5X8UtHIjBPxrvSF2Xcm8ahD31kL0wFDIgXRhaf4%2BQPdEe317FFZ6mZUh%2BlPbSzf96YjtxFmCJ8LTISe33ej5zL8zwLGKB1YJpnS3id4m%2BOqk%2FFQYdfYJYIBMtNuBMc3ZKyr5Rt%2B%2F6O4D7rpXpi0UDasr3NgdszqjVAFjX%2BNVMfskqeKeIi3hPmft4si8K8%2Ftrziac10sCk%2F2GsxF1AXVZEXWoqkA9DktC3q0ziqjNxkkLzRkj%2F%2B8qVARC3MfMOzAozSO3LqdRmKA7n%2BfWa4tL5bOATNP4npUS8FqbEvvtM7YeYF2yx4rKBKi4%2BbwSPPztD3iAESrBqWqRnh8J0UTGF4siJHcLulgVAp3v%2BjL89e67%2BuqYxi7O623fsK1uKOX7j6tq8iRDUvO590yxefGwlrHVcgAOiKhYluDe8mEI6TmWPwu891WxTYwAJ4qnScRMaTAdFw6uONk3CqtnBN6qY1gey7MPrU7ckGOqUBrywrLNNGFjGVAIV%2Bc98dhbgJkd6U3caljrqVu667PpOsrl7IpQizRgw1GHVvEDcDmnSPoa8yy%2BpfqwMEP8BS%2Fbd1mBNjyCociwZJIwKNNFnXlLU%2B0X1A2zL0QgQZCeo5YFDFiS3M2IDy1OqcXlK1dQlkEZh0HVpCuBw1NKB01mdM20LpvMcS6vnuW%2BHNe1PDhPo8gUcVlXH%2BoYR5Dma%2B6GhtiDN%2F&X-Amz-Signature=0e82c1033a0257f334dfb7995ff94be5d13dac8f349af7c1410329292bcc9f96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROA6CZVW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCEblmbVQZqbTvD8K2hMOqZDPQkRn6Cnwep2XNUCnD1kAIgMxEW8x%2FI6nvdA3I9eOGEEjPtHdc4D74u8F3c%2F8yoWggqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISZGczsOSE9RUzWTSrcA5c5MHj41tNOvoTqgDnYFa3GcAUfHpDeyTgRCYQvASAIeNIO9VBeJ85F1%2Bet9VqwUSmqW9R5JEWD2MCDWXJUPqNtWkREQ4%2BDRZ8sE8LjovUfxzu%2BaC7%2F3tVBInPaX%2BEUd2D02KDvN78C4XuKVULvabxOtm0DHU%2FCx5X8UtHIjBPxrvSF2Xcm8ahD31kL0wFDIgXRhaf4%2BQPdEe317FFZ6mZUh%2BlPbSzf96YjtxFmCJ8LTISe33ej5zL8zwLGKB1YJpnS3id4m%2BOqk%2FFQYdfYJYIBMtNuBMc3ZKyr5Rt%2B%2F6O4D7rpXpi0UDasr3NgdszqjVAFjX%2BNVMfskqeKeIi3hPmft4si8K8%2Ftrziac10sCk%2F2GsxF1AXVZEXWoqkA9DktC3q0ziqjNxkkLzRkj%2F%2B8qVARC3MfMOzAozSO3LqdRmKA7n%2BfWa4tL5bOATNP4npUS8FqbEvvtM7YeYF2yx4rKBKi4%2BbwSPPztD3iAESrBqWqRnh8J0UTGF4siJHcLulgVAp3v%2BjL89e67%2BuqYxi7O623fsK1uKOX7j6tq8iRDUvO590yxefGwlrHVcgAOiKhYluDe8mEI6TmWPwu891WxTYwAJ4qnScRMaTAdFw6uONk3CqtnBN6qY1gey7MPrU7ckGOqUBrywrLNNGFjGVAIV%2Bc98dhbgJkd6U3caljrqVu667PpOsrl7IpQizRgw1GHVvEDcDmnSPoa8yy%2BpfqwMEP8BS%2Fbd1mBNjyCociwZJIwKNNFnXlLU%2B0X1A2zL0QgQZCeo5YFDFiS3M2IDy1OqcXlK1dQlkEZh0HVpCuBw1NKB01mdM20LpvMcS6vnuW%2BHNe1PDhPo8gUcVlXH%2BoYR5Dma%2B6GhtiDN%2F&X-Amz-Signature=6589069ee86a3435cd46553e543f609a95cc3f37fd0d38bcc7523c739fd51ccf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROA6CZVW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCEblmbVQZqbTvD8K2hMOqZDPQkRn6Cnwep2XNUCnD1kAIgMxEW8x%2FI6nvdA3I9eOGEEjPtHdc4D74u8F3c%2F8yoWggqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISZGczsOSE9RUzWTSrcA5c5MHj41tNOvoTqgDnYFa3GcAUfHpDeyTgRCYQvASAIeNIO9VBeJ85F1%2Bet9VqwUSmqW9R5JEWD2MCDWXJUPqNtWkREQ4%2BDRZ8sE8LjovUfxzu%2BaC7%2F3tVBInPaX%2BEUd2D02KDvN78C4XuKVULvabxOtm0DHU%2FCx5X8UtHIjBPxrvSF2Xcm8ahD31kL0wFDIgXRhaf4%2BQPdEe317FFZ6mZUh%2BlPbSzf96YjtxFmCJ8LTISe33ej5zL8zwLGKB1YJpnS3id4m%2BOqk%2FFQYdfYJYIBMtNuBMc3ZKyr5Rt%2B%2F6O4D7rpXpi0UDasr3NgdszqjVAFjX%2BNVMfskqeKeIi3hPmft4si8K8%2Ftrziac10sCk%2F2GsxF1AXVZEXWoqkA9DktC3q0ziqjNxkkLzRkj%2F%2B8qVARC3MfMOzAozSO3LqdRmKA7n%2BfWa4tL5bOATNP4npUS8FqbEvvtM7YeYF2yx4rKBKi4%2BbwSPPztD3iAESrBqWqRnh8J0UTGF4siJHcLulgVAp3v%2BjL89e67%2BuqYxi7O623fsK1uKOX7j6tq8iRDUvO590yxefGwlrHVcgAOiKhYluDe8mEI6TmWPwu891WxTYwAJ4qnScRMaTAdFw6uONk3CqtnBN6qY1gey7MPrU7ckGOqUBrywrLNNGFjGVAIV%2Bc98dhbgJkd6U3caljrqVu667PpOsrl7IpQizRgw1GHVvEDcDmnSPoa8yy%2BpfqwMEP8BS%2Fbd1mBNjyCociwZJIwKNNFnXlLU%2B0X1A2zL0QgQZCeo5YFDFiS3M2IDy1OqcXlK1dQlkEZh0HVpCuBw1NKB01mdM20LpvMcS6vnuW%2BHNe1PDhPo8gUcVlXH%2BoYR5Dma%2B6GhtiDN%2F&X-Amz-Signature=16c2226ed7b2bbb1cb12db858d74935fc8e83d478f8b99cad9c4c86acfe660fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROA6CZVW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCEblmbVQZqbTvD8K2hMOqZDPQkRn6Cnwep2XNUCnD1kAIgMxEW8x%2FI6nvdA3I9eOGEEjPtHdc4D74u8F3c%2F8yoWggqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISZGczsOSE9RUzWTSrcA5c5MHj41tNOvoTqgDnYFa3GcAUfHpDeyTgRCYQvASAIeNIO9VBeJ85F1%2Bet9VqwUSmqW9R5JEWD2MCDWXJUPqNtWkREQ4%2BDRZ8sE8LjovUfxzu%2BaC7%2F3tVBInPaX%2BEUd2D02KDvN78C4XuKVULvabxOtm0DHU%2FCx5X8UtHIjBPxrvSF2Xcm8ahD31kL0wFDIgXRhaf4%2BQPdEe317FFZ6mZUh%2BlPbSzf96YjtxFmCJ8LTISe33ej5zL8zwLGKB1YJpnS3id4m%2BOqk%2FFQYdfYJYIBMtNuBMc3ZKyr5Rt%2B%2F6O4D7rpXpi0UDasr3NgdszqjVAFjX%2BNVMfskqeKeIi3hPmft4si8K8%2Ftrziac10sCk%2F2GsxF1AXVZEXWoqkA9DktC3q0ziqjNxkkLzRkj%2F%2B8qVARC3MfMOzAozSO3LqdRmKA7n%2BfWa4tL5bOATNP4npUS8FqbEvvtM7YeYF2yx4rKBKi4%2BbwSPPztD3iAESrBqWqRnh8J0UTGF4siJHcLulgVAp3v%2BjL89e67%2BuqYxi7O623fsK1uKOX7j6tq8iRDUvO590yxefGwlrHVcgAOiKhYluDe8mEI6TmWPwu891WxTYwAJ4qnScRMaTAdFw6uONk3CqtnBN6qY1gey7MPrU7ckGOqUBrywrLNNGFjGVAIV%2Bc98dhbgJkd6U3caljrqVu667PpOsrl7IpQizRgw1GHVvEDcDmnSPoa8yy%2BpfqwMEP8BS%2Fbd1mBNjyCociwZJIwKNNFnXlLU%2B0X1A2zL0QgQZCeo5YFDFiS3M2IDy1OqcXlK1dQlkEZh0HVpCuBw1NKB01mdM20LpvMcS6vnuW%2BHNe1PDhPo8gUcVlXH%2BoYR5Dma%2B6GhtiDN%2F&X-Amz-Signature=63038fff9da77c54abeff3a7d94a2ef614461810e3dcc2442e8e951126c38f11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROA6CZVW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCEblmbVQZqbTvD8K2hMOqZDPQkRn6Cnwep2XNUCnD1kAIgMxEW8x%2FI6nvdA3I9eOGEEjPtHdc4D74u8F3c%2F8yoWggqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISZGczsOSE9RUzWTSrcA5c5MHj41tNOvoTqgDnYFa3GcAUfHpDeyTgRCYQvASAIeNIO9VBeJ85F1%2Bet9VqwUSmqW9R5JEWD2MCDWXJUPqNtWkREQ4%2BDRZ8sE8LjovUfxzu%2BaC7%2F3tVBInPaX%2BEUd2D02KDvN78C4XuKVULvabxOtm0DHU%2FCx5X8UtHIjBPxrvSF2Xcm8ahD31kL0wFDIgXRhaf4%2BQPdEe317FFZ6mZUh%2BlPbSzf96YjtxFmCJ8LTISe33ej5zL8zwLGKB1YJpnS3id4m%2BOqk%2FFQYdfYJYIBMtNuBMc3ZKyr5Rt%2B%2F6O4D7rpXpi0UDasr3NgdszqjVAFjX%2BNVMfskqeKeIi3hPmft4si8K8%2Ftrziac10sCk%2F2GsxF1AXVZEXWoqkA9DktC3q0ziqjNxkkLzRkj%2F%2B8qVARC3MfMOzAozSO3LqdRmKA7n%2BfWa4tL5bOATNP4npUS8FqbEvvtM7YeYF2yx4rKBKi4%2BbwSPPztD3iAESrBqWqRnh8J0UTGF4siJHcLulgVAp3v%2BjL89e67%2BuqYxi7O623fsK1uKOX7j6tq8iRDUvO590yxefGwlrHVcgAOiKhYluDe8mEI6TmWPwu891WxTYwAJ4qnScRMaTAdFw6uONk3CqtnBN6qY1gey7MPrU7ckGOqUBrywrLNNGFjGVAIV%2Bc98dhbgJkd6U3caljrqVu667PpOsrl7IpQizRgw1GHVvEDcDmnSPoa8yy%2BpfqwMEP8BS%2Fbd1mBNjyCociwZJIwKNNFnXlLU%2B0X1A2zL0QgQZCeo5YFDFiS3M2IDy1OqcXlK1dQlkEZh0HVpCuBw1NKB01mdM20LpvMcS6vnuW%2BHNe1PDhPo8gUcVlXH%2BoYR5Dma%2B6GhtiDN%2F&X-Amz-Signature=5a5594cf74943b898d3b39f0732178472d4021a62acda0863a087b2431520b47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROA6CZVW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCEblmbVQZqbTvD8K2hMOqZDPQkRn6Cnwep2XNUCnD1kAIgMxEW8x%2FI6nvdA3I9eOGEEjPtHdc4D74u8F3c%2F8yoWggqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISZGczsOSE9RUzWTSrcA5c5MHj41tNOvoTqgDnYFa3GcAUfHpDeyTgRCYQvASAIeNIO9VBeJ85F1%2Bet9VqwUSmqW9R5JEWD2MCDWXJUPqNtWkREQ4%2BDRZ8sE8LjovUfxzu%2BaC7%2F3tVBInPaX%2BEUd2D02KDvN78C4XuKVULvabxOtm0DHU%2FCx5X8UtHIjBPxrvSF2Xcm8ahD31kL0wFDIgXRhaf4%2BQPdEe317FFZ6mZUh%2BlPbSzf96YjtxFmCJ8LTISe33ej5zL8zwLGKB1YJpnS3id4m%2BOqk%2FFQYdfYJYIBMtNuBMc3ZKyr5Rt%2B%2F6O4D7rpXpi0UDasr3NgdszqjVAFjX%2BNVMfskqeKeIi3hPmft4si8K8%2Ftrziac10sCk%2F2GsxF1AXVZEXWoqkA9DktC3q0ziqjNxkkLzRkj%2F%2B8qVARC3MfMOzAozSO3LqdRmKA7n%2BfWa4tL5bOATNP4npUS8FqbEvvtM7YeYF2yx4rKBKi4%2BbwSPPztD3iAESrBqWqRnh8J0UTGF4siJHcLulgVAp3v%2BjL89e67%2BuqYxi7O623fsK1uKOX7j6tq8iRDUvO590yxefGwlrHVcgAOiKhYluDe8mEI6TmWPwu891WxTYwAJ4qnScRMaTAdFw6uONk3CqtnBN6qY1gey7MPrU7ckGOqUBrywrLNNGFjGVAIV%2Bc98dhbgJkd6U3caljrqVu667PpOsrl7IpQizRgw1GHVvEDcDmnSPoa8yy%2BpfqwMEP8BS%2Fbd1mBNjyCociwZJIwKNNFnXlLU%2B0X1A2zL0QgQZCeo5YFDFiS3M2IDy1OqcXlK1dQlkEZh0HVpCuBw1NKB01mdM20LpvMcS6vnuW%2BHNe1PDhPo8gUcVlXH%2BoYR5Dma%2B6GhtiDN%2F&X-Amz-Signature=f86cb96cd118501102c6e23f9d0fcd177a0c9b0070a2d7544d5526bbae523709&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROA6CZVW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCEblmbVQZqbTvD8K2hMOqZDPQkRn6Cnwep2XNUCnD1kAIgMxEW8x%2FI6nvdA3I9eOGEEjPtHdc4D74u8F3c%2F8yoWggqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISZGczsOSE9RUzWTSrcA5c5MHj41tNOvoTqgDnYFa3GcAUfHpDeyTgRCYQvASAIeNIO9VBeJ85F1%2Bet9VqwUSmqW9R5JEWD2MCDWXJUPqNtWkREQ4%2BDRZ8sE8LjovUfxzu%2BaC7%2F3tVBInPaX%2BEUd2D02KDvN78C4XuKVULvabxOtm0DHU%2FCx5X8UtHIjBPxrvSF2Xcm8ahD31kL0wFDIgXRhaf4%2BQPdEe317FFZ6mZUh%2BlPbSzf96YjtxFmCJ8LTISe33ej5zL8zwLGKB1YJpnS3id4m%2BOqk%2FFQYdfYJYIBMtNuBMc3ZKyr5Rt%2B%2F6O4D7rpXpi0UDasr3NgdszqjVAFjX%2BNVMfskqeKeIi3hPmft4si8K8%2Ftrziac10sCk%2F2GsxF1AXVZEXWoqkA9DktC3q0ziqjNxkkLzRkj%2F%2B8qVARC3MfMOzAozSO3LqdRmKA7n%2BfWa4tL5bOATNP4npUS8FqbEvvtM7YeYF2yx4rKBKi4%2BbwSPPztD3iAESrBqWqRnh8J0UTGF4siJHcLulgVAp3v%2BjL89e67%2BuqYxi7O623fsK1uKOX7j6tq8iRDUvO590yxefGwlrHVcgAOiKhYluDe8mEI6TmWPwu891WxTYwAJ4qnScRMaTAdFw6uONk3CqtnBN6qY1gey7MPrU7ckGOqUBrywrLNNGFjGVAIV%2Bc98dhbgJkd6U3caljrqVu667PpOsrl7IpQizRgw1GHVvEDcDmnSPoa8yy%2BpfqwMEP8BS%2Fbd1mBNjyCociwZJIwKNNFnXlLU%2B0X1A2zL0QgQZCeo5YFDFiS3M2IDy1OqcXlK1dQlkEZh0HVpCuBw1NKB01mdM20LpvMcS6vnuW%2BHNe1PDhPo8gUcVlXH%2BoYR5Dma%2B6GhtiDN%2F&X-Amz-Signature=23bd87f95f2176fb60564d75385c7e93aa87c069ccc414f15f07e2eec696c86a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROA6CZVW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCEblmbVQZqbTvD8K2hMOqZDPQkRn6Cnwep2XNUCnD1kAIgMxEW8x%2FI6nvdA3I9eOGEEjPtHdc4D74u8F3c%2F8yoWggqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISZGczsOSE9RUzWTSrcA5c5MHj41tNOvoTqgDnYFa3GcAUfHpDeyTgRCYQvASAIeNIO9VBeJ85F1%2Bet9VqwUSmqW9R5JEWD2MCDWXJUPqNtWkREQ4%2BDRZ8sE8LjovUfxzu%2BaC7%2F3tVBInPaX%2BEUd2D02KDvN78C4XuKVULvabxOtm0DHU%2FCx5X8UtHIjBPxrvSF2Xcm8ahD31kL0wFDIgXRhaf4%2BQPdEe317FFZ6mZUh%2BlPbSzf96YjtxFmCJ8LTISe33ej5zL8zwLGKB1YJpnS3id4m%2BOqk%2FFQYdfYJYIBMtNuBMc3ZKyr5Rt%2B%2F6O4D7rpXpi0UDasr3NgdszqjVAFjX%2BNVMfskqeKeIi3hPmft4si8K8%2Ftrziac10sCk%2F2GsxF1AXVZEXWoqkA9DktC3q0ziqjNxkkLzRkj%2F%2B8qVARC3MfMOzAozSO3LqdRmKA7n%2BfWa4tL5bOATNP4npUS8FqbEvvtM7YeYF2yx4rKBKi4%2BbwSPPztD3iAESrBqWqRnh8J0UTGF4siJHcLulgVAp3v%2BjL89e67%2BuqYxi7O623fsK1uKOX7j6tq8iRDUvO590yxefGwlrHVcgAOiKhYluDe8mEI6TmWPwu891WxTYwAJ4qnScRMaTAdFw6uONk3CqtnBN6qY1gey7MPrU7ckGOqUBrywrLNNGFjGVAIV%2Bc98dhbgJkd6U3caljrqVu667PpOsrl7IpQizRgw1GHVvEDcDmnSPoa8yy%2BpfqwMEP8BS%2Fbd1mBNjyCociwZJIwKNNFnXlLU%2B0X1A2zL0QgQZCeo5YFDFiS3M2IDy1OqcXlK1dQlkEZh0HVpCuBw1NKB01mdM20LpvMcS6vnuW%2BHNe1PDhPo8gUcVlXH%2BoYR5Dma%2B6GhtiDN%2F&X-Amz-Signature=47f1b5a636dd523b0d26f2f8e53da449f5c626ac70f8376b4ed3bc5c6b2a9eff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

