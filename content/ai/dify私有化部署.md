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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/f74139a7-e3a8-448f-8ecc-ce9bee8e5977/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MZOE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDUhHWOJ%2FbPkQi%2BY7r%2B1lSOV8LoUKLn2YodtgACbbRkTwIhAMPcJVuenao9ePSMjQ%2F3LJIHT8FMQKHNKoaH%2F5vtB3%2FRKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtnquPgloxy4LzWcgq3AM0AmJpoPhGv%2F6PmpjgvIlQm8ES1MfbrTzIGXZE50UcCiSsU%2F2qru4Px1M8wOEJY8nbivPL1CWJn5pUMF2eZbuCUc11bcqLqhqypYNiFL17bzq1jrb67ggeem%2BYMyCVYG9Xi%2B9qB8%2BIHBq%2BeWGd7JPgdy0Nax67nuZG6kxYxCeYqrUZuN%2FuanZA%2F9IMlbbQwXZR4AMZbI8NSXfGNxYNBTuCNUigc%2BbxiDy0KRsE7ozq7yhIDjolGINPyixqbbM6cQEEXA42zQPdX9pbEoJTlL%2FTbvRYwCxvt0%2BlHX5Rf9trjqwCMtcp08wrSo0qY3Ram%2FBAKUCy2X%2FT4XUmtAx2P2LU4iBJ8cHmVkZDx3JJiD7kmUwj6MHbkKpgs2q3Egl4RQ33yP42SS7Tm%2Fw7W277Jhz3bIkCvmWzEL%2Fgr8FFbjpxEh63WfIOtmMtt66uyStPOK2z25MMY3vxXNqD4moSLJl4C7jtkRK917SYmVDt6PzYdcCobnHGH99EDtNL0SW9c3sTpy1%2FKpWPyh4Gvpm0Df3Q4oooTZz7eQx9j5Mp%2Fo7po4tBeM7QNboj8yZuBpczFadVRFzmiJ9zxOXntCHsQulwmI5J7Z91y47xcmzp%2BxKT5TqD8Xd6PwdOAdXlaDDy7cDPBjqkARxtzcF720CZyPm%2FcMB2RywjcUpYBpgWOito3vWfpU55zxCUhtbGc%2FVFCVzhF%2BOS3G7FMD%2F6r3jEOcHp0pwW47E4MRglpccq2twFwuSOKBBTY82ztA3BnEzSeIjXIZg86laOVcVS2t29zEaCaM6knTfOJwOViDdGcqntP8T4QynXRdwfAZm%2FN22tmopZXZwiigt3finmSE1s1krxIzcnPhtMQYsK&X-Amz-Signature=b3753db2f1e216ef9bb50e0f868f1056719c5ea6ad42f590ad01b8ccddb9e3a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



