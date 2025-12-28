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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDOTGNX%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4qKTLyxtmjCF3C%2FPxjRcqnIA%2B5XDW%2BynpqJ6XGR04fwIhAJ6yYkciWApOw8x0TKUQE6GG9lorqVbTVd1Is0ODpuzYKv8DCHkQABoMNjM3NDIzMTgzODA1Igz8GgdNuFRqLIgrfFMq3APPnK%2FgHtybLUeSCd4bW%2F5Cl2QCsdABxt1ZMl2Zsr%2Benbu4SGcn9nvPb%2BAqHnNnw3r8WksmtLJ7xUdnQellb1y7wa9B3ige6BIrfn3dE%2B%2BB1M%2BYHPDqDluMGdCx2Q%2FHAXlzvUwsGhE1%2FPM3MX5cxwROldei6jYP1RBKAJla0ArgJ1099czTJ%2BaWDu37BoL1oVFok33YwBs9zTYcpWbQgtpzOyKKDvB4aSQxSuMvcOs91fxRoOViOpIXYVTaTtAIZb%2Fq7q6lpsHOAcaDHBTTZl3cj1Ot%2BSBnMqFvNspM5N8NuPYk9M7%2BMqBZpNjDCBh1sun74XHBAGY2A2aSOYUq0EDC%2FC3IqwCfD44wjLlDGceQvaYHMRkgONbY6Xa8fwCvx%2BT12mLR3Z0fHaS%2BVuIjtTqkL5ph7ylTjyzQi6Zhgz05wU9qjHq10w8pJDjJQnuLaeHLZu1Iyr0vTWaJPNIHg8t%2FiEROf6CuLXPWhMlpZgDgVr8zEEVY1e955fI7jeIZLOGZTmD%2FbrSz2kIlacCmwVc9CPvLvPG4K0Gmd93XpDc%2BxQWLV%2Bcw97Pl20kSzptybsQFMglhcAhaHqBiCUsgfCiUo8v4%2FZjvNwytVidbYBXPfwS9NxIbvUVl2VZTGDD%2F3cHKBjqkAb6%2FPg6X%2FZhoVwNVN8AIUWQFzpmh6Urn8cr4PlaY8wOYZenWfY0tIhcKNLFjN2wOXIjLH0ex0Kh5lFWtb6kpKbbZopOqkNLE%2FDt2ofwwpv9WWiLRSA2mBCt%2Fh4q2R3pC%2BaL7cJRJB2u4y4sbSY15l%2BiWm%2F1k29RBmwBMYsRtWdw6tOclmjcxP%2BYo0xJh%2FGfmvVXQOFahtyge%2FVsw5R32zNELO1Nf&X-Amz-Signature=d9b5f2d7b1a0c2310bb29156d73eec370709f5556dbb3c3272159166980c2916&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDOTGNX%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4qKTLyxtmjCF3C%2FPxjRcqnIA%2B5XDW%2BynpqJ6XGR04fwIhAJ6yYkciWApOw8x0TKUQE6GG9lorqVbTVd1Is0ODpuzYKv8DCHkQABoMNjM3NDIzMTgzODA1Igz8GgdNuFRqLIgrfFMq3APPnK%2FgHtybLUeSCd4bW%2F5Cl2QCsdABxt1ZMl2Zsr%2Benbu4SGcn9nvPb%2BAqHnNnw3r8WksmtLJ7xUdnQellb1y7wa9B3ige6BIrfn3dE%2B%2BB1M%2BYHPDqDluMGdCx2Q%2FHAXlzvUwsGhE1%2FPM3MX5cxwROldei6jYP1RBKAJla0ArgJ1099czTJ%2BaWDu37BoL1oVFok33YwBs9zTYcpWbQgtpzOyKKDvB4aSQxSuMvcOs91fxRoOViOpIXYVTaTtAIZb%2Fq7q6lpsHOAcaDHBTTZl3cj1Ot%2BSBnMqFvNspM5N8NuPYk9M7%2BMqBZpNjDCBh1sun74XHBAGY2A2aSOYUq0EDC%2FC3IqwCfD44wjLlDGceQvaYHMRkgONbY6Xa8fwCvx%2BT12mLR3Z0fHaS%2BVuIjtTqkL5ph7ylTjyzQi6Zhgz05wU9qjHq10w8pJDjJQnuLaeHLZu1Iyr0vTWaJPNIHg8t%2FiEROf6CuLXPWhMlpZgDgVr8zEEVY1e955fI7jeIZLOGZTmD%2FbrSz2kIlacCmwVc9CPvLvPG4K0Gmd93XpDc%2BxQWLV%2Bcw97Pl20kSzptybsQFMglhcAhaHqBiCUsgfCiUo8v4%2FZjvNwytVidbYBXPfwS9NxIbvUVl2VZTGDD%2F3cHKBjqkAb6%2FPg6X%2FZhoVwNVN8AIUWQFzpmh6Urn8cr4PlaY8wOYZenWfY0tIhcKNLFjN2wOXIjLH0ex0Kh5lFWtb6kpKbbZopOqkNLE%2FDt2ofwwpv9WWiLRSA2mBCt%2Fh4q2R3pC%2BaL7cJRJB2u4y4sbSY15l%2BiWm%2F1k29RBmwBMYsRtWdw6tOclmjcxP%2BYo0xJh%2FGfmvVXQOFahtyge%2FVsw5R32zNELO1Nf&X-Amz-Signature=0b8510d1c9bab66cc9b047511065baea7b543521a31bbff0505ccab7c1917283&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDOTGNX%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4qKTLyxtmjCF3C%2FPxjRcqnIA%2B5XDW%2BynpqJ6XGR04fwIhAJ6yYkciWApOw8x0TKUQE6GG9lorqVbTVd1Is0ODpuzYKv8DCHkQABoMNjM3NDIzMTgzODA1Igz8GgdNuFRqLIgrfFMq3APPnK%2FgHtybLUeSCd4bW%2F5Cl2QCsdABxt1ZMl2Zsr%2Benbu4SGcn9nvPb%2BAqHnNnw3r8WksmtLJ7xUdnQellb1y7wa9B3ige6BIrfn3dE%2B%2BB1M%2BYHPDqDluMGdCx2Q%2FHAXlzvUwsGhE1%2FPM3MX5cxwROldei6jYP1RBKAJla0ArgJ1099czTJ%2BaWDu37BoL1oVFok33YwBs9zTYcpWbQgtpzOyKKDvB4aSQxSuMvcOs91fxRoOViOpIXYVTaTtAIZb%2Fq7q6lpsHOAcaDHBTTZl3cj1Ot%2BSBnMqFvNspM5N8NuPYk9M7%2BMqBZpNjDCBh1sun74XHBAGY2A2aSOYUq0EDC%2FC3IqwCfD44wjLlDGceQvaYHMRkgONbY6Xa8fwCvx%2BT12mLR3Z0fHaS%2BVuIjtTqkL5ph7ylTjyzQi6Zhgz05wU9qjHq10w8pJDjJQnuLaeHLZu1Iyr0vTWaJPNIHg8t%2FiEROf6CuLXPWhMlpZgDgVr8zEEVY1e955fI7jeIZLOGZTmD%2FbrSz2kIlacCmwVc9CPvLvPG4K0Gmd93XpDc%2BxQWLV%2Bcw97Pl20kSzptybsQFMglhcAhaHqBiCUsgfCiUo8v4%2FZjvNwytVidbYBXPfwS9NxIbvUVl2VZTGDD%2F3cHKBjqkAb6%2FPg6X%2FZhoVwNVN8AIUWQFzpmh6Urn8cr4PlaY8wOYZenWfY0tIhcKNLFjN2wOXIjLH0ex0Kh5lFWtb6kpKbbZopOqkNLE%2FDt2ofwwpv9WWiLRSA2mBCt%2Fh4q2R3pC%2BaL7cJRJB2u4y4sbSY15l%2BiWm%2F1k29RBmwBMYsRtWdw6tOclmjcxP%2BYo0xJh%2FGfmvVXQOFahtyge%2FVsw5R32zNELO1Nf&X-Amz-Signature=60eddc4363204fe1d3b31479c97249b0b752d54417e32280147a3911bc8fd1c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDOTGNX%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4qKTLyxtmjCF3C%2FPxjRcqnIA%2B5XDW%2BynpqJ6XGR04fwIhAJ6yYkciWApOw8x0TKUQE6GG9lorqVbTVd1Is0ODpuzYKv8DCHkQABoMNjM3NDIzMTgzODA1Igz8GgdNuFRqLIgrfFMq3APPnK%2FgHtybLUeSCd4bW%2F5Cl2QCsdABxt1ZMl2Zsr%2Benbu4SGcn9nvPb%2BAqHnNnw3r8WksmtLJ7xUdnQellb1y7wa9B3ige6BIrfn3dE%2B%2BB1M%2BYHPDqDluMGdCx2Q%2FHAXlzvUwsGhE1%2FPM3MX5cxwROldei6jYP1RBKAJla0ArgJ1099czTJ%2BaWDu37BoL1oVFok33YwBs9zTYcpWbQgtpzOyKKDvB4aSQxSuMvcOs91fxRoOViOpIXYVTaTtAIZb%2Fq7q6lpsHOAcaDHBTTZl3cj1Ot%2BSBnMqFvNspM5N8NuPYk9M7%2BMqBZpNjDCBh1sun74XHBAGY2A2aSOYUq0EDC%2FC3IqwCfD44wjLlDGceQvaYHMRkgONbY6Xa8fwCvx%2BT12mLR3Z0fHaS%2BVuIjtTqkL5ph7ylTjyzQi6Zhgz05wU9qjHq10w8pJDjJQnuLaeHLZu1Iyr0vTWaJPNIHg8t%2FiEROf6CuLXPWhMlpZgDgVr8zEEVY1e955fI7jeIZLOGZTmD%2FbrSz2kIlacCmwVc9CPvLvPG4K0Gmd93XpDc%2BxQWLV%2Bcw97Pl20kSzptybsQFMglhcAhaHqBiCUsgfCiUo8v4%2FZjvNwytVidbYBXPfwS9NxIbvUVl2VZTGDD%2F3cHKBjqkAb6%2FPg6X%2FZhoVwNVN8AIUWQFzpmh6Urn8cr4PlaY8wOYZenWfY0tIhcKNLFjN2wOXIjLH0ex0Kh5lFWtb6kpKbbZopOqkNLE%2FDt2ofwwpv9WWiLRSA2mBCt%2Fh4q2R3pC%2BaL7cJRJB2u4y4sbSY15l%2BiWm%2F1k29RBmwBMYsRtWdw6tOclmjcxP%2BYo0xJh%2FGfmvVXQOFahtyge%2FVsw5R32zNELO1Nf&X-Amz-Signature=32c71d22aaac9fd9ae813f80a491cc108806d7dc0d3bd5a4dead2bda65c3eb89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDOTGNX%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4qKTLyxtmjCF3C%2FPxjRcqnIA%2B5XDW%2BynpqJ6XGR04fwIhAJ6yYkciWApOw8x0TKUQE6GG9lorqVbTVd1Is0ODpuzYKv8DCHkQABoMNjM3NDIzMTgzODA1Igz8GgdNuFRqLIgrfFMq3APPnK%2FgHtybLUeSCd4bW%2F5Cl2QCsdABxt1ZMl2Zsr%2Benbu4SGcn9nvPb%2BAqHnNnw3r8WksmtLJ7xUdnQellb1y7wa9B3ige6BIrfn3dE%2B%2BB1M%2BYHPDqDluMGdCx2Q%2FHAXlzvUwsGhE1%2FPM3MX5cxwROldei6jYP1RBKAJla0ArgJ1099czTJ%2BaWDu37BoL1oVFok33YwBs9zTYcpWbQgtpzOyKKDvB4aSQxSuMvcOs91fxRoOViOpIXYVTaTtAIZb%2Fq7q6lpsHOAcaDHBTTZl3cj1Ot%2BSBnMqFvNspM5N8NuPYk9M7%2BMqBZpNjDCBh1sun74XHBAGY2A2aSOYUq0EDC%2FC3IqwCfD44wjLlDGceQvaYHMRkgONbY6Xa8fwCvx%2BT12mLR3Z0fHaS%2BVuIjtTqkL5ph7ylTjyzQi6Zhgz05wU9qjHq10w8pJDjJQnuLaeHLZu1Iyr0vTWaJPNIHg8t%2FiEROf6CuLXPWhMlpZgDgVr8zEEVY1e955fI7jeIZLOGZTmD%2FbrSz2kIlacCmwVc9CPvLvPG4K0Gmd93XpDc%2BxQWLV%2Bcw97Pl20kSzptybsQFMglhcAhaHqBiCUsgfCiUo8v4%2FZjvNwytVidbYBXPfwS9NxIbvUVl2VZTGDD%2F3cHKBjqkAb6%2FPg6X%2FZhoVwNVN8AIUWQFzpmh6Urn8cr4PlaY8wOYZenWfY0tIhcKNLFjN2wOXIjLH0ex0Kh5lFWtb6kpKbbZopOqkNLE%2FDt2ofwwpv9WWiLRSA2mBCt%2Fh4q2R3pC%2BaL7cJRJB2u4y4sbSY15l%2BiWm%2F1k29RBmwBMYsRtWdw6tOclmjcxP%2BYo0xJh%2FGfmvVXQOFahtyge%2FVsw5R32zNELO1Nf&X-Amz-Signature=3a87094b053b09ae310f8418eb2d78161852c882e4ebc7172f770d57ae79c8f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDOTGNX%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4qKTLyxtmjCF3C%2FPxjRcqnIA%2B5XDW%2BynpqJ6XGR04fwIhAJ6yYkciWApOw8x0TKUQE6GG9lorqVbTVd1Is0ODpuzYKv8DCHkQABoMNjM3NDIzMTgzODA1Igz8GgdNuFRqLIgrfFMq3APPnK%2FgHtybLUeSCd4bW%2F5Cl2QCsdABxt1ZMl2Zsr%2Benbu4SGcn9nvPb%2BAqHnNnw3r8WksmtLJ7xUdnQellb1y7wa9B3ige6BIrfn3dE%2B%2BB1M%2BYHPDqDluMGdCx2Q%2FHAXlzvUwsGhE1%2FPM3MX5cxwROldei6jYP1RBKAJla0ArgJ1099czTJ%2BaWDu37BoL1oVFok33YwBs9zTYcpWbQgtpzOyKKDvB4aSQxSuMvcOs91fxRoOViOpIXYVTaTtAIZb%2Fq7q6lpsHOAcaDHBTTZl3cj1Ot%2BSBnMqFvNspM5N8NuPYk9M7%2BMqBZpNjDCBh1sun74XHBAGY2A2aSOYUq0EDC%2FC3IqwCfD44wjLlDGceQvaYHMRkgONbY6Xa8fwCvx%2BT12mLR3Z0fHaS%2BVuIjtTqkL5ph7ylTjyzQi6Zhgz05wU9qjHq10w8pJDjJQnuLaeHLZu1Iyr0vTWaJPNIHg8t%2FiEROf6CuLXPWhMlpZgDgVr8zEEVY1e955fI7jeIZLOGZTmD%2FbrSz2kIlacCmwVc9CPvLvPG4K0Gmd93XpDc%2BxQWLV%2Bcw97Pl20kSzptybsQFMglhcAhaHqBiCUsgfCiUo8v4%2FZjvNwytVidbYBXPfwS9NxIbvUVl2VZTGDD%2F3cHKBjqkAb6%2FPg6X%2FZhoVwNVN8AIUWQFzpmh6Urn8cr4PlaY8wOYZenWfY0tIhcKNLFjN2wOXIjLH0ex0Kh5lFWtb6kpKbbZopOqkNLE%2FDt2ofwwpv9WWiLRSA2mBCt%2Fh4q2R3pC%2BaL7cJRJB2u4y4sbSY15l%2BiWm%2F1k29RBmwBMYsRtWdw6tOclmjcxP%2BYo0xJh%2FGfmvVXQOFahtyge%2FVsw5R32zNELO1Nf&X-Amz-Signature=7762b17ae8267753164a17de628613f847fa5b1082ec469f06d0f1d8adfa44de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDOTGNX%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4qKTLyxtmjCF3C%2FPxjRcqnIA%2B5XDW%2BynpqJ6XGR04fwIhAJ6yYkciWApOw8x0TKUQE6GG9lorqVbTVd1Is0ODpuzYKv8DCHkQABoMNjM3NDIzMTgzODA1Igz8GgdNuFRqLIgrfFMq3APPnK%2FgHtybLUeSCd4bW%2F5Cl2QCsdABxt1ZMl2Zsr%2Benbu4SGcn9nvPb%2BAqHnNnw3r8WksmtLJ7xUdnQellb1y7wa9B3ige6BIrfn3dE%2B%2BB1M%2BYHPDqDluMGdCx2Q%2FHAXlzvUwsGhE1%2FPM3MX5cxwROldei6jYP1RBKAJla0ArgJ1099czTJ%2BaWDu37BoL1oVFok33YwBs9zTYcpWbQgtpzOyKKDvB4aSQxSuMvcOs91fxRoOViOpIXYVTaTtAIZb%2Fq7q6lpsHOAcaDHBTTZl3cj1Ot%2BSBnMqFvNspM5N8NuPYk9M7%2BMqBZpNjDCBh1sun74XHBAGY2A2aSOYUq0EDC%2FC3IqwCfD44wjLlDGceQvaYHMRkgONbY6Xa8fwCvx%2BT12mLR3Z0fHaS%2BVuIjtTqkL5ph7ylTjyzQi6Zhgz05wU9qjHq10w8pJDjJQnuLaeHLZu1Iyr0vTWaJPNIHg8t%2FiEROf6CuLXPWhMlpZgDgVr8zEEVY1e955fI7jeIZLOGZTmD%2FbrSz2kIlacCmwVc9CPvLvPG4K0Gmd93XpDc%2BxQWLV%2Bcw97Pl20kSzptybsQFMglhcAhaHqBiCUsgfCiUo8v4%2FZjvNwytVidbYBXPfwS9NxIbvUVl2VZTGDD%2F3cHKBjqkAb6%2FPg6X%2FZhoVwNVN8AIUWQFzpmh6Urn8cr4PlaY8wOYZenWfY0tIhcKNLFjN2wOXIjLH0ex0Kh5lFWtb6kpKbbZopOqkNLE%2FDt2ofwwpv9WWiLRSA2mBCt%2Fh4q2R3pC%2BaL7cJRJB2u4y4sbSY15l%2BiWm%2F1k29RBmwBMYsRtWdw6tOclmjcxP%2BYo0xJh%2FGfmvVXQOFahtyge%2FVsw5R32zNELO1Nf&X-Amz-Signature=23d2f036a11f564090bdf0d36f1cf6c547282e39d169d1ae4f0ba354c3849044&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDOTGNX%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4qKTLyxtmjCF3C%2FPxjRcqnIA%2B5XDW%2BynpqJ6XGR04fwIhAJ6yYkciWApOw8x0TKUQE6GG9lorqVbTVd1Is0ODpuzYKv8DCHkQABoMNjM3NDIzMTgzODA1Igz8GgdNuFRqLIgrfFMq3APPnK%2FgHtybLUeSCd4bW%2F5Cl2QCsdABxt1ZMl2Zsr%2Benbu4SGcn9nvPb%2BAqHnNnw3r8WksmtLJ7xUdnQellb1y7wa9B3ige6BIrfn3dE%2B%2BB1M%2BYHPDqDluMGdCx2Q%2FHAXlzvUwsGhE1%2FPM3MX5cxwROldei6jYP1RBKAJla0ArgJ1099czTJ%2BaWDu37BoL1oVFok33YwBs9zTYcpWbQgtpzOyKKDvB4aSQxSuMvcOs91fxRoOViOpIXYVTaTtAIZb%2Fq7q6lpsHOAcaDHBTTZl3cj1Ot%2BSBnMqFvNspM5N8NuPYk9M7%2BMqBZpNjDCBh1sun74XHBAGY2A2aSOYUq0EDC%2FC3IqwCfD44wjLlDGceQvaYHMRkgONbY6Xa8fwCvx%2BT12mLR3Z0fHaS%2BVuIjtTqkL5ph7ylTjyzQi6Zhgz05wU9qjHq10w8pJDjJQnuLaeHLZu1Iyr0vTWaJPNIHg8t%2FiEROf6CuLXPWhMlpZgDgVr8zEEVY1e955fI7jeIZLOGZTmD%2FbrSz2kIlacCmwVc9CPvLvPG4K0Gmd93XpDc%2BxQWLV%2Bcw97Pl20kSzptybsQFMglhcAhaHqBiCUsgfCiUo8v4%2FZjvNwytVidbYBXPfwS9NxIbvUVl2VZTGDD%2F3cHKBjqkAb6%2FPg6X%2FZhoVwNVN8AIUWQFzpmh6Urn8cr4PlaY8wOYZenWfY0tIhcKNLFjN2wOXIjLH0ex0Kh5lFWtb6kpKbbZopOqkNLE%2FDt2ofwwpv9WWiLRSA2mBCt%2Fh4q2R3pC%2BaL7cJRJB2u4y4sbSY15l%2BiWm%2F1k29RBmwBMYsRtWdw6tOclmjcxP%2BYo0xJh%2FGfmvVXQOFahtyge%2FVsw5R32zNELO1Nf&X-Amz-Signature=cf6dcc9eea7b37ace5d9064ce066e0ef4fefef793c854a382cb38ee93c22adf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDOTGNX%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4qKTLyxtmjCF3C%2FPxjRcqnIA%2B5XDW%2BynpqJ6XGR04fwIhAJ6yYkciWApOw8x0TKUQE6GG9lorqVbTVd1Is0ODpuzYKv8DCHkQABoMNjM3NDIzMTgzODA1Igz8GgdNuFRqLIgrfFMq3APPnK%2FgHtybLUeSCd4bW%2F5Cl2QCsdABxt1ZMl2Zsr%2Benbu4SGcn9nvPb%2BAqHnNnw3r8WksmtLJ7xUdnQellb1y7wa9B3ige6BIrfn3dE%2B%2BB1M%2BYHPDqDluMGdCx2Q%2FHAXlzvUwsGhE1%2FPM3MX5cxwROldei6jYP1RBKAJla0ArgJ1099czTJ%2BaWDu37BoL1oVFok33YwBs9zTYcpWbQgtpzOyKKDvB4aSQxSuMvcOs91fxRoOViOpIXYVTaTtAIZb%2Fq7q6lpsHOAcaDHBTTZl3cj1Ot%2BSBnMqFvNspM5N8NuPYk9M7%2BMqBZpNjDCBh1sun74XHBAGY2A2aSOYUq0EDC%2FC3IqwCfD44wjLlDGceQvaYHMRkgONbY6Xa8fwCvx%2BT12mLR3Z0fHaS%2BVuIjtTqkL5ph7ylTjyzQi6Zhgz05wU9qjHq10w8pJDjJQnuLaeHLZu1Iyr0vTWaJPNIHg8t%2FiEROf6CuLXPWhMlpZgDgVr8zEEVY1e955fI7jeIZLOGZTmD%2FbrSz2kIlacCmwVc9CPvLvPG4K0Gmd93XpDc%2BxQWLV%2Bcw97Pl20kSzptybsQFMglhcAhaHqBiCUsgfCiUo8v4%2FZjvNwytVidbYBXPfwS9NxIbvUVl2VZTGDD%2F3cHKBjqkAb6%2FPg6X%2FZhoVwNVN8AIUWQFzpmh6Urn8cr4PlaY8wOYZenWfY0tIhcKNLFjN2wOXIjLH0ex0Kh5lFWtb6kpKbbZopOqkNLE%2FDt2ofwwpv9WWiLRSA2mBCt%2Fh4q2R3pC%2BaL7cJRJB2u4y4sbSY15l%2BiWm%2F1k29RBmwBMYsRtWdw6tOclmjcxP%2BYo0xJh%2FGfmvVXQOFahtyge%2FVsw5R32zNELO1Nf&X-Amz-Signature=b3ec107cb9211f294d975901a309db53e46254f0262ef5735252625086e78e53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTDOTGNX%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4qKTLyxtmjCF3C%2FPxjRcqnIA%2B5XDW%2BynpqJ6XGR04fwIhAJ6yYkciWApOw8x0TKUQE6GG9lorqVbTVd1Is0ODpuzYKv8DCHkQABoMNjM3NDIzMTgzODA1Igz8GgdNuFRqLIgrfFMq3APPnK%2FgHtybLUeSCd4bW%2F5Cl2QCsdABxt1ZMl2Zsr%2Benbu4SGcn9nvPb%2BAqHnNnw3r8WksmtLJ7xUdnQellb1y7wa9B3ige6BIrfn3dE%2B%2BB1M%2BYHPDqDluMGdCx2Q%2FHAXlzvUwsGhE1%2FPM3MX5cxwROldei6jYP1RBKAJla0ArgJ1099czTJ%2BaWDu37BoL1oVFok33YwBs9zTYcpWbQgtpzOyKKDvB4aSQxSuMvcOs91fxRoOViOpIXYVTaTtAIZb%2Fq7q6lpsHOAcaDHBTTZl3cj1Ot%2BSBnMqFvNspM5N8NuPYk9M7%2BMqBZpNjDCBh1sun74XHBAGY2A2aSOYUq0EDC%2FC3IqwCfD44wjLlDGceQvaYHMRkgONbY6Xa8fwCvx%2BT12mLR3Z0fHaS%2BVuIjtTqkL5ph7ylTjyzQi6Zhgz05wU9qjHq10w8pJDjJQnuLaeHLZu1Iyr0vTWaJPNIHg8t%2FiEROf6CuLXPWhMlpZgDgVr8zEEVY1e955fI7jeIZLOGZTmD%2FbrSz2kIlacCmwVc9CPvLvPG4K0Gmd93XpDc%2BxQWLV%2Bcw97Pl20kSzptybsQFMglhcAhaHqBiCUsgfCiUo8v4%2FZjvNwytVidbYBXPfwS9NxIbvUVl2VZTGDD%2F3cHKBjqkAb6%2FPg6X%2FZhoVwNVN8AIUWQFzpmh6Urn8cr4PlaY8wOYZenWfY0tIhcKNLFjN2wOXIjLH0ex0Kh5lFWtb6kpKbbZopOqkNLE%2FDt2ofwwpv9WWiLRSA2mBCt%2Fh4q2R3pC%2BaL7cJRJB2u4y4sbSY15l%2BiWm%2F1k29RBmwBMYsRtWdw6tOclmjcxP%2BYo0xJh%2FGfmvVXQOFahtyge%2FVsw5R32zNELO1Nf&X-Amz-Signature=6b6dfabab4cf280c82658a6b0ee3059a2a20cc5ac317bb170fd8ee5ed972cfec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

