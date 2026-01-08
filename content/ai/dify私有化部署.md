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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K7BJDM3%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs7GSYvwb3XN2LAfaisFP166Mtb9z%2FUFgsJvpVbNHMoQIgVvbP%2FXAUNwh2klgcoouDzN1TM5RBPsW6cOY4NXasC5YqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz22Wp7AzpPJlQedCrcA8yLHbQ%2FEzE1SApsdzh6w36SmrHu%2FkD8uUI9Tc2s4NfdleyELnlckqgv%2BWwjpCras3%2BJSwgdbDVKGPUVFKaaHg3TdLo%2BIGvH8u%2BXRvcWcdXVjCQ38vwVk1OyYOH7KVdCDNgVM0XuhEUCy282fMgL0CmYx0JqU5xiZed7%2Bk1LjI%2B%2FBjE4UkvCjjl6zZ9irccC15nwinmz%2BNCUFkLTuvjPySGxN9DdZ%2FXkOPK7xCmlWC%2FJ%2FZ3JPDdmeWDOsjVNtuk9pGgfSMPcmjWAcKD3xYw0%2FCrzdLSpVN9qKgwHvMpYihfwD%2FW2AH1yNJM4cJaorStrGglKMsF9cGPcpcbE4aHN4O%2F049%2FM7MX%2FSLD0YC%2FoMJ25P80RZ1BNdaEcrYZ1k3l6c6YB3OLLM0jP1zhmbry0%2Bq5yFL1h%2BRfkzxSr6whxC%2Fk2Ig1jletS8iwJij4cuwQ0aAlnrNpbRIQCyYihbvbwmQX22rTyZ7Lu4KaIljkZBGpQ48QTCwC9Rtj9NaUu2tJdG9eeloWwe0KXkrqBQljYr1AhbTp9sxITGhpQ%2BZTSgrye6bXMyrQTQyPecXyRTvKtPVwtT5o9pyGEswr%2BqcNK%2FmI7PigFaIu8mZE56wD1fMMcvFWicV9to%2FYSN%2FFBMOOo%2FMoGOqUB439JQAopKFnzaYC1Evc8hyTPaBMncoBo4pY4oS4pPLx%2FzdnIrhzZTPbajYIGldrBcM4%2F23H%2FuG%2B1GKIAJ6Xi0Q%2FEroIwBnIaUNneyO%2BeKH7M5jwO%2FKl%2FjwE5af3kU%2FZBNK9qE9xnSl2t%2FfxbSphEBknv9lv7noPW2hB%2B1O%2BwSqUPQjJ%2Bs6l%2BL9us4M5RHvqsNCYAA9M%2BiBkhmGERx6E0BeEfzDuq&X-Amz-Signature=3eaa0933a2bcdab124aada44e417e614a25bf628b6b9b3b916b04e8c0c79f6c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K7BJDM3%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs7GSYvwb3XN2LAfaisFP166Mtb9z%2FUFgsJvpVbNHMoQIgVvbP%2FXAUNwh2klgcoouDzN1TM5RBPsW6cOY4NXasC5YqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz22Wp7AzpPJlQedCrcA8yLHbQ%2FEzE1SApsdzh6w36SmrHu%2FkD8uUI9Tc2s4NfdleyELnlckqgv%2BWwjpCras3%2BJSwgdbDVKGPUVFKaaHg3TdLo%2BIGvH8u%2BXRvcWcdXVjCQ38vwVk1OyYOH7KVdCDNgVM0XuhEUCy282fMgL0CmYx0JqU5xiZed7%2Bk1LjI%2B%2FBjE4UkvCjjl6zZ9irccC15nwinmz%2BNCUFkLTuvjPySGxN9DdZ%2FXkOPK7xCmlWC%2FJ%2FZ3JPDdmeWDOsjVNtuk9pGgfSMPcmjWAcKD3xYw0%2FCrzdLSpVN9qKgwHvMpYihfwD%2FW2AH1yNJM4cJaorStrGglKMsF9cGPcpcbE4aHN4O%2F049%2FM7MX%2FSLD0YC%2FoMJ25P80RZ1BNdaEcrYZ1k3l6c6YB3OLLM0jP1zhmbry0%2Bq5yFL1h%2BRfkzxSr6whxC%2Fk2Ig1jletS8iwJij4cuwQ0aAlnrNpbRIQCyYihbvbwmQX22rTyZ7Lu4KaIljkZBGpQ48QTCwC9Rtj9NaUu2tJdG9eeloWwe0KXkrqBQljYr1AhbTp9sxITGhpQ%2BZTSgrye6bXMyrQTQyPecXyRTvKtPVwtT5o9pyGEswr%2BqcNK%2FmI7PigFaIu8mZE56wD1fMMcvFWicV9to%2FYSN%2FFBMOOo%2FMoGOqUB439JQAopKFnzaYC1Evc8hyTPaBMncoBo4pY4oS4pPLx%2FzdnIrhzZTPbajYIGldrBcM4%2F23H%2FuG%2B1GKIAJ6Xi0Q%2FEroIwBnIaUNneyO%2BeKH7M5jwO%2FKl%2FjwE5af3kU%2FZBNK9qE9xnSl2t%2FfxbSphEBknv9lv7noPW2hB%2B1O%2BwSqUPQjJ%2Bs6l%2BL9us4M5RHvqsNCYAA9M%2BiBkhmGERx6E0BeEfzDuq&X-Amz-Signature=4b7f8c50d2ffed778ede7ac94b5822b2cd4f1d05b4c43df1c445242bd3d66367&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K7BJDM3%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs7GSYvwb3XN2LAfaisFP166Mtb9z%2FUFgsJvpVbNHMoQIgVvbP%2FXAUNwh2klgcoouDzN1TM5RBPsW6cOY4NXasC5YqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz22Wp7AzpPJlQedCrcA8yLHbQ%2FEzE1SApsdzh6w36SmrHu%2FkD8uUI9Tc2s4NfdleyELnlckqgv%2BWwjpCras3%2BJSwgdbDVKGPUVFKaaHg3TdLo%2BIGvH8u%2BXRvcWcdXVjCQ38vwVk1OyYOH7KVdCDNgVM0XuhEUCy282fMgL0CmYx0JqU5xiZed7%2Bk1LjI%2B%2FBjE4UkvCjjl6zZ9irccC15nwinmz%2BNCUFkLTuvjPySGxN9DdZ%2FXkOPK7xCmlWC%2FJ%2FZ3JPDdmeWDOsjVNtuk9pGgfSMPcmjWAcKD3xYw0%2FCrzdLSpVN9qKgwHvMpYihfwD%2FW2AH1yNJM4cJaorStrGglKMsF9cGPcpcbE4aHN4O%2F049%2FM7MX%2FSLD0YC%2FoMJ25P80RZ1BNdaEcrYZ1k3l6c6YB3OLLM0jP1zhmbry0%2Bq5yFL1h%2BRfkzxSr6whxC%2Fk2Ig1jletS8iwJij4cuwQ0aAlnrNpbRIQCyYihbvbwmQX22rTyZ7Lu4KaIljkZBGpQ48QTCwC9Rtj9NaUu2tJdG9eeloWwe0KXkrqBQljYr1AhbTp9sxITGhpQ%2BZTSgrye6bXMyrQTQyPecXyRTvKtPVwtT5o9pyGEswr%2BqcNK%2FmI7PigFaIu8mZE56wD1fMMcvFWicV9to%2FYSN%2FFBMOOo%2FMoGOqUB439JQAopKFnzaYC1Evc8hyTPaBMncoBo4pY4oS4pPLx%2FzdnIrhzZTPbajYIGldrBcM4%2F23H%2FuG%2B1GKIAJ6Xi0Q%2FEroIwBnIaUNneyO%2BeKH7M5jwO%2FKl%2FjwE5af3kU%2FZBNK9qE9xnSl2t%2FfxbSphEBknv9lv7noPW2hB%2B1O%2BwSqUPQjJ%2Bs6l%2BL9us4M5RHvqsNCYAA9M%2BiBkhmGERx6E0BeEfzDuq&X-Amz-Signature=46099d4298c3c36dacb25d15b3d6a70b5b46c299e5ea8e120ace83775b1e89e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K7BJDM3%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs7GSYvwb3XN2LAfaisFP166Mtb9z%2FUFgsJvpVbNHMoQIgVvbP%2FXAUNwh2klgcoouDzN1TM5RBPsW6cOY4NXasC5YqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz22Wp7AzpPJlQedCrcA8yLHbQ%2FEzE1SApsdzh6w36SmrHu%2FkD8uUI9Tc2s4NfdleyELnlckqgv%2BWwjpCras3%2BJSwgdbDVKGPUVFKaaHg3TdLo%2BIGvH8u%2BXRvcWcdXVjCQ38vwVk1OyYOH7KVdCDNgVM0XuhEUCy282fMgL0CmYx0JqU5xiZed7%2Bk1LjI%2B%2FBjE4UkvCjjl6zZ9irccC15nwinmz%2BNCUFkLTuvjPySGxN9DdZ%2FXkOPK7xCmlWC%2FJ%2FZ3JPDdmeWDOsjVNtuk9pGgfSMPcmjWAcKD3xYw0%2FCrzdLSpVN9qKgwHvMpYihfwD%2FW2AH1yNJM4cJaorStrGglKMsF9cGPcpcbE4aHN4O%2F049%2FM7MX%2FSLD0YC%2FoMJ25P80RZ1BNdaEcrYZ1k3l6c6YB3OLLM0jP1zhmbry0%2Bq5yFL1h%2BRfkzxSr6whxC%2Fk2Ig1jletS8iwJij4cuwQ0aAlnrNpbRIQCyYihbvbwmQX22rTyZ7Lu4KaIljkZBGpQ48QTCwC9Rtj9NaUu2tJdG9eeloWwe0KXkrqBQljYr1AhbTp9sxITGhpQ%2BZTSgrye6bXMyrQTQyPecXyRTvKtPVwtT5o9pyGEswr%2BqcNK%2FmI7PigFaIu8mZE56wD1fMMcvFWicV9to%2FYSN%2FFBMOOo%2FMoGOqUB439JQAopKFnzaYC1Evc8hyTPaBMncoBo4pY4oS4pPLx%2FzdnIrhzZTPbajYIGldrBcM4%2F23H%2FuG%2B1GKIAJ6Xi0Q%2FEroIwBnIaUNneyO%2BeKH7M5jwO%2FKl%2FjwE5af3kU%2FZBNK9qE9xnSl2t%2FfxbSphEBknv9lv7noPW2hB%2B1O%2BwSqUPQjJ%2Bs6l%2BL9us4M5RHvqsNCYAA9M%2BiBkhmGERx6E0BeEfzDuq&X-Amz-Signature=26bf0a7b6463ea0c6228915ce4d6bff42f75e7af54c3de00e259ec69aa698542&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K7BJDM3%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs7GSYvwb3XN2LAfaisFP166Mtb9z%2FUFgsJvpVbNHMoQIgVvbP%2FXAUNwh2klgcoouDzN1TM5RBPsW6cOY4NXasC5YqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz22Wp7AzpPJlQedCrcA8yLHbQ%2FEzE1SApsdzh6w36SmrHu%2FkD8uUI9Tc2s4NfdleyELnlckqgv%2BWwjpCras3%2BJSwgdbDVKGPUVFKaaHg3TdLo%2BIGvH8u%2BXRvcWcdXVjCQ38vwVk1OyYOH7KVdCDNgVM0XuhEUCy282fMgL0CmYx0JqU5xiZed7%2Bk1LjI%2B%2FBjE4UkvCjjl6zZ9irccC15nwinmz%2BNCUFkLTuvjPySGxN9DdZ%2FXkOPK7xCmlWC%2FJ%2FZ3JPDdmeWDOsjVNtuk9pGgfSMPcmjWAcKD3xYw0%2FCrzdLSpVN9qKgwHvMpYihfwD%2FW2AH1yNJM4cJaorStrGglKMsF9cGPcpcbE4aHN4O%2F049%2FM7MX%2FSLD0YC%2FoMJ25P80RZ1BNdaEcrYZ1k3l6c6YB3OLLM0jP1zhmbry0%2Bq5yFL1h%2BRfkzxSr6whxC%2Fk2Ig1jletS8iwJij4cuwQ0aAlnrNpbRIQCyYihbvbwmQX22rTyZ7Lu4KaIljkZBGpQ48QTCwC9Rtj9NaUu2tJdG9eeloWwe0KXkrqBQljYr1AhbTp9sxITGhpQ%2BZTSgrye6bXMyrQTQyPecXyRTvKtPVwtT5o9pyGEswr%2BqcNK%2FmI7PigFaIu8mZE56wD1fMMcvFWicV9to%2FYSN%2FFBMOOo%2FMoGOqUB439JQAopKFnzaYC1Evc8hyTPaBMncoBo4pY4oS4pPLx%2FzdnIrhzZTPbajYIGldrBcM4%2F23H%2FuG%2B1GKIAJ6Xi0Q%2FEroIwBnIaUNneyO%2BeKH7M5jwO%2FKl%2FjwE5af3kU%2FZBNK9qE9xnSl2t%2FfxbSphEBknv9lv7noPW2hB%2B1O%2BwSqUPQjJ%2Bs6l%2BL9us4M5RHvqsNCYAA9M%2BiBkhmGERx6E0BeEfzDuq&X-Amz-Signature=1f45a34272317c21fef78724c9ffbd6d9cb5de4d634078f1b59ee924fedf9068&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K7BJDM3%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs7GSYvwb3XN2LAfaisFP166Mtb9z%2FUFgsJvpVbNHMoQIgVvbP%2FXAUNwh2klgcoouDzN1TM5RBPsW6cOY4NXasC5YqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz22Wp7AzpPJlQedCrcA8yLHbQ%2FEzE1SApsdzh6w36SmrHu%2FkD8uUI9Tc2s4NfdleyELnlckqgv%2BWwjpCras3%2BJSwgdbDVKGPUVFKaaHg3TdLo%2BIGvH8u%2BXRvcWcdXVjCQ38vwVk1OyYOH7KVdCDNgVM0XuhEUCy282fMgL0CmYx0JqU5xiZed7%2Bk1LjI%2B%2FBjE4UkvCjjl6zZ9irccC15nwinmz%2BNCUFkLTuvjPySGxN9DdZ%2FXkOPK7xCmlWC%2FJ%2FZ3JPDdmeWDOsjVNtuk9pGgfSMPcmjWAcKD3xYw0%2FCrzdLSpVN9qKgwHvMpYihfwD%2FW2AH1yNJM4cJaorStrGglKMsF9cGPcpcbE4aHN4O%2F049%2FM7MX%2FSLD0YC%2FoMJ25P80RZ1BNdaEcrYZ1k3l6c6YB3OLLM0jP1zhmbry0%2Bq5yFL1h%2BRfkzxSr6whxC%2Fk2Ig1jletS8iwJij4cuwQ0aAlnrNpbRIQCyYihbvbwmQX22rTyZ7Lu4KaIljkZBGpQ48QTCwC9Rtj9NaUu2tJdG9eeloWwe0KXkrqBQljYr1AhbTp9sxITGhpQ%2BZTSgrye6bXMyrQTQyPecXyRTvKtPVwtT5o9pyGEswr%2BqcNK%2FmI7PigFaIu8mZE56wD1fMMcvFWicV9to%2FYSN%2FFBMOOo%2FMoGOqUB439JQAopKFnzaYC1Evc8hyTPaBMncoBo4pY4oS4pPLx%2FzdnIrhzZTPbajYIGldrBcM4%2F23H%2FuG%2B1GKIAJ6Xi0Q%2FEroIwBnIaUNneyO%2BeKH7M5jwO%2FKl%2FjwE5af3kU%2FZBNK9qE9xnSl2t%2FfxbSphEBknv9lv7noPW2hB%2B1O%2BwSqUPQjJ%2Bs6l%2BL9us4M5RHvqsNCYAA9M%2BiBkhmGERx6E0BeEfzDuq&X-Amz-Signature=67181e3e2eeffb557c3f97ba9fece98b56eadcecb91f5003260f287949668bd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K7BJDM3%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs7GSYvwb3XN2LAfaisFP166Mtb9z%2FUFgsJvpVbNHMoQIgVvbP%2FXAUNwh2klgcoouDzN1TM5RBPsW6cOY4NXasC5YqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz22Wp7AzpPJlQedCrcA8yLHbQ%2FEzE1SApsdzh6w36SmrHu%2FkD8uUI9Tc2s4NfdleyELnlckqgv%2BWwjpCras3%2BJSwgdbDVKGPUVFKaaHg3TdLo%2BIGvH8u%2BXRvcWcdXVjCQ38vwVk1OyYOH7KVdCDNgVM0XuhEUCy282fMgL0CmYx0JqU5xiZed7%2Bk1LjI%2B%2FBjE4UkvCjjl6zZ9irccC15nwinmz%2BNCUFkLTuvjPySGxN9DdZ%2FXkOPK7xCmlWC%2FJ%2FZ3JPDdmeWDOsjVNtuk9pGgfSMPcmjWAcKD3xYw0%2FCrzdLSpVN9qKgwHvMpYihfwD%2FW2AH1yNJM4cJaorStrGglKMsF9cGPcpcbE4aHN4O%2F049%2FM7MX%2FSLD0YC%2FoMJ25P80RZ1BNdaEcrYZ1k3l6c6YB3OLLM0jP1zhmbry0%2Bq5yFL1h%2BRfkzxSr6whxC%2Fk2Ig1jletS8iwJij4cuwQ0aAlnrNpbRIQCyYihbvbwmQX22rTyZ7Lu4KaIljkZBGpQ48QTCwC9Rtj9NaUu2tJdG9eeloWwe0KXkrqBQljYr1AhbTp9sxITGhpQ%2BZTSgrye6bXMyrQTQyPecXyRTvKtPVwtT5o9pyGEswr%2BqcNK%2FmI7PigFaIu8mZE56wD1fMMcvFWicV9to%2FYSN%2FFBMOOo%2FMoGOqUB439JQAopKFnzaYC1Evc8hyTPaBMncoBo4pY4oS4pPLx%2FzdnIrhzZTPbajYIGldrBcM4%2F23H%2FuG%2B1GKIAJ6Xi0Q%2FEroIwBnIaUNneyO%2BeKH7M5jwO%2FKl%2FjwE5af3kU%2FZBNK9qE9xnSl2t%2FfxbSphEBknv9lv7noPW2hB%2B1O%2BwSqUPQjJ%2Bs6l%2BL9us4M5RHvqsNCYAA9M%2BiBkhmGERx6E0BeEfzDuq&X-Amz-Signature=b61ebf9b82d25c7ad76c501472376a82cb5f66225458c8c3c02c889d8554c259&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K7BJDM3%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs7GSYvwb3XN2LAfaisFP166Mtb9z%2FUFgsJvpVbNHMoQIgVvbP%2FXAUNwh2klgcoouDzN1TM5RBPsW6cOY4NXasC5YqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz22Wp7AzpPJlQedCrcA8yLHbQ%2FEzE1SApsdzh6w36SmrHu%2FkD8uUI9Tc2s4NfdleyELnlckqgv%2BWwjpCras3%2BJSwgdbDVKGPUVFKaaHg3TdLo%2BIGvH8u%2BXRvcWcdXVjCQ38vwVk1OyYOH7KVdCDNgVM0XuhEUCy282fMgL0CmYx0JqU5xiZed7%2Bk1LjI%2B%2FBjE4UkvCjjl6zZ9irccC15nwinmz%2BNCUFkLTuvjPySGxN9DdZ%2FXkOPK7xCmlWC%2FJ%2FZ3JPDdmeWDOsjVNtuk9pGgfSMPcmjWAcKD3xYw0%2FCrzdLSpVN9qKgwHvMpYihfwD%2FW2AH1yNJM4cJaorStrGglKMsF9cGPcpcbE4aHN4O%2F049%2FM7MX%2FSLD0YC%2FoMJ25P80RZ1BNdaEcrYZ1k3l6c6YB3OLLM0jP1zhmbry0%2Bq5yFL1h%2BRfkzxSr6whxC%2Fk2Ig1jletS8iwJij4cuwQ0aAlnrNpbRIQCyYihbvbwmQX22rTyZ7Lu4KaIljkZBGpQ48QTCwC9Rtj9NaUu2tJdG9eeloWwe0KXkrqBQljYr1AhbTp9sxITGhpQ%2BZTSgrye6bXMyrQTQyPecXyRTvKtPVwtT5o9pyGEswr%2BqcNK%2FmI7PigFaIu8mZE56wD1fMMcvFWicV9to%2FYSN%2FFBMOOo%2FMoGOqUB439JQAopKFnzaYC1Evc8hyTPaBMncoBo4pY4oS4pPLx%2FzdnIrhzZTPbajYIGldrBcM4%2F23H%2FuG%2B1GKIAJ6Xi0Q%2FEroIwBnIaUNneyO%2BeKH7M5jwO%2FKl%2FjwE5af3kU%2FZBNK9qE9xnSl2t%2FfxbSphEBknv9lv7noPW2hB%2B1O%2BwSqUPQjJ%2Bs6l%2BL9us4M5RHvqsNCYAA9M%2BiBkhmGERx6E0BeEfzDuq&X-Amz-Signature=0c7d94ab1625428758af59a61395c736b1cd3c29cd7a6c39e3b03ba0046e8e2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K7BJDM3%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs7GSYvwb3XN2LAfaisFP166Mtb9z%2FUFgsJvpVbNHMoQIgVvbP%2FXAUNwh2klgcoouDzN1TM5RBPsW6cOY4NXasC5YqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz22Wp7AzpPJlQedCrcA8yLHbQ%2FEzE1SApsdzh6w36SmrHu%2FkD8uUI9Tc2s4NfdleyELnlckqgv%2BWwjpCras3%2BJSwgdbDVKGPUVFKaaHg3TdLo%2BIGvH8u%2BXRvcWcdXVjCQ38vwVk1OyYOH7KVdCDNgVM0XuhEUCy282fMgL0CmYx0JqU5xiZed7%2Bk1LjI%2B%2FBjE4UkvCjjl6zZ9irccC15nwinmz%2BNCUFkLTuvjPySGxN9DdZ%2FXkOPK7xCmlWC%2FJ%2FZ3JPDdmeWDOsjVNtuk9pGgfSMPcmjWAcKD3xYw0%2FCrzdLSpVN9qKgwHvMpYihfwD%2FW2AH1yNJM4cJaorStrGglKMsF9cGPcpcbE4aHN4O%2F049%2FM7MX%2FSLD0YC%2FoMJ25P80RZ1BNdaEcrYZ1k3l6c6YB3OLLM0jP1zhmbry0%2Bq5yFL1h%2BRfkzxSr6whxC%2Fk2Ig1jletS8iwJij4cuwQ0aAlnrNpbRIQCyYihbvbwmQX22rTyZ7Lu4KaIljkZBGpQ48QTCwC9Rtj9NaUu2tJdG9eeloWwe0KXkrqBQljYr1AhbTp9sxITGhpQ%2BZTSgrye6bXMyrQTQyPecXyRTvKtPVwtT5o9pyGEswr%2BqcNK%2FmI7PigFaIu8mZE56wD1fMMcvFWicV9to%2FYSN%2FFBMOOo%2FMoGOqUB439JQAopKFnzaYC1Evc8hyTPaBMncoBo4pY4oS4pPLx%2FzdnIrhzZTPbajYIGldrBcM4%2F23H%2FuG%2B1GKIAJ6Xi0Q%2FEroIwBnIaUNneyO%2BeKH7M5jwO%2FKl%2FjwE5af3kU%2FZBNK9qE9xnSl2t%2FfxbSphEBknv9lv7noPW2hB%2B1O%2BwSqUPQjJ%2Bs6l%2BL9us4M5RHvqsNCYAA9M%2BiBkhmGERx6E0BeEfzDuq&X-Amz-Signature=af734d26ac4bd319a0a398b19c4be2dcab00f66726f15adfa4c961c9f4ad9eca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K7BJDM3%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs7GSYvwb3XN2LAfaisFP166Mtb9z%2FUFgsJvpVbNHMoQIgVvbP%2FXAUNwh2klgcoouDzN1TM5RBPsW6cOY4NXasC5YqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz22Wp7AzpPJlQedCrcA8yLHbQ%2FEzE1SApsdzh6w36SmrHu%2FkD8uUI9Tc2s4NfdleyELnlckqgv%2BWwjpCras3%2BJSwgdbDVKGPUVFKaaHg3TdLo%2BIGvH8u%2BXRvcWcdXVjCQ38vwVk1OyYOH7KVdCDNgVM0XuhEUCy282fMgL0CmYx0JqU5xiZed7%2Bk1LjI%2B%2FBjE4UkvCjjl6zZ9irccC15nwinmz%2BNCUFkLTuvjPySGxN9DdZ%2FXkOPK7xCmlWC%2FJ%2FZ3JPDdmeWDOsjVNtuk9pGgfSMPcmjWAcKD3xYw0%2FCrzdLSpVN9qKgwHvMpYihfwD%2FW2AH1yNJM4cJaorStrGglKMsF9cGPcpcbE4aHN4O%2F049%2FM7MX%2FSLD0YC%2FoMJ25P80RZ1BNdaEcrYZ1k3l6c6YB3OLLM0jP1zhmbry0%2Bq5yFL1h%2BRfkzxSr6whxC%2Fk2Ig1jletS8iwJij4cuwQ0aAlnrNpbRIQCyYihbvbwmQX22rTyZ7Lu4KaIljkZBGpQ48QTCwC9Rtj9NaUu2tJdG9eeloWwe0KXkrqBQljYr1AhbTp9sxITGhpQ%2BZTSgrye6bXMyrQTQyPecXyRTvKtPVwtT5o9pyGEswr%2BqcNK%2FmI7PigFaIu8mZE56wD1fMMcvFWicV9to%2FYSN%2FFBMOOo%2FMoGOqUB439JQAopKFnzaYC1Evc8hyTPaBMncoBo4pY4oS4pPLx%2FzdnIrhzZTPbajYIGldrBcM4%2F23H%2FuG%2B1GKIAJ6Xi0Q%2FEroIwBnIaUNneyO%2BeKH7M5jwO%2FKl%2FjwE5af3kU%2FZBNK9qE9xnSl2t%2FfxbSphEBknv9lv7noPW2hB%2B1O%2BwSqUPQjJ%2Bs6l%2BL9us4M5RHvqsNCYAA9M%2BiBkhmGERx6E0BeEfzDuq&X-Amz-Signature=29846dfbe903e1d6dd9e656252fa95f872a07f48d2e696b6a2c042c4b0084232&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

