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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5GRSCUI%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIG5kVFvFS3mkIm1rGW1%2FhsY4wsaNteVtE%2BTWelh5AlawAiAlsW1XZGeL9BBAvR2yWB6hwVIeogaHbBfC3IhP1AONLir%2FAwgGEAAaDDYzNzQyMzE4MzgwNSIMpijnNRB6y7F%2BGt0LKtwDoidxC97k6HfDN%2B6nrJxjbxPOkYEbKorhF8CRrBG7QT90PLouG7wEpVKgdtEl4EsZdOc1e%2FAvbQHniXE2br1pYPd7PaYSz8Hxb82knN0nGrreTWJM3z1w79HngaZ4waMiIHVVx6wPestJOJx6CqrTlZPb4uYXeB6NV9So6bn5CFkI%2BeJ%2FDCAyZJvX1UDK65xCVccq%2BC6anXTURaARPHtGK33nz8b51Z9n%2By59nLHDshyjFZkJwXp1bhAU3ui9mhaJHPi5a%2B1JEXHPs7C9RpSLUFuXxSP%2FP5vL3PMLfxD0%2FYQ6Odj6hxkv0reCVT1LTYOzBLMDT2pFnEDGCgt%2F5UG0WwRp7iReEPpeLX5AdPT1sr%2Bm1VfllklNEI9G0IhmTr7LoUcs5nnHdEFqgF0kJRcbcCgtu%2FdA9QF%2FLpwUlJ6CSviDzL6rZmapz4zWWloz0cUWA9%2FqfRK9w%2BzoeQSnzxGrPcZJ087Bqm1AM7W%2FRvnQVAP88AheoMSGNiiQBxAHuizmfVdNAuRHGbFEoOgK3bXdZJpfK92AIMhETBqZjpTxJ2dxZeQ1A%2Fsyr50eS7GfVV%2BcmUHe%2FHBZq2dxYE0kNvuwQybKkIdSMPm0C6pKvAN85P8QnlkhjL5ZK1CTXWQw67PLzwY6pgEy894MtvpWgDyKBXKFXuKc%2F0QlKvQTx%2BNk8W3eUehzf1nzf5L2FLzlXClfyma6BIblZC3gNUXK%2FeUgBq5e98yYOetJTauTU%2F4CbUQ27e2F9foZM9WYzf5RouQsckACF4PE8DfhKaQViOFAS2Ju3QPibNogvbneBo%2FLXeeOQvg2Sioa10hCjk1KH5JQz0aIY5CCrqvQoibvgtDvFbEIbNGFSuhf1QXz&X-Amz-Signature=da1bfafe414055f90822ef1d7817cb6b5d66c3f5f61f99b311eec6a876ccd892&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5GRSCUI%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIG5kVFvFS3mkIm1rGW1%2FhsY4wsaNteVtE%2BTWelh5AlawAiAlsW1XZGeL9BBAvR2yWB6hwVIeogaHbBfC3IhP1AONLir%2FAwgGEAAaDDYzNzQyMzE4MzgwNSIMpijnNRB6y7F%2BGt0LKtwDoidxC97k6HfDN%2B6nrJxjbxPOkYEbKorhF8CRrBG7QT90PLouG7wEpVKgdtEl4EsZdOc1e%2FAvbQHniXE2br1pYPd7PaYSz8Hxb82knN0nGrreTWJM3z1w79HngaZ4waMiIHVVx6wPestJOJx6CqrTlZPb4uYXeB6NV9So6bn5CFkI%2BeJ%2FDCAyZJvX1UDK65xCVccq%2BC6anXTURaARPHtGK33nz8b51Z9n%2By59nLHDshyjFZkJwXp1bhAU3ui9mhaJHPi5a%2B1JEXHPs7C9RpSLUFuXxSP%2FP5vL3PMLfxD0%2FYQ6Odj6hxkv0reCVT1LTYOzBLMDT2pFnEDGCgt%2F5UG0WwRp7iReEPpeLX5AdPT1sr%2Bm1VfllklNEI9G0IhmTr7LoUcs5nnHdEFqgF0kJRcbcCgtu%2FdA9QF%2FLpwUlJ6CSviDzL6rZmapz4zWWloz0cUWA9%2FqfRK9w%2BzoeQSnzxGrPcZJ087Bqm1AM7W%2FRvnQVAP88AheoMSGNiiQBxAHuizmfVdNAuRHGbFEoOgK3bXdZJpfK92AIMhETBqZjpTxJ2dxZeQ1A%2Fsyr50eS7GfVV%2BcmUHe%2FHBZq2dxYE0kNvuwQybKkIdSMPm0C6pKvAN85P8QnlkhjL5ZK1CTXWQw67PLzwY6pgEy894MtvpWgDyKBXKFXuKc%2F0QlKvQTx%2BNk8W3eUehzf1nzf5L2FLzlXClfyma6BIblZC3gNUXK%2FeUgBq5e98yYOetJTauTU%2F4CbUQ27e2F9foZM9WYzf5RouQsckACF4PE8DfhKaQViOFAS2Ju3QPibNogvbneBo%2FLXeeOQvg2Sioa10hCjk1KH5JQz0aIY5CCrqvQoibvgtDvFbEIbNGFSuhf1QXz&X-Amz-Signature=0a8351f7f3b398f0a5e9ba0ee63045f8963709ed20204d338ff6555bef0ee872&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

