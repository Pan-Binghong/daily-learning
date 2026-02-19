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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG7VNY5Y%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDggNsFwKJ%2BeZaMwbvHt5FDM6pcpCU9cKbQS0kPJv0IegIhAIKu%2FHYuO1n0IX78K3D6PiXlCuLJ03abIJRynPrXVriqKv8DCHQQABoMNjM3NDIzMTgzODA1Igw0xF9DKndb2aAQ3Ncq3AN96IfPaRaC1GcT1astfrWrOt1N0CVtoHYk1hAoyRWUEQiKY6%2FgMttQDllcWbf76bhOdbdyb5quHJY%2Brn78LVcfvi7bqbmpZQgR6IutqFy%2BPQafL5gFn7ZjDI8pyZwvHFfT%2FyxjkWy%2B0suVCQJ5ogUrXXDEiUeiL73a3i7K3g7QkuoEWhPWdT%2Bw7lLn3AZg1VsjSpVIXD3yBMsO2W%2BJu%2FFEaimFr4%2FfV2aSq3wXrDt1ZLrc0EgN71uLWTF6JW9uxxiMBvRaOC3JaW%2BbUw%2FF0cUFdetHgzq5gLOGjcVs5aVyLfI0po5fWrBBzWoPDD%2FRvXoR4rNlMHc3efKLBIVrOlP9xjIuJnBrUOCk%2BUnS7U%2FbqpL%2Bff6zDzC2gxL64BbeaGblvZepMPhxXdQIvYbuYkTY9puS1vwoTEv68hiBTdp%2FfJxKGRJarx6IXmypPvXCc3Qg7fkiJCjBQ669YMcyNG3yIfNak%2Beb0jwMw%2Bu3fKBH3gTy9R2eKuVcGx8WNWyCaUEY0ziFee4vfjN40dTHRYaqHB9NFLDuIeoba%2Fo5OS7egIyHWMPJ6lROtUxnZZjeXD6BkF0klQEe31gqYyeuw0%2BxBU1tu9XqzF5ZtXwJlRZbRV%2FEd5aOBYK30kV1EDCQ8tnMBjqkAXu0fFj0%2FeShi2eQ6RzW%2FZoLfrQvz6Yuwy68RYvWPFdFfBjzF92%2FXiYRVxrK%2FJWkN%2BwTdLtOQWtGaANG6yz3BXBEbTg5V6Qkd6ZiVO84NkoruFCZ%2Fh1Rg1IOdU8wIZK5YX%2BH%2FmZp26XHP815sISH9KaMdXcgZtT2bmMfPjBQQZC0y3X6mPz2TKtVEqxBohkqmmIVHJcFm9KIC49MOJcn7kuMYXW0&X-Amz-Signature=7dc4a5e6110b75aea7cdd7182c577c19d7cb6becd20179b5341089404a1de479&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG7VNY5Y%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDggNsFwKJ%2BeZaMwbvHt5FDM6pcpCU9cKbQS0kPJv0IegIhAIKu%2FHYuO1n0IX78K3D6PiXlCuLJ03abIJRynPrXVriqKv8DCHQQABoMNjM3NDIzMTgzODA1Igw0xF9DKndb2aAQ3Ncq3AN96IfPaRaC1GcT1astfrWrOt1N0CVtoHYk1hAoyRWUEQiKY6%2FgMttQDllcWbf76bhOdbdyb5quHJY%2Brn78LVcfvi7bqbmpZQgR6IutqFy%2BPQafL5gFn7ZjDI8pyZwvHFfT%2FyxjkWy%2B0suVCQJ5ogUrXXDEiUeiL73a3i7K3g7QkuoEWhPWdT%2Bw7lLn3AZg1VsjSpVIXD3yBMsO2W%2BJu%2FFEaimFr4%2FfV2aSq3wXrDt1ZLrc0EgN71uLWTF6JW9uxxiMBvRaOC3JaW%2BbUw%2FF0cUFdetHgzq5gLOGjcVs5aVyLfI0po5fWrBBzWoPDD%2FRvXoR4rNlMHc3efKLBIVrOlP9xjIuJnBrUOCk%2BUnS7U%2FbqpL%2Bff6zDzC2gxL64BbeaGblvZepMPhxXdQIvYbuYkTY9puS1vwoTEv68hiBTdp%2FfJxKGRJarx6IXmypPvXCc3Qg7fkiJCjBQ669YMcyNG3yIfNak%2Beb0jwMw%2Bu3fKBH3gTy9R2eKuVcGx8WNWyCaUEY0ziFee4vfjN40dTHRYaqHB9NFLDuIeoba%2Fo5OS7egIyHWMPJ6lROtUxnZZjeXD6BkF0klQEe31gqYyeuw0%2BxBU1tu9XqzF5ZtXwJlRZbRV%2FEd5aOBYK30kV1EDCQ8tnMBjqkAXu0fFj0%2FeShi2eQ6RzW%2FZoLfrQvz6Yuwy68RYvWPFdFfBjzF92%2FXiYRVxrK%2FJWkN%2BwTdLtOQWtGaANG6yz3BXBEbTg5V6Qkd6ZiVO84NkoruFCZ%2Fh1Rg1IOdU8wIZK5YX%2BH%2FmZp26XHP815sISH9KaMdXcgZtT2bmMfPjBQQZC0y3X6mPz2TKtVEqxBohkqmmIVHJcFm9KIC49MOJcn7kuMYXW0&X-Amz-Signature=315f8d36f8ca0c96df287ff52443d463cbcd83d20c2aad98a8a6e5207a81e69c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

