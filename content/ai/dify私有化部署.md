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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFZSVW33%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDj2A90ZG3oic4%2BoD0leRMpsI4DpbUK1ZuSDOfhj7FHXgIhAL66Hq0MqWtSRQ5jvDkKL%2FGwzc93Ymg8jD5gQLeZlhNkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B0iZB1q3xv13xguUq3AM1d83jx1N%2BYdH2UUz%2Fud45s32QwGILdxaTAgr6jd5g3l0tq0UPvnfNYD8wy6pPdOxcp9OOadjDh1o0S35%2FjssMlINbtkm%2BJ3YUmMlzZDE0FPDmHHB7o0GF0MRzpbphAQEmqfGy%2FfsNfAVkVVlIyXbsltBhDSaquvskYjkZk9TRvxOoU1lu9F8lOdNIA752rlrrTieBcyoS4mNfDtire%2Fbwo%2Bz7qcd7phvMQXt0TLofqa34s13Xuqn04JsAm%2BXuKiLBBBcb58V2BQ4oa6jiP9k%2Fz0VySU%2B1RGoa69kROvaeMQrN487S%2FYxy7lCLzsYTTh2%2FbDOg08KmG87TcNT16MKgGM%2FoyfbihxU8V2zkXrz7MP5bi%2F9WwiSjk%2FW1bXfkrlAe0xtS28aGR8lfyIif4EPzeuBuHiTHEaLBKOo1lkQ%2FHdWuPj%2FyG6YF0%2FOPiTvjFN42ixaPOPvIETk6WwVpMPnt%2FonDmA2vIJEvKiNABQfgE7OznBf5ZBT32RRUAtCVxdaJobgg41HmxDZXp%2Bruh1I4S%2FOC5Jg3mewEbMiK5MnXh0WOKwyzZNG%2FX%2FJgy9PRRLj9iax20edTQDMwtfXf1%2FnhnCh86%2B3CBDvaYAgM8bf8s9pXuqGdbpKa1swqTDC5t7%2FIBjqkAYW%2FViqhv1KNSawCjq5ViHr7jjvD%2Bnl0BXTqpOQIKx46S%2BD10AdS%2B5pQEkDzvWohr0ayGe%2BSGKlk%2BAqAxjfMZlRJX6OU4QmxreR9xDcAjwRpaSFL8Icu5DWAc%2Fs8%2Fdno5JMiah%2BCpgBLb%2FsDWVLvN2yOuGpL63a1sWql8AfkubrPxwslqrsU6ydCcJlxTv9t5U8YyrcxfT0kIdOMiVGO%2BlCI6M1p&X-Amz-Signature=5d98fc828b7bec39a578755e0934d0dfd022b5b1bf05afc976486a999e9994d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFZSVW33%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDj2A90ZG3oic4%2BoD0leRMpsI4DpbUK1ZuSDOfhj7FHXgIhAL66Hq0MqWtSRQ5jvDkKL%2FGwzc93Ymg8jD5gQLeZlhNkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B0iZB1q3xv13xguUq3AM1d83jx1N%2BYdH2UUz%2Fud45s32QwGILdxaTAgr6jd5g3l0tq0UPvnfNYD8wy6pPdOxcp9OOadjDh1o0S35%2FjssMlINbtkm%2BJ3YUmMlzZDE0FPDmHHB7o0GF0MRzpbphAQEmqfGy%2FfsNfAVkVVlIyXbsltBhDSaquvskYjkZk9TRvxOoU1lu9F8lOdNIA752rlrrTieBcyoS4mNfDtire%2Fbwo%2Bz7qcd7phvMQXt0TLofqa34s13Xuqn04JsAm%2BXuKiLBBBcb58V2BQ4oa6jiP9k%2Fz0VySU%2B1RGoa69kROvaeMQrN487S%2FYxy7lCLzsYTTh2%2FbDOg08KmG87TcNT16MKgGM%2FoyfbihxU8V2zkXrz7MP5bi%2F9WwiSjk%2FW1bXfkrlAe0xtS28aGR8lfyIif4EPzeuBuHiTHEaLBKOo1lkQ%2FHdWuPj%2FyG6YF0%2FOPiTvjFN42ixaPOPvIETk6WwVpMPnt%2FonDmA2vIJEvKiNABQfgE7OznBf5ZBT32RRUAtCVxdaJobgg41HmxDZXp%2Bruh1I4S%2FOC5Jg3mewEbMiK5MnXh0WOKwyzZNG%2FX%2FJgy9PRRLj9iax20edTQDMwtfXf1%2FnhnCh86%2B3CBDvaYAgM8bf8s9pXuqGdbpKa1swqTDC5t7%2FIBjqkAYW%2FViqhv1KNSawCjq5ViHr7jjvD%2Bnl0BXTqpOQIKx46S%2BD10AdS%2B5pQEkDzvWohr0ayGe%2BSGKlk%2BAqAxjfMZlRJX6OU4QmxreR9xDcAjwRpaSFL8Icu5DWAc%2Fs8%2Fdno5JMiah%2BCpgBLb%2FsDWVLvN2yOuGpL63a1sWql8AfkubrPxwslqrsU6ydCcJlxTv9t5U8YyrcxfT0kIdOMiVGO%2BlCI6M1p&X-Amz-Signature=3bc3a07a2d2bc76a24f6384e1bd116dc0534a2a64d29747d81bf84903deb34af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFZSVW33%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDj2A90ZG3oic4%2BoD0leRMpsI4DpbUK1ZuSDOfhj7FHXgIhAL66Hq0MqWtSRQ5jvDkKL%2FGwzc93Ymg8jD5gQLeZlhNkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B0iZB1q3xv13xguUq3AM1d83jx1N%2BYdH2UUz%2Fud45s32QwGILdxaTAgr6jd5g3l0tq0UPvnfNYD8wy6pPdOxcp9OOadjDh1o0S35%2FjssMlINbtkm%2BJ3YUmMlzZDE0FPDmHHB7o0GF0MRzpbphAQEmqfGy%2FfsNfAVkVVlIyXbsltBhDSaquvskYjkZk9TRvxOoU1lu9F8lOdNIA752rlrrTieBcyoS4mNfDtire%2Fbwo%2Bz7qcd7phvMQXt0TLofqa34s13Xuqn04JsAm%2BXuKiLBBBcb58V2BQ4oa6jiP9k%2Fz0VySU%2B1RGoa69kROvaeMQrN487S%2FYxy7lCLzsYTTh2%2FbDOg08KmG87TcNT16MKgGM%2FoyfbihxU8V2zkXrz7MP5bi%2F9WwiSjk%2FW1bXfkrlAe0xtS28aGR8lfyIif4EPzeuBuHiTHEaLBKOo1lkQ%2FHdWuPj%2FyG6YF0%2FOPiTvjFN42ixaPOPvIETk6WwVpMPnt%2FonDmA2vIJEvKiNABQfgE7OznBf5ZBT32RRUAtCVxdaJobgg41HmxDZXp%2Bruh1I4S%2FOC5Jg3mewEbMiK5MnXh0WOKwyzZNG%2FX%2FJgy9PRRLj9iax20edTQDMwtfXf1%2FnhnCh86%2B3CBDvaYAgM8bf8s9pXuqGdbpKa1swqTDC5t7%2FIBjqkAYW%2FViqhv1KNSawCjq5ViHr7jjvD%2Bnl0BXTqpOQIKx46S%2BD10AdS%2B5pQEkDzvWohr0ayGe%2BSGKlk%2BAqAxjfMZlRJX6OU4QmxreR9xDcAjwRpaSFL8Icu5DWAc%2Fs8%2Fdno5JMiah%2BCpgBLb%2FsDWVLvN2yOuGpL63a1sWql8AfkubrPxwslqrsU6ydCcJlxTv9t5U8YyrcxfT0kIdOMiVGO%2BlCI6M1p&X-Amz-Signature=178f81152675623b9ba0cbf71baf710271e1278f9eae76a9ad999a3827f0e3db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFZSVW33%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDj2A90ZG3oic4%2BoD0leRMpsI4DpbUK1ZuSDOfhj7FHXgIhAL66Hq0MqWtSRQ5jvDkKL%2FGwzc93Ymg8jD5gQLeZlhNkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B0iZB1q3xv13xguUq3AM1d83jx1N%2BYdH2UUz%2Fud45s32QwGILdxaTAgr6jd5g3l0tq0UPvnfNYD8wy6pPdOxcp9OOadjDh1o0S35%2FjssMlINbtkm%2BJ3YUmMlzZDE0FPDmHHB7o0GF0MRzpbphAQEmqfGy%2FfsNfAVkVVlIyXbsltBhDSaquvskYjkZk9TRvxOoU1lu9F8lOdNIA752rlrrTieBcyoS4mNfDtire%2Fbwo%2Bz7qcd7phvMQXt0TLofqa34s13Xuqn04JsAm%2BXuKiLBBBcb58V2BQ4oa6jiP9k%2Fz0VySU%2B1RGoa69kROvaeMQrN487S%2FYxy7lCLzsYTTh2%2FbDOg08KmG87TcNT16MKgGM%2FoyfbihxU8V2zkXrz7MP5bi%2F9WwiSjk%2FW1bXfkrlAe0xtS28aGR8lfyIif4EPzeuBuHiTHEaLBKOo1lkQ%2FHdWuPj%2FyG6YF0%2FOPiTvjFN42ixaPOPvIETk6WwVpMPnt%2FonDmA2vIJEvKiNABQfgE7OznBf5ZBT32RRUAtCVxdaJobgg41HmxDZXp%2Bruh1I4S%2FOC5Jg3mewEbMiK5MnXh0WOKwyzZNG%2FX%2FJgy9PRRLj9iax20edTQDMwtfXf1%2FnhnCh86%2B3CBDvaYAgM8bf8s9pXuqGdbpKa1swqTDC5t7%2FIBjqkAYW%2FViqhv1KNSawCjq5ViHr7jjvD%2Bnl0BXTqpOQIKx46S%2BD10AdS%2B5pQEkDzvWohr0ayGe%2BSGKlk%2BAqAxjfMZlRJX6OU4QmxreR9xDcAjwRpaSFL8Icu5DWAc%2Fs8%2Fdno5JMiah%2BCpgBLb%2FsDWVLvN2yOuGpL63a1sWql8AfkubrPxwslqrsU6ydCcJlxTv9t5U8YyrcxfT0kIdOMiVGO%2BlCI6M1p&X-Amz-Signature=1469c35d33d68d259f6ea77753d891835d5f4a8c5dd8ed5ff5b4b05f88708f3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFZSVW33%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDj2A90ZG3oic4%2BoD0leRMpsI4DpbUK1ZuSDOfhj7FHXgIhAL66Hq0MqWtSRQ5jvDkKL%2FGwzc93Ymg8jD5gQLeZlhNkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B0iZB1q3xv13xguUq3AM1d83jx1N%2BYdH2UUz%2Fud45s32QwGILdxaTAgr6jd5g3l0tq0UPvnfNYD8wy6pPdOxcp9OOadjDh1o0S35%2FjssMlINbtkm%2BJ3YUmMlzZDE0FPDmHHB7o0GF0MRzpbphAQEmqfGy%2FfsNfAVkVVlIyXbsltBhDSaquvskYjkZk9TRvxOoU1lu9F8lOdNIA752rlrrTieBcyoS4mNfDtire%2Fbwo%2Bz7qcd7phvMQXt0TLofqa34s13Xuqn04JsAm%2BXuKiLBBBcb58V2BQ4oa6jiP9k%2Fz0VySU%2B1RGoa69kROvaeMQrN487S%2FYxy7lCLzsYTTh2%2FbDOg08KmG87TcNT16MKgGM%2FoyfbihxU8V2zkXrz7MP5bi%2F9WwiSjk%2FW1bXfkrlAe0xtS28aGR8lfyIif4EPzeuBuHiTHEaLBKOo1lkQ%2FHdWuPj%2FyG6YF0%2FOPiTvjFN42ixaPOPvIETk6WwVpMPnt%2FonDmA2vIJEvKiNABQfgE7OznBf5ZBT32RRUAtCVxdaJobgg41HmxDZXp%2Bruh1I4S%2FOC5Jg3mewEbMiK5MnXh0WOKwyzZNG%2FX%2FJgy9PRRLj9iax20edTQDMwtfXf1%2FnhnCh86%2B3CBDvaYAgM8bf8s9pXuqGdbpKa1swqTDC5t7%2FIBjqkAYW%2FViqhv1KNSawCjq5ViHr7jjvD%2Bnl0BXTqpOQIKx46S%2BD10AdS%2B5pQEkDzvWohr0ayGe%2BSGKlk%2BAqAxjfMZlRJX6OU4QmxreR9xDcAjwRpaSFL8Icu5DWAc%2Fs8%2Fdno5JMiah%2BCpgBLb%2FsDWVLvN2yOuGpL63a1sWql8AfkubrPxwslqrsU6ydCcJlxTv9t5U8YyrcxfT0kIdOMiVGO%2BlCI6M1p&X-Amz-Signature=34dba02a0004b3ef25de4a952517b836099157a575bfa4e55b5d520c15cbe622&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFZSVW33%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDj2A90ZG3oic4%2BoD0leRMpsI4DpbUK1ZuSDOfhj7FHXgIhAL66Hq0MqWtSRQ5jvDkKL%2FGwzc93Ymg8jD5gQLeZlhNkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B0iZB1q3xv13xguUq3AM1d83jx1N%2BYdH2UUz%2Fud45s32QwGILdxaTAgr6jd5g3l0tq0UPvnfNYD8wy6pPdOxcp9OOadjDh1o0S35%2FjssMlINbtkm%2BJ3YUmMlzZDE0FPDmHHB7o0GF0MRzpbphAQEmqfGy%2FfsNfAVkVVlIyXbsltBhDSaquvskYjkZk9TRvxOoU1lu9F8lOdNIA752rlrrTieBcyoS4mNfDtire%2Fbwo%2Bz7qcd7phvMQXt0TLofqa34s13Xuqn04JsAm%2BXuKiLBBBcb58V2BQ4oa6jiP9k%2Fz0VySU%2B1RGoa69kROvaeMQrN487S%2FYxy7lCLzsYTTh2%2FbDOg08KmG87TcNT16MKgGM%2FoyfbihxU8V2zkXrz7MP5bi%2F9WwiSjk%2FW1bXfkrlAe0xtS28aGR8lfyIif4EPzeuBuHiTHEaLBKOo1lkQ%2FHdWuPj%2FyG6YF0%2FOPiTvjFN42ixaPOPvIETk6WwVpMPnt%2FonDmA2vIJEvKiNABQfgE7OznBf5ZBT32RRUAtCVxdaJobgg41HmxDZXp%2Bruh1I4S%2FOC5Jg3mewEbMiK5MnXh0WOKwyzZNG%2FX%2FJgy9PRRLj9iax20edTQDMwtfXf1%2FnhnCh86%2B3CBDvaYAgM8bf8s9pXuqGdbpKa1swqTDC5t7%2FIBjqkAYW%2FViqhv1KNSawCjq5ViHr7jjvD%2Bnl0BXTqpOQIKx46S%2BD10AdS%2B5pQEkDzvWohr0ayGe%2BSGKlk%2BAqAxjfMZlRJX6OU4QmxreR9xDcAjwRpaSFL8Icu5DWAc%2Fs8%2Fdno5JMiah%2BCpgBLb%2FsDWVLvN2yOuGpL63a1sWql8AfkubrPxwslqrsU6ydCcJlxTv9t5U8YyrcxfT0kIdOMiVGO%2BlCI6M1p&X-Amz-Signature=44f97d9febaf10827f00f863fae2cf67d41682aeef62858f647ec795b6138230&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFZSVW33%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDj2A90ZG3oic4%2BoD0leRMpsI4DpbUK1ZuSDOfhj7FHXgIhAL66Hq0MqWtSRQ5jvDkKL%2FGwzc93Ymg8jD5gQLeZlhNkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B0iZB1q3xv13xguUq3AM1d83jx1N%2BYdH2UUz%2Fud45s32QwGILdxaTAgr6jd5g3l0tq0UPvnfNYD8wy6pPdOxcp9OOadjDh1o0S35%2FjssMlINbtkm%2BJ3YUmMlzZDE0FPDmHHB7o0GF0MRzpbphAQEmqfGy%2FfsNfAVkVVlIyXbsltBhDSaquvskYjkZk9TRvxOoU1lu9F8lOdNIA752rlrrTieBcyoS4mNfDtire%2Fbwo%2Bz7qcd7phvMQXt0TLofqa34s13Xuqn04JsAm%2BXuKiLBBBcb58V2BQ4oa6jiP9k%2Fz0VySU%2B1RGoa69kROvaeMQrN487S%2FYxy7lCLzsYTTh2%2FbDOg08KmG87TcNT16MKgGM%2FoyfbihxU8V2zkXrz7MP5bi%2F9WwiSjk%2FW1bXfkrlAe0xtS28aGR8lfyIif4EPzeuBuHiTHEaLBKOo1lkQ%2FHdWuPj%2FyG6YF0%2FOPiTvjFN42ixaPOPvIETk6WwVpMPnt%2FonDmA2vIJEvKiNABQfgE7OznBf5ZBT32RRUAtCVxdaJobgg41HmxDZXp%2Bruh1I4S%2FOC5Jg3mewEbMiK5MnXh0WOKwyzZNG%2FX%2FJgy9PRRLj9iax20edTQDMwtfXf1%2FnhnCh86%2B3CBDvaYAgM8bf8s9pXuqGdbpKa1swqTDC5t7%2FIBjqkAYW%2FViqhv1KNSawCjq5ViHr7jjvD%2Bnl0BXTqpOQIKx46S%2BD10AdS%2B5pQEkDzvWohr0ayGe%2BSGKlk%2BAqAxjfMZlRJX6OU4QmxreR9xDcAjwRpaSFL8Icu5DWAc%2Fs8%2Fdno5JMiah%2BCpgBLb%2FsDWVLvN2yOuGpL63a1sWql8AfkubrPxwslqrsU6ydCcJlxTv9t5U8YyrcxfT0kIdOMiVGO%2BlCI6M1p&X-Amz-Signature=2da0b914ac86d4daf1c06c6804683a615e9b110ccf44b3fd827c3bbccf40ec45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFZSVW33%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDj2A90ZG3oic4%2BoD0leRMpsI4DpbUK1ZuSDOfhj7FHXgIhAL66Hq0MqWtSRQ5jvDkKL%2FGwzc93Ymg8jD5gQLeZlhNkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B0iZB1q3xv13xguUq3AM1d83jx1N%2BYdH2UUz%2Fud45s32QwGILdxaTAgr6jd5g3l0tq0UPvnfNYD8wy6pPdOxcp9OOadjDh1o0S35%2FjssMlINbtkm%2BJ3YUmMlzZDE0FPDmHHB7o0GF0MRzpbphAQEmqfGy%2FfsNfAVkVVlIyXbsltBhDSaquvskYjkZk9TRvxOoU1lu9F8lOdNIA752rlrrTieBcyoS4mNfDtire%2Fbwo%2Bz7qcd7phvMQXt0TLofqa34s13Xuqn04JsAm%2BXuKiLBBBcb58V2BQ4oa6jiP9k%2Fz0VySU%2B1RGoa69kROvaeMQrN487S%2FYxy7lCLzsYTTh2%2FbDOg08KmG87TcNT16MKgGM%2FoyfbihxU8V2zkXrz7MP5bi%2F9WwiSjk%2FW1bXfkrlAe0xtS28aGR8lfyIif4EPzeuBuHiTHEaLBKOo1lkQ%2FHdWuPj%2FyG6YF0%2FOPiTvjFN42ixaPOPvIETk6WwVpMPnt%2FonDmA2vIJEvKiNABQfgE7OznBf5ZBT32RRUAtCVxdaJobgg41HmxDZXp%2Bruh1I4S%2FOC5Jg3mewEbMiK5MnXh0WOKwyzZNG%2FX%2FJgy9PRRLj9iax20edTQDMwtfXf1%2FnhnCh86%2B3CBDvaYAgM8bf8s9pXuqGdbpKa1swqTDC5t7%2FIBjqkAYW%2FViqhv1KNSawCjq5ViHr7jjvD%2Bnl0BXTqpOQIKx46S%2BD10AdS%2B5pQEkDzvWohr0ayGe%2BSGKlk%2BAqAxjfMZlRJX6OU4QmxreR9xDcAjwRpaSFL8Icu5DWAc%2Fs8%2Fdno5JMiah%2BCpgBLb%2FsDWVLvN2yOuGpL63a1sWql8AfkubrPxwslqrsU6ydCcJlxTv9t5U8YyrcxfT0kIdOMiVGO%2BlCI6M1p&X-Amz-Signature=608d28989ea60292ece0a168d3a33f537ee2858a682bfe71f879e7097999acdd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFZSVW33%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDj2A90ZG3oic4%2BoD0leRMpsI4DpbUK1ZuSDOfhj7FHXgIhAL66Hq0MqWtSRQ5jvDkKL%2FGwzc93Ymg8jD5gQLeZlhNkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B0iZB1q3xv13xguUq3AM1d83jx1N%2BYdH2UUz%2Fud45s32QwGILdxaTAgr6jd5g3l0tq0UPvnfNYD8wy6pPdOxcp9OOadjDh1o0S35%2FjssMlINbtkm%2BJ3YUmMlzZDE0FPDmHHB7o0GF0MRzpbphAQEmqfGy%2FfsNfAVkVVlIyXbsltBhDSaquvskYjkZk9TRvxOoU1lu9F8lOdNIA752rlrrTieBcyoS4mNfDtire%2Fbwo%2Bz7qcd7phvMQXt0TLofqa34s13Xuqn04JsAm%2BXuKiLBBBcb58V2BQ4oa6jiP9k%2Fz0VySU%2B1RGoa69kROvaeMQrN487S%2FYxy7lCLzsYTTh2%2FbDOg08KmG87TcNT16MKgGM%2FoyfbihxU8V2zkXrz7MP5bi%2F9WwiSjk%2FW1bXfkrlAe0xtS28aGR8lfyIif4EPzeuBuHiTHEaLBKOo1lkQ%2FHdWuPj%2FyG6YF0%2FOPiTvjFN42ixaPOPvIETk6WwVpMPnt%2FonDmA2vIJEvKiNABQfgE7OznBf5ZBT32RRUAtCVxdaJobgg41HmxDZXp%2Bruh1I4S%2FOC5Jg3mewEbMiK5MnXh0WOKwyzZNG%2FX%2FJgy9PRRLj9iax20edTQDMwtfXf1%2FnhnCh86%2B3CBDvaYAgM8bf8s9pXuqGdbpKa1swqTDC5t7%2FIBjqkAYW%2FViqhv1KNSawCjq5ViHr7jjvD%2Bnl0BXTqpOQIKx46S%2BD10AdS%2B5pQEkDzvWohr0ayGe%2BSGKlk%2BAqAxjfMZlRJX6OU4QmxreR9xDcAjwRpaSFL8Icu5DWAc%2Fs8%2Fdno5JMiah%2BCpgBLb%2FsDWVLvN2yOuGpL63a1sWql8AfkubrPxwslqrsU6ydCcJlxTv9t5U8YyrcxfT0kIdOMiVGO%2BlCI6M1p&X-Amz-Signature=b9861aec8abff8624bd544f6eca06f774ee6019f2bd30449f7be33a132557665&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFZSVW33%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDj2A90ZG3oic4%2BoD0leRMpsI4DpbUK1ZuSDOfhj7FHXgIhAL66Hq0MqWtSRQ5jvDkKL%2FGwzc93Ymg8jD5gQLeZlhNkKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2B0iZB1q3xv13xguUq3AM1d83jx1N%2BYdH2UUz%2Fud45s32QwGILdxaTAgr6jd5g3l0tq0UPvnfNYD8wy6pPdOxcp9OOadjDh1o0S35%2FjssMlINbtkm%2BJ3YUmMlzZDE0FPDmHHB7o0GF0MRzpbphAQEmqfGy%2FfsNfAVkVVlIyXbsltBhDSaquvskYjkZk9TRvxOoU1lu9F8lOdNIA752rlrrTieBcyoS4mNfDtire%2Fbwo%2Bz7qcd7phvMQXt0TLofqa34s13Xuqn04JsAm%2BXuKiLBBBcb58V2BQ4oa6jiP9k%2Fz0VySU%2B1RGoa69kROvaeMQrN487S%2FYxy7lCLzsYTTh2%2FbDOg08KmG87TcNT16MKgGM%2FoyfbihxU8V2zkXrz7MP5bi%2F9WwiSjk%2FW1bXfkrlAe0xtS28aGR8lfyIif4EPzeuBuHiTHEaLBKOo1lkQ%2FHdWuPj%2FyG6YF0%2FOPiTvjFN42ixaPOPvIETk6WwVpMPnt%2FonDmA2vIJEvKiNABQfgE7OznBf5ZBT32RRUAtCVxdaJobgg41HmxDZXp%2Bruh1I4S%2FOC5Jg3mewEbMiK5MnXh0WOKwyzZNG%2FX%2FJgy9PRRLj9iax20edTQDMwtfXf1%2FnhnCh86%2B3CBDvaYAgM8bf8s9pXuqGdbpKa1swqTDC5t7%2FIBjqkAYW%2FViqhv1KNSawCjq5ViHr7jjvD%2Bnl0BXTqpOQIKx46S%2BD10AdS%2B5pQEkDzvWohr0ayGe%2BSGKlk%2BAqAxjfMZlRJX6OU4QmxreR9xDcAjwRpaSFL8Icu5DWAc%2Fs8%2Fdno5JMiah%2BCpgBLb%2FsDWVLvN2yOuGpL63a1sWql8AfkubrPxwslqrsU6ydCcJlxTv9t5U8YyrcxfT0kIdOMiVGO%2BlCI6M1p&X-Amz-Signature=e3d0a656c4bf5ab7fed51754e6c61acd2e6bad686b0b20b2f75dcdabb3d83326&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

