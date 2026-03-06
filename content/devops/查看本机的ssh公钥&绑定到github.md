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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TSISEPF%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T033024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQD5VCLuOgbkABaL7e6aIR3VlfHDMgFVkOiZtgAAyrqhiAIhAO4w9JuciFVMIbbTCY3wk%2BVQa9TrgeZGjXpYYDFy0dGIKogECNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwoo%2FNFwKK5bwvuTdUq3AOlqJfzZhN2hL8Op%2BmQBtApE7Pch%2FpP6gyMhKmgJx7LRQ3EJgpD2t3HzNisKBmBbYIwk82YxIbItp2QMDLG%2FtZgpgKzyPRILOVjxYPz2TyJAdoxDMO5PkGuIU1c34i0tgMMkPA%2FJQOvuVjEsUTa%2Bbvuu5BTikwfuXlXfWB%2B%2F%2BCmry4IDCE8nC72de8BInMehijiRBo5YQsgnUNE599YnbmQ6frBffEezRspOahF23vHnjQ%2FhsypXJd0N66JK6J5okqejWwLxuBvAm%2BlCF1LOVGea%2FoFZaHrSB6z%2BnwiFZVleNTmfz%2BAa%2BLcvDvX3%2FJ2AtwR1CbuazAugET%2FfQb3InYyOe9Nhotc6PzZwyB3HSwULK60qs%2BnHSrKeU4XH9En7BBT61Cfj5rGlXNxEe0aEF1e3WtxmRpAgUmz4PW%2F7FZ6R4CxaM3GHXKMnajeqIxb8AbPYSvuTniEkUh1aXJVi1%2FZZMiec%2FeptCsoUvsI9ayHVERvmkixAI19eJJmwcyLFIxkjN0pqS%2F3hu%2BdTd1LngQvFW%2BjNln0efORml7CPYN4USQCmJW7DYCVxuDN0kmGzXpcE3S%2FHwa5IvnGk3ifQ2Jas5A2e99yfQHW6yrFaXXlEVgAzJsBXZotD%2FySwDCAz6jNBjqkAdDHAMG16hE%2FREABbS9lxt40QGV47cn2KLQSlLp%2BPW%2BbfFUEpcIVEdccYbKJWX%2FIovn3Axw8zRgmXGZYYN1H5Io%2Bw13NECngSxwFkrWVz2xIB8dNxnWjsfvaUlt%2Be5Dc5Vz%2BOOS00YyiFrysONB6JjmTPAsqRnhxtc3EzqpxUSmZt0M%2FTem0XccK7a2wEK4Tx5O8xJPvRqeN7%2Bi6ZcmczkUK3SeJ&X-Amz-Signature=aae5a4fb83606d50995551a477b75b13901ac42b314363310cb6ea62a43cd3ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TSISEPF%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T033024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQD5VCLuOgbkABaL7e6aIR3VlfHDMgFVkOiZtgAAyrqhiAIhAO4w9JuciFVMIbbTCY3wk%2BVQa9TrgeZGjXpYYDFy0dGIKogECNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwoo%2FNFwKK5bwvuTdUq3AOlqJfzZhN2hL8Op%2BmQBtApE7Pch%2FpP6gyMhKmgJx7LRQ3EJgpD2t3HzNisKBmBbYIwk82YxIbItp2QMDLG%2FtZgpgKzyPRILOVjxYPz2TyJAdoxDMO5PkGuIU1c34i0tgMMkPA%2FJQOvuVjEsUTa%2Bbvuu5BTikwfuXlXfWB%2B%2F%2BCmry4IDCE8nC72de8BInMehijiRBo5YQsgnUNE599YnbmQ6frBffEezRspOahF23vHnjQ%2FhsypXJd0N66JK6J5okqejWwLxuBvAm%2BlCF1LOVGea%2FoFZaHrSB6z%2BnwiFZVleNTmfz%2BAa%2BLcvDvX3%2FJ2AtwR1CbuazAugET%2FfQb3InYyOe9Nhotc6PzZwyB3HSwULK60qs%2BnHSrKeU4XH9En7BBT61Cfj5rGlXNxEe0aEF1e3WtxmRpAgUmz4PW%2F7FZ6R4CxaM3GHXKMnajeqIxb8AbPYSvuTniEkUh1aXJVi1%2FZZMiec%2FeptCsoUvsI9ayHVERvmkixAI19eJJmwcyLFIxkjN0pqS%2F3hu%2BdTd1LngQvFW%2BjNln0efORml7CPYN4USQCmJW7DYCVxuDN0kmGzXpcE3S%2FHwa5IvnGk3ifQ2Jas5A2e99yfQHW6yrFaXXlEVgAzJsBXZotD%2FySwDCAz6jNBjqkAdDHAMG16hE%2FREABbS9lxt40QGV47cn2KLQSlLp%2BPW%2BbfFUEpcIVEdccYbKJWX%2FIovn3Axw8zRgmXGZYYN1H5Io%2Bw13NECngSxwFkrWVz2xIB8dNxnWjsfvaUlt%2Be5Dc5Vz%2BOOS00YyiFrysONB6JjmTPAsqRnhxtc3EzqpxUSmZt0M%2FTem0XccK7a2wEK4Tx5O8xJPvRqeN7%2Bi6ZcmczkUK3SeJ&X-Amz-Signature=948e83be6b5358dc3003caf3f77ac3d4a0203cd6ef70794a51736a1dc4c7c9a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

