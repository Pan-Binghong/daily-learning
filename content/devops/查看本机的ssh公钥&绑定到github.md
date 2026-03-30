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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLMAKFVG%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIA2xNBiOhiwPzu719d53FOGnRMm4o1%2BE4qTstwuIQqhbAiEAiHbjqWJVpUP6foWa7tXqEQxAK%2FTqumVp8ZaViOG1PdAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDPtQuGdqHz8ztJXNFSrcA56Cx3lcBxgrjnX1K7M82aYqjlKfwfKpHgPE%2FDFUuyOTRYBqL6RvGwXwvXEWqGrLFYK83OVzOGHieb3bHZ30sVXt%2FIp%2F3LG21jAZNg1ojlyJ%2BSooSeks2Cdrph4ECMXfKaoi2EWJlYM1kF2rrKk1v5tDtT92OyxVTT2huXt%2Fz2CCydduNKXQ1z8I4CJS7RY2zYbOg2dRNqHKNcWblkN%2FVllkFZsAvCj99SK%2BURiCzOPf0hah%2FItuXQdG6zA4GTFCnfYFBpitXVp182VWcLEZiQsJQAfbyMTjChufzgGpMSkgelTJtv3lQVLaLi%2F5snctXqgMH6Xji7Ueqr8it9SAKAISzcEEsXXV9ExTNiqO6uE28kykvz5nCBLsKWxV%2BOa0TUl%2BLEcOY1jXSzQSNX1LrNRLXVLkR%2BEHjYGHZ7Y2bJ5Mn%2B6W5RFhpuOBQKcw%2B%2BWicnQH%2BLQkowHU4HafmMejk2PUxWFCa9kPQqphx6DDNoYrjjjBaWH02HkVQ%2BOZ8B7YKcgjPFI6V%2BuhUPYNrp0OUpnSPLz7%2F4ejvn0fMuTn3llI3GnQqQ7hip8%2BcJtWreHDvbvUkKzQhtmSOz6BYXLS8bHK5%2BmmmsbFeH%2FnKnSf%2B5AeT4Dt9UipAo9inuJfMKTHp84GOqUBR1P46Ga7hY4HkABBBH56g2z%2B4KKK8ClJaHnNEe0ehr%2FIL5MbiI%2B3wpG%2B7EK0Kk18NP4h6gPifgPTWb9QTdGAw7di%2F2w82ZZkik5uoldy8sep%2BNm1wjq0LJNaVBp76pxVGKyrG%2BA4WlPokm9zLmhG8CMOi3Ha%2B2lKR9y3ssa3wMXDroJkLcGbc3QjEUp2tjtqi4dPiNn2kk4OEykh1a61BgVh3nip&X-Amz-Signature=d9f898ba17990b3a83830c88183e226fd3d1e50d7bd2f9b1d4e482420ece7414&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLMAKFVG%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIA2xNBiOhiwPzu719d53FOGnRMm4o1%2BE4qTstwuIQqhbAiEAiHbjqWJVpUP6foWa7tXqEQxAK%2FTqumVp8ZaViOG1PdAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDPtQuGdqHz8ztJXNFSrcA56Cx3lcBxgrjnX1K7M82aYqjlKfwfKpHgPE%2FDFUuyOTRYBqL6RvGwXwvXEWqGrLFYK83OVzOGHieb3bHZ30sVXt%2FIp%2F3LG21jAZNg1ojlyJ%2BSooSeks2Cdrph4ECMXfKaoi2EWJlYM1kF2rrKk1v5tDtT92OyxVTT2huXt%2Fz2CCydduNKXQ1z8I4CJS7RY2zYbOg2dRNqHKNcWblkN%2FVllkFZsAvCj99SK%2BURiCzOPf0hah%2FItuXQdG6zA4GTFCnfYFBpitXVp182VWcLEZiQsJQAfbyMTjChufzgGpMSkgelTJtv3lQVLaLi%2F5snctXqgMH6Xji7Ueqr8it9SAKAISzcEEsXXV9ExTNiqO6uE28kykvz5nCBLsKWxV%2BOa0TUl%2BLEcOY1jXSzQSNX1LrNRLXVLkR%2BEHjYGHZ7Y2bJ5Mn%2B6W5RFhpuOBQKcw%2B%2BWicnQH%2BLQkowHU4HafmMejk2PUxWFCa9kPQqphx6DDNoYrjjjBaWH02HkVQ%2BOZ8B7YKcgjPFI6V%2BuhUPYNrp0OUpnSPLz7%2F4ejvn0fMuTn3llI3GnQqQ7hip8%2BcJtWreHDvbvUkKzQhtmSOz6BYXLS8bHK5%2BmmmsbFeH%2FnKnSf%2B5AeT4Dt9UipAo9inuJfMKTHp84GOqUBR1P46Ga7hY4HkABBBH56g2z%2B4KKK8ClJaHnNEe0ehr%2FIL5MbiI%2B3wpG%2B7EK0Kk18NP4h6gPifgPTWb9QTdGAw7di%2F2w82ZZkik5uoldy8sep%2BNm1wjq0LJNaVBp76pxVGKyrG%2BA4WlPokm9zLmhG8CMOi3Ha%2B2lKR9y3ssa3wMXDroJkLcGbc3QjEUp2tjtqi4dPiNn2kk4OEykh1a61BgVh3nip&X-Amz-Signature=5d618112241b154a7b0fed690097df21eaf0f2814594e76b37c6962f7b78afc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

