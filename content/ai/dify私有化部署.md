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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTJMKY6Q%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCQJ8Wz139zeVsG3bQAC%2Bjzitsjc3kl%2B15BkJ%2FesdB8KwIhALyw3bldNUBNFDIv9iK5Y5SeUc%2BwBgPFzBLrY9Yj5RrXKv8DCAwQABoMNjM3NDIzMTgzODA1IgyiEf9TYxQuGIk%2FX9Yq3AMXrho%2FTfweZH185Y53rME%2B0Rn3TVTiLiTvCsMuXJgsqjcWaP0RIKt3LXh7TB5ecOwqbiFAMg%2FkVFYKL6a8L1aR7C%2F9FDYbE2QRGElOb%2BhwTS%2BXI2hYcU3ZGC74Ivd7%2BGkthY56UDWV2BHB9HLGthD01gA5ip6z0KsKgJQqQhsHrqE4jGD%2BXx796Tz4F4rxnvBkKxnNRgcOTnip7rFdIJfgdaflJmPjATxDRkulk8%2By6ImViLrgCn4wm2ND1tHIBZghF3S2TMs0RXTdw1NoPDu55Nl1sWpaOcgkdRYEHVco7y39BxAk984h27iffI157DyPfduJ5TVFmyL0uFi1b6WM7bbYtRtze1dKlLhctGLLAGzKZYafYi30zVH86U22Saq15quJwUEWc0ny6DrLSO58Qo6xx7uG4yg11p6hySCECmzJKlBGsgvnjDtVY7dNKtbwV3TqMRh2wktNrecFfymffs01LU0iFAH5SkGhbvqIuB7QF%2BYFBT%2FgtTA9b1hDLkOy5pfSK9ZCb3rS6zJpYqxtiZj5Jcs6E1cFtD9zyyil0daKvxzPhZyawYRz%2BsFi5B4mea%2BBc4VMw0Daqz%2BcP2jwTz6t%2BK39hEHcq2SS9kjdfvlyyjtsbkO3SXlB2TCLwrPNBjqkAWZClN6d5Q7soXFPZk31BC4RyKIjllFnQ%2BdPmV4szoT%2FVP7H50S1u9h80imYBzRJd6rI%2FEUfs5o6zxYPTPVpfpnedOeRIs1kcuBzpipOjcvWF1cTF5vXCMtNKGqAUjaKO8nEaJDEz%2FgAMd4qfiJQOlAFo5KffgJfpDVDQYeMJZjplvliFVWShFP272mZGVmrd%2BDlO%2Bg56oNWUIuOxDP0OX%2BQYrjc&X-Amz-Signature=97448ec94edb939ad2fd43b56fe0568b643ba4e72e0f4baeb29a91d6341ca699&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTJMKY6Q%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCQJ8Wz139zeVsG3bQAC%2Bjzitsjc3kl%2B15BkJ%2FesdB8KwIhALyw3bldNUBNFDIv9iK5Y5SeUc%2BwBgPFzBLrY9Yj5RrXKv8DCAwQABoMNjM3NDIzMTgzODA1IgyiEf9TYxQuGIk%2FX9Yq3AMXrho%2FTfweZH185Y53rME%2B0Rn3TVTiLiTvCsMuXJgsqjcWaP0RIKt3LXh7TB5ecOwqbiFAMg%2FkVFYKL6a8L1aR7C%2F9FDYbE2QRGElOb%2BhwTS%2BXI2hYcU3ZGC74Ivd7%2BGkthY56UDWV2BHB9HLGthD01gA5ip6z0KsKgJQqQhsHrqE4jGD%2BXx796Tz4F4rxnvBkKxnNRgcOTnip7rFdIJfgdaflJmPjATxDRkulk8%2By6ImViLrgCn4wm2ND1tHIBZghF3S2TMs0RXTdw1NoPDu55Nl1sWpaOcgkdRYEHVco7y39BxAk984h27iffI157DyPfduJ5TVFmyL0uFi1b6WM7bbYtRtze1dKlLhctGLLAGzKZYafYi30zVH86U22Saq15quJwUEWc0ny6DrLSO58Qo6xx7uG4yg11p6hySCECmzJKlBGsgvnjDtVY7dNKtbwV3TqMRh2wktNrecFfymffs01LU0iFAH5SkGhbvqIuB7QF%2BYFBT%2FgtTA9b1hDLkOy5pfSK9ZCb3rS6zJpYqxtiZj5Jcs6E1cFtD9zyyil0daKvxzPhZyawYRz%2BsFi5B4mea%2BBc4VMw0Daqz%2BcP2jwTz6t%2BK39hEHcq2SS9kjdfvlyyjtsbkO3SXlB2TCLwrPNBjqkAWZClN6d5Q7soXFPZk31BC4RyKIjllFnQ%2BdPmV4szoT%2FVP7H50S1u9h80imYBzRJd6rI%2FEUfs5o6zxYPTPVpfpnedOeRIs1kcuBzpipOjcvWF1cTF5vXCMtNKGqAUjaKO8nEaJDEz%2FgAMd4qfiJQOlAFo5KffgJfpDVDQYeMJZjplvliFVWShFP272mZGVmrd%2BDlO%2Bg56oNWUIuOxDP0OX%2BQYrjc&X-Amz-Signature=42872988ec6410c547d115520547e0fc310e59f0e46860a3a0ab9d13de2f0e12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTJMKY6Q%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCQJ8Wz139zeVsG3bQAC%2Bjzitsjc3kl%2B15BkJ%2FesdB8KwIhALyw3bldNUBNFDIv9iK5Y5SeUc%2BwBgPFzBLrY9Yj5RrXKv8DCAwQABoMNjM3NDIzMTgzODA1IgyiEf9TYxQuGIk%2FX9Yq3AMXrho%2FTfweZH185Y53rME%2B0Rn3TVTiLiTvCsMuXJgsqjcWaP0RIKt3LXh7TB5ecOwqbiFAMg%2FkVFYKL6a8L1aR7C%2F9FDYbE2QRGElOb%2BhwTS%2BXI2hYcU3ZGC74Ivd7%2BGkthY56UDWV2BHB9HLGthD01gA5ip6z0KsKgJQqQhsHrqE4jGD%2BXx796Tz4F4rxnvBkKxnNRgcOTnip7rFdIJfgdaflJmPjATxDRkulk8%2By6ImViLrgCn4wm2ND1tHIBZghF3S2TMs0RXTdw1NoPDu55Nl1sWpaOcgkdRYEHVco7y39BxAk984h27iffI157DyPfduJ5TVFmyL0uFi1b6WM7bbYtRtze1dKlLhctGLLAGzKZYafYi30zVH86U22Saq15quJwUEWc0ny6DrLSO58Qo6xx7uG4yg11p6hySCECmzJKlBGsgvnjDtVY7dNKtbwV3TqMRh2wktNrecFfymffs01LU0iFAH5SkGhbvqIuB7QF%2BYFBT%2FgtTA9b1hDLkOy5pfSK9ZCb3rS6zJpYqxtiZj5Jcs6E1cFtD9zyyil0daKvxzPhZyawYRz%2BsFi5B4mea%2BBc4VMw0Daqz%2BcP2jwTz6t%2BK39hEHcq2SS9kjdfvlyyjtsbkO3SXlB2TCLwrPNBjqkAWZClN6d5Q7soXFPZk31BC4RyKIjllFnQ%2BdPmV4szoT%2FVP7H50S1u9h80imYBzRJd6rI%2FEUfs5o6zxYPTPVpfpnedOeRIs1kcuBzpipOjcvWF1cTF5vXCMtNKGqAUjaKO8nEaJDEz%2FgAMd4qfiJQOlAFo5KffgJfpDVDQYeMJZjplvliFVWShFP272mZGVmrd%2BDlO%2Bg56oNWUIuOxDP0OX%2BQYrjc&X-Amz-Signature=f2d4b4267f543d219ed9aa9aa1651eddd02c16397781fee838fb9cd2fc03c270&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTJMKY6Q%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCQJ8Wz139zeVsG3bQAC%2Bjzitsjc3kl%2B15BkJ%2FesdB8KwIhALyw3bldNUBNFDIv9iK5Y5SeUc%2BwBgPFzBLrY9Yj5RrXKv8DCAwQABoMNjM3NDIzMTgzODA1IgyiEf9TYxQuGIk%2FX9Yq3AMXrho%2FTfweZH185Y53rME%2B0Rn3TVTiLiTvCsMuXJgsqjcWaP0RIKt3LXh7TB5ecOwqbiFAMg%2FkVFYKL6a8L1aR7C%2F9FDYbE2QRGElOb%2BhwTS%2BXI2hYcU3ZGC74Ivd7%2BGkthY56UDWV2BHB9HLGthD01gA5ip6z0KsKgJQqQhsHrqE4jGD%2BXx796Tz4F4rxnvBkKxnNRgcOTnip7rFdIJfgdaflJmPjATxDRkulk8%2By6ImViLrgCn4wm2ND1tHIBZghF3S2TMs0RXTdw1NoPDu55Nl1sWpaOcgkdRYEHVco7y39BxAk984h27iffI157DyPfduJ5TVFmyL0uFi1b6WM7bbYtRtze1dKlLhctGLLAGzKZYafYi30zVH86U22Saq15quJwUEWc0ny6DrLSO58Qo6xx7uG4yg11p6hySCECmzJKlBGsgvnjDtVY7dNKtbwV3TqMRh2wktNrecFfymffs01LU0iFAH5SkGhbvqIuB7QF%2BYFBT%2FgtTA9b1hDLkOy5pfSK9ZCb3rS6zJpYqxtiZj5Jcs6E1cFtD9zyyil0daKvxzPhZyawYRz%2BsFi5B4mea%2BBc4VMw0Daqz%2BcP2jwTz6t%2BK39hEHcq2SS9kjdfvlyyjtsbkO3SXlB2TCLwrPNBjqkAWZClN6d5Q7soXFPZk31BC4RyKIjllFnQ%2BdPmV4szoT%2FVP7H50S1u9h80imYBzRJd6rI%2FEUfs5o6zxYPTPVpfpnedOeRIs1kcuBzpipOjcvWF1cTF5vXCMtNKGqAUjaKO8nEaJDEz%2FgAMd4qfiJQOlAFo5KffgJfpDVDQYeMJZjplvliFVWShFP272mZGVmrd%2BDlO%2Bg56oNWUIuOxDP0OX%2BQYrjc&X-Amz-Signature=17ba27d41b6aa48b8f6d08bf303df03fa279ad5d750d0c7fd34d3f1f1916e650&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTJMKY6Q%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCQJ8Wz139zeVsG3bQAC%2Bjzitsjc3kl%2B15BkJ%2FesdB8KwIhALyw3bldNUBNFDIv9iK5Y5SeUc%2BwBgPFzBLrY9Yj5RrXKv8DCAwQABoMNjM3NDIzMTgzODA1IgyiEf9TYxQuGIk%2FX9Yq3AMXrho%2FTfweZH185Y53rME%2B0Rn3TVTiLiTvCsMuXJgsqjcWaP0RIKt3LXh7TB5ecOwqbiFAMg%2FkVFYKL6a8L1aR7C%2F9FDYbE2QRGElOb%2BhwTS%2BXI2hYcU3ZGC74Ivd7%2BGkthY56UDWV2BHB9HLGthD01gA5ip6z0KsKgJQqQhsHrqE4jGD%2BXx796Tz4F4rxnvBkKxnNRgcOTnip7rFdIJfgdaflJmPjATxDRkulk8%2By6ImViLrgCn4wm2ND1tHIBZghF3S2TMs0RXTdw1NoPDu55Nl1sWpaOcgkdRYEHVco7y39BxAk984h27iffI157DyPfduJ5TVFmyL0uFi1b6WM7bbYtRtze1dKlLhctGLLAGzKZYafYi30zVH86U22Saq15quJwUEWc0ny6DrLSO58Qo6xx7uG4yg11p6hySCECmzJKlBGsgvnjDtVY7dNKtbwV3TqMRh2wktNrecFfymffs01LU0iFAH5SkGhbvqIuB7QF%2BYFBT%2FgtTA9b1hDLkOy5pfSK9ZCb3rS6zJpYqxtiZj5Jcs6E1cFtD9zyyil0daKvxzPhZyawYRz%2BsFi5B4mea%2BBc4VMw0Daqz%2BcP2jwTz6t%2BK39hEHcq2SS9kjdfvlyyjtsbkO3SXlB2TCLwrPNBjqkAWZClN6d5Q7soXFPZk31BC4RyKIjllFnQ%2BdPmV4szoT%2FVP7H50S1u9h80imYBzRJd6rI%2FEUfs5o6zxYPTPVpfpnedOeRIs1kcuBzpipOjcvWF1cTF5vXCMtNKGqAUjaKO8nEaJDEz%2FgAMd4qfiJQOlAFo5KffgJfpDVDQYeMJZjplvliFVWShFP272mZGVmrd%2BDlO%2Bg56oNWUIuOxDP0OX%2BQYrjc&X-Amz-Signature=67564f38b4bce3daf259753e70adedf30924eb38b10da791e828d4644bd5a5c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTJMKY6Q%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCQJ8Wz139zeVsG3bQAC%2Bjzitsjc3kl%2B15BkJ%2FesdB8KwIhALyw3bldNUBNFDIv9iK5Y5SeUc%2BwBgPFzBLrY9Yj5RrXKv8DCAwQABoMNjM3NDIzMTgzODA1IgyiEf9TYxQuGIk%2FX9Yq3AMXrho%2FTfweZH185Y53rME%2B0Rn3TVTiLiTvCsMuXJgsqjcWaP0RIKt3LXh7TB5ecOwqbiFAMg%2FkVFYKL6a8L1aR7C%2F9FDYbE2QRGElOb%2BhwTS%2BXI2hYcU3ZGC74Ivd7%2BGkthY56UDWV2BHB9HLGthD01gA5ip6z0KsKgJQqQhsHrqE4jGD%2BXx796Tz4F4rxnvBkKxnNRgcOTnip7rFdIJfgdaflJmPjATxDRkulk8%2By6ImViLrgCn4wm2ND1tHIBZghF3S2TMs0RXTdw1NoPDu55Nl1sWpaOcgkdRYEHVco7y39BxAk984h27iffI157DyPfduJ5TVFmyL0uFi1b6WM7bbYtRtze1dKlLhctGLLAGzKZYafYi30zVH86U22Saq15quJwUEWc0ny6DrLSO58Qo6xx7uG4yg11p6hySCECmzJKlBGsgvnjDtVY7dNKtbwV3TqMRh2wktNrecFfymffs01LU0iFAH5SkGhbvqIuB7QF%2BYFBT%2FgtTA9b1hDLkOy5pfSK9ZCb3rS6zJpYqxtiZj5Jcs6E1cFtD9zyyil0daKvxzPhZyawYRz%2BsFi5B4mea%2BBc4VMw0Daqz%2BcP2jwTz6t%2BK39hEHcq2SS9kjdfvlyyjtsbkO3SXlB2TCLwrPNBjqkAWZClN6d5Q7soXFPZk31BC4RyKIjllFnQ%2BdPmV4szoT%2FVP7H50S1u9h80imYBzRJd6rI%2FEUfs5o6zxYPTPVpfpnedOeRIs1kcuBzpipOjcvWF1cTF5vXCMtNKGqAUjaKO8nEaJDEz%2FgAMd4qfiJQOlAFo5KffgJfpDVDQYeMJZjplvliFVWShFP272mZGVmrd%2BDlO%2Bg56oNWUIuOxDP0OX%2BQYrjc&X-Amz-Signature=da925229599cf151b9c3357fc647108ab12c5a6c5bbb4d21eb4580df2a0f3adf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTJMKY6Q%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCQJ8Wz139zeVsG3bQAC%2Bjzitsjc3kl%2B15BkJ%2FesdB8KwIhALyw3bldNUBNFDIv9iK5Y5SeUc%2BwBgPFzBLrY9Yj5RrXKv8DCAwQABoMNjM3NDIzMTgzODA1IgyiEf9TYxQuGIk%2FX9Yq3AMXrho%2FTfweZH185Y53rME%2B0Rn3TVTiLiTvCsMuXJgsqjcWaP0RIKt3LXh7TB5ecOwqbiFAMg%2FkVFYKL6a8L1aR7C%2F9FDYbE2QRGElOb%2BhwTS%2BXI2hYcU3ZGC74Ivd7%2BGkthY56UDWV2BHB9HLGthD01gA5ip6z0KsKgJQqQhsHrqE4jGD%2BXx796Tz4F4rxnvBkKxnNRgcOTnip7rFdIJfgdaflJmPjATxDRkulk8%2By6ImViLrgCn4wm2ND1tHIBZghF3S2TMs0RXTdw1NoPDu55Nl1sWpaOcgkdRYEHVco7y39BxAk984h27iffI157DyPfduJ5TVFmyL0uFi1b6WM7bbYtRtze1dKlLhctGLLAGzKZYafYi30zVH86U22Saq15quJwUEWc0ny6DrLSO58Qo6xx7uG4yg11p6hySCECmzJKlBGsgvnjDtVY7dNKtbwV3TqMRh2wktNrecFfymffs01LU0iFAH5SkGhbvqIuB7QF%2BYFBT%2FgtTA9b1hDLkOy5pfSK9ZCb3rS6zJpYqxtiZj5Jcs6E1cFtD9zyyil0daKvxzPhZyawYRz%2BsFi5B4mea%2BBc4VMw0Daqz%2BcP2jwTz6t%2BK39hEHcq2SS9kjdfvlyyjtsbkO3SXlB2TCLwrPNBjqkAWZClN6d5Q7soXFPZk31BC4RyKIjllFnQ%2BdPmV4szoT%2FVP7H50S1u9h80imYBzRJd6rI%2FEUfs5o6zxYPTPVpfpnedOeRIs1kcuBzpipOjcvWF1cTF5vXCMtNKGqAUjaKO8nEaJDEz%2FgAMd4qfiJQOlAFo5KffgJfpDVDQYeMJZjplvliFVWShFP272mZGVmrd%2BDlO%2Bg56oNWUIuOxDP0OX%2BQYrjc&X-Amz-Signature=0dc5f5b7525a91746fe5df0dbc3292da0fa58da9186c80dc9883362ddec64ea3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTJMKY6Q%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCQJ8Wz139zeVsG3bQAC%2Bjzitsjc3kl%2B15BkJ%2FesdB8KwIhALyw3bldNUBNFDIv9iK5Y5SeUc%2BwBgPFzBLrY9Yj5RrXKv8DCAwQABoMNjM3NDIzMTgzODA1IgyiEf9TYxQuGIk%2FX9Yq3AMXrho%2FTfweZH185Y53rME%2B0Rn3TVTiLiTvCsMuXJgsqjcWaP0RIKt3LXh7TB5ecOwqbiFAMg%2FkVFYKL6a8L1aR7C%2F9FDYbE2QRGElOb%2BhwTS%2BXI2hYcU3ZGC74Ivd7%2BGkthY56UDWV2BHB9HLGthD01gA5ip6z0KsKgJQqQhsHrqE4jGD%2BXx796Tz4F4rxnvBkKxnNRgcOTnip7rFdIJfgdaflJmPjATxDRkulk8%2By6ImViLrgCn4wm2ND1tHIBZghF3S2TMs0RXTdw1NoPDu55Nl1sWpaOcgkdRYEHVco7y39BxAk984h27iffI157DyPfduJ5TVFmyL0uFi1b6WM7bbYtRtze1dKlLhctGLLAGzKZYafYi30zVH86U22Saq15quJwUEWc0ny6DrLSO58Qo6xx7uG4yg11p6hySCECmzJKlBGsgvnjDtVY7dNKtbwV3TqMRh2wktNrecFfymffs01LU0iFAH5SkGhbvqIuB7QF%2BYFBT%2FgtTA9b1hDLkOy5pfSK9ZCb3rS6zJpYqxtiZj5Jcs6E1cFtD9zyyil0daKvxzPhZyawYRz%2BsFi5B4mea%2BBc4VMw0Daqz%2BcP2jwTz6t%2BK39hEHcq2SS9kjdfvlyyjtsbkO3SXlB2TCLwrPNBjqkAWZClN6d5Q7soXFPZk31BC4RyKIjllFnQ%2BdPmV4szoT%2FVP7H50S1u9h80imYBzRJd6rI%2FEUfs5o6zxYPTPVpfpnedOeRIs1kcuBzpipOjcvWF1cTF5vXCMtNKGqAUjaKO8nEaJDEz%2FgAMd4qfiJQOlAFo5KffgJfpDVDQYeMJZjplvliFVWShFP272mZGVmrd%2BDlO%2Bg56oNWUIuOxDP0OX%2BQYrjc&X-Amz-Signature=f5672466abd920f43518aa04a259d1ef49c71dfccfa0f922371cd1326905a909&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTJMKY6Q%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCQJ8Wz139zeVsG3bQAC%2Bjzitsjc3kl%2B15BkJ%2FesdB8KwIhALyw3bldNUBNFDIv9iK5Y5SeUc%2BwBgPFzBLrY9Yj5RrXKv8DCAwQABoMNjM3NDIzMTgzODA1IgyiEf9TYxQuGIk%2FX9Yq3AMXrho%2FTfweZH185Y53rME%2B0Rn3TVTiLiTvCsMuXJgsqjcWaP0RIKt3LXh7TB5ecOwqbiFAMg%2FkVFYKL6a8L1aR7C%2F9FDYbE2QRGElOb%2BhwTS%2BXI2hYcU3ZGC74Ivd7%2BGkthY56UDWV2BHB9HLGthD01gA5ip6z0KsKgJQqQhsHrqE4jGD%2BXx796Tz4F4rxnvBkKxnNRgcOTnip7rFdIJfgdaflJmPjATxDRkulk8%2By6ImViLrgCn4wm2ND1tHIBZghF3S2TMs0RXTdw1NoPDu55Nl1sWpaOcgkdRYEHVco7y39BxAk984h27iffI157DyPfduJ5TVFmyL0uFi1b6WM7bbYtRtze1dKlLhctGLLAGzKZYafYi30zVH86U22Saq15quJwUEWc0ny6DrLSO58Qo6xx7uG4yg11p6hySCECmzJKlBGsgvnjDtVY7dNKtbwV3TqMRh2wktNrecFfymffs01LU0iFAH5SkGhbvqIuB7QF%2BYFBT%2FgtTA9b1hDLkOy5pfSK9ZCb3rS6zJpYqxtiZj5Jcs6E1cFtD9zyyil0daKvxzPhZyawYRz%2BsFi5B4mea%2BBc4VMw0Daqz%2BcP2jwTz6t%2BK39hEHcq2SS9kjdfvlyyjtsbkO3SXlB2TCLwrPNBjqkAWZClN6d5Q7soXFPZk31BC4RyKIjllFnQ%2BdPmV4szoT%2FVP7H50S1u9h80imYBzRJd6rI%2FEUfs5o6zxYPTPVpfpnedOeRIs1kcuBzpipOjcvWF1cTF5vXCMtNKGqAUjaKO8nEaJDEz%2FgAMd4qfiJQOlAFo5KffgJfpDVDQYeMJZjplvliFVWShFP272mZGVmrd%2BDlO%2Bg56oNWUIuOxDP0OX%2BQYrjc&X-Amz-Signature=0d1e736a7802dd379729f367909ad08e6be6c045287b781236c57c875b476d02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTJMKY6Q%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCQJ8Wz139zeVsG3bQAC%2Bjzitsjc3kl%2B15BkJ%2FesdB8KwIhALyw3bldNUBNFDIv9iK5Y5SeUc%2BwBgPFzBLrY9Yj5RrXKv8DCAwQABoMNjM3NDIzMTgzODA1IgyiEf9TYxQuGIk%2FX9Yq3AMXrho%2FTfweZH185Y53rME%2B0Rn3TVTiLiTvCsMuXJgsqjcWaP0RIKt3LXh7TB5ecOwqbiFAMg%2FkVFYKL6a8L1aR7C%2F9FDYbE2QRGElOb%2BhwTS%2BXI2hYcU3ZGC74Ivd7%2BGkthY56UDWV2BHB9HLGthD01gA5ip6z0KsKgJQqQhsHrqE4jGD%2BXx796Tz4F4rxnvBkKxnNRgcOTnip7rFdIJfgdaflJmPjATxDRkulk8%2By6ImViLrgCn4wm2ND1tHIBZghF3S2TMs0RXTdw1NoPDu55Nl1sWpaOcgkdRYEHVco7y39BxAk984h27iffI157DyPfduJ5TVFmyL0uFi1b6WM7bbYtRtze1dKlLhctGLLAGzKZYafYi30zVH86U22Saq15quJwUEWc0ny6DrLSO58Qo6xx7uG4yg11p6hySCECmzJKlBGsgvnjDtVY7dNKtbwV3TqMRh2wktNrecFfymffs01LU0iFAH5SkGhbvqIuB7QF%2BYFBT%2FgtTA9b1hDLkOy5pfSK9ZCb3rS6zJpYqxtiZj5Jcs6E1cFtD9zyyil0daKvxzPhZyawYRz%2BsFi5B4mea%2BBc4VMw0Daqz%2BcP2jwTz6t%2BK39hEHcq2SS9kjdfvlyyjtsbkO3SXlB2TCLwrPNBjqkAWZClN6d5Q7soXFPZk31BC4RyKIjllFnQ%2BdPmV4szoT%2FVP7H50S1u9h80imYBzRJd6rI%2FEUfs5o6zxYPTPVpfpnedOeRIs1kcuBzpipOjcvWF1cTF5vXCMtNKGqAUjaKO8nEaJDEz%2FgAMd4qfiJQOlAFo5KffgJfpDVDQYeMJZjplvliFVWShFP272mZGVmrd%2BDlO%2Bg56oNWUIuOxDP0OX%2BQYrjc&X-Amz-Signature=658d70a90e807481339c4a76fc15476eea18f55aecea43cbf43a87c06ac08e43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

