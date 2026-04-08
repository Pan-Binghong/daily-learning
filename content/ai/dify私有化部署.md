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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPOQKCF%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDG294j%2FpzJOYbm2zUA0LOyCFy1y5gSOsEdHVVM994B2AiEAiWa73QODX1iNfS1dXXUvFDZ8aV98sFPWaMQhzJc88kMqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BCs3iU0YOmFloD8yrcA986lW5iK4lXzU9JXEjXSv52SXvAHVyZrlBCV4FAakJf%2B0b6iNlOef3iAQdsjPL%2BekApMY%2BQwcpFVM1D3KmBJ2odxxSyqKlD0MoBK0yCzksZzplyXiWqKn%2B0gl4%2Fd2v%2FcnVKXuocW2%2Bd1M3S4TTmrS%2FdYEEoLO3AG2qsdDe8fUWqkgQ3UvuF%2Fzu8DESPGzgdjJv8g6YKz2m0jgvxlxAYbJK5P515F%2FjMDONyTqEpqttuYve%2FXth%2Bde30pUcae9KFjIE5am%2Bj8WyjG8UXNtbrjCBdl0cPoKd4fh5kSNWZULHpMN4%2Fm%2BSOhf%2BajpC3aEDpsdsmUg819RyteuFhSGUNc1B%2Frpmfd9QqcC01l6tQ2cwOxW4DLzCLSFFXc8aztNXKTnipuoyzohMEqMDJuLTFAlOeJEvqWt9bkmE78XKU209u9FckU4Ckgra80%2FVJv7uuEi1NMPXKgfI1bRpQfuc0MKS19lCpym4sVBabDdkQyFQDeIhSO%2F%2Fe8WrO11ZhihMiPXWxxobCIExXxuNJsK14NuORxSB5Va56NTRQA%2FBMC3VrOSA40EOYK0FQ93SH%2FyF%2F3l2NJ%2BpcsKFGxTRKuBnekmUy4QEzGLlDCzY4%2Fs66HChPpvBRJVvv7gYZ2W%2BOMPOH184GOqUBxzgtxieCjdBhdu4arAW%2BOfbFQP%2B8kfZFFxrFzoewRJakACNAldg%2FDmZbF33bp6UNH9%2BJM89EPBd8SMaKvRLpWZeotMvV8xnraUauSzy08YU7d0C5lU7BbwN2l%2F3PZXPMF123W3cgrMARPRsFDvKvrkne%2FAubEeBdQpyOPbgiKD3XC3rsdHqwRBYzRPBKbom9Xs5aJDrQiKHBebRaXymOkCasWiY6&X-Amz-Signature=b67f4aa5cb04de64fbeadddb2f9cba4fd2eb668188a80e95b8da697d666da237&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPOQKCF%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDG294j%2FpzJOYbm2zUA0LOyCFy1y5gSOsEdHVVM994B2AiEAiWa73QODX1iNfS1dXXUvFDZ8aV98sFPWaMQhzJc88kMqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BCs3iU0YOmFloD8yrcA986lW5iK4lXzU9JXEjXSv52SXvAHVyZrlBCV4FAakJf%2B0b6iNlOef3iAQdsjPL%2BekApMY%2BQwcpFVM1D3KmBJ2odxxSyqKlD0MoBK0yCzksZzplyXiWqKn%2B0gl4%2Fd2v%2FcnVKXuocW2%2Bd1M3S4TTmrS%2FdYEEoLO3AG2qsdDe8fUWqkgQ3UvuF%2Fzu8DESPGzgdjJv8g6YKz2m0jgvxlxAYbJK5P515F%2FjMDONyTqEpqttuYve%2FXth%2Bde30pUcae9KFjIE5am%2Bj8WyjG8UXNtbrjCBdl0cPoKd4fh5kSNWZULHpMN4%2Fm%2BSOhf%2BajpC3aEDpsdsmUg819RyteuFhSGUNc1B%2Frpmfd9QqcC01l6tQ2cwOxW4DLzCLSFFXc8aztNXKTnipuoyzohMEqMDJuLTFAlOeJEvqWt9bkmE78XKU209u9FckU4Ckgra80%2FVJv7uuEi1NMPXKgfI1bRpQfuc0MKS19lCpym4sVBabDdkQyFQDeIhSO%2F%2Fe8WrO11ZhihMiPXWxxobCIExXxuNJsK14NuORxSB5Va56NTRQA%2FBMC3VrOSA40EOYK0FQ93SH%2FyF%2F3l2NJ%2BpcsKFGxTRKuBnekmUy4QEzGLlDCzY4%2Fs66HChPpvBRJVvv7gYZ2W%2BOMPOH184GOqUBxzgtxieCjdBhdu4arAW%2BOfbFQP%2B8kfZFFxrFzoewRJakACNAldg%2FDmZbF33bp6UNH9%2BJM89EPBd8SMaKvRLpWZeotMvV8xnraUauSzy08YU7d0C5lU7BbwN2l%2F3PZXPMF123W3cgrMARPRsFDvKvrkne%2FAubEeBdQpyOPbgiKD3XC3rsdHqwRBYzRPBKbom9Xs5aJDrQiKHBebRaXymOkCasWiY6&X-Amz-Signature=b451358d3dbd7434e4f034fea47b1ac192d7c37ca187bfbe99a5a22d84ba32fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPOQKCF%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDG294j%2FpzJOYbm2zUA0LOyCFy1y5gSOsEdHVVM994B2AiEAiWa73QODX1iNfS1dXXUvFDZ8aV98sFPWaMQhzJc88kMqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BCs3iU0YOmFloD8yrcA986lW5iK4lXzU9JXEjXSv52SXvAHVyZrlBCV4FAakJf%2B0b6iNlOef3iAQdsjPL%2BekApMY%2BQwcpFVM1D3KmBJ2odxxSyqKlD0MoBK0yCzksZzplyXiWqKn%2B0gl4%2Fd2v%2FcnVKXuocW2%2Bd1M3S4TTmrS%2FdYEEoLO3AG2qsdDe8fUWqkgQ3UvuF%2Fzu8DESPGzgdjJv8g6YKz2m0jgvxlxAYbJK5P515F%2FjMDONyTqEpqttuYve%2FXth%2Bde30pUcae9KFjIE5am%2Bj8WyjG8UXNtbrjCBdl0cPoKd4fh5kSNWZULHpMN4%2Fm%2BSOhf%2BajpC3aEDpsdsmUg819RyteuFhSGUNc1B%2Frpmfd9QqcC01l6tQ2cwOxW4DLzCLSFFXc8aztNXKTnipuoyzohMEqMDJuLTFAlOeJEvqWt9bkmE78XKU209u9FckU4Ckgra80%2FVJv7uuEi1NMPXKgfI1bRpQfuc0MKS19lCpym4sVBabDdkQyFQDeIhSO%2F%2Fe8WrO11ZhihMiPXWxxobCIExXxuNJsK14NuORxSB5Va56NTRQA%2FBMC3VrOSA40EOYK0FQ93SH%2FyF%2F3l2NJ%2BpcsKFGxTRKuBnekmUy4QEzGLlDCzY4%2Fs66HChPpvBRJVvv7gYZ2W%2BOMPOH184GOqUBxzgtxieCjdBhdu4arAW%2BOfbFQP%2B8kfZFFxrFzoewRJakACNAldg%2FDmZbF33bp6UNH9%2BJM89EPBd8SMaKvRLpWZeotMvV8xnraUauSzy08YU7d0C5lU7BbwN2l%2F3PZXPMF123W3cgrMARPRsFDvKvrkne%2FAubEeBdQpyOPbgiKD3XC3rsdHqwRBYzRPBKbom9Xs5aJDrQiKHBebRaXymOkCasWiY6&X-Amz-Signature=c847bfcf59c8b628c48948fdee1d9279c44b6dbca7d950878102b72199e66e9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPOQKCF%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDG294j%2FpzJOYbm2zUA0LOyCFy1y5gSOsEdHVVM994B2AiEAiWa73QODX1iNfS1dXXUvFDZ8aV98sFPWaMQhzJc88kMqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BCs3iU0YOmFloD8yrcA986lW5iK4lXzU9JXEjXSv52SXvAHVyZrlBCV4FAakJf%2B0b6iNlOef3iAQdsjPL%2BekApMY%2BQwcpFVM1D3KmBJ2odxxSyqKlD0MoBK0yCzksZzplyXiWqKn%2B0gl4%2Fd2v%2FcnVKXuocW2%2Bd1M3S4TTmrS%2FdYEEoLO3AG2qsdDe8fUWqkgQ3UvuF%2Fzu8DESPGzgdjJv8g6YKz2m0jgvxlxAYbJK5P515F%2FjMDONyTqEpqttuYve%2FXth%2Bde30pUcae9KFjIE5am%2Bj8WyjG8UXNtbrjCBdl0cPoKd4fh5kSNWZULHpMN4%2Fm%2BSOhf%2BajpC3aEDpsdsmUg819RyteuFhSGUNc1B%2Frpmfd9QqcC01l6tQ2cwOxW4DLzCLSFFXc8aztNXKTnipuoyzohMEqMDJuLTFAlOeJEvqWt9bkmE78XKU209u9FckU4Ckgra80%2FVJv7uuEi1NMPXKgfI1bRpQfuc0MKS19lCpym4sVBabDdkQyFQDeIhSO%2F%2Fe8WrO11ZhihMiPXWxxobCIExXxuNJsK14NuORxSB5Va56NTRQA%2FBMC3VrOSA40EOYK0FQ93SH%2FyF%2F3l2NJ%2BpcsKFGxTRKuBnekmUy4QEzGLlDCzY4%2Fs66HChPpvBRJVvv7gYZ2W%2BOMPOH184GOqUBxzgtxieCjdBhdu4arAW%2BOfbFQP%2B8kfZFFxrFzoewRJakACNAldg%2FDmZbF33bp6UNH9%2BJM89EPBd8SMaKvRLpWZeotMvV8xnraUauSzy08YU7d0C5lU7BbwN2l%2F3PZXPMF123W3cgrMARPRsFDvKvrkne%2FAubEeBdQpyOPbgiKD3XC3rsdHqwRBYzRPBKbom9Xs5aJDrQiKHBebRaXymOkCasWiY6&X-Amz-Signature=68f8915a540ba73bac38773d22f36a4bd18d29c4e97c0101a4208d23ada38b1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPOQKCF%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDG294j%2FpzJOYbm2zUA0LOyCFy1y5gSOsEdHVVM994B2AiEAiWa73QODX1iNfS1dXXUvFDZ8aV98sFPWaMQhzJc88kMqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BCs3iU0YOmFloD8yrcA986lW5iK4lXzU9JXEjXSv52SXvAHVyZrlBCV4FAakJf%2B0b6iNlOef3iAQdsjPL%2BekApMY%2BQwcpFVM1D3KmBJ2odxxSyqKlD0MoBK0yCzksZzplyXiWqKn%2B0gl4%2Fd2v%2FcnVKXuocW2%2Bd1M3S4TTmrS%2FdYEEoLO3AG2qsdDe8fUWqkgQ3UvuF%2Fzu8DESPGzgdjJv8g6YKz2m0jgvxlxAYbJK5P515F%2FjMDONyTqEpqttuYve%2FXth%2Bde30pUcae9KFjIE5am%2Bj8WyjG8UXNtbrjCBdl0cPoKd4fh5kSNWZULHpMN4%2Fm%2BSOhf%2BajpC3aEDpsdsmUg819RyteuFhSGUNc1B%2Frpmfd9QqcC01l6tQ2cwOxW4DLzCLSFFXc8aztNXKTnipuoyzohMEqMDJuLTFAlOeJEvqWt9bkmE78XKU209u9FckU4Ckgra80%2FVJv7uuEi1NMPXKgfI1bRpQfuc0MKS19lCpym4sVBabDdkQyFQDeIhSO%2F%2Fe8WrO11ZhihMiPXWxxobCIExXxuNJsK14NuORxSB5Va56NTRQA%2FBMC3VrOSA40EOYK0FQ93SH%2FyF%2F3l2NJ%2BpcsKFGxTRKuBnekmUy4QEzGLlDCzY4%2Fs66HChPpvBRJVvv7gYZ2W%2BOMPOH184GOqUBxzgtxieCjdBhdu4arAW%2BOfbFQP%2B8kfZFFxrFzoewRJakACNAldg%2FDmZbF33bp6UNH9%2BJM89EPBd8SMaKvRLpWZeotMvV8xnraUauSzy08YU7d0C5lU7BbwN2l%2F3PZXPMF123W3cgrMARPRsFDvKvrkne%2FAubEeBdQpyOPbgiKD3XC3rsdHqwRBYzRPBKbom9Xs5aJDrQiKHBebRaXymOkCasWiY6&X-Amz-Signature=677edb88a30d2ef27dbd01f585b9bebc44a5e787d38eca25695f8cbe4e00cd18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPOQKCF%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDG294j%2FpzJOYbm2zUA0LOyCFy1y5gSOsEdHVVM994B2AiEAiWa73QODX1iNfS1dXXUvFDZ8aV98sFPWaMQhzJc88kMqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BCs3iU0YOmFloD8yrcA986lW5iK4lXzU9JXEjXSv52SXvAHVyZrlBCV4FAakJf%2B0b6iNlOef3iAQdsjPL%2BekApMY%2BQwcpFVM1D3KmBJ2odxxSyqKlD0MoBK0yCzksZzplyXiWqKn%2B0gl4%2Fd2v%2FcnVKXuocW2%2Bd1M3S4TTmrS%2FdYEEoLO3AG2qsdDe8fUWqkgQ3UvuF%2Fzu8DESPGzgdjJv8g6YKz2m0jgvxlxAYbJK5P515F%2FjMDONyTqEpqttuYve%2FXth%2Bde30pUcae9KFjIE5am%2Bj8WyjG8UXNtbrjCBdl0cPoKd4fh5kSNWZULHpMN4%2Fm%2BSOhf%2BajpC3aEDpsdsmUg819RyteuFhSGUNc1B%2Frpmfd9QqcC01l6tQ2cwOxW4DLzCLSFFXc8aztNXKTnipuoyzohMEqMDJuLTFAlOeJEvqWt9bkmE78XKU209u9FckU4Ckgra80%2FVJv7uuEi1NMPXKgfI1bRpQfuc0MKS19lCpym4sVBabDdkQyFQDeIhSO%2F%2Fe8WrO11ZhihMiPXWxxobCIExXxuNJsK14NuORxSB5Va56NTRQA%2FBMC3VrOSA40EOYK0FQ93SH%2FyF%2F3l2NJ%2BpcsKFGxTRKuBnekmUy4QEzGLlDCzY4%2Fs66HChPpvBRJVvv7gYZ2W%2BOMPOH184GOqUBxzgtxieCjdBhdu4arAW%2BOfbFQP%2B8kfZFFxrFzoewRJakACNAldg%2FDmZbF33bp6UNH9%2BJM89EPBd8SMaKvRLpWZeotMvV8xnraUauSzy08YU7d0C5lU7BbwN2l%2F3PZXPMF123W3cgrMARPRsFDvKvrkne%2FAubEeBdQpyOPbgiKD3XC3rsdHqwRBYzRPBKbom9Xs5aJDrQiKHBebRaXymOkCasWiY6&X-Amz-Signature=e569506d676b6e5f4c463e023d83b8fab89b25f28da4c032be9fd6b1576c4a3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPOQKCF%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDG294j%2FpzJOYbm2zUA0LOyCFy1y5gSOsEdHVVM994B2AiEAiWa73QODX1iNfS1dXXUvFDZ8aV98sFPWaMQhzJc88kMqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BCs3iU0YOmFloD8yrcA986lW5iK4lXzU9JXEjXSv52SXvAHVyZrlBCV4FAakJf%2B0b6iNlOef3iAQdsjPL%2BekApMY%2BQwcpFVM1D3KmBJ2odxxSyqKlD0MoBK0yCzksZzplyXiWqKn%2B0gl4%2Fd2v%2FcnVKXuocW2%2Bd1M3S4TTmrS%2FdYEEoLO3AG2qsdDe8fUWqkgQ3UvuF%2Fzu8DESPGzgdjJv8g6YKz2m0jgvxlxAYbJK5P515F%2FjMDONyTqEpqttuYve%2FXth%2Bde30pUcae9KFjIE5am%2Bj8WyjG8UXNtbrjCBdl0cPoKd4fh5kSNWZULHpMN4%2Fm%2BSOhf%2BajpC3aEDpsdsmUg819RyteuFhSGUNc1B%2Frpmfd9QqcC01l6tQ2cwOxW4DLzCLSFFXc8aztNXKTnipuoyzohMEqMDJuLTFAlOeJEvqWt9bkmE78XKU209u9FckU4Ckgra80%2FVJv7uuEi1NMPXKgfI1bRpQfuc0MKS19lCpym4sVBabDdkQyFQDeIhSO%2F%2Fe8WrO11ZhihMiPXWxxobCIExXxuNJsK14NuORxSB5Va56NTRQA%2FBMC3VrOSA40EOYK0FQ93SH%2FyF%2F3l2NJ%2BpcsKFGxTRKuBnekmUy4QEzGLlDCzY4%2Fs66HChPpvBRJVvv7gYZ2W%2BOMPOH184GOqUBxzgtxieCjdBhdu4arAW%2BOfbFQP%2B8kfZFFxrFzoewRJakACNAldg%2FDmZbF33bp6UNH9%2BJM89EPBd8SMaKvRLpWZeotMvV8xnraUauSzy08YU7d0C5lU7BbwN2l%2F3PZXPMF123W3cgrMARPRsFDvKvrkne%2FAubEeBdQpyOPbgiKD3XC3rsdHqwRBYzRPBKbom9Xs5aJDrQiKHBebRaXymOkCasWiY6&X-Amz-Signature=b17b74b11c1ddcd1d5423b78aaf23c2a7658204b0fb17933efc334fb050609a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPOQKCF%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDG294j%2FpzJOYbm2zUA0LOyCFy1y5gSOsEdHVVM994B2AiEAiWa73QODX1iNfS1dXXUvFDZ8aV98sFPWaMQhzJc88kMqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BCs3iU0YOmFloD8yrcA986lW5iK4lXzU9JXEjXSv52SXvAHVyZrlBCV4FAakJf%2B0b6iNlOef3iAQdsjPL%2BekApMY%2BQwcpFVM1D3KmBJ2odxxSyqKlD0MoBK0yCzksZzplyXiWqKn%2B0gl4%2Fd2v%2FcnVKXuocW2%2Bd1M3S4TTmrS%2FdYEEoLO3AG2qsdDe8fUWqkgQ3UvuF%2Fzu8DESPGzgdjJv8g6YKz2m0jgvxlxAYbJK5P515F%2FjMDONyTqEpqttuYve%2FXth%2Bde30pUcae9KFjIE5am%2Bj8WyjG8UXNtbrjCBdl0cPoKd4fh5kSNWZULHpMN4%2Fm%2BSOhf%2BajpC3aEDpsdsmUg819RyteuFhSGUNc1B%2Frpmfd9QqcC01l6tQ2cwOxW4DLzCLSFFXc8aztNXKTnipuoyzohMEqMDJuLTFAlOeJEvqWt9bkmE78XKU209u9FckU4Ckgra80%2FVJv7uuEi1NMPXKgfI1bRpQfuc0MKS19lCpym4sVBabDdkQyFQDeIhSO%2F%2Fe8WrO11ZhihMiPXWxxobCIExXxuNJsK14NuORxSB5Va56NTRQA%2FBMC3VrOSA40EOYK0FQ93SH%2FyF%2F3l2NJ%2BpcsKFGxTRKuBnekmUy4QEzGLlDCzY4%2Fs66HChPpvBRJVvv7gYZ2W%2BOMPOH184GOqUBxzgtxieCjdBhdu4arAW%2BOfbFQP%2B8kfZFFxrFzoewRJakACNAldg%2FDmZbF33bp6UNH9%2BJM89EPBd8SMaKvRLpWZeotMvV8xnraUauSzy08YU7d0C5lU7BbwN2l%2F3PZXPMF123W3cgrMARPRsFDvKvrkne%2FAubEeBdQpyOPbgiKD3XC3rsdHqwRBYzRPBKbom9Xs5aJDrQiKHBebRaXymOkCasWiY6&X-Amz-Signature=83aad7659162468aaf27b2c4010312b4a3f1f5a7fe6a4d7ea3ff8628d2d345fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPOQKCF%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDG294j%2FpzJOYbm2zUA0LOyCFy1y5gSOsEdHVVM994B2AiEAiWa73QODX1iNfS1dXXUvFDZ8aV98sFPWaMQhzJc88kMqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BCs3iU0YOmFloD8yrcA986lW5iK4lXzU9JXEjXSv52SXvAHVyZrlBCV4FAakJf%2B0b6iNlOef3iAQdsjPL%2BekApMY%2BQwcpFVM1D3KmBJ2odxxSyqKlD0MoBK0yCzksZzplyXiWqKn%2B0gl4%2Fd2v%2FcnVKXuocW2%2Bd1M3S4TTmrS%2FdYEEoLO3AG2qsdDe8fUWqkgQ3UvuF%2Fzu8DESPGzgdjJv8g6YKz2m0jgvxlxAYbJK5P515F%2FjMDONyTqEpqttuYve%2FXth%2Bde30pUcae9KFjIE5am%2Bj8WyjG8UXNtbrjCBdl0cPoKd4fh5kSNWZULHpMN4%2Fm%2BSOhf%2BajpC3aEDpsdsmUg819RyteuFhSGUNc1B%2Frpmfd9QqcC01l6tQ2cwOxW4DLzCLSFFXc8aztNXKTnipuoyzohMEqMDJuLTFAlOeJEvqWt9bkmE78XKU209u9FckU4Ckgra80%2FVJv7uuEi1NMPXKgfI1bRpQfuc0MKS19lCpym4sVBabDdkQyFQDeIhSO%2F%2Fe8WrO11ZhihMiPXWxxobCIExXxuNJsK14NuORxSB5Va56NTRQA%2FBMC3VrOSA40EOYK0FQ93SH%2FyF%2F3l2NJ%2BpcsKFGxTRKuBnekmUy4QEzGLlDCzY4%2Fs66HChPpvBRJVvv7gYZ2W%2BOMPOH184GOqUBxzgtxieCjdBhdu4arAW%2BOfbFQP%2B8kfZFFxrFzoewRJakACNAldg%2FDmZbF33bp6UNH9%2BJM89EPBd8SMaKvRLpWZeotMvV8xnraUauSzy08YU7d0C5lU7BbwN2l%2F3PZXPMF123W3cgrMARPRsFDvKvrkne%2FAubEeBdQpyOPbgiKD3XC3rsdHqwRBYzRPBKbom9Xs5aJDrQiKHBebRaXymOkCasWiY6&X-Amz-Signature=06dbb75a95aac60f8d1ce2ecce026aa5f0d62080ba806cad69ac31bb9eeaa0d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLPOQKCF%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDG294j%2FpzJOYbm2zUA0LOyCFy1y5gSOsEdHVVM994B2AiEAiWa73QODX1iNfS1dXXUvFDZ8aV98sFPWaMQhzJc88kMqiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BCs3iU0YOmFloD8yrcA986lW5iK4lXzU9JXEjXSv52SXvAHVyZrlBCV4FAakJf%2B0b6iNlOef3iAQdsjPL%2BekApMY%2BQwcpFVM1D3KmBJ2odxxSyqKlD0MoBK0yCzksZzplyXiWqKn%2B0gl4%2Fd2v%2FcnVKXuocW2%2Bd1M3S4TTmrS%2FdYEEoLO3AG2qsdDe8fUWqkgQ3UvuF%2Fzu8DESPGzgdjJv8g6YKz2m0jgvxlxAYbJK5P515F%2FjMDONyTqEpqttuYve%2FXth%2Bde30pUcae9KFjIE5am%2Bj8WyjG8UXNtbrjCBdl0cPoKd4fh5kSNWZULHpMN4%2Fm%2BSOhf%2BajpC3aEDpsdsmUg819RyteuFhSGUNc1B%2Frpmfd9QqcC01l6tQ2cwOxW4DLzCLSFFXc8aztNXKTnipuoyzohMEqMDJuLTFAlOeJEvqWt9bkmE78XKU209u9FckU4Ckgra80%2FVJv7uuEi1NMPXKgfI1bRpQfuc0MKS19lCpym4sVBabDdkQyFQDeIhSO%2F%2Fe8WrO11ZhihMiPXWxxobCIExXxuNJsK14NuORxSB5Va56NTRQA%2FBMC3VrOSA40EOYK0FQ93SH%2FyF%2F3l2NJ%2BpcsKFGxTRKuBnekmUy4QEzGLlDCzY4%2Fs66HChPpvBRJVvv7gYZ2W%2BOMPOH184GOqUBxzgtxieCjdBhdu4arAW%2BOfbFQP%2B8kfZFFxrFzoewRJakACNAldg%2FDmZbF33bp6UNH9%2BJM89EPBd8SMaKvRLpWZeotMvV8xnraUauSzy08YU7d0C5lU7BbwN2l%2F3PZXPMF123W3cgrMARPRsFDvKvrkne%2FAubEeBdQpyOPbgiKD3XC3rsdHqwRBYzRPBKbom9Xs5aJDrQiKHBebRaXymOkCasWiY6&X-Amz-Signature=2e0f17523fc4522d86ac336ceff4baa281cd5eebd866057ff7a6b1ac61eea43b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

