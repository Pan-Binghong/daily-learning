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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI6CBTQB%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCTCd3qolaXwMK6REmsq2gSI2aU%2FCchAdQ9q9Y%2Bc%2FIHdwIgG9Zr%2FwD%2FfTVrXmbmQKGP7Na2aI0TE%2BoF7zHfhWt7YU4qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb4aJLPFqaw6BGp6CrcAy4MnvGRFnupl0wqxsW7utThHZycC8E7jd6gpKZKLImGAQuDiF1PcKeWc47oa7QpZ4ikF%2FLAeZFI%2FJCcsEWtnnA%2BVoRlLUhchuWKDacYfZL12uZpcjYB2y8PvEA8RSrwROrYUB2QOf770oXWx158E6ctHjwd8pBgmo8V374IlgLD9dG38az82fR9cYIJd0zHUJeDIXr5WUafYCgKWqZJpxy8RawWX2%2BgyIrivSPlLmuVSgg9Z2dfejHgVWUV%2FPNUrIvWY86yE3j0ntf1Eakzw302X1P9i6HYXms7G4n4PnJR2FiFh7H%2ByHQ9hkMNk%2FUKWXQWj369QGbV%2FmDLH%2FUGt0PofW3fuZdM3627WzyWg1e6JPhUpNxU7WPRJHh8y5%2FGAm4m1Al%2BnLBlC5hb%2FWsvNvGLQAhXpFUfAPiP6k0EwXuPCE1sG%2F1SojIhKp7x6bK%2FQciTXZBfZRR6Yf8JYnB4IkfpdO%2B1dk0Ey%2BI2Gm524eKyCy%2BhFPojNaqScJ24xABimY0Iip0%2BAQyMDU5XIhjBpiQSgZXEZmnDtY50QtEJuqXs6fW0nFQ2uZSqiwugxa3nYh4ApseHmuYAFR%2FuHYQZ7RAuk9w5mRHqCwtNzPGuY1gnx3ICvhPktfcHP83UMOeg18oGOqUB281A4Ok0byZ2BdwXlwgLQ0g7pPcZWt2%2Fm58cZfJbM7z%2FV1idBK8CHWXGI6ulzNhky4opN5AkMSNT6KJCSksonVp8lRGfTpUIsG0VRdlT1fT90s8gywaR9sHFDrWcWlpylAocsENiSnICv7OOMqRsXSbpFVQQ4cY7bUQx7mZC2E2AfVWti4VhvRHcSke8HB%2Fa2oSeBpDkmQKq%2BQMhE5vnGzbCJSmx&X-Amz-Signature=ba80a2307eef7a044db821786a09ae96c4013a7a6fdbeef846a61883dfb83c94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI6CBTQB%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCTCd3qolaXwMK6REmsq2gSI2aU%2FCchAdQ9q9Y%2Bc%2FIHdwIgG9Zr%2FwD%2FfTVrXmbmQKGP7Na2aI0TE%2BoF7zHfhWt7YU4qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb4aJLPFqaw6BGp6CrcAy4MnvGRFnupl0wqxsW7utThHZycC8E7jd6gpKZKLImGAQuDiF1PcKeWc47oa7QpZ4ikF%2FLAeZFI%2FJCcsEWtnnA%2BVoRlLUhchuWKDacYfZL12uZpcjYB2y8PvEA8RSrwROrYUB2QOf770oXWx158E6ctHjwd8pBgmo8V374IlgLD9dG38az82fR9cYIJd0zHUJeDIXr5WUafYCgKWqZJpxy8RawWX2%2BgyIrivSPlLmuVSgg9Z2dfejHgVWUV%2FPNUrIvWY86yE3j0ntf1Eakzw302X1P9i6HYXms7G4n4PnJR2FiFh7H%2ByHQ9hkMNk%2FUKWXQWj369QGbV%2FmDLH%2FUGt0PofW3fuZdM3627WzyWg1e6JPhUpNxU7WPRJHh8y5%2FGAm4m1Al%2BnLBlC5hb%2FWsvNvGLQAhXpFUfAPiP6k0EwXuPCE1sG%2F1SojIhKp7x6bK%2FQciTXZBfZRR6Yf8JYnB4IkfpdO%2B1dk0Ey%2BI2Gm524eKyCy%2BhFPojNaqScJ24xABimY0Iip0%2BAQyMDU5XIhjBpiQSgZXEZmnDtY50QtEJuqXs6fW0nFQ2uZSqiwugxa3nYh4ApseHmuYAFR%2FuHYQZ7RAuk9w5mRHqCwtNzPGuY1gnx3ICvhPktfcHP83UMOeg18oGOqUB281A4Ok0byZ2BdwXlwgLQ0g7pPcZWt2%2Fm58cZfJbM7z%2FV1idBK8CHWXGI6ulzNhky4opN5AkMSNT6KJCSksonVp8lRGfTpUIsG0VRdlT1fT90s8gywaR9sHFDrWcWlpylAocsENiSnICv7OOMqRsXSbpFVQQ4cY7bUQx7mZC2E2AfVWti4VhvRHcSke8HB%2Fa2oSeBpDkmQKq%2BQMhE5vnGzbCJSmx&X-Amz-Signature=63ece424ff5ce416d5e9b15c71cf38b82b89acf883b857b497094a383cd456b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI6CBTQB%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCTCd3qolaXwMK6REmsq2gSI2aU%2FCchAdQ9q9Y%2Bc%2FIHdwIgG9Zr%2FwD%2FfTVrXmbmQKGP7Na2aI0TE%2BoF7zHfhWt7YU4qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb4aJLPFqaw6BGp6CrcAy4MnvGRFnupl0wqxsW7utThHZycC8E7jd6gpKZKLImGAQuDiF1PcKeWc47oa7QpZ4ikF%2FLAeZFI%2FJCcsEWtnnA%2BVoRlLUhchuWKDacYfZL12uZpcjYB2y8PvEA8RSrwROrYUB2QOf770oXWx158E6ctHjwd8pBgmo8V374IlgLD9dG38az82fR9cYIJd0zHUJeDIXr5WUafYCgKWqZJpxy8RawWX2%2BgyIrivSPlLmuVSgg9Z2dfejHgVWUV%2FPNUrIvWY86yE3j0ntf1Eakzw302X1P9i6HYXms7G4n4PnJR2FiFh7H%2ByHQ9hkMNk%2FUKWXQWj369QGbV%2FmDLH%2FUGt0PofW3fuZdM3627WzyWg1e6JPhUpNxU7WPRJHh8y5%2FGAm4m1Al%2BnLBlC5hb%2FWsvNvGLQAhXpFUfAPiP6k0EwXuPCE1sG%2F1SojIhKp7x6bK%2FQciTXZBfZRR6Yf8JYnB4IkfpdO%2B1dk0Ey%2BI2Gm524eKyCy%2BhFPojNaqScJ24xABimY0Iip0%2BAQyMDU5XIhjBpiQSgZXEZmnDtY50QtEJuqXs6fW0nFQ2uZSqiwugxa3nYh4ApseHmuYAFR%2FuHYQZ7RAuk9w5mRHqCwtNzPGuY1gnx3ICvhPktfcHP83UMOeg18oGOqUB281A4Ok0byZ2BdwXlwgLQ0g7pPcZWt2%2Fm58cZfJbM7z%2FV1idBK8CHWXGI6ulzNhky4opN5AkMSNT6KJCSksonVp8lRGfTpUIsG0VRdlT1fT90s8gywaR9sHFDrWcWlpylAocsENiSnICv7OOMqRsXSbpFVQQ4cY7bUQx7mZC2E2AfVWti4VhvRHcSke8HB%2Fa2oSeBpDkmQKq%2BQMhE5vnGzbCJSmx&X-Amz-Signature=9db059f88d56c0f1f6c43d4b8f71072d5b4a8476844a0c2dc778d3a6c19ab58a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI6CBTQB%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCTCd3qolaXwMK6REmsq2gSI2aU%2FCchAdQ9q9Y%2Bc%2FIHdwIgG9Zr%2FwD%2FfTVrXmbmQKGP7Na2aI0TE%2BoF7zHfhWt7YU4qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb4aJLPFqaw6BGp6CrcAy4MnvGRFnupl0wqxsW7utThHZycC8E7jd6gpKZKLImGAQuDiF1PcKeWc47oa7QpZ4ikF%2FLAeZFI%2FJCcsEWtnnA%2BVoRlLUhchuWKDacYfZL12uZpcjYB2y8PvEA8RSrwROrYUB2QOf770oXWx158E6ctHjwd8pBgmo8V374IlgLD9dG38az82fR9cYIJd0zHUJeDIXr5WUafYCgKWqZJpxy8RawWX2%2BgyIrivSPlLmuVSgg9Z2dfejHgVWUV%2FPNUrIvWY86yE3j0ntf1Eakzw302X1P9i6HYXms7G4n4PnJR2FiFh7H%2ByHQ9hkMNk%2FUKWXQWj369QGbV%2FmDLH%2FUGt0PofW3fuZdM3627WzyWg1e6JPhUpNxU7WPRJHh8y5%2FGAm4m1Al%2BnLBlC5hb%2FWsvNvGLQAhXpFUfAPiP6k0EwXuPCE1sG%2F1SojIhKp7x6bK%2FQciTXZBfZRR6Yf8JYnB4IkfpdO%2B1dk0Ey%2BI2Gm524eKyCy%2BhFPojNaqScJ24xABimY0Iip0%2BAQyMDU5XIhjBpiQSgZXEZmnDtY50QtEJuqXs6fW0nFQ2uZSqiwugxa3nYh4ApseHmuYAFR%2FuHYQZ7RAuk9w5mRHqCwtNzPGuY1gnx3ICvhPktfcHP83UMOeg18oGOqUB281A4Ok0byZ2BdwXlwgLQ0g7pPcZWt2%2Fm58cZfJbM7z%2FV1idBK8CHWXGI6ulzNhky4opN5AkMSNT6KJCSksonVp8lRGfTpUIsG0VRdlT1fT90s8gywaR9sHFDrWcWlpylAocsENiSnICv7OOMqRsXSbpFVQQ4cY7bUQx7mZC2E2AfVWti4VhvRHcSke8HB%2Fa2oSeBpDkmQKq%2BQMhE5vnGzbCJSmx&X-Amz-Signature=ee61904b0bae02c83fd0402489bd2e3fe4c90f5ac35de4ddfec37d5768fdf664&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI6CBTQB%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCTCd3qolaXwMK6REmsq2gSI2aU%2FCchAdQ9q9Y%2Bc%2FIHdwIgG9Zr%2FwD%2FfTVrXmbmQKGP7Na2aI0TE%2BoF7zHfhWt7YU4qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb4aJLPFqaw6BGp6CrcAy4MnvGRFnupl0wqxsW7utThHZycC8E7jd6gpKZKLImGAQuDiF1PcKeWc47oa7QpZ4ikF%2FLAeZFI%2FJCcsEWtnnA%2BVoRlLUhchuWKDacYfZL12uZpcjYB2y8PvEA8RSrwROrYUB2QOf770oXWx158E6ctHjwd8pBgmo8V374IlgLD9dG38az82fR9cYIJd0zHUJeDIXr5WUafYCgKWqZJpxy8RawWX2%2BgyIrivSPlLmuVSgg9Z2dfejHgVWUV%2FPNUrIvWY86yE3j0ntf1Eakzw302X1P9i6HYXms7G4n4PnJR2FiFh7H%2ByHQ9hkMNk%2FUKWXQWj369QGbV%2FmDLH%2FUGt0PofW3fuZdM3627WzyWg1e6JPhUpNxU7WPRJHh8y5%2FGAm4m1Al%2BnLBlC5hb%2FWsvNvGLQAhXpFUfAPiP6k0EwXuPCE1sG%2F1SojIhKp7x6bK%2FQciTXZBfZRR6Yf8JYnB4IkfpdO%2B1dk0Ey%2BI2Gm524eKyCy%2BhFPojNaqScJ24xABimY0Iip0%2BAQyMDU5XIhjBpiQSgZXEZmnDtY50QtEJuqXs6fW0nFQ2uZSqiwugxa3nYh4ApseHmuYAFR%2FuHYQZ7RAuk9w5mRHqCwtNzPGuY1gnx3ICvhPktfcHP83UMOeg18oGOqUB281A4Ok0byZ2BdwXlwgLQ0g7pPcZWt2%2Fm58cZfJbM7z%2FV1idBK8CHWXGI6ulzNhky4opN5AkMSNT6KJCSksonVp8lRGfTpUIsG0VRdlT1fT90s8gywaR9sHFDrWcWlpylAocsENiSnICv7OOMqRsXSbpFVQQ4cY7bUQx7mZC2E2AfVWti4VhvRHcSke8HB%2Fa2oSeBpDkmQKq%2BQMhE5vnGzbCJSmx&X-Amz-Signature=63c656e67a5785d737533013b039d657b3f473dfb8299de6f0f86053f921dc85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI6CBTQB%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCTCd3qolaXwMK6REmsq2gSI2aU%2FCchAdQ9q9Y%2Bc%2FIHdwIgG9Zr%2FwD%2FfTVrXmbmQKGP7Na2aI0TE%2BoF7zHfhWt7YU4qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb4aJLPFqaw6BGp6CrcAy4MnvGRFnupl0wqxsW7utThHZycC8E7jd6gpKZKLImGAQuDiF1PcKeWc47oa7QpZ4ikF%2FLAeZFI%2FJCcsEWtnnA%2BVoRlLUhchuWKDacYfZL12uZpcjYB2y8PvEA8RSrwROrYUB2QOf770oXWx158E6ctHjwd8pBgmo8V374IlgLD9dG38az82fR9cYIJd0zHUJeDIXr5WUafYCgKWqZJpxy8RawWX2%2BgyIrivSPlLmuVSgg9Z2dfejHgVWUV%2FPNUrIvWY86yE3j0ntf1Eakzw302X1P9i6HYXms7G4n4PnJR2FiFh7H%2ByHQ9hkMNk%2FUKWXQWj369QGbV%2FmDLH%2FUGt0PofW3fuZdM3627WzyWg1e6JPhUpNxU7WPRJHh8y5%2FGAm4m1Al%2BnLBlC5hb%2FWsvNvGLQAhXpFUfAPiP6k0EwXuPCE1sG%2F1SojIhKp7x6bK%2FQciTXZBfZRR6Yf8JYnB4IkfpdO%2B1dk0Ey%2BI2Gm524eKyCy%2BhFPojNaqScJ24xABimY0Iip0%2BAQyMDU5XIhjBpiQSgZXEZmnDtY50QtEJuqXs6fW0nFQ2uZSqiwugxa3nYh4ApseHmuYAFR%2FuHYQZ7RAuk9w5mRHqCwtNzPGuY1gnx3ICvhPktfcHP83UMOeg18oGOqUB281A4Ok0byZ2BdwXlwgLQ0g7pPcZWt2%2Fm58cZfJbM7z%2FV1idBK8CHWXGI6ulzNhky4opN5AkMSNT6KJCSksonVp8lRGfTpUIsG0VRdlT1fT90s8gywaR9sHFDrWcWlpylAocsENiSnICv7OOMqRsXSbpFVQQ4cY7bUQx7mZC2E2AfVWti4VhvRHcSke8HB%2Fa2oSeBpDkmQKq%2BQMhE5vnGzbCJSmx&X-Amz-Signature=c2aafa8df37c97d536c5204efce66987d7fe67ec0907eabee4783e7815a214b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI6CBTQB%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCTCd3qolaXwMK6REmsq2gSI2aU%2FCchAdQ9q9Y%2Bc%2FIHdwIgG9Zr%2FwD%2FfTVrXmbmQKGP7Na2aI0TE%2BoF7zHfhWt7YU4qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb4aJLPFqaw6BGp6CrcAy4MnvGRFnupl0wqxsW7utThHZycC8E7jd6gpKZKLImGAQuDiF1PcKeWc47oa7QpZ4ikF%2FLAeZFI%2FJCcsEWtnnA%2BVoRlLUhchuWKDacYfZL12uZpcjYB2y8PvEA8RSrwROrYUB2QOf770oXWx158E6ctHjwd8pBgmo8V374IlgLD9dG38az82fR9cYIJd0zHUJeDIXr5WUafYCgKWqZJpxy8RawWX2%2BgyIrivSPlLmuVSgg9Z2dfejHgVWUV%2FPNUrIvWY86yE3j0ntf1Eakzw302X1P9i6HYXms7G4n4PnJR2FiFh7H%2ByHQ9hkMNk%2FUKWXQWj369QGbV%2FmDLH%2FUGt0PofW3fuZdM3627WzyWg1e6JPhUpNxU7WPRJHh8y5%2FGAm4m1Al%2BnLBlC5hb%2FWsvNvGLQAhXpFUfAPiP6k0EwXuPCE1sG%2F1SojIhKp7x6bK%2FQciTXZBfZRR6Yf8JYnB4IkfpdO%2B1dk0Ey%2BI2Gm524eKyCy%2BhFPojNaqScJ24xABimY0Iip0%2BAQyMDU5XIhjBpiQSgZXEZmnDtY50QtEJuqXs6fW0nFQ2uZSqiwugxa3nYh4ApseHmuYAFR%2FuHYQZ7RAuk9w5mRHqCwtNzPGuY1gnx3ICvhPktfcHP83UMOeg18oGOqUB281A4Ok0byZ2BdwXlwgLQ0g7pPcZWt2%2Fm58cZfJbM7z%2FV1idBK8CHWXGI6ulzNhky4opN5AkMSNT6KJCSksonVp8lRGfTpUIsG0VRdlT1fT90s8gywaR9sHFDrWcWlpylAocsENiSnICv7OOMqRsXSbpFVQQ4cY7bUQx7mZC2E2AfVWti4VhvRHcSke8HB%2Fa2oSeBpDkmQKq%2BQMhE5vnGzbCJSmx&X-Amz-Signature=ce9be6f43b4ba1c7e4324bcc2fed3ddf702a0e0052c215c5853e259f17ac2165&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI6CBTQB%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCTCd3qolaXwMK6REmsq2gSI2aU%2FCchAdQ9q9Y%2Bc%2FIHdwIgG9Zr%2FwD%2FfTVrXmbmQKGP7Na2aI0TE%2BoF7zHfhWt7YU4qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb4aJLPFqaw6BGp6CrcAy4MnvGRFnupl0wqxsW7utThHZycC8E7jd6gpKZKLImGAQuDiF1PcKeWc47oa7QpZ4ikF%2FLAeZFI%2FJCcsEWtnnA%2BVoRlLUhchuWKDacYfZL12uZpcjYB2y8PvEA8RSrwROrYUB2QOf770oXWx158E6ctHjwd8pBgmo8V374IlgLD9dG38az82fR9cYIJd0zHUJeDIXr5WUafYCgKWqZJpxy8RawWX2%2BgyIrivSPlLmuVSgg9Z2dfejHgVWUV%2FPNUrIvWY86yE3j0ntf1Eakzw302X1P9i6HYXms7G4n4PnJR2FiFh7H%2ByHQ9hkMNk%2FUKWXQWj369QGbV%2FmDLH%2FUGt0PofW3fuZdM3627WzyWg1e6JPhUpNxU7WPRJHh8y5%2FGAm4m1Al%2BnLBlC5hb%2FWsvNvGLQAhXpFUfAPiP6k0EwXuPCE1sG%2F1SojIhKp7x6bK%2FQciTXZBfZRR6Yf8JYnB4IkfpdO%2B1dk0Ey%2BI2Gm524eKyCy%2BhFPojNaqScJ24xABimY0Iip0%2BAQyMDU5XIhjBpiQSgZXEZmnDtY50QtEJuqXs6fW0nFQ2uZSqiwugxa3nYh4ApseHmuYAFR%2FuHYQZ7RAuk9w5mRHqCwtNzPGuY1gnx3ICvhPktfcHP83UMOeg18oGOqUB281A4Ok0byZ2BdwXlwgLQ0g7pPcZWt2%2Fm58cZfJbM7z%2FV1idBK8CHWXGI6ulzNhky4opN5AkMSNT6KJCSksonVp8lRGfTpUIsG0VRdlT1fT90s8gywaR9sHFDrWcWlpylAocsENiSnICv7OOMqRsXSbpFVQQ4cY7bUQx7mZC2E2AfVWti4VhvRHcSke8HB%2Fa2oSeBpDkmQKq%2BQMhE5vnGzbCJSmx&X-Amz-Signature=1da5e37200fa3bca79ffabbea55d124cda68e81fdb86785555c9684d2c39b636&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI6CBTQB%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCTCd3qolaXwMK6REmsq2gSI2aU%2FCchAdQ9q9Y%2Bc%2FIHdwIgG9Zr%2FwD%2FfTVrXmbmQKGP7Na2aI0TE%2BoF7zHfhWt7YU4qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb4aJLPFqaw6BGp6CrcAy4MnvGRFnupl0wqxsW7utThHZycC8E7jd6gpKZKLImGAQuDiF1PcKeWc47oa7QpZ4ikF%2FLAeZFI%2FJCcsEWtnnA%2BVoRlLUhchuWKDacYfZL12uZpcjYB2y8PvEA8RSrwROrYUB2QOf770oXWx158E6ctHjwd8pBgmo8V374IlgLD9dG38az82fR9cYIJd0zHUJeDIXr5WUafYCgKWqZJpxy8RawWX2%2BgyIrivSPlLmuVSgg9Z2dfejHgVWUV%2FPNUrIvWY86yE3j0ntf1Eakzw302X1P9i6HYXms7G4n4PnJR2FiFh7H%2ByHQ9hkMNk%2FUKWXQWj369QGbV%2FmDLH%2FUGt0PofW3fuZdM3627WzyWg1e6JPhUpNxU7WPRJHh8y5%2FGAm4m1Al%2BnLBlC5hb%2FWsvNvGLQAhXpFUfAPiP6k0EwXuPCE1sG%2F1SojIhKp7x6bK%2FQciTXZBfZRR6Yf8JYnB4IkfpdO%2B1dk0Ey%2BI2Gm524eKyCy%2BhFPojNaqScJ24xABimY0Iip0%2BAQyMDU5XIhjBpiQSgZXEZmnDtY50QtEJuqXs6fW0nFQ2uZSqiwugxa3nYh4ApseHmuYAFR%2FuHYQZ7RAuk9w5mRHqCwtNzPGuY1gnx3ICvhPktfcHP83UMOeg18oGOqUB281A4Ok0byZ2BdwXlwgLQ0g7pPcZWt2%2Fm58cZfJbM7z%2FV1idBK8CHWXGI6ulzNhky4opN5AkMSNT6KJCSksonVp8lRGfTpUIsG0VRdlT1fT90s8gywaR9sHFDrWcWlpylAocsENiSnICv7OOMqRsXSbpFVQQ4cY7bUQx7mZC2E2AfVWti4VhvRHcSke8HB%2Fa2oSeBpDkmQKq%2BQMhE5vnGzbCJSmx&X-Amz-Signature=151f84812cf78e95fcd35316a0eda4b265c38d0b0f75a19680e2a7ac07accc7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI6CBTQB%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCTCd3qolaXwMK6REmsq2gSI2aU%2FCchAdQ9q9Y%2Bc%2FIHdwIgG9Zr%2FwD%2FfTVrXmbmQKGP7Na2aI0TE%2BoF7zHfhWt7YU4qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb4aJLPFqaw6BGp6CrcAy4MnvGRFnupl0wqxsW7utThHZycC8E7jd6gpKZKLImGAQuDiF1PcKeWc47oa7QpZ4ikF%2FLAeZFI%2FJCcsEWtnnA%2BVoRlLUhchuWKDacYfZL12uZpcjYB2y8PvEA8RSrwROrYUB2QOf770oXWx158E6ctHjwd8pBgmo8V374IlgLD9dG38az82fR9cYIJd0zHUJeDIXr5WUafYCgKWqZJpxy8RawWX2%2BgyIrivSPlLmuVSgg9Z2dfejHgVWUV%2FPNUrIvWY86yE3j0ntf1Eakzw302X1P9i6HYXms7G4n4PnJR2FiFh7H%2ByHQ9hkMNk%2FUKWXQWj369QGbV%2FmDLH%2FUGt0PofW3fuZdM3627WzyWg1e6JPhUpNxU7WPRJHh8y5%2FGAm4m1Al%2BnLBlC5hb%2FWsvNvGLQAhXpFUfAPiP6k0EwXuPCE1sG%2F1SojIhKp7x6bK%2FQciTXZBfZRR6Yf8JYnB4IkfpdO%2B1dk0Ey%2BI2Gm524eKyCy%2BhFPojNaqScJ24xABimY0Iip0%2BAQyMDU5XIhjBpiQSgZXEZmnDtY50QtEJuqXs6fW0nFQ2uZSqiwugxa3nYh4ApseHmuYAFR%2FuHYQZ7RAuk9w5mRHqCwtNzPGuY1gnx3ICvhPktfcHP83UMOeg18oGOqUB281A4Ok0byZ2BdwXlwgLQ0g7pPcZWt2%2Fm58cZfJbM7z%2FV1idBK8CHWXGI6ulzNhky4opN5AkMSNT6KJCSksonVp8lRGfTpUIsG0VRdlT1fT90s8gywaR9sHFDrWcWlpylAocsENiSnICv7OOMqRsXSbpFVQQ4cY7bUQx7mZC2E2AfVWti4VhvRHcSke8HB%2Fa2oSeBpDkmQKq%2BQMhE5vnGzbCJSmx&X-Amz-Signature=bf2bafde50db041dad3544c17b8adcae5d68da8830e4ae8d60a221316ab350ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

