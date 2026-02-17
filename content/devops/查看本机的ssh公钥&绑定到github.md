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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4PT55SN%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIBi5NKM%2B6NzQ0vwsBIEywChhglXz9x1vMVKymqCujxFFAiEAmUIrEaAMeRgk%2F3u7gQM2tlD2GbD2PmevuJTwZQ2dzgkq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDPdF9J7OshVr9S7%2F0yrcA1GUeK2IWvjSsuSQ0JHHtsTjRYn7ATeDOAaUynul4OJ9XZiNi3Y1TanE3rXSq5L07GZYUCb8cGtKaTxvc4uKVIfiOlO%2BF51MjOg7Ndgs032ihbmMsgG%2BD405qRhsUelqFzQ%2B3C1G2ckmMoOQwOhHwh60Do53nc%2FX0apTFZz1N%2FBUcBm105pTgwoNEjSd90mHBqZbeWSpYBhEAefjyhjsydB%2FkQaFa4xpoOPG5dGYf5gUAuRTst%2B7M56548RfH38nDb%2FFi1Y8fntWyStbdSyRlU8VorO82SS%2F3APy2XO465l%2ByaSdbi6hhCZBiC3ky9sRHNPN1SNhFvlROjWGKA5wCtMFcdhaJo9ppRmDjhNUzy46V%2B%2FUduznZzCDrJ%2F9FpbVS8dKFQq0WCsKfX00vB%2BtJRNr3zJIfZ63e5%2BDvho8fVJYYvOgGr8796NXJdOeeCwbYfjlZPMbl9P3SKa0%2F88XYCpD8nQ8QxcsPGJ58o8H3Hbn8KttaNl7aH6jvBDJ4Y96TFpD%2BZmrT%2FNB7SrOMN9pTPVssAmEeX8QGW%2BZ5mlN35UxIcXJ0%2BdCG89Y7B46Z9PXEATQIeZqHfU2VvYnTglDiN%2FEEB76wkvr7ngXcDjeQqtgnooH47DHmXEuFuVmMI3Az8wGOqUBfdPCKllKzDAyMonWfNbd%2FXo6BBKoDn4VbeK1GukhWQf5mnyjQH9L1p25JsEAkBbVrZUmxD3dVQ42vzDo3bZwh2eXLD%2Fpmvz0mCQsXWkSw1qmdUWVKwXbpw%2FkgfzvOAkpnmv6fj9Es2RJIU%2B3AZdqEo8YC6Yf1JG%2FLqSJ%2BB1dfAF2iH%2F9rvvyDinbk%2BP65%2FCGszyViVOmMW%2FoAC4b3iaxrc2htNNF&X-Amz-Signature=6b52dfd408cfced84bec8dd938677bace22ed519c4eab7e3bfcb0603aa12c313&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4PT55SN%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIBi5NKM%2B6NzQ0vwsBIEywChhglXz9x1vMVKymqCujxFFAiEAmUIrEaAMeRgk%2F3u7gQM2tlD2GbD2PmevuJTwZQ2dzgkq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDPdF9J7OshVr9S7%2F0yrcA1GUeK2IWvjSsuSQ0JHHtsTjRYn7ATeDOAaUynul4OJ9XZiNi3Y1TanE3rXSq5L07GZYUCb8cGtKaTxvc4uKVIfiOlO%2BF51MjOg7Ndgs032ihbmMsgG%2BD405qRhsUelqFzQ%2B3C1G2ckmMoOQwOhHwh60Do53nc%2FX0apTFZz1N%2FBUcBm105pTgwoNEjSd90mHBqZbeWSpYBhEAefjyhjsydB%2FkQaFa4xpoOPG5dGYf5gUAuRTst%2B7M56548RfH38nDb%2FFi1Y8fntWyStbdSyRlU8VorO82SS%2F3APy2XO465l%2ByaSdbi6hhCZBiC3ky9sRHNPN1SNhFvlROjWGKA5wCtMFcdhaJo9ppRmDjhNUzy46V%2B%2FUduznZzCDrJ%2F9FpbVS8dKFQq0WCsKfX00vB%2BtJRNr3zJIfZ63e5%2BDvho8fVJYYvOgGr8796NXJdOeeCwbYfjlZPMbl9P3SKa0%2F88XYCpD8nQ8QxcsPGJ58o8H3Hbn8KttaNl7aH6jvBDJ4Y96TFpD%2BZmrT%2FNB7SrOMN9pTPVssAmEeX8QGW%2BZ5mlN35UxIcXJ0%2BdCG89Y7B46Z9PXEATQIeZqHfU2VvYnTglDiN%2FEEB76wkvr7ngXcDjeQqtgnooH47DHmXEuFuVmMI3Az8wGOqUBfdPCKllKzDAyMonWfNbd%2FXo6BBKoDn4VbeK1GukhWQf5mnyjQH9L1p25JsEAkBbVrZUmxD3dVQ42vzDo3bZwh2eXLD%2Fpmvz0mCQsXWkSw1qmdUWVKwXbpw%2FkgfzvOAkpnmv6fj9Es2RJIU%2B3AZdqEo8YC6Yf1JG%2FLqSJ%2BB1dfAF2iH%2F9rvvyDinbk%2BP65%2FCGszyViVOmMW%2FoAC4b3iaxrc2htNNF&X-Amz-Signature=e9bb5707de749c216f2d855a6b4099b663a54769f357cadc41946eb3397c2d48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

