---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XGTHHXF%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIDYZ06Xtdo1HfTXJpC8qshZhTk12QoqZaSX245%2BK4HNcAiBQBvY1ICswO9LSJmay0Q%2B8%2BwXIDR8PK6kwV4tEAnm%2B6yr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMycDb3FT12wgo7teHKtwD2pJQm4MNj3E5C4OHqTXq4SuPhxKWSbHxFxkihs%2FhmO0qM3N9LE%2B2B8qymJx6E9YctKXEzMD5ZPuG5BFM3WuZZgZ3nj0SrthT7QpO97wA4vyowmLC%2FPhDfy%2BkOFifEQLUHNLSxg8nsTPqaSeC62mWIflsPydtniV1TcIYRM1bbHE0gE2C4D%2BYzG2Jn%2B%2BXRqrxjNb1cKKmymeyvGPEA9cfYhkYmeXm9W5Kr2HhJ7rHUeWfhMs0DtA6gBA%2FZGkh64wKyRj7wK5GbpclQuEanWdLc9OjiZzizTX6LwFtoT54CBiCPUTz%2BipQ5fIbzACOyXArg8FT3AilhQwljqQI4XFF9EAv2zdovu3Q9UUR%2BZLJYOOLDv%2FaH03oWBu1Fo7IKerKf7H%2Bj6ZmBdTAXDkDpmzkF3DmQj3cW5ho9EFUPHrXJLYN6mQ193pCLuYUx%2BCJZ5vVcscsgbgPfcubXsQ3ajUP8pZ%2B83ldVfqPfKEO9GJz%2Bl2iMJiPz9rjPYo%2B5i%2B9knu1hzqbRVXxG0CHcU527T6FKDioMJoTZFI2aimHCDN7d3XCiZPK7eEBisoksTv%2BhIlhyc5NZbXmWh%2BBCGBH6VzRLZllo7Z%2BhA%2BQfcjAI0Qrhhz2hDHyvwjwW%2BCmIIYwo4aEzQY6pgHrSvgMOzVO91sowxL4lKSyjEkWeoyCffNjDIbGE3omZy8jb4zzh9yrtSAnZsaAk6VXNFcfdBRMuSRmcv6sxvmME2eOKUbGlc5UObmju%2FaawF%2B9qnJXF8B8FQxsqzp06Vz5%2Bw58WazEBrAL7pbh9f9rpdaj6pdZr%2B14JG2dx%2FDA%2BgKwENrjsYvEGd3arCAYyxKOdHtP0yVcb1Tj8LfOm5o9%2BjT4%2FE0g&X-Amz-Signature=a45d1afa3a2a1dabc5d549b8a25d0ebf78735a7ea1a5976157f7a663b73f5473&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XGTHHXF%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIDYZ06Xtdo1HfTXJpC8qshZhTk12QoqZaSX245%2BK4HNcAiBQBvY1ICswO9LSJmay0Q%2B8%2BwXIDR8PK6kwV4tEAnm%2B6yr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMycDb3FT12wgo7teHKtwD2pJQm4MNj3E5C4OHqTXq4SuPhxKWSbHxFxkihs%2FhmO0qM3N9LE%2B2B8qymJx6E9YctKXEzMD5ZPuG5BFM3WuZZgZ3nj0SrthT7QpO97wA4vyowmLC%2FPhDfy%2BkOFifEQLUHNLSxg8nsTPqaSeC62mWIflsPydtniV1TcIYRM1bbHE0gE2C4D%2BYzG2Jn%2B%2BXRqrxjNb1cKKmymeyvGPEA9cfYhkYmeXm9W5Kr2HhJ7rHUeWfhMs0DtA6gBA%2FZGkh64wKyRj7wK5GbpclQuEanWdLc9OjiZzizTX6LwFtoT54CBiCPUTz%2BipQ5fIbzACOyXArg8FT3AilhQwljqQI4XFF9EAv2zdovu3Q9UUR%2BZLJYOOLDv%2FaH03oWBu1Fo7IKerKf7H%2Bj6ZmBdTAXDkDpmzkF3DmQj3cW5ho9EFUPHrXJLYN6mQ193pCLuYUx%2BCJZ5vVcscsgbgPfcubXsQ3ajUP8pZ%2B83ldVfqPfKEO9GJz%2Bl2iMJiPz9rjPYo%2B5i%2B9knu1hzqbRVXxG0CHcU527T6FKDioMJoTZFI2aimHCDN7d3XCiZPK7eEBisoksTv%2BhIlhyc5NZbXmWh%2BBCGBH6VzRLZllo7Z%2BhA%2BQfcjAI0Qrhhz2hDHyvwjwW%2BCmIIYwo4aEzQY6pgHrSvgMOzVO91sowxL4lKSyjEkWeoyCffNjDIbGE3omZy8jb4zzh9yrtSAnZsaAk6VXNFcfdBRMuSRmcv6sxvmME2eOKUbGlc5UObmju%2FaawF%2B9qnJXF8B8FQxsqzp06Vz5%2Bw58WazEBrAL7pbh9f9rpdaj6pdZr%2B14JG2dx%2FDA%2BgKwENrjsYvEGd3arCAYyxKOdHtP0yVcb1Tj8LfOm5o9%2BjT4%2FE0g&X-Amz-Signature=b4c03f1b77fe3cff09f4e63b43916e95ceb841c1a4be47bdf686a27870a6637d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XGTHHXF%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIDYZ06Xtdo1HfTXJpC8qshZhTk12QoqZaSX245%2BK4HNcAiBQBvY1ICswO9LSJmay0Q%2B8%2BwXIDR8PK6kwV4tEAnm%2B6yr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMycDb3FT12wgo7teHKtwD2pJQm4MNj3E5C4OHqTXq4SuPhxKWSbHxFxkihs%2FhmO0qM3N9LE%2B2B8qymJx6E9YctKXEzMD5ZPuG5BFM3WuZZgZ3nj0SrthT7QpO97wA4vyowmLC%2FPhDfy%2BkOFifEQLUHNLSxg8nsTPqaSeC62mWIflsPydtniV1TcIYRM1bbHE0gE2C4D%2BYzG2Jn%2B%2BXRqrxjNb1cKKmymeyvGPEA9cfYhkYmeXm9W5Kr2HhJ7rHUeWfhMs0DtA6gBA%2FZGkh64wKyRj7wK5GbpclQuEanWdLc9OjiZzizTX6LwFtoT54CBiCPUTz%2BipQ5fIbzACOyXArg8FT3AilhQwljqQI4XFF9EAv2zdovu3Q9UUR%2BZLJYOOLDv%2FaH03oWBu1Fo7IKerKf7H%2Bj6ZmBdTAXDkDpmzkF3DmQj3cW5ho9EFUPHrXJLYN6mQ193pCLuYUx%2BCJZ5vVcscsgbgPfcubXsQ3ajUP8pZ%2B83ldVfqPfKEO9GJz%2Bl2iMJiPz9rjPYo%2B5i%2B9knu1hzqbRVXxG0CHcU527T6FKDioMJoTZFI2aimHCDN7d3XCiZPK7eEBisoksTv%2BhIlhyc5NZbXmWh%2BBCGBH6VzRLZllo7Z%2BhA%2BQfcjAI0Qrhhz2hDHyvwjwW%2BCmIIYwo4aEzQY6pgHrSvgMOzVO91sowxL4lKSyjEkWeoyCffNjDIbGE3omZy8jb4zzh9yrtSAnZsaAk6VXNFcfdBRMuSRmcv6sxvmME2eOKUbGlc5UObmju%2FaawF%2B9qnJXF8B8FQxsqzp06Vz5%2Bw58WazEBrAL7pbh9f9rpdaj6pdZr%2B14JG2dx%2FDA%2BgKwENrjsYvEGd3arCAYyxKOdHtP0yVcb1Tj8LfOm5o9%2BjT4%2FE0g&X-Amz-Signature=915056228e89ff7e18456d87f93d06a591b75b3800e40757ba1ba402fd6ba044&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

