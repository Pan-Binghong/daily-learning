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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IZQVO3L%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIBwPPbPF7K7YwSt5lvi5t3lCB6DFX8C2beAdMYV66qCPAiBmdsl4%2Frp7gNrTtTZT6yTWURLjyTwlvf9m3pFkfrLL%2FSr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMzKNwcdQfOVacBlWWKtwD8pr%2FHudGpb4AqItwio9p730wrlJK0%2F0uIUBJS9rHqA8T8fi2r5tMgRzAULIFrkz1wJW6wC1K7CKuQVdRNoXDD5s2v9qljXctxhOoiS8cLxwe%2B4pVyr14i8ZvUttpBiAr3wCcc07b68wKQAAvGi5iNLkWKrYut3Yvjn5UATAJQSGl%2FqPl%2BFS%2BVKAs4MlL6LI%2BJX%2FgacF6GSftlb0KC0Ye6ilrvjzt%2FDp2hDlLMiZlgGPmHSBR3Bv%2BfzCZ49uPC5b3h8c5WCXCZ6ZyezzG7jBs3KdDPs0WmLsLvKjsXVNGhuuUoJ3zObNiBojD3yO8mb%2F5hTO9G5CQa4FiNLhIjrBIujJfDfXxmBcDBCqPHJh6STcjW2JzD%2FhXbXI%2BpuOJ%2FrLPRnIT8c%2BXFC0GqKHCl0TlRhrYiRpY9ek%2FZiqmPJfKv0mdBpYt2TY85CW5GtjBBOrK7cV3IApgOcK8xK3qcCYXg0VYiYuG3EedKwUZib4XzziVQC62WwUqXCOwJIVkC9ZfG7ShVX1US20lYaUZE0k5RTUffMXcgkTaTKVi%2BRnZlVPRUNqmALx5%2FmI2y%2By3MDkX8fnyjPB9c6ygyiIJWaJcWNI7bRmTHPRtXKPAqtrbBJ%2Bi7m6CgOtvno%2FCfo4wr%2FynygY6pgFlS2v3aoaJNv55CIn0zj6qep5pynRzfFTTxboDYlDO6XaO1dGD73mrehzKFEGLjo%2FcizR64ZPxjBqO12LNOBG66na6ly6ao8wTi9Oz1KDRYVQVDzxRsxH7ZPYntRg07TbiL%2FCJVWIv2Ow2RdZI2BvVssid7tynSofREey21ZVlKCDe6AqKRTquWVyH5qkqx2qPILRbVmCIlheMHahPhkXqz2UDDZZX&X-Amz-Signature=6afdd7ec8e2015d9ec176bbcb76ead4ccb2a931825d0f4a7efa48078b7daee63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IZQVO3L%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIBwPPbPF7K7YwSt5lvi5t3lCB6DFX8C2beAdMYV66qCPAiBmdsl4%2Frp7gNrTtTZT6yTWURLjyTwlvf9m3pFkfrLL%2FSr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMzKNwcdQfOVacBlWWKtwD8pr%2FHudGpb4AqItwio9p730wrlJK0%2F0uIUBJS9rHqA8T8fi2r5tMgRzAULIFrkz1wJW6wC1K7CKuQVdRNoXDD5s2v9qljXctxhOoiS8cLxwe%2B4pVyr14i8ZvUttpBiAr3wCcc07b68wKQAAvGi5iNLkWKrYut3Yvjn5UATAJQSGl%2FqPl%2BFS%2BVKAs4MlL6LI%2BJX%2FgacF6GSftlb0KC0Ye6ilrvjzt%2FDp2hDlLMiZlgGPmHSBR3Bv%2BfzCZ49uPC5b3h8c5WCXCZ6ZyezzG7jBs3KdDPs0WmLsLvKjsXVNGhuuUoJ3zObNiBojD3yO8mb%2F5hTO9G5CQa4FiNLhIjrBIujJfDfXxmBcDBCqPHJh6STcjW2JzD%2FhXbXI%2BpuOJ%2FrLPRnIT8c%2BXFC0GqKHCl0TlRhrYiRpY9ek%2FZiqmPJfKv0mdBpYt2TY85CW5GtjBBOrK7cV3IApgOcK8xK3qcCYXg0VYiYuG3EedKwUZib4XzziVQC62WwUqXCOwJIVkC9ZfG7ShVX1US20lYaUZE0k5RTUffMXcgkTaTKVi%2BRnZlVPRUNqmALx5%2FmI2y%2By3MDkX8fnyjPB9c6ygyiIJWaJcWNI7bRmTHPRtXKPAqtrbBJ%2Bi7m6CgOtvno%2FCfo4wr%2FynygY6pgFlS2v3aoaJNv55CIn0zj6qep5pynRzfFTTxboDYlDO6XaO1dGD73mrehzKFEGLjo%2FcizR64ZPxjBqO12LNOBG66na6ly6ao8wTi9Oz1KDRYVQVDzxRsxH7ZPYntRg07TbiL%2FCJVWIv2Ow2RdZI2BvVssid7tynSofREey21ZVlKCDe6AqKRTquWVyH5qkqx2qPILRbVmCIlheMHahPhkXqz2UDDZZX&X-Amz-Signature=5ecad80d041cdf89e41ab544e6ee56525f9709f05928f217339a994b19fcc00f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IZQVO3L%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIBwPPbPF7K7YwSt5lvi5t3lCB6DFX8C2beAdMYV66qCPAiBmdsl4%2Frp7gNrTtTZT6yTWURLjyTwlvf9m3pFkfrLL%2FSr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMzKNwcdQfOVacBlWWKtwD8pr%2FHudGpb4AqItwio9p730wrlJK0%2F0uIUBJS9rHqA8T8fi2r5tMgRzAULIFrkz1wJW6wC1K7CKuQVdRNoXDD5s2v9qljXctxhOoiS8cLxwe%2B4pVyr14i8ZvUttpBiAr3wCcc07b68wKQAAvGi5iNLkWKrYut3Yvjn5UATAJQSGl%2FqPl%2BFS%2BVKAs4MlL6LI%2BJX%2FgacF6GSftlb0KC0Ye6ilrvjzt%2FDp2hDlLMiZlgGPmHSBR3Bv%2BfzCZ49uPC5b3h8c5WCXCZ6ZyezzG7jBs3KdDPs0WmLsLvKjsXVNGhuuUoJ3zObNiBojD3yO8mb%2F5hTO9G5CQa4FiNLhIjrBIujJfDfXxmBcDBCqPHJh6STcjW2JzD%2FhXbXI%2BpuOJ%2FrLPRnIT8c%2BXFC0GqKHCl0TlRhrYiRpY9ek%2FZiqmPJfKv0mdBpYt2TY85CW5GtjBBOrK7cV3IApgOcK8xK3qcCYXg0VYiYuG3EedKwUZib4XzziVQC62WwUqXCOwJIVkC9ZfG7ShVX1US20lYaUZE0k5RTUffMXcgkTaTKVi%2BRnZlVPRUNqmALx5%2FmI2y%2By3MDkX8fnyjPB9c6ygyiIJWaJcWNI7bRmTHPRtXKPAqtrbBJ%2Bi7m6CgOtvno%2FCfo4wr%2FynygY6pgFlS2v3aoaJNv55CIn0zj6qep5pynRzfFTTxboDYlDO6XaO1dGD73mrehzKFEGLjo%2FcizR64ZPxjBqO12LNOBG66na6ly6ao8wTi9Oz1KDRYVQVDzxRsxH7ZPYntRg07TbiL%2FCJVWIv2Ow2RdZI2BvVssid7tynSofREey21ZVlKCDe6AqKRTquWVyH5qkqx2qPILRbVmCIlheMHahPhkXqz2UDDZZX&X-Amz-Signature=e92d7ab288c8b9b47f40f4e210b8af2cf5e256f602794f2ca8a96c412e65e9d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IZQVO3L%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIBwPPbPF7K7YwSt5lvi5t3lCB6DFX8C2beAdMYV66qCPAiBmdsl4%2Frp7gNrTtTZT6yTWURLjyTwlvf9m3pFkfrLL%2FSr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMzKNwcdQfOVacBlWWKtwD8pr%2FHudGpb4AqItwio9p730wrlJK0%2F0uIUBJS9rHqA8T8fi2r5tMgRzAULIFrkz1wJW6wC1K7CKuQVdRNoXDD5s2v9qljXctxhOoiS8cLxwe%2B4pVyr14i8ZvUttpBiAr3wCcc07b68wKQAAvGi5iNLkWKrYut3Yvjn5UATAJQSGl%2FqPl%2BFS%2BVKAs4MlL6LI%2BJX%2FgacF6GSftlb0KC0Ye6ilrvjzt%2FDp2hDlLMiZlgGPmHSBR3Bv%2BfzCZ49uPC5b3h8c5WCXCZ6ZyezzG7jBs3KdDPs0WmLsLvKjsXVNGhuuUoJ3zObNiBojD3yO8mb%2F5hTO9G5CQa4FiNLhIjrBIujJfDfXxmBcDBCqPHJh6STcjW2JzD%2FhXbXI%2BpuOJ%2FrLPRnIT8c%2BXFC0GqKHCl0TlRhrYiRpY9ek%2FZiqmPJfKv0mdBpYt2TY85CW5GtjBBOrK7cV3IApgOcK8xK3qcCYXg0VYiYuG3EedKwUZib4XzziVQC62WwUqXCOwJIVkC9ZfG7ShVX1US20lYaUZE0k5RTUffMXcgkTaTKVi%2BRnZlVPRUNqmALx5%2FmI2y%2By3MDkX8fnyjPB9c6ygyiIJWaJcWNI7bRmTHPRtXKPAqtrbBJ%2Bi7m6CgOtvno%2FCfo4wr%2FynygY6pgFlS2v3aoaJNv55CIn0zj6qep5pynRzfFTTxboDYlDO6XaO1dGD73mrehzKFEGLjo%2FcizR64ZPxjBqO12LNOBG66na6ly6ao8wTi9Oz1KDRYVQVDzxRsxH7ZPYntRg07TbiL%2FCJVWIv2Ow2RdZI2BvVssid7tynSofREey21ZVlKCDe6AqKRTquWVyH5qkqx2qPILRbVmCIlheMHahPhkXqz2UDDZZX&X-Amz-Signature=d300cefd97bc3e4bad611c8bbb4bc659d3718bc57b9d1a5df86808a61fcc6d42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IZQVO3L%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIBwPPbPF7K7YwSt5lvi5t3lCB6DFX8C2beAdMYV66qCPAiBmdsl4%2Frp7gNrTtTZT6yTWURLjyTwlvf9m3pFkfrLL%2FSr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMzKNwcdQfOVacBlWWKtwD8pr%2FHudGpb4AqItwio9p730wrlJK0%2F0uIUBJS9rHqA8T8fi2r5tMgRzAULIFrkz1wJW6wC1K7CKuQVdRNoXDD5s2v9qljXctxhOoiS8cLxwe%2B4pVyr14i8ZvUttpBiAr3wCcc07b68wKQAAvGi5iNLkWKrYut3Yvjn5UATAJQSGl%2FqPl%2BFS%2BVKAs4MlL6LI%2BJX%2FgacF6GSftlb0KC0Ye6ilrvjzt%2FDp2hDlLMiZlgGPmHSBR3Bv%2BfzCZ49uPC5b3h8c5WCXCZ6ZyezzG7jBs3KdDPs0WmLsLvKjsXVNGhuuUoJ3zObNiBojD3yO8mb%2F5hTO9G5CQa4FiNLhIjrBIujJfDfXxmBcDBCqPHJh6STcjW2JzD%2FhXbXI%2BpuOJ%2FrLPRnIT8c%2BXFC0GqKHCl0TlRhrYiRpY9ek%2FZiqmPJfKv0mdBpYt2TY85CW5GtjBBOrK7cV3IApgOcK8xK3qcCYXg0VYiYuG3EedKwUZib4XzziVQC62WwUqXCOwJIVkC9ZfG7ShVX1US20lYaUZE0k5RTUffMXcgkTaTKVi%2BRnZlVPRUNqmALx5%2FmI2y%2By3MDkX8fnyjPB9c6ygyiIJWaJcWNI7bRmTHPRtXKPAqtrbBJ%2Bi7m6CgOtvno%2FCfo4wr%2FynygY6pgFlS2v3aoaJNv55CIn0zj6qep5pynRzfFTTxboDYlDO6XaO1dGD73mrehzKFEGLjo%2FcizR64ZPxjBqO12LNOBG66na6ly6ao8wTi9Oz1KDRYVQVDzxRsxH7ZPYntRg07TbiL%2FCJVWIv2Ow2RdZI2BvVssid7tynSofREey21ZVlKCDe6AqKRTquWVyH5qkqx2qPILRbVmCIlheMHahPhkXqz2UDDZZX&X-Amz-Signature=f80bbf26b2453fdc121b97756fe7f18372d22203c98cb9c3b1c441061fd7e02b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IZQVO3L%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIBwPPbPF7K7YwSt5lvi5t3lCB6DFX8C2beAdMYV66qCPAiBmdsl4%2Frp7gNrTtTZT6yTWURLjyTwlvf9m3pFkfrLL%2FSr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMzKNwcdQfOVacBlWWKtwD8pr%2FHudGpb4AqItwio9p730wrlJK0%2F0uIUBJS9rHqA8T8fi2r5tMgRzAULIFrkz1wJW6wC1K7CKuQVdRNoXDD5s2v9qljXctxhOoiS8cLxwe%2B4pVyr14i8ZvUttpBiAr3wCcc07b68wKQAAvGi5iNLkWKrYut3Yvjn5UATAJQSGl%2FqPl%2BFS%2BVKAs4MlL6LI%2BJX%2FgacF6GSftlb0KC0Ye6ilrvjzt%2FDp2hDlLMiZlgGPmHSBR3Bv%2BfzCZ49uPC5b3h8c5WCXCZ6ZyezzG7jBs3KdDPs0WmLsLvKjsXVNGhuuUoJ3zObNiBojD3yO8mb%2F5hTO9G5CQa4FiNLhIjrBIujJfDfXxmBcDBCqPHJh6STcjW2JzD%2FhXbXI%2BpuOJ%2FrLPRnIT8c%2BXFC0GqKHCl0TlRhrYiRpY9ek%2FZiqmPJfKv0mdBpYt2TY85CW5GtjBBOrK7cV3IApgOcK8xK3qcCYXg0VYiYuG3EedKwUZib4XzziVQC62WwUqXCOwJIVkC9ZfG7ShVX1US20lYaUZE0k5RTUffMXcgkTaTKVi%2BRnZlVPRUNqmALx5%2FmI2y%2By3MDkX8fnyjPB9c6ygyiIJWaJcWNI7bRmTHPRtXKPAqtrbBJ%2Bi7m6CgOtvno%2FCfo4wr%2FynygY6pgFlS2v3aoaJNv55CIn0zj6qep5pynRzfFTTxboDYlDO6XaO1dGD73mrehzKFEGLjo%2FcizR64ZPxjBqO12LNOBG66na6ly6ao8wTi9Oz1KDRYVQVDzxRsxH7ZPYntRg07TbiL%2FCJVWIv2Ow2RdZI2BvVssid7tynSofREey21ZVlKCDe6AqKRTquWVyH5qkqx2qPILRbVmCIlheMHahPhkXqz2UDDZZX&X-Amz-Signature=4f3be2ca6572622c46183f32a5a309fbf0fb4907570eedd5e3a4c55b3c48b27e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IZQVO3L%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIBwPPbPF7K7YwSt5lvi5t3lCB6DFX8C2beAdMYV66qCPAiBmdsl4%2Frp7gNrTtTZT6yTWURLjyTwlvf9m3pFkfrLL%2FSr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMzKNwcdQfOVacBlWWKtwD8pr%2FHudGpb4AqItwio9p730wrlJK0%2F0uIUBJS9rHqA8T8fi2r5tMgRzAULIFrkz1wJW6wC1K7CKuQVdRNoXDD5s2v9qljXctxhOoiS8cLxwe%2B4pVyr14i8ZvUttpBiAr3wCcc07b68wKQAAvGi5iNLkWKrYut3Yvjn5UATAJQSGl%2FqPl%2BFS%2BVKAs4MlL6LI%2BJX%2FgacF6GSftlb0KC0Ye6ilrvjzt%2FDp2hDlLMiZlgGPmHSBR3Bv%2BfzCZ49uPC5b3h8c5WCXCZ6ZyezzG7jBs3KdDPs0WmLsLvKjsXVNGhuuUoJ3zObNiBojD3yO8mb%2F5hTO9G5CQa4FiNLhIjrBIujJfDfXxmBcDBCqPHJh6STcjW2JzD%2FhXbXI%2BpuOJ%2FrLPRnIT8c%2BXFC0GqKHCl0TlRhrYiRpY9ek%2FZiqmPJfKv0mdBpYt2TY85CW5GtjBBOrK7cV3IApgOcK8xK3qcCYXg0VYiYuG3EedKwUZib4XzziVQC62WwUqXCOwJIVkC9ZfG7ShVX1US20lYaUZE0k5RTUffMXcgkTaTKVi%2BRnZlVPRUNqmALx5%2FmI2y%2By3MDkX8fnyjPB9c6ygyiIJWaJcWNI7bRmTHPRtXKPAqtrbBJ%2Bi7m6CgOtvno%2FCfo4wr%2FynygY6pgFlS2v3aoaJNv55CIn0zj6qep5pynRzfFTTxboDYlDO6XaO1dGD73mrehzKFEGLjo%2FcizR64ZPxjBqO12LNOBG66na6ly6ao8wTi9Oz1KDRYVQVDzxRsxH7ZPYntRg07TbiL%2FCJVWIv2Ow2RdZI2BvVssid7tynSofREey21ZVlKCDe6AqKRTquWVyH5qkqx2qPILRbVmCIlheMHahPhkXqz2UDDZZX&X-Amz-Signature=b51dd969d55f3b284a2a347024a29616fbd42a04399ab2d10b581977bd38c5c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IZQVO3L%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIBwPPbPF7K7YwSt5lvi5t3lCB6DFX8C2beAdMYV66qCPAiBmdsl4%2Frp7gNrTtTZT6yTWURLjyTwlvf9m3pFkfrLL%2FSr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMzKNwcdQfOVacBlWWKtwD8pr%2FHudGpb4AqItwio9p730wrlJK0%2F0uIUBJS9rHqA8T8fi2r5tMgRzAULIFrkz1wJW6wC1K7CKuQVdRNoXDD5s2v9qljXctxhOoiS8cLxwe%2B4pVyr14i8ZvUttpBiAr3wCcc07b68wKQAAvGi5iNLkWKrYut3Yvjn5UATAJQSGl%2FqPl%2BFS%2BVKAs4MlL6LI%2BJX%2FgacF6GSftlb0KC0Ye6ilrvjzt%2FDp2hDlLMiZlgGPmHSBR3Bv%2BfzCZ49uPC5b3h8c5WCXCZ6ZyezzG7jBs3KdDPs0WmLsLvKjsXVNGhuuUoJ3zObNiBojD3yO8mb%2F5hTO9G5CQa4FiNLhIjrBIujJfDfXxmBcDBCqPHJh6STcjW2JzD%2FhXbXI%2BpuOJ%2FrLPRnIT8c%2BXFC0GqKHCl0TlRhrYiRpY9ek%2FZiqmPJfKv0mdBpYt2TY85CW5GtjBBOrK7cV3IApgOcK8xK3qcCYXg0VYiYuG3EedKwUZib4XzziVQC62WwUqXCOwJIVkC9ZfG7ShVX1US20lYaUZE0k5RTUffMXcgkTaTKVi%2BRnZlVPRUNqmALx5%2FmI2y%2By3MDkX8fnyjPB9c6ygyiIJWaJcWNI7bRmTHPRtXKPAqtrbBJ%2Bi7m6CgOtvno%2FCfo4wr%2FynygY6pgFlS2v3aoaJNv55CIn0zj6qep5pynRzfFTTxboDYlDO6XaO1dGD73mrehzKFEGLjo%2FcizR64ZPxjBqO12LNOBG66na6ly6ao8wTi9Oz1KDRYVQVDzxRsxH7ZPYntRg07TbiL%2FCJVWIv2Ow2RdZI2BvVssid7tynSofREey21ZVlKCDe6AqKRTquWVyH5qkqx2qPILRbVmCIlheMHahPhkXqz2UDDZZX&X-Amz-Signature=ad349e45e52e32645fc3d2daffc88063fb27d60386cb88baf8ed48dbed4920d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IZQVO3L%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIBwPPbPF7K7YwSt5lvi5t3lCB6DFX8C2beAdMYV66qCPAiBmdsl4%2Frp7gNrTtTZT6yTWURLjyTwlvf9m3pFkfrLL%2FSr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMzKNwcdQfOVacBlWWKtwD8pr%2FHudGpb4AqItwio9p730wrlJK0%2F0uIUBJS9rHqA8T8fi2r5tMgRzAULIFrkz1wJW6wC1K7CKuQVdRNoXDD5s2v9qljXctxhOoiS8cLxwe%2B4pVyr14i8ZvUttpBiAr3wCcc07b68wKQAAvGi5iNLkWKrYut3Yvjn5UATAJQSGl%2FqPl%2BFS%2BVKAs4MlL6LI%2BJX%2FgacF6GSftlb0KC0Ye6ilrvjzt%2FDp2hDlLMiZlgGPmHSBR3Bv%2BfzCZ49uPC5b3h8c5WCXCZ6ZyezzG7jBs3KdDPs0WmLsLvKjsXVNGhuuUoJ3zObNiBojD3yO8mb%2F5hTO9G5CQa4FiNLhIjrBIujJfDfXxmBcDBCqPHJh6STcjW2JzD%2FhXbXI%2BpuOJ%2FrLPRnIT8c%2BXFC0GqKHCl0TlRhrYiRpY9ek%2FZiqmPJfKv0mdBpYt2TY85CW5GtjBBOrK7cV3IApgOcK8xK3qcCYXg0VYiYuG3EedKwUZib4XzziVQC62WwUqXCOwJIVkC9ZfG7ShVX1US20lYaUZE0k5RTUffMXcgkTaTKVi%2BRnZlVPRUNqmALx5%2FmI2y%2By3MDkX8fnyjPB9c6ygyiIJWaJcWNI7bRmTHPRtXKPAqtrbBJ%2Bi7m6CgOtvno%2FCfo4wr%2FynygY6pgFlS2v3aoaJNv55CIn0zj6qep5pynRzfFTTxboDYlDO6XaO1dGD73mrehzKFEGLjo%2FcizR64ZPxjBqO12LNOBG66na6ly6ao8wTi9Oz1KDRYVQVDzxRsxH7ZPYntRg07TbiL%2FCJVWIv2Ow2RdZI2BvVssid7tynSofREey21ZVlKCDe6AqKRTquWVyH5qkqx2qPILRbVmCIlheMHahPhkXqz2UDDZZX&X-Amz-Signature=444d9ef46cfcacfb473f3cfed6ce3df9d41cfc0076a9b04313d99b58845bc4f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IZQVO3L%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIBwPPbPF7K7YwSt5lvi5t3lCB6DFX8C2beAdMYV66qCPAiBmdsl4%2Frp7gNrTtTZT6yTWURLjyTwlvf9m3pFkfrLL%2FSr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMzKNwcdQfOVacBlWWKtwD8pr%2FHudGpb4AqItwio9p730wrlJK0%2F0uIUBJS9rHqA8T8fi2r5tMgRzAULIFrkz1wJW6wC1K7CKuQVdRNoXDD5s2v9qljXctxhOoiS8cLxwe%2B4pVyr14i8ZvUttpBiAr3wCcc07b68wKQAAvGi5iNLkWKrYut3Yvjn5UATAJQSGl%2FqPl%2BFS%2BVKAs4MlL6LI%2BJX%2FgacF6GSftlb0KC0Ye6ilrvjzt%2FDp2hDlLMiZlgGPmHSBR3Bv%2BfzCZ49uPC5b3h8c5WCXCZ6ZyezzG7jBs3KdDPs0WmLsLvKjsXVNGhuuUoJ3zObNiBojD3yO8mb%2F5hTO9G5CQa4FiNLhIjrBIujJfDfXxmBcDBCqPHJh6STcjW2JzD%2FhXbXI%2BpuOJ%2FrLPRnIT8c%2BXFC0GqKHCl0TlRhrYiRpY9ek%2FZiqmPJfKv0mdBpYt2TY85CW5GtjBBOrK7cV3IApgOcK8xK3qcCYXg0VYiYuG3EedKwUZib4XzziVQC62WwUqXCOwJIVkC9ZfG7ShVX1US20lYaUZE0k5RTUffMXcgkTaTKVi%2BRnZlVPRUNqmALx5%2FmI2y%2By3MDkX8fnyjPB9c6ygyiIJWaJcWNI7bRmTHPRtXKPAqtrbBJ%2Bi7m6CgOtvno%2FCfo4wr%2FynygY6pgFlS2v3aoaJNv55CIn0zj6qep5pynRzfFTTxboDYlDO6XaO1dGD73mrehzKFEGLjo%2FcizR64ZPxjBqO12LNOBG66na6ly6ao8wTi9Oz1KDRYVQVDzxRsxH7ZPYntRg07TbiL%2FCJVWIv2Ow2RdZI2BvVssid7tynSofREey21ZVlKCDe6AqKRTquWVyH5qkqx2qPILRbVmCIlheMHahPhkXqz2UDDZZX&X-Amz-Signature=af615b8848f253191174334d825a6320a0b3ebf12a0202d81949592cdb5a09ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

