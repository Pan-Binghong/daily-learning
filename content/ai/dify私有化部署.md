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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONYPCEU%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDUye3wHIDToGgZc3rmPDIQu0dvJ54Kd7Ot%2BxB3%2B4l3OgIgGGg099RZvVeFmEaBF46UO7JRPUjybQQ2ycZD7qLwG%2Bwq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKiRZzSNW%2FB7AxZyGyrcA6qBibYUkT1PJCBlJqctXmisFi%2BkaoxupyX6sTqc2sKsGyxLR1sLSFqYf9bvrrfL8FzUz1o93S%2FVMnAoXtVLKLZ5FLBIOHftSNt23mU7r4nx%2BrLfFb%2Fhs2qRUBTb9JZFvyfFugR2tX3n8y%2BCjfqAV3o6729sLt49Zrl51RTX5nuy9YwhkMx57igf1mp6z8pVO4JYw7EOVMeMmG8bKxsgjXVHK7JuoUT%2B%2B%2B7zvvz62s%2BDBZDudTsZcK%2BIu65%2BrWS1rcNRgDTqRIpXDNcVFVh%2BpdtUw5qyCq24vYH7pI22oE1Hes%2FhsxGagx3D8YwqVTlKVpgurpmdahCgwbSt%2Fl1cN%2FySNuFt3R73Xmu47rxdyWGcXffN4GbKh0%2FCFohaeM2dhHbFghWUJSP0bJBSPIMkKyXosFQkZ35mtN%2BtWaJmNEY7XTBPkdFNQ1sdEM8Q5jyVszNE1vjre5jT8S%2FGyiPwv0aZ6IdjSLT8ctQ0kPFe%2BUA6qC%2FL2yP3z9%2B8WMGYNM%2BENLygZVmqIfd8HDXgnVHfg%2FLEY5Sr%2BE7oo4U%2FeaP%2FxeWPlP8OimFaQFJUceNZRtAQ%2FXkdt1KVEcLN7PAU%2FjxkGKl5c957%2FEXohM5Y6Cju2AhEBvj5c7f%2Ft31CyjZpMK3euMkGOqUBK60hVz6o4TecNGHUDXeD47dJv%2FZGuNdZr3Ew9W40EfO1lxYHdc5oNx45YfPwYwUeYpggoF3o6JDumW8AJjzAnJO5r63hRxp43xgIpJebvbGqE2ssDt1oFVhrmeXPHAFBV2ypNFrk86uRsxaLWlcvium%2FSOG4gY6toqZUD1osO%2BT1k1JZi2e48eGQMXC84zFzUlSlT8hazYGWe%2BsrUHDVlWH%2F2FmE&X-Amz-Signature=0bdcd0df872f946e1cbdce83c28588232af085bb65ef6d9cf8e1234d1244a064&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONYPCEU%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDUye3wHIDToGgZc3rmPDIQu0dvJ54Kd7Ot%2BxB3%2B4l3OgIgGGg099RZvVeFmEaBF46UO7JRPUjybQQ2ycZD7qLwG%2Bwq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKiRZzSNW%2FB7AxZyGyrcA6qBibYUkT1PJCBlJqctXmisFi%2BkaoxupyX6sTqc2sKsGyxLR1sLSFqYf9bvrrfL8FzUz1o93S%2FVMnAoXtVLKLZ5FLBIOHftSNt23mU7r4nx%2BrLfFb%2Fhs2qRUBTb9JZFvyfFugR2tX3n8y%2BCjfqAV3o6729sLt49Zrl51RTX5nuy9YwhkMx57igf1mp6z8pVO4JYw7EOVMeMmG8bKxsgjXVHK7JuoUT%2B%2B%2B7zvvz62s%2BDBZDudTsZcK%2BIu65%2BrWS1rcNRgDTqRIpXDNcVFVh%2BpdtUw5qyCq24vYH7pI22oE1Hes%2FhsxGagx3D8YwqVTlKVpgurpmdahCgwbSt%2Fl1cN%2FySNuFt3R73Xmu47rxdyWGcXffN4GbKh0%2FCFohaeM2dhHbFghWUJSP0bJBSPIMkKyXosFQkZ35mtN%2BtWaJmNEY7XTBPkdFNQ1sdEM8Q5jyVszNE1vjre5jT8S%2FGyiPwv0aZ6IdjSLT8ctQ0kPFe%2BUA6qC%2FL2yP3z9%2B8WMGYNM%2BENLygZVmqIfd8HDXgnVHfg%2FLEY5Sr%2BE7oo4U%2FeaP%2FxeWPlP8OimFaQFJUceNZRtAQ%2FXkdt1KVEcLN7PAU%2FjxkGKl5c957%2FEXohM5Y6Cju2AhEBvj5c7f%2Ft31CyjZpMK3euMkGOqUBK60hVz6o4TecNGHUDXeD47dJv%2FZGuNdZr3Ew9W40EfO1lxYHdc5oNx45YfPwYwUeYpggoF3o6JDumW8AJjzAnJO5r63hRxp43xgIpJebvbGqE2ssDt1oFVhrmeXPHAFBV2ypNFrk86uRsxaLWlcvium%2FSOG4gY6toqZUD1osO%2BT1k1JZi2e48eGQMXC84zFzUlSlT8hazYGWe%2BsrUHDVlWH%2F2FmE&X-Amz-Signature=eaa8fa6fe8bae48c90f3b431d44c8503a1c15081d2356f3738de64e4f9be56f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONYPCEU%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDUye3wHIDToGgZc3rmPDIQu0dvJ54Kd7Ot%2BxB3%2B4l3OgIgGGg099RZvVeFmEaBF46UO7JRPUjybQQ2ycZD7qLwG%2Bwq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKiRZzSNW%2FB7AxZyGyrcA6qBibYUkT1PJCBlJqctXmisFi%2BkaoxupyX6sTqc2sKsGyxLR1sLSFqYf9bvrrfL8FzUz1o93S%2FVMnAoXtVLKLZ5FLBIOHftSNt23mU7r4nx%2BrLfFb%2Fhs2qRUBTb9JZFvyfFugR2tX3n8y%2BCjfqAV3o6729sLt49Zrl51RTX5nuy9YwhkMx57igf1mp6z8pVO4JYw7EOVMeMmG8bKxsgjXVHK7JuoUT%2B%2B%2B7zvvz62s%2BDBZDudTsZcK%2BIu65%2BrWS1rcNRgDTqRIpXDNcVFVh%2BpdtUw5qyCq24vYH7pI22oE1Hes%2FhsxGagx3D8YwqVTlKVpgurpmdahCgwbSt%2Fl1cN%2FySNuFt3R73Xmu47rxdyWGcXffN4GbKh0%2FCFohaeM2dhHbFghWUJSP0bJBSPIMkKyXosFQkZ35mtN%2BtWaJmNEY7XTBPkdFNQ1sdEM8Q5jyVszNE1vjre5jT8S%2FGyiPwv0aZ6IdjSLT8ctQ0kPFe%2BUA6qC%2FL2yP3z9%2B8WMGYNM%2BENLygZVmqIfd8HDXgnVHfg%2FLEY5Sr%2BE7oo4U%2FeaP%2FxeWPlP8OimFaQFJUceNZRtAQ%2FXkdt1KVEcLN7PAU%2FjxkGKl5c957%2FEXohM5Y6Cju2AhEBvj5c7f%2Ft31CyjZpMK3euMkGOqUBK60hVz6o4TecNGHUDXeD47dJv%2FZGuNdZr3Ew9W40EfO1lxYHdc5oNx45YfPwYwUeYpggoF3o6JDumW8AJjzAnJO5r63hRxp43xgIpJebvbGqE2ssDt1oFVhrmeXPHAFBV2ypNFrk86uRsxaLWlcvium%2FSOG4gY6toqZUD1osO%2BT1k1JZi2e48eGQMXC84zFzUlSlT8hazYGWe%2BsrUHDVlWH%2F2FmE&X-Amz-Signature=51ea4cf541215fe6dda99a9c8e76ae6ac70de3b83e97a2e557ddd6403ad30c8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONYPCEU%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDUye3wHIDToGgZc3rmPDIQu0dvJ54Kd7Ot%2BxB3%2B4l3OgIgGGg099RZvVeFmEaBF46UO7JRPUjybQQ2ycZD7qLwG%2Bwq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKiRZzSNW%2FB7AxZyGyrcA6qBibYUkT1PJCBlJqctXmisFi%2BkaoxupyX6sTqc2sKsGyxLR1sLSFqYf9bvrrfL8FzUz1o93S%2FVMnAoXtVLKLZ5FLBIOHftSNt23mU7r4nx%2BrLfFb%2Fhs2qRUBTb9JZFvyfFugR2tX3n8y%2BCjfqAV3o6729sLt49Zrl51RTX5nuy9YwhkMx57igf1mp6z8pVO4JYw7EOVMeMmG8bKxsgjXVHK7JuoUT%2B%2B%2B7zvvz62s%2BDBZDudTsZcK%2BIu65%2BrWS1rcNRgDTqRIpXDNcVFVh%2BpdtUw5qyCq24vYH7pI22oE1Hes%2FhsxGagx3D8YwqVTlKVpgurpmdahCgwbSt%2Fl1cN%2FySNuFt3R73Xmu47rxdyWGcXffN4GbKh0%2FCFohaeM2dhHbFghWUJSP0bJBSPIMkKyXosFQkZ35mtN%2BtWaJmNEY7XTBPkdFNQ1sdEM8Q5jyVszNE1vjre5jT8S%2FGyiPwv0aZ6IdjSLT8ctQ0kPFe%2BUA6qC%2FL2yP3z9%2B8WMGYNM%2BENLygZVmqIfd8HDXgnVHfg%2FLEY5Sr%2BE7oo4U%2FeaP%2FxeWPlP8OimFaQFJUceNZRtAQ%2FXkdt1KVEcLN7PAU%2FjxkGKl5c957%2FEXohM5Y6Cju2AhEBvj5c7f%2Ft31CyjZpMK3euMkGOqUBK60hVz6o4TecNGHUDXeD47dJv%2FZGuNdZr3Ew9W40EfO1lxYHdc5oNx45YfPwYwUeYpggoF3o6JDumW8AJjzAnJO5r63hRxp43xgIpJebvbGqE2ssDt1oFVhrmeXPHAFBV2ypNFrk86uRsxaLWlcvium%2FSOG4gY6toqZUD1osO%2BT1k1JZi2e48eGQMXC84zFzUlSlT8hazYGWe%2BsrUHDVlWH%2F2FmE&X-Amz-Signature=9b187aad706dbe193dd6dd10b97eed02c71d85a68fec73e5fd92b4b2d67cd1bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONYPCEU%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDUye3wHIDToGgZc3rmPDIQu0dvJ54Kd7Ot%2BxB3%2B4l3OgIgGGg099RZvVeFmEaBF46UO7JRPUjybQQ2ycZD7qLwG%2Bwq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKiRZzSNW%2FB7AxZyGyrcA6qBibYUkT1PJCBlJqctXmisFi%2BkaoxupyX6sTqc2sKsGyxLR1sLSFqYf9bvrrfL8FzUz1o93S%2FVMnAoXtVLKLZ5FLBIOHftSNt23mU7r4nx%2BrLfFb%2Fhs2qRUBTb9JZFvyfFugR2tX3n8y%2BCjfqAV3o6729sLt49Zrl51RTX5nuy9YwhkMx57igf1mp6z8pVO4JYw7EOVMeMmG8bKxsgjXVHK7JuoUT%2B%2B%2B7zvvz62s%2BDBZDudTsZcK%2BIu65%2BrWS1rcNRgDTqRIpXDNcVFVh%2BpdtUw5qyCq24vYH7pI22oE1Hes%2FhsxGagx3D8YwqVTlKVpgurpmdahCgwbSt%2Fl1cN%2FySNuFt3R73Xmu47rxdyWGcXffN4GbKh0%2FCFohaeM2dhHbFghWUJSP0bJBSPIMkKyXosFQkZ35mtN%2BtWaJmNEY7XTBPkdFNQ1sdEM8Q5jyVszNE1vjre5jT8S%2FGyiPwv0aZ6IdjSLT8ctQ0kPFe%2BUA6qC%2FL2yP3z9%2B8WMGYNM%2BENLygZVmqIfd8HDXgnVHfg%2FLEY5Sr%2BE7oo4U%2FeaP%2FxeWPlP8OimFaQFJUceNZRtAQ%2FXkdt1KVEcLN7PAU%2FjxkGKl5c957%2FEXohM5Y6Cju2AhEBvj5c7f%2Ft31CyjZpMK3euMkGOqUBK60hVz6o4TecNGHUDXeD47dJv%2FZGuNdZr3Ew9W40EfO1lxYHdc5oNx45YfPwYwUeYpggoF3o6JDumW8AJjzAnJO5r63hRxp43xgIpJebvbGqE2ssDt1oFVhrmeXPHAFBV2ypNFrk86uRsxaLWlcvium%2FSOG4gY6toqZUD1osO%2BT1k1JZi2e48eGQMXC84zFzUlSlT8hazYGWe%2BsrUHDVlWH%2F2FmE&X-Amz-Signature=632b907541449bdf6832b9b4c82ce8685665893f9bead83507055cb3f55583b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONYPCEU%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDUye3wHIDToGgZc3rmPDIQu0dvJ54Kd7Ot%2BxB3%2B4l3OgIgGGg099RZvVeFmEaBF46UO7JRPUjybQQ2ycZD7qLwG%2Bwq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKiRZzSNW%2FB7AxZyGyrcA6qBibYUkT1PJCBlJqctXmisFi%2BkaoxupyX6sTqc2sKsGyxLR1sLSFqYf9bvrrfL8FzUz1o93S%2FVMnAoXtVLKLZ5FLBIOHftSNt23mU7r4nx%2BrLfFb%2Fhs2qRUBTb9JZFvyfFugR2tX3n8y%2BCjfqAV3o6729sLt49Zrl51RTX5nuy9YwhkMx57igf1mp6z8pVO4JYw7EOVMeMmG8bKxsgjXVHK7JuoUT%2B%2B%2B7zvvz62s%2BDBZDudTsZcK%2BIu65%2BrWS1rcNRgDTqRIpXDNcVFVh%2BpdtUw5qyCq24vYH7pI22oE1Hes%2FhsxGagx3D8YwqVTlKVpgurpmdahCgwbSt%2Fl1cN%2FySNuFt3R73Xmu47rxdyWGcXffN4GbKh0%2FCFohaeM2dhHbFghWUJSP0bJBSPIMkKyXosFQkZ35mtN%2BtWaJmNEY7XTBPkdFNQ1sdEM8Q5jyVszNE1vjre5jT8S%2FGyiPwv0aZ6IdjSLT8ctQ0kPFe%2BUA6qC%2FL2yP3z9%2B8WMGYNM%2BENLygZVmqIfd8HDXgnVHfg%2FLEY5Sr%2BE7oo4U%2FeaP%2FxeWPlP8OimFaQFJUceNZRtAQ%2FXkdt1KVEcLN7PAU%2FjxkGKl5c957%2FEXohM5Y6Cju2AhEBvj5c7f%2Ft31CyjZpMK3euMkGOqUBK60hVz6o4TecNGHUDXeD47dJv%2FZGuNdZr3Ew9W40EfO1lxYHdc5oNx45YfPwYwUeYpggoF3o6JDumW8AJjzAnJO5r63hRxp43xgIpJebvbGqE2ssDt1oFVhrmeXPHAFBV2ypNFrk86uRsxaLWlcvium%2FSOG4gY6toqZUD1osO%2BT1k1JZi2e48eGQMXC84zFzUlSlT8hazYGWe%2BsrUHDVlWH%2F2FmE&X-Amz-Signature=67a8f17a8c4bf79c8ff620f2d194fee0882192b94b3e9340eb6b7e739eb17265&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONYPCEU%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDUye3wHIDToGgZc3rmPDIQu0dvJ54Kd7Ot%2BxB3%2B4l3OgIgGGg099RZvVeFmEaBF46UO7JRPUjybQQ2ycZD7qLwG%2Bwq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKiRZzSNW%2FB7AxZyGyrcA6qBibYUkT1PJCBlJqctXmisFi%2BkaoxupyX6sTqc2sKsGyxLR1sLSFqYf9bvrrfL8FzUz1o93S%2FVMnAoXtVLKLZ5FLBIOHftSNt23mU7r4nx%2BrLfFb%2Fhs2qRUBTb9JZFvyfFugR2tX3n8y%2BCjfqAV3o6729sLt49Zrl51RTX5nuy9YwhkMx57igf1mp6z8pVO4JYw7EOVMeMmG8bKxsgjXVHK7JuoUT%2B%2B%2B7zvvz62s%2BDBZDudTsZcK%2BIu65%2BrWS1rcNRgDTqRIpXDNcVFVh%2BpdtUw5qyCq24vYH7pI22oE1Hes%2FhsxGagx3D8YwqVTlKVpgurpmdahCgwbSt%2Fl1cN%2FySNuFt3R73Xmu47rxdyWGcXffN4GbKh0%2FCFohaeM2dhHbFghWUJSP0bJBSPIMkKyXosFQkZ35mtN%2BtWaJmNEY7XTBPkdFNQ1sdEM8Q5jyVszNE1vjre5jT8S%2FGyiPwv0aZ6IdjSLT8ctQ0kPFe%2BUA6qC%2FL2yP3z9%2B8WMGYNM%2BENLygZVmqIfd8HDXgnVHfg%2FLEY5Sr%2BE7oo4U%2FeaP%2FxeWPlP8OimFaQFJUceNZRtAQ%2FXkdt1KVEcLN7PAU%2FjxkGKl5c957%2FEXohM5Y6Cju2AhEBvj5c7f%2Ft31CyjZpMK3euMkGOqUBK60hVz6o4TecNGHUDXeD47dJv%2FZGuNdZr3Ew9W40EfO1lxYHdc5oNx45YfPwYwUeYpggoF3o6JDumW8AJjzAnJO5r63hRxp43xgIpJebvbGqE2ssDt1oFVhrmeXPHAFBV2ypNFrk86uRsxaLWlcvium%2FSOG4gY6toqZUD1osO%2BT1k1JZi2e48eGQMXC84zFzUlSlT8hazYGWe%2BsrUHDVlWH%2F2FmE&X-Amz-Signature=73aee4f3b4363e9eb0c0069f33ec7ac0e583dfa5fd15f2845b4022a92335f0b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONYPCEU%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDUye3wHIDToGgZc3rmPDIQu0dvJ54Kd7Ot%2BxB3%2B4l3OgIgGGg099RZvVeFmEaBF46UO7JRPUjybQQ2ycZD7qLwG%2Bwq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKiRZzSNW%2FB7AxZyGyrcA6qBibYUkT1PJCBlJqctXmisFi%2BkaoxupyX6sTqc2sKsGyxLR1sLSFqYf9bvrrfL8FzUz1o93S%2FVMnAoXtVLKLZ5FLBIOHftSNt23mU7r4nx%2BrLfFb%2Fhs2qRUBTb9JZFvyfFugR2tX3n8y%2BCjfqAV3o6729sLt49Zrl51RTX5nuy9YwhkMx57igf1mp6z8pVO4JYw7EOVMeMmG8bKxsgjXVHK7JuoUT%2B%2B%2B7zvvz62s%2BDBZDudTsZcK%2BIu65%2BrWS1rcNRgDTqRIpXDNcVFVh%2BpdtUw5qyCq24vYH7pI22oE1Hes%2FhsxGagx3D8YwqVTlKVpgurpmdahCgwbSt%2Fl1cN%2FySNuFt3R73Xmu47rxdyWGcXffN4GbKh0%2FCFohaeM2dhHbFghWUJSP0bJBSPIMkKyXosFQkZ35mtN%2BtWaJmNEY7XTBPkdFNQ1sdEM8Q5jyVszNE1vjre5jT8S%2FGyiPwv0aZ6IdjSLT8ctQ0kPFe%2BUA6qC%2FL2yP3z9%2B8WMGYNM%2BENLygZVmqIfd8HDXgnVHfg%2FLEY5Sr%2BE7oo4U%2FeaP%2FxeWPlP8OimFaQFJUceNZRtAQ%2FXkdt1KVEcLN7PAU%2FjxkGKl5c957%2FEXohM5Y6Cju2AhEBvj5c7f%2Ft31CyjZpMK3euMkGOqUBK60hVz6o4TecNGHUDXeD47dJv%2FZGuNdZr3Ew9W40EfO1lxYHdc5oNx45YfPwYwUeYpggoF3o6JDumW8AJjzAnJO5r63hRxp43xgIpJebvbGqE2ssDt1oFVhrmeXPHAFBV2ypNFrk86uRsxaLWlcvium%2FSOG4gY6toqZUD1osO%2BT1k1JZi2e48eGQMXC84zFzUlSlT8hazYGWe%2BsrUHDVlWH%2F2FmE&X-Amz-Signature=19d5bd3af221532c609bed3280fff19f4ce898daf3eed6901b3d481e1994ba53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONYPCEU%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDUye3wHIDToGgZc3rmPDIQu0dvJ54Kd7Ot%2BxB3%2B4l3OgIgGGg099RZvVeFmEaBF46UO7JRPUjybQQ2ycZD7qLwG%2Bwq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKiRZzSNW%2FB7AxZyGyrcA6qBibYUkT1PJCBlJqctXmisFi%2BkaoxupyX6sTqc2sKsGyxLR1sLSFqYf9bvrrfL8FzUz1o93S%2FVMnAoXtVLKLZ5FLBIOHftSNt23mU7r4nx%2BrLfFb%2Fhs2qRUBTb9JZFvyfFugR2tX3n8y%2BCjfqAV3o6729sLt49Zrl51RTX5nuy9YwhkMx57igf1mp6z8pVO4JYw7EOVMeMmG8bKxsgjXVHK7JuoUT%2B%2B%2B7zvvz62s%2BDBZDudTsZcK%2BIu65%2BrWS1rcNRgDTqRIpXDNcVFVh%2BpdtUw5qyCq24vYH7pI22oE1Hes%2FhsxGagx3D8YwqVTlKVpgurpmdahCgwbSt%2Fl1cN%2FySNuFt3R73Xmu47rxdyWGcXffN4GbKh0%2FCFohaeM2dhHbFghWUJSP0bJBSPIMkKyXosFQkZ35mtN%2BtWaJmNEY7XTBPkdFNQ1sdEM8Q5jyVszNE1vjre5jT8S%2FGyiPwv0aZ6IdjSLT8ctQ0kPFe%2BUA6qC%2FL2yP3z9%2B8WMGYNM%2BENLygZVmqIfd8HDXgnVHfg%2FLEY5Sr%2BE7oo4U%2FeaP%2FxeWPlP8OimFaQFJUceNZRtAQ%2FXkdt1KVEcLN7PAU%2FjxkGKl5c957%2FEXohM5Y6Cju2AhEBvj5c7f%2Ft31CyjZpMK3euMkGOqUBK60hVz6o4TecNGHUDXeD47dJv%2FZGuNdZr3Ew9W40EfO1lxYHdc5oNx45YfPwYwUeYpggoF3o6JDumW8AJjzAnJO5r63hRxp43xgIpJebvbGqE2ssDt1oFVhrmeXPHAFBV2ypNFrk86uRsxaLWlcvium%2FSOG4gY6toqZUD1osO%2BT1k1JZi2e48eGQMXC84zFzUlSlT8hazYGWe%2BsrUHDVlWH%2F2FmE&X-Amz-Signature=10a067bab6278aff74e59f74905d3950d2cb017489377226d448540a0c300376&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ONYPCEU%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDUye3wHIDToGgZc3rmPDIQu0dvJ54Kd7Ot%2BxB3%2B4l3OgIgGGg099RZvVeFmEaBF46UO7JRPUjybQQ2ycZD7qLwG%2Bwq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDKiRZzSNW%2FB7AxZyGyrcA6qBibYUkT1PJCBlJqctXmisFi%2BkaoxupyX6sTqc2sKsGyxLR1sLSFqYf9bvrrfL8FzUz1o93S%2FVMnAoXtVLKLZ5FLBIOHftSNt23mU7r4nx%2BrLfFb%2Fhs2qRUBTb9JZFvyfFugR2tX3n8y%2BCjfqAV3o6729sLt49Zrl51RTX5nuy9YwhkMx57igf1mp6z8pVO4JYw7EOVMeMmG8bKxsgjXVHK7JuoUT%2B%2B%2B7zvvz62s%2BDBZDudTsZcK%2BIu65%2BrWS1rcNRgDTqRIpXDNcVFVh%2BpdtUw5qyCq24vYH7pI22oE1Hes%2FhsxGagx3D8YwqVTlKVpgurpmdahCgwbSt%2Fl1cN%2FySNuFt3R73Xmu47rxdyWGcXffN4GbKh0%2FCFohaeM2dhHbFghWUJSP0bJBSPIMkKyXosFQkZ35mtN%2BtWaJmNEY7XTBPkdFNQ1sdEM8Q5jyVszNE1vjre5jT8S%2FGyiPwv0aZ6IdjSLT8ctQ0kPFe%2BUA6qC%2FL2yP3z9%2B8WMGYNM%2BENLygZVmqIfd8HDXgnVHfg%2FLEY5Sr%2BE7oo4U%2FeaP%2FxeWPlP8OimFaQFJUceNZRtAQ%2FXkdt1KVEcLN7PAU%2FjxkGKl5c957%2FEXohM5Y6Cju2AhEBvj5c7f%2Ft31CyjZpMK3euMkGOqUBK60hVz6o4TecNGHUDXeD47dJv%2FZGuNdZr3Ew9W40EfO1lxYHdc5oNx45YfPwYwUeYpggoF3o6JDumW8AJjzAnJO5r63hRxp43xgIpJebvbGqE2ssDt1oFVhrmeXPHAFBV2ypNFrk86uRsxaLWlcvium%2FSOG4gY6toqZUD1osO%2BT1k1JZi2e48eGQMXC84zFzUlSlT8hazYGWe%2BsrUHDVlWH%2F2FmE&X-Amz-Signature=e52d3dccad147522e6e7d5337a029b8fad56b5177d1169a806fa0ac6329d4b3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

