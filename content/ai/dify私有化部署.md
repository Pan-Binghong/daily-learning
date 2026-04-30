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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZ5LYX6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDMtBUIsj7cyJLtLpRJIEjyMZHvd3OH2Daee1CUG1e6dAIgU5OuiQmQIhE6TdNUgZiCh7oX5sZAhoBeLtrz2Rf9PLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCg8m%2BCCOaK7QNYWJyrcA1jHXWLmnakJ%2BCW9s%2BG0opx2qPeA3zAt6sONoUVgUbj71IUx%2BnYQJs%2FhzeFwf8yRnL6GE70v%2BFKi%2BeVIjld%2Bjleuyo941Mw8%2B3UEpF9W0B6en%2FZWyJhB08KUlKm0lrrv63YzICyh0%2BseaZRt3Gvk2BZUXpWz1TlOWyBYOuP6qMoPFVyyxex0YEqn74vIAajdL3JJynMtsk9kMWnurC1tUPxXGDSdRhtXB5jrx6aDp9PrbcD8BubiUWX4q%2FRFRHHhFm%2FkYo1RXdqs3x405Ss%2Fo1ULe1zspbQqPM%2BqCoeTFP5ZPuOU22asnEEorMDplnbyZtSAYgr6wMdAJ%2BPWTun5odmsyjeV1gcA0bQwJk1VWyD818gxTvZbtEug2wRuBbiJv3fNDyoxldMt6P8M4GCbkVyLw5ixUcsxznSkckcj%2FPm1Q%2B9QtM%2BQOJiqAQ%2FJ%2F%2FvZeqPk44Hhf%2Bmg26I5FDTYCQTZ3LQ5FhXDaIN31kq23E%2BB%2BxxeSyeOANQyjNPn2rI%2BJayOo4v3qz%2Fyc4Ror2V6rBm%2B3btYpJZfMcnMHEBZ4Msv%2BJy7EvB%2ButZVoGfknzh%2BLzROFQ8CotWYWZgQivSEYpTAAmgkF9%2F%2FcRSCdW010myPtRrRcm6a%2F5PC1HAIMN%2BezM8GOqUBFwsORA3eoKLE159hrxR6I2U6quLas9I6wLa3%2B0ofozYIv7M1pQu36Evfh%2BPTbiS3g%2F2bR6sk1H6ynKp3zXqnDNm6X54O8%2BHQr4lcpkarZr4S1dI9KUuglrqMo4mdrDmB8wo9CwEdSzeaaMTyrVmOqtHZDE1%2FjqRTPdZK5gAMTaHAMHlPK%2FHfXivPN1DNoSK6wGvN2xkKWSH6PrxR8DXwFAojtFjm&X-Amz-Signature=2668ca2a1c38a19291a1ad26850f48128c56eca46598b6a61a008e1293a9bc7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZ5LYX6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDMtBUIsj7cyJLtLpRJIEjyMZHvd3OH2Daee1CUG1e6dAIgU5OuiQmQIhE6TdNUgZiCh7oX5sZAhoBeLtrz2Rf9PLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCg8m%2BCCOaK7QNYWJyrcA1jHXWLmnakJ%2BCW9s%2BG0opx2qPeA3zAt6sONoUVgUbj71IUx%2BnYQJs%2FhzeFwf8yRnL6GE70v%2BFKi%2BeVIjld%2Bjleuyo941Mw8%2B3UEpF9W0B6en%2FZWyJhB08KUlKm0lrrv63YzICyh0%2BseaZRt3Gvk2BZUXpWz1TlOWyBYOuP6qMoPFVyyxex0YEqn74vIAajdL3JJynMtsk9kMWnurC1tUPxXGDSdRhtXB5jrx6aDp9PrbcD8BubiUWX4q%2FRFRHHhFm%2FkYo1RXdqs3x405Ss%2Fo1ULe1zspbQqPM%2BqCoeTFP5ZPuOU22asnEEorMDplnbyZtSAYgr6wMdAJ%2BPWTun5odmsyjeV1gcA0bQwJk1VWyD818gxTvZbtEug2wRuBbiJv3fNDyoxldMt6P8M4GCbkVyLw5ixUcsxznSkckcj%2FPm1Q%2B9QtM%2BQOJiqAQ%2FJ%2F%2FvZeqPk44Hhf%2Bmg26I5FDTYCQTZ3LQ5FhXDaIN31kq23E%2BB%2BxxeSyeOANQyjNPn2rI%2BJayOo4v3qz%2Fyc4Ror2V6rBm%2B3btYpJZfMcnMHEBZ4Msv%2BJy7EvB%2ButZVoGfknzh%2BLzROFQ8CotWYWZgQivSEYpTAAmgkF9%2F%2FcRSCdW010myPtRrRcm6a%2F5PC1HAIMN%2BezM8GOqUBFwsORA3eoKLE159hrxR6I2U6quLas9I6wLa3%2B0ofozYIv7M1pQu36Evfh%2BPTbiS3g%2F2bR6sk1H6ynKp3zXqnDNm6X54O8%2BHQr4lcpkarZr4S1dI9KUuglrqMo4mdrDmB8wo9CwEdSzeaaMTyrVmOqtHZDE1%2FjqRTPdZK5gAMTaHAMHlPK%2FHfXivPN1DNoSK6wGvN2xkKWSH6PrxR8DXwFAojtFjm&X-Amz-Signature=4b149d64ef4846e52ae7d2563710dbd53a648029952b9c72476f653975fc500b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZ5LYX6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDMtBUIsj7cyJLtLpRJIEjyMZHvd3OH2Daee1CUG1e6dAIgU5OuiQmQIhE6TdNUgZiCh7oX5sZAhoBeLtrz2Rf9PLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCg8m%2BCCOaK7QNYWJyrcA1jHXWLmnakJ%2BCW9s%2BG0opx2qPeA3zAt6sONoUVgUbj71IUx%2BnYQJs%2FhzeFwf8yRnL6GE70v%2BFKi%2BeVIjld%2Bjleuyo941Mw8%2B3UEpF9W0B6en%2FZWyJhB08KUlKm0lrrv63YzICyh0%2BseaZRt3Gvk2BZUXpWz1TlOWyBYOuP6qMoPFVyyxex0YEqn74vIAajdL3JJynMtsk9kMWnurC1tUPxXGDSdRhtXB5jrx6aDp9PrbcD8BubiUWX4q%2FRFRHHhFm%2FkYo1RXdqs3x405Ss%2Fo1ULe1zspbQqPM%2BqCoeTFP5ZPuOU22asnEEorMDplnbyZtSAYgr6wMdAJ%2BPWTun5odmsyjeV1gcA0bQwJk1VWyD818gxTvZbtEug2wRuBbiJv3fNDyoxldMt6P8M4GCbkVyLw5ixUcsxznSkckcj%2FPm1Q%2B9QtM%2BQOJiqAQ%2FJ%2F%2FvZeqPk44Hhf%2Bmg26I5FDTYCQTZ3LQ5FhXDaIN31kq23E%2BB%2BxxeSyeOANQyjNPn2rI%2BJayOo4v3qz%2Fyc4Ror2V6rBm%2B3btYpJZfMcnMHEBZ4Msv%2BJy7EvB%2ButZVoGfknzh%2BLzROFQ8CotWYWZgQivSEYpTAAmgkF9%2F%2FcRSCdW010myPtRrRcm6a%2F5PC1HAIMN%2BezM8GOqUBFwsORA3eoKLE159hrxR6I2U6quLas9I6wLa3%2B0ofozYIv7M1pQu36Evfh%2BPTbiS3g%2F2bR6sk1H6ynKp3zXqnDNm6X54O8%2BHQr4lcpkarZr4S1dI9KUuglrqMo4mdrDmB8wo9CwEdSzeaaMTyrVmOqtHZDE1%2FjqRTPdZK5gAMTaHAMHlPK%2FHfXivPN1DNoSK6wGvN2xkKWSH6PrxR8DXwFAojtFjm&X-Amz-Signature=e9f6e3686fa5a57b064d25a81e5ef63bb1efd4b910801986925bfd96e586e519&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZ5LYX6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDMtBUIsj7cyJLtLpRJIEjyMZHvd3OH2Daee1CUG1e6dAIgU5OuiQmQIhE6TdNUgZiCh7oX5sZAhoBeLtrz2Rf9PLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCg8m%2BCCOaK7QNYWJyrcA1jHXWLmnakJ%2BCW9s%2BG0opx2qPeA3zAt6sONoUVgUbj71IUx%2BnYQJs%2FhzeFwf8yRnL6GE70v%2BFKi%2BeVIjld%2Bjleuyo941Mw8%2B3UEpF9W0B6en%2FZWyJhB08KUlKm0lrrv63YzICyh0%2BseaZRt3Gvk2BZUXpWz1TlOWyBYOuP6qMoPFVyyxex0YEqn74vIAajdL3JJynMtsk9kMWnurC1tUPxXGDSdRhtXB5jrx6aDp9PrbcD8BubiUWX4q%2FRFRHHhFm%2FkYo1RXdqs3x405Ss%2Fo1ULe1zspbQqPM%2BqCoeTFP5ZPuOU22asnEEorMDplnbyZtSAYgr6wMdAJ%2BPWTun5odmsyjeV1gcA0bQwJk1VWyD818gxTvZbtEug2wRuBbiJv3fNDyoxldMt6P8M4GCbkVyLw5ixUcsxznSkckcj%2FPm1Q%2B9QtM%2BQOJiqAQ%2FJ%2F%2FvZeqPk44Hhf%2Bmg26I5FDTYCQTZ3LQ5FhXDaIN31kq23E%2BB%2BxxeSyeOANQyjNPn2rI%2BJayOo4v3qz%2Fyc4Ror2V6rBm%2B3btYpJZfMcnMHEBZ4Msv%2BJy7EvB%2ButZVoGfknzh%2BLzROFQ8CotWYWZgQivSEYpTAAmgkF9%2F%2FcRSCdW010myPtRrRcm6a%2F5PC1HAIMN%2BezM8GOqUBFwsORA3eoKLE159hrxR6I2U6quLas9I6wLa3%2B0ofozYIv7M1pQu36Evfh%2BPTbiS3g%2F2bR6sk1H6ynKp3zXqnDNm6X54O8%2BHQr4lcpkarZr4S1dI9KUuglrqMo4mdrDmB8wo9CwEdSzeaaMTyrVmOqtHZDE1%2FjqRTPdZK5gAMTaHAMHlPK%2FHfXivPN1DNoSK6wGvN2xkKWSH6PrxR8DXwFAojtFjm&X-Amz-Signature=9eb5212414f5d449eec3d922a8e506a4bfcd1bd280c385f42eed310311a7ed79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZ5LYX6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDMtBUIsj7cyJLtLpRJIEjyMZHvd3OH2Daee1CUG1e6dAIgU5OuiQmQIhE6TdNUgZiCh7oX5sZAhoBeLtrz2Rf9PLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCg8m%2BCCOaK7QNYWJyrcA1jHXWLmnakJ%2BCW9s%2BG0opx2qPeA3zAt6sONoUVgUbj71IUx%2BnYQJs%2FhzeFwf8yRnL6GE70v%2BFKi%2BeVIjld%2Bjleuyo941Mw8%2B3UEpF9W0B6en%2FZWyJhB08KUlKm0lrrv63YzICyh0%2BseaZRt3Gvk2BZUXpWz1TlOWyBYOuP6qMoPFVyyxex0YEqn74vIAajdL3JJynMtsk9kMWnurC1tUPxXGDSdRhtXB5jrx6aDp9PrbcD8BubiUWX4q%2FRFRHHhFm%2FkYo1RXdqs3x405Ss%2Fo1ULe1zspbQqPM%2BqCoeTFP5ZPuOU22asnEEorMDplnbyZtSAYgr6wMdAJ%2BPWTun5odmsyjeV1gcA0bQwJk1VWyD818gxTvZbtEug2wRuBbiJv3fNDyoxldMt6P8M4GCbkVyLw5ixUcsxznSkckcj%2FPm1Q%2B9QtM%2BQOJiqAQ%2FJ%2F%2FvZeqPk44Hhf%2Bmg26I5FDTYCQTZ3LQ5FhXDaIN31kq23E%2BB%2BxxeSyeOANQyjNPn2rI%2BJayOo4v3qz%2Fyc4Ror2V6rBm%2B3btYpJZfMcnMHEBZ4Msv%2BJy7EvB%2ButZVoGfknzh%2BLzROFQ8CotWYWZgQivSEYpTAAmgkF9%2F%2FcRSCdW010myPtRrRcm6a%2F5PC1HAIMN%2BezM8GOqUBFwsORA3eoKLE159hrxR6I2U6quLas9I6wLa3%2B0ofozYIv7M1pQu36Evfh%2BPTbiS3g%2F2bR6sk1H6ynKp3zXqnDNm6X54O8%2BHQr4lcpkarZr4S1dI9KUuglrqMo4mdrDmB8wo9CwEdSzeaaMTyrVmOqtHZDE1%2FjqRTPdZK5gAMTaHAMHlPK%2FHfXivPN1DNoSK6wGvN2xkKWSH6PrxR8DXwFAojtFjm&X-Amz-Signature=864dc338e890fbbf7944352249352745783d90041b4764773f3c922276a7b86f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZ5LYX6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDMtBUIsj7cyJLtLpRJIEjyMZHvd3OH2Daee1CUG1e6dAIgU5OuiQmQIhE6TdNUgZiCh7oX5sZAhoBeLtrz2Rf9PLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCg8m%2BCCOaK7QNYWJyrcA1jHXWLmnakJ%2BCW9s%2BG0opx2qPeA3zAt6sONoUVgUbj71IUx%2BnYQJs%2FhzeFwf8yRnL6GE70v%2BFKi%2BeVIjld%2Bjleuyo941Mw8%2B3UEpF9W0B6en%2FZWyJhB08KUlKm0lrrv63YzICyh0%2BseaZRt3Gvk2BZUXpWz1TlOWyBYOuP6qMoPFVyyxex0YEqn74vIAajdL3JJynMtsk9kMWnurC1tUPxXGDSdRhtXB5jrx6aDp9PrbcD8BubiUWX4q%2FRFRHHhFm%2FkYo1RXdqs3x405Ss%2Fo1ULe1zspbQqPM%2BqCoeTFP5ZPuOU22asnEEorMDplnbyZtSAYgr6wMdAJ%2BPWTun5odmsyjeV1gcA0bQwJk1VWyD818gxTvZbtEug2wRuBbiJv3fNDyoxldMt6P8M4GCbkVyLw5ixUcsxznSkckcj%2FPm1Q%2B9QtM%2BQOJiqAQ%2FJ%2F%2FvZeqPk44Hhf%2Bmg26I5FDTYCQTZ3LQ5FhXDaIN31kq23E%2BB%2BxxeSyeOANQyjNPn2rI%2BJayOo4v3qz%2Fyc4Ror2V6rBm%2B3btYpJZfMcnMHEBZ4Msv%2BJy7EvB%2ButZVoGfknzh%2BLzROFQ8CotWYWZgQivSEYpTAAmgkF9%2F%2FcRSCdW010myPtRrRcm6a%2F5PC1HAIMN%2BezM8GOqUBFwsORA3eoKLE159hrxR6I2U6quLas9I6wLa3%2B0ofozYIv7M1pQu36Evfh%2BPTbiS3g%2F2bR6sk1H6ynKp3zXqnDNm6X54O8%2BHQr4lcpkarZr4S1dI9KUuglrqMo4mdrDmB8wo9CwEdSzeaaMTyrVmOqtHZDE1%2FjqRTPdZK5gAMTaHAMHlPK%2FHfXivPN1DNoSK6wGvN2xkKWSH6PrxR8DXwFAojtFjm&X-Amz-Signature=5947a2204098053e9bef57d19114db9be554e505c43ef34fa6ca025e7f617075&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZ5LYX6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDMtBUIsj7cyJLtLpRJIEjyMZHvd3OH2Daee1CUG1e6dAIgU5OuiQmQIhE6TdNUgZiCh7oX5sZAhoBeLtrz2Rf9PLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCg8m%2BCCOaK7QNYWJyrcA1jHXWLmnakJ%2BCW9s%2BG0opx2qPeA3zAt6sONoUVgUbj71IUx%2BnYQJs%2FhzeFwf8yRnL6GE70v%2BFKi%2BeVIjld%2Bjleuyo941Mw8%2B3UEpF9W0B6en%2FZWyJhB08KUlKm0lrrv63YzICyh0%2BseaZRt3Gvk2BZUXpWz1TlOWyBYOuP6qMoPFVyyxex0YEqn74vIAajdL3JJynMtsk9kMWnurC1tUPxXGDSdRhtXB5jrx6aDp9PrbcD8BubiUWX4q%2FRFRHHhFm%2FkYo1RXdqs3x405Ss%2Fo1ULe1zspbQqPM%2BqCoeTFP5ZPuOU22asnEEorMDplnbyZtSAYgr6wMdAJ%2BPWTun5odmsyjeV1gcA0bQwJk1VWyD818gxTvZbtEug2wRuBbiJv3fNDyoxldMt6P8M4GCbkVyLw5ixUcsxznSkckcj%2FPm1Q%2B9QtM%2BQOJiqAQ%2FJ%2F%2FvZeqPk44Hhf%2Bmg26I5FDTYCQTZ3LQ5FhXDaIN31kq23E%2BB%2BxxeSyeOANQyjNPn2rI%2BJayOo4v3qz%2Fyc4Ror2V6rBm%2B3btYpJZfMcnMHEBZ4Msv%2BJy7EvB%2ButZVoGfknzh%2BLzROFQ8CotWYWZgQivSEYpTAAmgkF9%2F%2FcRSCdW010myPtRrRcm6a%2F5PC1HAIMN%2BezM8GOqUBFwsORA3eoKLE159hrxR6I2U6quLas9I6wLa3%2B0ofozYIv7M1pQu36Evfh%2BPTbiS3g%2F2bR6sk1H6ynKp3zXqnDNm6X54O8%2BHQr4lcpkarZr4S1dI9KUuglrqMo4mdrDmB8wo9CwEdSzeaaMTyrVmOqtHZDE1%2FjqRTPdZK5gAMTaHAMHlPK%2FHfXivPN1DNoSK6wGvN2xkKWSH6PrxR8DXwFAojtFjm&X-Amz-Signature=69b22f47e00bbfc5dca567e8dfbc7d78a66fa0145857dea8f77657e6fd48db62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZ5LYX6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDMtBUIsj7cyJLtLpRJIEjyMZHvd3OH2Daee1CUG1e6dAIgU5OuiQmQIhE6TdNUgZiCh7oX5sZAhoBeLtrz2Rf9PLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCg8m%2BCCOaK7QNYWJyrcA1jHXWLmnakJ%2BCW9s%2BG0opx2qPeA3zAt6sONoUVgUbj71IUx%2BnYQJs%2FhzeFwf8yRnL6GE70v%2BFKi%2BeVIjld%2Bjleuyo941Mw8%2B3UEpF9W0B6en%2FZWyJhB08KUlKm0lrrv63YzICyh0%2BseaZRt3Gvk2BZUXpWz1TlOWyBYOuP6qMoPFVyyxex0YEqn74vIAajdL3JJynMtsk9kMWnurC1tUPxXGDSdRhtXB5jrx6aDp9PrbcD8BubiUWX4q%2FRFRHHhFm%2FkYo1RXdqs3x405Ss%2Fo1ULe1zspbQqPM%2BqCoeTFP5ZPuOU22asnEEorMDplnbyZtSAYgr6wMdAJ%2BPWTun5odmsyjeV1gcA0bQwJk1VWyD818gxTvZbtEug2wRuBbiJv3fNDyoxldMt6P8M4GCbkVyLw5ixUcsxznSkckcj%2FPm1Q%2B9QtM%2BQOJiqAQ%2FJ%2F%2FvZeqPk44Hhf%2Bmg26I5FDTYCQTZ3LQ5FhXDaIN31kq23E%2BB%2BxxeSyeOANQyjNPn2rI%2BJayOo4v3qz%2Fyc4Ror2V6rBm%2B3btYpJZfMcnMHEBZ4Msv%2BJy7EvB%2ButZVoGfknzh%2BLzROFQ8CotWYWZgQivSEYpTAAmgkF9%2F%2FcRSCdW010myPtRrRcm6a%2F5PC1HAIMN%2BezM8GOqUBFwsORA3eoKLE159hrxR6I2U6quLas9I6wLa3%2B0ofozYIv7M1pQu36Evfh%2BPTbiS3g%2F2bR6sk1H6ynKp3zXqnDNm6X54O8%2BHQr4lcpkarZr4S1dI9KUuglrqMo4mdrDmB8wo9CwEdSzeaaMTyrVmOqtHZDE1%2FjqRTPdZK5gAMTaHAMHlPK%2FHfXivPN1DNoSK6wGvN2xkKWSH6PrxR8DXwFAojtFjm&X-Amz-Signature=6ab4f4329e43c952f65a7fd839fadc3183b8de1b32a438ba5426540a4ae0dd89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZ5LYX6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDMtBUIsj7cyJLtLpRJIEjyMZHvd3OH2Daee1CUG1e6dAIgU5OuiQmQIhE6TdNUgZiCh7oX5sZAhoBeLtrz2Rf9PLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCg8m%2BCCOaK7QNYWJyrcA1jHXWLmnakJ%2BCW9s%2BG0opx2qPeA3zAt6sONoUVgUbj71IUx%2BnYQJs%2FhzeFwf8yRnL6GE70v%2BFKi%2BeVIjld%2Bjleuyo941Mw8%2B3UEpF9W0B6en%2FZWyJhB08KUlKm0lrrv63YzICyh0%2BseaZRt3Gvk2BZUXpWz1TlOWyBYOuP6qMoPFVyyxex0YEqn74vIAajdL3JJynMtsk9kMWnurC1tUPxXGDSdRhtXB5jrx6aDp9PrbcD8BubiUWX4q%2FRFRHHhFm%2FkYo1RXdqs3x405Ss%2Fo1ULe1zspbQqPM%2BqCoeTFP5ZPuOU22asnEEorMDplnbyZtSAYgr6wMdAJ%2BPWTun5odmsyjeV1gcA0bQwJk1VWyD818gxTvZbtEug2wRuBbiJv3fNDyoxldMt6P8M4GCbkVyLw5ixUcsxznSkckcj%2FPm1Q%2B9QtM%2BQOJiqAQ%2FJ%2F%2FvZeqPk44Hhf%2Bmg26I5FDTYCQTZ3LQ5FhXDaIN31kq23E%2BB%2BxxeSyeOANQyjNPn2rI%2BJayOo4v3qz%2Fyc4Ror2V6rBm%2B3btYpJZfMcnMHEBZ4Msv%2BJy7EvB%2ButZVoGfknzh%2BLzROFQ8CotWYWZgQivSEYpTAAmgkF9%2F%2FcRSCdW010myPtRrRcm6a%2F5PC1HAIMN%2BezM8GOqUBFwsORA3eoKLE159hrxR6I2U6quLas9I6wLa3%2B0ofozYIv7M1pQu36Evfh%2BPTbiS3g%2F2bR6sk1H6ynKp3zXqnDNm6X54O8%2BHQr4lcpkarZr4S1dI9KUuglrqMo4mdrDmB8wo9CwEdSzeaaMTyrVmOqtHZDE1%2FjqRTPdZK5gAMTaHAMHlPK%2FHfXivPN1DNoSK6wGvN2xkKWSH6PrxR8DXwFAojtFjm&X-Amz-Signature=5e959d74e7372d9e71fd89cbc123aa4b568a68e092c2029714ae30a6da7eddc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXZ5LYX6%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDMtBUIsj7cyJLtLpRJIEjyMZHvd3OH2Daee1CUG1e6dAIgU5OuiQmQIhE6TdNUgZiCh7oX5sZAhoBeLtrz2Rf9PLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDCg8m%2BCCOaK7QNYWJyrcA1jHXWLmnakJ%2BCW9s%2BG0opx2qPeA3zAt6sONoUVgUbj71IUx%2BnYQJs%2FhzeFwf8yRnL6GE70v%2BFKi%2BeVIjld%2Bjleuyo941Mw8%2B3UEpF9W0B6en%2FZWyJhB08KUlKm0lrrv63YzICyh0%2BseaZRt3Gvk2BZUXpWz1TlOWyBYOuP6qMoPFVyyxex0YEqn74vIAajdL3JJynMtsk9kMWnurC1tUPxXGDSdRhtXB5jrx6aDp9PrbcD8BubiUWX4q%2FRFRHHhFm%2FkYo1RXdqs3x405Ss%2Fo1ULe1zspbQqPM%2BqCoeTFP5ZPuOU22asnEEorMDplnbyZtSAYgr6wMdAJ%2BPWTun5odmsyjeV1gcA0bQwJk1VWyD818gxTvZbtEug2wRuBbiJv3fNDyoxldMt6P8M4GCbkVyLw5ixUcsxznSkckcj%2FPm1Q%2B9QtM%2BQOJiqAQ%2FJ%2F%2FvZeqPk44Hhf%2Bmg26I5FDTYCQTZ3LQ5FhXDaIN31kq23E%2BB%2BxxeSyeOANQyjNPn2rI%2BJayOo4v3qz%2Fyc4Ror2V6rBm%2B3btYpJZfMcnMHEBZ4Msv%2BJy7EvB%2ButZVoGfknzh%2BLzROFQ8CotWYWZgQivSEYpTAAmgkF9%2F%2FcRSCdW010myPtRrRcm6a%2F5PC1HAIMN%2BezM8GOqUBFwsORA3eoKLE159hrxR6I2U6quLas9I6wLa3%2B0ofozYIv7M1pQu36Evfh%2BPTbiS3g%2F2bR6sk1H6ynKp3zXqnDNm6X54O8%2BHQr4lcpkarZr4S1dI9KUuglrqMo4mdrDmB8wo9CwEdSzeaaMTyrVmOqtHZDE1%2FjqRTPdZK5gAMTaHAMHlPK%2FHfXivPN1DNoSK6wGvN2xkKWSH6PrxR8DXwFAojtFjm&X-Amz-Signature=6318a99c886017b5d9eb5ec58b792dca12dfddc024757ab1f95619e50b127f55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

