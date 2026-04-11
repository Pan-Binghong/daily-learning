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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMZWGZX%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIBrTMS9ccABxSL%2BzR1CnV3T%2BUnAXKBGw7nqE6u3QJgeEAiAwPczfkN3U9mb95K7vdi1X%2F%2FovUre8LSn2yYHN8DEoBSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMrrjJ8fhCRR0yUeKJKtwDwgdsv0X8fp24AnoiXkcKtAtfRrp24Sq0abpQO%2FkbXxAJfWGlkMq6VQtMswAJEJtmJfJgiuetvdRrT88SFpB4gy2aUrZmpbbzZVSgKgruaoSfQWYvAenBhAgSG6eml9UAhM1gtq4obkV0xSLPRYFiYakDLmpvP0AuqqH7FrSPqb2SMuRFvU0BN%2BgILdjkQYhejiU7LQRCjFDJIRRIom5ie1uwG3c52C%2FrDq8EtZrq1v2gVvOUj9kU37gnAxPuDjxyvdDlDu1EH3%2BtQ51GDbwwPfNrotydE7BWZtepMJGDLvs5GjC79gstDsh0oEkhQr3mXyg%2BI3a2po5VK3Y9wK1sgoIYpBWcYL9959S8K7BUgZGAXheONo4Vr%2FXF24fgFsOYeaQ89LE1lmBBMOILBAx7c2jwjxs%2FAgJkXZB0D%2BYyW6psU2K1qKPohBhNwFKPcsLy3%2BX31BXdRXSO%2F5DlcoBacmbYwJqnYRzc9c465pHzAPdATfPhnKXxBDwT30q5G746SvDPg0TBd%2FEnvVo%2BBqyCkNAP%2B%2BLVMgQ6CC%2FBUKxlN%2FwpH5Mx%2BB%2Bix%2B6RpTne6hRikBJ2mLj3R1bVabUD2BnZuOVeD8F89qx5XZD80DYoTfl7T0kdk78%2Bv5PXI08w2urmzgY6pgEvQaAxaFIJQFmoypMIjOnKmqNSFdkly0tFKI8ZP7pB6xWhK1Wb2cBsbb3A6bcHlAj3FYPgHFrl%2FXAAOYerNXeL0WuyCCRtWISnwpUF0pSucBgEt2jMxBDme1D8sFv6%2FQg%2B8cfo%2BFBopyMiKRvH5nl7iuuCC7c7Bjr4fCDRDbi1hLtGoG%2FPABDo1qzJIP0waVvpod%2BXObz%2Bwmq99q4S5o82VlFGwh38&X-Amz-Signature=462c6dfbda9d63e49a8b4df0debf5e7b0ca466d376513b5e8fd4a42ebbea9e40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMZWGZX%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIBrTMS9ccABxSL%2BzR1CnV3T%2BUnAXKBGw7nqE6u3QJgeEAiAwPczfkN3U9mb95K7vdi1X%2F%2FovUre8LSn2yYHN8DEoBSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMrrjJ8fhCRR0yUeKJKtwDwgdsv0X8fp24AnoiXkcKtAtfRrp24Sq0abpQO%2FkbXxAJfWGlkMq6VQtMswAJEJtmJfJgiuetvdRrT88SFpB4gy2aUrZmpbbzZVSgKgruaoSfQWYvAenBhAgSG6eml9UAhM1gtq4obkV0xSLPRYFiYakDLmpvP0AuqqH7FrSPqb2SMuRFvU0BN%2BgILdjkQYhejiU7LQRCjFDJIRRIom5ie1uwG3c52C%2FrDq8EtZrq1v2gVvOUj9kU37gnAxPuDjxyvdDlDu1EH3%2BtQ51GDbwwPfNrotydE7BWZtepMJGDLvs5GjC79gstDsh0oEkhQr3mXyg%2BI3a2po5VK3Y9wK1sgoIYpBWcYL9959S8K7BUgZGAXheONo4Vr%2FXF24fgFsOYeaQ89LE1lmBBMOILBAx7c2jwjxs%2FAgJkXZB0D%2BYyW6psU2K1qKPohBhNwFKPcsLy3%2BX31BXdRXSO%2F5DlcoBacmbYwJqnYRzc9c465pHzAPdATfPhnKXxBDwT30q5G746SvDPg0TBd%2FEnvVo%2BBqyCkNAP%2B%2BLVMgQ6CC%2FBUKxlN%2FwpH5Mx%2BB%2Bix%2B6RpTne6hRikBJ2mLj3R1bVabUD2BnZuOVeD8F89qx5XZD80DYoTfl7T0kdk78%2Bv5PXI08w2urmzgY6pgEvQaAxaFIJQFmoypMIjOnKmqNSFdkly0tFKI8ZP7pB6xWhK1Wb2cBsbb3A6bcHlAj3FYPgHFrl%2FXAAOYerNXeL0WuyCCRtWISnwpUF0pSucBgEt2jMxBDme1D8sFv6%2FQg%2B8cfo%2BFBopyMiKRvH5nl7iuuCC7c7Bjr4fCDRDbi1hLtGoG%2FPABDo1qzJIP0waVvpod%2BXObz%2Bwmq99q4S5o82VlFGwh38&X-Amz-Signature=fcba5c4424ea1ca96250cfe30673d85f16002ce96de0c139859cfd6df63a81eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMZWGZX%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIBrTMS9ccABxSL%2BzR1CnV3T%2BUnAXKBGw7nqE6u3QJgeEAiAwPczfkN3U9mb95K7vdi1X%2F%2FovUre8LSn2yYHN8DEoBSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMrrjJ8fhCRR0yUeKJKtwDwgdsv0X8fp24AnoiXkcKtAtfRrp24Sq0abpQO%2FkbXxAJfWGlkMq6VQtMswAJEJtmJfJgiuetvdRrT88SFpB4gy2aUrZmpbbzZVSgKgruaoSfQWYvAenBhAgSG6eml9UAhM1gtq4obkV0xSLPRYFiYakDLmpvP0AuqqH7FrSPqb2SMuRFvU0BN%2BgILdjkQYhejiU7LQRCjFDJIRRIom5ie1uwG3c52C%2FrDq8EtZrq1v2gVvOUj9kU37gnAxPuDjxyvdDlDu1EH3%2BtQ51GDbwwPfNrotydE7BWZtepMJGDLvs5GjC79gstDsh0oEkhQr3mXyg%2BI3a2po5VK3Y9wK1sgoIYpBWcYL9959S8K7BUgZGAXheONo4Vr%2FXF24fgFsOYeaQ89LE1lmBBMOILBAx7c2jwjxs%2FAgJkXZB0D%2BYyW6psU2K1qKPohBhNwFKPcsLy3%2BX31BXdRXSO%2F5DlcoBacmbYwJqnYRzc9c465pHzAPdATfPhnKXxBDwT30q5G746SvDPg0TBd%2FEnvVo%2BBqyCkNAP%2B%2BLVMgQ6CC%2FBUKxlN%2FwpH5Mx%2BB%2Bix%2B6RpTne6hRikBJ2mLj3R1bVabUD2BnZuOVeD8F89qx5XZD80DYoTfl7T0kdk78%2Bv5PXI08w2urmzgY6pgEvQaAxaFIJQFmoypMIjOnKmqNSFdkly0tFKI8ZP7pB6xWhK1Wb2cBsbb3A6bcHlAj3FYPgHFrl%2FXAAOYerNXeL0WuyCCRtWISnwpUF0pSucBgEt2jMxBDme1D8sFv6%2FQg%2B8cfo%2BFBopyMiKRvH5nl7iuuCC7c7Bjr4fCDRDbi1hLtGoG%2FPABDo1qzJIP0waVvpod%2BXObz%2Bwmq99q4S5o82VlFGwh38&X-Amz-Signature=2645284d5ca78520d6951510792ebb079c450ec5e7d2f0285f24bc3b72062a5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMZWGZX%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIBrTMS9ccABxSL%2BzR1CnV3T%2BUnAXKBGw7nqE6u3QJgeEAiAwPczfkN3U9mb95K7vdi1X%2F%2FovUre8LSn2yYHN8DEoBSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMrrjJ8fhCRR0yUeKJKtwDwgdsv0X8fp24AnoiXkcKtAtfRrp24Sq0abpQO%2FkbXxAJfWGlkMq6VQtMswAJEJtmJfJgiuetvdRrT88SFpB4gy2aUrZmpbbzZVSgKgruaoSfQWYvAenBhAgSG6eml9UAhM1gtq4obkV0xSLPRYFiYakDLmpvP0AuqqH7FrSPqb2SMuRFvU0BN%2BgILdjkQYhejiU7LQRCjFDJIRRIom5ie1uwG3c52C%2FrDq8EtZrq1v2gVvOUj9kU37gnAxPuDjxyvdDlDu1EH3%2BtQ51GDbwwPfNrotydE7BWZtepMJGDLvs5GjC79gstDsh0oEkhQr3mXyg%2BI3a2po5VK3Y9wK1sgoIYpBWcYL9959S8K7BUgZGAXheONo4Vr%2FXF24fgFsOYeaQ89LE1lmBBMOILBAx7c2jwjxs%2FAgJkXZB0D%2BYyW6psU2K1qKPohBhNwFKPcsLy3%2BX31BXdRXSO%2F5DlcoBacmbYwJqnYRzc9c465pHzAPdATfPhnKXxBDwT30q5G746SvDPg0TBd%2FEnvVo%2BBqyCkNAP%2B%2BLVMgQ6CC%2FBUKxlN%2FwpH5Mx%2BB%2Bix%2B6RpTne6hRikBJ2mLj3R1bVabUD2BnZuOVeD8F89qx5XZD80DYoTfl7T0kdk78%2Bv5PXI08w2urmzgY6pgEvQaAxaFIJQFmoypMIjOnKmqNSFdkly0tFKI8ZP7pB6xWhK1Wb2cBsbb3A6bcHlAj3FYPgHFrl%2FXAAOYerNXeL0WuyCCRtWISnwpUF0pSucBgEt2jMxBDme1D8sFv6%2FQg%2B8cfo%2BFBopyMiKRvH5nl7iuuCC7c7Bjr4fCDRDbi1hLtGoG%2FPABDo1qzJIP0waVvpod%2BXObz%2Bwmq99q4S5o82VlFGwh38&X-Amz-Signature=3fb73f32821774f0946e613b8d41175d41f55abe32b96a966735807f21fa1223&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMZWGZX%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIBrTMS9ccABxSL%2BzR1CnV3T%2BUnAXKBGw7nqE6u3QJgeEAiAwPczfkN3U9mb95K7vdi1X%2F%2FovUre8LSn2yYHN8DEoBSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMrrjJ8fhCRR0yUeKJKtwDwgdsv0X8fp24AnoiXkcKtAtfRrp24Sq0abpQO%2FkbXxAJfWGlkMq6VQtMswAJEJtmJfJgiuetvdRrT88SFpB4gy2aUrZmpbbzZVSgKgruaoSfQWYvAenBhAgSG6eml9UAhM1gtq4obkV0xSLPRYFiYakDLmpvP0AuqqH7FrSPqb2SMuRFvU0BN%2BgILdjkQYhejiU7LQRCjFDJIRRIom5ie1uwG3c52C%2FrDq8EtZrq1v2gVvOUj9kU37gnAxPuDjxyvdDlDu1EH3%2BtQ51GDbwwPfNrotydE7BWZtepMJGDLvs5GjC79gstDsh0oEkhQr3mXyg%2BI3a2po5VK3Y9wK1sgoIYpBWcYL9959S8K7BUgZGAXheONo4Vr%2FXF24fgFsOYeaQ89LE1lmBBMOILBAx7c2jwjxs%2FAgJkXZB0D%2BYyW6psU2K1qKPohBhNwFKPcsLy3%2BX31BXdRXSO%2F5DlcoBacmbYwJqnYRzc9c465pHzAPdATfPhnKXxBDwT30q5G746SvDPg0TBd%2FEnvVo%2BBqyCkNAP%2B%2BLVMgQ6CC%2FBUKxlN%2FwpH5Mx%2BB%2Bix%2B6RpTne6hRikBJ2mLj3R1bVabUD2BnZuOVeD8F89qx5XZD80DYoTfl7T0kdk78%2Bv5PXI08w2urmzgY6pgEvQaAxaFIJQFmoypMIjOnKmqNSFdkly0tFKI8ZP7pB6xWhK1Wb2cBsbb3A6bcHlAj3FYPgHFrl%2FXAAOYerNXeL0WuyCCRtWISnwpUF0pSucBgEt2jMxBDme1D8sFv6%2FQg%2B8cfo%2BFBopyMiKRvH5nl7iuuCC7c7Bjr4fCDRDbi1hLtGoG%2FPABDo1qzJIP0waVvpod%2BXObz%2Bwmq99q4S5o82VlFGwh38&X-Amz-Signature=f485f10b98348d00aca03b48ddd38f87b9a1c42467832b3d01ae2bb21d5ba267&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMZWGZX%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIBrTMS9ccABxSL%2BzR1CnV3T%2BUnAXKBGw7nqE6u3QJgeEAiAwPczfkN3U9mb95K7vdi1X%2F%2FovUre8LSn2yYHN8DEoBSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMrrjJ8fhCRR0yUeKJKtwDwgdsv0X8fp24AnoiXkcKtAtfRrp24Sq0abpQO%2FkbXxAJfWGlkMq6VQtMswAJEJtmJfJgiuetvdRrT88SFpB4gy2aUrZmpbbzZVSgKgruaoSfQWYvAenBhAgSG6eml9UAhM1gtq4obkV0xSLPRYFiYakDLmpvP0AuqqH7FrSPqb2SMuRFvU0BN%2BgILdjkQYhejiU7LQRCjFDJIRRIom5ie1uwG3c52C%2FrDq8EtZrq1v2gVvOUj9kU37gnAxPuDjxyvdDlDu1EH3%2BtQ51GDbwwPfNrotydE7BWZtepMJGDLvs5GjC79gstDsh0oEkhQr3mXyg%2BI3a2po5VK3Y9wK1sgoIYpBWcYL9959S8K7BUgZGAXheONo4Vr%2FXF24fgFsOYeaQ89LE1lmBBMOILBAx7c2jwjxs%2FAgJkXZB0D%2BYyW6psU2K1qKPohBhNwFKPcsLy3%2BX31BXdRXSO%2F5DlcoBacmbYwJqnYRzc9c465pHzAPdATfPhnKXxBDwT30q5G746SvDPg0TBd%2FEnvVo%2BBqyCkNAP%2B%2BLVMgQ6CC%2FBUKxlN%2FwpH5Mx%2BB%2Bix%2B6RpTne6hRikBJ2mLj3R1bVabUD2BnZuOVeD8F89qx5XZD80DYoTfl7T0kdk78%2Bv5PXI08w2urmzgY6pgEvQaAxaFIJQFmoypMIjOnKmqNSFdkly0tFKI8ZP7pB6xWhK1Wb2cBsbb3A6bcHlAj3FYPgHFrl%2FXAAOYerNXeL0WuyCCRtWISnwpUF0pSucBgEt2jMxBDme1D8sFv6%2FQg%2B8cfo%2BFBopyMiKRvH5nl7iuuCC7c7Bjr4fCDRDbi1hLtGoG%2FPABDo1qzJIP0waVvpod%2BXObz%2Bwmq99q4S5o82VlFGwh38&X-Amz-Signature=e3e42f5f5e808c22367640bd7b98166c61ca3ce781dec5be37dad18a4b6f28ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMZWGZX%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIBrTMS9ccABxSL%2BzR1CnV3T%2BUnAXKBGw7nqE6u3QJgeEAiAwPczfkN3U9mb95K7vdi1X%2F%2FovUre8LSn2yYHN8DEoBSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMrrjJ8fhCRR0yUeKJKtwDwgdsv0X8fp24AnoiXkcKtAtfRrp24Sq0abpQO%2FkbXxAJfWGlkMq6VQtMswAJEJtmJfJgiuetvdRrT88SFpB4gy2aUrZmpbbzZVSgKgruaoSfQWYvAenBhAgSG6eml9UAhM1gtq4obkV0xSLPRYFiYakDLmpvP0AuqqH7FrSPqb2SMuRFvU0BN%2BgILdjkQYhejiU7LQRCjFDJIRRIom5ie1uwG3c52C%2FrDq8EtZrq1v2gVvOUj9kU37gnAxPuDjxyvdDlDu1EH3%2BtQ51GDbwwPfNrotydE7BWZtepMJGDLvs5GjC79gstDsh0oEkhQr3mXyg%2BI3a2po5VK3Y9wK1sgoIYpBWcYL9959S8K7BUgZGAXheONo4Vr%2FXF24fgFsOYeaQ89LE1lmBBMOILBAx7c2jwjxs%2FAgJkXZB0D%2BYyW6psU2K1qKPohBhNwFKPcsLy3%2BX31BXdRXSO%2F5DlcoBacmbYwJqnYRzc9c465pHzAPdATfPhnKXxBDwT30q5G746SvDPg0TBd%2FEnvVo%2BBqyCkNAP%2B%2BLVMgQ6CC%2FBUKxlN%2FwpH5Mx%2BB%2Bix%2B6RpTne6hRikBJ2mLj3R1bVabUD2BnZuOVeD8F89qx5XZD80DYoTfl7T0kdk78%2Bv5PXI08w2urmzgY6pgEvQaAxaFIJQFmoypMIjOnKmqNSFdkly0tFKI8ZP7pB6xWhK1Wb2cBsbb3A6bcHlAj3FYPgHFrl%2FXAAOYerNXeL0WuyCCRtWISnwpUF0pSucBgEt2jMxBDme1D8sFv6%2FQg%2B8cfo%2BFBopyMiKRvH5nl7iuuCC7c7Bjr4fCDRDbi1hLtGoG%2FPABDo1qzJIP0waVvpod%2BXObz%2Bwmq99q4S5o82VlFGwh38&X-Amz-Signature=ee5128fbf14d2a2284f8e433ca2a67972de1bef8b40e76f07bcd2f05ac1d885a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMZWGZX%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIBrTMS9ccABxSL%2BzR1CnV3T%2BUnAXKBGw7nqE6u3QJgeEAiAwPczfkN3U9mb95K7vdi1X%2F%2FovUre8LSn2yYHN8DEoBSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMrrjJ8fhCRR0yUeKJKtwDwgdsv0X8fp24AnoiXkcKtAtfRrp24Sq0abpQO%2FkbXxAJfWGlkMq6VQtMswAJEJtmJfJgiuetvdRrT88SFpB4gy2aUrZmpbbzZVSgKgruaoSfQWYvAenBhAgSG6eml9UAhM1gtq4obkV0xSLPRYFiYakDLmpvP0AuqqH7FrSPqb2SMuRFvU0BN%2BgILdjkQYhejiU7LQRCjFDJIRRIom5ie1uwG3c52C%2FrDq8EtZrq1v2gVvOUj9kU37gnAxPuDjxyvdDlDu1EH3%2BtQ51GDbwwPfNrotydE7BWZtepMJGDLvs5GjC79gstDsh0oEkhQr3mXyg%2BI3a2po5VK3Y9wK1sgoIYpBWcYL9959S8K7BUgZGAXheONo4Vr%2FXF24fgFsOYeaQ89LE1lmBBMOILBAx7c2jwjxs%2FAgJkXZB0D%2BYyW6psU2K1qKPohBhNwFKPcsLy3%2BX31BXdRXSO%2F5DlcoBacmbYwJqnYRzc9c465pHzAPdATfPhnKXxBDwT30q5G746SvDPg0TBd%2FEnvVo%2BBqyCkNAP%2B%2BLVMgQ6CC%2FBUKxlN%2FwpH5Mx%2BB%2Bix%2B6RpTne6hRikBJ2mLj3R1bVabUD2BnZuOVeD8F89qx5XZD80DYoTfl7T0kdk78%2Bv5PXI08w2urmzgY6pgEvQaAxaFIJQFmoypMIjOnKmqNSFdkly0tFKI8ZP7pB6xWhK1Wb2cBsbb3A6bcHlAj3FYPgHFrl%2FXAAOYerNXeL0WuyCCRtWISnwpUF0pSucBgEt2jMxBDme1D8sFv6%2FQg%2B8cfo%2BFBopyMiKRvH5nl7iuuCC7c7Bjr4fCDRDbi1hLtGoG%2FPABDo1qzJIP0waVvpod%2BXObz%2Bwmq99q4S5o82VlFGwh38&X-Amz-Signature=af3203a0c5ddca934b273b317721c4bb6cb2e549858f6bef9f0b1f162a04ede1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMZWGZX%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIBrTMS9ccABxSL%2BzR1CnV3T%2BUnAXKBGw7nqE6u3QJgeEAiAwPczfkN3U9mb95K7vdi1X%2F%2FovUre8LSn2yYHN8DEoBSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMrrjJ8fhCRR0yUeKJKtwDwgdsv0X8fp24AnoiXkcKtAtfRrp24Sq0abpQO%2FkbXxAJfWGlkMq6VQtMswAJEJtmJfJgiuetvdRrT88SFpB4gy2aUrZmpbbzZVSgKgruaoSfQWYvAenBhAgSG6eml9UAhM1gtq4obkV0xSLPRYFiYakDLmpvP0AuqqH7FrSPqb2SMuRFvU0BN%2BgILdjkQYhejiU7LQRCjFDJIRRIom5ie1uwG3c52C%2FrDq8EtZrq1v2gVvOUj9kU37gnAxPuDjxyvdDlDu1EH3%2BtQ51GDbwwPfNrotydE7BWZtepMJGDLvs5GjC79gstDsh0oEkhQr3mXyg%2BI3a2po5VK3Y9wK1sgoIYpBWcYL9959S8K7BUgZGAXheONo4Vr%2FXF24fgFsOYeaQ89LE1lmBBMOILBAx7c2jwjxs%2FAgJkXZB0D%2BYyW6psU2K1qKPohBhNwFKPcsLy3%2BX31BXdRXSO%2F5DlcoBacmbYwJqnYRzc9c465pHzAPdATfPhnKXxBDwT30q5G746SvDPg0TBd%2FEnvVo%2BBqyCkNAP%2B%2BLVMgQ6CC%2FBUKxlN%2FwpH5Mx%2BB%2Bix%2B6RpTne6hRikBJ2mLj3R1bVabUD2BnZuOVeD8F89qx5XZD80DYoTfl7T0kdk78%2Bv5PXI08w2urmzgY6pgEvQaAxaFIJQFmoypMIjOnKmqNSFdkly0tFKI8ZP7pB6xWhK1Wb2cBsbb3A6bcHlAj3FYPgHFrl%2FXAAOYerNXeL0WuyCCRtWISnwpUF0pSucBgEt2jMxBDme1D8sFv6%2FQg%2B8cfo%2BFBopyMiKRvH5nl7iuuCC7c7Bjr4fCDRDbi1hLtGoG%2FPABDo1qzJIP0waVvpod%2BXObz%2Bwmq99q4S5o82VlFGwh38&X-Amz-Signature=d21a844cbf03a37323ff5469f36674b3604f4778845e0e9fd11493da1ebac568&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIMZWGZX%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIBrTMS9ccABxSL%2BzR1CnV3T%2BUnAXKBGw7nqE6u3QJgeEAiAwPczfkN3U9mb95K7vdi1X%2F%2FovUre8LSn2yYHN8DEoBSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMrrjJ8fhCRR0yUeKJKtwDwgdsv0X8fp24AnoiXkcKtAtfRrp24Sq0abpQO%2FkbXxAJfWGlkMq6VQtMswAJEJtmJfJgiuetvdRrT88SFpB4gy2aUrZmpbbzZVSgKgruaoSfQWYvAenBhAgSG6eml9UAhM1gtq4obkV0xSLPRYFiYakDLmpvP0AuqqH7FrSPqb2SMuRFvU0BN%2BgILdjkQYhejiU7LQRCjFDJIRRIom5ie1uwG3c52C%2FrDq8EtZrq1v2gVvOUj9kU37gnAxPuDjxyvdDlDu1EH3%2BtQ51GDbwwPfNrotydE7BWZtepMJGDLvs5GjC79gstDsh0oEkhQr3mXyg%2BI3a2po5VK3Y9wK1sgoIYpBWcYL9959S8K7BUgZGAXheONo4Vr%2FXF24fgFsOYeaQ89LE1lmBBMOILBAx7c2jwjxs%2FAgJkXZB0D%2BYyW6psU2K1qKPohBhNwFKPcsLy3%2BX31BXdRXSO%2F5DlcoBacmbYwJqnYRzc9c465pHzAPdATfPhnKXxBDwT30q5G746SvDPg0TBd%2FEnvVo%2BBqyCkNAP%2B%2BLVMgQ6CC%2FBUKxlN%2FwpH5Mx%2BB%2Bix%2B6RpTne6hRikBJ2mLj3R1bVabUD2BnZuOVeD8F89qx5XZD80DYoTfl7T0kdk78%2Bv5PXI08w2urmzgY6pgEvQaAxaFIJQFmoypMIjOnKmqNSFdkly0tFKI8ZP7pB6xWhK1Wb2cBsbb3A6bcHlAj3FYPgHFrl%2FXAAOYerNXeL0WuyCCRtWISnwpUF0pSucBgEt2jMxBDme1D8sFv6%2FQg%2B8cfo%2BFBopyMiKRvH5nl7iuuCC7c7Bjr4fCDRDbi1hLtGoG%2FPABDo1qzJIP0waVvpod%2BXObz%2Bwmq99q4S5o82VlFGwh38&X-Amz-Signature=a4fc8390848cb6093c55465598cd7f9b4847dadcf3007bf31bf2622ca9beafaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

