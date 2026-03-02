---
title: 查看本机的SSH公钥&绑定到Github
date: '2026-02-03T02:14:00.000Z'
lastmod: '2026-02-03T03:32:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 配置Git使用SSH方式, 本文环境：windows + powershell + git guissh 

---

## 查看

```json
ls  ~/.ssh
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVFVGUGZ%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAg4wCMwkd2YGn81nqv9wSr3yyYFW68V1hMZtJehTZ3lAiAssoM8BJeH4NLvnIVf1BpQ4qMOxASvgqyxRuCwsy9%2BNSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMHLjrRIL42DfNlHsPKtwDgHQwLN5yvlINTSmTMBzuIehIXrMNH3HoTf7ciXNJZ49OON9%2BqeWVwOdyXn1Olc2k7NE7YtXyj7f7e44gjNKm1f62JfFwnaRMfTGoaY486R7tf6Tija9uXoz0DGsQ%2BVfgP%2BuYfHrB9Qdo%2BPuNAYCaxSlexGPVXc5uARUUQkOmN67mVjmbblLH7RAcugqVuQJnLi6XAtLwns97%2Be%2B%2FI3VY0GbKW6rtLvW2wThxH9uSFQORG5zpeT%2Fo%2F4AI663MdezMpYPqrQA8owS8iSqxkGj%2Fm8YWd0zBi1Z5D4hOBpzRjaLUdfAZrRuqrAqRr8i9ESxqEzpixg02G4cSBezcmPCEF5VSb3LRTluxWrtssovuBWcttF0NEjU7UJvoAOPRUCA25E9sbEarCrRYh2yjEJJV9ZOgTNI5NTBz07PNYmZT774dqbnmT35XWldlXlpVHOojsSTZLn3zKUFsY9%2FUh0KmV5Aa4of5bn5pXPJELRGBBx1J07dGiZ1PJ705vTFgZskRNnO%2Bxpc24OD4v6LddH0qRko0kp6kiJyUVtQ9SdzghXcXU7IzDcINTLMWJCJ3i%2Fia2Ir9LzmSuDegG18aMFF7HONqCJ9YFPLCx4YfXgz3pZ%2FpIvdjw3FsdN8S2RUwwP2TzQY6pgE36QznsvmsMg09kkTp2tT1OCTzaPjMdalj%2Bm23ckdqpXIE5zdpgcaNC1745NvwBZvXxpHS9gwCemXQbbt3T6yRHXgXuyJWc4c4Ojl%2Bgs8fo1hbE%2BjN3%2FHKNu4zI2F0MT%2BIqheCXtl%2FPOcjuuOTBesxJpcHv3Bqd%2FRQgtKQGcciB0LD9eZGY%2FTETONe4F2QgPxKhQtvmSC%2BWflN4%2FQ3uk5NJb%2Bc1C8f&X-Amz-Signature=9e359486ba7312767d95a7795c27d492bdbf2cb77cd9c292fca29af835474cae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 创建

```json
# 推荐使用Ed25519算法
ssh-keygen -t ed25519 -C "your_email@example.com"

# 备选
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

---

## 配置

```json
# 将ssh密钥添加到ssh-agent
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add .\.ssh\id_ed25519

# 查看是否添加成功
ssh-add -l
```

### 安装gh（github cli）

```json
# 打开powershell
choco install gh

# 登录
gh auth login
```

## 打开GIT/提交

```json
gh ssh-key add ~/.ssh/id_ed25519.pub --title "公司主机"
```

## 验证

```json
ssh -T git@github.com
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVFVGUGZ%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAg4wCMwkd2YGn81nqv9wSr3yyYFW68V1hMZtJehTZ3lAiAssoM8BJeH4NLvnIVf1BpQ4qMOxASvgqyxRuCwsy9%2BNSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMHLjrRIL42DfNlHsPKtwDgHQwLN5yvlINTSmTMBzuIehIXrMNH3HoTf7ciXNJZ49OON9%2BqeWVwOdyXn1Olc2k7NE7YtXyj7f7e44gjNKm1f62JfFwnaRMfTGoaY486R7tf6Tija9uXoz0DGsQ%2BVfgP%2BuYfHrB9Qdo%2BPuNAYCaxSlexGPVXc5uARUUQkOmN67mVjmbblLH7RAcugqVuQJnLi6XAtLwns97%2Be%2B%2FI3VY0GbKW6rtLvW2wThxH9uSFQORG5zpeT%2Fo%2F4AI663MdezMpYPqrQA8owS8iSqxkGj%2Fm8YWd0zBi1Z5D4hOBpzRjaLUdfAZrRuqrAqRr8i9ESxqEzpixg02G4cSBezcmPCEF5VSb3LRTluxWrtssovuBWcttF0NEjU7UJvoAOPRUCA25E9sbEarCrRYh2yjEJJV9ZOgTNI5NTBz07PNYmZT774dqbnmT35XWldlXlpVHOojsSTZLn3zKUFsY9%2FUh0KmV5Aa4of5bn5pXPJELRGBBx1J07dGiZ1PJ705vTFgZskRNnO%2Bxpc24OD4v6LddH0qRko0kp6kiJyUVtQ9SdzghXcXU7IzDcINTLMWJCJ3i%2Fia2Ir9LzmSuDegG18aMFF7HONqCJ9YFPLCx4YfXgz3pZ%2FpIvdjw3FsdN8S2RUwwP2TzQY6pgE36QznsvmsMg09kkTp2tT1OCTzaPjMdalj%2Bm23ckdqpXIE5zdpgcaNC1745NvwBZvXxpHS9gwCemXQbbt3T6yRHXgXuyJWc4c4Ojl%2Bgs8fo1hbE%2BjN3%2FHKNu4zI2F0MT%2BIqheCXtl%2FPOcjuuOTBesxJpcHv3Bqd%2FRQgtKQGcciB0LD9eZGY%2FTETONe4F2QgPxKhQtvmSC%2BWflN4%2FQ3uk5NJb%2Bc1C8f&X-Amz-Signature=e4ac4c20e0065c889f14ba1905985c0a389ab4bddd1a9432cdb4604bbab52df1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

