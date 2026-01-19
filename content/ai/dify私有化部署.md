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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AKJ24CK%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwAHVtTPYycRZaiyC77VmKnPDxJ5OGb5gQqbQv%2FwENgAIgKOVoLpbIO2sqsgTwkX%2FZEdoLJUOdARQng%2Fbz2982GFIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPdcblSVXQfS7TXfircA9J10KIWCDMYUWCKjUWefnE1hOBEUhUZmPtELujlxbB6no3qNLdzdCPArLMO%2BvW7K8O%2F8rsgfEN3KsUpKbkE7ySd2zx5byt0ZQFq0DDIbQoWkoez4QvXMh3RftJHbhFjC05zQtPU2ATOO5jerF3yhnlacSA92MmH5a8zk9HO%2FSwOLFmZNN9hYQ78pwFrtXAlnxxOAkg9gbM9db9itdid26Ff%2FVWEMMo3wJiRBZQcM%2FNWkh5R%2FItbIA2DZNRRF83nidocbAzECgXgcqzB7Jq%2BaYCdQ79eLxzSmp32rsAcmpXnOIMTUIn8dOEZyP289w3IjQpPDLvz5Z4fbzXaJR9kwwAhAboALVHdXVXuyVc2JvXK%2FIkco4eVIlNxQF9x6rfWBKPf33IItVFbKjBH9PPJBTsN3hv29%2F9N4mGX7BVnLFAn0fE1CXhB%2BJ%2FUS4ysHhmZp8j3KU52ST2edSSe9oebxb24BIghgFqFMxy7KilZVpAHRG8iOmlU%2BGFpViAuJIbOw48s%2BRnayTrU%2BcTBpohVbOHSHcbQTK%2Bwuie2J6g6th1l9E5qw%2FZaiZyuZKbECu9oINlzzBwLMLbOoI20s9lmsfMb0WqIVKacHfzToDXm7wVfri%2Fb6k%2F%2FDPHz9qMXMOjctcsGOqUBo7OiikLdMApOmicaD%2BujjKQ6DdUlztHgDdiQ2z%2BmozDyVMnAWHr2%2FiFdk1K20R%2Fo6YrJni%2BZ56uVKrNlrqOfF5zY14lkjie8G6KFos1gIn51lQaL8brLeP4XWyAZMrRRKi3vdUrFaKSClEJpXGy%2FEDPhqW%2FwFzt71qk6HxfcK3emlVimsOrSxiYQs5KzR4loIBNjbcA4PkPbPs1wIOeLG8y4UL05&X-Amz-Signature=29fb9a323bbb99b19e967d7e01f6ecff96200257c0c2eb43f115a73786d3f4a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AKJ24CK%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwAHVtTPYycRZaiyC77VmKnPDxJ5OGb5gQqbQv%2FwENgAIgKOVoLpbIO2sqsgTwkX%2FZEdoLJUOdARQng%2Fbz2982GFIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPdcblSVXQfS7TXfircA9J10KIWCDMYUWCKjUWefnE1hOBEUhUZmPtELujlxbB6no3qNLdzdCPArLMO%2BvW7K8O%2F8rsgfEN3KsUpKbkE7ySd2zx5byt0ZQFq0DDIbQoWkoez4QvXMh3RftJHbhFjC05zQtPU2ATOO5jerF3yhnlacSA92MmH5a8zk9HO%2FSwOLFmZNN9hYQ78pwFrtXAlnxxOAkg9gbM9db9itdid26Ff%2FVWEMMo3wJiRBZQcM%2FNWkh5R%2FItbIA2DZNRRF83nidocbAzECgXgcqzB7Jq%2BaYCdQ79eLxzSmp32rsAcmpXnOIMTUIn8dOEZyP289w3IjQpPDLvz5Z4fbzXaJR9kwwAhAboALVHdXVXuyVc2JvXK%2FIkco4eVIlNxQF9x6rfWBKPf33IItVFbKjBH9PPJBTsN3hv29%2F9N4mGX7BVnLFAn0fE1CXhB%2BJ%2FUS4ysHhmZp8j3KU52ST2edSSe9oebxb24BIghgFqFMxy7KilZVpAHRG8iOmlU%2BGFpViAuJIbOw48s%2BRnayTrU%2BcTBpohVbOHSHcbQTK%2Bwuie2J6g6th1l9E5qw%2FZaiZyuZKbECu9oINlzzBwLMLbOoI20s9lmsfMb0WqIVKacHfzToDXm7wVfri%2Fb6k%2F%2FDPHz9qMXMOjctcsGOqUBo7OiikLdMApOmicaD%2BujjKQ6DdUlztHgDdiQ2z%2BmozDyVMnAWHr2%2FiFdk1K20R%2Fo6YrJni%2BZ56uVKrNlrqOfF5zY14lkjie8G6KFos1gIn51lQaL8brLeP4XWyAZMrRRKi3vdUrFaKSClEJpXGy%2FEDPhqW%2FwFzt71qk6HxfcK3emlVimsOrSxiYQs5KzR4loIBNjbcA4PkPbPs1wIOeLG8y4UL05&X-Amz-Signature=af7d5f9f37ff50bab1d3640bd312a0f9ceff60e3ad6fcce9bdac1f1c76f356d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AKJ24CK%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwAHVtTPYycRZaiyC77VmKnPDxJ5OGb5gQqbQv%2FwENgAIgKOVoLpbIO2sqsgTwkX%2FZEdoLJUOdARQng%2Fbz2982GFIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPdcblSVXQfS7TXfircA9J10KIWCDMYUWCKjUWefnE1hOBEUhUZmPtELujlxbB6no3qNLdzdCPArLMO%2BvW7K8O%2F8rsgfEN3KsUpKbkE7ySd2zx5byt0ZQFq0DDIbQoWkoez4QvXMh3RftJHbhFjC05zQtPU2ATOO5jerF3yhnlacSA92MmH5a8zk9HO%2FSwOLFmZNN9hYQ78pwFrtXAlnxxOAkg9gbM9db9itdid26Ff%2FVWEMMo3wJiRBZQcM%2FNWkh5R%2FItbIA2DZNRRF83nidocbAzECgXgcqzB7Jq%2BaYCdQ79eLxzSmp32rsAcmpXnOIMTUIn8dOEZyP289w3IjQpPDLvz5Z4fbzXaJR9kwwAhAboALVHdXVXuyVc2JvXK%2FIkco4eVIlNxQF9x6rfWBKPf33IItVFbKjBH9PPJBTsN3hv29%2F9N4mGX7BVnLFAn0fE1CXhB%2BJ%2FUS4ysHhmZp8j3KU52ST2edSSe9oebxb24BIghgFqFMxy7KilZVpAHRG8iOmlU%2BGFpViAuJIbOw48s%2BRnayTrU%2BcTBpohVbOHSHcbQTK%2Bwuie2J6g6th1l9E5qw%2FZaiZyuZKbECu9oINlzzBwLMLbOoI20s9lmsfMb0WqIVKacHfzToDXm7wVfri%2Fb6k%2F%2FDPHz9qMXMOjctcsGOqUBo7OiikLdMApOmicaD%2BujjKQ6DdUlztHgDdiQ2z%2BmozDyVMnAWHr2%2FiFdk1K20R%2Fo6YrJni%2BZ56uVKrNlrqOfF5zY14lkjie8G6KFos1gIn51lQaL8brLeP4XWyAZMrRRKi3vdUrFaKSClEJpXGy%2FEDPhqW%2FwFzt71qk6HxfcK3emlVimsOrSxiYQs5KzR4loIBNjbcA4PkPbPs1wIOeLG8y4UL05&X-Amz-Signature=a1667bb995b7f799205ba51faa48e92b003984f4bddfa8257fd57ddbd422a28d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AKJ24CK%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwAHVtTPYycRZaiyC77VmKnPDxJ5OGb5gQqbQv%2FwENgAIgKOVoLpbIO2sqsgTwkX%2FZEdoLJUOdARQng%2Fbz2982GFIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPdcblSVXQfS7TXfircA9J10KIWCDMYUWCKjUWefnE1hOBEUhUZmPtELujlxbB6no3qNLdzdCPArLMO%2BvW7K8O%2F8rsgfEN3KsUpKbkE7ySd2zx5byt0ZQFq0DDIbQoWkoez4QvXMh3RftJHbhFjC05zQtPU2ATOO5jerF3yhnlacSA92MmH5a8zk9HO%2FSwOLFmZNN9hYQ78pwFrtXAlnxxOAkg9gbM9db9itdid26Ff%2FVWEMMo3wJiRBZQcM%2FNWkh5R%2FItbIA2DZNRRF83nidocbAzECgXgcqzB7Jq%2BaYCdQ79eLxzSmp32rsAcmpXnOIMTUIn8dOEZyP289w3IjQpPDLvz5Z4fbzXaJR9kwwAhAboALVHdXVXuyVc2JvXK%2FIkco4eVIlNxQF9x6rfWBKPf33IItVFbKjBH9PPJBTsN3hv29%2F9N4mGX7BVnLFAn0fE1CXhB%2BJ%2FUS4ysHhmZp8j3KU52ST2edSSe9oebxb24BIghgFqFMxy7KilZVpAHRG8iOmlU%2BGFpViAuJIbOw48s%2BRnayTrU%2BcTBpohVbOHSHcbQTK%2Bwuie2J6g6th1l9E5qw%2FZaiZyuZKbECu9oINlzzBwLMLbOoI20s9lmsfMb0WqIVKacHfzToDXm7wVfri%2Fb6k%2F%2FDPHz9qMXMOjctcsGOqUBo7OiikLdMApOmicaD%2BujjKQ6DdUlztHgDdiQ2z%2BmozDyVMnAWHr2%2FiFdk1K20R%2Fo6YrJni%2BZ56uVKrNlrqOfF5zY14lkjie8G6KFos1gIn51lQaL8brLeP4XWyAZMrRRKi3vdUrFaKSClEJpXGy%2FEDPhqW%2FwFzt71qk6HxfcK3emlVimsOrSxiYQs5KzR4loIBNjbcA4PkPbPs1wIOeLG8y4UL05&X-Amz-Signature=2f4260432bbcea49d5775e4764704ec6ef4876eabfc7fc5704e5be11b8726182&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AKJ24CK%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwAHVtTPYycRZaiyC77VmKnPDxJ5OGb5gQqbQv%2FwENgAIgKOVoLpbIO2sqsgTwkX%2FZEdoLJUOdARQng%2Fbz2982GFIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPdcblSVXQfS7TXfircA9J10KIWCDMYUWCKjUWefnE1hOBEUhUZmPtELujlxbB6no3qNLdzdCPArLMO%2BvW7K8O%2F8rsgfEN3KsUpKbkE7ySd2zx5byt0ZQFq0DDIbQoWkoez4QvXMh3RftJHbhFjC05zQtPU2ATOO5jerF3yhnlacSA92MmH5a8zk9HO%2FSwOLFmZNN9hYQ78pwFrtXAlnxxOAkg9gbM9db9itdid26Ff%2FVWEMMo3wJiRBZQcM%2FNWkh5R%2FItbIA2DZNRRF83nidocbAzECgXgcqzB7Jq%2BaYCdQ79eLxzSmp32rsAcmpXnOIMTUIn8dOEZyP289w3IjQpPDLvz5Z4fbzXaJR9kwwAhAboALVHdXVXuyVc2JvXK%2FIkco4eVIlNxQF9x6rfWBKPf33IItVFbKjBH9PPJBTsN3hv29%2F9N4mGX7BVnLFAn0fE1CXhB%2BJ%2FUS4ysHhmZp8j3KU52ST2edSSe9oebxb24BIghgFqFMxy7KilZVpAHRG8iOmlU%2BGFpViAuJIbOw48s%2BRnayTrU%2BcTBpohVbOHSHcbQTK%2Bwuie2J6g6th1l9E5qw%2FZaiZyuZKbECu9oINlzzBwLMLbOoI20s9lmsfMb0WqIVKacHfzToDXm7wVfri%2Fb6k%2F%2FDPHz9qMXMOjctcsGOqUBo7OiikLdMApOmicaD%2BujjKQ6DdUlztHgDdiQ2z%2BmozDyVMnAWHr2%2FiFdk1K20R%2Fo6YrJni%2BZ56uVKrNlrqOfF5zY14lkjie8G6KFos1gIn51lQaL8brLeP4XWyAZMrRRKi3vdUrFaKSClEJpXGy%2FEDPhqW%2FwFzt71qk6HxfcK3emlVimsOrSxiYQs5KzR4loIBNjbcA4PkPbPs1wIOeLG8y4UL05&X-Amz-Signature=a3431144a82007cf680e5b4f341de511430e681a2953167cc4e0a7df3752645c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AKJ24CK%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwAHVtTPYycRZaiyC77VmKnPDxJ5OGb5gQqbQv%2FwENgAIgKOVoLpbIO2sqsgTwkX%2FZEdoLJUOdARQng%2Fbz2982GFIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPdcblSVXQfS7TXfircA9J10KIWCDMYUWCKjUWefnE1hOBEUhUZmPtELujlxbB6no3qNLdzdCPArLMO%2BvW7K8O%2F8rsgfEN3KsUpKbkE7ySd2zx5byt0ZQFq0DDIbQoWkoez4QvXMh3RftJHbhFjC05zQtPU2ATOO5jerF3yhnlacSA92MmH5a8zk9HO%2FSwOLFmZNN9hYQ78pwFrtXAlnxxOAkg9gbM9db9itdid26Ff%2FVWEMMo3wJiRBZQcM%2FNWkh5R%2FItbIA2DZNRRF83nidocbAzECgXgcqzB7Jq%2BaYCdQ79eLxzSmp32rsAcmpXnOIMTUIn8dOEZyP289w3IjQpPDLvz5Z4fbzXaJR9kwwAhAboALVHdXVXuyVc2JvXK%2FIkco4eVIlNxQF9x6rfWBKPf33IItVFbKjBH9PPJBTsN3hv29%2F9N4mGX7BVnLFAn0fE1CXhB%2BJ%2FUS4ysHhmZp8j3KU52ST2edSSe9oebxb24BIghgFqFMxy7KilZVpAHRG8iOmlU%2BGFpViAuJIbOw48s%2BRnayTrU%2BcTBpohVbOHSHcbQTK%2Bwuie2J6g6th1l9E5qw%2FZaiZyuZKbECu9oINlzzBwLMLbOoI20s9lmsfMb0WqIVKacHfzToDXm7wVfri%2Fb6k%2F%2FDPHz9qMXMOjctcsGOqUBo7OiikLdMApOmicaD%2BujjKQ6DdUlztHgDdiQ2z%2BmozDyVMnAWHr2%2FiFdk1K20R%2Fo6YrJni%2BZ56uVKrNlrqOfF5zY14lkjie8G6KFos1gIn51lQaL8brLeP4XWyAZMrRRKi3vdUrFaKSClEJpXGy%2FEDPhqW%2FwFzt71qk6HxfcK3emlVimsOrSxiYQs5KzR4loIBNjbcA4PkPbPs1wIOeLG8y4UL05&X-Amz-Signature=38ab2f674dd4d290e27f658fa3aa495d134b787dac56f8b04a7f2f117cba99df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AKJ24CK%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwAHVtTPYycRZaiyC77VmKnPDxJ5OGb5gQqbQv%2FwENgAIgKOVoLpbIO2sqsgTwkX%2FZEdoLJUOdARQng%2Fbz2982GFIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPdcblSVXQfS7TXfircA9J10KIWCDMYUWCKjUWefnE1hOBEUhUZmPtELujlxbB6no3qNLdzdCPArLMO%2BvW7K8O%2F8rsgfEN3KsUpKbkE7ySd2zx5byt0ZQFq0DDIbQoWkoez4QvXMh3RftJHbhFjC05zQtPU2ATOO5jerF3yhnlacSA92MmH5a8zk9HO%2FSwOLFmZNN9hYQ78pwFrtXAlnxxOAkg9gbM9db9itdid26Ff%2FVWEMMo3wJiRBZQcM%2FNWkh5R%2FItbIA2DZNRRF83nidocbAzECgXgcqzB7Jq%2BaYCdQ79eLxzSmp32rsAcmpXnOIMTUIn8dOEZyP289w3IjQpPDLvz5Z4fbzXaJR9kwwAhAboALVHdXVXuyVc2JvXK%2FIkco4eVIlNxQF9x6rfWBKPf33IItVFbKjBH9PPJBTsN3hv29%2F9N4mGX7BVnLFAn0fE1CXhB%2BJ%2FUS4ysHhmZp8j3KU52ST2edSSe9oebxb24BIghgFqFMxy7KilZVpAHRG8iOmlU%2BGFpViAuJIbOw48s%2BRnayTrU%2BcTBpohVbOHSHcbQTK%2Bwuie2J6g6th1l9E5qw%2FZaiZyuZKbECu9oINlzzBwLMLbOoI20s9lmsfMb0WqIVKacHfzToDXm7wVfri%2Fb6k%2F%2FDPHz9qMXMOjctcsGOqUBo7OiikLdMApOmicaD%2BujjKQ6DdUlztHgDdiQ2z%2BmozDyVMnAWHr2%2FiFdk1K20R%2Fo6YrJni%2BZ56uVKrNlrqOfF5zY14lkjie8G6KFos1gIn51lQaL8brLeP4XWyAZMrRRKi3vdUrFaKSClEJpXGy%2FEDPhqW%2FwFzt71qk6HxfcK3emlVimsOrSxiYQs5KzR4loIBNjbcA4PkPbPs1wIOeLG8y4UL05&X-Amz-Signature=121eeba3ad90aa137158931e4aa8b75245d22da1a9c2e312aa36fb014b133b19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AKJ24CK%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwAHVtTPYycRZaiyC77VmKnPDxJ5OGb5gQqbQv%2FwENgAIgKOVoLpbIO2sqsgTwkX%2FZEdoLJUOdARQng%2Fbz2982GFIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPdcblSVXQfS7TXfircA9J10KIWCDMYUWCKjUWefnE1hOBEUhUZmPtELujlxbB6no3qNLdzdCPArLMO%2BvW7K8O%2F8rsgfEN3KsUpKbkE7ySd2zx5byt0ZQFq0DDIbQoWkoez4QvXMh3RftJHbhFjC05zQtPU2ATOO5jerF3yhnlacSA92MmH5a8zk9HO%2FSwOLFmZNN9hYQ78pwFrtXAlnxxOAkg9gbM9db9itdid26Ff%2FVWEMMo3wJiRBZQcM%2FNWkh5R%2FItbIA2DZNRRF83nidocbAzECgXgcqzB7Jq%2BaYCdQ79eLxzSmp32rsAcmpXnOIMTUIn8dOEZyP289w3IjQpPDLvz5Z4fbzXaJR9kwwAhAboALVHdXVXuyVc2JvXK%2FIkco4eVIlNxQF9x6rfWBKPf33IItVFbKjBH9PPJBTsN3hv29%2F9N4mGX7BVnLFAn0fE1CXhB%2BJ%2FUS4ysHhmZp8j3KU52ST2edSSe9oebxb24BIghgFqFMxy7KilZVpAHRG8iOmlU%2BGFpViAuJIbOw48s%2BRnayTrU%2BcTBpohVbOHSHcbQTK%2Bwuie2J6g6th1l9E5qw%2FZaiZyuZKbECu9oINlzzBwLMLbOoI20s9lmsfMb0WqIVKacHfzToDXm7wVfri%2Fb6k%2F%2FDPHz9qMXMOjctcsGOqUBo7OiikLdMApOmicaD%2BujjKQ6DdUlztHgDdiQ2z%2BmozDyVMnAWHr2%2FiFdk1K20R%2Fo6YrJni%2BZ56uVKrNlrqOfF5zY14lkjie8G6KFos1gIn51lQaL8brLeP4XWyAZMrRRKi3vdUrFaKSClEJpXGy%2FEDPhqW%2FwFzt71qk6HxfcK3emlVimsOrSxiYQs5KzR4loIBNjbcA4PkPbPs1wIOeLG8y4UL05&X-Amz-Signature=db353d54bfb4a65102a6e9683336dd3239bf20cf30c504f8f037ffec9c687c22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AKJ24CK%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwAHVtTPYycRZaiyC77VmKnPDxJ5OGb5gQqbQv%2FwENgAIgKOVoLpbIO2sqsgTwkX%2FZEdoLJUOdARQng%2Fbz2982GFIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPdcblSVXQfS7TXfircA9J10KIWCDMYUWCKjUWefnE1hOBEUhUZmPtELujlxbB6no3qNLdzdCPArLMO%2BvW7K8O%2F8rsgfEN3KsUpKbkE7ySd2zx5byt0ZQFq0DDIbQoWkoez4QvXMh3RftJHbhFjC05zQtPU2ATOO5jerF3yhnlacSA92MmH5a8zk9HO%2FSwOLFmZNN9hYQ78pwFrtXAlnxxOAkg9gbM9db9itdid26Ff%2FVWEMMo3wJiRBZQcM%2FNWkh5R%2FItbIA2DZNRRF83nidocbAzECgXgcqzB7Jq%2BaYCdQ79eLxzSmp32rsAcmpXnOIMTUIn8dOEZyP289w3IjQpPDLvz5Z4fbzXaJR9kwwAhAboALVHdXVXuyVc2JvXK%2FIkco4eVIlNxQF9x6rfWBKPf33IItVFbKjBH9PPJBTsN3hv29%2F9N4mGX7BVnLFAn0fE1CXhB%2BJ%2FUS4ysHhmZp8j3KU52ST2edSSe9oebxb24BIghgFqFMxy7KilZVpAHRG8iOmlU%2BGFpViAuJIbOw48s%2BRnayTrU%2BcTBpohVbOHSHcbQTK%2Bwuie2J6g6th1l9E5qw%2FZaiZyuZKbECu9oINlzzBwLMLbOoI20s9lmsfMb0WqIVKacHfzToDXm7wVfri%2Fb6k%2F%2FDPHz9qMXMOjctcsGOqUBo7OiikLdMApOmicaD%2BujjKQ6DdUlztHgDdiQ2z%2BmozDyVMnAWHr2%2FiFdk1K20R%2Fo6YrJni%2BZ56uVKrNlrqOfF5zY14lkjie8G6KFos1gIn51lQaL8brLeP4XWyAZMrRRKi3vdUrFaKSClEJpXGy%2FEDPhqW%2FwFzt71qk6HxfcK3emlVimsOrSxiYQs5KzR4loIBNjbcA4PkPbPs1wIOeLG8y4UL05&X-Amz-Signature=d6df118da8b2bf540987344cc4d5855a6881e577404363ad253fea26f3f2c087&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AKJ24CK%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwAHVtTPYycRZaiyC77VmKnPDxJ5OGb5gQqbQv%2FwENgAIgKOVoLpbIO2sqsgTwkX%2FZEdoLJUOdARQng%2Fbz2982GFIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPdcblSVXQfS7TXfircA9J10KIWCDMYUWCKjUWefnE1hOBEUhUZmPtELujlxbB6no3qNLdzdCPArLMO%2BvW7K8O%2F8rsgfEN3KsUpKbkE7ySd2zx5byt0ZQFq0DDIbQoWkoez4QvXMh3RftJHbhFjC05zQtPU2ATOO5jerF3yhnlacSA92MmH5a8zk9HO%2FSwOLFmZNN9hYQ78pwFrtXAlnxxOAkg9gbM9db9itdid26Ff%2FVWEMMo3wJiRBZQcM%2FNWkh5R%2FItbIA2DZNRRF83nidocbAzECgXgcqzB7Jq%2BaYCdQ79eLxzSmp32rsAcmpXnOIMTUIn8dOEZyP289w3IjQpPDLvz5Z4fbzXaJR9kwwAhAboALVHdXVXuyVc2JvXK%2FIkco4eVIlNxQF9x6rfWBKPf33IItVFbKjBH9PPJBTsN3hv29%2F9N4mGX7BVnLFAn0fE1CXhB%2BJ%2FUS4ysHhmZp8j3KU52ST2edSSe9oebxb24BIghgFqFMxy7KilZVpAHRG8iOmlU%2BGFpViAuJIbOw48s%2BRnayTrU%2BcTBpohVbOHSHcbQTK%2Bwuie2J6g6th1l9E5qw%2FZaiZyuZKbECu9oINlzzBwLMLbOoI20s9lmsfMb0WqIVKacHfzToDXm7wVfri%2Fb6k%2F%2FDPHz9qMXMOjctcsGOqUBo7OiikLdMApOmicaD%2BujjKQ6DdUlztHgDdiQ2z%2BmozDyVMnAWHr2%2FiFdk1K20R%2Fo6YrJni%2BZ56uVKrNlrqOfF5zY14lkjie8G6KFos1gIn51lQaL8brLeP4XWyAZMrRRKi3vdUrFaKSClEJpXGy%2FEDPhqW%2FwFzt71qk6HxfcK3emlVimsOrSxiYQs5KzR4loIBNjbcA4PkPbPs1wIOeLG8y4UL05&X-Amz-Signature=07415faa3ddd73443a0f72b79c890705c58bd6725161c07e2537d032bebf5400&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

