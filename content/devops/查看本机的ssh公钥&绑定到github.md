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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y5IM377%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIEXgwqsneg6k5UthJAEwRWIHtfD5C2zYai5WLSIVtoQmAiA6Fm%2Fk71VqJFIztrc7CkGEys0sznmCs0FKc7jo%2F9D3ryqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMm2g1NnfuMvFnWyWBKtwD%2BivtO7zwTSkOS%2BGB24tASroskvrwX3FhF5aOicfgeIViEj2sqEvb5sDgjhU9NItv6KYHU%2BC5AUL73HazU1bgXDbhMJ6cv%2B%2BYAUo52y3SMA3UdSY2llMJ%2FtvhuxtZWYXAh%2FJt85WaB%2BYlUJeKQMGOMIMqIKX4MZksX8vo4sCZrxFz2j44WXOxddu7C9hDK2%2FlDDZdsEQNQkxh9W%2B44czbsotX%2BIe58wQwZlgz3Rx2mHiu7COooDDIepHjuyWpnXg2faCSeNr3mKBWPGEBATsq46moShKEs3uswDBxgZpkiQfI90IPFETy59LdX9jp0FMNWUW%2BgPRe6DFlGAKLCQGh68IZr3KiJ6ah%2ByCwx9R6gOTeHOCQS7WaA0pD38tWpqPoqDVY8EcK77XN0lIKudBVEnvvp75EoWUUKJ%2BYXfbY55bYQISSMm2Xjhl2wjS915cbFrHW3GYaG8nwq4k%2FbrvwRTK93YlYHY2ATCLBNEP1xJXVdGrpOg8pLHSmbf5ZjU%2BN2T9UO1VyaFCU1GDSF0OTv11wDyOwSvnMk9hQTNYUDtPi6OPpeEnlyaeNpIjb0dSgomyH4y3RPfVYYMeIZlM8PqFZPPbWfnW%2BPhVRWnVMy7O5hnYKrVMPbI8n%2FPswp6yLzwY6pgGEEjhQ3jt1FP13arbVG8%2B5tHdg7TGytPYaoRSzQu%2Fni7dvebPBXO4ukNJGnw00SXcFQq46d9DTL%2BdDlVAZYZkaWPtKQbT4Vn7%2Ff%2FznBhdVjNRwg7L4MWEj6nritzFlrsCZGdNWT7GBbjYi0Vt7LrXK0rhSo0VfcmlNTBf%2FONzRvvdAGftOk2oiiyzRsfbKtDMgcomUfK0DXwi0ULynG%2F%2Fz7LJAgmdd&X-Amz-Signature=118098cfe75a00656b52429d0be0fd7ed126335d168907f4cbf5be330a92ca12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Y5IM377%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIEXgwqsneg6k5UthJAEwRWIHtfD5C2zYai5WLSIVtoQmAiA6Fm%2Fk71VqJFIztrc7CkGEys0sznmCs0FKc7jo%2F9D3ryqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMm2g1NnfuMvFnWyWBKtwD%2BivtO7zwTSkOS%2BGB24tASroskvrwX3FhF5aOicfgeIViEj2sqEvb5sDgjhU9NItv6KYHU%2BC5AUL73HazU1bgXDbhMJ6cv%2B%2BYAUo52y3SMA3UdSY2llMJ%2FtvhuxtZWYXAh%2FJt85WaB%2BYlUJeKQMGOMIMqIKX4MZksX8vo4sCZrxFz2j44WXOxddu7C9hDK2%2FlDDZdsEQNQkxh9W%2B44czbsotX%2BIe58wQwZlgz3Rx2mHiu7COooDDIepHjuyWpnXg2faCSeNr3mKBWPGEBATsq46moShKEs3uswDBxgZpkiQfI90IPFETy59LdX9jp0FMNWUW%2BgPRe6DFlGAKLCQGh68IZr3KiJ6ah%2ByCwx9R6gOTeHOCQS7WaA0pD38tWpqPoqDVY8EcK77XN0lIKudBVEnvvp75EoWUUKJ%2BYXfbY55bYQISSMm2Xjhl2wjS915cbFrHW3GYaG8nwq4k%2FbrvwRTK93YlYHY2ATCLBNEP1xJXVdGrpOg8pLHSmbf5ZjU%2BN2T9UO1VyaFCU1GDSF0OTv11wDyOwSvnMk9hQTNYUDtPi6OPpeEnlyaeNpIjb0dSgomyH4y3RPfVYYMeIZlM8PqFZPPbWfnW%2BPhVRWnVMy7O5hnYKrVMPbI8n%2FPswp6yLzwY6pgGEEjhQ3jt1FP13arbVG8%2B5tHdg7TGytPYaoRSzQu%2Fni7dvebPBXO4ukNJGnw00SXcFQq46d9DTL%2BdDlVAZYZkaWPtKQbT4Vn7%2Ff%2FznBhdVjNRwg7L4MWEj6nritzFlrsCZGdNWT7GBbjYi0Vt7LrXK0rhSo0VfcmlNTBf%2FONzRvvdAGftOk2oiiyzRsfbKtDMgcomUfK0DXwi0ULynG%2F%2Fz7LJAgmdd&X-Amz-Signature=5610b5114f5334fbbfee7777a7a7554223955714dcadbb9183eae969e684cf71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

