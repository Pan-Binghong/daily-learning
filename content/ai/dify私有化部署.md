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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PK447Q2%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDezilxltV1x8Nrz3QMEVf%2FfdfNQXPbt8pXDuZnjNwEYQIhAOUgB8ZQrGeZ4Tm6s08Ysnit59FT59qFywxGizCJ%2BqiiKv8DCGQQABoMNjM3NDIzMTgzODA1IgzQXOpsd3ftBC3g19kq3AM2wPRRDdAdQ0TRW1CZOlJv5avl0LPZZ9H%2BK66Uty0eaeuAHcizCUUfbFl2m923r8M1lE8nfTgKVDPPY1F7ewYssd2LAiomX67tF82I9MTggscjYQr3Fho3hu1ONLezk8FrPc5gvp1yX4aF%2Bwt6J%2FpjQDYmj1EiVCZHzYtqgbaR08HvpID1w12ItUJ5ASWrHaDP4j%2BKkh%2FcfMv9WkJ%2BshUk6awv7tzaH%2Fd4SGz1l3Jejm2Ci41ANHrDPOAThJJ4GlMkFtPmw7XB3kKWEDN1I%2BD%2BB3KthUmA2VDIarPYjqrm%2FC5GSvE1RJzt%2B7SNm5CEiXT0Qoc9dz01dYM4OC01TxvS6yco6ZO44JELbbTccthDIYR2asgld86Cu5ZAE9sewaMQnGEaC%2Beadhnw6wWNxh6HDACZl5Mxua%2FrzCVF4K8zxKw18VL4Pg24y6D3%2B8ozwKRsvew%2BGIP8%2ByQGYKSThP%2BJmo9xJ%2FKo5fEZvaSv8GMa9cbiQgXyqq1qQRzB3I1YVdl6R1Ny9RLo1e5AkaEMOUGFn9npJ1J2o5l6W3OfjEoB9x1yuf67boGK0M2XG2nF0nFth0rd%2FjGPDVq7scayDT1thKzLOOyq%2BsxpMZasaib3gyj9qWg3KH9E5Qi5aDD3zI7NBjqkAcWR8hTwGjpwn%2F1%2FVUoVbztttHMVrn8BbO4UEhxiO%2FaOLbp0YeFF%2B5mhzRd4goFNAQ%2B7W8fkdEAzAdYyKkneRYpAssjLSV67415ZpHfXunv1J%2FY5K6z34LaguUkFX%2FtTbkjgIlhNUWBv9TBu7dnGczUEsMJKie%2FuUos2NPUzjlfdESsk2ItER8YgFCQyxCFrKdoSkiefci62YhBzr3iaM7GNPuJ7&X-Amz-Signature=1fcda307c234e7a0688af1eddfc17a194fe59b22a560e1c8dd065947c18b3c9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PK447Q2%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDezilxltV1x8Nrz3QMEVf%2FfdfNQXPbt8pXDuZnjNwEYQIhAOUgB8ZQrGeZ4Tm6s08Ysnit59FT59qFywxGizCJ%2BqiiKv8DCGQQABoMNjM3NDIzMTgzODA1IgzQXOpsd3ftBC3g19kq3AM2wPRRDdAdQ0TRW1CZOlJv5avl0LPZZ9H%2BK66Uty0eaeuAHcizCUUfbFl2m923r8M1lE8nfTgKVDPPY1F7ewYssd2LAiomX67tF82I9MTggscjYQr3Fho3hu1ONLezk8FrPc5gvp1yX4aF%2Bwt6J%2FpjQDYmj1EiVCZHzYtqgbaR08HvpID1w12ItUJ5ASWrHaDP4j%2BKkh%2FcfMv9WkJ%2BshUk6awv7tzaH%2Fd4SGz1l3Jejm2Ci41ANHrDPOAThJJ4GlMkFtPmw7XB3kKWEDN1I%2BD%2BB3KthUmA2VDIarPYjqrm%2FC5GSvE1RJzt%2B7SNm5CEiXT0Qoc9dz01dYM4OC01TxvS6yco6ZO44JELbbTccthDIYR2asgld86Cu5ZAE9sewaMQnGEaC%2Beadhnw6wWNxh6HDACZl5Mxua%2FrzCVF4K8zxKw18VL4Pg24y6D3%2B8ozwKRsvew%2BGIP8%2ByQGYKSThP%2BJmo9xJ%2FKo5fEZvaSv8GMa9cbiQgXyqq1qQRzB3I1YVdl6R1Ny9RLo1e5AkaEMOUGFn9npJ1J2o5l6W3OfjEoB9x1yuf67boGK0M2XG2nF0nFth0rd%2FjGPDVq7scayDT1thKzLOOyq%2BsxpMZasaib3gyj9qWg3KH9E5Qi5aDD3zI7NBjqkAcWR8hTwGjpwn%2F1%2FVUoVbztttHMVrn8BbO4UEhxiO%2FaOLbp0YeFF%2B5mhzRd4goFNAQ%2B7W8fkdEAzAdYyKkneRYpAssjLSV67415ZpHfXunv1J%2FY5K6z34LaguUkFX%2FtTbkjgIlhNUWBv9TBu7dnGczUEsMJKie%2FuUos2NPUzjlfdESsk2ItER8YgFCQyxCFrKdoSkiefci62YhBzr3iaM7GNPuJ7&X-Amz-Signature=605ad95e8cad3dcbbd836657ea36c28cb5019993efa7013586e65b4a71eff9bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PK447Q2%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDezilxltV1x8Nrz3QMEVf%2FfdfNQXPbt8pXDuZnjNwEYQIhAOUgB8ZQrGeZ4Tm6s08Ysnit59FT59qFywxGizCJ%2BqiiKv8DCGQQABoMNjM3NDIzMTgzODA1IgzQXOpsd3ftBC3g19kq3AM2wPRRDdAdQ0TRW1CZOlJv5avl0LPZZ9H%2BK66Uty0eaeuAHcizCUUfbFl2m923r8M1lE8nfTgKVDPPY1F7ewYssd2LAiomX67tF82I9MTggscjYQr3Fho3hu1ONLezk8FrPc5gvp1yX4aF%2Bwt6J%2FpjQDYmj1EiVCZHzYtqgbaR08HvpID1w12ItUJ5ASWrHaDP4j%2BKkh%2FcfMv9WkJ%2BshUk6awv7tzaH%2Fd4SGz1l3Jejm2Ci41ANHrDPOAThJJ4GlMkFtPmw7XB3kKWEDN1I%2BD%2BB3KthUmA2VDIarPYjqrm%2FC5GSvE1RJzt%2B7SNm5CEiXT0Qoc9dz01dYM4OC01TxvS6yco6ZO44JELbbTccthDIYR2asgld86Cu5ZAE9sewaMQnGEaC%2Beadhnw6wWNxh6HDACZl5Mxua%2FrzCVF4K8zxKw18VL4Pg24y6D3%2B8ozwKRsvew%2BGIP8%2ByQGYKSThP%2BJmo9xJ%2FKo5fEZvaSv8GMa9cbiQgXyqq1qQRzB3I1YVdl6R1Ny9RLo1e5AkaEMOUGFn9npJ1J2o5l6W3OfjEoB9x1yuf67boGK0M2XG2nF0nFth0rd%2FjGPDVq7scayDT1thKzLOOyq%2BsxpMZasaib3gyj9qWg3KH9E5Qi5aDD3zI7NBjqkAcWR8hTwGjpwn%2F1%2FVUoVbztttHMVrn8BbO4UEhxiO%2FaOLbp0YeFF%2B5mhzRd4goFNAQ%2B7W8fkdEAzAdYyKkneRYpAssjLSV67415ZpHfXunv1J%2FY5K6z34LaguUkFX%2FtTbkjgIlhNUWBv9TBu7dnGczUEsMJKie%2FuUos2NPUzjlfdESsk2ItER8YgFCQyxCFrKdoSkiefci62YhBzr3iaM7GNPuJ7&X-Amz-Signature=13e4b88753a1a49a43974ec6a9bbb0cfe647149215ec8001fdb85c6452804874&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PK447Q2%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDezilxltV1x8Nrz3QMEVf%2FfdfNQXPbt8pXDuZnjNwEYQIhAOUgB8ZQrGeZ4Tm6s08Ysnit59FT59qFywxGizCJ%2BqiiKv8DCGQQABoMNjM3NDIzMTgzODA1IgzQXOpsd3ftBC3g19kq3AM2wPRRDdAdQ0TRW1CZOlJv5avl0LPZZ9H%2BK66Uty0eaeuAHcizCUUfbFl2m923r8M1lE8nfTgKVDPPY1F7ewYssd2LAiomX67tF82I9MTggscjYQr3Fho3hu1ONLezk8FrPc5gvp1yX4aF%2Bwt6J%2FpjQDYmj1EiVCZHzYtqgbaR08HvpID1w12ItUJ5ASWrHaDP4j%2BKkh%2FcfMv9WkJ%2BshUk6awv7tzaH%2Fd4SGz1l3Jejm2Ci41ANHrDPOAThJJ4GlMkFtPmw7XB3kKWEDN1I%2BD%2BB3KthUmA2VDIarPYjqrm%2FC5GSvE1RJzt%2B7SNm5CEiXT0Qoc9dz01dYM4OC01TxvS6yco6ZO44JELbbTccthDIYR2asgld86Cu5ZAE9sewaMQnGEaC%2Beadhnw6wWNxh6HDACZl5Mxua%2FrzCVF4K8zxKw18VL4Pg24y6D3%2B8ozwKRsvew%2BGIP8%2ByQGYKSThP%2BJmo9xJ%2FKo5fEZvaSv8GMa9cbiQgXyqq1qQRzB3I1YVdl6R1Ny9RLo1e5AkaEMOUGFn9npJ1J2o5l6W3OfjEoB9x1yuf67boGK0M2XG2nF0nFth0rd%2FjGPDVq7scayDT1thKzLOOyq%2BsxpMZasaib3gyj9qWg3KH9E5Qi5aDD3zI7NBjqkAcWR8hTwGjpwn%2F1%2FVUoVbztttHMVrn8BbO4UEhxiO%2FaOLbp0YeFF%2B5mhzRd4goFNAQ%2B7W8fkdEAzAdYyKkneRYpAssjLSV67415ZpHfXunv1J%2FY5K6z34LaguUkFX%2FtTbkjgIlhNUWBv9TBu7dnGczUEsMJKie%2FuUos2NPUzjlfdESsk2ItER8YgFCQyxCFrKdoSkiefci62YhBzr3iaM7GNPuJ7&X-Amz-Signature=65febd9d73a3a79d0c39b07e34ba64da21f19b3554bb55c8e6e6f534d232501b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PK447Q2%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDezilxltV1x8Nrz3QMEVf%2FfdfNQXPbt8pXDuZnjNwEYQIhAOUgB8ZQrGeZ4Tm6s08Ysnit59FT59qFywxGizCJ%2BqiiKv8DCGQQABoMNjM3NDIzMTgzODA1IgzQXOpsd3ftBC3g19kq3AM2wPRRDdAdQ0TRW1CZOlJv5avl0LPZZ9H%2BK66Uty0eaeuAHcizCUUfbFl2m923r8M1lE8nfTgKVDPPY1F7ewYssd2LAiomX67tF82I9MTggscjYQr3Fho3hu1ONLezk8FrPc5gvp1yX4aF%2Bwt6J%2FpjQDYmj1EiVCZHzYtqgbaR08HvpID1w12ItUJ5ASWrHaDP4j%2BKkh%2FcfMv9WkJ%2BshUk6awv7tzaH%2Fd4SGz1l3Jejm2Ci41ANHrDPOAThJJ4GlMkFtPmw7XB3kKWEDN1I%2BD%2BB3KthUmA2VDIarPYjqrm%2FC5GSvE1RJzt%2B7SNm5CEiXT0Qoc9dz01dYM4OC01TxvS6yco6ZO44JELbbTccthDIYR2asgld86Cu5ZAE9sewaMQnGEaC%2Beadhnw6wWNxh6HDACZl5Mxua%2FrzCVF4K8zxKw18VL4Pg24y6D3%2B8ozwKRsvew%2BGIP8%2ByQGYKSThP%2BJmo9xJ%2FKo5fEZvaSv8GMa9cbiQgXyqq1qQRzB3I1YVdl6R1Ny9RLo1e5AkaEMOUGFn9npJ1J2o5l6W3OfjEoB9x1yuf67boGK0M2XG2nF0nFth0rd%2FjGPDVq7scayDT1thKzLOOyq%2BsxpMZasaib3gyj9qWg3KH9E5Qi5aDD3zI7NBjqkAcWR8hTwGjpwn%2F1%2FVUoVbztttHMVrn8BbO4UEhxiO%2FaOLbp0YeFF%2B5mhzRd4goFNAQ%2B7W8fkdEAzAdYyKkneRYpAssjLSV67415ZpHfXunv1J%2FY5K6z34LaguUkFX%2FtTbkjgIlhNUWBv9TBu7dnGczUEsMJKie%2FuUos2NPUzjlfdESsk2ItER8YgFCQyxCFrKdoSkiefci62YhBzr3iaM7GNPuJ7&X-Amz-Signature=d984b7a1413b94c1f375d4f6d49dc4a27508175567a0d7f8221bf97c34feb7a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PK447Q2%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDezilxltV1x8Nrz3QMEVf%2FfdfNQXPbt8pXDuZnjNwEYQIhAOUgB8ZQrGeZ4Tm6s08Ysnit59FT59qFywxGizCJ%2BqiiKv8DCGQQABoMNjM3NDIzMTgzODA1IgzQXOpsd3ftBC3g19kq3AM2wPRRDdAdQ0TRW1CZOlJv5avl0LPZZ9H%2BK66Uty0eaeuAHcizCUUfbFl2m923r8M1lE8nfTgKVDPPY1F7ewYssd2LAiomX67tF82I9MTggscjYQr3Fho3hu1ONLezk8FrPc5gvp1yX4aF%2Bwt6J%2FpjQDYmj1EiVCZHzYtqgbaR08HvpID1w12ItUJ5ASWrHaDP4j%2BKkh%2FcfMv9WkJ%2BshUk6awv7tzaH%2Fd4SGz1l3Jejm2Ci41ANHrDPOAThJJ4GlMkFtPmw7XB3kKWEDN1I%2BD%2BB3KthUmA2VDIarPYjqrm%2FC5GSvE1RJzt%2B7SNm5CEiXT0Qoc9dz01dYM4OC01TxvS6yco6ZO44JELbbTccthDIYR2asgld86Cu5ZAE9sewaMQnGEaC%2Beadhnw6wWNxh6HDACZl5Mxua%2FrzCVF4K8zxKw18VL4Pg24y6D3%2B8ozwKRsvew%2BGIP8%2ByQGYKSThP%2BJmo9xJ%2FKo5fEZvaSv8GMa9cbiQgXyqq1qQRzB3I1YVdl6R1Ny9RLo1e5AkaEMOUGFn9npJ1J2o5l6W3OfjEoB9x1yuf67boGK0M2XG2nF0nFth0rd%2FjGPDVq7scayDT1thKzLOOyq%2BsxpMZasaib3gyj9qWg3KH9E5Qi5aDD3zI7NBjqkAcWR8hTwGjpwn%2F1%2FVUoVbztttHMVrn8BbO4UEhxiO%2FaOLbp0YeFF%2B5mhzRd4goFNAQ%2B7W8fkdEAzAdYyKkneRYpAssjLSV67415ZpHfXunv1J%2FY5K6z34LaguUkFX%2FtTbkjgIlhNUWBv9TBu7dnGczUEsMJKie%2FuUos2NPUzjlfdESsk2ItER8YgFCQyxCFrKdoSkiefci62YhBzr3iaM7GNPuJ7&X-Amz-Signature=3039ea1a72fded01369480a1e5de9f0506fdbf08f0736bae814f3ac10ef47fd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PK447Q2%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDezilxltV1x8Nrz3QMEVf%2FfdfNQXPbt8pXDuZnjNwEYQIhAOUgB8ZQrGeZ4Tm6s08Ysnit59FT59qFywxGizCJ%2BqiiKv8DCGQQABoMNjM3NDIzMTgzODA1IgzQXOpsd3ftBC3g19kq3AM2wPRRDdAdQ0TRW1CZOlJv5avl0LPZZ9H%2BK66Uty0eaeuAHcizCUUfbFl2m923r8M1lE8nfTgKVDPPY1F7ewYssd2LAiomX67tF82I9MTggscjYQr3Fho3hu1ONLezk8FrPc5gvp1yX4aF%2Bwt6J%2FpjQDYmj1EiVCZHzYtqgbaR08HvpID1w12ItUJ5ASWrHaDP4j%2BKkh%2FcfMv9WkJ%2BshUk6awv7tzaH%2Fd4SGz1l3Jejm2Ci41ANHrDPOAThJJ4GlMkFtPmw7XB3kKWEDN1I%2BD%2BB3KthUmA2VDIarPYjqrm%2FC5GSvE1RJzt%2B7SNm5CEiXT0Qoc9dz01dYM4OC01TxvS6yco6ZO44JELbbTccthDIYR2asgld86Cu5ZAE9sewaMQnGEaC%2Beadhnw6wWNxh6HDACZl5Mxua%2FrzCVF4K8zxKw18VL4Pg24y6D3%2B8ozwKRsvew%2BGIP8%2ByQGYKSThP%2BJmo9xJ%2FKo5fEZvaSv8GMa9cbiQgXyqq1qQRzB3I1YVdl6R1Ny9RLo1e5AkaEMOUGFn9npJ1J2o5l6W3OfjEoB9x1yuf67boGK0M2XG2nF0nFth0rd%2FjGPDVq7scayDT1thKzLOOyq%2BsxpMZasaib3gyj9qWg3KH9E5Qi5aDD3zI7NBjqkAcWR8hTwGjpwn%2F1%2FVUoVbztttHMVrn8BbO4UEhxiO%2FaOLbp0YeFF%2B5mhzRd4goFNAQ%2B7W8fkdEAzAdYyKkneRYpAssjLSV67415ZpHfXunv1J%2FY5K6z34LaguUkFX%2FtTbkjgIlhNUWBv9TBu7dnGczUEsMJKie%2FuUos2NPUzjlfdESsk2ItER8YgFCQyxCFrKdoSkiefci62YhBzr3iaM7GNPuJ7&X-Amz-Signature=bd01ee96f0099205f4f9c903701a2d20e5428c2ebc672c3d6df4ea0c5580b6fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PK447Q2%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDezilxltV1x8Nrz3QMEVf%2FfdfNQXPbt8pXDuZnjNwEYQIhAOUgB8ZQrGeZ4Tm6s08Ysnit59FT59qFywxGizCJ%2BqiiKv8DCGQQABoMNjM3NDIzMTgzODA1IgzQXOpsd3ftBC3g19kq3AM2wPRRDdAdQ0TRW1CZOlJv5avl0LPZZ9H%2BK66Uty0eaeuAHcizCUUfbFl2m923r8M1lE8nfTgKVDPPY1F7ewYssd2LAiomX67tF82I9MTggscjYQr3Fho3hu1ONLezk8FrPc5gvp1yX4aF%2Bwt6J%2FpjQDYmj1EiVCZHzYtqgbaR08HvpID1w12ItUJ5ASWrHaDP4j%2BKkh%2FcfMv9WkJ%2BshUk6awv7tzaH%2Fd4SGz1l3Jejm2Ci41ANHrDPOAThJJ4GlMkFtPmw7XB3kKWEDN1I%2BD%2BB3KthUmA2VDIarPYjqrm%2FC5GSvE1RJzt%2B7SNm5CEiXT0Qoc9dz01dYM4OC01TxvS6yco6ZO44JELbbTccthDIYR2asgld86Cu5ZAE9sewaMQnGEaC%2Beadhnw6wWNxh6HDACZl5Mxua%2FrzCVF4K8zxKw18VL4Pg24y6D3%2B8ozwKRsvew%2BGIP8%2ByQGYKSThP%2BJmo9xJ%2FKo5fEZvaSv8GMa9cbiQgXyqq1qQRzB3I1YVdl6R1Ny9RLo1e5AkaEMOUGFn9npJ1J2o5l6W3OfjEoB9x1yuf67boGK0M2XG2nF0nFth0rd%2FjGPDVq7scayDT1thKzLOOyq%2BsxpMZasaib3gyj9qWg3KH9E5Qi5aDD3zI7NBjqkAcWR8hTwGjpwn%2F1%2FVUoVbztttHMVrn8BbO4UEhxiO%2FaOLbp0YeFF%2B5mhzRd4goFNAQ%2B7W8fkdEAzAdYyKkneRYpAssjLSV67415ZpHfXunv1J%2FY5K6z34LaguUkFX%2FtTbkjgIlhNUWBv9TBu7dnGczUEsMJKie%2FuUos2NPUzjlfdESsk2ItER8YgFCQyxCFrKdoSkiefci62YhBzr3iaM7GNPuJ7&X-Amz-Signature=e58f5c7386c850bf85b95e6f3a13ef194d080a04fdb674810b53346abb04046b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PK447Q2%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDezilxltV1x8Nrz3QMEVf%2FfdfNQXPbt8pXDuZnjNwEYQIhAOUgB8ZQrGeZ4Tm6s08Ysnit59FT59qFywxGizCJ%2BqiiKv8DCGQQABoMNjM3NDIzMTgzODA1IgzQXOpsd3ftBC3g19kq3AM2wPRRDdAdQ0TRW1CZOlJv5avl0LPZZ9H%2BK66Uty0eaeuAHcizCUUfbFl2m923r8M1lE8nfTgKVDPPY1F7ewYssd2LAiomX67tF82I9MTggscjYQr3Fho3hu1ONLezk8FrPc5gvp1yX4aF%2Bwt6J%2FpjQDYmj1EiVCZHzYtqgbaR08HvpID1w12ItUJ5ASWrHaDP4j%2BKkh%2FcfMv9WkJ%2BshUk6awv7tzaH%2Fd4SGz1l3Jejm2Ci41ANHrDPOAThJJ4GlMkFtPmw7XB3kKWEDN1I%2BD%2BB3KthUmA2VDIarPYjqrm%2FC5GSvE1RJzt%2B7SNm5CEiXT0Qoc9dz01dYM4OC01TxvS6yco6ZO44JELbbTccthDIYR2asgld86Cu5ZAE9sewaMQnGEaC%2Beadhnw6wWNxh6HDACZl5Mxua%2FrzCVF4K8zxKw18VL4Pg24y6D3%2B8ozwKRsvew%2BGIP8%2ByQGYKSThP%2BJmo9xJ%2FKo5fEZvaSv8GMa9cbiQgXyqq1qQRzB3I1YVdl6R1Ny9RLo1e5AkaEMOUGFn9npJ1J2o5l6W3OfjEoB9x1yuf67boGK0M2XG2nF0nFth0rd%2FjGPDVq7scayDT1thKzLOOyq%2BsxpMZasaib3gyj9qWg3KH9E5Qi5aDD3zI7NBjqkAcWR8hTwGjpwn%2F1%2FVUoVbztttHMVrn8BbO4UEhxiO%2FaOLbp0YeFF%2B5mhzRd4goFNAQ%2B7W8fkdEAzAdYyKkneRYpAssjLSV67415ZpHfXunv1J%2FY5K6z34LaguUkFX%2FtTbkjgIlhNUWBv9TBu7dnGczUEsMJKie%2FuUos2NPUzjlfdESsk2ItER8YgFCQyxCFrKdoSkiefci62YhBzr3iaM7GNPuJ7&X-Amz-Signature=6f8ab2a30b568b989a617b103ba2833267e65cca06fb2cba4ae4ef8a9636b15b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PK447Q2%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDezilxltV1x8Nrz3QMEVf%2FfdfNQXPbt8pXDuZnjNwEYQIhAOUgB8ZQrGeZ4Tm6s08Ysnit59FT59qFywxGizCJ%2BqiiKv8DCGQQABoMNjM3NDIzMTgzODA1IgzQXOpsd3ftBC3g19kq3AM2wPRRDdAdQ0TRW1CZOlJv5avl0LPZZ9H%2BK66Uty0eaeuAHcizCUUfbFl2m923r8M1lE8nfTgKVDPPY1F7ewYssd2LAiomX67tF82I9MTggscjYQr3Fho3hu1ONLezk8FrPc5gvp1yX4aF%2Bwt6J%2FpjQDYmj1EiVCZHzYtqgbaR08HvpID1w12ItUJ5ASWrHaDP4j%2BKkh%2FcfMv9WkJ%2BshUk6awv7tzaH%2Fd4SGz1l3Jejm2Ci41ANHrDPOAThJJ4GlMkFtPmw7XB3kKWEDN1I%2BD%2BB3KthUmA2VDIarPYjqrm%2FC5GSvE1RJzt%2B7SNm5CEiXT0Qoc9dz01dYM4OC01TxvS6yco6ZO44JELbbTccthDIYR2asgld86Cu5ZAE9sewaMQnGEaC%2Beadhnw6wWNxh6HDACZl5Mxua%2FrzCVF4K8zxKw18VL4Pg24y6D3%2B8ozwKRsvew%2BGIP8%2ByQGYKSThP%2BJmo9xJ%2FKo5fEZvaSv8GMa9cbiQgXyqq1qQRzB3I1YVdl6R1Ny9RLo1e5AkaEMOUGFn9npJ1J2o5l6W3OfjEoB9x1yuf67boGK0M2XG2nF0nFth0rd%2FjGPDVq7scayDT1thKzLOOyq%2BsxpMZasaib3gyj9qWg3KH9E5Qi5aDD3zI7NBjqkAcWR8hTwGjpwn%2F1%2FVUoVbztttHMVrn8BbO4UEhxiO%2FaOLbp0YeFF%2B5mhzRd4goFNAQ%2B7W8fkdEAzAdYyKkneRYpAssjLSV67415ZpHfXunv1J%2FY5K6z34LaguUkFX%2FtTbkjgIlhNUWBv9TBu7dnGczUEsMJKie%2FuUos2NPUzjlfdESsk2ItER8YgFCQyxCFrKdoSkiefci62YhBzr3iaM7GNPuJ7&X-Amz-Signature=1540b8cdd5872b4996ea7a94198411fdb19da277ed3d5e4a8c2663901cf568a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