无论是在本地的服务器还是在网上的服务器（阿里云，腾讯云，天翼云…）都要满足这个配置,至少要有2个cpu核心并且有4g的内存

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fa9b78cc-a1fb-4411-9a98-78111a3badf7/946a4c0a5fbcb748a6abe213a5069d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MZOE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDUhHWOJ%2FbPkQi%2BY7r%2B1lSOV8LoUKLn2YodtgACbbRkTwIhAMPcJVuenao9ePSMjQ%2F3LJIHT8FMQKHNKoaH%2F5vtB3%2FRKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtnquPgloxy4LzWcgq3AM0AmJpoPhGv%2F6PmpjgvIlQm8ES1MfbrTzIGXZE50UcCiSsU%2F2qru4Px1M8wOEJY8nbivPL1CWJn5pUMF2eZbuCUc11bcqLqhqypYNiFL17bzq1jrb67ggeem%2BYMyCVYG9Xi%2B9qB8%2BIHBq%2BeWGd7JPgdy0Nax67nuZG6kxYxCeYqrUZuN%2FuanZA%2F9IMlbbQwXZR4AMZbI8NSXfGNxYNBTuCNUigc%2BbxiDy0KRsE7ozq7yhIDjolGINPyixqbbM6cQEEXA42zQPdX9pbEoJTlL%2FTbvRYwCxvt0%2BlHX5Rf9trjqwCMtcp08wrSo0qY3Ram%2FBAKUCy2X%2FT4XUmtAx2P2LU4iBJ8cHmVkZDx3JJiD7kmUwj6MHbkKpgs2q3Egl4RQ33yP42SS7Tm%2Fw7W277Jhz3bIkCvmWzEL%2Fgr8FFbjpxEh63WfIOtmMtt66uyStPOK2z25MMY3vxXNqD4moSLJl4C7jtkRK917SYmVDt6PzYdcCobnHGH99EDtNL0SW9c3sTpy1%2FKpWPyh4Gvpm0Df3Q4oooTZz7eQx9j5Mp%2Fo7po4tBeM7QNboj8yZuBpczFadVRFzmiJ9zxOXntCHsQulwmI5J7Z91y47xcmzp%2BxKT5TqD8Xd6PwdOAdXlaDDy7cDPBjqkARxtzcF720CZyPm%2FcMB2RywjcUpYBpgWOito3vWfpU55zxCUhtbGc%2FVFCVzhF%2BOS3G7FMD%2F6r3jEOcHp0pwW47E4MRglpccq2twFwuSOKBBTY82ztA3BnEzSeIjXIZg86laOVcVS2t29zEaCaM6knTfOJwOViDdGcqntP8T4QynXRdwfAZm%2FN22tmopZXZwiigt3finmSE1s1krxIzcnPhtMQYsK&X-Amz-Signature=945debfbe8d8ced43ac5425df3819744fe823479073826b74d3bdb7637547225&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863dda37-caa8-476d-8c6d-2b77deddf378/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MZOE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDUhHWOJ%2FbPkQi%2BY7r%2B1lSOV8LoUKLn2YodtgACbbRkTwIhAMPcJVuenao9ePSMjQ%2F3LJIHT8FMQKHNKoaH%2F5vtB3%2FRKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtnquPgloxy4LzWcgq3AM0AmJpoPhGv%2F6PmpjgvIlQm8ES1MfbrTzIGXZE50UcCiSsU%2F2qru4Px1M8wOEJY8nbivPL1CWJn5pUMF2eZbuCUc11bcqLqhqypYNiFL17bzq1jrb67ggeem%2BYMyCVYG9Xi%2B9qB8%2BIHBq%2BeWGd7JPgdy0Nax67nuZG6kxYxCeYqrUZuN%2FuanZA%2F9IMlbbQwXZR4AMZbI8NSXfGNxYNBTuCNUigc%2BbxiDy0KRsE7ozq7yhIDjolGINPyixqbbM6cQEEXA42zQPdX9pbEoJTlL%2FTbvRYwCxvt0%2BlHX5Rf9trjqwCMtcp08wrSo0qY3Ram%2FBAKUCy2X%2FT4XUmtAx2P2LU4iBJ8cHmVkZDx3JJiD7kmUwj6MHbkKpgs2q3Egl4RQ33yP42SS7Tm%2Fw7W277Jhz3bIkCvmWzEL%2Fgr8FFbjpxEh63WfIOtmMtt66uyStPOK2z25MMY3vxXNqD4moSLJl4C7jtkRK917SYmVDt6PzYdcCobnHGH99EDtNL0SW9c3sTpy1%2FKpWPyh4Gvpm0Df3Q4oooTZz7eQx9j5Mp%2Fo7po4tBeM7QNboj8yZuBpczFadVRFzmiJ9zxOXntCHsQulwmI5J7Z91y47xcmzp%2BxKT5TqD8Xd6PwdOAdXlaDDy7cDPBjqkARxtzcF720CZyPm%2FcMB2RywjcUpYBpgWOito3vWfpU55zxCUhtbGc%2FVFCVzhF%2BOS3G7FMD%2F6r3jEOcHp0pwW47E4MRglpccq2twFwuSOKBBTY82ztA3BnEzSeIjXIZg86laOVcVS2t29zEaCaM6knTfOJwOViDdGcqntP8T4QynXRdwfAZm%2FN22tmopZXZwiigt3finmSE1s1krxIzcnPhtMQYsK&X-Amz-Signature=1961378412481fb1ce7e82e365e51063f8fb8d71bca46a1fc79546f25ddd6d14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3141a330-4da5-47d2-ba61-e70f1eac99d8/d2efba5c7c0b16e6a7acff2b62f81b4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MZOE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDUhHWOJ%2FbPkQi%2BY7r%2B1lSOV8LoUKLn2YodtgACbbRkTwIhAMPcJVuenao9ePSMjQ%2F3LJIHT8FMQKHNKoaH%2F5vtB3%2FRKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtnquPgloxy4LzWcgq3AM0AmJpoPhGv%2F6PmpjgvIlQm8ES1MfbrTzIGXZE50UcCiSsU%2F2qru4Px1M8wOEJY8nbivPL1CWJn5pUMF2eZbuCUc11bcqLqhqypYNiFL17bzq1jrb67ggeem%2BYMyCVYG9Xi%2B9qB8%2BIHBq%2BeWGd7JPgdy0Nax67nuZG6kxYxCeYqrUZuN%2FuanZA%2F9IMlbbQwXZR4AMZbI8NSXfGNxYNBTuCNUigc%2BbxiDy0KRsE7ozq7yhIDjolGINPyixqbbM6cQEEXA42zQPdX9pbEoJTlL%2FTbvRYwCxvt0%2BlHX5Rf9trjqwCMtcp08wrSo0qY3Ram%2FBAKUCy2X%2FT4XUmtAx2P2LU4iBJ8cHmVkZDx3JJiD7kmUwj6MHbkKpgs2q3Egl4RQ33yP42SS7Tm%2Fw7W277Jhz3bIkCvmWzEL%2Fgr8FFbjpxEh63WfIOtmMtt66uyStPOK2z25MMY3vxXNqD4moSLJl4C7jtkRK917SYmVDt6PzYdcCobnHGH99EDtNL0SW9c3sTpy1%2FKpWPyh4Gvpm0Df3Q4oooTZz7eQx9j5Mp%2Fo7po4tBeM7QNboj8yZuBpczFadVRFzmiJ9zxOXntCHsQulwmI5J7Z91y47xcmzp%2BxKT5TqD8Xd6PwdOAdXlaDDy7cDPBjqkARxtzcF720CZyPm%2FcMB2RywjcUpYBpgWOito3vWfpU55zxCUhtbGc%2FVFCVzhF%2BOS3G7FMD%2F6r3jEOcHp0pwW47E4MRglpccq2twFwuSOKBBTY82ztA3BnEzSeIjXIZg86laOVcVS2t29zEaCaM6knTfOJwOViDdGcqntP8T4QynXRdwfAZm%2FN22tmopZXZwiigt3finmSE1s1krxIzcnPhtMQYsK&X-Amz-Signature=a79cddfc12e9b3f79bdd2cde52fd9fe32d7b3fd6b29852a6dd17a542e8f33c04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



