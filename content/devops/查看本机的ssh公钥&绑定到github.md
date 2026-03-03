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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SC4F4RBW%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiuIjZ%2BHjRTxRY8htGsLbxzUgrI7AiqfV8I2BgC7kyDAIgBWO0vtFPRZni8IwKmHDBFYwDhC1BNzNsFK0TEuHN1yIqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGpAgFWLAs5lpJk%2BYircAxyFfpgvgiOEP8E82kV3UL3AGvargwwxLt9XiwD1NZj0hUsZ2agGfUSRlJA7Jd%2FqxeoPHD5%2BK2INX2mT1xFlkkV2d4Jb7oaku%2BwE6kHEvSYl1UbbOKXUGhlC9gjRrDoHi8zBdLVj%2BDwg3hhNYilR09SRLM0R2%2B%2BhsAI1yY2Gbzsajue11QXKn9jn4O%2Fcp2byqfIPCja5Tj0QpurY%2BUj19S0ik5tezBKUR7qbMaVyDu7UlOnYsMLwhErq%2Bg%2FDrLp9Eq5JJm8FnkAzG2BvkvzltHDwZHUZf0z2%2FjFORb3Pf4eVWdfBs0OG2FsNFtm2DymkGBq7HgyGZ87O09pJMstsgPQ7YerlD2tCs8KtK2Su2NsOrftJokzXp0jR6T6lnNgF6eGY1ETAPSUXxFx2d34HSds3YgsBXsO86UHDcG0R%2FGekGN3qtdMi6hZskb5oObX6fWWv9YmhJI4SjNUWsoSaVIAWsD%2FodBI9qlEDY91LLIaLb89Z5pafZ2RvIEinbxUigmM2fNGRYBRHVJ3qMXu6QtySL%2F2luzCg1UY8U6En8aWwDUqt7NM7jWcQGu%2FA1WtmZVtxtTdJvHoDuBVxv8vn%2BOY5Qzvdztt2trRhegBaND9S858rLhxj73QKroJFMLi2mM0GOqUBTml56aH5BzXXPXejhb%2FJ%2BolUFjdKXioymkTKAWO5w0kSrGgB5ShAmdC%2FjM0LMojs6i3lHwKoWy%2FUifHmRK%2FKVG0DomSmpJ8pIfoPClqHLeczaze8fMzyNWlLH6W%2F6SKRY1RcBgEgyDQN1Yav9M8XcGxKZsAvphSBrPd9rFULAk%2BduddD6DW%2F3SBE8JdHAFdkIZxVvEvp92FeGk4EZ994Sn79yaxR&X-Amz-Signature=e4e0be684925a4745753072acd3efb2ae64fbf3e07b1e8d7f26c54bbaa46ca4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SC4F4RBW%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiuIjZ%2BHjRTxRY8htGsLbxzUgrI7AiqfV8I2BgC7kyDAIgBWO0vtFPRZni8IwKmHDBFYwDhC1BNzNsFK0TEuHN1yIqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGpAgFWLAs5lpJk%2BYircAxyFfpgvgiOEP8E82kV3UL3AGvargwwxLt9XiwD1NZj0hUsZ2agGfUSRlJA7Jd%2FqxeoPHD5%2BK2INX2mT1xFlkkV2d4Jb7oaku%2BwE6kHEvSYl1UbbOKXUGhlC9gjRrDoHi8zBdLVj%2BDwg3hhNYilR09SRLM0R2%2B%2BhsAI1yY2Gbzsajue11QXKn9jn4O%2Fcp2byqfIPCja5Tj0QpurY%2BUj19S0ik5tezBKUR7qbMaVyDu7UlOnYsMLwhErq%2Bg%2FDrLp9Eq5JJm8FnkAzG2BvkvzltHDwZHUZf0z2%2FjFORb3Pf4eVWdfBs0OG2FsNFtm2DymkGBq7HgyGZ87O09pJMstsgPQ7YerlD2tCs8KtK2Su2NsOrftJokzXp0jR6T6lnNgF6eGY1ETAPSUXxFx2d34HSds3YgsBXsO86UHDcG0R%2FGekGN3qtdMi6hZskb5oObX6fWWv9YmhJI4SjNUWsoSaVIAWsD%2FodBI9qlEDY91LLIaLb89Z5pafZ2RvIEinbxUigmM2fNGRYBRHVJ3qMXu6QtySL%2F2luzCg1UY8U6En8aWwDUqt7NM7jWcQGu%2FA1WtmZVtxtTdJvHoDuBVxv8vn%2BOY5Qzvdztt2trRhegBaND9S858rLhxj73QKroJFMLi2mM0GOqUBTml56aH5BzXXPXejhb%2FJ%2BolUFjdKXioymkTKAWO5w0kSrGgB5ShAmdC%2FjM0LMojs6i3lHwKoWy%2FUifHmRK%2FKVG0DomSmpJ8pIfoPClqHLeczaze8fMzyNWlLH6W%2F6SKRY1RcBgEgyDQN1Yav9M8XcGxKZsAvphSBrPd9rFULAk%2BduddD6DW%2F3SBE8JdHAFdkIZxVvEvp92FeGk4EZ994Sn79yaxR&X-Amz-Signature=712f9d969f7f413185169ba2990c675e9c90f0fcd25d6905f7d22efc131ffa51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

