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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TJB3OHU%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjkJLphFJf79uqd%2FlgnUJwG933H8WqkQuWfDCyIBQr9QIgan8nuClvjw52pJMjgbMCGDJXRfBNXiLhudwx1kShjZEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCq%2BKrqaFCsgSDJrsCrcA%2Bpbkx1SOBnBp5F5VxmOBxT%2BLM4GZVyT2dBOGsuCurIAhIYq%2FlstKPr9z6NH3ZlMl9xzBvjtoKb%2FZ0MC3w8MbxqPpYo6ETt9ZsFTKYeVG9J5KRhDHCHwHQMLXsUdbSktCAaxq5hrHhy5Ts07bsFcUdGtw6xndUJU2x0hNGgf%2BHGHJLMJwx7g%2FxhINgoUbEhpTHplBOYv1oAjdmUb7YriYtD%2BQ5LrORhxUHJ7dloZf%2FWYDr42Ht366mcrqWFfYCve9FUULa%2B95JfKtK1rqyXhUjCr7FwNiZcxeoMvg3TsyIuf%2Fk1ebMvQBxymN%2FQmyzceLVo2kYXewDNVZYnKjBfN3zXu%2Bk9g3Obb%2B%2FEGNAo8Jkr7yaD4a8Jrf8Kqu0kmJF3iztPXXSvVN1QMejvCZyboevNb%2BpX2ZkAGdL23MNb56YpFKSsA5CP9LX13pp14yEG8jG64vkwJzJc8zqwvJLxA7LJVSl7AeT0K0enhyMIt%2FT39T1gLIidmu%2BMsYV2o8WzUbi0AeK%2Bh2V3q4gCyP%2Fo49zvXBrFBhTQySq%2FPstxcoPp7gEoOgth40J7Y%2BeqEgSGEaEbxsnWlIyKhsUob%2Fe1DsacudDvU12f09D0X6WENt41C80%2FAOXmUtSfa9%2B5pMJGiss4GOqUBWYMddcS3jXc7IeYwfht8ZAHeGoMx5CcxTGE8OpMp2i9nhlnP6DkFmbRVD2QEigNO1a16U0l0sVGNFB9VTBqY%2FbHErACJSh4eOO8BupP%2BzXPCFkJgRnJr9SuOf4RjxOv2mqXOGD0wrRzL2vCSZIUClFQdCqf8V3Q5foFez64VObNr5%2FkLbQvPxFvyn5%2Fh5LjfkO7GaTJhi2o%2Bc%2BbXBrJ7CoRCU0of&X-Amz-Signature=3326abeedcdb24a3ac87b3a54a7306bd225c4be6e55eacbafad906cad7a0a81e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TJB3OHU%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjkJLphFJf79uqd%2FlgnUJwG933H8WqkQuWfDCyIBQr9QIgan8nuClvjw52pJMjgbMCGDJXRfBNXiLhudwx1kShjZEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCq%2BKrqaFCsgSDJrsCrcA%2Bpbkx1SOBnBp5F5VxmOBxT%2BLM4GZVyT2dBOGsuCurIAhIYq%2FlstKPr9z6NH3ZlMl9xzBvjtoKb%2FZ0MC3w8MbxqPpYo6ETt9ZsFTKYeVG9J5KRhDHCHwHQMLXsUdbSktCAaxq5hrHhy5Ts07bsFcUdGtw6xndUJU2x0hNGgf%2BHGHJLMJwx7g%2FxhINgoUbEhpTHplBOYv1oAjdmUb7YriYtD%2BQ5LrORhxUHJ7dloZf%2FWYDr42Ht366mcrqWFfYCve9FUULa%2B95JfKtK1rqyXhUjCr7FwNiZcxeoMvg3TsyIuf%2Fk1ebMvQBxymN%2FQmyzceLVo2kYXewDNVZYnKjBfN3zXu%2Bk9g3Obb%2B%2FEGNAo8Jkr7yaD4a8Jrf8Kqu0kmJF3iztPXXSvVN1QMejvCZyboevNb%2BpX2ZkAGdL23MNb56YpFKSsA5CP9LX13pp14yEG8jG64vkwJzJc8zqwvJLxA7LJVSl7AeT0K0enhyMIt%2FT39T1gLIidmu%2BMsYV2o8WzUbi0AeK%2Bh2V3q4gCyP%2Fo49zvXBrFBhTQySq%2FPstxcoPp7gEoOgth40J7Y%2BeqEgSGEaEbxsnWlIyKhsUob%2Fe1DsacudDvU12f09D0X6WENt41C80%2FAOXmUtSfa9%2B5pMJGiss4GOqUBWYMddcS3jXc7IeYwfht8ZAHeGoMx5CcxTGE8OpMp2i9nhlnP6DkFmbRVD2QEigNO1a16U0l0sVGNFB9VTBqY%2FbHErACJSh4eOO8BupP%2BzXPCFkJgRnJr9SuOf4RjxOv2mqXOGD0wrRzL2vCSZIUClFQdCqf8V3Q5foFez64VObNr5%2FkLbQvPxFvyn5%2Fh5LjfkO7GaTJhi2o%2Bc%2BbXBrJ7CoRCU0of&X-Amz-Signature=89057b84f15493a4eac32737de6620eff1f7c4c340f2ed3033697de230a66e62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TJB3OHU%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjkJLphFJf79uqd%2FlgnUJwG933H8WqkQuWfDCyIBQr9QIgan8nuClvjw52pJMjgbMCGDJXRfBNXiLhudwx1kShjZEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCq%2BKrqaFCsgSDJrsCrcA%2Bpbkx1SOBnBp5F5VxmOBxT%2BLM4GZVyT2dBOGsuCurIAhIYq%2FlstKPr9z6NH3ZlMl9xzBvjtoKb%2FZ0MC3w8MbxqPpYo6ETt9ZsFTKYeVG9J5KRhDHCHwHQMLXsUdbSktCAaxq5hrHhy5Ts07bsFcUdGtw6xndUJU2x0hNGgf%2BHGHJLMJwx7g%2FxhINgoUbEhpTHplBOYv1oAjdmUb7YriYtD%2BQ5LrORhxUHJ7dloZf%2FWYDr42Ht366mcrqWFfYCve9FUULa%2B95JfKtK1rqyXhUjCr7FwNiZcxeoMvg3TsyIuf%2Fk1ebMvQBxymN%2FQmyzceLVo2kYXewDNVZYnKjBfN3zXu%2Bk9g3Obb%2B%2FEGNAo8Jkr7yaD4a8Jrf8Kqu0kmJF3iztPXXSvVN1QMejvCZyboevNb%2BpX2ZkAGdL23MNb56YpFKSsA5CP9LX13pp14yEG8jG64vkwJzJc8zqwvJLxA7LJVSl7AeT0K0enhyMIt%2FT39T1gLIidmu%2BMsYV2o8WzUbi0AeK%2Bh2V3q4gCyP%2Fo49zvXBrFBhTQySq%2FPstxcoPp7gEoOgth40J7Y%2BeqEgSGEaEbxsnWlIyKhsUob%2Fe1DsacudDvU12f09D0X6WENt41C80%2FAOXmUtSfa9%2B5pMJGiss4GOqUBWYMddcS3jXc7IeYwfht8ZAHeGoMx5CcxTGE8OpMp2i9nhlnP6DkFmbRVD2QEigNO1a16U0l0sVGNFB9VTBqY%2FbHErACJSh4eOO8BupP%2BzXPCFkJgRnJr9SuOf4RjxOv2mqXOGD0wrRzL2vCSZIUClFQdCqf8V3Q5foFez64VObNr5%2FkLbQvPxFvyn5%2Fh5LjfkO7GaTJhi2o%2Bc%2BbXBrJ7CoRCU0of&X-Amz-Signature=078ab36e30b4c737e719c329d19861c94c83403ef83d10c91f8d6bd59853bfbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TJB3OHU%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjkJLphFJf79uqd%2FlgnUJwG933H8WqkQuWfDCyIBQr9QIgan8nuClvjw52pJMjgbMCGDJXRfBNXiLhudwx1kShjZEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCq%2BKrqaFCsgSDJrsCrcA%2Bpbkx1SOBnBp5F5VxmOBxT%2BLM4GZVyT2dBOGsuCurIAhIYq%2FlstKPr9z6NH3ZlMl9xzBvjtoKb%2FZ0MC3w8MbxqPpYo6ETt9ZsFTKYeVG9J5KRhDHCHwHQMLXsUdbSktCAaxq5hrHhy5Ts07bsFcUdGtw6xndUJU2x0hNGgf%2BHGHJLMJwx7g%2FxhINgoUbEhpTHplBOYv1oAjdmUb7YriYtD%2BQ5LrORhxUHJ7dloZf%2FWYDr42Ht366mcrqWFfYCve9FUULa%2B95JfKtK1rqyXhUjCr7FwNiZcxeoMvg3TsyIuf%2Fk1ebMvQBxymN%2FQmyzceLVo2kYXewDNVZYnKjBfN3zXu%2Bk9g3Obb%2B%2FEGNAo8Jkr7yaD4a8Jrf8Kqu0kmJF3iztPXXSvVN1QMejvCZyboevNb%2BpX2ZkAGdL23MNb56YpFKSsA5CP9LX13pp14yEG8jG64vkwJzJc8zqwvJLxA7LJVSl7AeT0K0enhyMIt%2FT39T1gLIidmu%2BMsYV2o8WzUbi0AeK%2Bh2V3q4gCyP%2Fo49zvXBrFBhTQySq%2FPstxcoPp7gEoOgth40J7Y%2BeqEgSGEaEbxsnWlIyKhsUob%2Fe1DsacudDvU12f09D0X6WENt41C80%2FAOXmUtSfa9%2B5pMJGiss4GOqUBWYMddcS3jXc7IeYwfht8ZAHeGoMx5CcxTGE8OpMp2i9nhlnP6DkFmbRVD2QEigNO1a16U0l0sVGNFB9VTBqY%2FbHErACJSh4eOO8BupP%2BzXPCFkJgRnJr9SuOf4RjxOv2mqXOGD0wrRzL2vCSZIUClFQdCqf8V3Q5foFez64VObNr5%2FkLbQvPxFvyn5%2Fh5LjfkO7GaTJhi2o%2Bc%2BbXBrJ7CoRCU0of&X-Amz-Signature=0fa718dfb77965ff3bc00d66488373902b4d3bf082f41068e5731b03a0fb4d9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TJB3OHU%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjkJLphFJf79uqd%2FlgnUJwG933H8WqkQuWfDCyIBQr9QIgan8nuClvjw52pJMjgbMCGDJXRfBNXiLhudwx1kShjZEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCq%2BKrqaFCsgSDJrsCrcA%2Bpbkx1SOBnBp5F5VxmOBxT%2BLM4GZVyT2dBOGsuCurIAhIYq%2FlstKPr9z6NH3ZlMl9xzBvjtoKb%2FZ0MC3w8MbxqPpYo6ETt9ZsFTKYeVG9J5KRhDHCHwHQMLXsUdbSktCAaxq5hrHhy5Ts07bsFcUdGtw6xndUJU2x0hNGgf%2BHGHJLMJwx7g%2FxhINgoUbEhpTHplBOYv1oAjdmUb7YriYtD%2BQ5LrORhxUHJ7dloZf%2FWYDr42Ht366mcrqWFfYCve9FUULa%2B95JfKtK1rqyXhUjCr7FwNiZcxeoMvg3TsyIuf%2Fk1ebMvQBxymN%2FQmyzceLVo2kYXewDNVZYnKjBfN3zXu%2Bk9g3Obb%2B%2FEGNAo8Jkr7yaD4a8Jrf8Kqu0kmJF3iztPXXSvVN1QMejvCZyboevNb%2BpX2ZkAGdL23MNb56YpFKSsA5CP9LX13pp14yEG8jG64vkwJzJc8zqwvJLxA7LJVSl7AeT0K0enhyMIt%2FT39T1gLIidmu%2BMsYV2o8WzUbi0AeK%2Bh2V3q4gCyP%2Fo49zvXBrFBhTQySq%2FPstxcoPp7gEoOgth40J7Y%2BeqEgSGEaEbxsnWlIyKhsUob%2Fe1DsacudDvU12f09D0X6WENt41C80%2FAOXmUtSfa9%2B5pMJGiss4GOqUBWYMddcS3jXc7IeYwfht8ZAHeGoMx5CcxTGE8OpMp2i9nhlnP6DkFmbRVD2QEigNO1a16U0l0sVGNFB9VTBqY%2FbHErACJSh4eOO8BupP%2BzXPCFkJgRnJr9SuOf4RjxOv2mqXOGD0wrRzL2vCSZIUClFQdCqf8V3Q5foFez64VObNr5%2FkLbQvPxFvyn5%2Fh5LjfkO7GaTJhi2o%2Bc%2BbXBrJ7CoRCU0of&X-Amz-Signature=d13217f918b3ca600b7d1ba4136681b5df31d8cdf4b9f81ab38bc49589854e44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TJB3OHU%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjkJLphFJf79uqd%2FlgnUJwG933H8WqkQuWfDCyIBQr9QIgan8nuClvjw52pJMjgbMCGDJXRfBNXiLhudwx1kShjZEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCq%2BKrqaFCsgSDJrsCrcA%2Bpbkx1SOBnBp5F5VxmOBxT%2BLM4GZVyT2dBOGsuCurIAhIYq%2FlstKPr9z6NH3ZlMl9xzBvjtoKb%2FZ0MC3w8MbxqPpYo6ETt9ZsFTKYeVG9J5KRhDHCHwHQMLXsUdbSktCAaxq5hrHhy5Ts07bsFcUdGtw6xndUJU2x0hNGgf%2BHGHJLMJwx7g%2FxhINgoUbEhpTHplBOYv1oAjdmUb7YriYtD%2BQ5LrORhxUHJ7dloZf%2FWYDr42Ht366mcrqWFfYCve9FUULa%2B95JfKtK1rqyXhUjCr7FwNiZcxeoMvg3TsyIuf%2Fk1ebMvQBxymN%2FQmyzceLVo2kYXewDNVZYnKjBfN3zXu%2Bk9g3Obb%2B%2FEGNAo8Jkr7yaD4a8Jrf8Kqu0kmJF3iztPXXSvVN1QMejvCZyboevNb%2BpX2ZkAGdL23MNb56YpFKSsA5CP9LX13pp14yEG8jG64vkwJzJc8zqwvJLxA7LJVSl7AeT0K0enhyMIt%2FT39T1gLIidmu%2BMsYV2o8WzUbi0AeK%2Bh2V3q4gCyP%2Fo49zvXBrFBhTQySq%2FPstxcoPp7gEoOgth40J7Y%2BeqEgSGEaEbxsnWlIyKhsUob%2Fe1DsacudDvU12f09D0X6WENt41C80%2FAOXmUtSfa9%2B5pMJGiss4GOqUBWYMddcS3jXc7IeYwfht8ZAHeGoMx5CcxTGE8OpMp2i9nhlnP6DkFmbRVD2QEigNO1a16U0l0sVGNFB9VTBqY%2FbHErACJSh4eOO8BupP%2BzXPCFkJgRnJr9SuOf4RjxOv2mqXOGD0wrRzL2vCSZIUClFQdCqf8V3Q5foFez64VObNr5%2FkLbQvPxFvyn5%2Fh5LjfkO7GaTJhi2o%2Bc%2BbXBrJ7CoRCU0of&X-Amz-Signature=b5f631526377505bd44e07dca0bdcc31ba6f06f674331a5dc53011f058e3f562&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TJB3OHU%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjkJLphFJf79uqd%2FlgnUJwG933H8WqkQuWfDCyIBQr9QIgan8nuClvjw52pJMjgbMCGDJXRfBNXiLhudwx1kShjZEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCq%2BKrqaFCsgSDJrsCrcA%2Bpbkx1SOBnBp5F5VxmOBxT%2BLM4GZVyT2dBOGsuCurIAhIYq%2FlstKPr9z6NH3ZlMl9xzBvjtoKb%2FZ0MC3w8MbxqPpYo6ETt9ZsFTKYeVG9J5KRhDHCHwHQMLXsUdbSktCAaxq5hrHhy5Ts07bsFcUdGtw6xndUJU2x0hNGgf%2BHGHJLMJwx7g%2FxhINgoUbEhpTHplBOYv1oAjdmUb7YriYtD%2BQ5LrORhxUHJ7dloZf%2FWYDr42Ht366mcrqWFfYCve9FUULa%2B95JfKtK1rqyXhUjCr7FwNiZcxeoMvg3TsyIuf%2Fk1ebMvQBxymN%2FQmyzceLVo2kYXewDNVZYnKjBfN3zXu%2Bk9g3Obb%2B%2FEGNAo8Jkr7yaD4a8Jrf8Kqu0kmJF3iztPXXSvVN1QMejvCZyboevNb%2BpX2ZkAGdL23MNb56YpFKSsA5CP9LX13pp14yEG8jG64vkwJzJc8zqwvJLxA7LJVSl7AeT0K0enhyMIt%2FT39T1gLIidmu%2BMsYV2o8WzUbi0AeK%2Bh2V3q4gCyP%2Fo49zvXBrFBhTQySq%2FPstxcoPp7gEoOgth40J7Y%2BeqEgSGEaEbxsnWlIyKhsUob%2Fe1DsacudDvU12f09D0X6WENt41C80%2FAOXmUtSfa9%2B5pMJGiss4GOqUBWYMddcS3jXc7IeYwfht8ZAHeGoMx5CcxTGE8OpMp2i9nhlnP6DkFmbRVD2QEigNO1a16U0l0sVGNFB9VTBqY%2FbHErACJSh4eOO8BupP%2BzXPCFkJgRnJr9SuOf4RjxOv2mqXOGD0wrRzL2vCSZIUClFQdCqf8V3Q5foFez64VObNr5%2FkLbQvPxFvyn5%2Fh5LjfkO7GaTJhi2o%2Bc%2BbXBrJ7CoRCU0of&X-Amz-Signature=f5c45cddee8d6be4f0e5a30ac9cc421c8877dcd1499630850bbb4348ec6be353&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TJB3OHU%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjkJLphFJf79uqd%2FlgnUJwG933H8WqkQuWfDCyIBQr9QIgan8nuClvjw52pJMjgbMCGDJXRfBNXiLhudwx1kShjZEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCq%2BKrqaFCsgSDJrsCrcA%2Bpbkx1SOBnBp5F5VxmOBxT%2BLM4GZVyT2dBOGsuCurIAhIYq%2FlstKPr9z6NH3ZlMl9xzBvjtoKb%2FZ0MC3w8MbxqPpYo6ETt9ZsFTKYeVG9J5KRhDHCHwHQMLXsUdbSktCAaxq5hrHhy5Ts07bsFcUdGtw6xndUJU2x0hNGgf%2BHGHJLMJwx7g%2FxhINgoUbEhpTHplBOYv1oAjdmUb7YriYtD%2BQ5LrORhxUHJ7dloZf%2FWYDr42Ht366mcrqWFfYCve9FUULa%2B95JfKtK1rqyXhUjCr7FwNiZcxeoMvg3TsyIuf%2Fk1ebMvQBxymN%2FQmyzceLVo2kYXewDNVZYnKjBfN3zXu%2Bk9g3Obb%2B%2FEGNAo8Jkr7yaD4a8Jrf8Kqu0kmJF3iztPXXSvVN1QMejvCZyboevNb%2BpX2ZkAGdL23MNb56YpFKSsA5CP9LX13pp14yEG8jG64vkwJzJc8zqwvJLxA7LJVSl7AeT0K0enhyMIt%2FT39T1gLIidmu%2BMsYV2o8WzUbi0AeK%2Bh2V3q4gCyP%2Fo49zvXBrFBhTQySq%2FPstxcoPp7gEoOgth40J7Y%2BeqEgSGEaEbxsnWlIyKhsUob%2Fe1DsacudDvU12f09D0X6WENt41C80%2FAOXmUtSfa9%2B5pMJGiss4GOqUBWYMddcS3jXc7IeYwfht8ZAHeGoMx5CcxTGE8OpMp2i9nhlnP6DkFmbRVD2QEigNO1a16U0l0sVGNFB9VTBqY%2FbHErACJSh4eOO8BupP%2BzXPCFkJgRnJr9SuOf4RjxOv2mqXOGD0wrRzL2vCSZIUClFQdCqf8V3Q5foFez64VObNr5%2FkLbQvPxFvyn5%2Fh5LjfkO7GaTJhi2o%2Bc%2BbXBrJ7CoRCU0of&X-Amz-Signature=75e22163e26988fcf0f8330de5e5f6890ebe3ce3ffb723f1fb790849481efd8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TJB3OHU%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjkJLphFJf79uqd%2FlgnUJwG933H8WqkQuWfDCyIBQr9QIgan8nuClvjw52pJMjgbMCGDJXRfBNXiLhudwx1kShjZEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCq%2BKrqaFCsgSDJrsCrcA%2Bpbkx1SOBnBp5F5VxmOBxT%2BLM4GZVyT2dBOGsuCurIAhIYq%2FlstKPr9z6NH3ZlMl9xzBvjtoKb%2FZ0MC3w8MbxqPpYo6ETt9ZsFTKYeVG9J5KRhDHCHwHQMLXsUdbSktCAaxq5hrHhy5Ts07bsFcUdGtw6xndUJU2x0hNGgf%2BHGHJLMJwx7g%2FxhINgoUbEhpTHplBOYv1oAjdmUb7YriYtD%2BQ5LrORhxUHJ7dloZf%2FWYDr42Ht366mcrqWFfYCve9FUULa%2B95JfKtK1rqyXhUjCr7FwNiZcxeoMvg3TsyIuf%2Fk1ebMvQBxymN%2FQmyzceLVo2kYXewDNVZYnKjBfN3zXu%2Bk9g3Obb%2B%2FEGNAo8Jkr7yaD4a8Jrf8Kqu0kmJF3iztPXXSvVN1QMejvCZyboevNb%2BpX2ZkAGdL23MNb56YpFKSsA5CP9LX13pp14yEG8jG64vkwJzJc8zqwvJLxA7LJVSl7AeT0K0enhyMIt%2FT39T1gLIidmu%2BMsYV2o8WzUbi0AeK%2Bh2V3q4gCyP%2Fo49zvXBrFBhTQySq%2FPstxcoPp7gEoOgth40J7Y%2BeqEgSGEaEbxsnWlIyKhsUob%2Fe1DsacudDvU12f09D0X6WENt41C80%2FAOXmUtSfa9%2B5pMJGiss4GOqUBWYMddcS3jXc7IeYwfht8ZAHeGoMx5CcxTGE8OpMp2i9nhlnP6DkFmbRVD2QEigNO1a16U0l0sVGNFB9VTBqY%2FbHErACJSh4eOO8BupP%2BzXPCFkJgRnJr9SuOf4RjxOv2mqXOGD0wrRzL2vCSZIUClFQdCqf8V3Q5foFez64VObNr5%2FkLbQvPxFvyn5%2Fh5LjfkO7GaTJhi2o%2Bc%2BbXBrJ7CoRCU0of&X-Amz-Signature=3768333a979245263d20883c245ad7be1f9edf4fce8bdb24e37dbe01e9441408&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TJB3OHU%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjkJLphFJf79uqd%2FlgnUJwG933H8WqkQuWfDCyIBQr9QIgan8nuClvjw52pJMjgbMCGDJXRfBNXiLhudwx1kShjZEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCq%2BKrqaFCsgSDJrsCrcA%2Bpbkx1SOBnBp5F5VxmOBxT%2BLM4GZVyT2dBOGsuCurIAhIYq%2FlstKPr9z6NH3ZlMl9xzBvjtoKb%2FZ0MC3w8MbxqPpYo6ETt9ZsFTKYeVG9J5KRhDHCHwHQMLXsUdbSktCAaxq5hrHhy5Ts07bsFcUdGtw6xndUJU2x0hNGgf%2BHGHJLMJwx7g%2FxhINgoUbEhpTHplBOYv1oAjdmUb7YriYtD%2BQ5LrORhxUHJ7dloZf%2FWYDr42Ht366mcrqWFfYCve9FUULa%2B95JfKtK1rqyXhUjCr7FwNiZcxeoMvg3TsyIuf%2Fk1ebMvQBxymN%2FQmyzceLVo2kYXewDNVZYnKjBfN3zXu%2Bk9g3Obb%2B%2FEGNAo8Jkr7yaD4a8Jrf8Kqu0kmJF3iztPXXSvVN1QMejvCZyboevNb%2BpX2ZkAGdL23MNb56YpFKSsA5CP9LX13pp14yEG8jG64vkwJzJc8zqwvJLxA7LJVSl7AeT0K0enhyMIt%2FT39T1gLIidmu%2BMsYV2o8WzUbi0AeK%2Bh2V3q4gCyP%2Fo49zvXBrFBhTQySq%2FPstxcoPp7gEoOgth40J7Y%2BeqEgSGEaEbxsnWlIyKhsUob%2Fe1DsacudDvU12f09D0X6WENt41C80%2FAOXmUtSfa9%2B5pMJGiss4GOqUBWYMddcS3jXc7IeYwfht8ZAHeGoMx5CcxTGE8OpMp2i9nhlnP6DkFmbRVD2QEigNO1a16U0l0sVGNFB9VTBqY%2FbHErACJSh4eOO8BupP%2BzXPCFkJgRnJr9SuOf4RjxOv2mqXOGD0wrRzL2vCSZIUClFQdCqf8V3Q5foFez64VObNr5%2FkLbQvPxFvyn5%2Fh5LjfkO7GaTJhi2o%2Bc%2BbXBrJ7CoRCU0of&X-Amz-Signature=43f7af51fe152d28918d4385cf73c542b20349892f8a54690ff9c21c8c02e039&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