## 访问Dify

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/92cfa41b-56dc-4eda-a755-74807fd82049/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MZOE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDUhHWOJ%2FbPkQi%2BY7r%2B1lSOV8LoUKLn2YodtgACbbRkTwIhAMPcJVuenao9ePSMjQ%2F3LJIHT8FMQKHNKoaH%2F5vtB3%2FRKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtnquPgloxy4LzWcgq3AM0AmJpoPhGv%2F6PmpjgvIlQm8ES1MfbrTzIGXZE50UcCiSsU%2F2qru4Px1M8wOEJY8nbivPL1CWJn5pUMF2eZbuCUc11bcqLqhqypYNiFL17bzq1jrb67ggeem%2BYMyCVYG9Xi%2B9qB8%2BIHBq%2BeWGd7JPgdy0Nax67nuZG6kxYxCeYqrUZuN%2FuanZA%2F9IMlbbQwXZR4AMZbI8NSXfGNxYNBTuCNUigc%2BbxiDy0KRsE7ozq7yhIDjolGINPyixqbbM6cQEEXA42zQPdX9pbEoJTlL%2FTbvRYwCxvt0%2BlHX5Rf9trjqwCMtcp08wrSo0qY3Ram%2FBAKUCy2X%2FT4XUmtAx2P2LU4iBJ8cHmVkZDx3JJiD7kmUwj6MHbkKpgs2q3Egl4RQ33yP42SS7Tm%2Fw7W277Jhz3bIkCvmWzEL%2Fgr8FFbjpxEh63WfIOtmMtt66uyStPOK2z25MMY3vxXNqD4moSLJl4C7jtkRK917SYmVDt6PzYdcCobnHGH99EDtNL0SW9c3sTpy1%2FKpWPyh4Gvpm0Df3Q4oooTZz7eQx9j5Mp%2Fo7po4tBeM7QNboj8yZuBpczFadVRFzmiJ9zxOXntCHsQulwmI5J7Z91y47xcmzp%2BxKT5TqD8Xd6PwdOAdXlaDDy7cDPBjqkARxtzcF720CZyPm%2FcMB2RywjcUpYBpgWOito3vWfpU55zxCUhtbGc%2FVFCVzhF%2BOS3G7FMD%2F6r3jEOcHp0pwW47E4MRglpccq2twFwuSOKBBTY82ztA3BnEzSeIjXIZg86laOVcVS2t29zEaCaM6knTfOJwOViDdGcqntP8T4QynXRdwfAZm%2FN22tmopZXZwiigt3finmSE1s1krxIzcnPhtMQYsK&X-Amz-Signature=3b688a9d2feec0d1bde9d5cb717338b2a50606a569bfb0814fcd9b21f2717b59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



