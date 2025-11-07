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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTO4QLIX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeS9jxNdG2oYy%2FQdkczT6YvWY7QSsJSFv5%2F%2B4QY4vquAiEA7KrjfdR%2BFrETcK21Pt8OtynCC9RFppfrEOwxcqFljwQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbixCgKEh0F5yMrsSrcAwbnPGYAWftiTgDy8YXJtM03trDm9In8kx3c1Mv%2BCPg%2F7GiH0v%2FqrPjz8o4k5z0JJEA18aEFcl5fFzA%2B7RIwmnflHx8%2FMGNFJjWMrSt4xV75KhhpQJD%2FyZXcMG1mMbU%2BIVE9s%2FWrvgecm4Aws7%2FpRX7pgw8%2BL8cY3y7MnrTykdy8nO2rFs554kV%2FXIHRAmj%2BK2S4%2BEOGrwawMjtRk1de%2Bk%2BN70xcUTVb261FZfbULo08Bn%2BwpREQ1kcbZN4AeyAUHMoB5sJ0SQiGGgycXGgOSdTrj5uyHmqAlDT29HdNfznmn42DQGAzsFAztYS8S%2FaXFKA%2Bh74g6caULPm5qr0sZzmPHKqe0ArJjCIaz8VjXjD7LVoCjl0mErz0DtL%2FObthksm2SRHIkVZfnHE%2Bsxjp0WDPQA5Q0gs05%2BFApPCOvGFTLuGvifwY5JcE7x10iCRDEnR5sL4oQPMYX5ol3GkUZdfpEpPUhzbE8n3pNW0wlq5OgC5d9FifcMHgSKmaMhs9Had9bsw0G7QMGNCsOKeu89e767xyv2WRzNJM%2F3ke29xklUz10nPU0PEWMG401tDGsiTaWPZ0sOW8bo%2FjxY30yWgPggKu4kVdaju8s3JYgSmaHHoHmbNmy1CLazG4MIi1tcgGOqUBTT1Xl2P6gNhvCaK6wZIJ3VrtKdRnCQBrs9StWllXgOnaQV4h53JOu8Yzmbqf7czoMa%2FS4LhX4qd7iZ%2Fu2PGUogUzKQJ9ghdla%2BzNz%2Frjwfr5PN1wDbeCG%2FArzjvFF1VeA9%2BbBWJ6op8cuPXpMcT9Q2RRLFwYIuQ2WfsS3Jgd3cEFY5q5vYwhEDzcPbY4O9KXrY%2BzdlYqsPqnSOYb9HdY9O%2F1Bi1K&X-Amz-Signature=49a7de9996cf97949d9c7adef3f25bf44e74ce4006de2cf96733818327aa4d90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTO4QLIX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeS9jxNdG2oYy%2FQdkczT6YvWY7QSsJSFv5%2F%2B4QY4vquAiEA7KrjfdR%2BFrETcK21Pt8OtynCC9RFppfrEOwxcqFljwQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbixCgKEh0F5yMrsSrcAwbnPGYAWftiTgDy8YXJtM03trDm9In8kx3c1Mv%2BCPg%2F7GiH0v%2FqrPjz8o4k5z0JJEA18aEFcl5fFzA%2B7RIwmnflHx8%2FMGNFJjWMrSt4xV75KhhpQJD%2FyZXcMG1mMbU%2BIVE9s%2FWrvgecm4Aws7%2FpRX7pgw8%2BL8cY3y7MnrTykdy8nO2rFs554kV%2FXIHRAmj%2BK2S4%2BEOGrwawMjtRk1de%2Bk%2BN70xcUTVb261FZfbULo08Bn%2BwpREQ1kcbZN4AeyAUHMoB5sJ0SQiGGgycXGgOSdTrj5uyHmqAlDT29HdNfznmn42DQGAzsFAztYS8S%2FaXFKA%2Bh74g6caULPm5qr0sZzmPHKqe0ArJjCIaz8VjXjD7LVoCjl0mErz0DtL%2FObthksm2SRHIkVZfnHE%2Bsxjp0WDPQA5Q0gs05%2BFApPCOvGFTLuGvifwY5JcE7x10iCRDEnR5sL4oQPMYX5ol3GkUZdfpEpPUhzbE8n3pNW0wlq5OgC5d9FifcMHgSKmaMhs9Had9bsw0G7QMGNCsOKeu89e767xyv2WRzNJM%2F3ke29xklUz10nPU0PEWMG401tDGsiTaWPZ0sOW8bo%2FjxY30yWgPggKu4kVdaju8s3JYgSmaHHoHmbNmy1CLazG4MIi1tcgGOqUBTT1Xl2P6gNhvCaK6wZIJ3VrtKdRnCQBrs9StWllXgOnaQV4h53JOu8Yzmbqf7czoMa%2FS4LhX4qd7iZ%2Fu2PGUogUzKQJ9ghdla%2BzNz%2Frjwfr5PN1wDbeCG%2FArzjvFF1VeA9%2BbBWJ6op8cuPXpMcT9Q2RRLFwYIuQ2WfsS3Jgd3cEFY5q5vYwhEDzcPbY4O9KXrY%2BzdlYqsPqnSOYb9HdY9O%2F1Bi1K&X-Amz-Signature=196ae0efdc5c7e3124190214b03428322593751b7f6d31241fc587988550cd71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTO4QLIX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeS9jxNdG2oYy%2FQdkczT6YvWY7QSsJSFv5%2F%2B4QY4vquAiEA7KrjfdR%2BFrETcK21Pt8OtynCC9RFppfrEOwxcqFljwQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbixCgKEh0F5yMrsSrcAwbnPGYAWftiTgDy8YXJtM03trDm9In8kx3c1Mv%2BCPg%2F7GiH0v%2FqrPjz8o4k5z0JJEA18aEFcl5fFzA%2B7RIwmnflHx8%2FMGNFJjWMrSt4xV75KhhpQJD%2FyZXcMG1mMbU%2BIVE9s%2FWrvgecm4Aws7%2FpRX7pgw8%2BL8cY3y7MnrTykdy8nO2rFs554kV%2FXIHRAmj%2BK2S4%2BEOGrwawMjtRk1de%2Bk%2BN70xcUTVb261FZfbULo08Bn%2BwpREQ1kcbZN4AeyAUHMoB5sJ0SQiGGgycXGgOSdTrj5uyHmqAlDT29HdNfznmn42DQGAzsFAztYS8S%2FaXFKA%2Bh74g6caULPm5qr0sZzmPHKqe0ArJjCIaz8VjXjD7LVoCjl0mErz0DtL%2FObthksm2SRHIkVZfnHE%2Bsxjp0WDPQA5Q0gs05%2BFApPCOvGFTLuGvifwY5JcE7x10iCRDEnR5sL4oQPMYX5ol3GkUZdfpEpPUhzbE8n3pNW0wlq5OgC5d9FifcMHgSKmaMhs9Had9bsw0G7QMGNCsOKeu89e767xyv2WRzNJM%2F3ke29xklUz10nPU0PEWMG401tDGsiTaWPZ0sOW8bo%2FjxY30yWgPggKu4kVdaju8s3JYgSmaHHoHmbNmy1CLazG4MIi1tcgGOqUBTT1Xl2P6gNhvCaK6wZIJ3VrtKdRnCQBrs9StWllXgOnaQV4h53JOu8Yzmbqf7czoMa%2FS4LhX4qd7iZ%2Fu2PGUogUzKQJ9ghdla%2BzNz%2Frjwfr5PN1wDbeCG%2FArzjvFF1VeA9%2BbBWJ6op8cuPXpMcT9Q2RRLFwYIuQ2WfsS3Jgd3cEFY5q5vYwhEDzcPbY4O9KXrY%2BzdlYqsPqnSOYb9HdY9O%2F1Bi1K&X-Amz-Signature=e59571a25f813f08e8f18ae2bb989a1d4c2789e3b352e1e9db948a1ca80d40a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTO4QLIX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeS9jxNdG2oYy%2FQdkczT6YvWY7QSsJSFv5%2F%2B4QY4vquAiEA7KrjfdR%2BFrETcK21Pt8OtynCC9RFppfrEOwxcqFljwQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbixCgKEh0F5yMrsSrcAwbnPGYAWftiTgDy8YXJtM03trDm9In8kx3c1Mv%2BCPg%2F7GiH0v%2FqrPjz8o4k5z0JJEA18aEFcl5fFzA%2B7RIwmnflHx8%2FMGNFJjWMrSt4xV75KhhpQJD%2FyZXcMG1mMbU%2BIVE9s%2FWrvgecm4Aws7%2FpRX7pgw8%2BL8cY3y7MnrTykdy8nO2rFs554kV%2FXIHRAmj%2BK2S4%2BEOGrwawMjtRk1de%2Bk%2BN70xcUTVb261FZfbULo08Bn%2BwpREQ1kcbZN4AeyAUHMoB5sJ0SQiGGgycXGgOSdTrj5uyHmqAlDT29HdNfznmn42DQGAzsFAztYS8S%2FaXFKA%2Bh74g6caULPm5qr0sZzmPHKqe0ArJjCIaz8VjXjD7LVoCjl0mErz0DtL%2FObthksm2SRHIkVZfnHE%2Bsxjp0WDPQA5Q0gs05%2BFApPCOvGFTLuGvifwY5JcE7x10iCRDEnR5sL4oQPMYX5ol3GkUZdfpEpPUhzbE8n3pNW0wlq5OgC5d9FifcMHgSKmaMhs9Had9bsw0G7QMGNCsOKeu89e767xyv2WRzNJM%2F3ke29xklUz10nPU0PEWMG401tDGsiTaWPZ0sOW8bo%2FjxY30yWgPggKu4kVdaju8s3JYgSmaHHoHmbNmy1CLazG4MIi1tcgGOqUBTT1Xl2P6gNhvCaK6wZIJ3VrtKdRnCQBrs9StWllXgOnaQV4h53JOu8Yzmbqf7czoMa%2FS4LhX4qd7iZ%2Fu2PGUogUzKQJ9ghdla%2BzNz%2Frjwfr5PN1wDbeCG%2FArzjvFF1VeA9%2BbBWJ6op8cuPXpMcT9Q2RRLFwYIuQ2WfsS3Jgd3cEFY5q5vYwhEDzcPbY4O9KXrY%2BzdlYqsPqnSOYb9HdY9O%2F1Bi1K&X-Amz-Signature=c94eacb91f5e95cff532bc7ade414fab4fbdd890f6a7f7213ac676c991af2e36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTO4QLIX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeS9jxNdG2oYy%2FQdkczT6YvWY7QSsJSFv5%2F%2B4QY4vquAiEA7KrjfdR%2BFrETcK21Pt8OtynCC9RFppfrEOwxcqFljwQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbixCgKEh0F5yMrsSrcAwbnPGYAWftiTgDy8YXJtM03trDm9In8kx3c1Mv%2BCPg%2F7GiH0v%2FqrPjz8o4k5z0JJEA18aEFcl5fFzA%2B7RIwmnflHx8%2FMGNFJjWMrSt4xV75KhhpQJD%2FyZXcMG1mMbU%2BIVE9s%2FWrvgecm4Aws7%2FpRX7pgw8%2BL8cY3y7MnrTykdy8nO2rFs554kV%2FXIHRAmj%2BK2S4%2BEOGrwawMjtRk1de%2Bk%2BN70xcUTVb261FZfbULo08Bn%2BwpREQ1kcbZN4AeyAUHMoB5sJ0SQiGGgycXGgOSdTrj5uyHmqAlDT29HdNfznmn42DQGAzsFAztYS8S%2FaXFKA%2Bh74g6caULPm5qr0sZzmPHKqe0ArJjCIaz8VjXjD7LVoCjl0mErz0DtL%2FObthksm2SRHIkVZfnHE%2Bsxjp0WDPQA5Q0gs05%2BFApPCOvGFTLuGvifwY5JcE7x10iCRDEnR5sL4oQPMYX5ol3GkUZdfpEpPUhzbE8n3pNW0wlq5OgC5d9FifcMHgSKmaMhs9Had9bsw0G7QMGNCsOKeu89e767xyv2WRzNJM%2F3ke29xklUz10nPU0PEWMG401tDGsiTaWPZ0sOW8bo%2FjxY30yWgPggKu4kVdaju8s3JYgSmaHHoHmbNmy1CLazG4MIi1tcgGOqUBTT1Xl2P6gNhvCaK6wZIJ3VrtKdRnCQBrs9StWllXgOnaQV4h53JOu8Yzmbqf7czoMa%2FS4LhX4qd7iZ%2Fu2PGUogUzKQJ9ghdla%2BzNz%2Frjwfr5PN1wDbeCG%2FArzjvFF1VeA9%2BbBWJ6op8cuPXpMcT9Q2RRLFwYIuQ2WfsS3Jgd3cEFY5q5vYwhEDzcPbY4O9KXrY%2BzdlYqsPqnSOYb9HdY9O%2F1Bi1K&X-Amz-Signature=35af72849c72a2a3cdc1e699be0b598191f9d33c3aa7445da64acd52ae632241&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTO4QLIX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeS9jxNdG2oYy%2FQdkczT6YvWY7QSsJSFv5%2F%2B4QY4vquAiEA7KrjfdR%2BFrETcK21Pt8OtynCC9RFppfrEOwxcqFljwQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbixCgKEh0F5yMrsSrcAwbnPGYAWftiTgDy8YXJtM03trDm9In8kx3c1Mv%2BCPg%2F7GiH0v%2FqrPjz8o4k5z0JJEA18aEFcl5fFzA%2B7RIwmnflHx8%2FMGNFJjWMrSt4xV75KhhpQJD%2FyZXcMG1mMbU%2BIVE9s%2FWrvgecm4Aws7%2FpRX7pgw8%2BL8cY3y7MnrTykdy8nO2rFs554kV%2FXIHRAmj%2BK2S4%2BEOGrwawMjtRk1de%2Bk%2BN70xcUTVb261FZfbULo08Bn%2BwpREQ1kcbZN4AeyAUHMoB5sJ0SQiGGgycXGgOSdTrj5uyHmqAlDT29HdNfznmn42DQGAzsFAztYS8S%2FaXFKA%2Bh74g6caULPm5qr0sZzmPHKqe0ArJjCIaz8VjXjD7LVoCjl0mErz0DtL%2FObthksm2SRHIkVZfnHE%2Bsxjp0WDPQA5Q0gs05%2BFApPCOvGFTLuGvifwY5JcE7x10iCRDEnR5sL4oQPMYX5ol3GkUZdfpEpPUhzbE8n3pNW0wlq5OgC5d9FifcMHgSKmaMhs9Had9bsw0G7QMGNCsOKeu89e767xyv2WRzNJM%2F3ke29xklUz10nPU0PEWMG401tDGsiTaWPZ0sOW8bo%2FjxY30yWgPggKu4kVdaju8s3JYgSmaHHoHmbNmy1CLazG4MIi1tcgGOqUBTT1Xl2P6gNhvCaK6wZIJ3VrtKdRnCQBrs9StWllXgOnaQV4h53JOu8Yzmbqf7czoMa%2FS4LhX4qd7iZ%2Fu2PGUogUzKQJ9ghdla%2BzNz%2Frjwfr5PN1wDbeCG%2FArzjvFF1VeA9%2BbBWJ6op8cuPXpMcT9Q2RRLFwYIuQ2WfsS3Jgd3cEFY5q5vYwhEDzcPbY4O9KXrY%2BzdlYqsPqnSOYb9HdY9O%2F1Bi1K&X-Amz-Signature=ff06802edad02d8f39922f251cbbc8014f5f36b86988a66d9e2449b08d36e598&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTO4QLIX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeS9jxNdG2oYy%2FQdkczT6YvWY7QSsJSFv5%2F%2B4QY4vquAiEA7KrjfdR%2BFrETcK21Pt8OtynCC9RFppfrEOwxcqFljwQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbixCgKEh0F5yMrsSrcAwbnPGYAWftiTgDy8YXJtM03trDm9In8kx3c1Mv%2BCPg%2F7GiH0v%2FqrPjz8o4k5z0JJEA18aEFcl5fFzA%2B7RIwmnflHx8%2FMGNFJjWMrSt4xV75KhhpQJD%2FyZXcMG1mMbU%2BIVE9s%2FWrvgecm4Aws7%2FpRX7pgw8%2BL8cY3y7MnrTykdy8nO2rFs554kV%2FXIHRAmj%2BK2S4%2BEOGrwawMjtRk1de%2Bk%2BN70xcUTVb261FZfbULo08Bn%2BwpREQ1kcbZN4AeyAUHMoB5sJ0SQiGGgycXGgOSdTrj5uyHmqAlDT29HdNfznmn42DQGAzsFAztYS8S%2FaXFKA%2Bh74g6caULPm5qr0sZzmPHKqe0ArJjCIaz8VjXjD7LVoCjl0mErz0DtL%2FObthksm2SRHIkVZfnHE%2Bsxjp0WDPQA5Q0gs05%2BFApPCOvGFTLuGvifwY5JcE7x10iCRDEnR5sL4oQPMYX5ol3GkUZdfpEpPUhzbE8n3pNW0wlq5OgC5d9FifcMHgSKmaMhs9Had9bsw0G7QMGNCsOKeu89e767xyv2WRzNJM%2F3ke29xklUz10nPU0PEWMG401tDGsiTaWPZ0sOW8bo%2FjxY30yWgPggKu4kVdaju8s3JYgSmaHHoHmbNmy1CLazG4MIi1tcgGOqUBTT1Xl2P6gNhvCaK6wZIJ3VrtKdRnCQBrs9StWllXgOnaQV4h53JOu8Yzmbqf7czoMa%2FS4LhX4qd7iZ%2Fu2PGUogUzKQJ9ghdla%2BzNz%2Frjwfr5PN1wDbeCG%2FArzjvFF1VeA9%2BbBWJ6op8cuPXpMcT9Q2RRLFwYIuQ2WfsS3Jgd3cEFY5q5vYwhEDzcPbY4O9KXrY%2BzdlYqsPqnSOYb9HdY9O%2F1Bi1K&X-Amz-Signature=81e7617f3bdf923248968fcdc36cda2a958308be82c231f8a5acdf9c744b3a2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTO4QLIX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeS9jxNdG2oYy%2FQdkczT6YvWY7QSsJSFv5%2F%2B4QY4vquAiEA7KrjfdR%2BFrETcK21Pt8OtynCC9RFppfrEOwxcqFljwQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbixCgKEh0F5yMrsSrcAwbnPGYAWftiTgDy8YXJtM03trDm9In8kx3c1Mv%2BCPg%2F7GiH0v%2FqrPjz8o4k5z0JJEA18aEFcl5fFzA%2B7RIwmnflHx8%2FMGNFJjWMrSt4xV75KhhpQJD%2FyZXcMG1mMbU%2BIVE9s%2FWrvgecm4Aws7%2FpRX7pgw8%2BL8cY3y7MnrTykdy8nO2rFs554kV%2FXIHRAmj%2BK2S4%2BEOGrwawMjtRk1de%2Bk%2BN70xcUTVb261FZfbULo08Bn%2BwpREQ1kcbZN4AeyAUHMoB5sJ0SQiGGgycXGgOSdTrj5uyHmqAlDT29HdNfznmn42DQGAzsFAztYS8S%2FaXFKA%2Bh74g6caULPm5qr0sZzmPHKqe0ArJjCIaz8VjXjD7LVoCjl0mErz0DtL%2FObthksm2SRHIkVZfnHE%2Bsxjp0WDPQA5Q0gs05%2BFApPCOvGFTLuGvifwY5JcE7x10iCRDEnR5sL4oQPMYX5ol3GkUZdfpEpPUhzbE8n3pNW0wlq5OgC5d9FifcMHgSKmaMhs9Had9bsw0G7QMGNCsOKeu89e767xyv2WRzNJM%2F3ke29xklUz10nPU0PEWMG401tDGsiTaWPZ0sOW8bo%2FjxY30yWgPggKu4kVdaju8s3JYgSmaHHoHmbNmy1CLazG4MIi1tcgGOqUBTT1Xl2P6gNhvCaK6wZIJ3VrtKdRnCQBrs9StWllXgOnaQV4h53JOu8Yzmbqf7czoMa%2FS4LhX4qd7iZ%2Fu2PGUogUzKQJ9ghdla%2BzNz%2Frjwfr5PN1wDbeCG%2FArzjvFF1VeA9%2BbBWJ6op8cuPXpMcT9Q2RRLFwYIuQ2WfsS3Jgd3cEFY5q5vYwhEDzcPbY4O9KXrY%2BzdlYqsPqnSOYb9HdY9O%2F1Bi1K&X-Amz-Signature=adca6074ee3f2449a39f09d27afb94f60e8b31a0796d7d9dba4c5e85781ce1bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTO4QLIX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeS9jxNdG2oYy%2FQdkczT6YvWY7QSsJSFv5%2F%2B4QY4vquAiEA7KrjfdR%2BFrETcK21Pt8OtynCC9RFppfrEOwxcqFljwQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbixCgKEh0F5yMrsSrcAwbnPGYAWftiTgDy8YXJtM03trDm9In8kx3c1Mv%2BCPg%2F7GiH0v%2FqrPjz8o4k5z0JJEA18aEFcl5fFzA%2B7RIwmnflHx8%2FMGNFJjWMrSt4xV75KhhpQJD%2FyZXcMG1mMbU%2BIVE9s%2FWrvgecm4Aws7%2FpRX7pgw8%2BL8cY3y7MnrTykdy8nO2rFs554kV%2FXIHRAmj%2BK2S4%2BEOGrwawMjtRk1de%2Bk%2BN70xcUTVb261FZfbULo08Bn%2BwpREQ1kcbZN4AeyAUHMoB5sJ0SQiGGgycXGgOSdTrj5uyHmqAlDT29HdNfznmn42DQGAzsFAztYS8S%2FaXFKA%2Bh74g6caULPm5qr0sZzmPHKqe0ArJjCIaz8VjXjD7LVoCjl0mErz0DtL%2FObthksm2SRHIkVZfnHE%2Bsxjp0WDPQA5Q0gs05%2BFApPCOvGFTLuGvifwY5JcE7x10iCRDEnR5sL4oQPMYX5ol3GkUZdfpEpPUhzbE8n3pNW0wlq5OgC5d9FifcMHgSKmaMhs9Had9bsw0G7QMGNCsOKeu89e767xyv2WRzNJM%2F3ke29xklUz10nPU0PEWMG401tDGsiTaWPZ0sOW8bo%2FjxY30yWgPggKu4kVdaju8s3JYgSmaHHoHmbNmy1CLazG4MIi1tcgGOqUBTT1Xl2P6gNhvCaK6wZIJ3VrtKdRnCQBrs9StWllXgOnaQV4h53JOu8Yzmbqf7czoMa%2FS4LhX4qd7iZ%2Fu2PGUogUzKQJ9ghdla%2BzNz%2Frjwfr5PN1wDbeCG%2FArzjvFF1VeA9%2BbBWJ6op8cuPXpMcT9Q2RRLFwYIuQ2WfsS3Jgd3cEFY5q5vYwhEDzcPbY4O9KXrY%2BzdlYqsPqnSOYb9HdY9O%2F1Bi1K&X-Amz-Signature=800ea410225f7206a492f67d2e24dd0da9912bcbd7a7817dd75e3f6c89b83fe4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTO4QLIX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeS9jxNdG2oYy%2FQdkczT6YvWY7QSsJSFv5%2F%2B4QY4vquAiEA7KrjfdR%2BFrETcK21Pt8OtynCC9RFppfrEOwxcqFljwQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbixCgKEh0F5yMrsSrcAwbnPGYAWftiTgDy8YXJtM03trDm9In8kx3c1Mv%2BCPg%2F7GiH0v%2FqrPjz8o4k5z0JJEA18aEFcl5fFzA%2B7RIwmnflHx8%2FMGNFJjWMrSt4xV75KhhpQJD%2FyZXcMG1mMbU%2BIVE9s%2FWrvgecm4Aws7%2FpRX7pgw8%2BL8cY3y7MnrTykdy8nO2rFs554kV%2FXIHRAmj%2BK2S4%2BEOGrwawMjtRk1de%2Bk%2BN70xcUTVb261FZfbULo08Bn%2BwpREQ1kcbZN4AeyAUHMoB5sJ0SQiGGgycXGgOSdTrj5uyHmqAlDT29HdNfznmn42DQGAzsFAztYS8S%2FaXFKA%2Bh74g6caULPm5qr0sZzmPHKqe0ArJjCIaz8VjXjD7LVoCjl0mErz0DtL%2FObthksm2SRHIkVZfnHE%2Bsxjp0WDPQA5Q0gs05%2BFApPCOvGFTLuGvifwY5JcE7x10iCRDEnR5sL4oQPMYX5ol3GkUZdfpEpPUhzbE8n3pNW0wlq5OgC5d9FifcMHgSKmaMhs9Had9bsw0G7QMGNCsOKeu89e767xyv2WRzNJM%2F3ke29xklUz10nPU0PEWMG401tDGsiTaWPZ0sOW8bo%2FjxY30yWgPggKu4kVdaju8s3JYgSmaHHoHmbNmy1CLazG4MIi1tcgGOqUBTT1Xl2P6gNhvCaK6wZIJ3VrtKdRnCQBrs9StWllXgOnaQV4h53JOu8Yzmbqf7czoMa%2FS4LhX4qd7iZ%2Fu2PGUogUzKQJ9ghdla%2BzNz%2Frjwfr5PN1wDbeCG%2FArzjvFF1VeA9%2BbBWJ6op8cuPXpMcT9Q2RRLFwYIuQ2WfsS3Jgd3cEFY5q5vYwhEDzcPbY4O9KXrY%2BzdlYqsPqnSOYb9HdY9O%2F1Bi1K&X-Amz-Signature=ecbe53c342ae37f4a198f04f462bd33e60cc263880050a8b99b0d2b0f14c4a8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

