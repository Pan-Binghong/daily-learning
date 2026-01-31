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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB76VJOR%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBR%2BuG7NYuor%2FrTEeReIeO6kqhrdH67e%2FR3cByFBUMdAiAmf5JFRXfyzX87ROmomnKufLjCNzFdAX4GwQQ60YnCmCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgul27IcNAK%2FafYYWKtwD9OA8lB6B6jjFsQxo9FxWIZhvLfY9ehiv9fUisHOgr32bG7wxZQipkm952mgWOMMcbq5CV15HerqN92A4WC3Xhv%2BppmHCift0i6D149tLJNNW2q6au3E9B7mjG53wJOlSw3jUUfAPUNyipcDF5JMxyHGpnjmBCCLFJyqzeBpz8mIEzB5wedgUm951qYPUtK0OK%2Fx%2FnsahTHlkQ3Im8cM3Q4kqKV2I2prQJKN63r8F7ImeBz1pLLZdbNdCyfq4kPWvb9an8O%2FmNXdGL0MfJutgT2CduJvsZnhgt6TAeI97ZMX4zLOeLn1TygBi3IcmLOMjwQBhs07J4F5WWuU7wr%2BV8UMp6b1DqF%2Fe0BmK5pQYBb367ofCrM6FLKyANavrvyVrysjsPu0Yk1znJt8AzAqWcYIAQxE1fRcF1Q65el9xQIFf6W2JRi9oxVcGtKWGhrXJPSinUAUIffEGvwUaGhcj3GxLDCl3vnBdVzxh7geU%2Fp7cBNTalZuQdqbkLAqm2BS7G9UxTiXzByYfaeirm7saKc%2Fhmbt8uJJGAmoEG5TkHRR05VSQqrZRDNaodHFCRXOfA%2BCOjbPYU6MN%2BbszVGKKiK4LNX34Ljg5LiRXRPfNZKR6bPpag1oSi6JdvM0wgsz1ywY6pgEuB3o%2FokKasFFz1nWPGXncbJY7Ec2Wb%2FhFGfp5uada%2Bcs0FA%2FLdq4rYnAqRI0YZL%2BVKJRrynxZcPgiwwwIsePUHZEyK39d02VA6IEc%2BGmC3tMRsqygIq4cgJw%2FvJXWRk4OiCSSm9VLUim8dHxzk19xoXYPRetlCmHNwTV2IpjVaHS%2B5vNpSdL7zpTCGxu%2FNdYEyq1c48JgxgRJ3y%2BVDIMaFL7FBu%2Bc&X-Amz-Signature=cbb0a1af971119f94b40fe7b7ff6992f440fb05885357a842b21eb1e9c6fcc6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB76VJOR%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBR%2BuG7NYuor%2FrTEeReIeO6kqhrdH67e%2FR3cByFBUMdAiAmf5JFRXfyzX87ROmomnKufLjCNzFdAX4GwQQ60YnCmCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgul27IcNAK%2FafYYWKtwD9OA8lB6B6jjFsQxo9FxWIZhvLfY9ehiv9fUisHOgr32bG7wxZQipkm952mgWOMMcbq5CV15HerqN92A4WC3Xhv%2BppmHCift0i6D149tLJNNW2q6au3E9B7mjG53wJOlSw3jUUfAPUNyipcDF5JMxyHGpnjmBCCLFJyqzeBpz8mIEzB5wedgUm951qYPUtK0OK%2Fx%2FnsahTHlkQ3Im8cM3Q4kqKV2I2prQJKN63r8F7ImeBz1pLLZdbNdCyfq4kPWvb9an8O%2FmNXdGL0MfJutgT2CduJvsZnhgt6TAeI97ZMX4zLOeLn1TygBi3IcmLOMjwQBhs07J4F5WWuU7wr%2BV8UMp6b1DqF%2Fe0BmK5pQYBb367ofCrM6FLKyANavrvyVrysjsPu0Yk1znJt8AzAqWcYIAQxE1fRcF1Q65el9xQIFf6W2JRi9oxVcGtKWGhrXJPSinUAUIffEGvwUaGhcj3GxLDCl3vnBdVzxh7geU%2Fp7cBNTalZuQdqbkLAqm2BS7G9UxTiXzByYfaeirm7saKc%2Fhmbt8uJJGAmoEG5TkHRR05VSQqrZRDNaodHFCRXOfA%2BCOjbPYU6MN%2BbszVGKKiK4LNX34Ljg5LiRXRPfNZKR6bPpag1oSi6JdvM0wgsz1ywY6pgEuB3o%2FokKasFFz1nWPGXncbJY7Ec2Wb%2FhFGfp5uada%2Bcs0FA%2FLdq4rYnAqRI0YZL%2BVKJRrynxZcPgiwwwIsePUHZEyK39d02VA6IEc%2BGmC3tMRsqygIq4cgJw%2FvJXWRk4OiCSSm9VLUim8dHxzk19xoXYPRetlCmHNwTV2IpjVaHS%2B5vNpSdL7zpTCGxu%2FNdYEyq1c48JgxgRJ3y%2BVDIMaFL7FBu%2Bc&X-Amz-Signature=daa8bda94a68aa621f3790315b8d5ab3d1458f8f914ceb7c62601453bacfa5aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB76VJOR%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEBR%2BuG7NYuor%2FrTEeReIeO6kqhrdH67e%2FR3cByFBUMdAiAmf5JFRXfyzX87ROmomnKufLjCNzFdAX4GwQQ60YnCmCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgul27IcNAK%2FafYYWKtwD9OA8lB6B6jjFsQxo9FxWIZhvLfY9ehiv9fUisHOgr32bG7wxZQipkm952mgWOMMcbq5CV15HerqN92A4WC3Xhv%2BppmHCift0i6D149tLJNNW2q6au3E9B7mjG53wJOlSw3jUUfAPUNyipcDF5JMxyHGpnjmBCCLFJyqzeBpz8mIEzB5wedgUm951qYPUtK0OK%2Fx%2FnsahTHlkQ3Im8cM3Q4kqKV2I2prQJKN63r8F7ImeBz1pLLZdbNdCyfq4kPWvb9an8O%2FmNXdGL0MfJutgT2CduJvsZnhgt6TAeI97ZMX4zLOeLn1TygBi3IcmLOMjwQBhs07J4F5WWuU7wr%2BV8UMp6b1DqF%2Fe0BmK5pQYBb367ofCrM6FLKyANavrvyVrysjsPu0Yk1znJt8AzAqWcYIAQxE1fRcF1Q65el9xQIFf6W2JRi9oxVcGtKWGhrXJPSinUAUIffEGvwUaGhcj3GxLDCl3vnBdVzxh7geU%2Fp7cBNTalZuQdqbkLAqm2BS7G9UxTiXzByYfaeirm7saKc%2Fhmbt8uJJGAmoEG5TkHRR05VSQqrZRDNaodHFCRXOfA%2BCOjbPYU6MN%2BbszVGKKiK4LNX34Ljg5LiRXRPfNZKR6bPpag1oSi6JdvM0wgsz1ywY6pgEuB3o%2FokKasFFz1nWPGXncbJY7Ec2Wb%2FhFGfp5uada%2Bcs0FA%2FLdq4rYnAqRI0YZL%2BVKJRrynxZcPgiwwwIsePUHZEyK39d02VA6IEc%2BGmC3tMRsqygIq4cgJw%2FvJXWRk4OiCSSm9VLUim8dHxzk19xoXYPRetlCmHNwTV2IpjVaHS%2B5vNpSdL7zpTCGxu%2FNdYEyq1c48JgxgRJ3y%2BVDIMaFL7FBu%2Bc&X-Amz-Signature=d9f9d15a9f15ad57efb2c302a4c4f7b3f1fbf1e3c92dbc0b2ac9231562691049&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

