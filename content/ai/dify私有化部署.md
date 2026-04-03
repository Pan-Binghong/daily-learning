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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLN5BWG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGtF3GEg37lFzFPgQCU7aPYf5MDsLhmNWZM87IfP7udAIgTVNBrmfl4aAu0X2WsgGfmcOeux5vJqGYb4z%2B5WxeNE0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNPFFnCD5QhLKAsJsyrcA3C9k3aWs%2FVsbf02nNHGzSAr1rPNaYVz3tHWb5l4QE66W3bwN8reUzUcnmBfpL7CWX1%2FJOsXitANhj9VKpicJE4tCmtOZgs8sAPSX%2BUk3uCfhtc2nr8dbEOj1eY6YzlrB4rG9V3WNSblymNE4sVepU%2F8cNnHJajihhZmduMpu2eQVP7fCgA9xFM%2F5VuotdJsIAjjChVmTUTmMxEj98KK0IRdW%2BJwTSqJE0%2FRu58zdChq7bqZ2CKlnyLcamEVmS6z1JqMKjg6%2BBcnnToC6pOOTM5boK0ITKaxl%2BPmJNSnA257f3%2BfGYCfuBxPZrprxuZqVAsywbt7%2BFnmBoBlR7eRkyMdbJKykkeuwTeHSQZop0Y1H6jRfOWsW3o%2BWe%2FqKDtQvTCoUIOsGzqG7%2B8ZaoeYPBvSkFDrw%2B4FHdwt3WDo4OjufKsusniel7sMFnrlh39ZMDEuxakA0aq7nJp%2BnqhqPOFmcmdUbMaef6xfIiNdJVd91NM3Rezg2lx8VaR5Kv9HPXP1XlXxnb0ueaXsewafVxTIr1m8RI1%2FfIcH5NkV74X7WErpvTwXrHLUd%2FAy0O3zlhZkVFzqttJ2pl%2BrIfVdRw8BH8gJVzF%2Fs%2BATpczqOovDwtupMp2H3MkKSo6sMKnqvM4GOqUBzsztY6evUEUg1PQXxDNs5xXRUSbwKYPpTd3wjsbvo9tCWRNanjoRHaKSUi8NvGC8dP3YomWFCpzP4nQtLAeg2tWIhSFNBhSnhVTeAHd7FMGRHItMsrCd1JtSlgdugcxpKOvlACe0nlLIcifuIVt%2BsJYYMoG%2Bl4izws5jyUrbUShGJD3UYb0ceJegc3IA6hDEL%2BR8eel1FsrozKrknAEDek9iI5P%2F&X-Amz-Signature=e08d276ecc2e14f0c952148102466406e0d7fd62007257f280548d5c93b44011&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLN5BWG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGtF3GEg37lFzFPgQCU7aPYf5MDsLhmNWZM87IfP7udAIgTVNBrmfl4aAu0X2WsgGfmcOeux5vJqGYb4z%2B5WxeNE0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNPFFnCD5QhLKAsJsyrcA3C9k3aWs%2FVsbf02nNHGzSAr1rPNaYVz3tHWb5l4QE66W3bwN8reUzUcnmBfpL7CWX1%2FJOsXitANhj9VKpicJE4tCmtOZgs8sAPSX%2BUk3uCfhtc2nr8dbEOj1eY6YzlrB4rG9V3WNSblymNE4sVepU%2F8cNnHJajihhZmduMpu2eQVP7fCgA9xFM%2F5VuotdJsIAjjChVmTUTmMxEj98KK0IRdW%2BJwTSqJE0%2FRu58zdChq7bqZ2CKlnyLcamEVmS6z1JqMKjg6%2BBcnnToC6pOOTM5boK0ITKaxl%2BPmJNSnA257f3%2BfGYCfuBxPZrprxuZqVAsywbt7%2BFnmBoBlR7eRkyMdbJKykkeuwTeHSQZop0Y1H6jRfOWsW3o%2BWe%2FqKDtQvTCoUIOsGzqG7%2B8ZaoeYPBvSkFDrw%2B4FHdwt3WDo4OjufKsusniel7sMFnrlh39ZMDEuxakA0aq7nJp%2BnqhqPOFmcmdUbMaef6xfIiNdJVd91NM3Rezg2lx8VaR5Kv9HPXP1XlXxnb0ueaXsewafVxTIr1m8RI1%2FfIcH5NkV74X7WErpvTwXrHLUd%2FAy0O3zlhZkVFzqttJ2pl%2BrIfVdRw8BH8gJVzF%2Fs%2BATpczqOovDwtupMp2H3MkKSo6sMKnqvM4GOqUBzsztY6evUEUg1PQXxDNs5xXRUSbwKYPpTd3wjsbvo9tCWRNanjoRHaKSUi8NvGC8dP3YomWFCpzP4nQtLAeg2tWIhSFNBhSnhVTeAHd7FMGRHItMsrCd1JtSlgdugcxpKOvlACe0nlLIcifuIVt%2BsJYYMoG%2Bl4izws5jyUrbUShGJD3UYb0ceJegc3IA6hDEL%2BR8eel1FsrozKrknAEDek9iI5P%2F&X-Amz-Signature=7973dfab6995b8d4a62c4a0005848e52f20fe819c003e09bb163a03204373507&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLN5BWG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGtF3GEg37lFzFPgQCU7aPYf5MDsLhmNWZM87IfP7udAIgTVNBrmfl4aAu0X2WsgGfmcOeux5vJqGYb4z%2B5WxeNE0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNPFFnCD5QhLKAsJsyrcA3C9k3aWs%2FVsbf02nNHGzSAr1rPNaYVz3tHWb5l4QE66W3bwN8reUzUcnmBfpL7CWX1%2FJOsXitANhj9VKpicJE4tCmtOZgs8sAPSX%2BUk3uCfhtc2nr8dbEOj1eY6YzlrB4rG9V3WNSblymNE4sVepU%2F8cNnHJajihhZmduMpu2eQVP7fCgA9xFM%2F5VuotdJsIAjjChVmTUTmMxEj98KK0IRdW%2BJwTSqJE0%2FRu58zdChq7bqZ2CKlnyLcamEVmS6z1JqMKjg6%2BBcnnToC6pOOTM5boK0ITKaxl%2BPmJNSnA257f3%2BfGYCfuBxPZrprxuZqVAsywbt7%2BFnmBoBlR7eRkyMdbJKykkeuwTeHSQZop0Y1H6jRfOWsW3o%2BWe%2FqKDtQvTCoUIOsGzqG7%2B8ZaoeYPBvSkFDrw%2B4FHdwt3WDo4OjufKsusniel7sMFnrlh39ZMDEuxakA0aq7nJp%2BnqhqPOFmcmdUbMaef6xfIiNdJVd91NM3Rezg2lx8VaR5Kv9HPXP1XlXxnb0ueaXsewafVxTIr1m8RI1%2FfIcH5NkV74X7WErpvTwXrHLUd%2FAy0O3zlhZkVFzqttJ2pl%2BrIfVdRw8BH8gJVzF%2Fs%2BATpczqOovDwtupMp2H3MkKSo6sMKnqvM4GOqUBzsztY6evUEUg1PQXxDNs5xXRUSbwKYPpTd3wjsbvo9tCWRNanjoRHaKSUi8NvGC8dP3YomWFCpzP4nQtLAeg2tWIhSFNBhSnhVTeAHd7FMGRHItMsrCd1JtSlgdugcxpKOvlACe0nlLIcifuIVt%2BsJYYMoG%2Bl4izws5jyUrbUShGJD3UYb0ceJegc3IA6hDEL%2BR8eel1FsrozKrknAEDek9iI5P%2F&X-Amz-Signature=00b8ef923529c5c3521e4bd5f3609083cdad89ef2fc001cac62973c94ae90ba4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLN5BWG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGtF3GEg37lFzFPgQCU7aPYf5MDsLhmNWZM87IfP7udAIgTVNBrmfl4aAu0X2WsgGfmcOeux5vJqGYb4z%2B5WxeNE0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNPFFnCD5QhLKAsJsyrcA3C9k3aWs%2FVsbf02nNHGzSAr1rPNaYVz3tHWb5l4QE66W3bwN8reUzUcnmBfpL7CWX1%2FJOsXitANhj9VKpicJE4tCmtOZgs8sAPSX%2BUk3uCfhtc2nr8dbEOj1eY6YzlrB4rG9V3WNSblymNE4sVepU%2F8cNnHJajihhZmduMpu2eQVP7fCgA9xFM%2F5VuotdJsIAjjChVmTUTmMxEj98KK0IRdW%2BJwTSqJE0%2FRu58zdChq7bqZ2CKlnyLcamEVmS6z1JqMKjg6%2BBcnnToC6pOOTM5boK0ITKaxl%2BPmJNSnA257f3%2BfGYCfuBxPZrprxuZqVAsywbt7%2BFnmBoBlR7eRkyMdbJKykkeuwTeHSQZop0Y1H6jRfOWsW3o%2BWe%2FqKDtQvTCoUIOsGzqG7%2B8ZaoeYPBvSkFDrw%2B4FHdwt3WDo4OjufKsusniel7sMFnrlh39ZMDEuxakA0aq7nJp%2BnqhqPOFmcmdUbMaef6xfIiNdJVd91NM3Rezg2lx8VaR5Kv9HPXP1XlXxnb0ueaXsewafVxTIr1m8RI1%2FfIcH5NkV74X7WErpvTwXrHLUd%2FAy0O3zlhZkVFzqttJ2pl%2BrIfVdRw8BH8gJVzF%2Fs%2BATpczqOovDwtupMp2H3MkKSo6sMKnqvM4GOqUBzsztY6evUEUg1PQXxDNs5xXRUSbwKYPpTd3wjsbvo9tCWRNanjoRHaKSUi8NvGC8dP3YomWFCpzP4nQtLAeg2tWIhSFNBhSnhVTeAHd7FMGRHItMsrCd1JtSlgdugcxpKOvlACe0nlLIcifuIVt%2BsJYYMoG%2Bl4izws5jyUrbUShGJD3UYb0ceJegc3IA6hDEL%2BR8eel1FsrozKrknAEDek9iI5P%2F&X-Amz-Signature=57ad6dd4c77638f0286011c27b878b4decfb857ff9f13481bc170d5ce6350e25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLN5BWG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGtF3GEg37lFzFPgQCU7aPYf5MDsLhmNWZM87IfP7udAIgTVNBrmfl4aAu0X2WsgGfmcOeux5vJqGYb4z%2B5WxeNE0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNPFFnCD5QhLKAsJsyrcA3C9k3aWs%2FVsbf02nNHGzSAr1rPNaYVz3tHWb5l4QE66W3bwN8reUzUcnmBfpL7CWX1%2FJOsXitANhj9VKpicJE4tCmtOZgs8sAPSX%2BUk3uCfhtc2nr8dbEOj1eY6YzlrB4rG9V3WNSblymNE4sVepU%2F8cNnHJajihhZmduMpu2eQVP7fCgA9xFM%2F5VuotdJsIAjjChVmTUTmMxEj98KK0IRdW%2BJwTSqJE0%2FRu58zdChq7bqZ2CKlnyLcamEVmS6z1JqMKjg6%2BBcnnToC6pOOTM5boK0ITKaxl%2BPmJNSnA257f3%2BfGYCfuBxPZrprxuZqVAsywbt7%2BFnmBoBlR7eRkyMdbJKykkeuwTeHSQZop0Y1H6jRfOWsW3o%2BWe%2FqKDtQvTCoUIOsGzqG7%2B8ZaoeYPBvSkFDrw%2B4FHdwt3WDo4OjufKsusniel7sMFnrlh39ZMDEuxakA0aq7nJp%2BnqhqPOFmcmdUbMaef6xfIiNdJVd91NM3Rezg2lx8VaR5Kv9HPXP1XlXxnb0ueaXsewafVxTIr1m8RI1%2FfIcH5NkV74X7WErpvTwXrHLUd%2FAy0O3zlhZkVFzqttJ2pl%2BrIfVdRw8BH8gJVzF%2Fs%2BATpczqOovDwtupMp2H3MkKSo6sMKnqvM4GOqUBzsztY6evUEUg1PQXxDNs5xXRUSbwKYPpTd3wjsbvo9tCWRNanjoRHaKSUi8NvGC8dP3YomWFCpzP4nQtLAeg2tWIhSFNBhSnhVTeAHd7FMGRHItMsrCd1JtSlgdugcxpKOvlACe0nlLIcifuIVt%2BsJYYMoG%2Bl4izws5jyUrbUShGJD3UYb0ceJegc3IA6hDEL%2BR8eel1FsrozKrknAEDek9iI5P%2F&X-Amz-Signature=3635885edddba7f52158b53731f5153ab9dfdea13eb0f48cd329bf6ac8c1f837&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLN5BWG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGtF3GEg37lFzFPgQCU7aPYf5MDsLhmNWZM87IfP7udAIgTVNBrmfl4aAu0X2WsgGfmcOeux5vJqGYb4z%2B5WxeNE0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNPFFnCD5QhLKAsJsyrcA3C9k3aWs%2FVsbf02nNHGzSAr1rPNaYVz3tHWb5l4QE66W3bwN8reUzUcnmBfpL7CWX1%2FJOsXitANhj9VKpicJE4tCmtOZgs8sAPSX%2BUk3uCfhtc2nr8dbEOj1eY6YzlrB4rG9V3WNSblymNE4sVepU%2F8cNnHJajihhZmduMpu2eQVP7fCgA9xFM%2F5VuotdJsIAjjChVmTUTmMxEj98KK0IRdW%2BJwTSqJE0%2FRu58zdChq7bqZ2CKlnyLcamEVmS6z1JqMKjg6%2BBcnnToC6pOOTM5boK0ITKaxl%2BPmJNSnA257f3%2BfGYCfuBxPZrprxuZqVAsywbt7%2BFnmBoBlR7eRkyMdbJKykkeuwTeHSQZop0Y1H6jRfOWsW3o%2BWe%2FqKDtQvTCoUIOsGzqG7%2B8ZaoeYPBvSkFDrw%2B4FHdwt3WDo4OjufKsusniel7sMFnrlh39ZMDEuxakA0aq7nJp%2BnqhqPOFmcmdUbMaef6xfIiNdJVd91NM3Rezg2lx8VaR5Kv9HPXP1XlXxnb0ueaXsewafVxTIr1m8RI1%2FfIcH5NkV74X7WErpvTwXrHLUd%2FAy0O3zlhZkVFzqttJ2pl%2BrIfVdRw8BH8gJVzF%2Fs%2BATpczqOovDwtupMp2H3MkKSo6sMKnqvM4GOqUBzsztY6evUEUg1PQXxDNs5xXRUSbwKYPpTd3wjsbvo9tCWRNanjoRHaKSUi8NvGC8dP3YomWFCpzP4nQtLAeg2tWIhSFNBhSnhVTeAHd7FMGRHItMsrCd1JtSlgdugcxpKOvlACe0nlLIcifuIVt%2BsJYYMoG%2Bl4izws5jyUrbUShGJD3UYb0ceJegc3IA6hDEL%2BR8eel1FsrozKrknAEDek9iI5P%2F&X-Amz-Signature=376c7ed8832fbe4664372ca6c6ef91d4898d05aac7ca130c1bf538e136496a78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLN5BWG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGtF3GEg37lFzFPgQCU7aPYf5MDsLhmNWZM87IfP7udAIgTVNBrmfl4aAu0X2WsgGfmcOeux5vJqGYb4z%2B5WxeNE0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNPFFnCD5QhLKAsJsyrcA3C9k3aWs%2FVsbf02nNHGzSAr1rPNaYVz3tHWb5l4QE66W3bwN8reUzUcnmBfpL7CWX1%2FJOsXitANhj9VKpicJE4tCmtOZgs8sAPSX%2BUk3uCfhtc2nr8dbEOj1eY6YzlrB4rG9V3WNSblymNE4sVepU%2F8cNnHJajihhZmduMpu2eQVP7fCgA9xFM%2F5VuotdJsIAjjChVmTUTmMxEj98KK0IRdW%2BJwTSqJE0%2FRu58zdChq7bqZ2CKlnyLcamEVmS6z1JqMKjg6%2BBcnnToC6pOOTM5boK0ITKaxl%2BPmJNSnA257f3%2BfGYCfuBxPZrprxuZqVAsywbt7%2BFnmBoBlR7eRkyMdbJKykkeuwTeHSQZop0Y1H6jRfOWsW3o%2BWe%2FqKDtQvTCoUIOsGzqG7%2B8ZaoeYPBvSkFDrw%2B4FHdwt3WDo4OjufKsusniel7sMFnrlh39ZMDEuxakA0aq7nJp%2BnqhqPOFmcmdUbMaef6xfIiNdJVd91NM3Rezg2lx8VaR5Kv9HPXP1XlXxnb0ueaXsewafVxTIr1m8RI1%2FfIcH5NkV74X7WErpvTwXrHLUd%2FAy0O3zlhZkVFzqttJ2pl%2BrIfVdRw8BH8gJVzF%2Fs%2BATpczqOovDwtupMp2H3MkKSo6sMKnqvM4GOqUBzsztY6evUEUg1PQXxDNs5xXRUSbwKYPpTd3wjsbvo9tCWRNanjoRHaKSUi8NvGC8dP3YomWFCpzP4nQtLAeg2tWIhSFNBhSnhVTeAHd7FMGRHItMsrCd1JtSlgdugcxpKOvlACe0nlLIcifuIVt%2BsJYYMoG%2Bl4izws5jyUrbUShGJD3UYb0ceJegc3IA6hDEL%2BR8eel1FsrozKrknAEDek9iI5P%2F&X-Amz-Signature=72ea6776ed39d2a374712cf9d220afb50efc052d444e24b32b24928b4512c3ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLN5BWG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGtF3GEg37lFzFPgQCU7aPYf5MDsLhmNWZM87IfP7udAIgTVNBrmfl4aAu0X2WsgGfmcOeux5vJqGYb4z%2B5WxeNE0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNPFFnCD5QhLKAsJsyrcA3C9k3aWs%2FVsbf02nNHGzSAr1rPNaYVz3tHWb5l4QE66W3bwN8reUzUcnmBfpL7CWX1%2FJOsXitANhj9VKpicJE4tCmtOZgs8sAPSX%2BUk3uCfhtc2nr8dbEOj1eY6YzlrB4rG9V3WNSblymNE4sVepU%2F8cNnHJajihhZmduMpu2eQVP7fCgA9xFM%2F5VuotdJsIAjjChVmTUTmMxEj98KK0IRdW%2BJwTSqJE0%2FRu58zdChq7bqZ2CKlnyLcamEVmS6z1JqMKjg6%2BBcnnToC6pOOTM5boK0ITKaxl%2BPmJNSnA257f3%2BfGYCfuBxPZrprxuZqVAsywbt7%2BFnmBoBlR7eRkyMdbJKykkeuwTeHSQZop0Y1H6jRfOWsW3o%2BWe%2FqKDtQvTCoUIOsGzqG7%2B8ZaoeYPBvSkFDrw%2B4FHdwt3WDo4OjufKsusniel7sMFnrlh39ZMDEuxakA0aq7nJp%2BnqhqPOFmcmdUbMaef6xfIiNdJVd91NM3Rezg2lx8VaR5Kv9HPXP1XlXxnb0ueaXsewafVxTIr1m8RI1%2FfIcH5NkV74X7WErpvTwXrHLUd%2FAy0O3zlhZkVFzqttJ2pl%2BrIfVdRw8BH8gJVzF%2Fs%2BATpczqOovDwtupMp2H3MkKSo6sMKnqvM4GOqUBzsztY6evUEUg1PQXxDNs5xXRUSbwKYPpTd3wjsbvo9tCWRNanjoRHaKSUi8NvGC8dP3YomWFCpzP4nQtLAeg2tWIhSFNBhSnhVTeAHd7FMGRHItMsrCd1JtSlgdugcxpKOvlACe0nlLIcifuIVt%2BsJYYMoG%2Bl4izws5jyUrbUShGJD3UYb0ceJegc3IA6hDEL%2BR8eel1FsrozKrknAEDek9iI5P%2F&X-Amz-Signature=cd599edd7609fbb64f008b48f2fb101185c544bdadc472136dfba5819dea4389&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLN5BWG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGtF3GEg37lFzFPgQCU7aPYf5MDsLhmNWZM87IfP7udAIgTVNBrmfl4aAu0X2WsgGfmcOeux5vJqGYb4z%2B5WxeNE0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNPFFnCD5QhLKAsJsyrcA3C9k3aWs%2FVsbf02nNHGzSAr1rPNaYVz3tHWb5l4QE66W3bwN8reUzUcnmBfpL7CWX1%2FJOsXitANhj9VKpicJE4tCmtOZgs8sAPSX%2BUk3uCfhtc2nr8dbEOj1eY6YzlrB4rG9V3WNSblymNE4sVepU%2F8cNnHJajihhZmduMpu2eQVP7fCgA9xFM%2F5VuotdJsIAjjChVmTUTmMxEj98KK0IRdW%2BJwTSqJE0%2FRu58zdChq7bqZ2CKlnyLcamEVmS6z1JqMKjg6%2BBcnnToC6pOOTM5boK0ITKaxl%2BPmJNSnA257f3%2BfGYCfuBxPZrprxuZqVAsywbt7%2BFnmBoBlR7eRkyMdbJKykkeuwTeHSQZop0Y1H6jRfOWsW3o%2BWe%2FqKDtQvTCoUIOsGzqG7%2B8ZaoeYPBvSkFDrw%2B4FHdwt3WDo4OjufKsusniel7sMFnrlh39ZMDEuxakA0aq7nJp%2BnqhqPOFmcmdUbMaef6xfIiNdJVd91NM3Rezg2lx8VaR5Kv9HPXP1XlXxnb0ueaXsewafVxTIr1m8RI1%2FfIcH5NkV74X7WErpvTwXrHLUd%2FAy0O3zlhZkVFzqttJ2pl%2BrIfVdRw8BH8gJVzF%2Fs%2BATpczqOovDwtupMp2H3MkKSo6sMKnqvM4GOqUBzsztY6evUEUg1PQXxDNs5xXRUSbwKYPpTd3wjsbvo9tCWRNanjoRHaKSUi8NvGC8dP3YomWFCpzP4nQtLAeg2tWIhSFNBhSnhVTeAHd7FMGRHItMsrCd1JtSlgdugcxpKOvlACe0nlLIcifuIVt%2BsJYYMoG%2Bl4izws5jyUrbUShGJD3UYb0ceJegc3IA6hDEL%2BR8eel1FsrozKrknAEDek9iI5P%2F&X-Amz-Signature=0f51d77f00760bdb24886ee82198d15cdc42848b0f2d964d98f430049fa64b5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLN5BWG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGtF3GEg37lFzFPgQCU7aPYf5MDsLhmNWZM87IfP7udAIgTVNBrmfl4aAu0X2WsgGfmcOeux5vJqGYb4z%2B5WxeNE0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDNPFFnCD5QhLKAsJsyrcA3C9k3aWs%2FVsbf02nNHGzSAr1rPNaYVz3tHWb5l4QE66W3bwN8reUzUcnmBfpL7CWX1%2FJOsXitANhj9VKpicJE4tCmtOZgs8sAPSX%2BUk3uCfhtc2nr8dbEOj1eY6YzlrB4rG9V3WNSblymNE4sVepU%2F8cNnHJajihhZmduMpu2eQVP7fCgA9xFM%2F5VuotdJsIAjjChVmTUTmMxEj98KK0IRdW%2BJwTSqJE0%2FRu58zdChq7bqZ2CKlnyLcamEVmS6z1JqMKjg6%2BBcnnToC6pOOTM5boK0ITKaxl%2BPmJNSnA257f3%2BfGYCfuBxPZrprxuZqVAsywbt7%2BFnmBoBlR7eRkyMdbJKykkeuwTeHSQZop0Y1H6jRfOWsW3o%2BWe%2FqKDtQvTCoUIOsGzqG7%2B8ZaoeYPBvSkFDrw%2B4FHdwt3WDo4OjufKsusniel7sMFnrlh39ZMDEuxakA0aq7nJp%2BnqhqPOFmcmdUbMaef6xfIiNdJVd91NM3Rezg2lx8VaR5Kv9HPXP1XlXxnb0ueaXsewafVxTIr1m8RI1%2FfIcH5NkV74X7WErpvTwXrHLUd%2FAy0O3zlhZkVFzqttJ2pl%2BrIfVdRw8BH8gJVzF%2Fs%2BATpczqOovDwtupMp2H3MkKSo6sMKnqvM4GOqUBzsztY6evUEUg1PQXxDNs5xXRUSbwKYPpTd3wjsbvo9tCWRNanjoRHaKSUi8NvGC8dP3YomWFCpzP4nQtLAeg2tWIhSFNBhSnhVTeAHd7FMGRHItMsrCd1JtSlgdugcxpKOvlACe0nlLIcifuIVt%2BsJYYMoG%2Bl4izws5jyUrbUShGJD3UYb0ceJegc3IA6hDEL%2BR8eel1FsrozKrknAEDek9iI5P%2F&X-Amz-Signature=4c2e4832ca8f02a7ef82b8fb920036167b83b3deefc617ed2bfe1d9caf5fd79b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

