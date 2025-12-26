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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TGMTNPY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDJ81%2FtFJYWcKhmrY4pLvDL2bplxmi13ZX7kfL%2FIQXPwIgPJLLOQ2vJGFz9YqcvuToNNCyXPii1AtNUD7wHUKSjiAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDGEUNn6Z2l1dCYTw7yrcA4Z3VmtiYG0TGofMmAwJ5Oq%2FSjn39b7g6cyvADP%2FWDKUSWZhkeFKospxM6B56HjP0%2FxcyA4jTEGj5dilvz%2FkB5KJrcab59I0e55n8QFg4GS5%2BvDYKZfNajhMFQ1ckny4G8ohqiszVHTnoYquDmDhpNdFJ3e38xN4goVdI6FQ%2FfZHoWzXE6%2FE0saCdc6E6%2FbR4AGInpSXq0LVvSsZ8czqGBysqtdX8tr0fdilHZC1dj3pgW%2BRt089%2BEBm%2B74RRYqcqewMYS120pp%2FXbbYllkLymhzL7pnhcLnfOoZw9N7om%2F552Ofgdjwdnm3E56RaLFS7ZieQQV7Yo3qEwQ3oPPZcWuf0fWYfqcyqAbkv%2Bjqqg1AhnxS%2FEDDDlT7IaNAKe9omBGlbEjInz%2FGayN1I9aFjbCB33t5yhbeVuLpe9Ys2KrBTB9s2Bvj4pvflVFwLq9YN70V5ApAuOdQmb73VE3fW3a3GfoDotdpfWI%2B0VjT0aF3JD2zxqgb4ETxxjun4O0ybTTIxFJCAjdg%2F60ytqPyVWv83hL%2B%2BlhK%2Ft%2FRmSl6XKlM0KTiC%2BEbNSvN0%2FWL3doN4q8QcxJaWas83gTIKKlC8J8qRpcahmbt2effPE%2FMl9MPnd9YGsKKrsOsO39wMJHNt8oGOqUBASdkkD%2B0i1OccjTLUjPvWA%2FFOMH%2F%2F8exKw6u2leZ4gxtbJwD%2F4RkOEoROnXZitQzYWzIHmAiVB0ocOHU0OApUTUvHk4Dohh9%2BEEEMZHiVI2%2BvDl%2FTXwciOOWhzIw4JuhtA9EyRF4g6die5njIOBHvMku5UHJ2txq9HBn2odFdBb%2FynoKBC8XkP2KoCPwea3IPwSFr7C0VRxfwSMRqkCgyf1U1BXr&X-Amz-Signature=c63e9b8e8c4db8d932062fa6b874fefab3fd9d33b20a686811636aa57d298e19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TGMTNPY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDJ81%2FtFJYWcKhmrY4pLvDL2bplxmi13ZX7kfL%2FIQXPwIgPJLLOQ2vJGFz9YqcvuToNNCyXPii1AtNUD7wHUKSjiAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDGEUNn6Z2l1dCYTw7yrcA4Z3VmtiYG0TGofMmAwJ5Oq%2FSjn39b7g6cyvADP%2FWDKUSWZhkeFKospxM6B56HjP0%2FxcyA4jTEGj5dilvz%2FkB5KJrcab59I0e55n8QFg4GS5%2BvDYKZfNajhMFQ1ckny4G8ohqiszVHTnoYquDmDhpNdFJ3e38xN4goVdI6FQ%2FfZHoWzXE6%2FE0saCdc6E6%2FbR4AGInpSXq0LVvSsZ8czqGBysqtdX8tr0fdilHZC1dj3pgW%2BRt089%2BEBm%2B74RRYqcqewMYS120pp%2FXbbYllkLymhzL7pnhcLnfOoZw9N7om%2F552Ofgdjwdnm3E56RaLFS7ZieQQV7Yo3qEwQ3oPPZcWuf0fWYfqcyqAbkv%2Bjqqg1AhnxS%2FEDDDlT7IaNAKe9omBGlbEjInz%2FGayN1I9aFjbCB33t5yhbeVuLpe9Ys2KrBTB9s2Bvj4pvflVFwLq9YN70V5ApAuOdQmb73VE3fW3a3GfoDotdpfWI%2B0VjT0aF3JD2zxqgb4ETxxjun4O0ybTTIxFJCAjdg%2F60ytqPyVWv83hL%2B%2BlhK%2Ft%2FRmSl6XKlM0KTiC%2BEbNSvN0%2FWL3doN4q8QcxJaWas83gTIKKlC8J8qRpcahmbt2effPE%2FMl9MPnd9YGsKKrsOsO39wMJHNt8oGOqUBASdkkD%2B0i1OccjTLUjPvWA%2FFOMH%2F%2F8exKw6u2leZ4gxtbJwD%2F4RkOEoROnXZitQzYWzIHmAiVB0ocOHU0OApUTUvHk4Dohh9%2BEEEMZHiVI2%2BvDl%2FTXwciOOWhzIw4JuhtA9EyRF4g6die5njIOBHvMku5UHJ2txq9HBn2odFdBb%2FynoKBC8XkP2KoCPwea3IPwSFr7C0VRxfwSMRqkCgyf1U1BXr&X-Amz-Signature=6efdafb49390fa77ff37b64eef5e196c3542363c7397468a382799443cb98df5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TGMTNPY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDJ81%2FtFJYWcKhmrY4pLvDL2bplxmi13ZX7kfL%2FIQXPwIgPJLLOQ2vJGFz9YqcvuToNNCyXPii1AtNUD7wHUKSjiAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDGEUNn6Z2l1dCYTw7yrcA4Z3VmtiYG0TGofMmAwJ5Oq%2FSjn39b7g6cyvADP%2FWDKUSWZhkeFKospxM6B56HjP0%2FxcyA4jTEGj5dilvz%2FkB5KJrcab59I0e55n8QFg4GS5%2BvDYKZfNajhMFQ1ckny4G8ohqiszVHTnoYquDmDhpNdFJ3e38xN4goVdI6FQ%2FfZHoWzXE6%2FE0saCdc6E6%2FbR4AGInpSXq0LVvSsZ8czqGBysqtdX8tr0fdilHZC1dj3pgW%2BRt089%2BEBm%2B74RRYqcqewMYS120pp%2FXbbYllkLymhzL7pnhcLnfOoZw9N7om%2F552Ofgdjwdnm3E56RaLFS7ZieQQV7Yo3qEwQ3oPPZcWuf0fWYfqcyqAbkv%2Bjqqg1AhnxS%2FEDDDlT7IaNAKe9omBGlbEjInz%2FGayN1I9aFjbCB33t5yhbeVuLpe9Ys2KrBTB9s2Bvj4pvflVFwLq9YN70V5ApAuOdQmb73VE3fW3a3GfoDotdpfWI%2B0VjT0aF3JD2zxqgb4ETxxjun4O0ybTTIxFJCAjdg%2F60ytqPyVWv83hL%2B%2BlhK%2Ft%2FRmSl6XKlM0KTiC%2BEbNSvN0%2FWL3doN4q8QcxJaWas83gTIKKlC8J8qRpcahmbt2effPE%2FMl9MPnd9YGsKKrsOsO39wMJHNt8oGOqUBASdkkD%2B0i1OccjTLUjPvWA%2FFOMH%2F%2F8exKw6u2leZ4gxtbJwD%2F4RkOEoROnXZitQzYWzIHmAiVB0ocOHU0OApUTUvHk4Dohh9%2BEEEMZHiVI2%2BvDl%2FTXwciOOWhzIw4JuhtA9EyRF4g6die5njIOBHvMku5UHJ2txq9HBn2odFdBb%2FynoKBC8XkP2KoCPwea3IPwSFr7C0VRxfwSMRqkCgyf1U1BXr&X-Amz-Signature=9321fa1b3184b543180c5411e8af57732d0e23946eb68c3114d6ddc80cb2e7fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TGMTNPY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDJ81%2FtFJYWcKhmrY4pLvDL2bplxmi13ZX7kfL%2FIQXPwIgPJLLOQ2vJGFz9YqcvuToNNCyXPii1AtNUD7wHUKSjiAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDGEUNn6Z2l1dCYTw7yrcA4Z3VmtiYG0TGofMmAwJ5Oq%2FSjn39b7g6cyvADP%2FWDKUSWZhkeFKospxM6B56HjP0%2FxcyA4jTEGj5dilvz%2FkB5KJrcab59I0e55n8QFg4GS5%2BvDYKZfNajhMFQ1ckny4G8ohqiszVHTnoYquDmDhpNdFJ3e38xN4goVdI6FQ%2FfZHoWzXE6%2FE0saCdc6E6%2FbR4AGInpSXq0LVvSsZ8czqGBysqtdX8tr0fdilHZC1dj3pgW%2BRt089%2BEBm%2B74RRYqcqewMYS120pp%2FXbbYllkLymhzL7pnhcLnfOoZw9N7om%2F552Ofgdjwdnm3E56RaLFS7ZieQQV7Yo3qEwQ3oPPZcWuf0fWYfqcyqAbkv%2Bjqqg1AhnxS%2FEDDDlT7IaNAKe9omBGlbEjInz%2FGayN1I9aFjbCB33t5yhbeVuLpe9Ys2KrBTB9s2Bvj4pvflVFwLq9YN70V5ApAuOdQmb73VE3fW3a3GfoDotdpfWI%2B0VjT0aF3JD2zxqgb4ETxxjun4O0ybTTIxFJCAjdg%2F60ytqPyVWv83hL%2B%2BlhK%2Ft%2FRmSl6XKlM0KTiC%2BEbNSvN0%2FWL3doN4q8QcxJaWas83gTIKKlC8J8qRpcahmbt2effPE%2FMl9MPnd9YGsKKrsOsO39wMJHNt8oGOqUBASdkkD%2B0i1OccjTLUjPvWA%2FFOMH%2F%2F8exKw6u2leZ4gxtbJwD%2F4RkOEoROnXZitQzYWzIHmAiVB0ocOHU0OApUTUvHk4Dohh9%2BEEEMZHiVI2%2BvDl%2FTXwciOOWhzIw4JuhtA9EyRF4g6die5njIOBHvMku5UHJ2txq9HBn2odFdBb%2FynoKBC8XkP2KoCPwea3IPwSFr7C0VRxfwSMRqkCgyf1U1BXr&X-Amz-Signature=a7e1c3ae761a1acffde4ca252664e07777572851a97f4468804aaf9ee6bad413&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TGMTNPY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDJ81%2FtFJYWcKhmrY4pLvDL2bplxmi13ZX7kfL%2FIQXPwIgPJLLOQ2vJGFz9YqcvuToNNCyXPii1AtNUD7wHUKSjiAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDGEUNn6Z2l1dCYTw7yrcA4Z3VmtiYG0TGofMmAwJ5Oq%2FSjn39b7g6cyvADP%2FWDKUSWZhkeFKospxM6B56HjP0%2FxcyA4jTEGj5dilvz%2FkB5KJrcab59I0e55n8QFg4GS5%2BvDYKZfNajhMFQ1ckny4G8ohqiszVHTnoYquDmDhpNdFJ3e38xN4goVdI6FQ%2FfZHoWzXE6%2FE0saCdc6E6%2FbR4AGInpSXq0LVvSsZ8czqGBysqtdX8tr0fdilHZC1dj3pgW%2BRt089%2BEBm%2B74RRYqcqewMYS120pp%2FXbbYllkLymhzL7pnhcLnfOoZw9N7om%2F552Ofgdjwdnm3E56RaLFS7ZieQQV7Yo3qEwQ3oPPZcWuf0fWYfqcyqAbkv%2Bjqqg1AhnxS%2FEDDDlT7IaNAKe9omBGlbEjInz%2FGayN1I9aFjbCB33t5yhbeVuLpe9Ys2KrBTB9s2Bvj4pvflVFwLq9YN70V5ApAuOdQmb73VE3fW3a3GfoDotdpfWI%2B0VjT0aF3JD2zxqgb4ETxxjun4O0ybTTIxFJCAjdg%2F60ytqPyVWv83hL%2B%2BlhK%2Ft%2FRmSl6XKlM0KTiC%2BEbNSvN0%2FWL3doN4q8QcxJaWas83gTIKKlC8J8qRpcahmbt2effPE%2FMl9MPnd9YGsKKrsOsO39wMJHNt8oGOqUBASdkkD%2B0i1OccjTLUjPvWA%2FFOMH%2F%2F8exKw6u2leZ4gxtbJwD%2F4RkOEoROnXZitQzYWzIHmAiVB0ocOHU0OApUTUvHk4Dohh9%2BEEEMZHiVI2%2BvDl%2FTXwciOOWhzIw4JuhtA9EyRF4g6die5njIOBHvMku5UHJ2txq9HBn2odFdBb%2FynoKBC8XkP2KoCPwea3IPwSFr7C0VRxfwSMRqkCgyf1U1BXr&X-Amz-Signature=565d62305945fd4e48cc82ec372e38155d5f89005e09293d3215c7c3ea7ead14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TGMTNPY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDJ81%2FtFJYWcKhmrY4pLvDL2bplxmi13ZX7kfL%2FIQXPwIgPJLLOQ2vJGFz9YqcvuToNNCyXPii1AtNUD7wHUKSjiAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDGEUNn6Z2l1dCYTw7yrcA4Z3VmtiYG0TGofMmAwJ5Oq%2FSjn39b7g6cyvADP%2FWDKUSWZhkeFKospxM6B56HjP0%2FxcyA4jTEGj5dilvz%2FkB5KJrcab59I0e55n8QFg4GS5%2BvDYKZfNajhMFQ1ckny4G8ohqiszVHTnoYquDmDhpNdFJ3e38xN4goVdI6FQ%2FfZHoWzXE6%2FE0saCdc6E6%2FbR4AGInpSXq0LVvSsZ8czqGBysqtdX8tr0fdilHZC1dj3pgW%2BRt089%2BEBm%2B74RRYqcqewMYS120pp%2FXbbYllkLymhzL7pnhcLnfOoZw9N7om%2F552Ofgdjwdnm3E56RaLFS7ZieQQV7Yo3qEwQ3oPPZcWuf0fWYfqcyqAbkv%2Bjqqg1AhnxS%2FEDDDlT7IaNAKe9omBGlbEjInz%2FGayN1I9aFjbCB33t5yhbeVuLpe9Ys2KrBTB9s2Bvj4pvflVFwLq9YN70V5ApAuOdQmb73VE3fW3a3GfoDotdpfWI%2B0VjT0aF3JD2zxqgb4ETxxjun4O0ybTTIxFJCAjdg%2F60ytqPyVWv83hL%2B%2BlhK%2Ft%2FRmSl6XKlM0KTiC%2BEbNSvN0%2FWL3doN4q8QcxJaWas83gTIKKlC8J8qRpcahmbt2effPE%2FMl9MPnd9YGsKKrsOsO39wMJHNt8oGOqUBASdkkD%2B0i1OccjTLUjPvWA%2FFOMH%2F%2F8exKw6u2leZ4gxtbJwD%2F4RkOEoROnXZitQzYWzIHmAiVB0ocOHU0OApUTUvHk4Dohh9%2BEEEMZHiVI2%2BvDl%2FTXwciOOWhzIw4JuhtA9EyRF4g6die5njIOBHvMku5UHJ2txq9HBn2odFdBb%2FynoKBC8XkP2KoCPwea3IPwSFr7C0VRxfwSMRqkCgyf1U1BXr&X-Amz-Signature=0ea351c2f2eefd5ecebda78fe8499faa4987d43aa45ec7a14ee780c3b9420a55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TGMTNPY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDJ81%2FtFJYWcKhmrY4pLvDL2bplxmi13ZX7kfL%2FIQXPwIgPJLLOQ2vJGFz9YqcvuToNNCyXPii1AtNUD7wHUKSjiAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDGEUNn6Z2l1dCYTw7yrcA4Z3VmtiYG0TGofMmAwJ5Oq%2FSjn39b7g6cyvADP%2FWDKUSWZhkeFKospxM6B56HjP0%2FxcyA4jTEGj5dilvz%2FkB5KJrcab59I0e55n8QFg4GS5%2BvDYKZfNajhMFQ1ckny4G8ohqiszVHTnoYquDmDhpNdFJ3e38xN4goVdI6FQ%2FfZHoWzXE6%2FE0saCdc6E6%2FbR4AGInpSXq0LVvSsZ8czqGBysqtdX8tr0fdilHZC1dj3pgW%2BRt089%2BEBm%2B74RRYqcqewMYS120pp%2FXbbYllkLymhzL7pnhcLnfOoZw9N7om%2F552Ofgdjwdnm3E56RaLFS7ZieQQV7Yo3qEwQ3oPPZcWuf0fWYfqcyqAbkv%2Bjqqg1AhnxS%2FEDDDlT7IaNAKe9omBGlbEjInz%2FGayN1I9aFjbCB33t5yhbeVuLpe9Ys2KrBTB9s2Bvj4pvflVFwLq9YN70V5ApAuOdQmb73VE3fW3a3GfoDotdpfWI%2B0VjT0aF3JD2zxqgb4ETxxjun4O0ybTTIxFJCAjdg%2F60ytqPyVWv83hL%2B%2BlhK%2Ft%2FRmSl6XKlM0KTiC%2BEbNSvN0%2FWL3doN4q8QcxJaWas83gTIKKlC8J8qRpcahmbt2effPE%2FMl9MPnd9YGsKKrsOsO39wMJHNt8oGOqUBASdkkD%2B0i1OccjTLUjPvWA%2FFOMH%2F%2F8exKw6u2leZ4gxtbJwD%2F4RkOEoROnXZitQzYWzIHmAiVB0ocOHU0OApUTUvHk4Dohh9%2BEEEMZHiVI2%2BvDl%2FTXwciOOWhzIw4JuhtA9EyRF4g6die5njIOBHvMku5UHJ2txq9HBn2odFdBb%2FynoKBC8XkP2KoCPwea3IPwSFr7C0VRxfwSMRqkCgyf1U1BXr&X-Amz-Signature=f470ec641558f4c4adff684faf001ef7d7e7026ecd539369137dfc576a5ba051&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TGMTNPY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDJ81%2FtFJYWcKhmrY4pLvDL2bplxmi13ZX7kfL%2FIQXPwIgPJLLOQ2vJGFz9YqcvuToNNCyXPii1AtNUD7wHUKSjiAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDGEUNn6Z2l1dCYTw7yrcA4Z3VmtiYG0TGofMmAwJ5Oq%2FSjn39b7g6cyvADP%2FWDKUSWZhkeFKospxM6B56HjP0%2FxcyA4jTEGj5dilvz%2FkB5KJrcab59I0e55n8QFg4GS5%2BvDYKZfNajhMFQ1ckny4G8ohqiszVHTnoYquDmDhpNdFJ3e38xN4goVdI6FQ%2FfZHoWzXE6%2FE0saCdc6E6%2FbR4AGInpSXq0LVvSsZ8czqGBysqtdX8tr0fdilHZC1dj3pgW%2BRt089%2BEBm%2B74RRYqcqewMYS120pp%2FXbbYllkLymhzL7pnhcLnfOoZw9N7om%2F552Ofgdjwdnm3E56RaLFS7ZieQQV7Yo3qEwQ3oPPZcWuf0fWYfqcyqAbkv%2Bjqqg1AhnxS%2FEDDDlT7IaNAKe9omBGlbEjInz%2FGayN1I9aFjbCB33t5yhbeVuLpe9Ys2KrBTB9s2Bvj4pvflVFwLq9YN70V5ApAuOdQmb73VE3fW3a3GfoDotdpfWI%2B0VjT0aF3JD2zxqgb4ETxxjun4O0ybTTIxFJCAjdg%2F60ytqPyVWv83hL%2B%2BlhK%2Ft%2FRmSl6XKlM0KTiC%2BEbNSvN0%2FWL3doN4q8QcxJaWas83gTIKKlC8J8qRpcahmbt2effPE%2FMl9MPnd9YGsKKrsOsO39wMJHNt8oGOqUBASdkkD%2B0i1OccjTLUjPvWA%2FFOMH%2F%2F8exKw6u2leZ4gxtbJwD%2F4RkOEoROnXZitQzYWzIHmAiVB0ocOHU0OApUTUvHk4Dohh9%2BEEEMZHiVI2%2BvDl%2FTXwciOOWhzIw4JuhtA9EyRF4g6die5njIOBHvMku5UHJ2txq9HBn2odFdBb%2FynoKBC8XkP2KoCPwea3IPwSFr7C0VRxfwSMRqkCgyf1U1BXr&X-Amz-Signature=50b09dafeb6a5189642629092f3c8f3286395f09b29a3ec123abf5fddd970031&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TGMTNPY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDJ81%2FtFJYWcKhmrY4pLvDL2bplxmi13ZX7kfL%2FIQXPwIgPJLLOQ2vJGFz9YqcvuToNNCyXPii1AtNUD7wHUKSjiAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDGEUNn6Z2l1dCYTw7yrcA4Z3VmtiYG0TGofMmAwJ5Oq%2FSjn39b7g6cyvADP%2FWDKUSWZhkeFKospxM6B56HjP0%2FxcyA4jTEGj5dilvz%2FkB5KJrcab59I0e55n8QFg4GS5%2BvDYKZfNajhMFQ1ckny4G8ohqiszVHTnoYquDmDhpNdFJ3e38xN4goVdI6FQ%2FfZHoWzXE6%2FE0saCdc6E6%2FbR4AGInpSXq0LVvSsZ8czqGBysqtdX8tr0fdilHZC1dj3pgW%2BRt089%2BEBm%2B74RRYqcqewMYS120pp%2FXbbYllkLymhzL7pnhcLnfOoZw9N7om%2F552Ofgdjwdnm3E56RaLFS7ZieQQV7Yo3qEwQ3oPPZcWuf0fWYfqcyqAbkv%2Bjqqg1AhnxS%2FEDDDlT7IaNAKe9omBGlbEjInz%2FGayN1I9aFjbCB33t5yhbeVuLpe9Ys2KrBTB9s2Bvj4pvflVFwLq9YN70V5ApAuOdQmb73VE3fW3a3GfoDotdpfWI%2B0VjT0aF3JD2zxqgb4ETxxjun4O0ybTTIxFJCAjdg%2F60ytqPyVWv83hL%2B%2BlhK%2Ft%2FRmSl6XKlM0KTiC%2BEbNSvN0%2FWL3doN4q8QcxJaWas83gTIKKlC8J8qRpcahmbt2effPE%2FMl9MPnd9YGsKKrsOsO39wMJHNt8oGOqUBASdkkD%2B0i1OccjTLUjPvWA%2FFOMH%2F%2F8exKw6u2leZ4gxtbJwD%2F4RkOEoROnXZitQzYWzIHmAiVB0ocOHU0OApUTUvHk4Dohh9%2BEEEMZHiVI2%2BvDl%2FTXwciOOWhzIw4JuhtA9EyRF4g6die5njIOBHvMku5UHJ2txq9HBn2odFdBb%2FynoKBC8XkP2KoCPwea3IPwSFr7C0VRxfwSMRqkCgyf1U1BXr&X-Amz-Signature=526fcf29dd631525a0e75b3960ac73aac9cc5104dfe41b00e33d6f73d37c7f32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TGMTNPY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDJ81%2FtFJYWcKhmrY4pLvDL2bplxmi13ZX7kfL%2FIQXPwIgPJLLOQ2vJGFz9YqcvuToNNCyXPii1AtNUD7wHUKSjiAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDGEUNn6Z2l1dCYTw7yrcA4Z3VmtiYG0TGofMmAwJ5Oq%2FSjn39b7g6cyvADP%2FWDKUSWZhkeFKospxM6B56HjP0%2FxcyA4jTEGj5dilvz%2FkB5KJrcab59I0e55n8QFg4GS5%2BvDYKZfNajhMFQ1ckny4G8ohqiszVHTnoYquDmDhpNdFJ3e38xN4goVdI6FQ%2FfZHoWzXE6%2FE0saCdc6E6%2FbR4AGInpSXq0LVvSsZ8czqGBysqtdX8tr0fdilHZC1dj3pgW%2BRt089%2BEBm%2B74RRYqcqewMYS120pp%2FXbbYllkLymhzL7pnhcLnfOoZw9N7om%2F552Ofgdjwdnm3E56RaLFS7ZieQQV7Yo3qEwQ3oPPZcWuf0fWYfqcyqAbkv%2Bjqqg1AhnxS%2FEDDDlT7IaNAKe9omBGlbEjInz%2FGayN1I9aFjbCB33t5yhbeVuLpe9Ys2KrBTB9s2Bvj4pvflVFwLq9YN70V5ApAuOdQmb73VE3fW3a3GfoDotdpfWI%2B0VjT0aF3JD2zxqgb4ETxxjun4O0ybTTIxFJCAjdg%2F60ytqPyVWv83hL%2B%2BlhK%2Ft%2FRmSl6XKlM0KTiC%2BEbNSvN0%2FWL3doN4q8QcxJaWas83gTIKKlC8J8qRpcahmbt2effPE%2FMl9MPnd9YGsKKrsOsO39wMJHNt8oGOqUBASdkkD%2B0i1OccjTLUjPvWA%2FFOMH%2F%2F8exKw6u2leZ4gxtbJwD%2F4RkOEoROnXZitQzYWzIHmAiVB0ocOHU0OApUTUvHk4Dohh9%2BEEEMZHiVI2%2BvDl%2FTXwciOOWhzIw4JuhtA9EyRF4g6die5njIOBHvMku5UHJ2txq9HBn2odFdBb%2FynoKBC8XkP2KoCPwea3IPwSFr7C0VRxfwSMRqkCgyf1U1BXr&X-Amz-Signature=199b12119f7a2717eaf73adaa5337d11fb7d0cbea4349ce139407b14d1706c68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