# 5.端口注意事项

如果我们的镜像全部拉下来并且全部运行，进入http://your_server_ip/install发现打不开，这很有可能是端口的问题

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/55ab71b1-7944-486e-93d4-d0022f21c927/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MZOE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDUhHWOJ%2FbPkQi%2BY7r%2B1lSOV8LoUKLn2YodtgACbbRkTwIhAMPcJVuenao9ePSMjQ%2F3LJIHT8FMQKHNKoaH%2F5vtB3%2FRKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtnquPgloxy4LzWcgq3AM0AmJpoPhGv%2F6PmpjgvIlQm8ES1MfbrTzIGXZE50UcCiSsU%2F2qru4Px1M8wOEJY8nbivPL1CWJn5pUMF2eZbuCUc11bcqLqhqypYNiFL17bzq1jrb67ggeem%2BYMyCVYG9Xi%2B9qB8%2BIHBq%2BeWGd7JPgdy0Nax67nuZG6kxYxCeYqrUZuN%2FuanZA%2F9IMlbbQwXZR4AMZbI8NSXfGNxYNBTuCNUigc%2BbxiDy0KRsE7ozq7yhIDjolGINPyixqbbM6cQEEXA42zQPdX9pbEoJTlL%2FTbvRYwCxvt0%2BlHX5Rf9trjqwCMtcp08wrSo0qY3Ram%2FBAKUCy2X%2FT4XUmtAx2P2LU4iBJ8cHmVkZDx3JJiD7kmUwj6MHbkKpgs2q3Egl4RQ33yP42SS7Tm%2Fw7W277Jhz3bIkCvmWzEL%2Fgr8FFbjpxEh63WfIOtmMtt66uyStPOK2z25MMY3vxXNqD4moSLJl4C7jtkRK917SYmVDt6PzYdcCobnHGH99EDtNL0SW9c3sTpy1%2FKpWPyh4Gvpm0Df3Q4oooTZz7eQx9j5Mp%2Fo7po4tBeM7QNboj8yZuBpczFadVRFzmiJ9zxOXntCHsQulwmI5J7Z91y47xcmzp%2BxKT5TqD8Xd6PwdOAdXlaDDy7cDPBjqkARxtzcF720CZyPm%2FcMB2RywjcUpYBpgWOito3vWfpU55zxCUhtbGc%2FVFCVzhF%2BOS3G7FMD%2F6r3jEOcHp0pwW47E4MRglpccq2twFwuSOKBBTY82ztA3BnEzSeIjXIZg86laOVcVS2t29zEaCaM6knTfOJwOViDdGcqntP8T4QynXRdwfAZm%2FN22tmopZXZwiigt3finmSE1s1krxIzcnPhtMQYsK&X-Amz-Signature=9c18d668bb8330f8be6b739ca2fc3a0e2dd29ae41a91943af0aec34c5db34d6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



