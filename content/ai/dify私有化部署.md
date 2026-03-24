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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTATYTHV%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDToBAMgpjR61ANUO2XrjNhZo0al68SsseNANvSeZAeqQIgO%2FRZL3mHGDAlwrOl0bksJ6CnCQa%2BBum1FCWbb3hy9y0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKDUvb4vm3LW40%2FFCrcA2uetDnRW3aWdqGwFTcIvpESotutffqMXIFCZRKdgFvTNuZa8xBaMSr3fNlcMKsba4Ckm%2F6ObIu3siV%2B5VDT6ldVUfbAOKvVCsFuuzc%2Fdy8UasaUMEicocU4kg3cCfBv2k06N3fsdJuqEnVZN82bw1dWIOHn9vvHvPlLxrV5QTpnoV6JSGimmQfoGgI3oh%2BRVhq3hOmJwA4Q1oqJp89ryUHsBKqYfhRxg4Jv8gt2qlsqCLA%2FolkQPTOb16iy5NC16hPljEY%2BoGti3boWCTtBpLXnyu6YlI0dQCbe2Qn24UI5HRNF55nuBpnTZFnbHmkv74EHbzg8FOwLUtqnSwMcwd7Xue03%2FHnnBUMsvQZNXlgPgCXkONfKwz6p0cs3vwUfSmkYVQMaoWjAjIH3LouIhUMf5gCb2geVcvSoafIhcilpHzCHlXjPVZ74SYFLJgqSMBGZ1vKhgN3Nw%2F2hJqJE1b8whBuO%2F0emHFsNPG7YCOpqox2NGxbaukQjmm4E5xnYTZqdjY%2Bu%2BO7%2Bmq98j9GuWgM7SnUyOsb%2BwD6z0WUQ7rULULkHJDwP%2BwlmdLzm68uHobkGC5ID3GHj7U08ud%2FudPKVemgTeY2UxWn5s58zPejZ%2F2mAjiZDiB2uOmRhMOD0h84GOqUBuOcFUvrrKYK9ekdkw0frjRtU4vbVyCiGhodrGmuC%2FJykNacOeNi4Tcf7AtgA60nlCp3wWfxgXy%2BSZXoyuJsvuHd2MyFlVn1Ho7NTIKdTtu6GuMFo8uXrBfCf%2B6WyJQ5GoRNvVLWqa8KLgmfxTAGowop610Y%2BsPgxS7y%2FM91A8aHCrccPKm3gSLSW7gYpP%2BkPNJEMaGx7F1YwgcOm%2FQQm32cWzGdJ&X-Amz-Signature=23e4b196b4eaaa3705c1ae47faf073108393df5c1b2f04bcd00e02991701808c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTATYTHV%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDToBAMgpjR61ANUO2XrjNhZo0al68SsseNANvSeZAeqQIgO%2FRZL3mHGDAlwrOl0bksJ6CnCQa%2BBum1FCWbb3hy9y0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKDUvb4vm3LW40%2FFCrcA2uetDnRW3aWdqGwFTcIvpESotutffqMXIFCZRKdgFvTNuZa8xBaMSr3fNlcMKsba4Ckm%2F6ObIu3siV%2B5VDT6ldVUfbAOKvVCsFuuzc%2Fdy8UasaUMEicocU4kg3cCfBv2k06N3fsdJuqEnVZN82bw1dWIOHn9vvHvPlLxrV5QTpnoV6JSGimmQfoGgI3oh%2BRVhq3hOmJwA4Q1oqJp89ryUHsBKqYfhRxg4Jv8gt2qlsqCLA%2FolkQPTOb16iy5NC16hPljEY%2BoGti3boWCTtBpLXnyu6YlI0dQCbe2Qn24UI5HRNF55nuBpnTZFnbHmkv74EHbzg8FOwLUtqnSwMcwd7Xue03%2FHnnBUMsvQZNXlgPgCXkONfKwz6p0cs3vwUfSmkYVQMaoWjAjIH3LouIhUMf5gCb2geVcvSoafIhcilpHzCHlXjPVZ74SYFLJgqSMBGZ1vKhgN3Nw%2F2hJqJE1b8whBuO%2F0emHFsNPG7YCOpqox2NGxbaukQjmm4E5xnYTZqdjY%2Bu%2BO7%2Bmq98j9GuWgM7SnUyOsb%2BwD6z0WUQ7rULULkHJDwP%2BwlmdLzm68uHobkGC5ID3GHj7U08ud%2FudPKVemgTeY2UxWn5s58zPejZ%2F2mAjiZDiB2uOmRhMOD0h84GOqUBuOcFUvrrKYK9ekdkw0frjRtU4vbVyCiGhodrGmuC%2FJykNacOeNi4Tcf7AtgA60nlCp3wWfxgXy%2BSZXoyuJsvuHd2MyFlVn1Ho7NTIKdTtu6GuMFo8uXrBfCf%2B6WyJQ5GoRNvVLWqa8KLgmfxTAGowop610Y%2BsPgxS7y%2FM91A8aHCrccPKm3gSLSW7gYpP%2BkPNJEMaGx7F1YwgcOm%2FQQm32cWzGdJ&X-Amz-Signature=248ea77b976d630c29c896bbe564fd54284eb5993b4421c637c59b22896f5547&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTATYTHV%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDToBAMgpjR61ANUO2XrjNhZo0al68SsseNANvSeZAeqQIgO%2FRZL3mHGDAlwrOl0bksJ6CnCQa%2BBum1FCWbb3hy9y0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKDUvb4vm3LW40%2FFCrcA2uetDnRW3aWdqGwFTcIvpESotutffqMXIFCZRKdgFvTNuZa8xBaMSr3fNlcMKsba4Ckm%2F6ObIu3siV%2B5VDT6ldVUfbAOKvVCsFuuzc%2Fdy8UasaUMEicocU4kg3cCfBv2k06N3fsdJuqEnVZN82bw1dWIOHn9vvHvPlLxrV5QTpnoV6JSGimmQfoGgI3oh%2BRVhq3hOmJwA4Q1oqJp89ryUHsBKqYfhRxg4Jv8gt2qlsqCLA%2FolkQPTOb16iy5NC16hPljEY%2BoGti3boWCTtBpLXnyu6YlI0dQCbe2Qn24UI5HRNF55nuBpnTZFnbHmkv74EHbzg8FOwLUtqnSwMcwd7Xue03%2FHnnBUMsvQZNXlgPgCXkONfKwz6p0cs3vwUfSmkYVQMaoWjAjIH3LouIhUMf5gCb2geVcvSoafIhcilpHzCHlXjPVZ74SYFLJgqSMBGZ1vKhgN3Nw%2F2hJqJE1b8whBuO%2F0emHFsNPG7YCOpqox2NGxbaukQjmm4E5xnYTZqdjY%2Bu%2BO7%2Bmq98j9GuWgM7SnUyOsb%2BwD6z0WUQ7rULULkHJDwP%2BwlmdLzm68uHobkGC5ID3GHj7U08ud%2FudPKVemgTeY2UxWn5s58zPejZ%2F2mAjiZDiB2uOmRhMOD0h84GOqUBuOcFUvrrKYK9ekdkw0frjRtU4vbVyCiGhodrGmuC%2FJykNacOeNi4Tcf7AtgA60nlCp3wWfxgXy%2BSZXoyuJsvuHd2MyFlVn1Ho7NTIKdTtu6GuMFo8uXrBfCf%2B6WyJQ5GoRNvVLWqa8KLgmfxTAGowop610Y%2BsPgxS7y%2FM91A8aHCrccPKm3gSLSW7gYpP%2BkPNJEMaGx7F1YwgcOm%2FQQm32cWzGdJ&X-Amz-Signature=c557d355c9bfbe7653683e2223fa964ddae5ad8e4060fc4f6c9b4f6695a9c20c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTATYTHV%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDToBAMgpjR61ANUO2XrjNhZo0al68SsseNANvSeZAeqQIgO%2FRZL3mHGDAlwrOl0bksJ6CnCQa%2BBum1FCWbb3hy9y0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKDUvb4vm3LW40%2FFCrcA2uetDnRW3aWdqGwFTcIvpESotutffqMXIFCZRKdgFvTNuZa8xBaMSr3fNlcMKsba4Ckm%2F6ObIu3siV%2B5VDT6ldVUfbAOKvVCsFuuzc%2Fdy8UasaUMEicocU4kg3cCfBv2k06N3fsdJuqEnVZN82bw1dWIOHn9vvHvPlLxrV5QTpnoV6JSGimmQfoGgI3oh%2BRVhq3hOmJwA4Q1oqJp89ryUHsBKqYfhRxg4Jv8gt2qlsqCLA%2FolkQPTOb16iy5NC16hPljEY%2BoGti3boWCTtBpLXnyu6YlI0dQCbe2Qn24UI5HRNF55nuBpnTZFnbHmkv74EHbzg8FOwLUtqnSwMcwd7Xue03%2FHnnBUMsvQZNXlgPgCXkONfKwz6p0cs3vwUfSmkYVQMaoWjAjIH3LouIhUMf5gCb2geVcvSoafIhcilpHzCHlXjPVZ74SYFLJgqSMBGZ1vKhgN3Nw%2F2hJqJE1b8whBuO%2F0emHFsNPG7YCOpqox2NGxbaukQjmm4E5xnYTZqdjY%2Bu%2BO7%2Bmq98j9GuWgM7SnUyOsb%2BwD6z0WUQ7rULULkHJDwP%2BwlmdLzm68uHobkGC5ID3GHj7U08ud%2FudPKVemgTeY2UxWn5s58zPejZ%2F2mAjiZDiB2uOmRhMOD0h84GOqUBuOcFUvrrKYK9ekdkw0frjRtU4vbVyCiGhodrGmuC%2FJykNacOeNi4Tcf7AtgA60nlCp3wWfxgXy%2BSZXoyuJsvuHd2MyFlVn1Ho7NTIKdTtu6GuMFo8uXrBfCf%2B6WyJQ5GoRNvVLWqa8KLgmfxTAGowop610Y%2BsPgxS7y%2FM91A8aHCrccPKm3gSLSW7gYpP%2BkPNJEMaGx7F1YwgcOm%2FQQm32cWzGdJ&X-Amz-Signature=03edc939e4409b04c4fafbf436e0c24da3373ef1d2b2c16913e30eee2547fc2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTATYTHV%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDToBAMgpjR61ANUO2XrjNhZo0al68SsseNANvSeZAeqQIgO%2FRZL3mHGDAlwrOl0bksJ6CnCQa%2BBum1FCWbb3hy9y0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKDUvb4vm3LW40%2FFCrcA2uetDnRW3aWdqGwFTcIvpESotutffqMXIFCZRKdgFvTNuZa8xBaMSr3fNlcMKsba4Ckm%2F6ObIu3siV%2B5VDT6ldVUfbAOKvVCsFuuzc%2Fdy8UasaUMEicocU4kg3cCfBv2k06N3fsdJuqEnVZN82bw1dWIOHn9vvHvPlLxrV5QTpnoV6JSGimmQfoGgI3oh%2BRVhq3hOmJwA4Q1oqJp89ryUHsBKqYfhRxg4Jv8gt2qlsqCLA%2FolkQPTOb16iy5NC16hPljEY%2BoGti3boWCTtBpLXnyu6YlI0dQCbe2Qn24UI5HRNF55nuBpnTZFnbHmkv74EHbzg8FOwLUtqnSwMcwd7Xue03%2FHnnBUMsvQZNXlgPgCXkONfKwz6p0cs3vwUfSmkYVQMaoWjAjIH3LouIhUMf5gCb2geVcvSoafIhcilpHzCHlXjPVZ74SYFLJgqSMBGZ1vKhgN3Nw%2F2hJqJE1b8whBuO%2F0emHFsNPG7YCOpqox2NGxbaukQjmm4E5xnYTZqdjY%2Bu%2BO7%2Bmq98j9GuWgM7SnUyOsb%2BwD6z0WUQ7rULULkHJDwP%2BwlmdLzm68uHobkGC5ID3GHj7U08ud%2FudPKVemgTeY2UxWn5s58zPejZ%2F2mAjiZDiB2uOmRhMOD0h84GOqUBuOcFUvrrKYK9ekdkw0frjRtU4vbVyCiGhodrGmuC%2FJykNacOeNi4Tcf7AtgA60nlCp3wWfxgXy%2BSZXoyuJsvuHd2MyFlVn1Ho7NTIKdTtu6GuMFo8uXrBfCf%2B6WyJQ5GoRNvVLWqa8KLgmfxTAGowop610Y%2BsPgxS7y%2FM91A8aHCrccPKm3gSLSW7gYpP%2BkPNJEMaGx7F1YwgcOm%2FQQm32cWzGdJ&X-Amz-Signature=aef2cb04f24092d7a03b5ab9e76856d66091dd4a0e12ba1aaa60c41d0be96bb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTATYTHV%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDToBAMgpjR61ANUO2XrjNhZo0al68SsseNANvSeZAeqQIgO%2FRZL3mHGDAlwrOl0bksJ6CnCQa%2BBum1FCWbb3hy9y0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKDUvb4vm3LW40%2FFCrcA2uetDnRW3aWdqGwFTcIvpESotutffqMXIFCZRKdgFvTNuZa8xBaMSr3fNlcMKsba4Ckm%2F6ObIu3siV%2B5VDT6ldVUfbAOKvVCsFuuzc%2Fdy8UasaUMEicocU4kg3cCfBv2k06N3fsdJuqEnVZN82bw1dWIOHn9vvHvPlLxrV5QTpnoV6JSGimmQfoGgI3oh%2BRVhq3hOmJwA4Q1oqJp89ryUHsBKqYfhRxg4Jv8gt2qlsqCLA%2FolkQPTOb16iy5NC16hPljEY%2BoGti3boWCTtBpLXnyu6YlI0dQCbe2Qn24UI5HRNF55nuBpnTZFnbHmkv74EHbzg8FOwLUtqnSwMcwd7Xue03%2FHnnBUMsvQZNXlgPgCXkONfKwz6p0cs3vwUfSmkYVQMaoWjAjIH3LouIhUMf5gCb2geVcvSoafIhcilpHzCHlXjPVZ74SYFLJgqSMBGZ1vKhgN3Nw%2F2hJqJE1b8whBuO%2F0emHFsNPG7YCOpqox2NGxbaukQjmm4E5xnYTZqdjY%2Bu%2BO7%2Bmq98j9GuWgM7SnUyOsb%2BwD6z0WUQ7rULULkHJDwP%2BwlmdLzm68uHobkGC5ID3GHj7U08ud%2FudPKVemgTeY2UxWn5s58zPejZ%2F2mAjiZDiB2uOmRhMOD0h84GOqUBuOcFUvrrKYK9ekdkw0frjRtU4vbVyCiGhodrGmuC%2FJykNacOeNi4Tcf7AtgA60nlCp3wWfxgXy%2BSZXoyuJsvuHd2MyFlVn1Ho7NTIKdTtu6GuMFo8uXrBfCf%2B6WyJQ5GoRNvVLWqa8KLgmfxTAGowop610Y%2BsPgxS7y%2FM91A8aHCrccPKm3gSLSW7gYpP%2BkPNJEMaGx7F1YwgcOm%2FQQm32cWzGdJ&X-Amz-Signature=c256705364e37e730d8a557f7c26ffb8a913ef6a14c6d1b907bf4b224c0c6807&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTATYTHV%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDToBAMgpjR61ANUO2XrjNhZo0al68SsseNANvSeZAeqQIgO%2FRZL3mHGDAlwrOl0bksJ6CnCQa%2BBum1FCWbb3hy9y0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKDUvb4vm3LW40%2FFCrcA2uetDnRW3aWdqGwFTcIvpESotutffqMXIFCZRKdgFvTNuZa8xBaMSr3fNlcMKsba4Ckm%2F6ObIu3siV%2B5VDT6ldVUfbAOKvVCsFuuzc%2Fdy8UasaUMEicocU4kg3cCfBv2k06N3fsdJuqEnVZN82bw1dWIOHn9vvHvPlLxrV5QTpnoV6JSGimmQfoGgI3oh%2BRVhq3hOmJwA4Q1oqJp89ryUHsBKqYfhRxg4Jv8gt2qlsqCLA%2FolkQPTOb16iy5NC16hPljEY%2BoGti3boWCTtBpLXnyu6YlI0dQCbe2Qn24UI5HRNF55nuBpnTZFnbHmkv74EHbzg8FOwLUtqnSwMcwd7Xue03%2FHnnBUMsvQZNXlgPgCXkONfKwz6p0cs3vwUfSmkYVQMaoWjAjIH3LouIhUMf5gCb2geVcvSoafIhcilpHzCHlXjPVZ74SYFLJgqSMBGZ1vKhgN3Nw%2F2hJqJE1b8whBuO%2F0emHFsNPG7YCOpqox2NGxbaukQjmm4E5xnYTZqdjY%2Bu%2BO7%2Bmq98j9GuWgM7SnUyOsb%2BwD6z0WUQ7rULULkHJDwP%2BwlmdLzm68uHobkGC5ID3GHj7U08ud%2FudPKVemgTeY2UxWn5s58zPejZ%2F2mAjiZDiB2uOmRhMOD0h84GOqUBuOcFUvrrKYK9ekdkw0frjRtU4vbVyCiGhodrGmuC%2FJykNacOeNi4Tcf7AtgA60nlCp3wWfxgXy%2BSZXoyuJsvuHd2MyFlVn1Ho7NTIKdTtu6GuMFo8uXrBfCf%2B6WyJQ5GoRNvVLWqa8KLgmfxTAGowop610Y%2BsPgxS7y%2FM91A8aHCrccPKm3gSLSW7gYpP%2BkPNJEMaGx7F1YwgcOm%2FQQm32cWzGdJ&X-Amz-Signature=0556365a00d15243da0939d40e37101bae8a03e50043387232f351b649e8e04e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTATYTHV%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDToBAMgpjR61ANUO2XrjNhZo0al68SsseNANvSeZAeqQIgO%2FRZL3mHGDAlwrOl0bksJ6CnCQa%2BBum1FCWbb3hy9y0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKDUvb4vm3LW40%2FFCrcA2uetDnRW3aWdqGwFTcIvpESotutffqMXIFCZRKdgFvTNuZa8xBaMSr3fNlcMKsba4Ckm%2F6ObIu3siV%2B5VDT6ldVUfbAOKvVCsFuuzc%2Fdy8UasaUMEicocU4kg3cCfBv2k06N3fsdJuqEnVZN82bw1dWIOHn9vvHvPlLxrV5QTpnoV6JSGimmQfoGgI3oh%2BRVhq3hOmJwA4Q1oqJp89ryUHsBKqYfhRxg4Jv8gt2qlsqCLA%2FolkQPTOb16iy5NC16hPljEY%2BoGti3boWCTtBpLXnyu6YlI0dQCbe2Qn24UI5HRNF55nuBpnTZFnbHmkv74EHbzg8FOwLUtqnSwMcwd7Xue03%2FHnnBUMsvQZNXlgPgCXkONfKwz6p0cs3vwUfSmkYVQMaoWjAjIH3LouIhUMf5gCb2geVcvSoafIhcilpHzCHlXjPVZ74SYFLJgqSMBGZ1vKhgN3Nw%2F2hJqJE1b8whBuO%2F0emHFsNPG7YCOpqox2NGxbaukQjmm4E5xnYTZqdjY%2Bu%2BO7%2Bmq98j9GuWgM7SnUyOsb%2BwD6z0WUQ7rULULkHJDwP%2BwlmdLzm68uHobkGC5ID3GHj7U08ud%2FudPKVemgTeY2UxWn5s58zPejZ%2F2mAjiZDiB2uOmRhMOD0h84GOqUBuOcFUvrrKYK9ekdkw0frjRtU4vbVyCiGhodrGmuC%2FJykNacOeNi4Tcf7AtgA60nlCp3wWfxgXy%2BSZXoyuJsvuHd2MyFlVn1Ho7NTIKdTtu6GuMFo8uXrBfCf%2B6WyJQ5GoRNvVLWqa8KLgmfxTAGowop610Y%2BsPgxS7y%2FM91A8aHCrccPKm3gSLSW7gYpP%2BkPNJEMaGx7F1YwgcOm%2FQQm32cWzGdJ&X-Amz-Signature=10f95045945aa2272fc691eef5c9c20df9f8e19d868c579211a626cc54d0a586&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTATYTHV%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDToBAMgpjR61ANUO2XrjNhZo0al68SsseNANvSeZAeqQIgO%2FRZL3mHGDAlwrOl0bksJ6CnCQa%2BBum1FCWbb3hy9y0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKDUvb4vm3LW40%2FFCrcA2uetDnRW3aWdqGwFTcIvpESotutffqMXIFCZRKdgFvTNuZa8xBaMSr3fNlcMKsba4Ckm%2F6ObIu3siV%2B5VDT6ldVUfbAOKvVCsFuuzc%2Fdy8UasaUMEicocU4kg3cCfBv2k06N3fsdJuqEnVZN82bw1dWIOHn9vvHvPlLxrV5QTpnoV6JSGimmQfoGgI3oh%2BRVhq3hOmJwA4Q1oqJp89ryUHsBKqYfhRxg4Jv8gt2qlsqCLA%2FolkQPTOb16iy5NC16hPljEY%2BoGti3boWCTtBpLXnyu6YlI0dQCbe2Qn24UI5HRNF55nuBpnTZFnbHmkv74EHbzg8FOwLUtqnSwMcwd7Xue03%2FHnnBUMsvQZNXlgPgCXkONfKwz6p0cs3vwUfSmkYVQMaoWjAjIH3LouIhUMf5gCb2geVcvSoafIhcilpHzCHlXjPVZ74SYFLJgqSMBGZ1vKhgN3Nw%2F2hJqJE1b8whBuO%2F0emHFsNPG7YCOpqox2NGxbaukQjmm4E5xnYTZqdjY%2Bu%2BO7%2Bmq98j9GuWgM7SnUyOsb%2BwD6z0WUQ7rULULkHJDwP%2BwlmdLzm68uHobkGC5ID3GHj7U08ud%2FudPKVemgTeY2UxWn5s58zPejZ%2F2mAjiZDiB2uOmRhMOD0h84GOqUBuOcFUvrrKYK9ekdkw0frjRtU4vbVyCiGhodrGmuC%2FJykNacOeNi4Tcf7AtgA60nlCp3wWfxgXy%2BSZXoyuJsvuHd2MyFlVn1Ho7NTIKdTtu6GuMFo8uXrBfCf%2B6WyJQ5GoRNvVLWqa8KLgmfxTAGowop610Y%2BsPgxS7y%2FM91A8aHCrccPKm3gSLSW7gYpP%2BkPNJEMaGx7F1YwgcOm%2FQQm32cWzGdJ&X-Amz-Signature=20da66cd9fd7c635adf0d7543538c76c9bb0fdef40e5e9e897d5482e5edc8fba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTATYTHV%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDToBAMgpjR61ANUO2XrjNhZo0al68SsseNANvSeZAeqQIgO%2FRZL3mHGDAlwrOl0bksJ6CnCQa%2BBum1FCWbb3hy9y0qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHKDUvb4vm3LW40%2FFCrcA2uetDnRW3aWdqGwFTcIvpESotutffqMXIFCZRKdgFvTNuZa8xBaMSr3fNlcMKsba4Ckm%2F6ObIu3siV%2B5VDT6ldVUfbAOKvVCsFuuzc%2Fdy8UasaUMEicocU4kg3cCfBv2k06N3fsdJuqEnVZN82bw1dWIOHn9vvHvPlLxrV5QTpnoV6JSGimmQfoGgI3oh%2BRVhq3hOmJwA4Q1oqJp89ryUHsBKqYfhRxg4Jv8gt2qlsqCLA%2FolkQPTOb16iy5NC16hPljEY%2BoGti3boWCTtBpLXnyu6YlI0dQCbe2Qn24UI5HRNF55nuBpnTZFnbHmkv74EHbzg8FOwLUtqnSwMcwd7Xue03%2FHnnBUMsvQZNXlgPgCXkONfKwz6p0cs3vwUfSmkYVQMaoWjAjIH3LouIhUMf5gCb2geVcvSoafIhcilpHzCHlXjPVZ74SYFLJgqSMBGZ1vKhgN3Nw%2F2hJqJE1b8whBuO%2F0emHFsNPG7YCOpqox2NGxbaukQjmm4E5xnYTZqdjY%2Bu%2BO7%2Bmq98j9GuWgM7SnUyOsb%2BwD6z0WUQ7rULULkHJDwP%2BwlmdLzm68uHobkGC5ID3GHj7U08ud%2FudPKVemgTeY2UxWn5s58zPejZ%2F2mAjiZDiB2uOmRhMOD0h84GOqUBuOcFUvrrKYK9ekdkw0frjRtU4vbVyCiGhodrGmuC%2FJykNacOeNi4Tcf7AtgA60nlCp3wWfxgXy%2BSZXoyuJsvuHd2MyFlVn1Ho7NTIKdTtu6GuMFo8uXrBfCf%2B6WyJQ5GoRNvVLWqa8KLgmfxTAGowop610Y%2BsPgxS7y%2FM91A8aHCrccPKm3gSLSW7gYpP%2BkPNJEMaGx7F1YwgcOm%2FQQm32cWzGdJ&X-Amz-Signature=b5e927015220b2c63a5b5e8a445ff5965f97b7991fc47f96704e425dc31591e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

