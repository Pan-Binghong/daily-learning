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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHKF6IR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIAF7pOEUjdk1skWMWfBHEPgHmwyjSoAmzIAB2Wg%2FZpHDAiAg0VsLTXfk7EEX2pvi7cWi9UzLtR9gfQNjv6y2YUYjGir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMZZzoOWvLhmg%2BZhS4KtwDbeW763cIcs69Zv%2Bdxi%2B3Mi6vmF7y8iT1zKnpemhMIKb9CqEG1Z%2FfbmkzeIIvjan0ygODqXFjSbmESrHg9QdnunKOp1X3O%2F7cLdnEXAAQ2koffX%2F6HxJzHQaTyiAZ02ej9dBpKJjVfVR%2Bup8fKz5%2Fu6Vx073blJz5Ktx7ZqeOCZhzJHLXR62xDZmbuCVkDNLE2deaDRdkg%2BHsozrfWwpvzwMogBMmfkL%2Fh0w2V1o2lyrEj2PBOEEC5hXf4IJdzSyTSq40i%2Fk2JkZ%2BZE1mVYq1%2FxigJE%2BYS9crJPXZ%2Bx0YlZN3ox0OL5k4AprMflvIVEJuIy%2BQ40QU75rW3TgLbIWRxIQ5%2BDOOxURgkBg8Qyrz%2BJMCibX8vuw6zq4q1RnKF6baKJ6S%2B5VYsBqgTmHmpPtLcjJo2zQ8gp5DzYDbB53TwVaoBi9L%2FJj28m1PcJXnfy3P1z%2BB1qARPNyInvR0cTjfCi2VeqnxhjerODq9UBRQCyaDn%2FgYi%2Bfj9%2FvnSBviAzV%2FBIh5Rrrpvpm2u0Prg5myA1fxGrUlx8T5Ab%2BewwgVudEVJ00VIlEloJuR5FIKC1Q4%2BP%2F9PeqJlU7DOPnasgCamxkEi6%2FHx4zO8irQ0R%2F3ggmkHAqfnF7xJr61OKQwqOmKzAY6pgG67igBDpQW5gLsaF5oNFtCIQAuQKSXcfnqr32CY6WnYtIsk3jDuFqcRIBrM7ELs4YX7vf20%2FLTa5eGIND6Tu%2BW%2BzI9zJdijTRJhMfiUAaSQED19%2BiEDPbba2Au%2Fce8brlnprz6toAhweZDm2ujqWNWdUeasxbSgxWBUmPkKfPXk28o33%2BgyFQr%2BBHViUOaxZkM6cODYeSeLzC7qWJv0vdAgDTuLhAS&X-Amz-Signature=814a8e185ea04320a0196cd69a5fed2f736fd0d028b6a0bf85f4f7e1e15f926c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHKF6IR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIAF7pOEUjdk1skWMWfBHEPgHmwyjSoAmzIAB2Wg%2FZpHDAiAg0VsLTXfk7EEX2pvi7cWi9UzLtR9gfQNjv6y2YUYjGir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMZZzoOWvLhmg%2BZhS4KtwDbeW763cIcs69Zv%2Bdxi%2B3Mi6vmF7y8iT1zKnpemhMIKb9CqEG1Z%2FfbmkzeIIvjan0ygODqXFjSbmESrHg9QdnunKOp1X3O%2F7cLdnEXAAQ2koffX%2F6HxJzHQaTyiAZ02ej9dBpKJjVfVR%2Bup8fKz5%2Fu6Vx073blJz5Ktx7ZqeOCZhzJHLXR62xDZmbuCVkDNLE2deaDRdkg%2BHsozrfWwpvzwMogBMmfkL%2Fh0w2V1o2lyrEj2PBOEEC5hXf4IJdzSyTSq40i%2Fk2JkZ%2BZE1mVYq1%2FxigJE%2BYS9crJPXZ%2Bx0YlZN3ox0OL5k4AprMflvIVEJuIy%2BQ40QU75rW3TgLbIWRxIQ5%2BDOOxURgkBg8Qyrz%2BJMCibX8vuw6zq4q1RnKF6baKJ6S%2B5VYsBqgTmHmpPtLcjJo2zQ8gp5DzYDbB53TwVaoBi9L%2FJj28m1PcJXnfy3P1z%2BB1qARPNyInvR0cTjfCi2VeqnxhjerODq9UBRQCyaDn%2FgYi%2Bfj9%2FvnSBviAzV%2FBIh5Rrrpvpm2u0Prg5myA1fxGrUlx8T5Ab%2BewwgVudEVJ00VIlEloJuR5FIKC1Q4%2BP%2F9PeqJlU7DOPnasgCamxkEi6%2FHx4zO8irQ0R%2F3ggmkHAqfnF7xJr61OKQwqOmKzAY6pgG67igBDpQW5gLsaF5oNFtCIQAuQKSXcfnqr32CY6WnYtIsk3jDuFqcRIBrM7ELs4YX7vf20%2FLTa5eGIND6Tu%2BW%2BzI9zJdijTRJhMfiUAaSQED19%2BiEDPbba2Au%2Fce8brlnprz6toAhweZDm2ujqWNWdUeasxbSgxWBUmPkKfPXk28o33%2BgyFQr%2BBHViUOaxZkM6cODYeSeLzC7qWJv0vdAgDTuLhAS&X-Amz-Signature=56bf8a46a942aa812e98c66d64320b940b361cfe0b09a9ba795885517de64bd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHKF6IR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIAF7pOEUjdk1skWMWfBHEPgHmwyjSoAmzIAB2Wg%2FZpHDAiAg0VsLTXfk7EEX2pvi7cWi9UzLtR9gfQNjv6y2YUYjGir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMZZzoOWvLhmg%2BZhS4KtwDbeW763cIcs69Zv%2Bdxi%2B3Mi6vmF7y8iT1zKnpemhMIKb9CqEG1Z%2FfbmkzeIIvjan0ygODqXFjSbmESrHg9QdnunKOp1X3O%2F7cLdnEXAAQ2koffX%2F6HxJzHQaTyiAZ02ej9dBpKJjVfVR%2Bup8fKz5%2Fu6Vx073blJz5Ktx7ZqeOCZhzJHLXR62xDZmbuCVkDNLE2deaDRdkg%2BHsozrfWwpvzwMogBMmfkL%2Fh0w2V1o2lyrEj2PBOEEC5hXf4IJdzSyTSq40i%2Fk2JkZ%2BZE1mVYq1%2FxigJE%2BYS9crJPXZ%2Bx0YlZN3ox0OL5k4AprMflvIVEJuIy%2BQ40QU75rW3TgLbIWRxIQ5%2BDOOxURgkBg8Qyrz%2BJMCibX8vuw6zq4q1RnKF6baKJ6S%2B5VYsBqgTmHmpPtLcjJo2zQ8gp5DzYDbB53TwVaoBi9L%2FJj28m1PcJXnfy3P1z%2BB1qARPNyInvR0cTjfCi2VeqnxhjerODq9UBRQCyaDn%2FgYi%2Bfj9%2FvnSBviAzV%2FBIh5Rrrpvpm2u0Prg5myA1fxGrUlx8T5Ab%2BewwgVudEVJ00VIlEloJuR5FIKC1Q4%2BP%2F9PeqJlU7DOPnasgCamxkEi6%2FHx4zO8irQ0R%2F3ggmkHAqfnF7xJr61OKQwqOmKzAY6pgG67igBDpQW5gLsaF5oNFtCIQAuQKSXcfnqr32CY6WnYtIsk3jDuFqcRIBrM7ELs4YX7vf20%2FLTa5eGIND6Tu%2BW%2BzI9zJdijTRJhMfiUAaSQED19%2BiEDPbba2Au%2Fce8brlnprz6toAhweZDm2ujqWNWdUeasxbSgxWBUmPkKfPXk28o33%2BgyFQr%2BBHViUOaxZkM6cODYeSeLzC7qWJv0vdAgDTuLhAS&X-Amz-Signature=97b3e53458c581a518b7381498f2b1c5fac3a23640cb4f42e1f9d022f0261a43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHKF6IR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIAF7pOEUjdk1skWMWfBHEPgHmwyjSoAmzIAB2Wg%2FZpHDAiAg0VsLTXfk7EEX2pvi7cWi9UzLtR9gfQNjv6y2YUYjGir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMZZzoOWvLhmg%2BZhS4KtwDbeW763cIcs69Zv%2Bdxi%2B3Mi6vmF7y8iT1zKnpemhMIKb9CqEG1Z%2FfbmkzeIIvjan0ygODqXFjSbmESrHg9QdnunKOp1X3O%2F7cLdnEXAAQ2koffX%2F6HxJzHQaTyiAZ02ej9dBpKJjVfVR%2Bup8fKz5%2Fu6Vx073blJz5Ktx7ZqeOCZhzJHLXR62xDZmbuCVkDNLE2deaDRdkg%2BHsozrfWwpvzwMogBMmfkL%2Fh0w2V1o2lyrEj2PBOEEC5hXf4IJdzSyTSq40i%2Fk2JkZ%2BZE1mVYq1%2FxigJE%2BYS9crJPXZ%2Bx0YlZN3ox0OL5k4AprMflvIVEJuIy%2BQ40QU75rW3TgLbIWRxIQ5%2BDOOxURgkBg8Qyrz%2BJMCibX8vuw6zq4q1RnKF6baKJ6S%2B5VYsBqgTmHmpPtLcjJo2zQ8gp5DzYDbB53TwVaoBi9L%2FJj28m1PcJXnfy3P1z%2BB1qARPNyInvR0cTjfCi2VeqnxhjerODq9UBRQCyaDn%2FgYi%2Bfj9%2FvnSBviAzV%2FBIh5Rrrpvpm2u0Prg5myA1fxGrUlx8T5Ab%2BewwgVudEVJ00VIlEloJuR5FIKC1Q4%2BP%2F9PeqJlU7DOPnasgCamxkEi6%2FHx4zO8irQ0R%2F3ggmkHAqfnF7xJr61OKQwqOmKzAY6pgG67igBDpQW5gLsaF5oNFtCIQAuQKSXcfnqr32CY6WnYtIsk3jDuFqcRIBrM7ELs4YX7vf20%2FLTa5eGIND6Tu%2BW%2BzI9zJdijTRJhMfiUAaSQED19%2BiEDPbba2Au%2Fce8brlnprz6toAhweZDm2ujqWNWdUeasxbSgxWBUmPkKfPXk28o33%2BgyFQr%2BBHViUOaxZkM6cODYeSeLzC7qWJv0vdAgDTuLhAS&X-Amz-Signature=523f75bca515c53be621136c7d395bb4a987352a2d538d8b581ed2d4c6bfc373&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHKF6IR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIAF7pOEUjdk1skWMWfBHEPgHmwyjSoAmzIAB2Wg%2FZpHDAiAg0VsLTXfk7EEX2pvi7cWi9UzLtR9gfQNjv6y2YUYjGir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMZZzoOWvLhmg%2BZhS4KtwDbeW763cIcs69Zv%2Bdxi%2B3Mi6vmF7y8iT1zKnpemhMIKb9CqEG1Z%2FfbmkzeIIvjan0ygODqXFjSbmESrHg9QdnunKOp1X3O%2F7cLdnEXAAQ2koffX%2F6HxJzHQaTyiAZ02ej9dBpKJjVfVR%2Bup8fKz5%2Fu6Vx073blJz5Ktx7ZqeOCZhzJHLXR62xDZmbuCVkDNLE2deaDRdkg%2BHsozrfWwpvzwMogBMmfkL%2Fh0w2V1o2lyrEj2PBOEEC5hXf4IJdzSyTSq40i%2Fk2JkZ%2BZE1mVYq1%2FxigJE%2BYS9crJPXZ%2Bx0YlZN3ox0OL5k4AprMflvIVEJuIy%2BQ40QU75rW3TgLbIWRxIQ5%2BDOOxURgkBg8Qyrz%2BJMCibX8vuw6zq4q1RnKF6baKJ6S%2B5VYsBqgTmHmpPtLcjJo2zQ8gp5DzYDbB53TwVaoBi9L%2FJj28m1PcJXnfy3P1z%2BB1qARPNyInvR0cTjfCi2VeqnxhjerODq9UBRQCyaDn%2FgYi%2Bfj9%2FvnSBviAzV%2FBIh5Rrrpvpm2u0Prg5myA1fxGrUlx8T5Ab%2BewwgVudEVJ00VIlEloJuR5FIKC1Q4%2BP%2F9PeqJlU7DOPnasgCamxkEi6%2FHx4zO8irQ0R%2F3ggmkHAqfnF7xJr61OKQwqOmKzAY6pgG67igBDpQW5gLsaF5oNFtCIQAuQKSXcfnqr32CY6WnYtIsk3jDuFqcRIBrM7ELs4YX7vf20%2FLTa5eGIND6Tu%2BW%2BzI9zJdijTRJhMfiUAaSQED19%2BiEDPbba2Au%2Fce8brlnprz6toAhweZDm2ujqWNWdUeasxbSgxWBUmPkKfPXk28o33%2BgyFQr%2BBHViUOaxZkM6cODYeSeLzC7qWJv0vdAgDTuLhAS&X-Amz-Signature=9671cee944b23466268c7af61db1d21d66191cb6e59abfe716a74139bbc20c08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHKF6IR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIAF7pOEUjdk1skWMWfBHEPgHmwyjSoAmzIAB2Wg%2FZpHDAiAg0VsLTXfk7EEX2pvi7cWi9UzLtR9gfQNjv6y2YUYjGir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMZZzoOWvLhmg%2BZhS4KtwDbeW763cIcs69Zv%2Bdxi%2B3Mi6vmF7y8iT1zKnpemhMIKb9CqEG1Z%2FfbmkzeIIvjan0ygODqXFjSbmESrHg9QdnunKOp1X3O%2F7cLdnEXAAQ2koffX%2F6HxJzHQaTyiAZ02ej9dBpKJjVfVR%2Bup8fKz5%2Fu6Vx073blJz5Ktx7ZqeOCZhzJHLXR62xDZmbuCVkDNLE2deaDRdkg%2BHsozrfWwpvzwMogBMmfkL%2Fh0w2V1o2lyrEj2PBOEEC5hXf4IJdzSyTSq40i%2Fk2JkZ%2BZE1mVYq1%2FxigJE%2BYS9crJPXZ%2Bx0YlZN3ox0OL5k4AprMflvIVEJuIy%2BQ40QU75rW3TgLbIWRxIQ5%2BDOOxURgkBg8Qyrz%2BJMCibX8vuw6zq4q1RnKF6baKJ6S%2B5VYsBqgTmHmpPtLcjJo2zQ8gp5DzYDbB53TwVaoBi9L%2FJj28m1PcJXnfy3P1z%2BB1qARPNyInvR0cTjfCi2VeqnxhjerODq9UBRQCyaDn%2FgYi%2Bfj9%2FvnSBviAzV%2FBIh5Rrrpvpm2u0Prg5myA1fxGrUlx8T5Ab%2BewwgVudEVJ00VIlEloJuR5FIKC1Q4%2BP%2F9PeqJlU7DOPnasgCamxkEi6%2FHx4zO8irQ0R%2F3ggmkHAqfnF7xJr61OKQwqOmKzAY6pgG67igBDpQW5gLsaF5oNFtCIQAuQKSXcfnqr32CY6WnYtIsk3jDuFqcRIBrM7ELs4YX7vf20%2FLTa5eGIND6Tu%2BW%2BzI9zJdijTRJhMfiUAaSQED19%2BiEDPbba2Au%2Fce8brlnprz6toAhweZDm2ujqWNWdUeasxbSgxWBUmPkKfPXk28o33%2BgyFQr%2BBHViUOaxZkM6cODYeSeLzC7qWJv0vdAgDTuLhAS&X-Amz-Signature=87625bd342ac10d1c645c7addf5646ecafb52465b0318ff7d5616d3978243b7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHKF6IR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIAF7pOEUjdk1skWMWfBHEPgHmwyjSoAmzIAB2Wg%2FZpHDAiAg0VsLTXfk7EEX2pvi7cWi9UzLtR9gfQNjv6y2YUYjGir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMZZzoOWvLhmg%2BZhS4KtwDbeW763cIcs69Zv%2Bdxi%2B3Mi6vmF7y8iT1zKnpemhMIKb9CqEG1Z%2FfbmkzeIIvjan0ygODqXFjSbmESrHg9QdnunKOp1X3O%2F7cLdnEXAAQ2koffX%2F6HxJzHQaTyiAZ02ej9dBpKJjVfVR%2Bup8fKz5%2Fu6Vx073blJz5Ktx7ZqeOCZhzJHLXR62xDZmbuCVkDNLE2deaDRdkg%2BHsozrfWwpvzwMogBMmfkL%2Fh0w2V1o2lyrEj2PBOEEC5hXf4IJdzSyTSq40i%2Fk2JkZ%2BZE1mVYq1%2FxigJE%2BYS9crJPXZ%2Bx0YlZN3ox0OL5k4AprMflvIVEJuIy%2BQ40QU75rW3TgLbIWRxIQ5%2BDOOxURgkBg8Qyrz%2BJMCibX8vuw6zq4q1RnKF6baKJ6S%2B5VYsBqgTmHmpPtLcjJo2zQ8gp5DzYDbB53TwVaoBi9L%2FJj28m1PcJXnfy3P1z%2BB1qARPNyInvR0cTjfCi2VeqnxhjerODq9UBRQCyaDn%2FgYi%2Bfj9%2FvnSBviAzV%2FBIh5Rrrpvpm2u0Prg5myA1fxGrUlx8T5Ab%2BewwgVudEVJ00VIlEloJuR5FIKC1Q4%2BP%2F9PeqJlU7DOPnasgCamxkEi6%2FHx4zO8irQ0R%2F3ggmkHAqfnF7xJr61OKQwqOmKzAY6pgG67igBDpQW5gLsaF5oNFtCIQAuQKSXcfnqr32CY6WnYtIsk3jDuFqcRIBrM7ELs4YX7vf20%2FLTa5eGIND6Tu%2BW%2BzI9zJdijTRJhMfiUAaSQED19%2BiEDPbba2Au%2Fce8brlnprz6toAhweZDm2ujqWNWdUeasxbSgxWBUmPkKfPXk28o33%2BgyFQr%2BBHViUOaxZkM6cODYeSeLzC7qWJv0vdAgDTuLhAS&X-Amz-Signature=e4e5ee58dfe681b78cf618bf080980135c3140d5202c124d13dc6dc2ac9ba716&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHKF6IR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIAF7pOEUjdk1skWMWfBHEPgHmwyjSoAmzIAB2Wg%2FZpHDAiAg0VsLTXfk7EEX2pvi7cWi9UzLtR9gfQNjv6y2YUYjGir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMZZzoOWvLhmg%2BZhS4KtwDbeW763cIcs69Zv%2Bdxi%2B3Mi6vmF7y8iT1zKnpemhMIKb9CqEG1Z%2FfbmkzeIIvjan0ygODqXFjSbmESrHg9QdnunKOp1X3O%2F7cLdnEXAAQ2koffX%2F6HxJzHQaTyiAZ02ej9dBpKJjVfVR%2Bup8fKz5%2Fu6Vx073blJz5Ktx7ZqeOCZhzJHLXR62xDZmbuCVkDNLE2deaDRdkg%2BHsozrfWwpvzwMogBMmfkL%2Fh0w2V1o2lyrEj2PBOEEC5hXf4IJdzSyTSq40i%2Fk2JkZ%2BZE1mVYq1%2FxigJE%2BYS9crJPXZ%2Bx0YlZN3ox0OL5k4AprMflvIVEJuIy%2BQ40QU75rW3TgLbIWRxIQ5%2BDOOxURgkBg8Qyrz%2BJMCibX8vuw6zq4q1RnKF6baKJ6S%2B5VYsBqgTmHmpPtLcjJo2zQ8gp5DzYDbB53TwVaoBi9L%2FJj28m1PcJXnfy3P1z%2BB1qARPNyInvR0cTjfCi2VeqnxhjerODq9UBRQCyaDn%2FgYi%2Bfj9%2FvnSBviAzV%2FBIh5Rrrpvpm2u0Prg5myA1fxGrUlx8T5Ab%2BewwgVudEVJ00VIlEloJuR5FIKC1Q4%2BP%2F9PeqJlU7DOPnasgCamxkEi6%2FHx4zO8irQ0R%2F3ggmkHAqfnF7xJr61OKQwqOmKzAY6pgG67igBDpQW5gLsaF5oNFtCIQAuQKSXcfnqr32CY6WnYtIsk3jDuFqcRIBrM7ELs4YX7vf20%2FLTa5eGIND6Tu%2BW%2BzI9zJdijTRJhMfiUAaSQED19%2BiEDPbba2Au%2Fce8brlnprz6toAhweZDm2ujqWNWdUeasxbSgxWBUmPkKfPXk28o33%2BgyFQr%2BBHViUOaxZkM6cODYeSeLzC7qWJv0vdAgDTuLhAS&X-Amz-Signature=e6b8daf3ca34e27f1b092fb04c3db0519c2f641ac9b329ba5fc55de5b4069bfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHKF6IR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIAF7pOEUjdk1skWMWfBHEPgHmwyjSoAmzIAB2Wg%2FZpHDAiAg0VsLTXfk7EEX2pvi7cWi9UzLtR9gfQNjv6y2YUYjGir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMZZzoOWvLhmg%2BZhS4KtwDbeW763cIcs69Zv%2Bdxi%2B3Mi6vmF7y8iT1zKnpemhMIKb9CqEG1Z%2FfbmkzeIIvjan0ygODqXFjSbmESrHg9QdnunKOp1X3O%2F7cLdnEXAAQ2koffX%2F6HxJzHQaTyiAZ02ej9dBpKJjVfVR%2Bup8fKz5%2Fu6Vx073blJz5Ktx7ZqeOCZhzJHLXR62xDZmbuCVkDNLE2deaDRdkg%2BHsozrfWwpvzwMogBMmfkL%2Fh0w2V1o2lyrEj2PBOEEC5hXf4IJdzSyTSq40i%2Fk2JkZ%2BZE1mVYq1%2FxigJE%2BYS9crJPXZ%2Bx0YlZN3ox0OL5k4AprMflvIVEJuIy%2BQ40QU75rW3TgLbIWRxIQ5%2BDOOxURgkBg8Qyrz%2BJMCibX8vuw6zq4q1RnKF6baKJ6S%2B5VYsBqgTmHmpPtLcjJo2zQ8gp5DzYDbB53TwVaoBi9L%2FJj28m1PcJXnfy3P1z%2BB1qARPNyInvR0cTjfCi2VeqnxhjerODq9UBRQCyaDn%2FgYi%2Bfj9%2FvnSBviAzV%2FBIh5Rrrpvpm2u0Prg5myA1fxGrUlx8T5Ab%2BewwgVudEVJ00VIlEloJuR5FIKC1Q4%2BP%2F9PeqJlU7DOPnasgCamxkEi6%2FHx4zO8irQ0R%2F3ggmkHAqfnF7xJr61OKQwqOmKzAY6pgG67igBDpQW5gLsaF5oNFtCIQAuQKSXcfnqr32CY6WnYtIsk3jDuFqcRIBrM7ELs4YX7vf20%2FLTa5eGIND6Tu%2BW%2BzI9zJdijTRJhMfiUAaSQED19%2BiEDPbba2Au%2Fce8brlnprz6toAhweZDm2ujqWNWdUeasxbSgxWBUmPkKfPXk28o33%2BgyFQr%2BBHViUOaxZkM6cODYeSeLzC7qWJv0vdAgDTuLhAS&X-Amz-Signature=e56ee9e3b9a4fe87d0d420b07a08ddfca43e4d19ce6908322eea8ca7abd90383&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GHKF6IR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIAF7pOEUjdk1skWMWfBHEPgHmwyjSoAmzIAB2Wg%2FZpHDAiAg0VsLTXfk7EEX2pvi7cWi9UzLtR9gfQNjv6y2YUYjGir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMZZzoOWvLhmg%2BZhS4KtwDbeW763cIcs69Zv%2Bdxi%2B3Mi6vmF7y8iT1zKnpemhMIKb9CqEG1Z%2FfbmkzeIIvjan0ygODqXFjSbmESrHg9QdnunKOp1X3O%2F7cLdnEXAAQ2koffX%2F6HxJzHQaTyiAZ02ej9dBpKJjVfVR%2Bup8fKz5%2Fu6Vx073blJz5Ktx7ZqeOCZhzJHLXR62xDZmbuCVkDNLE2deaDRdkg%2BHsozrfWwpvzwMogBMmfkL%2Fh0w2V1o2lyrEj2PBOEEC5hXf4IJdzSyTSq40i%2Fk2JkZ%2BZE1mVYq1%2FxigJE%2BYS9crJPXZ%2Bx0YlZN3ox0OL5k4AprMflvIVEJuIy%2BQ40QU75rW3TgLbIWRxIQ5%2BDOOxURgkBg8Qyrz%2BJMCibX8vuw6zq4q1RnKF6baKJ6S%2B5VYsBqgTmHmpPtLcjJo2zQ8gp5DzYDbB53TwVaoBi9L%2FJj28m1PcJXnfy3P1z%2BB1qARPNyInvR0cTjfCi2VeqnxhjerODq9UBRQCyaDn%2FgYi%2Bfj9%2FvnSBviAzV%2FBIh5Rrrpvpm2u0Prg5myA1fxGrUlx8T5Ab%2BewwgVudEVJ00VIlEloJuR5FIKC1Q4%2BP%2F9PeqJlU7DOPnasgCamxkEi6%2FHx4zO8irQ0R%2F3ggmkHAqfnF7xJr61OKQwqOmKzAY6pgG67igBDpQW5gLsaF5oNFtCIQAuQKSXcfnqr32CY6WnYtIsk3jDuFqcRIBrM7ELs4YX7vf20%2FLTa5eGIND6Tu%2BW%2BzI9zJdijTRJhMfiUAaSQED19%2BiEDPbba2Au%2Fce8brlnprz6toAhweZDm2ujqWNWdUeasxbSgxWBUmPkKfPXk28o33%2BgyFQr%2BBHViUOaxZkM6cODYeSeLzC7qWJv0vdAgDTuLhAS&X-Amz-Signature=9d06c85115a04e666257a1a6cc0382cd2f04bff479d03a8a2298da72449d5496&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