所以我们要解决端口问题，如果你用的腾讯云，阿里云等等，我们在安全组配置里把80和433端口打开

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d5aeaa97-70dc-46c2-8a9c-f3863bebf45d/40ef88873b101899d4fbb11e8575789.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MZOE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDUhHWOJ%2FbPkQi%2BY7r%2B1lSOV8LoUKLn2YodtgACbbRkTwIhAMPcJVuenao9ePSMjQ%2F3LJIHT8FMQKHNKoaH%2F5vtB3%2FRKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtnquPgloxy4LzWcgq3AM0AmJpoPhGv%2F6PmpjgvIlQm8ES1MfbrTzIGXZE50UcCiSsU%2F2qru4Px1M8wOEJY8nbivPL1CWJn5pUMF2eZbuCUc11bcqLqhqypYNiFL17bzq1jrb67ggeem%2BYMyCVYG9Xi%2B9qB8%2BIHBq%2BeWGd7JPgdy0Nax67nuZG6kxYxCeYqrUZuN%2FuanZA%2F9IMlbbQwXZR4AMZbI8NSXfGNxYNBTuCNUigc%2BbxiDy0KRsE7ozq7yhIDjolGINPyixqbbM6cQEEXA42zQPdX9pbEoJTlL%2FTbvRYwCxvt0%2BlHX5Rf9trjqwCMtcp08wrSo0qY3Ram%2FBAKUCy2X%2FT4XUmtAx2P2LU4iBJ8cHmVkZDx3JJiD7kmUwj6MHbkKpgs2q3Egl4RQ33yP42SS7Tm%2Fw7W277Jhz3bIkCvmWzEL%2Fgr8FFbjpxEh63WfIOtmMtt66uyStPOK2z25MMY3vxXNqD4moSLJl4C7jtkRK917SYmVDt6PzYdcCobnHGH99EDtNL0SW9c3sTpy1%2FKpWPyh4Gvpm0Df3Q4oooTZz7eQx9j5Mp%2Fo7po4tBeM7QNboj8yZuBpczFadVRFzmiJ9zxOXntCHsQulwmI5J7Z91y47xcmzp%2BxKT5TqD8Xd6PwdOAdXlaDDy7cDPBjqkARxtzcF720CZyPm%2FcMB2RywjcUpYBpgWOito3vWfpU55zxCUhtbGc%2FVFCVzhF%2BOS3G7FMD%2F6r3jEOcHp0pwW47E4MRglpccq2twFwuSOKBBTY82ztA3BnEzSeIjXIZg86laOVcVS2t29zEaCaM6knTfOJwOViDdGcqntP8T4QynXRdwfAZm%2FN22tmopZXZwiigt3finmSE1s1krxIzcnPhtMQYsK&X-Amz-Signature=cebd6c37ad10ae0d555eab051c4e87e0cf82db01f4b1b4dd49c42dc133df9842&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

