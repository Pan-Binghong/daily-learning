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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KZQWXL%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQDDsCvk1tvdtwKiNTcXcY5dvivuGA50MVDCfdlcVDf0VgIgbKa9UIPlf3O27TKaiA7Uho2UROx7tez8VLBiCPTHjzkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCSFOpG3J972niekFircAxV5e%2BHHcJAedr0sZxPYU%2FDjWQAoRv254pFUGyiABqc9o20r%2BFgTQQE8q%2BAtH9aIeelmwIekJFAFw21dKsWuWcOPRmqRIkKSmCT2RV%2FjXqc57mDjzq4%2B2jH7v5sPY4DE0563%2B8gQ%2FceNMDONeN7x5sovnmRewwcKSYtyo%2BsHQlYfaYH5TwHph3kewbypYQJ3AYXMmF%2FPenzhKFXsAKxDDE5xPxWUmG1PLFBVdYlKlVMpLmmYZ0jJ5k0hUQnxgeJj4yytkk8CPyHtNFVugvFjMVdQCghP1aycCfzciKAvbGPy%2FEz9ya04M1C%2BhacBNN6hTQQZr0yAeM4mEKN0EjR07Q6EiSoNrLq%2F8%2FNkXtyfEjogASjtec4gzJ%2B8yFOghOQWB45LLEyWsJBW45Ki0arDuELRG4U11yrhDZXEh4CHIgo6yZP%2FSBK%2BFFF01oq8j32rlxoL1vkSnvEvpN2X5nb3iVXLIgudjgUIXB4vRDWD47UQsuqMWr3OExKhgDQL%2FqVjfDAHwFljttv8Ios55lah%2FIFcFCBtqDA01ZSxGTjJcprIqeq0k9WMxL%2F2SSfrNAF0Oh%2B35yAhnnGydblxihEMMMW9jztZR4d74Lb2pHIP9S8mt7opawwCnR2IYWMXMNe19MwGOqUBG19imfY3M7jykqRICy024OkdJuvbQnfPwy0VA5nLXMzIeILT7ofxR34EcacAZWEVLTWL2ytCY3HXUWFeXF8pUaC5eBcnpB9p%2Fer8x8zlhS28qYVrXmH%2Bz3JalFEQkjmmzvG935UVQIL5unC7zxQlLWgh5PLs37GA%2Fz93Nss%2FCPxibIPVgvKpaCKdbOmCYdOAwylJTt2XWhbVKjfuIt5RnAyWV2DI&X-Amz-Signature=1cb2e751da7ea072f536e8005d39b4af5ea28fea05fb87ae8598fb99ffaf58bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3KZQWXL%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQDDsCvk1tvdtwKiNTcXcY5dvivuGA50MVDCfdlcVDf0VgIgbKa9UIPlf3O27TKaiA7Uho2UROx7tez8VLBiCPTHjzkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCSFOpG3J972niekFircAxV5e%2BHHcJAedr0sZxPYU%2FDjWQAoRv254pFUGyiABqc9o20r%2BFgTQQE8q%2BAtH9aIeelmwIekJFAFw21dKsWuWcOPRmqRIkKSmCT2RV%2FjXqc57mDjzq4%2B2jH7v5sPY4DE0563%2B8gQ%2FceNMDONeN7x5sovnmRewwcKSYtyo%2BsHQlYfaYH5TwHph3kewbypYQJ3AYXMmF%2FPenzhKFXsAKxDDE5xPxWUmG1PLFBVdYlKlVMpLmmYZ0jJ5k0hUQnxgeJj4yytkk8CPyHtNFVugvFjMVdQCghP1aycCfzciKAvbGPy%2FEz9ya04M1C%2BhacBNN6hTQQZr0yAeM4mEKN0EjR07Q6EiSoNrLq%2F8%2FNkXtyfEjogASjtec4gzJ%2B8yFOghOQWB45LLEyWsJBW45Ki0arDuELRG4U11yrhDZXEh4CHIgo6yZP%2FSBK%2BFFF01oq8j32rlxoL1vkSnvEvpN2X5nb3iVXLIgudjgUIXB4vRDWD47UQsuqMWr3OExKhgDQL%2FqVjfDAHwFljttv8Ios55lah%2FIFcFCBtqDA01ZSxGTjJcprIqeq0k9WMxL%2F2SSfrNAF0Oh%2B35yAhnnGydblxihEMMMW9jztZR4d74Lb2pHIP9S8mt7opawwCnR2IYWMXMNe19MwGOqUBG19imfY3M7jykqRICy024OkdJuvbQnfPwy0VA5nLXMzIeILT7ofxR34EcacAZWEVLTWL2ytCY3HXUWFeXF8pUaC5eBcnpB9p%2Fer8x8zlhS28qYVrXmH%2Bz3JalFEQkjmmzvG935UVQIL5unC7zxQlLWgh5PLs37GA%2Fz93Nss%2FCPxibIPVgvKpaCKdbOmCYdOAwylJTt2XWhbVKjfuIt5RnAyWV2DI&X-Amz-Signature=a930b4379e2c8a50809d5ea2ba1a8a7be4d1e57ce4cdf99434db6831845c8051&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

