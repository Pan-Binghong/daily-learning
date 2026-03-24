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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBEJG7HA%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGz67H6i5lrNyYtRbJleyXqKcQxG%2F2%2F%2Bo3e87tRQaQxlAiEAwfJr17TsjFxJhgqQqX51UuMyszCkSAW70vf5qKbTJtEqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGaKsabUu7NBd83CtCrcA%2Fp0UqF6aV8rjHYxnWcphkVnHHfgJ%2B4qFsBAFXUQ3tWDZYp33C3DAsNtrG%2F%2Fy3hZSyEtwyMBYujRyLgxl5xGue4m965Q2GyyQZ74v6brLKNQ41rTNUuZsgWWtziHUSt2rbTeQxPECc5nyUooy7d1Wj0OJt8SAYK5Q4dTgIISf%2Fb1bMNg5e3Hxl1wjMe5CmZIpK4evKW40I%2BKYYF%2BWmhrclp2%2BtqrkL6UZrIeAHvXNLJIBCiqcUUSOuwZ0RXUCSSCzf706SLSN%2Bv1f2VeuYXgCT9D9G04k%2B%2Bi1ptehixsfJoh5iFJWFOcxWne%2F95b0%2F21ElT8VHG4UEjRnRHNM%2BNezUP%2FiPjKcnH12A4enxrOyWado5xKeRF9c5YaUhOu23ulGbPUGDoGgCD0X%2FPdSAooK2yx9bSC61YbkmkuFC3njZS6nv1ee0shOUBxGjoCdSdFE9qPaub2WMySurcWQ8bBNMH7qsvHOGsRVUVlyvLXnroTFNZspU0em40m8ZwgDI6Sh5LQamyHl%2Bla8i%2FetYE7pMoBGRGId7RjMg3F9otr6osz6h1xDkLGeG6GFKxG7Z42WcJi7qqp7JTteFBMla8WW45lAi5q4Z%2FHq1d88WeKuSaA%2B1tsu%2BjznDm%2FuxMRMJn0h84GOqUBxqYV2JBUuU%2BWEakK69Nc%2F6e66sDoPvexL5xpcVp5lSQTZDEj0jzUyk2bb3xOLuSBITbO7CBUh%2BMJTf%2FRKUAlleua2emYSzvQQ3gY2rZJVlhhG4QcwvE6xI%2FR%2BWCX3FW0EDtuSSlog99JMEnXrAvgWoNhn0wuXRvVU37SHuDlVL4q30IMRb6jMGDiSFkDnRIaDuCOS9LZqV0maBSBBSJpJpWKguEx&X-Amz-Signature=c2b8e1cadfe0822e88b9b22e1a9505d1af581872e9fa5db76bd8708836923394&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBEJG7HA%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGz67H6i5lrNyYtRbJleyXqKcQxG%2F2%2F%2Bo3e87tRQaQxlAiEAwfJr17TsjFxJhgqQqX51UuMyszCkSAW70vf5qKbTJtEqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGaKsabUu7NBd83CtCrcA%2Fp0UqF6aV8rjHYxnWcphkVnHHfgJ%2B4qFsBAFXUQ3tWDZYp33C3DAsNtrG%2F%2Fy3hZSyEtwyMBYujRyLgxl5xGue4m965Q2GyyQZ74v6brLKNQ41rTNUuZsgWWtziHUSt2rbTeQxPECc5nyUooy7d1Wj0OJt8SAYK5Q4dTgIISf%2Fb1bMNg5e3Hxl1wjMe5CmZIpK4evKW40I%2BKYYF%2BWmhrclp2%2BtqrkL6UZrIeAHvXNLJIBCiqcUUSOuwZ0RXUCSSCzf706SLSN%2Bv1f2VeuYXgCT9D9G04k%2B%2Bi1ptehixsfJoh5iFJWFOcxWne%2F95b0%2F21ElT8VHG4UEjRnRHNM%2BNezUP%2FiPjKcnH12A4enxrOyWado5xKeRF9c5YaUhOu23ulGbPUGDoGgCD0X%2FPdSAooK2yx9bSC61YbkmkuFC3njZS6nv1ee0shOUBxGjoCdSdFE9qPaub2WMySurcWQ8bBNMH7qsvHOGsRVUVlyvLXnroTFNZspU0em40m8ZwgDI6Sh5LQamyHl%2Bla8i%2FetYE7pMoBGRGId7RjMg3F9otr6osz6h1xDkLGeG6GFKxG7Z42WcJi7qqp7JTteFBMla8WW45lAi5q4Z%2FHq1d88WeKuSaA%2B1tsu%2BjznDm%2FuxMRMJn0h84GOqUBxqYV2JBUuU%2BWEakK69Nc%2F6e66sDoPvexL5xpcVp5lSQTZDEj0jzUyk2bb3xOLuSBITbO7CBUh%2BMJTf%2FRKUAlleua2emYSzvQQ3gY2rZJVlhhG4QcwvE6xI%2FR%2BWCX3FW0EDtuSSlog99JMEnXrAvgWoNhn0wuXRvVU37SHuDlVL4q30IMRb6jMGDiSFkDnRIaDuCOS9LZqV0maBSBBSJpJpWKguEx&X-Amz-Signature=59bdf2094e0b6cdb4c0c7e6362e646dee48c1571ef2890979c43fb6e34e76e1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