如果我们用的其他平台（天翼云….）就要我们更改配置文件docker-compose.yaml和.env文件

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12b65748-58a4-4ea2-a594-2bf08ecea6d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MZOE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDUhHWOJ%2FbPkQi%2BY7r%2B1lSOV8LoUKLn2YodtgACbbRkTwIhAMPcJVuenao9ePSMjQ%2F3LJIHT8FMQKHNKoaH%2F5vtB3%2FRKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtnquPgloxy4LzWcgq3AM0AmJpoPhGv%2F6PmpjgvIlQm8ES1MfbrTzIGXZE50UcCiSsU%2F2qru4Px1M8wOEJY8nbivPL1CWJn5pUMF2eZbuCUc11bcqLqhqypYNiFL17bzq1jrb67ggeem%2BYMyCVYG9Xi%2B9qB8%2BIHBq%2BeWGd7JPgdy0Nax67nuZG6kxYxCeYqrUZuN%2FuanZA%2F9IMlbbQwXZR4AMZbI8NSXfGNxYNBTuCNUigc%2BbxiDy0KRsE7ozq7yhIDjolGINPyixqbbM6cQEEXA42zQPdX9pbEoJTlL%2FTbvRYwCxvt0%2BlHX5Rf9trjqwCMtcp08wrSo0qY3Ram%2FBAKUCy2X%2FT4XUmtAx2P2LU4iBJ8cHmVkZDx3JJiD7kmUwj6MHbkKpgs2q3Egl4RQ33yP42SS7Tm%2Fw7W277Jhz3bIkCvmWzEL%2Fgr8FFbjpxEh63WfIOtmMtt66uyStPOK2z25MMY3vxXNqD4moSLJl4C7jtkRK917SYmVDt6PzYdcCobnHGH99EDtNL0SW9c3sTpy1%2FKpWPyh4Gvpm0Df3Q4oooTZz7eQx9j5Mp%2Fo7po4tBeM7QNboj8yZuBpczFadVRFzmiJ9zxOXntCHsQulwmI5J7Z91y47xcmzp%2BxKT5TqD8Xd6PwdOAdXlaDDy7cDPBjqkARxtzcF720CZyPm%2FcMB2RywjcUpYBpgWOito3vWfpU55zxCUhtbGc%2FVFCVzhF%2BOS3G7FMD%2F6r3jEOcHp0pwW47E4MRglpccq2twFwuSOKBBTY82ztA3BnEzSeIjXIZg86laOVcVS2t29zEaCaM6knTfOJwOViDdGcqntP8T4QynXRdwfAZm%2FN22tmopZXZwiigt3finmSE1s1krxIzcnPhtMQYsK&X-Amz-Signature=b0b1f320ce4d6e1169a4d597f98381fa2d0622d2dffbb33c030ee97a184d5352&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



首先来改docker-compose.yaml文件

