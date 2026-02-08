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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWOFZB5%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGBwwzF2TQLvuxPAX%2FoFf9lBGs2ZpZfG1d7HzpyR7AjEAiBT5I5oN60Z4Ig55i3ggYdTl4IbdVimeUodHWGZKUXpAir%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMEGv8gmK52Ph%2B3ayKKtwDv4QhN%2F0BwmVbyKfCKJrySlRncOSFaQ7K%2FQIoJSXdwrHZRIv00W4E24PjgWtm%2BJo3iATSAV7clc5Aqft1XmT%2BjYt8Gk%2Fk8nvm6kFJai%2BAbKXc1ljiq8G07EYdxPXvNYktz5jEBGCfFvueDqnOxaqKO0wOOPvixDrzgX5T4WsmZ7TKFyq2ohnR7d5sUBcoJpX79BXzIoWi9Q03DR%2FjaOh1K8VEXzxvTVVa3aot8wzlCOZqXuZZFyFYDjKfll7ZhCqChQgs5%2BmPutJx4plfoAXuOyYQxj7CLsUXOT7LyPoksURjG2%2B8gYugNdp0fkxk8dd00o7rHWuhE73wDpKWaEDWiLbwwtVebl2IEg%2F%2FnytN7sv3DvfL6%2B2LFWGi3WessrDrfmoCjf5Y76WFsgUFsDgqv%2BJxlE%2FHWGviLQBYTyXRHtb83fF4Kc8KEVpE9ku3Zf%2BIicAySdWsj8uAjDBc%2FCNWcQDcI%2FzKvChDoC9Ixniipw%2Fmm9c6mUuy0yBV0RHJ%2BnriZ%2BEX3glzVAIt3B6yB7ao3%2BqJFp%2Bz79gOPIvA8R5bS4uMrAnBYjTrEGZodjnhq0XRfUb1P5cFtOoWDQJs0SFlpW3MK4MLW%2BAuTVOtHBsGh4fgcEg4hxHjXhr670wwhYygzAY6pgFGcrXg1B3eHn0Gq%2BVVC1XC5GZoEwGyQmr2UeT3hyo8DnqhP9wGXpx3zFFKaqpZrUiRS1OxlLZ%2F%2F5v1XHp9I9m%2BZGKvFJXYU7%2BniAqa8kwI2ZFDyqsx6dSAK%2FgrE6QY%2BedMrmi5YtLxvH6Ba6lBiRd%2B9LvHFSBcppPLO9jCCk5oz3xFr2oB0TLxVfQBBAZR3p2DRdJNuQclph9FezM%2BoBru0ORpYa0W&X-Amz-Signature=1df4a4776dce9c0dd150882aca172a788e69598a45d1446495b3bea06c139af7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWOFZB5%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGBwwzF2TQLvuxPAX%2FoFf9lBGs2ZpZfG1d7HzpyR7AjEAiBT5I5oN60Z4Ig55i3ggYdTl4IbdVimeUodHWGZKUXpAir%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMEGv8gmK52Ph%2B3ayKKtwDv4QhN%2F0BwmVbyKfCKJrySlRncOSFaQ7K%2FQIoJSXdwrHZRIv00W4E24PjgWtm%2BJo3iATSAV7clc5Aqft1XmT%2BjYt8Gk%2Fk8nvm6kFJai%2BAbKXc1ljiq8G07EYdxPXvNYktz5jEBGCfFvueDqnOxaqKO0wOOPvixDrzgX5T4WsmZ7TKFyq2ohnR7d5sUBcoJpX79BXzIoWi9Q03DR%2FjaOh1K8VEXzxvTVVa3aot8wzlCOZqXuZZFyFYDjKfll7ZhCqChQgs5%2BmPutJx4plfoAXuOyYQxj7CLsUXOT7LyPoksURjG2%2B8gYugNdp0fkxk8dd00o7rHWuhE73wDpKWaEDWiLbwwtVebl2IEg%2F%2FnytN7sv3DvfL6%2B2LFWGi3WessrDrfmoCjf5Y76WFsgUFsDgqv%2BJxlE%2FHWGviLQBYTyXRHtb83fF4Kc8KEVpE9ku3Zf%2BIicAySdWsj8uAjDBc%2FCNWcQDcI%2FzKvChDoC9Ixniipw%2Fmm9c6mUuy0yBV0RHJ%2BnriZ%2BEX3glzVAIt3B6yB7ao3%2BqJFp%2Bz79gOPIvA8R5bS4uMrAnBYjTrEGZodjnhq0XRfUb1P5cFtOoWDQJs0SFlpW3MK4MLW%2BAuTVOtHBsGh4fgcEg4hxHjXhr670wwhYygzAY6pgFGcrXg1B3eHn0Gq%2BVVC1XC5GZoEwGyQmr2UeT3hyo8DnqhP9wGXpx3zFFKaqpZrUiRS1OxlLZ%2F%2F5v1XHp9I9m%2BZGKvFJXYU7%2BniAqa8kwI2ZFDyqsx6dSAK%2FgrE6QY%2BedMrmi5YtLxvH6Ba6lBiRd%2B9LvHFSBcppPLO9jCCk5oz3xFr2oB0TLxVfQBBAZR3p2DRdJNuQclph9FezM%2BoBru0ORpYa0W&X-Amz-Signature=9cb0904c3fe7152c00b683fb72ab3ace8a7d070d229129deb78f877f5fa580de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWOFZB5%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGBwwzF2TQLvuxPAX%2FoFf9lBGs2ZpZfG1d7HzpyR7AjEAiBT5I5oN60Z4Ig55i3ggYdTl4IbdVimeUodHWGZKUXpAir%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMEGv8gmK52Ph%2B3ayKKtwDv4QhN%2F0BwmVbyKfCKJrySlRncOSFaQ7K%2FQIoJSXdwrHZRIv00W4E24PjgWtm%2BJo3iATSAV7clc5Aqft1XmT%2BjYt8Gk%2Fk8nvm6kFJai%2BAbKXc1ljiq8G07EYdxPXvNYktz5jEBGCfFvueDqnOxaqKO0wOOPvixDrzgX5T4WsmZ7TKFyq2ohnR7d5sUBcoJpX79BXzIoWi9Q03DR%2FjaOh1K8VEXzxvTVVa3aot8wzlCOZqXuZZFyFYDjKfll7ZhCqChQgs5%2BmPutJx4plfoAXuOyYQxj7CLsUXOT7LyPoksURjG2%2B8gYugNdp0fkxk8dd00o7rHWuhE73wDpKWaEDWiLbwwtVebl2IEg%2F%2FnytN7sv3DvfL6%2B2LFWGi3WessrDrfmoCjf5Y76WFsgUFsDgqv%2BJxlE%2FHWGviLQBYTyXRHtb83fF4Kc8KEVpE9ku3Zf%2BIicAySdWsj8uAjDBc%2FCNWcQDcI%2FzKvChDoC9Ixniipw%2Fmm9c6mUuy0yBV0RHJ%2BnriZ%2BEX3glzVAIt3B6yB7ao3%2BqJFp%2Bz79gOPIvA8R5bS4uMrAnBYjTrEGZodjnhq0XRfUb1P5cFtOoWDQJs0SFlpW3MK4MLW%2BAuTVOtHBsGh4fgcEg4hxHjXhr670wwhYygzAY6pgFGcrXg1B3eHn0Gq%2BVVC1XC5GZoEwGyQmr2UeT3hyo8DnqhP9wGXpx3zFFKaqpZrUiRS1OxlLZ%2F%2F5v1XHp9I9m%2BZGKvFJXYU7%2BniAqa8kwI2ZFDyqsx6dSAK%2FgrE6QY%2BedMrmi5YtLxvH6Ba6lBiRd%2B9LvHFSBcppPLO9jCCk5oz3xFr2oB0TLxVfQBBAZR3p2DRdJNuQclph9FezM%2BoBru0ORpYa0W&X-Amz-Signature=89ecc6ec2e2fcb009d4af6f755115c42eaf21478fa1fc2f90828016e5815a853&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWOFZB5%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGBwwzF2TQLvuxPAX%2FoFf9lBGs2ZpZfG1d7HzpyR7AjEAiBT5I5oN60Z4Ig55i3ggYdTl4IbdVimeUodHWGZKUXpAir%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMEGv8gmK52Ph%2B3ayKKtwDv4QhN%2F0BwmVbyKfCKJrySlRncOSFaQ7K%2FQIoJSXdwrHZRIv00W4E24PjgWtm%2BJo3iATSAV7clc5Aqft1XmT%2BjYt8Gk%2Fk8nvm6kFJai%2BAbKXc1ljiq8G07EYdxPXvNYktz5jEBGCfFvueDqnOxaqKO0wOOPvixDrzgX5T4WsmZ7TKFyq2ohnR7d5sUBcoJpX79BXzIoWi9Q03DR%2FjaOh1K8VEXzxvTVVa3aot8wzlCOZqXuZZFyFYDjKfll7ZhCqChQgs5%2BmPutJx4plfoAXuOyYQxj7CLsUXOT7LyPoksURjG2%2B8gYugNdp0fkxk8dd00o7rHWuhE73wDpKWaEDWiLbwwtVebl2IEg%2F%2FnytN7sv3DvfL6%2B2LFWGi3WessrDrfmoCjf5Y76WFsgUFsDgqv%2BJxlE%2FHWGviLQBYTyXRHtb83fF4Kc8KEVpE9ku3Zf%2BIicAySdWsj8uAjDBc%2FCNWcQDcI%2FzKvChDoC9Ixniipw%2Fmm9c6mUuy0yBV0RHJ%2BnriZ%2BEX3glzVAIt3B6yB7ao3%2BqJFp%2Bz79gOPIvA8R5bS4uMrAnBYjTrEGZodjnhq0XRfUb1P5cFtOoWDQJs0SFlpW3MK4MLW%2BAuTVOtHBsGh4fgcEg4hxHjXhr670wwhYygzAY6pgFGcrXg1B3eHn0Gq%2BVVC1XC5GZoEwGyQmr2UeT3hyo8DnqhP9wGXpx3zFFKaqpZrUiRS1OxlLZ%2F%2F5v1XHp9I9m%2BZGKvFJXYU7%2BniAqa8kwI2ZFDyqsx6dSAK%2FgrE6QY%2BedMrmi5YtLxvH6Ba6lBiRd%2B9LvHFSBcppPLO9jCCk5oz3xFr2oB0TLxVfQBBAZR3p2DRdJNuQclph9FezM%2BoBru0ORpYa0W&X-Amz-Signature=128d0c5735d4c846ceeab87e65202208264c8ad12227f00a89d053c1a1f6751c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWOFZB5%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGBwwzF2TQLvuxPAX%2FoFf9lBGs2ZpZfG1d7HzpyR7AjEAiBT5I5oN60Z4Ig55i3ggYdTl4IbdVimeUodHWGZKUXpAir%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMEGv8gmK52Ph%2B3ayKKtwDv4QhN%2F0BwmVbyKfCKJrySlRncOSFaQ7K%2FQIoJSXdwrHZRIv00W4E24PjgWtm%2BJo3iATSAV7clc5Aqft1XmT%2BjYt8Gk%2Fk8nvm6kFJai%2BAbKXc1ljiq8G07EYdxPXvNYktz5jEBGCfFvueDqnOxaqKO0wOOPvixDrzgX5T4WsmZ7TKFyq2ohnR7d5sUBcoJpX79BXzIoWi9Q03DR%2FjaOh1K8VEXzxvTVVa3aot8wzlCOZqXuZZFyFYDjKfll7ZhCqChQgs5%2BmPutJx4plfoAXuOyYQxj7CLsUXOT7LyPoksURjG2%2B8gYugNdp0fkxk8dd00o7rHWuhE73wDpKWaEDWiLbwwtVebl2IEg%2F%2FnytN7sv3DvfL6%2B2LFWGi3WessrDrfmoCjf5Y76WFsgUFsDgqv%2BJxlE%2FHWGviLQBYTyXRHtb83fF4Kc8KEVpE9ku3Zf%2BIicAySdWsj8uAjDBc%2FCNWcQDcI%2FzKvChDoC9Ixniipw%2Fmm9c6mUuy0yBV0RHJ%2BnriZ%2BEX3glzVAIt3B6yB7ao3%2BqJFp%2Bz79gOPIvA8R5bS4uMrAnBYjTrEGZodjnhq0XRfUb1P5cFtOoWDQJs0SFlpW3MK4MLW%2BAuTVOtHBsGh4fgcEg4hxHjXhr670wwhYygzAY6pgFGcrXg1B3eHn0Gq%2BVVC1XC5GZoEwGyQmr2UeT3hyo8DnqhP9wGXpx3zFFKaqpZrUiRS1OxlLZ%2F%2F5v1XHp9I9m%2BZGKvFJXYU7%2BniAqa8kwI2ZFDyqsx6dSAK%2FgrE6QY%2BedMrmi5YtLxvH6Ba6lBiRd%2B9LvHFSBcppPLO9jCCk5oz3xFr2oB0TLxVfQBBAZR3p2DRdJNuQclph9FezM%2BoBru0ORpYa0W&X-Amz-Signature=2b9a3855b4a47b8f3642eef361a75d2f2282005732ad4c77555599f6cd16f176&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWOFZB5%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGBwwzF2TQLvuxPAX%2FoFf9lBGs2ZpZfG1d7HzpyR7AjEAiBT5I5oN60Z4Ig55i3ggYdTl4IbdVimeUodHWGZKUXpAir%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMEGv8gmK52Ph%2B3ayKKtwDv4QhN%2F0BwmVbyKfCKJrySlRncOSFaQ7K%2FQIoJSXdwrHZRIv00W4E24PjgWtm%2BJo3iATSAV7clc5Aqft1XmT%2BjYt8Gk%2Fk8nvm6kFJai%2BAbKXc1ljiq8G07EYdxPXvNYktz5jEBGCfFvueDqnOxaqKO0wOOPvixDrzgX5T4WsmZ7TKFyq2ohnR7d5sUBcoJpX79BXzIoWi9Q03DR%2FjaOh1K8VEXzxvTVVa3aot8wzlCOZqXuZZFyFYDjKfll7ZhCqChQgs5%2BmPutJx4plfoAXuOyYQxj7CLsUXOT7LyPoksURjG2%2B8gYugNdp0fkxk8dd00o7rHWuhE73wDpKWaEDWiLbwwtVebl2IEg%2F%2FnytN7sv3DvfL6%2B2LFWGi3WessrDrfmoCjf5Y76WFsgUFsDgqv%2BJxlE%2FHWGviLQBYTyXRHtb83fF4Kc8KEVpE9ku3Zf%2BIicAySdWsj8uAjDBc%2FCNWcQDcI%2FzKvChDoC9Ixniipw%2Fmm9c6mUuy0yBV0RHJ%2BnriZ%2BEX3glzVAIt3B6yB7ao3%2BqJFp%2Bz79gOPIvA8R5bS4uMrAnBYjTrEGZodjnhq0XRfUb1P5cFtOoWDQJs0SFlpW3MK4MLW%2BAuTVOtHBsGh4fgcEg4hxHjXhr670wwhYygzAY6pgFGcrXg1B3eHn0Gq%2BVVC1XC5GZoEwGyQmr2UeT3hyo8DnqhP9wGXpx3zFFKaqpZrUiRS1OxlLZ%2F%2F5v1XHp9I9m%2BZGKvFJXYU7%2BniAqa8kwI2ZFDyqsx6dSAK%2FgrE6QY%2BedMrmi5YtLxvH6Ba6lBiRd%2B9LvHFSBcppPLO9jCCk5oz3xFr2oB0TLxVfQBBAZR3p2DRdJNuQclph9FezM%2BoBru0ORpYa0W&X-Amz-Signature=29396d378890a600b08041c66f7aae0d6fee2c9eda720d66f721574185438b80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWOFZB5%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGBwwzF2TQLvuxPAX%2FoFf9lBGs2ZpZfG1d7HzpyR7AjEAiBT5I5oN60Z4Ig55i3ggYdTl4IbdVimeUodHWGZKUXpAir%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMEGv8gmK52Ph%2B3ayKKtwDv4QhN%2F0BwmVbyKfCKJrySlRncOSFaQ7K%2FQIoJSXdwrHZRIv00W4E24PjgWtm%2BJo3iATSAV7clc5Aqft1XmT%2BjYt8Gk%2Fk8nvm6kFJai%2BAbKXc1ljiq8G07EYdxPXvNYktz5jEBGCfFvueDqnOxaqKO0wOOPvixDrzgX5T4WsmZ7TKFyq2ohnR7d5sUBcoJpX79BXzIoWi9Q03DR%2FjaOh1K8VEXzxvTVVa3aot8wzlCOZqXuZZFyFYDjKfll7ZhCqChQgs5%2BmPutJx4plfoAXuOyYQxj7CLsUXOT7LyPoksURjG2%2B8gYugNdp0fkxk8dd00o7rHWuhE73wDpKWaEDWiLbwwtVebl2IEg%2F%2FnytN7sv3DvfL6%2B2LFWGi3WessrDrfmoCjf5Y76WFsgUFsDgqv%2BJxlE%2FHWGviLQBYTyXRHtb83fF4Kc8KEVpE9ku3Zf%2BIicAySdWsj8uAjDBc%2FCNWcQDcI%2FzKvChDoC9Ixniipw%2Fmm9c6mUuy0yBV0RHJ%2BnriZ%2BEX3glzVAIt3B6yB7ao3%2BqJFp%2Bz79gOPIvA8R5bS4uMrAnBYjTrEGZodjnhq0XRfUb1P5cFtOoWDQJs0SFlpW3MK4MLW%2BAuTVOtHBsGh4fgcEg4hxHjXhr670wwhYygzAY6pgFGcrXg1B3eHn0Gq%2BVVC1XC5GZoEwGyQmr2UeT3hyo8DnqhP9wGXpx3zFFKaqpZrUiRS1OxlLZ%2F%2F5v1XHp9I9m%2BZGKvFJXYU7%2BniAqa8kwI2ZFDyqsx6dSAK%2FgrE6QY%2BedMrmi5YtLxvH6Ba6lBiRd%2B9LvHFSBcppPLO9jCCk5oz3xFr2oB0TLxVfQBBAZR3p2DRdJNuQclph9FezM%2BoBru0ORpYa0W&X-Amz-Signature=ff00396279ed55466832630155321ff021d298505eba95b2aa802554f2cd7e14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWOFZB5%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGBwwzF2TQLvuxPAX%2FoFf9lBGs2ZpZfG1d7HzpyR7AjEAiBT5I5oN60Z4Ig55i3ggYdTl4IbdVimeUodHWGZKUXpAir%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMEGv8gmK52Ph%2B3ayKKtwDv4QhN%2F0BwmVbyKfCKJrySlRncOSFaQ7K%2FQIoJSXdwrHZRIv00W4E24PjgWtm%2BJo3iATSAV7clc5Aqft1XmT%2BjYt8Gk%2Fk8nvm6kFJai%2BAbKXc1ljiq8G07EYdxPXvNYktz5jEBGCfFvueDqnOxaqKO0wOOPvixDrzgX5T4WsmZ7TKFyq2ohnR7d5sUBcoJpX79BXzIoWi9Q03DR%2FjaOh1K8VEXzxvTVVa3aot8wzlCOZqXuZZFyFYDjKfll7ZhCqChQgs5%2BmPutJx4plfoAXuOyYQxj7CLsUXOT7LyPoksURjG2%2B8gYugNdp0fkxk8dd00o7rHWuhE73wDpKWaEDWiLbwwtVebl2IEg%2F%2FnytN7sv3DvfL6%2B2LFWGi3WessrDrfmoCjf5Y76WFsgUFsDgqv%2BJxlE%2FHWGviLQBYTyXRHtb83fF4Kc8KEVpE9ku3Zf%2BIicAySdWsj8uAjDBc%2FCNWcQDcI%2FzKvChDoC9Ixniipw%2Fmm9c6mUuy0yBV0RHJ%2BnriZ%2BEX3glzVAIt3B6yB7ao3%2BqJFp%2Bz79gOPIvA8R5bS4uMrAnBYjTrEGZodjnhq0XRfUb1P5cFtOoWDQJs0SFlpW3MK4MLW%2BAuTVOtHBsGh4fgcEg4hxHjXhr670wwhYygzAY6pgFGcrXg1B3eHn0Gq%2BVVC1XC5GZoEwGyQmr2UeT3hyo8DnqhP9wGXpx3zFFKaqpZrUiRS1OxlLZ%2F%2F5v1XHp9I9m%2BZGKvFJXYU7%2BniAqa8kwI2ZFDyqsx6dSAK%2FgrE6QY%2BedMrmi5YtLxvH6Ba6lBiRd%2B9LvHFSBcppPLO9jCCk5oz3xFr2oB0TLxVfQBBAZR3p2DRdJNuQclph9FezM%2BoBru0ORpYa0W&X-Amz-Signature=1cb5cf4d82c4ac534ab54461ba30f67bb81c18291faa2c108d01f51f72f40ab3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWOFZB5%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGBwwzF2TQLvuxPAX%2FoFf9lBGs2ZpZfG1d7HzpyR7AjEAiBT5I5oN60Z4Ig55i3ggYdTl4IbdVimeUodHWGZKUXpAir%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMEGv8gmK52Ph%2B3ayKKtwDv4QhN%2F0BwmVbyKfCKJrySlRncOSFaQ7K%2FQIoJSXdwrHZRIv00W4E24PjgWtm%2BJo3iATSAV7clc5Aqft1XmT%2BjYt8Gk%2Fk8nvm6kFJai%2BAbKXc1ljiq8G07EYdxPXvNYktz5jEBGCfFvueDqnOxaqKO0wOOPvixDrzgX5T4WsmZ7TKFyq2ohnR7d5sUBcoJpX79BXzIoWi9Q03DR%2FjaOh1K8VEXzxvTVVa3aot8wzlCOZqXuZZFyFYDjKfll7ZhCqChQgs5%2BmPutJx4plfoAXuOyYQxj7CLsUXOT7LyPoksURjG2%2B8gYugNdp0fkxk8dd00o7rHWuhE73wDpKWaEDWiLbwwtVebl2IEg%2F%2FnytN7sv3DvfL6%2B2LFWGi3WessrDrfmoCjf5Y76WFsgUFsDgqv%2BJxlE%2FHWGviLQBYTyXRHtb83fF4Kc8KEVpE9ku3Zf%2BIicAySdWsj8uAjDBc%2FCNWcQDcI%2FzKvChDoC9Ixniipw%2Fmm9c6mUuy0yBV0RHJ%2BnriZ%2BEX3glzVAIt3B6yB7ao3%2BqJFp%2Bz79gOPIvA8R5bS4uMrAnBYjTrEGZodjnhq0XRfUb1P5cFtOoWDQJs0SFlpW3MK4MLW%2BAuTVOtHBsGh4fgcEg4hxHjXhr670wwhYygzAY6pgFGcrXg1B3eHn0Gq%2BVVC1XC5GZoEwGyQmr2UeT3hyo8DnqhP9wGXpx3zFFKaqpZrUiRS1OxlLZ%2F%2F5v1XHp9I9m%2BZGKvFJXYU7%2BniAqa8kwI2ZFDyqsx6dSAK%2FgrE6QY%2BedMrmi5YtLxvH6Ba6lBiRd%2B9LvHFSBcppPLO9jCCk5oz3xFr2oB0TLxVfQBBAZR3p2DRdJNuQclph9FezM%2BoBru0ORpYa0W&X-Amz-Signature=2d8b1543f72a7ca610cfc31443b826927480eefde0f3efafdd1106cdc0841212&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BWOFZB5%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGBwwzF2TQLvuxPAX%2FoFf9lBGs2ZpZfG1d7HzpyR7AjEAiBT5I5oN60Z4Ig55i3ggYdTl4IbdVimeUodHWGZKUXpAir%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMEGv8gmK52Ph%2B3ayKKtwDv4QhN%2F0BwmVbyKfCKJrySlRncOSFaQ7K%2FQIoJSXdwrHZRIv00W4E24PjgWtm%2BJo3iATSAV7clc5Aqft1XmT%2BjYt8Gk%2Fk8nvm6kFJai%2BAbKXc1ljiq8G07EYdxPXvNYktz5jEBGCfFvueDqnOxaqKO0wOOPvixDrzgX5T4WsmZ7TKFyq2ohnR7d5sUBcoJpX79BXzIoWi9Q03DR%2FjaOh1K8VEXzxvTVVa3aot8wzlCOZqXuZZFyFYDjKfll7ZhCqChQgs5%2BmPutJx4plfoAXuOyYQxj7CLsUXOT7LyPoksURjG2%2B8gYugNdp0fkxk8dd00o7rHWuhE73wDpKWaEDWiLbwwtVebl2IEg%2F%2FnytN7sv3DvfL6%2B2LFWGi3WessrDrfmoCjf5Y76WFsgUFsDgqv%2BJxlE%2FHWGviLQBYTyXRHtb83fF4Kc8KEVpE9ku3Zf%2BIicAySdWsj8uAjDBc%2FCNWcQDcI%2FzKvChDoC9Ixniipw%2Fmm9c6mUuy0yBV0RHJ%2BnriZ%2BEX3glzVAIt3B6yB7ao3%2BqJFp%2Bz79gOPIvA8R5bS4uMrAnBYjTrEGZodjnhq0XRfUb1P5cFtOoWDQJs0SFlpW3MK4MLW%2BAuTVOtHBsGh4fgcEg4hxHjXhr670wwhYygzAY6pgFGcrXg1B3eHn0Gq%2BVVC1XC5GZoEwGyQmr2UeT3hyo8DnqhP9wGXpx3zFFKaqpZrUiRS1OxlLZ%2F%2F5v1XHp9I9m%2BZGKvFJXYU7%2BniAqa8kwI2ZFDyqsx6dSAK%2FgrE6QY%2BedMrmi5YtLxvH6Ba6lBiRd%2B9LvHFSBcppPLO9jCCk5oz3xFr2oB0TLxVfQBBAZR3p2DRdJNuQclph9FezM%2BoBru0ORpYa0W&X-Amz-Signature=812e56309c3a6247f22b5dcb7df94271a81a4637701a4406f14c0418c4a20d44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

