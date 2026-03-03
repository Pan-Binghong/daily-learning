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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZCWIGLE%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ69LF6sL6Ae6ny5r85PJBzxslqEwx5iVb0QmfZc4H8gIhAJRSmnpnsg%2BA598egQTvBfB2%2FmMg8JcEun12rCids3mkKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsDVFfN9gApYlGtswq3AMDzBuLzFSjOzCdRsTn8kHytJ%2BI9fe4luf09efu2fvIbuNjNXWBdoEiIsKPyCye2YoY4Rcm89186vXVPivg64mo90WzrP4%2BiJmwhfEP4bj4AQdZCkA0WfFtYPyRAz%2B%2F%2Bj2FdfFy7fXTszvn1D5fD5ngTVGkBFunZSWNGUqiwIws%2FsRSMPl08tORvD1LlydyzhdS7z4ugESjz6xnugd4LWdYhuMm6bw9w22gh0VUm%2FmD4FhJQVUOTQv%2Fh3yk0Lg%2Fd9n7LXF%2BvOKUC9pkDLQRDVg9vPXqHLq4SwiRRaILIFgWI7DsIV1HfgIhJ%2BvrxDDshBodX%2FS5kfuMJmo6O%2BZGMspPmkWJuFq0SPWcghEw7wDXKKS8MFOExMDfu73vpkt%2Fpla7UvKqVBjhS5KF%2BGUhspSXf1b%2BkYyLpy5w4o1S8Bw8kpHIQqV88Kz0MI6Ah%2FvRdI8qGe57oIAsliR40IOPdH93skYcZF5Q3piyOFv34bng6ABLgpWUVxSTuIFmpVB%2BFRqOhdCj2%2BYuhV519OuCs46UbO%2BGMCmlJXeE114%2BLYZPJ9DEHlYBh6ged4pxbHPLwr2oE7MPo%2BCdXH%2F263CYG7CA11v%2FN%2BPlNpYKELeibuNBuN5uVv7kQaNKVAcOMTC1tZjNBjqkAZwKRKBVu40MxzMf%2FSvmr%2BlENp8v2HPn8y4ewrTyuWistgAb%2FCLuOTGHIIYCtZf3Cj3jnRdsd%2BbY7EXt%2FFEqpCRKrrCD%2BfZoYna5zd24kvmgzxnLiv89DyPA253aS3ffpxCEq2%2B%2FdfYwWxzmtPwLXdiEG2o5Pt1kotXS2vANr53OASP8jbtvsxzmcYNYCsj8jC6EY%2BNwzUxw2XxX2lWRGsTDqLL%2F&X-Amz-Signature=1ff57c1a1786f312b162cd40d50ccd96b953f61fb989900d46b119996b0e4882&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZCWIGLE%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ69LF6sL6Ae6ny5r85PJBzxslqEwx5iVb0QmfZc4H8gIhAJRSmnpnsg%2BA598egQTvBfB2%2FmMg8JcEun12rCids3mkKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsDVFfN9gApYlGtswq3AMDzBuLzFSjOzCdRsTn8kHytJ%2BI9fe4luf09efu2fvIbuNjNXWBdoEiIsKPyCye2YoY4Rcm89186vXVPivg64mo90WzrP4%2BiJmwhfEP4bj4AQdZCkA0WfFtYPyRAz%2B%2F%2Bj2FdfFy7fXTszvn1D5fD5ngTVGkBFunZSWNGUqiwIws%2FsRSMPl08tORvD1LlydyzhdS7z4ugESjz6xnugd4LWdYhuMm6bw9w22gh0VUm%2FmD4FhJQVUOTQv%2Fh3yk0Lg%2Fd9n7LXF%2BvOKUC9pkDLQRDVg9vPXqHLq4SwiRRaILIFgWI7DsIV1HfgIhJ%2BvrxDDshBodX%2FS5kfuMJmo6O%2BZGMspPmkWJuFq0SPWcghEw7wDXKKS8MFOExMDfu73vpkt%2Fpla7UvKqVBjhS5KF%2BGUhspSXf1b%2BkYyLpy5w4o1S8Bw8kpHIQqV88Kz0MI6Ah%2FvRdI8qGe57oIAsliR40IOPdH93skYcZF5Q3piyOFv34bng6ABLgpWUVxSTuIFmpVB%2BFRqOhdCj2%2BYuhV519OuCs46UbO%2BGMCmlJXeE114%2BLYZPJ9DEHlYBh6ged4pxbHPLwr2oE7MPo%2BCdXH%2F263CYG7CA11v%2FN%2BPlNpYKELeibuNBuN5uVv7kQaNKVAcOMTC1tZjNBjqkAZwKRKBVu40MxzMf%2FSvmr%2BlENp8v2HPn8y4ewrTyuWistgAb%2FCLuOTGHIIYCtZf3Cj3jnRdsd%2BbY7EXt%2FFEqpCRKrrCD%2BfZoYna5zd24kvmgzxnLiv89DyPA253aS3ffpxCEq2%2B%2FdfYwWxzmtPwLXdiEG2o5Pt1kotXS2vANr53OASP8jbtvsxzmcYNYCsj8jC6EY%2BNwzUxw2XxX2lWRGsTDqLL%2F&X-Amz-Signature=f04e395d615d90fe4cb215fb6db943839d3da37ae49b300bae1de14aa47491b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZCWIGLE%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ69LF6sL6Ae6ny5r85PJBzxslqEwx5iVb0QmfZc4H8gIhAJRSmnpnsg%2BA598egQTvBfB2%2FmMg8JcEun12rCids3mkKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsDVFfN9gApYlGtswq3AMDzBuLzFSjOzCdRsTn8kHytJ%2BI9fe4luf09efu2fvIbuNjNXWBdoEiIsKPyCye2YoY4Rcm89186vXVPivg64mo90WzrP4%2BiJmwhfEP4bj4AQdZCkA0WfFtYPyRAz%2B%2F%2Bj2FdfFy7fXTszvn1D5fD5ngTVGkBFunZSWNGUqiwIws%2FsRSMPl08tORvD1LlydyzhdS7z4ugESjz6xnugd4LWdYhuMm6bw9w22gh0VUm%2FmD4FhJQVUOTQv%2Fh3yk0Lg%2Fd9n7LXF%2BvOKUC9pkDLQRDVg9vPXqHLq4SwiRRaILIFgWI7DsIV1HfgIhJ%2BvrxDDshBodX%2FS5kfuMJmo6O%2BZGMspPmkWJuFq0SPWcghEw7wDXKKS8MFOExMDfu73vpkt%2Fpla7UvKqVBjhS5KF%2BGUhspSXf1b%2BkYyLpy5w4o1S8Bw8kpHIQqV88Kz0MI6Ah%2FvRdI8qGe57oIAsliR40IOPdH93skYcZF5Q3piyOFv34bng6ABLgpWUVxSTuIFmpVB%2BFRqOhdCj2%2BYuhV519OuCs46UbO%2BGMCmlJXeE114%2BLYZPJ9DEHlYBh6ged4pxbHPLwr2oE7MPo%2BCdXH%2F263CYG7CA11v%2FN%2BPlNpYKELeibuNBuN5uVv7kQaNKVAcOMTC1tZjNBjqkAZwKRKBVu40MxzMf%2FSvmr%2BlENp8v2HPn8y4ewrTyuWistgAb%2FCLuOTGHIIYCtZf3Cj3jnRdsd%2BbY7EXt%2FFEqpCRKrrCD%2BfZoYna5zd24kvmgzxnLiv89DyPA253aS3ffpxCEq2%2B%2FdfYwWxzmtPwLXdiEG2o5Pt1kotXS2vANr53OASP8jbtvsxzmcYNYCsj8jC6EY%2BNwzUxw2XxX2lWRGsTDqLL%2F&X-Amz-Signature=7de6a99d6762a4e6710f7b4463b3c2341c9d7821af1c3cdd443401252f121804&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZCWIGLE%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ69LF6sL6Ae6ny5r85PJBzxslqEwx5iVb0QmfZc4H8gIhAJRSmnpnsg%2BA598egQTvBfB2%2FmMg8JcEun12rCids3mkKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsDVFfN9gApYlGtswq3AMDzBuLzFSjOzCdRsTn8kHytJ%2BI9fe4luf09efu2fvIbuNjNXWBdoEiIsKPyCye2YoY4Rcm89186vXVPivg64mo90WzrP4%2BiJmwhfEP4bj4AQdZCkA0WfFtYPyRAz%2B%2F%2Bj2FdfFy7fXTszvn1D5fD5ngTVGkBFunZSWNGUqiwIws%2FsRSMPl08tORvD1LlydyzhdS7z4ugESjz6xnugd4LWdYhuMm6bw9w22gh0VUm%2FmD4FhJQVUOTQv%2Fh3yk0Lg%2Fd9n7LXF%2BvOKUC9pkDLQRDVg9vPXqHLq4SwiRRaILIFgWI7DsIV1HfgIhJ%2BvrxDDshBodX%2FS5kfuMJmo6O%2BZGMspPmkWJuFq0SPWcghEw7wDXKKS8MFOExMDfu73vpkt%2Fpla7UvKqVBjhS5KF%2BGUhspSXf1b%2BkYyLpy5w4o1S8Bw8kpHIQqV88Kz0MI6Ah%2FvRdI8qGe57oIAsliR40IOPdH93skYcZF5Q3piyOFv34bng6ABLgpWUVxSTuIFmpVB%2BFRqOhdCj2%2BYuhV519OuCs46UbO%2BGMCmlJXeE114%2BLYZPJ9DEHlYBh6ged4pxbHPLwr2oE7MPo%2BCdXH%2F263CYG7CA11v%2FN%2BPlNpYKELeibuNBuN5uVv7kQaNKVAcOMTC1tZjNBjqkAZwKRKBVu40MxzMf%2FSvmr%2BlENp8v2HPn8y4ewrTyuWistgAb%2FCLuOTGHIIYCtZf3Cj3jnRdsd%2BbY7EXt%2FFEqpCRKrrCD%2BfZoYna5zd24kvmgzxnLiv89DyPA253aS3ffpxCEq2%2B%2FdfYwWxzmtPwLXdiEG2o5Pt1kotXS2vANr53OASP8jbtvsxzmcYNYCsj8jC6EY%2BNwzUxw2XxX2lWRGsTDqLL%2F&X-Amz-Signature=b70630f76837b85b270e65aeb91ed7b1a2f45c0b893a15d7fe1fe8f980ded169&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZCWIGLE%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ69LF6sL6Ae6ny5r85PJBzxslqEwx5iVb0QmfZc4H8gIhAJRSmnpnsg%2BA598egQTvBfB2%2FmMg8JcEun12rCids3mkKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsDVFfN9gApYlGtswq3AMDzBuLzFSjOzCdRsTn8kHytJ%2BI9fe4luf09efu2fvIbuNjNXWBdoEiIsKPyCye2YoY4Rcm89186vXVPivg64mo90WzrP4%2BiJmwhfEP4bj4AQdZCkA0WfFtYPyRAz%2B%2F%2Bj2FdfFy7fXTszvn1D5fD5ngTVGkBFunZSWNGUqiwIws%2FsRSMPl08tORvD1LlydyzhdS7z4ugESjz6xnugd4LWdYhuMm6bw9w22gh0VUm%2FmD4FhJQVUOTQv%2Fh3yk0Lg%2Fd9n7LXF%2BvOKUC9pkDLQRDVg9vPXqHLq4SwiRRaILIFgWI7DsIV1HfgIhJ%2BvrxDDshBodX%2FS5kfuMJmo6O%2BZGMspPmkWJuFq0SPWcghEw7wDXKKS8MFOExMDfu73vpkt%2Fpla7UvKqVBjhS5KF%2BGUhspSXf1b%2BkYyLpy5w4o1S8Bw8kpHIQqV88Kz0MI6Ah%2FvRdI8qGe57oIAsliR40IOPdH93skYcZF5Q3piyOFv34bng6ABLgpWUVxSTuIFmpVB%2BFRqOhdCj2%2BYuhV519OuCs46UbO%2BGMCmlJXeE114%2BLYZPJ9DEHlYBh6ged4pxbHPLwr2oE7MPo%2BCdXH%2F263CYG7CA11v%2FN%2BPlNpYKELeibuNBuN5uVv7kQaNKVAcOMTC1tZjNBjqkAZwKRKBVu40MxzMf%2FSvmr%2BlENp8v2HPn8y4ewrTyuWistgAb%2FCLuOTGHIIYCtZf3Cj3jnRdsd%2BbY7EXt%2FFEqpCRKrrCD%2BfZoYna5zd24kvmgzxnLiv89DyPA253aS3ffpxCEq2%2B%2FdfYwWxzmtPwLXdiEG2o5Pt1kotXS2vANr53OASP8jbtvsxzmcYNYCsj8jC6EY%2BNwzUxw2XxX2lWRGsTDqLL%2F&X-Amz-Signature=60c87d30489acc32c0ad217d93bd8fe10701ac7872e831cd603e195d9193f8e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZCWIGLE%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ69LF6sL6Ae6ny5r85PJBzxslqEwx5iVb0QmfZc4H8gIhAJRSmnpnsg%2BA598egQTvBfB2%2FmMg8JcEun12rCids3mkKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsDVFfN9gApYlGtswq3AMDzBuLzFSjOzCdRsTn8kHytJ%2BI9fe4luf09efu2fvIbuNjNXWBdoEiIsKPyCye2YoY4Rcm89186vXVPivg64mo90WzrP4%2BiJmwhfEP4bj4AQdZCkA0WfFtYPyRAz%2B%2F%2Bj2FdfFy7fXTszvn1D5fD5ngTVGkBFunZSWNGUqiwIws%2FsRSMPl08tORvD1LlydyzhdS7z4ugESjz6xnugd4LWdYhuMm6bw9w22gh0VUm%2FmD4FhJQVUOTQv%2Fh3yk0Lg%2Fd9n7LXF%2BvOKUC9pkDLQRDVg9vPXqHLq4SwiRRaILIFgWI7DsIV1HfgIhJ%2BvrxDDshBodX%2FS5kfuMJmo6O%2BZGMspPmkWJuFq0SPWcghEw7wDXKKS8MFOExMDfu73vpkt%2Fpla7UvKqVBjhS5KF%2BGUhspSXf1b%2BkYyLpy5w4o1S8Bw8kpHIQqV88Kz0MI6Ah%2FvRdI8qGe57oIAsliR40IOPdH93skYcZF5Q3piyOFv34bng6ABLgpWUVxSTuIFmpVB%2BFRqOhdCj2%2BYuhV519OuCs46UbO%2BGMCmlJXeE114%2BLYZPJ9DEHlYBh6ged4pxbHPLwr2oE7MPo%2BCdXH%2F263CYG7CA11v%2FN%2BPlNpYKELeibuNBuN5uVv7kQaNKVAcOMTC1tZjNBjqkAZwKRKBVu40MxzMf%2FSvmr%2BlENp8v2HPn8y4ewrTyuWistgAb%2FCLuOTGHIIYCtZf3Cj3jnRdsd%2BbY7EXt%2FFEqpCRKrrCD%2BfZoYna5zd24kvmgzxnLiv89DyPA253aS3ffpxCEq2%2B%2FdfYwWxzmtPwLXdiEG2o5Pt1kotXS2vANr53OASP8jbtvsxzmcYNYCsj8jC6EY%2BNwzUxw2XxX2lWRGsTDqLL%2F&X-Amz-Signature=539c6709563e0f51ba9fe5713789571611eff1daf890c1273a1e9ffb08956055&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZCWIGLE%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ69LF6sL6Ae6ny5r85PJBzxslqEwx5iVb0QmfZc4H8gIhAJRSmnpnsg%2BA598egQTvBfB2%2FmMg8JcEun12rCids3mkKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsDVFfN9gApYlGtswq3AMDzBuLzFSjOzCdRsTn8kHytJ%2BI9fe4luf09efu2fvIbuNjNXWBdoEiIsKPyCye2YoY4Rcm89186vXVPivg64mo90WzrP4%2BiJmwhfEP4bj4AQdZCkA0WfFtYPyRAz%2B%2F%2Bj2FdfFy7fXTszvn1D5fD5ngTVGkBFunZSWNGUqiwIws%2FsRSMPl08tORvD1LlydyzhdS7z4ugESjz6xnugd4LWdYhuMm6bw9w22gh0VUm%2FmD4FhJQVUOTQv%2Fh3yk0Lg%2Fd9n7LXF%2BvOKUC9pkDLQRDVg9vPXqHLq4SwiRRaILIFgWI7DsIV1HfgIhJ%2BvrxDDshBodX%2FS5kfuMJmo6O%2BZGMspPmkWJuFq0SPWcghEw7wDXKKS8MFOExMDfu73vpkt%2Fpla7UvKqVBjhS5KF%2BGUhspSXf1b%2BkYyLpy5w4o1S8Bw8kpHIQqV88Kz0MI6Ah%2FvRdI8qGe57oIAsliR40IOPdH93skYcZF5Q3piyOFv34bng6ABLgpWUVxSTuIFmpVB%2BFRqOhdCj2%2BYuhV519OuCs46UbO%2BGMCmlJXeE114%2BLYZPJ9DEHlYBh6ged4pxbHPLwr2oE7MPo%2BCdXH%2F263CYG7CA11v%2FN%2BPlNpYKELeibuNBuN5uVv7kQaNKVAcOMTC1tZjNBjqkAZwKRKBVu40MxzMf%2FSvmr%2BlENp8v2HPn8y4ewrTyuWistgAb%2FCLuOTGHIIYCtZf3Cj3jnRdsd%2BbY7EXt%2FFEqpCRKrrCD%2BfZoYna5zd24kvmgzxnLiv89DyPA253aS3ffpxCEq2%2B%2FdfYwWxzmtPwLXdiEG2o5Pt1kotXS2vANr53OASP8jbtvsxzmcYNYCsj8jC6EY%2BNwzUxw2XxX2lWRGsTDqLL%2F&X-Amz-Signature=4f48539e15ef0d08c5b5cfc17d2e38b358cb67f0f74aaa8d62432be59eb8de7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZCWIGLE%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ69LF6sL6Ae6ny5r85PJBzxslqEwx5iVb0QmfZc4H8gIhAJRSmnpnsg%2BA598egQTvBfB2%2FmMg8JcEun12rCids3mkKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsDVFfN9gApYlGtswq3AMDzBuLzFSjOzCdRsTn8kHytJ%2BI9fe4luf09efu2fvIbuNjNXWBdoEiIsKPyCye2YoY4Rcm89186vXVPivg64mo90WzrP4%2BiJmwhfEP4bj4AQdZCkA0WfFtYPyRAz%2B%2F%2Bj2FdfFy7fXTszvn1D5fD5ngTVGkBFunZSWNGUqiwIws%2FsRSMPl08tORvD1LlydyzhdS7z4ugESjz6xnugd4LWdYhuMm6bw9w22gh0VUm%2FmD4FhJQVUOTQv%2Fh3yk0Lg%2Fd9n7LXF%2BvOKUC9pkDLQRDVg9vPXqHLq4SwiRRaILIFgWI7DsIV1HfgIhJ%2BvrxDDshBodX%2FS5kfuMJmo6O%2BZGMspPmkWJuFq0SPWcghEw7wDXKKS8MFOExMDfu73vpkt%2Fpla7UvKqVBjhS5KF%2BGUhspSXf1b%2BkYyLpy5w4o1S8Bw8kpHIQqV88Kz0MI6Ah%2FvRdI8qGe57oIAsliR40IOPdH93skYcZF5Q3piyOFv34bng6ABLgpWUVxSTuIFmpVB%2BFRqOhdCj2%2BYuhV519OuCs46UbO%2BGMCmlJXeE114%2BLYZPJ9DEHlYBh6ged4pxbHPLwr2oE7MPo%2BCdXH%2F263CYG7CA11v%2FN%2BPlNpYKELeibuNBuN5uVv7kQaNKVAcOMTC1tZjNBjqkAZwKRKBVu40MxzMf%2FSvmr%2BlENp8v2HPn8y4ewrTyuWistgAb%2FCLuOTGHIIYCtZf3Cj3jnRdsd%2BbY7EXt%2FFEqpCRKrrCD%2BfZoYna5zd24kvmgzxnLiv89DyPA253aS3ffpxCEq2%2B%2FdfYwWxzmtPwLXdiEG2o5Pt1kotXS2vANr53OASP8jbtvsxzmcYNYCsj8jC6EY%2BNwzUxw2XxX2lWRGsTDqLL%2F&X-Amz-Signature=e7cca75cf96d6aad381be9457926302f0324e97387d879421f1502f798ee4f3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZCWIGLE%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ69LF6sL6Ae6ny5r85PJBzxslqEwx5iVb0QmfZc4H8gIhAJRSmnpnsg%2BA598egQTvBfB2%2FmMg8JcEun12rCids3mkKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsDVFfN9gApYlGtswq3AMDzBuLzFSjOzCdRsTn8kHytJ%2BI9fe4luf09efu2fvIbuNjNXWBdoEiIsKPyCye2YoY4Rcm89186vXVPivg64mo90WzrP4%2BiJmwhfEP4bj4AQdZCkA0WfFtYPyRAz%2B%2F%2Bj2FdfFy7fXTszvn1D5fD5ngTVGkBFunZSWNGUqiwIws%2FsRSMPl08tORvD1LlydyzhdS7z4ugESjz6xnugd4LWdYhuMm6bw9w22gh0VUm%2FmD4FhJQVUOTQv%2Fh3yk0Lg%2Fd9n7LXF%2BvOKUC9pkDLQRDVg9vPXqHLq4SwiRRaILIFgWI7DsIV1HfgIhJ%2BvrxDDshBodX%2FS5kfuMJmo6O%2BZGMspPmkWJuFq0SPWcghEw7wDXKKS8MFOExMDfu73vpkt%2Fpla7UvKqVBjhS5KF%2BGUhspSXf1b%2BkYyLpy5w4o1S8Bw8kpHIQqV88Kz0MI6Ah%2FvRdI8qGe57oIAsliR40IOPdH93skYcZF5Q3piyOFv34bng6ABLgpWUVxSTuIFmpVB%2BFRqOhdCj2%2BYuhV519OuCs46UbO%2BGMCmlJXeE114%2BLYZPJ9DEHlYBh6ged4pxbHPLwr2oE7MPo%2BCdXH%2F263CYG7CA11v%2FN%2BPlNpYKELeibuNBuN5uVv7kQaNKVAcOMTC1tZjNBjqkAZwKRKBVu40MxzMf%2FSvmr%2BlENp8v2HPn8y4ewrTyuWistgAb%2FCLuOTGHIIYCtZf3Cj3jnRdsd%2BbY7EXt%2FFEqpCRKrrCD%2BfZoYna5zd24kvmgzxnLiv89DyPA253aS3ffpxCEq2%2B%2FdfYwWxzmtPwLXdiEG2o5Pt1kotXS2vANr53OASP8jbtvsxzmcYNYCsj8jC6EY%2BNwzUxw2XxX2lWRGsTDqLL%2F&X-Amz-Signature=81ddfc3a3d63a257d6e635aa054bb4af7f1341dce08b197c73e3aa2adef51ae3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZCWIGLE%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ69LF6sL6Ae6ny5r85PJBzxslqEwx5iVb0QmfZc4H8gIhAJRSmnpnsg%2BA598egQTvBfB2%2FmMg8JcEun12rCids3mkKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsDVFfN9gApYlGtswq3AMDzBuLzFSjOzCdRsTn8kHytJ%2BI9fe4luf09efu2fvIbuNjNXWBdoEiIsKPyCye2YoY4Rcm89186vXVPivg64mo90WzrP4%2BiJmwhfEP4bj4AQdZCkA0WfFtYPyRAz%2B%2F%2Bj2FdfFy7fXTszvn1D5fD5ngTVGkBFunZSWNGUqiwIws%2FsRSMPl08tORvD1LlydyzhdS7z4ugESjz6xnugd4LWdYhuMm6bw9w22gh0VUm%2FmD4FhJQVUOTQv%2Fh3yk0Lg%2Fd9n7LXF%2BvOKUC9pkDLQRDVg9vPXqHLq4SwiRRaILIFgWI7DsIV1HfgIhJ%2BvrxDDshBodX%2FS5kfuMJmo6O%2BZGMspPmkWJuFq0SPWcghEw7wDXKKS8MFOExMDfu73vpkt%2Fpla7UvKqVBjhS5KF%2BGUhspSXf1b%2BkYyLpy5w4o1S8Bw8kpHIQqV88Kz0MI6Ah%2FvRdI8qGe57oIAsliR40IOPdH93skYcZF5Q3piyOFv34bng6ABLgpWUVxSTuIFmpVB%2BFRqOhdCj2%2BYuhV519OuCs46UbO%2BGMCmlJXeE114%2BLYZPJ9DEHlYBh6ged4pxbHPLwr2oE7MPo%2BCdXH%2F263CYG7CA11v%2FN%2BPlNpYKELeibuNBuN5uVv7kQaNKVAcOMTC1tZjNBjqkAZwKRKBVu40MxzMf%2FSvmr%2BlENp8v2HPn8y4ewrTyuWistgAb%2FCLuOTGHIIYCtZf3Cj3jnRdsd%2BbY7EXt%2FFEqpCRKrrCD%2BfZoYna5zd24kvmgzxnLiv89DyPA253aS3ffpxCEq2%2B%2FdfYwWxzmtPwLXdiEG2o5Pt1kotXS2vANr53OASP8jbtvsxzmcYNYCsj8jC6EY%2BNwzUxw2XxX2lWRGsTDqLL%2F&X-Amz-Signature=986a35da1c975a3fa4c22fbcabc50a2de2c5a3a31fabfcc07f87310f9815add7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