```javascript
cd dify/docker

vim docker-compose.yaml
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/568fa06e-1eaa-49a1-a5f7-dabc3559d265/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MZOE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDUhHWOJ%2FbPkQi%2BY7r%2B1lSOV8LoUKLn2YodtgACbbRkTwIhAMPcJVuenao9ePSMjQ%2F3LJIHT8FMQKHNKoaH%2F5vtB3%2FRKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtnquPgloxy4LzWcgq3AM0AmJpoPhGv%2F6PmpjgvIlQm8ES1MfbrTzIGXZE50UcCiSsU%2F2qru4Px1M8wOEJY8nbivPL1CWJn5pUMF2eZbuCUc11bcqLqhqypYNiFL17bzq1jrb67ggeem%2BYMyCVYG9Xi%2B9qB8%2BIHBq%2BeWGd7JPgdy0Nax67nuZG6kxYxCeYqrUZuN%2FuanZA%2F9IMlbbQwXZR4AMZbI8NSXfGNxYNBTuCNUigc%2BbxiDy0KRsE7ozq7yhIDjolGINPyixqbbM6cQEEXA42zQPdX9pbEoJTlL%2FTbvRYwCxvt0%2BlHX5Rf9trjqwCMtcp08wrSo0qY3Ram%2FBAKUCy2X%2FT4XUmtAx2P2LU4iBJ8cHmVkZDx3JJiD7kmUwj6MHbkKpgs2q3Egl4RQ33yP42SS7Tm%2Fw7W277Jhz3bIkCvmWzEL%2Fgr8FFbjpxEh63WfIOtmMtt66uyStPOK2z25MMY3vxXNqD4moSLJl4C7jtkRK917SYmVDt6PzYdcCobnHGH99EDtNL0SW9c3sTpy1%2FKpWPyh4Gvpm0Df3Q4oooTZz7eQx9j5Mp%2Fo7po4tBeM7QNboj8yZuBpczFadVRFzmiJ9zxOXntCHsQulwmI5J7Z91y47xcmzp%2BxKT5TqD8Xd6PwdOAdXlaDDy7cDPBjqkARxtzcF720CZyPm%2FcMB2RywjcUpYBpgWOito3vWfpU55zxCUhtbGc%2FVFCVzhF%2BOS3G7FMD%2F6r3jEOcHp0pwW47E4MRglpccq2twFwuSOKBBTY82ztA3BnEzSeIjXIZg86laOVcVS2t29zEaCaM6knTfOJwOViDdGcqntP8T4QynXRdwfAZm%2FN22tmopZXZwiigt3finmSE1s1krxIzcnPhtMQYsK&X-Amz-Signature=a6fdb487f9c06e9989a6f13bd0b01e3db39e0b5b28a7b0c3aeb896016dc72671&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

找到nginx的环境端口，把80和433端口改掉



接下来还有.env文件也要进行修改



```javascript
vim .env
```



![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/b23319e4-b5d6-490a-84d9-b69f15e77a88/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MZOE%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDUhHWOJ%2FbPkQi%2BY7r%2B1lSOV8LoUKLn2YodtgACbbRkTwIhAMPcJVuenao9ePSMjQ%2F3LJIHT8FMQKHNKoaH%2F5vtB3%2FRKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtnquPgloxy4LzWcgq3AM0AmJpoPhGv%2F6PmpjgvIlQm8ES1MfbrTzIGXZE50UcCiSsU%2F2qru4Px1M8wOEJY8nbivPL1CWJn5pUMF2eZbuCUc11bcqLqhqypYNiFL17bzq1jrb67ggeem%2BYMyCVYG9Xi%2B9qB8%2BIHBq%2BeWGd7JPgdy0Nax67nuZG6kxYxCeYqrUZuN%2FuanZA%2F9IMlbbQwXZR4AMZbI8NSXfGNxYNBTuCNUigc%2BbxiDy0KRsE7ozq7yhIDjolGINPyixqbbM6cQEEXA42zQPdX9pbEoJTlL%2FTbvRYwCxvt0%2BlHX5Rf9trjqwCMtcp08wrSo0qY3Ram%2FBAKUCy2X%2FT4XUmtAx2P2LU4iBJ8cHmVkZDx3JJiD7kmUwj6MHbkKpgs2q3Egl4RQ33yP42SS7Tm%2Fw7W277Jhz3bIkCvmWzEL%2Fgr8FFbjpxEh63WfIOtmMtt66uyStPOK2z25MMY3vxXNqD4moSLJl4C7jtkRK917SYmVDt6PzYdcCobnHGH99EDtNL0SW9c3sTpy1%2FKpWPyh4Gvpm0Df3Q4oooTZz7eQx9j5Mp%2Fo7po4tBeM7QNboj8yZuBpczFadVRFzmiJ9zxOXntCHsQulwmI5J7Z91y47xcmzp%2BxKT5TqD8Xd6PwdOAdXlaDDy7cDPBjqkARxtzcF720CZyPm%2FcMB2RywjcUpYBpgWOito3vWfpU55zxCUhtbGc%2FVFCVzhF%2BOS3G7FMD%2F6r3jEOcHp0pwW47E4MRglpccq2twFwuSOKBBTY82ztA3BnEzSeIjXIZg86laOVcVS2t29zEaCaM6knTfOJwOViDdGcqntP8T4QynXRdwfAZm%2FN22tmopZXZwiigt3finmSE1s1krxIzcnPhtMQYsK&X-Amz-Signature=d3a945c4778be0fb249ad17875a16b81a86f0e294e05d839dc5a1b0d989c80ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



改完之后我们最后刷新一下docker



```javascript
docker compose up -d

systemctl restart docker
```

接下来就可以打开网站了，因为端口改成8001，所以http://your_server_ip:8001就可以了

