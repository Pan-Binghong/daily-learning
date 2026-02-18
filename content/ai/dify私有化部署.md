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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X44S5E5E%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIElVIm0%2FXsqShf2NEGw%2BJJyvgq7XCMstvaRyV3AUCRMoAiEAgCcVU9d8XA%2FW27EcRUsSdBNKfJ9Dls%2BAM9GmA9q2mSQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHWPuSFSMBgrjs2i1SrcA8hmB5BLrm5HFfcp7fWq4vAgMppp9GZ5C3%2FCn%2F0Gnyb1sTGvrjwbsWHzN1f6sGIQK7D76xPGE8XuVCx%2F9kUOfE8iLY%2FonbJ1024NV%2Fum67HoNEMpdUoNGI8FdoZna8v1GHunV74pb%2B6rSSy%2F92fWpE3EeeASmZ2YRM%2FppFOLQ%2FPGatHtl2PVEifJnv6w%2B%2Bjz52riih5V3x%2FEjY3J3ist8nwzEMR8Mm9nOgoj80G72ahWorV8u5bzE9YsgX3gKvDg5TjDwQL0wrwPHfE8u%2BEVKfxULEzqZDKp8cPXNd7YlqN32tM0wA3aX2%2FBDdLSJ9TLUkZyp4TIa2FeprdgE9v4x0%2B9Y3isw%2F51aYE85LP2LBQNrgLkBT8n7UZI84NvlCr0AvnNq4%2FAMlIMDESzkOUZdvJ2xQfeoAAiVRAQDzQiQyE5fmWs3iqgIkFOTN1JlirDPa06fkNVOn1dDovEqOWe%2FBNC7ZfvhZJKfAVKDE%2FwWeT09PHhLNnd4V5d711mtzcQSFX8mAvuWq5rEVKqhktLspukDnMQ3%2FXrqZok54xQft434mc3q2sh5mwHju4FK5h7qkQ%2FEmO97MWUcccYuB4sMqISgP2LpAyrTXJEXtiPdz9GwnY5htlogDx9uM7dMKig1MwGOqUBdu0novigd3Jqjl49eBPvNaCF60aALmlr%2FjWI2AtUP5ihnW1pgHhFTHaiIDU3YlJuGSZ5FrSfGRin69WLDKq7QY4C4n9Ub%2BDrz6hZJf1NpZOlFNUPpNHZchuBF5j36wAdY4GfVvnHE4eM2pDwB97PoFlzCsF2yl04ml9SBYoCqvbGl2bA5FVu9991t1u%2FzZGNdZb%2FSBQzawF%2Boq0U%2Bl29EtyaraYu&X-Amz-Signature=e085746cb80841bcfd004aa5d0c6e32aefb1abd11df7c830c0e5f04ec02c9716&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X44S5E5E%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIElVIm0%2FXsqShf2NEGw%2BJJyvgq7XCMstvaRyV3AUCRMoAiEAgCcVU9d8XA%2FW27EcRUsSdBNKfJ9Dls%2BAM9GmA9q2mSQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHWPuSFSMBgrjs2i1SrcA8hmB5BLrm5HFfcp7fWq4vAgMppp9GZ5C3%2FCn%2F0Gnyb1sTGvrjwbsWHzN1f6sGIQK7D76xPGE8XuVCx%2F9kUOfE8iLY%2FonbJ1024NV%2Fum67HoNEMpdUoNGI8FdoZna8v1GHunV74pb%2B6rSSy%2F92fWpE3EeeASmZ2YRM%2FppFOLQ%2FPGatHtl2PVEifJnv6w%2B%2Bjz52riih5V3x%2FEjY3J3ist8nwzEMR8Mm9nOgoj80G72ahWorV8u5bzE9YsgX3gKvDg5TjDwQL0wrwPHfE8u%2BEVKfxULEzqZDKp8cPXNd7YlqN32tM0wA3aX2%2FBDdLSJ9TLUkZyp4TIa2FeprdgE9v4x0%2B9Y3isw%2F51aYE85LP2LBQNrgLkBT8n7UZI84NvlCr0AvnNq4%2FAMlIMDESzkOUZdvJ2xQfeoAAiVRAQDzQiQyE5fmWs3iqgIkFOTN1JlirDPa06fkNVOn1dDovEqOWe%2FBNC7ZfvhZJKfAVKDE%2FwWeT09PHhLNnd4V5d711mtzcQSFX8mAvuWq5rEVKqhktLspukDnMQ3%2FXrqZok54xQft434mc3q2sh5mwHju4FK5h7qkQ%2FEmO97MWUcccYuB4sMqISgP2LpAyrTXJEXtiPdz9GwnY5htlogDx9uM7dMKig1MwGOqUBdu0novigd3Jqjl49eBPvNaCF60aALmlr%2FjWI2AtUP5ihnW1pgHhFTHaiIDU3YlJuGSZ5FrSfGRin69WLDKq7QY4C4n9Ub%2BDrz6hZJf1NpZOlFNUPpNHZchuBF5j36wAdY4GfVvnHE4eM2pDwB97PoFlzCsF2yl04ml9SBYoCqvbGl2bA5FVu9991t1u%2FzZGNdZb%2FSBQzawF%2Boq0U%2Bl29EtyaraYu&X-Amz-Signature=17e547debd250910ac84f8ac2dea5100101a79f9f8a9058bbab4b88421ef9907&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X44S5E5E%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIElVIm0%2FXsqShf2NEGw%2BJJyvgq7XCMstvaRyV3AUCRMoAiEAgCcVU9d8XA%2FW27EcRUsSdBNKfJ9Dls%2BAM9GmA9q2mSQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHWPuSFSMBgrjs2i1SrcA8hmB5BLrm5HFfcp7fWq4vAgMppp9GZ5C3%2FCn%2F0Gnyb1sTGvrjwbsWHzN1f6sGIQK7D76xPGE8XuVCx%2F9kUOfE8iLY%2FonbJ1024NV%2Fum67HoNEMpdUoNGI8FdoZna8v1GHunV74pb%2B6rSSy%2F92fWpE3EeeASmZ2YRM%2FppFOLQ%2FPGatHtl2PVEifJnv6w%2B%2Bjz52riih5V3x%2FEjY3J3ist8nwzEMR8Mm9nOgoj80G72ahWorV8u5bzE9YsgX3gKvDg5TjDwQL0wrwPHfE8u%2BEVKfxULEzqZDKp8cPXNd7YlqN32tM0wA3aX2%2FBDdLSJ9TLUkZyp4TIa2FeprdgE9v4x0%2B9Y3isw%2F51aYE85LP2LBQNrgLkBT8n7UZI84NvlCr0AvnNq4%2FAMlIMDESzkOUZdvJ2xQfeoAAiVRAQDzQiQyE5fmWs3iqgIkFOTN1JlirDPa06fkNVOn1dDovEqOWe%2FBNC7ZfvhZJKfAVKDE%2FwWeT09PHhLNnd4V5d711mtzcQSFX8mAvuWq5rEVKqhktLspukDnMQ3%2FXrqZok54xQft434mc3q2sh5mwHju4FK5h7qkQ%2FEmO97MWUcccYuB4sMqISgP2LpAyrTXJEXtiPdz9GwnY5htlogDx9uM7dMKig1MwGOqUBdu0novigd3Jqjl49eBPvNaCF60aALmlr%2FjWI2AtUP5ihnW1pgHhFTHaiIDU3YlJuGSZ5FrSfGRin69WLDKq7QY4C4n9Ub%2BDrz6hZJf1NpZOlFNUPpNHZchuBF5j36wAdY4GfVvnHE4eM2pDwB97PoFlzCsF2yl04ml9SBYoCqvbGl2bA5FVu9991t1u%2FzZGNdZb%2FSBQzawF%2Boq0U%2Bl29EtyaraYu&X-Amz-Signature=47a6a42f457bd8822c5913dfec35d7974608377f84e4ea679eee03863bcbbd91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X44S5E5E%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIElVIm0%2FXsqShf2NEGw%2BJJyvgq7XCMstvaRyV3AUCRMoAiEAgCcVU9d8XA%2FW27EcRUsSdBNKfJ9Dls%2BAM9GmA9q2mSQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHWPuSFSMBgrjs2i1SrcA8hmB5BLrm5HFfcp7fWq4vAgMppp9GZ5C3%2FCn%2F0Gnyb1sTGvrjwbsWHzN1f6sGIQK7D76xPGE8XuVCx%2F9kUOfE8iLY%2FonbJ1024NV%2Fum67HoNEMpdUoNGI8FdoZna8v1GHunV74pb%2B6rSSy%2F92fWpE3EeeASmZ2YRM%2FppFOLQ%2FPGatHtl2PVEifJnv6w%2B%2Bjz52riih5V3x%2FEjY3J3ist8nwzEMR8Mm9nOgoj80G72ahWorV8u5bzE9YsgX3gKvDg5TjDwQL0wrwPHfE8u%2BEVKfxULEzqZDKp8cPXNd7YlqN32tM0wA3aX2%2FBDdLSJ9TLUkZyp4TIa2FeprdgE9v4x0%2B9Y3isw%2F51aYE85LP2LBQNrgLkBT8n7UZI84NvlCr0AvnNq4%2FAMlIMDESzkOUZdvJ2xQfeoAAiVRAQDzQiQyE5fmWs3iqgIkFOTN1JlirDPa06fkNVOn1dDovEqOWe%2FBNC7ZfvhZJKfAVKDE%2FwWeT09PHhLNnd4V5d711mtzcQSFX8mAvuWq5rEVKqhktLspukDnMQ3%2FXrqZok54xQft434mc3q2sh5mwHju4FK5h7qkQ%2FEmO97MWUcccYuB4sMqISgP2LpAyrTXJEXtiPdz9GwnY5htlogDx9uM7dMKig1MwGOqUBdu0novigd3Jqjl49eBPvNaCF60aALmlr%2FjWI2AtUP5ihnW1pgHhFTHaiIDU3YlJuGSZ5FrSfGRin69WLDKq7QY4C4n9Ub%2BDrz6hZJf1NpZOlFNUPpNHZchuBF5j36wAdY4GfVvnHE4eM2pDwB97PoFlzCsF2yl04ml9SBYoCqvbGl2bA5FVu9991t1u%2FzZGNdZb%2FSBQzawF%2Boq0U%2Bl29EtyaraYu&X-Amz-Signature=f0a2bbe58bb930dfa03ae702ba9a7fba10eb36fba66fcb69631039d9cc437b01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X44S5E5E%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIElVIm0%2FXsqShf2NEGw%2BJJyvgq7XCMstvaRyV3AUCRMoAiEAgCcVU9d8XA%2FW27EcRUsSdBNKfJ9Dls%2BAM9GmA9q2mSQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHWPuSFSMBgrjs2i1SrcA8hmB5BLrm5HFfcp7fWq4vAgMppp9GZ5C3%2FCn%2F0Gnyb1sTGvrjwbsWHzN1f6sGIQK7D76xPGE8XuVCx%2F9kUOfE8iLY%2FonbJ1024NV%2Fum67HoNEMpdUoNGI8FdoZna8v1GHunV74pb%2B6rSSy%2F92fWpE3EeeASmZ2YRM%2FppFOLQ%2FPGatHtl2PVEifJnv6w%2B%2Bjz52riih5V3x%2FEjY3J3ist8nwzEMR8Mm9nOgoj80G72ahWorV8u5bzE9YsgX3gKvDg5TjDwQL0wrwPHfE8u%2BEVKfxULEzqZDKp8cPXNd7YlqN32tM0wA3aX2%2FBDdLSJ9TLUkZyp4TIa2FeprdgE9v4x0%2B9Y3isw%2F51aYE85LP2LBQNrgLkBT8n7UZI84NvlCr0AvnNq4%2FAMlIMDESzkOUZdvJ2xQfeoAAiVRAQDzQiQyE5fmWs3iqgIkFOTN1JlirDPa06fkNVOn1dDovEqOWe%2FBNC7ZfvhZJKfAVKDE%2FwWeT09PHhLNnd4V5d711mtzcQSFX8mAvuWq5rEVKqhktLspukDnMQ3%2FXrqZok54xQft434mc3q2sh5mwHju4FK5h7qkQ%2FEmO97MWUcccYuB4sMqISgP2LpAyrTXJEXtiPdz9GwnY5htlogDx9uM7dMKig1MwGOqUBdu0novigd3Jqjl49eBPvNaCF60aALmlr%2FjWI2AtUP5ihnW1pgHhFTHaiIDU3YlJuGSZ5FrSfGRin69WLDKq7QY4C4n9Ub%2BDrz6hZJf1NpZOlFNUPpNHZchuBF5j36wAdY4GfVvnHE4eM2pDwB97PoFlzCsF2yl04ml9SBYoCqvbGl2bA5FVu9991t1u%2FzZGNdZb%2FSBQzawF%2Boq0U%2Bl29EtyaraYu&X-Amz-Signature=3b933d99d6f1971531b0ff86921c9bb7a51f9cc234916768135d08dce2570ad4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X44S5E5E%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIElVIm0%2FXsqShf2NEGw%2BJJyvgq7XCMstvaRyV3AUCRMoAiEAgCcVU9d8XA%2FW27EcRUsSdBNKfJ9Dls%2BAM9GmA9q2mSQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHWPuSFSMBgrjs2i1SrcA8hmB5BLrm5HFfcp7fWq4vAgMppp9GZ5C3%2FCn%2F0Gnyb1sTGvrjwbsWHzN1f6sGIQK7D76xPGE8XuVCx%2F9kUOfE8iLY%2FonbJ1024NV%2Fum67HoNEMpdUoNGI8FdoZna8v1GHunV74pb%2B6rSSy%2F92fWpE3EeeASmZ2YRM%2FppFOLQ%2FPGatHtl2PVEifJnv6w%2B%2Bjz52riih5V3x%2FEjY3J3ist8nwzEMR8Mm9nOgoj80G72ahWorV8u5bzE9YsgX3gKvDg5TjDwQL0wrwPHfE8u%2BEVKfxULEzqZDKp8cPXNd7YlqN32tM0wA3aX2%2FBDdLSJ9TLUkZyp4TIa2FeprdgE9v4x0%2B9Y3isw%2F51aYE85LP2LBQNrgLkBT8n7UZI84NvlCr0AvnNq4%2FAMlIMDESzkOUZdvJ2xQfeoAAiVRAQDzQiQyE5fmWs3iqgIkFOTN1JlirDPa06fkNVOn1dDovEqOWe%2FBNC7ZfvhZJKfAVKDE%2FwWeT09PHhLNnd4V5d711mtzcQSFX8mAvuWq5rEVKqhktLspukDnMQ3%2FXrqZok54xQft434mc3q2sh5mwHju4FK5h7qkQ%2FEmO97MWUcccYuB4sMqISgP2LpAyrTXJEXtiPdz9GwnY5htlogDx9uM7dMKig1MwGOqUBdu0novigd3Jqjl49eBPvNaCF60aALmlr%2FjWI2AtUP5ihnW1pgHhFTHaiIDU3YlJuGSZ5FrSfGRin69WLDKq7QY4C4n9Ub%2BDrz6hZJf1NpZOlFNUPpNHZchuBF5j36wAdY4GfVvnHE4eM2pDwB97PoFlzCsF2yl04ml9SBYoCqvbGl2bA5FVu9991t1u%2FzZGNdZb%2FSBQzawF%2Boq0U%2Bl29EtyaraYu&X-Amz-Signature=7b9ff08af86c2248fdb6ef69443d0c8cf48dabaca76141ad047ffb665dc3045e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X44S5E5E%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIElVIm0%2FXsqShf2NEGw%2BJJyvgq7XCMstvaRyV3AUCRMoAiEAgCcVU9d8XA%2FW27EcRUsSdBNKfJ9Dls%2BAM9GmA9q2mSQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHWPuSFSMBgrjs2i1SrcA8hmB5BLrm5HFfcp7fWq4vAgMppp9GZ5C3%2FCn%2F0Gnyb1sTGvrjwbsWHzN1f6sGIQK7D76xPGE8XuVCx%2F9kUOfE8iLY%2FonbJ1024NV%2Fum67HoNEMpdUoNGI8FdoZna8v1GHunV74pb%2B6rSSy%2F92fWpE3EeeASmZ2YRM%2FppFOLQ%2FPGatHtl2PVEifJnv6w%2B%2Bjz52riih5V3x%2FEjY3J3ist8nwzEMR8Mm9nOgoj80G72ahWorV8u5bzE9YsgX3gKvDg5TjDwQL0wrwPHfE8u%2BEVKfxULEzqZDKp8cPXNd7YlqN32tM0wA3aX2%2FBDdLSJ9TLUkZyp4TIa2FeprdgE9v4x0%2B9Y3isw%2F51aYE85LP2LBQNrgLkBT8n7UZI84NvlCr0AvnNq4%2FAMlIMDESzkOUZdvJ2xQfeoAAiVRAQDzQiQyE5fmWs3iqgIkFOTN1JlirDPa06fkNVOn1dDovEqOWe%2FBNC7ZfvhZJKfAVKDE%2FwWeT09PHhLNnd4V5d711mtzcQSFX8mAvuWq5rEVKqhktLspukDnMQ3%2FXrqZok54xQft434mc3q2sh5mwHju4FK5h7qkQ%2FEmO97MWUcccYuB4sMqISgP2LpAyrTXJEXtiPdz9GwnY5htlogDx9uM7dMKig1MwGOqUBdu0novigd3Jqjl49eBPvNaCF60aALmlr%2FjWI2AtUP5ihnW1pgHhFTHaiIDU3YlJuGSZ5FrSfGRin69WLDKq7QY4C4n9Ub%2BDrz6hZJf1NpZOlFNUPpNHZchuBF5j36wAdY4GfVvnHE4eM2pDwB97PoFlzCsF2yl04ml9SBYoCqvbGl2bA5FVu9991t1u%2FzZGNdZb%2FSBQzawF%2Boq0U%2Bl29EtyaraYu&X-Amz-Signature=3060e8a7c29f7a98393cf73853d5f13177c37cb66ab1e9c697f03dca2f81ec98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X44S5E5E%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIElVIm0%2FXsqShf2NEGw%2BJJyvgq7XCMstvaRyV3AUCRMoAiEAgCcVU9d8XA%2FW27EcRUsSdBNKfJ9Dls%2BAM9GmA9q2mSQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHWPuSFSMBgrjs2i1SrcA8hmB5BLrm5HFfcp7fWq4vAgMppp9GZ5C3%2FCn%2F0Gnyb1sTGvrjwbsWHzN1f6sGIQK7D76xPGE8XuVCx%2F9kUOfE8iLY%2FonbJ1024NV%2Fum67HoNEMpdUoNGI8FdoZna8v1GHunV74pb%2B6rSSy%2F92fWpE3EeeASmZ2YRM%2FppFOLQ%2FPGatHtl2PVEifJnv6w%2B%2Bjz52riih5V3x%2FEjY3J3ist8nwzEMR8Mm9nOgoj80G72ahWorV8u5bzE9YsgX3gKvDg5TjDwQL0wrwPHfE8u%2BEVKfxULEzqZDKp8cPXNd7YlqN32tM0wA3aX2%2FBDdLSJ9TLUkZyp4TIa2FeprdgE9v4x0%2B9Y3isw%2F51aYE85LP2LBQNrgLkBT8n7UZI84NvlCr0AvnNq4%2FAMlIMDESzkOUZdvJ2xQfeoAAiVRAQDzQiQyE5fmWs3iqgIkFOTN1JlirDPa06fkNVOn1dDovEqOWe%2FBNC7ZfvhZJKfAVKDE%2FwWeT09PHhLNnd4V5d711mtzcQSFX8mAvuWq5rEVKqhktLspukDnMQ3%2FXrqZok54xQft434mc3q2sh5mwHju4FK5h7qkQ%2FEmO97MWUcccYuB4sMqISgP2LpAyrTXJEXtiPdz9GwnY5htlogDx9uM7dMKig1MwGOqUBdu0novigd3Jqjl49eBPvNaCF60aALmlr%2FjWI2AtUP5ihnW1pgHhFTHaiIDU3YlJuGSZ5FrSfGRin69WLDKq7QY4C4n9Ub%2BDrz6hZJf1NpZOlFNUPpNHZchuBF5j36wAdY4GfVvnHE4eM2pDwB97PoFlzCsF2yl04ml9SBYoCqvbGl2bA5FVu9991t1u%2FzZGNdZb%2FSBQzawF%2Boq0U%2Bl29EtyaraYu&X-Amz-Signature=e8cc45be7a23191a7a43cc9620ac39e0db94fc4a08b14ca26082d1ae36e04c85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X44S5E5E%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIElVIm0%2FXsqShf2NEGw%2BJJyvgq7XCMstvaRyV3AUCRMoAiEAgCcVU9d8XA%2FW27EcRUsSdBNKfJ9Dls%2BAM9GmA9q2mSQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHWPuSFSMBgrjs2i1SrcA8hmB5BLrm5HFfcp7fWq4vAgMppp9GZ5C3%2FCn%2F0Gnyb1sTGvrjwbsWHzN1f6sGIQK7D76xPGE8XuVCx%2F9kUOfE8iLY%2FonbJ1024NV%2Fum67HoNEMpdUoNGI8FdoZna8v1GHunV74pb%2B6rSSy%2F92fWpE3EeeASmZ2YRM%2FppFOLQ%2FPGatHtl2PVEifJnv6w%2B%2Bjz52riih5V3x%2FEjY3J3ist8nwzEMR8Mm9nOgoj80G72ahWorV8u5bzE9YsgX3gKvDg5TjDwQL0wrwPHfE8u%2BEVKfxULEzqZDKp8cPXNd7YlqN32tM0wA3aX2%2FBDdLSJ9TLUkZyp4TIa2FeprdgE9v4x0%2B9Y3isw%2F51aYE85LP2LBQNrgLkBT8n7UZI84NvlCr0AvnNq4%2FAMlIMDESzkOUZdvJ2xQfeoAAiVRAQDzQiQyE5fmWs3iqgIkFOTN1JlirDPa06fkNVOn1dDovEqOWe%2FBNC7ZfvhZJKfAVKDE%2FwWeT09PHhLNnd4V5d711mtzcQSFX8mAvuWq5rEVKqhktLspukDnMQ3%2FXrqZok54xQft434mc3q2sh5mwHju4FK5h7qkQ%2FEmO97MWUcccYuB4sMqISgP2LpAyrTXJEXtiPdz9GwnY5htlogDx9uM7dMKig1MwGOqUBdu0novigd3Jqjl49eBPvNaCF60aALmlr%2FjWI2AtUP5ihnW1pgHhFTHaiIDU3YlJuGSZ5FrSfGRin69WLDKq7QY4C4n9Ub%2BDrz6hZJf1NpZOlFNUPpNHZchuBF5j36wAdY4GfVvnHE4eM2pDwB97PoFlzCsF2yl04ml9SBYoCqvbGl2bA5FVu9991t1u%2FzZGNdZb%2FSBQzawF%2Boq0U%2Bl29EtyaraYu&X-Amz-Signature=a15faab2a49ab19abe265ef4865dd44dcba7a9b00f2bbdce4a0ff078753978ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X44S5E5E%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIElVIm0%2FXsqShf2NEGw%2BJJyvgq7XCMstvaRyV3AUCRMoAiEAgCcVU9d8XA%2FW27EcRUsSdBNKfJ9Dls%2BAM9GmA9q2mSQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHWPuSFSMBgrjs2i1SrcA8hmB5BLrm5HFfcp7fWq4vAgMppp9GZ5C3%2FCn%2F0Gnyb1sTGvrjwbsWHzN1f6sGIQK7D76xPGE8XuVCx%2F9kUOfE8iLY%2FonbJ1024NV%2Fum67HoNEMpdUoNGI8FdoZna8v1GHunV74pb%2B6rSSy%2F92fWpE3EeeASmZ2YRM%2FppFOLQ%2FPGatHtl2PVEifJnv6w%2B%2Bjz52riih5V3x%2FEjY3J3ist8nwzEMR8Mm9nOgoj80G72ahWorV8u5bzE9YsgX3gKvDg5TjDwQL0wrwPHfE8u%2BEVKfxULEzqZDKp8cPXNd7YlqN32tM0wA3aX2%2FBDdLSJ9TLUkZyp4TIa2FeprdgE9v4x0%2B9Y3isw%2F51aYE85LP2LBQNrgLkBT8n7UZI84NvlCr0AvnNq4%2FAMlIMDESzkOUZdvJ2xQfeoAAiVRAQDzQiQyE5fmWs3iqgIkFOTN1JlirDPa06fkNVOn1dDovEqOWe%2FBNC7ZfvhZJKfAVKDE%2FwWeT09PHhLNnd4V5d711mtzcQSFX8mAvuWq5rEVKqhktLspukDnMQ3%2FXrqZok54xQft434mc3q2sh5mwHju4FK5h7qkQ%2FEmO97MWUcccYuB4sMqISgP2LpAyrTXJEXtiPdz9GwnY5htlogDx9uM7dMKig1MwGOqUBdu0novigd3Jqjl49eBPvNaCF60aALmlr%2FjWI2AtUP5ihnW1pgHhFTHaiIDU3YlJuGSZ5FrSfGRin69WLDKq7QY4C4n9Ub%2BDrz6hZJf1NpZOlFNUPpNHZchuBF5j36wAdY4GfVvnHE4eM2pDwB97PoFlzCsF2yl04ml9SBYoCqvbGl2bA5FVu9991t1u%2FzZGNdZb%2FSBQzawF%2Boq0U%2Bl29EtyaraYu&X-Amz-Signature=47e26452f0954c5d206dada1183e69a2b804bb7ec29326730101724bb56e5512&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

