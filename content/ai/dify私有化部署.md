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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY6BHQFF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQR5zaUlGlBaHeB9PczEUF7kWMepb3QQVDftWi5p0QSwIhAPrm3uJAWEwR6KUiIjoxGJu6E7rzuL5%2F5tVd1WCNDgKbKv8DCH8QABoMNjM3NDIzMTgzODA1IgxzB0A95J%2FbivQiOTAq3AMaD2rZaxXAqaptvBXOrEKzmBHIh8K6DUAPmm0OyLbz84AVfb0QdnTg5ayW84ziVzwhTHC3VKm1WqKfngMslFucmNa6Pvh%2F0xBylgLdKFQONy4wNkkF4edpWWcRDtnffogdD9hYXEucXd7bH6iApMXVW7dqeLbn1gYGi0c%2FzE%2B6t6bmZGohBqvMm06uYnwqKP9JiUrFiJWsrjC5B1wXWHb%2Fwcuz4AMLjuPjZAkie06swKGJvGR36IkMIeC1%2F3WIyOqgwgvHCnSrB8Zb3cD8RvKniutJKQCb%2Bi%2BWuZYKjol%2FTeZvn4jZXnlbNI2Rkeng53V8vmlNKZ7TrdEbGIeJe%2FMo56aSBawjdzwqLySLa%2FtVEJHpSxnDVxG7BXb1M5ILLmjdhEYXpBC5S2HDseEA80Wjc375OF8XYLNvzsBI14%2FTAfm0BDFuqQpBRRH60EurBz8gMzu1NlIcARfL%2Fs8IGkuNjVUi%2FiPaLwAmYHsW2eRL3SeQyBnI4LAvsr2KHEyIjm4XmR1up5Jj5mbufv7UlT2u5MYeLQBWSMDkq3WcxqA9wOmmJiCSuQQS7RMYfT9z%2FL6imNLtZY9DIvYv3jj0n226H6g5Pb2iWTv2oRs2HZYNg%2FwEyPLZdVJsvr6AZzDlrL3OBjqkAS2Wto%2FRgyefXJjl8pdxQcOiSChLEV3bXuqyx%2BfY8bQ%2FWVhjIe9yUFEqg0Br6%2FPW4kd2yyxDfYWS9VPaEZ6YPtzd3Txp9BpRFO04EC2lt61NrYz%2Bl%2FVAZ1aF0uyeAyBJBYala08yuWE1QX1gyFw8XyVmjTAd5Ul5xUvdoLSmBN9YSYglGGJWDgS75aSH%2FptSttrDQh0AmULvXjZQYehpF%2BDeoHPi&X-Amz-Signature=1dc61e5671ca132ac3d78a0a37441b1700a4663ba290434b49473ca3f729e5eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY6BHQFF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQR5zaUlGlBaHeB9PczEUF7kWMepb3QQVDftWi5p0QSwIhAPrm3uJAWEwR6KUiIjoxGJu6E7rzuL5%2F5tVd1WCNDgKbKv8DCH8QABoMNjM3NDIzMTgzODA1IgxzB0A95J%2FbivQiOTAq3AMaD2rZaxXAqaptvBXOrEKzmBHIh8K6DUAPmm0OyLbz84AVfb0QdnTg5ayW84ziVzwhTHC3VKm1WqKfngMslFucmNa6Pvh%2F0xBylgLdKFQONy4wNkkF4edpWWcRDtnffogdD9hYXEucXd7bH6iApMXVW7dqeLbn1gYGi0c%2FzE%2B6t6bmZGohBqvMm06uYnwqKP9JiUrFiJWsrjC5B1wXWHb%2Fwcuz4AMLjuPjZAkie06swKGJvGR36IkMIeC1%2F3WIyOqgwgvHCnSrB8Zb3cD8RvKniutJKQCb%2Bi%2BWuZYKjol%2FTeZvn4jZXnlbNI2Rkeng53V8vmlNKZ7TrdEbGIeJe%2FMo56aSBawjdzwqLySLa%2FtVEJHpSxnDVxG7BXb1M5ILLmjdhEYXpBC5S2HDseEA80Wjc375OF8XYLNvzsBI14%2FTAfm0BDFuqQpBRRH60EurBz8gMzu1NlIcARfL%2Fs8IGkuNjVUi%2FiPaLwAmYHsW2eRL3SeQyBnI4LAvsr2KHEyIjm4XmR1up5Jj5mbufv7UlT2u5MYeLQBWSMDkq3WcxqA9wOmmJiCSuQQS7RMYfT9z%2FL6imNLtZY9DIvYv3jj0n226H6g5Pb2iWTv2oRs2HZYNg%2FwEyPLZdVJsvr6AZzDlrL3OBjqkAS2Wto%2FRgyefXJjl8pdxQcOiSChLEV3bXuqyx%2BfY8bQ%2FWVhjIe9yUFEqg0Br6%2FPW4kd2yyxDfYWS9VPaEZ6YPtzd3Txp9BpRFO04EC2lt61NrYz%2Bl%2FVAZ1aF0uyeAyBJBYala08yuWE1QX1gyFw8XyVmjTAd5Ul5xUvdoLSmBN9YSYglGGJWDgS75aSH%2FptSttrDQh0AmULvXjZQYehpF%2BDeoHPi&X-Amz-Signature=f1da9ce2fefd951f27c385f608c0bdbc052677ef76cf51cb6ca5a1c3951ecc08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY6BHQFF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQR5zaUlGlBaHeB9PczEUF7kWMepb3QQVDftWi5p0QSwIhAPrm3uJAWEwR6KUiIjoxGJu6E7rzuL5%2F5tVd1WCNDgKbKv8DCH8QABoMNjM3NDIzMTgzODA1IgxzB0A95J%2FbivQiOTAq3AMaD2rZaxXAqaptvBXOrEKzmBHIh8K6DUAPmm0OyLbz84AVfb0QdnTg5ayW84ziVzwhTHC3VKm1WqKfngMslFucmNa6Pvh%2F0xBylgLdKFQONy4wNkkF4edpWWcRDtnffogdD9hYXEucXd7bH6iApMXVW7dqeLbn1gYGi0c%2FzE%2B6t6bmZGohBqvMm06uYnwqKP9JiUrFiJWsrjC5B1wXWHb%2Fwcuz4AMLjuPjZAkie06swKGJvGR36IkMIeC1%2F3WIyOqgwgvHCnSrB8Zb3cD8RvKniutJKQCb%2Bi%2BWuZYKjol%2FTeZvn4jZXnlbNI2Rkeng53V8vmlNKZ7TrdEbGIeJe%2FMo56aSBawjdzwqLySLa%2FtVEJHpSxnDVxG7BXb1M5ILLmjdhEYXpBC5S2HDseEA80Wjc375OF8XYLNvzsBI14%2FTAfm0BDFuqQpBRRH60EurBz8gMzu1NlIcARfL%2Fs8IGkuNjVUi%2FiPaLwAmYHsW2eRL3SeQyBnI4LAvsr2KHEyIjm4XmR1up5Jj5mbufv7UlT2u5MYeLQBWSMDkq3WcxqA9wOmmJiCSuQQS7RMYfT9z%2FL6imNLtZY9DIvYv3jj0n226H6g5Pb2iWTv2oRs2HZYNg%2FwEyPLZdVJsvr6AZzDlrL3OBjqkAS2Wto%2FRgyefXJjl8pdxQcOiSChLEV3bXuqyx%2BfY8bQ%2FWVhjIe9yUFEqg0Br6%2FPW4kd2yyxDfYWS9VPaEZ6YPtzd3Txp9BpRFO04EC2lt61NrYz%2Bl%2FVAZ1aF0uyeAyBJBYala08yuWE1QX1gyFw8XyVmjTAd5Ul5xUvdoLSmBN9YSYglGGJWDgS75aSH%2FptSttrDQh0AmULvXjZQYehpF%2BDeoHPi&X-Amz-Signature=d22a53afd03b8ac2c308c69e279f8c7c6fd10de840ca0db20e2566964f51332b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY6BHQFF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQR5zaUlGlBaHeB9PczEUF7kWMepb3QQVDftWi5p0QSwIhAPrm3uJAWEwR6KUiIjoxGJu6E7rzuL5%2F5tVd1WCNDgKbKv8DCH8QABoMNjM3NDIzMTgzODA1IgxzB0A95J%2FbivQiOTAq3AMaD2rZaxXAqaptvBXOrEKzmBHIh8K6DUAPmm0OyLbz84AVfb0QdnTg5ayW84ziVzwhTHC3VKm1WqKfngMslFucmNa6Pvh%2F0xBylgLdKFQONy4wNkkF4edpWWcRDtnffogdD9hYXEucXd7bH6iApMXVW7dqeLbn1gYGi0c%2FzE%2B6t6bmZGohBqvMm06uYnwqKP9JiUrFiJWsrjC5B1wXWHb%2Fwcuz4AMLjuPjZAkie06swKGJvGR36IkMIeC1%2F3WIyOqgwgvHCnSrB8Zb3cD8RvKniutJKQCb%2Bi%2BWuZYKjol%2FTeZvn4jZXnlbNI2Rkeng53V8vmlNKZ7TrdEbGIeJe%2FMo56aSBawjdzwqLySLa%2FtVEJHpSxnDVxG7BXb1M5ILLmjdhEYXpBC5S2HDseEA80Wjc375OF8XYLNvzsBI14%2FTAfm0BDFuqQpBRRH60EurBz8gMzu1NlIcARfL%2Fs8IGkuNjVUi%2FiPaLwAmYHsW2eRL3SeQyBnI4LAvsr2KHEyIjm4XmR1up5Jj5mbufv7UlT2u5MYeLQBWSMDkq3WcxqA9wOmmJiCSuQQS7RMYfT9z%2FL6imNLtZY9DIvYv3jj0n226H6g5Pb2iWTv2oRs2HZYNg%2FwEyPLZdVJsvr6AZzDlrL3OBjqkAS2Wto%2FRgyefXJjl8pdxQcOiSChLEV3bXuqyx%2BfY8bQ%2FWVhjIe9yUFEqg0Br6%2FPW4kd2yyxDfYWS9VPaEZ6YPtzd3Txp9BpRFO04EC2lt61NrYz%2Bl%2FVAZ1aF0uyeAyBJBYala08yuWE1QX1gyFw8XyVmjTAd5Ul5xUvdoLSmBN9YSYglGGJWDgS75aSH%2FptSttrDQh0AmULvXjZQYehpF%2BDeoHPi&X-Amz-Signature=901b74efc75bce1f415d7371ddb971fb7d3af6fe4883142a3b09c56367244ac3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY6BHQFF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQR5zaUlGlBaHeB9PczEUF7kWMepb3QQVDftWi5p0QSwIhAPrm3uJAWEwR6KUiIjoxGJu6E7rzuL5%2F5tVd1WCNDgKbKv8DCH8QABoMNjM3NDIzMTgzODA1IgxzB0A95J%2FbivQiOTAq3AMaD2rZaxXAqaptvBXOrEKzmBHIh8K6DUAPmm0OyLbz84AVfb0QdnTg5ayW84ziVzwhTHC3VKm1WqKfngMslFucmNa6Pvh%2F0xBylgLdKFQONy4wNkkF4edpWWcRDtnffogdD9hYXEucXd7bH6iApMXVW7dqeLbn1gYGi0c%2FzE%2B6t6bmZGohBqvMm06uYnwqKP9JiUrFiJWsrjC5B1wXWHb%2Fwcuz4AMLjuPjZAkie06swKGJvGR36IkMIeC1%2F3WIyOqgwgvHCnSrB8Zb3cD8RvKniutJKQCb%2Bi%2BWuZYKjol%2FTeZvn4jZXnlbNI2Rkeng53V8vmlNKZ7TrdEbGIeJe%2FMo56aSBawjdzwqLySLa%2FtVEJHpSxnDVxG7BXb1M5ILLmjdhEYXpBC5S2HDseEA80Wjc375OF8XYLNvzsBI14%2FTAfm0BDFuqQpBRRH60EurBz8gMzu1NlIcARfL%2Fs8IGkuNjVUi%2FiPaLwAmYHsW2eRL3SeQyBnI4LAvsr2KHEyIjm4XmR1up5Jj5mbufv7UlT2u5MYeLQBWSMDkq3WcxqA9wOmmJiCSuQQS7RMYfT9z%2FL6imNLtZY9DIvYv3jj0n226H6g5Pb2iWTv2oRs2HZYNg%2FwEyPLZdVJsvr6AZzDlrL3OBjqkAS2Wto%2FRgyefXJjl8pdxQcOiSChLEV3bXuqyx%2BfY8bQ%2FWVhjIe9yUFEqg0Br6%2FPW4kd2yyxDfYWS9VPaEZ6YPtzd3Txp9BpRFO04EC2lt61NrYz%2Bl%2FVAZ1aF0uyeAyBJBYala08yuWE1QX1gyFw8XyVmjTAd5Ul5xUvdoLSmBN9YSYglGGJWDgS75aSH%2FptSttrDQh0AmULvXjZQYehpF%2BDeoHPi&X-Amz-Signature=742e6de3c15af43bae4bd4705ae78b81a96c81a54e87b1f0f8c5cfdf88d5b2ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY6BHQFF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQR5zaUlGlBaHeB9PczEUF7kWMepb3QQVDftWi5p0QSwIhAPrm3uJAWEwR6KUiIjoxGJu6E7rzuL5%2F5tVd1WCNDgKbKv8DCH8QABoMNjM3NDIzMTgzODA1IgxzB0A95J%2FbivQiOTAq3AMaD2rZaxXAqaptvBXOrEKzmBHIh8K6DUAPmm0OyLbz84AVfb0QdnTg5ayW84ziVzwhTHC3VKm1WqKfngMslFucmNa6Pvh%2F0xBylgLdKFQONy4wNkkF4edpWWcRDtnffogdD9hYXEucXd7bH6iApMXVW7dqeLbn1gYGi0c%2FzE%2B6t6bmZGohBqvMm06uYnwqKP9JiUrFiJWsrjC5B1wXWHb%2Fwcuz4AMLjuPjZAkie06swKGJvGR36IkMIeC1%2F3WIyOqgwgvHCnSrB8Zb3cD8RvKniutJKQCb%2Bi%2BWuZYKjol%2FTeZvn4jZXnlbNI2Rkeng53V8vmlNKZ7TrdEbGIeJe%2FMo56aSBawjdzwqLySLa%2FtVEJHpSxnDVxG7BXb1M5ILLmjdhEYXpBC5S2HDseEA80Wjc375OF8XYLNvzsBI14%2FTAfm0BDFuqQpBRRH60EurBz8gMzu1NlIcARfL%2Fs8IGkuNjVUi%2FiPaLwAmYHsW2eRL3SeQyBnI4LAvsr2KHEyIjm4XmR1up5Jj5mbufv7UlT2u5MYeLQBWSMDkq3WcxqA9wOmmJiCSuQQS7RMYfT9z%2FL6imNLtZY9DIvYv3jj0n226H6g5Pb2iWTv2oRs2HZYNg%2FwEyPLZdVJsvr6AZzDlrL3OBjqkAS2Wto%2FRgyefXJjl8pdxQcOiSChLEV3bXuqyx%2BfY8bQ%2FWVhjIe9yUFEqg0Br6%2FPW4kd2yyxDfYWS9VPaEZ6YPtzd3Txp9BpRFO04EC2lt61NrYz%2Bl%2FVAZ1aF0uyeAyBJBYala08yuWE1QX1gyFw8XyVmjTAd5Ul5xUvdoLSmBN9YSYglGGJWDgS75aSH%2FptSttrDQh0AmULvXjZQYehpF%2BDeoHPi&X-Amz-Signature=c7b8c82c4e680e3e0afa101ef2ca0b70bdccc37e53a3314228a7ee3876bda3ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY6BHQFF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQR5zaUlGlBaHeB9PczEUF7kWMepb3QQVDftWi5p0QSwIhAPrm3uJAWEwR6KUiIjoxGJu6E7rzuL5%2F5tVd1WCNDgKbKv8DCH8QABoMNjM3NDIzMTgzODA1IgxzB0A95J%2FbivQiOTAq3AMaD2rZaxXAqaptvBXOrEKzmBHIh8K6DUAPmm0OyLbz84AVfb0QdnTg5ayW84ziVzwhTHC3VKm1WqKfngMslFucmNa6Pvh%2F0xBylgLdKFQONy4wNkkF4edpWWcRDtnffogdD9hYXEucXd7bH6iApMXVW7dqeLbn1gYGi0c%2FzE%2B6t6bmZGohBqvMm06uYnwqKP9JiUrFiJWsrjC5B1wXWHb%2Fwcuz4AMLjuPjZAkie06swKGJvGR36IkMIeC1%2F3WIyOqgwgvHCnSrB8Zb3cD8RvKniutJKQCb%2Bi%2BWuZYKjol%2FTeZvn4jZXnlbNI2Rkeng53V8vmlNKZ7TrdEbGIeJe%2FMo56aSBawjdzwqLySLa%2FtVEJHpSxnDVxG7BXb1M5ILLmjdhEYXpBC5S2HDseEA80Wjc375OF8XYLNvzsBI14%2FTAfm0BDFuqQpBRRH60EurBz8gMzu1NlIcARfL%2Fs8IGkuNjVUi%2FiPaLwAmYHsW2eRL3SeQyBnI4LAvsr2KHEyIjm4XmR1up5Jj5mbufv7UlT2u5MYeLQBWSMDkq3WcxqA9wOmmJiCSuQQS7RMYfT9z%2FL6imNLtZY9DIvYv3jj0n226H6g5Pb2iWTv2oRs2HZYNg%2FwEyPLZdVJsvr6AZzDlrL3OBjqkAS2Wto%2FRgyefXJjl8pdxQcOiSChLEV3bXuqyx%2BfY8bQ%2FWVhjIe9yUFEqg0Br6%2FPW4kd2yyxDfYWS9VPaEZ6YPtzd3Txp9BpRFO04EC2lt61NrYz%2Bl%2FVAZ1aF0uyeAyBJBYala08yuWE1QX1gyFw8XyVmjTAd5Ul5xUvdoLSmBN9YSYglGGJWDgS75aSH%2FptSttrDQh0AmULvXjZQYehpF%2BDeoHPi&X-Amz-Signature=9f9dc63c08fce48a1a7a99f2b886fde3685d0b3cf25c8db4638f6dc4d188807a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY6BHQFF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQR5zaUlGlBaHeB9PczEUF7kWMepb3QQVDftWi5p0QSwIhAPrm3uJAWEwR6KUiIjoxGJu6E7rzuL5%2F5tVd1WCNDgKbKv8DCH8QABoMNjM3NDIzMTgzODA1IgxzB0A95J%2FbivQiOTAq3AMaD2rZaxXAqaptvBXOrEKzmBHIh8K6DUAPmm0OyLbz84AVfb0QdnTg5ayW84ziVzwhTHC3VKm1WqKfngMslFucmNa6Pvh%2F0xBylgLdKFQONy4wNkkF4edpWWcRDtnffogdD9hYXEucXd7bH6iApMXVW7dqeLbn1gYGi0c%2FzE%2B6t6bmZGohBqvMm06uYnwqKP9JiUrFiJWsrjC5B1wXWHb%2Fwcuz4AMLjuPjZAkie06swKGJvGR36IkMIeC1%2F3WIyOqgwgvHCnSrB8Zb3cD8RvKniutJKQCb%2Bi%2BWuZYKjol%2FTeZvn4jZXnlbNI2Rkeng53V8vmlNKZ7TrdEbGIeJe%2FMo56aSBawjdzwqLySLa%2FtVEJHpSxnDVxG7BXb1M5ILLmjdhEYXpBC5S2HDseEA80Wjc375OF8XYLNvzsBI14%2FTAfm0BDFuqQpBRRH60EurBz8gMzu1NlIcARfL%2Fs8IGkuNjVUi%2FiPaLwAmYHsW2eRL3SeQyBnI4LAvsr2KHEyIjm4XmR1up5Jj5mbufv7UlT2u5MYeLQBWSMDkq3WcxqA9wOmmJiCSuQQS7RMYfT9z%2FL6imNLtZY9DIvYv3jj0n226H6g5Pb2iWTv2oRs2HZYNg%2FwEyPLZdVJsvr6AZzDlrL3OBjqkAS2Wto%2FRgyefXJjl8pdxQcOiSChLEV3bXuqyx%2BfY8bQ%2FWVhjIe9yUFEqg0Br6%2FPW4kd2yyxDfYWS9VPaEZ6YPtzd3Txp9BpRFO04EC2lt61NrYz%2Bl%2FVAZ1aF0uyeAyBJBYala08yuWE1QX1gyFw8XyVmjTAd5Ul5xUvdoLSmBN9YSYglGGJWDgS75aSH%2FptSttrDQh0AmULvXjZQYehpF%2BDeoHPi&X-Amz-Signature=d6415047d9c29759490f3f163a1a6531199233cbac3ebe459ec5d019f5b675ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY6BHQFF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQR5zaUlGlBaHeB9PczEUF7kWMepb3QQVDftWi5p0QSwIhAPrm3uJAWEwR6KUiIjoxGJu6E7rzuL5%2F5tVd1WCNDgKbKv8DCH8QABoMNjM3NDIzMTgzODA1IgxzB0A95J%2FbivQiOTAq3AMaD2rZaxXAqaptvBXOrEKzmBHIh8K6DUAPmm0OyLbz84AVfb0QdnTg5ayW84ziVzwhTHC3VKm1WqKfngMslFucmNa6Pvh%2F0xBylgLdKFQONy4wNkkF4edpWWcRDtnffogdD9hYXEucXd7bH6iApMXVW7dqeLbn1gYGi0c%2FzE%2B6t6bmZGohBqvMm06uYnwqKP9JiUrFiJWsrjC5B1wXWHb%2Fwcuz4AMLjuPjZAkie06swKGJvGR36IkMIeC1%2F3WIyOqgwgvHCnSrB8Zb3cD8RvKniutJKQCb%2Bi%2BWuZYKjol%2FTeZvn4jZXnlbNI2Rkeng53V8vmlNKZ7TrdEbGIeJe%2FMo56aSBawjdzwqLySLa%2FtVEJHpSxnDVxG7BXb1M5ILLmjdhEYXpBC5S2HDseEA80Wjc375OF8XYLNvzsBI14%2FTAfm0BDFuqQpBRRH60EurBz8gMzu1NlIcARfL%2Fs8IGkuNjVUi%2FiPaLwAmYHsW2eRL3SeQyBnI4LAvsr2KHEyIjm4XmR1up5Jj5mbufv7UlT2u5MYeLQBWSMDkq3WcxqA9wOmmJiCSuQQS7RMYfT9z%2FL6imNLtZY9DIvYv3jj0n226H6g5Pb2iWTv2oRs2HZYNg%2FwEyPLZdVJsvr6AZzDlrL3OBjqkAS2Wto%2FRgyefXJjl8pdxQcOiSChLEV3bXuqyx%2BfY8bQ%2FWVhjIe9yUFEqg0Br6%2FPW4kd2yyxDfYWS9VPaEZ6YPtzd3Txp9BpRFO04EC2lt61NrYz%2Bl%2FVAZ1aF0uyeAyBJBYala08yuWE1QX1gyFw8XyVmjTAd5Ul5xUvdoLSmBN9YSYglGGJWDgS75aSH%2FptSttrDQh0AmULvXjZQYehpF%2BDeoHPi&X-Amz-Signature=afba0343707c1bd258b7ed8c6e0c92117eb15199f8fa16579eeb4ccb50a0a331&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY6BHQFF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQR5zaUlGlBaHeB9PczEUF7kWMepb3QQVDftWi5p0QSwIhAPrm3uJAWEwR6KUiIjoxGJu6E7rzuL5%2F5tVd1WCNDgKbKv8DCH8QABoMNjM3NDIzMTgzODA1IgxzB0A95J%2FbivQiOTAq3AMaD2rZaxXAqaptvBXOrEKzmBHIh8K6DUAPmm0OyLbz84AVfb0QdnTg5ayW84ziVzwhTHC3VKm1WqKfngMslFucmNa6Pvh%2F0xBylgLdKFQONy4wNkkF4edpWWcRDtnffogdD9hYXEucXd7bH6iApMXVW7dqeLbn1gYGi0c%2FzE%2B6t6bmZGohBqvMm06uYnwqKP9JiUrFiJWsrjC5B1wXWHb%2Fwcuz4AMLjuPjZAkie06swKGJvGR36IkMIeC1%2F3WIyOqgwgvHCnSrB8Zb3cD8RvKniutJKQCb%2Bi%2BWuZYKjol%2FTeZvn4jZXnlbNI2Rkeng53V8vmlNKZ7TrdEbGIeJe%2FMo56aSBawjdzwqLySLa%2FtVEJHpSxnDVxG7BXb1M5ILLmjdhEYXpBC5S2HDseEA80Wjc375OF8XYLNvzsBI14%2FTAfm0BDFuqQpBRRH60EurBz8gMzu1NlIcARfL%2Fs8IGkuNjVUi%2FiPaLwAmYHsW2eRL3SeQyBnI4LAvsr2KHEyIjm4XmR1up5Jj5mbufv7UlT2u5MYeLQBWSMDkq3WcxqA9wOmmJiCSuQQS7RMYfT9z%2FL6imNLtZY9DIvYv3jj0n226H6g5Pb2iWTv2oRs2HZYNg%2FwEyPLZdVJsvr6AZzDlrL3OBjqkAS2Wto%2FRgyefXJjl8pdxQcOiSChLEV3bXuqyx%2BfY8bQ%2FWVhjIe9yUFEqg0Br6%2FPW4kd2yyxDfYWS9VPaEZ6YPtzd3Txp9BpRFO04EC2lt61NrYz%2Bl%2FVAZ1aF0uyeAyBJBYala08yuWE1QX1gyFw8XyVmjTAd5Ul5xUvdoLSmBN9YSYglGGJWDgS75aSH%2FptSttrDQh0AmULvXjZQYehpF%2BDeoHPi&X-Amz-Signature=0d86619f9ac43187293d10422b01aa553fb6b532fda72f57bf049c5579105107&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

