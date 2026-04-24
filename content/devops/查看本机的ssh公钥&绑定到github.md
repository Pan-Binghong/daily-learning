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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3I3PMPN%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T042009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1RVOD6LBzbiymGBhIQmtmo0DdYFMPq1iuqk3ELUOSLwIgCE5d9u8onJFzOpFkzirmL1CcAvvGjZk6buxHnprWP30q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDApH1ONQmeAzO4FXBircAxio0tLJw37C644n%2Bz9xhL4VgEVF0dRKZ0IzEW%2BNDGyfxjH3IlM%2BPGEUxfCXUDmhUDh9ih19mBGcXYPhjxyV1p%2F8WYwx0yQ9rJ%2B0ju4VIQJkpdOaHbvKPCJuC7hHplYgl17OZPhDnNv6Iqh8j51OuS%2BEBkrNIQXyaDRhTroVAVDRZIzcg1zY%2FlpMjcUwUQUiWIy7aj%2F0cLBVKJ66Yny%2B%2FXfqsYj1vczbxQS9Qa0bw7XmSVuRkeouiHhXUQHZjWeEFQflOI2zqgHF3j%2BvpTQ%2BqWs%2B%2FsiO4PdLINBGmYE2I1g4mVVVbk%2F3jUGipIduxtf4R5SJ0ZBF%2FfP8mm9a8VWs6OBGWIROCQbxvPifZ02%2B%2FMZwuFcEMIVHvalKPp%2FEQM5IAnGzbWPkgk9RRFmAZEdF0mnMnYENgDpVUIJwK%2BkllBhP5gxN3Pt96rnFyvKJFzBf1SQ%2F9CsnKUGHOrrnu6xCoacUDFBhn%2BBicQ1npTA%2BGe1Rm6Ge1lVFUSTZY2KPCE28eVj7DGLiWS3PIYSEyOlPbPh8N46pNuWkyHOOlE8gyiS1meIqI3Ui4sJUM6XA5IIw9m0Z810DosNLeU1DNmSO6judLfJuPK1NmXz3QV7Br8%2FI4BQtKnKnmGTNQmDPMNqxq88GOqUBiuI2S6OuIJbUbySU5eRWmcXw%2F1dJgJTNe4ue4kScK2WHLOGZPtMBuLtsCUhYwS45OZF4JO%2Bmmle0huhRrQf9j3Z2GMDpND7a9FIX2XTLQWlw%2BUoPhAT8leihb5M1gyl1ar0hkde1UjyKpuWhcDpTgT5Ik1Y0kNWKiCdew3F9yzF8lEJZZmU4CoiTpNRskTs0Hatxt2jrw46B2qzwoG%2B1en91uH7P&X-Amz-Signature=ea9352fdb610771194b11f74342b8de119906d0bc374f8fd21503b8daf65e44e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3I3PMPN%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T042009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1RVOD6LBzbiymGBhIQmtmo0DdYFMPq1iuqk3ELUOSLwIgCE5d9u8onJFzOpFkzirmL1CcAvvGjZk6buxHnprWP30q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDApH1ONQmeAzO4FXBircAxio0tLJw37C644n%2Bz9xhL4VgEVF0dRKZ0IzEW%2BNDGyfxjH3IlM%2BPGEUxfCXUDmhUDh9ih19mBGcXYPhjxyV1p%2F8WYwx0yQ9rJ%2B0ju4VIQJkpdOaHbvKPCJuC7hHplYgl17OZPhDnNv6Iqh8j51OuS%2BEBkrNIQXyaDRhTroVAVDRZIzcg1zY%2FlpMjcUwUQUiWIy7aj%2F0cLBVKJ66Yny%2B%2FXfqsYj1vczbxQS9Qa0bw7XmSVuRkeouiHhXUQHZjWeEFQflOI2zqgHF3j%2BvpTQ%2BqWs%2B%2FsiO4PdLINBGmYE2I1g4mVVVbk%2F3jUGipIduxtf4R5SJ0ZBF%2FfP8mm9a8VWs6OBGWIROCQbxvPifZ02%2B%2FMZwuFcEMIVHvalKPp%2FEQM5IAnGzbWPkgk9RRFmAZEdF0mnMnYENgDpVUIJwK%2BkllBhP5gxN3Pt96rnFyvKJFzBf1SQ%2F9CsnKUGHOrrnu6xCoacUDFBhn%2BBicQ1npTA%2BGe1Rm6Ge1lVFUSTZY2KPCE28eVj7DGLiWS3PIYSEyOlPbPh8N46pNuWkyHOOlE8gyiS1meIqI3Ui4sJUM6XA5IIw9m0Z810DosNLeU1DNmSO6judLfJuPK1NmXz3QV7Br8%2FI4BQtKnKnmGTNQmDPMNqxq88GOqUBiuI2S6OuIJbUbySU5eRWmcXw%2F1dJgJTNe4ue4kScK2WHLOGZPtMBuLtsCUhYwS45OZF4JO%2Bmmle0huhRrQf9j3Z2GMDpND7a9FIX2XTLQWlw%2BUoPhAT8leihb5M1gyl1ar0hkde1UjyKpuWhcDpTgT5Ik1Y0kNWKiCdew3F9yzF8lEJZZmU4CoiTpNRskTs0Hatxt2jrw46B2qzwoG%2B1en91uH7P&X-Amz-Signature=dd2837921677352ff2d33979d94893619cffab0a2a81acb87e90979710122647&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

