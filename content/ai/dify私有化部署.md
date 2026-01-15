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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUBAC3Z4%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQD19lhUsO1oJu6dLtdhbpNcVsmLBupIuv1lUoDZrEnBCAIgUWvT9pzmEG3KbPdEO%2BzCKHBCrnrNc0LxUvLbTuhXmWgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIc2WetTmMNeUzJrSircA1xLIrDKMqfaoAwvrxhS8muikRgySqc5PiGaa1raGVOptMQNRgy4QCCy8InYmPleM3bW2TWC2eriar0mOvTUfGbMTvwdBnNP%2BmfWIZSgGomqIwDTOYKb7u%2BjnaLHEQduxS8AXtv4iGkvn4eja%2F3mfw2xDYi4uwuj8BRyz96mT5NOVo25%2FEGm8jeWfSuqAviSBkHld4wTJ9xGRXNmNmol22%2FG4fT8uq5v0mXjo6dpzuPcKuS%2Be%2FZF8WEW03kCVin8vmkcrAuzw4%2F7AzyVg0wdov2%2Fki6RrKo6fvwOLU1b22rGLpF%2FnNXYJZXI36IQMctcqnOlj%2BxAem0LDDTyznYWEfjgP8yz4bXPfk%2Fo0MIpX%2Fe04MgZ5TiCBBX41CYRrRJ9Vs%2B4SDNPwv0SSqgWP2GD4POg6bcbUiSHTedh5DlOs3QGWVN1y5GR9prz%2BtYv5tr6PtWSiWuKB%2FWwTe1%2Bg4kPyBKc6qWGu9uOMOrGxWIlRRgA4%2BFKrphvSi82nZ3oWBUpN1JGjVEgwEuH0n5f%2Fvjh5AqHvUZNKwnBw280Q0E5Ii0Ecy7xh%2FCLZ4muHNXbYKx6RcEUAdXPS0CFycJkIzdhFeEgCKCiCQoJrmf%2BzL5M71Y3X1Khn9FfiZLig2a7MOqaocsGOqUBNMYL2g62I4t909klh1i6FTXwBvH34bJ%2BgKkvIYOkagAk8pxk3FE61K%2Fc6F27TPpks0ymd7vvFjtiaJKpHxT0q4Ht4hwHL0X0Y%2B5QQIa5aP0M%2F5C4r1rAV7I8lpWB5%2BjlihJ%2FC44CTcY4n6oBSVhHlHRLUV89r5NI7ileYPmjVQ%2ByAIB1Vc5g9Svuu%2BVF7LmeiLaYbL%2BLnqBZqlMwZstoyWx6VUmQ&X-Amz-Signature=88cc8cb1e4fcf759615ac96ee0a0dbc98389fabef7b6f4090e8d018172e05825&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUBAC3Z4%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQD19lhUsO1oJu6dLtdhbpNcVsmLBupIuv1lUoDZrEnBCAIgUWvT9pzmEG3KbPdEO%2BzCKHBCrnrNc0LxUvLbTuhXmWgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIc2WetTmMNeUzJrSircA1xLIrDKMqfaoAwvrxhS8muikRgySqc5PiGaa1raGVOptMQNRgy4QCCy8InYmPleM3bW2TWC2eriar0mOvTUfGbMTvwdBnNP%2BmfWIZSgGomqIwDTOYKb7u%2BjnaLHEQduxS8AXtv4iGkvn4eja%2F3mfw2xDYi4uwuj8BRyz96mT5NOVo25%2FEGm8jeWfSuqAviSBkHld4wTJ9xGRXNmNmol22%2FG4fT8uq5v0mXjo6dpzuPcKuS%2Be%2FZF8WEW03kCVin8vmkcrAuzw4%2F7AzyVg0wdov2%2Fki6RrKo6fvwOLU1b22rGLpF%2FnNXYJZXI36IQMctcqnOlj%2BxAem0LDDTyznYWEfjgP8yz4bXPfk%2Fo0MIpX%2Fe04MgZ5TiCBBX41CYRrRJ9Vs%2B4SDNPwv0SSqgWP2GD4POg6bcbUiSHTedh5DlOs3QGWVN1y5GR9prz%2BtYv5tr6PtWSiWuKB%2FWwTe1%2Bg4kPyBKc6qWGu9uOMOrGxWIlRRgA4%2BFKrphvSi82nZ3oWBUpN1JGjVEgwEuH0n5f%2Fvjh5AqHvUZNKwnBw280Q0E5Ii0Ecy7xh%2FCLZ4muHNXbYKx6RcEUAdXPS0CFycJkIzdhFeEgCKCiCQoJrmf%2BzL5M71Y3X1Khn9FfiZLig2a7MOqaocsGOqUBNMYL2g62I4t909klh1i6FTXwBvH34bJ%2BgKkvIYOkagAk8pxk3FE61K%2Fc6F27TPpks0ymd7vvFjtiaJKpHxT0q4Ht4hwHL0X0Y%2B5QQIa5aP0M%2F5C4r1rAV7I8lpWB5%2BjlihJ%2FC44CTcY4n6oBSVhHlHRLUV89r5NI7ileYPmjVQ%2ByAIB1Vc5g9Svuu%2BVF7LmeiLaYbL%2BLnqBZqlMwZstoyWx6VUmQ&X-Amz-Signature=b373be7f0eb96c336a6a5c4484037439c83e527e39da3ecaa30edce8000a5769&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUBAC3Z4%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQD19lhUsO1oJu6dLtdhbpNcVsmLBupIuv1lUoDZrEnBCAIgUWvT9pzmEG3KbPdEO%2BzCKHBCrnrNc0LxUvLbTuhXmWgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIc2WetTmMNeUzJrSircA1xLIrDKMqfaoAwvrxhS8muikRgySqc5PiGaa1raGVOptMQNRgy4QCCy8InYmPleM3bW2TWC2eriar0mOvTUfGbMTvwdBnNP%2BmfWIZSgGomqIwDTOYKb7u%2BjnaLHEQduxS8AXtv4iGkvn4eja%2F3mfw2xDYi4uwuj8BRyz96mT5NOVo25%2FEGm8jeWfSuqAviSBkHld4wTJ9xGRXNmNmol22%2FG4fT8uq5v0mXjo6dpzuPcKuS%2Be%2FZF8WEW03kCVin8vmkcrAuzw4%2F7AzyVg0wdov2%2Fki6RrKo6fvwOLU1b22rGLpF%2FnNXYJZXI36IQMctcqnOlj%2BxAem0LDDTyznYWEfjgP8yz4bXPfk%2Fo0MIpX%2Fe04MgZ5TiCBBX41CYRrRJ9Vs%2B4SDNPwv0SSqgWP2GD4POg6bcbUiSHTedh5DlOs3QGWVN1y5GR9prz%2BtYv5tr6PtWSiWuKB%2FWwTe1%2Bg4kPyBKc6qWGu9uOMOrGxWIlRRgA4%2BFKrphvSi82nZ3oWBUpN1JGjVEgwEuH0n5f%2Fvjh5AqHvUZNKwnBw280Q0E5Ii0Ecy7xh%2FCLZ4muHNXbYKx6RcEUAdXPS0CFycJkIzdhFeEgCKCiCQoJrmf%2BzL5M71Y3X1Khn9FfiZLig2a7MOqaocsGOqUBNMYL2g62I4t909klh1i6FTXwBvH34bJ%2BgKkvIYOkagAk8pxk3FE61K%2Fc6F27TPpks0ymd7vvFjtiaJKpHxT0q4Ht4hwHL0X0Y%2B5QQIa5aP0M%2F5C4r1rAV7I8lpWB5%2BjlihJ%2FC44CTcY4n6oBSVhHlHRLUV89r5NI7ileYPmjVQ%2ByAIB1Vc5g9Svuu%2BVF7LmeiLaYbL%2BLnqBZqlMwZstoyWx6VUmQ&X-Amz-Signature=22ed0ab34296fbda17159583308a18dd425d809a6971777374a9b41a089011d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUBAC3Z4%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQD19lhUsO1oJu6dLtdhbpNcVsmLBupIuv1lUoDZrEnBCAIgUWvT9pzmEG3KbPdEO%2BzCKHBCrnrNc0LxUvLbTuhXmWgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIc2WetTmMNeUzJrSircA1xLIrDKMqfaoAwvrxhS8muikRgySqc5PiGaa1raGVOptMQNRgy4QCCy8InYmPleM3bW2TWC2eriar0mOvTUfGbMTvwdBnNP%2BmfWIZSgGomqIwDTOYKb7u%2BjnaLHEQduxS8AXtv4iGkvn4eja%2F3mfw2xDYi4uwuj8BRyz96mT5NOVo25%2FEGm8jeWfSuqAviSBkHld4wTJ9xGRXNmNmol22%2FG4fT8uq5v0mXjo6dpzuPcKuS%2Be%2FZF8WEW03kCVin8vmkcrAuzw4%2F7AzyVg0wdov2%2Fki6RrKo6fvwOLU1b22rGLpF%2FnNXYJZXI36IQMctcqnOlj%2BxAem0LDDTyznYWEfjgP8yz4bXPfk%2Fo0MIpX%2Fe04MgZ5TiCBBX41CYRrRJ9Vs%2B4SDNPwv0SSqgWP2GD4POg6bcbUiSHTedh5DlOs3QGWVN1y5GR9prz%2BtYv5tr6PtWSiWuKB%2FWwTe1%2Bg4kPyBKc6qWGu9uOMOrGxWIlRRgA4%2BFKrphvSi82nZ3oWBUpN1JGjVEgwEuH0n5f%2Fvjh5AqHvUZNKwnBw280Q0E5Ii0Ecy7xh%2FCLZ4muHNXbYKx6RcEUAdXPS0CFycJkIzdhFeEgCKCiCQoJrmf%2BzL5M71Y3X1Khn9FfiZLig2a7MOqaocsGOqUBNMYL2g62I4t909klh1i6FTXwBvH34bJ%2BgKkvIYOkagAk8pxk3FE61K%2Fc6F27TPpks0ymd7vvFjtiaJKpHxT0q4Ht4hwHL0X0Y%2B5QQIa5aP0M%2F5C4r1rAV7I8lpWB5%2BjlihJ%2FC44CTcY4n6oBSVhHlHRLUV89r5NI7ileYPmjVQ%2ByAIB1Vc5g9Svuu%2BVF7LmeiLaYbL%2BLnqBZqlMwZstoyWx6VUmQ&X-Amz-Signature=30afe47a75fb50f42d680f92d1ac4dd04381fd961e30266027db2226824dbe70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUBAC3Z4%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQD19lhUsO1oJu6dLtdhbpNcVsmLBupIuv1lUoDZrEnBCAIgUWvT9pzmEG3KbPdEO%2BzCKHBCrnrNc0LxUvLbTuhXmWgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIc2WetTmMNeUzJrSircA1xLIrDKMqfaoAwvrxhS8muikRgySqc5PiGaa1raGVOptMQNRgy4QCCy8InYmPleM3bW2TWC2eriar0mOvTUfGbMTvwdBnNP%2BmfWIZSgGomqIwDTOYKb7u%2BjnaLHEQduxS8AXtv4iGkvn4eja%2F3mfw2xDYi4uwuj8BRyz96mT5NOVo25%2FEGm8jeWfSuqAviSBkHld4wTJ9xGRXNmNmol22%2FG4fT8uq5v0mXjo6dpzuPcKuS%2Be%2FZF8WEW03kCVin8vmkcrAuzw4%2F7AzyVg0wdov2%2Fki6RrKo6fvwOLU1b22rGLpF%2FnNXYJZXI36IQMctcqnOlj%2BxAem0LDDTyznYWEfjgP8yz4bXPfk%2Fo0MIpX%2Fe04MgZ5TiCBBX41CYRrRJ9Vs%2B4SDNPwv0SSqgWP2GD4POg6bcbUiSHTedh5DlOs3QGWVN1y5GR9prz%2BtYv5tr6PtWSiWuKB%2FWwTe1%2Bg4kPyBKc6qWGu9uOMOrGxWIlRRgA4%2BFKrphvSi82nZ3oWBUpN1JGjVEgwEuH0n5f%2Fvjh5AqHvUZNKwnBw280Q0E5Ii0Ecy7xh%2FCLZ4muHNXbYKx6RcEUAdXPS0CFycJkIzdhFeEgCKCiCQoJrmf%2BzL5M71Y3X1Khn9FfiZLig2a7MOqaocsGOqUBNMYL2g62I4t909klh1i6FTXwBvH34bJ%2BgKkvIYOkagAk8pxk3FE61K%2Fc6F27TPpks0ymd7vvFjtiaJKpHxT0q4Ht4hwHL0X0Y%2B5QQIa5aP0M%2F5C4r1rAV7I8lpWB5%2BjlihJ%2FC44CTcY4n6oBSVhHlHRLUV89r5NI7ileYPmjVQ%2ByAIB1Vc5g9Svuu%2BVF7LmeiLaYbL%2BLnqBZqlMwZstoyWx6VUmQ&X-Amz-Signature=19696d2c6fecfa09fe80820852810d5714be36d22cf07b43eb6bd32a86d1f052&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUBAC3Z4%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQD19lhUsO1oJu6dLtdhbpNcVsmLBupIuv1lUoDZrEnBCAIgUWvT9pzmEG3KbPdEO%2BzCKHBCrnrNc0LxUvLbTuhXmWgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIc2WetTmMNeUzJrSircA1xLIrDKMqfaoAwvrxhS8muikRgySqc5PiGaa1raGVOptMQNRgy4QCCy8InYmPleM3bW2TWC2eriar0mOvTUfGbMTvwdBnNP%2BmfWIZSgGomqIwDTOYKb7u%2BjnaLHEQduxS8AXtv4iGkvn4eja%2F3mfw2xDYi4uwuj8BRyz96mT5NOVo25%2FEGm8jeWfSuqAviSBkHld4wTJ9xGRXNmNmol22%2FG4fT8uq5v0mXjo6dpzuPcKuS%2Be%2FZF8WEW03kCVin8vmkcrAuzw4%2F7AzyVg0wdov2%2Fki6RrKo6fvwOLU1b22rGLpF%2FnNXYJZXI36IQMctcqnOlj%2BxAem0LDDTyznYWEfjgP8yz4bXPfk%2Fo0MIpX%2Fe04MgZ5TiCBBX41CYRrRJ9Vs%2B4SDNPwv0SSqgWP2GD4POg6bcbUiSHTedh5DlOs3QGWVN1y5GR9prz%2BtYv5tr6PtWSiWuKB%2FWwTe1%2Bg4kPyBKc6qWGu9uOMOrGxWIlRRgA4%2BFKrphvSi82nZ3oWBUpN1JGjVEgwEuH0n5f%2Fvjh5AqHvUZNKwnBw280Q0E5Ii0Ecy7xh%2FCLZ4muHNXbYKx6RcEUAdXPS0CFycJkIzdhFeEgCKCiCQoJrmf%2BzL5M71Y3X1Khn9FfiZLig2a7MOqaocsGOqUBNMYL2g62I4t909klh1i6FTXwBvH34bJ%2BgKkvIYOkagAk8pxk3FE61K%2Fc6F27TPpks0ymd7vvFjtiaJKpHxT0q4Ht4hwHL0X0Y%2B5QQIa5aP0M%2F5C4r1rAV7I8lpWB5%2BjlihJ%2FC44CTcY4n6oBSVhHlHRLUV89r5NI7ileYPmjVQ%2ByAIB1Vc5g9Svuu%2BVF7LmeiLaYbL%2BLnqBZqlMwZstoyWx6VUmQ&X-Amz-Signature=d0f181469ba177a8254dda3fe5e207cf6eb75805236805594276d5ef934f314d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUBAC3Z4%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQD19lhUsO1oJu6dLtdhbpNcVsmLBupIuv1lUoDZrEnBCAIgUWvT9pzmEG3KbPdEO%2BzCKHBCrnrNc0LxUvLbTuhXmWgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIc2WetTmMNeUzJrSircA1xLIrDKMqfaoAwvrxhS8muikRgySqc5PiGaa1raGVOptMQNRgy4QCCy8InYmPleM3bW2TWC2eriar0mOvTUfGbMTvwdBnNP%2BmfWIZSgGomqIwDTOYKb7u%2BjnaLHEQduxS8AXtv4iGkvn4eja%2F3mfw2xDYi4uwuj8BRyz96mT5NOVo25%2FEGm8jeWfSuqAviSBkHld4wTJ9xGRXNmNmol22%2FG4fT8uq5v0mXjo6dpzuPcKuS%2Be%2FZF8WEW03kCVin8vmkcrAuzw4%2F7AzyVg0wdov2%2Fki6RrKo6fvwOLU1b22rGLpF%2FnNXYJZXI36IQMctcqnOlj%2BxAem0LDDTyznYWEfjgP8yz4bXPfk%2Fo0MIpX%2Fe04MgZ5TiCBBX41CYRrRJ9Vs%2B4SDNPwv0SSqgWP2GD4POg6bcbUiSHTedh5DlOs3QGWVN1y5GR9prz%2BtYv5tr6PtWSiWuKB%2FWwTe1%2Bg4kPyBKc6qWGu9uOMOrGxWIlRRgA4%2BFKrphvSi82nZ3oWBUpN1JGjVEgwEuH0n5f%2Fvjh5AqHvUZNKwnBw280Q0E5Ii0Ecy7xh%2FCLZ4muHNXbYKx6RcEUAdXPS0CFycJkIzdhFeEgCKCiCQoJrmf%2BzL5M71Y3X1Khn9FfiZLig2a7MOqaocsGOqUBNMYL2g62I4t909klh1i6FTXwBvH34bJ%2BgKkvIYOkagAk8pxk3FE61K%2Fc6F27TPpks0ymd7vvFjtiaJKpHxT0q4Ht4hwHL0X0Y%2B5QQIa5aP0M%2F5C4r1rAV7I8lpWB5%2BjlihJ%2FC44CTcY4n6oBSVhHlHRLUV89r5NI7ileYPmjVQ%2ByAIB1Vc5g9Svuu%2BVF7LmeiLaYbL%2BLnqBZqlMwZstoyWx6VUmQ&X-Amz-Signature=2b27adbfffc2b4577f3dbed0dd42122411cd88998901577d6819ca6dd4dc8b72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUBAC3Z4%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQD19lhUsO1oJu6dLtdhbpNcVsmLBupIuv1lUoDZrEnBCAIgUWvT9pzmEG3KbPdEO%2BzCKHBCrnrNc0LxUvLbTuhXmWgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIc2WetTmMNeUzJrSircA1xLIrDKMqfaoAwvrxhS8muikRgySqc5PiGaa1raGVOptMQNRgy4QCCy8InYmPleM3bW2TWC2eriar0mOvTUfGbMTvwdBnNP%2BmfWIZSgGomqIwDTOYKb7u%2BjnaLHEQduxS8AXtv4iGkvn4eja%2F3mfw2xDYi4uwuj8BRyz96mT5NOVo25%2FEGm8jeWfSuqAviSBkHld4wTJ9xGRXNmNmol22%2FG4fT8uq5v0mXjo6dpzuPcKuS%2Be%2FZF8WEW03kCVin8vmkcrAuzw4%2F7AzyVg0wdov2%2Fki6RrKo6fvwOLU1b22rGLpF%2FnNXYJZXI36IQMctcqnOlj%2BxAem0LDDTyznYWEfjgP8yz4bXPfk%2Fo0MIpX%2Fe04MgZ5TiCBBX41CYRrRJ9Vs%2B4SDNPwv0SSqgWP2GD4POg6bcbUiSHTedh5DlOs3QGWVN1y5GR9prz%2BtYv5tr6PtWSiWuKB%2FWwTe1%2Bg4kPyBKc6qWGu9uOMOrGxWIlRRgA4%2BFKrphvSi82nZ3oWBUpN1JGjVEgwEuH0n5f%2Fvjh5AqHvUZNKwnBw280Q0E5Ii0Ecy7xh%2FCLZ4muHNXbYKx6RcEUAdXPS0CFycJkIzdhFeEgCKCiCQoJrmf%2BzL5M71Y3X1Khn9FfiZLig2a7MOqaocsGOqUBNMYL2g62I4t909klh1i6FTXwBvH34bJ%2BgKkvIYOkagAk8pxk3FE61K%2Fc6F27TPpks0ymd7vvFjtiaJKpHxT0q4Ht4hwHL0X0Y%2B5QQIa5aP0M%2F5C4r1rAV7I8lpWB5%2BjlihJ%2FC44CTcY4n6oBSVhHlHRLUV89r5NI7ileYPmjVQ%2ByAIB1Vc5g9Svuu%2BVF7LmeiLaYbL%2BLnqBZqlMwZstoyWx6VUmQ&X-Amz-Signature=9fab79e1a700ff14f9a4afe5d3cfaec6804b33d52f6e381a24d5cffe62141a28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUBAC3Z4%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQD19lhUsO1oJu6dLtdhbpNcVsmLBupIuv1lUoDZrEnBCAIgUWvT9pzmEG3KbPdEO%2BzCKHBCrnrNc0LxUvLbTuhXmWgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIc2WetTmMNeUzJrSircA1xLIrDKMqfaoAwvrxhS8muikRgySqc5PiGaa1raGVOptMQNRgy4QCCy8InYmPleM3bW2TWC2eriar0mOvTUfGbMTvwdBnNP%2BmfWIZSgGomqIwDTOYKb7u%2BjnaLHEQduxS8AXtv4iGkvn4eja%2F3mfw2xDYi4uwuj8BRyz96mT5NOVo25%2FEGm8jeWfSuqAviSBkHld4wTJ9xGRXNmNmol22%2FG4fT8uq5v0mXjo6dpzuPcKuS%2Be%2FZF8WEW03kCVin8vmkcrAuzw4%2F7AzyVg0wdov2%2Fki6RrKo6fvwOLU1b22rGLpF%2FnNXYJZXI36IQMctcqnOlj%2BxAem0LDDTyznYWEfjgP8yz4bXPfk%2Fo0MIpX%2Fe04MgZ5TiCBBX41CYRrRJ9Vs%2B4SDNPwv0SSqgWP2GD4POg6bcbUiSHTedh5DlOs3QGWVN1y5GR9prz%2BtYv5tr6PtWSiWuKB%2FWwTe1%2Bg4kPyBKc6qWGu9uOMOrGxWIlRRgA4%2BFKrphvSi82nZ3oWBUpN1JGjVEgwEuH0n5f%2Fvjh5AqHvUZNKwnBw280Q0E5Ii0Ecy7xh%2FCLZ4muHNXbYKx6RcEUAdXPS0CFycJkIzdhFeEgCKCiCQoJrmf%2BzL5M71Y3X1Khn9FfiZLig2a7MOqaocsGOqUBNMYL2g62I4t909klh1i6FTXwBvH34bJ%2BgKkvIYOkagAk8pxk3FE61K%2Fc6F27TPpks0ymd7vvFjtiaJKpHxT0q4Ht4hwHL0X0Y%2B5QQIa5aP0M%2F5C4r1rAV7I8lpWB5%2BjlihJ%2FC44CTcY4n6oBSVhHlHRLUV89r5NI7ileYPmjVQ%2ByAIB1Vc5g9Svuu%2BVF7LmeiLaYbL%2BLnqBZqlMwZstoyWx6VUmQ&X-Amz-Signature=6433085a9d6b4bd5d037350c98e1725a3369c0f924f60d1cec5980e22282622c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUBAC3Z4%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030046Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQD19lhUsO1oJu6dLtdhbpNcVsmLBupIuv1lUoDZrEnBCAIgUWvT9pzmEG3KbPdEO%2BzCKHBCrnrNc0LxUvLbTuhXmWgq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIc2WetTmMNeUzJrSircA1xLIrDKMqfaoAwvrxhS8muikRgySqc5PiGaa1raGVOptMQNRgy4QCCy8InYmPleM3bW2TWC2eriar0mOvTUfGbMTvwdBnNP%2BmfWIZSgGomqIwDTOYKb7u%2BjnaLHEQduxS8AXtv4iGkvn4eja%2F3mfw2xDYi4uwuj8BRyz96mT5NOVo25%2FEGm8jeWfSuqAviSBkHld4wTJ9xGRXNmNmol22%2FG4fT8uq5v0mXjo6dpzuPcKuS%2Be%2FZF8WEW03kCVin8vmkcrAuzw4%2F7AzyVg0wdov2%2Fki6RrKo6fvwOLU1b22rGLpF%2FnNXYJZXI36IQMctcqnOlj%2BxAem0LDDTyznYWEfjgP8yz4bXPfk%2Fo0MIpX%2Fe04MgZ5TiCBBX41CYRrRJ9Vs%2B4SDNPwv0SSqgWP2GD4POg6bcbUiSHTedh5DlOs3QGWVN1y5GR9prz%2BtYv5tr6PtWSiWuKB%2FWwTe1%2Bg4kPyBKc6qWGu9uOMOrGxWIlRRgA4%2BFKrphvSi82nZ3oWBUpN1JGjVEgwEuH0n5f%2Fvjh5AqHvUZNKwnBw280Q0E5Ii0Ecy7xh%2FCLZ4muHNXbYKx6RcEUAdXPS0CFycJkIzdhFeEgCKCiCQoJrmf%2BzL5M71Y3X1Khn9FfiZLig2a7MOqaocsGOqUBNMYL2g62I4t909klh1i6FTXwBvH34bJ%2BgKkvIYOkagAk8pxk3FE61K%2Fc6F27TPpks0ymd7vvFjtiaJKpHxT0q4Ht4hwHL0X0Y%2B5QQIa5aP0M%2F5C4r1rAV7I8lpWB5%2BjlihJ%2FC44CTcY4n6oBSVhHlHRLUV89r5NI7ileYPmjVQ%2ByAIB1Vc5g9Svuu%2BVF7LmeiLaYbL%2BLnqBZqlMwZstoyWx6VUmQ&X-Amz-Signature=52436538ca3e9c61045258e1f085c687f5030374acc74f06671bca9068f70191&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

