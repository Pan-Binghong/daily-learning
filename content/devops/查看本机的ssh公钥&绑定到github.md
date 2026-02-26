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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2NPWWXT%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCetju2JkPRhJXml7SOoMMRziGm4zdX3DcTxszYKSDodAIgLd%2BQWhRUGvIGmnEoFtVY6P%2F9EaPato%2FGx3P5Vm3IYrAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDJv%2BaGf%2BxY01%2F3XK%2FircA2UFQWCDf2Xh27ANXbNSZwF3ErlV0Bno5tIKDCBzNAxsBJcGKtV2pTUDra8O2hJaTeX%2BphWSycfcB%2BQsVTXRj5LZO5s%2Fc4thUemF2AhcgP%2FtGDB7gCOCkebCsg2C8%2FJ7XyWt2xben0CtM7rXN3%2BUVF1hzQtZCekIpHCcHVRpqVbeWN463Ib4pB9rDW9Y9GSVKeoqQKs1wE6RX2WQ%2BycrIrqbcb9PSqK8H36oiJZ1NluEd%2FL%2BwYuL7%2FlnJBVbs2iOAPYEUAi7SUUwmbSbbZsAOXaWEEFshuHr2cS7EHyvQ79DkCm9FqZlo%2FFw7SvfknrQ1iKdCMWNu%2BsY9PgmDHKieX21jLBxaaY7n9vSroJ7WlfXstV%2Fp68dtDBsYZmY1wZGkZZR2qk8CfdasPSWkau9xB%2BRSOWrr1Ja32y29bs9iOphqgvf4%2Bhe6QR6Mx4enJ5TocPurmMhxuurp7tJ85wc%2BLyVRoHC09n3QXh%2FrB48COzoyVvCdiTGEmqnf6joYmIUhIJrEFlXdSaRxUawLC9bIldNdb1j1gsk4cQWpy2mOlWjmZb9Sh%2FufZw5xqzo3UfFCO6ydJVYwWs7AbepB2Ie9VfzPUVMjCoQerA30eu75balhnLo3lsr3Zq5qyIDML%2F1%2FswGOqUB2aNM%2Fjsgot4eNcO3iFz7TfYgNQwRsy7amcPUc6r3eBoykORS%2BHgVZf9rm0za49EJldPL062gcdf0ZxJFKerlOv%2FcGwjWZiQaxPWZFdokapLRILBZc3nxELromKSsqRMfZRVmRdUFfLh9%2BScDyRjL6jT7Fcvb6URq4hA1Dk8ZzkAa%2BzXIWOZAakd0cfU7qOUQu8E5sdAEI6TcNHyCijC7MPoyJ3G9&X-Amz-Signature=83bf450fb0f85666943fbf566d86f7eaf5e97b1ea7abaec6a1757f0fb30cd43e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2NPWWXT%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCetju2JkPRhJXml7SOoMMRziGm4zdX3DcTxszYKSDodAIgLd%2BQWhRUGvIGmnEoFtVY6P%2F9EaPato%2FGx3P5Vm3IYrAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDJv%2BaGf%2BxY01%2F3XK%2FircA2UFQWCDf2Xh27ANXbNSZwF3ErlV0Bno5tIKDCBzNAxsBJcGKtV2pTUDra8O2hJaTeX%2BphWSycfcB%2BQsVTXRj5LZO5s%2Fc4thUemF2AhcgP%2FtGDB7gCOCkebCsg2C8%2FJ7XyWt2xben0CtM7rXN3%2BUVF1hzQtZCekIpHCcHVRpqVbeWN463Ib4pB9rDW9Y9GSVKeoqQKs1wE6RX2WQ%2BycrIrqbcb9PSqK8H36oiJZ1NluEd%2FL%2BwYuL7%2FlnJBVbs2iOAPYEUAi7SUUwmbSbbZsAOXaWEEFshuHr2cS7EHyvQ79DkCm9FqZlo%2FFw7SvfknrQ1iKdCMWNu%2BsY9PgmDHKieX21jLBxaaY7n9vSroJ7WlfXstV%2Fp68dtDBsYZmY1wZGkZZR2qk8CfdasPSWkau9xB%2BRSOWrr1Ja32y29bs9iOphqgvf4%2Bhe6QR6Mx4enJ5TocPurmMhxuurp7tJ85wc%2BLyVRoHC09n3QXh%2FrB48COzoyVvCdiTGEmqnf6joYmIUhIJrEFlXdSaRxUawLC9bIldNdb1j1gsk4cQWpy2mOlWjmZb9Sh%2FufZw5xqzo3UfFCO6ydJVYwWs7AbepB2Ie9VfzPUVMjCoQerA30eu75balhnLo3lsr3Zq5qyIDML%2F1%2FswGOqUB2aNM%2Fjsgot4eNcO3iFz7TfYgNQwRsy7amcPUc6r3eBoykORS%2BHgVZf9rm0za49EJldPL062gcdf0ZxJFKerlOv%2FcGwjWZiQaxPWZFdokapLRILBZc3nxELromKSsqRMfZRVmRdUFfLh9%2BScDyRjL6jT7Fcvb6URq4hA1Dk8ZzkAa%2BzXIWOZAakd0cfU7qOUQu8E5sdAEI6TcNHyCijC7MPoyJ3G9&X-Amz-Signature=43d1653d6b778efab347257f1be1a65b71da29d2f7226f8ca345db30944db7ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

