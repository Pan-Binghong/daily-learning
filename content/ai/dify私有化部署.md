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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DGQBGJ6%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIDVekMzRQQyGjY8Jf93fXmI6ED%2FCEubgZDSz4QuvGNecAiBHOC%2FsAmbM9Nlrc53Vy9NHTtyulnubP3LE1VKcyZMiFCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMtGF2r5FcttQ3onD8KtwDee%2F3zR5cYuVRpOlE8tLASuL8iXLiMNtmhH10W3F78W%2BGr1hjIU%2BHsxU08uNF8QuvrcvU3QMLEvxJKUyH3OTleYaa%2BfStVhUQim6zGBw3L0nPYO7V%2BgfMke9EWQHOuitHrBCQTRNYe2LVGIiUyr8dw93nVmg1bHFnQJhOyT2dbF82grOUrcxWc1xgO4xRv38svGh5rBJ1qASZ%2F92gXeZPZFsfaiYvHmR5Oo0GvwY%2FdVYcyGjnhYaS5mXQCnGejWlfA86R8T%2FsPtMR4yTfFn%2FlYXT5OL%2FNEz%2B3i1gDg2hswRTQVMunC1bvk%2FgY03Tq24W3CK0zjzhiUogG81DBpdfagMa2uvjqcFr%2F7IsDLbbI24lFIW%2FWfXkyvipeTYAWv3XvGJ4ZfZC%2BEUQ52BuzhxoDsnof3PKmkTSyVkicCKDIrlhWthOn3r2Iz7G7aZ%2BpU%2FsbGNOJ4T6Ab7rohZarBrJNg7OV8m2pBzSK%2FBpk5%2BrfCVGd%2BqMv9aTVPUeJIMDnEGaRlSC7qiIo2euVOhlrv%2FhB%2FZK%2BrkczcWrlLHrwNqnpqLl9ar6YRVEkWNseiex8uoUtSpUOtJP%2FIA6G%2BAkl9Sg0JS0HOa%2BBKsRXlCS2kG%2FMK%2B4ms8sYgFI5PdA2%2BiQw5p%2F%2FyAY6pgFCupXY7x3yFg4A4p10XWqkscAO5%2FfZDsQbEucT3PFCsQNo8C0vWkkN2gnui5Tmc9kye6ShgJwVEuhhYUqRJu%2Be2tN7rReEQ1SBlVHRqzm1Jc1nqXpnvp53eCECNdZMRpjWrwB%2BElrqjfnb%2Bi6RVUPPxkVcHVj19ZZ3iHlSLOyuJndsTJoOdSBxX3heSlcO7ub608QoDyTpJaUl8DMGKnhZS4AhTi1m&X-Amz-Signature=1cc41251d35ee15d2655f9df6b14809aa8d17162bb262f67cc891e9bb0cc49a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DGQBGJ6%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIDVekMzRQQyGjY8Jf93fXmI6ED%2FCEubgZDSz4QuvGNecAiBHOC%2FsAmbM9Nlrc53Vy9NHTtyulnubP3LE1VKcyZMiFCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMtGF2r5FcttQ3onD8KtwDee%2F3zR5cYuVRpOlE8tLASuL8iXLiMNtmhH10W3F78W%2BGr1hjIU%2BHsxU08uNF8QuvrcvU3QMLEvxJKUyH3OTleYaa%2BfStVhUQim6zGBw3L0nPYO7V%2BgfMke9EWQHOuitHrBCQTRNYe2LVGIiUyr8dw93nVmg1bHFnQJhOyT2dbF82grOUrcxWc1xgO4xRv38svGh5rBJ1qASZ%2F92gXeZPZFsfaiYvHmR5Oo0GvwY%2FdVYcyGjnhYaS5mXQCnGejWlfA86R8T%2FsPtMR4yTfFn%2FlYXT5OL%2FNEz%2B3i1gDg2hswRTQVMunC1bvk%2FgY03Tq24W3CK0zjzhiUogG81DBpdfagMa2uvjqcFr%2F7IsDLbbI24lFIW%2FWfXkyvipeTYAWv3XvGJ4ZfZC%2BEUQ52BuzhxoDsnof3PKmkTSyVkicCKDIrlhWthOn3r2Iz7G7aZ%2BpU%2FsbGNOJ4T6Ab7rohZarBrJNg7OV8m2pBzSK%2FBpk5%2BrfCVGd%2BqMv9aTVPUeJIMDnEGaRlSC7qiIo2euVOhlrv%2FhB%2FZK%2BrkczcWrlLHrwNqnpqLl9ar6YRVEkWNseiex8uoUtSpUOtJP%2FIA6G%2BAkl9Sg0JS0HOa%2BBKsRXlCS2kG%2FMK%2B4ms8sYgFI5PdA2%2BiQw5p%2F%2FyAY6pgFCupXY7x3yFg4A4p10XWqkscAO5%2FfZDsQbEucT3PFCsQNo8C0vWkkN2gnui5Tmc9kye6ShgJwVEuhhYUqRJu%2Be2tN7rReEQ1SBlVHRqzm1Jc1nqXpnvp53eCECNdZMRpjWrwB%2BElrqjfnb%2Bi6RVUPPxkVcHVj19ZZ3iHlSLOyuJndsTJoOdSBxX3heSlcO7ub608QoDyTpJaUl8DMGKnhZS4AhTi1m&X-Amz-Signature=ae266ed1cc09669770eeaa457a9fcf8192018c091ba846881f55f37e1e57e097&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DGQBGJ6%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIDVekMzRQQyGjY8Jf93fXmI6ED%2FCEubgZDSz4QuvGNecAiBHOC%2FsAmbM9Nlrc53Vy9NHTtyulnubP3LE1VKcyZMiFCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMtGF2r5FcttQ3onD8KtwDee%2F3zR5cYuVRpOlE8tLASuL8iXLiMNtmhH10W3F78W%2BGr1hjIU%2BHsxU08uNF8QuvrcvU3QMLEvxJKUyH3OTleYaa%2BfStVhUQim6zGBw3L0nPYO7V%2BgfMke9EWQHOuitHrBCQTRNYe2LVGIiUyr8dw93nVmg1bHFnQJhOyT2dbF82grOUrcxWc1xgO4xRv38svGh5rBJ1qASZ%2F92gXeZPZFsfaiYvHmR5Oo0GvwY%2FdVYcyGjnhYaS5mXQCnGejWlfA86R8T%2FsPtMR4yTfFn%2FlYXT5OL%2FNEz%2B3i1gDg2hswRTQVMunC1bvk%2FgY03Tq24W3CK0zjzhiUogG81DBpdfagMa2uvjqcFr%2F7IsDLbbI24lFIW%2FWfXkyvipeTYAWv3XvGJ4ZfZC%2BEUQ52BuzhxoDsnof3PKmkTSyVkicCKDIrlhWthOn3r2Iz7G7aZ%2BpU%2FsbGNOJ4T6Ab7rohZarBrJNg7OV8m2pBzSK%2FBpk5%2BrfCVGd%2BqMv9aTVPUeJIMDnEGaRlSC7qiIo2euVOhlrv%2FhB%2FZK%2BrkczcWrlLHrwNqnpqLl9ar6YRVEkWNseiex8uoUtSpUOtJP%2FIA6G%2BAkl9Sg0JS0HOa%2BBKsRXlCS2kG%2FMK%2B4ms8sYgFI5PdA2%2BiQw5p%2F%2FyAY6pgFCupXY7x3yFg4A4p10XWqkscAO5%2FfZDsQbEucT3PFCsQNo8C0vWkkN2gnui5Tmc9kye6ShgJwVEuhhYUqRJu%2Be2tN7rReEQ1SBlVHRqzm1Jc1nqXpnvp53eCECNdZMRpjWrwB%2BElrqjfnb%2Bi6RVUPPxkVcHVj19ZZ3iHlSLOyuJndsTJoOdSBxX3heSlcO7ub608QoDyTpJaUl8DMGKnhZS4AhTi1m&X-Amz-Signature=cf82c22c347d37bee954688a1f0e12a0480719b6387c1f996cce7aadac78ac81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DGQBGJ6%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIDVekMzRQQyGjY8Jf93fXmI6ED%2FCEubgZDSz4QuvGNecAiBHOC%2FsAmbM9Nlrc53Vy9NHTtyulnubP3LE1VKcyZMiFCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMtGF2r5FcttQ3onD8KtwDee%2F3zR5cYuVRpOlE8tLASuL8iXLiMNtmhH10W3F78W%2BGr1hjIU%2BHsxU08uNF8QuvrcvU3QMLEvxJKUyH3OTleYaa%2BfStVhUQim6zGBw3L0nPYO7V%2BgfMke9EWQHOuitHrBCQTRNYe2LVGIiUyr8dw93nVmg1bHFnQJhOyT2dbF82grOUrcxWc1xgO4xRv38svGh5rBJ1qASZ%2F92gXeZPZFsfaiYvHmR5Oo0GvwY%2FdVYcyGjnhYaS5mXQCnGejWlfA86R8T%2FsPtMR4yTfFn%2FlYXT5OL%2FNEz%2B3i1gDg2hswRTQVMunC1bvk%2FgY03Tq24W3CK0zjzhiUogG81DBpdfagMa2uvjqcFr%2F7IsDLbbI24lFIW%2FWfXkyvipeTYAWv3XvGJ4ZfZC%2BEUQ52BuzhxoDsnof3PKmkTSyVkicCKDIrlhWthOn3r2Iz7G7aZ%2BpU%2FsbGNOJ4T6Ab7rohZarBrJNg7OV8m2pBzSK%2FBpk5%2BrfCVGd%2BqMv9aTVPUeJIMDnEGaRlSC7qiIo2euVOhlrv%2FhB%2FZK%2BrkczcWrlLHrwNqnpqLl9ar6YRVEkWNseiex8uoUtSpUOtJP%2FIA6G%2BAkl9Sg0JS0HOa%2BBKsRXlCS2kG%2FMK%2B4ms8sYgFI5PdA2%2BiQw5p%2F%2FyAY6pgFCupXY7x3yFg4A4p10XWqkscAO5%2FfZDsQbEucT3PFCsQNo8C0vWkkN2gnui5Tmc9kye6ShgJwVEuhhYUqRJu%2Be2tN7rReEQ1SBlVHRqzm1Jc1nqXpnvp53eCECNdZMRpjWrwB%2BElrqjfnb%2Bi6RVUPPxkVcHVj19ZZ3iHlSLOyuJndsTJoOdSBxX3heSlcO7ub608QoDyTpJaUl8DMGKnhZS4AhTi1m&X-Amz-Signature=2fb46a3fac66fc7d8505f91492f433ad4522f5f979342659cff3c7e6b801d6b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DGQBGJ6%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIDVekMzRQQyGjY8Jf93fXmI6ED%2FCEubgZDSz4QuvGNecAiBHOC%2FsAmbM9Nlrc53Vy9NHTtyulnubP3LE1VKcyZMiFCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMtGF2r5FcttQ3onD8KtwDee%2F3zR5cYuVRpOlE8tLASuL8iXLiMNtmhH10W3F78W%2BGr1hjIU%2BHsxU08uNF8QuvrcvU3QMLEvxJKUyH3OTleYaa%2BfStVhUQim6zGBw3L0nPYO7V%2BgfMke9EWQHOuitHrBCQTRNYe2LVGIiUyr8dw93nVmg1bHFnQJhOyT2dbF82grOUrcxWc1xgO4xRv38svGh5rBJ1qASZ%2F92gXeZPZFsfaiYvHmR5Oo0GvwY%2FdVYcyGjnhYaS5mXQCnGejWlfA86R8T%2FsPtMR4yTfFn%2FlYXT5OL%2FNEz%2B3i1gDg2hswRTQVMunC1bvk%2FgY03Tq24W3CK0zjzhiUogG81DBpdfagMa2uvjqcFr%2F7IsDLbbI24lFIW%2FWfXkyvipeTYAWv3XvGJ4ZfZC%2BEUQ52BuzhxoDsnof3PKmkTSyVkicCKDIrlhWthOn3r2Iz7G7aZ%2BpU%2FsbGNOJ4T6Ab7rohZarBrJNg7OV8m2pBzSK%2FBpk5%2BrfCVGd%2BqMv9aTVPUeJIMDnEGaRlSC7qiIo2euVOhlrv%2FhB%2FZK%2BrkczcWrlLHrwNqnpqLl9ar6YRVEkWNseiex8uoUtSpUOtJP%2FIA6G%2BAkl9Sg0JS0HOa%2BBKsRXlCS2kG%2FMK%2B4ms8sYgFI5PdA2%2BiQw5p%2F%2FyAY6pgFCupXY7x3yFg4A4p10XWqkscAO5%2FfZDsQbEucT3PFCsQNo8C0vWkkN2gnui5Tmc9kye6ShgJwVEuhhYUqRJu%2Be2tN7rReEQ1SBlVHRqzm1Jc1nqXpnvp53eCECNdZMRpjWrwB%2BElrqjfnb%2Bi6RVUPPxkVcHVj19ZZ3iHlSLOyuJndsTJoOdSBxX3heSlcO7ub608QoDyTpJaUl8DMGKnhZS4AhTi1m&X-Amz-Signature=e8f3f16c53d7749e23e54cf65b023a7816732f2aad1aca7600ec7f1803ac6e0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DGQBGJ6%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIDVekMzRQQyGjY8Jf93fXmI6ED%2FCEubgZDSz4QuvGNecAiBHOC%2FsAmbM9Nlrc53Vy9NHTtyulnubP3LE1VKcyZMiFCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMtGF2r5FcttQ3onD8KtwDee%2F3zR5cYuVRpOlE8tLASuL8iXLiMNtmhH10W3F78W%2BGr1hjIU%2BHsxU08uNF8QuvrcvU3QMLEvxJKUyH3OTleYaa%2BfStVhUQim6zGBw3L0nPYO7V%2BgfMke9EWQHOuitHrBCQTRNYe2LVGIiUyr8dw93nVmg1bHFnQJhOyT2dbF82grOUrcxWc1xgO4xRv38svGh5rBJ1qASZ%2F92gXeZPZFsfaiYvHmR5Oo0GvwY%2FdVYcyGjnhYaS5mXQCnGejWlfA86R8T%2FsPtMR4yTfFn%2FlYXT5OL%2FNEz%2B3i1gDg2hswRTQVMunC1bvk%2FgY03Tq24W3CK0zjzhiUogG81DBpdfagMa2uvjqcFr%2F7IsDLbbI24lFIW%2FWfXkyvipeTYAWv3XvGJ4ZfZC%2BEUQ52BuzhxoDsnof3PKmkTSyVkicCKDIrlhWthOn3r2Iz7G7aZ%2BpU%2FsbGNOJ4T6Ab7rohZarBrJNg7OV8m2pBzSK%2FBpk5%2BrfCVGd%2BqMv9aTVPUeJIMDnEGaRlSC7qiIo2euVOhlrv%2FhB%2FZK%2BrkczcWrlLHrwNqnpqLl9ar6YRVEkWNseiex8uoUtSpUOtJP%2FIA6G%2BAkl9Sg0JS0HOa%2BBKsRXlCS2kG%2FMK%2B4ms8sYgFI5PdA2%2BiQw5p%2F%2FyAY6pgFCupXY7x3yFg4A4p10XWqkscAO5%2FfZDsQbEucT3PFCsQNo8C0vWkkN2gnui5Tmc9kye6ShgJwVEuhhYUqRJu%2Be2tN7rReEQ1SBlVHRqzm1Jc1nqXpnvp53eCECNdZMRpjWrwB%2BElrqjfnb%2Bi6RVUPPxkVcHVj19ZZ3iHlSLOyuJndsTJoOdSBxX3heSlcO7ub608QoDyTpJaUl8DMGKnhZS4AhTi1m&X-Amz-Signature=01c297a2ee21a86dfee2ce27ff3172956d17fdf2e01d702d43998a24fbb64fdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DGQBGJ6%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIDVekMzRQQyGjY8Jf93fXmI6ED%2FCEubgZDSz4QuvGNecAiBHOC%2FsAmbM9Nlrc53Vy9NHTtyulnubP3LE1VKcyZMiFCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMtGF2r5FcttQ3onD8KtwDee%2F3zR5cYuVRpOlE8tLASuL8iXLiMNtmhH10W3F78W%2BGr1hjIU%2BHsxU08uNF8QuvrcvU3QMLEvxJKUyH3OTleYaa%2BfStVhUQim6zGBw3L0nPYO7V%2BgfMke9EWQHOuitHrBCQTRNYe2LVGIiUyr8dw93nVmg1bHFnQJhOyT2dbF82grOUrcxWc1xgO4xRv38svGh5rBJ1qASZ%2F92gXeZPZFsfaiYvHmR5Oo0GvwY%2FdVYcyGjnhYaS5mXQCnGejWlfA86R8T%2FsPtMR4yTfFn%2FlYXT5OL%2FNEz%2B3i1gDg2hswRTQVMunC1bvk%2FgY03Tq24W3CK0zjzhiUogG81DBpdfagMa2uvjqcFr%2F7IsDLbbI24lFIW%2FWfXkyvipeTYAWv3XvGJ4ZfZC%2BEUQ52BuzhxoDsnof3PKmkTSyVkicCKDIrlhWthOn3r2Iz7G7aZ%2BpU%2FsbGNOJ4T6Ab7rohZarBrJNg7OV8m2pBzSK%2FBpk5%2BrfCVGd%2BqMv9aTVPUeJIMDnEGaRlSC7qiIo2euVOhlrv%2FhB%2FZK%2BrkczcWrlLHrwNqnpqLl9ar6YRVEkWNseiex8uoUtSpUOtJP%2FIA6G%2BAkl9Sg0JS0HOa%2BBKsRXlCS2kG%2FMK%2B4ms8sYgFI5PdA2%2BiQw5p%2F%2FyAY6pgFCupXY7x3yFg4A4p10XWqkscAO5%2FfZDsQbEucT3PFCsQNo8C0vWkkN2gnui5Tmc9kye6ShgJwVEuhhYUqRJu%2Be2tN7rReEQ1SBlVHRqzm1Jc1nqXpnvp53eCECNdZMRpjWrwB%2BElrqjfnb%2Bi6RVUPPxkVcHVj19ZZ3iHlSLOyuJndsTJoOdSBxX3heSlcO7ub608QoDyTpJaUl8DMGKnhZS4AhTi1m&X-Amz-Signature=5b043f2976119ae09832b3c46d357995f46ac83df8691df06957b95f57bfdb35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DGQBGJ6%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIDVekMzRQQyGjY8Jf93fXmI6ED%2FCEubgZDSz4QuvGNecAiBHOC%2FsAmbM9Nlrc53Vy9NHTtyulnubP3LE1VKcyZMiFCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMtGF2r5FcttQ3onD8KtwDee%2F3zR5cYuVRpOlE8tLASuL8iXLiMNtmhH10W3F78W%2BGr1hjIU%2BHsxU08uNF8QuvrcvU3QMLEvxJKUyH3OTleYaa%2BfStVhUQim6zGBw3L0nPYO7V%2BgfMke9EWQHOuitHrBCQTRNYe2LVGIiUyr8dw93nVmg1bHFnQJhOyT2dbF82grOUrcxWc1xgO4xRv38svGh5rBJ1qASZ%2F92gXeZPZFsfaiYvHmR5Oo0GvwY%2FdVYcyGjnhYaS5mXQCnGejWlfA86R8T%2FsPtMR4yTfFn%2FlYXT5OL%2FNEz%2B3i1gDg2hswRTQVMunC1bvk%2FgY03Tq24W3CK0zjzhiUogG81DBpdfagMa2uvjqcFr%2F7IsDLbbI24lFIW%2FWfXkyvipeTYAWv3XvGJ4ZfZC%2BEUQ52BuzhxoDsnof3PKmkTSyVkicCKDIrlhWthOn3r2Iz7G7aZ%2BpU%2FsbGNOJ4T6Ab7rohZarBrJNg7OV8m2pBzSK%2FBpk5%2BrfCVGd%2BqMv9aTVPUeJIMDnEGaRlSC7qiIo2euVOhlrv%2FhB%2FZK%2BrkczcWrlLHrwNqnpqLl9ar6YRVEkWNseiex8uoUtSpUOtJP%2FIA6G%2BAkl9Sg0JS0HOa%2BBKsRXlCS2kG%2FMK%2B4ms8sYgFI5PdA2%2BiQw5p%2F%2FyAY6pgFCupXY7x3yFg4A4p10XWqkscAO5%2FfZDsQbEucT3PFCsQNo8C0vWkkN2gnui5Tmc9kye6ShgJwVEuhhYUqRJu%2Be2tN7rReEQ1SBlVHRqzm1Jc1nqXpnvp53eCECNdZMRpjWrwB%2BElrqjfnb%2Bi6RVUPPxkVcHVj19ZZ3iHlSLOyuJndsTJoOdSBxX3heSlcO7ub608QoDyTpJaUl8DMGKnhZS4AhTi1m&X-Amz-Signature=4855ac4ac04d9ada1b9437170fb5c4dfd9720943545f29107a9a86f34df10d5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DGQBGJ6%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIDVekMzRQQyGjY8Jf93fXmI6ED%2FCEubgZDSz4QuvGNecAiBHOC%2FsAmbM9Nlrc53Vy9NHTtyulnubP3LE1VKcyZMiFCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMtGF2r5FcttQ3onD8KtwDee%2F3zR5cYuVRpOlE8tLASuL8iXLiMNtmhH10W3F78W%2BGr1hjIU%2BHsxU08uNF8QuvrcvU3QMLEvxJKUyH3OTleYaa%2BfStVhUQim6zGBw3L0nPYO7V%2BgfMke9EWQHOuitHrBCQTRNYe2LVGIiUyr8dw93nVmg1bHFnQJhOyT2dbF82grOUrcxWc1xgO4xRv38svGh5rBJ1qASZ%2F92gXeZPZFsfaiYvHmR5Oo0GvwY%2FdVYcyGjnhYaS5mXQCnGejWlfA86R8T%2FsPtMR4yTfFn%2FlYXT5OL%2FNEz%2B3i1gDg2hswRTQVMunC1bvk%2FgY03Tq24W3CK0zjzhiUogG81DBpdfagMa2uvjqcFr%2F7IsDLbbI24lFIW%2FWfXkyvipeTYAWv3XvGJ4ZfZC%2BEUQ52BuzhxoDsnof3PKmkTSyVkicCKDIrlhWthOn3r2Iz7G7aZ%2BpU%2FsbGNOJ4T6Ab7rohZarBrJNg7OV8m2pBzSK%2FBpk5%2BrfCVGd%2BqMv9aTVPUeJIMDnEGaRlSC7qiIo2euVOhlrv%2FhB%2FZK%2BrkczcWrlLHrwNqnpqLl9ar6YRVEkWNseiex8uoUtSpUOtJP%2FIA6G%2BAkl9Sg0JS0HOa%2BBKsRXlCS2kG%2FMK%2B4ms8sYgFI5PdA2%2BiQw5p%2F%2FyAY6pgFCupXY7x3yFg4A4p10XWqkscAO5%2FfZDsQbEucT3PFCsQNo8C0vWkkN2gnui5Tmc9kye6ShgJwVEuhhYUqRJu%2Be2tN7rReEQ1SBlVHRqzm1Jc1nqXpnvp53eCECNdZMRpjWrwB%2BElrqjfnb%2Bi6RVUPPxkVcHVj19ZZ3iHlSLOyuJndsTJoOdSBxX3heSlcO7ub608QoDyTpJaUl8DMGKnhZS4AhTi1m&X-Amz-Signature=b833dd71d2992af8181b6e09ea60aa70a80924844c3155e6ffd06875d585421f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DGQBGJ6%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIDVekMzRQQyGjY8Jf93fXmI6ED%2FCEubgZDSz4QuvGNecAiBHOC%2FsAmbM9Nlrc53Vy9NHTtyulnubP3LE1VKcyZMiFCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMtGF2r5FcttQ3onD8KtwDee%2F3zR5cYuVRpOlE8tLASuL8iXLiMNtmhH10W3F78W%2BGr1hjIU%2BHsxU08uNF8QuvrcvU3QMLEvxJKUyH3OTleYaa%2BfStVhUQim6zGBw3L0nPYO7V%2BgfMke9EWQHOuitHrBCQTRNYe2LVGIiUyr8dw93nVmg1bHFnQJhOyT2dbF82grOUrcxWc1xgO4xRv38svGh5rBJ1qASZ%2F92gXeZPZFsfaiYvHmR5Oo0GvwY%2FdVYcyGjnhYaS5mXQCnGejWlfA86R8T%2FsPtMR4yTfFn%2FlYXT5OL%2FNEz%2B3i1gDg2hswRTQVMunC1bvk%2FgY03Tq24W3CK0zjzhiUogG81DBpdfagMa2uvjqcFr%2F7IsDLbbI24lFIW%2FWfXkyvipeTYAWv3XvGJ4ZfZC%2BEUQ52BuzhxoDsnof3PKmkTSyVkicCKDIrlhWthOn3r2Iz7G7aZ%2BpU%2FsbGNOJ4T6Ab7rohZarBrJNg7OV8m2pBzSK%2FBpk5%2BrfCVGd%2BqMv9aTVPUeJIMDnEGaRlSC7qiIo2euVOhlrv%2FhB%2FZK%2BrkczcWrlLHrwNqnpqLl9ar6YRVEkWNseiex8uoUtSpUOtJP%2FIA6G%2BAkl9Sg0JS0HOa%2BBKsRXlCS2kG%2FMK%2B4ms8sYgFI5PdA2%2BiQw5p%2F%2FyAY6pgFCupXY7x3yFg4A4p10XWqkscAO5%2FfZDsQbEucT3PFCsQNo8C0vWkkN2gnui5Tmc9kye6ShgJwVEuhhYUqRJu%2Be2tN7rReEQ1SBlVHRqzm1Jc1nqXpnvp53eCECNdZMRpjWrwB%2BElrqjfnb%2Bi6RVUPPxkVcHVj19ZZ3iHlSLOyuJndsTJoOdSBxX3heSlcO7ub608QoDyTpJaUl8DMGKnhZS4AhTi1m&X-Amz-Signature=a3d33fdccd18aeb1675d50a431343c455771ed0352ae870d8844eb4f9b06877d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

