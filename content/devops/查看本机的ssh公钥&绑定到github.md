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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LE4NHHJ%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFlGzXBlPW2ALVU25hm3lBO8LZ%2Fv8mJoOY3TTflmLKyLAiBENSRhqjmvHi2PXLVx3HTtmVEt%2Fi3V79Dom%2BOHVRBbiSr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMPUL2iOivBNw1oguDKtwDIu4Ams9%2FmqPXKudD4inheyV6%2Bk7kUnhPCOo%2FIG4IdsWgE88jGlhu9Tk9Jo2s0to0EncuvMan5GVq1jRuxJelsedPQXxL1OqnUrKZVhzMGWJ9I3MrQydBV0QxKmMKjceuCs51I4gE767jtX%2BFi8x5%2F3fWrKujyUL%2BFID8QPlxCdyVQYG9DA5d7PQuWl1YaoEL50rbfqo9t1BT%2Bg14%2B59Ks58j7G0T4apxgjaQLDaTsLGmmuc33fIoY5p0RqJkrT67hMcMxLyXJWEt9Ey8j1wB1%2F9iUrf6gr%2BjgSbEAHh%2F3OajLeqrCewP%2BdDLmHBk0RAE52w7XrxOh2WrUNs1tslkmgQlzE54uf12i%2Bt5vXkMbte6Cz7Lvj5tJ%2Bj9Z%2BlhZmWkGg73pmtLMogLJHBHDVqPsnkr%2BcbKfFZjP8n3DBLfup0v8wfo6SBWP245x30knrAOGskhCQ5viMPfsofV9kbbdMGVehVzlc7InDv8AV3fbpFtkZiu31WcSkikxnPMYAavR1Zlt%2BVrwgRPuVcqBW%2Fq6Fa2BmV3A%2BCZ%2B3q%2B%2B8CklePsuWfpiJu5%2BCEy9LHTT3vI4%2FXZYRxdwNJZ3r1HHWr3cFlB2jI3A3kiyj9p2AO0VgzxANdqVv9kX2M6obMwv6z9zQY6pgFS5k9kxCbq8U0GsEGNTA4SkzBHrcrWT4VFwUp4%2Bv%2BjW%2FVLck%2BXsGMrT2VMXmuyI2yr%2FgSAVWt2C4gWbYtCyZYhCxshmePI1v6ikPukoJOdAP5OffG4iYVmN1Aj8ZIcRMnQkjovA8jIPEVp918Q4hU25f%2BB81Hr1kUkmYCAlXvrKerAQk0qmITuIYib%2Bv1IlY3xfZo2xYvaEwcxSN3%2BGqSluccm7Vjv&X-Amz-Signature=1dbb5b0cb9d0532c6b17b37e08f076587f3d766ea196ee9e51ca146b3ed972c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LE4NHHJ%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFlGzXBlPW2ALVU25hm3lBO8LZ%2Fv8mJoOY3TTflmLKyLAiBENSRhqjmvHi2PXLVx3HTtmVEt%2Fi3V79Dom%2BOHVRBbiSr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMPUL2iOivBNw1oguDKtwDIu4Ams9%2FmqPXKudD4inheyV6%2Bk7kUnhPCOo%2FIG4IdsWgE88jGlhu9Tk9Jo2s0to0EncuvMan5GVq1jRuxJelsedPQXxL1OqnUrKZVhzMGWJ9I3MrQydBV0QxKmMKjceuCs51I4gE767jtX%2BFi8x5%2F3fWrKujyUL%2BFID8QPlxCdyVQYG9DA5d7PQuWl1YaoEL50rbfqo9t1BT%2Bg14%2B59Ks58j7G0T4apxgjaQLDaTsLGmmuc33fIoY5p0RqJkrT67hMcMxLyXJWEt9Ey8j1wB1%2F9iUrf6gr%2BjgSbEAHh%2F3OajLeqrCewP%2BdDLmHBk0RAE52w7XrxOh2WrUNs1tslkmgQlzE54uf12i%2Bt5vXkMbte6Cz7Lvj5tJ%2Bj9Z%2BlhZmWkGg73pmtLMogLJHBHDVqPsnkr%2BcbKfFZjP8n3DBLfup0v8wfo6SBWP245x30knrAOGskhCQ5viMPfsofV9kbbdMGVehVzlc7InDv8AV3fbpFtkZiu31WcSkikxnPMYAavR1Zlt%2BVrwgRPuVcqBW%2Fq6Fa2BmV3A%2BCZ%2B3q%2B%2B8CklePsuWfpiJu5%2BCEy9LHTT3vI4%2FXZYRxdwNJZ3r1HHWr3cFlB2jI3A3kiyj9p2AO0VgzxANdqVv9kX2M6obMwv6z9zQY6pgFS5k9kxCbq8U0GsEGNTA4SkzBHrcrWT4VFwUp4%2Bv%2BjW%2FVLck%2BXsGMrT2VMXmuyI2yr%2FgSAVWt2C4gWbYtCyZYhCxshmePI1v6ikPukoJOdAP5OffG4iYVmN1Aj8ZIcRMnQkjovA8jIPEVp918Q4hU25f%2BB81Hr1kUkmYCAlXvrKerAQk0qmITuIYib%2Bv1IlY3xfZo2xYvaEwcxSN3%2BGqSluccm7Vjv&X-Amz-Signature=60d56fec4215a36223ed01b1043fc7cc7655e7a21951ace013e4b407fc310e15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

