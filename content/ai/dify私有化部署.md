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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVTTFVGD%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3izy9gzabstd1p5E7QTFaOnvSw2caU76g6mLbUtT94AIhAPBA2oq5J3%2B4W1l6TsC%2FeABpYbW%2Bx8ICarCZH85RDUchKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxacumG5GB0adfNozsq3AM8lqbw3YQN8UkNShgxwRCBB3wRnQrax%2Fu5tb%2BKXfMwVmkWR7j7FqegfwhvIvhR4IJtMQlHFSJzU8TxcOtZh%2FNWPCDJm2WJBHWKtm3%2Bv%2FpwE7p04cpNCr%2FPmfE2cRyp5RFu2%2Bje%2Fs2Q5AjZxtWz%2B0vaCne00VIHMb76VGXptBODq1zjnjbY4rqaks%2Fj1oxzh3I9R20H%2F8dOHJX1Z39cEl1yax5VVWzLgdCs%2BJbHoA0mCQ6%2B%2B98SdO2JdENmT9Q0SMteqU2vGXqh9IlKUUimCcIs0HD57okO0mcsJlouKBQS1ByeMvTMlRCQdoeBn8I0BJAR%2FjpHDEQn7kB8jaMD9u%2BmeHILzeZGeTZnSUj4drG3s1szS4oM4ey2OF5oTrU4Pg3f9NPfczMAbn8ZFxw0Yj0NwIo8U6S083AK0DK9ng2b3jCh%2BFsmlQc5d7ft0o8MgI3M0Va4tKK6HbbvB%2FQkdcC6g1CENE0ftiE%2Be5jx1p3nroq4uC0xRBPgdb6zVu5l%2F5u9kxLYxS1u2iK4Uv3cMMgqPFx0DRpsSWPuzqeebc%2B62yxNz0lJfOz9JMK98knwz%2FYOHFKPnvKilmTIIajfYhMnV%2BBxvsnTXfKe%2BeC2lLpGruEJqtiN5fKEDlyVtjDR4OTIBjqkAciQp35lxy9a6WLxe7hDXCOMpiQps8rP1s9vvOosFwHfAb0vHCWYYZjn7cSRxOdSAEk4Pl87xSHDwzlh1tlUGX1Q0c1CtLhgCau%2FwtMSqrZtGB8OC%2Bksd5orv3MOoyxneyu2p94NOzp8K34I0cPvXAqOrojtqkBXcfASnYmkpCpMttS4kwiFyNnR9fs%2FawjLqcjtGn4w7ZWsE5zOc3ozQO2o3Oke&X-Amz-Signature=78622a86e2283f29cfdbbc66d28f92c26774eb9e93e10d115c6da72bf7f9e756&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVTTFVGD%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3izy9gzabstd1p5E7QTFaOnvSw2caU76g6mLbUtT94AIhAPBA2oq5J3%2B4W1l6TsC%2FeABpYbW%2Bx8ICarCZH85RDUchKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxacumG5GB0adfNozsq3AM8lqbw3YQN8UkNShgxwRCBB3wRnQrax%2Fu5tb%2BKXfMwVmkWR7j7FqegfwhvIvhR4IJtMQlHFSJzU8TxcOtZh%2FNWPCDJm2WJBHWKtm3%2Bv%2FpwE7p04cpNCr%2FPmfE2cRyp5RFu2%2Bje%2Fs2Q5AjZxtWz%2B0vaCne00VIHMb76VGXptBODq1zjnjbY4rqaks%2Fj1oxzh3I9R20H%2F8dOHJX1Z39cEl1yax5VVWzLgdCs%2BJbHoA0mCQ6%2B%2B98SdO2JdENmT9Q0SMteqU2vGXqh9IlKUUimCcIs0HD57okO0mcsJlouKBQS1ByeMvTMlRCQdoeBn8I0BJAR%2FjpHDEQn7kB8jaMD9u%2BmeHILzeZGeTZnSUj4drG3s1szS4oM4ey2OF5oTrU4Pg3f9NPfczMAbn8ZFxw0Yj0NwIo8U6S083AK0DK9ng2b3jCh%2BFsmlQc5d7ft0o8MgI3M0Va4tKK6HbbvB%2FQkdcC6g1CENE0ftiE%2Be5jx1p3nroq4uC0xRBPgdb6zVu5l%2F5u9kxLYxS1u2iK4Uv3cMMgqPFx0DRpsSWPuzqeebc%2B62yxNz0lJfOz9JMK98knwz%2FYOHFKPnvKilmTIIajfYhMnV%2BBxvsnTXfKe%2BeC2lLpGruEJqtiN5fKEDlyVtjDR4OTIBjqkAciQp35lxy9a6WLxe7hDXCOMpiQps8rP1s9vvOosFwHfAb0vHCWYYZjn7cSRxOdSAEk4Pl87xSHDwzlh1tlUGX1Q0c1CtLhgCau%2FwtMSqrZtGB8OC%2Bksd5orv3MOoyxneyu2p94NOzp8K34I0cPvXAqOrojtqkBXcfASnYmkpCpMttS4kwiFyNnR9fs%2FawjLqcjtGn4w7ZWsE5zOc3ozQO2o3Oke&X-Amz-Signature=c633996557e0426e6e284a7780fccd36d875298b31dfebbc53143c540eedc49c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVTTFVGD%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3izy9gzabstd1p5E7QTFaOnvSw2caU76g6mLbUtT94AIhAPBA2oq5J3%2B4W1l6TsC%2FeABpYbW%2Bx8ICarCZH85RDUchKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxacumG5GB0adfNozsq3AM8lqbw3YQN8UkNShgxwRCBB3wRnQrax%2Fu5tb%2BKXfMwVmkWR7j7FqegfwhvIvhR4IJtMQlHFSJzU8TxcOtZh%2FNWPCDJm2WJBHWKtm3%2Bv%2FpwE7p04cpNCr%2FPmfE2cRyp5RFu2%2Bje%2Fs2Q5AjZxtWz%2B0vaCne00VIHMb76VGXptBODq1zjnjbY4rqaks%2Fj1oxzh3I9R20H%2F8dOHJX1Z39cEl1yax5VVWzLgdCs%2BJbHoA0mCQ6%2B%2B98SdO2JdENmT9Q0SMteqU2vGXqh9IlKUUimCcIs0HD57okO0mcsJlouKBQS1ByeMvTMlRCQdoeBn8I0BJAR%2FjpHDEQn7kB8jaMD9u%2BmeHILzeZGeTZnSUj4drG3s1szS4oM4ey2OF5oTrU4Pg3f9NPfczMAbn8ZFxw0Yj0NwIo8U6S083AK0DK9ng2b3jCh%2BFsmlQc5d7ft0o8MgI3M0Va4tKK6HbbvB%2FQkdcC6g1CENE0ftiE%2Be5jx1p3nroq4uC0xRBPgdb6zVu5l%2F5u9kxLYxS1u2iK4Uv3cMMgqPFx0DRpsSWPuzqeebc%2B62yxNz0lJfOz9JMK98knwz%2FYOHFKPnvKilmTIIajfYhMnV%2BBxvsnTXfKe%2BeC2lLpGruEJqtiN5fKEDlyVtjDR4OTIBjqkAciQp35lxy9a6WLxe7hDXCOMpiQps8rP1s9vvOosFwHfAb0vHCWYYZjn7cSRxOdSAEk4Pl87xSHDwzlh1tlUGX1Q0c1CtLhgCau%2FwtMSqrZtGB8OC%2Bksd5orv3MOoyxneyu2p94NOzp8K34I0cPvXAqOrojtqkBXcfASnYmkpCpMttS4kwiFyNnR9fs%2FawjLqcjtGn4w7ZWsE5zOc3ozQO2o3Oke&X-Amz-Signature=40938747c3e95dd07e9ae4876f18970ed346462f58bbf32b9e21230619fb056c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVTTFVGD%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3izy9gzabstd1p5E7QTFaOnvSw2caU76g6mLbUtT94AIhAPBA2oq5J3%2B4W1l6TsC%2FeABpYbW%2Bx8ICarCZH85RDUchKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxacumG5GB0adfNozsq3AM8lqbw3YQN8UkNShgxwRCBB3wRnQrax%2Fu5tb%2BKXfMwVmkWR7j7FqegfwhvIvhR4IJtMQlHFSJzU8TxcOtZh%2FNWPCDJm2WJBHWKtm3%2Bv%2FpwE7p04cpNCr%2FPmfE2cRyp5RFu2%2Bje%2Fs2Q5AjZxtWz%2B0vaCne00VIHMb76VGXptBODq1zjnjbY4rqaks%2Fj1oxzh3I9R20H%2F8dOHJX1Z39cEl1yax5VVWzLgdCs%2BJbHoA0mCQ6%2B%2B98SdO2JdENmT9Q0SMteqU2vGXqh9IlKUUimCcIs0HD57okO0mcsJlouKBQS1ByeMvTMlRCQdoeBn8I0BJAR%2FjpHDEQn7kB8jaMD9u%2BmeHILzeZGeTZnSUj4drG3s1szS4oM4ey2OF5oTrU4Pg3f9NPfczMAbn8ZFxw0Yj0NwIo8U6S083AK0DK9ng2b3jCh%2BFsmlQc5d7ft0o8MgI3M0Va4tKK6HbbvB%2FQkdcC6g1CENE0ftiE%2Be5jx1p3nroq4uC0xRBPgdb6zVu5l%2F5u9kxLYxS1u2iK4Uv3cMMgqPFx0DRpsSWPuzqeebc%2B62yxNz0lJfOz9JMK98knwz%2FYOHFKPnvKilmTIIajfYhMnV%2BBxvsnTXfKe%2BeC2lLpGruEJqtiN5fKEDlyVtjDR4OTIBjqkAciQp35lxy9a6WLxe7hDXCOMpiQps8rP1s9vvOosFwHfAb0vHCWYYZjn7cSRxOdSAEk4Pl87xSHDwzlh1tlUGX1Q0c1CtLhgCau%2FwtMSqrZtGB8OC%2Bksd5orv3MOoyxneyu2p94NOzp8K34I0cPvXAqOrojtqkBXcfASnYmkpCpMttS4kwiFyNnR9fs%2FawjLqcjtGn4w7ZWsE5zOc3ozQO2o3Oke&X-Amz-Signature=59e1db68bbde914855af2c710e0f9a191ef64b6d8848f02e0e5a186f67c45157&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVTTFVGD%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3izy9gzabstd1p5E7QTFaOnvSw2caU76g6mLbUtT94AIhAPBA2oq5J3%2B4W1l6TsC%2FeABpYbW%2Bx8ICarCZH85RDUchKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxacumG5GB0adfNozsq3AM8lqbw3YQN8UkNShgxwRCBB3wRnQrax%2Fu5tb%2BKXfMwVmkWR7j7FqegfwhvIvhR4IJtMQlHFSJzU8TxcOtZh%2FNWPCDJm2WJBHWKtm3%2Bv%2FpwE7p04cpNCr%2FPmfE2cRyp5RFu2%2Bje%2Fs2Q5AjZxtWz%2B0vaCne00VIHMb76VGXptBODq1zjnjbY4rqaks%2Fj1oxzh3I9R20H%2F8dOHJX1Z39cEl1yax5VVWzLgdCs%2BJbHoA0mCQ6%2B%2B98SdO2JdENmT9Q0SMteqU2vGXqh9IlKUUimCcIs0HD57okO0mcsJlouKBQS1ByeMvTMlRCQdoeBn8I0BJAR%2FjpHDEQn7kB8jaMD9u%2BmeHILzeZGeTZnSUj4drG3s1szS4oM4ey2OF5oTrU4Pg3f9NPfczMAbn8ZFxw0Yj0NwIo8U6S083AK0DK9ng2b3jCh%2BFsmlQc5d7ft0o8MgI3M0Va4tKK6HbbvB%2FQkdcC6g1CENE0ftiE%2Be5jx1p3nroq4uC0xRBPgdb6zVu5l%2F5u9kxLYxS1u2iK4Uv3cMMgqPFx0DRpsSWPuzqeebc%2B62yxNz0lJfOz9JMK98knwz%2FYOHFKPnvKilmTIIajfYhMnV%2BBxvsnTXfKe%2BeC2lLpGruEJqtiN5fKEDlyVtjDR4OTIBjqkAciQp35lxy9a6WLxe7hDXCOMpiQps8rP1s9vvOosFwHfAb0vHCWYYZjn7cSRxOdSAEk4Pl87xSHDwzlh1tlUGX1Q0c1CtLhgCau%2FwtMSqrZtGB8OC%2Bksd5orv3MOoyxneyu2p94NOzp8K34I0cPvXAqOrojtqkBXcfASnYmkpCpMttS4kwiFyNnR9fs%2FawjLqcjtGn4w7ZWsE5zOc3ozQO2o3Oke&X-Amz-Signature=7beda3e6808bba0380d21d7fd58fcf8444a2e2511f29549f26db3b79b261d3be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVTTFVGD%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3izy9gzabstd1p5E7QTFaOnvSw2caU76g6mLbUtT94AIhAPBA2oq5J3%2B4W1l6TsC%2FeABpYbW%2Bx8ICarCZH85RDUchKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxacumG5GB0adfNozsq3AM8lqbw3YQN8UkNShgxwRCBB3wRnQrax%2Fu5tb%2BKXfMwVmkWR7j7FqegfwhvIvhR4IJtMQlHFSJzU8TxcOtZh%2FNWPCDJm2WJBHWKtm3%2Bv%2FpwE7p04cpNCr%2FPmfE2cRyp5RFu2%2Bje%2Fs2Q5AjZxtWz%2B0vaCne00VIHMb76VGXptBODq1zjnjbY4rqaks%2Fj1oxzh3I9R20H%2F8dOHJX1Z39cEl1yax5VVWzLgdCs%2BJbHoA0mCQ6%2B%2B98SdO2JdENmT9Q0SMteqU2vGXqh9IlKUUimCcIs0HD57okO0mcsJlouKBQS1ByeMvTMlRCQdoeBn8I0BJAR%2FjpHDEQn7kB8jaMD9u%2BmeHILzeZGeTZnSUj4drG3s1szS4oM4ey2OF5oTrU4Pg3f9NPfczMAbn8ZFxw0Yj0NwIo8U6S083AK0DK9ng2b3jCh%2BFsmlQc5d7ft0o8MgI3M0Va4tKK6HbbvB%2FQkdcC6g1CENE0ftiE%2Be5jx1p3nroq4uC0xRBPgdb6zVu5l%2F5u9kxLYxS1u2iK4Uv3cMMgqPFx0DRpsSWPuzqeebc%2B62yxNz0lJfOz9JMK98knwz%2FYOHFKPnvKilmTIIajfYhMnV%2BBxvsnTXfKe%2BeC2lLpGruEJqtiN5fKEDlyVtjDR4OTIBjqkAciQp35lxy9a6WLxe7hDXCOMpiQps8rP1s9vvOosFwHfAb0vHCWYYZjn7cSRxOdSAEk4Pl87xSHDwzlh1tlUGX1Q0c1CtLhgCau%2FwtMSqrZtGB8OC%2Bksd5orv3MOoyxneyu2p94NOzp8K34I0cPvXAqOrojtqkBXcfASnYmkpCpMttS4kwiFyNnR9fs%2FawjLqcjtGn4w7ZWsE5zOc3ozQO2o3Oke&X-Amz-Signature=48ee49523e805c1510c98b09559475400d8b4493958e74b50031114580a79c18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVTTFVGD%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3izy9gzabstd1p5E7QTFaOnvSw2caU76g6mLbUtT94AIhAPBA2oq5J3%2B4W1l6TsC%2FeABpYbW%2Bx8ICarCZH85RDUchKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxacumG5GB0adfNozsq3AM8lqbw3YQN8UkNShgxwRCBB3wRnQrax%2Fu5tb%2BKXfMwVmkWR7j7FqegfwhvIvhR4IJtMQlHFSJzU8TxcOtZh%2FNWPCDJm2WJBHWKtm3%2Bv%2FpwE7p04cpNCr%2FPmfE2cRyp5RFu2%2Bje%2Fs2Q5AjZxtWz%2B0vaCne00VIHMb76VGXptBODq1zjnjbY4rqaks%2Fj1oxzh3I9R20H%2F8dOHJX1Z39cEl1yax5VVWzLgdCs%2BJbHoA0mCQ6%2B%2B98SdO2JdENmT9Q0SMteqU2vGXqh9IlKUUimCcIs0HD57okO0mcsJlouKBQS1ByeMvTMlRCQdoeBn8I0BJAR%2FjpHDEQn7kB8jaMD9u%2BmeHILzeZGeTZnSUj4drG3s1szS4oM4ey2OF5oTrU4Pg3f9NPfczMAbn8ZFxw0Yj0NwIo8U6S083AK0DK9ng2b3jCh%2BFsmlQc5d7ft0o8MgI3M0Va4tKK6HbbvB%2FQkdcC6g1CENE0ftiE%2Be5jx1p3nroq4uC0xRBPgdb6zVu5l%2F5u9kxLYxS1u2iK4Uv3cMMgqPFx0DRpsSWPuzqeebc%2B62yxNz0lJfOz9JMK98knwz%2FYOHFKPnvKilmTIIajfYhMnV%2BBxvsnTXfKe%2BeC2lLpGruEJqtiN5fKEDlyVtjDR4OTIBjqkAciQp35lxy9a6WLxe7hDXCOMpiQps8rP1s9vvOosFwHfAb0vHCWYYZjn7cSRxOdSAEk4Pl87xSHDwzlh1tlUGX1Q0c1CtLhgCau%2FwtMSqrZtGB8OC%2Bksd5orv3MOoyxneyu2p94NOzp8K34I0cPvXAqOrojtqkBXcfASnYmkpCpMttS4kwiFyNnR9fs%2FawjLqcjtGn4w7ZWsE5zOc3ozQO2o3Oke&X-Amz-Signature=78420df667c4b60f8ddaf0eca66793caf4e91a81ce737876b3edbe2819aee5ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVTTFVGD%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3izy9gzabstd1p5E7QTFaOnvSw2caU76g6mLbUtT94AIhAPBA2oq5J3%2B4W1l6TsC%2FeABpYbW%2Bx8ICarCZH85RDUchKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxacumG5GB0adfNozsq3AM8lqbw3YQN8UkNShgxwRCBB3wRnQrax%2Fu5tb%2BKXfMwVmkWR7j7FqegfwhvIvhR4IJtMQlHFSJzU8TxcOtZh%2FNWPCDJm2WJBHWKtm3%2Bv%2FpwE7p04cpNCr%2FPmfE2cRyp5RFu2%2Bje%2Fs2Q5AjZxtWz%2B0vaCne00VIHMb76VGXptBODq1zjnjbY4rqaks%2Fj1oxzh3I9R20H%2F8dOHJX1Z39cEl1yax5VVWzLgdCs%2BJbHoA0mCQ6%2B%2B98SdO2JdENmT9Q0SMteqU2vGXqh9IlKUUimCcIs0HD57okO0mcsJlouKBQS1ByeMvTMlRCQdoeBn8I0BJAR%2FjpHDEQn7kB8jaMD9u%2BmeHILzeZGeTZnSUj4drG3s1szS4oM4ey2OF5oTrU4Pg3f9NPfczMAbn8ZFxw0Yj0NwIo8U6S083AK0DK9ng2b3jCh%2BFsmlQc5d7ft0o8MgI3M0Va4tKK6HbbvB%2FQkdcC6g1CENE0ftiE%2Be5jx1p3nroq4uC0xRBPgdb6zVu5l%2F5u9kxLYxS1u2iK4Uv3cMMgqPFx0DRpsSWPuzqeebc%2B62yxNz0lJfOz9JMK98knwz%2FYOHFKPnvKilmTIIajfYhMnV%2BBxvsnTXfKe%2BeC2lLpGruEJqtiN5fKEDlyVtjDR4OTIBjqkAciQp35lxy9a6WLxe7hDXCOMpiQps8rP1s9vvOosFwHfAb0vHCWYYZjn7cSRxOdSAEk4Pl87xSHDwzlh1tlUGX1Q0c1CtLhgCau%2FwtMSqrZtGB8OC%2Bksd5orv3MOoyxneyu2p94NOzp8K34I0cPvXAqOrojtqkBXcfASnYmkpCpMttS4kwiFyNnR9fs%2FawjLqcjtGn4w7ZWsE5zOc3ozQO2o3Oke&X-Amz-Signature=47a0faf9c09fee269af1e9bd8c3c032e12be97b676c20acd872b5494864a079c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVTTFVGD%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3izy9gzabstd1p5E7QTFaOnvSw2caU76g6mLbUtT94AIhAPBA2oq5J3%2B4W1l6TsC%2FeABpYbW%2Bx8ICarCZH85RDUchKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxacumG5GB0adfNozsq3AM8lqbw3YQN8UkNShgxwRCBB3wRnQrax%2Fu5tb%2BKXfMwVmkWR7j7FqegfwhvIvhR4IJtMQlHFSJzU8TxcOtZh%2FNWPCDJm2WJBHWKtm3%2Bv%2FpwE7p04cpNCr%2FPmfE2cRyp5RFu2%2Bje%2Fs2Q5AjZxtWz%2B0vaCne00VIHMb76VGXptBODq1zjnjbY4rqaks%2Fj1oxzh3I9R20H%2F8dOHJX1Z39cEl1yax5VVWzLgdCs%2BJbHoA0mCQ6%2B%2B98SdO2JdENmT9Q0SMteqU2vGXqh9IlKUUimCcIs0HD57okO0mcsJlouKBQS1ByeMvTMlRCQdoeBn8I0BJAR%2FjpHDEQn7kB8jaMD9u%2BmeHILzeZGeTZnSUj4drG3s1szS4oM4ey2OF5oTrU4Pg3f9NPfczMAbn8ZFxw0Yj0NwIo8U6S083AK0DK9ng2b3jCh%2BFsmlQc5d7ft0o8MgI3M0Va4tKK6HbbvB%2FQkdcC6g1CENE0ftiE%2Be5jx1p3nroq4uC0xRBPgdb6zVu5l%2F5u9kxLYxS1u2iK4Uv3cMMgqPFx0DRpsSWPuzqeebc%2B62yxNz0lJfOz9JMK98knwz%2FYOHFKPnvKilmTIIajfYhMnV%2BBxvsnTXfKe%2BeC2lLpGruEJqtiN5fKEDlyVtjDR4OTIBjqkAciQp35lxy9a6WLxe7hDXCOMpiQps8rP1s9vvOosFwHfAb0vHCWYYZjn7cSRxOdSAEk4Pl87xSHDwzlh1tlUGX1Q0c1CtLhgCau%2FwtMSqrZtGB8OC%2Bksd5orv3MOoyxneyu2p94NOzp8K34I0cPvXAqOrojtqkBXcfASnYmkpCpMttS4kwiFyNnR9fs%2FawjLqcjtGn4w7ZWsE5zOc3ozQO2o3Oke&X-Amz-Signature=85a959e17cce67bbba7bc1eb6c81fca9d9ef27321e2daf61016b3e2b72dc8ae5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVTTFVGD%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3izy9gzabstd1p5E7QTFaOnvSw2caU76g6mLbUtT94AIhAPBA2oq5J3%2B4W1l6TsC%2FeABpYbW%2Bx8ICarCZH85RDUchKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxacumG5GB0adfNozsq3AM8lqbw3YQN8UkNShgxwRCBB3wRnQrax%2Fu5tb%2BKXfMwVmkWR7j7FqegfwhvIvhR4IJtMQlHFSJzU8TxcOtZh%2FNWPCDJm2WJBHWKtm3%2Bv%2FpwE7p04cpNCr%2FPmfE2cRyp5RFu2%2Bje%2Fs2Q5AjZxtWz%2B0vaCne00VIHMb76VGXptBODq1zjnjbY4rqaks%2Fj1oxzh3I9R20H%2F8dOHJX1Z39cEl1yax5VVWzLgdCs%2BJbHoA0mCQ6%2B%2B98SdO2JdENmT9Q0SMteqU2vGXqh9IlKUUimCcIs0HD57okO0mcsJlouKBQS1ByeMvTMlRCQdoeBn8I0BJAR%2FjpHDEQn7kB8jaMD9u%2BmeHILzeZGeTZnSUj4drG3s1szS4oM4ey2OF5oTrU4Pg3f9NPfczMAbn8ZFxw0Yj0NwIo8U6S083AK0DK9ng2b3jCh%2BFsmlQc5d7ft0o8MgI3M0Va4tKK6HbbvB%2FQkdcC6g1CENE0ftiE%2Be5jx1p3nroq4uC0xRBPgdb6zVu5l%2F5u9kxLYxS1u2iK4Uv3cMMgqPFx0DRpsSWPuzqeebc%2B62yxNz0lJfOz9JMK98knwz%2FYOHFKPnvKilmTIIajfYhMnV%2BBxvsnTXfKe%2BeC2lLpGruEJqtiN5fKEDlyVtjDR4OTIBjqkAciQp35lxy9a6WLxe7hDXCOMpiQps8rP1s9vvOosFwHfAb0vHCWYYZjn7cSRxOdSAEk4Pl87xSHDwzlh1tlUGX1Q0c1CtLhgCau%2FwtMSqrZtGB8OC%2Bksd5orv3MOoyxneyu2p94NOzp8K34I0cPvXAqOrojtqkBXcfASnYmkpCpMttS4kwiFyNnR9fs%2FawjLqcjtGn4w7ZWsE5zOc3ozQO2o3Oke&X-Amz-Signature=c99ffd6bf4674322a1eedbea42ba191d1053239cb129e1c5336a491ca063cd17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

