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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHBE7Y2L%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJsNYEzuZ26jSRpIgn0I6hlqAWWnJUTCfk%2FtZI%2BFzRDgIgYHRDWcMapX%2FsZTyUmJJK6FO34vbSH5zPp%2BWD7ixaE9cqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHNgjjRev%2BP4dDf5SrcA5X7zgBObygp2e%2FCRL4753bDcwDries5WFJA1bPAIxoQTNeADLt4%2FVKcs7GyFklUHDQlkctqLY%2Bqa%2FW%2FbqMmze36QX0dF58pBF9wShALGDRMUVzAfkNBW2p480HYjMbdzP9UYY07sOqa4HyH9yJ%2FaYLoDJ8YPQZnhO34jaEnXQUCmuya0evvb5g%2B1BITj7Qo1YXwF4n2N3hZ2BXz9EVBJjBG%2F7Bqzkp5iIXKy3nEPHrnjv%2Bfyn32k2F6AYBpvAtAQH2Ubpe3F8MD4hGWFtiG8gM8R12hL9jjo4EGBxXJTLLyAXChhwY71DLVsDeWbKoTty%2BtTN1xzQvVxR5eekcinrIW%2F96P2rzIWwvbJS%2B3yrJEDUc7D22nLPz8GOwhTtcuAPxXlRBfzaVfCp2zqv0E5xRgHgm7jasWRwmdsfjIeQLmFi5%2Fb8dIyE9bXFK7icXWwsag0aOS2uh4IiQB1YRK0gDaycVPADJoi0E4KLNUMaWmoQkgbKxzXy6AKT%2BNsyQBgMmxLZ39o75sbwhGv48fSRQb3KfL3PdAMIAXQniuN7ZcvqBXpAV1aQS02MdPWwwxSxyVJYVSQ75bRzUewdfqjobLAFaWyx1ejqPxNuJ7%2F2GEgGkTEw%2Bxn4ev%2F%2BAuMOrlwc4GOqUBgRTPK0IgBtJDHPP8Lwrwj6ECLEhKMg3d4A49SA7gMGXxh0FbG2eamJMAoh4Bei1GmCINOGr05t6IrjxfmJvqUIYQlnVUR41DigF9%2F8qT78cP9iTjKDLt0Ov7niSgePxanVGyXL%2FceyYiDso%2BrNsVO9l7%2Bw%2BZOg2M7E4moPy83l9LrnGKl9sQQ%2Fv8I7OZRVtk%2Bkn9C3ud3rXuoy5k6heWEtZ9TzEE&X-Amz-Signature=b546a8628c91a2993fc5e50cb6b70bfba620144872c74f5ef92797804794d1e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHBE7Y2L%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJsNYEzuZ26jSRpIgn0I6hlqAWWnJUTCfk%2FtZI%2BFzRDgIgYHRDWcMapX%2FsZTyUmJJK6FO34vbSH5zPp%2BWD7ixaE9cqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHNgjjRev%2BP4dDf5SrcA5X7zgBObygp2e%2FCRL4753bDcwDries5WFJA1bPAIxoQTNeADLt4%2FVKcs7GyFklUHDQlkctqLY%2Bqa%2FW%2FbqMmze36QX0dF58pBF9wShALGDRMUVzAfkNBW2p480HYjMbdzP9UYY07sOqa4HyH9yJ%2FaYLoDJ8YPQZnhO34jaEnXQUCmuya0evvb5g%2B1BITj7Qo1YXwF4n2N3hZ2BXz9EVBJjBG%2F7Bqzkp5iIXKy3nEPHrnjv%2Bfyn32k2F6AYBpvAtAQH2Ubpe3F8MD4hGWFtiG8gM8R12hL9jjo4EGBxXJTLLyAXChhwY71DLVsDeWbKoTty%2BtTN1xzQvVxR5eekcinrIW%2F96P2rzIWwvbJS%2B3yrJEDUc7D22nLPz8GOwhTtcuAPxXlRBfzaVfCp2zqv0E5xRgHgm7jasWRwmdsfjIeQLmFi5%2Fb8dIyE9bXFK7icXWwsag0aOS2uh4IiQB1YRK0gDaycVPADJoi0E4KLNUMaWmoQkgbKxzXy6AKT%2BNsyQBgMmxLZ39o75sbwhGv48fSRQb3KfL3PdAMIAXQniuN7ZcvqBXpAV1aQS02MdPWwwxSxyVJYVSQ75bRzUewdfqjobLAFaWyx1ejqPxNuJ7%2F2GEgGkTEw%2Bxn4ev%2F%2BAuMOrlwc4GOqUBgRTPK0IgBtJDHPP8Lwrwj6ECLEhKMg3d4A49SA7gMGXxh0FbG2eamJMAoh4Bei1GmCINOGr05t6IrjxfmJvqUIYQlnVUR41DigF9%2F8qT78cP9iTjKDLt0Ov7niSgePxanVGyXL%2FceyYiDso%2BrNsVO9l7%2Bw%2BZOg2M7E4moPy83l9LrnGKl9sQQ%2Fv8I7OZRVtk%2Bkn9C3ud3rXuoy5k6heWEtZ9TzEE&X-Amz-Signature=940b8ec907fb7ea4d755af87a160b8f8cc0226292360f7c39d3d50790ea0dd0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHBE7Y2L%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJsNYEzuZ26jSRpIgn0I6hlqAWWnJUTCfk%2FtZI%2BFzRDgIgYHRDWcMapX%2FsZTyUmJJK6FO34vbSH5zPp%2BWD7ixaE9cqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHNgjjRev%2BP4dDf5SrcA5X7zgBObygp2e%2FCRL4753bDcwDries5WFJA1bPAIxoQTNeADLt4%2FVKcs7GyFklUHDQlkctqLY%2Bqa%2FW%2FbqMmze36QX0dF58pBF9wShALGDRMUVzAfkNBW2p480HYjMbdzP9UYY07sOqa4HyH9yJ%2FaYLoDJ8YPQZnhO34jaEnXQUCmuya0evvb5g%2B1BITj7Qo1YXwF4n2N3hZ2BXz9EVBJjBG%2F7Bqzkp5iIXKy3nEPHrnjv%2Bfyn32k2F6AYBpvAtAQH2Ubpe3F8MD4hGWFtiG8gM8R12hL9jjo4EGBxXJTLLyAXChhwY71DLVsDeWbKoTty%2BtTN1xzQvVxR5eekcinrIW%2F96P2rzIWwvbJS%2B3yrJEDUc7D22nLPz8GOwhTtcuAPxXlRBfzaVfCp2zqv0E5xRgHgm7jasWRwmdsfjIeQLmFi5%2Fb8dIyE9bXFK7icXWwsag0aOS2uh4IiQB1YRK0gDaycVPADJoi0E4KLNUMaWmoQkgbKxzXy6AKT%2BNsyQBgMmxLZ39o75sbwhGv48fSRQb3KfL3PdAMIAXQniuN7ZcvqBXpAV1aQS02MdPWwwxSxyVJYVSQ75bRzUewdfqjobLAFaWyx1ejqPxNuJ7%2F2GEgGkTEw%2Bxn4ev%2F%2BAuMOrlwc4GOqUBgRTPK0IgBtJDHPP8Lwrwj6ECLEhKMg3d4A49SA7gMGXxh0FbG2eamJMAoh4Bei1GmCINOGr05t6IrjxfmJvqUIYQlnVUR41DigF9%2F8qT78cP9iTjKDLt0Ov7niSgePxanVGyXL%2FceyYiDso%2BrNsVO9l7%2Bw%2BZOg2M7E4moPy83l9LrnGKl9sQQ%2Fv8I7OZRVtk%2Bkn9C3ud3rXuoy5k6heWEtZ9TzEE&X-Amz-Signature=c7496f086f6bea14b5c042e1add75eb18bf7de150a177e494036ee91950afca2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHBE7Y2L%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJsNYEzuZ26jSRpIgn0I6hlqAWWnJUTCfk%2FtZI%2BFzRDgIgYHRDWcMapX%2FsZTyUmJJK6FO34vbSH5zPp%2BWD7ixaE9cqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHNgjjRev%2BP4dDf5SrcA5X7zgBObygp2e%2FCRL4753bDcwDries5WFJA1bPAIxoQTNeADLt4%2FVKcs7GyFklUHDQlkctqLY%2Bqa%2FW%2FbqMmze36QX0dF58pBF9wShALGDRMUVzAfkNBW2p480HYjMbdzP9UYY07sOqa4HyH9yJ%2FaYLoDJ8YPQZnhO34jaEnXQUCmuya0evvb5g%2B1BITj7Qo1YXwF4n2N3hZ2BXz9EVBJjBG%2F7Bqzkp5iIXKy3nEPHrnjv%2Bfyn32k2F6AYBpvAtAQH2Ubpe3F8MD4hGWFtiG8gM8R12hL9jjo4EGBxXJTLLyAXChhwY71DLVsDeWbKoTty%2BtTN1xzQvVxR5eekcinrIW%2F96P2rzIWwvbJS%2B3yrJEDUc7D22nLPz8GOwhTtcuAPxXlRBfzaVfCp2zqv0E5xRgHgm7jasWRwmdsfjIeQLmFi5%2Fb8dIyE9bXFK7icXWwsag0aOS2uh4IiQB1YRK0gDaycVPADJoi0E4KLNUMaWmoQkgbKxzXy6AKT%2BNsyQBgMmxLZ39o75sbwhGv48fSRQb3KfL3PdAMIAXQniuN7ZcvqBXpAV1aQS02MdPWwwxSxyVJYVSQ75bRzUewdfqjobLAFaWyx1ejqPxNuJ7%2F2GEgGkTEw%2Bxn4ev%2F%2BAuMOrlwc4GOqUBgRTPK0IgBtJDHPP8Lwrwj6ECLEhKMg3d4A49SA7gMGXxh0FbG2eamJMAoh4Bei1GmCINOGr05t6IrjxfmJvqUIYQlnVUR41DigF9%2F8qT78cP9iTjKDLt0Ov7niSgePxanVGyXL%2FceyYiDso%2BrNsVO9l7%2Bw%2BZOg2M7E4moPy83l9LrnGKl9sQQ%2Fv8I7OZRVtk%2Bkn9C3ud3rXuoy5k6heWEtZ9TzEE&X-Amz-Signature=d29da227cf8213708a50eb998d5d7cdcd271565fc0b27dd0d7b24ea915a3c4ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHBE7Y2L%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJsNYEzuZ26jSRpIgn0I6hlqAWWnJUTCfk%2FtZI%2BFzRDgIgYHRDWcMapX%2FsZTyUmJJK6FO34vbSH5zPp%2BWD7ixaE9cqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHNgjjRev%2BP4dDf5SrcA5X7zgBObygp2e%2FCRL4753bDcwDries5WFJA1bPAIxoQTNeADLt4%2FVKcs7GyFklUHDQlkctqLY%2Bqa%2FW%2FbqMmze36QX0dF58pBF9wShALGDRMUVzAfkNBW2p480HYjMbdzP9UYY07sOqa4HyH9yJ%2FaYLoDJ8YPQZnhO34jaEnXQUCmuya0evvb5g%2B1BITj7Qo1YXwF4n2N3hZ2BXz9EVBJjBG%2F7Bqzkp5iIXKy3nEPHrnjv%2Bfyn32k2F6AYBpvAtAQH2Ubpe3F8MD4hGWFtiG8gM8R12hL9jjo4EGBxXJTLLyAXChhwY71DLVsDeWbKoTty%2BtTN1xzQvVxR5eekcinrIW%2F96P2rzIWwvbJS%2B3yrJEDUc7D22nLPz8GOwhTtcuAPxXlRBfzaVfCp2zqv0E5xRgHgm7jasWRwmdsfjIeQLmFi5%2Fb8dIyE9bXFK7icXWwsag0aOS2uh4IiQB1YRK0gDaycVPADJoi0E4KLNUMaWmoQkgbKxzXy6AKT%2BNsyQBgMmxLZ39o75sbwhGv48fSRQb3KfL3PdAMIAXQniuN7ZcvqBXpAV1aQS02MdPWwwxSxyVJYVSQ75bRzUewdfqjobLAFaWyx1ejqPxNuJ7%2F2GEgGkTEw%2Bxn4ev%2F%2BAuMOrlwc4GOqUBgRTPK0IgBtJDHPP8Lwrwj6ECLEhKMg3d4A49SA7gMGXxh0FbG2eamJMAoh4Bei1GmCINOGr05t6IrjxfmJvqUIYQlnVUR41DigF9%2F8qT78cP9iTjKDLt0Ov7niSgePxanVGyXL%2FceyYiDso%2BrNsVO9l7%2Bw%2BZOg2M7E4moPy83l9LrnGKl9sQQ%2Fv8I7OZRVtk%2Bkn9C3ud3rXuoy5k6heWEtZ9TzEE&X-Amz-Signature=9f578405067a664c72fb5f8f6746edc3763d0ef88c61c5a93b6c1a13b9f9b0fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHBE7Y2L%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJsNYEzuZ26jSRpIgn0I6hlqAWWnJUTCfk%2FtZI%2BFzRDgIgYHRDWcMapX%2FsZTyUmJJK6FO34vbSH5zPp%2BWD7ixaE9cqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHNgjjRev%2BP4dDf5SrcA5X7zgBObygp2e%2FCRL4753bDcwDries5WFJA1bPAIxoQTNeADLt4%2FVKcs7GyFklUHDQlkctqLY%2Bqa%2FW%2FbqMmze36QX0dF58pBF9wShALGDRMUVzAfkNBW2p480HYjMbdzP9UYY07sOqa4HyH9yJ%2FaYLoDJ8YPQZnhO34jaEnXQUCmuya0evvb5g%2B1BITj7Qo1YXwF4n2N3hZ2BXz9EVBJjBG%2F7Bqzkp5iIXKy3nEPHrnjv%2Bfyn32k2F6AYBpvAtAQH2Ubpe3F8MD4hGWFtiG8gM8R12hL9jjo4EGBxXJTLLyAXChhwY71DLVsDeWbKoTty%2BtTN1xzQvVxR5eekcinrIW%2F96P2rzIWwvbJS%2B3yrJEDUc7D22nLPz8GOwhTtcuAPxXlRBfzaVfCp2zqv0E5xRgHgm7jasWRwmdsfjIeQLmFi5%2Fb8dIyE9bXFK7icXWwsag0aOS2uh4IiQB1YRK0gDaycVPADJoi0E4KLNUMaWmoQkgbKxzXy6AKT%2BNsyQBgMmxLZ39o75sbwhGv48fSRQb3KfL3PdAMIAXQniuN7ZcvqBXpAV1aQS02MdPWwwxSxyVJYVSQ75bRzUewdfqjobLAFaWyx1ejqPxNuJ7%2F2GEgGkTEw%2Bxn4ev%2F%2BAuMOrlwc4GOqUBgRTPK0IgBtJDHPP8Lwrwj6ECLEhKMg3d4A49SA7gMGXxh0FbG2eamJMAoh4Bei1GmCINOGr05t6IrjxfmJvqUIYQlnVUR41DigF9%2F8qT78cP9iTjKDLt0Ov7niSgePxanVGyXL%2FceyYiDso%2BrNsVO9l7%2Bw%2BZOg2M7E4moPy83l9LrnGKl9sQQ%2Fv8I7OZRVtk%2Bkn9C3ud3rXuoy5k6heWEtZ9TzEE&X-Amz-Signature=9f3731bf4a3e22fae26f61087d3060ae7731bed649521ee9cc51d3d0fcce6865&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHBE7Y2L%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJsNYEzuZ26jSRpIgn0I6hlqAWWnJUTCfk%2FtZI%2BFzRDgIgYHRDWcMapX%2FsZTyUmJJK6FO34vbSH5zPp%2BWD7ixaE9cqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHNgjjRev%2BP4dDf5SrcA5X7zgBObygp2e%2FCRL4753bDcwDries5WFJA1bPAIxoQTNeADLt4%2FVKcs7GyFklUHDQlkctqLY%2Bqa%2FW%2FbqMmze36QX0dF58pBF9wShALGDRMUVzAfkNBW2p480HYjMbdzP9UYY07sOqa4HyH9yJ%2FaYLoDJ8YPQZnhO34jaEnXQUCmuya0evvb5g%2B1BITj7Qo1YXwF4n2N3hZ2BXz9EVBJjBG%2F7Bqzkp5iIXKy3nEPHrnjv%2Bfyn32k2F6AYBpvAtAQH2Ubpe3F8MD4hGWFtiG8gM8R12hL9jjo4EGBxXJTLLyAXChhwY71DLVsDeWbKoTty%2BtTN1xzQvVxR5eekcinrIW%2F96P2rzIWwvbJS%2B3yrJEDUc7D22nLPz8GOwhTtcuAPxXlRBfzaVfCp2zqv0E5xRgHgm7jasWRwmdsfjIeQLmFi5%2Fb8dIyE9bXFK7icXWwsag0aOS2uh4IiQB1YRK0gDaycVPADJoi0E4KLNUMaWmoQkgbKxzXy6AKT%2BNsyQBgMmxLZ39o75sbwhGv48fSRQb3KfL3PdAMIAXQniuN7ZcvqBXpAV1aQS02MdPWwwxSxyVJYVSQ75bRzUewdfqjobLAFaWyx1ejqPxNuJ7%2F2GEgGkTEw%2Bxn4ev%2F%2BAuMOrlwc4GOqUBgRTPK0IgBtJDHPP8Lwrwj6ECLEhKMg3d4A49SA7gMGXxh0FbG2eamJMAoh4Bei1GmCINOGr05t6IrjxfmJvqUIYQlnVUR41DigF9%2F8qT78cP9iTjKDLt0Ov7niSgePxanVGyXL%2FceyYiDso%2BrNsVO9l7%2Bw%2BZOg2M7E4moPy83l9LrnGKl9sQQ%2Fv8I7OZRVtk%2Bkn9C3ud3rXuoy5k6heWEtZ9TzEE&X-Amz-Signature=f0d97ce0c5ce582a3552300fd23e9f4b064014933e84a04422808477bcf9b4a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHBE7Y2L%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJsNYEzuZ26jSRpIgn0I6hlqAWWnJUTCfk%2FtZI%2BFzRDgIgYHRDWcMapX%2FsZTyUmJJK6FO34vbSH5zPp%2BWD7ixaE9cqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHNgjjRev%2BP4dDf5SrcA5X7zgBObygp2e%2FCRL4753bDcwDries5WFJA1bPAIxoQTNeADLt4%2FVKcs7GyFklUHDQlkctqLY%2Bqa%2FW%2FbqMmze36QX0dF58pBF9wShALGDRMUVzAfkNBW2p480HYjMbdzP9UYY07sOqa4HyH9yJ%2FaYLoDJ8YPQZnhO34jaEnXQUCmuya0evvb5g%2B1BITj7Qo1YXwF4n2N3hZ2BXz9EVBJjBG%2F7Bqzkp5iIXKy3nEPHrnjv%2Bfyn32k2F6AYBpvAtAQH2Ubpe3F8MD4hGWFtiG8gM8R12hL9jjo4EGBxXJTLLyAXChhwY71DLVsDeWbKoTty%2BtTN1xzQvVxR5eekcinrIW%2F96P2rzIWwvbJS%2B3yrJEDUc7D22nLPz8GOwhTtcuAPxXlRBfzaVfCp2zqv0E5xRgHgm7jasWRwmdsfjIeQLmFi5%2Fb8dIyE9bXFK7icXWwsag0aOS2uh4IiQB1YRK0gDaycVPADJoi0E4KLNUMaWmoQkgbKxzXy6AKT%2BNsyQBgMmxLZ39o75sbwhGv48fSRQb3KfL3PdAMIAXQniuN7ZcvqBXpAV1aQS02MdPWwwxSxyVJYVSQ75bRzUewdfqjobLAFaWyx1ejqPxNuJ7%2F2GEgGkTEw%2Bxn4ev%2F%2BAuMOrlwc4GOqUBgRTPK0IgBtJDHPP8Lwrwj6ECLEhKMg3d4A49SA7gMGXxh0FbG2eamJMAoh4Bei1GmCINOGr05t6IrjxfmJvqUIYQlnVUR41DigF9%2F8qT78cP9iTjKDLt0Ov7niSgePxanVGyXL%2FceyYiDso%2BrNsVO9l7%2Bw%2BZOg2M7E4moPy83l9LrnGKl9sQQ%2Fv8I7OZRVtk%2Bkn9C3ud3rXuoy5k6heWEtZ9TzEE&X-Amz-Signature=95ff3699b0157e29d38b7a5fd7afdd6241bf899b6a015034dab3a943a3934806&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHBE7Y2L%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJsNYEzuZ26jSRpIgn0I6hlqAWWnJUTCfk%2FtZI%2BFzRDgIgYHRDWcMapX%2FsZTyUmJJK6FO34vbSH5zPp%2BWD7ixaE9cqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHNgjjRev%2BP4dDf5SrcA5X7zgBObygp2e%2FCRL4753bDcwDries5WFJA1bPAIxoQTNeADLt4%2FVKcs7GyFklUHDQlkctqLY%2Bqa%2FW%2FbqMmze36QX0dF58pBF9wShALGDRMUVzAfkNBW2p480HYjMbdzP9UYY07sOqa4HyH9yJ%2FaYLoDJ8YPQZnhO34jaEnXQUCmuya0evvb5g%2B1BITj7Qo1YXwF4n2N3hZ2BXz9EVBJjBG%2F7Bqzkp5iIXKy3nEPHrnjv%2Bfyn32k2F6AYBpvAtAQH2Ubpe3F8MD4hGWFtiG8gM8R12hL9jjo4EGBxXJTLLyAXChhwY71DLVsDeWbKoTty%2BtTN1xzQvVxR5eekcinrIW%2F96P2rzIWwvbJS%2B3yrJEDUc7D22nLPz8GOwhTtcuAPxXlRBfzaVfCp2zqv0E5xRgHgm7jasWRwmdsfjIeQLmFi5%2Fb8dIyE9bXFK7icXWwsag0aOS2uh4IiQB1YRK0gDaycVPADJoi0E4KLNUMaWmoQkgbKxzXy6AKT%2BNsyQBgMmxLZ39o75sbwhGv48fSRQb3KfL3PdAMIAXQniuN7ZcvqBXpAV1aQS02MdPWwwxSxyVJYVSQ75bRzUewdfqjobLAFaWyx1ejqPxNuJ7%2F2GEgGkTEw%2Bxn4ev%2F%2BAuMOrlwc4GOqUBgRTPK0IgBtJDHPP8Lwrwj6ECLEhKMg3d4A49SA7gMGXxh0FbG2eamJMAoh4Bei1GmCINOGr05t6IrjxfmJvqUIYQlnVUR41DigF9%2F8qT78cP9iTjKDLt0Ov7niSgePxanVGyXL%2FceyYiDso%2BrNsVO9l7%2Bw%2BZOg2M7E4moPy83l9LrnGKl9sQQ%2Fv8I7OZRVtk%2Bkn9C3ud3rXuoy5k6heWEtZ9TzEE&X-Amz-Signature=368c6a56f49ce142444e9435b6d87cfa29e5ba6f092a9675dd231868dbf939a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHBE7Y2L%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJsNYEzuZ26jSRpIgn0I6hlqAWWnJUTCfk%2FtZI%2BFzRDgIgYHRDWcMapX%2FsZTyUmJJK6FO34vbSH5zPp%2BWD7ixaE9cqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHNgjjRev%2BP4dDf5SrcA5X7zgBObygp2e%2FCRL4753bDcwDries5WFJA1bPAIxoQTNeADLt4%2FVKcs7GyFklUHDQlkctqLY%2Bqa%2FW%2FbqMmze36QX0dF58pBF9wShALGDRMUVzAfkNBW2p480HYjMbdzP9UYY07sOqa4HyH9yJ%2FaYLoDJ8YPQZnhO34jaEnXQUCmuya0evvb5g%2B1BITj7Qo1YXwF4n2N3hZ2BXz9EVBJjBG%2F7Bqzkp5iIXKy3nEPHrnjv%2Bfyn32k2F6AYBpvAtAQH2Ubpe3F8MD4hGWFtiG8gM8R12hL9jjo4EGBxXJTLLyAXChhwY71DLVsDeWbKoTty%2BtTN1xzQvVxR5eekcinrIW%2F96P2rzIWwvbJS%2B3yrJEDUc7D22nLPz8GOwhTtcuAPxXlRBfzaVfCp2zqv0E5xRgHgm7jasWRwmdsfjIeQLmFi5%2Fb8dIyE9bXFK7icXWwsag0aOS2uh4IiQB1YRK0gDaycVPADJoi0E4KLNUMaWmoQkgbKxzXy6AKT%2BNsyQBgMmxLZ39o75sbwhGv48fSRQb3KfL3PdAMIAXQniuN7ZcvqBXpAV1aQS02MdPWwwxSxyVJYVSQ75bRzUewdfqjobLAFaWyx1ejqPxNuJ7%2F2GEgGkTEw%2Bxn4ev%2F%2BAuMOrlwc4GOqUBgRTPK0IgBtJDHPP8Lwrwj6ECLEhKMg3d4A49SA7gMGXxh0FbG2eamJMAoh4Bei1GmCINOGr05t6IrjxfmJvqUIYQlnVUR41DigF9%2F8qT78cP9iTjKDLt0Ov7niSgePxanVGyXL%2FceyYiDso%2BrNsVO9l7%2Bw%2BZOg2M7E4moPy83l9LrnGKl9sQQ%2Fv8I7OZRVtk%2Bkn9C3ud3rXuoy5k6heWEtZ9TzEE&X-Amz-Signature=96c8a4b7df244c3ae2609591aa1b3432e227fc1e056706e60809e32237ad84ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

