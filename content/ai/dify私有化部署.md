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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDARSZLD%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIH0lK1CFqLrdtX1V%2FmIol1V21v%2F2qaGpAO6zG%2FoFnYlfAiAxB%2BKftomFgkDJso4vEHflPwozLG89pNAZ2ztcQZmxSCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT3GoDdFRsHwlgYHuKtwDM%2BaygMXY4VbUsStljplb2e5LVxFjVzhFwYWpv4tsGpJbjWAIM8MqjXF%2FbUi2nKTE7iisugFFscvH5Ozmk%2BMR%2BEz8zC%2Bu6u8v9PePkF2APUyzkprY1L2Oc92Nvp29N5tsl3rJ62Zl7PrhZ%2BMu8%2F2biFJyE%2FXomWU5H7AOxyuO87zGskTOt6Vb%2FkqjX2HY67osjn%2BzcC6ZQLikZnD18eKumcOb7EH%2BKt8FIprT8lE02QJOIeFcdgtdotUy65%2F2ENCEk1iJWCwqXw5nKsflcGHELmD82vss2Ofw21vi6QIqBnCxBmQtZyoFev%2F8clKgx7XD%2B%2BsIWRAhocxhxXyQ6APthLO8iUPqMgIInLCvNipBgbLIBLQmxfpLmo6C8Fht3P2p8dYClhXlhnlv%2BcNCGtiHjNkHE63Hsid0bDZzWrvvFs1p1CcR4gpNG9daxD14fIqbo3e2fjhOfZhtOJpbqEXZWTCW9sBWJUxpdw4YWKZDetxdrhUXicpX4Mrd5pcsvTswVXulUVHTy5X73hIKKyVnbRQ8juLU%2Bui%2FXbasvmHtXSNyVEpWqIg83zJwFJ34TJuIQxdRwI3ZW0EzIKcsriucQfcIAhkmzQBNJuRsNUdPevqGsb0vXo%2BJQ%2B2ptEwwmr3cygY6pgGQVzWnCSvr%2FQ%2FbEyHmQU6xi3K5lGWdwWCzSmfJkyJIEGogAEVu%2BpLk%2F5BB3EEn6%2FMumBTySb%2FdGKVG8c03lzTz01mzPPxkvMnnIyudxoKb9%2Br5lhvg2ekH1Et8%2BkjDXcJBoecdZCz3ikvxmd4MsbEvieQTGWs0wfMhL9CbtKHX5X2bFlRcN6MvfBoBn5pJWY8B4kwHibLrP%2FSDbKa0IQ5oM4q5yAFU&X-Amz-Signature=e7cad1b878b9f3470d43eb8d341e29e0332ccfb7bba5af9e79460a0e4648a7b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDARSZLD%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIH0lK1CFqLrdtX1V%2FmIol1V21v%2F2qaGpAO6zG%2FoFnYlfAiAxB%2BKftomFgkDJso4vEHflPwozLG89pNAZ2ztcQZmxSCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT3GoDdFRsHwlgYHuKtwDM%2BaygMXY4VbUsStljplb2e5LVxFjVzhFwYWpv4tsGpJbjWAIM8MqjXF%2FbUi2nKTE7iisugFFscvH5Ozmk%2BMR%2BEz8zC%2Bu6u8v9PePkF2APUyzkprY1L2Oc92Nvp29N5tsl3rJ62Zl7PrhZ%2BMu8%2F2biFJyE%2FXomWU5H7AOxyuO87zGskTOt6Vb%2FkqjX2HY67osjn%2BzcC6ZQLikZnD18eKumcOb7EH%2BKt8FIprT8lE02QJOIeFcdgtdotUy65%2F2ENCEk1iJWCwqXw5nKsflcGHELmD82vss2Ofw21vi6QIqBnCxBmQtZyoFev%2F8clKgx7XD%2B%2BsIWRAhocxhxXyQ6APthLO8iUPqMgIInLCvNipBgbLIBLQmxfpLmo6C8Fht3P2p8dYClhXlhnlv%2BcNCGtiHjNkHE63Hsid0bDZzWrvvFs1p1CcR4gpNG9daxD14fIqbo3e2fjhOfZhtOJpbqEXZWTCW9sBWJUxpdw4YWKZDetxdrhUXicpX4Mrd5pcsvTswVXulUVHTy5X73hIKKyVnbRQ8juLU%2Bui%2FXbasvmHtXSNyVEpWqIg83zJwFJ34TJuIQxdRwI3ZW0EzIKcsriucQfcIAhkmzQBNJuRsNUdPevqGsb0vXo%2BJQ%2B2ptEwwmr3cygY6pgGQVzWnCSvr%2FQ%2FbEyHmQU6xi3K5lGWdwWCzSmfJkyJIEGogAEVu%2BpLk%2F5BB3EEn6%2FMumBTySb%2FdGKVG8c03lzTz01mzPPxkvMnnIyudxoKb9%2Br5lhvg2ekH1Et8%2BkjDXcJBoecdZCz3ikvxmd4MsbEvieQTGWs0wfMhL9CbtKHX5X2bFlRcN6MvfBoBn5pJWY8B4kwHibLrP%2FSDbKa0IQ5oM4q5yAFU&X-Amz-Signature=c5a0bf6d4a3d82d1bdd97e41b24e5865e77755776ed6005493f65ba7d19f1f6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDARSZLD%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIH0lK1CFqLrdtX1V%2FmIol1V21v%2F2qaGpAO6zG%2FoFnYlfAiAxB%2BKftomFgkDJso4vEHflPwozLG89pNAZ2ztcQZmxSCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT3GoDdFRsHwlgYHuKtwDM%2BaygMXY4VbUsStljplb2e5LVxFjVzhFwYWpv4tsGpJbjWAIM8MqjXF%2FbUi2nKTE7iisugFFscvH5Ozmk%2BMR%2BEz8zC%2Bu6u8v9PePkF2APUyzkprY1L2Oc92Nvp29N5tsl3rJ62Zl7PrhZ%2BMu8%2F2biFJyE%2FXomWU5H7AOxyuO87zGskTOt6Vb%2FkqjX2HY67osjn%2BzcC6ZQLikZnD18eKumcOb7EH%2BKt8FIprT8lE02QJOIeFcdgtdotUy65%2F2ENCEk1iJWCwqXw5nKsflcGHELmD82vss2Ofw21vi6QIqBnCxBmQtZyoFev%2F8clKgx7XD%2B%2BsIWRAhocxhxXyQ6APthLO8iUPqMgIInLCvNipBgbLIBLQmxfpLmo6C8Fht3P2p8dYClhXlhnlv%2BcNCGtiHjNkHE63Hsid0bDZzWrvvFs1p1CcR4gpNG9daxD14fIqbo3e2fjhOfZhtOJpbqEXZWTCW9sBWJUxpdw4YWKZDetxdrhUXicpX4Mrd5pcsvTswVXulUVHTy5X73hIKKyVnbRQ8juLU%2Bui%2FXbasvmHtXSNyVEpWqIg83zJwFJ34TJuIQxdRwI3ZW0EzIKcsriucQfcIAhkmzQBNJuRsNUdPevqGsb0vXo%2BJQ%2B2ptEwwmr3cygY6pgGQVzWnCSvr%2FQ%2FbEyHmQU6xi3K5lGWdwWCzSmfJkyJIEGogAEVu%2BpLk%2F5BB3EEn6%2FMumBTySb%2FdGKVG8c03lzTz01mzPPxkvMnnIyudxoKb9%2Br5lhvg2ekH1Et8%2BkjDXcJBoecdZCz3ikvxmd4MsbEvieQTGWs0wfMhL9CbtKHX5X2bFlRcN6MvfBoBn5pJWY8B4kwHibLrP%2FSDbKa0IQ5oM4q5yAFU&X-Amz-Signature=7e411819ef34b1a3cb6e664e6b72ce0ba846e0fab8f843f4c0bef390abf8d4ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDARSZLD%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIH0lK1CFqLrdtX1V%2FmIol1V21v%2F2qaGpAO6zG%2FoFnYlfAiAxB%2BKftomFgkDJso4vEHflPwozLG89pNAZ2ztcQZmxSCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT3GoDdFRsHwlgYHuKtwDM%2BaygMXY4VbUsStljplb2e5LVxFjVzhFwYWpv4tsGpJbjWAIM8MqjXF%2FbUi2nKTE7iisugFFscvH5Ozmk%2BMR%2BEz8zC%2Bu6u8v9PePkF2APUyzkprY1L2Oc92Nvp29N5tsl3rJ62Zl7PrhZ%2BMu8%2F2biFJyE%2FXomWU5H7AOxyuO87zGskTOt6Vb%2FkqjX2HY67osjn%2BzcC6ZQLikZnD18eKumcOb7EH%2BKt8FIprT8lE02QJOIeFcdgtdotUy65%2F2ENCEk1iJWCwqXw5nKsflcGHELmD82vss2Ofw21vi6QIqBnCxBmQtZyoFev%2F8clKgx7XD%2B%2BsIWRAhocxhxXyQ6APthLO8iUPqMgIInLCvNipBgbLIBLQmxfpLmo6C8Fht3P2p8dYClhXlhnlv%2BcNCGtiHjNkHE63Hsid0bDZzWrvvFs1p1CcR4gpNG9daxD14fIqbo3e2fjhOfZhtOJpbqEXZWTCW9sBWJUxpdw4YWKZDetxdrhUXicpX4Mrd5pcsvTswVXulUVHTy5X73hIKKyVnbRQ8juLU%2Bui%2FXbasvmHtXSNyVEpWqIg83zJwFJ34TJuIQxdRwI3ZW0EzIKcsriucQfcIAhkmzQBNJuRsNUdPevqGsb0vXo%2BJQ%2B2ptEwwmr3cygY6pgGQVzWnCSvr%2FQ%2FbEyHmQU6xi3K5lGWdwWCzSmfJkyJIEGogAEVu%2BpLk%2F5BB3EEn6%2FMumBTySb%2FdGKVG8c03lzTz01mzPPxkvMnnIyudxoKb9%2Br5lhvg2ekH1Et8%2BkjDXcJBoecdZCz3ikvxmd4MsbEvieQTGWs0wfMhL9CbtKHX5X2bFlRcN6MvfBoBn5pJWY8B4kwHibLrP%2FSDbKa0IQ5oM4q5yAFU&X-Amz-Signature=55c8eef8dad187a7ff267b2fc6e462441bbbc5701fe1407952c5da1e13f31c23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDARSZLD%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIH0lK1CFqLrdtX1V%2FmIol1V21v%2F2qaGpAO6zG%2FoFnYlfAiAxB%2BKftomFgkDJso4vEHflPwozLG89pNAZ2ztcQZmxSCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT3GoDdFRsHwlgYHuKtwDM%2BaygMXY4VbUsStljplb2e5LVxFjVzhFwYWpv4tsGpJbjWAIM8MqjXF%2FbUi2nKTE7iisugFFscvH5Ozmk%2BMR%2BEz8zC%2Bu6u8v9PePkF2APUyzkprY1L2Oc92Nvp29N5tsl3rJ62Zl7PrhZ%2BMu8%2F2biFJyE%2FXomWU5H7AOxyuO87zGskTOt6Vb%2FkqjX2HY67osjn%2BzcC6ZQLikZnD18eKumcOb7EH%2BKt8FIprT8lE02QJOIeFcdgtdotUy65%2F2ENCEk1iJWCwqXw5nKsflcGHELmD82vss2Ofw21vi6QIqBnCxBmQtZyoFev%2F8clKgx7XD%2B%2BsIWRAhocxhxXyQ6APthLO8iUPqMgIInLCvNipBgbLIBLQmxfpLmo6C8Fht3P2p8dYClhXlhnlv%2BcNCGtiHjNkHE63Hsid0bDZzWrvvFs1p1CcR4gpNG9daxD14fIqbo3e2fjhOfZhtOJpbqEXZWTCW9sBWJUxpdw4YWKZDetxdrhUXicpX4Mrd5pcsvTswVXulUVHTy5X73hIKKyVnbRQ8juLU%2Bui%2FXbasvmHtXSNyVEpWqIg83zJwFJ34TJuIQxdRwI3ZW0EzIKcsriucQfcIAhkmzQBNJuRsNUdPevqGsb0vXo%2BJQ%2B2ptEwwmr3cygY6pgGQVzWnCSvr%2FQ%2FbEyHmQU6xi3K5lGWdwWCzSmfJkyJIEGogAEVu%2BpLk%2F5BB3EEn6%2FMumBTySb%2FdGKVG8c03lzTz01mzPPxkvMnnIyudxoKb9%2Br5lhvg2ekH1Et8%2BkjDXcJBoecdZCz3ikvxmd4MsbEvieQTGWs0wfMhL9CbtKHX5X2bFlRcN6MvfBoBn5pJWY8B4kwHibLrP%2FSDbKa0IQ5oM4q5yAFU&X-Amz-Signature=83568c350dc9730be695ba3d4ccd51a1a1819c215745e5bdd96397bcd4addc8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDARSZLD%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIH0lK1CFqLrdtX1V%2FmIol1V21v%2F2qaGpAO6zG%2FoFnYlfAiAxB%2BKftomFgkDJso4vEHflPwozLG89pNAZ2ztcQZmxSCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT3GoDdFRsHwlgYHuKtwDM%2BaygMXY4VbUsStljplb2e5LVxFjVzhFwYWpv4tsGpJbjWAIM8MqjXF%2FbUi2nKTE7iisugFFscvH5Ozmk%2BMR%2BEz8zC%2Bu6u8v9PePkF2APUyzkprY1L2Oc92Nvp29N5tsl3rJ62Zl7PrhZ%2BMu8%2F2biFJyE%2FXomWU5H7AOxyuO87zGskTOt6Vb%2FkqjX2HY67osjn%2BzcC6ZQLikZnD18eKumcOb7EH%2BKt8FIprT8lE02QJOIeFcdgtdotUy65%2F2ENCEk1iJWCwqXw5nKsflcGHELmD82vss2Ofw21vi6QIqBnCxBmQtZyoFev%2F8clKgx7XD%2B%2BsIWRAhocxhxXyQ6APthLO8iUPqMgIInLCvNipBgbLIBLQmxfpLmo6C8Fht3P2p8dYClhXlhnlv%2BcNCGtiHjNkHE63Hsid0bDZzWrvvFs1p1CcR4gpNG9daxD14fIqbo3e2fjhOfZhtOJpbqEXZWTCW9sBWJUxpdw4YWKZDetxdrhUXicpX4Mrd5pcsvTswVXulUVHTy5X73hIKKyVnbRQ8juLU%2Bui%2FXbasvmHtXSNyVEpWqIg83zJwFJ34TJuIQxdRwI3ZW0EzIKcsriucQfcIAhkmzQBNJuRsNUdPevqGsb0vXo%2BJQ%2B2ptEwwmr3cygY6pgGQVzWnCSvr%2FQ%2FbEyHmQU6xi3K5lGWdwWCzSmfJkyJIEGogAEVu%2BpLk%2F5BB3EEn6%2FMumBTySb%2FdGKVG8c03lzTz01mzPPxkvMnnIyudxoKb9%2Br5lhvg2ekH1Et8%2BkjDXcJBoecdZCz3ikvxmd4MsbEvieQTGWs0wfMhL9CbtKHX5X2bFlRcN6MvfBoBn5pJWY8B4kwHibLrP%2FSDbKa0IQ5oM4q5yAFU&X-Amz-Signature=b0ce3189f1d8483952aeece2b0cd0d911626e73a7eec4e8a9b9d69a00427f844&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDARSZLD%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIH0lK1CFqLrdtX1V%2FmIol1V21v%2F2qaGpAO6zG%2FoFnYlfAiAxB%2BKftomFgkDJso4vEHflPwozLG89pNAZ2ztcQZmxSCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT3GoDdFRsHwlgYHuKtwDM%2BaygMXY4VbUsStljplb2e5LVxFjVzhFwYWpv4tsGpJbjWAIM8MqjXF%2FbUi2nKTE7iisugFFscvH5Ozmk%2BMR%2BEz8zC%2Bu6u8v9PePkF2APUyzkprY1L2Oc92Nvp29N5tsl3rJ62Zl7PrhZ%2BMu8%2F2biFJyE%2FXomWU5H7AOxyuO87zGskTOt6Vb%2FkqjX2HY67osjn%2BzcC6ZQLikZnD18eKumcOb7EH%2BKt8FIprT8lE02QJOIeFcdgtdotUy65%2F2ENCEk1iJWCwqXw5nKsflcGHELmD82vss2Ofw21vi6QIqBnCxBmQtZyoFev%2F8clKgx7XD%2B%2BsIWRAhocxhxXyQ6APthLO8iUPqMgIInLCvNipBgbLIBLQmxfpLmo6C8Fht3P2p8dYClhXlhnlv%2BcNCGtiHjNkHE63Hsid0bDZzWrvvFs1p1CcR4gpNG9daxD14fIqbo3e2fjhOfZhtOJpbqEXZWTCW9sBWJUxpdw4YWKZDetxdrhUXicpX4Mrd5pcsvTswVXulUVHTy5X73hIKKyVnbRQ8juLU%2Bui%2FXbasvmHtXSNyVEpWqIg83zJwFJ34TJuIQxdRwI3ZW0EzIKcsriucQfcIAhkmzQBNJuRsNUdPevqGsb0vXo%2BJQ%2B2ptEwwmr3cygY6pgGQVzWnCSvr%2FQ%2FbEyHmQU6xi3K5lGWdwWCzSmfJkyJIEGogAEVu%2BpLk%2F5BB3EEn6%2FMumBTySb%2FdGKVG8c03lzTz01mzPPxkvMnnIyudxoKb9%2Br5lhvg2ekH1Et8%2BkjDXcJBoecdZCz3ikvxmd4MsbEvieQTGWs0wfMhL9CbtKHX5X2bFlRcN6MvfBoBn5pJWY8B4kwHibLrP%2FSDbKa0IQ5oM4q5yAFU&X-Amz-Signature=6db3317bd6c6281aa734207bddad09ccf5199feca895602a4b6c8f639dbf503d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDARSZLD%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIH0lK1CFqLrdtX1V%2FmIol1V21v%2F2qaGpAO6zG%2FoFnYlfAiAxB%2BKftomFgkDJso4vEHflPwozLG89pNAZ2ztcQZmxSCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT3GoDdFRsHwlgYHuKtwDM%2BaygMXY4VbUsStljplb2e5LVxFjVzhFwYWpv4tsGpJbjWAIM8MqjXF%2FbUi2nKTE7iisugFFscvH5Ozmk%2BMR%2BEz8zC%2Bu6u8v9PePkF2APUyzkprY1L2Oc92Nvp29N5tsl3rJ62Zl7PrhZ%2BMu8%2F2biFJyE%2FXomWU5H7AOxyuO87zGskTOt6Vb%2FkqjX2HY67osjn%2BzcC6ZQLikZnD18eKumcOb7EH%2BKt8FIprT8lE02QJOIeFcdgtdotUy65%2F2ENCEk1iJWCwqXw5nKsflcGHELmD82vss2Ofw21vi6QIqBnCxBmQtZyoFev%2F8clKgx7XD%2B%2BsIWRAhocxhxXyQ6APthLO8iUPqMgIInLCvNipBgbLIBLQmxfpLmo6C8Fht3P2p8dYClhXlhnlv%2BcNCGtiHjNkHE63Hsid0bDZzWrvvFs1p1CcR4gpNG9daxD14fIqbo3e2fjhOfZhtOJpbqEXZWTCW9sBWJUxpdw4YWKZDetxdrhUXicpX4Mrd5pcsvTswVXulUVHTy5X73hIKKyVnbRQ8juLU%2Bui%2FXbasvmHtXSNyVEpWqIg83zJwFJ34TJuIQxdRwI3ZW0EzIKcsriucQfcIAhkmzQBNJuRsNUdPevqGsb0vXo%2BJQ%2B2ptEwwmr3cygY6pgGQVzWnCSvr%2FQ%2FbEyHmQU6xi3K5lGWdwWCzSmfJkyJIEGogAEVu%2BpLk%2F5BB3EEn6%2FMumBTySb%2FdGKVG8c03lzTz01mzPPxkvMnnIyudxoKb9%2Br5lhvg2ekH1Et8%2BkjDXcJBoecdZCz3ikvxmd4MsbEvieQTGWs0wfMhL9CbtKHX5X2bFlRcN6MvfBoBn5pJWY8B4kwHibLrP%2FSDbKa0IQ5oM4q5yAFU&X-Amz-Signature=06e7162ce766f066695703cf718ce86ea595552586e907f7fcbf547f19221347&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDARSZLD%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIH0lK1CFqLrdtX1V%2FmIol1V21v%2F2qaGpAO6zG%2FoFnYlfAiAxB%2BKftomFgkDJso4vEHflPwozLG89pNAZ2ztcQZmxSCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT3GoDdFRsHwlgYHuKtwDM%2BaygMXY4VbUsStljplb2e5LVxFjVzhFwYWpv4tsGpJbjWAIM8MqjXF%2FbUi2nKTE7iisugFFscvH5Ozmk%2BMR%2BEz8zC%2Bu6u8v9PePkF2APUyzkprY1L2Oc92Nvp29N5tsl3rJ62Zl7PrhZ%2BMu8%2F2biFJyE%2FXomWU5H7AOxyuO87zGskTOt6Vb%2FkqjX2HY67osjn%2BzcC6ZQLikZnD18eKumcOb7EH%2BKt8FIprT8lE02QJOIeFcdgtdotUy65%2F2ENCEk1iJWCwqXw5nKsflcGHELmD82vss2Ofw21vi6QIqBnCxBmQtZyoFev%2F8clKgx7XD%2B%2BsIWRAhocxhxXyQ6APthLO8iUPqMgIInLCvNipBgbLIBLQmxfpLmo6C8Fht3P2p8dYClhXlhnlv%2BcNCGtiHjNkHE63Hsid0bDZzWrvvFs1p1CcR4gpNG9daxD14fIqbo3e2fjhOfZhtOJpbqEXZWTCW9sBWJUxpdw4YWKZDetxdrhUXicpX4Mrd5pcsvTswVXulUVHTy5X73hIKKyVnbRQ8juLU%2Bui%2FXbasvmHtXSNyVEpWqIg83zJwFJ34TJuIQxdRwI3ZW0EzIKcsriucQfcIAhkmzQBNJuRsNUdPevqGsb0vXo%2BJQ%2B2ptEwwmr3cygY6pgGQVzWnCSvr%2FQ%2FbEyHmQU6xi3K5lGWdwWCzSmfJkyJIEGogAEVu%2BpLk%2F5BB3EEn6%2FMumBTySb%2FdGKVG8c03lzTz01mzPPxkvMnnIyudxoKb9%2Br5lhvg2ekH1Et8%2BkjDXcJBoecdZCz3ikvxmd4MsbEvieQTGWs0wfMhL9CbtKHX5X2bFlRcN6MvfBoBn5pJWY8B4kwHibLrP%2FSDbKa0IQ5oM4q5yAFU&X-Amz-Signature=4cf3d74f05dcf8ec69be14bf038ef2fa42f273a848144a8bdc1b75e3dbf8913e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDARSZLD%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIH0lK1CFqLrdtX1V%2FmIol1V21v%2F2qaGpAO6zG%2FoFnYlfAiAxB%2BKftomFgkDJso4vEHflPwozLG89pNAZ2ztcQZmxSCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT3GoDdFRsHwlgYHuKtwDM%2BaygMXY4VbUsStljplb2e5LVxFjVzhFwYWpv4tsGpJbjWAIM8MqjXF%2FbUi2nKTE7iisugFFscvH5Ozmk%2BMR%2BEz8zC%2Bu6u8v9PePkF2APUyzkprY1L2Oc92Nvp29N5tsl3rJ62Zl7PrhZ%2BMu8%2F2biFJyE%2FXomWU5H7AOxyuO87zGskTOt6Vb%2FkqjX2HY67osjn%2BzcC6ZQLikZnD18eKumcOb7EH%2BKt8FIprT8lE02QJOIeFcdgtdotUy65%2F2ENCEk1iJWCwqXw5nKsflcGHELmD82vss2Ofw21vi6QIqBnCxBmQtZyoFev%2F8clKgx7XD%2B%2BsIWRAhocxhxXyQ6APthLO8iUPqMgIInLCvNipBgbLIBLQmxfpLmo6C8Fht3P2p8dYClhXlhnlv%2BcNCGtiHjNkHE63Hsid0bDZzWrvvFs1p1CcR4gpNG9daxD14fIqbo3e2fjhOfZhtOJpbqEXZWTCW9sBWJUxpdw4YWKZDetxdrhUXicpX4Mrd5pcsvTswVXulUVHTy5X73hIKKyVnbRQ8juLU%2Bui%2FXbasvmHtXSNyVEpWqIg83zJwFJ34TJuIQxdRwI3ZW0EzIKcsriucQfcIAhkmzQBNJuRsNUdPevqGsb0vXo%2BJQ%2B2ptEwwmr3cygY6pgGQVzWnCSvr%2FQ%2FbEyHmQU6xi3K5lGWdwWCzSmfJkyJIEGogAEVu%2BpLk%2F5BB3EEn6%2FMumBTySb%2FdGKVG8c03lzTz01mzPPxkvMnnIyudxoKb9%2Br5lhvg2ekH1Et8%2BkjDXcJBoecdZCz3ikvxmd4MsbEvieQTGWs0wfMhL9CbtKHX5X2bFlRcN6MvfBoBn5pJWY8B4kwHibLrP%2FSDbKa0IQ5oM4q5yAFU&X-Amz-Signature=4931d13783f273eb65b6d547992007f37bda9cd101e76207d73d8d14e0836cf3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

