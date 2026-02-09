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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5F4HC5I%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYjtkp9yr5YF5PpsUjeZHO3%2FnXPgX6ONDJy5Z1d%2FjHbwIgTrBtrMpoX1AuwJkmZQ%2FrDQk7qxmH5jldIjyBZExrhqoqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA1LiWefNyqqnVcNyCrcA8clWDkihoBP6s25lFHQkFKDwvQ7FEqW9oXx9jQIUhjah2x7vvJTWNFzOdaHD7%2BDiB59MRSboZo1PAvm6%2BrU%2F4BcQM5Ld2512OrWTMwZ%2BJALobErbiwPhrOGA6mBWt%2Fa8mJXyhi52yS4hqK%2BYL1SDssLXNuXfWc%2BQw6YYCP2bRi8Yw1SoDIjpjRLbj7j3QOgkEV5xzWh98%2Bb%2BGU8vdC88XKXTNW1VrtZmPoc0FVvVZ6hnvQbo5T4YTptehxMQSe1wlOBg2TslcLCJqM73q7HtX6k98zoIBBqjJUAf0kkUyN3hTy%2B8iS2KzVJJ74nIr9WNt5C6C7VDVqc6%2BaA89HyYjFpBhSjysnt24h0%2BwdIZrag6J0Pl%2FQrAnDCQlf1wbaTXT1rpfoN24FkjO%2F3nRRKx4VXQdRbtZIm5JdfgH7NZO7SBUSsDYhHFw01O3ukXnX3usOVDlOWLYr%2BaB50zFCzfwV14S5UoIEbuui%2FprfbFBhsi%2FZR1%2FOlJpKwCCpdF5lLW%2BbL1b7zzDdWQC8MddnHCprx9PkOdRAxhRw3NYhmlMiBBn4wAMZjQygNbA2zGgCjutDxuwnDZMkK5PuDzNOmz%2FYXRgMaiF02LuOaRTsIJ9McoBOj5r8UvbVsENi4MLOWpcwGOqUBcp0rOvEq7cQAOD7b3h2fsikJgpHsWVQJOYztmLFwkVtjU%2FPG2Vgku%2B5YYiLinjnQKVxZSrWDw7mO6WoX4zHPOW%2BsCsf8WJJK4UxmN5Tcr%2Fsu65WBH5%2FKI3XMn795AFpwhxOvcO4uB1DuGCX61Xm%2Frio0DI88oea0yyN8xSqly5Osp5dCrMzELpwR2TdLvA6uON8uibC1R2qy%2Fb1e6TjchCp5%2BZU6&X-Amz-Signature=4d246b3878ed42603ede87a4d8f4a226bd1febbaae32d9c923e05587908c5e2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5F4HC5I%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYjtkp9yr5YF5PpsUjeZHO3%2FnXPgX6ONDJy5Z1d%2FjHbwIgTrBtrMpoX1AuwJkmZQ%2FrDQk7qxmH5jldIjyBZExrhqoqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA1LiWefNyqqnVcNyCrcA8clWDkihoBP6s25lFHQkFKDwvQ7FEqW9oXx9jQIUhjah2x7vvJTWNFzOdaHD7%2BDiB59MRSboZo1PAvm6%2BrU%2F4BcQM5Ld2512OrWTMwZ%2BJALobErbiwPhrOGA6mBWt%2Fa8mJXyhi52yS4hqK%2BYL1SDssLXNuXfWc%2BQw6YYCP2bRi8Yw1SoDIjpjRLbj7j3QOgkEV5xzWh98%2Bb%2BGU8vdC88XKXTNW1VrtZmPoc0FVvVZ6hnvQbo5T4YTptehxMQSe1wlOBg2TslcLCJqM73q7HtX6k98zoIBBqjJUAf0kkUyN3hTy%2B8iS2KzVJJ74nIr9WNt5C6C7VDVqc6%2BaA89HyYjFpBhSjysnt24h0%2BwdIZrag6J0Pl%2FQrAnDCQlf1wbaTXT1rpfoN24FkjO%2F3nRRKx4VXQdRbtZIm5JdfgH7NZO7SBUSsDYhHFw01O3ukXnX3usOVDlOWLYr%2BaB50zFCzfwV14S5UoIEbuui%2FprfbFBhsi%2FZR1%2FOlJpKwCCpdF5lLW%2BbL1b7zzDdWQC8MddnHCprx9PkOdRAxhRw3NYhmlMiBBn4wAMZjQygNbA2zGgCjutDxuwnDZMkK5PuDzNOmz%2FYXRgMaiF02LuOaRTsIJ9McoBOj5r8UvbVsENi4MLOWpcwGOqUBcp0rOvEq7cQAOD7b3h2fsikJgpHsWVQJOYztmLFwkVtjU%2FPG2Vgku%2B5YYiLinjnQKVxZSrWDw7mO6WoX4zHPOW%2BsCsf8WJJK4UxmN5Tcr%2Fsu65WBH5%2FKI3XMn795AFpwhxOvcO4uB1DuGCX61Xm%2Frio0DI88oea0yyN8xSqly5Osp5dCrMzELpwR2TdLvA6uON8uibC1R2qy%2Fb1e6TjchCp5%2BZU6&X-Amz-Signature=afda65999fe4af2af0bc4ebca763987da2dc2c1473d96a67d87f1f0724742630&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

