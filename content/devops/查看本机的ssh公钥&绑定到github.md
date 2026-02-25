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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662U2OQ72V%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T034000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIHLzrido%2Bd1MZTnYvV5jOHnVgHH4l36cJ1CU9%2BWgWhNQAiEAqkjU9QpQr2US8Qg%2ByltBNSQLWUmIriag6ESgmnRk7dMq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDNxwCfOG0rsmBd%2FRyircAwF3KbDZn02ZJQei92O1TQMbPOw8%2FZ%2BluVvSZ5Kw1sfjTgKanOn8mxYLxyaTQ9%2FW8mrrieyEMw9d%2BNZfXeCgbVuKlB7l83%2BL6rLUZRDwzTz0BcU%2F6x3kgEPsAHRRJUyKTnn%2Bi67AiwkHeQEGACZz6cIEdo%2FwvKIXEc4QkUQaoMUt6DFAce3x8ykQ4lqODTvZBkCBROZXVLOhjvURGLjrH2ssMHQHRIGIYJAYEXJAO7QwxY7AWWl1JRsrWZBFb%2F5NkJIodW5xgTWXuRLDTL2AtCBBI1MX4qqZdkn2fGnE%2BTOtgR2L6uFVqhzb8ugAaZsRBfsuw8%2FCSfe5jtAcjkfyYh83R3SwLkEuFNGD1%2BChgBjaUqZRqTDXtV%2BWEXoYejGc7weOojI%2Fhywrw5wWK8P9c0jZ2lYzTedZAyX9XXr2KOWoVuKokmZssDaCptRj9D8BPP93bDlwyZ6VRoD4%2FD2zMRTHKD6H%2B9BeBEGglwg6d1RcvS8dbnrpH5Kn9ylGodLo5ljDr5r%2FzpQuH%2FDOnIwOXMLeDumr5lpl2gLZuvPdTpzkczmYwPQm0cuqv89BT%2F0UdyhP4LOWSgYM4yQ2krPCJQ7s%2FTM0BHezErKNsPFy3oQn2OR46y4eogXI1aQrMJbL%2BcwGOqUBJzED1VTRsn7PEolO%2BnjBdULcZrWfoV06d8dNOp8bAXRrX8KMSjIgikXVLl%2FrJU9lIB0wyPeHd%2Fzd3rq%2FQ7AUA3%2BZLwb7bIbvQ3aDM7qOBu%2B%2FNtpQ0xe8quuAesMM%2B3XpTTGYOZTzIKKd3npPH31IlOdsFXWs%2B%2ByDI08xbXqjSyKmfINqLSsLhUERXxjzGBtnjo2ZoXJ%2FiYf9oW27KigqF6VIcGxy&X-Amz-Signature=b711e4f2f6537119db45d19eedf2f00a0159742603cae52076970da03e7b844c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662U2OQ72V%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T034000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIHLzrido%2Bd1MZTnYvV5jOHnVgHH4l36cJ1CU9%2BWgWhNQAiEAqkjU9QpQr2US8Qg%2ByltBNSQLWUmIriag6ESgmnRk7dMq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDNxwCfOG0rsmBd%2FRyircAwF3KbDZn02ZJQei92O1TQMbPOw8%2FZ%2BluVvSZ5Kw1sfjTgKanOn8mxYLxyaTQ9%2FW8mrrieyEMw9d%2BNZfXeCgbVuKlB7l83%2BL6rLUZRDwzTz0BcU%2F6x3kgEPsAHRRJUyKTnn%2Bi67AiwkHeQEGACZz6cIEdo%2FwvKIXEc4QkUQaoMUt6DFAce3x8ykQ4lqODTvZBkCBROZXVLOhjvURGLjrH2ssMHQHRIGIYJAYEXJAO7QwxY7AWWl1JRsrWZBFb%2F5NkJIodW5xgTWXuRLDTL2AtCBBI1MX4qqZdkn2fGnE%2BTOtgR2L6uFVqhzb8ugAaZsRBfsuw8%2FCSfe5jtAcjkfyYh83R3SwLkEuFNGD1%2BChgBjaUqZRqTDXtV%2BWEXoYejGc7weOojI%2Fhywrw5wWK8P9c0jZ2lYzTedZAyX9XXr2KOWoVuKokmZssDaCptRj9D8BPP93bDlwyZ6VRoD4%2FD2zMRTHKD6H%2B9BeBEGglwg6d1RcvS8dbnrpH5Kn9ylGodLo5ljDr5r%2FzpQuH%2FDOnIwOXMLeDumr5lpl2gLZuvPdTpzkczmYwPQm0cuqv89BT%2F0UdyhP4LOWSgYM4yQ2krPCJQ7s%2FTM0BHezErKNsPFy3oQn2OR46y4eogXI1aQrMJbL%2BcwGOqUBJzED1VTRsn7PEolO%2BnjBdULcZrWfoV06d8dNOp8bAXRrX8KMSjIgikXVLl%2FrJU9lIB0wyPeHd%2Fzd3rq%2FQ7AUA3%2BZLwb7bIbvQ3aDM7qOBu%2B%2FNtpQ0xe8quuAesMM%2B3XpTTGYOZTzIKKd3npPH31IlOdsFXWs%2B%2ByDI08xbXqjSyKmfINqLSsLhUERXxjzGBtnjo2ZoXJ%2FiYf9oW27KigqF6VIcGxy&X-Amz-Signature=9ea03da648080b497ea607c2ac919b47b52c509e23d1eac9be561c8650c3da3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

