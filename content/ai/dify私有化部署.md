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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGAK2MEX%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCiYFLzQEVcVJgUehlUJ8JU%2FO8hT7gODbxNfr9fcynjcAIgFoCjSksddb8Bgw6YFinn7NlAoIgwMskpk6z9XNGG7loqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHe6ojufVbGn62JZCSrcA%2FKPDylvWjbTkZdZr98ffenUjiu1oWNjQdpZeqrCZ7pNH7PC8u4iIt2N1q1DCzKP27y9WUY9wi0Yw15uM6MJONgxIJXtWmeXwbTvmAEPXrY4JokpVsysJtfQx%2FslZtJn195zzAMCMZ5GqiB7XhiPn8NqdOVJ5uUmvmiUDt7dv5ROEPMFyH5t2J%2FuV94oqahpGDTfSp39IBl%2FBenJ%2BBy22K0gzg%2Fdd%2FsnV9RA%2FH2v2LNVpDpQOky4J%2BKJE%2BULgzkkpJ98RwKJVWW1SDmtPMHICMDGlriHHY6nc%2BGIuUAViET9emadcvIQHo6SCxf15Hpu3cKEGOLIVaKtzJ4VTGVuYN50qWHiUZuPK%2FKdtdVBLEvYRkk%2FsStY%2BSgslyL2Q1zt6EOfMaV4bz9%2BpIWnX6NMBL4QzAW1CAZjutsZUtQX7WVtO%2FNNQ41khA1kbCcuVczLBZVnJPl6gjnmxOlnSAJUNH89M%2FnBTngYdSSEzECePNYTxAQ4NlIBtTx8%2BsusG%2Br1MlZmh3Rj1Cg72go4bmH%2Feya6gwX7r3ivMf1kexZtt4Zm2%2FQd9gmfBmDwFZL3XuBu9EzMB8aPHI%2FlxVSwsLykWBscTSfo8ITe2iDOA8mw005rOalVdn9c9kOiVP6wMMb00c4GOqUBIaYOivWl6KZ8aizJuxDYDI3ws0FOdbSCojgTgl0dU0mDlyzgbVt%2Ftkddsr0lt0LrRiWRTPtbSO64Gk2CcQJap8rxOvI1GNaq7xGq4e%2FQuBDlOkrDJiDWhVcUtiZopUEaK4ViKn0Ucdo31oysdINa4sGFgRZk6wQXVYc1rBe7V2S1dkyUjYIUvA670cxAf7qzJq8lYO7%2FlMDWdexo1lHLiJQbAjTk&X-Amz-Signature=97a682c7c1b66f2853c12e6b3bf48a3d743d5ae5ac5a644dbbcfe4d924bcbb76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGAK2MEX%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCiYFLzQEVcVJgUehlUJ8JU%2FO8hT7gODbxNfr9fcynjcAIgFoCjSksddb8Bgw6YFinn7NlAoIgwMskpk6z9XNGG7loqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHe6ojufVbGn62JZCSrcA%2FKPDylvWjbTkZdZr98ffenUjiu1oWNjQdpZeqrCZ7pNH7PC8u4iIt2N1q1DCzKP27y9WUY9wi0Yw15uM6MJONgxIJXtWmeXwbTvmAEPXrY4JokpVsysJtfQx%2FslZtJn195zzAMCMZ5GqiB7XhiPn8NqdOVJ5uUmvmiUDt7dv5ROEPMFyH5t2J%2FuV94oqahpGDTfSp39IBl%2FBenJ%2BBy22K0gzg%2Fdd%2FsnV9RA%2FH2v2LNVpDpQOky4J%2BKJE%2BULgzkkpJ98RwKJVWW1SDmtPMHICMDGlriHHY6nc%2BGIuUAViET9emadcvIQHo6SCxf15Hpu3cKEGOLIVaKtzJ4VTGVuYN50qWHiUZuPK%2FKdtdVBLEvYRkk%2FsStY%2BSgslyL2Q1zt6EOfMaV4bz9%2BpIWnX6NMBL4QzAW1CAZjutsZUtQX7WVtO%2FNNQ41khA1kbCcuVczLBZVnJPl6gjnmxOlnSAJUNH89M%2FnBTngYdSSEzECePNYTxAQ4NlIBtTx8%2BsusG%2Br1MlZmh3Rj1Cg72go4bmH%2Feya6gwX7r3ivMf1kexZtt4Zm2%2FQd9gmfBmDwFZL3XuBu9EzMB8aPHI%2FlxVSwsLykWBscTSfo8ITe2iDOA8mw005rOalVdn9c9kOiVP6wMMb00c4GOqUBIaYOivWl6KZ8aizJuxDYDI3ws0FOdbSCojgTgl0dU0mDlyzgbVt%2Ftkddsr0lt0LrRiWRTPtbSO64Gk2CcQJap8rxOvI1GNaq7xGq4e%2FQuBDlOkrDJiDWhVcUtiZopUEaK4ViKn0Ucdo31oysdINa4sGFgRZk6wQXVYc1rBe7V2S1dkyUjYIUvA670cxAf7qzJq8lYO7%2FlMDWdexo1lHLiJQbAjTk&X-Amz-Signature=d3106a5457811d0be1f9dcfe158ca59c9fe0c68964a93f0308002998d2c630c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGAK2MEX%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCiYFLzQEVcVJgUehlUJ8JU%2FO8hT7gODbxNfr9fcynjcAIgFoCjSksddb8Bgw6YFinn7NlAoIgwMskpk6z9XNGG7loqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHe6ojufVbGn62JZCSrcA%2FKPDylvWjbTkZdZr98ffenUjiu1oWNjQdpZeqrCZ7pNH7PC8u4iIt2N1q1DCzKP27y9WUY9wi0Yw15uM6MJONgxIJXtWmeXwbTvmAEPXrY4JokpVsysJtfQx%2FslZtJn195zzAMCMZ5GqiB7XhiPn8NqdOVJ5uUmvmiUDt7dv5ROEPMFyH5t2J%2FuV94oqahpGDTfSp39IBl%2FBenJ%2BBy22K0gzg%2Fdd%2FsnV9RA%2FH2v2LNVpDpQOky4J%2BKJE%2BULgzkkpJ98RwKJVWW1SDmtPMHICMDGlriHHY6nc%2BGIuUAViET9emadcvIQHo6SCxf15Hpu3cKEGOLIVaKtzJ4VTGVuYN50qWHiUZuPK%2FKdtdVBLEvYRkk%2FsStY%2BSgslyL2Q1zt6EOfMaV4bz9%2BpIWnX6NMBL4QzAW1CAZjutsZUtQX7WVtO%2FNNQ41khA1kbCcuVczLBZVnJPl6gjnmxOlnSAJUNH89M%2FnBTngYdSSEzECePNYTxAQ4NlIBtTx8%2BsusG%2Br1MlZmh3Rj1Cg72go4bmH%2Feya6gwX7r3ivMf1kexZtt4Zm2%2FQd9gmfBmDwFZL3XuBu9EzMB8aPHI%2FlxVSwsLykWBscTSfo8ITe2iDOA8mw005rOalVdn9c9kOiVP6wMMb00c4GOqUBIaYOivWl6KZ8aizJuxDYDI3ws0FOdbSCojgTgl0dU0mDlyzgbVt%2Ftkddsr0lt0LrRiWRTPtbSO64Gk2CcQJap8rxOvI1GNaq7xGq4e%2FQuBDlOkrDJiDWhVcUtiZopUEaK4ViKn0Ucdo31oysdINa4sGFgRZk6wQXVYc1rBe7V2S1dkyUjYIUvA670cxAf7qzJq8lYO7%2FlMDWdexo1lHLiJQbAjTk&X-Amz-Signature=f341246660b21f5b5942eb29a78e688a68d79b5d5f3516f9d7e09feb62686293&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGAK2MEX%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCiYFLzQEVcVJgUehlUJ8JU%2FO8hT7gODbxNfr9fcynjcAIgFoCjSksddb8Bgw6YFinn7NlAoIgwMskpk6z9XNGG7loqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHe6ojufVbGn62JZCSrcA%2FKPDylvWjbTkZdZr98ffenUjiu1oWNjQdpZeqrCZ7pNH7PC8u4iIt2N1q1DCzKP27y9WUY9wi0Yw15uM6MJONgxIJXtWmeXwbTvmAEPXrY4JokpVsysJtfQx%2FslZtJn195zzAMCMZ5GqiB7XhiPn8NqdOVJ5uUmvmiUDt7dv5ROEPMFyH5t2J%2FuV94oqahpGDTfSp39IBl%2FBenJ%2BBy22K0gzg%2Fdd%2FsnV9RA%2FH2v2LNVpDpQOky4J%2BKJE%2BULgzkkpJ98RwKJVWW1SDmtPMHICMDGlriHHY6nc%2BGIuUAViET9emadcvIQHo6SCxf15Hpu3cKEGOLIVaKtzJ4VTGVuYN50qWHiUZuPK%2FKdtdVBLEvYRkk%2FsStY%2BSgslyL2Q1zt6EOfMaV4bz9%2BpIWnX6NMBL4QzAW1CAZjutsZUtQX7WVtO%2FNNQ41khA1kbCcuVczLBZVnJPl6gjnmxOlnSAJUNH89M%2FnBTngYdSSEzECePNYTxAQ4NlIBtTx8%2BsusG%2Br1MlZmh3Rj1Cg72go4bmH%2Feya6gwX7r3ivMf1kexZtt4Zm2%2FQd9gmfBmDwFZL3XuBu9EzMB8aPHI%2FlxVSwsLykWBscTSfo8ITe2iDOA8mw005rOalVdn9c9kOiVP6wMMb00c4GOqUBIaYOivWl6KZ8aizJuxDYDI3ws0FOdbSCojgTgl0dU0mDlyzgbVt%2Ftkddsr0lt0LrRiWRTPtbSO64Gk2CcQJap8rxOvI1GNaq7xGq4e%2FQuBDlOkrDJiDWhVcUtiZopUEaK4ViKn0Ucdo31oysdINa4sGFgRZk6wQXVYc1rBe7V2S1dkyUjYIUvA670cxAf7qzJq8lYO7%2FlMDWdexo1lHLiJQbAjTk&X-Amz-Signature=ee0cf48c162c8b6538d708e6da3e10c75171715348560b79c7921626249a4756&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGAK2MEX%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCiYFLzQEVcVJgUehlUJ8JU%2FO8hT7gODbxNfr9fcynjcAIgFoCjSksddb8Bgw6YFinn7NlAoIgwMskpk6z9XNGG7loqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHe6ojufVbGn62JZCSrcA%2FKPDylvWjbTkZdZr98ffenUjiu1oWNjQdpZeqrCZ7pNH7PC8u4iIt2N1q1DCzKP27y9WUY9wi0Yw15uM6MJONgxIJXtWmeXwbTvmAEPXrY4JokpVsysJtfQx%2FslZtJn195zzAMCMZ5GqiB7XhiPn8NqdOVJ5uUmvmiUDt7dv5ROEPMFyH5t2J%2FuV94oqahpGDTfSp39IBl%2FBenJ%2BBy22K0gzg%2Fdd%2FsnV9RA%2FH2v2LNVpDpQOky4J%2BKJE%2BULgzkkpJ98RwKJVWW1SDmtPMHICMDGlriHHY6nc%2BGIuUAViET9emadcvIQHo6SCxf15Hpu3cKEGOLIVaKtzJ4VTGVuYN50qWHiUZuPK%2FKdtdVBLEvYRkk%2FsStY%2BSgslyL2Q1zt6EOfMaV4bz9%2BpIWnX6NMBL4QzAW1CAZjutsZUtQX7WVtO%2FNNQ41khA1kbCcuVczLBZVnJPl6gjnmxOlnSAJUNH89M%2FnBTngYdSSEzECePNYTxAQ4NlIBtTx8%2BsusG%2Br1MlZmh3Rj1Cg72go4bmH%2Feya6gwX7r3ivMf1kexZtt4Zm2%2FQd9gmfBmDwFZL3XuBu9EzMB8aPHI%2FlxVSwsLykWBscTSfo8ITe2iDOA8mw005rOalVdn9c9kOiVP6wMMb00c4GOqUBIaYOivWl6KZ8aizJuxDYDI3ws0FOdbSCojgTgl0dU0mDlyzgbVt%2Ftkddsr0lt0LrRiWRTPtbSO64Gk2CcQJap8rxOvI1GNaq7xGq4e%2FQuBDlOkrDJiDWhVcUtiZopUEaK4ViKn0Ucdo31oysdINa4sGFgRZk6wQXVYc1rBe7V2S1dkyUjYIUvA670cxAf7qzJq8lYO7%2FlMDWdexo1lHLiJQbAjTk&X-Amz-Signature=dd22ed29eea4f091ab13b0ea2a1fd739a7f82ffedc2ececc10cc52aa8a6d6b11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGAK2MEX%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCiYFLzQEVcVJgUehlUJ8JU%2FO8hT7gODbxNfr9fcynjcAIgFoCjSksddb8Bgw6YFinn7NlAoIgwMskpk6z9XNGG7loqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHe6ojufVbGn62JZCSrcA%2FKPDylvWjbTkZdZr98ffenUjiu1oWNjQdpZeqrCZ7pNH7PC8u4iIt2N1q1DCzKP27y9WUY9wi0Yw15uM6MJONgxIJXtWmeXwbTvmAEPXrY4JokpVsysJtfQx%2FslZtJn195zzAMCMZ5GqiB7XhiPn8NqdOVJ5uUmvmiUDt7dv5ROEPMFyH5t2J%2FuV94oqahpGDTfSp39IBl%2FBenJ%2BBy22K0gzg%2Fdd%2FsnV9RA%2FH2v2LNVpDpQOky4J%2BKJE%2BULgzkkpJ98RwKJVWW1SDmtPMHICMDGlriHHY6nc%2BGIuUAViET9emadcvIQHo6SCxf15Hpu3cKEGOLIVaKtzJ4VTGVuYN50qWHiUZuPK%2FKdtdVBLEvYRkk%2FsStY%2BSgslyL2Q1zt6EOfMaV4bz9%2BpIWnX6NMBL4QzAW1CAZjutsZUtQX7WVtO%2FNNQ41khA1kbCcuVczLBZVnJPl6gjnmxOlnSAJUNH89M%2FnBTngYdSSEzECePNYTxAQ4NlIBtTx8%2BsusG%2Br1MlZmh3Rj1Cg72go4bmH%2Feya6gwX7r3ivMf1kexZtt4Zm2%2FQd9gmfBmDwFZL3XuBu9EzMB8aPHI%2FlxVSwsLykWBscTSfo8ITe2iDOA8mw005rOalVdn9c9kOiVP6wMMb00c4GOqUBIaYOivWl6KZ8aizJuxDYDI3ws0FOdbSCojgTgl0dU0mDlyzgbVt%2Ftkddsr0lt0LrRiWRTPtbSO64Gk2CcQJap8rxOvI1GNaq7xGq4e%2FQuBDlOkrDJiDWhVcUtiZopUEaK4ViKn0Ucdo31oysdINa4sGFgRZk6wQXVYc1rBe7V2S1dkyUjYIUvA670cxAf7qzJq8lYO7%2FlMDWdexo1lHLiJQbAjTk&X-Amz-Signature=396d4389c370996f983b4b94b07582e5c425fc6f3c49a2e43cf407044c2cab24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGAK2MEX%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCiYFLzQEVcVJgUehlUJ8JU%2FO8hT7gODbxNfr9fcynjcAIgFoCjSksddb8Bgw6YFinn7NlAoIgwMskpk6z9XNGG7loqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHe6ojufVbGn62JZCSrcA%2FKPDylvWjbTkZdZr98ffenUjiu1oWNjQdpZeqrCZ7pNH7PC8u4iIt2N1q1DCzKP27y9WUY9wi0Yw15uM6MJONgxIJXtWmeXwbTvmAEPXrY4JokpVsysJtfQx%2FslZtJn195zzAMCMZ5GqiB7XhiPn8NqdOVJ5uUmvmiUDt7dv5ROEPMFyH5t2J%2FuV94oqahpGDTfSp39IBl%2FBenJ%2BBy22K0gzg%2Fdd%2FsnV9RA%2FH2v2LNVpDpQOky4J%2BKJE%2BULgzkkpJ98RwKJVWW1SDmtPMHICMDGlriHHY6nc%2BGIuUAViET9emadcvIQHo6SCxf15Hpu3cKEGOLIVaKtzJ4VTGVuYN50qWHiUZuPK%2FKdtdVBLEvYRkk%2FsStY%2BSgslyL2Q1zt6EOfMaV4bz9%2BpIWnX6NMBL4QzAW1CAZjutsZUtQX7WVtO%2FNNQ41khA1kbCcuVczLBZVnJPl6gjnmxOlnSAJUNH89M%2FnBTngYdSSEzECePNYTxAQ4NlIBtTx8%2BsusG%2Br1MlZmh3Rj1Cg72go4bmH%2Feya6gwX7r3ivMf1kexZtt4Zm2%2FQd9gmfBmDwFZL3XuBu9EzMB8aPHI%2FlxVSwsLykWBscTSfo8ITe2iDOA8mw005rOalVdn9c9kOiVP6wMMb00c4GOqUBIaYOivWl6KZ8aizJuxDYDI3ws0FOdbSCojgTgl0dU0mDlyzgbVt%2Ftkddsr0lt0LrRiWRTPtbSO64Gk2CcQJap8rxOvI1GNaq7xGq4e%2FQuBDlOkrDJiDWhVcUtiZopUEaK4ViKn0Ucdo31oysdINa4sGFgRZk6wQXVYc1rBe7V2S1dkyUjYIUvA670cxAf7qzJq8lYO7%2FlMDWdexo1lHLiJQbAjTk&X-Amz-Signature=0de3bd958a592a7dbabef42528c53d8ca198fe6d411d937ed8e5fbf263a5d327&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGAK2MEX%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCiYFLzQEVcVJgUehlUJ8JU%2FO8hT7gODbxNfr9fcynjcAIgFoCjSksddb8Bgw6YFinn7NlAoIgwMskpk6z9XNGG7loqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHe6ojufVbGn62JZCSrcA%2FKPDylvWjbTkZdZr98ffenUjiu1oWNjQdpZeqrCZ7pNH7PC8u4iIt2N1q1DCzKP27y9WUY9wi0Yw15uM6MJONgxIJXtWmeXwbTvmAEPXrY4JokpVsysJtfQx%2FslZtJn195zzAMCMZ5GqiB7XhiPn8NqdOVJ5uUmvmiUDt7dv5ROEPMFyH5t2J%2FuV94oqahpGDTfSp39IBl%2FBenJ%2BBy22K0gzg%2Fdd%2FsnV9RA%2FH2v2LNVpDpQOky4J%2BKJE%2BULgzkkpJ98RwKJVWW1SDmtPMHICMDGlriHHY6nc%2BGIuUAViET9emadcvIQHo6SCxf15Hpu3cKEGOLIVaKtzJ4VTGVuYN50qWHiUZuPK%2FKdtdVBLEvYRkk%2FsStY%2BSgslyL2Q1zt6EOfMaV4bz9%2BpIWnX6NMBL4QzAW1CAZjutsZUtQX7WVtO%2FNNQ41khA1kbCcuVczLBZVnJPl6gjnmxOlnSAJUNH89M%2FnBTngYdSSEzECePNYTxAQ4NlIBtTx8%2BsusG%2Br1MlZmh3Rj1Cg72go4bmH%2Feya6gwX7r3ivMf1kexZtt4Zm2%2FQd9gmfBmDwFZL3XuBu9EzMB8aPHI%2FlxVSwsLykWBscTSfo8ITe2iDOA8mw005rOalVdn9c9kOiVP6wMMb00c4GOqUBIaYOivWl6KZ8aizJuxDYDI3ws0FOdbSCojgTgl0dU0mDlyzgbVt%2Ftkddsr0lt0LrRiWRTPtbSO64Gk2CcQJap8rxOvI1GNaq7xGq4e%2FQuBDlOkrDJiDWhVcUtiZopUEaK4ViKn0Ucdo31oysdINa4sGFgRZk6wQXVYc1rBe7V2S1dkyUjYIUvA670cxAf7qzJq8lYO7%2FlMDWdexo1lHLiJQbAjTk&X-Amz-Signature=5f3586fc6b99cb9ad6bc2112749058f9b6d7c3476840c7279c391d8b9f497cbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGAK2MEX%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCiYFLzQEVcVJgUehlUJ8JU%2FO8hT7gODbxNfr9fcynjcAIgFoCjSksddb8Bgw6YFinn7NlAoIgwMskpk6z9XNGG7loqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHe6ojufVbGn62JZCSrcA%2FKPDylvWjbTkZdZr98ffenUjiu1oWNjQdpZeqrCZ7pNH7PC8u4iIt2N1q1DCzKP27y9WUY9wi0Yw15uM6MJONgxIJXtWmeXwbTvmAEPXrY4JokpVsysJtfQx%2FslZtJn195zzAMCMZ5GqiB7XhiPn8NqdOVJ5uUmvmiUDt7dv5ROEPMFyH5t2J%2FuV94oqahpGDTfSp39IBl%2FBenJ%2BBy22K0gzg%2Fdd%2FsnV9RA%2FH2v2LNVpDpQOky4J%2BKJE%2BULgzkkpJ98RwKJVWW1SDmtPMHICMDGlriHHY6nc%2BGIuUAViET9emadcvIQHo6SCxf15Hpu3cKEGOLIVaKtzJ4VTGVuYN50qWHiUZuPK%2FKdtdVBLEvYRkk%2FsStY%2BSgslyL2Q1zt6EOfMaV4bz9%2BpIWnX6NMBL4QzAW1CAZjutsZUtQX7WVtO%2FNNQ41khA1kbCcuVczLBZVnJPl6gjnmxOlnSAJUNH89M%2FnBTngYdSSEzECePNYTxAQ4NlIBtTx8%2BsusG%2Br1MlZmh3Rj1Cg72go4bmH%2Feya6gwX7r3ivMf1kexZtt4Zm2%2FQd9gmfBmDwFZL3XuBu9EzMB8aPHI%2FlxVSwsLykWBscTSfo8ITe2iDOA8mw005rOalVdn9c9kOiVP6wMMb00c4GOqUBIaYOivWl6KZ8aizJuxDYDI3ws0FOdbSCojgTgl0dU0mDlyzgbVt%2Ftkddsr0lt0LrRiWRTPtbSO64Gk2CcQJap8rxOvI1GNaq7xGq4e%2FQuBDlOkrDJiDWhVcUtiZopUEaK4ViKn0Ucdo31oysdINa4sGFgRZk6wQXVYc1rBe7V2S1dkyUjYIUvA670cxAf7qzJq8lYO7%2FlMDWdexo1lHLiJQbAjTk&X-Amz-Signature=7d6b16c9a7741ae44c4a5317924e900f09c59cac65412c7dc3dc657b40b46aec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGAK2MEX%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCiYFLzQEVcVJgUehlUJ8JU%2FO8hT7gODbxNfr9fcynjcAIgFoCjSksddb8Bgw6YFinn7NlAoIgwMskpk6z9XNGG7loqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHe6ojufVbGn62JZCSrcA%2FKPDylvWjbTkZdZr98ffenUjiu1oWNjQdpZeqrCZ7pNH7PC8u4iIt2N1q1DCzKP27y9WUY9wi0Yw15uM6MJONgxIJXtWmeXwbTvmAEPXrY4JokpVsysJtfQx%2FslZtJn195zzAMCMZ5GqiB7XhiPn8NqdOVJ5uUmvmiUDt7dv5ROEPMFyH5t2J%2FuV94oqahpGDTfSp39IBl%2FBenJ%2BBy22K0gzg%2Fdd%2FsnV9RA%2FH2v2LNVpDpQOky4J%2BKJE%2BULgzkkpJ98RwKJVWW1SDmtPMHICMDGlriHHY6nc%2BGIuUAViET9emadcvIQHo6SCxf15Hpu3cKEGOLIVaKtzJ4VTGVuYN50qWHiUZuPK%2FKdtdVBLEvYRkk%2FsStY%2BSgslyL2Q1zt6EOfMaV4bz9%2BpIWnX6NMBL4QzAW1CAZjutsZUtQX7WVtO%2FNNQ41khA1kbCcuVczLBZVnJPl6gjnmxOlnSAJUNH89M%2FnBTngYdSSEzECePNYTxAQ4NlIBtTx8%2BsusG%2Br1MlZmh3Rj1Cg72go4bmH%2Feya6gwX7r3ivMf1kexZtt4Zm2%2FQd9gmfBmDwFZL3XuBu9EzMB8aPHI%2FlxVSwsLykWBscTSfo8ITe2iDOA8mw005rOalVdn9c9kOiVP6wMMb00c4GOqUBIaYOivWl6KZ8aizJuxDYDI3ws0FOdbSCojgTgl0dU0mDlyzgbVt%2Ftkddsr0lt0LrRiWRTPtbSO64Gk2CcQJap8rxOvI1GNaq7xGq4e%2FQuBDlOkrDJiDWhVcUtiZopUEaK4ViKn0Ucdo31oysdINa4sGFgRZk6wQXVYc1rBe7V2S1dkyUjYIUvA670cxAf7qzJq8lYO7%2FlMDWdexo1lHLiJQbAjTk&X-Amz-Signature=d96882f8f4af3600187b999491e96f74e505fad532b183e553c6536356ba2c65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

