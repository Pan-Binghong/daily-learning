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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ENDA62Z%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCMcex2MRNUIIby%2BeYZmLT4ljF21bbQ3YndWUnj9Sf0mAIgZUEdUNF8YQWWgCyA6MnXsPDhGSowcW0qgyHRtRfi%2FEoq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDCUHyHwOfgGfSe1R%2FSrcA0ypq0tyoKA597BEfUSTBJ69A9f5opMBa87lw9uxZZ6SjoFBAUP6IC%2FtEqulagmwK1X0lYRIWI4EtHW7oVQvzUUmBes3F%2FEEHeKIq%2B7CFv2ptjeBeQAKuyjK5p88fiBAN0lz8oOQb6S1tUJNvVeH36I5unnQOJXG51VpIUgqKoDcnLYB4HgtDHMEmYPvy%2Bwue%2FgyDbmvT05XSGN843ImSy0lKI%2FFt8ioKa4EluLQ0SV6xRbQaF%2BYlm7UavQIsw6JcPuYwk%2FO2tKjNjP4E30JiVf3RWty2UYbk5V4idp8yiedEa3g3RQ17TSNSEwvdBkUR6Ee3ksE2LM6TUw1sU%2F%2FDHDWnvJ%2FCPIvyvoL%2FaITApKDasMhin8Of88sKndXrGdEqncAKKc1j%2FsrABV%2F8AF45jRxUlKIpxyrFIMOJmLlbpNeG7AV%2FcNcCpXf49%2FJBtiHrmtl5egSfUBrtW7nx2tAxNARPV6HgXAA4jxHEnJRBz3oBhi6737oh26b3t%2FFwdSfkXOdWXB7n3W4pRUcu74ibXxhbE%2FQHvTiDpHhr73dc1v9i%2BP3x3gHRpba%2F72rn7AOjli1WyV4VVv1JzBG%2BG8TXwuThsrcZJQUek7wtLdTbaI1moiNCH%2FCCSHYeVcmMPOSkMwGOqUBw61ltLN7FJhqXzMPAOCUCu4Kwy58k5KhvNqy8UZEwUKbQDogseA%2B2E%2Fvs4BlFCoxFISLvZYoA%2FCca8VMHaeUPyBm2SQaYfXKOGM%2BQsAupvRoqkF6HgcOX%2B9Oionhq%2F9F0y2qOj8Rha2Qag%2BdS4A2odu0hRHge8daBWD3ZcfpKT0A21F7rqnqbSIdEci2ThbzFKvaQZVDimizPlXN7Mb4FYSqaGT%2B&X-Amz-Signature=60e9b5909d54238ab1cf39df7e0af20deb264d63abe6a5da558229589f8395d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ENDA62Z%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQCMcex2MRNUIIby%2BeYZmLT4ljF21bbQ3YndWUnj9Sf0mAIgZUEdUNF8YQWWgCyA6MnXsPDhGSowcW0qgyHRtRfi%2FEoq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDCUHyHwOfgGfSe1R%2FSrcA0ypq0tyoKA597BEfUSTBJ69A9f5opMBa87lw9uxZZ6SjoFBAUP6IC%2FtEqulagmwK1X0lYRIWI4EtHW7oVQvzUUmBes3F%2FEEHeKIq%2B7CFv2ptjeBeQAKuyjK5p88fiBAN0lz8oOQb6S1tUJNvVeH36I5unnQOJXG51VpIUgqKoDcnLYB4HgtDHMEmYPvy%2Bwue%2FgyDbmvT05XSGN843ImSy0lKI%2FFt8ioKa4EluLQ0SV6xRbQaF%2BYlm7UavQIsw6JcPuYwk%2FO2tKjNjP4E30JiVf3RWty2UYbk5V4idp8yiedEa3g3RQ17TSNSEwvdBkUR6Ee3ksE2LM6TUw1sU%2F%2FDHDWnvJ%2FCPIvyvoL%2FaITApKDasMhin8Of88sKndXrGdEqncAKKc1j%2FsrABV%2F8AF45jRxUlKIpxyrFIMOJmLlbpNeG7AV%2FcNcCpXf49%2FJBtiHrmtl5egSfUBrtW7nx2tAxNARPV6HgXAA4jxHEnJRBz3oBhi6737oh26b3t%2FFwdSfkXOdWXB7n3W4pRUcu74ibXxhbE%2FQHvTiDpHhr73dc1v9i%2BP3x3gHRpba%2F72rn7AOjli1WyV4VVv1JzBG%2BG8TXwuThsrcZJQUek7wtLdTbaI1moiNCH%2FCCSHYeVcmMPOSkMwGOqUBw61ltLN7FJhqXzMPAOCUCu4Kwy58k5KhvNqy8UZEwUKbQDogseA%2B2E%2Fvs4BlFCoxFISLvZYoA%2FCca8VMHaeUPyBm2SQaYfXKOGM%2BQsAupvRoqkF6HgcOX%2B9Oionhq%2F9F0y2qOj8Rha2Qag%2BdS4A2odu0hRHge8daBWD3ZcfpKT0A21F7rqnqbSIdEci2ThbzFKvaQZVDimizPlXN7Mb4FYSqaGT%2B&X-Amz-Signature=18e2923009b5543803a801e15a2a5931f161468d5e1d693f0ac5ad7375f25df9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

