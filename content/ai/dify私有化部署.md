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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W26KV6JK%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdVbfUvpEJKqdsPdQ2rL8yqQjwtBYMkTTqCJqmn%2F2NAIhAIIwoL0fjtXuN9BJTOubbjtEAKPkoo%2FLCwPhcLwbLkyhKv8DCGQQABoMNjM3NDIzMTgzODA1Igzx2YInervzk2Z6NCUq3ANw8lg7rGI54bzjzMbJcBog06iAAluSD%2B7JoEOeclIDetWW4DYEQn1s5nKyfZUqJTag1QZ%2FCfX%2FmPHeOxRASEgpoc455gjQirovoZidzDngGleHznR1cZy%2FWfoUlvvOvVC%2FkByWqUfH6uHjhRI44Zju9A6nnl4Sx5Ycvvu3Ma2VWNc7W0QRHSieBkiYKtOlZOSJ9Ss%2BLYdq%2FOkyODcrGiDpOpxQdHx%2Fm%2Bcfig6a7vVScVcW8JLW8dm6nRSbsYWY88R3aiMeNwq4TBmtDjmP6h8XBncY1oF4DQTtcqfh92CPD38Ld3qGv%2BW9flQ6bYZsOXl5PQvrCprj2ehsszcX6LvFajnT4mauiwOKWQSimQ3PK5SeNNLlVsgYNhahbV49PemCHciGNFbvq8Z3KlUPL05Dc%2BtyNacPks5372%2FOntkovGqUruRnGpBdjUrEmMeF1GLMYE2hIxXQsSe105UHamoVr41Ei6S82sSscGNV3luOLM9qRE540WdvS6nn0wDrDrtmNGJpvFhOCMuAxdiof3KI%2FHqavVga6q7orCtg9JBz9XXxfPEuxZevNz5vdssrYe32tR4m9tOSMfhPzUYHqaXb9NdTHQ%2BOANrPCvAy3tSbfLPUcReA7ZQWh75neDDTsLfOBjqkARBcgp7lPecKZDWvCkGHoudSAIsBvhKRe3le%2FAoZs%2BUXTfr3mRh1LCTiGvziwIIpoZDLaoR4U19kkzXfbCF2w7dkc0IHopfh9E5pS4LsjQoBSWHoAHCPPVNHykzwuCABkg%2FexocsmRrCXt8arCb3ZOeFJPEjBP%2BfEsK4%2FA5zEihhxdL2Gazc8c2bnIBwQY7PgjiOhuC%2F6up8MhyrqF6WTmAoKAGd&X-Amz-Signature=1e3a270fb83dd0436c9c4facc652e49dc4ae5d898e57688a207a381e98d31bcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W26KV6JK%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdVbfUvpEJKqdsPdQ2rL8yqQjwtBYMkTTqCJqmn%2F2NAIhAIIwoL0fjtXuN9BJTOubbjtEAKPkoo%2FLCwPhcLwbLkyhKv8DCGQQABoMNjM3NDIzMTgzODA1Igzx2YInervzk2Z6NCUq3ANw8lg7rGI54bzjzMbJcBog06iAAluSD%2B7JoEOeclIDetWW4DYEQn1s5nKyfZUqJTag1QZ%2FCfX%2FmPHeOxRASEgpoc455gjQirovoZidzDngGleHznR1cZy%2FWfoUlvvOvVC%2FkByWqUfH6uHjhRI44Zju9A6nnl4Sx5Ycvvu3Ma2VWNc7W0QRHSieBkiYKtOlZOSJ9Ss%2BLYdq%2FOkyODcrGiDpOpxQdHx%2Fm%2Bcfig6a7vVScVcW8JLW8dm6nRSbsYWY88R3aiMeNwq4TBmtDjmP6h8XBncY1oF4DQTtcqfh92CPD38Ld3qGv%2BW9flQ6bYZsOXl5PQvrCprj2ehsszcX6LvFajnT4mauiwOKWQSimQ3PK5SeNNLlVsgYNhahbV49PemCHciGNFbvq8Z3KlUPL05Dc%2BtyNacPks5372%2FOntkovGqUruRnGpBdjUrEmMeF1GLMYE2hIxXQsSe105UHamoVr41Ei6S82sSscGNV3luOLM9qRE540WdvS6nn0wDrDrtmNGJpvFhOCMuAxdiof3KI%2FHqavVga6q7orCtg9JBz9XXxfPEuxZevNz5vdssrYe32tR4m9tOSMfhPzUYHqaXb9NdTHQ%2BOANrPCvAy3tSbfLPUcReA7ZQWh75neDDTsLfOBjqkARBcgp7lPecKZDWvCkGHoudSAIsBvhKRe3le%2FAoZs%2BUXTfr3mRh1LCTiGvziwIIpoZDLaoR4U19kkzXfbCF2w7dkc0IHopfh9E5pS4LsjQoBSWHoAHCPPVNHykzwuCABkg%2FexocsmRrCXt8arCb3ZOeFJPEjBP%2BfEsK4%2FA5zEihhxdL2Gazc8c2bnIBwQY7PgjiOhuC%2F6up8MhyrqF6WTmAoKAGd&X-Amz-Signature=527e50487bf5ca37da27a11a9726580ccd1d783d15fa16fee7290e436ec6d4d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W26KV6JK%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdVbfUvpEJKqdsPdQ2rL8yqQjwtBYMkTTqCJqmn%2F2NAIhAIIwoL0fjtXuN9BJTOubbjtEAKPkoo%2FLCwPhcLwbLkyhKv8DCGQQABoMNjM3NDIzMTgzODA1Igzx2YInervzk2Z6NCUq3ANw8lg7rGI54bzjzMbJcBog06iAAluSD%2B7JoEOeclIDetWW4DYEQn1s5nKyfZUqJTag1QZ%2FCfX%2FmPHeOxRASEgpoc455gjQirovoZidzDngGleHznR1cZy%2FWfoUlvvOvVC%2FkByWqUfH6uHjhRI44Zju9A6nnl4Sx5Ycvvu3Ma2VWNc7W0QRHSieBkiYKtOlZOSJ9Ss%2BLYdq%2FOkyODcrGiDpOpxQdHx%2Fm%2Bcfig6a7vVScVcW8JLW8dm6nRSbsYWY88R3aiMeNwq4TBmtDjmP6h8XBncY1oF4DQTtcqfh92CPD38Ld3qGv%2BW9flQ6bYZsOXl5PQvrCprj2ehsszcX6LvFajnT4mauiwOKWQSimQ3PK5SeNNLlVsgYNhahbV49PemCHciGNFbvq8Z3KlUPL05Dc%2BtyNacPks5372%2FOntkovGqUruRnGpBdjUrEmMeF1GLMYE2hIxXQsSe105UHamoVr41Ei6S82sSscGNV3luOLM9qRE540WdvS6nn0wDrDrtmNGJpvFhOCMuAxdiof3KI%2FHqavVga6q7orCtg9JBz9XXxfPEuxZevNz5vdssrYe32tR4m9tOSMfhPzUYHqaXb9NdTHQ%2BOANrPCvAy3tSbfLPUcReA7ZQWh75neDDTsLfOBjqkARBcgp7lPecKZDWvCkGHoudSAIsBvhKRe3le%2FAoZs%2BUXTfr3mRh1LCTiGvziwIIpoZDLaoR4U19kkzXfbCF2w7dkc0IHopfh9E5pS4LsjQoBSWHoAHCPPVNHykzwuCABkg%2FexocsmRrCXt8arCb3ZOeFJPEjBP%2BfEsK4%2FA5zEihhxdL2Gazc8c2bnIBwQY7PgjiOhuC%2F6up8MhyrqF6WTmAoKAGd&X-Amz-Signature=786b1bbe756b5b48f8661eeeb8877bd928580d2323d55c73858d48120c73c473&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W26KV6JK%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdVbfUvpEJKqdsPdQ2rL8yqQjwtBYMkTTqCJqmn%2F2NAIhAIIwoL0fjtXuN9BJTOubbjtEAKPkoo%2FLCwPhcLwbLkyhKv8DCGQQABoMNjM3NDIzMTgzODA1Igzx2YInervzk2Z6NCUq3ANw8lg7rGI54bzjzMbJcBog06iAAluSD%2B7JoEOeclIDetWW4DYEQn1s5nKyfZUqJTag1QZ%2FCfX%2FmPHeOxRASEgpoc455gjQirovoZidzDngGleHznR1cZy%2FWfoUlvvOvVC%2FkByWqUfH6uHjhRI44Zju9A6nnl4Sx5Ycvvu3Ma2VWNc7W0QRHSieBkiYKtOlZOSJ9Ss%2BLYdq%2FOkyODcrGiDpOpxQdHx%2Fm%2Bcfig6a7vVScVcW8JLW8dm6nRSbsYWY88R3aiMeNwq4TBmtDjmP6h8XBncY1oF4DQTtcqfh92CPD38Ld3qGv%2BW9flQ6bYZsOXl5PQvrCprj2ehsszcX6LvFajnT4mauiwOKWQSimQ3PK5SeNNLlVsgYNhahbV49PemCHciGNFbvq8Z3KlUPL05Dc%2BtyNacPks5372%2FOntkovGqUruRnGpBdjUrEmMeF1GLMYE2hIxXQsSe105UHamoVr41Ei6S82sSscGNV3luOLM9qRE540WdvS6nn0wDrDrtmNGJpvFhOCMuAxdiof3KI%2FHqavVga6q7orCtg9JBz9XXxfPEuxZevNz5vdssrYe32tR4m9tOSMfhPzUYHqaXb9NdTHQ%2BOANrPCvAy3tSbfLPUcReA7ZQWh75neDDTsLfOBjqkARBcgp7lPecKZDWvCkGHoudSAIsBvhKRe3le%2FAoZs%2BUXTfr3mRh1LCTiGvziwIIpoZDLaoR4U19kkzXfbCF2w7dkc0IHopfh9E5pS4LsjQoBSWHoAHCPPVNHykzwuCABkg%2FexocsmRrCXt8arCb3ZOeFJPEjBP%2BfEsK4%2FA5zEihhxdL2Gazc8c2bnIBwQY7PgjiOhuC%2F6up8MhyrqF6WTmAoKAGd&X-Amz-Signature=368dada4d104a3bebf1bf97365689278b48892bc61f29d5a15dc87472a786a2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W26KV6JK%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdVbfUvpEJKqdsPdQ2rL8yqQjwtBYMkTTqCJqmn%2F2NAIhAIIwoL0fjtXuN9BJTOubbjtEAKPkoo%2FLCwPhcLwbLkyhKv8DCGQQABoMNjM3NDIzMTgzODA1Igzx2YInervzk2Z6NCUq3ANw8lg7rGI54bzjzMbJcBog06iAAluSD%2B7JoEOeclIDetWW4DYEQn1s5nKyfZUqJTag1QZ%2FCfX%2FmPHeOxRASEgpoc455gjQirovoZidzDngGleHznR1cZy%2FWfoUlvvOvVC%2FkByWqUfH6uHjhRI44Zju9A6nnl4Sx5Ycvvu3Ma2VWNc7W0QRHSieBkiYKtOlZOSJ9Ss%2BLYdq%2FOkyODcrGiDpOpxQdHx%2Fm%2Bcfig6a7vVScVcW8JLW8dm6nRSbsYWY88R3aiMeNwq4TBmtDjmP6h8XBncY1oF4DQTtcqfh92CPD38Ld3qGv%2BW9flQ6bYZsOXl5PQvrCprj2ehsszcX6LvFajnT4mauiwOKWQSimQ3PK5SeNNLlVsgYNhahbV49PemCHciGNFbvq8Z3KlUPL05Dc%2BtyNacPks5372%2FOntkovGqUruRnGpBdjUrEmMeF1GLMYE2hIxXQsSe105UHamoVr41Ei6S82sSscGNV3luOLM9qRE540WdvS6nn0wDrDrtmNGJpvFhOCMuAxdiof3KI%2FHqavVga6q7orCtg9JBz9XXxfPEuxZevNz5vdssrYe32tR4m9tOSMfhPzUYHqaXb9NdTHQ%2BOANrPCvAy3tSbfLPUcReA7ZQWh75neDDTsLfOBjqkARBcgp7lPecKZDWvCkGHoudSAIsBvhKRe3le%2FAoZs%2BUXTfr3mRh1LCTiGvziwIIpoZDLaoR4U19kkzXfbCF2w7dkc0IHopfh9E5pS4LsjQoBSWHoAHCPPVNHykzwuCABkg%2FexocsmRrCXt8arCb3ZOeFJPEjBP%2BfEsK4%2FA5zEihhxdL2Gazc8c2bnIBwQY7PgjiOhuC%2F6up8MhyrqF6WTmAoKAGd&X-Amz-Signature=8943efd4da35a30e27acd8036cf1716c233243233bdac0cf09451f828fa7c74b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W26KV6JK%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdVbfUvpEJKqdsPdQ2rL8yqQjwtBYMkTTqCJqmn%2F2NAIhAIIwoL0fjtXuN9BJTOubbjtEAKPkoo%2FLCwPhcLwbLkyhKv8DCGQQABoMNjM3NDIzMTgzODA1Igzx2YInervzk2Z6NCUq3ANw8lg7rGI54bzjzMbJcBog06iAAluSD%2B7JoEOeclIDetWW4DYEQn1s5nKyfZUqJTag1QZ%2FCfX%2FmPHeOxRASEgpoc455gjQirovoZidzDngGleHznR1cZy%2FWfoUlvvOvVC%2FkByWqUfH6uHjhRI44Zju9A6nnl4Sx5Ycvvu3Ma2VWNc7W0QRHSieBkiYKtOlZOSJ9Ss%2BLYdq%2FOkyODcrGiDpOpxQdHx%2Fm%2Bcfig6a7vVScVcW8JLW8dm6nRSbsYWY88R3aiMeNwq4TBmtDjmP6h8XBncY1oF4DQTtcqfh92CPD38Ld3qGv%2BW9flQ6bYZsOXl5PQvrCprj2ehsszcX6LvFajnT4mauiwOKWQSimQ3PK5SeNNLlVsgYNhahbV49PemCHciGNFbvq8Z3KlUPL05Dc%2BtyNacPks5372%2FOntkovGqUruRnGpBdjUrEmMeF1GLMYE2hIxXQsSe105UHamoVr41Ei6S82sSscGNV3luOLM9qRE540WdvS6nn0wDrDrtmNGJpvFhOCMuAxdiof3KI%2FHqavVga6q7orCtg9JBz9XXxfPEuxZevNz5vdssrYe32tR4m9tOSMfhPzUYHqaXb9NdTHQ%2BOANrPCvAy3tSbfLPUcReA7ZQWh75neDDTsLfOBjqkARBcgp7lPecKZDWvCkGHoudSAIsBvhKRe3le%2FAoZs%2BUXTfr3mRh1LCTiGvziwIIpoZDLaoR4U19kkzXfbCF2w7dkc0IHopfh9E5pS4LsjQoBSWHoAHCPPVNHykzwuCABkg%2FexocsmRrCXt8arCb3ZOeFJPEjBP%2BfEsK4%2FA5zEihhxdL2Gazc8c2bnIBwQY7PgjiOhuC%2F6up8MhyrqF6WTmAoKAGd&X-Amz-Signature=881f1bcf3269996b1a8dc1e668011ca584d7803439c03888443bd48d0725a904&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W26KV6JK%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdVbfUvpEJKqdsPdQ2rL8yqQjwtBYMkTTqCJqmn%2F2NAIhAIIwoL0fjtXuN9BJTOubbjtEAKPkoo%2FLCwPhcLwbLkyhKv8DCGQQABoMNjM3NDIzMTgzODA1Igzx2YInervzk2Z6NCUq3ANw8lg7rGI54bzjzMbJcBog06iAAluSD%2B7JoEOeclIDetWW4DYEQn1s5nKyfZUqJTag1QZ%2FCfX%2FmPHeOxRASEgpoc455gjQirovoZidzDngGleHznR1cZy%2FWfoUlvvOvVC%2FkByWqUfH6uHjhRI44Zju9A6nnl4Sx5Ycvvu3Ma2VWNc7W0QRHSieBkiYKtOlZOSJ9Ss%2BLYdq%2FOkyODcrGiDpOpxQdHx%2Fm%2Bcfig6a7vVScVcW8JLW8dm6nRSbsYWY88R3aiMeNwq4TBmtDjmP6h8XBncY1oF4DQTtcqfh92CPD38Ld3qGv%2BW9flQ6bYZsOXl5PQvrCprj2ehsszcX6LvFajnT4mauiwOKWQSimQ3PK5SeNNLlVsgYNhahbV49PemCHciGNFbvq8Z3KlUPL05Dc%2BtyNacPks5372%2FOntkovGqUruRnGpBdjUrEmMeF1GLMYE2hIxXQsSe105UHamoVr41Ei6S82sSscGNV3luOLM9qRE540WdvS6nn0wDrDrtmNGJpvFhOCMuAxdiof3KI%2FHqavVga6q7orCtg9JBz9XXxfPEuxZevNz5vdssrYe32tR4m9tOSMfhPzUYHqaXb9NdTHQ%2BOANrPCvAy3tSbfLPUcReA7ZQWh75neDDTsLfOBjqkARBcgp7lPecKZDWvCkGHoudSAIsBvhKRe3le%2FAoZs%2BUXTfr3mRh1LCTiGvziwIIpoZDLaoR4U19kkzXfbCF2w7dkc0IHopfh9E5pS4LsjQoBSWHoAHCPPVNHykzwuCABkg%2FexocsmRrCXt8arCb3ZOeFJPEjBP%2BfEsK4%2FA5zEihhxdL2Gazc8c2bnIBwQY7PgjiOhuC%2F6up8MhyrqF6WTmAoKAGd&X-Amz-Signature=4b98b5c327db5a8195795ddf508e293144a996c58d63ebae4105c3ce4d9462fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W26KV6JK%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdVbfUvpEJKqdsPdQ2rL8yqQjwtBYMkTTqCJqmn%2F2NAIhAIIwoL0fjtXuN9BJTOubbjtEAKPkoo%2FLCwPhcLwbLkyhKv8DCGQQABoMNjM3NDIzMTgzODA1Igzx2YInervzk2Z6NCUq3ANw8lg7rGI54bzjzMbJcBog06iAAluSD%2B7JoEOeclIDetWW4DYEQn1s5nKyfZUqJTag1QZ%2FCfX%2FmPHeOxRASEgpoc455gjQirovoZidzDngGleHznR1cZy%2FWfoUlvvOvVC%2FkByWqUfH6uHjhRI44Zju9A6nnl4Sx5Ycvvu3Ma2VWNc7W0QRHSieBkiYKtOlZOSJ9Ss%2BLYdq%2FOkyODcrGiDpOpxQdHx%2Fm%2Bcfig6a7vVScVcW8JLW8dm6nRSbsYWY88R3aiMeNwq4TBmtDjmP6h8XBncY1oF4DQTtcqfh92CPD38Ld3qGv%2BW9flQ6bYZsOXl5PQvrCprj2ehsszcX6LvFajnT4mauiwOKWQSimQ3PK5SeNNLlVsgYNhahbV49PemCHciGNFbvq8Z3KlUPL05Dc%2BtyNacPks5372%2FOntkovGqUruRnGpBdjUrEmMeF1GLMYE2hIxXQsSe105UHamoVr41Ei6S82sSscGNV3luOLM9qRE540WdvS6nn0wDrDrtmNGJpvFhOCMuAxdiof3KI%2FHqavVga6q7orCtg9JBz9XXxfPEuxZevNz5vdssrYe32tR4m9tOSMfhPzUYHqaXb9NdTHQ%2BOANrPCvAy3tSbfLPUcReA7ZQWh75neDDTsLfOBjqkARBcgp7lPecKZDWvCkGHoudSAIsBvhKRe3le%2FAoZs%2BUXTfr3mRh1LCTiGvziwIIpoZDLaoR4U19kkzXfbCF2w7dkc0IHopfh9E5pS4LsjQoBSWHoAHCPPVNHykzwuCABkg%2FexocsmRrCXt8arCb3ZOeFJPEjBP%2BfEsK4%2FA5zEihhxdL2Gazc8c2bnIBwQY7PgjiOhuC%2F6up8MhyrqF6WTmAoKAGd&X-Amz-Signature=d96b5460bd9f12849fccd05050b6b2c9044d225ecba86d7764c44343a1d39769&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W26KV6JK%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdVbfUvpEJKqdsPdQ2rL8yqQjwtBYMkTTqCJqmn%2F2NAIhAIIwoL0fjtXuN9BJTOubbjtEAKPkoo%2FLCwPhcLwbLkyhKv8DCGQQABoMNjM3NDIzMTgzODA1Igzx2YInervzk2Z6NCUq3ANw8lg7rGI54bzjzMbJcBog06iAAluSD%2B7JoEOeclIDetWW4DYEQn1s5nKyfZUqJTag1QZ%2FCfX%2FmPHeOxRASEgpoc455gjQirovoZidzDngGleHznR1cZy%2FWfoUlvvOvVC%2FkByWqUfH6uHjhRI44Zju9A6nnl4Sx5Ycvvu3Ma2VWNc7W0QRHSieBkiYKtOlZOSJ9Ss%2BLYdq%2FOkyODcrGiDpOpxQdHx%2Fm%2Bcfig6a7vVScVcW8JLW8dm6nRSbsYWY88R3aiMeNwq4TBmtDjmP6h8XBncY1oF4DQTtcqfh92CPD38Ld3qGv%2BW9flQ6bYZsOXl5PQvrCprj2ehsszcX6LvFajnT4mauiwOKWQSimQ3PK5SeNNLlVsgYNhahbV49PemCHciGNFbvq8Z3KlUPL05Dc%2BtyNacPks5372%2FOntkovGqUruRnGpBdjUrEmMeF1GLMYE2hIxXQsSe105UHamoVr41Ei6S82sSscGNV3luOLM9qRE540WdvS6nn0wDrDrtmNGJpvFhOCMuAxdiof3KI%2FHqavVga6q7orCtg9JBz9XXxfPEuxZevNz5vdssrYe32tR4m9tOSMfhPzUYHqaXb9NdTHQ%2BOANrPCvAy3tSbfLPUcReA7ZQWh75neDDTsLfOBjqkARBcgp7lPecKZDWvCkGHoudSAIsBvhKRe3le%2FAoZs%2BUXTfr3mRh1LCTiGvziwIIpoZDLaoR4U19kkzXfbCF2w7dkc0IHopfh9E5pS4LsjQoBSWHoAHCPPVNHykzwuCABkg%2FexocsmRrCXt8arCb3ZOeFJPEjBP%2BfEsK4%2FA5zEihhxdL2Gazc8c2bnIBwQY7PgjiOhuC%2F6up8MhyrqF6WTmAoKAGd&X-Amz-Signature=a929b40ce68d899761baafb97ec249e41366768892212092147081ba3466d189&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W26KV6JK%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdVbfUvpEJKqdsPdQ2rL8yqQjwtBYMkTTqCJqmn%2F2NAIhAIIwoL0fjtXuN9BJTOubbjtEAKPkoo%2FLCwPhcLwbLkyhKv8DCGQQABoMNjM3NDIzMTgzODA1Igzx2YInervzk2Z6NCUq3ANw8lg7rGI54bzjzMbJcBog06iAAluSD%2B7JoEOeclIDetWW4DYEQn1s5nKyfZUqJTag1QZ%2FCfX%2FmPHeOxRASEgpoc455gjQirovoZidzDngGleHznR1cZy%2FWfoUlvvOvVC%2FkByWqUfH6uHjhRI44Zju9A6nnl4Sx5Ycvvu3Ma2VWNc7W0QRHSieBkiYKtOlZOSJ9Ss%2BLYdq%2FOkyODcrGiDpOpxQdHx%2Fm%2Bcfig6a7vVScVcW8JLW8dm6nRSbsYWY88R3aiMeNwq4TBmtDjmP6h8XBncY1oF4DQTtcqfh92CPD38Ld3qGv%2BW9flQ6bYZsOXl5PQvrCprj2ehsszcX6LvFajnT4mauiwOKWQSimQ3PK5SeNNLlVsgYNhahbV49PemCHciGNFbvq8Z3KlUPL05Dc%2BtyNacPks5372%2FOntkovGqUruRnGpBdjUrEmMeF1GLMYE2hIxXQsSe105UHamoVr41Ei6S82sSscGNV3luOLM9qRE540WdvS6nn0wDrDrtmNGJpvFhOCMuAxdiof3KI%2FHqavVga6q7orCtg9JBz9XXxfPEuxZevNz5vdssrYe32tR4m9tOSMfhPzUYHqaXb9NdTHQ%2BOANrPCvAy3tSbfLPUcReA7ZQWh75neDDTsLfOBjqkARBcgp7lPecKZDWvCkGHoudSAIsBvhKRe3le%2FAoZs%2BUXTfr3mRh1LCTiGvziwIIpoZDLaoR4U19kkzXfbCF2w7dkc0IHopfh9E5pS4LsjQoBSWHoAHCPPVNHykzwuCABkg%2FexocsmRrCXt8arCb3ZOeFJPEjBP%2BfEsK4%2FA5zEihhxdL2Gazc8c2bnIBwQY7PgjiOhuC%2F6up8MhyrqF6WTmAoKAGd&X-Amz-Signature=4a0c8466999f852d46d1a53526d8ad93564b7f6f80f390931e7165ff7a169845&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

