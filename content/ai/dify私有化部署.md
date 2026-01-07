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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GBH3ZZ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BEzIwcCl51b5qwh6pU95IaeUDcy6DZyxCP0IpiqGKWwIgAOkNY1Jihj0eMGvn2bA1xr9XpwRB3RhCx3qw4z%2FQSdQq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDGOCNDQrqJJiaafaECrcAxStyLv2M3chMyN9N6hqMbHUYZKXM5Z5PbnER%2FbcRAM9pWVohhCoXY28roRtfC7%2FsBOdwrEgTUj3GkqH21Y1WrEARAIT90Oj%2BgVH9og3kZh102UynlKSzp%2B8NIBo0n6riPK5k2%2BQvFGVguht2CDg9acKN2o%2FG3%2BMFBqzCDKe9GLYakMV6qGQoMh5LpNKs0EmaC943xVBcpjBAPM8fI5COTSLKM5acYtFfsS5l3B4Sq%2Bzc%2BlHkHZujFOU54nmNVnYxmQEOq%2FaE%2BSxVST2VpPjrOcJyN7lRb7IsGF%2BaK5%2FR6dLq3RtU9Opi85cJfCuQKYHc2Fp%2FS3BrI8jPCCjehUKLSCKtlRrrBK8ssQll3DumMJfM4bP7FWcoKOxHfXR%2BDgStQzhLSCjUcdzUAmqBZa0wcHLeFQFPGM5R8J85duzAGwJS4Q3P6zhIL9VBx5%2BrhAfl0wCuf5Vgq72SvxBhEo3eGHhNJTdWudM7Nn9z1GgT3tI5IckJKEcuopRtHVFdSWtGbZ%2Fv9JBSDm6F54mwz3huAtVxOwQVwMUFKrNtP7aSVB8%2FpsXZIfUg%2B75bHkasYi187X0g23rvXN4wSIwaIfSAV5Nx1wGzesxFb9%2FovcH34d%2BP3KJygmdE2kD83jwMNuO98oGOqUBEW4Is8666RFMwndR1qFwFzr0lA582UzTbAcJGWuPB1Zcu0Rc2PZ5tuUOtoc4nPpOBSuTMPOCNhV4mAWqxeUg0ZDxStxF0WlQz%2Bt2snKQvvW8CEsvMihZOHoFzoARp4lJTCmmb2tqm7tHIsj7IkWmOnQXebvZ1FP9eGEtUT1Y9OC7CiXZwRyyWwICwKeoyxu3ZIh%2B6bjoWb78CwoSwmy1D4QfsXWG&X-Amz-Signature=ca0f4140b4d30935e30d4a8e590cec8968daeea09b91cafe46a7ee22979b9c6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GBH3ZZ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BEzIwcCl51b5qwh6pU95IaeUDcy6DZyxCP0IpiqGKWwIgAOkNY1Jihj0eMGvn2bA1xr9XpwRB3RhCx3qw4z%2FQSdQq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDGOCNDQrqJJiaafaECrcAxStyLv2M3chMyN9N6hqMbHUYZKXM5Z5PbnER%2FbcRAM9pWVohhCoXY28roRtfC7%2FsBOdwrEgTUj3GkqH21Y1WrEARAIT90Oj%2BgVH9og3kZh102UynlKSzp%2B8NIBo0n6riPK5k2%2BQvFGVguht2CDg9acKN2o%2FG3%2BMFBqzCDKe9GLYakMV6qGQoMh5LpNKs0EmaC943xVBcpjBAPM8fI5COTSLKM5acYtFfsS5l3B4Sq%2Bzc%2BlHkHZujFOU54nmNVnYxmQEOq%2FaE%2BSxVST2VpPjrOcJyN7lRb7IsGF%2BaK5%2FR6dLq3RtU9Opi85cJfCuQKYHc2Fp%2FS3BrI8jPCCjehUKLSCKtlRrrBK8ssQll3DumMJfM4bP7FWcoKOxHfXR%2BDgStQzhLSCjUcdzUAmqBZa0wcHLeFQFPGM5R8J85duzAGwJS4Q3P6zhIL9VBx5%2BrhAfl0wCuf5Vgq72SvxBhEo3eGHhNJTdWudM7Nn9z1GgT3tI5IckJKEcuopRtHVFdSWtGbZ%2Fv9JBSDm6F54mwz3huAtVxOwQVwMUFKrNtP7aSVB8%2FpsXZIfUg%2B75bHkasYi187X0g23rvXN4wSIwaIfSAV5Nx1wGzesxFb9%2FovcH34d%2BP3KJygmdE2kD83jwMNuO98oGOqUBEW4Is8666RFMwndR1qFwFzr0lA582UzTbAcJGWuPB1Zcu0Rc2PZ5tuUOtoc4nPpOBSuTMPOCNhV4mAWqxeUg0ZDxStxF0WlQz%2Bt2snKQvvW8CEsvMihZOHoFzoARp4lJTCmmb2tqm7tHIsj7IkWmOnQXebvZ1FP9eGEtUT1Y9OC7CiXZwRyyWwICwKeoyxu3ZIh%2B6bjoWb78CwoSwmy1D4QfsXWG&X-Amz-Signature=3107c9d1744d221e29b32c662051c6b92ce871df43ac7599dc4b39464c60fef5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GBH3ZZ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BEzIwcCl51b5qwh6pU95IaeUDcy6DZyxCP0IpiqGKWwIgAOkNY1Jihj0eMGvn2bA1xr9XpwRB3RhCx3qw4z%2FQSdQq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDGOCNDQrqJJiaafaECrcAxStyLv2M3chMyN9N6hqMbHUYZKXM5Z5PbnER%2FbcRAM9pWVohhCoXY28roRtfC7%2FsBOdwrEgTUj3GkqH21Y1WrEARAIT90Oj%2BgVH9og3kZh102UynlKSzp%2B8NIBo0n6riPK5k2%2BQvFGVguht2CDg9acKN2o%2FG3%2BMFBqzCDKe9GLYakMV6qGQoMh5LpNKs0EmaC943xVBcpjBAPM8fI5COTSLKM5acYtFfsS5l3B4Sq%2Bzc%2BlHkHZujFOU54nmNVnYxmQEOq%2FaE%2BSxVST2VpPjrOcJyN7lRb7IsGF%2BaK5%2FR6dLq3RtU9Opi85cJfCuQKYHc2Fp%2FS3BrI8jPCCjehUKLSCKtlRrrBK8ssQll3DumMJfM4bP7FWcoKOxHfXR%2BDgStQzhLSCjUcdzUAmqBZa0wcHLeFQFPGM5R8J85duzAGwJS4Q3P6zhIL9VBx5%2BrhAfl0wCuf5Vgq72SvxBhEo3eGHhNJTdWudM7Nn9z1GgT3tI5IckJKEcuopRtHVFdSWtGbZ%2Fv9JBSDm6F54mwz3huAtVxOwQVwMUFKrNtP7aSVB8%2FpsXZIfUg%2B75bHkasYi187X0g23rvXN4wSIwaIfSAV5Nx1wGzesxFb9%2FovcH34d%2BP3KJygmdE2kD83jwMNuO98oGOqUBEW4Is8666RFMwndR1qFwFzr0lA582UzTbAcJGWuPB1Zcu0Rc2PZ5tuUOtoc4nPpOBSuTMPOCNhV4mAWqxeUg0ZDxStxF0WlQz%2Bt2snKQvvW8CEsvMihZOHoFzoARp4lJTCmmb2tqm7tHIsj7IkWmOnQXebvZ1FP9eGEtUT1Y9OC7CiXZwRyyWwICwKeoyxu3ZIh%2B6bjoWb78CwoSwmy1D4QfsXWG&X-Amz-Signature=b68363743b24687aad785886b7c29aa2070a70b2df183784c66acb4cb7e27409&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GBH3ZZ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BEzIwcCl51b5qwh6pU95IaeUDcy6DZyxCP0IpiqGKWwIgAOkNY1Jihj0eMGvn2bA1xr9XpwRB3RhCx3qw4z%2FQSdQq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDGOCNDQrqJJiaafaECrcAxStyLv2M3chMyN9N6hqMbHUYZKXM5Z5PbnER%2FbcRAM9pWVohhCoXY28roRtfC7%2FsBOdwrEgTUj3GkqH21Y1WrEARAIT90Oj%2BgVH9og3kZh102UynlKSzp%2B8NIBo0n6riPK5k2%2BQvFGVguht2CDg9acKN2o%2FG3%2BMFBqzCDKe9GLYakMV6qGQoMh5LpNKs0EmaC943xVBcpjBAPM8fI5COTSLKM5acYtFfsS5l3B4Sq%2Bzc%2BlHkHZujFOU54nmNVnYxmQEOq%2FaE%2BSxVST2VpPjrOcJyN7lRb7IsGF%2BaK5%2FR6dLq3RtU9Opi85cJfCuQKYHc2Fp%2FS3BrI8jPCCjehUKLSCKtlRrrBK8ssQll3DumMJfM4bP7FWcoKOxHfXR%2BDgStQzhLSCjUcdzUAmqBZa0wcHLeFQFPGM5R8J85duzAGwJS4Q3P6zhIL9VBx5%2BrhAfl0wCuf5Vgq72SvxBhEo3eGHhNJTdWudM7Nn9z1GgT3tI5IckJKEcuopRtHVFdSWtGbZ%2Fv9JBSDm6F54mwz3huAtVxOwQVwMUFKrNtP7aSVB8%2FpsXZIfUg%2B75bHkasYi187X0g23rvXN4wSIwaIfSAV5Nx1wGzesxFb9%2FovcH34d%2BP3KJygmdE2kD83jwMNuO98oGOqUBEW4Is8666RFMwndR1qFwFzr0lA582UzTbAcJGWuPB1Zcu0Rc2PZ5tuUOtoc4nPpOBSuTMPOCNhV4mAWqxeUg0ZDxStxF0WlQz%2Bt2snKQvvW8CEsvMihZOHoFzoARp4lJTCmmb2tqm7tHIsj7IkWmOnQXebvZ1FP9eGEtUT1Y9OC7CiXZwRyyWwICwKeoyxu3ZIh%2B6bjoWb78CwoSwmy1D4QfsXWG&X-Amz-Signature=18ca99ef18c354bd641c06724e7ba8d6402cb8a66a068f20eb6dc1c8bccdcc56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GBH3ZZ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BEzIwcCl51b5qwh6pU95IaeUDcy6DZyxCP0IpiqGKWwIgAOkNY1Jihj0eMGvn2bA1xr9XpwRB3RhCx3qw4z%2FQSdQq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDGOCNDQrqJJiaafaECrcAxStyLv2M3chMyN9N6hqMbHUYZKXM5Z5PbnER%2FbcRAM9pWVohhCoXY28roRtfC7%2FsBOdwrEgTUj3GkqH21Y1WrEARAIT90Oj%2BgVH9og3kZh102UynlKSzp%2B8NIBo0n6riPK5k2%2BQvFGVguht2CDg9acKN2o%2FG3%2BMFBqzCDKe9GLYakMV6qGQoMh5LpNKs0EmaC943xVBcpjBAPM8fI5COTSLKM5acYtFfsS5l3B4Sq%2Bzc%2BlHkHZujFOU54nmNVnYxmQEOq%2FaE%2BSxVST2VpPjrOcJyN7lRb7IsGF%2BaK5%2FR6dLq3RtU9Opi85cJfCuQKYHc2Fp%2FS3BrI8jPCCjehUKLSCKtlRrrBK8ssQll3DumMJfM4bP7FWcoKOxHfXR%2BDgStQzhLSCjUcdzUAmqBZa0wcHLeFQFPGM5R8J85duzAGwJS4Q3P6zhIL9VBx5%2BrhAfl0wCuf5Vgq72SvxBhEo3eGHhNJTdWudM7Nn9z1GgT3tI5IckJKEcuopRtHVFdSWtGbZ%2Fv9JBSDm6F54mwz3huAtVxOwQVwMUFKrNtP7aSVB8%2FpsXZIfUg%2B75bHkasYi187X0g23rvXN4wSIwaIfSAV5Nx1wGzesxFb9%2FovcH34d%2BP3KJygmdE2kD83jwMNuO98oGOqUBEW4Is8666RFMwndR1qFwFzr0lA582UzTbAcJGWuPB1Zcu0Rc2PZ5tuUOtoc4nPpOBSuTMPOCNhV4mAWqxeUg0ZDxStxF0WlQz%2Bt2snKQvvW8CEsvMihZOHoFzoARp4lJTCmmb2tqm7tHIsj7IkWmOnQXebvZ1FP9eGEtUT1Y9OC7CiXZwRyyWwICwKeoyxu3ZIh%2B6bjoWb78CwoSwmy1D4QfsXWG&X-Amz-Signature=29f502b0c0ee335d3ede8cb4f98b64f666eaf71b5e053d82a5da682b7a78dc88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GBH3ZZ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BEzIwcCl51b5qwh6pU95IaeUDcy6DZyxCP0IpiqGKWwIgAOkNY1Jihj0eMGvn2bA1xr9XpwRB3RhCx3qw4z%2FQSdQq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDGOCNDQrqJJiaafaECrcAxStyLv2M3chMyN9N6hqMbHUYZKXM5Z5PbnER%2FbcRAM9pWVohhCoXY28roRtfC7%2FsBOdwrEgTUj3GkqH21Y1WrEARAIT90Oj%2BgVH9og3kZh102UynlKSzp%2B8NIBo0n6riPK5k2%2BQvFGVguht2CDg9acKN2o%2FG3%2BMFBqzCDKe9GLYakMV6qGQoMh5LpNKs0EmaC943xVBcpjBAPM8fI5COTSLKM5acYtFfsS5l3B4Sq%2Bzc%2BlHkHZujFOU54nmNVnYxmQEOq%2FaE%2BSxVST2VpPjrOcJyN7lRb7IsGF%2BaK5%2FR6dLq3RtU9Opi85cJfCuQKYHc2Fp%2FS3BrI8jPCCjehUKLSCKtlRrrBK8ssQll3DumMJfM4bP7FWcoKOxHfXR%2BDgStQzhLSCjUcdzUAmqBZa0wcHLeFQFPGM5R8J85duzAGwJS4Q3P6zhIL9VBx5%2BrhAfl0wCuf5Vgq72SvxBhEo3eGHhNJTdWudM7Nn9z1GgT3tI5IckJKEcuopRtHVFdSWtGbZ%2Fv9JBSDm6F54mwz3huAtVxOwQVwMUFKrNtP7aSVB8%2FpsXZIfUg%2B75bHkasYi187X0g23rvXN4wSIwaIfSAV5Nx1wGzesxFb9%2FovcH34d%2BP3KJygmdE2kD83jwMNuO98oGOqUBEW4Is8666RFMwndR1qFwFzr0lA582UzTbAcJGWuPB1Zcu0Rc2PZ5tuUOtoc4nPpOBSuTMPOCNhV4mAWqxeUg0ZDxStxF0WlQz%2Bt2snKQvvW8CEsvMihZOHoFzoARp4lJTCmmb2tqm7tHIsj7IkWmOnQXebvZ1FP9eGEtUT1Y9OC7CiXZwRyyWwICwKeoyxu3ZIh%2B6bjoWb78CwoSwmy1D4QfsXWG&X-Amz-Signature=690c1d7394a56ee47b154a9cd4a9e26aa52bc319a432b8b6042358591d8f8608&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GBH3ZZ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BEzIwcCl51b5qwh6pU95IaeUDcy6DZyxCP0IpiqGKWwIgAOkNY1Jihj0eMGvn2bA1xr9XpwRB3RhCx3qw4z%2FQSdQq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDGOCNDQrqJJiaafaECrcAxStyLv2M3chMyN9N6hqMbHUYZKXM5Z5PbnER%2FbcRAM9pWVohhCoXY28roRtfC7%2FsBOdwrEgTUj3GkqH21Y1WrEARAIT90Oj%2BgVH9og3kZh102UynlKSzp%2B8NIBo0n6riPK5k2%2BQvFGVguht2CDg9acKN2o%2FG3%2BMFBqzCDKe9GLYakMV6qGQoMh5LpNKs0EmaC943xVBcpjBAPM8fI5COTSLKM5acYtFfsS5l3B4Sq%2Bzc%2BlHkHZujFOU54nmNVnYxmQEOq%2FaE%2BSxVST2VpPjrOcJyN7lRb7IsGF%2BaK5%2FR6dLq3RtU9Opi85cJfCuQKYHc2Fp%2FS3BrI8jPCCjehUKLSCKtlRrrBK8ssQll3DumMJfM4bP7FWcoKOxHfXR%2BDgStQzhLSCjUcdzUAmqBZa0wcHLeFQFPGM5R8J85duzAGwJS4Q3P6zhIL9VBx5%2BrhAfl0wCuf5Vgq72SvxBhEo3eGHhNJTdWudM7Nn9z1GgT3tI5IckJKEcuopRtHVFdSWtGbZ%2Fv9JBSDm6F54mwz3huAtVxOwQVwMUFKrNtP7aSVB8%2FpsXZIfUg%2B75bHkasYi187X0g23rvXN4wSIwaIfSAV5Nx1wGzesxFb9%2FovcH34d%2BP3KJygmdE2kD83jwMNuO98oGOqUBEW4Is8666RFMwndR1qFwFzr0lA582UzTbAcJGWuPB1Zcu0Rc2PZ5tuUOtoc4nPpOBSuTMPOCNhV4mAWqxeUg0ZDxStxF0WlQz%2Bt2snKQvvW8CEsvMihZOHoFzoARp4lJTCmmb2tqm7tHIsj7IkWmOnQXebvZ1FP9eGEtUT1Y9OC7CiXZwRyyWwICwKeoyxu3ZIh%2B6bjoWb78CwoSwmy1D4QfsXWG&X-Amz-Signature=b2f7c8ff68e8544f5d075c3d50465a5b19b8d4ad70f5dad81c1611d8488ff0e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GBH3ZZ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BEzIwcCl51b5qwh6pU95IaeUDcy6DZyxCP0IpiqGKWwIgAOkNY1Jihj0eMGvn2bA1xr9XpwRB3RhCx3qw4z%2FQSdQq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDGOCNDQrqJJiaafaECrcAxStyLv2M3chMyN9N6hqMbHUYZKXM5Z5PbnER%2FbcRAM9pWVohhCoXY28roRtfC7%2FsBOdwrEgTUj3GkqH21Y1WrEARAIT90Oj%2BgVH9og3kZh102UynlKSzp%2B8NIBo0n6riPK5k2%2BQvFGVguht2CDg9acKN2o%2FG3%2BMFBqzCDKe9GLYakMV6qGQoMh5LpNKs0EmaC943xVBcpjBAPM8fI5COTSLKM5acYtFfsS5l3B4Sq%2Bzc%2BlHkHZujFOU54nmNVnYxmQEOq%2FaE%2BSxVST2VpPjrOcJyN7lRb7IsGF%2BaK5%2FR6dLq3RtU9Opi85cJfCuQKYHc2Fp%2FS3BrI8jPCCjehUKLSCKtlRrrBK8ssQll3DumMJfM4bP7FWcoKOxHfXR%2BDgStQzhLSCjUcdzUAmqBZa0wcHLeFQFPGM5R8J85duzAGwJS4Q3P6zhIL9VBx5%2BrhAfl0wCuf5Vgq72SvxBhEo3eGHhNJTdWudM7Nn9z1GgT3tI5IckJKEcuopRtHVFdSWtGbZ%2Fv9JBSDm6F54mwz3huAtVxOwQVwMUFKrNtP7aSVB8%2FpsXZIfUg%2B75bHkasYi187X0g23rvXN4wSIwaIfSAV5Nx1wGzesxFb9%2FovcH34d%2BP3KJygmdE2kD83jwMNuO98oGOqUBEW4Is8666RFMwndR1qFwFzr0lA582UzTbAcJGWuPB1Zcu0Rc2PZ5tuUOtoc4nPpOBSuTMPOCNhV4mAWqxeUg0ZDxStxF0WlQz%2Bt2snKQvvW8CEsvMihZOHoFzoARp4lJTCmmb2tqm7tHIsj7IkWmOnQXebvZ1FP9eGEtUT1Y9OC7CiXZwRyyWwICwKeoyxu3ZIh%2B6bjoWb78CwoSwmy1D4QfsXWG&X-Amz-Signature=b300fd091485fd83de1e5a99f6a41cefc60355142c6f1b56aef54aa1898888b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GBH3ZZ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BEzIwcCl51b5qwh6pU95IaeUDcy6DZyxCP0IpiqGKWwIgAOkNY1Jihj0eMGvn2bA1xr9XpwRB3RhCx3qw4z%2FQSdQq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDGOCNDQrqJJiaafaECrcAxStyLv2M3chMyN9N6hqMbHUYZKXM5Z5PbnER%2FbcRAM9pWVohhCoXY28roRtfC7%2FsBOdwrEgTUj3GkqH21Y1WrEARAIT90Oj%2BgVH9og3kZh102UynlKSzp%2B8NIBo0n6riPK5k2%2BQvFGVguht2CDg9acKN2o%2FG3%2BMFBqzCDKe9GLYakMV6qGQoMh5LpNKs0EmaC943xVBcpjBAPM8fI5COTSLKM5acYtFfsS5l3B4Sq%2Bzc%2BlHkHZujFOU54nmNVnYxmQEOq%2FaE%2BSxVST2VpPjrOcJyN7lRb7IsGF%2BaK5%2FR6dLq3RtU9Opi85cJfCuQKYHc2Fp%2FS3BrI8jPCCjehUKLSCKtlRrrBK8ssQll3DumMJfM4bP7FWcoKOxHfXR%2BDgStQzhLSCjUcdzUAmqBZa0wcHLeFQFPGM5R8J85duzAGwJS4Q3P6zhIL9VBx5%2BrhAfl0wCuf5Vgq72SvxBhEo3eGHhNJTdWudM7Nn9z1GgT3tI5IckJKEcuopRtHVFdSWtGbZ%2Fv9JBSDm6F54mwz3huAtVxOwQVwMUFKrNtP7aSVB8%2FpsXZIfUg%2B75bHkasYi187X0g23rvXN4wSIwaIfSAV5Nx1wGzesxFb9%2FovcH34d%2BP3KJygmdE2kD83jwMNuO98oGOqUBEW4Is8666RFMwndR1qFwFzr0lA582UzTbAcJGWuPB1Zcu0Rc2PZ5tuUOtoc4nPpOBSuTMPOCNhV4mAWqxeUg0ZDxStxF0WlQz%2Bt2snKQvvW8CEsvMihZOHoFzoARp4lJTCmmb2tqm7tHIsj7IkWmOnQXebvZ1FP9eGEtUT1Y9OC7CiXZwRyyWwICwKeoyxu3ZIh%2B6bjoWb78CwoSwmy1D4QfsXWG&X-Amz-Signature=c94a5e4f5e0b3af4301105b08c65ad9ff5837d9d00246517bca9bf9611fc4b54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GBH3ZZ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BEzIwcCl51b5qwh6pU95IaeUDcy6DZyxCP0IpiqGKWwIgAOkNY1Jihj0eMGvn2bA1xr9XpwRB3RhCx3qw4z%2FQSdQq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDGOCNDQrqJJiaafaECrcAxStyLv2M3chMyN9N6hqMbHUYZKXM5Z5PbnER%2FbcRAM9pWVohhCoXY28roRtfC7%2FsBOdwrEgTUj3GkqH21Y1WrEARAIT90Oj%2BgVH9og3kZh102UynlKSzp%2B8NIBo0n6riPK5k2%2BQvFGVguht2CDg9acKN2o%2FG3%2BMFBqzCDKe9GLYakMV6qGQoMh5LpNKs0EmaC943xVBcpjBAPM8fI5COTSLKM5acYtFfsS5l3B4Sq%2Bzc%2BlHkHZujFOU54nmNVnYxmQEOq%2FaE%2BSxVST2VpPjrOcJyN7lRb7IsGF%2BaK5%2FR6dLq3RtU9Opi85cJfCuQKYHc2Fp%2FS3BrI8jPCCjehUKLSCKtlRrrBK8ssQll3DumMJfM4bP7FWcoKOxHfXR%2BDgStQzhLSCjUcdzUAmqBZa0wcHLeFQFPGM5R8J85duzAGwJS4Q3P6zhIL9VBx5%2BrhAfl0wCuf5Vgq72SvxBhEo3eGHhNJTdWudM7Nn9z1GgT3tI5IckJKEcuopRtHVFdSWtGbZ%2Fv9JBSDm6F54mwz3huAtVxOwQVwMUFKrNtP7aSVB8%2FpsXZIfUg%2B75bHkasYi187X0g23rvXN4wSIwaIfSAV5Nx1wGzesxFb9%2FovcH34d%2BP3KJygmdE2kD83jwMNuO98oGOqUBEW4Is8666RFMwndR1qFwFzr0lA582UzTbAcJGWuPB1Zcu0Rc2PZ5tuUOtoc4nPpOBSuTMPOCNhV4mAWqxeUg0ZDxStxF0WlQz%2Bt2snKQvvW8CEsvMihZOHoFzoARp4lJTCmmb2tqm7tHIsj7IkWmOnQXebvZ1FP9eGEtUT1Y9OC7CiXZwRyyWwICwKeoyxu3ZIh%2B6bjoWb78CwoSwmy1D4QfsXWG&X-Amz-Signature=5582f59156f96a768440b053fae9e4675fbe2cb5de1489cdb954e79c4765f634&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

