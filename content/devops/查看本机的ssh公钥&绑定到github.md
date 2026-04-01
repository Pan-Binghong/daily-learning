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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6YJYL5L%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgne3O7%2BoX64vqRoL6vwxLo%2BIUBPl1m%2B55gOfEN0RFbwIhAJbDLXw0vGsCzLVoNpt%2B4%2BCB0W6kFjGlGGsOSOqA%2FOTSKv8DCE0QABoMNjM3NDIzMTgzODA1Igz2LBnSyVdbMXcAcxgq3AOhhmiGuk7j25OKjNFyO%2BKJFzushL%2FKtTvB7brDkRluFqZWdUEGngbhI%2FCy31DUnkmbeZcIg%2FQr3QEcaFsqjmVZHZ1WYnZB1VobUsn7POTFEAurwOTsMHV2P0C3LO22RWGtsgdGiZT%2Fu0WbRjo6YLnBWRj9uhfp3Zc7cacBmo0jqMmVwy1GoVEBmWf3EfnfGRB8AsnRfjCfOKiGDxa8fjCx3GwapfKnXZrM7ZE%2FYmg5sP0jqLAyIAC8dBvDanjMpRsu55RX7G94DjwFNnQmF56SDdNGANwzNceNN91IK0HjFdGUGk4KKm399Flhn7YSe7I9kb%2FHmpw59BgQSLbivI2t9OhhpX0KJAMjxnJEqwXcGtEkL2jlsHa5vPk4JelKFNCt1AiiZdDINib9x1girYtsN4u0jaNX8PWBWni3m%2B9DqgkxZa2vo50cchzot1cyzzV2r8VWThwtHYANkHISg6f20cQ5craQtZBJPs2ImJ2PYCbt8jMLkowZ0UGiiwa3lUP6wYh4SSHN%2FPH%2Fn1dLBdx73iuY3XBMXBJqQo1FzIkkO5VBOHQ%2BDah8NyRpneF7VyBiGQ8k0pGGtnyORdRCGI%2FJb9sNsizHjWFcWuPG%2B3mqi0GjwLXkSCKCm8gobjDuobLOBjqkAdoVauAxSdDISpVR%2B6tXxXxIj%2FcKDetJHW9WuBXg2NiiD%2Bshzjf0FXS6g8wdZ3c8C02MF81JhVXra2fIoYXoWejj34x3RICPLs861aem29R2tTzUJe3Bey7RbRfie1uUzv593qVban2jeLHyKwZxmTSmZsOuhgnkHBfjB7vgh%2FHSf4n0tpHCHialxVRktfBmg6s8uaVzd4HH1oOYRKfltEedF3sF&X-Amz-Signature=b9a0a2cd4644e5bc0e050c8115963b6651daa817925bb93ec5aa113fe0124f5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6YJYL5L%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgne3O7%2BoX64vqRoL6vwxLo%2BIUBPl1m%2B55gOfEN0RFbwIhAJbDLXw0vGsCzLVoNpt%2B4%2BCB0W6kFjGlGGsOSOqA%2FOTSKv8DCE0QABoMNjM3NDIzMTgzODA1Igz2LBnSyVdbMXcAcxgq3AOhhmiGuk7j25OKjNFyO%2BKJFzushL%2FKtTvB7brDkRluFqZWdUEGngbhI%2FCy31DUnkmbeZcIg%2FQr3QEcaFsqjmVZHZ1WYnZB1VobUsn7POTFEAurwOTsMHV2P0C3LO22RWGtsgdGiZT%2Fu0WbRjo6YLnBWRj9uhfp3Zc7cacBmo0jqMmVwy1GoVEBmWf3EfnfGRB8AsnRfjCfOKiGDxa8fjCx3GwapfKnXZrM7ZE%2FYmg5sP0jqLAyIAC8dBvDanjMpRsu55RX7G94DjwFNnQmF56SDdNGANwzNceNN91IK0HjFdGUGk4KKm399Flhn7YSe7I9kb%2FHmpw59BgQSLbivI2t9OhhpX0KJAMjxnJEqwXcGtEkL2jlsHa5vPk4JelKFNCt1AiiZdDINib9x1girYtsN4u0jaNX8PWBWni3m%2B9DqgkxZa2vo50cchzot1cyzzV2r8VWThwtHYANkHISg6f20cQ5craQtZBJPs2ImJ2PYCbt8jMLkowZ0UGiiwa3lUP6wYh4SSHN%2FPH%2Fn1dLBdx73iuY3XBMXBJqQo1FzIkkO5VBOHQ%2BDah8NyRpneF7VyBiGQ8k0pGGtnyORdRCGI%2FJb9sNsizHjWFcWuPG%2B3mqi0GjwLXkSCKCm8gobjDuobLOBjqkAdoVauAxSdDISpVR%2B6tXxXxIj%2FcKDetJHW9WuBXg2NiiD%2Bshzjf0FXS6g8wdZ3c8C02MF81JhVXra2fIoYXoWejj34x3RICPLs861aem29R2tTzUJe3Bey7RbRfie1uUzv593qVban2jeLHyKwZxmTSmZsOuhgnkHBfjB7vgh%2FHSf4n0tpHCHialxVRktfBmg6s8uaVzd4HH1oOYRKfltEedF3sF&X-Amz-Signature=73045f9429bf2930f2d23c6576c9d3332ecca83bcc1e7d2781ea6c9d82656e85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

