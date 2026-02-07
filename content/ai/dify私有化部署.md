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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYI6PDM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQG99j4rcuCvGi1ugNx03%2FvtpNX5xNL9MlVGsCF7RLcAiEAhV4nGV9O8B7fZqFoANTBSmD2%2FwM6IxQ1zwUoIb69xqkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMphEa8u6vVZ2oJruircA475X30GdXKl3KBXfdb82OUlv5FHgjbhE1WxkMzfvh0EzoIlmQVWvu6Fxecq6vTcOaSNR62l4uzwLvVOrnWMo%2FL%2FseOwUzHj0o2BhIyrsm05pNJtdEGnotx3I%2B%2FVfGWeYH5qLfvenPjTTum8cGS5m6F7ZSwbK0aPvKy%2BHU5T7%2F8P1jF2%2B%2BqGctkBzHeqNrTg%2BxouDp1nwwoysU3jadzsxuieLnNpDVoX33K%2BrugjeL5LpKuY0sfgdtWc1eEIa6j%2BPSYRqa9zd7HmRY%2FsbDcyXlVYj7nE4N%2FTcFg56t%2FrrGSpla%2FvI%2BGmxfWkIL%2BkbsmPDGCYg6XtSBHwK1vyz%2B1hMoOhr4yaqtEPEYCskzbQMJg4TaaQbcYleBFeAw%2FuE9DoZxLpWe5101nXyaWqNhUC7%2Bi%2F1dIKP%2FEKMAygJYLq2syXmDBQ9ymu1DXfbmwPsSuMEnanhj7aIYi3iSOGIVS1IFTZKr%2FFiEdR2nIjZxGTC2NOfTwO6Dt0LUDjkxfN2Xjtq2C6ikN700uUsM8p56aZZK8mt9sudwUR%2BsGvCPbugmVHgIa0iQrKGFTilEHhcIejYqPPGMrEHUrnGE2sNtCowOe3upHvO6BgYsVKlcaxGgDammARJvFshoJWRpjPMJDEmswGOqUB6iW%2BHeltF2UUNeII2JGcXDjtziN5o224r%2F37mfNTJVDCg%2F2UXxlKH4ySmw8M6oLXpPC%2BWXLhdgGDbJSrtAbMlCHf3NFs3C0QouKPBVG2pMLv0ZMjAvsOaPprWN4ppCCqmAK3vDOoKL7zeZjxo0PhBNx3ct0rA4Vnts5sFfMEX7Ae4K9lbvDBLFMDl0iJgtOoysR%2BNM3hEBLTZsaBk8NmQTwmaUFV&X-Amz-Signature=6735093506241fa37843638eceace142af33f86fb4fdb85af04dc87d0831f6a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYI6PDM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQG99j4rcuCvGi1ugNx03%2FvtpNX5xNL9MlVGsCF7RLcAiEAhV4nGV9O8B7fZqFoANTBSmD2%2FwM6IxQ1zwUoIb69xqkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMphEa8u6vVZ2oJruircA475X30GdXKl3KBXfdb82OUlv5FHgjbhE1WxkMzfvh0EzoIlmQVWvu6Fxecq6vTcOaSNR62l4uzwLvVOrnWMo%2FL%2FseOwUzHj0o2BhIyrsm05pNJtdEGnotx3I%2B%2FVfGWeYH5qLfvenPjTTum8cGS5m6F7ZSwbK0aPvKy%2BHU5T7%2F8P1jF2%2B%2BqGctkBzHeqNrTg%2BxouDp1nwwoysU3jadzsxuieLnNpDVoX33K%2BrugjeL5LpKuY0sfgdtWc1eEIa6j%2BPSYRqa9zd7HmRY%2FsbDcyXlVYj7nE4N%2FTcFg56t%2FrrGSpla%2FvI%2BGmxfWkIL%2BkbsmPDGCYg6XtSBHwK1vyz%2B1hMoOhr4yaqtEPEYCskzbQMJg4TaaQbcYleBFeAw%2FuE9DoZxLpWe5101nXyaWqNhUC7%2Bi%2F1dIKP%2FEKMAygJYLq2syXmDBQ9ymu1DXfbmwPsSuMEnanhj7aIYi3iSOGIVS1IFTZKr%2FFiEdR2nIjZxGTC2NOfTwO6Dt0LUDjkxfN2Xjtq2C6ikN700uUsM8p56aZZK8mt9sudwUR%2BsGvCPbugmVHgIa0iQrKGFTilEHhcIejYqPPGMrEHUrnGE2sNtCowOe3upHvO6BgYsVKlcaxGgDammARJvFshoJWRpjPMJDEmswGOqUB6iW%2BHeltF2UUNeII2JGcXDjtziN5o224r%2F37mfNTJVDCg%2F2UXxlKH4ySmw8M6oLXpPC%2BWXLhdgGDbJSrtAbMlCHf3NFs3C0QouKPBVG2pMLv0ZMjAvsOaPprWN4ppCCqmAK3vDOoKL7zeZjxo0PhBNx3ct0rA4Vnts5sFfMEX7Ae4K9lbvDBLFMDl0iJgtOoysR%2BNM3hEBLTZsaBk8NmQTwmaUFV&X-Amz-Signature=6128ba32d37e50dd266f90c32d2d7331e83bfa7dc13e8e00df4b09003c4a2be3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYI6PDM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQG99j4rcuCvGi1ugNx03%2FvtpNX5xNL9MlVGsCF7RLcAiEAhV4nGV9O8B7fZqFoANTBSmD2%2FwM6IxQ1zwUoIb69xqkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMphEa8u6vVZ2oJruircA475X30GdXKl3KBXfdb82OUlv5FHgjbhE1WxkMzfvh0EzoIlmQVWvu6Fxecq6vTcOaSNR62l4uzwLvVOrnWMo%2FL%2FseOwUzHj0o2BhIyrsm05pNJtdEGnotx3I%2B%2FVfGWeYH5qLfvenPjTTum8cGS5m6F7ZSwbK0aPvKy%2BHU5T7%2F8P1jF2%2B%2BqGctkBzHeqNrTg%2BxouDp1nwwoysU3jadzsxuieLnNpDVoX33K%2BrugjeL5LpKuY0sfgdtWc1eEIa6j%2BPSYRqa9zd7HmRY%2FsbDcyXlVYj7nE4N%2FTcFg56t%2FrrGSpla%2FvI%2BGmxfWkIL%2BkbsmPDGCYg6XtSBHwK1vyz%2B1hMoOhr4yaqtEPEYCskzbQMJg4TaaQbcYleBFeAw%2FuE9DoZxLpWe5101nXyaWqNhUC7%2Bi%2F1dIKP%2FEKMAygJYLq2syXmDBQ9ymu1DXfbmwPsSuMEnanhj7aIYi3iSOGIVS1IFTZKr%2FFiEdR2nIjZxGTC2NOfTwO6Dt0LUDjkxfN2Xjtq2C6ikN700uUsM8p56aZZK8mt9sudwUR%2BsGvCPbugmVHgIa0iQrKGFTilEHhcIejYqPPGMrEHUrnGE2sNtCowOe3upHvO6BgYsVKlcaxGgDammARJvFshoJWRpjPMJDEmswGOqUB6iW%2BHeltF2UUNeII2JGcXDjtziN5o224r%2F37mfNTJVDCg%2F2UXxlKH4ySmw8M6oLXpPC%2BWXLhdgGDbJSrtAbMlCHf3NFs3C0QouKPBVG2pMLv0ZMjAvsOaPprWN4ppCCqmAK3vDOoKL7zeZjxo0PhBNx3ct0rA4Vnts5sFfMEX7Ae4K9lbvDBLFMDl0iJgtOoysR%2BNM3hEBLTZsaBk8NmQTwmaUFV&X-Amz-Signature=c92cd10a988fb83ebd75d0ddb7fa97f66f575c208925a0a653e08db3426cdbad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYI6PDM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQG99j4rcuCvGi1ugNx03%2FvtpNX5xNL9MlVGsCF7RLcAiEAhV4nGV9O8B7fZqFoANTBSmD2%2FwM6IxQ1zwUoIb69xqkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMphEa8u6vVZ2oJruircA475X30GdXKl3KBXfdb82OUlv5FHgjbhE1WxkMzfvh0EzoIlmQVWvu6Fxecq6vTcOaSNR62l4uzwLvVOrnWMo%2FL%2FseOwUzHj0o2BhIyrsm05pNJtdEGnotx3I%2B%2FVfGWeYH5qLfvenPjTTum8cGS5m6F7ZSwbK0aPvKy%2BHU5T7%2F8P1jF2%2B%2BqGctkBzHeqNrTg%2BxouDp1nwwoysU3jadzsxuieLnNpDVoX33K%2BrugjeL5LpKuY0sfgdtWc1eEIa6j%2BPSYRqa9zd7HmRY%2FsbDcyXlVYj7nE4N%2FTcFg56t%2FrrGSpla%2FvI%2BGmxfWkIL%2BkbsmPDGCYg6XtSBHwK1vyz%2B1hMoOhr4yaqtEPEYCskzbQMJg4TaaQbcYleBFeAw%2FuE9DoZxLpWe5101nXyaWqNhUC7%2Bi%2F1dIKP%2FEKMAygJYLq2syXmDBQ9ymu1DXfbmwPsSuMEnanhj7aIYi3iSOGIVS1IFTZKr%2FFiEdR2nIjZxGTC2NOfTwO6Dt0LUDjkxfN2Xjtq2C6ikN700uUsM8p56aZZK8mt9sudwUR%2BsGvCPbugmVHgIa0iQrKGFTilEHhcIejYqPPGMrEHUrnGE2sNtCowOe3upHvO6BgYsVKlcaxGgDammARJvFshoJWRpjPMJDEmswGOqUB6iW%2BHeltF2UUNeII2JGcXDjtziN5o224r%2F37mfNTJVDCg%2F2UXxlKH4ySmw8M6oLXpPC%2BWXLhdgGDbJSrtAbMlCHf3NFs3C0QouKPBVG2pMLv0ZMjAvsOaPprWN4ppCCqmAK3vDOoKL7zeZjxo0PhBNx3ct0rA4Vnts5sFfMEX7Ae4K9lbvDBLFMDl0iJgtOoysR%2BNM3hEBLTZsaBk8NmQTwmaUFV&X-Amz-Signature=99d9c5a6b819f856c9efda39fe49f7b596f35f5de68561d27034530c38534cc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYI6PDM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQG99j4rcuCvGi1ugNx03%2FvtpNX5xNL9MlVGsCF7RLcAiEAhV4nGV9O8B7fZqFoANTBSmD2%2FwM6IxQ1zwUoIb69xqkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMphEa8u6vVZ2oJruircA475X30GdXKl3KBXfdb82OUlv5FHgjbhE1WxkMzfvh0EzoIlmQVWvu6Fxecq6vTcOaSNR62l4uzwLvVOrnWMo%2FL%2FseOwUzHj0o2BhIyrsm05pNJtdEGnotx3I%2B%2FVfGWeYH5qLfvenPjTTum8cGS5m6F7ZSwbK0aPvKy%2BHU5T7%2F8P1jF2%2B%2BqGctkBzHeqNrTg%2BxouDp1nwwoysU3jadzsxuieLnNpDVoX33K%2BrugjeL5LpKuY0sfgdtWc1eEIa6j%2BPSYRqa9zd7HmRY%2FsbDcyXlVYj7nE4N%2FTcFg56t%2FrrGSpla%2FvI%2BGmxfWkIL%2BkbsmPDGCYg6XtSBHwK1vyz%2B1hMoOhr4yaqtEPEYCskzbQMJg4TaaQbcYleBFeAw%2FuE9DoZxLpWe5101nXyaWqNhUC7%2Bi%2F1dIKP%2FEKMAygJYLq2syXmDBQ9ymu1DXfbmwPsSuMEnanhj7aIYi3iSOGIVS1IFTZKr%2FFiEdR2nIjZxGTC2NOfTwO6Dt0LUDjkxfN2Xjtq2C6ikN700uUsM8p56aZZK8mt9sudwUR%2BsGvCPbugmVHgIa0iQrKGFTilEHhcIejYqPPGMrEHUrnGE2sNtCowOe3upHvO6BgYsVKlcaxGgDammARJvFshoJWRpjPMJDEmswGOqUB6iW%2BHeltF2UUNeII2JGcXDjtziN5o224r%2F37mfNTJVDCg%2F2UXxlKH4ySmw8M6oLXpPC%2BWXLhdgGDbJSrtAbMlCHf3NFs3C0QouKPBVG2pMLv0ZMjAvsOaPprWN4ppCCqmAK3vDOoKL7zeZjxo0PhBNx3ct0rA4Vnts5sFfMEX7Ae4K9lbvDBLFMDl0iJgtOoysR%2BNM3hEBLTZsaBk8NmQTwmaUFV&X-Amz-Signature=afeefa60cab3a84baed230d34f8c2b72b4c4a0998848d8917952294c0f88adc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYI6PDM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQG99j4rcuCvGi1ugNx03%2FvtpNX5xNL9MlVGsCF7RLcAiEAhV4nGV9O8B7fZqFoANTBSmD2%2FwM6IxQ1zwUoIb69xqkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMphEa8u6vVZ2oJruircA475X30GdXKl3KBXfdb82OUlv5FHgjbhE1WxkMzfvh0EzoIlmQVWvu6Fxecq6vTcOaSNR62l4uzwLvVOrnWMo%2FL%2FseOwUzHj0o2BhIyrsm05pNJtdEGnotx3I%2B%2FVfGWeYH5qLfvenPjTTum8cGS5m6F7ZSwbK0aPvKy%2BHU5T7%2F8P1jF2%2B%2BqGctkBzHeqNrTg%2BxouDp1nwwoysU3jadzsxuieLnNpDVoX33K%2BrugjeL5LpKuY0sfgdtWc1eEIa6j%2BPSYRqa9zd7HmRY%2FsbDcyXlVYj7nE4N%2FTcFg56t%2FrrGSpla%2FvI%2BGmxfWkIL%2BkbsmPDGCYg6XtSBHwK1vyz%2B1hMoOhr4yaqtEPEYCskzbQMJg4TaaQbcYleBFeAw%2FuE9DoZxLpWe5101nXyaWqNhUC7%2Bi%2F1dIKP%2FEKMAygJYLq2syXmDBQ9ymu1DXfbmwPsSuMEnanhj7aIYi3iSOGIVS1IFTZKr%2FFiEdR2nIjZxGTC2NOfTwO6Dt0LUDjkxfN2Xjtq2C6ikN700uUsM8p56aZZK8mt9sudwUR%2BsGvCPbugmVHgIa0iQrKGFTilEHhcIejYqPPGMrEHUrnGE2sNtCowOe3upHvO6BgYsVKlcaxGgDammARJvFshoJWRpjPMJDEmswGOqUB6iW%2BHeltF2UUNeII2JGcXDjtziN5o224r%2F37mfNTJVDCg%2F2UXxlKH4ySmw8M6oLXpPC%2BWXLhdgGDbJSrtAbMlCHf3NFs3C0QouKPBVG2pMLv0ZMjAvsOaPprWN4ppCCqmAK3vDOoKL7zeZjxo0PhBNx3ct0rA4Vnts5sFfMEX7Ae4K9lbvDBLFMDl0iJgtOoysR%2BNM3hEBLTZsaBk8NmQTwmaUFV&X-Amz-Signature=11f34cb2ebd16d9e0275b2c8807931c6538669cb9eb07ec101d24fde775f25c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYI6PDM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQG99j4rcuCvGi1ugNx03%2FvtpNX5xNL9MlVGsCF7RLcAiEAhV4nGV9O8B7fZqFoANTBSmD2%2FwM6IxQ1zwUoIb69xqkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMphEa8u6vVZ2oJruircA475X30GdXKl3KBXfdb82OUlv5FHgjbhE1WxkMzfvh0EzoIlmQVWvu6Fxecq6vTcOaSNR62l4uzwLvVOrnWMo%2FL%2FseOwUzHj0o2BhIyrsm05pNJtdEGnotx3I%2B%2FVfGWeYH5qLfvenPjTTum8cGS5m6F7ZSwbK0aPvKy%2BHU5T7%2F8P1jF2%2B%2BqGctkBzHeqNrTg%2BxouDp1nwwoysU3jadzsxuieLnNpDVoX33K%2BrugjeL5LpKuY0sfgdtWc1eEIa6j%2BPSYRqa9zd7HmRY%2FsbDcyXlVYj7nE4N%2FTcFg56t%2FrrGSpla%2FvI%2BGmxfWkIL%2BkbsmPDGCYg6XtSBHwK1vyz%2B1hMoOhr4yaqtEPEYCskzbQMJg4TaaQbcYleBFeAw%2FuE9DoZxLpWe5101nXyaWqNhUC7%2Bi%2F1dIKP%2FEKMAygJYLq2syXmDBQ9ymu1DXfbmwPsSuMEnanhj7aIYi3iSOGIVS1IFTZKr%2FFiEdR2nIjZxGTC2NOfTwO6Dt0LUDjkxfN2Xjtq2C6ikN700uUsM8p56aZZK8mt9sudwUR%2BsGvCPbugmVHgIa0iQrKGFTilEHhcIejYqPPGMrEHUrnGE2sNtCowOe3upHvO6BgYsVKlcaxGgDammARJvFshoJWRpjPMJDEmswGOqUB6iW%2BHeltF2UUNeII2JGcXDjtziN5o224r%2F37mfNTJVDCg%2F2UXxlKH4ySmw8M6oLXpPC%2BWXLhdgGDbJSrtAbMlCHf3NFs3C0QouKPBVG2pMLv0ZMjAvsOaPprWN4ppCCqmAK3vDOoKL7zeZjxo0PhBNx3ct0rA4Vnts5sFfMEX7Ae4K9lbvDBLFMDl0iJgtOoysR%2BNM3hEBLTZsaBk8NmQTwmaUFV&X-Amz-Signature=640c8e5adda377f8beb7524d7674df65706bee61856430e604729dc0c8bc5761&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYI6PDM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQG99j4rcuCvGi1ugNx03%2FvtpNX5xNL9MlVGsCF7RLcAiEAhV4nGV9O8B7fZqFoANTBSmD2%2FwM6IxQ1zwUoIb69xqkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMphEa8u6vVZ2oJruircA475X30GdXKl3KBXfdb82OUlv5FHgjbhE1WxkMzfvh0EzoIlmQVWvu6Fxecq6vTcOaSNR62l4uzwLvVOrnWMo%2FL%2FseOwUzHj0o2BhIyrsm05pNJtdEGnotx3I%2B%2FVfGWeYH5qLfvenPjTTum8cGS5m6F7ZSwbK0aPvKy%2BHU5T7%2F8P1jF2%2B%2BqGctkBzHeqNrTg%2BxouDp1nwwoysU3jadzsxuieLnNpDVoX33K%2BrugjeL5LpKuY0sfgdtWc1eEIa6j%2BPSYRqa9zd7HmRY%2FsbDcyXlVYj7nE4N%2FTcFg56t%2FrrGSpla%2FvI%2BGmxfWkIL%2BkbsmPDGCYg6XtSBHwK1vyz%2B1hMoOhr4yaqtEPEYCskzbQMJg4TaaQbcYleBFeAw%2FuE9DoZxLpWe5101nXyaWqNhUC7%2Bi%2F1dIKP%2FEKMAygJYLq2syXmDBQ9ymu1DXfbmwPsSuMEnanhj7aIYi3iSOGIVS1IFTZKr%2FFiEdR2nIjZxGTC2NOfTwO6Dt0LUDjkxfN2Xjtq2C6ikN700uUsM8p56aZZK8mt9sudwUR%2BsGvCPbugmVHgIa0iQrKGFTilEHhcIejYqPPGMrEHUrnGE2sNtCowOe3upHvO6BgYsVKlcaxGgDammARJvFshoJWRpjPMJDEmswGOqUB6iW%2BHeltF2UUNeII2JGcXDjtziN5o224r%2F37mfNTJVDCg%2F2UXxlKH4ySmw8M6oLXpPC%2BWXLhdgGDbJSrtAbMlCHf3NFs3C0QouKPBVG2pMLv0ZMjAvsOaPprWN4ppCCqmAK3vDOoKL7zeZjxo0PhBNx3ct0rA4Vnts5sFfMEX7Ae4K9lbvDBLFMDl0iJgtOoysR%2BNM3hEBLTZsaBk8NmQTwmaUFV&X-Amz-Signature=bc3b4b49b6a25bb5dbad72f80fab513ef65d82a3c9df2e5b38c396e755798b0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYI6PDM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQG99j4rcuCvGi1ugNx03%2FvtpNX5xNL9MlVGsCF7RLcAiEAhV4nGV9O8B7fZqFoANTBSmD2%2FwM6IxQ1zwUoIb69xqkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMphEa8u6vVZ2oJruircA475X30GdXKl3KBXfdb82OUlv5FHgjbhE1WxkMzfvh0EzoIlmQVWvu6Fxecq6vTcOaSNR62l4uzwLvVOrnWMo%2FL%2FseOwUzHj0o2BhIyrsm05pNJtdEGnotx3I%2B%2FVfGWeYH5qLfvenPjTTum8cGS5m6F7ZSwbK0aPvKy%2BHU5T7%2F8P1jF2%2B%2BqGctkBzHeqNrTg%2BxouDp1nwwoysU3jadzsxuieLnNpDVoX33K%2BrugjeL5LpKuY0sfgdtWc1eEIa6j%2BPSYRqa9zd7HmRY%2FsbDcyXlVYj7nE4N%2FTcFg56t%2FrrGSpla%2FvI%2BGmxfWkIL%2BkbsmPDGCYg6XtSBHwK1vyz%2B1hMoOhr4yaqtEPEYCskzbQMJg4TaaQbcYleBFeAw%2FuE9DoZxLpWe5101nXyaWqNhUC7%2Bi%2F1dIKP%2FEKMAygJYLq2syXmDBQ9ymu1DXfbmwPsSuMEnanhj7aIYi3iSOGIVS1IFTZKr%2FFiEdR2nIjZxGTC2NOfTwO6Dt0LUDjkxfN2Xjtq2C6ikN700uUsM8p56aZZK8mt9sudwUR%2BsGvCPbugmVHgIa0iQrKGFTilEHhcIejYqPPGMrEHUrnGE2sNtCowOe3upHvO6BgYsVKlcaxGgDammARJvFshoJWRpjPMJDEmswGOqUB6iW%2BHeltF2UUNeII2JGcXDjtziN5o224r%2F37mfNTJVDCg%2F2UXxlKH4ySmw8M6oLXpPC%2BWXLhdgGDbJSrtAbMlCHf3NFs3C0QouKPBVG2pMLv0ZMjAvsOaPprWN4ppCCqmAK3vDOoKL7zeZjxo0PhBNx3ct0rA4Vnts5sFfMEX7Ae4K9lbvDBLFMDl0iJgtOoysR%2BNM3hEBLTZsaBk8NmQTwmaUFV&X-Amz-Signature=a599b9cdcc232288ff104324c1588326c6a8314b9cbe97d20d05878d199bb95a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYI6PDM%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQG99j4rcuCvGi1ugNx03%2FvtpNX5xNL9MlVGsCF7RLcAiEAhV4nGV9O8B7fZqFoANTBSmD2%2FwM6IxQ1zwUoIb69xqkq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDMphEa8u6vVZ2oJruircA475X30GdXKl3KBXfdb82OUlv5FHgjbhE1WxkMzfvh0EzoIlmQVWvu6Fxecq6vTcOaSNR62l4uzwLvVOrnWMo%2FL%2FseOwUzHj0o2BhIyrsm05pNJtdEGnotx3I%2B%2FVfGWeYH5qLfvenPjTTum8cGS5m6F7ZSwbK0aPvKy%2BHU5T7%2F8P1jF2%2B%2BqGctkBzHeqNrTg%2BxouDp1nwwoysU3jadzsxuieLnNpDVoX33K%2BrugjeL5LpKuY0sfgdtWc1eEIa6j%2BPSYRqa9zd7HmRY%2FsbDcyXlVYj7nE4N%2FTcFg56t%2FrrGSpla%2FvI%2BGmxfWkIL%2BkbsmPDGCYg6XtSBHwK1vyz%2B1hMoOhr4yaqtEPEYCskzbQMJg4TaaQbcYleBFeAw%2FuE9DoZxLpWe5101nXyaWqNhUC7%2Bi%2F1dIKP%2FEKMAygJYLq2syXmDBQ9ymu1DXfbmwPsSuMEnanhj7aIYi3iSOGIVS1IFTZKr%2FFiEdR2nIjZxGTC2NOfTwO6Dt0LUDjkxfN2Xjtq2C6ikN700uUsM8p56aZZK8mt9sudwUR%2BsGvCPbugmVHgIa0iQrKGFTilEHhcIejYqPPGMrEHUrnGE2sNtCowOe3upHvO6BgYsVKlcaxGgDammARJvFshoJWRpjPMJDEmswGOqUB6iW%2BHeltF2UUNeII2JGcXDjtziN5o224r%2F37mfNTJVDCg%2F2UXxlKH4ySmw8M6oLXpPC%2BWXLhdgGDbJSrtAbMlCHf3NFs3C0QouKPBVG2pMLv0ZMjAvsOaPprWN4ppCCqmAK3vDOoKL7zeZjxo0PhBNx3ct0rA4Vnts5sFfMEX7Ae4K9lbvDBLFMDl0iJgtOoysR%2BNM3hEBLTZsaBk8NmQTwmaUFV&X-Amz-Signature=92ff8e1ad1f17eda0339cac347bb4cec65b14a82dda65ce72866baadc743ffd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

