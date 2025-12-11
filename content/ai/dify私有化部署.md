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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFII4UMI%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCESTkctg0taQcQPBJ1NKYLQVLuPMNqON1x7lLQ58YTsgIgLQucrZHggRGdQb8x8WT2gqFBVG3pOa%2F2E4R7Vsx4WawqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8cvJek6SZjMAWooCrcAzQ10lkgYksQH60qT%2F%2BnFbpjLgux2sf3TKHOUhvSazEL6eF7iflrutLh8Zd5kLabfrGbognjzdqZ3Y%2FSboOGwkuAQcbOyVRj45C%2BY524gJiv6mIgIz4%2BxQadW%2F7KzS13rx5Sae73jtFuJfQbiGl2kMew3yPQNxYRZhZ6aaKJKAzt%2B6EMftalS57mFXReUoZVskAGP0Q9NP15r10EKJ70mtYfOeZ4HF6EKLmY756wkxI0GzBhuOYOfUQKcVKRaNvSHCtrFpTyVSCuiCApIYRi3q%2FRzcHwatLyO2j%2BJvExAeGvcLARVXtIm02pBNOFLyU%2FuDfmSLgWgNeQZHKmxL%2FIxAYkls6C3zOM1ko6os%2BveU4Wy0Eop7FTPLMDKrU%2B1dNAJ9b5y4Y7Lx5s8oTGJRcNMHdU8FOLFhmLRotI3aXS%2F1zHSSf5vwO0lHWdTvWeThSWKZw9YCfv9lmy7H1qMYaVdpCWhyaYfXNaUgJ%2BcAnJo7a6VxS5tGuYg5g4RucXOSm8bM0tpOwYc2UakTyqewCYbKoFIKowAg2M6xLHhP%2BTV9AoGZMvHRiNvlh%2Bo17n8%2FlijFmRwbk2PFqfPQY%2FlPLpZXzzkg0ZkR7j53XcMwihw%2B6DoWq6BBRaIM5%2Fg6d6MOa06MkGOqUBU8Djx1ab9qvmAVefN3WBJtEVvO51KZunEBMNWQKOu2FoLZ69XQG5Cej92NlJY3jJBc55aoPXIg%2FhPztcMn5LyvLniaX6ly6advyRFKnh6P9I1SKH%2Bc1jjmtp3NTM0moQV4EzXq3rti5Zo45%2Fa3lC3hy1P04%2F6L5jcOzTAj9s%2F0xuPflWHdmAofGhnbBpUQoFBcFycJtyw%2BDGpnfmpBQIeUVtxthT&X-Amz-Signature=3ebde94a5a711dde7682221cb2ff24c1907e4accd83c3aba49f7fa08ec6ec2d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFII4UMI%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCESTkctg0taQcQPBJ1NKYLQVLuPMNqON1x7lLQ58YTsgIgLQucrZHggRGdQb8x8WT2gqFBVG3pOa%2F2E4R7Vsx4WawqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8cvJek6SZjMAWooCrcAzQ10lkgYksQH60qT%2F%2BnFbpjLgux2sf3TKHOUhvSazEL6eF7iflrutLh8Zd5kLabfrGbognjzdqZ3Y%2FSboOGwkuAQcbOyVRj45C%2BY524gJiv6mIgIz4%2BxQadW%2F7KzS13rx5Sae73jtFuJfQbiGl2kMew3yPQNxYRZhZ6aaKJKAzt%2B6EMftalS57mFXReUoZVskAGP0Q9NP15r10EKJ70mtYfOeZ4HF6EKLmY756wkxI0GzBhuOYOfUQKcVKRaNvSHCtrFpTyVSCuiCApIYRi3q%2FRzcHwatLyO2j%2BJvExAeGvcLARVXtIm02pBNOFLyU%2FuDfmSLgWgNeQZHKmxL%2FIxAYkls6C3zOM1ko6os%2BveU4Wy0Eop7FTPLMDKrU%2B1dNAJ9b5y4Y7Lx5s8oTGJRcNMHdU8FOLFhmLRotI3aXS%2F1zHSSf5vwO0lHWdTvWeThSWKZw9YCfv9lmy7H1qMYaVdpCWhyaYfXNaUgJ%2BcAnJo7a6VxS5tGuYg5g4RucXOSm8bM0tpOwYc2UakTyqewCYbKoFIKowAg2M6xLHhP%2BTV9AoGZMvHRiNvlh%2Bo17n8%2FlijFmRwbk2PFqfPQY%2FlPLpZXzzkg0ZkR7j53XcMwihw%2B6DoWq6BBRaIM5%2Fg6d6MOa06MkGOqUBU8Djx1ab9qvmAVefN3WBJtEVvO51KZunEBMNWQKOu2FoLZ69XQG5Cej92NlJY3jJBc55aoPXIg%2FhPztcMn5LyvLniaX6ly6advyRFKnh6P9I1SKH%2Bc1jjmtp3NTM0moQV4EzXq3rti5Zo45%2Fa3lC3hy1P04%2F6L5jcOzTAj9s%2F0xuPflWHdmAofGhnbBpUQoFBcFycJtyw%2BDGpnfmpBQIeUVtxthT&X-Amz-Signature=22b9a83604f4f966e46262449247946eb4b940c67ae302201f7b2118bb6a33ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFII4UMI%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCESTkctg0taQcQPBJ1NKYLQVLuPMNqON1x7lLQ58YTsgIgLQucrZHggRGdQb8x8WT2gqFBVG3pOa%2F2E4R7Vsx4WawqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8cvJek6SZjMAWooCrcAzQ10lkgYksQH60qT%2F%2BnFbpjLgux2sf3TKHOUhvSazEL6eF7iflrutLh8Zd5kLabfrGbognjzdqZ3Y%2FSboOGwkuAQcbOyVRj45C%2BY524gJiv6mIgIz4%2BxQadW%2F7KzS13rx5Sae73jtFuJfQbiGl2kMew3yPQNxYRZhZ6aaKJKAzt%2B6EMftalS57mFXReUoZVskAGP0Q9NP15r10EKJ70mtYfOeZ4HF6EKLmY756wkxI0GzBhuOYOfUQKcVKRaNvSHCtrFpTyVSCuiCApIYRi3q%2FRzcHwatLyO2j%2BJvExAeGvcLARVXtIm02pBNOFLyU%2FuDfmSLgWgNeQZHKmxL%2FIxAYkls6C3zOM1ko6os%2BveU4Wy0Eop7FTPLMDKrU%2B1dNAJ9b5y4Y7Lx5s8oTGJRcNMHdU8FOLFhmLRotI3aXS%2F1zHSSf5vwO0lHWdTvWeThSWKZw9YCfv9lmy7H1qMYaVdpCWhyaYfXNaUgJ%2BcAnJo7a6VxS5tGuYg5g4RucXOSm8bM0tpOwYc2UakTyqewCYbKoFIKowAg2M6xLHhP%2BTV9AoGZMvHRiNvlh%2Bo17n8%2FlijFmRwbk2PFqfPQY%2FlPLpZXzzkg0ZkR7j53XcMwihw%2B6DoWq6BBRaIM5%2Fg6d6MOa06MkGOqUBU8Djx1ab9qvmAVefN3WBJtEVvO51KZunEBMNWQKOu2FoLZ69XQG5Cej92NlJY3jJBc55aoPXIg%2FhPztcMn5LyvLniaX6ly6advyRFKnh6P9I1SKH%2Bc1jjmtp3NTM0moQV4EzXq3rti5Zo45%2Fa3lC3hy1P04%2F6L5jcOzTAj9s%2F0xuPflWHdmAofGhnbBpUQoFBcFycJtyw%2BDGpnfmpBQIeUVtxthT&X-Amz-Signature=962b0661a48dbd3dbe99c9d6d2f07c1a25c32d0e77e4fa6467a83ed46cf5d129&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFII4UMI%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCESTkctg0taQcQPBJ1NKYLQVLuPMNqON1x7lLQ58YTsgIgLQucrZHggRGdQb8x8WT2gqFBVG3pOa%2F2E4R7Vsx4WawqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8cvJek6SZjMAWooCrcAzQ10lkgYksQH60qT%2F%2BnFbpjLgux2sf3TKHOUhvSazEL6eF7iflrutLh8Zd5kLabfrGbognjzdqZ3Y%2FSboOGwkuAQcbOyVRj45C%2BY524gJiv6mIgIz4%2BxQadW%2F7KzS13rx5Sae73jtFuJfQbiGl2kMew3yPQNxYRZhZ6aaKJKAzt%2B6EMftalS57mFXReUoZVskAGP0Q9NP15r10EKJ70mtYfOeZ4HF6EKLmY756wkxI0GzBhuOYOfUQKcVKRaNvSHCtrFpTyVSCuiCApIYRi3q%2FRzcHwatLyO2j%2BJvExAeGvcLARVXtIm02pBNOFLyU%2FuDfmSLgWgNeQZHKmxL%2FIxAYkls6C3zOM1ko6os%2BveU4Wy0Eop7FTPLMDKrU%2B1dNAJ9b5y4Y7Lx5s8oTGJRcNMHdU8FOLFhmLRotI3aXS%2F1zHSSf5vwO0lHWdTvWeThSWKZw9YCfv9lmy7H1qMYaVdpCWhyaYfXNaUgJ%2BcAnJo7a6VxS5tGuYg5g4RucXOSm8bM0tpOwYc2UakTyqewCYbKoFIKowAg2M6xLHhP%2BTV9AoGZMvHRiNvlh%2Bo17n8%2FlijFmRwbk2PFqfPQY%2FlPLpZXzzkg0ZkR7j53XcMwihw%2B6DoWq6BBRaIM5%2Fg6d6MOa06MkGOqUBU8Djx1ab9qvmAVefN3WBJtEVvO51KZunEBMNWQKOu2FoLZ69XQG5Cej92NlJY3jJBc55aoPXIg%2FhPztcMn5LyvLniaX6ly6advyRFKnh6P9I1SKH%2Bc1jjmtp3NTM0moQV4EzXq3rti5Zo45%2Fa3lC3hy1P04%2F6L5jcOzTAj9s%2F0xuPflWHdmAofGhnbBpUQoFBcFycJtyw%2BDGpnfmpBQIeUVtxthT&X-Amz-Signature=18c8a711c0675a81d92e2217128182b9c1b7c5a59ee1147302e6d0f26926c618&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFII4UMI%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCESTkctg0taQcQPBJ1NKYLQVLuPMNqON1x7lLQ58YTsgIgLQucrZHggRGdQb8x8WT2gqFBVG3pOa%2F2E4R7Vsx4WawqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8cvJek6SZjMAWooCrcAzQ10lkgYksQH60qT%2F%2BnFbpjLgux2sf3TKHOUhvSazEL6eF7iflrutLh8Zd5kLabfrGbognjzdqZ3Y%2FSboOGwkuAQcbOyVRj45C%2BY524gJiv6mIgIz4%2BxQadW%2F7KzS13rx5Sae73jtFuJfQbiGl2kMew3yPQNxYRZhZ6aaKJKAzt%2B6EMftalS57mFXReUoZVskAGP0Q9NP15r10EKJ70mtYfOeZ4HF6EKLmY756wkxI0GzBhuOYOfUQKcVKRaNvSHCtrFpTyVSCuiCApIYRi3q%2FRzcHwatLyO2j%2BJvExAeGvcLARVXtIm02pBNOFLyU%2FuDfmSLgWgNeQZHKmxL%2FIxAYkls6C3zOM1ko6os%2BveU4Wy0Eop7FTPLMDKrU%2B1dNAJ9b5y4Y7Lx5s8oTGJRcNMHdU8FOLFhmLRotI3aXS%2F1zHSSf5vwO0lHWdTvWeThSWKZw9YCfv9lmy7H1qMYaVdpCWhyaYfXNaUgJ%2BcAnJo7a6VxS5tGuYg5g4RucXOSm8bM0tpOwYc2UakTyqewCYbKoFIKowAg2M6xLHhP%2BTV9AoGZMvHRiNvlh%2Bo17n8%2FlijFmRwbk2PFqfPQY%2FlPLpZXzzkg0ZkR7j53XcMwihw%2B6DoWq6BBRaIM5%2Fg6d6MOa06MkGOqUBU8Djx1ab9qvmAVefN3WBJtEVvO51KZunEBMNWQKOu2FoLZ69XQG5Cej92NlJY3jJBc55aoPXIg%2FhPztcMn5LyvLniaX6ly6advyRFKnh6P9I1SKH%2Bc1jjmtp3NTM0moQV4EzXq3rti5Zo45%2Fa3lC3hy1P04%2F6L5jcOzTAj9s%2F0xuPflWHdmAofGhnbBpUQoFBcFycJtyw%2BDGpnfmpBQIeUVtxthT&X-Amz-Signature=7bc2f7728c8e9cd613b5fbb730e9ae248015d09a6739aff8ce6b49ab680b9638&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFII4UMI%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCESTkctg0taQcQPBJ1NKYLQVLuPMNqON1x7lLQ58YTsgIgLQucrZHggRGdQb8x8WT2gqFBVG3pOa%2F2E4R7Vsx4WawqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8cvJek6SZjMAWooCrcAzQ10lkgYksQH60qT%2F%2BnFbpjLgux2sf3TKHOUhvSazEL6eF7iflrutLh8Zd5kLabfrGbognjzdqZ3Y%2FSboOGwkuAQcbOyVRj45C%2BY524gJiv6mIgIz4%2BxQadW%2F7KzS13rx5Sae73jtFuJfQbiGl2kMew3yPQNxYRZhZ6aaKJKAzt%2B6EMftalS57mFXReUoZVskAGP0Q9NP15r10EKJ70mtYfOeZ4HF6EKLmY756wkxI0GzBhuOYOfUQKcVKRaNvSHCtrFpTyVSCuiCApIYRi3q%2FRzcHwatLyO2j%2BJvExAeGvcLARVXtIm02pBNOFLyU%2FuDfmSLgWgNeQZHKmxL%2FIxAYkls6C3zOM1ko6os%2BveU4Wy0Eop7FTPLMDKrU%2B1dNAJ9b5y4Y7Lx5s8oTGJRcNMHdU8FOLFhmLRotI3aXS%2F1zHSSf5vwO0lHWdTvWeThSWKZw9YCfv9lmy7H1qMYaVdpCWhyaYfXNaUgJ%2BcAnJo7a6VxS5tGuYg5g4RucXOSm8bM0tpOwYc2UakTyqewCYbKoFIKowAg2M6xLHhP%2BTV9AoGZMvHRiNvlh%2Bo17n8%2FlijFmRwbk2PFqfPQY%2FlPLpZXzzkg0ZkR7j53XcMwihw%2B6DoWq6BBRaIM5%2Fg6d6MOa06MkGOqUBU8Djx1ab9qvmAVefN3WBJtEVvO51KZunEBMNWQKOu2FoLZ69XQG5Cej92NlJY3jJBc55aoPXIg%2FhPztcMn5LyvLniaX6ly6advyRFKnh6P9I1SKH%2Bc1jjmtp3NTM0moQV4EzXq3rti5Zo45%2Fa3lC3hy1P04%2F6L5jcOzTAj9s%2F0xuPflWHdmAofGhnbBpUQoFBcFycJtyw%2BDGpnfmpBQIeUVtxthT&X-Amz-Signature=c69f9c05e231a7c4890095c7636138db4a227edccb534dd2e891081285cd7b1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFII4UMI%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCESTkctg0taQcQPBJ1NKYLQVLuPMNqON1x7lLQ58YTsgIgLQucrZHggRGdQb8x8WT2gqFBVG3pOa%2F2E4R7Vsx4WawqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8cvJek6SZjMAWooCrcAzQ10lkgYksQH60qT%2F%2BnFbpjLgux2sf3TKHOUhvSazEL6eF7iflrutLh8Zd5kLabfrGbognjzdqZ3Y%2FSboOGwkuAQcbOyVRj45C%2BY524gJiv6mIgIz4%2BxQadW%2F7KzS13rx5Sae73jtFuJfQbiGl2kMew3yPQNxYRZhZ6aaKJKAzt%2B6EMftalS57mFXReUoZVskAGP0Q9NP15r10EKJ70mtYfOeZ4HF6EKLmY756wkxI0GzBhuOYOfUQKcVKRaNvSHCtrFpTyVSCuiCApIYRi3q%2FRzcHwatLyO2j%2BJvExAeGvcLARVXtIm02pBNOFLyU%2FuDfmSLgWgNeQZHKmxL%2FIxAYkls6C3zOM1ko6os%2BveU4Wy0Eop7FTPLMDKrU%2B1dNAJ9b5y4Y7Lx5s8oTGJRcNMHdU8FOLFhmLRotI3aXS%2F1zHSSf5vwO0lHWdTvWeThSWKZw9YCfv9lmy7H1qMYaVdpCWhyaYfXNaUgJ%2BcAnJo7a6VxS5tGuYg5g4RucXOSm8bM0tpOwYc2UakTyqewCYbKoFIKowAg2M6xLHhP%2BTV9AoGZMvHRiNvlh%2Bo17n8%2FlijFmRwbk2PFqfPQY%2FlPLpZXzzkg0ZkR7j53XcMwihw%2B6DoWq6BBRaIM5%2Fg6d6MOa06MkGOqUBU8Djx1ab9qvmAVefN3WBJtEVvO51KZunEBMNWQKOu2FoLZ69XQG5Cej92NlJY3jJBc55aoPXIg%2FhPztcMn5LyvLniaX6ly6advyRFKnh6P9I1SKH%2Bc1jjmtp3NTM0moQV4EzXq3rti5Zo45%2Fa3lC3hy1P04%2F6L5jcOzTAj9s%2F0xuPflWHdmAofGhnbBpUQoFBcFycJtyw%2BDGpnfmpBQIeUVtxthT&X-Amz-Signature=de99eacf602f882dd40e1bd571bf963f374db924b3c2c691611ca88d50ab2b52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFII4UMI%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCESTkctg0taQcQPBJ1NKYLQVLuPMNqON1x7lLQ58YTsgIgLQucrZHggRGdQb8x8WT2gqFBVG3pOa%2F2E4R7Vsx4WawqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8cvJek6SZjMAWooCrcAzQ10lkgYksQH60qT%2F%2BnFbpjLgux2sf3TKHOUhvSazEL6eF7iflrutLh8Zd5kLabfrGbognjzdqZ3Y%2FSboOGwkuAQcbOyVRj45C%2BY524gJiv6mIgIz4%2BxQadW%2F7KzS13rx5Sae73jtFuJfQbiGl2kMew3yPQNxYRZhZ6aaKJKAzt%2B6EMftalS57mFXReUoZVskAGP0Q9NP15r10EKJ70mtYfOeZ4HF6EKLmY756wkxI0GzBhuOYOfUQKcVKRaNvSHCtrFpTyVSCuiCApIYRi3q%2FRzcHwatLyO2j%2BJvExAeGvcLARVXtIm02pBNOFLyU%2FuDfmSLgWgNeQZHKmxL%2FIxAYkls6C3zOM1ko6os%2BveU4Wy0Eop7FTPLMDKrU%2B1dNAJ9b5y4Y7Lx5s8oTGJRcNMHdU8FOLFhmLRotI3aXS%2F1zHSSf5vwO0lHWdTvWeThSWKZw9YCfv9lmy7H1qMYaVdpCWhyaYfXNaUgJ%2BcAnJo7a6VxS5tGuYg5g4RucXOSm8bM0tpOwYc2UakTyqewCYbKoFIKowAg2M6xLHhP%2BTV9AoGZMvHRiNvlh%2Bo17n8%2FlijFmRwbk2PFqfPQY%2FlPLpZXzzkg0ZkR7j53XcMwihw%2B6DoWq6BBRaIM5%2Fg6d6MOa06MkGOqUBU8Djx1ab9qvmAVefN3WBJtEVvO51KZunEBMNWQKOu2FoLZ69XQG5Cej92NlJY3jJBc55aoPXIg%2FhPztcMn5LyvLniaX6ly6advyRFKnh6P9I1SKH%2Bc1jjmtp3NTM0moQV4EzXq3rti5Zo45%2Fa3lC3hy1P04%2F6L5jcOzTAj9s%2F0xuPflWHdmAofGhnbBpUQoFBcFycJtyw%2BDGpnfmpBQIeUVtxthT&X-Amz-Signature=66385b70d443b6190504f660680df0b7b74c8456ef9632d0d59f38f02e50b748&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFII4UMI%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCESTkctg0taQcQPBJ1NKYLQVLuPMNqON1x7lLQ58YTsgIgLQucrZHggRGdQb8x8WT2gqFBVG3pOa%2F2E4R7Vsx4WawqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8cvJek6SZjMAWooCrcAzQ10lkgYksQH60qT%2F%2BnFbpjLgux2sf3TKHOUhvSazEL6eF7iflrutLh8Zd5kLabfrGbognjzdqZ3Y%2FSboOGwkuAQcbOyVRj45C%2BY524gJiv6mIgIz4%2BxQadW%2F7KzS13rx5Sae73jtFuJfQbiGl2kMew3yPQNxYRZhZ6aaKJKAzt%2B6EMftalS57mFXReUoZVskAGP0Q9NP15r10EKJ70mtYfOeZ4HF6EKLmY756wkxI0GzBhuOYOfUQKcVKRaNvSHCtrFpTyVSCuiCApIYRi3q%2FRzcHwatLyO2j%2BJvExAeGvcLARVXtIm02pBNOFLyU%2FuDfmSLgWgNeQZHKmxL%2FIxAYkls6C3zOM1ko6os%2BveU4Wy0Eop7FTPLMDKrU%2B1dNAJ9b5y4Y7Lx5s8oTGJRcNMHdU8FOLFhmLRotI3aXS%2F1zHSSf5vwO0lHWdTvWeThSWKZw9YCfv9lmy7H1qMYaVdpCWhyaYfXNaUgJ%2BcAnJo7a6VxS5tGuYg5g4RucXOSm8bM0tpOwYc2UakTyqewCYbKoFIKowAg2M6xLHhP%2BTV9AoGZMvHRiNvlh%2Bo17n8%2FlijFmRwbk2PFqfPQY%2FlPLpZXzzkg0ZkR7j53XcMwihw%2B6DoWq6BBRaIM5%2Fg6d6MOa06MkGOqUBU8Djx1ab9qvmAVefN3WBJtEVvO51KZunEBMNWQKOu2FoLZ69XQG5Cej92NlJY3jJBc55aoPXIg%2FhPztcMn5LyvLniaX6ly6advyRFKnh6P9I1SKH%2Bc1jjmtp3NTM0moQV4EzXq3rti5Zo45%2Fa3lC3hy1P04%2F6L5jcOzTAj9s%2F0xuPflWHdmAofGhnbBpUQoFBcFycJtyw%2BDGpnfmpBQIeUVtxthT&X-Amz-Signature=7af0bbafee1517b17be57dfb704d67090ab53c7a741c7aef0f2f873f0dffd700&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFII4UMI%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCESTkctg0taQcQPBJ1NKYLQVLuPMNqON1x7lLQ58YTsgIgLQucrZHggRGdQb8x8WT2gqFBVG3pOa%2F2E4R7Vsx4WawqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN8cvJek6SZjMAWooCrcAzQ10lkgYksQH60qT%2F%2BnFbpjLgux2sf3TKHOUhvSazEL6eF7iflrutLh8Zd5kLabfrGbognjzdqZ3Y%2FSboOGwkuAQcbOyVRj45C%2BY524gJiv6mIgIz4%2BxQadW%2F7KzS13rx5Sae73jtFuJfQbiGl2kMew3yPQNxYRZhZ6aaKJKAzt%2B6EMftalS57mFXReUoZVskAGP0Q9NP15r10EKJ70mtYfOeZ4HF6EKLmY756wkxI0GzBhuOYOfUQKcVKRaNvSHCtrFpTyVSCuiCApIYRi3q%2FRzcHwatLyO2j%2BJvExAeGvcLARVXtIm02pBNOFLyU%2FuDfmSLgWgNeQZHKmxL%2FIxAYkls6C3zOM1ko6os%2BveU4Wy0Eop7FTPLMDKrU%2B1dNAJ9b5y4Y7Lx5s8oTGJRcNMHdU8FOLFhmLRotI3aXS%2F1zHSSf5vwO0lHWdTvWeThSWKZw9YCfv9lmy7H1qMYaVdpCWhyaYfXNaUgJ%2BcAnJo7a6VxS5tGuYg5g4RucXOSm8bM0tpOwYc2UakTyqewCYbKoFIKowAg2M6xLHhP%2BTV9AoGZMvHRiNvlh%2Bo17n8%2FlijFmRwbk2PFqfPQY%2FlPLpZXzzkg0ZkR7j53XcMwihw%2B6DoWq6BBRaIM5%2Fg6d6MOa06MkGOqUBU8Djx1ab9qvmAVefN3WBJtEVvO51KZunEBMNWQKOu2FoLZ69XQG5Cej92NlJY3jJBc55aoPXIg%2FhPztcMn5LyvLniaX6ly6advyRFKnh6P9I1SKH%2Bc1jjmtp3NTM0moQV4EzXq3rti5Zo45%2Fa3lC3hy1P04%2F6L5jcOzTAj9s%2F0xuPflWHdmAofGhnbBpUQoFBcFycJtyw%2BDGpnfmpBQIeUVtxthT&X-Amz-Signature=a51df3c2b4f0e9e1698e246a625d07eabe6ffd5b4dcde46af5b8e576b9e03d85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

