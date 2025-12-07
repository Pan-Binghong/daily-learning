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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIHUP7D%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVk8M1UvneOz4uB2l5gAvaxL5LL2yzUIOCnJi9ALwJ9AiEAvmfwqizcIVwTEDoorjpHMssR9OIZoFniNLGn2H7rff4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyFHmgAT6OpI3PMRircA%2BmsnlBYSSBoApQZ32UxDwyIdVl44zhykkkwp136EEmAfCxHrbrkvNFIBdYc7hGodqmvPoQTsOrqDFhyagmxKCpKRrC%2FdbAzj99HsGRMc2ttmGrJJwieIbBvvK4Ej1JeShWh%2FM2gWj4IhJPx7PkJfO%2FU89CSxes1I7EuRrIf6XUz4osaJKkjRhZ4rHSmPoouP99rQ8trcH74MOxC5Ah6ozBVx2OoEXYfpXJIBxqq1ox4mRTDv2KUWfDbxs9HYiFGiDHQnR6Mt0mh%2BOFeNGpu0TIs5KfYEXkVmgBCjsyt0R0sdIaY9pWM81BpDtGl0LRG6PaglZcnbopV05mp3zThbNV6Q07CicX7FaRmxEmt99fLF7kagr7zBJByn%2FTMhhP7yEG4G6e1IbFOmAa%2F33GTTteX1L1E7hMVIRIuGh38Zc9AximnVXFbsDYxW2BNGGWufQnpAPSb5n2riG8h%2BtO5dwQI0IwIUQD%2FwLL7yVIiNJzOF33S%2B%2BXWuPdwYaqJDLimzHSirnZRsI0b9vA8ibBatljKuzDQ0WFr0mpLiP3RnZyNMC93fpW4DaItnls6YhLPN0VrOeQQojbIiCWNXvgJXHFbzljXkFaG%2F0KTvrE7q9nKm%2FoQytKo3K7hvpP%2BMPj90skGOqUBDg9jfa76fKOh%2FGRiNREOa3AU37M%2FZfHvATkfFFwwfdw2c5TUm0k7L%2BaO6pWZ6r14zPruERM5eQWPOi2CWl9ppIV35griANq2ZPb5j8zFi9i10mDHmN%2BsKzvt7vG19%2FiL8t5AW4egtbkm9I6WzOJ%2Bi36klBUDjVzO59nha%2Fa6o0qf6Q5Hb2kw1Z5w7xpzaTjiGirWd8FC5kzFj%2FE4yLum6gtlqm5f&X-Amz-Signature=672256957ae569338c7d420f9752dd80abe9d492813500f51410613e5ccc5860&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIHUP7D%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVk8M1UvneOz4uB2l5gAvaxL5LL2yzUIOCnJi9ALwJ9AiEAvmfwqizcIVwTEDoorjpHMssR9OIZoFniNLGn2H7rff4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyFHmgAT6OpI3PMRircA%2BmsnlBYSSBoApQZ32UxDwyIdVl44zhykkkwp136EEmAfCxHrbrkvNFIBdYc7hGodqmvPoQTsOrqDFhyagmxKCpKRrC%2FdbAzj99HsGRMc2ttmGrJJwieIbBvvK4Ej1JeShWh%2FM2gWj4IhJPx7PkJfO%2FU89CSxes1I7EuRrIf6XUz4osaJKkjRhZ4rHSmPoouP99rQ8trcH74MOxC5Ah6ozBVx2OoEXYfpXJIBxqq1ox4mRTDv2KUWfDbxs9HYiFGiDHQnR6Mt0mh%2BOFeNGpu0TIs5KfYEXkVmgBCjsyt0R0sdIaY9pWM81BpDtGl0LRG6PaglZcnbopV05mp3zThbNV6Q07CicX7FaRmxEmt99fLF7kagr7zBJByn%2FTMhhP7yEG4G6e1IbFOmAa%2F33GTTteX1L1E7hMVIRIuGh38Zc9AximnVXFbsDYxW2BNGGWufQnpAPSb5n2riG8h%2BtO5dwQI0IwIUQD%2FwLL7yVIiNJzOF33S%2B%2BXWuPdwYaqJDLimzHSirnZRsI0b9vA8ibBatljKuzDQ0WFr0mpLiP3RnZyNMC93fpW4DaItnls6YhLPN0VrOeQQojbIiCWNXvgJXHFbzljXkFaG%2F0KTvrE7q9nKm%2FoQytKo3K7hvpP%2BMPj90skGOqUBDg9jfa76fKOh%2FGRiNREOa3AU37M%2FZfHvATkfFFwwfdw2c5TUm0k7L%2BaO6pWZ6r14zPruERM5eQWPOi2CWl9ppIV35griANq2ZPb5j8zFi9i10mDHmN%2BsKzvt7vG19%2FiL8t5AW4egtbkm9I6WzOJ%2Bi36klBUDjVzO59nha%2Fa6o0qf6Q5Hb2kw1Z5w7xpzaTjiGirWd8FC5kzFj%2FE4yLum6gtlqm5f&X-Amz-Signature=1fc79c242b52cfdab678b94ada1f9d5f10c2663c0d98c074f76fcd7f74d47119&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIHUP7D%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVk8M1UvneOz4uB2l5gAvaxL5LL2yzUIOCnJi9ALwJ9AiEAvmfwqizcIVwTEDoorjpHMssR9OIZoFniNLGn2H7rff4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyFHmgAT6OpI3PMRircA%2BmsnlBYSSBoApQZ32UxDwyIdVl44zhykkkwp136EEmAfCxHrbrkvNFIBdYc7hGodqmvPoQTsOrqDFhyagmxKCpKRrC%2FdbAzj99HsGRMc2ttmGrJJwieIbBvvK4Ej1JeShWh%2FM2gWj4IhJPx7PkJfO%2FU89CSxes1I7EuRrIf6XUz4osaJKkjRhZ4rHSmPoouP99rQ8trcH74MOxC5Ah6ozBVx2OoEXYfpXJIBxqq1ox4mRTDv2KUWfDbxs9HYiFGiDHQnR6Mt0mh%2BOFeNGpu0TIs5KfYEXkVmgBCjsyt0R0sdIaY9pWM81BpDtGl0LRG6PaglZcnbopV05mp3zThbNV6Q07CicX7FaRmxEmt99fLF7kagr7zBJByn%2FTMhhP7yEG4G6e1IbFOmAa%2F33GTTteX1L1E7hMVIRIuGh38Zc9AximnVXFbsDYxW2BNGGWufQnpAPSb5n2riG8h%2BtO5dwQI0IwIUQD%2FwLL7yVIiNJzOF33S%2B%2BXWuPdwYaqJDLimzHSirnZRsI0b9vA8ibBatljKuzDQ0WFr0mpLiP3RnZyNMC93fpW4DaItnls6YhLPN0VrOeQQojbIiCWNXvgJXHFbzljXkFaG%2F0KTvrE7q9nKm%2FoQytKo3K7hvpP%2BMPj90skGOqUBDg9jfa76fKOh%2FGRiNREOa3AU37M%2FZfHvATkfFFwwfdw2c5TUm0k7L%2BaO6pWZ6r14zPruERM5eQWPOi2CWl9ppIV35griANq2ZPb5j8zFi9i10mDHmN%2BsKzvt7vG19%2FiL8t5AW4egtbkm9I6WzOJ%2Bi36klBUDjVzO59nha%2Fa6o0qf6Q5Hb2kw1Z5w7xpzaTjiGirWd8FC5kzFj%2FE4yLum6gtlqm5f&X-Amz-Signature=5e3964c43ecc48ece4e68ae971f6a63d9f8617dfd6920501ed8bf5c3ec4838a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIHUP7D%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVk8M1UvneOz4uB2l5gAvaxL5LL2yzUIOCnJi9ALwJ9AiEAvmfwqizcIVwTEDoorjpHMssR9OIZoFniNLGn2H7rff4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyFHmgAT6OpI3PMRircA%2BmsnlBYSSBoApQZ32UxDwyIdVl44zhykkkwp136EEmAfCxHrbrkvNFIBdYc7hGodqmvPoQTsOrqDFhyagmxKCpKRrC%2FdbAzj99HsGRMc2ttmGrJJwieIbBvvK4Ej1JeShWh%2FM2gWj4IhJPx7PkJfO%2FU89CSxes1I7EuRrIf6XUz4osaJKkjRhZ4rHSmPoouP99rQ8trcH74MOxC5Ah6ozBVx2OoEXYfpXJIBxqq1ox4mRTDv2KUWfDbxs9HYiFGiDHQnR6Mt0mh%2BOFeNGpu0TIs5KfYEXkVmgBCjsyt0R0sdIaY9pWM81BpDtGl0LRG6PaglZcnbopV05mp3zThbNV6Q07CicX7FaRmxEmt99fLF7kagr7zBJByn%2FTMhhP7yEG4G6e1IbFOmAa%2F33GTTteX1L1E7hMVIRIuGh38Zc9AximnVXFbsDYxW2BNGGWufQnpAPSb5n2riG8h%2BtO5dwQI0IwIUQD%2FwLL7yVIiNJzOF33S%2B%2BXWuPdwYaqJDLimzHSirnZRsI0b9vA8ibBatljKuzDQ0WFr0mpLiP3RnZyNMC93fpW4DaItnls6YhLPN0VrOeQQojbIiCWNXvgJXHFbzljXkFaG%2F0KTvrE7q9nKm%2FoQytKo3K7hvpP%2BMPj90skGOqUBDg9jfa76fKOh%2FGRiNREOa3AU37M%2FZfHvATkfFFwwfdw2c5TUm0k7L%2BaO6pWZ6r14zPruERM5eQWPOi2CWl9ppIV35griANq2ZPb5j8zFi9i10mDHmN%2BsKzvt7vG19%2FiL8t5AW4egtbkm9I6WzOJ%2Bi36klBUDjVzO59nha%2Fa6o0qf6Q5Hb2kw1Z5w7xpzaTjiGirWd8FC5kzFj%2FE4yLum6gtlqm5f&X-Amz-Signature=5d5ebde799c223db66221639827377c1dd8a714f8a44bfb91c8460e2ae97dc61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIHUP7D%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVk8M1UvneOz4uB2l5gAvaxL5LL2yzUIOCnJi9ALwJ9AiEAvmfwqizcIVwTEDoorjpHMssR9OIZoFniNLGn2H7rff4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyFHmgAT6OpI3PMRircA%2BmsnlBYSSBoApQZ32UxDwyIdVl44zhykkkwp136EEmAfCxHrbrkvNFIBdYc7hGodqmvPoQTsOrqDFhyagmxKCpKRrC%2FdbAzj99HsGRMc2ttmGrJJwieIbBvvK4Ej1JeShWh%2FM2gWj4IhJPx7PkJfO%2FU89CSxes1I7EuRrIf6XUz4osaJKkjRhZ4rHSmPoouP99rQ8trcH74MOxC5Ah6ozBVx2OoEXYfpXJIBxqq1ox4mRTDv2KUWfDbxs9HYiFGiDHQnR6Mt0mh%2BOFeNGpu0TIs5KfYEXkVmgBCjsyt0R0sdIaY9pWM81BpDtGl0LRG6PaglZcnbopV05mp3zThbNV6Q07CicX7FaRmxEmt99fLF7kagr7zBJByn%2FTMhhP7yEG4G6e1IbFOmAa%2F33GTTteX1L1E7hMVIRIuGh38Zc9AximnVXFbsDYxW2BNGGWufQnpAPSb5n2riG8h%2BtO5dwQI0IwIUQD%2FwLL7yVIiNJzOF33S%2B%2BXWuPdwYaqJDLimzHSirnZRsI0b9vA8ibBatljKuzDQ0WFr0mpLiP3RnZyNMC93fpW4DaItnls6YhLPN0VrOeQQojbIiCWNXvgJXHFbzljXkFaG%2F0KTvrE7q9nKm%2FoQytKo3K7hvpP%2BMPj90skGOqUBDg9jfa76fKOh%2FGRiNREOa3AU37M%2FZfHvATkfFFwwfdw2c5TUm0k7L%2BaO6pWZ6r14zPruERM5eQWPOi2CWl9ppIV35griANq2ZPb5j8zFi9i10mDHmN%2BsKzvt7vG19%2FiL8t5AW4egtbkm9I6WzOJ%2Bi36klBUDjVzO59nha%2Fa6o0qf6Q5Hb2kw1Z5w7xpzaTjiGirWd8FC5kzFj%2FE4yLum6gtlqm5f&X-Amz-Signature=2c0e117c3d822d80e29c738e550c32d196cb5fa88987e29cb5257ce882b8f386&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIHUP7D%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVk8M1UvneOz4uB2l5gAvaxL5LL2yzUIOCnJi9ALwJ9AiEAvmfwqizcIVwTEDoorjpHMssR9OIZoFniNLGn2H7rff4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyFHmgAT6OpI3PMRircA%2BmsnlBYSSBoApQZ32UxDwyIdVl44zhykkkwp136EEmAfCxHrbrkvNFIBdYc7hGodqmvPoQTsOrqDFhyagmxKCpKRrC%2FdbAzj99HsGRMc2ttmGrJJwieIbBvvK4Ej1JeShWh%2FM2gWj4IhJPx7PkJfO%2FU89CSxes1I7EuRrIf6XUz4osaJKkjRhZ4rHSmPoouP99rQ8trcH74MOxC5Ah6ozBVx2OoEXYfpXJIBxqq1ox4mRTDv2KUWfDbxs9HYiFGiDHQnR6Mt0mh%2BOFeNGpu0TIs5KfYEXkVmgBCjsyt0R0sdIaY9pWM81BpDtGl0LRG6PaglZcnbopV05mp3zThbNV6Q07CicX7FaRmxEmt99fLF7kagr7zBJByn%2FTMhhP7yEG4G6e1IbFOmAa%2F33GTTteX1L1E7hMVIRIuGh38Zc9AximnVXFbsDYxW2BNGGWufQnpAPSb5n2riG8h%2BtO5dwQI0IwIUQD%2FwLL7yVIiNJzOF33S%2B%2BXWuPdwYaqJDLimzHSirnZRsI0b9vA8ibBatljKuzDQ0WFr0mpLiP3RnZyNMC93fpW4DaItnls6YhLPN0VrOeQQojbIiCWNXvgJXHFbzljXkFaG%2F0KTvrE7q9nKm%2FoQytKo3K7hvpP%2BMPj90skGOqUBDg9jfa76fKOh%2FGRiNREOa3AU37M%2FZfHvATkfFFwwfdw2c5TUm0k7L%2BaO6pWZ6r14zPruERM5eQWPOi2CWl9ppIV35griANq2ZPb5j8zFi9i10mDHmN%2BsKzvt7vG19%2FiL8t5AW4egtbkm9I6WzOJ%2Bi36klBUDjVzO59nha%2Fa6o0qf6Q5Hb2kw1Z5w7xpzaTjiGirWd8FC5kzFj%2FE4yLum6gtlqm5f&X-Amz-Signature=538e151f4793a0015eb53727a52c24d2e59168be78d5c615fe152ea32db6af34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIHUP7D%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVk8M1UvneOz4uB2l5gAvaxL5LL2yzUIOCnJi9ALwJ9AiEAvmfwqizcIVwTEDoorjpHMssR9OIZoFniNLGn2H7rff4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyFHmgAT6OpI3PMRircA%2BmsnlBYSSBoApQZ32UxDwyIdVl44zhykkkwp136EEmAfCxHrbrkvNFIBdYc7hGodqmvPoQTsOrqDFhyagmxKCpKRrC%2FdbAzj99HsGRMc2ttmGrJJwieIbBvvK4Ej1JeShWh%2FM2gWj4IhJPx7PkJfO%2FU89CSxes1I7EuRrIf6XUz4osaJKkjRhZ4rHSmPoouP99rQ8trcH74MOxC5Ah6ozBVx2OoEXYfpXJIBxqq1ox4mRTDv2KUWfDbxs9HYiFGiDHQnR6Mt0mh%2BOFeNGpu0TIs5KfYEXkVmgBCjsyt0R0sdIaY9pWM81BpDtGl0LRG6PaglZcnbopV05mp3zThbNV6Q07CicX7FaRmxEmt99fLF7kagr7zBJByn%2FTMhhP7yEG4G6e1IbFOmAa%2F33GTTteX1L1E7hMVIRIuGh38Zc9AximnVXFbsDYxW2BNGGWufQnpAPSb5n2riG8h%2BtO5dwQI0IwIUQD%2FwLL7yVIiNJzOF33S%2B%2BXWuPdwYaqJDLimzHSirnZRsI0b9vA8ibBatljKuzDQ0WFr0mpLiP3RnZyNMC93fpW4DaItnls6YhLPN0VrOeQQojbIiCWNXvgJXHFbzljXkFaG%2F0KTvrE7q9nKm%2FoQytKo3K7hvpP%2BMPj90skGOqUBDg9jfa76fKOh%2FGRiNREOa3AU37M%2FZfHvATkfFFwwfdw2c5TUm0k7L%2BaO6pWZ6r14zPruERM5eQWPOi2CWl9ppIV35griANq2ZPb5j8zFi9i10mDHmN%2BsKzvt7vG19%2FiL8t5AW4egtbkm9I6WzOJ%2Bi36klBUDjVzO59nha%2Fa6o0qf6Q5Hb2kw1Z5w7xpzaTjiGirWd8FC5kzFj%2FE4yLum6gtlqm5f&X-Amz-Signature=7ec9d13878346f8d25ffbc3f20c2fddc42ed7eaaadde99730cd10b36c8f0d4ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIHUP7D%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVk8M1UvneOz4uB2l5gAvaxL5LL2yzUIOCnJi9ALwJ9AiEAvmfwqizcIVwTEDoorjpHMssR9OIZoFniNLGn2H7rff4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyFHmgAT6OpI3PMRircA%2BmsnlBYSSBoApQZ32UxDwyIdVl44zhykkkwp136EEmAfCxHrbrkvNFIBdYc7hGodqmvPoQTsOrqDFhyagmxKCpKRrC%2FdbAzj99HsGRMc2ttmGrJJwieIbBvvK4Ej1JeShWh%2FM2gWj4IhJPx7PkJfO%2FU89CSxes1I7EuRrIf6XUz4osaJKkjRhZ4rHSmPoouP99rQ8trcH74MOxC5Ah6ozBVx2OoEXYfpXJIBxqq1ox4mRTDv2KUWfDbxs9HYiFGiDHQnR6Mt0mh%2BOFeNGpu0TIs5KfYEXkVmgBCjsyt0R0sdIaY9pWM81BpDtGl0LRG6PaglZcnbopV05mp3zThbNV6Q07CicX7FaRmxEmt99fLF7kagr7zBJByn%2FTMhhP7yEG4G6e1IbFOmAa%2F33GTTteX1L1E7hMVIRIuGh38Zc9AximnVXFbsDYxW2BNGGWufQnpAPSb5n2riG8h%2BtO5dwQI0IwIUQD%2FwLL7yVIiNJzOF33S%2B%2BXWuPdwYaqJDLimzHSirnZRsI0b9vA8ibBatljKuzDQ0WFr0mpLiP3RnZyNMC93fpW4DaItnls6YhLPN0VrOeQQojbIiCWNXvgJXHFbzljXkFaG%2F0KTvrE7q9nKm%2FoQytKo3K7hvpP%2BMPj90skGOqUBDg9jfa76fKOh%2FGRiNREOa3AU37M%2FZfHvATkfFFwwfdw2c5TUm0k7L%2BaO6pWZ6r14zPruERM5eQWPOi2CWl9ppIV35griANq2ZPb5j8zFi9i10mDHmN%2BsKzvt7vG19%2FiL8t5AW4egtbkm9I6WzOJ%2Bi36klBUDjVzO59nha%2Fa6o0qf6Q5Hb2kw1Z5w7xpzaTjiGirWd8FC5kzFj%2FE4yLum6gtlqm5f&X-Amz-Signature=bdd8e15ee911ff44dbb528dde6366e00273a33857babd94d77fbc1ae8852469d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIHUP7D%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVk8M1UvneOz4uB2l5gAvaxL5LL2yzUIOCnJi9ALwJ9AiEAvmfwqizcIVwTEDoorjpHMssR9OIZoFniNLGn2H7rff4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyFHmgAT6OpI3PMRircA%2BmsnlBYSSBoApQZ32UxDwyIdVl44zhykkkwp136EEmAfCxHrbrkvNFIBdYc7hGodqmvPoQTsOrqDFhyagmxKCpKRrC%2FdbAzj99HsGRMc2ttmGrJJwieIbBvvK4Ej1JeShWh%2FM2gWj4IhJPx7PkJfO%2FU89CSxes1I7EuRrIf6XUz4osaJKkjRhZ4rHSmPoouP99rQ8trcH74MOxC5Ah6ozBVx2OoEXYfpXJIBxqq1ox4mRTDv2KUWfDbxs9HYiFGiDHQnR6Mt0mh%2BOFeNGpu0TIs5KfYEXkVmgBCjsyt0R0sdIaY9pWM81BpDtGl0LRG6PaglZcnbopV05mp3zThbNV6Q07CicX7FaRmxEmt99fLF7kagr7zBJByn%2FTMhhP7yEG4G6e1IbFOmAa%2F33GTTteX1L1E7hMVIRIuGh38Zc9AximnVXFbsDYxW2BNGGWufQnpAPSb5n2riG8h%2BtO5dwQI0IwIUQD%2FwLL7yVIiNJzOF33S%2B%2BXWuPdwYaqJDLimzHSirnZRsI0b9vA8ibBatljKuzDQ0WFr0mpLiP3RnZyNMC93fpW4DaItnls6YhLPN0VrOeQQojbIiCWNXvgJXHFbzljXkFaG%2F0KTvrE7q9nKm%2FoQytKo3K7hvpP%2BMPj90skGOqUBDg9jfa76fKOh%2FGRiNREOa3AU37M%2FZfHvATkfFFwwfdw2c5TUm0k7L%2BaO6pWZ6r14zPruERM5eQWPOi2CWl9ppIV35griANq2ZPb5j8zFi9i10mDHmN%2BsKzvt7vG19%2FiL8t5AW4egtbkm9I6WzOJ%2Bi36klBUDjVzO59nha%2Fa6o0qf6Q5Hb2kw1Z5w7xpzaTjiGirWd8FC5kzFj%2FE4yLum6gtlqm5f&X-Amz-Signature=f7f2e479f2a9c31ddb2f3cae3e12378923ca1f8b93316e151a156aa7c69a2f39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVIHUP7D%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVk8M1UvneOz4uB2l5gAvaxL5LL2yzUIOCnJi9ALwJ9AiEAvmfwqizcIVwTEDoorjpHMssR9OIZoFniNLGn2H7rff4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyFHmgAT6OpI3PMRircA%2BmsnlBYSSBoApQZ32UxDwyIdVl44zhykkkwp136EEmAfCxHrbrkvNFIBdYc7hGodqmvPoQTsOrqDFhyagmxKCpKRrC%2FdbAzj99HsGRMc2ttmGrJJwieIbBvvK4Ej1JeShWh%2FM2gWj4IhJPx7PkJfO%2FU89CSxes1I7EuRrIf6XUz4osaJKkjRhZ4rHSmPoouP99rQ8trcH74MOxC5Ah6ozBVx2OoEXYfpXJIBxqq1ox4mRTDv2KUWfDbxs9HYiFGiDHQnR6Mt0mh%2BOFeNGpu0TIs5KfYEXkVmgBCjsyt0R0sdIaY9pWM81BpDtGl0LRG6PaglZcnbopV05mp3zThbNV6Q07CicX7FaRmxEmt99fLF7kagr7zBJByn%2FTMhhP7yEG4G6e1IbFOmAa%2F33GTTteX1L1E7hMVIRIuGh38Zc9AximnVXFbsDYxW2BNGGWufQnpAPSb5n2riG8h%2BtO5dwQI0IwIUQD%2FwLL7yVIiNJzOF33S%2B%2BXWuPdwYaqJDLimzHSirnZRsI0b9vA8ibBatljKuzDQ0WFr0mpLiP3RnZyNMC93fpW4DaItnls6YhLPN0VrOeQQojbIiCWNXvgJXHFbzljXkFaG%2F0KTvrE7q9nKm%2FoQytKo3K7hvpP%2BMPj90skGOqUBDg9jfa76fKOh%2FGRiNREOa3AU37M%2FZfHvATkfFFwwfdw2c5TUm0k7L%2BaO6pWZ6r14zPruERM5eQWPOi2CWl9ppIV35griANq2ZPb5j8zFi9i10mDHmN%2BsKzvt7vG19%2FiL8t5AW4egtbkm9I6WzOJ%2Bi36klBUDjVzO59nha%2Fa6o0qf6Q5Hb2kw1Z5w7xpzaTjiGirWd8FC5kzFj%2FE4yLum6gtlqm5f&X-Amz-Signature=dd86ebf4a4f775414ab25fab3bf2e43035ace3a1a460cf3acb0e90bc1623bdc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

