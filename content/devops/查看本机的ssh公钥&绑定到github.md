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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDX42HXQ%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCICKFYOEmctno5cHyE6iIF27%2F7Rn3LMDjUd2rVZpEyy%2BZAiEAu1KVn1vwPTKUrdoJ1ylI%2FZDO%2FcvUbsqmgBocpeZNyUEq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIv2XEIhGG0%2FN3FOEyrcAwJ2dBSKceO7H5X8qPk3Jbr2BXKe8JPQZmfFwcZEiXasctFmUdxrCvdDJeEVyvnJ7OFt2dBE99BktcYMDadm1CJnuW6JZ9VZBtSlPT2W8FfEoAFnq%2FBIv%2BRTj%2FEgCL9Nua9HcsFqy%2BmdQLKYkE9%2FE0dwFnKD8rpqztwrSmqnK%2BqG1ogDAha13an08RRtfK3eIeoz3YxUbdGyzXdizSzpM3RishG43L9lHUmt2z%2FxnjImX79OZhA3ivnlFLplRKXGtcqH8Pa72Djkz93FjSttSR%2B3f5E44fjY8bQ8qBq92MDZr7foXG7kp%2FGQIO%2BzLpNb85sNXo6SCtB6joiHqiggDKMnOYCrL7bKCU7cJkoY54Pa860Rc531%2FdayFxsStFr1taUwSkE9pEnMhrolJL2ha%2BCBZvziMKp%2FbnzB2t8IGyqcSk97QZGFaSh0s0Rx4nbmmZYDAUzTtOrX0qVtuzlPOqg7wh%2F9z%2BfT9sbrOMe1TcCa7EAGuNPQ7tsLM5mxBCpRjAulIPRckY9BujAfZENbKcJnxTuDiJK1qnMqa%2FINstMazYeu6uQ99gIh5Eq1d%2BOzOrTguGFRH1qvx0PT3nE%2FonA1IYl%2FHkBu74QXkutFvXTuq2zf%2BSJx9ceoFRTWMLGUyswGOqUBZyEOm3cTPUoCl59MY8lXmUxCUX9sMbEV5uZpOiBHmxGGo%2FoAnn9DFNyABHWTglnE0BmPZE%2B0yFwnttI8mJQkLK3lyBz9mI0otgbZWilzpswr4ejmfOw31gpbdgf8%2FZngRQ66%2BVsL%2BTlU6augbWC7Rbbhzw%2BU9Ao0VjSWdMg%2FSaTV2ffSwTEt%2FNPkOcmbis9q4vuEhguQW8k7moAClvNPTYZ0cy0z&X-Amz-Signature=4a3f829035a9e9ba58a750d4cefd3c776e5195f3dcb02828605f9f62f9c8cb5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDX42HXQ%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCICKFYOEmctno5cHyE6iIF27%2F7Rn3LMDjUd2rVZpEyy%2BZAiEAu1KVn1vwPTKUrdoJ1ylI%2FZDO%2FcvUbsqmgBocpeZNyUEq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIv2XEIhGG0%2FN3FOEyrcAwJ2dBSKceO7H5X8qPk3Jbr2BXKe8JPQZmfFwcZEiXasctFmUdxrCvdDJeEVyvnJ7OFt2dBE99BktcYMDadm1CJnuW6JZ9VZBtSlPT2W8FfEoAFnq%2FBIv%2BRTj%2FEgCL9Nua9HcsFqy%2BmdQLKYkE9%2FE0dwFnKD8rpqztwrSmqnK%2BqG1ogDAha13an08RRtfK3eIeoz3YxUbdGyzXdizSzpM3RishG43L9lHUmt2z%2FxnjImX79OZhA3ivnlFLplRKXGtcqH8Pa72Djkz93FjSttSR%2B3f5E44fjY8bQ8qBq92MDZr7foXG7kp%2FGQIO%2BzLpNb85sNXo6SCtB6joiHqiggDKMnOYCrL7bKCU7cJkoY54Pa860Rc531%2FdayFxsStFr1taUwSkE9pEnMhrolJL2ha%2BCBZvziMKp%2FbnzB2t8IGyqcSk97QZGFaSh0s0Rx4nbmmZYDAUzTtOrX0qVtuzlPOqg7wh%2F9z%2BfT9sbrOMe1TcCa7EAGuNPQ7tsLM5mxBCpRjAulIPRckY9BujAfZENbKcJnxTuDiJK1qnMqa%2FINstMazYeu6uQ99gIh5Eq1d%2BOzOrTguGFRH1qvx0PT3nE%2FonA1IYl%2FHkBu74QXkutFvXTuq2zf%2BSJx9ceoFRTWMLGUyswGOqUBZyEOm3cTPUoCl59MY8lXmUxCUX9sMbEV5uZpOiBHmxGGo%2FoAnn9DFNyABHWTglnE0BmPZE%2B0yFwnttI8mJQkLK3lyBz9mI0otgbZWilzpswr4ejmfOw31gpbdgf8%2FZngRQ66%2BVsL%2BTlU6augbWC7Rbbhzw%2BU9Ao0VjSWdMg%2FSaTV2ffSwTEt%2FNPkOcmbis9q4vuEhguQW8k7moAClvNPTYZ0cy0z&X-Amz-Signature=f84e7c0a2037587602803620c21f6813ded4e462bacc2ed3b740c0b79a269968&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

