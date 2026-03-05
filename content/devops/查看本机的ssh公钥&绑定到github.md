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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLSFJFFR%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGr%2FFo1jWSnk7JyTB9gIsHVzf6sBioXuA%2FpSIAJXjIZAiEAiiYWYeGpgppr4o9VWsq9Re4li8t6Hcjggql12AxDQakqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCwPg8HmYN6bI1%2BHtyrcA2Y0vnnIMXk0C47nt2%2FcZL8tmzZct2Pah3O%2Bwd%2BM%2FncWkuipr2%2BOVZwqUy0dBU96bnroLo2aqAZb31M28TwhBtBtTE6hVEVa%2F8uo0SXVDZsth%2Bgq5%2FTflsiLYFbPC2B43TZJBKPczFhrnOsTYV4OFPDzNvvHiSFtEZTi%2BdRMVGimE%2FOKQjCQ5yYlvgrntFOfTDIVSoOuoJ2PQ0bqiuHHB%2BNn%2BpMFdEpBxWGyWrTh2sKYD1jWb9Szv1AD%2FohUYh4BZrRaOzTp27L7G55swxnHG98MgtMegnHAZKP4OvTrO0Ft2k4yKvPJKDnJv6XkMw2Xr3Ye0P2qk0o8kwmuYWZ5OjJuDVI0%2FYvLjQaN2k0bWm70YaPg1pdwmx8qFe2KIVqN7DEOVN3h8FZHW1Y7WYRi5jm3IbNaw1EW3p74TUhrTm4RmtaxQpKPeRcZ5H5Xz3EKXzDIHYpzJ4%2BTKP0iWgf3ICgU5iCaaQT3bSFQcjt1fiYF%2BQi8bVI9Ti1rn9SlKIzbVCprj3EoofoLirE05bs0Qax3Al%2FaIKGqhDIlqiV%2BfBFjkgVZkqC8ep0otTomJQccuNA22FwQZE2H1CyJlpFBc8ykeHBuoE8odyBrdTvLooG3a6wDcpC1tyWasrUUMOXfo80GOqUBv6DnXe69Y8i%2B5IcgfVf6gmZJymg4D49VuUTDWaCCibOnWddWHM9k80uj24WDcGUUDI59%2BxT8Qeixd%2B5UGFqdUSChX4%2BV2ahp%2BVwTWNQUxHyKmvAmDbX3S%2BoOmfe0ByB%2FOQCgC7sJxtB4ifZxSmeTpzJBS5DEIFYcxVpb7oWVBGL8egBX6EVuhRxY9a0RgBuPexUykXDlkd%2Fb62UPlzL9TAd14S4u&X-Amz-Signature=bc79569ecd5d76e240e9761ec95c8f7695b86603cdff35b41195886c934f047f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLSFJFFR%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGr%2FFo1jWSnk7JyTB9gIsHVzf6sBioXuA%2FpSIAJXjIZAiEAiiYWYeGpgppr4o9VWsq9Re4li8t6Hcjggql12AxDQakqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCwPg8HmYN6bI1%2BHtyrcA2Y0vnnIMXk0C47nt2%2FcZL8tmzZct2Pah3O%2Bwd%2BM%2FncWkuipr2%2BOVZwqUy0dBU96bnroLo2aqAZb31M28TwhBtBtTE6hVEVa%2F8uo0SXVDZsth%2Bgq5%2FTflsiLYFbPC2B43TZJBKPczFhrnOsTYV4OFPDzNvvHiSFtEZTi%2BdRMVGimE%2FOKQjCQ5yYlvgrntFOfTDIVSoOuoJ2PQ0bqiuHHB%2BNn%2BpMFdEpBxWGyWrTh2sKYD1jWb9Szv1AD%2FohUYh4BZrRaOzTp27L7G55swxnHG98MgtMegnHAZKP4OvTrO0Ft2k4yKvPJKDnJv6XkMw2Xr3Ye0P2qk0o8kwmuYWZ5OjJuDVI0%2FYvLjQaN2k0bWm70YaPg1pdwmx8qFe2KIVqN7DEOVN3h8FZHW1Y7WYRi5jm3IbNaw1EW3p74TUhrTm4RmtaxQpKPeRcZ5H5Xz3EKXzDIHYpzJ4%2BTKP0iWgf3ICgU5iCaaQT3bSFQcjt1fiYF%2BQi8bVI9Ti1rn9SlKIzbVCprj3EoofoLirE05bs0Qax3Al%2FaIKGqhDIlqiV%2BfBFjkgVZkqC8ep0otTomJQccuNA22FwQZE2H1CyJlpFBc8ykeHBuoE8odyBrdTvLooG3a6wDcpC1tyWasrUUMOXfo80GOqUBv6DnXe69Y8i%2B5IcgfVf6gmZJymg4D49VuUTDWaCCibOnWddWHM9k80uj24WDcGUUDI59%2BxT8Qeixd%2B5UGFqdUSChX4%2BV2ahp%2BVwTWNQUxHyKmvAmDbX3S%2BoOmfe0ByB%2FOQCgC7sJxtB4ifZxSmeTpzJBS5DEIFYcxVpb7oWVBGL8egBX6EVuhRxY9a0RgBuPexUykXDlkd%2Fb62UPlzL9TAd14S4u&X-Amz-Signature=bef12ff2d79c85bea42ab988169cdcde346dd84d51d09a20ea1202db7dd4fbe7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

