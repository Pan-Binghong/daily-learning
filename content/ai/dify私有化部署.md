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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSIKXGYA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE88zPNSgDHRh72XdRGKmsEnZ69MrfmdfKYljIHggs7tAiEAqsQebLDjPtUfUk37D2sx5yMIhjevLy0Kx8MMW%2FvIDqAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGZiEQrSy6QxTOn1fyrcA1FWb2t63bKTUBIF7ymX3%2FF6KfUAT8RqvilMWsMXh0o5LREARXZZsAXgzXLlBvW0Ie50%2BF44Ls6NgmrtAC0AFnVTi%2FxdJFd3bFafCugdjVQKfQCXSDJqbwtPAmRfpy92cG1qqMf3nxWo3BHL6kaYyLoXY1UouYv2bIze%2FrOj%2FOeWpINlqmW2Zfllyhy0qR4OjMiMtJXBPxfn%2B%2FtwuEapmy47BAuPeN8V57Mlx6q%2FhRg1KYzVku6ObvOI9gBEvgm%2BPKD%2FAqp%2For9I9QVGTVXKIOpybn%2BuI3dnmKx2rzR0Oam5MsDJS3nEqtcSL4yFvVF%2FrUd7nwlVchNL5ywyt3PUGEMy39XPjKrnfUwYWUhmY%2BfyZBhmaKlECtvLR9fKpjPZ3upHgt34O9ciRPWq2zXz22iidr%2Bu6IU0rdRvOwHeofO5nyZg4yA31gX0Z57iPP0qfinc%2FJDb5aMCAfuuGWxuW8jxHfTtnEe0j9XAcD%2BJG8z3yK1UjIlJtqHp%2BiXpZy8UrOP2bSrGT%2BHW6%2By2ib2c06Ot8SjHzCaFpiAjQdSLM9IJ84hg0nJ8ujJ1A8Ev2d1%2FqoSq2G4yCPF4qL9qjhq%2FhXUOQdTdcGOhCCYFw9YPVDgYFDS2HCLQSNOJv%2BqkMOXx2cwGOqUBZ7SSz%2BOo4Ud57QcgbwWIcX%2BJBDaEZ2fIYevIG0x9cy%2BMWe%2FONvatMPLjpp31Jifnz%2B7uiAoi2Tp3WswtsBh3bGn6ih0eDL%2Fl63LIiujyUan52OEXnhKrq0n9%2FJxXQ80xZb9wNdl0L60Q833Ml7ZDR%2BybKXdpOSDBbjLSBYZ%2BdR5Lk4%2B3O2AopLSbk0%2Ffdq%2BxdRQnwisRH%2BmV4MnxS5749lTfoLpi&X-Amz-Signature=20aa2000165c9dbe1c3ea00286bfcfb7470b3a4648bb1387997842b63587bb59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSIKXGYA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE88zPNSgDHRh72XdRGKmsEnZ69MrfmdfKYljIHggs7tAiEAqsQebLDjPtUfUk37D2sx5yMIhjevLy0Kx8MMW%2FvIDqAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGZiEQrSy6QxTOn1fyrcA1FWb2t63bKTUBIF7ymX3%2FF6KfUAT8RqvilMWsMXh0o5LREARXZZsAXgzXLlBvW0Ie50%2BF44Ls6NgmrtAC0AFnVTi%2FxdJFd3bFafCugdjVQKfQCXSDJqbwtPAmRfpy92cG1qqMf3nxWo3BHL6kaYyLoXY1UouYv2bIze%2FrOj%2FOeWpINlqmW2Zfllyhy0qR4OjMiMtJXBPxfn%2B%2FtwuEapmy47BAuPeN8V57Mlx6q%2FhRg1KYzVku6ObvOI9gBEvgm%2BPKD%2FAqp%2For9I9QVGTVXKIOpybn%2BuI3dnmKx2rzR0Oam5MsDJS3nEqtcSL4yFvVF%2FrUd7nwlVchNL5ywyt3PUGEMy39XPjKrnfUwYWUhmY%2BfyZBhmaKlECtvLR9fKpjPZ3upHgt34O9ciRPWq2zXz22iidr%2Bu6IU0rdRvOwHeofO5nyZg4yA31gX0Z57iPP0qfinc%2FJDb5aMCAfuuGWxuW8jxHfTtnEe0j9XAcD%2BJG8z3yK1UjIlJtqHp%2BiXpZy8UrOP2bSrGT%2BHW6%2By2ib2c06Ot8SjHzCaFpiAjQdSLM9IJ84hg0nJ8ujJ1A8Ev2d1%2FqoSq2G4yCPF4qL9qjhq%2FhXUOQdTdcGOhCCYFw9YPVDgYFDS2HCLQSNOJv%2BqkMOXx2cwGOqUBZ7SSz%2BOo4Ud57QcgbwWIcX%2BJBDaEZ2fIYevIG0x9cy%2BMWe%2FONvatMPLjpp31Jifnz%2B7uiAoi2Tp3WswtsBh3bGn6ih0eDL%2Fl63LIiujyUan52OEXnhKrq0n9%2FJxXQ80xZb9wNdl0L60Q833Ml7ZDR%2BybKXdpOSDBbjLSBYZ%2BdR5Lk4%2B3O2AopLSbk0%2Ffdq%2BxdRQnwisRH%2BmV4MnxS5749lTfoLpi&X-Amz-Signature=bf80f91bddd24116b7ba34a1697806e5109fcc009f0f4d86783cfa9ba5ee69f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSIKXGYA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE88zPNSgDHRh72XdRGKmsEnZ69MrfmdfKYljIHggs7tAiEAqsQebLDjPtUfUk37D2sx5yMIhjevLy0Kx8MMW%2FvIDqAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGZiEQrSy6QxTOn1fyrcA1FWb2t63bKTUBIF7ymX3%2FF6KfUAT8RqvilMWsMXh0o5LREARXZZsAXgzXLlBvW0Ie50%2BF44Ls6NgmrtAC0AFnVTi%2FxdJFd3bFafCugdjVQKfQCXSDJqbwtPAmRfpy92cG1qqMf3nxWo3BHL6kaYyLoXY1UouYv2bIze%2FrOj%2FOeWpINlqmW2Zfllyhy0qR4OjMiMtJXBPxfn%2B%2FtwuEapmy47BAuPeN8V57Mlx6q%2FhRg1KYzVku6ObvOI9gBEvgm%2BPKD%2FAqp%2For9I9QVGTVXKIOpybn%2BuI3dnmKx2rzR0Oam5MsDJS3nEqtcSL4yFvVF%2FrUd7nwlVchNL5ywyt3PUGEMy39XPjKrnfUwYWUhmY%2BfyZBhmaKlECtvLR9fKpjPZ3upHgt34O9ciRPWq2zXz22iidr%2Bu6IU0rdRvOwHeofO5nyZg4yA31gX0Z57iPP0qfinc%2FJDb5aMCAfuuGWxuW8jxHfTtnEe0j9XAcD%2BJG8z3yK1UjIlJtqHp%2BiXpZy8UrOP2bSrGT%2BHW6%2By2ib2c06Ot8SjHzCaFpiAjQdSLM9IJ84hg0nJ8ujJ1A8Ev2d1%2FqoSq2G4yCPF4qL9qjhq%2FhXUOQdTdcGOhCCYFw9YPVDgYFDS2HCLQSNOJv%2BqkMOXx2cwGOqUBZ7SSz%2BOo4Ud57QcgbwWIcX%2BJBDaEZ2fIYevIG0x9cy%2BMWe%2FONvatMPLjpp31Jifnz%2B7uiAoi2Tp3WswtsBh3bGn6ih0eDL%2Fl63LIiujyUan52OEXnhKrq0n9%2FJxXQ80xZb9wNdl0L60Q833Ml7ZDR%2BybKXdpOSDBbjLSBYZ%2BdR5Lk4%2B3O2AopLSbk0%2Ffdq%2BxdRQnwisRH%2BmV4MnxS5749lTfoLpi&X-Amz-Signature=0286b90d8dc67a818446d9c6235c2814195119e1d1a3dac935efe99472c26488&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSIKXGYA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE88zPNSgDHRh72XdRGKmsEnZ69MrfmdfKYljIHggs7tAiEAqsQebLDjPtUfUk37D2sx5yMIhjevLy0Kx8MMW%2FvIDqAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGZiEQrSy6QxTOn1fyrcA1FWb2t63bKTUBIF7ymX3%2FF6KfUAT8RqvilMWsMXh0o5LREARXZZsAXgzXLlBvW0Ie50%2BF44Ls6NgmrtAC0AFnVTi%2FxdJFd3bFafCugdjVQKfQCXSDJqbwtPAmRfpy92cG1qqMf3nxWo3BHL6kaYyLoXY1UouYv2bIze%2FrOj%2FOeWpINlqmW2Zfllyhy0qR4OjMiMtJXBPxfn%2B%2FtwuEapmy47BAuPeN8V57Mlx6q%2FhRg1KYzVku6ObvOI9gBEvgm%2BPKD%2FAqp%2For9I9QVGTVXKIOpybn%2BuI3dnmKx2rzR0Oam5MsDJS3nEqtcSL4yFvVF%2FrUd7nwlVchNL5ywyt3PUGEMy39XPjKrnfUwYWUhmY%2BfyZBhmaKlECtvLR9fKpjPZ3upHgt34O9ciRPWq2zXz22iidr%2Bu6IU0rdRvOwHeofO5nyZg4yA31gX0Z57iPP0qfinc%2FJDb5aMCAfuuGWxuW8jxHfTtnEe0j9XAcD%2BJG8z3yK1UjIlJtqHp%2BiXpZy8UrOP2bSrGT%2BHW6%2By2ib2c06Ot8SjHzCaFpiAjQdSLM9IJ84hg0nJ8ujJ1A8Ev2d1%2FqoSq2G4yCPF4qL9qjhq%2FhXUOQdTdcGOhCCYFw9YPVDgYFDS2HCLQSNOJv%2BqkMOXx2cwGOqUBZ7SSz%2BOo4Ud57QcgbwWIcX%2BJBDaEZ2fIYevIG0x9cy%2BMWe%2FONvatMPLjpp31Jifnz%2B7uiAoi2Tp3WswtsBh3bGn6ih0eDL%2Fl63LIiujyUan52OEXnhKrq0n9%2FJxXQ80xZb9wNdl0L60Q833Ml7ZDR%2BybKXdpOSDBbjLSBYZ%2BdR5Lk4%2B3O2AopLSbk0%2Ffdq%2BxdRQnwisRH%2BmV4MnxS5749lTfoLpi&X-Amz-Signature=fdc1acef5724df3f260cb2a7da2660e7ebf46faeed5b03492cfca9a7de3261eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSIKXGYA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE88zPNSgDHRh72XdRGKmsEnZ69MrfmdfKYljIHggs7tAiEAqsQebLDjPtUfUk37D2sx5yMIhjevLy0Kx8MMW%2FvIDqAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGZiEQrSy6QxTOn1fyrcA1FWb2t63bKTUBIF7ymX3%2FF6KfUAT8RqvilMWsMXh0o5LREARXZZsAXgzXLlBvW0Ie50%2BF44Ls6NgmrtAC0AFnVTi%2FxdJFd3bFafCugdjVQKfQCXSDJqbwtPAmRfpy92cG1qqMf3nxWo3BHL6kaYyLoXY1UouYv2bIze%2FrOj%2FOeWpINlqmW2Zfllyhy0qR4OjMiMtJXBPxfn%2B%2FtwuEapmy47BAuPeN8V57Mlx6q%2FhRg1KYzVku6ObvOI9gBEvgm%2BPKD%2FAqp%2For9I9QVGTVXKIOpybn%2BuI3dnmKx2rzR0Oam5MsDJS3nEqtcSL4yFvVF%2FrUd7nwlVchNL5ywyt3PUGEMy39XPjKrnfUwYWUhmY%2BfyZBhmaKlECtvLR9fKpjPZ3upHgt34O9ciRPWq2zXz22iidr%2Bu6IU0rdRvOwHeofO5nyZg4yA31gX0Z57iPP0qfinc%2FJDb5aMCAfuuGWxuW8jxHfTtnEe0j9XAcD%2BJG8z3yK1UjIlJtqHp%2BiXpZy8UrOP2bSrGT%2BHW6%2By2ib2c06Ot8SjHzCaFpiAjQdSLM9IJ84hg0nJ8ujJ1A8Ev2d1%2FqoSq2G4yCPF4qL9qjhq%2FhXUOQdTdcGOhCCYFw9YPVDgYFDS2HCLQSNOJv%2BqkMOXx2cwGOqUBZ7SSz%2BOo4Ud57QcgbwWIcX%2BJBDaEZ2fIYevIG0x9cy%2BMWe%2FONvatMPLjpp31Jifnz%2B7uiAoi2Tp3WswtsBh3bGn6ih0eDL%2Fl63LIiujyUan52OEXnhKrq0n9%2FJxXQ80xZb9wNdl0L60Q833Ml7ZDR%2BybKXdpOSDBbjLSBYZ%2BdR5Lk4%2B3O2AopLSbk0%2Ffdq%2BxdRQnwisRH%2BmV4MnxS5749lTfoLpi&X-Amz-Signature=2ac8118427d4c69eeee80d52675495d15153cf7fbc9ecfd411c3e91b44c47519&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSIKXGYA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE88zPNSgDHRh72XdRGKmsEnZ69MrfmdfKYljIHggs7tAiEAqsQebLDjPtUfUk37D2sx5yMIhjevLy0Kx8MMW%2FvIDqAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGZiEQrSy6QxTOn1fyrcA1FWb2t63bKTUBIF7ymX3%2FF6KfUAT8RqvilMWsMXh0o5LREARXZZsAXgzXLlBvW0Ie50%2BF44Ls6NgmrtAC0AFnVTi%2FxdJFd3bFafCugdjVQKfQCXSDJqbwtPAmRfpy92cG1qqMf3nxWo3BHL6kaYyLoXY1UouYv2bIze%2FrOj%2FOeWpINlqmW2Zfllyhy0qR4OjMiMtJXBPxfn%2B%2FtwuEapmy47BAuPeN8V57Mlx6q%2FhRg1KYzVku6ObvOI9gBEvgm%2BPKD%2FAqp%2For9I9QVGTVXKIOpybn%2BuI3dnmKx2rzR0Oam5MsDJS3nEqtcSL4yFvVF%2FrUd7nwlVchNL5ywyt3PUGEMy39XPjKrnfUwYWUhmY%2BfyZBhmaKlECtvLR9fKpjPZ3upHgt34O9ciRPWq2zXz22iidr%2Bu6IU0rdRvOwHeofO5nyZg4yA31gX0Z57iPP0qfinc%2FJDb5aMCAfuuGWxuW8jxHfTtnEe0j9XAcD%2BJG8z3yK1UjIlJtqHp%2BiXpZy8UrOP2bSrGT%2BHW6%2By2ib2c06Ot8SjHzCaFpiAjQdSLM9IJ84hg0nJ8ujJ1A8Ev2d1%2FqoSq2G4yCPF4qL9qjhq%2FhXUOQdTdcGOhCCYFw9YPVDgYFDS2HCLQSNOJv%2BqkMOXx2cwGOqUBZ7SSz%2BOo4Ud57QcgbwWIcX%2BJBDaEZ2fIYevIG0x9cy%2BMWe%2FONvatMPLjpp31Jifnz%2B7uiAoi2Tp3WswtsBh3bGn6ih0eDL%2Fl63LIiujyUan52OEXnhKrq0n9%2FJxXQ80xZb9wNdl0L60Q833Ml7ZDR%2BybKXdpOSDBbjLSBYZ%2BdR5Lk4%2B3O2AopLSbk0%2Ffdq%2BxdRQnwisRH%2BmV4MnxS5749lTfoLpi&X-Amz-Signature=74bda7eccb21bfa93e1dcd0f446a6843c8e9136ed306e2d542d1a6e6ec1ad364&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSIKXGYA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE88zPNSgDHRh72XdRGKmsEnZ69MrfmdfKYljIHggs7tAiEAqsQebLDjPtUfUk37D2sx5yMIhjevLy0Kx8MMW%2FvIDqAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGZiEQrSy6QxTOn1fyrcA1FWb2t63bKTUBIF7ymX3%2FF6KfUAT8RqvilMWsMXh0o5LREARXZZsAXgzXLlBvW0Ie50%2BF44Ls6NgmrtAC0AFnVTi%2FxdJFd3bFafCugdjVQKfQCXSDJqbwtPAmRfpy92cG1qqMf3nxWo3BHL6kaYyLoXY1UouYv2bIze%2FrOj%2FOeWpINlqmW2Zfllyhy0qR4OjMiMtJXBPxfn%2B%2FtwuEapmy47BAuPeN8V57Mlx6q%2FhRg1KYzVku6ObvOI9gBEvgm%2BPKD%2FAqp%2For9I9QVGTVXKIOpybn%2BuI3dnmKx2rzR0Oam5MsDJS3nEqtcSL4yFvVF%2FrUd7nwlVchNL5ywyt3PUGEMy39XPjKrnfUwYWUhmY%2BfyZBhmaKlECtvLR9fKpjPZ3upHgt34O9ciRPWq2zXz22iidr%2Bu6IU0rdRvOwHeofO5nyZg4yA31gX0Z57iPP0qfinc%2FJDb5aMCAfuuGWxuW8jxHfTtnEe0j9XAcD%2BJG8z3yK1UjIlJtqHp%2BiXpZy8UrOP2bSrGT%2BHW6%2By2ib2c06Ot8SjHzCaFpiAjQdSLM9IJ84hg0nJ8ujJ1A8Ev2d1%2FqoSq2G4yCPF4qL9qjhq%2FhXUOQdTdcGOhCCYFw9YPVDgYFDS2HCLQSNOJv%2BqkMOXx2cwGOqUBZ7SSz%2BOo4Ud57QcgbwWIcX%2BJBDaEZ2fIYevIG0x9cy%2BMWe%2FONvatMPLjpp31Jifnz%2B7uiAoi2Tp3WswtsBh3bGn6ih0eDL%2Fl63LIiujyUan52OEXnhKrq0n9%2FJxXQ80xZb9wNdl0L60Q833Ml7ZDR%2BybKXdpOSDBbjLSBYZ%2BdR5Lk4%2B3O2AopLSbk0%2Ffdq%2BxdRQnwisRH%2BmV4MnxS5749lTfoLpi&X-Amz-Signature=5498836fc285904784e465a498ee98d166acb34f193e9f843ff7826bb4450590&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSIKXGYA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE88zPNSgDHRh72XdRGKmsEnZ69MrfmdfKYljIHggs7tAiEAqsQebLDjPtUfUk37D2sx5yMIhjevLy0Kx8MMW%2FvIDqAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGZiEQrSy6QxTOn1fyrcA1FWb2t63bKTUBIF7ymX3%2FF6KfUAT8RqvilMWsMXh0o5LREARXZZsAXgzXLlBvW0Ie50%2BF44Ls6NgmrtAC0AFnVTi%2FxdJFd3bFafCugdjVQKfQCXSDJqbwtPAmRfpy92cG1qqMf3nxWo3BHL6kaYyLoXY1UouYv2bIze%2FrOj%2FOeWpINlqmW2Zfllyhy0qR4OjMiMtJXBPxfn%2B%2FtwuEapmy47BAuPeN8V57Mlx6q%2FhRg1KYzVku6ObvOI9gBEvgm%2BPKD%2FAqp%2For9I9QVGTVXKIOpybn%2BuI3dnmKx2rzR0Oam5MsDJS3nEqtcSL4yFvVF%2FrUd7nwlVchNL5ywyt3PUGEMy39XPjKrnfUwYWUhmY%2BfyZBhmaKlECtvLR9fKpjPZ3upHgt34O9ciRPWq2zXz22iidr%2Bu6IU0rdRvOwHeofO5nyZg4yA31gX0Z57iPP0qfinc%2FJDb5aMCAfuuGWxuW8jxHfTtnEe0j9XAcD%2BJG8z3yK1UjIlJtqHp%2BiXpZy8UrOP2bSrGT%2BHW6%2By2ib2c06Ot8SjHzCaFpiAjQdSLM9IJ84hg0nJ8ujJ1A8Ev2d1%2FqoSq2G4yCPF4qL9qjhq%2FhXUOQdTdcGOhCCYFw9YPVDgYFDS2HCLQSNOJv%2BqkMOXx2cwGOqUBZ7SSz%2BOo4Ud57QcgbwWIcX%2BJBDaEZ2fIYevIG0x9cy%2BMWe%2FONvatMPLjpp31Jifnz%2B7uiAoi2Tp3WswtsBh3bGn6ih0eDL%2Fl63LIiujyUan52OEXnhKrq0n9%2FJxXQ80xZb9wNdl0L60Q833Ml7ZDR%2BybKXdpOSDBbjLSBYZ%2BdR5Lk4%2B3O2AopLSbk0%2Ffdq%2BxdRQnwisRH%2BmV4MnxS5749lTfoLpi&X-Amz-Signature=0004146497fa92a266305de01e05dbe5d7a3535068ef86356eb257e4319b95b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSIKXGYA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE88zPNSgDHRh72XdRGKmsEnZ69MrfmdfKYljIHggs7tAiEAqsQebLDjPtUfUk37D2sx5yMIhjevLy0Kx8MMW%2FvIDqAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGZiEQrSy6QxTOn1fyrcA1FWb2t63bKTUBIF7ymX3%2FF6KfUAT8RqvilMWsMXh0o5LREARXZZsAXgzXLlBvW0Ie50%2BF44Ls6NgmrtAC0AFnVTi%2FxdJFd3bFafCugdjVQKfQCXSDJqbwtPAmRfpy92cG1qqMf3nxWo3BHL6kaYyLoXY1UouYv2bIze%2FrOj%2FOeWpINlqmW2Zfllyhy0qR4OjMiMtJXBPxfn%2B%2FtwuEapmy47BAuPeN8V57Mlx6q%2FhRg1KYzVku6ObvOI9gBEvgm%2BPKD%2FAqp%2For9I9QVGTVXKIOpybn%2BuI3dnmKx2rzR0Oam5MsDJS3nEqtcSL4yFvVF%2FrUd7nwlVchNL5ywyt3PUGEMy39XPjKrnfUwYWUhmY%2BfyZBhmaKlECtvLR9fKpjPZ3upHgt34O9ciRPWq2zXz22iidr%2Bu6IU0rdRvOwHeofO5nyZg4yA31gX0Z57iPP0qfinc%2FJDb5aMCAfuuGWxuW8jxHfTtnEe0j9XAcD%2BJG8z3yK1UjIlJtqHp%2BiXpZy8UrOP2bSrGT%2BHW6%2By2ib2c06Ot8SjHzCaFpiAjQdSLM9IJ84hg0nJ8ujJ1A8Ev2d1%2FqoSq2G4yCPF4qL9qjhq%2FhXUOQdTdcGOhCCYFw9YPVDgYFDS2HCLQSNOJv%2BqkMOXx2cwGOqUBZ7SSz%2BOo4Ud57QcgbwWIcX%2BJBDaEZ2fIYevIG0x9cy%2BMWe%2FONvatMPLjpp31Jifnz%2B7uiAoi2Tp3WswtsBh3bGn6ih0eDL%2Fl63LIiujyUan52OEXnhKrq0n9%2FJxXQ80xZb9wNdl0L60Q833Ml7ZDR%2BybKXdpOSDBbjLSBYZ%2BdR5Lk4%2B3O2AopLSbk0%2Ffdq%2BxdRQnwisRH%2BmV4MnxS5749lTfoLpi&X-Amz-Signature=a34a39e287f59193f08ba473e3e1cda7228e9f6f858701938987cae634d8fee4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSIKXGYA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE88zPNSgDHRh72XdRGKmsEnZ69MrfmdfKYljIHggs7tAiEAqsQebLDjPtUfUk37D2sx5yMIhjevLy0Kx8MMW%2FvIDqAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGZiEQrSy6QxTOn1fyrcA1FWb2t63bKTUBIF7ymX3%2FF6KfUAT8RqvilMWsMXh0o5LREARXZZsAXgzXLlBvW0Ie50%2BF44Ls6NgmrtAC0AFnVTi%2FxdJFd3bFafCugdjVQKfQCXSDJqbwtPAmRfpy92cG1qqMf3nxWo3BHL6kaYyLoXY1UouYv2bIze%2FrOj%2FOeWpINlqmW2Zfllyhy0qR4OjMiMtJXBPxfn%2B%2FtwuEapmy47BAuPeN8V57Mlx6q%2FhRg1KYzVku6ObvOI9gBEvgm%2BPKD%2FAqp%2For9I9QVGTVXKIOpybn%2BuI3dnmKx2rzR0Oam5MsDJS3nEqtcSL4yFvVF%2FrUd7nwlVchNL5ywyt3PUGEMy39XPjKrnfUwYWUhmY%2BfyZBhmaKlECtvLR9fKpjPZ3upHgt34O9ciRPWq2zXz22iidr%2Bu6IU0rdRvOwHeofO5nyZg4yA31gX0Z57iPP0qfinc%2FJDb5aMCAfuuGWxuW8jxHfTtnEe0j9XAcD%2BJG8z3yK1UjIlJtqHp%2BiXpZy8UrOP2bSrGT%2BHW6%2By2ib2c06Ot8SjHzCaFpiAjQdSLM9IJ84hg0nJ8ujJ1A8Ev2d1%2FqoSq2G4yCPF4qL9qjhq%2FhXUOQdTdcGOhCCYFw9YPVDgYFDS2HCLQSNOJv%2BqkMOXx2cwGOqUBZ7SSz%2BOo4Ud57QcgbwWIcX%2BJBDaEZ2fIYevIG0x9cy%2BMWe%2FONvatMPLjpp31Jifnz%2B7uiAoi2Tp3WswtsBh3bGn6ih0eDL%2Fl63LIiujyUan52OEXnhKrq0n9%2FJxXQ80xZb9wNdl0L60Q833Ml7ZDR%2BybKXdpOSDBbjLSBYZ%2BdR5Lk4%2B3O2AopLSbk0%2Ffdq%2BxdRQnwisRH%2BmV4MnxS5749lTfoLpi&X-Amz-Signature=ff69f0bbbd1d074fe84d1ee03433b3881b437fb12ba5883a755cb7f4b6171cd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

