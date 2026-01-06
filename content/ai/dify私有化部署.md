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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFCIEBOZ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4r7n6ofcoxc3sbzu0hFzm%2BrLmacmGYT0Em7RwYPOlAiEApD7HISmtuXKK9ac2Ux7eTicRCRbt8Z00%2FZ1tm%2FveXo4q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDFxRoweR1KEY0BgjkircA2aasayji5yGOuGEvOZ%2FXxRt3GRdTOJRKA0tOHm2UPcrKdktd1UPXSlRvfyhvGKRj6Z%2FJn%2BJZQ8h%2B5H%2F7QQ3MtAoPYZ7jHa5kWJiAjK1j6ujx2vLBdncPXKkqMGbfTcJD9RyBVZYrHlJU%2FewogV%2FahGIR3%2B9njg3gmv1GqLEk2mQUaizswvwbjiEl7Qqf3qBa9qiOfW4A9mfVepNQPjbf3iBUf49Jsovy1GyF3dbKyiku5B1m%2BdB66MGLXdYENZxuxF%2FwlzD0Ov54015SsQ04CXVHih5w37HwSp%2FpyndmpERVnQ%2BWxzhcWt55Uw99IoZSNQQa6UWBF9sQb7SfIVdAxVDmZ89YOAJZKFdq0bB4tgFJ3ALbrcflssjfSQC2u%2FFStYJTOmb43U2v1MJ%2Bh4AWRLpSRlSeXlxYXkB29cIbSHpGKvHMoUihyd8TrbNJIC6OtfN9um71dzBXn2RkpGx4b1MlmOnoVMjbUo2Xnxhux4gXcmF3q4VL9KVfbkLhnT2HSDZy0smZK1QPh%2B%2BD0YfgAJ1Res0EoPCr1pRhSYP72Dih3Fyz32oXsbuzeLlMbp5db%2Bo0vozRLm5fxVRvtweUAZUBhU8HoGWZd%2FQoUIw0hgQD6gTeIJU3CASfDVmMKrk8coGOqUBtU2cQTlLryPMQXj%2BHrHhSMpw%2B8hVfay6J73IEaWR79vI%2BJ0m3zFbDQk09jh%2FhA7hvakCKe3M1bHQ5eyXWBorCCKMZGLyIk0CBdasvEpQwfgkAbvE%2ByI6tOGklrgggo4co609Rzn%2Bg1CNP2PLv0jVnaO3Sm4nehfq9ulEVtpWqkytnDSc87sJwGW2LahJg4zvLyqGMvgzmteaNzCTL%2BOMEFehe%2FNd&X-Amz-Signature=be42a556316bbd4b6b0af34ca6b256b37f8c3db0ef99481765a2fa31380ae948&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFCIEBOZ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4r7n6ofcoxc3sbzu0hFzm%2BrLmacmGYT0Em7RwYPOlAiEApD7HISmtuXKK9ac2Ux7eTicRCRbt8Z00%2FZ1tm%2FveXo4q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDFxRoweR1KEY0BgjkircA2aasayji5yGOuGEvOZ%2FXxRt3GRdTOJRKA0tOHm2UPcrKdktd1UPXSlRvfyhvGKRj6Z%2FJn%2BJZQ8h%2B5H%2F7QQ3MtAoPYZ7jHa5kWJiAjK1j6ujx2vLBdncPXKkqMGbfTcJD9RyBVZYrHlJU%2FewogV%2FahGIR3%2B9njg3gmv1GqLEk2mQUaizswvwbjiEl7Qqf3qBa9qiOfW4A9mfVepNQPjbf3iBUf49Jsovy1GyF3dbKyiku5B1m%2BdB66MGLXdYENZxuxF%2FwlzD0Ov54015SsQ04CXVHih5w37HwSp%2FpyndmpERVnQ%2BWxzhcWt55Uw99IoZSNQQa6UWBF9sQb7SfIVdAxVDmZ89YOAJZKFdq0bB4tgFJ3ALbrcflssjfSQC2u%2FFStYJTOmb43U2v1MJ%2Bh4AWRLpSRlSeXlxYXkB29cIbSHpGKvHMoUihyd8TrbNJIC6OtfN9um71dzBXn2RkpGx4b1MlmOnoVMjbUo2Xnxhux4gXcmF3q4VL9KVfbkLhnT2HSDZy0smZK1QPh%2B%2BD0YfgAJ1Res0EoPCr1pRhSYP72Dih3Fyz32oXsbuzeLlMbp5db%2Bo0vozRLm5fxVRvtweUAZUBhU8HoGWZd%2FQoUIw0hgQD6gTeIJU3CASfDVmMKrk8coGOqUBtU2cQTlLryPMQXj%2BHrHhSMpw%2B8hVfay6J73IEaWR79vI%2BJ0m3zFbDQk09jh%2FhA7hvakCKe3M1bHQ5eyXWBorCCKMZGLyIk0CBdasvEpQwfgkAbvE%2ByI6tOGklrgggo4co609Rzn%2Bg1CNP2PLv0jVnaO3Sm4nehfq9ulEVtpWqkytnDSc87sJwGW2LahJg4zvLyqGMvgzmteaNzCTL%2BOMEFehe%2FNd&X-Amz-Signature=a470e121c8f727f8e1b565a967784a8deb38367992e56c87605755a6351adcde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFCIEBOZ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4r7n6ofcoxc3sbzu0hFzm%2BrLmacmGYT0Em7RwYPOlAiEApD7HISmtuXKK9ac2Ux7eTicRCRbt8Z00%2FZ1tm%2FveXo4q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDFxRoweR1KEY0BgjkircA2aasayji5yGOuGEvOZ%2FXxRt3GRdTOJRKA0tOHm2UPcrKdktd1UPXSlRvfyhvGKRj6Z%2FJn%2BJZQ8h%2B5H%2F7QQ3MtAoPYZ7jHa5kWJiAjK1j6ujx2vLBdncPXKkqMGbfTcJD9RyBVZYrHlJU%2FewogV%2FahGIR3%2B9njg3gmv1GqLEk2mQUaizswvwbjiEl7Qqf3qBa9qiOfW4A9mfVepNQPjbf3iBUf49Jsovy1GyF3dbKyiku5B1m%2BdB66MGLXdYENZxuxF%2FwlzD0Ov54015SsQ04CXVHih5w37HwSp%2FpyndmpERVnQ%2BWxzhcWt55Uw99IoZSNQQa6UWBF9sQb7SfIVdAxVDmZ89YOAJZKFdq0bB4tgFJ3ALbrcflssjfSQC2u%2FFStYJTOmb43U2v1MJ%2Bh4AWRLpSRlSeXlxYXkB29cIbSHpGKvHMoUihyd8TrbNJIC6OtfN9um71dzBXn2RkpGx4b1MlmOnoVMjbUo2Xnxhux4gXcmF3q4VL9KVfbkLhnT2HSDZy0smZK1QPh%2B%2BD0YfgAJ1Res0EoPCr1pRhSYP72Dih3Fyz32oXsbuzeLlMbp5db%2Bo0vozRLm5fxVRvtweUAZUBhU8HoGWZd%2FQoUIw0hgQD6gTeIJU3CASfDVmMKrk8coGOqUBtU2cQTlLryPMQXj%2BHrHhSMpw%2B8hVfay6J73IEaWR79vI%2BJ0m3zFbDQk09jh%2FhA7hvakCKe3M1bHQ5eyXWBorCCKMZGLyIk0CBdasvEpQwfgkAbvE%2ByI6tOGklrgggo4co609Rzn%2Bg1CNP2PLv0jVnaO3Sm4nehfq9ulEVtpWqkytnDSc87sJwGW2LahJg4zvLyqGMvgzmteaNzCTL%2BOMEFehe%2FNd&X-Amz-Signature=38509c41dc2e823ec630f0dc069d17ce648f5a0b4423eaf5d15893551509f666&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFCIEBOZ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4r7n6ofcoxc3sbzu0hFzm%2BrLmacmGYT0Em7RwYPOlAiEApD7HISmtuXKK9ac2Ux7eTicRCRbt8Z00%2FZ1tm%2FveXo4q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDFxRoweR1KEY0BgjkircA2aasayji5yGOuGEvOZ%2FXxRt3GRdTOJRKA0tOHm2UPcrKdktd1UPXSlRvfyhvGKRj6Z%2FJn%2BJZQ8h%2B5H%2F7QQ3MtAoPYZ7jHa5kWJiAjK1j6ujx2vLBdncPXKkqMGbfTcJD9RyBVZYrHlJU%2FewogV%2FahGIR3%2B9njg3gmv1GqLEk2mQUaizswvwbjiEl7Qqf3qBa9qiOfW4A9mfVepNQPjbf3iBUf49Jsovy1GyF3dbKyiku5B1m%2BdB66MGLXdYENZxuxF%2FwlzD0Ov54015SsQ04CXVHih5w37HwSp%2FpyndmpERVnQ%2BWxzhcWt55Uw99IoZSNQQa6UWBF9sQb7SfIVdAxVDmZ89YOAJZKFdq0bB4tgFJ3ALbrcflssjfSQC2u%2FFStYJTOmb43U2v1MJ%2Bh4AWRLpSRlSeXlxYXkB29cIbSHpGKvHMoUihyd8TrbNJIC6OtfN9um71dzBXn2RkpGx4b1MlmOnoVMjbUo2Xnxhux4gXcmF3q4VL9KVfbkLhnT2HSDZy0smZK1QPh%2B%2BD0YfgAJ1Res0EoPCr1pRhSYP72Dih3Fyz32oXsbuzeLlMbp5db%2Bo0vozRLm5fxVRvtweUAZUBhU8HoGWZd%2FQoUIw0hgQD6gTeIJU3CASfDVmMKrk8coGOqUBtU2cQTlLryPMQXj%2BHrHhSMpw%2B8hVfay6J73IEaWR79vI%2BJ0m3zFbDQk09jh%2FhA7hvakCKe3M1bHQ5eyXWBorCCKMZGLyIk0CBdasvEpQwfgkAbvE%2ByI6tOGklrgggo4co609Rzn%2Bg1CNP2PLv0jVnaO3Sm4nehfq9ulEVtpWqkytnDSc87sJwGW2LahJg4zvLyqGMvgzmteaNzCTL%2BOMEFehe%2FNd&X-Amz-Signature=e3d51c3d4356a59b13977969cf500a2a82eed3ebbea770ed543fc603f03666fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFCIEBOZ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4r7n6ofcoxc3sbzu0hFzm%2BrLmacmGYT0Em7RwYPOlAiEApD7HISmtuXKK9ac2Ux7eTicRCRbt8Z00%2FZ1tm%2FveXo4q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDFxRoweR1KEY0BgjkircA2aasayji5yGOuGEvOZ%2FXxRt3GRdTOJRKA0tOHm2UPcrKdktd1UPXSlRvfyhvGKRj6Z%2FJn%2BJZQ8h%2B5H%2F7QQ3MtAoPYZ7jHa5kWJiAjK1j6ujx2vLBdncPXKkqMGbfTcJD9RyBVZYrHlJU%2FewogV%2FahGIR3%2B9njg3gmv1GqLEk2mQUaizswvwbjiEl7Qqf3qBa9qiOfW4A9mfVepNQPjbf3iBUf49Jsovy1GyF3dbKyiku5B1m%2BdB66MGLXdYENZxuxF%2FwlzD0Ov54015SsQ04CXVHih5w37HwSp%2FpyndmpERVnQ%2BWxzhcWt55Uw99IoZSNQQa6UWBF9sQb7SfIVdAxVDmZ89YOAJZKFdq0bB4tgFJ3ALbrcflssjfSQC2u%2FFStYJTOmb43U2v1MJ%2Bh4AWRLpSRlSeXlxYXkB29cIbSHpGKvHMoUihyd8TrbNJIC6OtfN9um71dzBXn2RkpGx4b1MlmOnoVMjbUo2Xnxhux4gXcmF3q4VL9KVfbkLhnT2HSDZy0smZK1QPh%2B%2BD0YfgAJ1Res0EoPCr1pRhSYP72Dih3Fyz32oXsbuzeLlMbp5db%2Bo0vozRLm5fxVRvtweUAZUBhU8HoGWZd%2FQoUIw0hgQD6gTeIJU3CASfDVmMKrk8coGOqUBtU2cQTlLryPMQXj%2BHrHhSMpw%2B8hVfay6J73IEaWR79vI%2BJ0m3zFbDQk09jh%2FhA7hvakCKe3M1bHQ5eyXWBorCCKMZGLyIk0CBdasvEpQwfgkAbvE%2ByI6tOGklrgggo4co609Rzn%2Bg1CNP2PLv0jVnaO3Sm4nehfq9ulEVtpWqkytnDSc87sJwGW2LahJg4zvLyqGMvgzmteaNzCTL%2BOMEFehe%2FNd&X-Amz-Signature=1f8ea9f5ba8434a14bfc73c6562b94decdb4ecbfdd3cdcefb4c70856843babef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFCIEBOZ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4r7n6ofcoxc3sbzu0hFzm%2BrLmacmGYT0Em7RwYPOlAiEApD7HISmtuXKK9ac2Ux7eTicRCRbt8Z00%2FZ1tm%2FveXo4q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDFxRoweR1KEY0BgjkircA2aasayji5yGOuGEvOZ%2FXxRt3GRdTOJRKA0tOHm2UPcrKdktd1UPXSlRvfyhvGKRj6Z%2FJn%2BJZQ8h%2B5H%2F7QQ3MtAoPYZ7jHa5kWJiAjK1j6ujx2vLBdncPXKkqMGbfTcJD9RyBVZYrHlJU%2FewogV%2FahGIR3%2B9njg3gmv1GqLEk2mQUaizswvwbjiEl7Qqf3qBa9qiOfW4A9mfVepNQPjbf3iBUf49Jsovy1GyF3dbKyiku5B1m%2BdB66MGLXdYENZxuxF%2FwlzD0Ov54015SsQ04CXVHih5w37HwSp%2FpyndmpERVnQ%2BWxzhcWt55Uw99IoZSNQQa6UWBF9sQb7SfIVdAxVDmZ89YOAJZKFdq0bB4tgFJ3ALbrcflssjfSQC2u%2FFStYJTOmb43U2v1MJ%2Bh4AWRLpSRlSeXlxYXkB29cIbSHpGKvHMoUihyd8TrbNJIC6OtfN9um71dzBXn2RkpGx4b1MlmOnoVMjbUo2Xnxhux4gXcmF3q4VL9KVfbkLhnT2HSDZy0smZK1QPh%2B%2BD0YfgAJ1Res0EoPCr1pRhSYP72Dih3Fyz32oXsbuzeLlMbp5db%2Bo0vozRLm5fxVRvtweUAZUBhU8HoGWZd%2FQoUIw0hgQD6gTeIJU3CASfDVmMKrk8coGOqUBtU2cQTlLryPMQXj%2BHrHhSMpw%2B8hVfay6J73IEaWR79vI%2BJ0m3zFbDQk09jh%2FhA7hvakCKe3M1bHQ5eyXWBorCCKMZGLyIk0CBdasvEpQwfgkAbvE%2ByI6tOGklrgggo4co609Rzn%2Bg1CNP2PLv0jVnaO3Sm4nehfq9ulEVtpWqkytnDSc87sJwGW2LahJg4zvLyqGMvgzmteaNzCTL%2BOMEFehe%2FNd&X-Amz-Signature=8bc8bba9facc47aca4be815dd85a2ff78c28246a65296435abd4f973c309e90d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFCIEBOZ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4r7n6ofcoxc3sbzu0hFzm%2BrLmacmGYT0Em7RwYPOlAiEApD7HISmtuXKK9ac2Ux7eTicRCRbt8Z00%2FZ1tm%2FveXo4q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDFxRoweR1KEY0BgjkircA2aasayji5yGOuGEvOZ%2FXxRt3GRdTOJRKA0tOHm2UPcrKdktd1UPXSlRvfyhvGKRj6Z%2FJn%2BJZQ8h%2B5H%2F7QQ3MtAoPYZ7jHa5kWJiAjK1j6ujx2vLBdncPXKkqMGbfTcJD9RyBVZYrHlJU%2FewogV%2FahGIR3%2B9njg3gmv1GqLEk2mQUaizswvwbjiEl7Qqf3qBa9qiOfW4A9mfVepNQPjbf3iBUf49Jsovy1GyF3dbKyiku5B1m%2BdB66MGLXdYENZxuxF%2FwlzD0Ov54015SsQ04CXVHih5w37HwSp%2FpyndmpERVnQ%2BWxzhcWt55Uw99IoZSNQQa6UWBF9sQb7SfIVdAxVDmZ89YOAJZKFdq0bB4tgFJ3ALbrcflssjfSQC2u%2FFStYJTOmb43U2v1MJ%2Bh4AWRLpSRlSeXlxYXkB29cIbSHpGKvHMoUihyd8TrbNJIC6OtfN9um71dzBXn2RkpGx4b1MlmOnoVMjbUo2Xnxhux4gXcmF3q4VL9KVfbkLhnT2HSDZy0smZK1QPh%2B%2BD0YfgAJ1Res0EoPCr1pRhSYP72Dih3Fyz32oXsbuzeLlMbp5db%2Bo0vozRLm5fxVRvtweUAZUBhU8HoGWZd%2FQoUIw0hgQD6gTeIJU3CASfDVmMKrk8coGOqUBtU2cQTlLryPMQXj%2BHrHhSMpw%2B8hVfay6J73IEaWR79vI%2BJ0m3zFbDQk09jh%2FhA7hvakCKe3M1bHQ5eyXWBorCCKMZGLyIk0CBdasvEpQwfgkAbvE%2ByI6tOGklrgggo4co609Rzn%2Bg1CNP2PLv0jVnaO3Sm4nehfq9ulEVtpWqkytnDSc87sJwGW2LahJg4zvLyqGMvgzmteaNzCTL%2BOMEFehe%2FNd&X-Amz-Signature=0dc20fa24da7a33155bb977787844cbf333057ccff4030a33491ae5edea728a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFCIEBOZ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4r7n6ofcoxc3sbzu0hFzm%2BrLmacmGYT0Em7RwYPOlAiEApD7HISmtuXKK9ac2Ux7eTicRCRbt8Z00%2FZ1tm%2FveXo4q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDFxRoweR1KEY0BgjkircA2aasayji5yGOuGEvOZ%2FXxRt3GRdTOJRKA0tOHm2UPcrKdktd1UPXSlRvfyhvGKRj6Z%2FJn%2BJZQ8h%2B5H%2F7QQ3MtAoPYZ7jHa5kWJiAjK1j6ujx2vLBdncPXKkqMGbfTcJD9RyBVZYrHlJU%2FewogV%2FahGIR3%2B9njg3gmv1GqLEk2mQUaizswvwbjiEl7Qqf3qBa9qiOfW4A9mfVepNQPjbf3iBUf49Jsovy1GyF3dbKyiku5B1m%2BdB66MGLXdYENZxuxF%2FwlzD0Ov54015SsQ04CXVHih5w37HwSp%2FpyndmpERVnQ%2BWxzhcWt55Uw99IoZSNQQa6UWBF9sQb7SfIVdAxVDmZ89YOAJZKFdq0bB4tgFJ3ALbrcflssjfSQC2u%2FFStYJTOmb43U2v1MJ%2Bh4AWRLpSRlSeXlxYXkB29cIbSHpGKvHMoUihyd8TrbNJIC6OtfN9um71dzBXn2RkpGx4b1MlmOnoVMjbUo2Xnxhux4gXcmF3q4VL9KVfbkLhnT2HSDZy0smZK1QPh%2B%2BD0YfgAJ1Res0EoPCr1pRhSYP72Dih3Fyz32oXsbuzeLlMbp5db%2Bo0vozRLm5fxVRvtweUAZUBhU8HoGWZd%2FQoUIw0hgQD6gTeIJU3CASfDVmMKrk8coGOqUBtU2cQTlLryPMQXj%2BHrHhSMpw%2B8hVfay6J73IEaWR79vI%2BJ0m3zFbDQk09jh%2FhA7hvakCKe3M1bHQ5eyXWBorCCKMZGLyIk0CBdasvEpQwfgkAbvE%2ByI6tOGklrgggo4co609Rzn%2Bg1CNP2PLv0jVnaO3Sm4nehfq9ulEVtpWqkytnDSc87sJwGW2LahJg4zvLyqGMvgzmteaNzCTL%2BOMEFehe%2FNd&X-Amz-Signature=783cf3bab10288354963aed3bde1f94ddabf2847b19231227c28e63c8c80da31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFCIEBOZ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4r7n6ofcoxc3sbzu0hFzm%2BrLmacmGYT0Em7RwYPOlAiEApD7HISmtuXKK9ac2Ux7eTicRCRbt8Z00%2FZ1tm%2FveXo4q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDFxRoweR1KEY0BgjkircA2aasayji5yGOuGEvOZ%2FXxRt3GRdTOJRKA0tOHm2UPcrKdktd1UPXSlRvfyhvGKRj6Z%2FJn%2BJZQ8h%2B5H%2F7QQ3MtAoPYZ7jHa5kWJiAjK1j6ujx2vLBdncPXKkqMGbfTcJD9RyBVZYrHlJU%2FewogV%2FahGIR3%2B9njg3gmv1GqLEk2mQUaizswvwbjiEl7Qqf3qBa9qiOfW4A9mfVepNQPjbf3iBUf49Jsovy1GyF3dbKyiku5B1m%2BdB66MGLXdYENZxuxF%2FwlzD0Ov54015SsQ04CXVHih5w37HwSp%2FpyndmpERVnQ%2BWxzhcWt55Uw99IoZSNQQa6UWBF9sQb7SfIVdAxVDmZ89YOAJZKFdq0bB4tgFJ3ALbrcflssjfSQC2u%2FFStYJTOmb43U2v1MJ%2Bh4AWRLpSRlSeXlxYXkB29cIbSHpGKvHMoUihyd8TrbNJIC6OtfN9um71dzBXn2RkpGx4b1MlmOnoVMjbUo2Xnxhux4gXcmF3q4VL9KVfbkLhnT2HSDZy0smZK1QPh%2B%2BD0YfgAJ1Res0EoPCr1pRhSYP72Dih3Fyz32oXsbuzeLlMbp5db%2Bo0vozRLm5fxVRvtweUAZUBhU8HoGWZd%2FQoUIw0hgQD6gTeIJU3CASfDVmMKrk8coGOqUBtU2cQTlLryPMQXj%2BHrHhSMpw%2B8hVfay6J73IEaWR79vI%2BJ0m3zFbDQk09jh%2FhA7hvakCKe3M1bHQ5eyXWBorCCKMZGLyIk0CBdasvEpQwfgkAbvE%2ByI6tOGklrgggo4co609Rzn%2Bg1CNP2PLv0jVnaO3Sm4nehfq9ulEVtpWqkytnDSc87sJwGW2LahJg4zvLyqGMvgzmteaNzCTL%2BOMEFehe%2FNd&X-Amz-Signature=ffd658e2d216e46327f71fa4048039a854ca503f1c27d9029651a38d774afca7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFCIEBOZ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDU4r7n6ofcoxc3sbzu0hFzm%2BrLmacmGYT0Em7RwYPOlAiEApD7HISmtuXKK9ac2Ux7eTicRCRbt8Z00%2FZ1tm%2FveXo4q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDFxRoweR1KEY0BgjkircA2aasayji5yGOuGEvOZ%2FXxRt3GRdTOJRKA0tOHm2UPcrKdktd1UPXSlRvfyhvGKRj6Z%2FJn%2BJZQ8h%2B5H%2F7QQ3MtAoPYZ7jHa5kWJiAjK1j6ujx2vLBdncPXKkqMGbfTcJD9RyBVZYrHlJU%2FewogV%2FahGIR3%2B9njg3gmv1GqLEk2mQUaizswvwbjiEl7Qqf3qBa9qiOfW4A9mfVepNQPjbf3iBUf49Jsovy1GyF3dbKyiku5B1m%2BdB66MGLXdYENZxuxF%2FwlzD0Ov54015SsQ04CXVHih5w37HwSp%2FpyndmpERVnQ%2BWxzhcWt55Uw99IoZSNQQa6UWBF9sQb7SfIVdAxVDmZ89YOAJZKFdq0bB4tgFJ3ALbrcflssjfSQC2u%2FFStYJTOmb43U2v1MJ%2Bh4AWRLpSRlSeXlxYXkB29cIbSHpGKvHMoUihyd8TrbNJIC6OtfN9um71dzBXn2RkpGx4b1MlmOnoVMjbUo2Xnxhux4gXcmF3q4VL9KVfbkLhnT2HSDZy0smZK1QPh%2B%2BD0YfgAJ1Res0EoPCr1pRhSYP72Dih3Fyz32oXsbuzeLlMbp5db%2Bo0vozRLm5fxVRvtweUAZUBhU8HoGWZd%2FQoUIw0hgQD6gTeIJU3CASfDVmMKrk8coGOqUBtU2cQTlLryPMQXj%2BHrHhSMpw%2B8hVfay6J73IEaWR79vI%2BJ0m3zFbDQk09jh%2FhA7hvakCKe3M1bHQ5eyXWBorCCKMZGLyIk0CBdasvEpQwfgkAbvE%2ByI6tOGklrgggo4co609Rzn%2Bg1CNP2PLv0jVnaO3Sm4nehfq9ulEVtpWqkytnDSc87sJwGW2LahJg4zvLyqGMvgzmteaNzCTL%2BOMEFehe%2FNd&X-Amz-Signature=970ea73e61eb784076b94f78bb5deba401bffa8441f854b0bdb299772d047e46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

