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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466323CEERS%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDslPFKqFilHXS1q%2Bm6d5Cfa%2B0AWDXvGzvVLh3V4xVm%2FAIhAJ0t0rPE08%2FkzNuBEhJSnVCj%2FLLmDzWRDHsn58k1xx17KogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwJmKJ8pwg3zo%2F8eVUq3AP1M4%2Bqd8uZ5Yy8mvqHZ0XLTUGoHcxwfpV0W1BcXKKIRA%2BZSGfuWrcVzw37fyPuMML8svz9c7rCjoRJypVHXDgsndIpYWGYaPcxhf5Y%2BkxZATmhYbmAENuMIikAKohjQ4cWbKJDntQddD77FCecN3%2FWx2%2BZp6sU8SsYjenOxEFJerDPE8nfOTD7GpnO9hj%2B7toxZqwC5%2FTGtYp90QiRAYfg1lBpfcam2p1mGOPROYGeC6B2FMHi5kcM2KLtIxlpTh6%2F%2BIgSjaOvqGvUwvl2gJynQjSE4BAZo1MohjDnJnYexIdZsEHr6zstU%2Bmt3UCIbas8R%2FFExcjq1FezsiPcXKr%2F3Xq8J%2F7VApE%2FVx9LjGkxwL2KSTmGnRVebH2Id1en%2B1TJDC%2BYJxgMQ%2B0H65W%2BCSjkBqRUAH9tZcBR8oVzwhJKFMng%2B%2BXTUVmKG%2B81hUiduB1DQE3h1bMJdwBSmM7qQJEVlyaDiRSuYDueNb8slE9G8ZRtFkVeYc0XV0hCT8RpVc4IP33z4AyXPol2gTzI0pixRVZaibt1euue49CZn%2Bm6%2FZXlea47DIVcu0Nv23TVaoBWdqC88skanQ2zT70xWoXQFIT1RSXsBj4XGDP6N5ESOOAS7%2Fe0WQmotmkenTDFkN%2FMBjqkAezj5d9een%2F6QS7is3XoRMN0AOEenIesdb95KZMfawyDjtdBMyK1eelYNDmjyFzlvMBMnWYJ2Hv92rlnXwQRe%2FgH6BHccJZg3mLV06rE8QdRIkpoNQ5J5y3V0eFb7bO33UeivL1IW6XdEt6ZejoMbh9sfO9oS66hzA%2B0DfXqSoDSHNbtKoUpg2arNqkkQg3qWGksHTvvEBB7qWsigjs2G06saYi7&X-Amz-Signature=443ed209b9c0aec60a737f4ad0122021bf76846745b8a6f019440bf5e5f93f0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466323CEERS%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDslPFKqFilHXS1q%2Bm6d5Cfa%2B0AWDXvGzvVLh3V4xVm%2FAIhAJ0t0rPE08%2FkzNuBEhJSnVCj%2FLLmDzWRDHsn58k1xx17KogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwJmKJ8pwg3zo%2F8eVUq3AP1M4%2Bqd8uZ5Yy8mvqHZ0XLTUGoHcxwfpV0W1BcXKKIRA%2BZSGfuWrcVzw37fyPuMML8svz9c7rCjoRJypVHXDgsndIpYWGYaPcxhf5Y%2BkxZATmhYbmAENuMIikAKohjQ4cWbKJDntQddD77FCecN3%2FWx2%2BZp6sU8SsYjenOxEFJerDPE8nfOTD7GpnO9hj%2B7toxZqwC5%2FTGtYp90QiRAYfg1lBpfcam2p1mGOPROYGeC6B2FMHi5kcM2KLtIxlpTh6%2F%2BIgSjaOvqGvUwvl2gJynQjSE4BAZo1MohjDnJnYexIdZsEHr6zstU%2Bmt3UCIbas8R%2FFExcjq1FezsiPcXKr%2F3Xq8J%2F7VApE%2FVx9LjGkxwL2KSTmGnRVebH2Id1en%2B1TJDC%2BYJxgMQ%2B0H65W%2BCSjkBqRUAH9tZcBR8oVzwhJKFMng%2B%2BXTUVmKG%2B81hUiduB1DQE3h1bMJdwBSmM7qQJEVlyaDiRSuYDueNb8slE9G8ZRtFkVeYc0XV0hCT8RpVc4IP33z4AyXPol2gTzI0pixRVZaibt1euue49CZn%2Bm6%2FZXlea47DIVcu0Nv23TVaoBWdqC88skanQ2zT70xWoXQFIT1RSXsBj4XGDP6N5ESOOAS7%2Fe0WQmotmkenTDFkN%2FMBjqkAezj5d9een%2F6QS7is3XoRMN0AOEenIesdb95KZMfawyDjtdBMyK1eelYNDmjyFzlvMBMnWYJ2Hv92rlnXwQRe%2FgH6BHccJZg3mLV06rE8QdRIkpoNQ5J5y3V0eFb7bO33UeivL1IW6XdEt6ZejoMbh9sfO9oS66hzA%2B0DfXqSoDSHNbtKoUpg2arNqkkQg3qWGksHTvvEBB7qWsigjs2G06saYi7&X-Amz-Signature=d0dcea22852eddf2ae12fedee47eadbf0fc85213d34102ecd2ebd1fca8b34bf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

