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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z35MHNMI%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxmRzU%2Blp9Y2%2Bokte03Fu3L3rkTETL%2FnS9zg7jpSQ3VwIgHj%2BXqDMTgm%2F78LOfKd8%2BVYMcjUqsCvB7jNggtWcO4nAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhbN6k1MGJUtqEd2SrcA%2B5dC1F4psuAvY8sPJJHZb%2F5E1J79Zu2Var0xwv70waYtEuHjbhFMCA5pbFRYeR3SeiRUSGeJyxTOiPUZZwfQGtc3YvapnxrTRM%2F05KkRIZYuzDrz%2BidFifh0jjTt03DiFa8I7XjmxH9fQI%2B358x1Snj95l0yQ05bsqXE31y8icd1EYCLZUWBwJXr9Gx6znGnDbGAX%2F7Y9sY2ojMY8%2Fjr8mxh2PXXlUrYZu2%2FUtjJ4y644M71TNpTV1WHp5L45D37zAWclIH3K6s1pDDsX%2F4jdHKc9o%2F6lCHFoDdk5HPkfKRrgTakmR%2FDNj1dHFpgZHRR1LktKl58td%2FSeshjizQugfUg%2FgUc%2BQDIQyVVtLX7cwJxqhKX%2F64doA0OGvH6kIFqo06nCG3UWx%2F7SEe%2BKbOjNlIN%2FMvM7c8Kla9z5ZzrDPFX4bo7vA4ZQHy1O%2F8Ggx5MWHU%2B6s5AYU9r2dCulgFTb0eRPm%2FZZIwWHXoeU%2FUW3dkdkGW0i6B2DZvu1PW49cL%2BDZwGWd9UYqXSWLazs6MIKJlSEJw%2FTY%2Be%2FYwfNpM7oK6Bv78tYLD2s%2B14sK7qWhiVq7LgJ9OMl8mhUslOWgDIGIYWgTe8NHObL1l5bmTKpPmxSTTxCAIce4oKRd6MLiH6sgGOqUBZOnj8hs39a0M85MGzEWMAAeLWNL7styiZT3UlFZM%2B7w%2B6sWhCHCtS012m8PM4T6tzMOUiaqqjVIYyIYYhCLVzb%2FIVZHLBxPXY8wXWdXKjvt7fuxOLH0DUYB1QF4U75jrNc0gDkh%2BveSlyd8K8174Dz53tq24ntzO%2BNTI%2Fn0VRYZnaxx4dWrr25uc7UqWYZ57pssFe%2F0sptbZZm29l7nHcouUELfP&X-Amz-Signature=a57e882950a7cb5d31fcc9a612fec7fe359cc2cd11dbfb8badabc2c8203deed0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z35MHNMI%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxmRzU%2Blp9Y2%2Bokte03Fu3L3rkTETL%2FnS9zg7jpSQ3VwIgHj%2BXqDMTgm%2F78LOfKd8%2BVYMcjUqsCvB7jNggtWcO4nAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhbN6k1MGJUtqEd2SrcA%2B5dC1F4psuAvY8sPJJHZb%2F5E1J79Zu2Var0xwv70waYtEuHjbhFMCA5pbFRYeR3SeiRUSGeJyxTOiPUZZwfQGtc3YvapnxrTRM%2F05KkRIZYuzDrz%2BidFifh0jjTt03DiFa8I7XjmxH9fQI%2B358x1Snj95l0yQ05bsqXE31y8icd1EYCLZUWBwJXr9Gx6znGnDbGAX%2F7Y9sY2ojMY8%2Fjr8mxh2PXXlUrYZu2%2FUtjJ4y644M71TNpTV1WHp5L45D37zAWclIH3K6s1pDDsX%2F4jdHKc9o%2F6lCHFoDdk5HPkfKRrgTakmR%2FDNj1dHFpgZHRR1LktKl58td%2FSeshjizQugfUg%2FgUc%2BQDIQyVVtLX7cwJxqhKX%2F64doA0OGvH6kIFqo06nCG3UWx%2F7SEe%2BKbOjNlIN%2FMvM7c8Kla9z5ZzrDPFX4bo7vA4ZQHy1O%2F8Ggx5MWHU%2B6s5AYU9r2dCulgFTb0eRPm%2FZZIwWHXoeU%2FUW3dkdkGW0i6B2DZvu1PW49cL%2BDZwGWd9UYqXSWLazs6MIKJlSEJw%2FTY%2Be%2FYwfNpM7oK6Bv78tYLD2s%2B14sK7qWhiVq7LgJ9OMl8mhUslOWgDIGIYWgTe8NHObL1l5bmTKpPmxSTTxCAIce4oKRd6MLiH6sgGOqUBZOnj8hs39a0M85MGzEWMAAeLWNL7styiZT3UlFZM%2B7w%2B6sWhCHCtS012m8PM4T6tzMOUiaqqjVIYyIYYhCLVzb%2FIVZHLBxPXY8wXWdXKjvt7fuxOLH0DUYB1QF4U75jrNc0gDkh%2BveSlyd8K8174Dz53tq24ntzO%2BNTI%2Fn0VRYZnaxx4dWrr25uc7UqWYZ57pssFe%2F0sptbZZm29l7nHcouUELfP&X-Amz-Signature=685f1066074d734997a6e3d50f90f959b753669fecfa43351eecdca0d32ea368&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z35MHNMI%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxmRzU%2Blp9Y2%2Bokte03Fu3L3rkTETL%2FnS9zg7jpSQ3VwIgHj%2BXqDMTgm%2F78LOfKd8%2BVYMcjUqsCvB7jNggtWcO4nAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhbN6k1MGJUtqEd2SrcA%2B5dC1F4psuAvY8sPJJHZb%2F5E1J79Zu2Var0xwv70waYtEuHjbhFMCA5pbFRYeR3SeiRUSGeJyxTOiPUZZwfQGtc3YvapnxrTRM%2F05KkRIZYuzDrz%2BidFifh0jjTt03DiFa8I7XjmxH9fQI%2B358x1Snj95l0yQ05bsqXE31y8icd1EYCLZUWBwJXr9Gx6znGnDbGAX%2F7Y9sY2ojMY8%2Fjr8mxh2PXXlUrYZu2%2FUtjJ4y644M71TNpTV1WHp5L45D37zAWclIH3K6s1pDDsX%2F4jdHKc9o%2F6lCHFoDdk5HPkfKRrgTakmR%2FDNj1dHFpgZHRR1LktKl58td%2FSeshjizQugfUg%2FgUc%2BQDIQyVVtLX7cwJxqhKX%2F64doA0OGvH6kIFqo06nCG3UWx%2F7SEe%2BKbOjNlIN%2FMvM7c8Kla9z5ZzrDPFX4bo7vA4ZQHy1O%2F8Ggx5MWHU%2B6s5AYU9r2dCulgFTb0eRPm%2FZZIwWHXoeU%2FUW3dkdkGW0i6B2DZvu1PW49cL%2BDZwGWd9UYqXSWLazs6MIKJlSEJw%2FTY%2Be%2FYwfNpM7oK6Bv78tYLD2s%2B14sK7qWhiVq7LgJ9OMl8mhUslOWgDIGIYWgTe8NHObL1l5bmTKpPmxSTTxCAIce4oKRd6MLiH6sgGOqUBZOnj8hs39a0M85MGzEWMAAeLWNL7styiZT3UlFZM%2B7w%2B6sWhCHCtS012m8PM4T6tzMOUiaqqjVIYyIYYhCLVzb%2FIVZHLBxPXY8wXWdXKjvt7fuxOLH0DUYB1QF4U75jrNc0gDkh%2BveSlyd8K8174Dz53tq24ntzO%2BNTI%2Fn0VRYZnaxx4dWrr25uc7UqWYZ57pssFe%2F0sptbZZm29l7nHcouUELfP&X-Amz-Signature=d6cee66e09fec77183b0db6f93582fe74f475fda09c8ef475bbf524ca5c21f76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z35MHNMI%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxmRzU%2Blp9Y2%2Bokte03Fu3L3rkTETL%2FnS9zg7jpSQ3VwIgHj%2BXqDMTgm%2F78LOfKd8%2BVYMcjUqsCvB7jNggtWcO4nAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhbN6k1MGJUtqEd2SrcA%2B5dC1F4psuAvY8sPJJHZb%2F5E1J79Zu2Var0xwv70waYtEuHjbhFMCA5pbFRYeR3SeiRUSGeJyxTOiPUZZwfQGtc3YvapnxrTRM%2F05KkRIZYuzDrz%2BidFifh0jjTt03DiFa8I7XjmxH9fQI%2B358x1Snj95l0yQ05bsqXE31y8icd1EYCLZUWBwJXr9Gx6znGnDbGAX%2F7Y9sY2ojMY8%2Fjr8mxh2PXXlUrYZu2%2FUtjJ4y644M71TNpTV1WHp5L45D37zAWclIH3K6s1pDDsX%2F4jdHKc9o%2F6lCHFoDdk5HPkfKRrgTakmR%2FDNj1dHFpgZHRR1LktKl58td%2FSeshjizQugfUg%2FgUc%2BQDIQyVVtLX7cwJxqhKX%2F64doA0OGvH6kIFqo06nCG3UWx%2F7SEe%2BKbOjNlIN%2FMvM7c8Kla9z5ZzrDPFX4bo7vA4ZQHy1O%2F8Ggx5MWHU%2B6s5AYU9r2dCulgFTb0eRPm%2FZZIwWHXoeU%2FUW3dkdkGW0i6B2DZvu1PW49cL%2BDZwGWd9UYqXSWLazs6MIKJlSEJw%2FTY%2Be%2FYwfNpM7oK6Bv78tYLD2s%2B14sK7qWhiVq7LgJ9OMl8mhUslOWgDIGIYWgTe8NHObL1l5bmTKpPmxSTTxCAIce4oKRd6MLiH6sgGOqUBZOnj8hs39a0M85MGzEWMAAeLWNL7styiZT3UlFZM%2B7w%2B6sWhCHCtS012m8PM4T6tzMOUiaqqjVIYyIYYhCLVzb%2FIVZHLBxPXY8wXWdXKjvt7fuxOLH0DUYB1QF4U75jrNc0gDkh%2BveSlyd8K8174Dz53tq24ntzO%2BNTI%2Fn0VRYZnaxx4dWrr25uc7UqWYZ57pssFe%2F0sptbZZm29l7nHcouUELfP&X-Amz-Signature=a804fcaca8b0d9c3c0c0aead57febc0cbc51364f0df2268f00d69f96ae878136&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z35MHNMI%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxmRzU%2Blp9Y2%2Bokte03Fu3L3rkTETL%2FnS9zg7jpSQ3VwIgHj%2BXqDMTgm%2F78LOfKd8%2BVYMcjUqsCvB7jNggtWcO4nAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhbN6k1MGJUtqEd2SrcA%2B5dC1F4psuAvY8sPJJHZb%2F5E1J79Zu2Var0xwv70waYtEuHjbhFMCA5pbFRYeR3SeiRUSGeJyxTOiPUZZwfQGtc3YvapnxrTRM%2F05KkRIZYuzDrz%2BidFifh0jjTt03DiFa8I7XjmxH9fQI%2B358x1Snj95l0yQ05bsqXE31y8icd1EYCLZUWBwJXr9Gx6znGnDbGAX%2F7Y9sY2ojMY8%2Fjr8mxh2PXXlUrYZu2%2FUtjJ4y644M71TNpTV1WHp5L45D37zAWclIH3K6s1pDDsX%2F4jdHKc9o%2F6lCHFoDdk5HPkfKRrgTakmR%2FDNj1dHFpgZHRR1LktKl58td%2FSeshjizQugfUg%2FgUc%2BQDIQyVVtLX7cwJxqhKX%2F64doA0OGvH6kIFqo06nCG3UWx%2F7SEe%2BKbOjNlIN%2FMvM7c8Kla9z5ZzrDPFX4bo7vA4ZQHy1O%2F8Ggx5MWHU%2B6s5AYU9r2dCulgFTb0eRPm%2FZZIwWHXoeU%2FUW3dkdkGW0i6B2DZvu1PW49cL%2BDZwGWd9UYqXSWLazs6MIKJlSEJw%2FTY%2Be%2FYwfNpM7oK6Bv78tYLD2s%2B14sK7qWhiVq7LgJ9OMl8mhUslOWgDIGIYWgTe8NHObL1l5bmTKpPmxSTTxCAIce4oKRd6MLiH6sgGOqUBZOnj8hs39a0M85MGzEWMAAeLWNL7styiZT3UlFZM%2B7w%2B6sWhCHCtS012m8PM4T6tzMOUiaqqjVIYyIYYhCLVzb%2FIVZHLBxPXY8wXWdXKjvt7fuxOLH0DUYB1QF4U75jrNc0gDkh%2BveSlyd8K8174Dz53tq24ntzO%2BNTI%2Fn0VRYZnaxx4dWrr25uc7UqWYZ57pssFe%2F0sptbZZm29l7nHcouUELfP&X-Amz-Signature=33bcd36278060633d163688a79267d67257717f5c9def3b8fa50616447ee2cc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z35MHNMI%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxmRzU%2Blp9Y2%2Bokte03Fu3L3rkTETL%2FnS9zg7jpSQ3VwIgHj%2BXqDMTgm%2F78LOfKd8%2BVYMcjUqsCvB7jNggtWcO4nAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhbN6k1MGJUtqEd2SrcA%2B5dC1F4psuAvY8sPJJHZb%2F5E1J79Zu2Var0xwv70waYtEuHjbhFMCA5pbFRYeR3SeiRUSGeJyxTOiPUZZwfQGtc3YvapnxrTRM%2F05KkRIZYuzDrz%2BidFifh0jjTt03DiFa8I7XjmxH9fQI%2B358x1Snj95l0yQ05bsqXE31y8icd1EYCLZUWBwJXr9Gx6znGnDbGAX%2F7Y9sY2ojMY8%2Fjr8mxh2PXXlUrYZu2%2FUtjJ4y644M71TNpTV1WHp5L45D37zAWclIH3K6s1pDDsX%2F4jdHKc9o%2F6lCHFoDdk5HPkfKRrgTakmR%2FDNj1dHFpgZHRR1LktKl58td%2FSeshjizQugfUg%2FgUc%2BQDIQyVVtLX7cwJxqhKX%2F64doA0OGvH6kIFqo06nCG3UWx%2F7SEe%2BKbOjNlIN%2FMvM7c8Kla9z5ZzrDPFX4bo7vA4ZQHy1O%2F8Ggx5MWHU%2B6s5AYU9r2dCulgFTb0eRPm%2FZZIwWHXoeU%2FUW3dkdkGW0i6B2DZvu1PW49cL%2BDZwGWd9UYqXSWLazs6MIKJlSEJw%2FTY%2Be%2FYwfNpM7oK6Bv78tYLD2s%2B14sK7qWhiVq7LgJ9OMl8mhUslOWgDIGIYWgTe8NHObL1l5bmTKpPmxSTTxCAIce4oKRd6MLiH6sgGOqUBZOnj8hs39a0M85MGzEWMAAeLWNL7styiZT3UlFZM%2B7w%2B6sWhCHCtS012m8PM4T6tzMOUiaqqjVIYyIYYhCLVzb%2FIVZHLBxPXY8wXWdXKjvt7fuxOLH0DUYB1QF4U75jrNc0gDkh%2BveSlyd8K8174Dz53tq24ntzO%2BNTI%2Fn0VRYZnaxx4dWrr25uc7UqWYZ57pssFe%2F0sptbZZm29l7nHcouUELfP&X-Amz-Signature=f78dcc44fa82f618138028ccfd1a239011983616257fea88e015fb59e8d17586&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z35MHNMI%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxmRzU%2Blp9Y2%2Bokte03Fu3L3rkTETL%2FnS9zg7jpSQ3VwIgHj%2BXqDMTgm%2F78LOfKd8%2BVYMcjUqsCvB7jNggtWcO4nAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhbN6k1MGJUtqEd2SrcA%2B5dC1F4psuAvY8sPJJHZb%2F5E1J79Zu2Var0xwv70waYtEuHjbhFMCA5pbFRYeR3SeiRUSGeJyxTOiPUZZwfQGtc3YvapnxrTRM%2F05KkRIZYuzDrz%2BidFifh0jjTt03DiFa8I7XjmxH9fQI%2B358x1Snj95l0yQ05bsqXE31y8icd1EYCLZUWBwJXr9Gx6znGnDbGAX%2F7Y9sY2ojMY8%2Fjr8mxh2PXXlUrYZu2%2FUtjJ4y644M71TNpTV1WHp5L45D37zAWclIH3K6s1pDDsX%2F4jdHKc9o%2F6lCHFoDdk5HPkfKRrgTakmR%2FDNj1dHFpgZHRR1LktKl58td%2FSeshjizQugfUg%2FgUc%2BQDIQyVVtLX7cwJxqhKX%2F64doA0OGvH6kIFqo06nCG3UWx%2F7SEe%2BKbOjNlIN%2FMvM7c8Kla9z5ZzrDPFX4bo7vA4ZQHy1O%2F8Ggx5MWHU%2B6s5AYU9r2dCulgFTb0eRPm%2FZZIwWHXoeU%2FUW3dkdkGW0i6B2DZvu1PW49cL%2BDZwGWd9UYqXSWLazs6MIKJlSEJw%2FTY%2Be%2FYwfNpM7oK6Bv78tYLD2s%2B14sK7qWhiVq7LgJ9OMl8mhUslOWgDIGIYWgTe8NHObL1l5bmTKpPmxSTTxCAIce4oKRd6MLiH6sgGOqUBZOnj8hs39a0M85MGzEWMAAeLWNL7styiZT3UlFZM%2B7w%2B6sWhCHCtS012m8PM4T6tzMOUiaqqjVIYyIYYhCLVzb%2FIVZHLBxPXY8wXWdXKjvt7fuxOLH0DUYB1QF4U75jrNc0gDkh%2BveSlyd8K8174Dz53tq24ntzO%2BNTI%2Fn0VRYZnaxx4dWrr25uc7UqWYZ57pssFe%2F0sptbZZm29l7nHcouUELfP&X-Amz-Signature=5609dfaf1b6ad926443732d390b335ddddc6fdc1f1885f073c638f55f6894789&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z35MHNMI%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxmRzU%2Blp9Y2%2Bokte03Fu3L3rkTETL%2FnS9zg7jpSQ3VwIgHj%2BXqDMTgm%2F78LOfKd8%2BVYMcjUqsCvB7jNggtWcO4nAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhbN6k1MGJUtqEd2SrcA%2B5dC1F4psuAvY8sPJJHZb%2F5E1J79Zu2Var0xwv70waYtEuHjbhFMCA5pbFRYeR3SeiRUSGeJyxTOiPUZZwfQGtc3YvapnxrTRM%2F05KkRIZYuzDrz%2BidFifh0jjTt03DiFa8I7XjmxH9fQI%2B358x1Snj95l0yQ05bsqXE31y8icd1EYCLZUWBwJXr9Gx6znGnDbGAX%2F7Y9sY2ojMY8%2Fjr8mxh2PXXlUrYZu2%2FUtjJ4y644M71TNpTV1WHp5L45D37zAWclIH3K6s1pDDsX%2F4jdHKc9o%2F6lCHFoDdk5HPkfKRrgTakmR%2FDNj1dHFpgZHRR1LktKl58td%2FSeshjizQugfUg%2FgUc%2BQDIQyVVtLX7cwJxqhKX%2F64doA0OGvH6kIFqo06nCG3UWx%2F7SEe%2BKbOjNlIN%2FMvM7c8Kla9z5ZzrDPFX4bo7vA4ZQHy1O%2F8Ggx5MWHU%2B6s5AYU9r2dCulgFTb0eRPm%2FZZIwWHXoeU%2FUW3dkdkGW0i6B2DZvu1PW49cL%2BDZwGWd9UYqXSWLazs6MIKJlSEJw%2FTY%2Be%2FYwfNpM7oK6Bv78tYLD2s%2B14sK7qWhiVq7LgJ9OMl8mhUslOWgDIGIYWgTe8NHObL1l5bmTKpPmxSTTxCAIce4oKRd6MLiH6sgGOqUBZOnj8hs39a0M85MGzEWMAAeLWNL7styiZT3UlFZM%2B7w%2B6sWhCHCtS012m8PM4T6tzMOUiaqqjVIYyIYYhCLVzb%2FIVZHLBxPXY8wXWdXKjvt7fuxOLH0DUYB1QF4U75jrNc0gDkh%2BveSlyd8K8174Dz53tq24ntzO%2BNTI%2Fn0VRYZnaxx4dWrr25uc7UqWYZ57pssFe%2F0sptbZZm29l7nHcouUELfP&X-Amz-Signature=7dc26ce1d4832eaf141d3fd1ef69f165d41118e477dce6e38b02bf1fd0b6010c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z35MHNMI%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxmRzU%2Blp9Y2%2Bokte03Fu3L3rkTETL%2FnS9zg7jpSQ3VwIgHj%2BXqDMTgm%2F78LOfKd8%2BVYMcjUqsCvB7jNggtWcO4nAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhbN6k1MGJUtqEd2SrcA%2B5dC1F4psuAvY8sPJJHZb%2F5E1J79Zu2Var0xwv70waYtEuHjbhFMCA5pbFRYeR3SeiRUSGeJyxTOiPUZZwfQGtc3YvapnxrTRM%2F05KkRIZYuzDrz%2BidFifh0jjTt03DiFa8I7XjmxH9fQI%2B358x1Snj95l0yQ05bsqXE31y8icd1EYCLZUWBwJXr9Gx6znGnDbGAX%2F7Y9sY2ojMY8%2Fjr8mxh2PXXlUrYZu2%2FUtjJ4y644M71TNpTV1WHp5L45D37zAWclIH3K6s1pDDsX%2F4jdHKc9o%2F6lCHFoDdk5HPkfKRrgTakmR%2FDNj1dHFpgZHRR1LktKl58td%2FSeshjizQugfUg%2FgUc%2BQDIQyVVtLX7cwJxqhKX%2F64doA0OGvH6kIFqo06nCG3UWx%2F7SEe%2BKbOjNlIN%2FMvM7c8Kla9z5ZzrDPFX4bo7vA4ZQHy1O%2F8Ggx5MWHU%2B6s5AYU9r2dCulgFTb0eRPm%2FZZIwWHXoeU%2FUW3dkdkGW0i6B2DZvu1PW49cL%2BDZwGWd9UYqXSWLazs6MIKJlSEJw%2FTY%2Be%2FYwfNpM7oK6Bv78tYLD2s%2B14sK7qWhiVq7LgJ9OMl8mhUslOWgDIGIYWgTe8NHObL1l5bmTKpPmxSTTxCAIce4oKRd6MLiH6sgGOqUBZOnj8hs39a0M85MGzEWMAAeLWNL7styiZT3UlFZM%2B7w%2B6sWhCHCtS012m8PM4T6tzMOUiaqqjVIYyIYYhCLVzb%2FIVZHLBxPXY8wXWdXKjvt7fuxOLH0DUYB1QF4U75jrNc0gDkh%2BveSlyd8K8174Dz53tq24ntzO%2BNTI%2Fn0VRYZnaxx4dWrr25uc7UqWYZ57pssFe%2F0sptbZZm29l7nHcouUELfP&X-Amz-Signature=0e89628786bb58da88788f573548e4033c29e8709fb6aee7cb4c34c6c8e0aafc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z35MHNMI%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxmRzU%2Blp9Y2%2Bokte03Fu3L3rkTETL%2FnS9zg7jpSQ3VwIgHj%2BXqDMTgm%2F78LOfKd8%2BVYMcjUqsCvB7jNggtWcO4nAqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhbN6k1MGJUtqEd2SrcA%2B5dC1F4psuAvY8sPJJHZb%2F5E1J79Zu2Var0xwv70waYtEuHjbhFMCA5pbFRYeR3SeiRUSGeJyxTOiPUZZwfQGtc3YvapnxrTRM%2F05KkRIZYuzDrz%2BidFifh0jjTt03DiFa8I7XjmxH9fQI%2B358x1Snj95l0yQ05bsqXE31y8icd1EYCLZUWBwJXr9Gx6znGnDbGAX%2F7Y9sY2ojMY8%2Fjr8mxh2PXXlUrYZu2%2FUtjJ4y644M71TNpTV1WHp5L45D37zAWclIH3K6s1pDDsX%2F4jdHKc9o%2F6lCHFoDdk5HPkfKRrgTakmR%2FDNj1dHFpgZHRR1LktKl58td%2FSeshjizQugfUg%2FgUc%2BQDIQyVVtLX7cwJxqhKX%2F64doA0OGvH6kIFqo06nCG3UWx%2F7SEe%2BKbOjNlIN%2FMvM7c8Kla9z5ZzrDPFX4bo7vA4ZQHy1O%2F8Ggx5MWHU%2B6s5AYU9r2dCulgFTb0eRPm%2FZZIwWHXoeU%2FUW3dkdkGW0i6B2DZvu1PW49cL%2BDZwGWd9UYqXSWLazs6MIKJlSEJw%2FTY%2Be%2FYwfNpM7oK6Bv78tYLD2s%2B14sK7qWhiVq7LgJ9OMl8mhUslOWgDIGIYWgTe8NHObL1l5bmTKpPmxSTTxCAIce4oKRd6MLiH6sgGOqUBZOnj8hs39a0M85MGzEWMAAeLWNL7styiZT3UlFZM%2B7w%2B6sWhCHCtS012m8PM4T6tzMOUiaqqjVIYyIYYhCLVzb%2FIVZHLBxPXY8wXWdXKjvt7fuxOLH0DUYB1QF4U75jrNc0gDkh%2BveSlyd8K8174Dz53tq24ntzO%2BNTI%2Fn0VRYZnaxx4dWrr25uc7UqWYZ57pssFe%2F0sptbZZm29l7nHcouUELfP&X-Amz-Signature=ee3b18934ee6357f8ec8ad4a0211de533499a68c4913bebdefc97b087010af90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

