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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753TDFEM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWRzzTsiaFh0y5cV3Q7JsGfLSwzRyQXYwGvlX67neu1AiAI1vOUNHQP0HcQNttKQVQp80%2BaXj252UaOZ6XRn2%2FyfyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8BjR0mdRyyVQXhNeKtwDLyYuD3iPRjFX%2BPIV%2Fu7Uv7mSmWeCo76VsY6N758JlFEoTGePPMNF4kFH4nO1CG95Tk1%2BeZ7fpdY6UQMmin5pkUSzPVNmn94KAfWEEym56nyH%2F6rT174q5cR4UWDdIq4bXLHjbB0NYz7VBcCa1MCKd%2BsOQ7%2BZ9PH%2B5kaLDvNJZTCvmLhmiVwQyz0kJmPlhn7423S2YC12KBw2UWcuREDziBXJRoUJunTuIIbW8wuPUatLkUmVoUeA8amv7ayiMHuVBMajAX0kLiu5Agtt4wfNQggXJVvwJhQxfH1DwZk6EDLHfVDfN9j5oLaqED%2F7l7s0GWinfwxcBDs9PYtfOF4yf5pwgwv3O3CrMgPO%2BkFsDLA2M2hhQD2hX2lkAptZHd6O6siWuflS%2B5Ne5rG3z9HubKh33aDSNFddnUaqKMVQKGs3dVxrosFIkM0Hp3E5t221kdf9hTBZP9s95Tsq3cD0MFsEifC41FHBBgj1XFjTpFBfKpatwaEtvS35oYGtiOYnZA5tLxHCTjLonDvREg6FhB%2FEtnluwwc2V3BCQQVJztnx7vpDGJAePY1XEWlJtVBCRd4Dtgv2pQFHGn5Nu26Lzz38qozw2AtyBJnNgzw%2FS9xUUxjAWmQ9Jq5s62Ew1KWNzgY6pgEmNSjBj8C3MWrYuJJlosAYF6DDmckUPRo2iXUVjEmClYDOQ0o24CI95BISH4yEPNlhITf2dk86SmlB0suEesNpL5%2FQuT%2F2xpYH8EUQcrtlaWs3Dm1xrO57MlBV%2FmUMJlvfv9EecZrqpzpF8U3l9KNBJVE4pKgYXo49aGKLj2qXCPVLg6dT44kOa1lUDm7cLUFYUFI75eZvOQuyu3%2FcQBloyz54Olo8&X-Amz-Signature=e8ace12013a59630ab3759f6f8131572583fcd40492fc8b5844bb400abbac531&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753TDFEM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWRzzTsiaFh0y5cV3Q7JsGfLSwzRyQXYwGvlX67neu1AiAI1vOUNHQP0HcQNttKQVQp80%2BaXj252UaOZ6XRn2%2FyfyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8BjR0mdRyyVQXhNeKtwDLyYuD3iPRjFX%2BPIV%2Fu7Uv7mSmWeCo76VsY6N758JlFEoTGePPMNF4kFH4nO1CG95Tk1%2BeZ7fpdY6UQMmin5pkUSzPVNmn94KAfWEEym56nyH%2F6rT174q5cR4UWDdIq4bXLHjbB0NYz7VBcCa1MCKd%2BsOQ7%2BZ9PH%2B5kaLDvNJZTCvmLhmiVwQyz0kJmPlhn7423S2YC12KBw2UWcuREDziBXJRoUJunTuIIbW8wuPUatLkUmVoUeA8amv7ayiMHuVBMajAX0kLiu5Agtt4wfNQggXJVvwJhQxfH1DwZk6EDLHfVDfN9j5oLaqED%2F7l7s0GWinfwxcBDs9PYtfOF4yf5pwgwv3O3CrMgPO%2BkFsDLA2M2hhQD2hX2lkAptZHd6O6siWuflS%2B5Ne5rG3z9HubKh33aDSNFddnUaqKMVQKGs3dVxrosFIkM0Hp3E5t221kdf9hTBZP9s95Tsq3cD0MFsEifC41FHBBgj1XFjTpFBfKpatwaEtvS35oYGtiOYnZA5tLxHCTjLonDvREg6FhB%2FEtnluwwc2V3BCQQVJztnx7vpDGJAePY1XEWlJtVBCRd4Dtgv2pQFHGn5Nu26Lzz38qozw2AtyBJnNgzw%2FS9xUUxjAWmQ9Jq5s62Ew1KWNzgY6pgEmNSjBj8C3MWrYuJJlosAYF6DDmckUPRo2iXUVjEmClYDOQ0o24CI95BISH4yEPNlhITf2dk86SmlB0suEesNpL5%2FQuT%2F2xpYH8EUQcrtlaWs3Dm1xrO57MlBV%2FmUMJlvfv9EecZrqpzpF8U3l9KNBJVE4pKgYXo49aGKLj2qXCPVLg6dT44kOa1lUDm7cLUFYUFI75eZvOQuyu3%2FcQBloyz54Olo8&X-Amz-Signature=5cf689f71adeb9ffd52e43e58d308cc31aabf82ba8570501ec0db907b46f42c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753TDFEM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWRzzTsiaFh0y5cV3Q7JsGfLSwzRyQXYwGvlX67neu1AiAI1vOUNHQP0HcQNttKQVQp80%2BaXj252UaOZ6XRn2%2FyfyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8BjR0mdRyyVQXhNeKtwDLyYuD3iPRjFX%2BPIV%2Fu7Uv7mSmWeCo76VsY6N758JlFEoTGePPMNF4kFH4nO1CG95Tk1%2BeZ7fpdY6UQMmin5pkUSzPVNmn94KAfWEEym56nyH%2F6rT174q5cR4UWDdIq4bXLHjbB0NYz7VBcCa1MCKd%2BsOQ7%2BZ9PH%2B5kaLDvNJZTCvmLhmiVwQyz0kJmPlhn7423S2YC12KBw2UWcuREDziBXJRoUJunTuIIbW8wuPUatLkUmVoUeA8amv7ayiMHuVBMajAX0kLiu5Agtt4wfNQggXJVvwJhQxfH1DwZk6EDLHfVDfN9j5oLaqED%2F7l7s0GWinfwxcBDs9PYtfOF4yf5pwgwv3O3CrMgPO%2BkFsDLA2M2hhQD2hX2lkAptZHd6O6siWuflS%2B5Ne5rG3z9HubKh33aDSNFddnUaqKMVQKGs3dVxrosFIkM0Hp3E5t221kdf9hTBZP9s95Tsq3cD0MFsEifC41FHBBgj1XFjTpFBfKpatwaEtvS35oYGtiOYnZA5tLxHCTjLonDvREg6FhB%2FEtnluwwc2V3BCQQVJztnx7vpDGJAePY1XEWlJtVBCRd4Dtgv2pQFHGn5Nu26Lzz38qozw2AtyBJnNgzw%2FS9xUUxjAWmQ9Jq5s62Ew1KWNzgY6pgEmNSjBj8C3MWrYuJJlosAYF6DDmckUPRo2iXUVjEmClYDOQ0o24CI95BISH4yEPNlhITf2dk86SmlB0suEesNpL5%2FQuT%2F2xpYH8EUQcrtlaWs3Dm1xrO57MlBV%2FmUMJlvfv9EecZrqpzpF8U3l9KNBJVE4pKgYXo49aGKLj2qXCPVLg6dT44kOa1lUDm7cLUFYUFI75eZvOQuyu3%2FcQBloyz54Olo8&X-Amz-Signature=c956ee888e10bfbb847e63c73c15347df2bdc61182e20a2f913e3dc63f788e03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753TDFEM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWRzzTsiaFh0y5cV3Q7JsGfLSwzRyQXYwGvlX67neu1AiAI1vOUNHQP0HcQNttKQVQp80%2BaXj252UaOZ6XRn2%2FyfyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8BjR0mdRyyVQXhNeKtwDLyYuD3iPRjFX%2BPIV%2Fu7Uv7mSmWeCo76VsY6N758JlFEoTGePPMNF4kFH4nO1CG95Tk1%2BeZ7fpdY6UQMmin5pkUSzPVNmn94KAfWEEym56nyH%2F6rT174q5cR4UWDdIq4bXLHjbB0NYz7VBcCa1MCKd%2BsOQ7%2BZ9PH%2B5kaLDvNJZTCvmLhmiVwQyz0kJmPlhn7423S2YC12KBw2UWcuREDziBXJRoUJunTuIIbW8wuPUatLkUmVoUeA8amv7ayiMHuVBMajAX0kLiu5Agtt4wfNQggXJVvwJhQxfH1DwZk6EDLHfVDfN9j5oLaqED%2F7l7s0GWinfwxcBDs9PYtfOF4yf5pwgwv3O3CrMgPO%2BkFsDLA2M2hhQD2hX2lkAptZHd6O6siWuflS%2B5Ne5rG3z9HubKh33aDSNFddnUaqKMVQKGs3dVxrosFIkM0Hp3E5t221kdf9hTBZP9s95Tsq3cD0MFsEifC41FHBBgj1XFjTpFBfKpatwaEtvS35oYGtiOYnZA5tLxHCTjLonDvREg6FhB%2FEtnluwwc2V3BCQQVJztnx7vpDGJAePY1XEWlJtVBCRd4Dtgv2pQFHGn5Nu26Lzz38qozw2AtyBJnNgzw%2FS9xUUxjAWmQ9Jq5s62Ew1KWNzgY6pgEmNSjBj8C3MWrYuJJlosAYF6DDmckUPRo2iXUVjEmClYDOQ0o24CI95BISH4yEPNlhITf2dk86SmlB0suEesNpL5%2FQuT%2F2xpYH8EUQcrtlaWs3Dm1xrO57MlBV%2FmUMJlvfv9EecZrqpzpF8U3l9KNBJVE4pKgYXo49aGKLj2qXCPVLg6dT44kOa1lUDm7cLUFYUFI75eZvOQuyu3%2FcQBloyz54Olo8&X-Amz-Signature=c643dc08992ae34be86a5b50f6e5222f1347f428c58b534e06cca21aa86cf7d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753TDFEM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWRzzTsiaFh0y5cV3Q7JsGfLSwzRyQXYwGvlX67neu1AiAI1vOUNHQP0HcQNttKQVQp80%2BaXj252UaOZ6XRn2%2FyfyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8BjR0mdRyyVQXhNeKtwDLyYuD3iPRjFX%2BPIV%2Fu7Uv7mSmWeCo76VsY6N758JlFEoTGePPMNF4kFH4nO1CG95Tk1%2BeZ7fpdY6UQMmin5pkUSzPVNmn94KAfWEEym56nyH%2F6rT174q5cR4UWDdIq4bXLHjbB0NYz7VBcCa1MCKd%2BsOQ7%2BZ9PH%2B5kaLDvNJZTCvmLhmiVwQyz0kJmPlhn7423S2YC12KBw2UWcuREDziBXJRoUJunTuIIbW8wuPUatLkUmVoUeA8amv7ayiMHuVBMajAX0kLiu5Agtt4wfNQggXJVvwJhQxfH1DwZk6EDLHfVDfN9j5oLaqED%2F7l7s0GWinfwxcBDs9PYtfOF4yf5pwgwv3O3CrMgPO%2BkFsDLA2M2hhQD2hX2lkAptZHd6O6siWuflS%2B5Ne5rG3z9HubKh33aDSNFddnUaqKMVQKGs3dVxrosFIkM0Hp3E5t221kdf9hTBZP9s95Tsq3cD0MFsEifC41FHBBgj1XFjTpFBfKpatwaEtvS35oYGtiOYnZA5tLxHCTjLonDvREg6FhB%2FEtnluwwc2V3BCQQVJztnx7vpDGJAePY1XEWlJtVBCRd4Dtgv2pQFHGn5Nu26Lzz38qozw2AtyBJnNgzw%2FS9xUUxjAWmQ9Jq5s62Ew1KWNzgY6pgEmNSjBj8C3MWrYuJJlosAYF6DDmckUPRo2iXUVjEmClYDOQ0o24CI95BISH4yEPNlhITf2dk86SmlB0suEesNpL5%2FQuT%2F2xpYH8EUQcrtlaWs3Dm1xrO57MlBV%2FmUMJlvfv9EecZrqpzpF8U3l9KNBJVE4pKgYXo49aGKLj2qXCPVLg6dT44kOa1lUDm7cLUFYUFI75eZvOQuyu3%2FcQBloyz54Olo8&X-Amz-Signature=0c8423725361407a394e570989f19a4b2f256c2daad9e04ab7646214f7436584&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753TDFEM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWRzzTsiaFh0y5cV3Q7JsGfLSwzRyQXYwGvlX67neu1AiAI1vOUNHQP0HcQNttKQVQp80%2BaXj252UaOZ6XRn2%2FyfyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8BjR0mdRyyVQXhNeKtwDLyYuD3iPRjFX%2BPIV%2Fu7Uv7mSmWeCo76VsY6N758JlFEoTGePPMNF4kFH4nO1CG95Tk1%2BeZ7fpdY6UQMmin5pkUSzPVNmn94KAfWEEym56nyH%2F6rT174q5cR4UWDdIq4bXLHjbB0NYz7VBcCa1MCKd%2BsOQ7%2BZ9PH%2B5kaLDvNJZTCvmLhmiVwQyz0kJmPlhn7423S2YC12KBw2UWcuREDziBXJRoUJunTuIIbW8wuPUatLkUmVoUeA8amv7ayiMHuVBMajAX0kLiu5Agtt4wfNQggXJVvwJhQxfH1DwZk6EDLHfVDfN9j5oLaqED%2F7l7s0GWinfwxcBDs9PYtfOF4yf5pwgwv3O3CrMgPO%2BkFsDLA2M2hhQD2hX2lkAptZHd6O6siWuflS%2B5Ne5rG3z9HubKh33aDSNFddnUaqKMVQKGs3dVxrosFIkM0Hp3E5t221kdf9hTBZP9s95Tsq3cD0MFsEifC41FHBBgj1XFjTpFBfKpatwaEtvS35oYGtiOYnZA5tLxHCTjLonDvREg6FhB%2FEtnluwwc2V3BCQQVJztnx7vpDGJAePY1XEWlJtVBCRd4Dtgv2pQFHGn5Nu26Lzz38qozw2AtyBJnNgzw%2FS9xUUxjAWmQ9Jq5s62Ew1KWNzgY6pgEmNSjBj8C3MWrYuJJlosAYF6DDmckUPRo2iXUVjEmClYDOQ0o24CI95BISH4yEPNlhITf2dk86SmlB0suEesNpL5%2FQuT%2F2xpYH8EUQcrtlaWs3Dm1xrO57MlBV%2FmUMJlvfv9EecZrqpzpF8U3l9KNBJVE4pKgYXo49aGKLj2qXCPVLg6dT44kOa1lUDm7cLUFYUFI75eZvOQuyu3%2FcQBloyz54Olo8&X-Amz-Signature=85ec28ef039f91dfa5e1c1c9785ce833ba74b375a3e76b9819841bc8bcb7f85c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753TDFEM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWRzzTsiaFh0y5cV3Q7JsGfLSwzRyQXYwGvlX67neu1AiAI1vOUNHQP0HcQNttKQVQp80%2BaXj252UaOZ6XRn2%2FyfyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8BjR0mdRyyVQXhNeKtwDLyYuD3iPRjFX%2BPIV%2Fu7Uv7mSmWeCo76VsY6N758JlFEoTGePPMNF4kFH4nO1CG95Tk1%2BeZ7fpdY6UQMmin5pkUSzPVNmn94KAfWEEym56nyH%2F6rT174q5cR4UWDdIq4bXLHjbB0NYz7VBcCa1MCKd%2BsOQ7%2BZ9PH%2B5kaLDvNJZTCvmLhmiVwQyz0kJmPlhn7423S2YC12KBw2UWcuREDziBXJRoUJunTuIIbW8wuPUatLkUmVoUeA8amv7ayiMHuVBMajAX0kLiu5Agtt4wfNQggXJVvwJhQxfH1DwZk6EDLHfVDfN9j5oLaqED%2F7l7s0GWinfwxcBDs9PYtfOF4yf5pwgwv3O3CrMgPO%2BkFsDLA2M2hhQD2hX2lkAptZHd6O6siWuflS%2B5Ne5rG3z9HubKh33aDSNFddnUaqKMVQKGs3dVxrosFIkM0Hp3E5t221kdf9hTBZP9s95Tsq3cD0MFsEifC41FHBBgj1XFjTpFBfKpatwaEtvS35oYGtiOYnZA5tLxHCTjLonDvREg6FhB%2FEtnluwwc2V3BCQQVJztnx7vpDGJAePY1XEWlJtVBCRd4Dtgv2pQFHGn5Nu26Lzz38qozw2AtyBJnNgzw%2FS9xUUxjAWmQ9Jq5s62Ew1KWNzgY6pgEmNSjBj8C3MWrYuJJlosAYF6DDmckUPRo2iXUVjEmClYDOQ0o24CI95BISH4yEPNlhITf2dk86SmlB0suEesNpL5%2FQuT%2F2xpYH8EUQcrtlaWs3Dm1xrO57MlBV%2FmUMJlvfv9EecZrqpzpF8U3l9KNBJVE4pKgYXo49aGKLj2qXCPVLg6dT44kOa1lUDm7cLUFYUFI75eZvOQuyu3%2FcQBloyz54Olo8&X-Amz-Signature=b59d821e205a702593223a8dda366b6fee4ebed391b9f8a48fc292c6d9a046ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753TDFEM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWRzzTsiaFh0y5cV3Q7JsGfLSwzRyQXYwGvlX67neu1AiAI1vOUNHQP0HcQNttKQVQp80%2BaXj252UaOZ6XRn2%2FyfyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8BjR0mdRyyVQXhNeKtwDLyYuD3iPRjFX%2BPIV%2Fu7Uv7mSmWeCo76VsY6N758JlFEoTGePPMNF4kFH4nO1CG95Tk1%2BeZ7fpdY6UQMmin5pkUSzPVNmn94KAfWEEym56nyH%2F6rT174q5cR4UWDdIq4bXLHjbB0NYz7VBcCa1MCKd%2BsOQ7%2BZ9PH%2B5kaLDvNJZTCvmLhmiVwQyz0kJmPlhn7423S2YC12KBw2UWcuREDziBXJRoUJunTuIIbW8wuPUatLkUmVoUeA8amv7ayiMHuVBMajAX0kLiu5Agtt4wfNQggXJVvwJhQxfH1DwZk6EDLHfVDfN9j5oLaqED%2F7l7s0GWinfwxcBDs9PYtfOF4yf5pwgwv3O3CrMgPO%2BkFsDLA2M2hhQD2hX2lkAptZHd6O6siWuflS%2B5Ne5rG3z9HubKh33aDSNFddnUaqKMVQKGs3dVxrosFIkM0Hp3E5t221kdf9hTBZP9s95Tsq3cD0MFsEifC41FHBBgj1XFjTpFBfKpatwaEtvS35oYGtiOYnZA5tLxHCTjLonDvREg6FhB%2FEtnluwwc2V3BCQQVJztnx7vpDGJAePY1XEWlJtVBCRd4Dtgv2pQFHGn5Nu26Lzz38qozw2AtyBJnNgzw%2FS9xUUxjAWmQ9Jq5s62Ew1KWNzgY6pgEmNSjBj8C3MWrYuJJlosAYF6DDmckUPRo2iXUVjEmClYDOQ0o24CI95BISH4yEPNlhITf2dk86SmlB0suEesNpL5%2FQuT%2F2xpYH8EUQcrtlaWs3Dm1xrO57MlBV%2FmUMJlvfv9EecZrqpzpF8U3l9KNBJVE4pKgYXo49aGKLj2qXCPVLg6dT44kOa1lUDm7cLUFYUFI75eZvOQuyu3%2FcQBloyz54Olo8&X-Amz-Signature=72217be2cd259c6db60d491076cf9cdfccf843e817e4310ecac349e4c7c5ce91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753TDFEM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWRzzTsiaFh0y5cV3Q7JsGfLSwzRyQXYwGvlX67neu1AiAI1vOUNHQP0HcQNttKQVQp80%2BaXj252UaOZ6XRn2%2FyfyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8BjR0mdRyyVQXhNeKtwDLyYuD3iPRjFX%2BPIV%2Fu7Uv7mSmWeCo76VsY6N758JlFEoTGePPMNF4kFH4nO1CG95Tk1%2BeZ7fpdY6UQMmin5pkUSzPVNmn94KAfWEEym56nyH%2F6rT174q5cR4UWDdIq4bXLHjbB0NYz7VBcCa1MCKd%2BsOQ7%2BZ9PH%2B5kaLDvNJZTCvmLhmiVwQyz0kJmPlhn7423S2YC12KBw2UWcuREDziBXJRoUJunTuIIbW8wuPUatLkUmVoUeA8amv7ayiMHuVBMajAX0kLiu5Agtt4wfNQggXJVvwJhQxfH1DwZk6EDLHfVDfN9j5oLaqED%2F7l7s0GWinfwxcBDs9PYtfOF4yf5pwgwv3O3CrMgPO%2BkFsDLA2M2hhQD2hX2lkAptZHd6O6siWuflS%2B5Ne5rG3z9HubKh33aDSNFddnUaqKMVQKGs3dVxrosFIkM0Hp3E5t221kdf9hTBZP9s95Tsq3cD0MFsEifC41FHBBgj1XFjTpFBfKpatwaEtvS35oYGtiOYnZA5tLxHCTjLonDvREg6FhB%2FEtnluwwc2V3BCQQVJztnx7vpDGJAePY1XEWlJtVBCRd4Dtgv2pQFHGn5Nu26Lzz38qozw2AtyBJnNgzw%2FS9xUUxjAWmQ9Jq5s62Ew1KWNzgY6pgEmNSjBj8C3MWrYuJJlosAYF6DDmckUPRo2iXUVjEmClYDOQ0o24CI95BISH4yEPNlhITf2dk86SmlB0suEesNpL5%2FQuT%2F2xpYH8EUQcrtlaWs3Dm1xrO57MlBV%2FmUMJlvfv9EecZrqpzpF8U3l9KNBJVE4pKgYXo49aGKLj2qXCPVLg6dT44kOa1lUDm7cLUFYUFI75eZvOQuyu3%2FcQBloyz54Olo8&X-Amz-Signature=1a1396c6cf55042b3472ca95330e5e6acc0a4ed6cc38837ff11384d029cb730f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753TDFEM%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWRzzTsiaFh0y5cV3Q7JsGfLSwzRyQXYwGvlX67neu1AiAI1vOUNHQP0HcQNttKQVQp80%2BaXj252UaOZ6XRn2%2FyfyqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8BjR0mdRyyVQXhNeKtwDLyYuD3iPRjFX%2BPIV%2Fu7Uv7mSmWeCo76VsY6N758JlFEoTGePPMNF4kFH4nO1CG95Tk1%2BeZ7fpdY6UQMmin5pkUSzPVNmn94KAfWEEym56nyH%2F6rT174q5cR4UWDdIq4bXLHjbB0NYz7VBcCa1MCKd%2BsOQ7%2BZ9PH%2B5kaLDvNJZTCvmLhmiVwQyz0kJmPlhn7423S2YC12KBw2UWcuREDziBXJRoUJunTuIIbW8wuPUatLkUmVoUeA8amv7ayiMHuVBMajAX0kLiu5Agtt4wfNQggXJVvwJhQxfH1DwZk6EDLHfVDfN9j5oLaqED%2F7l7s0GWinfwxcBDs9PYtfOF4yf5pwgwv3O3CrMgPO%2BkFsDLA2M2hhQD2hX2lkAptZHd6O6siWuflS%2B5Ne5rG3z9HubKh33aDSNFddnUaqKMVQKGs3dVxrosFIkM0Hp3E5t221kdf9hTBZP9s95Tsq3cD0MFsEifC41FHBBgj1XFjTpFBfKpatwaEtvS35oYGtiOYnZA5tLxHCTjLonDvREg6FhB%2FEtnluwwc2V3BCQQVJztnx7vpDGJAePY1XEWlJtVBCRd4Dtgv2pQFHGn5Nu26Lzz38qozw2AtyBJnNgzw%2FS9xUUxjAWmQ9Jq5s62Ew1KWNzgY6pgEmNSjBj8C3MWrYuJJlosAYF6DDmckUPRo2iXUVjEmClYDOQ0o24CI95BISH4yEPNlhITf2dk86SmlB0suEesNpL5%2FQuT%2F2xpYH8EUQcrtlaWs3Dm1xrO57MlBV%2FmUMJlvfv9EecZrqpzpF8U3l9KNBJVE4pKgYXo49aGKLj2qXCPVLg6dT44kOa1lUDm7cLUFYUFI75eZvOQuyu3%2FcQBloyz54Olo8&X-Amz-Signature=27541dd93794ed372a9a9db4caadb8158f71265739674ae866ce6ed446f151d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

