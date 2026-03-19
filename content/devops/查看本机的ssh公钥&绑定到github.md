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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LRZKRDW%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIB9B%2B%2BN4NPduKdp%2F7AFsEc64U4pdngBDygdpuSk677wGAiEA28VGUjjiDgmr5f5QToZGHhFtXIo4QJ37uwTlyTptri8q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDCSwD%2FapAiHcuZ2Z4yrcA7IutJXdgp8ZND0v2WYXXxOWkRdCUq6OYtYebbLq7sfVmpE%2FK4CoKWz8p9uosyVmQahW2HEs5JCmotsQfZOANqe6gUbbj5p88cXF1XC76Ejz0QFTcpFg9jnWuVZEWeXLzto4Z8O9xpTn48H1nn1%2BQEtnNbcErV17a50EejpBV8f0VYCpoD%2BImg9VhcT9rSXcY8yeMlq6KNmEjMMX6tUIdCNAhJxHqeduV61PCHYhuOA4QutBb9r5ITtOGpiWcsQPvC4aNjN5Xe5x20vK%2FIKHF0kgb2OxD9R6McDGQDGCLdTJLIfURApBKU%2Fza333FAi0nYXjBXHYN1kKA8I5Fk6Q57qAed16aPS2Y03%2B3sbdUByxBPY1hPqew0ekeLVUrhP9jkvG0gzLpveDxEca7DVzSK48j3w55cf4JhRE0yH49qHuvp3AG1%2Brm4JZyxAtgIPjMZBh2A439ZzqJ9o8wWGROO%2B9Po%2FE8gdILvYKTY90B%2B%2FxRQmbZTRR6T3Cfu%2BzIP0R5NV84Rsi0%2FiFQWyjXS%2BHMGSMPIr%2FgricsNKXt8VSxGHyub0G%2BlKjYUGuHnhoD9G0JSeJnBZcLYRARUgaS05fp4Gndq9RscLrDDKc6C5oiEL%2FMO4Dn33TEBkygW1AMI7H7c0GOqUBFjqpAQvFF%2BOMoPVZaCNWHVkYU9PrUqHDu7%2FntdZZ6Aqt3Gl%2F5tbpBH1F6LNdA%2FgjcCvpfD56g9TSZqnsjDtw7dhXB5wernq9c1xbrlnt5NthXShnZisBsO5dUOFp2SCUM8%2FM5fIdLEJ39g6yxvYcknNLuHY5x0n%2FW7njm%2FZZAmLMZQk6F%2BJ4KoaGIbrCua8dC8ym6ihGyROC77EUPpl2jbNwEQX6&X-Amz-Signature=dbd7497bd655532bbf212a924a9924539b212b40ea89ccf6ac2afcabac630786&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LRZKRDW%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIB9B%2B%2BN4NPduKdp%2F7AFsEc64U4pdngBDygdpuSk677wGAiEA28VGUjjiDgmr5f5QToZGHhFtXIo4QJ37uwTlyTptri8q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDCSwD%2FapAiHcuZ2Z4yrcA7IutJXdgp8ZND0v2WYXXxOWkRdCUq6OYtYebbLq7sfVmpE%2FK4CoKWz8p9uosyVmQahW2HEs5JCmotsQfZOANqe6gUbbj5p88cXF1XC76Ejz0QFTcpFg9jnWuVZEWeXLzto4Z8O9xpTn48H1nn1%2BQEtnNbcErV17a50EejpBV8f0VYCpoD%2BImg9VhcT9rSXcY8yeMlq6KNmEjMMX6tUIdCNAhJxHqeduV61PCHYhuOA4QutBb9r5ITtOGpiWcsQPvC4aNjN5Xe5x20vK%2FIKHF0kgb2OxD9R6McDGQDGCLdTJLIfURApBKU%2Fza333FAi0nYXjBXHYN1kKA8I5Fk6Q57qAed16aPS2Y03%2B3sbdUByxBPY1hPqew0ekeLVUrhP9jkvG0gzLpveDxEca7DVzSK48j3w55cf4JhRE0yH49qHuvp3AG1%2Brm4JZyxAtgIPjMZBh2A439ZzqJ9o8wWGROO%2B9Po%2FE8gdILvYKTY90B%2B%2FxRQmbZTRR6T3Cfu%2BzIP0R5NV84Rsi0%2FiFQWyjXS%2BHMGSMPIr%2FgricsNKXt8VSxGHyub0G%2BlKjYUGuHnhoD9G0JSeJnBZcLYRARUgaS05fp4Gndq9RscLrDDKc6C5oiEL%2FMO4Dn33TEBkygW1AMI7H7c0GOqUBFjqpAQvFF%2BOMoPVZaCNWHVkYU9PrUqHDu7%2FntdZZ6Aqt3Gl%2F5tbpBH1F6LNdA%2FgjcCvpfD56g9TSZqnsjDtw7dhXB5wernq9c1xbrlnt5NthXShnZisBsO5dUOFp2SCUM8%2FM5fIdLEJ39g6yxvYcknNLuHY5x0n%2FW7njm%2FZZAmLMZQk6F%2BJ4KoaGIbrCua8dC8ym6ihGyROC77EUPpl2jbNwEQX6&X-Amz-Signature=d1e372b31ebb8c00ad58c78a9e305911cd45d208b8fab81b54cf10a49dd7df7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

