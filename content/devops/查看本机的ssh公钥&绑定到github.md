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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/fe6cede4-097d-4b42-b12f-a631e083d66e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4IYEUXS%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICZvCUqn%2F6PNs9FBZ%2FO%2FPwqhTBzWZpSL83ao5ulXtWcRAiAHuIZALHF2hSBCTewhCO%2B0shnfwKdk7AojJoWfhgSKMir%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMwv5mGo5%2F%2FCRrkUflKtwDLInbeQ5ljWWEaFeBK2gZCkOgWxXKgPXkbdj%2FPIwwlG3VLdGLTKz1qIaA8Nk0Dg8h%2BAmW%2F5XzOAxjYGDl%2Boi2uIIROFCxXd5qZj65N9D79R724gIK1VCcBN%2BXYV3AjEvgIDHyWWf855L7XTLjErBSBS%2BvdxrIAYPnHOFOtgS%2FFWo0Q8WpqaGTqT3GJLwdl7pXlSsMJfUrOQj2vq0tVQIgyikT0OT3C19a%2B1AcnvFKKuLyPkPYnGp1ysd2bxAfhxmfqPEVwanKNGVfNki0SGdI6%2BcRdkerCI3LwV26xK0KXiIGWp5BU2k%2BPyM3rgwpnNKLLbGNBB%2FgLuLbVxKANDwX%2F3WPw%2BMpnM4BKyc1MrsHg0GoKN75Mk94rEQaBj0fBXjqejDZehq12zojrCuCe5uPlMpCDN5x4fXU%2FIGYHAwlzKEbdsp7UG9YKChgTeylOvN5wTX%2FPbUkiHMwJ5laEF6HC39MCCbBo3OFWctqOKsj8fCmnwDRJQzTYJU%2FFe1qoU9gYg3ym%2B3xOxQKFdpLQnrcS%2FEFL8gJtkgfq00A5Qxoob1lToiNyS%2FmhfaAnPq6zQ4Udrp6GixAxsXt4YR2RrNBhPdiomm8J8K%2BHBMyp3QIgeg2sq10mhtea8FYXDkw6rC3zgY6pgGQ31XUBVDdBG1LDqFf4OKsKc2sWBedvk7SGYBY83kVUVrJomL4yVGeIMKsDwlnwJlhuo4TxW5pSVyu1SUA2UALbFWlRb7D20EoZ9ZBFq9z8t5cgoSuqN1gLuCboyFUmTN3OIKuMPe964TeyLL2lCsgFQoPyiLcQKuVyGAsh9KBvDAykldzHmZmXZWruu84ESGpLRVx8BbUi%2BDhkfTsD6wjI8iAtsUb&X-Amz-Signature=3aeecb1d5cab28a6a3e8aedca4102e0d2e2ea5f041c89642c517f4289d576c86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/edba0e64-2598-46d9-91d5-7a4acdc9e627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4IYEUXS%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICZvCUqn%2F6PNs9FBZ%2FO%2FPwqhTBzWZpSL83ao5ulXtWcRAiAHuIZALHF2hSBCTewhCO%2B0shnfwKdk7AojJoWfhgSKMir%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMwv5mGo5%2F%2FCRrkUflKtwDLInbeQ5ljWWEaFeBK2gZCkOgWxXKgPXkbdj%2FPIwwlG3VLdGLTKz1qIaA8Nk0Dg8h%2BAmW%2F5XzOAxjYGDl%2Boi2uIIROFCxXd5qZj65N9D79R724gIK1VCcBN%2BXYV3AjEvgIDHyWWf855L7XTLjErBSBS%2BvdxrIAYPnHOFOtgS%2FFWo0Q8WpqaGTqT3GJLwdl7pXlSsMJfUrOQj2vq0tVQIgyikT0OT3C19a%2B1AcnvFKKuLyPkPYnGp1ysd2bxAfhxmfqPEVwanKNGVfNki0SGdI6%2BcRdkerCI3LwV26xK0KXiIGWp5BU2k%2BPyM3rgwpnNKLLbGNBB%2FgLuLbVxKANDwX%2F3WPw%2BMpnM4BKyc1MrsHg0GoKN75Mk94rEQaBj0fBXjqejDZehq12zojrCuCe5uPlMpCDN5x4fXU%2FIGYHAwlzKEbdsp7UG9YKChgTeylOvN5wTX%2FPbUkiHMwJ5laEF6HC39MCCbBo3OFWctqOKsj8fCmnwDRJQzTYJU%2FFe1qoU9gYg3ym%2B3xOxQKFdpLQnrcS%2FEFL8gJtkgfq00A5Qxoob1lToiNyS%2FmhfaAnPq6zQ4Udrp6GixAxsXt4YR2RrNBhPdiomm8J8K%2BHBMyp3QIgeg2sq10mhtea8FYXDkw6rC3zgY6pgGQ31XUBVDdBG1LDqFf4OKsKc2sWBedvk7SGYBY83kVUVrJomL4yVGeIMKsDwlnwJlhuo4TxW5pSVyu1SUA2UALbFWlRb7D20EoZ9ZBFq9z8t5cgoSuqN1gLuCboyFUmTN3OIKuMPe964TeyLL2lCsgFQoPyiLcQKuVyGAsh9KBvDAykldzHmZmXZWruu84ESGpLRVx8BbUi%2BDhkfTsD6wjI8iAtsUb&X-Amz-Signature=d4eb8d427a25d6f258e212bf6c06622bb012ca353da679ea548f831af65e40b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> References

